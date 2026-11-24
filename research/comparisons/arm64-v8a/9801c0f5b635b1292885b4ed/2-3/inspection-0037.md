# v16.0.1 → v16.0.2 · 要調査の変更候補 (37)

[一覧の目次](README.md)

<a id="compare-03b54fb26a2ce3ec06b7eff2fefbc207"></a>

### [`00b022b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b022b4.md) → [`00b02350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b02/00b02350.md) FUN_00b02350

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)
- 新版 呼出元 3件 [`006c6e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c6e68.md) [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) [`00b00a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b00/00b00a78.md) · 呼出先 3件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00b027c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b02/00b027c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b022d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b022b4.md#insn-00b022d0) · [`00b022e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b022b4.md#insn-00b022e4) · [`00b022f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b022b4.md#insn-00b022f4)
- 新版 `00b0236c`（命令位置の公開資料なし） · `00b02380`（命令位置の公開資料なし） · `00b02390`（命令位置の公開資料なし）

~~~diff
- 00b022d0 ["INT_ADD", "register:40f0:8", ["const:b022d0:8", "const:4:8"]]
- 00b022d0 ["CALL", null, ["callee:00851550:8"]]
+ 00b0236c ["INT_ADD", "register:40f0:8", ["const:b0236c:8", "const:4:8"]]
+ 00b0236c ["CALL", null, ["callee:00851550:8"]]
- 00b022d0 bytes 8a3cf597
+ 00b0236c bytes 793cf597
- 00b022e4 ["INT_ADD", "register:40f0:8", ["const:b022e4:8", "const:4:8"]]
- 00b022e4 ["CALL", null, ["callee:005e7460:8"]]
+ 00b02380 ["INT_ADD", "register:40f0:8", ["const:b02380:8", "const:4:8"]]
+ 00b02380 ["CALL", null, ["callee:005e7460:8"]]
- 00b022e4 bytes 4f94eb97
+ 00b02380 bytes 3894eb97
- 00b022f4 ["INT_ADD", "register:40f0:8", ["const:b022f4:8", "const:4:8"]]
- 00b022f4 ["CALL", null, ["callee:00851550:8"]]
+ 00b02390 ["INT_ADD", "register:40f0:8", ["const:b02390:8", "const:4:8"]]
+ 00b02390 ["CALL", null, ["callee:00851550:8"]]
- 00b022f4 bytes 813cf597
+ 00b02390 bytes 703cf597
~~~


<a id="compare-5134bdde56358efb594094af481f1199"></a>

### [`00b02408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02408.md) → [`00b024a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b02/00b024a4.md) FUN_00b024a4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)
- 新版 呼出元 3件 [`006c6e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c6e68.md) [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) [`00b00a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b00/00b00a78.md) · 呼出先 3件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00afeb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afe/00afeb84.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b02424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02408.md#insn-00b02424) · [`00b02438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02408.md#insn-00b02438) · [`00b02448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02408.md#insn-00b02448)
- 新版 `00b024c0`（命令位置の公開資料なし） · `00b024d4`（命令位置の公開資料なし） · `00b024e4`（命令位置の公開資料なし）

~~~diff
- 00b02424 ["INT_ADD", "register:40f0:8", ["const:b02424:8", "const:4:8"]]
- 00b02424 ["CALL", null, ["callee:00851550:8"]]
+ 00b024c0 ["INT_ADD", "register:40f0:8", ["const:b024c0:8", "const:4:8"]]
+ 00b024c0 ["CALL", null, ["callee:00851550:8"]]
- 00b02424 bytes 353cf597
+ 00b024c0 bytes 243cf597
- 00b02438 ["INT_ADD", "register:40f0:8", ["const:b02438:8", "const:4:8"]]
- 00b02438 ["CALL", null, ["callee:005e7460:8"]]
+ 00b024d4 ["INT_ADD", "register:40f0:8", ["const:b024d4:8", "const:4:8"]]
+ 00b024d4 ["CALL", null, ["callee:005e7460:8"]]
- 00b02438 bytes fa93eb97
+ 00b024d4 bytes e393eb97
- 00b02448 ["INT_ADD", "register:40f0:8", ["const:b02448:8", "const:4:8"]]
- 00b02448 ["CALL", null, ["callee:00851550:8"]]
+ 00b024e4 ["INT_ADD", "register:40f0:8", ["const:b024e4:8", "const:4:8"]]
+ 00b024e4 ["CALL", null, ["callee:00851550:8"]]
- 00b02448 bytes 2c3cf597
+ 00b024e4 bytes 1b3cf597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0b89a30821a29c26f55db8b05a116f2"></a>

### [`00b02550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02550.md) → [`00b025ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b02/00b025ec.md) FUN_00b025ec

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 3件 [`006c6e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c6e68.md) [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) [`00b00a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b00/00b00a78.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0256c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02550.md#insn-00b0256c) · [`00b02580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02550.md#insn-00b02580) · [`00b02590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02550.md#insn-00b02590)
- 新版 `00b02608`（命令位置の公開資料なし） · `00b0261c`（命令位置の公開資料なし） · `00b0262c`（命令位置の公開資料なし）

~~~diff
- 00b0256c ["INT_ADD", "register:40f0:8", ["const:b0256c:8", "const:4:8"]]
- 00b0256c ["CALL", null, ["callee:00851550:8"]]
+ 00b02608 ["INT_ADD", "register:40f0:8", ["const:b02608:8", "const:4:8"]]
+ 00b02608 ["CALL", null, ["callee:00851550:8"]]
- 00b0256c bytes e33bf597
+ 00b02608 bytes d23bf597
- 00b02580 ["INT_ADD", "register:40f0:8", ["const:b02580:8", "const:4:8"]]
- 00b02580 ["CALL", null, ["callee:005e7460:8"]]
+ 00b0261c ["INT_ADD", "register:40f0:8", ["const:b0261c:8", "const:4:8"]]
+ 00b0261c ["CALL", null, ["callee:005e7460:8"]]
- 00b02580 bytes a893eb97
+ 00b0261c bytes 9193eb97
- 00b02590 ["INT_ADD", "register:40f0:8", ["const:b02590:8", "const:4:8"]]
- 00b02590 ["CALL", null, ["callee:00851550:8"]]
+ 00b0262c ["INT_ADD", "register:40f0:8", ["const:b0262c:8", "const:4:8"]]
+ 00b0262c ["CALL", null, ["callee:00851550:8"]]
- 00b02590 bytes da3bf597
+ 00b0262c bytes c93bf597
~~~


<a id="compare-59cef03b176921f3ce999bf2b0e3e7fc"></a>

### [`00b037b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b037b4.md) → [`00b03850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b03/00b03850.md) FUN_00b03850

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)
- 新版 呼出元 3件 [`006c6e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c6e68.md) [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) [`00b00a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b00/00b00a78.md) · 呼出先 3件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00afeb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afe/00afeb84.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b037d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b037b4.md#insn-00b037d0) · [`00b037e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b037b4.md#insn-00b037e4) · [`00b037f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b037b4.md#insn-00b037f4)
- 新版 `00b0386c`（命令位置の公開資料なし） · `00b03880`（命令位置の公開資料なし） · `00b03890`（命令位置の公開資料なし）

~~~diff
- 00b037d0 ["INT_ADD", "register:40f0:8", ["const:b037d0:8", "const:4:8"]]
- 00b037d0 ["CALL", null, ["callee:00851550:8"]]
+ 00b0386c ["INT_ADD", "register:40f0:8", ["const:b0386c:8", "const:4:8"]]
+ 00b0386c ["CALL", null, ["callee:00851550:8"]]
- 00b037d0 bytes 4a37f597
+ 00b0386c bytes 3937f597
- 00b037e4 ["INT_ADD", "register:40f0:8", ["const:b037e4:8", "const:4:8"]]
- 00b037e4 ["CALL", null, ["callee:005e7460:8"]]
+ 00b03880 ["INT_ADD", "register:40f0:8", ["const:b03880:8", "const:4:8"]]
+ 00b03880 ["CALL", null, ["callee:005e7460:8"]]
- 00b037e4 bytes 0f8feb97
+ 00b03880 bytes f88eeb97
- 00b037f4 ["INT_ADD", "register:40f0:8", ["const:b037f4:8", "const:4:8"]]
- 00b037f4 ["CALL", null, ["callee:00851550:8"]]
+ 00b03890 ["INT_ADD", "register:40f0:8", ["const:b03890:8", "const:4:8"]]
+ 00b03890 ["CALL", null, ["callee:00851550:8"]]
- 00b037f4 bytes 4137f597
+ 00b03890 bytes 3037f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39593f37368448a4ef801129037dd162"></a>

### [`00b03910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03910.md) → [`00b039ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b03/00b039ac.md) FUN_00b039ac

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`006cb1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006cb/006cb1d0.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)
- 新版 呼出元 4件 [`006c6e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c6e68.md) [`006cb228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cb/006cb228.md) [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) [`00b00a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b00/00b00a78.md) · 呼出先 3件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00b027c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b02/00b027c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0392c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03910.md#insn-00b0392c) · [`00b03940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03910.md#insn-00b03940) · [`00b03950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03910.md#insn-00b03950)
- 新版 `00b039c8`（命令位置の公開資料なし） · `00b039dc`（命令位置の公開資料なし） · `00b039ec`（命令位置の公開資料なし）

~~~diff
- 00b0392c ["INT_ADD", "register:40f0:8", ["const:b0392c:8", "const:4:8"]]
- 00b0392c ["CALL", null, ["callee:00851550:8"]]
+ 00b039c8 ["INT_ADD", "register:40f0:8", ["const:b039c8:8", "const:4:8"]]
+ 00b039c8 ["CALL", null, ["callee:00851550:8"]]
- 00b0392c bytes f336f597
+ 00b039c8 bytes e236f597
- 00b03940 ["INT_ADD", "register:40f0:8", ["const:b03940:8", "const:4:8"]]
- 00b03940 ["CALL", null, ["callee:005e7460:8"]]
+ 00b039dc ["INT_ADD", "register:40f0:8", ["const:b039dc:8", "const:4:8"]]
+ 00b039dc ["CALL", null, ["callee:005e7460:8"]]
- 00b03940 bytes b88eeb97
+ 00b039dc bytes a18eeb97
- 00b03950 ["INT_ADD", "register:40f0:8", ["const:b03950:8", "const:4:8"]]
- 00b03950 ["CALL", null, ["callee:00851550:8"]]
+ 00b039ec ["INT_ADD", "register:40f0:8", ["const:b039ec:8", "const:4:8"]]
+ 00b039ec ["CALL", null, ["callee:00851550:8"]]
- 00b03950 bytes ea36f597
+ 00b039ec bytes d936f597
~~~


<a id="compare-77916503083539967e2472f8b4e73a6c"></a>

### [`00b039a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b039a8.md) → [`00b03a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b03/00b03a44.md) FUN_00b03a44

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)
- 新版 呼出元 3件 [`006c6e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c6e68.md) [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) [`00b00a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b00/00b00a78.md) · 呼出先 3件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00b027c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b02/00b027c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b039c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b039a8.md#insn-00b039c4) · [`00b039d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b039a8.md#insn-00b039d8) · [`00b039e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b039a8.md#insn-00b039e8)
- 新版 `00b03a60`（命令位置の公開資料なし） · `00b03a74`（命令位置の公開資料なし） · `00b03a84`（命令位置の公開資料なし）

~~~diff
- 00b039c4 ["INT_ADD", "register:40f0:8", ["const:b039c4:8", "const:4:8"]]
- 00b039c4 ["CALL", null, ["callee:00851550:8"]]
+ 00b03a60 ["INT_ADD", "register:40f0:8", ["const:b03a60:8", "const:4:8"]]
+ 00b03a60 ["CALL", null, ["callee:00851550:8"]]
- 00b039c4 bytes cd36f597
+ 00b03a60 bytes bc36f597
- 00b039d8 ["INT_ADD", "register:40f0:8", ["const:b039d8:8", "const:4:8"]]
- 00b039d8 ["CALL", null, ["callee:005e7460:8"]]
+ 00b03a74 ["INT_ADD", "register:40f0:8", ["const:b03a74:8", "const:4:8"]]
+ 00b03a74 ["CALL", null, ["callee:005e7460:8"]]
- 00b039d8 bytes 928eeb97
+ 00b03a74 bytes 7b8eeb97
- 00b039e8 ["INT_ADD", "register:40f0:8", ["const:b039e8:8", "const:4:8"]]
- 00b039e8 ["CALL", null, ["callee:00851550:8"]]
+ 00b03a84 ["INT_ADD", "register:40f0:8", ["const:b03a84:8", "const:4:8"]]
+ 00b03a84 ["CALL", null, ["callee:00851550:8"]]
- 00b039e8 bytes c436f597
+ 00b03a84 bytes b336f597
~~~


<a id="compare-20a278b9ab1b55396df932e3182b6761"></a>

### [`00b03a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03a40.md) → [`00b03adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b03/00b03adc.md) FUN_00b03adc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)
- 新版 呼出元 3件 [`006c6e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c6e68.md) [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) [`00b00a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b00/00b00a78.md) · 呼出先 3件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00b027c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b02/00b027c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b03a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03a40.md#insn-00b03a5c) · [`00b03a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03a40.md#insn-00b03a70) · [`00b03a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03a40.md#insn-00b03a80)
- 新版 `00b03af8`（命令位置の公開資料なし） · `00b03b0c`（命令位置の公開資料なし） · `00b03b1c`（命令位置の公開資料なし）

~~~diff
- 00b03a5c ["INT_ADD", "register:40f0:8", ["const:b03a5c:8", "const:4:8"]]
- 00b03a5c ["CALL", null, ["callee:00851550:8"]]
+ 00b03af8 ["INT_ADD", "register:40f0:8", ["const:b03af8:8", "const:4:8"]]
+ 00b03af8 ["CALL", null, ["callee:00851550:8"]]
- 00b03a5c bytes a736f597
+ 00b03af8 bytes 9636f597
- 00b03a70 ["INT_ADD", "register:40f0:8", ["const:b03a70:8", "const:4:8"]]
- 00b03a70 ["CALL", null, ["callee:005e7460:8"]]
+ 00b03b0c ["INT_ADD", "register:40f0:8", ["const:b03b0c:8", "const:4:8"]]
+ 00b03b0c ["CALL", null, ["callee:005e7460:8"]]
- 00b03a70 bytes 6c8eeb97
+ 00b03b0c bytes 558eeb97
- 00b03a80 ["INT_ADD", "register:40f0:8", ["const:b03a80:8", "const:4:8"]]
- 00b03a80 ["CALL", null, ["callee:00851550:8"]]
+ 00b03b1c ["INT_ADD", "register:40f0:8", ["const:b03b1c:8", "const:4:8"]]
+ 00b03b1c ["CALL", null, ["callee:00851550:8"]]
- 00b03a80 bytes 9e36f597
+ 00b03b1c bytes 8d36f597
~~~


<a id="compare-51b1f021bc54e57ac47d429d0bd5124c"></a>

### [`00b03c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03c18.md) → [`00b03cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b03/00b03cb4.md) FUN_00b03cb4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)
- 新版 呼出元 3件 [`006c6e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c6e68.md) [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) [`00b00a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b00/00b00a78.md) · 呼出先 3件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00b027c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b02/00b027c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b03c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03c18.md#insn-00b03c34) · [`00b03c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03c18.md#insn-00b03c48) · [`00b03c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03c18.md#insn-00b03c58)
- 新版 `00b03cd0`（命令位置の公開資料なし） · `00b03ce4`（命令位置の公開資料なし） · `00b03cf4`（命令位置の公開資料なし）

~~~diff
- 00b03c34 ["INT_ADD", "register:40f0:8", ["const:b03c34:8", "const:4:8"]]
- 00b03c34 ["CALL", null, ["callee:00851550:8"]]
+ 00b03cd0 ["INT_ADD", "register:40f0:8", ["const:b03cd0:8", "const:4:8"]]
+ 00b03cd0 ["CALL", null, ["callee:00851550:8"]]
- 00b03c34 bytes 3136f597
+ 00b03cd0 bytes 2036f597
- 00b03c48 ["INT_ADD", "register:40f0:8", ["const:b03c48:8", "const:4:8"]]
- 00b03c48 ["CALL", null, ["callee:005e7460:8"]]
+ 00b03ce4 ["INT_ADD", "register:40f0:8", ["const:b03ce4:8", "const:4:8"]]
+ 00b03ce4 ["CALL", null, ["callee:005e7460:8"]]
- 00b03c48 bytes f68deb97
+ 00b03ce4 bytes df8deb97
- 00b03c58 ["INT_ADD", "register:40f0:8", ["const:b03c58:8", "const:4:8"]]
- 00b03c58 ["CALL", null, ["callee:00851550:8"]]
+ 00b03cf4 ["INT_ADD", "register:40f0:8", ["const:b03cf4:8", "const:4:8"]]
+ 00b03cf4 ["CALL", null, ["callee:00851550:8"]]
- 00b03c58 bytes 2836f597
+ 00b03cf4 bytes 1736f597
~~~


<a id="compare-e25d4662461dba758a7b560110874884"></a>

### [`00b03cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03cb0.md) → [`00b03d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b03/00b03d4c.md) FUN_00b03d4c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 3件 [`006c6e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c6e68.md) [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) [`00b00a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b00/00b00a78.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b03ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03cb0.md#insn-00b03ccc) · [`00b03ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03cb0.md#insn-00b03ce0) · [`00b03cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03cb0.md#insn-00b03cf0)
- 新版 `00b03d68`（命令位置の公開資料なし） · `00b03d7c`（命令位置の公開資料なし） · `00b03d8c`（命令位置の公開資料なし）

~~~diff
- 00b03ccc ["INT_ADD", "register:40f0:8", ["const:b03ccc:8", "const:4:8"]]
- 00b03ccc ["CALL", null, ["callee:00851550:8"]]
+ 00b03d68 ["INT_ADD", "register:40f0:8", ["const:b03d68:8", "const:4:8"]]
+ 00b03d68 ["CALL", null, ["callee:00851550:8"]]
- 00b03ccc bytes 0b36f597
+ 00b03d68 bytes fa35f597
- 00b03ce0 ["INT_ADD", "register:40f0:8", ["const:b03ce0:8", "const:4:8"]]
- 00b03ce0 ["CALL", null, ["callee:005e7460:8"]]
+ 00b03d7c ["INT_ADD", "register:40f0:8", ["const:b03d7c:8", "const:4:8"]]
+ 00b03d7c ["CALL", null, ["callee:005e7460:8"]]
- 00b03ce0 bytes d08deb97
+ 00b03d7c bytes b98deb97
- 00b03cf0 ["INT_ADD", "register:40f0:8", ["const:b03cf0:8", "const:4:8"]]
- 00b03cf0 ["CALL", null, ["callee:00851550:8"]]
+ 00b03d8c ["INT_ADD", "register:40f0:8", ["const:b03d8c:8", "const:4:8"]]
+ 00b03d8c ["CALL", null, ["callee:00851550:8"]]
- 00b03cf0 bytes 0236f597
+ 00b03d8c bytes f135f597
~~~


<a id="compare-bf946de9b224f0d9215f078243dfdeab"></a>

### [`00b06334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b06334.md) → [`00b063d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b06/00b063d0.md) FUN_00b063d0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 3件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00afeb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afe/00afeb84.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b06350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b06334.md#insn-00b06350) · [`00b06364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b06334.md#insn-00b06364) · [`00b06374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b06334.md#insn-00b06374)
- 新版 `00b063ec`（命令位置の公開資料なし） · `00b06400`（命令位置の公開資料なし） · `00b06410`（命令位置の公開資料なし）

~~~diff
- 00b06350 ["INT_ADD", "register:40f0:8", ["const:b06350:8", "const:4:8"]]
- 00b06350 ["CALL", null, ["callee:00851550:8"]]
+ 00b063ec ["INT_ADD", "register:40f0:8", ["const:b063ec:8", "const:4:8"]]
+ 00b063ec ["CALL", null, ["callee:00851550:8"]]
- 00b06350 bytes 6a2cf597
+ 00b063ec bytes 592cf597
- 00b06364 ["INT_ADD", "register:40f0:8", ["const:b06364:8", "const:4:8"]]
- 00b06364 ["CALL", null, ["callee:005e7460:8"]]
+ 00b06400 ["INT_ADD", "register:40f0:8", ["const:b06400:8", "const:4:8"]]
+ 00b06400 ["CALL", null, ["callee:005e7460:8"]]
- 00b06364 bytes 2f84eb97
+ 00b06400 bytes 1884eb97
- 00b06374 ["INT_ADD", "register:40f0:8", ["const:b06374:8", "const:4:8"]]
- 00b06374 ["CALL", null, ["callee:00851550:8"]]
+ 00b06410 ["INT_ADD", "register:40f0:8", ["const:b06410:8", "const:4:8"]]
+ 00b06410 ["CALL", null, ["callee:00851550:8"]]
- 00b06374 bytes 612cf597
+ 00b06410 bytes 502cf597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c21e304e7a4d93cd403d5bc85a38b619"></a>

### [`00b063c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b063c0.md) → [`00b0645c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b06/00b0645c.md) FUN_00b0645c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 3件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00afeb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afe/00afeb84.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b063dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b063c0.md#insn-00b063dc) · [`00b063f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b063c0.md#insn-00b063f0) · [`00b06400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b063c0.md#insn-00b06400)
- 新版 `00b06478`（命令位置の公開資料なし） · `00b0648c`（命令位置の公開資料なし） · `00b0649c`（命令位置の公開資料なし）

~~~diff
- 00b063dc ["INT_ADD", "register:40f0:8", ["const:b063dc:8", "const:4:8"]]
- 00b063dc ["CALL", null, ["callee:00851550:8"]]
+ 00b06478 ["INT_ADD", "register:40f0:8", ["const:b06478:8", "const:4:8"]]
+ 00b06478 ["CALL", null, ["callee:00851550:8"]]
- 00b063dc bytes 472cf597
+ 00b06478 bytes 362cf597
- 00b063f0 ["INT_ADD", "register:40f0:8", ["const:b063f0:8", "const:4:8"]]
- 00b063f0 ["CALL", null, ["callee:005e7460:8"]]
+ 00b0648c ["INT_ADD", "register:40f0:8", ["const:b0648c:8", "const:4:8"]]
+ 00b0648c ["CALL", null, ["callee:005e7460:8"]]
- 00b063f0 bytes 0c84eb97
+ 00b0648c bytes f583eb97
- 00b06400 ["INT_ADD", "register:40f0:8", ["const:b06400:8", "const:4:8"]]
- 00b06400 ["CALL", null, ["callee:00851550:8"]]
+ 00b0649c ["INT_ADD", "register:40f0:8", ["const:b0649c:8", "const:4:8"]]
+ 00b0649c ["CALL", null, ["callee:00851550:8"]]
- 00b06400 bytes 3e2cf597
+ 00b0649c bytes 2d2cf597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67f9cffd5a15b6ee15abd4f7e67f3c52"></a>

### [`00b06504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b06504.md) → [`00b065a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b06/00b065a0.md) FUN_00b065a0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b06520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b06504.md#insn-00b06520) · [`00b06534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b06504.md#insn-00b06534) · [`00b06544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b06504.md#insn-00b06544)
- 新版 `00b065bc`（命令位置の公開資料なし） · `00b065d0`（命令位置の公開資料なし） · `00b065e0`（命令位置の公開資料なし）

~~~diff
- 00b06520 ["INT_ADD", "register:40f0:8", ["const:b06520:8", "const:4:8"]]
- 00b06520 ["CALL", null, ["callee:00851550:8"]]
+ 00b065bc ["INT_ADD", "register:40f0:8", ["const:b065bc:8", "const:4:8"]]
+ 00b065bc ["CALL", null, ["callee:00851550:8"]]
- 00b06520 bytes f62bf597
+ 00b065bc bytes e52bf597
- 00b06534 ["INT_ADD", "register:40f0:8", ["const:b06534:8", "const:4:8"]]
- 00b06534 ["CALL", null, ["callee:005e7460:8"]]
+ 00b065d0 ["INT_ADD", "register:40f0:8", ["const:b065d0:8", "const:4:8"]]
+ 00b065d0 ["CALL", null, ["callee:005e7460:8"]]
- 00b06534 bytes bb83eb97
+ 00b065d0 bytes a483eb97
- 00b06544 ["INT_ADD", "register:40f0:8", ["const:b06544:8", "const:4:8"]]
- 00b06544 ["CALL", null, ["callee:00851550:8"]]
+ 00b065e0 ["INT_ADD", "register:40f0:8", ["const:b065e0:8", "const:4:8"]]
+ 00b065e0 ["CALL", null, ["callee:00851550:8"]]
- 00b06544 bytes ed2bf597
+ 00b065e0 bytes dc2bf597
~~~


<a id="compare-a77aab68e5b4ef0298501a2a304380e1"></a>

### [`00b0657c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b0657c.md) → [`00b06618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b06/00b06618.md) FUN_00b06618

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`006c6e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c6e68.md) [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b06598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b0657c.md#insn-00b06598) · [`00b065ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b0657c.md#insn-00b065ac) · [`00b065bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b0657c.md#insn-00b065bc)
- 新版 `00b06634`（命令位置の公開資料なし） · `00b06648`（命令位置の公開資料なし） · `00b06658`（命令位置の公開資料なし）

~~~diff
- 00b06598 ["INT_ADD", "register:40f0:8", ["const:b06598:8", "const:4:8"]]
- 00b06598 ["CALL", null, ["callee:00851550:8"]]
+ 00b06634 ["INT_ADD", "register:40f0:8", ["const:b06634:8", "const:4:8"]]
+ 00b06634 ["CALL", null, ["callee:00851550:8"]]
- 00b06598 bytes d82bf597
+ 00b06634 bytes c72bf597
- 00b065ac ["INT_ADD", "register:40f0:8", ["const:b065ac:8", "const:4:8"]]
- 00b065ac ["CALL", null, ["callee:005e7460:8"]]
+ 00b06648 ["INT_ADD", "register:40f0:8", ["const:b06648:8", "const:4:8"]]
+ 00b06648 ["CALL", null, ["callee:005e7460:8"]]
- 00b065ac bytes 9d83eb97
+ 00b06648 bytes 8683eb97
- 00b065bc ["INT_ADD", "register:40f0:8", ["const:b065bc:8", "const:4:8"]]
- 00b065bc ["CALL", null, ["callee:00851550:8"]]
+ 00b06658 ["INT_ADD", "register:40f0:8", ["const:b06658:8", "const:4:8"]]
+ 00b06658 ["CALL", null, ["callee:00851550:8"]]
- 00b065bc bytes cf2bf597
+ 00b06658 bytes be2bf597
~~~


<a id="compare-54872ec2a048be67681eee2eece7df1a"></a>

### [`00b06888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b06888.md) → [`00b06924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b06/00b06924.md) FUN_00b06924

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b04c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04c7c.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 1件 [`00b04d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b04/00b04d18.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b068f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b06888.md#insn-00b068f0) · [`00b06908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b06888.md#insn-00b06908) · [`00b06934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b06888.md#insn-00b06934)
- 新版 `00b0698c`（命令位置の公開資料なし） · `00b069a4`（命令位置の公開資料なし） · `00b069d0`（命令位置の公開資料なし）

~~~diff
- 00b068f0 ["INT_ADD", "register:40f0:8", ["const:b068f0:8", "const:4:8"]]
- 00b068f0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b0698c ["INT_ADD", "register:40f0:8", ["const:b0698c:8", "const:4:8"]]
+ 00b0698c ["CALL", null, ["callee:00c57f60:8"]]
- 00b068f0 bytes 68450594
+ 00b0698c bytes 75450594
- 00b06908 ["INT_ADD", "register:40f0:8", ["const:b06908:8", "const:4:8"]]
- 00b06908 ["CALL", null, ["callee:00c58160:8"]]
+ 00b069a4 ["INT_ADD", "register:40f0:8", ["const:b069a4:8", "const:4:8"]]
+ 00b069a4 ["CALL", null, ["callee:00c58160:8"]]
- 00b06908 bytes e2450594
+ 00b069a4 bytes ef450594
- 00b06934 ["INT_ADD", "register:40f0:8", ["const:b06934:8", "const:4:8"]]
- 00b06934 ["CALL", null, ["callee:0043bbe4:8"]]
+ 00b069d0 ["INT_ADD", "register:40f0:8", ["const:b069d0:8", "const:4:8"]]
+ 00b069d0 ["CALL", null, ["callee:0043bbe4:8"]]
- 00b06934 bytes 9cd4e497
+ 00b069d0 bytes 85d4e497
~~~


<a id="compare-f509f8867d76c60f5da155ab004d4579"></a>

### [`00b070d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b070d0.md) → [`00b0716c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b07/00b0716c.md) FUN_00b0716c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b04c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04c7c.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00b073ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b073ec.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00b04d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b04/00b04d18.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00b07488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b07/00b07488.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0711c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b070d0.md#insn-00b0711c) · [`00b0714c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b070d0.md#insn-00b0714c) · [`00b07160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b070d0.md#insn-00b07160)
- 新版 `00b071b8`（命令位置の公開資料なし） · `00b071e8`（命令位置の公開資料なし） · `00b071fc`（命令位置の公開資料なし）

~~~diff
- 00b0711c ["INT_ADD", "register:40f0:8", ["const:b0711c:8", "const:4:8"]]
- 00b0711c ["CALL", null, ["callee:0043bbe4:8"]]
+ 00b071b8 ["INT_ADD", "register:40f0:8", ["const:b071b8:8", "const:4:8"]]
+ 00b071b8 ["CALL", null, ["callee:0043bbe4:8"]]
- 00b0711c bytes a2d2e497
+ 00b071b8 bytes 8bd2e497
- 00b0714c ["INT_ADD", "register:40f0:8", ["const:b0714c:8", "const:4:8"]]
- 00b0714c ["CALL", null, ["callee:00b07488:8"]]
+ 00b071e8 ["INT_ADD", "register:40f0:8", ["const:b071e8:8", "const:4:8"]]
+ 00b071e8 ["CALL", null, ["callee:00b07488:8"]]
- 00b0714c bytes a8000094
+ 00b071e8 bytes a8000094
- 00b07160 ["INT_ADD", "register:40f0:8", ["const:b07160:8", "const:4:8"]]
- 00b07160 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b071fc ["INT_ADD", "register:40f0:8", ["const:b071fc:8", "const:4:8"]]
+ 00b071fc ["CALL", null, ["callee:00c57f60:8"]]
- 00b07160 bytes 4c430594
+ 00b071fc bytes 59430594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c824bd08a4d54bc5b574f1dbf8023c9f"></a>

### [`00b07594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b07594.md) → [`00b07630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b07/00b07630.md) FUN_00b07630

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b04c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04c7c.md) [`00b07594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b07594.md) · 呼出先 2件 [`00b07594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b07594.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`00b04d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b04/00b04d18.md) [`00b07630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b07/00b07630.md) · 呼出先 2件 [`00b07630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b07/00b07630.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b075b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b07594.md#insn-00b075b4) · [`00b075c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b07594.md#insn-00b075c0)
- 新版 `00b07650`（命令位置の公開資料なし） · `00b0765c`（命令位置の公開資料なし）

~~~diff
- 00b075b4 ["INT_ADD", "register:40f0:8", ["const:b075b4:8", "const:4:8"]]
- 00b075b4 ["CALL", null, ["local:b0:8"]]
+ 00b07650 ["INT_ADD", "register:40f0:8", ["const:b07650:8", "const:4:8"]]
+ 00b07650 ["CALL", null, ["local:b0:8"]]
- 00b075b4 bytes f8ffff97
+ 00b07650 bytes f8ffff97
- 00b075c0 ["INT_ADD", "register:40f0:8", ["const:b075c0:8", "const:4:8"]]
- 00b075c0 ["CALL", null, ["local:b0:8"]]
+ 00b0765c ["INT_ADD", "register:40f0:8", ["const:b0765c:8", "const:4:8"]]
+ 00b0765c ["CALL", null, ["local:b0:8"]]
- 00b075c0 bytes f5ffff97
+ 00b0765c bytes f5ffff97
~~~


<a id="compare-7f7d1c845980e2ff77aebd3c19105c2f"></a>

### [`00b07968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b07968.md) → [`00b07a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b07/00b07a04.md) FUN_00b07a04

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) · 呼出先 2件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b07980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b07968.md#insn-00b07980) · [`00b0798c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b07968.md#insn-00b0798c) · [`00b07998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b07968.md#insn-00b07998)
- 新版 `00b07a1c`（命令位置の公開資料なし） · `00b07a28`（命令位置の公開資料なし） · `00b07a34`（命令位置の公開資料なし）

~~~diff
- 00b07980 ["INT_ADD", "register:40f0:8", ["const:b07980:8", "const:4:8"]]
- 00b07980 ["CALL", null, ["callee:005c17dc:8"]]
+ 00b07a1c ["INT_ADD", "register:40f0:8", ["const:b07a1c:8", "const:4:8"]]
+ 00b07a1c ["CALL", null, ["callee:005c17dc:8"]]
- 00b07980 bytes 87e7ea97
+ 00b07a1c bytes 70e7ea97
- 00b0798c ["INT_ADD", "register:40f0:8", ["const:b0798c:8", "const:4:8"]]
- 00b0798c ["CALL", null, ["callee:00851550:8"]]
+ 00b07a28 ["INT_ADD", "register:40f0:8", ["const:b07a28:8", "const:4:8"]]
+ 00b07a28 ["CALL", null, ["callee:00851550:8"]]
- 00b0798c bytes db26f597
+ 00b07a28 bytes ca26f597
- 00b07998 ["INT_ADD", "register:40f0:8", ["const:b07998:8", "const:4:8"]]
- 00b07998 ["CALL", null, ["callee:00851550:8"]]
+ 00b07a34 ["INT_ADD", "register:40f0:8", ["const:b07a34:8", "const:4:8"]]
+ 00b07a34 ["CALL", null, ["callee:00851550:8"]]
- 00b07998 bytes d826f597
+ 00b07a34 bytes c726f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-294a92b1c9e9549fa11837e63e497420"></a>

### [`00b08d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b08/00b08d1c.md) → [`00b08db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b08/00b08db8.md) FUN_00b08db8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b08d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b08/00b08d1c.md#insn-00b08d40) · [`00b08d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b08/00b08d1c.md#insn-00b08d50)
- 新版 `00b08ddc`（命令位置の公開資料なし） · `00b08dec`（命令位置の公開資料なし）

~~~diff
- 00b08d40 ["INT_ADD", "register:40f0:8", ["const:b08d40:8", "const:4:8"]]
- 00b08d40 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b08ddc ["INT_ADD", "register:40f0:8", ["const:b08ddc:8", "const:4:8"]]
+ 00b08ddc ["CALL", null, ["callee:00c57f80:8"]]
- 00b08d40 bytes 5c3c0594
+ 00b08ddc bytes 693c0594
- 00b08d50 ["INT_ADD", "register:40f0:8", ["const:b08d50:8", "const:4:8"]]
- 00b08d50 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b08dec ["INT_ADD", "register:40f0:8", ["const:b08dec:8", "const:4:8"]]
+ 00b08dec ["CALL", null, ["callee:00c57f80:8"]]
- 00b08d50 bytes 583c0594
+ 00b08dec bytes 653c0594
~~~


<a id="compare-18cf829ce6327c081e95b1f524d9b1d6"></a>

### [`00b08d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b08/00b08d70.md) → [`00b08e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b08/00b08e0c.md) FUN_00b08e0c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) [`00b3d618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3d/00b3d618.md) · 呼出先 7件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0911c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b0911c.md)
- 新版 呼出元 2件 [`00a06df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06df0.md) [`00b3d6b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3d/00b3d6b4.md) · 呼出先 7件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0049f430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f430.md) [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00b091b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b09/00b091b8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b08d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b08/00b08d70.md#insn-00b08d9c) · [`00b08dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b08/00b08d70.md#insn-00b08dac) · [`00b08db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b08/00b08d70.md#insn-00b08db8)
- 新版 `00b08e38`（命令位置の公開資料なし） · `00b08e48`（命令位置の公開資料なし） · `00b08e54`（命令位置の公開資料なし）

~~~diff
- 00b08d9c ["INT_ADD", "register:40f0:8", ["const:b08d9c:8", "const:4:8"]]
- 00b08d9c ["CALL", null, ["callee:005c17dc:8"]]
+ 00b08e38 ["INT_ADD", "register:40f0:8", ["const:b08e38:8", "const:4:8"]]
+ 00b08e38 ["CALL", null, ["callee:005c17dc:8"]]
- 00b08d9c bytes 80e2ea97
+ 00b08e38 bytes 69e2ea97
- 00b08dac ["INT_ADD", "register:40f0:8", ["const:b08dac:8", "const:4:8"]]
- 00b08dac ["CALL", null, ["callee:00851550:8"]]
+ 00b08e48 ["INT_ADD", "register:40f0:8", ["const:b08e48:8", "const:4:8"]]
+ 00b08e48 ["CALL", null, ["callee:00851550:8"]]
- 00b08dac bytes d321f597
+ 00b08e48 bytes c221f597
- 00b08db8 ["INT_ADD", "register:40f0:8", ["const:b08db8:8", "const:4:8"]]
- 00b08db8 ["CALL", null, ["callee:00851550:8"]]
+ 00b08e54 ["INT_ADD", "register:40f0:8", ["const:b08e54:8", "const:4:8"]]
+ 00b08e54 ["CALL", null, ["callee:00851550:8"]]
- 00b08db8 bytes d021f597
+ 00b08e54 bytes bf21f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1259c85b19c039a8688dcf27f49954a"></a>

### [`00b0911c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b0911c.md) → [`00b091b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b09/00b091b8.md) FUN_00b091b8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b08d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b08/00b08d70.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00b08e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b08/00b08e0c.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b09144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b0911c.md#insn-00b09144) · [`00b0915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b0911c.md#insn-00b0915c) · [`00b09174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b0911c.md#insn-00b09174)
- 新版 `00b091e0`（命令位置の公開資料なし） · `00b091f8`（命令位置の公開資料なし） · `00b09210`（命令位置の公開資料なし）

~~~diff
- 00b09144 ["INT_ADD", "register:40f0:8", ["const:b09144:8", "const:4:8"]]
- 00b09144 ["CALL", null, ["callee:00851550:8"]]
+ 00b091e0 ["INT_ADD", "register:40f0:8", ["const:b091e0:8", "const:4:8"]]
+ 00b091e0 ["CALL", null, ["callee:00851550:8"]]
- 00b09144 bytes ed20f597
+ 00b091e0 bytes dc20f597
- 00b0915c ["INT_ADD", "register:40f0:8", ["const:b0915c:8", "const:4:8"]]
- 00b0915c ["CALL", null, ["callee:00851550:8"]]
+ 00b091f8 ["INT_ADD", "register:40f0:8", ["const:b091f8:8", "const:4:8"]]
+ 00b091f8 ["CALL", null, ["callee:00851550:8"]]
- 00b0915c bytes e720f597
+ 00b091f8 bytes d620f597
- 00b09174 ["INT_ADD", "register:40f0:8", ["const:b09174:8", "const:4:8"]]
- 00b09174 ["CALL", null, ["callee:00851550:8"]]
+ 00b09210 ["INT_ADD", "register:40f0:8", ["const:b09210:8", "const:4:8"]]
+ 00b09210 ["CALL", null, ["callee:00851550:8"]]
- 00b09174 bytes e120f597
+ 00b09210 bytes d020f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5ecef88e4b57b0f6ce0a480ff32681b"></a>

### [`00b09604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09604.md) → [`00b096a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b09/00b096a0.md) FUN_00b096a0

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) · 呼出先 2件 [`0086a7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a7a4.md) [`0086a838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a838.md)
- 新版 呼出元 1件 [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) · 呼出先 2件 [`0086a7fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a7fc.md) [`0086a890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a890.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b09620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09604.md#insn-00b09620) · [`00b0963c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09604.md#insn-00b0963c)
- 新版 `00b096bc`（命令位置の公開資料なし） · `00b096d8`（命令位置の公開資料なし）

~~~diff
- 00b09620 ["INT_ADD", "register:40f0:8", ["const:b09620:8", "const:4:8"]]
- 00b09620 ["CALL", null, ["callee:0086a890:8"]]
+ 00b096bc ["INT_ADD", "register:40f0:8", ["const:b096bc:8", "const:4:8"]]
+ 00b096bc ["CALL", null, ["callee:0086a890:8"]]
- 00b09620 bytes 8684f597
+ 00b096bc bytes 7584f597
- 00b0963c ["INT_ADD", "register:40f0:8", ["const:b0963c:8", "const:4:8"]]
- 00b0963c ["CALL", null, ["callee:0086a7fc:8"]]
+ 00b096d8 ["INT_ADD", "register:40f0:8", ["const:b096d8:8", "const:4:8"]]
+ 00b096d8 ["CALL", null, ["callee:0086a7fc:8"]]
- 00b0963c bytes 5a84f597
+ 00b096d8 bytes 4984f597
~~~


<a id="compare-5f3fb251106bd1734b11a2c38ec219d8"></a>

### [`00b09708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09708.md) → [`00b097a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b09/00b097a4.md) FUN_00b097a4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 14件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00480118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480118.md) [`00480178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md) [`004801d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004801d8.md)
- 新版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 14件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00480158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480158.md) [`004801b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/004801b8.md) [`00480218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480218.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0973c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09708.md#insn-00b0973c) · [`00b09758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09708.md#insn-00b09758) · [`00b09774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09708.md#insn-00b09774)
- 新版 `00b097d8`（命令位置の公開資料なし） · `00b097f4`（命令位置の公開資料なし） · `00b09810`（命令位置の公開資料なし）

~~~diff
- 00b0973c ["INT_ADD", "register:40f0:8", ["const:b0973c:8", "const:4:8"]]
- 00b0973c ["CALL", null, ["callee:0086a890:8"]]
+ 00b097d8 ["INT_ADD", "register:40f0:8", ["const:b097d8:8", "const:4:8"]]
+ 00b097d8 ["CALL", null, ["callee:0086a890:8"]]
- 00b0973c bytes 3f84f597
+ 00b097d8 bytes 2e84f597
- 00b09758 ["INT_ADD", "register:40f0:8", ["const:b09758:8", "const:4:8"]]
- 00b09758 ["CALL", null, ["callee:0086a7fc:8"]]
+ 00b097f4 ["INT_ADD", "register:40f0:8", ["const:b097f4:8", "const:4:8"]]
+ 00b097f4 ["CALL", null, ["callee:0086a7fc:8"]]
- 00b09758 bytes 1384f597
+ 00b097f4 bytes 0284f597
- 00b09774 ["INT_ADD", "register:40f0:8", ["const:b09774:8", "const:4:8"]]
- 00b09774 ["CALL", null, ["callee:004801b8:8"]]
+ 00b09810 ["INT_ADD", "register:40f0:8", ["const:b09810:8", "const:4:8"]]
+ 00b09810 ["CALL", null, ["callee:004801b8:8"]]
- 00b09774 bytes 81dae597
+ 00b09810 bytes 6adae597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e3737000a5891f9bd6bb1c80128ea84"></a>

### [`00b09eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09eac.md) → [`00b09f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b09/00b09f48.md) FUN_00b09f48

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 3件 [`00480b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md) [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md) [`00480be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md)
- 新版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 3件 [`00480b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480b78.md) [`00480bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480bd0.md) [`00480c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480c28.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b09ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09eac.md#insn-00b09ed8) · [`00b09ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09eac.md#insn-00b09ef4) · [`00b09f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09eac.md#insn-00b09f28)
- 新版 `00b09f74`（命令位置の公開資料なし） · `00b09f90`（命令位置の公開資料なし） · `00b09fc4`（命令位置の公開資料なし）

~~~diff
- 00b09ed8 ["INT_ADD", "register:40f0:8", ["const:b09ed8:8", "const:4:8"]]
- 00b09ed8 ["CALL", null, ["callee:00480bd0:8"]]
+ 00b09f74 ["INT_ADD", "register:40f0:8", ["const:b09f74:8", "const:4:8"]]
+ 00b09f74 ["CALL", null, ["callee:00480bd0:8"]]
- 00b09ed8 bytes 2edbe597
+ 00b09f74 bytes 17dbe597
- 00b09ef4 ["INT_ADD", "register:40f0:8", ["const:b09ef4:8", "const:4:8"]]
- 00b09ef4 ["CALL", null, ["callee:00480bd0:8"]]
+ 00b09f90 ["INT_ADD", "register:40f0:8", ["const:b09f90:8", "const:4:8"]]
+ 00b09f90 ["CALL", null, ["callee:00480bd0:8"]]
- 00b09ef4 bytes 27dbe597
+ 00b09f90 bytes 10dbe597
- 00b09f28 ["INT_ADD", "register:40f0:8", ["const:b09f28:8", "const:4:8"]]
- 00b09f28 ["CALL", null, ["callee:00480c28:8"]]
+ 00b09fc4 ["INT_ADD", "register:40f0:8", ["const:b09fc4:8", "const:4:8"]]
+ 00b09fc4 ["CALL", null, ["callee:00480c28:8"]]
- 00b09f28 bytes 30dbe597
+ 00b09fc4 bytes 19dbe597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d8a8100cec3ed44185d80434b8072cd"></a>

### [`00b0a5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0a5b8.md) → [`00b0a654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0a/00b0a654.md) FUN_00b0a654

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00b0a088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0a088.md) [`00b0ad58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0ad58.md) [`00b0c254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0c254.md) · 呼出先 9件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md)
- 新版 呼出元 3件 [`00b0a124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0a/00b0a124.md) [`00b0adf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0a/00b0adf4.md) [`00b0c2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0c2f0.md) · 呼出先 9件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md) [`00802d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802d00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0a5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0a5b8.md#insn-00b0a5e8) · [`00b0a5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0a5b8.md#insn-00b0a5f0) · [`00b0a5f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0a5b8.md#insn-00b0a5f8)
- 新版 `00b0a684`（命令位置の公開資料なし） · `00b0a68c`（命令位置の公開資料なし） · `00b0a694`（命令位置の公開資料なし）

~~~diff
- 00b0a5e8 ["INT_ADD", "register:40f0:8", ["const:b0a5e8:8", "const:4:8"]]
- 00b0a5e8 ["CALL", null, ["callee:00802bb0:8"]]
+ 00b0a684 ["INT_ADD", "register:40f0:8", ["const:b0a684:8", "const:4:8"]]
+ 00b0a684 ["CALL", null, ["callee:00802bb0:8"]]
- 00b0a5e8 bytes 5ce1f397
+ 00b0a684 bytes 4be1f397
- 00b0a5f0 ["INT_ADD", "register:40f0:8", ["const:b0a5f0:8", "const:4:8"]]
- 00b0a5f0 ["CALL", null, ["callee:00802d00:8"]]
+ 00b0a68c ["INT_ADD", "register:40f0:8", ["const:b0a68c:8", "const:4:8"]]
+ 00b0a68c ["CALL", null, ["callee:00802d00:8"]]
- 00b0a5f0 bytes aee1f397
+ 00b0a68c bytes 9de1f397
- 00b0a5f8 ["INT_ADD", "register:40f0:8", ["const:b0a5f8:8", "const:4:8"]]
- 00b0a5f8 ["CALL", null, ["callee:00802f38:8"]]
+ 00b0a694 ["INT_ADD", "register:40f0:8", ["const:b0a694:8", "const:4:8"]]
+ 00b0a694 ["CALL", null, ["callee:00802f38:8"]]
- 00b0a5f8 bytes 3ae2f397
+ 00b0a694 bytes 29e2f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1070ed8d8db3addc349ff96d28245132"></a>

### [`00b0a7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0a7f4.md) → [`00b0a890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0a/00b0a890.md) FUN_00b0a890

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00ae0b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae0/00ae0b68.md) [`00aed778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aed/00aed778.md) · 呼出先 13件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`006623ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/006623ec.md) [`00662490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/00662490.md) [`00662534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/00662534.md)
- 新版 呼出元 2件 [`00ae0c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae0/00ae0c04.md) [`00aed814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aed814.md) · 呼出先 13件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0066242c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00662/0066242c.md) [`006624d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00662/006624d0.md) [`00662574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00662/00662574.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0a824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0a7f4.md#insn-00b0a824) · [`00b0a82c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0a7f4.md#insn-00b0a82c) · [`00b0a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0a7f4.md#insn-00b0a830)
- 新版 `00b0a8c0`（命令位置の公開資料なし） · `00b0a8c8`（命令位置の公開資料なし） · `00b0a8cc`（命令位置の公開資料なし）

~~~diff
- 00b0a824 ["INT_ADD", "register:40f0:8", ["const:b0a824:8", "const:4:8"]]
- 00b0a824 ["CALL", null, ["callee:00802bb0:8"]]
+ 00b0a8c0 ["INT_ADD", "register:40f0:8", ["const:b0a8c0:8", "const:4:8"]]
+ 00b0a8c0 ["CALL", null, ["callee:00802bb0:8"]]
- 00b0a824 bytes cde0f397
+ 00b0a8c0 bytes bce0f397
- 00b0a82c ["INT_ADD", "register:40f0:8", ["const:b0a82c:8", "const:4:8"]]
- 00b0a82c ["CALL", null, ["callee:00802d00:8"]]
+ 00b0a8c8 ["INT_ADD", "register:40f0:8", ["const:b0a8c8:8", "const:4:8"]]
+ 00b0a8c8 ["CALL", null, ["callee:00802d00:8"]]
- 00b0a82c bytes 1fe1f397
+ 00b0a8c8 bytes 0ee1f397
- 00b0a830 ["INT_ADD", "register:40f0:8", ["const:b0a830:8", "const:4:8"]]
- 00b0a830 ["CALL", null, ["callee:00802f38:8"]]
+ 00b0a8cc ["INT_ADD", "register:40f0:8", ["const:b0a8cc:8", "const:4:8"]]
+ 00b0a8cc ["CALL", null, ["callee:00802f38:8"]]
- 00b0a830 bytes ace1f397
+ 00b0a8cc bytes 9be1f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cf35635d48359626ff136af01ae012f"></a>

### [`00b0ad14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0ad14.md) → [`00b0adb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0a/00b0adb0.md) FUN_00b0adb0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`00ad0958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad0/00ad0958.md) [`00ad6a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6a88.md) [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) [`00adf090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00adf/00adf090.md) · 呼出先 1件 [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)
- 新版 呼出元 8件 [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md) [`00ad09c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad0/00ad09c8.md) [`00ad6af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6af8.md) [`00ad6fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6fbc.md) [`00adf100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00adf/00adf100.md) · 呼出先 1件 [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0ad34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0ad14.md#insn-00b0ad34)
- 新版 `00b0add0`（命令位置の公開資料なし）

~~~diff
- 00b0ad34 ["INT_ADD", "register:40f0:8", ["const:b0ad34:8", "const:4:8"]]
- 00b0ad34 ["CALL", null, ["callee:00c58520:8"]]
+ 00b0add0 ["INT_ADD", "register:40f0:8", ["const:b0add0:8", "const:4:8"]]
+ 00b0add0 ["CALL", null, ["callee:00c58520:8"]]
- 00b0ad34 bytes c7350594
+ 00b0add0 bytes d4350594
~~~


<a id="compare-ab04362e52a6b3fd9410722af39ea19a"></a>

### [`00b0ad58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0ad58.md) → [`00b0adf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0a/00b0adf4.md) FUN_00b0adf4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00ad0958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad0/00ad0958.md) · 呼出先 6件 [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) [`00802ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ee0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0a5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0a5b8.md)
- 新版 呼出元 2件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`00ad09c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad0/00ad09c8.md) · 呼出先 6件 [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md) [`00802d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802d00.md) [`00802f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802f38.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00b0a654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0a/00b0a654.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0ad78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0ad58.md#insn-00b0ad78) · [`00b0ad80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0ad58.md#insn-00b0ad80) · [`00b0ad88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0ad58.md#insn-00b0ad88)
- 新版 `00b0ae14`（命令位置の公開資料なし） · `00b0ae1c`（命令位置の公開資料なし） · `00b0ae24`（命令位置の公開資料なし）

~~~diff
- 00b0ad78 ["INT_ADD", "register:40f0:8", ["const:b0ad78:8", "const:4:8"]]
- 00b0ad78 ["CALL", null, ["callee:00802bb0:8"]]
+ 00b0ae14 ["INT_ADD", "register:40f0:8", ["const:b0ae14:8", "const:4:8"]]
+ 00b0ae14 ["CALL", null, ["callee:00802bb0:8"]]
- 00b0ad78 bytes 78dff397
+ 00b0ae14 bytes 67dff397
- 00b0ad80 ["INT_ADD", "register:40f0:8", ["const:b0ad80:8", "const:4:8"]]
- 00b0ad80 ["CALL", null, ["callee:00802d00:8"]]
+ 00b0ae1c ["INT_ADD", "register:40f0:8", ["const:b0ae1c:8", "const:4:8"]]
+ 00b0ae1c ["CALL", null, ["callee:00802d00:8"]]
- 00b0ad80 bytes cadff397
+ 00b0ae1c bytes b9dff397
- 00b0ad88 ["INT_ADD", "register:40f0:8", ["const:b0ad88:8", "const:4:8"]]
- 00b0ad88 ["CALL", null, ["callee:00802f38:8"]]
+ 00b0ae24 ["INT_ADD", "register:40f0:8", ["const:b0ae24:8", "const:4:8"]]
+ 00b0ae24 ["CALL", null, ["callee:00802f38:8"]]
- 00b0ad88 bytes 56e0f397
+ 00b0ae24 bytes 45e0f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9c50b650a33e09ceb369b3893ea8c51"></a>

### [`00b0aea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0aea0.md) → [`00b0af3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0a/00b0af3c.md) FUN_00b0af3c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) · 呼出先 12件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) [`00802ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ee0.md)
- 新版 呼出元 1件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) · 呼出先 12件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md) [`00802d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802d00.md) [`00802f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802f38.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0aee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0aea0.md#insn-00b0aee8) · [`00b0aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0aea0.md#insn-00b0aef0) · [`00b0aef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0aea0.md#insn-00b0aef8)
- 新版 `00b0af84`（命令位置の公開資料なし） · `00b0af8c`（命令位置の公開資料なし） · `00b0af94`（命令位置の公開資料なし）

~~~diff
- 00b0aee8 ["INT_ADD", "register:40f0:8", ["const:b0aee8:8", "const:4:8"]]
- 00b0aee8 ["CALL", null, ["callee:00802bb0:8"]]
+ 00b0af84 ["INT_ADD", "register:40f0:8", ["const:b0af84:8", "const:4:8"]]
+ 00b0af84 ["CALL", null, ["callee:00802bb0:8"]]
- 00b0aee8 bytes 1cdff397
+ 00b0af84 bytes 0bdff397
- 00b0aef0 ["INT_ADD", "register:40f0:8", ["const:b0aef0:8", "const:4:8"]]
- 00b0aef0 ["CALL", null, ["callee:00802d00:8"]]
+ 00b0af8c ["INT_ADD", "register:40f0:8", ["const:b0af8c:8", "const:4:8"]]
+ 00b0af8c ["CALL", null, ["callee:00802d00:8"]]
- 00b0aef0 bytes 6edff397
+ 00b0af8c bytes 5ddff397
- 00b0aef8 ["INT_ADD", "register:40f0:8", ["const:b0aef8:8", "const:4:8"]]
- 00b0aef8 ["CALL", null, ["callee:00802f38:8"]]
+ 00b0af94 ["INT_ADD", "register:40f0:8", ["const:b0af94:8", "const:4:8"]]
+ 00b0af94 ["CALL", null, ["callee:00802f38:8"]]
- 00b0aef8 bytes fadff397
+ 00b0af94 bytes e9dff397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a4125e2845c7ba8a4f84d3f043b722c"></a>

### [`00b0b384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b384.md) → [`00b0b420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0b/00b0b420.md) FUN_00b0b420

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`00ad0958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad0/00ad0958.md) [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) [`00802ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ee0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 8件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) [`00ad09c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad0/00ad09c8.md) [`00ad6fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6fbc.md) · 呼出先 5件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md) [`00802d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802d00.md) [`00802f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802f38.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0b3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b384.md#insn-00b0b3bc) · [`00b0b3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b384.md#insn-00b0b3c4) · [`00b0b3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b384.md#insn-00b0b3cc)
- 新版 `00b0b458`（命令位置の公開資料なし） · `00b0b460`（命令位置の公開資料なし） · `00b0b468`（命令位置の公開資料なし）

~~~diff
- 00b0b3bc ["INT_ADD", "register:40f0:8", ["const:b0b3bc:8", "const:4:8"]]
- 00b0b3bc ["CALL", null, ["callee:00802bb0:8"]]
+ 00b0b458 ["INT_ADD", "register:40f0:8", ["const:b0b458:8", "const:4:8"]]
+ 00b0b458 ["CALL", null, ["callee:00802bb0:8"]]
- 00b0b3bc bytes e7ddf397
+ 00b0b458 bytes d6ddf397
- 00b0b3c4 ["INT_ADD", "register:40f0:8", ["const:b0b3c4:8", "const:4:8"]]
- 00b0b3c4 ["CALL", null, ["callee:00802d00:8"]]
+ 00b0b460 ["INT_ADD", "register:40f0:8", ["const:b0b460:8", "const:4:8"]]
+ 00b0b460 ["CALL", null, ["callee:00802d00:8"]]
- 00b0b3c4 bytes 39def397
+ 00b0b460 bytes 28def397
- 00b0b3cc ["INT_ADD", "register:40f0:8", ["const:b0b3cc:8", "const:4:8"]]
- 00b0b3cc ["CALL", null, ["callee:00802f38:8"]]
+ 00b0b468 ["INT_ADD", "register:40f0:8", ["const:b0b468:8", "const:4:8"]]
+ 00b0b468 ["CALL", null, ["callee:00802f38:8"]]
- 00b0b3cc bytes c5def397
+ 00b0b468 bytes b4def397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07d0eb2a00217eeced1d6df4261b04ca"></a>

### [`00b0b4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b4dc.md) → [`00b0b578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0b/00b0b578.md) FUN_00b0b578

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b0b640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b640.md) [`00b0bd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0bd00.md) · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) [`00802ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ee0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`00b0b6dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0b/00b0b6dc.md) [`00b0bd9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0b/00b0bd9c.md) · 呼出先 5件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md) [`00802d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802d00.md) [`00802f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802f38.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0b518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b4dc.md#insn-00b0b518) · [`00b0b520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b4dc.md#insn-00b0b520) · [`00b0b528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b4dc.md#insn-00b0b528)
- 新版 `00b0b5b4`（命令位置の公開資料なし） · `00b0b5bc`（命令位置の公開資料なし） · `00b0b5c4`（命令位置の公開資料なし）

~~~diff
- 00b0b518 ["INT_ADD", "register:40f0:8", ["const:b0b518:8", "const:4:8"]]
- 00b0b518 ["CALL", null, ["callee:00802bb0:8"]]
+ 00b0b5b4 ["INT_ADD", "register:40f0:8", ["const:b0b5b4:8", "const:4:8"]]
+ 00b0b5b4 ["CALL", null, ["callee:00802bb0:8"]]
- 00b0b518 bytes 90ddf397
+ 00b0b5b4 bytes 7fddf397
- 00b0b520 ["INT_ADD", "register:40f0:8", ["const:b0b520:8", "const:4:8"]]
- 00b0b520 ["CALL", null, ["callee:00802d00:8"]]
+ 00b0b5bc ["INT_ADD", "register:40f0:8", ["const:b0b5bc:8", "const:4:8"]]
+ 00b0b5bc ["CALL", null, ["callee:00802d00:8"]]
- 00b0b520 bytes e2ddf397
+ 00b0b5bc bytes d1ddf397
- 00b0b528 ["INT_ADD", "register:40f0:8", ["const:b0b528:8", "const:4:8"]]
- 00b0b528 ["CALL", null, ["callee:00802f38:8"]]
+ 00b0b5c4 ["INT_ADD", "register:40f0:8", ["const:b0b5c4:8", "const:4:8"]]
+ 00b0b5c4 ["CALL", null, ["callee:00802f38:8"]]
- 00b0b528 bytes 6edef397
+ 00b0b5c4 bytes 5ddef397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce9c854e47bdb674a88b6c792aeb27fc"></a>

### [`00b0c81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0c81c.md) → [`00b0c8b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0c8b8.md) FUN_00b0c8b8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b09708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09708.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b0ca28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0ca28.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 1件 [`00b097a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b09/00b097a4.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00b0cac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0cac4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0c8c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0c81c.md#insn-00b0c8c8) · [`00b0c90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0c81c.md#insn-00b0c90c) · [`00b0c950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0c81c.md#insn-00b0c950)
- 新版 `00b0c964`（命令位置の公開資料なし） · `00b0c9a8`（命令位置の公開資料なし） · `00b0c9ec`（命令位置の公開資料なし）

~~~diff
- 00b0c8c8 ["INT_ADD", "register:40f0:8", ["const:b0c8c8:8", "const:4:8"]]
- 00b0c8c8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b0c964 ["INT_ADD", "register:40f0:8", ["const:b0c964:8", "const:4:8"]]
+ 00b0c964 ["CALL", null, ["callee:00c57f60:8"]]
- 00b0c8c8 bytes 722d0594
+ 00b0c964 bytes 7f2d0594
- 00b0c90c ["INT_ADD", "register:40f0:8", ["const:b0c90c:8", "const:4:8"]]
- 00b0c90c ["CALL", null, ["callee:00c58160:8"]]
+ 00b0c9a8 ["INT_ADD", "register:40f0:8", ["const:b0c9a8:8", "const:4:8"]]
+ 00b0c9a8 ["CALL", null, ["callee:00c58160:8"]]
- 00b0c90c bytes e12d0594
+ 00b0c9a8 bytes ee2d0594
- 00b0c950 ["INT_ADD", "register:40f0:8", ["const:b0c950:8", "const:4:8"]]
- 00b0c950 ["CALL", null, ["callee:00c58160:8"]]
+ 00b0c9ec ["INT_ADD", "register:40f0:8", ["const:b0c9ec:8", "const:4:8"]]
+ 00b0c9ec ["CALL", null, ["callee:00c58160:8"]]
- 00b0c950 bytes d02d0594
+ 00b0c9ec bytes dd2d0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f4bc19a21260a66c6800b50304b5823"></a>

### [`00b0ca50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0ca50.md) → [`00b0caec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0caec.md) FUN_00b0caec

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b0aea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0aea0.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b0ca28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0ca28.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00b0af3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0a/00b0af3c.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00b0cac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0cac4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0cadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0ca50.md#insn-00b0cadc) · [`00b0cb94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0ca50.md#insn-00b0cb94) · [`00b0cbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0ca50.md#insn-00b0cbb0)
- 新版 `00b0cb78`（命令位置の公開資料なし） · `00b0cc30`（命令位置の公開資料なし） · `00b0cc4c`（命令位置の公開資料なし）

~~~diff
- 00b0cadc ["INT_ADD", "register:40f0:8", ["const:b0cadc:8", "const:4:8"]]
- 00b0cadc ["CALL", null, ["callee:00c57f60:8"]]
+ 00b0cb78 ["INT_ADD", "register:40f0:8", ["const:b0cb78:8", "const:4:8"]]
+ 00b0cb78 ["CALL", null, ["callee:00c57f60:8"]]
- 00b0cadc bytes ed2c0594
+ 00b0cb78 bytes fa2c0594
- 00b0cb94 ["INT_ADD", "register:40f0:8", ["const:b0cb94:8", "const:4:8"]]
- 00b0cb94 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b0cc30 ["INT_ADD", "register:40f0:8", ["const:b0cc30:8", "const:4:8"]]
+ 00b0cc30 ["CALL", null, ["callee:00c57f80:8"]]
- 00b0cb94 bytes c72c0594
+ 00b0cc30 bytes d42c0594
- 00b0cbb0 ["INT_ADD", "register:40f0:8", ["const:b0cbb0:8", "const:4:8"]]
- 00b0cbb0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b0cc4c ["INT_ADD", "register:40f0:8", ["const:b0cc4c:8", "const:4:8"]]
+ 00b0cc4c ["CALL", null, ["callee:00c57f80:8"]]
- 00b0cbb0 bytes c02c0594
+ 00b0cc4c bytes cd2c0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6c65c3a899ad01c9fc5a1f2323c5e16"></a>

### [`00b0d2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d2f4.md) → [`00b0d390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d390.md) FUN_00b0d390

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6a5c.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6ab4.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d2f4.md#insn-00b0d300) · [`00b0d310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d2f4.md#insn-00b0d310) · [`00b0d318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d2f4.md#insn-00b0d318)
- 新版 `00b0d39c`（命令位置の公開資料なし） · `00b0d3ac`（命令位置の公開資料なし） · `00b0d3b4`（命令位置の公開資料なし）

~~~diff
- 00b0d300 ["INT_ADD", "register:40f0:8", ["const:b0d300:8", "const:4:8"]]
- 00b0d300 ["CALL", null, ["callee:00851550:8"]]
+ 00b0d39c ["INT_ADD", "register:40f0:8", ["const:b0d39c:8", "const:4:8"]]
+ 00b0d39c ["CALL", null, ["callee:00851550:8"]]
- 00b0d300 bytes 7e10f597
+ 00b0d39c bytes 6d10f597
- 00b0d310 ["INT_ADD", "register:40f0:8", ["const:b0d310:8", "const:4:8"]]
- 00b0d310 ["CALL", null, ["callee:008b7a20:8"]]
+ 00b0d3ac ["INT_ADD", "register:40f0:8", ["const:b0d3ac:8", "const:4:8"]]
+ 00b0d3ac ["CALL", null, ["callee:008b7a20:8"]]
- 00b0d310 bytes aea9f697
+ 00b0d3ac bytes 9da9f697
- 00b0d318 ["INT_ADD", "register:40f0:8", ["const:b0d318:8", "const:4:8"]]
- 00b0d318 ["CALL", null, ["callee:008b6ab4:8"]]
+ 00b0d3b4 ["INT_ADD", "register:40f0:8", ["const:b0d3b4:8", "const:4:8"]]
+ 00b0d3b4 ["CALL", null, ["callee:008b6ab4:8"]]
- 00b0d318 bytes d1a5f697
+ 00b0d3b4 bytes c0a5f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ed35760a0ee952788038ee2e836b6e7"></a>

### [`00b0d3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d3d0.md) → [`00b0d46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d46c.md) FUN_00b0d46c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 13件 [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d3d0.md#insn-00b0d3fc) · [`00b0d41c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d3d0.md#insn-00b0d41c) · [`00b0d428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d3d0.md#insn-00b0d428)
- 新版 `00b0d498`（命令位置の公開資料なし） · `00b0d4b8`（命令位置の公開資料なし） · `00b0d4c4`（命令位置の公開資料なし）

~~~diff
- 00b0d3fc ["INT_ADD", "register:40f0:8", ["const:b0d3fc:8", "const:4:8"]]
- 00b0d3fc ["CALL", null, ["callee:008b92e8:8"]]
+ 00b0d498 ["INT_ADD", "register:40f0:8", ["const:b0d498:8", "const:4:8"]]
+ 00b0d498 ["CALL", null, ["callee:008b92e8:8"]]
- 00b0d3fc bytes a5aff697
+ 00b0d498 bytes 94aff697
- 00b0d41c ["INT_ADD", "register:40f0:8", ["const:b0d41c:8", "const:4:8"]]
- 00b0d41c ["CALL", null, ["callee:008b92f0:8"]]
+ 00b0d4b8 ["INT_ADD", "register:40f0:8", ["const:b0d4b8:8", "const:4:8"]]
+ 00b0d4b8 ["CALL", null, ["callee:008b92f0:8"]]
- 00b0d41c bytes 9faff697
+ 00b0d4b8 bytes 8eaff697
- 00b0d428 ["INT_ADD", "register:40f0:8", ["const:b0d428:8", "const:4:8"]]
- 00b0d428 ["CALL", null, ["callee:008b92f0:8"]]
+ 00b0d4c4 ["INT_ADD", "register:40f0:8", ["const:b0d4c4:8", "const:4:8"]]
+ 00b0d4c4 ["CALL", null, ["callee:008b92f0:8"]]
- 00b0d428 bytes 9caff697
+ 00b0d4c4 bytes 8baff697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c70a7e7578215bae6de8b92d1b13a6ba"></a>

### [`00b0daa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0daa0.md) → [`00b0db3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0db3c.md) FUN_00b0db3c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b0c254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0c254.md) · 呼出先 2件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00b0c2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0c2f0.md) · 呼出先 2件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0db08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0daa0.md#insn-00b0db08) · [`00b0db44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0daa0.md#insn-00b0db44) · [`00b0db54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0daa0.md#insn-00b0db54)
- 新版 `00b0dba4`（命令位置の公開資料なし） · `00b0dbe0`（命令位置の公開資料なし） · `00b0dbf0`（命令位置の公開資料なし）

~~~diff
- 00b0db08 ["INT_ADD", "register:40f0:8", ["const:b0db08:8", "const:4:8"]]
- 00b0db08 ["CALL", null, ["callee:00494650:8"]]
+ 00b0dba4 ["INT_ADD", "register:40f0:8", ["const:b0dba4:8", "const:4:8"]]
+ 00b0dba4 ["CALL", null, ["callee:00494650:8"]]
- 00b0db08 bytes c21ae697
+ 00b0dba4 bytes ab1ae697
- 00b0db44 ["INT_ADD", "register:40f0:8", ["const:b0db44:8", "const:4:8"]]
- 00b0db44 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b0dbe0 ["INT_ADD", "register:40f0:8", ["const:b0dbe0:8", "const:4:8"]]
+ 00b0dbe0 ["CALL", null, ["callee:00c57f80:8"]]
- 00b0db44 bytes db280594
+ 00b0dbe0 bytes e8280594
- 00b0db54 ["INT_ADD", "register:40f0:8", ["const:b0db54:8", "const:4:8"]]
- 00b0db54 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b0dbf0 ["INT_ADD", "register:40f0:8", ["const:b0dbf0:8", "const:4:8"]]
+ 00b0dbf0 ["CALL", null, ["callee:00c57f80:8"]]
- 00b0db54 bytes d7280594
+ 00b0dbf0 bytes e4280594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d8233a1056290d8f956f5e9bef4dbab"></a>

### [`00b0edbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0edbc.md) → [`00b0ee58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0e/00b0ee58.md) FUN_00b0ee58

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a1a750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a750.md) · 呼出先 2件 [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md) [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md)
- 新版 呼出元 1件 [`00a1a7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a7a4.md) · 呼出先 2件 [`00480338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480338.md) [`00480430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0eddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0edbc.md#insn-00b0eddc) · [`00b0ede8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0edbc.md#insn-00b0ede8) · [`00b0edf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0edbc.md#insn-00b0edf4)
- 新版 `00b0ee78`（命令位置の公開資料なし） · `00b0ee84`（命令位置の公開資料なし） · `00b0ee90`（命令位置の公開資料なし）

~~~diff
- 00b0eddc ["INT_ADD", "register:40f0:8", ["const:b0eddc:8", "const:4:8"]]
- 00b0eddc ["CALL", null, ["callee:00480430:8"]]
+ 00b0ee78 ["INT_ADD", "register:40f0:8", ["const:b0ee78:8", "const:4:8"]]
+ 00b0ee78 ["CALL", null, ["callee:00480430:8"]]
- 00b0eddc bytes 85c5e597
+ 00b0ee78 bytes 6ec5e597
- 00b0ede8 ["INT_ADD", "register:40f0:8", ["const:b0ede8:8", "const:4:8"]]
- 00b0ede8 ["CALL", null, ["callee:00480430:8"]]
+ 00b0ee84 ["INT_ADD", "register:40f0:8", ["const:b0ee84:8", "const:4:8"]]
+ 00b0ee84 ["CALL", null, ["callee:00480430:8"]]
- 00b0ede8 bytes 82c5e597
+ 00b0ee84 bytes 6bc5e597
- 00b0edf4 ["INT_ADD", "register:40f0:8", ["const:b0edf4:8", "const:4:8"]]
- 00b0edf4 ["CALL", null, ["callee:00480430:8"]]
+ 00b0ee90 ["INT_ADD", "register:40f0:8", ["const:b0ee90:8", "const:4:8"]]
+ 00b0ee90 ["CALL", null, ["callee:00480430:8"]]
- 00b0edf4 bytes 7fc5e597
+ 00b0ee90 bytes 68c5e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e316d0bdb8209f2614bee64e23a813e1"></a>

### [`00b0eedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0eedc.md) → [`00b0ef78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0e/00b0ef78.md) FUN_00b0ef78

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a223d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a22/00a223d0.md) · 呼出先 2件 [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md)
- 新版 呼出元 1件 [`00a22424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a22/00a22424.md) · 呼出先 2件 [`00480d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480d88.md) [`00480e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480e68.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0eefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0eedc.md#insn-00b0eefc) · [`00b0ef08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0eedc.md#insn-00b0ef08) · [`00b0ef14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0eedc.md#insn-00b0ef14)
- 新版 `00b0ef98`（命令位置の公開資料なし） · `00b0efa4`（命令位置の公開資料なし） · `00b0efb0`（命令位置の公開資料なし）

~~~diff
- 00b0eefc ["INT_ADD", "register:40f0:8", ["const:b0eefc:8", "const:4:8"]]
- 00b0eefc ["CALL", null, ["callee:00480e68:8"]]
+ 00b0ef98 ["INT_ADD", "register:40f0:8", ["const:b0ef98:8", "const:4:8"]]
+ 00b0ef98 ["CALL", null, ["callee:00480e68:8"]]
- 00b0eefc bytes cbc7e597
+ 00b0ef98 bytes b4c7e597
- 00b0ef08 ["INT_ADD", "register:40f0:8", ["const:b0ef08:8", "const:4:8"]]
- 00b0ef08 ["CALL", null, ["callee:00480e68:8"]]
+ 00b0efa4 ["INT_ADD", "register:40f0:8", ["const:b0efa4:8", "const:4:8"]]
+ 00b0efa4 ["CALL", null, ["callee:00480e68:8"]]
- 00b0ef08 bytes c8c7e597
+ 00b0efa4 bytes b1c7e597
- 00b0ef14 ["INT_ADD", "register:40f0:8", ["const:b0ef14:8", "const:4:8"]]
- 00b0ef14 ["CALL", null, ["callee:00480e68:8"]]
+ 00b0efb0 ["INT_ADD", "register:40f0:8", ["const:b0efb0:8", "const:4:8"]]
+ 00b0efb0 ["CALL", null, ["callee:00480e68:8"]]
- 00b0ef14 bytes c5c7e597
+ 00b0efb0 bytes aec7e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4968e1c1b26bc23ee29c46b0ac93b56"></a>

### [`00b0efa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0efa0.md) → [`00b0f03c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0f/00b0f03c.md) FUN_00b0f03c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a1a750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a750.md) · 呼出先 1件 [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md)
- 新版 呼出元 1件 [`00a1a7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a7a4.md) · 呼出先 1件 [`00480430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0efb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0efa0.md#insn-00b0efb8) · [`00b0efc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0efa0.md#insn-00b0efc4)
- 新版 `00b0f054`（命令位置の公開資料なし） · `00b0f060`（命令位置の公開資料なし）

~~~diff
- 00b0efb8 ["INT_ADD", "register:40f0:8", ["const:b0efb8:8", "const:4:8"]]
- 00b0efb8 ["CALL", null, ["callee:00480430:8"]]
+ 00b0f054 ["INT_ADD", "register:40f0:8", ["const:b0f054:8", "const:4:8"]]
+ 00b0f054 ["CALL", null, ["callee:00480430:8"]]
- 00b0efb8 bytes 0ec5e597
+ 00b0f054 bytes f7c4e597
- 00b0efc4 ["INT_ADD", "register:40f0:8", ["const:b0efc4:8", "const:4:8"]]
- 00b0efc4 ["CALL", null, ["callee:00480430:8"]]
+ 00b0f060 ["INT_ADD", "register:40f0:8", ["const:b0f060:8", "const:4:8"]]
+ 00b0f060 ["CALL", null, ["callee:00480430:8"]]
- 00b0efc4 bytes 0bc5e597
+ 00b0f060 bytes f4c4e597
~~~


<a id="compare-cf2d91665c70941efdd0e046b8e02cca"></a>

### [`00b0efd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0efd8.md) → [`00b0f074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0f/00b0f074.md) FUN_00b0f074

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a223d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a22/00a223d0.md) · 呼出先 1件 [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md)
- 新版 呼出元 1件 [`00a22424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a22/00a22424.md) · 呼出先 1件 [`00480e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480e68.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0eff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0efd8.md#insn-00b0eff8)
- 新版 `00b0f094`（命令位置の公開資料なし）

~~~diff
- 00b0eff8 ["INT_ADD", "register:40f0:8", ["const:b0eff8:8", "const:4:8"]]
- 00b0eff8 ["CALL", null, ["callee:00480e68:8"]]
+ 00b0f094 ["INT_ADD", "register:40f0:8", ["const:b0f094:8", "const:4:8"]]
+ 00b0f094 ["CALL", null, ["callee:00480e68:8"]]
- 00b0eff8 bytes 8cc7e597
+ 00b0f094 bytes 75c7e597
~~~


<a id="compare-fb66cc46c8d66ca90e128904f6462b8b"></a>

### [`00b0f40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f40c.md) → [`00b0f4a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0f/00b0f4a8.md) FUN_00b0f4a8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b0f5f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f5f4.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00b10d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b10/00b10d34.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00b0f690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0f/00b0f690.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00b10dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b10/00b10dd0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0f44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f40c.md#insn-00b0f44c) · [`00b0f45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f40c.md#insn-00b0f45c) · [`00b0f484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f40c.md#insn-00b0f484)
- 新版 `00b0f4e8`（命令位置の公開資料なし） · `00b0f4f8`（命令位置の公開資料なし） · `00b0f520`（命令位置の公開資料なし）

~~~diff
- 00b0f44c ["INT_ADD", "register:40f0:8", ["const:b0f44c:8", "const:4:8"]]
- 00b0f44c ["CALL", null, ["callee:0048797c:8"]]
+ 00b0f4e8 ["INT_ADD", "register:40f0:8", ["const:b0f4e8:8", "const:4:8"]]
+ 00b0f4e8 ["CALL", null, ["callee:0048797c:8"]]
- 00b0f44c bytes 3ce1e597
+ 00b0f4e8 bytes 25e1e597
- 00b0f45c ["INT_ADD", "register:40f0:8", ["const:b0f45c:8", "const:4:8"]]
- 00b0f45c ["CALL", null, ["callee:0048797c:8"]]
+ 00b0f4f8 ["INT_ADD", "register:40f0:8", ["const:b0f4f8:8", "const:4:8"]]
+ 00b0f4f8 ["CALL", null, ["callee:0048797c:8"]]
- 00b0f45c bytes 38e1e597
+ 00b0f4f8 bytes 21e1e597
- 00b0f484 ["INT_ADD", "register:40f0:8", ["const:b0f484:8", "const:4:8"]]
- 00b0f484 ["CALL", null, ["callee:0048795c:8"]]
+ 00b0f520 ["INT_ADD", "register:40f0:8", ["const:b0f520:8", "const:4:8"]]
+ 00b0f520 ["CALL", null, ["callee:0048795c:8"]]
- 00b0f484 bytes 26e1e597
+ 00b0f520 bytes 0fe1e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3ab92c51b8ff9cee432e0facb446aff"></a>

### [`00b1ee84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1ee84.md) → [`00b1ef20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1e/00b1ef20.md) FUN_00b1ef20

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b1e088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1e088.md) · 呼出先 3件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00b1e124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1e/00b1e124.md) · 呼出先 3件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1eee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1ee84.md#insn-00b1eee4) · [`00b1ef3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1ee84.md#insn-00b1ef3c) · [`00b1ef74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1ee84.md#insn-00b1ef74)
- 新版 `00b1ef80`（命令位置の公開資料なし） · `00b1efd8`（命令位置の公開資料なし） · `00b1f010`（命令位置の公開資料なし）

~~~diff
- 00b1eee4 ["INT_ADD", "register:40f0:8", ["const:b1eee4:8", "const:4:8"]]
- 00b1eee4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b1ef80 ["INT_ADD", "register:40f0:8", ["const:b1ef80:8", "const:4:8"]]
+ 00b1ef80 ["CALL", null, ["callee:00c57f60:8"]]
- 00b1eee4 bytes ebe30494
+ 00b1ef80 bytes f8e30494
- 00b1ef3c ["INT_ADD", "register:40f0:8", ["const:b1ef3c:8", "const:4:8"]]
- 00b1ef3c ["CALL", null, ["callee:00c57f80:8"]]
+ 00b1efd8 ["INT_ADD", "register:40f0:8", ["const:b1efd8:8", "const:4:8"]]
+ 00b1efd8 ["CALL", null, ["callee:00c57f80:8"]]
- 00b1ef3c bytes dde30494
+ 00b1efd8 bytes eae30494
- 00b1ef74 ["INT_ADD", "register:40f0:8", ["const:b1ef74:8", "const:4:8"]]
- 00b1ef74 ["CALL", null, ["callee:00440f00:8"]]
+ 00b1f010 ["INT_ADD", "register:40f0:8", ["const:b1f010:8", "const:4:8"]]
+ 00b1f010 ["CALL", null, ["callee:00440f00:8"]]
- 00b1ef74 bytes d387e497
+ 00b1f010 bytes bc87e497
~~~


<a id="compare-3f690a4d51b526a5cdf12bbe1e674cb0"></a>

### [`00b28e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28e0c.md) → [`00b28ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b28/00b28ea8.md) FUN_00b28ea8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)
- 新版 呼出元 1件 [`00b1f4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1f/00b1f4c4.md) · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b28e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28e0c.md#insn-00b28e68) · [`00b28e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28e0c.md#insn-00b28e90)
- 新版 `00b28f04`（命令位置の公開資料なし） · `00b28f2c`（命令位置の公開資料なし）

~~~diff
- 00b28e68 ["INT_ADD", "register:40f0:8", ["const:b28e68:8", "const:4:8"]]
- 00b28e68 ["CALL", null, ["callee:0043bb60:8"]]
+ 00b28f04 ["INT_ADD", "register:40f0:8", ["const:b28f04:8", "const:4:8"]]
+ 00b28f04 ["CALL", null, ["callee:0043bb60:8"]]
- 00b28e68 bytes 2e4be497
+ 00b28f04 bytes 174be497
- 00b28e90 ["INT_ADD", "register:40f0:8", ["const:b28e90:8", "const:4:8"]]
- 00b28e90 ["CALL", null, ["callee:0043bb60:8"]]
+ 00b28f2c ["INT_ADD", "register:40f0:8", ["const:b28f2c:8", "const:4:8"]]
+ 00b28f2c ["CALL", null, ["callee:0043bb60:8"]]
- 00b28e90 bytes 244be497
+ 00b28f2c bytes 0d4be497
~~~


<a id="compare-61acbd982751e9776e485e805a087be3"></a>

### [`00b28ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28ef0.md) → [`00b28f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b28/00b28f8c.md) FUN_00b28f8c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b28f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28ef0.md#insn-00b28f2c) · [`00b28f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28ef0.md#insn-00b28f3c)
- 新版 `00b28fc8`（命令位置の公開資料なし） · `00b28fd8`（命令位置の公開資料なし）

~~~diff
- 00b28f2c ["INT_ADD", "register:40f0:8", ["const:b28f2c:8", "const:4:8"]]
- 00b28f2c ["CALL", null, ["callee:00c57f80:8"]]
+ 00b28fc8 ["INT_ADD", "register:40f0:8", ["const:b28fc8:8", "const:4:8"]]
+ 00b28fc8 ["CALL", null, ["callee:00c57f80:8"]]
- 00b28f2c bytes e1bb0494
+ 00b28fc8 bytes eebb0494
- 00b28f3c ["INT_ADD", "register:40f0:8", ["const:b28f3c:8", "const:4:8"]]
- 00b28f3c ["CALL", null, ["callee:00c57f80:8"]]
+ 00b28fd8 ["INT_ADD", "register:40f0:8", ["const:b28fd8:8", "const:4:8"]]
+ 00b28fd8 ["CALL", null, ["callee:00c57f80:8"]]
- 00b28f3c bytes ddbb0494
+ 00b28fd8 bytes eabb0494
~~~


<a id="compare-1909b75d1867d962f77421dee59e5a3a"></a>

### [`00b29cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29cd8.md) → [`00b29d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b29/00b29d74.md) FUN_00b29d74

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b29e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29e6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00b13398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b13/00b13398.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00b29f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b29/00b29f08.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b29d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29cd8.md#insn-00b29d80) · [`00b29dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29cd8.md#insn-00b29dc0) · [`00b29e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29cd8.md#insn-00b29e04)
- 新版 `00b29e1c`（命令位置の公開資料なし） · `00b29e5c`（命令位置の公開資料なし） · `00b29ea0`（命令位置の公開資料なし）

~~~diff
- 00b29d80 ["INT_ADD", "register:40f0:8", ["const:b29d80:8", "const:4:8"]]
- 00b29d80 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b29e1c ["INT_ADD", "register:40f0:8", ["const:b29e1c:8", "const:4:8"]]
+ 00b29e1c ["CALL", null, ["callee:00c57f60:8"]]
- 00b29d80 bytes 44b80494
+ 00b29e1c bytes 51b80494
- 00b29dc0 ["INT_ADD", "register:40f0:8", ["const:b29dc0:8", "const:4:8"]]
- 00b29dc0 ["CALL", null, ["callee:00c58160:8"]]
+ 00b29e5c ["INT_ADD", "register:40f0:8", ["const:b29e5c:8", "const:4:8"]]
+ 00b29e5c ["CALL", null, ["callee:00c58160:8"]]
- 00b29dc0 bytes b4b80494
+ 00b29e5c bytes c1b80494
- 00b29e04 ["INT_ADD", "register:40f0:8", ["const:b29e04:8", "const:4:8"]]
- 00b29e04 ["CALL", null, ["callee:00c58160:8"]]
+ 00b29ea0 ["INT_ADD", "register:40f0:8", ["const:b29ea0:8", "const:4:8"]]
+ 00b29ea0 ["CALL", null, ["callee:00c58160:8"]]
- 00b29e04 bytes a3b80494
+ 00b29ea0 bytes b0b80494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-789d79951baf51333fcc01ccbb57c123"></a>

### [`00b29e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29e80.md) → [`00b29f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b29/00b29f1c.md) FUN_00b29f1c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b2a010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a010.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00b13398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b13/00b13398.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00b2a0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a0ac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b29f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29e80.md#insn-00b29f24) · [`00b29f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29e80.md#insn-00b29f64) · [`00b29fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29e80.md#insn-00b29fb0)
- 新版 `00b29fc0`（命令位置の公開資料なし） · `00b2a000`（命令位置の公開資料なし） · `00b2a04c`（命令位置の公開資料なし）

~~~diff
- 00b29f24 ["INT_ADD", "register:40f0:8", ["const:b29f24:8", "const:4:8"]]
- 00b29f24 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b29fc0 ["INT_ADD", "register:40f0:8", ["const:b29fc0:8", "const:4:8"]]
+ 00b29fc0 ["CALL", null, ["callee:00c57f60:8"]]
- 00b29f24 bytes dbb70494
+ 00b29fc0 bytes e8b70494
- 00b29f64 ["INT_ADD", "register:40f0:8", ["const:b29f64:8", "const:4:8"]]
- 00b29f64 ["CALL", null, ["callee:00c58160:8"]]
+ 00b2a000 ["INT_ADD", "register:40f0:8", ["const:b2a000:8", "const:4:8"]]
+ 00b2a000 ["CALL", null, ["callee:00c58160:8"]]
- 00b29f64 bytes 4bb80494
+ 00b2a000 bytes 58b80494
- 00b29fb0 ["INT_ADD", "register:40f0:8", ["const:b29fb0:8", "const:4:8"]]
- 00b29fb0 ["CALL", null, ["callee:00c58160:8"]]
+ 00b2a04c ["INT_ADD", "register:40f0:8", ["const:b2a04c:8", "const:4:8"]]
+ 00b2a04c ["CALL", null, ["callee:00c58160:8"]]
- 00b29fb0 bytes 38b80494
+ 00b2a04c bytes 45b80494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f0010c0ec2ff66a10691f11b721ae65"></a>

### [`00b2a024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a024.md) → [`00b2a0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a0c0.md) FUN_00b2a0c0

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b2a150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a150.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00b13398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b13/00b13398.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00b2a1ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a1ec.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2a09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a024.md#insn-00b2a09c) · [`00b2a0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a024.md#insn-00b2a0c0) · [`00b2a0ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a024.md#insn-00b2a0ec)
- 新版 `00b2a138`（命令位置の公開資料なし） · `00b2a15c`（命令位置の公開資料なし） · `00b2a188`（命令位置の公開資料なし）

~~~diff
- 00b2a09c ["INT_ADD", "register:40f0:8", ["const:b2a09c:8", "const:4:8"]]
- 00b2a09c ["CALL", null, ["callee:00c57f60:8"]]
+ 00b2a138 ["INT_ADD", "register:40f0:8", ["const:b2a138:8", "const:4:8"]]
+ 00b2a138 ["CALL", null, ["callee:00c57f60:8"]]
- 00b2a09c bytes 7db70494
+ 00b2a138 bytes 8ab70494
- 00b2a0c0 ["INT_ADD", "register:40f0:8", ["const:b2a0c0:8", "const:4:8"]]
- 00b2a0c0 ["CALL", null, ["callee:00c58160:8"]]
+ 00b2a15c ["INT_ADD", "register:40f0:8", ["const:b2a15c:8", "const:4:8"]]
+ 00b2a15c ["CALL", null, ["callee:00c58160:8"]]
- 00b2a0c0 bytes f4b70494
+ 00b2a15c bytes 01b80494
- 00b2a0ec ["INT_ADD", "register:40f0:8", ["const:b2a0ec:8", "const:4:8"]]
- 00b2a0ec ["CALL", null, ["callee:00c58160:8"]]
+ 00b2a188 ["INT_ADD", "register:40f0:8", ["const:b2a188:8", "const:4:8"]]
+ 00b2a188 ["CALL", null, ["callee:00c58160:8"]]
- 00b2a0ec bytes e9b70494
+ 00b2a188 bytes f6b70494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13788baf7ec36c6ab89b6c0c7754d1f8"></a>

### [`00b2a164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a164.md) → [`00b2a200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a200.md) FUN_00b2a200

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b2a2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a2f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00b13398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b13/00b13398.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00b2a394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a394.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2a20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a164.md#insn-00b2a20c) · [`00b2a24c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a164.md#insn-00b2a24c) · [`00b2a290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a164.md#insn-00b2a290)
- 新版 `00b2a2a8`（命令位置の公開資料なし） · `00b2a2e8`（命令位置の公開資料なし） · `00b2a32c`（命令位置の公開資料なし）

~~~diff
- 00b2a20c ["INT_ADD", "register:40f0:8", ["const:b2a20c:8", "const:4:8"]]
- 00b2a20c ["CALL", null, ["callee:00c57f60:8"]]
+ 00b2a2a8 ["INT_ADD", "register:40f0:8", ["const:b2a2a8:8", "const:4:8"]]
+ 00b2a2a8 ["CALL", null, ["callee:00c57f60:8"]]
- 00b2a20c bytes 21b70494
+ 00b2a2a8 bytes 2eb70494
- 00b2a24c ["INT_ADD", "register:40f0:8", ["const:b2a24c:8", "const:4:8"]]
- 00b2a24c ["CALL", null, ["callee:00c58160:8"]]
+ 00b2a2e8 ["INT_ADD", "register:40f0:8", ["const:b2a2e8:8", "const:4:8"]]
+ 00b2a2e8 ["CALL", null, ["callee:00c58160:8"]]
- 00b2a24c bytes 91b70494
+ 00b2a2e8 bytes 9eb70494
- 00b2a290 ["INT_ADD", "register:40f0:8", ["const:b2a290:8", "const:4:8"]]
- 00b2a290 ["CALL", null, ["callee:00c58160:8"]]
+ 00b2a32c ["INT_ADD", "register:40f0:8", ["const:b2a32c:8", "const:4:8"]]
+ 00b2a32c ["CALL", null, ["callee:00c58160:8"]]
- 00b2a290 bytes 80b70494
+ 00b2a32c bytes 8db70494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e09ab9e48a6914eecffada46d0f21dfb"></a>

### [`00b2a30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a30c.md) → [`00b2a3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a3a8.md) FUN_00b2a3a8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b2a49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a49c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00b13398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b13/00b13398.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00b2a538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a538.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2a3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a30c.md#insn-00b2a3b0) · [`00b2a3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a30c.md#insn-00b2a3f0) · [`00b2a43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a30c.md#insn-00b2a43c)
- 新版 `00b2a44c`（命令位置の公開資料なし） · `00b2a48c`（命令位置の公開資料なし） · `00b2a4d8`（命令位置の公開資料なし）

~~~diff
- 00b2a3b0 ["INT_ADD", "register:40f0:8", ["const:b2a3b0:8", "const:4:8"]]
- 00b2a3b0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b2a44c ["INT_ADD", "register:40f0:8", ["const:b2a44c:8", "const:4:8"]]
+ 00b2a44c ["CALL", null, ["callee:00c57f60:8"]]
- 00b2a3b0 bytes b8b60494
+ 00b2a44c bytes c5b60494
- 00b2a3f0 ["INT_ADD", "register:40f0:8", ["const:b2a3f0:8", "const:4:8"]]
- 00b2a3f0 ["CALL", null, ["callee:00c58160:8"]]
+ 00b2a48c ["INT_ADD", "register:40f0:8", ["const:b2a48c:8", "const:4:8"]]
+ 00b2a48c ["CALL", null, ["callee:00c58160:8"]]
- 00b2a3f0 bytes 28b70494
+ 00b2a48c bytes 35b70494
- 00b2a43c ["INT_ADD", "register:40f0:8", ["const:b2a43c:8", "const:4:8"]]
- 00b2a43c ["CALL", null, ["callee:00c58160:8"]]
+ 00b2a4d8 ["INT_ADD", "register:40f0:8", ["const:b2a4d8:8", "const:4:8"]]
+ 00b2a4d8 ["CALL", null, ["callee:00c58160:8"]]
- 00b2a43c bytes 15b70494
+ 00b2a4d8 bytes 22b70494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c5617fda52dbb5238b0bb8b7eb4b791"></a>

### [`00b2a4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a4c4.md) → [`00b2a560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a560.md) FUN_00b2a560

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b2a5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a5f0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00b13398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b13/00b13398.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00b2a68c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a68c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2a53c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a4c4.md#insn-00b2a53c) · [`00b2a560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a4c4.md#insn-00b2a560) · [`00b2a58c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a4c4.md#insn-00b2a58c)
- 新版 `00b2a5d8`（命令位置の公開資料なし） · `00b2a5fc`（命令位置の公開資料なし） · `00b2a628`（命令位置の公開資料なし）

~~~diff
- 00b2a53c ["INT_ADD", "register:40f0:8", ["const:b2a53c:8", "const:4:8"]]
- 00b2a53c ["CALL", null, ["callee:00c57f60:8"]]
+ 00b2a5d8 ["INT_ADD", "register:40f0:8", ["const:b2a5d8:8", "const:4:8"]]
+ 00b2a5d8 ["CALL", null, ["callee:00c57f60:8"]]
- 00b2a53c bytes 55b60494
+ 00b2a5d8 bytes 62b60494
- 00b2a560 ["INT_ADD", "register:40f0:8", ["const:b2a560:8", "const:4:8"]]
- 00b2a560 ["CALL", null, ["callee:00c58160:8"]]
+ 00b2a5fc ["INT_ADD", "register:40f0:8", ["const:b2a5fc:8", "const:4:8"]]
+ 00b2a5fc ["CALL", null, ["callee:00c58160:8"]]
- 00b2a560 bytes ccb60494
+ 00b2a5fc bytes d9b60494
- 00b2a58c ["INT_ADD", "register:40f0:8", ["const:b2a58c:8", "const:4:8"]]
- 00b2a58c ["CALL", null, ["callee:00c58160:8"]]
+ 00b2a628 ["INT_ADD", "register:40f0:8", ["const:b2a628:8", "const:4:8"]]
+ 00b2a628 ["CALL", null, ["callee:00c58160:8"]]
- 00b2a58c bytes c1b60494
+ 00b2a628 bytes ceb60494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5996beab3c40aef06a6fb706597a1b3f"></a>

### [`00b2a83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a83c.md) → [`00b2a8d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a8d8.md) FUN_00b2a8d8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b2aab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2aab0.md) [`00b2aac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2aac4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00b1f4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1f/00b1f4c4.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00b2ab4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2ab4c.md) [`00b2ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2ab60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2a8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a83c.md#insn-00b2a8dc) · [`00b2a96c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a83c.md#insn-00b2a96c) · [`00b2a988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a83c.md#insn-00b2a988)
- 新版 `00b2a978`（命令位置の公開資料なし） · `00b2aa08`（命令位置の公開資料なし） · `00b2aa24`（命令位置の公開資料なし）

~~~diff
- 00b2a8dc ["INT_ADD", "register:40f0:8", ["const:b2a8dc:8", "const:4:8"]]
- 00b2a8dc ["CALL", null, ["callee:00c57f60:8"]]
+ 00b2a978 ["INT_ADD", "register:40f0:8", ["const:b2a978:8", "const:4:8"]]
+ 00b2a978 ["CALL", null, ["callee:00c57f60:8"]]
- 00b2a8dc bytes 6db50494
+ 00b2a978 bytes 7ab50494
- 00b2a96c ["INT_ADD", "register:40f0:8", ["const:b2a96c:8", "const:4:8"]]
- 00b2a96c ["CALL", null, ["callee:00b2ab60:8"]]
+ 00b2aa08 ["INT_ADD", "register:40f0:8", ["const:b2aa08:8", "const:4:8"]]
+ 00b2aa08 ["CALL", null, ["callee:00b2ab60:8"]]
- 00b2a96c bytes 56000094
+ 00b2aa08 bytes 56000094
- 00b2a988 ["INT_ADD", "register:40f0:8", ["const:b2a988:8", "const:4:8"]]
- 00b2a988 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b2aa24 ["INT_ADD", "register:40f0:8", ["const:b2aa24:8", "const:4:8"]]
+ 00b2aa24 ["CALL", null, ["callee:00c57f80:8"]]
- 00b2a988 bytes 4ab50494
+ 00b2aa24 bytes 57b50494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0b4b7bc6318714843adb94cb4b4d223"></a>

### [`00b2aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2aa10.md) → [`00b2aaac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2aaac.md) FUN_00b2aaac

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2aa60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2aa10.md#insn-00b2aa60) · [`00b2aa70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2aa10.md#insn-00b2aa70) · [`00b2aa80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2aa10.md#insn-00b2aa80)
- 新版 `00b2aafc`（命令位置の公開資料なし） · `00b2ab0c`（命令位置の公開資料なし） · `00b2ab1c`（命令位置の公開資料なし）

~~~diff
- 00b2aa60 ["INT_ADD", "register:40f0:8", ["const:b2aa60:8", "const:4:8"]]
- 00b2aa60 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b2aafc ["INT_ADD", "register:40f0:8", ["const:b2aafc:8", "const:4:8"]]
+ 00b2aafc ["CALL", null, ["callee:00c57f80:8"]]
- 00b2aa60 bytes 14b50494
+ 00b2aafc bytes 21b50494
- 00b2aa70 ["INT_ADD", "register:40f0:8", ["const:b2aa70:8", "const:4:8"]]
- 00b2aa70 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b2ab0c ["INT_ADD", "register:40f0:8", ["const:b2ab0c:8", "const:4:8"]]
+ 00b2ab0c ["CALL", null, ["callee:00c57f80:8"]]
- 00b2aa70 bytes 10b50494
+ 00b2ab0c bytes 1db50494
- 00b2aa80 ["INT_ADD", "register:40f0:8", ["const:b2aa80:8", "const:4:8"]]
- 00b2aa80 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b2ab1c ["INT_ADD", "register:40f0:8", ["const:b2ab1c:8", "const:4:8"]]
+ 00b2ab1c ["CALL", null, ["callee:00c57f80:8"]]
- 00b2aa80 bytes 0cb50494
+ 00b2ab1c bytes 19b50494
~~~


<a id="compare-336cd127b9adeb6d47962f6e19dbd297"></a>

### [`00b2aac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2aac4.md) → [`00b2ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2ab60.md) FUN_00b2ab60

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b2a83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a83c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00b2a8d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a8d8.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2ab84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2aac4.md#insn-00b2ab84) · [`00b2ab94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2aac4.md#insn-00b2ab94) · [`00b2aba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2aac4.md#insn-00b2aba4)
- 新版 `00b2ac20`（命令位置の公開資料なし） · `00b2ac30`（命令位置の公開資料なし） · `00b2ac40`（命令位置の公開資料なし）

~~~diff
- 00b2ab84 ["INT_ADD", "register:40f0:8", ["const:b2ab84:8", "const:4:8"]]
- 00b2ab84 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b2ac20 ["INT_ADD", "register:40f0:8", ["const:b2ac20:8", "const:4:8"]]
+ 00b2ac20 ["CALL", null, ["callee:00c57f80:8"]]
- 00b2ab84 bytes cbb40494
+ 00b2ac20 bytes d8b40494
- 00b2ab94 ["INT_ADD", "register:40f0:8", ["const:b2ab94:8", "const:4:8"]]
- 00b2ab94 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b2ac30 ["INT_ADD", "register:40f0:8", ["const:b2ac30:8", "const:4:8"]]
+ 00b2ac30 ["CALL", null, ["callee:00c57f80:8"]]
- 00b2ab94 bytes c7b40494
+ 00b2ac30 bytes d4b40494
- 00b2aba4 ["INT_ADD", "register:40f0:8", ["const:b2aba4:8", "const:4:8"]]
- 00b2aba4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b2ac40 ["INT_ADD", "register:40f0:8", ["const:b2ac40:8", "const:4:8"]]
+ 00b2ac40 ["CALL", null, ["callee:00c57f80:8"]]
- 00b2aba4 bytes c3b40494
+ 00b2ac40 bytes d0b40494
~~~


<a id="compare-0ba0518c28c856d25c826b33acdca748"></a>

### [`00b2abcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2abcc.md) → [`00b2ac68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2ac68.md) FUN_00b2ac68

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0054075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054075c.md) [`00794b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794b6c.md) [`0080da5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080da5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00b1f4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1f/00b1f4c4.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0054079c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054079c.md) [`00794bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794bc4.md) [`0080dab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080dab4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2abcc.md#insn-00b2ac70) · [`00b2acb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2abcc.md#insn-00b2acb8) · [`00b2acd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2abcc.md#insn-00b2acd0)
- 新版 `00b2ad0c`（命令位置の公開資料なし） · `00b2ad54`（命令位置の公開資料なし） · `00b2ad6c`（命令位置の公開資料なし）

~~~diff
- 00b2ac70 ["INT_ADD", "register:40f0:8", ["const:b2ac70:8", "const:4:8"]]
- 00b2ac70 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b2ad0c ["INT_ADD", "register:40f0:8", ["const:b2ad0c:8", "const:4:8"]]
+ 00b2ad0c ["CALL", null, ["callee:00c57f60:8"]]
- 00b2ac70 bytes 88b40494
+ 00b2ad0c bytes 95b40494
- 00b2acb8 ["INT_ADD", "register:40f0:8", ["const:b2acb8:8", "const:4:8"]]
- 00b2acb8 ["CALL", null, ["callee:0054079c:8"]]
+ 00b2ad54 ["INT_ADD", "register:40f0:8", ["const:b2ad54:8", "const:4:8"]]
+ 00b2ad54 ["CALL", null, ["callee:0054079c:8"]]
- 00b2acb8 bytes a956e897
+ 00b2ad54 bytes 9256e897
- 00b2acd0 ["INT_ADD", "register:40f0:8", ["const:b2acd0:8", "const:4:8"]]
- 00b2acd0 ["CALL", null, ["callee:0080dab4:8"]]
+ 00b2ad6c ["INT_ADD", "register:40f0:8", ["const:b2ad6c:8", "const:4:8"]]
+ 00b2ad6c ["CALL", null, ["callee:0080dab4:8"]]
- 00b2acd0 bytes 638bf397
+ 00b2ad6c bytes 528bf397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0754a2be9b35a614cd559b2af860bd0"></a>

### [`00b2addc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2addc.md) → [`00b2ae78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2ae78.md) FUN_00b2ae78

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005e8198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e8/005e8198.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00b1f4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1f/00b1f4c4.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005e81d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e8/005e81d8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2ae5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2addc.md#insn-00b2ae5c) · [`00b2ae90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2addc.md#insn-00b2ae90) · [`00b2ae9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2addc.md#insn-00b2ae9c)
- 新版 `00b2aef8`（命令位置の公開資料なし） · `00b2af2c`（命令位置の公開資料なし） · `00b2af38`（命令位置の公開資料なし）

~~~diff
- 00b2ae5c ["INT_ADD", "register:40f0:8", ["const:b2ae5c:8", "const:4:8"]]
- 00b2ae5c ["CALL", null, ["callee:00c57f60:8"]]
+ 00b2aef8 ["INT_ADD", "register:40f0:8", ["const:b2aef8:8", "const:4:8"]]
+ 00b2aef8 ["CALL", null, ["callee:00c57f60:8"]]
- 00b2ae5c bytes 0db40494
+ 00b2aef8 bytes 1ab40494
- 00b2ae90 ["INT_ADD", "register:40f0:8", ["const:b2ae90:8", "const:4:8"]]
- 00b2ae90 ["CALL", null, ["callee:005e81d8:8"]]
+ 00b2af2c ["INT_ADD", "register:40f0:8", ["const:b2af2c:8", "const:4:8"]]
+ 00b2af2c ["CALL", null, ["callee:005e81d8:8"]]
- 00b2ae90 bytes c2f4ea97
+ 00b2af2c bytes abf4ea97
- 00b2ae9c ["INT_ADD", "register:40f0:8", ["const:b2ae9c:8", "const:4:8"]]
- 00b2ae9c ["CALL", null, ["callee:005e81d8:8"]]
+ 00b2af38 ["INT_ADD", "register:40f0:8", ["const:b2af38:8", "const:4:8"]]
+ 00b2af38 ["CALL", null, ["callee:005e81d8:8"]]
- 00b2ae9c bytes bff4ea97
+ 00b2af38 bytes a8f4ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29b5e8fd9be7abcf72c16d47a7baa98d"></a>

### [`00b2af48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2af48.md) → [`00b2afe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2afe4.md) FUN_00b2afe4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 6件 [`00615ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615ecc.md) [`006524c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00652/006524c0.md) [`0065254c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00652/0065254c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00b1f4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1f/00b1f4c4.md) · 呼出先 6件 [`00615f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00615/00615f0c.md) [`00652500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652500.md) [`0065258c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/0065258c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2afc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2af48.md#insn-00b2afc0) · [`00b2afe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2af48.md#insn-00b2afe4) · [`00b2b034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2af48.md#insn-00b2b034)
- 新版 `00b2b05c`（命令位置の公開資料なし） · `00b2b080`（命令位置の公開資料なし） · `00b2b0d0`（命令位置の公開資料なし）

~~~diff
- 00b2afc0 ["INT_ADD", "register:40f0:8", ["const:b2afc0:8", "const:4:8"]]
- 00b2afc0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b2b05c ["INT_ADD", "register:40f0:8", ["const:b2b05c:8", "const:4:8"]]
+ 00b2b05c ["CALL", null, ["callee:00c57f60:8"]]
- 00b2afc0 bytes b4b30494
+ 00b2b05c bytes c1b30494
- 00b2afe4 ["INT_ADD", "register:40f0:8", ["const:b2afe4:8", "const:4:8"]]
- 00b2afe4 ["CALL", null, ["callee:0065258c:8"]]
+ 00b2b080 ["INT_ADD", "register:40f0:8", ["const:b2b080:8", "const:4:8"]]
+ 00b2b080 ["CALL", null, ["callee:0065258c:8"]]
- 00b2afe4 bytes 5a9dec97
+ 00b2b080 bytes 439dec97
- 00b2b034 ["INT_ADD", "register:40f0:8", ["const:b2b034:8", "const:4:8"]]
- 00b2b034 ["CALL", null, ["callee:00615f0c:8"]]
+ 00b2b0d0 ["INT_ADD", "register:40f0:8", ["const:b2b0d0:8", "const:4:8"]]
+ 00b2b0d0 ["CALL", null, ["callee:00615f0c:8"]]
- 00b2b034 bytes a6abeb97
+ 00b2b0d0 bytes 8fabeb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50e97a7e2de068af7653b5eeffd95d40"></a>

### [`00b2b2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b2f4.md) → [`00b2b390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b390.md) FUN_00b2b390

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b2b070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b070.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00b2b10c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b10c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2b370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b2f4.md#insn-00b2b370) · [`00b2b3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b2f4.md#insn-00b2b3b8)
- 新版 `00b2b40c`（命令位置の公開資料なし） · `00b2b454`（命令位置の公開資料なし）

~~~diff
- 00b2b370 ["INT_ADD", "register:40f0:8", ["const:b2b370:8", "const:4:8"]]
- 00b2b370 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b2b40c ["INT_ADD", "register:40f0:8", ["const:b2b40c:8", "const:4:8"]]
+ 00b2b40c ["CALL", null, ["callee:00c57f80:8"]]
- 00b2b370 bytes d0b20494
+ 00b2b40c bytes ddb20494
- 00b2b3b8 ["INT_ADD", "register:40f0:8", ["const:b2b3b8:8", "const:4:8"]]
- 00b2b3b8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b2b454 ["INT_ADD", "register:40f0:8", ["const:b2b454:8", "const:4:8"]]
+ 00b2b454 ["CALL", null, ["callee:00c57f80:8"]]
- 00b2b3b8 bytes beb20494
+ 00b2b454 bytes cbb20494
~~~


<a id="compare-1421151b73533b21c1a6b9f67a47f9d1"></a>

### [`00b2b410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b410.md) → [`00b2b4ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b4ac.md) FUN_00b2b4ac

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b2b070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b070.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00b2b10c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b10c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2b444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b410.md#insn-00b2b444) · [`00b2b494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b410.md#insn-00b2b494)
- 新版 `00b2b4e0`（命令位置の公開資料なし） · `00b2b530`（命令位置の公開資料なし）

~~~diff
- 00b2b444 ["INT_ADD", "register:40f0:8", ["const:b2b444:8", "const:4:8"]]
- 00b2b444 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b2b4e0 ["INT_ADD", "register:40f0:8", ["const:b2b4e0:8", "const:4:8"]]
+ 00b2b4e0 ["CALL", null, ["callee:00c57f80:8"]]
- 00b2b444 bytes 9bb20494
+ 00b2b4e0 bytes a8b20494
- 00b2b494 ["INT_ADD", "register:40f0:8", ["const:b2b494:8", "const:4:8"]]
- 00b2b494 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b2b530 ["INT_ADD", "register:40f0:8", ["const:b2b530:8", "const:4:8"]]
+ 00b2b530 ["CALL", null, ["callee:00c57f80:8"]]
- 00b2b494 bytes 87b20494
+ 00b2b530 bytes 94b20494
~~~


<a id="compare-d14324d9d9d8ea65f9eb49a9c0b601b6"></a>

### [`00b2bbcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bbcc.md) → [`00b2bc68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2bc68.md) FUN_00b2bc68

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0043b5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b5a8.md) [`0043b658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b658.md) · 呼出先 4件 [`0046caa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046caa4.md) [`0046cabc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cabc.md) [`0046cac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cac8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`0043b5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b5e8.md) [`0043b698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b698.md) · 呼出先 4件 [`0046cae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cae4.md) [`0046cafc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cafc.md) [`0046cb08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cb08.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2bbdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bbcc.md#insn-00b2bbdc) · [`00b2bbe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bbcc.md#insn-00b2bbe4) · [`00b2bbec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bbcc.md#insn-00b2bbec)
- 新版 `00b2bc78`（命令位置の公開資料なし） · `00b2bc80`（命令位置の公開資料なし） · `00b2bc88`（命令位置の公開資料なし）

~~~diff
- 00b2bbdc ["INT_ADD", "register:40f0:8", ["const:b2bbdc:8", "const:4:8"]]
- 00b2bbdc ["CALL", null, ["callee:00851550:8"]]
+ 00b2bc78 ["INT_ADD", "register:40f0:8", ["const:b2bc78:8", "const:4:8"]]
+ 00b2bc78 ["CALL", null, ["callee:00851550:8"]]
- 00b2bbdc bytes 4796f497
+ 00b2bc78 bytes 3696f497
- 00b2bbe4 ["INT_ADD", "register:40f0:8", ["const:b2bbe4:8", "const:4:8"]]
- 00b2bbe4 ["CALL", null, ["callee:0046cafc:8"]]
+ 00b2bc80 ["INT_ADD", "register:40f0:8", ["const:b2bc80:8", "const:4:8"]]
+ 00b2bc80 ["CALL", null, ["callee:0046cafc:8"]]
- 00b2bbe4 bytes b603e597
+ 00b2bc80 bytes 9f03e597
- 00b2bbec ["INT_ADD", "register:40f0:8", ["const:b2bbec:8", "const:4:8"]]
- 00b2bbec ["CALL", null, ["callee:00851550:8"]]
+ 00b2bc88 ["INT_ADD", "register:40f0:8", ["const:b2bc88:8", "const:4:8"]]
+ 00b2bc88 ["CALL", null, ["callee:00851550:8"]]
- 00b2bbec bytes 4396f497
+ 00b2bc88 bytes 3296f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-132d1067d1e4ac8ada49868339314148"></a>

### [`00b2bc34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bc34.md) → [`00b2bcd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2bcd0.md) FUN_00b2bcd0

採用 · 移動量 `+0x9c` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0043b428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b428.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`0043b468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b468.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2bc44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bc34.md#insn-00b2bc44)
- 新版 `00b2bce0`（命令位置の公開資料なし）

~~~diff
- 00b2bc44 ["INT_ADD", "register:40f0:8", ["const:b2bc44:8", "const:4:8"]]
- 00b2bc44 ["CALL", null, ["callee:00851550:8"]]
+ 00b2bce0 ["INT_ADD", "register:40f0:8", ["const:b2bce0:8", "const:4:8"]]
+ 00b2bce0 ["CALL", null, ["callee:00851550:8"]]
- 00b2bc44 bytes 2d96f497
+ 00b2bce0 bytes 1c96f497
~~~


<a id="compare-2d2541974b9497af995dd96bde22ee62"></a>

### [`00b2d25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d25c.md) → [`00b2d2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d2f8.md) FUN_00b2d2f8

採用 · 移動量 `+0x9c` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0043b368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b368.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`0043b3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b3a8.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2d278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d25c.md#insn-00b2d278)
- 新版 `00b2d314`（命令位置の公開資料なし）

~~~diff
- 00b2d278 ["INT_ADD", "register:40f0:8", ["const:b2d278:8", "const:4:8"]]
- 00b2d278 ["CALL", null, ["callee:00851550:8"]]
+ 00b2d314 ["INT_ADD", "register:40f0:8", ["const:b2d314:8", "const:4:8"]]
+ 00b2d314 ["CALL", null, ["callee:00851550:8"]]
- 00b2d278 bytes a090f497
+ 00b2d314 bytes 8f90f497
~~~


<a id="compare-8cb382db91b39a5738d8df368fbca7d8"></a>

### [`00b2d2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d2a4.md) → [`00b2d340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d340.md) FUN_00b2d340

採用 · 移動量 `+0x9c` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0043b368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b368.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`0043b3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b3a8.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2d2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d2a4.md#insn-00b2d2c0)
- 新版 `00b2d35c`（命令位置の公開資料なし）

~~~diff
- 00b2d2c0 ["INT_ADD", "register:40f0:8", ["const:b2d2c0:8", "const:4:8"]]
- 00b2d2c0 ["CALL", null, ["callee:00851550:8"]]
+ 00b2d35c ["INT_ADD", "register:40f0:8", ["const:b2d35c:8", "const:4:8"]]
+ 00b2d35c ["CALL", null, ["callee:00851550:8"]]
- 00b2d2c0 bytes 8e90f497
+ 00b2d35c bytes 7d90f497
~~~


<a id="compare-a191113179284e3dff96991f0ec73619"></a>

### [`00b2d2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d2ec.md) → [`00b2d388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d388.md) FUN_00b2d388

採用 · 移動量 `+0x9c` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0043b368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b368.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`0043b3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b3a8.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2d308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d2ec.md#insn-00b2d308)
- 新版 `00b2d3a4`（命令位置の公開資料なし）

~~~diff
- 00b2d308 ["INT_ADD", "register:40f0:8", ["const:b2d308:8", "const:4:8"]]
- 00b2d308 ["CALL", null, ["callee:00851550:8"]]
+ 00b2d3a4 ["INT_ADD", "register:40f0:8", ["const:b2d3a4:8", "const:4:8"]]
+ 00b2d3a4 ["CALL", null, ["callee:00851550:8"]]
- 00b2d308 bytes 7c90f497
+ 00b2d3a4 bytes 6b90f497
~~~


<a id="compare-b1b5da0900bf65e3efdc293e8ec138c6"></a>

### [`00b2d414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d414.md) → [`00b2d4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d4b0.md) FUN_00b2d4b0

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2d41c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d414.md#insn-00b2d41c)
- 新版 `00b2d4b8`（命令位置の公開資料なし）

~~~diff
- 00b2d41c ["INT_ADD", "register:40f0:8", ["const:b2d41c:8", "const:4:8"]]
- 00b2d41c ["CALL", null, ["callee:00851550:8"]]
+ 00b2d4b8 ["INT_ADD", "register:40f0:8", ["const:b2d4b8:8", "const:4:8"]]
+ 00b2d4b8 ["CALL", null, ["callee:00851550:8"]]
- 00b2d41c bytes 3790f497
+ 00b2d4b8 bytes 2690f497
~~~


<a id="compare-5712cb91d0a6dee67131764f77688e81"></a>

### [`00b2d498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d498.md) → [`00b2d534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d534.md) FUN_00b2d534

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2d4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d498.md#insn-00b2d4a0)
- 新版 `00b2d53c`（命令位置の公開資料なし）

~~~diff
- 00b2d4a0 ["INT_ADD", "register:40f0:8", ["const:b2d4a0:8", "const:4:8"]]
- 00b2d4a0 ["CALL", null, ["callee:00851550:8"]]
+ 00b2d53c ["INT_ADD", "register:40f0:8", ["const:b2d53c:8", "const:4:8"]]
+ 00b2d53c ["CALL", null, ["callee:00851550:8"]]
- 00b2d4a0 bytes 1690f497
+ 00b2d53c bytes 0590f497
~~~


<a id="compare-172e1ad389ff7e361e83967018ebd284"></a>

### [`00b2d824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d824.md) → [`00b2d8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d8c0.md) FUN_00b2d8c0

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b2c450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c450.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00b2c4ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c4ec.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2d844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d824.md#insn-00b2d844)
- 新版 `00b2d8e0`（命令位置の公開資料なし）

~~~diff
- 00b2d844 ["INT_ADD", "register:40f0:8", ["const:b2d844:8", "const:4:8"]]
- 00b2d844 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b2d8e0 ["INT_ADD", "register:40f0:8", ["const:b2d8e0:8", "const:4:8"]]
+ 00b2d8e0 ["CALL", null, ["callee:00c57f80:8"]]
- 00b2d844 bytes 9ba90494
+ 00b2d8e0 bytes a8a90494
~~~


<a id="compare-6f8487b240e3e5214d85acd0b86f8c66"></a>

### [`00b2f880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f880.md) → [`00b2f91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2f/00b2f91c.md) FUN_00b2f91c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 19件 [`0060a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060a/0060a8a0.md) [`00664a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664a8c.md) [`00664bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664bcc.md) [`00664c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664c28.md) [`00665110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00665/00665110.md) · 呼出先 1件 [`00b3be94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be94.md)
- 新版 呼出元 19件 [`0060a8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0060a/0060a8e0.md) [`00664acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664acc.md) [`00664c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664c0c.md) [`00664c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664c68.md) [`00665150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00665/00665150.md) · 呼出先 1件 [`00b3bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2f888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f880.md#insn-00b2f888)
- 新版 `00b2f924`（命令位置の公開資料なし）

~~~diff
- 00b2f888 ["INT_ADD", "register:40f0:8", ["const:b2f888:8", "const:4:8"]]
- 00b2f888 ["CALL", null, ["callee:00b3bf30:8"]]
+ 00b2f924 ["INT_ADD", "register:40f0:8", ["const:b2f924:8", "const:4:8"]]
+ 00b2f924 ["CALL", null, ["callee:00b3bf30:8"]]
- 00b2f888 bytes 83310094
+ 00b2f924 bytes 83310094
~~~


<a id="compare-195c0928bbb0d2308a446923a1ba64df"></a>

### [`00b2f9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f9b8.md) → [`00b2fa54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2f/00b2fa54.md) FUN_00b2fa54

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 32件 [`005afc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afc78.md) [`005fdc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fd/005fdc58.md) [`0063d914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063d/0063d914.md) [`0064a530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064a/0064a530.md) [`006535a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00653/006535a0.md) · 呼出先 1件 [`00b3be94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be94.md)
- 新版 呼出元 32件 [`005afcb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005af/005afcb8.md) [`005fdc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fd/005fdc98.md) [`0063d954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063d954.md) [`0064a570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064a/0064a570.md) [`006535e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/006535e0.md) · 呼出先 1件 [`00b3bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2f9cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f9b8.md#insn-00b2f9cc) · [`00b2f9e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f9b8.md#insn-00b2f9e8)
- 新版 `00b2fa68`（命令位置の公開資料なし） · `00b2fa84`（命令位置の公開資料なし）

~~~diff
- 00b2f9cc ["INT_ADD", "register:40f0:8", ["const:b2f9cc:8", "const:4:8"]]
- 00b2f9cc ["CALL", null, ["callee:00b3bf30:8"]]
+ 00b2fa68 ["INT_ADD", "register:40f0:8", ["const:b2fa68:8", "const:4:8"]]
+ 00b2fa68 ["CALL", null, ["callee:00b3bf30:8"]]
- 00b2f9cc bytes 32310094
+ 00b2fa68 bytes 32310094
- 00b2f9e8 ["INT_ADD", "register:40f0:8", ["const:b2f9e8:8", "const:4:8"]]
- 00b2f9e8 ["CALL", null, ["callee:00b3bf30:8"]]
+ 00b2fa84 ["INT_ADD", "register:40f0:8", ["const:b2fa84:8", "const:4:8"]]
+ 00b2fa84 ["CALL", null, ["callee:00b3bf30:8"]]
- 00b2f9e8 bytes 2b310094
+ 00b2fa84 bytes 2b310094
~~~


<a id="compare-2558602a8d8f89e7bb28679a719b660b"></a>

### [`00b34700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34700.md) → [`00b3479c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b3479c.md) FUN_00b3479c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3471c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34700.md#insn-00b3471c) · [`00b34758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34700.md#insn-00b34758) · [`00b34768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34700.md#insn-00b34768)
- 新版 `00b347b8`（命令位置の公開資料なし） · `00b347f4`（命令位置の公開資料なし） · `00b34804`（命令位置の公開資料なし）

~~~diff
- 00b3471c ["INT_ADD", "register:40f0:8", ["const:b3471c:8", "const:4:8"]]
- 00b3471c ["CALL", null, ["callee:0046d4d0:8"]]
+ 00b347b8 ["INT_ADD", "register:40f0:8", ["const:b347b8:8", "const:4:8"]]
+ 00b347b8 ["CALL", null, ["callee:0046d4d0:8"]]
- 00b3471c bytes 5de3e497
+ 00b347b8 bytes 46e3e497
- 00b34758 ["INT_ADD", "register:40f0:8", ["const:b34758:8", "const:4:8"]]
- 00b34758 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b347f4 ["INT_ADD", "register:40f0:8", ["const:b347f4:8", "const:4:8"]]
+ 00b347f4 ["CALL", null, ["callee:00c57f80:8"]]
- 00b34758 bytes d68d0494
+ 00b347f4 bytes e38d0494
- 00b34768 ["INT_ADD", "register:40f0:8", ["const:b34768:8", "const:4:8"]]
- 00b34768 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b34804 ["INT_ADD", "register:40f0:8", ["const:b34804:8", "const:4:8"]]
+ 00b34804 ["CALL", null, ["callee:00c57f80:8"]]
- 00b34768 bytes d28d0494
+ 00b34804 bytes df8d0494
~~~


<a id="compare-40ff3a9a7cc51d1e3d19299b11646cb7"></a>

### [`00b34798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34798.md) → [`00b34834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b34834.md) FUN_00b34834

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b34280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34280.md) [`00b369f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b369f4.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`00b3431c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b3431c.md) [`00b36a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b36/00b36a90.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b34804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34798.md#insn-00b34804) · [`00b34814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34798.md#insn-00b34814) · [`00b34834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34798.md#insn-00b34834)
- 新版 `00b348a0`（命令位置の公開資料なし） · `00b348b0`（命令位置の公開資料なし） · `00b348d0`（命令位置の公開資料なし）

~~~diff
- 00b34804 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b34804 ["INT_ADD", "register:40f0:8", ["const:b34804:8", "const:4:8"]]
- 00b34804 ["CALLIND", null, ["register:0:8"]]
+ 00b348a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b348a0 ["INT_ADD", "register:40f0:8", ["const:b348a0:8", "const:4:8"]]
+ 00b348a0 ["CALLIND", null, ["register:0:8"]]
- 00b34804 bytes 00013fd6
+ 00b348a0 bytes 00013fd6
- 00b34814 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b34814 ["INT_ADD", "register:40f0:8", ["const:b34814:8", "const:4:8"]]
- 00b34814 ["CALLIND", null, ["register:0:8"]]
+ 00b348b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b348b0 ["INT_ADD", "register:40f0:8", ["const:b348b0:8", "const:4:8"]]
+ 00b348b0 ["CALLIND", null, ["register:0:8"]]
- 00b34814 bytes 00013fd6
+ 00b348b0 bytes 00013fd6
- 00b34834 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b34834 ["INT_ADD", "register:40f0:8", ["const:b34834:8", "const:4:8"]]
- 00b34834 ["CALLIND", null, ["register:0:8"]]
+ 00b348d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b348d0 ["INT_ADD", "register:40f0:8", ["const:b348d0:8", "const:4:8"]]
+ 00b348d0 ["CALLIND", null, ["register:0:8"]]
- 00b34834 bytes 00013fd6
+ 00b348d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19ca1d86005e22656abe29c05055fd59"></a>

### [`00b34900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34900.md) → [`00b3499c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b3499c.md) FUN_00b3499c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b34348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34348.md) [`00b36abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b36abc.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`00b343e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b343e4.md) [`00b36b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b36/00b36b58.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3496c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34900.md#insn-00b3496c) · [`00b3497c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34900.md#insn-00b3497c) · [`00b3499c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34900.md#insn-00b3499c)
- 新版 `00b34a08`（命令位置の公開資料なし） · `00b34a18`（命令位置の公開資料なし） · `00b34a38`（命令位置の公開資料なし）

~~~diff
- 00b3496c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b3496c ["INT_ADD", "register:40f0:8", ["const:b3496c:8", "const:4:8"]]
- 00b3496c ["CALLIND", null, ["register:0:8"]]
+ 00b34a08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b34a08 ["INT_ADD", "register:40f0:8", ["const:b34a08:8", "const:4:8"]]
+ 00b34a08 ["CALLIND", null, ["register:0:8"]]
- 00b3496c bytes 00013fd6
+ 00b34a08 bytes 00013fd6
- 00b3497c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b3497c ["INT_ADD", "register:40f0:8", ["const:b3497c:8", "const:4:8"]]
- 00b3497c ["CALLIND", null, ["register:0:8"]]
+ 00b34a18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b34a18 ["INT_ADD", "register:40f0:8", ["const:b34a18:8", "const:4:8"]]
+ 00b34a18 ["CALLIND", null, ["register:0:8"]]
- 00b3497c bytes 00013fd6
+ 00b34a18 bytes 00013fd6
- 00b3499c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b3499c ["INT_ADD", "register:40f0:8", ["const:b3499c:8", "const:4:8"]]
- 00b3499c ["CALLIND", null, ["register:0:8"]]
+ 00b34a38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b34a38 ["INT_ADD", "register:40f0:8", ["const:b34a38:8", "const:4:8"]]
+ 00b34a38 ["CALLIND", null, ["register:0:8"]]
- 00b3499c bytes 00013fd6
+ 00b34a38 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d9eafe8d0ef2c3021e4d854e107077e"></a>

### [`00b34a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34a68.md) → [`00b34b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b34b04.md) FUN_00b34b04

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b34410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34410.md) · 呼出先 9件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00b344ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b344ac.md) · 呼出先 9件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b34b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34a68.md#insn-00b34b08) · [`00b34b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34a68.md#insn-00b34b2c) · [`00b34b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34a68.md#insn-00b34b70)
- 新版 `00b34ba4`（命令位置の公開資料なし） · `00b34bc8`（命令位置の公開資料なし） · `00b34c0c`（命令位置の公開資料なし）

~~~diff
- 00b34b08 ["INT_ADD", "register:40f0:8", ["const:b34b08:8", "const:4:8"]]
- 00b34b08 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b34ba4 ["INT_ADD", "register:40f0:8", ["const:b34ba4:8", "const:4:8"]]
+ 00b34ba4 ["CALL", null, ["callee:00c57f60:8"]]
- 00b34b08 bytes e28c0494
+ 00b34ba4 bytes ef8c0494
- 00b34b2c ["INT_ADD", "register:40f0:8", ["const:b34b2c:8", "const:4:8"]]
- 00b34b2c ["CALL", null, ["callee:00c580b0:8"]]
+ 00b34bc8 ["INT_ADD", "register:40f0:8", ["const:b34bc8:8", "const:4:8"]]
+ 00b34bc8 ["CALL", null, ["callee:00c580b0:8"]]
- 00b34b2c bytes 2d8d0494
+ 00b34bc8 bytes 3a8d0494
- 00b34b70 ["INT_ADD", "register:40f0:8", ["const:b34b70:8", "const:4:8"]]
- 00b34b70 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b34c0c ["INT_ADD", "register:40f0:8", ["const:b34c0c:8", "const:4:8"]]
+ 00b34c0c ["CALL", null, ["callee:00c57f60:8"]]
- 00b34b70 bytes c88c0494
+ 00b34c0c bytes d58c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e3b1a4c826976315956aa01b050e464"></a>

### [`00b34c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34c64.md) → [`00b34d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b34d00.md) FUN_00b34d00

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b34410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34410.md) · 呼出先 9件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00b344ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b344ac.md) · 呼出先 9件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b34d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34c64.md#insn-00b34d04) · [`00b34d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34c64.md#insn-00b34d28) · [`00b34d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34c64.md#insn-00b34d6c)
- 新版 `00b34da0`（命令位置の公開資料なし） · `00b34dc4`（命令位置の公開資料なし） · `00b34e08`（命令位置の公開資料なし）

~~~diff
- 00b34d04 ["INT_ADD", "register:40f0:8", ["const:b34d04:8", "const:4:8"]]
- 00b34d04 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b34da0 ["INT_ADD", "register:40f0:8", ["const:b34da0:8", "const:4:8"]]
+ 00b34da0 ["CALL", null, ["callee:00c57f60:8"]]
- 00b34d04 bytes 638c0494
+ 00b34da0 bytes 708c0494
- 00b34d28 ["INT_ADD", "register:40f0:8", ["const:b34d28:8", "const:4:8"]]
- 00b34d28 ["CALL", null, ["callee:00c580b0:8"]]
+ 00b34dc4 ["INT_ADD", "register:40f0:8", ["const:b34dc4:8", "const:4:8"]]
+ 00b34dc4 ["CALL", null, ["callee:00c580b0:8"]]
- 00b34d28 bytes ae8c0494
+ 00b34dc4 bytes bb8c0494
- 00b34d6c ["INT_ADD", "register:40f0:8", ["const:b34d6c:8", "const:4:8"]]
- 00b34d6c ["CALL", null, ["callee:00c57f60:8"]]
+ 00b34e08 ["INT_ADD", "register:40f0:8", ["const:b34e08:8", "const:4:8"]]
+ 00b34e08 ["CALL", null, ["callee:00c57f60:8"]]
- 00b34d6c bytes 498c0494
+ 00b34e08 bytes 568c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79029bf78ea4cc3f0976ef3a86b10db6"></a>

### [`00b35e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35e78.md) → [`00b35f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35f14.md) FUN_00b35f14

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b35d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35d04.md) [`00b35e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35e78.md) · 呼出先 2件 [`00b35e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35e78.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`00b35da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35da0.md) [`00b35f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35f14.md) · 呼出先 2件 [`00b35f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35f14.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b35e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35e78.md#insn-00b35e94) · [`00b35ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35e78.md#insn-00b35ea0) · [`00b35ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35e78.md#insn-00b35ed4)
- 新版 `00b35f30`（命令位置の公開資料なし） · `00b35f3c`（命令位置の公開資料なし） · `00b35f70`（命令位置の公開資料なし）

~~~diff
- 00b35e94 ["INT_ADD", "register:40f0:8", ["const:b35e94:8", "const:4:8"]]
- 00b35e94 ["CALL", null, ["local:b0:8"]]
+ 00b35f30 ["INT_ADD", "register:40f0:8", ["const:b35f30:8", "const:4:8"]]
+ 00b35f30 ["CALL", null, ["local:b0:8"]]
- 00b35e94 bytes f9ffff97
+ 00b35f30 bytes f9ffff97
- 00b35ea0 ["INT_ADD", "register:40f0:8", ["const:b35ea0:8", "const:4:8"]]
- 00b35ea0 ["CALL", null, ["local:b0:8"]]
+ 00b35f3c ["INT_ADD", "register:40f0:8", ["const:b35f3c:8", "const:4:8"]]
+ 00b35f3c ["CALL", null, ["local:b0:8"]]
- 00b35ea0 bytes f6ffff97
+ 00b35f3c bytes f6ffff97
- 00b35ed4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b35ed4 ["INT_ADD", "register:40f0:8", ["const:b35ed4:8", "const:4:8"]]
- 00b35ed4 ["CALLIND", null, ["register:0:8"]]
+ 00b35f70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b35f70 ["INT_ADD", "register:40f0:8", ["const:b35f70:8", "const:4:8"]]
+ 00b35f70 ["CALLIND", null, ["register:0:8"]]
- 00b35ed4 bytes 00013fd6
+ 00b35f70 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6444fd0b5c00418b3f694827967bb753"></a>

### [`00b372f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b372f8.md) → [`00b37394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b37/00b37394.md) FUN_00b37394

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b38e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b38/00b38e88.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00b38f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b38/00b38f24.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b37334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b372f8.md#insn-00b37334) · [`00b37364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b372f8.md#insn-00b37364) · [`00b37394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b372f8.md#insn-00b37394)
- 新版 `00b373d0`（命令位置の公開資料なし） · `00b37400`（命令位置の公開資料なし） · `00b37430`（命令位置の公開資料なし）

~~~diff
- 00b37334 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b37334 ["INT_ADD", "register:40f0:8", ["const:b37334:8", "const:4:8"]]
- 00b37334 ["CALLIND", null, ["register:0:8"]]
+ 00b373d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b373d0 ["INT_ADD", "register:40f0:8", ["const:b373d0:8", "const:4:8"]]
+ 00b373d0 ["CALLIND", null, ["register:0:8"]]
- 00b37334 bytes 00013fd6
+ 00b373d0 bytes 00013fd6
- 00b37364 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b37364 ["INT_ADD", "register:40f0:8", ["const:b37364:8", "const:4:8"]]
- 00b37364 ["CALLIND", null, ["register:0:8"]]
+ 00b37400 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b37400 ["INT_ADD", "register:40f0:8", ["const:b37400:8", "const:4:8"]]
+ 00b37400 ["CALLIND", null, ["register:0:8"]]
- 00b37364 bytes 00013fd6
+ 00b37400 bytes 00013fd6
- 00b37394 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b37394 ["INT_ADD", "register:40f0:8", ["const:b37394:8", "const:4:8"]]
- 00b37394 ["CALLIND", null, ["register:0:8"]]
+ 00b37430 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b37430 ["INT_ADD", "register:40f0:8", ["const:b37430:8", "const:4:8"]]
+ 00b37430 ["CALLIND", null, ["register:0:8"]]
- 00b37394 bytes 00013fd6
+ 00b37430 bytes 00013fd6
~~~


<a id="compare-83147957698a9aeff9bade0f56d35e09"></a>

### [`00b39cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b39/00b39cfc.md) → [`00b39d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b39/00b39d98.md) FUN_00b39d98

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b39964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b39/00b39964.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00b39a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b39/00b39a00.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b39d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b39/00b39cfc.md#insn-00b39d44) · [`00b39d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b39/00b39cfc.md#insn-00b39d84) · [`00b39dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b39/00b39cfc.md#insn-00b39dbc)
- 新版 `00b39de0`（命令位置の公開資料なし） · `00b39e20`（命令位置の公開資料なし） · `00b39e58`（命令位置の公開資料なし）

~~~diff
- 00b39d44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b39d44 ["INT_ADD", "register:40f0:8", ["const:b39d44:8", "const:4:8"]]
- 00b39d44 ["CALLIND", null, ["register:0:8"]]
+ 00b39de0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b39de0 ["INT_ADD", "register:40f0:8", ["const:b39de0:8", "const:4:8"]]
+ 00b39de0 ["CALLIND", null, ["register:0:8"]]
- 00b39d44 bytes 00013fd6
+ 00b39de0 bytes 00013fd6
- 00b39d84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b39d84 ["INT_ADD", "register:40f0:8", ["const:b39d84:8", "const:4:8"]]
- 00b39d84 ["CALLIND", null, ["register:0:8"]]
+ 00b39e20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b39e20 ["INT_ADD", "register:40f0:8", ["const:b39e20:8", "const:4:8"]]
+ 00b39e20 ["CALLIND", null, ["register:0:8"]]
- 00b39d84 bytes 00013fd6
+ 00b39e20 bytes 00013fd6
- 00b39dbc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b39dbc ["INT_ADD", "register:40f0:8", ["const:b39dbc:8", "const:4:8"]]
- 00b39dbc ["CALLIND", null, ["register:0:8"]]
+ 00b39e58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b39e58 ["INT_ADD", "register:40f0:8", ["const:b39e58:8", "const:4:8"]]
+ 00b39e58 ["CALLIND", null, ["register:0:8"]]
- 00b39dbc bytes 00013fd6
+ 00b39e58 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-102be877ce665bd8a5e3ca6c98d66316"></a>

### [`00b3b3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3b3d0.md) → [`00b3b46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b46c.md) FUN_00b3b46c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b39f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b39/00b39f54.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00b3b508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3b508.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00b39ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b39/00b39ff0.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00b3b5a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b5a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3b404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3b3d0.md#insn-00b3b404) · [`00b3b424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3b3d0.md#insn-00b3b424) · [`00b3b460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3b3d0.md#insn-00b3b460)
- 新版 `00b3b4a0`（命令位置の公開資料なし） · `00b3b4c0`（命令位置の公開資料なし） · `00b3b4fc`（命令位置の公開資料なし）

~~~diff
- 00b3b404 ["INT_ADD", "register:40f0:8", ["const:b3b404:8", "const:4:8"]]
- 00b3b404 ["CALL", null, ["callee:00b3b5a4:8"]]
+ 00b3b4a0 ["INT_ADD", "register:40f0:8", ["const:b3b4a0:8", "const:4:8"]]
+ 00b3b4a0 ["CALL", null, ["callee:00b3b5a4:8"]]
- 00b3b404 bytes 41000094
+ 00b3b4a0 bytes 41000094
- 00b3b424 ["INT_ADD", "register:40f0:8", ["const:b3b424:8", "const:4:8"]]
- 00b3b424 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b3b4c0 ["INT_ADD", "register:40f0:8", ["const:b3b4c0:8", "const:4:8"]]
+ 00b3b4c0 ["CALL", null, ["callee:00c57f60:8"]]
- 00b3b424 bytes 9b720494
+ 00b3b4c0 bytes a8720494
- 00b3b460 ["INT_ADD", "register:40f0:8", ["const:b3b460:8", "const:4:8"]]
- 00b3b460 ["CALL", null, ["callee:0043bb60:8"]]
+ 00b3b4fc ["INT_ADD", "register:40f0:8", ["const:b3b4fc:8", "const:4:8"]]
+ 00b3b4fc ["CALL", null, ["callee:0043bb60:8"]]
- 00b3b460 bytes b001e497
+ 00b3b4fc bytes 9901e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-912192f2449b33804dca4c041266fc76"></a>

### [`00b3be68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be68.md) → [`00b3bf04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf04.md) FUN_00b3bf04

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) [`00846508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/00846508.md) · 呼出先 1件 [`005e8198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e8/005e8198.md)
- 新版 呼出元 2件 [`0083f8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f8dc.md) [`00846560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846560.md) · 呼出先 1件 [`005e81d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e8/005e81d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3be7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be68.md#insn-00b3be7c)
- 新版 `00b3bf18`（命令位置の公開資料なし）

~~~diff
- 00b3be7c ["INT_ADD", "register:40f0:8", ["const:b3be7c:8", "const:4:8"]]
- 00b3be7c ["CALL", null, ["callee:005e81d8:8"]]
+ 00b3bf18 ["INT_ADD", "register:40f0:8", ["const:b3bf18:8", "const:4:8"]]
+ 00b3bf18 ["CALL", null, ["callee:005e81d8:8"]]
- 00b3be7c bytes c7b0ea97
+ 00b3bf18 bytes b0b0ea97
~~~


<a id="compare-2839cd0c517818ee397eca7912259e3f"></a>

### [`00b3fea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3fea4.md) → [`00b3ff40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3ff40.md) FUN_00b3ff40

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b403ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b403ac.md) · 呼出先 2件 [`00c5a940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a940.md) [`00c5ac60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac60.md)
- 新版 呼出元 1件 [`00b40448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40448.md) · 呼出先 2件 [`00c5aa10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aa10.md) [`00c5ad30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3feb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3fea4.md#insn-00b3feb4)
- 新版 `00b3ff50`（命令位置の公開資料なし）

~~~diff
- 00b3feb4 ["INT_ADD", "register:40f0:8", ["const:b3feb4:8", "const:4:8"]]
- 00b3feb4 ["CALL", null, ["callee:00c5ad30:8"]]
+ 00b3ff50 ["INT_ADD", "register:40f0:8", ["const:b3ff50:8", "const:4:8"]]
+ 00b3ff50 ["CALL", null, ["callee:00c5ad30:8"]]
- 00b3feb4 bytes 6b6b0494
+ 00b3ff50 bytes 786b0494
~~~


<a id="compare-a6887ff53db4b13735c2d3268ece889d"></a>

### [`00b44120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44120.md) → [`00b441bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b441bc.md) FUN_00b441bc

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00b44150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44150.md) [`00b4464c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b4464c.md) [`00b44678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44678.md) · 呼出先 2件 [`00b446c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b446c0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 3件 [`00b441ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b441ec.md) [`00b446e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b446e8.md) [`00b44714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44714.md) · 呼出先 2件 [`00b4475c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b4475c.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b44134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44120.md#insn-00b44134) · [`00b4414c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44120.md#insn-00b4414c)
- 新版 `00b441d0`（命令位置の公開資料なし） · `00b441e8`（命令位置の公開資料なし）

~~~diff
- 00b44134 ["INT_ADD", "register:40f0:8", ["const:b44134:8", "const:4:8"]]
- 00b44134 ["CALL", null, ["callee:00b4475c:8"]]
+ 00b441d0 ["INT_ADD", "register:40f0:8", ["const:b441d0:8", "const:4:8"]]
+ 00b441d0 ["CALL", null, ["callee:00b4475c:8"]]
- 00b44134 bytes 63010094
+ 00b441d0 bytes 63010094
- 00b4414c ["INT_ADD", "register:40f0:8", ["const:b4414c:8", "const:4:8"]]
- 00b4414c ["CALL", null, ["callee:00c5b210:8"]]
+ 00b441e8 ["INT_ADD", "register:40f0:8", ["const:b441e8:8", "const:4:8"]]
+ 00b441e8 ["CALL", null, ["callee:00c5b210:8"]]
- 00b4414c bytes fd5b0494
+ 00b441e8 bytes 0a5c0494
~~~


<a id="compare-c4efc423fee9a2bcdc471636419fc17b"></a>

### [`00b443cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b443cc.md) → [`00b44468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44468.md) _ZN8firebase10LogWarningEPKcz

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ade0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ade0.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b120.md)
- 新版 呼出元 1件 [`00c5aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aeb0.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b1f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b44448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b443cc.md#insn-00b44448) · [`00b4446c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b443cc.md#insn-00b4446c)
- 新版 `00b444e4`（命令位置の公開資料なし） · `00b44508`（命令位置の公開資料なし）

~~~diff
- 00b44448 ["INT_ADD", "register:40f0:8", ["const:b44448:8", "const:4:8"]]
- 00b44448 ["CALL", null, ["callee:00c5b1f0:8"]]
+ 00b444e4 ["INT_ADD", "register:40f0:8", ["const:b444e4:8", "const:4:8"]]
+ 00b444e4 ["CALL", null, ["callee:00c5b1f0:8"]]
- 00b44448 bytes 365b0494
+ 00b444e4 bytes 435b0494
- 00b4446c ["INT_ADD", "register:40f0:8", ["const:b4446c:8", "const:4:8"]]
- 00b4446c ["CALL", null, ["callee:00c57fb0:8"]]
+ 00b44508 ["INT_ADD", "register:40f0:8", ["const:b44508:8", "const:4:8"]]
+ 00b44508 ["CALL", null, ["callee:00c57fb0:8"]]
- 00b4446c bytes 9d4e0494
+ 00b44508 bytes aa4e0494
~~~


<a id="compare-d335eabe0b9f12ce7a0b741021bfc6e3"></a>

### [`00b517a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b517a0.md) → [`00b5183c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b5183c.md) FUN_00b5183c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b44d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44d44.md) [`00b4505c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b4505c.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b150.md)
- 新版 呼出元 2件 [`00b44de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44de0.md) [`00b450f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b450f8.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b51810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b517a0.md#insn-00b51810) · [`00b51834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b517a0.md#insn-00b51834)
- 新版 `00b518ac`（命令位置の公開資料なし） · `00b518d0`（命令位置の公開資料なし）

~~~diff
- 00b51810 ["INT_ADD", "register:40f0:8", ["const:b51810:8", "const:4:8"]]
- 00b51810 ["CALL", null, ["callee:00c5b220:8"]]
+ 00b518ac ["INT_ADD", "register:40f0:8", ["const:b518ac:8", "const:4:8"]]
+ 00b518ac ["CALL", null, ["callee:00c5b220:8"]]
- 00b51810 bytes 50260494
+ 00b518ac bytes 5d260494
- 00b51834 ["INT_ADD", "register:40f0:8", ["const:b51834:8", "const:4:8"]]
- 00b51834 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00b518d0 ["INT_ADD", "register:40f0:8", ["const:b518d0:8", "const:4:8"]]
+ 00b518d0 ["CALL", null, ["callee:00c57fb0:8"]]
- 00b51834 bytes ab190494
+ 00b518d0 bytes b8190494
~~~


<a id="compare-961928220be6ae6e6b3c8934371c174f"></a>

### [`00b54430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54430.md) → [`00b544cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b544cc.md) _ZN7_JNIEnv16CallDoubleMethodEP8_jobjectP10_jmethodIDz

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b230.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c5b300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b300.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b544a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54430.md#insn-00b544a4) · [`00b544c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54430.md#insn-00b544c8)
- 新版 `00b54540`（命令位置の公開資料なし） · `00b54564`（命令位置の公開資料なし）

~~~diff
- 00b544a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b544a4 ["INT_ADD", "register:40f0:8", ["const:b544a4:8", "const:4:8"]]
- 00b544a4 ["CALLIND", null, ["register:0:8"]]
+ 00b54540 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b54540 ["INT_ADD", "register:40f0:8", ["const:b54540:8", "const:4:8"]]
+ 00b54540 ["CALLIND", null, ["register:0:8"]]
- 00b544a4 bytes 00013fd6
+ 00b54540 bytes 00013fd6
- 00b544c8 ["INT_ADD", "register:40f0:8", ["const:b544c8:8", "const:4:8"]]
- 00b544c8 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00b54564 ["INT_ADD", "register:40f0:8", ["const:b54564:8", "const:4:8"]]
+ 00b54564 ["CALL", null, ["callee:00c57fb0:8"]]
- 00b544c8 bytes 860e0494
+ 00b54564 bytes 930e0494
~~~


<a id="compare-a9bde79a9523efeb11b92637f1f2fbc3"></a>

### [`00b5488c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b5488c.md) → [`00b54928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54928.md) _ZN8firebase4util22JBooleanArrayToVariantEP7_JNIEnvP14_jbooleanArray

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b4b0.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5b580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b580.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b548cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b5488c.md#insn-00b548cc) · [`00b548e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b5488c.md#insn-00b548e8) · [`00b548f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b5488c.md#insn-00b548f4)
- 新版 `00b54968`（命令位置の公開資料なし） · `00b54984`（命令位置の公開資料なし） · `00b54990`（命令位置の公開資料なし）

~~~diff
- 00b548cc ["COPY", "register:0:8", ["register:4048:8"]]
- 00b548cc ["INT_ADD", "register:40f0:8", ["const:b548cc:8", "const:4:8"]]
- 00b548cc ["CALLIND", null, ["register:0:8"]]
+ 00b54968 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b54968 ["INT_ADD", "register:40f0:8", ["const:b54968:8", "const:4:8"]]
+ 00b54968 ["CALLIND", null, ["register:0:8"]]
- 00b548cc bytes 20013fd6
+ 00b54968 bytes 20013fd6
- 00b548e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b548e8 ["INT_ADD", "register:40f0:8", ["const:b548e8:8", "const:4:8"]]
- 00b548e8 ["CALLIND", null, ["register:0:8"]]
+ 00b54984 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b54984 ["INT_ADD", "register:40f0:8", ["const:b54984:8", "const:4:8"]]
+ 00b54984 ["CALLIND", null, ["register:0:8"]]
- 00b548e8 bytes 00013fd6
+ 00b54984 bytes 00013fd6
- 00b548f4 ["INT_ADD", "register:40f0:8", ["const:b548f4:8", "const:4:8"]]
- 00b548f4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b54990 ["INT_ADD", "register:40f0:8", ["const:b54990:8", "const:4:8"]]
+ 00b54990 ["CALL", null, ["callee:00c57f60:8"]]
- 00b548f4 bytes 670d0494
+ 00b54990 bytes 740d0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f97ce712871a934f189cc821fe9a6df0"></a>

### [`00b579bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b579bc.md) → [`00b57a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57a58.md) _ZN8firebase4util16GetJNIEnvFromAppEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b340.md) · 呼出先 3件 [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b250.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md)
- 新版 呼出元 1件 [`00c5b410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b410.md) · 呼出先 3件 [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b320.md) [`00c5b330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b579c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b579bc.md#insn-00b579c4) · [`00b579cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b579bc.md#insn-00b579cc)
- 新版 `00b57a60`（命令位置の公開資料なし） · `00b57a68`（命令位置の公開資料なし）

~~~diff
- 00b579c4 ["INT_ADD", "register:40f0:8", ["const:b579c4:8", "const:4:8"]]
- 00b579c4 ["CALL", null, ["callee:00c5b320:8"]]
+ 00b57a60 ["INT_ADD", "register:40f0:8", ["const:b57a60:8", "const:4:8"]]
+ 00b57a60 ["CALL", null, ["callee:00c5b320:8"]]
- 00b579c4 bytes 230e0494
+ 00b57a60 bytes 300e0494
- 00b579cc ["INT_ADD", "register:40f0:8", ["const:b579cc:8", "const:4:8"]]
- 00b579cc ["CALL", null, ["callee:00c5b330:8"]]
+ 00b57a68 ["INT_ADD", "register:40f0:8", ["const:b57a68:8", "const:4:8"]]
+ 00b57a68 ["CALL", null, ["callee:00c5b330:8"]]
- 00b579cc bytes 250e0494
+ 00b57a68 bytes 320e0494
~~~


<a id="compare-bb8b3a3acdbf78653ea00e2c5bfea9c7"></a>

### [`00b5ac9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5ac9c.md) → [`00b5ad38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5ad38.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b7f0.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5b8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b8c0.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5ad1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5ac9c.md#insn-00b5ad1c) · [`00b5ad3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5ac9c.md#insn-00b5ad3c) · [`00b5ad58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5ac9c.md#insn-00b5ad58)
- 新版 `00b5adb8`（命令位置の公開資料なし） · `00b5add8`（命令位置の公開資料なし） · `00b5adf4`（命令位置の公開資料なし）

~~~diff
- 00b5ad1c ["INT_ADD", "register:40f0:8", ["const:b5ad1c:8", "const:4:8"]]
- 00b5ad1c ["CALL", null, ["callee:00c57f60:8"]]
+ 00b5adb8 ["INT_ADD", "register:40f0:8", ["const:b5adb8:8", "const:4:8"]]
+ 00b5adb8 ["CALL", null, ["callee:00c57f60:8"]]
- 00b5ad1c bytes 5df40394
+ 00b5adb8 bytes 6af40394
- 00b5ad3c ["INT_ADD", "register:40f0:8", ["const:b5ad3c:8", "const:4:8"]]
- 00b5ad3c ["CALL", null, ["callee:00c580d0:8"]]
+ 00b5add8 ["INT_ADD", "register:40f0:8", ["const:b5add8:8", "const:4:8"]]
+ 00b5add8 ["CALL", null, ["callee:00c580d0:8"]]
- 00b5ad3c bytes b1f40394
+ 00b5add8 bytes bef40394
- 00b5ad58 ["INT_ADD", "register:40f0:8", ["const:b5ad58:8", "const:4:8"]]
- 00b5ad58 ["CALL", null, ["callee:00c5b210:8"]]
+ 00b5adf4 ["INT_ADD", "register:40f0:8", ["const:b5adf4:8", "const:4:8"]]
+ 00b5adf4 ["CALL", null, ["callee:00c5b210:8"]]
- 00b5ad58 bytes fa000494
+ 00b5adf4 bytes 07010494
~~~


<a id="compare-1283e512890d09436a939b4b8869deba"></a>

### [`00b5ad5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5ad5c.md) → [`00b5adf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5adf8.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b800.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00c5b8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b8d0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5adf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5ad5c.md#insn-00b5adf8) · [`00b5ae38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5ad5c.md#insn-00b5ae38)
- 新版 `00b5ae94`（命令位置の公開資料なし） · `00b5aed4`（命令位置の公開資料なし）

~~~diff
- 00b5adf8 ["INT_ADD", "register:40f0:8", ["const:b5adf8:8", "const:4:8"]]
- 00b5adf8 ["CALL", null, ["callee:00c58120:8"]]
+ 00b5ae94 ["INT_ADD", "register:40f0:8", ["const:b5ae94:8", "const:4:8"]]
+ 00b5ae94 ["CALL", null, ["callee:00c58120:8"]]
- 00b5adf8 bytes 96f40394
+ 00b5ae94 bytes a3f40394
- 00b5ae38 ["INT_ADD", "register:40f0:8", ["const:b5ae38:8", "const:4:8"]]
- 00b5ae38 ["CALL", null, ["callee:00c58120:8"]]
+ 00b5aed4 ["INT_ADD", "register:40f0:8", ["const:b5aed4:8", "const:4:8"]]
+ 00b5aed4 ["CALL", null, ["callee:00c58120:8"]]
- 00b5ae38 bytes 86f40394
+ 00b5aed4 bytes 93f40394
~~~


<a id="compare-b71697edd61a77bca393d355f672671e"></a>

### [`00b5ae7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5ae7c.md) → [`00b5af18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5af18.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b810.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00c5b8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b8e0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5af14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5ae7c.md#insn-00b5af14) · [`00b5af5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5ae7c.md#insn-00b5af5c)
- 新版 `00b5afb0`（命令位置の公開資料なし） · `00b5aff8`（命令位置の公開資料なし）

~~~diff
- 00b5af14 ["INT_ADD", "register:40f0:8", ["const:b5af14:8", "const:4:8"]]
- 00b5af14 ["CALL", null, ["callee:00c58120:8"]]
+ 00b5afb0 ["INT_ADD", "register:40f0:8", ["const:b5afb0:8", "const:4:8"]]
+ 00b5afb0 ["CALL", null, ["callee:00c58120:8"]]
- 00b5af14 bytes 4ff40394
+ 00b5afb0 bytes 5cf40394
- 00b5af5c ["INT_ADD", "register:40f0:8", ["const:b5af5c:8", "const:4:8"]]
- 00b5af5c ["CALL", null, ["callee:00c58120:8"]]
+ 00b5aff8 ["INT_ADD", "register:40f0:8", ["const:b5aff8:8", "const:4:8"]]
+ 00b5aff8 ["CALL", null, ["callee:00c58120:8"]]
- 00b5af5c bytes 3df40394
+ 00b5aff8 bytes 4af40394
~~~


<a id="compare-e806e7beab1d75e5e5ff50937d3a29f8"></a>

### [`00b5af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5af90.md) → [`00b5b02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b02c.md) _ZNSt6__ndk16vectorIPN8firebase3AppENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b840.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5b910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b910.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5aff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5af90.md#insn-00b5aff4) · [`00b5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5af90.md#insn-00b5b000) · [`00b5b02c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5af90.md#insn-00b5b02c)
- 新版 `00b5b090`（命令位置の公開資料なし） · `00b5b09c`（命令位置の公開資料なし） · `00b5b0c8`（命令位置の公開資料なし）

~~~diff
- 00b5aff4 ["INT_ADD", "register:40f0:8", ["const:b5aff4:8", "const:4:8"]]
- 00b5aff4 ["CALL", null, ["callee:00c5b210:8"]]
+ 00b5b090 ["INT_ADD", "register:40f0:8", ["const:b5b090:8", "const:4:8"]]
+ 00b5b090 ["CALL", null, ["callee:00c5b210:8"]]
- 00b5aff4 bytes 53000494
+ 00b5b090 bytes 60000494
- 00b5b000 ["INT_ADD", "register:40f0:8", ["const:b5b000:8", "const:4:8"]]
- 00b5b000 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b5b09c ["INT_ADD", "register:40f0:8", ["const:b5b09c:8", "const:4:8"]]
+ 00b5b09c ["CALL", null, ["callee:00c57f60:8"]]
- 00b5b000 bytes a4f30394
+ 00b5b09c bytes b1f30394
- 00b5b02c ["INT_ADD", "register:40f0:8", ["const:b5b02c:8", "const:4:8"]]
- 00b5b02c ["CALL", null, ["callee:00c580d0:8"]]
+ 00b5b0c8 ["INT_ADD", "register:40f0:8", ["const:b5b0c8:8", "const:4:8"]]
+ 00b5b0c8 ["CALL", null, ["callee:00c580d0:8"]]
- 00b5b02c bytes f5f30394
+ 00b5b0c8 bytes 02f40394
~~~


<a id="compare-9cb44f5a843498de79e094d13b7d4446"></a>

### [`00b5b078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b078.md) → [`00b5b114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b114.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b820.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ac30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac30.md) [`00c5b160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b160.md) [`00c5b5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5d0.md)
- 新版 呼出元 1件 [`00c5b8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b8f0.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ad00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad00.md) [`00c5b230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b230.md) [`00c5b6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b078.md#insn-00b5b0f4) · [`00b5b108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b078.md#insn-00b5b108) · [`00b5b110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b078.md#insn-00b5b110)
- 新版 `00b5b190`（命令位置の公開資料なし） · `00b5b1a4`（命令位置の公開資料なし） · `00b5b1ac`（命令位置の公開資料なし）

~~~diff
- 00b5b0f4 ["INT_ADD", "register:40f0:8", ["const:b5b0f4:8", "const:4:8"]]
- 00b5b0f4 ["CALL", null, ["callee:00c5b6a0:8"]]
+ 00b5b190 ["INT_ADD", "register:40f0:8", ["const:b5b190:8", "const:4:8"]]
+ 00b5b190 ["CALL", null, ["callee:00c5b6a0:8"]]
- 00b5b0f4 bytes 37010494
+ 00b5b190 bytes 44010494
- 00b5b108 ["INT_ADD", "register:40f0:8", ["const:b5b108:8", "const:4:8"]]
- 00b5b108 ["CALL", null, ["callee:00c5b230:8"]]
+ 00b5b1a4 ["INT_ADD", "register:40f0:8", ["const:b5b1a4:8", "const:4:8"]]
+ 00b5b1a4 ["CALL", null, ["callee:00c5b230:8"]]
- 00b5b108 bytes 16000494
+ 00b5b1a4 bytes 23000494
- 00b5b110 ["INT_ADD", "register:40f0:8", ["const:b5b110:8", "const:4:8"]]
- 00b5b110 ["CALL", null, ["callee:00c5ad00:8"]]
+ 00b5b1ac ["INT_ADD", "register:40f0:8", ["const:b5b1ac:8", "const:4:8"]]
+ 00b5b1ac ["CALL", null, ["callee:00c5ad00:8"]]
- 00b5b110 bytes c8fe0394
+ 00b5b1ac bytes d5fe0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ee0936b201373bae0e6735154ae42df"></a>

### [`00b5b148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b148.md) → [`00b5b1e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b1e4.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b830.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ac30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac30.md) [`00c5b160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b160.md) [`00c5b830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b830.md)
- 新版 呼出元 1件 [`00c5b900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b900.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ad00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad00.md) [`00c5b230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b230.md) [`00c5b900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b900.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b148.md#insn-00b5b164) · [`00b5b170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b148.md#insn-00b5b170) · [`00b5b184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b148.md#insn-00b5b184)
- 新版 `00b5b200`（命令位置の公開資料なし） · `00b5b20c`（命令位置の公開資料なし） · `00b5b220`（命令位置の公開資料なし）

~~~diff
- 00b5b164 ["INT_ADD", "register:40f0:8", ["const:b5b164:8", "const:4:8"]]
- 00b5b164 ["CALL", null, ["callee:00c5b900:8"]]
+ 00b5b200 ["INT_ADD", "register:40f0:8", ["const:b5b200:8", "const:4:8"]]
+ 00b5b200 ["CALL", null, ["callee:00c5b900:8"]]
- 00b5b164 bytes b3010494
+ 00b5b200 bytes c0010494
- 00b5b170 ["INT_ADD", "register:40f0:8", ["const:b5b170:8", "const:4:8"]]
- 00b5b170 ["CALL", null, ["callee:00c5b900:8"]]
+ 00b5b20c ["INT_ADD", "register:40f0:8", ["const:b5b20c:8", "const:4:8"]]
+ 00b5b20c ["CALL", null, ["callee:00c5b900:8"]]
- 00b5b170 bytes b0010494
+ 00b5b20c bytes bd010494
- 00b5b184 ["INT_ADD", "register:40f0:8", ["const:b5b184:8", "const:4:8"]]
- 00b5b184 ["CALL", null, ["callee:00c5b230:8"]]
+ 00b5b220 ["INT_ADD", "register:40f0:8", ["const:b5b220:8", "const:4:8"]]
+ 00b5b220 ["CALL", null, ["callee:00c5b230:8"]]
- 00b5b184 bytes f7ff0394
+ 00b5b220 bytes 04000494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93ea42d1cc74353b1395b86f67139c7d"></a>

### [`00b5b214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b214.md) → [`00b5b2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b2b0.md) _ZNK8firebase10LoggerBase8LogDebugEPKcz

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b214.md#insn-00b5b28c) · [`00b5b2b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b214.md#insn-00b5b2b8) · [`00b5b2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b214.md#insn-00b5b2e0)
- 新版 `00b5b328`（命令位置の公開資料なし） · `00b5b354`（命令位置の公開資料なし） · `00b5b37c`（命令位置の公開資料なし）

~~~diff
- 00b5b28c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b28c ["INT_ADD", "register:40f0:8", ["const:b5b28c:8", "const:4:8"]]
- 00b5b28c ["CALLIND", null, ["register:0:8"]]
+ 00b5b328 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5b328 ["INT_ADD", "register:40f0:8", ["const:b5b328:8", "const:4:8"]]
+ 00b5b328 ["CALLIND", null, ["register:0:8"]]
- 00b5b28c bytes 00013fd6
+ 00b5b328 bytes 00013fd6
- 00b5b2b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b2b8 ["INT_ADD", "register:40f0:8", ["const:b5b2b8:8", "const:4:8"]]
- 00b5b2b8 ["CALLIND", null, ["register:0:8"]]
+ 00b5b354 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5b354 ["INT_ADD", "register:40f0:8", ["const:b5b354:8", "const:4:8"]]
+ 00b5b354 ["CALLIND", null, ["register:0:8"]]
- 00b5b2b8 bytes 00013fd6
+ 00b5b354 bytes 00013fd6
- 00b5b2e0 ["INT_ADD", "register:40f0:8", ["const:b5b2e0:8", "const:4:8"]]
- 00b5b2e0 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00b5b37c ["INT_ADD", "register:40f0:8", ["const:b5b37c:8", "const:4:8"]]
+ 00b5b37c ["CALL", null, ["callee:00c57fb0:8"]]
- 00b5b2e0 bytes 00f30394
+ 00b5b37c bytes 0df30394
~~~


<a id="compare-9b0031676817d7eb77a5d2ae80876b32"></a>

### [`00b5b5ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b5ec.md) → [`00b5b688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b688.md) _ZNK8firebase10LoggerBase9LogAssertEPKcz

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b5ec.md#insn-00b5b664) · [`00b5b690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b5ec.md#insn-00b5b690) · [`00b5b6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b5ec.md#insn-00b5b6b8)
- 新版 `00b5b700`（命令位置の公開資料なし） · `00b5b72c`（命令位置の公開資料なし） · `00b5b754`（命令位置の公開資料なし）

~~~diff
- 00b5b664 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b664 ["INT_ADD", "register:40f0:8", ["const:b5b664:8", "const:4:8"]]
- 00b5b664 ["CALLIND", null, ["register:0:8"]]
+ 00b5b700 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5b700 ["INT_ADD", "register:40f0:8", ["const:b5b700:8", "const:4:8"]]
+ 00b5b700 ["CALLIND", null, ["register:0:8"]]
- 00b5b664 bytes 00013fd6
+ 00b5b700 bytes 00013fd6
- 00b5b690 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b690 ["INT_ADD", "register:40f0:8", ["const:b5b690:8", "const:4:8"]]
- 00b5b690 ["CALLIND", null, ["register:0:8"]]
+ 00b5b72c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5b72c ["INT_ADD", "register:40f0:8", ["const:b5b72c:8", "const:4:8"]]
+ 00b5b72c ["CALLIND", null, ["register:0:8"]]
- 00b5b690 bytes 00013fd6
+ 00b5b72c bytes 00013fd6
- 00b5b6b8 ["INT_ADD", "register:40f0:8", ["const:b5b6b8:8", "const:4:8"]]
- 00b5b6b8 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00b5b754 ["INT_ADD", "register:40f0:8", ["const:b5b754:8", "const:4:8"]]
+ 00b5b754 ["CALL", null, ["callee:00c57fb0:8"]]
- 00b5b6b8 bytes 0af20394
+ 00b5b754 bytes 17f20394
~~~


<a id="compare-c513366622bd49fbc9b0cafb8f47ae33"></a>

### [`00b5b6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b6bc.md) → [`00b5b758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b758.md) _ZNK8firebase10LoggerBase10LogMessageENS_8LogLevelEPKcz

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b73c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b6bc.md#insn-00b5b73c) · [`00b5b768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b6bc.md#insn-00b5b768) · [`00b5b794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b6bc.md#insn-00b5b794)
- 新版 `00b5b7d8`（命令位置の公開資料なし） · `00b5b804`（命令位置の公開資料なし） · `00b5b830`（命令位置の公開資料なし）

~~~diff
- 00b5b73c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b73c ["INT_ADD", "register:40f0:8", ["const:b5b73c:8", "const:4:8"]]
- 00b5b73c ["CALLIND", null, ["register:0:8"]]
+ 00b5b7d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5b7d8 ["INT_ADD", "register:40f0:8", ["const:b5b7d8:8", "const:4:8"]]
+ 00b5b7d8 ["CALLIND", null, ["register:0:8"]]
- 00b5b73c bytes 00013fd6
+ 00b5b7d8 bytes 00013fd6
- 00b5b768 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b768 ["INT_ADD", "register:40f0:8", ["const:b5b768:8", "const:4:8"]]
- 00b5b768 ["CALLIND", null, ["register:0:8"]]
+ 00b5b804 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5b804 ["INT_ADD", "register:40f0:8", ["const:b5b804:8", "const:4:8"]]
+ 00b5b804 ["CALLIND", null, ["register:0:8"]]
- 00b5b768 bytes 00013fd6
+ 00b5b804 bytes 00013fd6
- 00b5b794 ["INT_ADD", "register:40f0:8", ["const:b5b794:8", "const:4:8"]]
- 00b5b794 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00b5b830 ["INT_ADD", "register:40f0:8", ["const:b5b830:8", "const:4:8"]]
+ 00b5b830 ["CALL", null, ["callee:00c57fb0:8"]]
- 00b5b794 bytes d3f10394
+ 00b5b830 bytes e0f10394
~~~


<a id="compare-a971237126b0b7d80502b5ac9b75f6cd"></a>

### [`00b5b798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b798.md) → [`00b5b834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b834.md) _ZNK8firebase10LoggerBase11LogMessageVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b798.md#insn-00b5b7d4) · [`00b5b800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b798.md#insn-00b5b800) · [`00b5b828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b798.md#insn-00b5b828)
- 新版 `00b5b870`（命令位置の公開資料なし） · `00b5b89c`（命令位置の公開資料なし） · `00b5b8c4`（命令位置の公開資料なし）

~~~diff
- 00b5b7d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b7d4 ["INT_ADD", "register:40f0:8", ["const:b5b7d4:8", "const:4:8"]]
- 00b5b7d4 ["CALLIND", null, ["register:0:8"]]
+ 00b5b870 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5b870 ["INT_ADD", "register:40f0:8", ["const:b5b870:8", "const:4:8"]]
+ 00b5b870 ["CALLIND", null, ["register:0:8"]]
- 00b5b7d4 bytes 00013fd6
+ 00b5b870 bytes 00013fd6
- 00b5b800 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b800 ["INT_ADD", "register:40f0:8", ["const:b5b800:8", "const:4:8"]]
- 00b5b800 ["CALLIND", null, ["register:0:8"]]
+ 00b5b89c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5b89c ["INT_ADD", "register:40f0:8", ["const:b5b89c:8", "const:4:8"]]
+ 00b5b89c ["CALLIND", null, ["register:0:8"]]
- 00b5b800 bytes 00013fd6
+ 00b5b89c bytes 00013fd6
- 00b5b828 ["INT_ADD", "register:40f0:8", ["const:b5b828:8", "const:4:8"]]
- 00b5b828 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00b5b8c4 ["INT_ADD", "register:40f0:8", ["const:b5b8c4:8", "const:4:8"]]
+ 00b5b8c4 ["CALL", null, ["callee:00c57fb0:8"]]
- 00b5b828 bytes aef10394
+ 00b5b8c4 bytes bbf10394
~~~


<a id="compare-e2269212fb2b29cfb0ec2328e33bb411"></a>

### [`00b5b83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b83c.md) → [`00b5b8d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b8d8.md) _ZNK8firebase12SystemLogger15LogMessageImplVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b120.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b1f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b83c.md#insn-00b5b870) · [`00b5b894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b83c.md#insn-00b5b894)
- 新版 `00b5b90c`（命令位置の公開資料なし） · `00b5b930`（命令位置の公開資料なし）

~~~diff
- 00b5b870 ["INT_ADD", "register:40f0:8", ["const:b5b870:8", "const:4:8"]]
- 00b5b870 ["CALL", null, ["callee:00c5b1f0:8"]]
+ 00b5b90c ["INT_ADD", "register:40f0:8", ["const:b5b90c:8", "const:4:8"]]
+ 00b5b90c ["CALL", null, ["callee:00c5b1f0:8"]]
- 00b5b870 bytes 2cfe0394
+ 00b5b90c bytes 39fe0394
- 00b5b894 ["INT_ADD", "register:40f0:8", ["const:b5b894:8", "const:4:8"]]
- 00b5b894 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00b5b930 ["INT_ADD", "register:40f0:8", ["const:b5b930:8", "const:4:8"]]
+ 00b5b930 ["CALL", null, ["callee:00c57fb0:8"]]
- 00b5b894 bytes 93f10394
+ 00b5b930 bytes a0f10394
~~~


<a id="compare-66f6f0301b38772b7569d0d8c9fcad0a"></a>

### [`00b5b8ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b8ac.md) → [`00b5b948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b948.md) _ZNK8firebase6Logger15LogMessageImplVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b8ac.md#insn-00b5b8ec) · [`00b5b918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b8ac.md#insn-00b5b918) · [`00b5b940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b8ac.md#insn-00b5b940)
- 新版 `00b5b988`（命令位置の公開資料なし） · `00b5b9b4`（命令位置の公開資料なし） · `00b5b9dc`（命令位置の公開資料なし）

~~~diff
- 00b5b8ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b8ec ["INT_ADD", "register:40f0:8", ["const:b5b8ec:8", "const:4:8"]]
- 00b5b8ec ["CALLIND", null, ["register:0:8"]]
+ 00b5b988 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5b988 ["INT_ADD", "register:40f0:8", ["const:b5b988:8", "const:4:8"]]
+ 00b5b988 ["CALLIND", null, ["register:0:8"]]
- 00b5b8ec bytes 00013fd6
+ 00b5b988 bytes 00013fd6
- 00b5b918 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b918 ["INT_ADD", "register:40f0:8", ["const:b5b918:8", "const:4:8"]]
- 00b5b918 ["CALLIND", null, ["register:0:8"]]
+ 00b5b9b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5b9b4 ["INT_ADD", "register:40f0:8", ["const:b5b9b4:8", "const:4:8"]]
+ 00b5b9b4 ["CALLIND", null, ["register:0:8"]]
- 00b5b918 bytes 00013fd6
+ 00b5b9b4 bytes 00013fd6
- 00b5b940 ["INT_ADD", "register:40f0:8", ["const:b5b940:8", "const:4:8"]]
- 00b5b940 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00b5b9dc ["INT_ADD", "register:40f0:8", ["const:b5b9dc:8", "const:4:8"]]
+ 00b5b9dc ["CALL", null, ["callee:00c57fb0:8"]]
- 00b5b940 bytes 68f10394
+ 00b5b9dc bytes 75f10394
~~~


<a id="compare-9bc17f07f8d7c9608fc6b407177988ce"></a>

### [`00b5ba2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5ba2c.md) → [`00b5bac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bac8.md) _ZN8firebase8callback18CallbackDispatcher14FlushCallbacksEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bb20.md) · 呼出先 4件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 1件 [`00c5bbf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bbf0.md) · 呼出先 4件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5ba4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5ba2c.md#insn-00b5ba4c) · [`00b5ba64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5ba2c.md#insn-00b5ba64) · [`00b5baa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5ba2c.md#insn-00b5baa8)
- 新版 `00b5bae8`（命令位置の公開資料なし） · `00b5bb00`（命令位置の公開資料なし） · `00b5bb44`（命令位置の公開資料なし）

~~~diff
- 00b5ba4c ["INT_ADD", "register:40f0:8", ["const:b5ba4c:8", "const:4:8"]]
- 00b5ba4c ["CALL", null, ["callee:00c5aad0:8"]]
+ 00b5bae8 ["INT_ADD", "register:40f0:8", ["const:b5bae8:8", "const:4:8"]]
+ 00b5bae8 ["CALL", null, ["callee:00c5aad0:8"]]
- 00b5ba4c bytes edfb0394
+ 00b5bae8 bytes fafb0394
- 00b5ba64 ["INT_ADD", "register:40f0:8", ["const:b5ba64:8", "const:4:8"]]
- 00b5ba64 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b5bb00 ["INT_ADD", "register:40f0:8", ["const:b5bb00:8", "const:4:8"]]
+ 00b5bb00 ["CALL", null, ["callee:00c57f80:8"]]
- 00b5ba64 bytes 13f10394
+ 00b5bb00 bytes 20f10394
- 00b5baa8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5baa8 ["INT_ADD", "register:40f0:8", ["const:b5baa8:8", "const:4:8"]]
- 00b5baa8 ["CALLIND", null, ["register:0:8"]]
+ 00b5bb44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5bb44 ["INT_ADD", "register:40f0:8", ["const:b5bb44:8", "const:4:8"]]
+ 00b5bb44 ["CALLIND", null, ["register:0:8"]]
- 00b5baa8 bytes 00013fd6
+ 00b5bb44 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a47710160bf815126c560ade5f3792cd"></a>

### [`00b5c124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c124.md) → [`00b5c1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c1c0.md) _ZN8firebase8callback18CallbackDispatcher17DispatchCallbacksEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5bb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bb30.md) · 呼出先 5件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5bb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bb00.md)
- 新版 呼出元 1件 [`00c5bc00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bc00.md) · 呼出先 5件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5bbd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bbd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5c148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c124.md#insn-00b5c148) · [`00b5c1cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c124.md#insn-00b5c1cc) · [`00b5c1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c124.md#insn-00b5c1d4)
- 新版 `00b5c1e4`（命令位置の公開資料なし） · `00b5c268`（命令位置の公開資料なし） · `00b5c270`（命令位置の公開資料なし）

~~~diff
- 00b5c148 ["INT_ADD", "register:40f0:8", ["const:b5c148:8", "const:4:8"]]
- 00b5c148 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00b5c1e4 ["INT_ADD", "register:40f0:8", ["const:b5c1e4:8", "const:4:8"]]
+ 00b5c1e4 ["CALL", null, ["callee:00c5aad0:8"]]
- 00b5c148 bytes 2efa0394
+ 00b5c1e4 bytes 3bfa0394
- 00b5c1cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5c1cc ["INT_ADD", "register:40f0:8", ["const:b5c1cc:8", "const:4:8"]]
- 00b5c1cc ["CALLIND", null, ["register:0:8"]]
+ 00b5c268 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5c268 ["INT_ADD", "register:40f0:8", ["const:b5c268:8", "const:4:8"]]
+ 00b5c268 ["CALLIND", null, ["register:0:8"]]
- 00b5c1cc bytes 00013fd6
+ 00b5c268 bytes 00013fd6
- 00b5c1d4 ["INT_ADD", "register:40f0:8", ["const:b5c1d4:8", "const:4:8"]]
- 00b5c1d4 ["CALL", null, ["callee:00c57f50:8"]]
+ 00b5c270 ["INT_ADD", "register:40f0:8", ["const:b5c270:8", "const:4:8"]]
+ 00b5c270 ["CALL", null, ["callee:00c57f50:8"]]
- 00b5c1d4 bytes 2bef0394
+ 00b5c270 bytes 38ef0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-865817368083f95d494a8cf28049fd56"></a>

### [`00b5dd1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5dd1c.md) → [`00b5ddb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5ddb8.md) _ZNK8firebase4Path14FrontDirectoryEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5bbf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bbf0.md) [`00c5bc00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bc00.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5bcc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bcc0.md) [`00c5bcd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bcd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5dd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5dd1c.md#insn-00b5dd54) · [`00b5dd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5dd1c.md#insn-00b5dd60) · [`00b5dd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5dd1c.md#insn-00b5dd9c)
- 新版 `00b5ddf0`（命令位置の公開資料なし） · `00b5ddfc`（命令位置の公開資料なし） · `00b5de38`（命令位置の公開資料なし）

~~~diff
- 00b5dd54 ["INT_ADD", "register:40f0:8", ["const:b5dd54:8", "const:4:8"]]
- 00b5dd54 ["CALL", null, ["callee:00c5bcd0:8"]]
+ 00b5ddf0 ["INT_ADD", "register:40f0:8", ["const:b5ddf0:8", "const:4:8"]]
+ 00b5ddf0 ["CALL", null, ["callee:00c5bcd0:8"]]
- 00b5dd54 bytes abf70394
+ 00b5ddf0 bytes b8f70394
- 00b5dd60 ["INT_ADD", "register:40f0:8", ["const:b5dd60:8", "const:4:8"]]
- 00b5dd60 ["CALL", null, ["callee:00c5bcc0:8"]]
+ 00b5ddfc ["INT_ADD", "register:40f0:8", ["const:b5ddfc:8", "const:4:8"]]
+ 00b5ddfc ["CALL", null, ["callee:00c5bcc0:8"]]
- 00b5dd60 bytes a4f70394
+ 00b5ddfc bytes b1f70394
- 00b5dd9c ["INT_ADD", "register:40f0:8", ["const:b5dd9c:8", "const:4:8"]]
- 00b5dd9c ["CALL", null, ["callee:00c57f80:8"]]
+ 00b5de38 ["INT_ADD", "register:40f0:8", ["const:b5de38:8", "const:4:8"]]
+ 00b5de38 ["CALL", null, ["callee:00c57f80:8"]]
- 00b5dd9c bytes 45e80394
+ 00b5de38 bytes 52e80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee714a2de09137ced4f241606ed76008"></a>

### [`00b5ddf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5ddf4.md) → [`00b5de90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5de90.md) _ZNK8firebase4Path17PopFrontDirectoryEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b5d458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d458.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5bbf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bbf0.md) [`00c5bc00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bc00.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b5d4f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d4f4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5bcc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bcc0.md) [`00c5bcd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bcd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5de2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5ddf4.md#insn-00b5de2c) · [`00b5de3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5ddf4.md#insn-00b5de3c) · [`00b5de48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5ddf4.md#insn-00b5de48)
- 新版 `00b5dec8`（命令位置の公開資料なし） · `00b5ded8`（命令位置の公開資料なし） · `00b5dee4`（命令位置の公開資料なし）

~~~diff
- 00b5de2c ["INT_ADD", "register:40f0:8", ["const:b5de2c:8", "const:4:8"]]
- 00b5de2c ["CALL", null, ["callee:00c5bcd0:8"]]
+ 00b5dec8 ["INT_ADD", "register:40f0:8", ["const:b5dec8:8", "const:4:8"]]
+ 00b5dec8 ["CALL", null, ["callee:00c5bcd0:8"]]
- 00b5de2c bytes 75f70394
+ 00b5dec8 bytes 82f70394
- 00b5de3c ["INT_ADD", "register:40f0:8", ["const:b5de3c:8", "const:4:8"]]
- 00b5de3c ["CALL", null, ["callee:00b5d4f4:8"]]
+ 00b5ded8 ["INT_ADD", "register:40f0:8", ["const:b5ded8:8", "const:4:8"]]
+ 00b5ded8 ["CALL", null, ["callee:00b5d4f4:8"]]
- 00b5de3c bytes 87fdff97
+ 00b5ded8 bytes 87fdff97
- 00b5de48 ["INT_ADD", "register:40f0:8", ["const:b5de48:8", "const:4:8"]]
- 00b5de48 ["CALL", null, ["callee:00c5bcc0:8"]]
+ 00b5dee4 ["INT_ADD", "register:40f0:8", ["const:b5dee4:8", "const:4:8"]]
+ 00b5dee4 ["CALL", null, ["callee:00c5bcc0:8"]]
- 00b5de48 bytes 6af70394
+ 00b5dee4 bytes 77f70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

