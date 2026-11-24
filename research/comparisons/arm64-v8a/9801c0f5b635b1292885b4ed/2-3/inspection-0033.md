# v16.0.1 → v16.0.2 · 要調査の変更候補 (33)

[一覧の目次](README.md)

<a id="compare-4cad789a7e910f5fec24fef662598fd0"></a>

### [`00a32d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32d94.md) → [`00a32de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a32/00a32de8.md) FUN_00a32de8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 1件 [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md)
- 新版 呼出元 2件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 1件 [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a32dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32d94.md#insn-00a32dbc)
- 新版 `00a32e10`（命令位置の公開資料なし）

~~~diff
- 00a32dbc ["INT_ADD", "register:40f0:8", ["const:a32dbc:8", "const:4:8"]]
- 00a32dbc ["CALL", null, ["callee:00802bb0:8"]]
+ 00a32e10 ["INT_ADD", "register:40f0:8", ["const:a32e10:8", "const:4:8"]]
+ 00a32e10 ["CALL", null, ["callee:00802bb0:8"]]
- 00a32dbc bytes 673ff797
+ 00a32e10 bytes 683ff797
~~~


<a id="compare-d5f1fafe27e4eae5d9885e50c7bc071c"></a>

### [`00a32e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32e08.md) → [`00a32e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a32/00a32e5c.md) FUN_00a32e5c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00611e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00611/00611e60.md) [`007efbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efbb0.md) [`00934078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934078.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 1件 [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md)
- 新版 呼出元 7件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00611ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00611/00611ea0.md) [`007efc08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007efc08.md) [`009340cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00934/009340cc.md) [`00a47f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47f54.md) · 呼出先 1件 [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a32e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32e08.md#insn-00a32e1c)
- 新版 `00a32e70`（命令位置の公開資料なし）

~~~diff
- 00a32e1c ["INT_ADD", "register:40f0:8", ["const:a32e1c:8", "const:4:8"]]
- 00a32e1c ["CALL", null, ["callee:00802bb0:8"]]
+ 00a32e70 ["INT_ADD", "register:40f0:8", ["const:a32e70:8", "const:4:8"]]
+ 00a32e70 ["CALL", null, ["callee:00802bb0:8"]]
- 00a32e1c bytes 4f3ff797
+ 00a32e70 bytes 503ff797
~~~


<a id="compare-5ebe037e58fddf3cd6bc79e7b02dac89"></a>

### [`00a32e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32e98.md) → [`00a32eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a32/00a32eec.md) FUN_00a32eec

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`007cb5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb5e0.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`007ef684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef684.md) [`00802d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d78.md) [`009d992c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d9/009d992c.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 8件 [`007cb638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cb/007cb638.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) [`007ef6dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007ef6dc.md) [`00802dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802dd0.md) [`009d9980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d9/009d9980.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a32f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32e98.md#insn-00a32f30) · [`00a32f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32e98.md#insn-00a32f64)
- 新版 `00a32f84`（命令位置の公開資料なし） · `00a32fb8`（命令位置の公開資料なし）

~~~diff
- 00a32f30 ["INT_ADD", "register:40f0:8", ["const:a32f30:8", "const:4:8"]]
- 00a32f30 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a32f84 ["INT_ADD", "register:40f0:8", ["const:a32f84:8", "const:4:8"]]
+ 00a32f84 ["CALL", null, ["callee:00c57f60:8"]]
- 00a32f30 bytes d8930894
+ 00a32f84 bytes f7930894
- 00a32f64 ["INT_ADD", "register:40f0:8", ["const:a32f64:8", "const:4:8"]]
- 00a32f64 ["CALL", null, ["callee:0043bbe4:8"]]
+ 00a32fb8 ["INT_ADD", "register:40f0:8", ["const:a32fb8:8", "const:4:8"]]
+ 00a32fb8 ["CALL", null, ["callee:0043bbe4:8"]]
- 00a32f64 bytes 1023e897
+ 00a32fb8 bytes 0b23e897
~~~


<a id="compare-41f226873f9474000671ed17486f1744"></a>

### [`00a333d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a333d4.md) → [`00a33428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a33/00a33428.md) FUN_00a33428

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 11件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00480118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480118.md) [`004801d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004801d8.md)
- 新版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 11件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00480158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480158.md) [`00480218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480218.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a33400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a333d4.md#insn-00a33400) · [`00a3340c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a333d4.md#insn-00a3340c) · [`00a33418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a333d4.md#insn-00a33418)
- 新版 `00a33454`（命令位置の公開資料なし） · `00a33460`（命令位置の公開資料なし） · `00a3346c`（命令位置の公開資料なし）

~~~diff
- 00a33400 ["INT_ADD", "register:40f0:8", ["const:a33400:8", "const:4:8"]]
- 00a33400 ["CALL", null, ["callee:00480218:8"]]
+ 00a33454 ["INT_ADD", "register:40f0:8", ["const:a33454:8", "const:4:8"]]
+ 00a33454 ["CALL", null, ["callee:00480218:8"]]
- 00a33400 bytes 7633e997
+ 00a33454 bytes 7133e997
- 00a3340c ["INT_ADD", "register:40f0:8", ["const:a3340c:8", "const:4:8"]]
- 00a3340c ["CALL", null, ["callee:00480784:8"]]
+ 00a33460 ["INT_ADD", "register:40f0:8", ["const:a33460:8", "const:4:8"]]
+ 00a33460 ["CALL", null, ["callee:00480784:8"]]
- 00a3340c bytes ce34e997
+ 00a33460 bytes c934e997
- 00a33418 ["INT_ADD", "register:40f0:8", ["const:a33418:8", "const:4:8"]]
- 00a33418 ["CALL", null, ["callee:00480338:8"]]
+ 00a3346c ["INT_ADD", "register:40f0:8", ["const:a3346c:8", "const:4:8"]]
+ 00a3346c ["CALL", null, ["callee:00480338:8"]]
- 00a33418 bytes b833e997
+ 00a3346c bytes b333e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95ad2269ce279359f5dd61e16b34f6e8"></a>

### [`00a3362c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a3362c.md) → [`00a33680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a33/00a33680.md) FUN_00a33680

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 9件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00480b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md) [`00480be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md) [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) [`00481098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481098.md)
- 新版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 9件 [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00480b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480b78.md) [`00480c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480c28.md) [`00480d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480d88.md) [`004810d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/004810d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3366c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a3362c.md#insn-00a3366c) · [`00a33678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a3362c.md#insn-00a33678) · [`00a33684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a3362c.md#insn-00a33684)
- 新版 `00a336c0`（命令位置の公開資料なし） · `00a336cc`（命令位置の公開資料なし） · `00a336d8`（命令位置の公開資料なし）

~~~diff
- 00a3366c ["INT_ADD", "register:40f0:8", ["const:a3366c:8", "const:4:8"]]
- 00a3366c ["CALL", null, ["callee:00480c28:8"]]
+ 00a336c0 ["INT_ADD", "register:40f0:8", ["const:a336c0:8", "const:4:8"]]
+ 00a336c0 ["CALL", null, ["callee:00480c28:8"]]
- 00a3366c bytes 5f35e997
+ 00a336c0 bytes 5a35e997
- 00a33678 ["INT_ADD", "register:40f0:8", ["const:a33678:8", "const:4:8"]]
- 00a33678 ["CALL", null, ["callee:004810d8:8"]]
+ 00a336cc ["INT_ADD", "register:40f0:8", ["const:a336cc:8", "const:4:8"]]
+ 00a336cc ["CALL", null, ["callee:004810d8:8"]]
- 00a33678 bytes 8836e997
+ 00a336cc bytes 8336e997
- 00a33684 ["INT_ADD", "register:40f0:8", ["const:a33684:8", "const:4:8"]]
- 00a33684 ["CALL", null, ["callee:00480d88:8"]]
+ 00a336d8 ["INT_ADD", "register:40f0:8", ["const:a336d8:8", "const:4:8"]]
+ 00a336d8 ["CALL", null, ["callee:00480d88:8"]]
- 00a33684 bytes b135e997
+ 00a336d8 bytes ac35e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-646c36c504ac6f7cf7e9876cc8295618"></a>

### [`00a33c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33c1c.md) → [`00a33c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a33/00a33c70.md) FUN_00a33c70

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 12件 [`0062c0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062c/0062c0c0.md) [`0069a504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069a/0069a504.md) [`00732cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732cf8.md) [`00745930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/00745930.md) [`007473e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/007473e0.md) · 呼出先 3件 [`00597778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597778.md) [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 12件 [`0062c100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0062c/0062c100.md) [`0069a55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069a/0069a55c.md) [`00732d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00732/00732d50.md) [`00745988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00745/00745988.md) [`00747438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/00747438.md) · 呼出先 3件 [`005977b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005977b8.md) [`00597acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597acc.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a33c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33c1c.md#insn-00a33c50) · [`00a33c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33c1c.md#insn-00a33c58) · [`00a33c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33c1c.md#insn-00a33c80)
- 新版 `00a33ca4`（命令位置の公開資料なし） · `00a33cac`（命令位置の公開資料なし） · `00a33cd4`（命令位置の公開資料なし）

~~~diff
- 00a33c50 ["INT_ADD", "register:40f0:8", ["const:a33c50:8", "const:4:8"]]
- 00a33c50 ["CALL", null, ["callee:005977b8:8"]]
+ 00a33ca4 ["INT_ADD", "register:40f0:8", ["const:a33ca4:8", "const:4:8"]]
+ 00a33ca4 ["CALL", null, ["callee:005977b8:8"]]
- 00a33c50 bytes ca8eed97
+ 00a33ca4 bytes c58eed97
- 00a33c58 ["INT_ADD", "register:40f0:8", ["const:a33c58:8", "const:4:8"]]
- 00a33c58 ["CALL", null, ["callee:00597acc:8"]]
+ 00a33cac ["INT_ADD", "register:40f0:8", ["const:a33cac:8", "const:4:8"]]
+ 00a33cac ["CALL", null, ["callee:00597acc:8"]]
- 00a33c58 bytes 8d8fed97
+ 00a33cac bytes 888fed97
- 00a33c80 ["INT_ADD", "register:40f0:8", ["const:a33c80:8", "const:4:8"]]
- 00a33c80 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00a33cd4 ["INT_ADD", "register:40f0:8", ["const:a33cd4:8", "const:4:8"]]
+ 00a33cd4 ["CALL", null, ["callee:00c57fb0:8"]]
- 00a33c80 bytes 98900894
+ 00a33cd4 bytes b7900894
~~~


<a id="compare-1fc40f0b40bd17a28479ad8b71b2b140"></a>

### [`00a33cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33cac.md) → [`00a33d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a33/00a33d00.md) FUN_00a33d00

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a33f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33f7c.md) · 呼出先 2件 [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00a38cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38cc4.md)
- 新版 呼出元 1件 [`00a33fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a33/00a33fd0.md) · 呼出先 2件 [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00a38d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a38d18.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a33ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33cac.md#insn-00a33ce0) · [`00a33cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33cac.md#insn-00a33cfc) · [`00a33d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33cac.md#insn-00a33d2c)
- 新版 `00a33d34`（命令位置の公開資料なし） · `00a33d50`（命令位置の公開資料なし） · `00a33d80`（命令位置の公開資料なし）

~~~diff
- 00a33ce0 ["INT_ADD", "register:40f0:8", ["const:a33ce0:8", "const:4:8"]]
- 00a33ce0 ["CALL", null, ["callee:0048797c:8"]]
+ 00a33d34 ["INT_ADD", "register:40f0:8", ["const:a33d34:8", "const:4:8"]]
+ 00a33d34 ["CALL", null, ["callee:0048797c:8"]]
- 00a33ce0 bytes 174fe997
+ 00a33d34 bytes 124fe997
- 00a33cfc ["INT_ADD", "register:40f0:8", ["const:a33cfc:8", "const:4:8"]]
- 00a33cfc ["CALL", null, ["callee:0048797c:8"]]
+ 00a33d50 ["INT_ADD", "register:40f0:8", ["const:a33d50:8", "const:4:8"]]
+ 00a33d50 ["CALL", null, ["callee:0048797c:8"]]
- 00a33cfc bytes 104fe997
+ 00a33d50 bytes 0b4fe997
- 00a33d2c ["INT_ADD", "register:40f0:8", ["const:a33d2c:8", "const:4:8"]]
- 00a33d2c ["CALL", null, ["callee:0048797c:8"]]
+ 00a33d80 ["INT_ADD", "register:40f0:8", ["const:a33d80:8", "const:4:8"]]
+ 00a33d80 ["CALL", null, ["callee:0048797c:8"]]
- 00a33d2c bytes 044fe997
+ 00a33d80 bytes ff4ee997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e04a8eae1a0b4e87e0bc8c343fe8777"></a>

### [`00a33f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33f7c.md) → [`00a33fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a33/00a33fd0.md) FUN_00a33fd0

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00a35594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a35594.md) [`00a3611c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a36/00a3611c.md) [`00a36b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a36/00a36b18.md) · 呼出先 4件 [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00a33cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33cac.md) [`00a38e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38e58.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`00a355e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a35/00a355e8.md) [`00a36170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a36/00a36170.md) [`00a36b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a36/00a36b6c.md) · 呼出先 4件 [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00a33d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a33/00a33d00.md) [`00a38eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a38eac.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a33fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33f7c.md#insn-00a33fa8) · [`00a34010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33f7c.md#insn-00a34010) · [`00a3403c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33f7c.md#insn-00a3403c)
- 新版 `00a33ffc`（命令位置の公開資料なし） · `00a34064`（命令位置の公開資料なし） · `00a34090`（命令位置の公開資料なし）

~~~diff
- 00a33fa8 ["INT_ADD", "register:40f0:8", ["const:a33fa8:8", "const:4:8"]]
- 00a33fa8 ["CALL", null, ["callee:0048797c:8"]]
+ 00a33ffc ["INT_ADD", "register:40f0:8", ["const:a33ffc:8", "const:4:8"]]
+ 00a33ffc ["CALL", null, ["callee:0048797c:8"]]
- 00a33fa8 bytes 654ee997
+ 00a33ffc bytes 604ee997
- 00a34010 ["INT_ADD", "register:40f0:8", ["const:a34010:8", "const:4:8"]]
- 00a34010 ["CALL", null, ["callee:0048797c:8"]]
+ 00a34064 ["INT_ADD", "register:40f0:8", ["const:a34064:8", "const:4:8"]]
+ 00a34064 ["CALL", null, ["callee:0048797c:8"]]
- 00a34010 bytes 4b4ee997
+ 00a34064 bytes 464ee997
- 00a3403c ["INT_ADD", "register:40f0:8", ["const:a3403c:8", "const:4:8"]]
- 00a3403c ["CALL", null, ["callee:0048797c:8"]]
+ 00a34090 ["INT_ADD", "register:40f0:8", ["const:a34090:8", "const:4:8"]]
+ 00a34090 ["CALL", null, ["callee:0048797c:8"]]
- 00a3403c bytes 404ee997
+ 00a34090 bytes 3b4ee997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6db015afb968f0cab41b0996a89701ee"></a>

### [`00a34694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a34/00a34694.md) → [`00a346e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a34/00a346e8.md) FUN_00a346e8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0086588c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/0086588c.md) · 呼出先 3件 [`00597778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597778.md) [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`008658e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/008658e4.md) · 呼出先 3件 [`005977b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005977b8.md) [`00597acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597acc.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a346d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a34/00a34694.md#insn-00a346d4) · [`00a346dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a34/00a34694.md#insn-00a346dc) · [`00a34708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a34/00a34694.md#insn-00a34708)
- 新版 `00a34728`（命令位置の公開資料なし） · `00a34730`（命令位置の公開資料なし） · `00a3475c`（命令位置の公開資料なし）

~~~diff
- 00a346d4 ["INT_ADD", "register:40f0:8", ["const:a346d4:8", "const:4:8"]]
- 00a346d4 ["CALL", null, ["callee:005977b8:8"]]
+ 00a34728 ["INT_ADD", "register:40f0:8", ["const:a34728:8", "const:4:8"]]
+ 00a34728 ["CALL", null, ["callee:005977b8:8"]]
- 00a346d4 bytes 298ced97
+ 00a34728 bytes 248ced97
- 00a346dc ["INT_ADD", "register:40f0:8", ["const:a346dc:8", "const:4:8"]]
- 00a346dc ["CALL", null, ["callee:00597acc:8"]]
+ 00a34730 ["INT_ADD", "register:40f0:8", ["const:a34730:8", "const:4:8"]]
+ 00a34730 ["CALL", null, ["callee:00597acc:8"]]
- 00a346dc bytes ec8ced97
+ 00a34730 bytes e78ced97
- 00a34708 ["INT_ADD", "register:40f0:8", ["const:a34708:8", "const:4:8"]]
- 00a34708 ["CALL", null, ["callee:005977b8:8"]]
+ 00a3475c ["INT_ADD", "register:40f0:8", ["const:a3475c:8", "const:4:8"]]
+ 00a3475c ["CALL", null, ["callee:005977b8:8"]]
- 00a34708 bytes 1c8ced97
+ 00a3475c bytes 178ced97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-082d81bfd3c8d15c3918d7fe29a44be1"></a>

### [`00a34750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a34/00a34750.md) → [`00a347a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a34/00a347a4.md) FUN_00a347a4

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) [`009d3420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3420.md) [`009d3930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3930.md) [`009d3af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3af4.md) · 呼出先 10件 [`005976e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005976e8.md) [`00597778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597778.md) [`00597a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a4c.md) [`00597a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a58.md) [`00597a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a64.md)
- 新版 呼出元 4件 [`009d0374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d0/009d0374.md) [`009d3474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d3/009d3474.md) [`009d3984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d3/009d3984.md) [`009d3b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d3/009d3b48.md) · 呼出先 10件 [`00597728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597728.md) [`005977b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005977b8.md) [`00597a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597a8c.md) [`00597a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597a98.md) [`00597aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597aa4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a34798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a34/00a34750.md#insn-00a34798) · [`00a347b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a34/00a34750.md#insn-00a347b4) · [`00a347bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a34/00a34750.md#insn-00a347bc)
- 新版 `00a347ec`（命令位置の公開資料なし） · `00a34808`（命令位置の公開資料なし） · `00a34810`（命令位置の公開資料なし）

~~~diff
- 00a34798 ["INT_ADD", "register:40f0:8", ["const:a34798:8", "const:4:8"]]
- 00a34798 ["CALL", null, ["callee:00597728:8"]]
+ 00a347ec ["INT_ADD", "register:40f0:8", ["const:a347ec:8", "const:4:8"]]
+ 00a347ec ["CALL", null, ["callee:00597728:8"]]
- 00a34798 bytes d48bed97
+ 00a347ec bytes cf8bed97
- 00a347b4 ["INT_ADD", "register:40f0:8", ["const:a347b4:8", "const:4:8"]]
- 00a347b4 ["CALL", null, ["callee:005977b8:8"]]
+ 00a34808 ["INT_ADD", "register:40f0:8", ["const:a34808:8", "const:4:8"]]
+ 00a34808 ["CALL", null, ["callee:005977b8:8"]]
- 00a347b4 bytes f18bed97
+ 00a34808 bytes ec8bed97
- 00a347bc ["INT_ADD", "register:40f0:8", ["const:a347bc:8", "const:4:8"]]
- 00a347bc ["CALL", null, ["callee:00597acc:8"]]
+ 00a34810 ["INT_ADD", "register:40f0:8", ["const:a34810:8", "const:4:8"]]
+ 00a34810 ["CALL", null, ["callee:00597acc:8"]]
- 00a347bc bytes b48ced97
+ 00a34810 bytes af8ced97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62aedab89190655c0d442f231d49fb63"></a>

### [`00a34e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a34/00a34e14.md) → [`00a34e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a34/00a34e68.md) FUN_00a34e68

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 10件 [`005976e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005976e8.md) [`00597778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597778.md) [`00597a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a4c.md) [`00597a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a58.md) [`00597a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a64.md)
- 新版 呼出元 1件 [`009d0374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d0/009d0374.md) · 呼出先 10件 [`00597728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597728.md) [`005977b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005977b8.md) [`00597a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597a8c.md) [`00597a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597a98.md) [`00597aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597aa4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a34e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a34/00a34e14.md#insn-00a34e5c) · [`00a34e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a34/00a34e14.md#insn-00a34e78) · [`00a34e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a34/00a34e14.md#insn-00a34e80)
- 新版 `00a34eb0`（命令位置の公開資料なし） · `00a34ecc`（命令位置の公開資料なし） · `00a34ed4`（命令位置の公開資料なし）

~~~diff
- 00a34e5c ["INT_ADD", "register:40f0:8", ["const:a34e5c:8", "const:4:8"]]
- 00a34e5c ["CALL", null, ["callee:00597728:8"]]
+ 00a34eb0 ["INT_ADD", "register:40f0:8", ["const:a34eb0:8", "const:4:8"]]
+ 00a34eb0 ["CALL", null, ["callee:00597728:8"]]
- 00a34e5c bytes 238aed97
+ 00a34eb0 bytes 1e8aed97
- 00a34e78 ["INT_ADD", "register:40f0:8", ["const:a34e78:8", "const:4:8"]]
- 00a34e78 ["CALL", null, ["callee:005977b8:8"]]
+ 00a34ecc ["INT_ADD", "register:40f0:8", ["const:a34ecc:8", "const:4:8"]]
+ 00a34ecc ["CALL", null, ["callee:005977b8:8"]]
- 00a34e78 bytes 408aed97
+ 00a34ecc bytes 3b8aed97
- 00a34e80 ["INT_ADD", "register:40f0:8", ["const:a34e80:8", "const:4:8"]]
- 00a34e80 ["CALL", null, ["callee:00597acc:8"]]
+ 00a34ed4 ["INT_ADD", "register:40f0:8", ["const:a34ed4:8", "const:4:8"]]
+ 00a34ed4 ["CALL", null, ["callee:00597acc:8"]]
- 00a34e80 bytes 038bed97
+ 00a34ed4 bytes fe8aed97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f7a8b956ebc9aaa46c8992248796aee"></a>

### [`00a35594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a35594.md) → [`00a355e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a35/00a355e8.md) FUN_00a355e8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a38108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38108.md) · 呼出先 6件 [`00470714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470714.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md) [`00a33f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33f7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00a3815c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a3815c.md) · 呼出先 6件 [`00470754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470754.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487aa4.md) [`00a33fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a33/00a33fd0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a355c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a35594.md#insn-00a355c0) · [`00a355d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a35594.md#insn-00a355d4) · [`00a355f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a35594.md#insn-00a355f4)
- 新版 `00a35614`（命令位置の公開資料なし） · `00a35628`（命令位置の公開資料なし） · `00a35648`（命令位置の公開資料なし）

~~~diff
- 00a355c0 ["INT_ADD", "register:40f0:8", ["const:a355c0:8", "const:4:8"]]
- 00a355c0 ["CALL", null, ["callee:00a33fd0:8"]]
+ 00a35614 ["INT_ADD", "register:40f0:8", ["const:a35614:8", "const:4:8"]]
+ 00a35614 ["CALL", null, ["callee:00a33fd0:8"]]
- 00a355c0 bytes 6ffaff97
+ 00a35614 bytes 6ffaff97
- 00a355d4 ["INT_ADD", "register:40f0:8", ["const:a355d4:8", "const:4:8"]]
- 00a355d4 ["CALL", null, ["callee:0048797c:8"]]
+ 00a35628 ["INT_ADD", "register:40f0:8", ["const:a35628:8", "const:4:8"]]
+ 00a35628 ["CALL", null, ["callee:0048797c:8"]]
- 00a355d4 bytes da48e997
+ 00a35628 bytes d548e997
- 00a355f4 ["INT_ADD", "register:40f0:8", ["const:a355f4:8", "const:4:8"]]
- 00a355f4 ["CALL", null, ["callee:00470754:8"]]
+ 00a35648 ["INT_ADD", "register:40f0:8", ["const:a35648:8", "const:4:8"]]
+ 00a35648 ["CALL", null, ["callee:00470754:8"]]
- 00a355f4 bytes 48ece897
+ 00a35648 bytes 43ece897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dab96d114b27bd104b649028a350960"></a>

### [`00a356f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a356f8.md) → [`00a3574c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a35/00a3574c.md) FUN_00a3574c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009d3af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3af4.md) · 呼出先 4件 [`007279d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007279d0.md) [`00727d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727d1c.md) [`00727e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727e68.md) [`00727fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727fb4.md)
- 新版 呼出元 1件 [`009d3b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d3/009d3b48.md) · 呼出先 4件 [`00727a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00727/00727a28.md) [`00727d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00727/00727d74.md) [`00727ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00727/00727ec0.md) [`0072800c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00728/0072800c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3571c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a356f8.md#insn-00a3571c) · [`00a35758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a356f8.md#insn-00a35758) · [`00a35794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a356f8.md#insn-00a35794)
- 新版 `00a35770`（命令位置の公開資料なし） · `00a357ac`（命令位置の公開資料なし） · `00a357e8`（命令位置の公開資料なし）

~~~diff
- 00a3571c ["INT_ADD", "register:40f0:8", ["const:a3571c:8", "const:4:8"]]
- 00a3571c ["CALL", null, ["callee:00727d74:8"]]
+ 00a35770 ["INT_ADD", "register:40f0:8", ["const:a35770:8", "const:4:8"]]
+ 00a35770 ["CALL", null, ["callee:00727d74:8"]]
- 00a3571c bytes 80c9f397
+ 00a35770 bytes 81c9f397
- 00a35758 ["INT_ADD", "register:40f0:8", ["const:a35758:8", "const:4:8"]]
- 00a35758 ["CALL", null, ["callee:00727ec0:8"]]
+ 00a357ac ["INT_ADD", "register:40f0:8", ["const:a357ac:8", "const:4:8"]]
+ 00a357ac ["CALL", null, ["callee:00727ec0:8"]]
- 00a35758 bytes c4c9f397
+ 00a357ac bytes c5c9f397
- 00a35794 ["INT_ADD", "register:40f0:8", ["const:a35794:8", "const:4:8"]]
- 00a35794 ["CALL", null, ["callee:0072800c:8"]]
+ 00a357e8 ["INT_ADD", "register:40f0:8", ["const:a357e8:8", "const:4:8"]]
+ 00a357e8 ["CALL", null, ["callee:0072800c:8"]]
- 00a35794 bytes 08caf397
+ 00a357e8 bytes 09caf397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55cd473ffa93f6c453a69cc18068a8ba"></a>

### [`00a37e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37e04.md) → [`00a37e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a37/00a37e58.md) FUN_00a37e58

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006312f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00631/006312f4.md) [`0075b9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075b/0075b9c4.md) · 呼出先 4件 [`005626f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/005626f4.md) [`00a37b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37b48.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`00631334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00631/00631334.md) [`0075ba1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075b/0075ba1c.md) · 呼出先 4件 [`00562734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562734.md) [`00a37b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a37/00a37b9c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a37e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37e04.md#insn-00a37e28) · [`00a37e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37e04.md#insn-00a37e50) · [`00a37e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37e04.md#insn-00a37e60)
- 新版 `00a37e7c`（命令位置の公開資料なし） · `00a37ea4`（命令位置の公開資料なし） · `00a37eb4`（命令位置の公開資料なし）

~~~diff
- 00a37e28 ["INT_ADD", "register:40f0:8", ["const:a37e28:8", "const:4:8"]]
- 00a37e28 ["CALL", null, ["callee:00a37b9c:8"]]
+ 00a37e7c ["INT_ADD", "register:40f0:8", ["const:a37e7c:8", "const:4:8"]]
+ 00a37e7c ["CALL", null, ["callee:00a37b9c:8"]]
- 00a37e28 bytes 48ffff97
+ 00a37e7c bytes 48ffff97
- 00a37e50 ["INT_ADD", "register:40f0:8", ["const:a37e50:8", "const:4:8"]]
- 00a37e50 ["CALL", null, ["callee:00562734:8"]]
+ 00a37ea4 ["INT_ADD", "register:40f0:8", ["const:a37ea4:8", "const:4:8"]]
+ 00a37ea4 ["CALL", null, ["callee:00562734:8"]]
- 00a37e50 bytes 29aaec97
+ 00a37ea4 bytes 24aaec97
- 00a37e60 ["INT_ADD", "register:40f0:8", ["const:a37e60:8", "const:4:8"]]
- 00a37e60 ["CALL", null, ["callee:00c57f80:8"]]
+ 00a37eb4 ["INT_ADD", "register:40f0:8", ["const:a37eb4:8", "const:4:8"]]
+ 00a37eb4 ["CALL", null, ["callee:00c57f80:8"]]
- 00a37e60 bytes 14800894
+ 00a37eb4 bytes 33800894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15bf47463ee8288f42b1ad2d1aabf8a1"></a>

### [`00a37ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37ff8.md) → [`00a3804c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a3804c.md) FUN_00a3804c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00869188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869188.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`008691e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008691e0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a38030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37ff8.md#insn-00a38030)
- 新版 `00a38084`（命令位置の公開資料なし）

~~~diff
- 00a38030 ["INT_ADD", "register:40f0:8", ["const:a38030:8", "const:4:8"]]
- 00a38030 ["CALL", null, ["callee:008691e0:8"]]
+ 00a38084 ["INT_ADD", "register:40f0:8", ["const:a38084:8", "const:4:8"]]
+ 00a38084 ["CALL", null, ["callee:008691e0:8"]]
- 00a38030 bytes 56c4f897
+ 00a38084 bytes 57c4f897
~~~


<a id="compare-36f062f925f74b9781e0ddd21083ae57"></a>

### [`00a38064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38064.md) → [`00a380b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a380b8.md) FUN_00a380b8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00869228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869228.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00869280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869280.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a38098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38064.md#insn-00a38098)
- 新版 `00a380ec`（命令位置の公開資料なし）

~~~diff
- 00a38098 ["INT_ADD", "register:40f0:8", ["const:a38098:8", "const:4:8"]]
- 00a38098 ["CALL", null, ["callee:00869280:8"]]
+ 00a380ec ["INT_ADD", "register:40f0:8", ["const:a380ec:8", "const:4:8"]]
+ 00a380ec ["CALL", null, ["callee:00869280:8"]]
- 00a38098 bytes 64c4f897
+ 00a380ec bytes 65c4f897
~~~


<a id="compare-35e27edeea3f24bb7dc34d9df1b15139"></a>

### [`00a380cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a380cc.md) → [`00a38120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a38120.md) FUN_00a38120

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0086930c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/0086930c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00869364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869364.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a380e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a380cc.md#insn-00a380e4)
- 新版 `00a38138`（命令位置の公開資料なし）

~~~diff
- 00a380e4 ["INT_ADD", "register:40f0:8", ["const:a380e4:8", "const:4:8"]]
- 00a380e4 ["CALL", null, ["callee:00869364:8"]]
+ 00a38138 ["INT_ADD", "register:40f0:8", ["const:a38138:8", "const:4:8"]]
+ 00a38138 ["CALL", null, ["callee:00869364:8"]]
- 00a380e4 bytes 8ac4f897
+ 00a38138 bytes 8bc4f897
~~~


<a id="compare-fa1276270eb6da31505941973fa38cf4"></a>

### [`00a38cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38cc4.md) → [`00a38d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a38d18.md) FUN_00a38d18

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a33cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33cac.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00726260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726260.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00a33d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a33/00a33d00.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`007262b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/007262b8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a38d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38cc4.md#insn-00a38d6c) · [`00a38dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38cc4.md#insn-00a38dac) · [`00a38df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38cc4.md#insn-00a38df0)
- 新版 `00a38dc0`（命令位置の公開資料なし） · `00a38e00`（命令位置の公開資料なし） · `00a38e44`（命令位置の公開資料なし）

~~~diff
- 00a38d6c ["INT_ADD", "register:40f0:8", ["const:a38d6c:8", "const:4:8"]]
- 00a38d6c ["CALL", null, ["callee:00c57f60:8"]]
+ 00a38dc0 ["INT_ADD", "register:40f0:8", ["const:a38dc0:8", "const:4:8"]]
+ 00a38dc0 ["CALL", null, ["callee:00c57f60:8"]]
- 00a38d6c bytes 497c0894
+ 00a38dc0 bytes 687c0894
- 00a38dac ["INT_ADD", "register:40f0:8", ["const:a38dac:8", "const:4:8"]]
- 00a38dac ["CALL", null, ["callee:00c58160:8"]]
+ 00a38e00 ["INT_ADD", "register:40f0:8", ["const:a38e00:8", "const:4:8"]]
+ 00a38e00 ["CALL", null, ["callee:00c58160:8"]]
- 00a38dac bytes b97c0894
+ 00a38e00 bytes d87c0894
- 00a38df0 ["INT_ADD", "register:40f0:8", ["const:a38df0:8", "const:4:8"]]
- 00a38df0 ["CALL", null, ["callee:00c58160:8"]]
+ 00a38e44 ["INT_ADD", "register:40f0:8", ["const:a38e44:8", "const:4:8"]]
+ 00a38e44 ["CALL", null, ["callee:00c58160:8"]]
- 00a38df0 bytes a87c0894
+ 00a38e44 bytes c77c0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-490536d753ee52d1725239a6265ac369"></a>

### [`00a38e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38e58.md) → [`00a38eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a38eac.md) FUN_00a38eac

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a33f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33f7c.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0072608c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/0072608c.md) [`00a39078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39078.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00a33fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a33/00a33fd0.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`007260e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/007260e4.md) [`00a390cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a390cc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a38f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38e58.md#insn-00a38f18) · [`00a38f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38e58.md#insn-00a38f50) · [`00a38f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38e58.md#insn-00a38f9c)
- 新版 `00a38f6c`（命令位置の公開資料なし） · `00a38fa4`（命令位置の公開資料なし） · `00a38ff0`（命令位置の公開資料なし）

~~~diff
- 00a38f18 ["INT_ADD", "register:40f0:8", ["const:a38f18:8", "const:4:8"]]
- 00a38f18 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a38f6c ["INT_ADD", "register:40f0:8", ["const:a38f6c:8", "const:4:8"]]
+ 00a38f6c ["CALL", null, ["callee:00c57f60:8"]]
- 00a38f18 bytes de7b0894
+ 00a38f6c bytes fd7b0894
- 00a38f50 ["INT_ADD", "register:40f0:8", ["const:a38f50:8", "const:4:8"]]
- 00a38f50 ["CALL", null, ["callee:00c58160:8"]]
+ 00a38fa4 ["INT_ADD", "register:40f0:8", ["const:a38fa4:8", "const:4:8"]]
+ 00a38fa4 ["CALL", null, ["callee:00c58160:8"]]
- 00a38f50 bytes 507c0894
+ 00a38fa4 bytes 6f7c0894
- 00a38f9c ["INT_ADD", "register:40f0:8", ["const:a38f9c:8", "const:4:8"]]
- 00a38f9c ["CALL", null, ["callee:00c58160:8"]]
+ 00a38ff0 ["INT_ADD", "register:40f0:8", ["const:a38ff0:8", "const:4:8"]]
+ 00a38ff0 ["CALL", null, ["callee:00c58160:8"]]
- 00a38f9c bytes 3d7c0894
+ 00a38ff0 bytes 5c7c0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ee7ae8a644afc26c69258e70b06a87b"></a>

### [`00a39078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39078.md) → [`00a390cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a390cc.md) FUN_00a390cc

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a38e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38e58.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00a38eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a38eac.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3913c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39078.md#insn-00a3913c) · [`00a3914c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39078.md#insn-00a3914c)
- 新版 `00a39190`（命令位置の公開資料なし） · `00a391a0`（命令位置の公開資料なし）

~~~diff
- 00a3913c ["INT_ADD", "register:40f0:8", ["const:a3913c:8", "const:4:8"]]
- 00a3913c ["CALL", null, ["callee:00c57f80:8"]]
+ 00a39190 ["INT_ADD", "register:40f0:8", ["const:a39190:8", "const:4:8"]]
+ 00a39190 ["CALL", null, ["callee:00c57f80:8"]]
- 00a3913c bytes 5d7b0894
+ 00a39190 bytes 7c7b0894
- 00a3914c ["INT_ADD", "register:40f0:8", ["const:a3914c:8", "const:4:8"]]
- 00a3914c ["CALL", null, ["callee:00c57f80:8"]]
+ 00a391a0 ["INT_ADD", "register:40f0:8", ["const:a391a0:8", "const:4:8"]]
+ 00a391a0 ["CALL", null, ["callee:00c57f80:8"]]
- 00a3914c bytes 597b0894
+ 00a391a0 bytes 787b0894
~~~


<a id="compare-bb27bb1026e05aeafc802f4f70b31276"></a>

### [`00a391a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a391a0.md) → [`00a391f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a391f4.md) FUN_00a391f4

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a391dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a391a0.md#insn-00a391dc) · [`00a391ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a391a0.md#insn-00a391ec)
- 新版 `00a39230`（命令位置の公開資料なし） · `00a39240`（命令位置の公開資料なし）

~~~diff
- 00a391dc ["INT_ADD", "register:40f0:8", ["const:a391dc:8", "const:4:8"]]
- 00a391dc ["CALL", null, ["callee:00c57f80:8"]]
+ 00a39230 ["INT_ADD", "register:40f0:8", ["const:a39230:8", "const:4:8"]]
+ 00a39230 ["CALL", null, ["callee:00c57f80:8"]]
- 00a391dc bytes 357b0894
+ 00a39230 bytes 547b0894
- 00a391ec ["INT_ADD", "register:40f0:8", ["const:a391ec:8", "const:4:8"]]
- 00a391ec ["CALL", null, ["callee:00c57f80:8"]]
+ 00a39240 ["INT_ADD", "register:40f0:8", ["const:a39240:8", "const:4:8"]]
+ 00a39240 ["CALL", null, ["callee:00c57f80:8"]]
- 00a391ec bytes 317b0894
+ 00a39240 bytes 507b0894
~~~


<a id="compare-8e08d42b2eee33433d64fadf783d5c1c"></a>

### [`00a3921c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a3921c.md) → [`00a39270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39270.md) FUN_00a39270

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a3611c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a36/00a3611c.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00a39400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39400.md) [`00a39528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39528.md) [`00a396d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a396d0.md) [`00a396e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a396e4.md)
- 新版 呼出元 1件 [`00a36170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a36/00a36170.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00a39454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39454.md) [`00a3957c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a3957c.md) [`00a39724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39724.md) [`00a39738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39738.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a392ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a3921c.md#insn-00a392ec) · [`00a39340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a3921c.md#insn-00a39340) · [`00a3935c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a3921c.md#insn-00a3935c)
- 新版 `00a39340`（命令位置の公開資料なし） · `00a39394`（命令位置の公開資料なし） · `00a393b0`（命令位置の公開資料なし）

~~~diff
- 00a392ec ["INT_ADD", "register:40f0:8", ["const:a392ec:8", "const:4:8"]]
- 00a392ec ["CALL", null, ["callee:00c57f60:8"]]
+ 00a39340 ["INT_ADD", "register:40f0:8", ["const:a39340:8", "const:4:8"]]
+ 00a39340 ["CALL", null, ["callee:00c57f60:8"]]
- 00a392ec bytes e97a0894
+ 00a39340 bytes 087b0894
- 00a39340 ["INT_ADD", "register:40f0:8", ["const:a39340:8", "const:4:8"]]
- 00a39340 ["CALL", null, ["callee:00a3957c:8"]]
+ 00a39394 ["INT_ADD", "register:40f0:8", ["const:a39394:8", "const:4:8"]]
+ 00a39394 ["CALL", null, ["callee:00a3957c:8"]]
- 00a39340 bytes 7a000094
+ 00a39394 bytes 7a000094
- 00a3935c ["INT_ADD", "register:40f0:8", ["const:a3935c:8", "const:4:8"]]
- 00a3935c ["CALL", null, ["callee:00a39738:8"]]
+ 00a393b0 ["INT_ADD", "register:40f0:8", ["const:a393b0:8", "const:4:8"]]
+ 00a393b0 ["CALL", null, ["callee:00a39738:8"]]
- 00a3935c bytes e2000094
+ 00a393b0 bytes e2000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-933393b44cc09c349f9e390cc58684e0"></a>

### [`00a39400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39400.md) → [`00a39454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39454.md) FUN_00a39454

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a3921c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a3921c.md) · 呼出先 1件 [`0086cd64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086cd64.md)
- 新版 呼出元 1件 [`00a39270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39270.md) · 呼出先 1件 [`0086cdbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086cdbc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a39474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39400.md#insn-00a39474) · [`00a394a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39400.md#insn-00a394a4)
- 新版 `00a394c8`（命令位置の公開資料なし） · `00a394f8`（命令位置の公開資料なし）

~~~diff
- 00a39474 ["INT_ADD", "register:40f0:8", ["const:a39474:8", "const:4:8"]]
- 00a39474 ["CALL", null, ["callee:0086cdbc:8"]]
+ 00a394c8 ["INT_ADD", "register:40f0:8", ["const:a394c8:8", "const:4:8"]]
+ 00a394c8 ["CALL", null, ["callee:0086cdbc:8"]]
- 00a39474 bytes 3ccef897
+ 00a394c8 bytes 3dcef897
- 00a394a4 ["INT_ADD", "register:40f0:8", ["const:a394a4:8", "const:4:8"]]
- 00a394a4 ["CALL", null, ["callee:0086cdbc:8"]]
+ 00a394f8 ["INT_ADD", "register:40f0:8", ["const:a394f8:8", "const:4:8"]]
+ 00a394f8 ["CALL", null, ["callee:0086cdbc:8"]]
- 00a394a4 bytes 30cef897
+ 00a394f8 bytes 31cef897
~~~


<a id="compare-0ed418cb2872f5f85b47f00a793a99da"></a>

### [`00a39528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39528.md) → [`00a3957c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a3957c.md) FUN_00a3957c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a3921c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a3921c.md) · 呼出先 1件 [`0086cd64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086cd64.md)
- 新版 呼出元 1件 [`00a39270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39270.md) · 呼出先 1件 [`0086cdbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086cdbc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3959c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39528.md#insn-00a3959c) · [`00a395cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39528.md#insn-00a395cc)
- 新版 `00a395f0`（命令位置の公開資料なし） · `00a39620`（命令位置の公開資料なし）

~~~diff
- 00a3959c ["INT_ADD", "register:40f0:8", ["const:a3959c:8", "const:4:8"]]
- 00a3959c ["CALL", null, ["callee:0086cdbc:8"]]
+ 00a395f0 ["INT_ADD", "register:40f0:8", ["const:a395f0:8", "const:4:8"]]
+ 00a395f0 ["CALL", null, ["callee:0086cdbc:8"]]
- 00a3959c bytes f2cdf897
+ 00a395f0 bytes f3cdf897
- 00a395cc ["INT_ADD", "register:40f0:8", ["const:a395cc:8", "const:4:8"]]
- 00a395cc ["CALL", null, ["callee:0086cdbc:8"]]
+ 00a39620 ["INT_ADD", "register:40f0:8", ["const:a39620:8", "const:4:8"]]
+ 00a39620 ["CALL", null, ["callee:0086cdbc:8"]]
- 00a395cc bytes e6cdf897
+ 00a39620 bytes e7cdf897
~~~


<a id="compare-6b3918dc2e80815dc471d71a8a5dca2c"></a>

### [`00a39650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39650.md) → [`00a396a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a396a4.md) FUN_00a396a4

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a39680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39650.md#insn-00a39680) · [`00a3968c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39650.md#insn-00a3968c) · [`00a39698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39650.md#insn-00a39698)
- 新版 `00a396d4`（命令位置の公開資料なし） · `00a396e0`（命令位置の公開資料なし） · `00a396ec`（命令位置の公開資料なし）

~~~diff
- 00a39680 ["INT_ADD", "register:40f0:8", ["const:a39680:8", "const:4:8"]]
- 00a39680 ["CALL", null, ["callee:0046d4d0:8"]]
+ 00a396d4 ["INT_ADD", "register:40f0:8", ["const:a396d4:8", "const:4:8"]]
+ 00a396d4 ["CALL", null, ["callee:0046d4d0:8"]]
- 00a39680 bytes 84cfe897
+ 00a396d4 bytes 7fcfe897
- 00a3968c ["INT_ADD", "register:40f0:8", ["const:a3968c:8", "const:4:8"]]
- 00a3968c ["CALL", null, ["callee:0046d4d0:8"]]
+ 00a396e0 ["INT_ADD", "register:40f0:8", ["const:a396e0:8", "const:4:8"]]
+ 00a396e0 ["CALL", null, ["callee:0046d4d0:8"]]
- 00a3968c bytes 81cfe897
+ 00a396e0 bytes 7ccfe897
- 00a39698 ["INT_ADD", "register:40f0:8", ["const:a39698:8", "const:4:8"]]
- 00a39698 ["CALL", null, ["callee:0046d4d0:8"]]
+ 00a396ec ["INT_ADD", "register:40f0:8", ["const:a396ec:8", "const:4:8"]]
+ 00a396ec ["CALL", null, ["callee:0046d4d0:8"]]
- 00a39698 bytes 7ecfe897
+ 00a396ec bytes 79cfe897
~~~


<a id="compare-ebf188f2ea01af226ebaf0f7abe4b0ab"></a>

### [`00a396e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a396e4.md) → [`00a39738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39738.md) FUN_00a39738

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a3921c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a3921c.md) · 呼出先 1件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md)
- 新版 呼出元 1件 [`00a39270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39270.md) · 呼出先 1件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a39808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a396e4.md#insn-00a39808) · [`00a39814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a396e4.md#insn-00a39814) · [`00a39820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a396e4.md#insn-00a39820)
- 新版 `00a3985c`（命令位置の公開資料なし） · `00a39868`（命令位置の公開資料なし） · `00a39874`（命令位置の公開資料なし）

~~~diff
- 00a39808 ["INT_ADD", "register:40f0:8", ["const:a39808:8", "const:4:8"]]
- 00a39808 ["CALL", null, ["callee:0046d4d0:8"]]
+ 00a3985c ["INT_ADD", "register:40f0:8", ["const:a3985c:8", "const:4:8"]]
+ 00a3985c ["CALL", null, ["callee:0046d4d0:8"]]
- 00a39808 bytes 22cfe897
+ 00a3985c bytes 1dcfe897
- 00a39814 ["INT_ADD", "register:40f0:8", ["const:a39814:8", "const:4:8"]]
- 00a39814 ["CALL", null, ["callee:0046d4d0:8"]]
+ 00a39868 ["INT_ADD", "register:40f0:8", ["const:a39868:8", "const:4:8"]]
+ 00a39868 ["CALL", null, ["callee:0046d4d0:8"]]
- 00a39814 bytes 1fcfe897
+ 00a39868 bytes 1acfe897
- 00a39820 ["INT_ADD", "register:40f0:8", ["const:a39820:8", "const:4:8"]]
- 00a39820 ["CALL", null, ["callee:0046d4d0:8"]]
+ 00a39874 ["INT_ADD", "register:40f0:8", ["const:a39874:8", "const:4:8"]]
+ 00a39874 ["CALL", null, ["callee:0046d4d0:8"]]
- 00a39820 bytes 1ccfe897
+ 00a39874 bytes 17cfe897
~~~


<a id="compare-a3913a26dd4d0896d2b0cb458a75b56a"></a>

### [`00a39840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39840.md) → [`00a39894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39894.md) FUN_00a39894

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a38108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38108.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00a399d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a399d0.md) [`00a39b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39b80.md) [`00a39d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39d1c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00a3815c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a3815c.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00a39a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39a24.md) [`00a39bd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39bd4.md) [`00a39d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a398d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39840.md#insn-00a398d0) · [`00a398f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39840.md#insn-00a398f0) · [`00a39924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39840.md#insn-00a39924)
- 新版 `00a39924`（命令位置の公開資料なし） · `00a39944`（命令位置の公開資料なし） · `00a39978`（命令位置の公開資料なし）

~~~diff
- 00a398d0 ["INT_ADD", "register:40f0:8", ["const:a398d0:8", "const:4:8"]]
- 00a398d0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a39924 ["INT_ADD", "register:40f0:8", ["const:a39924:8", "const:4:8"]]
+ 00a39924 ["CALL", null, ["callee:00c57f60:8"]]
- 00a398d0 bytes 70790894
+ 00a39924 bytes 8f790894
- 00a398f0 ["INT_ADD", "register:40f0:8", ["const:a398f0:8", "const:4:8"]]
- 00a398f0 ["CALL", null, ["callee:00c58160:8"]]
+ 00a39944 ["INT_ADD", "register:40f0:8", ["const:a39944:8", "const:4:8"]]
+ 00a39944 ["CALL", null, ["callee:00c58160:8"]]
- 00a398f0 bytes e8790894
+ 00a39944 bytes 077a0894
- 00a39924 ["INT_ADD", "register:40f0:8", ["const:a39924:8", "const:4:8"]]
- 00a39924 ["CALL", null, ["callee:00c58160:8"]]
+ 00a39978 ["INT_ADD", "register:40f0:8", ["const:a39978:8", "const:4:8"]]
+ 00a39978 ["CALL", null, ["callee:00c58160:8"]]
- 00a39924 bytes db790894
+ 00a39978 bytes fa790894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00b546a23337ffbb7d9ae7250ef0b6ad"></a>

### [`00a399d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a399d0.md) → [`00a39a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39a24.md) FUN_00a39a24

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a39840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39840.md) · 呼出先 2件 [`00a39b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39b94.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00a39894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39894.md) · 呼出先 2件 [`00a39be8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39be8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a39ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a399d0.md#insn-00a39ab8) · [`00a39b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a399d0.md#insn-00a39b44)
- 新版 `00a39b0c`（命令位置の公開資料なし） · `00a39b98`（命令位置の公開資料なし）

~~~diff
- 00a39ab8 ["INT_ADD", "register:40f0:8", ["const:a39ab8:8", "const:4:8"]]
- 00a39ab8 ["CALL", null, ["callee:00a39be8:8"]]
+ 00a39b0c ["INT_ADD", "register:40f0:8", ["const:a39b0c:8", "const:4:8"]]
+ 00a39b0c ["CALL", null, ["callee:00a39be8:8"]]
- 00a39ab8 bytes 37000094
+ 00a39b0c bytes 37000094
- 00a39b44 ["INT_ADD", "register:40f0:8", ["const:a39b44:8", "const:4:8"]]
- 00a39b44 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00a39b98 ["INT_ADD", "register:40f0:8", ["const:a39b98:8", "const:4:8"]]
+ 00a39b98 ["CALL", null, ["callee:00c57fb0:8"]]
- 00a39b44 bytes e7780894
+ 00a39b98 bytes 06790894
~~~


<a id="compare-f43395ea9c415212eb5edb3a71de20f1"></a>

### [`00a39b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39b48.md) → [`00a39b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39b9c.md) FUN_00a39b9c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00a39d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39d1c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00a39d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39d70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a39b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39b48.md#insn-00a39b5c)
- 新版 `00a39bb0`（命令位置の公開資料なし）

~~~diff
- 00a39b5c ["INT_ADD", "register:40f0:8", ["const:a39b5c:8", "const:4:8"]]
- 00a39b5c ["CALL", null, ["callee:00a39d70:8"]]
+ 00a39bb0 ["INT_ADD", "register:40f0:8", ["const:a39bb0:8", "const:4:8"]]
+ 00a39bb0 ["CALL", null, ["callee:00a39d70:8"]]
- 00a39b5c bytes 70000094
+ 00a39bb0 bytes 70000094
~~~


<a id="compare-e91d0311f15d4a03325dd1cd86ae1479"></a>

### [`00a39b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39b94.md) → [`00a39be8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39be8.md) FUN_00a39be8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a399d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a399d0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00a39a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39a24.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a39bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39b94.md#insn-00a39bc0) · [`00a39bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39b94.md#insn-00a39bdc) · [`00a39c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39b94.md#insn-00a39c14)
- 新版 `00a39c14`（命令位置の公開資料なし） · `00a39c30`（命令位置の公開資料なし） · `00a39c68`（命令位置の公開資料なし）

~~~diff
- 00a39bc0 ["INT_ADD", "register:40f0:8", ["const:a39bc0:8", "const:4:8"]]
- 00a39bc0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00a39c14 ["INT_ADD", "register:40f0:8", ["const:a39c14:8", "const:4:8"]]
+ 00a39c14 ["CALL", null, ["callee:00c57f80:8"]]
- 00a39bc0 bytes bc780894
+ 00a39c14 bytes db780894
- 00a39bdc ["INT_ADD", "register:40f0:8", ["const:a39bdc:8", "const:4:8"]]
- 00a39bdc ["CALL", null, ["callee:00c57f80:8"]]
+ 00a39c30 ["INT_ADD", "register:40f0:8", ["const:a39c30:8", "const:4:8"]]
+ 00a39c30 ["CALL", null, ["callee:00c57f80:8"]]
- 00a39bdc bytes b5780894
+ 00a39c30 bytes d4780894
- 00a39c14 ["INT_ADD", "register:40f0:8", ["const:a39c14:8", "const:4:8"]]
- 00a39c14 ["CALL", null, ["callee:00c57f80:8"]]
+ 00a39c68 ["INT_ADD", "register:40f0:8", ["const:a39c68:8", "const:4:8"]]
+ 00a39c68 ["CALL", null, ["callee:00c57f80:8"]]
- 00a39c14 bytes a7780894
+ 00a39c68 bytes c6780894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25252de104764c4cf5d01bc993bd775a"></a>

### [`00a39c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39c3c.md) → [`00a39c90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39c90.md) FUN_00a39c90

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00a39c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39c74.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00a39cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39cc8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a39c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39c3c.md#insn-00a39c64)
- 新版 `00a39cb8`（命令位置の公開資料なし）

~~~diff
- 00a39c64 ["INT_ADD", "register:40f0:8", ["const:a39c64:8", "const:4:8"]]
- 00a39c64 ["CALL", null, ["callee:00a39cc8:8"]]
+ 00a39cb8 ["INT_ADD", "register:40f0:8", ["const:a39cb8:8", "const:4:8"]]
+ 00a39cb8 ["CALL", null, ["callee:00a39cc8:8"]]
- 00a39c64 bytes 04000094
+ 00a39cb8 bytes 04000094
~~~


<a id="compare-4c5f1728353aefab40dda943dd65593b"></a>

### [`00a39c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39c74.md) → [`00a39cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39cc8.md) FUN_00a39cc8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a39c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39c3c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00a39c90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39c90.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a39ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39c74.md#insn-00a39ca0) · [`00a39cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39c74.md#insn-00a39cbc) · [`00a39cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39c74.md#insn-00a39cf4)
- 新版 `00a39cf4`（命令位置の公開資料なし） · `00a39d10`（命令位置の公開資料なし） · `00a39d48`（命令位置の公開資料なし）

~~~diff
- 00a39ca0 ["INT_ADD", "register:40f0:8", ["const:a39ca0:8", "const:4:8"]]
- 00a39ca0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00a39cf4 ["INT_ADD", "register:40f0:8", ["const:a39cf4:8", "const:4:8"]]
+ 00a39cf4 ["CALL", null, ["callee:00c57f80:8"]]
- 00a39ca0 bytes 84780894
+ 00a39cf4 bytes a3780894
- 00a39cbc ["INT_ADD", "register:40f0:8", ["const:a39cbc:8", "const:4:8"]]
- 00a39cbc ["CALL", null, ["callee:00c57f80:8"]]
+ 00a39d10 ["INT_ADD", "register:40f0:8", ["const:a39d10:8", "const:4:8"]]
+ 00a39d10 ["CALL", null, ["callee:00c57f80:8"]]
- 00a39cbc bytes 7d780894
+ 00a39d10 bytes 9c780894
- 00a39cf4 ["INT_ADD", "register:40f0:8", ["const:a39cf4:8", "const:4:8"]]
- 00a39cf4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00a39d48 ["INT_ADD", "register:40f0:8", ["const:a39d48:8", "const:4:8"]]
+ 00a39d48 ["CALL", null, ["callee:00c57f80:8"]]
- 00a39cf4 bytes 6f780894
+ 00a39d48 bytes 8e780894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-607a269c7c071c79c575509d198ddbfd"></a>

### [`00a39d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39d1c.md) → [`00a39d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39d70.md) FUN_00a39d70

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00a39840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39840.md) [`00a39b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39b48.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`00a39894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39894.md) [`00a39b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39b9c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a39d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39d1c.md#insn-00a39d50) · [`00a39d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39d1c.md#insn-00a39d74) · [`00a39dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39d1c.md#insn-00a39dac)
- 新版 `00a39da4`（命令位置の公開資料なし） · `00a39dc8`（命令位置の公開資料なし） · `00a39e00`（命令位置の公開資料なし）

~~~diff
- 00a39d50 ["INT_ADD", "register:40f0:8", ["const:a39d50:8", "const:4:8"]]
- 00a39d50 ["CALL", null, ["callee:00c57f80:8"]]
+ 00a39da4 ["INT_ADD", "register:40f0:8", ["const:a39da4:8", "const:4:8"]]
+ 00a39da4 ["CALL", null, ["callee:00c57f80:8"]]
- 00a39d50 bytes 58780894
+ 00a39da4 bytes 77780894
- 00a39d74 ["INT_ADD", "register:40f0:8", ["const:a39d74:8", "const:4:8"]]
- 00a39d74 ["CALL", null, ["callee:00c57f80:8"]]
+ 00a39dc8 ["INT_ADD", "register:40f0:8", ["const:a39dc8:8", "const:4:8"]]
+ 00a39dc8 ["CALL", null, ["callee:00c57f80:8"]]
- 00a39d74 bytes 4f780894
+ 00a39dc8 bytes 6e780894
- 00a39dac ["INT_ADD", "register:40f0:8", ["const:a39dac:8", "const:4:8"]]
- 00a39dac ["CALL", null, ["callee:00c57f80:8"]]
+ 00a39e00 ["INT_ADD", "register:40f0:8", ["const:a39e00:8", "const:4:8"]]
+ 00a39e00 ["CALL", null, ["callee:00c57f80:8"]]
- 00a39dac bytes 41780894
+ 00a39e00 bytes 60780894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-faf21714be0a795c6c07fad282621c5a"></a>

### [`00a39dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39dd8.md) → [`00a39e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39e2c.md) FUN_00a39e2c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a38108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38108.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00869228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869228.md) [`00a3a004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a004.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00a3815c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a3815c.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00869280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869280.md) [`00a3a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3a058.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a39e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39dd8.md#insn-00a39e80) · [`00a39ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39dd8.md#insn-00a39ec0) · [`00a39f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39dd8.md#insn-00a39f0c)
- 新版 `00a39ed4`（命令位置の公開資料なし） · `00a39f14`（命令位置の公開資料なし） · `00a39f60`（命令位置の公開資料なし）

~~~diff
- 00a39e80 ["INT_ADD", "register:40f0:8", ["const:a39e80:8", "const:4:8"]]
- 00a39e80 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a39ed4 ["INT_ADD", "register:40f0:8", ["const:a39ed4:8", "const:4:8"]]
+ 00a39ed4 ["CALL", null, ["callee:00c57f60:8"]]
- 00a39e80 bytes 04780894
+ 00a39ed4 bytes 23780894
- 00a39ec0 ["INT_ADD", "register:40f0:8", ["const:a39ec0:8", "const:4:8"]]
- 00a39ec0 ["CALL", null, ["callee:00c58160:8"]]
+ 00a39f14 ["INT_ADD", "register:40f0:8", ["const:a39f14:8", "const:4:8"]]
+ 00a39f14 ["CALL", null, ["callee:00c58160:8"]]
- 00a39ec0 bytes 74780894
+ 00a39f14 bytes 93780894
- 00a39f0c ["INT_ADD", "register:40f0:8", ["const:a39f0c:8", "const:4:8"]]
- 00a39f0c ["CALL", null, ["callee:00c58160:8"]]
+ 00a39f60 ["INT_ADD", "register:40f0:8", ["const:a39f60:8", "const:4:8"]]
+ 00a39f60 ["CALL", null, ["callee:00c58160:8"]]
- 00a39f0c bytes 61780894
+ 00a39f60 bytes 80780894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23caa4b2bdca9264d885200c4a7ddff7"></a>

### [`00a3a018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a018.md) → [`00a3a06c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3a06c.md) FUN_00a3a06c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a38108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38108.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00869188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869188.md) [`00a3a268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a268.md) [`00a3a460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a460.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00a3815c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a3815c.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`008691e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008691e0.md) [`00a3a2bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3a2bc.md) [`00a3a4b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3a4b4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3a0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a018.md#insn-00a3a0e8) · [`00a3a1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a018.md#insn-00a3a1b8) · [`00a3a1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a018.md#insn-00a3a1d8)
- 新版 `00a3a13c`（命令位置の公開資料なし） · `00a3a20c`（命令位置の公開資料なし） · `00a3a22c`（命令位置の公開資料なし）

~~~diff
- 00a3a0e8 ["INT_ADD", "register:40f0:8", ["const:a3a0e8:8", "const:4:8"]]
- 00a3a0e8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a3a13c ["INT_ADD", "register:40f0:8", ["const:a3a13c:8", "const:4:8"]]
+ 00a3a13c ["CALL", null, ["callee:00c57f60:8"]]
- 00a3a0e8 bytes 6a770894
+ 00a3a13c bytes 89770894
- 00a3a1b8 ["INT_ADD", "register:40f0:8", ["const:a3a1b8:8", "const:4:8"]]
- 00a3a1b8 ["CALL", null, ["callee:00a3a2bc:8"]]
+ 00a3a20c ["INT_ADD", "register:40f0:8", ["const:a3a20c:8", "const:4:8"]]
+ 00a3a20c ["CALL", null, ["callee:00a3a2bc:8"]]
- 00a3a1b8 bytes 2c000094
+ 00a3a20c bytes 2c000094
- 00a3a1d8 ["INT_ADD", "register:40f0:8", ["const:a3a1d8:8", "const:4:8"]]
- 00a3a1d8 ["CALL", null, ["callee:008691e0:8"]]
+ 00a3a22c ["INT_ADD", "register:40f0:8", ["const:a3a22c:8", "const:4:8"]]
+ 00a3a22c ["CALL", null, ["callee:008691e0:8"]]
- 00a3a1d8 bytes ecbbf897
+ 00a3a22c bytes edbbf897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f353ecdeb4e7337daad4979a0408e68"></a>

### [`00a3a268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a268.md) → [`00a3a2bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3a2bc.md) FUN_00a3a2bc

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a3a018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a018.md) · 呼出先 1件 [`00869188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869188.md)
- 新版 呼出元 1件 [`00a3a06c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3a06c.md) · 呼出先 1件 [`008691e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008691e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3a3ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a268.md#insn-00a3a3ac)
- 新版 `00a3a400`（命令位置の公開資料なし）

~~~diff
- 00a3a3ac ["INT_ADD", "register:40f0:8", ["const:a3a3ac:8", "const:4:8"]]
- 00a3a3ac ["CALL", null, ["callee:008691e0:8"]]
+ 00a3a400 ["INT_ADD", "register:40f0:8", ["const:a3a400:8", "const:4:8"]]
+ 00a3a400 ["CALL", null, ["callee:008691e0:8"]]
- 00a3a3ac bytes 77bbf897
+ 00a3a400 bytes 78bbf897
~~~


<a id="compare-d7cd16da69704363b9789e98885eed77"></a>

### [`00a3a408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a408.md) → [`00a3a45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3a45c.md) FUN_00a3a45c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00869188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869188.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`008691e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008691e0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3a430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a408.md#insn-00a3a430)
- 新版 `00a3a484`（命令位置の公開資料なし）

~~~diff
- 00a3a430 ["INT_ADD", "register:40f0:8", ["const:a3a430:8", "const:4:8"]]
- 00a3a430 ["CALL", null, ["callee:008691e0:8"]]
+ 00a3a484 ["INT_ADD", "register:40f0:8", ["const:a3a484:8", "const:4:8"]]
+ 00a3a484 ["CALL", null, ["callee:008691e0:8"]]
- 00a3a430 bytes 56bbf897
+ 00a3a484 bytes 57bbf897
~~~


<a id="compare-a2c4118386c895953dbb8a05738797d9"></a>

### [`00a3a804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a804.md) → [`00a3a858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3a858.md) FUN_00a3a858

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00a3a938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a938.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`009d0374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d0/009d0374.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00a3a98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3a98c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3a8ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a804.md#insn-00a3a8ac) · [`00a3a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a804.md#insn-00a3a8e0) · [`00a3a92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a804.md#insn-00a3a92c)
- 新版 `00a3a900`（命令位置の公開資料なし） · `00a3a934`（命令位置の公開資料なし） · `00a3a980`（命令位置の公開資料なし）

~~~diff
- 00a3a8ac ["INT_ADD", "register:40f0:8", ["const:a3a8ac:8", "const:4:8"]]
- 00a3a8ac ["CALL", null, ["callee:00c57f60:8"]]
+ 00a3a900 ["INT_ADD", "register:40f0:8", ["const:a3a900:8", "const:4:8"]]
+ 00a3a900 ["CALL", null, ["callee:00c57f60:8"]]
- 00a3a8ac bytes 79750894
+ 00a3a900 bytes 98750894
- 00a3a8e0 ["INT_ADD", "register:40f0:8", ["const:a3a8e0:8", "const:4:8"]]
- 00a3a8e0 ["CALL", null, ["callee:0043bbe4:8"]]
+ 00a3a934 ["INT_ADD", "register:40f0:8", ["const:a3a934:8", "const:4:8"]]
+ 00a3a934 ["CALL", null, ["callee:0043bbe4:8"]]
- 00a3a8e0 bytes b104e897
+ 00a3a934 bytes ac04e897
- 00a3a92c ["INT_ADD", "register:40f0:8", ["const:a3a92c:8", "const:4:8"]]
- 00a3a92c ["CALL", null, ["callee:00a3a98c:8"]]
+ 00a3a980 ["INT_ADD", "register:40f0:8", ["const:a3a980:8", "const:4:8"]]
+ 00a3a980 ["CALL", null, ["callee:00a3a98c:8"]]
- 00a3a92c bytes 03000094
+ 00a3a980 bytes 03000094
~~~


<a id="compare-dbdc05f6df89f160d0a695f0005ca6ef"></a>

### [`00a3a938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a938.md) → [`00a3a98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3a98c.md) FUN_00a3a98c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a3a804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a804.md) · 呼出先 3件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00a3a858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3a858.md) · 呼出先 3件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3a9e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a938.md#insn-00a3a9e8) · [`00a3a9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a938.md#insn-00a3a9f0) · [`00a3aaa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a938.md#insn-00a3aaa4)
- 新版 `00a3aa3c`（命令位置の公開資料なし） · `00a3aa44`（命令位置の公開資料なし） · `00a3aaf8`（命令位置の公開資料なし）

~~~diff
- 00a3a9e8 ["INT_ADD", "register:40f0:8", ["const:a3a9e8:8", "const:4:8"]]
- 00a3a9e8 ["CALL", null, ["callee:00494650:8"]]
+ 00a3aa3c ["INT_ADD", "register:40f0:8", ["const:a3aa3c:8", "const:4:8"]]
+ 00a3aa3c ["CALL", null, ["callee:00494650:8"]]
- 00a3a9e8 bytes 0a67e997
+ 00a3aa3c bytes 0567e997
- 00a3a9f0 ["INT_ADD", "register:40f0:8", ["const:a3a9f0:8", "const:4:8"]]
- 00a3a9f0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00a3aa44 ["INT_ADD", "register:40f0:8", ["const:a3aa44:8", "const:4:8"]]
+ 00a3aa44 ["CALL", null, ["callee:00c57f80:8"]]
- 00a3a9f0 bytes 30750894
+ 00a3aa44 bytes 4f750894
- 00a3aaa4 ["INT_ADD", "register:40f0:8", ["const:a3aaa4:8", "const:4:8"]]
- 00a3aaa4 ["CALL", null, ["callee:00494650:8"]]
+ 00a3aaf8 ["INT_ADD", "register:40f0:8", ["const:a3aaf8:8", "const:4:8"]]
+ 00a3aaf8 ["CALL", null, ["callee:00494650:8"]]
- 00a3aaa4 bytes db66e997
+ 00a3aaf8 bytes d666e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0afd936b9fa48c0ca912a7838332818a"></a>

### [`00a3b884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3b/00a3b884.md) → [`00a3b8d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3b/00a3b8d8.md) FUN_00a3b8d8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a3aac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3aac8.md) · 呼出先 3件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`0086a1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a1a8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00a3ab1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3ab1c.md) · 呼出先 3件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`0086a200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a200.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3b89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3b/00a3b884.md#insn-00a3b89c) · [`00a3b8ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3b/00a3b884.md#insn-00a3b8ac)
- 新版 `00a3b8f0`（命令位置の公開資料なし） · `00a3b900`（命令位置の公開資料なし）

~~~diff
- 00a3b89c ["INT_ADD", "register:40f0:8", ["const:a3b89c:8", "const:4:8"]]
- 00a3b89c ["CALL", null, ["callee:005c17dc:8"]]
+ 00a3b8f0 ["INT_ADD", "register:40f0:8", ["const:a3b8f0:8", "const:4:8"]]
+ 00a3b8f0 ["CALL", null, ["callee:005c17dc:8"]]
- 00a3b89c bytes c017ee97
+ 00a3b8f0 bytes bb17ee97
- 00a3b8ac ["INT_ADD", "register:40f0:8", ["const:a3b8ac:8", "const:4:8"]]
- 00a3b8ac ["CALL", null, ["callee:00c57f80:8"]]
+ 00a3b900 ["INT_ADD", "register:40f0:8", ["const:a3b900:8", "const:4:8"]]
+ 00a3b900 ["CALL", null, ["callee:00c57f80:8"]]
- 00a3b8ac bytes 81710894
+ 00a3b900 bytes a0710894
~~~


<a id="compare-771dacae4b85ff9e78d303063080697f"></a>

### [`00a3b8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3b/00a3b8c4.md) → [`00a3b918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3b/00a3b918.md) FUN_00a3b918

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a3aac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3aac8.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00a3ab1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3ab1c.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3b918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3b/00a3b8c4.md#insn-00a3b918) · [`00a3b96c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3b/00a3b8c4.md#insn-00a3b96c) · [`00a3b9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3b/00a3b8c4.md#insn-00a3b9a0)
- 新版 `00a3b96c`（命令位置の公開資料なし） · `00a3b9c0`（命令位置の公開資料なし） · `00a3b9f4`（命令位置の公開資料なし）

~~~diff
- 00a3b918 ["INT_ADD", "register:40f0:8", ["const:a3b918:8", "const:4:8"]]
- 00a3b918 ["CALL", null, ["callee:0046d7f0:8"]]
+ 00a3b96c ["INT_ADD", "register:40f0:8", ["const:a3b96c:8", "const:4:8"]]
+ 00a3b96c ["CALL", null, ["callee:0046d7f0:8"]]
- 00a3b918 bytes a6c7e897
+ 00a3b96c bytes a1c7e897
- 00a3b96c ["INT_ADD", "register:40f0:8", ["const:a3b96c:8", "const:4:8"]]
- 00a3b96c ["CALL", null, ["callee:00c57f60:8"]]
+ 00a3b9c0 ["INT_ADD", "register:40f0:8", ["const:a3b9c0:8", "const:4:8"]]
+ 00a3b9c0 ["CALL", null, ["callee:00c57f60:8"]]
- 00a3b96c bytes 49710894
+ 00a3b9c0 bytes 68710894
- 00a3b9a0 ["INT_ADD", "register:40f0:8", ["const:a3b9a0:8", "const:4:8"]]
- 00a3b9a0 ["CALL", null, ["callee:0043bbe4:8"]]
+ 00a3b9f4 ["INT_ADD", "register:40f0:8", ["const:a3b9f4:8", "const:4:8"]]
+ 00a3b9f4 ["CALL", null, ["callee:0043bbe4:8"]]
- 00a3b9a0 bytes 8100e897
+ 00a3b9f4 bytes 7c00e897
~~~


<a id="compare-04ca4396f6a4cb1377c84442d8b3e4e9"></a>

### [`00a3d9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3d/00a3d9f4.md) → [`00a3da48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3d/00a3da48.md) FUN_00a3da48

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a3ce18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3c/00a3ce18.md) · 呼出先 2件 [`008ab968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ab/008ab968.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00a3ce6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3c/00a3ce6c.md) · 呼出先 2件 [`008ab9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ab/008ab9c0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3da18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3d/00a3d9f4.md#insn-00a3da18) · [`00a3da50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3d/00a3d9f4.md#insn-00a3da50)
- 新版 `00a3da6c`（命令位置の公開資料なし） · `00a3daa4`（命令位置の公開資料なし）

~~~diff
- 00a3da18 ["INT_ADD", "register:40f0:8", ["const:a3da18:8", "const:4:8"]]
- 00a3da18 ["CALL", null, ["callee:008ab9c0:8"]]
+ 00a3da6c ["INT_ADD", "register:40f0:8", ["const:a3da6c:8", "const:4:8"]]
+ 00a3da6c ["CALL", null, ["callee:008ab9c0:8"]]
- 00a3da18 bytes d4b7f997
+ 00a3da6c bytes d5b7f997
- 00a3da50 ["INT_ADD", "register:40f0:8", ["const:a3da50:8", "const:4:8"]]
- 00a3da50 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00a3daa4 ["INT_ADD", "register:40f0:8", ["const:a3daa4:8", "const:4:8"]]
+ 00a3daa4 ["CALL", null, ["callee:00c57fb0:8"]]
- 00a3da50 bytes 24690894
+ 00a3daa4 bytes 43690894
~~~


<a id="compare-43474b47294365218a0f36f4f4d1e083"></a>

### [`00a3da54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3d/00a3da54.md) → [`00a3daa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3d/00a3daa8.md) FUN_00a3daa8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3da6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3d/00a3da54.md#insn-00a3da6c) · [`00a3da78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3d/00a3da54.md#insn-00a3da78)
- 新版 `00a3dac0`（命令位置の公開資料なし） · `00a3dacc`（命令位置の公開資料なし）

~~~diff
- 00a3da6c ["INT_ADD", "register:40f0:8", ["const:a3da6c:8", "const:4:8"]]
- 00a3da6c ["CALL", null, ["callee:005c17dc:8"]]
+ 00a3dac0 ["INT_ADD", "register:40f0:8", ["const:a3dac0:8", "const:4:8"]]
+ 00a3dac0 ["CALL", null, ["callee:005c17dc:8"]]
- 00a3da6c bytes 4c0fee97
+ 00a3dac0 bytes 470fee97
- 00a3da78 ["INT_ADD", "register:40f0:8", ["const:a3da78:8", "const:4:8"]]
- 00a3da78 ["CALL", null, ["callee:005c17dc:8"]]
+ 00a3dacc ["INT_ADD", "register:40f0:8", ["const:a3dacc:8", "const:4:8"]]
+ 00a3dacc ["CALL", null, ["callee:005c17dc:8"]]
- 00a3da78 bytes 490fee97
+ 00a3dacc bytes 440fee97
~~~


<a id="compare-3e8717b6820c7b8c0fc33833706ddb47"></a>

### [`00a3e690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e690.md) → [`00a3e6e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3e6e4.md) FUN_00a3e6e4

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a3b0bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3b/00a3b0bc.md) · 呼出先 1件 [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md)
- 新版 呼出元 1件 [`00a3b110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3b/00a3b110.md) · 呼出先 1件 [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3e6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e690.md#insn-00a3e6bc) · [`00a3e6cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e690.md#insn-00a3e6cc) · [`00a3e6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e690.md#insn-00a3e6dc)
- 新版 `00a3e710`（命令位置の公開資料なし） · `00a3e720`（命令位置の公開資料なし） · `00a3e730`（命令位置の公開資料なし）

~~~diff
- 00a3e6bc ["INT_ADD", "register:40f0:8", ["const:a3e6bc:8", "const:4:8"]]
- 00a3e6bc ["CALL", null, ["callee:0048797c:8"]]
+ 00a3e710 ["INT_ADD", "register:40f0:8", ["const:a3e710:8", "const:4:8"]]
+ 00a3e710 ["CALL", null, ["callee:0048797c:8"]]
- 00a3e6bc bytes a024e997
+ 00a3e710 bytes 9b24e997
- 00a3e6cc ["INT_ADD", "register:40f0:8", ["const:a3e6cc:8", "const:4:8"]]
- 00a3e6cc ["CALL", null, ["callee:0048797c:8"]]
+ 00a3e720 ["INT_ADD", "register:40f0:8", ["const:a3e720:8", "const:4:8"]]
+ 00a3e720 ["CALL", null, ["callee:0048797c:8"]]
- 00a3e6cc bytes 9c24e997
+ 00a3e720 bytes 9724e997
- 00a3e6dc ["INT_ADD", "register:40f0:8", ["const:a3e6dc:8", "const:4:8"]]
- 00a3e6dc ["CALL", null, ["callee:0048797c:8"]]
+ 00a3e730 ["INT_ADD", "register:40f0:8", ["const:a3e730:8", "const:4:8"]]
+ 00a3e730 ["CALL", null, ["callee:0048797c:8"]]
- 00a3e6dc bytes 9824e997
+ 00a3e730 bytes 9324e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cee4fdc25ea1f6edf2b3abffcf740eff"></a>

### [`00a3e93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e93c.md) → [`00a3e990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3e990.md) FUN_00a3e990

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3e954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e93c.md#insn-00a3e954) · [`00a3e960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e93c.md#insn-00a3e960)
- 新版 `00a3e9a8`（命令位置の公開資料なし） · `00a3e9b4`（命令位置の公開資料なし）

~~~diff
- 00a3e954 ["INT_ADD", "register:40f0:8", ["const:a3e954:8", "const:4:8"]]
- 00a3e954 ["CALL", null, ["callee:005c17dc:8"]]
+ 00a3e9a8 ["INT_ADD", "register:40f0:8", ["const:a3e9a8:8", "const:4:8"]]
+ 00a3e9a8 ["CALL", null, ["callee:005c17dc:8"]]
- 00a3e954 bytes 920bee97
+ 00a3e9a8 bytes 8d0bee97
- 00a3e960 ["INT_ADD", "register:40f0:8", ["const:a3e960:8", "const:4:8"]]
- 00a3e960 ["CALL", null, ["callee:005c17dc:8"]]
+ 00a3e9b4 ["INT_ADD", "register:40f0:8", ["const:a3e9b4:8", "const:4:8"]]
+ 00a3e9b4 ["CALL", null, ["callee:005c17dc:8"]]
- 00a3e960 bytes 8f0bee97
+ 00a3e9b4 bytes 8a0bee97
~~~


<a id="compare-b83514c3a91bfabde0983024011cfdb7"></a>

### [`00a3e988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e988.md) → [`00a3e9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3e9dc.md) FUN_00a3e9dc

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a3ce18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3c/00a3ce18.md) · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00a3ce6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3c/00a3ce6c.md) · 呼出先 2件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3e9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e988.md#insn-00a3e9a0) · [`00a3e9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e988.md#insn-00a3e9ac) · [`00a3e9bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e988.md#insn-00a3e9bc)
- 新版 `00a3e9f4`（命令位置の公開資料なし） · `00a3ea00`（命令位置の公開資料なし） · `00a3ea10`（命令位置の公開資料なし）

~~~diff
- 00a3e9a0 ["INT_ADD", "register:40f0:8", ["const:a3e9a0:8", "const:4:8"]]
- 00a3e9a0 ["CALL", null, ["callee:005c17dc:8"]]
+ 00a3e9f4 ["INT_ADD", "register:40f0:8", ["const:a3e9f4:8", "const:4:8"]]
+ 00a3e9f4 ["CALL", null, ["callee:005c17dc:8"]]
- 00a3e9a0 bytes 7f0bee97
+ 00a3e9f4 bytes 7a0bee97
- 00a3e9ac ["INT_ADD", "register:40f0:8", ["const:a3e9ac:8", "const:4:8"]]
- 00a3e9ac ["CALL", null, ["callee:005c17dc:8"]]
+ 00a3ea00 ["INT_ADD", "register:40f0:8", ["const:a3ea00:8", "const:4:8"]]
+ 00a3ea00 ["CALL", null, ["callee:005c17dc:8"]]
- 00a3e9ac bytes 7c0bee97
+ 00a3ea00 bytes 770bee97
- 00a3e9bc ["INT_ADD", "register:40f0:8", ["const:a3e9bc:8", "const:4:8"]]
- 00a3e9bc ["CALL", null, ["callee:00c57f80:8"]]
+ 00a3ea10 ["INT_ADD", "register:40f0:8", ["const:a3ea10:8", "const:4:8"]]
+ 00a3ea10 ["CALL", null, ["callee:00c57f80:8"]]
- 00a3e9bc bytes 3d650894
+ 00a3ea10 bytes 5c650894
~~~


<a id="compare-04124a8d62625454c22058bf68fd0be1"></a>

### [`00a3ec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3ec64.md) → [`00a3ecb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3ecb8.md) FUN_00a3ecb8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00a3e8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e8cc.md) [`00a3e920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e920.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00691800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691800.md)
- 新版 呼出元 2件 [`00a3e920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3e920.md) [`00a3e974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3e974.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00691858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691858.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3ecb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3ec64.md#insn-00a3ecb8) · [`00a3ecdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3ec64.md#insn-00a3ecdc) · [`00a3ed00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3ec64.md#insn-00a3ed00)
- 新版 `00a3ed0c`（命令位置の公開資料なし） · `00a3ed30`（命令位置の公開資料なし） · `00a3ed54`（命令位置の公開資料なし）

~~~diff
- 00a3ecb8 ["INT_ADD", "register:40f0:8", ["const:a3ecb8:8", "const:4:8"]]
- 00a3ecb8 ["CALL", null, ["callee:0043bb60:8"]]
+ 00a3ed0c ["INT_ADD", "register:40f0:8", ["const:a3ed0c:8", "const:4:8"]]
+ 00a3ed0c ["CALL", null, ["callee:0043bb60:8"]]
- 00a3ecb8 bytes 9af3e797
+ 00a3ed0c bytes 95f3e797
- 00a3ecdc ["INT_ADD", "register:40f0:8", ["const:a3ecdc:8", "const:4:8"]]
- 00a3ecdc ["CALL", null, ["callee:00691858:8"]]
+ 00a3ed30 ["INT_ADD", "register:40f0:8", ["const:a3ed30:8", "const:4:8"]]
+ 00a3ed30 ["CALL", null, ["callee:00691858:8"]]
- 00a3ecdc bytes c94af197
+ 00a3ed30 bytes ca4af197
- 00a3ed00 ["INT_ADD", "register:40f0:8", ["const:a3ed00:8", "const:4:8"]]
- 00a3ed00 ["CALL", null, ["callee:00691858:8"]]
+ 00a3ed54 ["INT_ADD", "register:40f0:8", ["const:a3ed54:8", "const:4:8"]]
+ 00a3ed54 ["CALL", null, ["callee:00691858:8"]]
- 00a3ed00 bytes c04af197
+ 00a3ed54 bytes c14af197
~~~


<a id="compare-857e42a00fe8bb91c4e8c287a5cb9f3f"></a>

### [`00a3ed58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3ed58.md) → [`00a3edac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3edac.md) FUN_00a3edac

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3ed70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3ed58.md#insn-00a3ed70)
- 新版 `00a3edc4`（命令位置の公開資料なし）

~~~diff
- 00a3ed70 ["INT_ADD", "register:40f0:8", ["const:a3ed70:8", "const:4:8"]]
- 00a3ed70 ["CALL", null, ["callee:005c17dc:8"]]
+ 00a3edc4 ["INT_ADD", "register:40f0:8", ["const:a3edc4:8", "const:4:8"]]
+ 00a3edc4 ["CALL", null, ["callee:005c17dc:8"]]
- 00a3ed70 bytes 8b0aee97
+ 00a3edc4 bytes 860aee97
~~~


<a id="compare-b74378806ff738f872e5086fbabc85fc"></a>

### [`00a3ef78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3ef78.md) → [`00a3efcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3efcc.md) FUN_00a3efcc

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3ef90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3ef78.md#insn-00a3ef90)
- 新版 `00a3efe4`（命令位置の公開資料なし）

~~~diff
- 00a3ef90 ["INT_ADD", "register:40f0:8", ["const:a3ef90:8", "const:4:8"]]
- 00a3ef90 ["CALL", null, ["callee:005c17dc:8"]]
+ 00a3efe4 ["INT_ADD", "register:40f0:8", ["const:a3efe4:8", "const:4:8"]]
+ 00a3efe4 ["CALL", null, ["callee:005c17dc:8"]]
- 00a3ef90 bytes 030aee97
+ 00a3efe4 bytes fe09ee97
~~~


<a id="compare-45e1c215b356c8fe88d737e673eeb8f7"></a>

### [`00a3efa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3efa8.md) → [`00a3effc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3effc.md) FUN_00a3effc

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a3e9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e9d0.md) · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00a3ea24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3ea24.md) · 呼出先 2件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3efc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3efa8.md#insn-00a3efc0) · [`00a3efcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3efa8.md#insn-00a3efcc)
- 新版 `00a3f014`（命令位置の公開資料なし） · `00a3f020`（命令位置の公開資料なし）

~~~diff
- 00a3efc0 ["INT_ADD", "register:40f0:8", ["const:a3efc0:8", "const:4:8"]]
- 00a3efc0 ["CALL", null, ["callee:005c17dc:8"]]
+ 00a3f014 ["INT_ADD", "register:40f0:8", ["const:a3f014:8", "const:4:8"]]
+ 00a3f014 ["CALL", null, ["callee:005c17dc:8"]]
- 00a3efc0 bytes f709ee97
+ 00a3f014 bytes f209ee97
- 00a3efcc ["INT_ADD", "register:40f0:8", ["const:a3efcc:8", "const:4:8"]]
- 00a3efcc ["CALL", null, ["callee:005c17dc:8"]]
+ 00a3f020 ["INT_ADD", "register:40f0:8", ["const:a3f020:8", "const:4:8"]]
+ 00a3f020 ["CALL", null, ["callee:005c17dc:8"]]
- 00a3efcc bytes f409ee97
+ 00a3f020 bytes ef09ee97
~~~


<a id="compare-1cc76899e5dfc2d8d52f52f03c1549d0"></a>

### [`00a40c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a40/00a40c8c.md) → [`00a40ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a40/00a40ce0.md) FUN_00a40ce0

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00a40b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a40/00a40b94.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00a40be8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a40/00a40be8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a40c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a40/00a40c8c.md#insn-00a40c9c)
- 新版 `00a40cf0`（命令位置の公開資料なし）

~~~diff
- 00a40c9c ["INT_ADD", "register:40f0:8", ["const:a40c9c:8", "const:4:8"]]
- 00a40c9c ["CALL", null, ["callee:00a40be8:8"]]
+ 00a40cf0 ["INT_ADD", "register:40f0:8", ["const:a40cf0:8", "const:4:8"]]
+ 00a40cf0 ["CALL", null, ["callee:00a40be8:8"]]
- 00a40c9c bytes beffff97
+ 00a40cf0 bytes beffff97
~~~


<a id="compare-e83d34d7e124d3171be61d677fef4c11"></a>

### [`00a41384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a41/00a41384.md) → [`00a413d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a41/00a413d8.md) FUN_00a413d8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a415ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a41/00a415ac.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00a41600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a41/00a41600.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487aa4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a413e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a41/00a41384.md#insn-00a413e0) · [`00a413f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a41/00a41384.md#insn-00a413f0) · [`00a4140c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a41/00a41384.md#insn-00a4140c)
- 新版 `00a41434`（命令位置の公開資料なし） · `00a41444`（命令位置の公開資料なし） · `00a41460`（命令位置の公開資料なし）

~~~diff
- 00a413e0 ["INT_ADD", "register:40f0:8", ["const:a413e0:8", "const:4:8"]]
- 00a413e0 ["CALL", null, ["callee:00487aa4:8"]]
+ 00a41434 ["INT_ADD", "register:40f0:8", ["const:a41434:8", "const:4:8"]]
+ 00a41434 ["CALL", null, ["callee:00487aa4:8"]]
- 00a413e0 bytes a119e997
+ 00a41434 bytes 9c19e997
- 00a413f0 ["INT_ADD", "register:40f0:8", ["const:a413f0:8", "const:4:8"]]
- 00a413f0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00a41444 ["INT_ADD", "register:40f0:8", ["const:a41444:8", "const:4:8"]]
+ 00a41444 ["CALL", null, ["callee:00c57f80:8"]]
- 00a413f0 bytes b05a0894
+ 00a41444 bytes cf5a0894
- 00a4140c ["INT_ADD", "register:40f0:8", ["const:a4140c:8", "const:4:8"]]
- 00a4140c ["CALL", null, ["callee:0048797c:8"]]
+ 00a41460 ["INT_ADD", "register:40f0:8", ["const:a41460:8", "const:4:8"]]
+ 00a41460 ["CALL", null, ["callee:0048797c:8"]]
- 00a4140c bytes 4c19e997
+ 00a41460 bytes 4719e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd20faeae126e24a1a9add7be8e68658"></a>

### [`00a41f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a41/00a41f08.md) → [`00a41f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a41/00a41f5c.md) FUN_00a41f5c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a41f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a41/00a41f08.md#insn-00a41f24)
- 新版 `00a41f78`（命令位置の公開資料なし）

~~~diff
- 00a41f24 ["INT_ADD", "register:40f0:8", ["const:a41f24:8", "const:4:8"]]
- 00a41f24 ["CALL", null, ["callee:00c57f80:8"]]
+ 00a41f78 ["INT_ADD", "register:40f0:8", ["const:a41f78:8", "const:4:8"]]
+ 00a41f78 ["CALL", null, ["callee:00c57f80:8"]]
- 00a41f24 bytes e3570894
+ 00a41f78 bytes 02580894
~~~


<a id="compare-82801b4345f290e0da08a50c122c3304"></a>

### [`00a41f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a41/00a41f4c.md) → [`00a41fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a41/00a41fa0.md) FUN_00a41fa0

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`008c2d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c2/008c2d24.md) [`008c2eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c2/008c2eac.md) · 呼出先 1件 [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)
- 新版 呼出元 2件 [`008c2d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2d7c.md) [`008c2f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2f04.md) · 呼出先 1件 [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a41fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a41/00a41f4c.md#insn-00a41fb4)
- 新版 `00a42008`（命令位置の公開資料なし）

~~~diff
- 00a41fb4 ["INT_ADD", "register:40f0:8", ["const:a41fb4:8", "const:4:8"]]
- 00a41fb4 ["CALL", null, ["callee:00c58520:8"]]
+ 00a42008 ["INT_ADD", "register:40f0:8", ["const:a42008:8", "const:4:8"]]
+ 00a42008 ["CALL", null, ["callee:00c58520:8"]]
- 00a41fb4 bytes 27590894
+ 00a42008 bytes 46590894
~~~


<a id="compare-358ef355c88a8701ec9f06ddbbf8b143"></a>

### [`00a42030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a42/00a42030.md) → [`00a42084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a42/00a42084.md) FUN_00a42084

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 19件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`005e1620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1620.md) [`005f5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5790.md) [`006d02a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d0/006d02a4.md) [`007595dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00759/007595dc.md) · 呼出先 4件 [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) [`00802ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ee0.md)
- 新版 呼出元 19件 [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md) [`005e1660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e1660.md) [`005f57d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f5/005f57d0.md) [`006d02fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d0/006d02fc.md) [`00759634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00759/00759634.md) · 呼出先 4件 [`00802710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802710.md) [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md) [`00802d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802d00.md) [`00802f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802f38.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a42040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a42/00a42030.md#insn-00a42040) · [`00a4204c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a42/00a42030.md#insn-00a4204c) · [`00a4205c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a42/00a42030.md#insn-00a4205c)
- 新版 `00a42094`（命令位置の公開資料なし） · `00a420a0`（命令位置の公開資料なし） · `00a420b0`（命令位置の公開資料なし）

~~~diff
- 00a42040 ["INT_ADD", "register:40f0:8", ["const:a42040:8", "const:4:8"]]
- 00a42040 ["CALL", null, ["callee:00802710:8"]]
+ 00a42094 ["INT_ADD", "register:40f0:8", ["const:a42094:8", "const:4:8"]]
+ 00a42094 ["CALL", null, ["callee:00802710:8"]]
- 00a42040 bytes 9e01f797
+ 00a42094 bytes 9f01f797
- 00a4204c ["INT_ADD", "register:40f0:8", ["const:a4204c:8", "const:4:8"]]
- 00a4204c ["CALL", null, ["callee:00802710:8"]]
+ 00a420a0 ["INT_ADD", "register:40f0:8", ["const:a420a0:8", "const:4:8"]]
+ 00a420a0 ["CALL", null, ["callee:00802710:8"]]
- 00a4204c bytes 9b01f797
+ 00a420a0 bytes 9c01f797
- 00a4205c ["INT_ADD", "register:40f0:8", ["const:a4205c:8", "const:4:8"]]
- 00a4205c ["CALL", null, ["callee:00802710:8"]]
+ 00a420b0 ["INT_ADD", "register:40f0:8", ["const:a420b0:8", "const:4:8"]]
+ 00a420b0 ["CALL", null, ["callee:00802710:8"]]
- 00a4205c bytes 9701f797
+ 00a420b0 bytes 9801f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85bc464cdd087d44d762ac4f966180af"></a>

### [`00a420bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a42/00a420bc.md) → [`00a42110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a42/00a42110.md) FUN_00a42110

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 16件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`005e1620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1620.md) [`005f5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5790.md) [`006d02a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d0/006d02a4.md) [`007595dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00759/007595dc.md) · 呼出先 2件 [`0066a408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066a/0066a408.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 16件 [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md) [`005e1660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e1660.md) [`005f57d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f5/005f57d0.md) [`006d02fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d0/006d02fc.md) [`00759634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00759/00759634.md) · 呼出先 2件 [`0066a448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066a/0066a448.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a420d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a42/00a420bc.md#insn-00a420d4) · [`00a420f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a42/00a420bc.md#insn-00a420f8) · [`00a42100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a42/00a420bc.md#insn-00a42100)
- 新版 `00a42128`（命令位置の公開資料なし） · `00a4214c`（命令位置の公開資料なし） · `00a42154`（命令位置の公開資料なし）

~~~diff
- 00a420d4 ["INT_ADD", "register:40f0:8", ["const:a420d4:8", "const:4:8"]]
- 00a420d4 ["CALL", null, ["callee:00851550:8"]]
+ 00a42128 ["INT_ADD", "register:40f0:8", ["const:a42128:8", "const:4:8"]]
+ 00a42128 ["CALL", null, ["callee:00851550:8"]]
- 00a420d4 bytes 093df897
+ 00a42128 bytes 0a3df897
- 00a420f8 ["INT_ADD", "register:40f0:8", ["const:a420f8:8", "const:4:8"]]
- 00a420f8 ["CALL", null, ["callee:0066a448:8"]]
+ 00a4214c ["INT_ADD", "register:40f0:8", ["const:a4214c:8", "const:4:8"]]
+ 00a4214c ["CALL", null, ["callee:0066a448:8"]]
- 00a420f8 bytes c4a0f097
+ 00a4214c bytes bfa0f097
- 00a42100 ["INT_ADD", "register:40f0:8", ["const:a42100:8", "const:4:8"]]
- 00a42100 ["CALL", null, ["callee:00851550:8"]]
+ 00a42154 ["INT_ADD", "register:40f0:8", ["const:a42154:8", "const:4:8"]]
+ 00a42154 ["CALL", null, ["callee:00851550:8"]]
- 00a42100 bytes fe3cf897
+ 00a42154 bytes ff3cf897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b445a76fc25a1cb4ba943f41caccb99b"></a>

### [`00a428f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a42/00a428f0.md) → [`00a42944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a42/00a42944.md) FUN_00a42944

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005f5230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5230.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`00718774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00718/00718774.md) · 呼出先 4件 [`005e0eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0eec.md) [`006647c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006647c0.md) [`00af38f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af38f0.md) [`00af39b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af39b0.md)
- 新版 呼出元 3件 [`005f5270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f5/005f5270.md) [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) [`007187cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00718/007187cc.md) · 呼出先 4件 [`005e0f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e0/005e0f2c.md) [`00664800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664800.md) [`00af398c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af3/00af398c.md) [`00af3a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af3/00af3a4c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a42924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a42/00a428f0.md#insn-00a42924) · [`00a42938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a42/00a428f0.md#insn-00a42938) · [`00a4294c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a42/00a428f0.md#insn-00a4294c)
- 新版 `00a42978`（命令位置の公開資料なし） · `00a4298c`（命令位置の公開資料なし） · `00a429a0`（命令位置の公開資料なし）

~~~diff
- 00a42924 ["INT_ADD", "register:40f0:8", ["const:a42924:8", "const:4:8"]]
- 00a42924 ["CALL", null, ["callee:00af398c:8"]]
+ 00a42978 ["INT_ADD", "register:40f0:8", ["const:a42978:8", "const:4:8"]]
+ 00a42978 ["CALL", null, ["callee:00af398c:8"]]
- 00a42924 bytes f3c30294
+ 00a42978 bytes 05c40294
- 00a42938 ["INT_ADD", "register:40f0:8", ["const:a42938:8", "const:4:8"]]
- 00a42938 ["CALL", null, ["callee:005e0f2c:8"]]
+ 00a4298c ["INT_ADD", "register:40f0:8", ["const:a4298c:8", "const:4:8"]]
+ 00a4298c ["CALL", null, ["callee:005e0f2c:8"]]
- 00a42938 bytes 6d79ee97
+ 00a4298c bytes 6879ee97
- 00a4294c ["INT_ADD", "register:40f0:8", ["const:a4294c:8", "const:4:8"]]
- 00a4294c ["CALL", null, ["callee:00af3a4c:8"]]
+ 00a429a0 ["INT_ADD", "register:40f0:8", ["const:a429a0:8", "const:4:8"]]
+ 00a429a0 ["CALL", null, ["callee:00af3a4c:8"]]
- 00a4294c bytes 19c40294
+ 00a429a0 bytes 2bc40294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48db38e39e6e5f129cc0fb6f25d97c07"></a>

### [`00a42974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a42/00a42974.md) → [`00a429c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a42/00a429c8.md) FUN_00a429c8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005f5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5790.md) [`00718774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00718/00718774.md) [`00a51fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a51/00a51fc4.md) · 呼出先 8件 [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`005e1b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1b18.md) [`005e2e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e2/005e2e40.md) [`005e7430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7430.md) [`006647c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006647c0.md)
- 新版 呼出元 3件 [`005f57d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f5/005f57d0.md) [`007187cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00718/007187cc.md) [`00a52034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a52/00a52034.md) · 呼出先 8件 [`0049f430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f430.md) [`005e1b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e1b58.md) [`005e2e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e2/005e2e80.md) [`005e7470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7470.md) [`00664800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664800.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a4298c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a42/00a42974.md#insn-00a4298c) · [`00a42998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a42/00a42974.md#insn-00a42998) · [`00a429a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a42/00a42974.md#insn-00a429a8)
- 新版 `00a429e0`（命令位置の公開資料なし） · `00a429ec`（命令位置の公開資料なし） · `00a429fc`（命令位置の公開資料なし）

~~~diff
- 00a4298c ["INT_ADD", "register:40f0:8", ["const:a4298c:8", "const:4:8"]]
- 00a4298c ["CALL", null, ["callee:00851550:8"]]
+ 00a429e0 ["INT_ADD", "register:40f0:8", ["const:a429e0:8", "const:4:8"]]
+ 00a429e0 ["CALL", null, ["callee:00851550:8"]]
- 00a4298c bytes db3af897
+ 00a429e0 bytes dc3af897
- 00a42998 ["INT_ADD", "register:40f0:8", ["const:a42998:8", "const:4:8"]]
- 00a42998 ["CALL", null, ["callee:00802bb0:8"]]
+ 00a429ec ["INT_ADD", "register:40f0:8", ["const:a429ec:8", "const:4:8"]]
+ 00a429ec ["CALL", null, ["callee:00802bb0:8"]]
- 00a42998 bytes 7000f797
+ 00a429ec bytes 7100f797
- 00a429a8 ["INT_ADD", "register:40f0:8", ["const:a429a8:8", "const:4:8"]]
- 00a429a8 ["CALL", null, ["callee:0066a65c:8"]]
+ 00a429fc ["INT_ADD", "register:40f0:8", ["const:a429fc:8", "const:4:8"]]
+ 00a429fc ["CALL", null, ["callee:0066a65c:8"]]
- 00a429a8 bytes 1d9ff097
+ 00a429fc bytes 189ff097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-479f45823847d4d89f859f56e6bbda64"></a>

### [`00a43058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a43/00a43058.md) → [`00a430ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a43/00a430ac.md) FUN_00a430ac

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005e1620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1620.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 5件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00853c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853c70.md) [`00a42030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a42/00a42030.md) [`00a420bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a42/00a420bc.md) [`00af38f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af38f0.md)
- 新版 呼出元 2件 [`005e1660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e1660.md) [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) · 呼出先 5件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00853cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00853/00853cc8.md) [`00a42084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a42/00a42084.md) [`00a42110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a42/00a42110.md) [`00af398c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af3/00af398c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a4306c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a43/00a43058.md#insn-00a4306c) · [`00a430b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a43/00a43058.md#insn-00a430b4) · [`00a430c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a43/00a43058.md#insn-00a430c4)
- 新版 `00a430c0`（命令位置の公開資料なし） · `00a43108`（命令位置の公開資料なし） · `00a43118`（命令位置の公開資料なし）

~~~diff
- 00a4306c ["INT_ADD", "register:40f0:8", ["const:a4306c:8", "const:4:8"]]
- 00a4306c ["CALL", null, ["callee:00a42084:8"]]
+ 00a430c0 ["INT_ADD", "register:40f0:8", ["const:a430c0:8", "const:4:8"]]
+ 00a430c0 ["CALL", null, ["callee:00a42084:8"]]
- 00a4306c bytes f1fbff97
+ 00a430c0 bytes f1fbff97
- 00a430b4 ["INT_ADD", "register:40f0:8", ["const:a430b4:8", "const:4:8"]]
- 00a430b4 ["CALL", null, ["callee:00a42110:8"]]
+ 00a43108 ["INT_ADD", "register:40f0:8", ["const:a43108:8", "const:4:8"]]
+ 00a43108 ["CALL", null, ["callee:00a42110:8"]]
- 00a430b4 bytes 02fcff97
+ 00a43108 bytes 02fcff97
- 00a430c4 ["INT_ADD", "register:40f0:8", ["const:a430c4:8", "const:4:8"]]
- 00a430c4 ["CALL", null, ["callee:00851550:8"]]
+ 00a43118 ["INT_ADD", "register:40f0:8", ["const:a43118:8", "const:4:8"]]
+ 00a43118 ["CALL", null, ["callee:00851550:8"]]
- 00a430c4 bytes 0d39f897
+ 00a43118 bytes 0e39f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce42925e51920b05cd3e896de1004105"></a>

### [`00a465fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a465fc.md) → [`00a46650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46650.md) FUN_00a46650

採用 · 移動量 `+0x54` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00788cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/00788cac.md) [`007caac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007caac8.md) [`00a8a418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8a/00a8a418.md) · 呼出先 2件 [`00a46650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46650.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 3件 [`00788d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/00788d04.md) [`007cab20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ca/007cab20.md) [`00a8a488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a8a/00a8a488.md) · 呼出先 2件 [`00a466a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a466a4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a46620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a465fc.md#insn-00a46620) · [`00a4664c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a465fc.md#insn-00a4664c)
- 新版 `00a46674`（命令位置の公開資料なし） · `00a466a0`（命令位置の公開資料なし）

~~~diff
- 00a46620 ["INT_ADD", "register:40f0:8", ["const:a46620:8", "const:4:8"]]
- 00a46620 ["CALL", null, ["callee:00a466a4:8"]]
+ 00a46674 ["INT_ADD", "register:40f0:8", ["const:a46674:8", "const:4:8"]]
+ 00a46674 ["CALL", null, ["callee:00a466a4:8"]]
- 00a46620 bytes 0c000094
+ 00a46674 bytes 0c000094
- 00a4664c ["INT_ADD", "register:40f0:8", ["const:a4664c:8", "const:4:8"]]
- 00a4664c ["CALL", null, ["callee:00c57fb0:8"]]
+ 00a466a0 ["INT_ADD", "register:40f0:8", ["const:a466a0:8", "const:4:8"]]
+ 00a466a0 ["CALL", null, ["callee:00c57fb0:8"]]
- 00a4664c bytes 25460894
+ 00a466a0 bytes 44460894
~~~


<a id="compare-58285c26d3a4cc2031be6ce490a7b777"></a>

### [`00a46784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46784.md) → [`00a467d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a467d8.md) FUN_00a467d8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 62件 [`005c4958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c4/005c4958.md) [`005c8efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c8/005c8efc.md) [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`006064d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/006064d4.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00a47a9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47a9c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 63件 [`005c4998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c4998.md) [`005c8f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8f3c.md) [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00606514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606514.md) [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00a47af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47af0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a4680c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46784.md#insn-00a4680c) · [`00a46848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46784.md#insn-00a46848) · [`00a4685c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46784.md#insn-00a4685c)
- 新版 `00a46860`（命令位置の公開資料なし） · `00a4689c`（命令位置の公開資料なし） · `00a468b0`（命令位置の公開資料なし）

~~~diff
- 00a4680c ["INT_ADD", "register:40f0:8", ["const:a4680c:8", "const:4:8"]]
- 00a4680c ["CALL", null, ["callee:00c57f60:8"]]
+ 00a46860 ["INT_ADD", "register:40f0:8", ["const:a46860:8", "const:4:8"]]
+ 00a46860 ["CALL", null, ["callee:00c57f60:8"]]
- 00a4680c bytes a1450894
+ 00a46860 bytes c0450894
- 00a46848 ["INT_ADD", "register:40f0:8", ["const:a46848:8", "const:4:8"]]
- 00a46848 ["CALL", null, ["callee:00c580d0:8"]]
+ 00a4689c ["INT_ADD", "register:40f0:8", ["const:a4689c:8", "const:4:8"]]
+ 00a4689c ["CALL", null, ["callee:00c580d0:8"]]
- 00a46848 bytes ee450894
+ 00a4689c bytes 0d460894
- 00a4685c ["INT_ADD", "register:40f0:8", ["const:a4685c:8", "const:4:8"]]
- 00a4685c ["CALL", null, ["callee:00c57f80:8"]]
+ 00a468b0 ["INT_ADD", "register:40f0:8", ["const:a468b0:8", "const:4:8"]]
+ 00a468b0 ["CALL", null, ["callee:00c57f80:8"]]
- 00a4685c bytes 95450894
+ 00a468b0 bytes b4450894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88cfbc81bbb796d516b95ab421af10f9"></a>

### [`00a468fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a468fc.md) → [`00a46950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46950.md) FUN_00a46950

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 76件 [`005c4958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c4/005c4958.md) [`005c8efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c8/005c8efc.md) [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`006064d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/006064d4.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) · 呼出先 9件 [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`00489f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f58.md) [`0048ab40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab40.md) [`0048ab48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab48.md) [`00a46a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46a24.md)
- 新版 呼出元 77件 [`005c4998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c4998.md) [`005c8f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8f3c.md) [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00606514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606514.md) [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) · 呼出先 9件 [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`00489f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f98.md) [`0048ab80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab80.md) [`0048ab88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab88.md) [`00a46a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46a78.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a46928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a468fc.md#insn-00a46928) · [`00a46940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a468fc.md#insn-00a46940) · [`00a46958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a468fc.md#insn-00a46958)
- 新版 `00a4697c`（命令位置の公開資料なし） · `00a46994`（命令位置の公開資料なし） · `00a469ac`（命令位置の公開資料なし）

~~~diff
- 00a46928 ["INT_ADD", "register:40f0:8", ["const:a46928:8", "const:4:8"]]
- 00a46928 ["CALL", null, ["callee:00a46a78:8"]]
+ 00a4697c ["INT_ADD", "register:40f0:8", ["const:a4697c:8", "const:4:8"]]
+ 00a4697c ["CALL", null, ["callee:00a46a78:8"]]
- 00a46928 bytes 3f000094
+ 00a4697c bytes 3f000094
- 00a46940 ["INT_ADD", "register:40f0:8", ["const:a46940:8", "const:4:8"]]
- 00a46940 ["CALL", null, ["callee:00c53d70:8"]]
+ 00a46994 ["INT_ADD", "register:40f0:8", ["const:a46994:8", "const:4:8"]]
+ 00a46994 ["CALL", null, ["callee:00c53d70:8"]]
- 00a46940 bytes e4340894
+ 00a46994 bytes f7340894
- 00a46958 ["INT_ADD", "register:40f0:8", ["const:a46958:8", "const:4:8"]]
- 00a46958 ["CALL", null, ["callee:00c53da0:8"]]
+ 00a469ac ["INT_ADD", "register:40f0:8", ["const:a469ac:8", "const:4:8"]]
+ 00a469ac ["CALL", null, ["callee:00c53da0:8"]]
- 00a46958 bytes ea340894
+ 00a469ac bytes fd340894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-369b4c8ab53d32cde35f565fbbb4ce23"></a>

### [`00a46b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46b48.md) → [`00a46b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46b9c.md) FUN_00a46b9c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00786ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/00786ba8.md) [`007c8cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c8/007c8cf0.md) [`00a8ddb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8d/00a8ddb8.md) [`00a91e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a91/00a91e10.md) [`00a927fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a92/00a927fc.md) · 呼出先 3件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 5件 [`00786c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00786/00786c00.md) [`007c8d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007c8/007c8d48.md) [`00a8de28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a8d/00a8de28.md) [`00a91e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a91/00a91e80.md) [`00a9286c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a92/00a9286c.md) · 呼出先 3件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a46b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46b48.md#insn-00a46b6c) · [`00a46b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46b48.md#insn-00a46b84) · [`00a46b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46b48.md#insn-00a46b98)
- 新版 `00a46bc0`（命令位置の公開資料なし） · `00a46bd8`（命令位置の公開資料なし） · `00a46bec`（命令位置の公開資料なし）

~~~diff
- 00a46b6c ["INT_ADD", "register:40f0:8", ["const:a46b6c:8", "const:4:8"]]
- 00a46b6c ["CALL", null, ["callee:00c53d70:8"]]
+ 00a46bc0 ["INT_ADD", "register:40f0:8", ["const:a46bc0:8", "const:4:8"]]
+ 00a46bc0 ["CALL", null, ["callee:00c53d70:8"]]
- 00a46b6c bytes 59340894
+ 00a46bc0 bytes 6c340894
- 00a46b84 ["INT_ADD", "register:40f0:8", ["const:a46b84:8", "const:4:8"]]
- 00a46b84 ["CALL", null, ["callee:00c53da0:8"]]
+ 00a46bd8 ["INT_ADD", "register:40f0:8", ["const:a46bd8:8", "const:4:8"]]
+ 00a46bd8 ["CALL", null, ["callee:00c53da0:8"]]
- 00a46b84 bytes 5f340894
+ 00a46bd8 bytes 72340894
- 00a46b98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a46b98 ["INT_ADD", "register:40f0:8", ["const:a46b98:8", "const:4:8"]]
- 00a46b98 ["CALLIND", null, ["register:0:8"]]
+ 00a46bec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a46bec ["INT_ADD", "register:40f0:8", ["const:a46bec:8", "const:4:8"]]
+ 00a46bec ["CALLIND", null, ["register:0:8"]]
- 00a46b98 bytes 00013fd6
+ 00a46bec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1efbcd0009c6e456b10a1257cd8466a"></a>

### [`00a46bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46bb8.md) → [`00a46c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46c0c.md) FUN_00a46c0c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 59件 [`005c6978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c6/005c6978.md) [`005c87c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c8/005c87c0.md) [`005c8efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c8/005c8efc.md) [`005dc1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005dc/005dc1e0.md) [`0061e598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e598.md) · 呼出先 4件 [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`00489f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f58.md) [`0048ab40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab40.md) [`0048ab48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab48.md)
- 新版 呼出元 59件 [`005c69b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c69b8.md) [`005c8800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8800.md) [`005c8f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8f3c.md) [`005dc220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005dc/005dc220.md) [`0061e5d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e5d8.md) · 呼出先 4件 [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`00489f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f98.md) [`0048ab80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab80.md) [`0048ab88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab88.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a46bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46bb8.md#insn-00a46bd8) · [`00a46bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46bb8.md#insn-00a46bec) · [`00a46c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46bb8.md#insn-00a46c04)
- 新版 `00a46c2c`（命令位置の公開資料なし） · `00a46c40`（命令位置の公開資料なし） · `00a46c58`（命令位置の公開資料なし）

~~~diff
- 00a46bd8 ["INT_ADD", "register:40f0:8", ["const:a46bd8:8", "const:4:8"]]
- 00a46bd8 ["CALL", null, ["callee:00489f98:8"]]
+ 00a46c2c ["INT_ADD", "register:40f0:8", ["const:a46c2c:8", "const:4:8"]]
+ 00a46c2c ["CALL", null, ["callee:00489f98:8"]]
- 00a46bd8 bytes e00ce997
+ 00a46c2c bytes db0ce997
- 00a46bec ["INT_ADD", "register:40f0:8", ["const:a46bec:8", "const:4:8"]]
- 00a46bec ["CALL", null, ["callee:00489f8c:8"]]
+ 00a46c40 ["INT_ADD", "register:40f0:8", ["const:a46c40:8", "const:4:8"]]
+ 00a46c40 ["CALL", null, ["callee:00489f8c:8"]]
- 00a46bec bytes d80ce997
+ 00a46c40 bytes d30ce997
- 00a46c04 ["INT_ADD", "register:40f0:8", ["const:a46c04:8", "const:4:8"]]
- 00a46c04 ["CALL", null, ["callee:0048ab80:8"]]
+ 00a46c58 ["INT_ADD", "register:40f0:8", ["const:a46c58:8", "const:4:8"]]
+ 00a46c58 ["CALL", null, ["callee:0048ab80:8"]]
- 00a46c04 bytes cf0fe997
+ 00a46c58 bytes ca0fe997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee8e3300366264ed6076fb5146e471e9"></a>

### [`00a46cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46cc8.md) → [`00a46d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46d1c.md) FUN_00a46d1c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`005c4958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c4/005c4958.md) [`007caac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007caac8.md) [`007f0574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0574.md) · 呼出先 9件 [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`00489f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f58.md) [`0048ab40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab40.md) [`0048ab48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab48.md) [`00a46a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46a24.md)
- 新版 呼出元 3件 [`005c4998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c4998.md) [`007cab20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ca/007cab20.md) [`007f05cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f0/007f05cc.md) · 呼出先 9件 [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`00489f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f98.md) [`0048ab80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab80.md) [`0048ab88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab88.md) [`00a46a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46a78.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a46cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46cc8.md#insn-00a46cf4) · [`00a46d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46cc8.md#insn-00a46d0c) · [`00a46d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46cc8.md#insn-00a46d24)
- 新版 `00a46d48`（命令位置の公開資料なし） · `00a46d60`（命令位置の公開資料なし） · `00a46d78`（命令位置の公開資料なし）

~~~diff
- 00a46cf4 ["INT_ADD", "register:40f0:8", ["const:a46cf4:8", "const:4:8"]]
- 00a46cf4 ["CALL", null, ["callee:00a46a78:8"]]
+ 00a46d48 ["INT_ADD", "register:40f0:8", ["const:a46d48:8", "const:4:8"]]
+ 00a46d48 ["CALL", null, ["callee:00a46a78:8"]]
- 00a46cf4 bytes 4cffff97
+ 00a46d48 bytes 4cffff97
- 00a46d0c ["INT_ADD", "register:40f0:8", ["const:a46d0c:8", "const:4:8"]]
- 00a46d0c ["CALL", null, ["callee:00c53d70:8"]]
+ 00a46d60 ["INT_ADD", "register:40f0:8", ["const:a46d60:8", "const:4:8"]]
+ 00a46d60 ["CALL", null, ["callee:00c53d70:8"]]
- 00a46d0c bytes f1330894
+ 00a46d60 bytes 04340894
- 00a46d24 ["INT_ADD", "register:40f0:8", ["const:a46d24:8", "const:4:8"]]
- 00a46d24 ["CALL", null, ["callee:00c53da0:8"]]
+ 00a46d78 ["INT_ADD", "register:40f0:8", ["const:a46d78:8", "const:4:8"]]
+ 00a46d78 ["CALL", null, ["callee:00c53da0:8"]]
- 00a46d24 bytes f7330894
+ 00a46d78 bytes 0a340894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88df61b6322bbbe75b5a4b7e17dbe472"></a>

### [`00a46de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46de8.md) → [`00a46e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46e3c.md) FUN_00a46e3c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008bdb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008bd/008bdb00.md) · 呼出先 5件 [`00a46a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46a24.md) [`00a46c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46c34.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`008bdb58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bd/008bdb58.md) · 呼出先 5件 [`00a46a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46a78.md) [`00a46c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46c88.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a46e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46de8.md#insn-00a46e28) · [`00a46e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46de8.md#insn-00a46e40) · [`00a46e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46de8.md#insn-00a46e58)
- 新版 `00a46e7c`（命令位置の公開資料なし） · `00a46e94`（命令位置の公開資料なし） · `00a46eac`（命令位置の公開資料なし）

~~~diff
- 00a46e28 ["INT_ADD", "register:40f0:8", ["const:a46e28:8", "const:4:8"]]
- 00a46e28 ["CALL", null, ["callee:00a46a78:8"]]
+ 00a46e7c ["INT_ADD", "register:40f0:8", ["const:a46e7c:8", "const:4:8"]]
+ 00a46e7c ["CALL", null, ["callee:00a46a78:8"]]
- 00a46e28 bytes fffeff97
+ 00a46e7c bytes fffeff97
- 00a46e40 ["INT_ADD", "register:40f0:8", ["const:a46e40:8", "const:4:8"]]
- 00a46e40 ["CALL", null, ["callee:00c53d70:8"]]
+ 00a46e94 ["INT_ADD", "register:40f0:8", ["const:a46e94:8", "const:4:8"]]
+ 00a46e94 ["CALL", null, ["callee:00c53d70:8"]]
- 00a46e40 bytes a4330894
+ 00a46e94 bytes b7330894
- 00a46e58 ["INT_ADD", "register:40f0:8", ["const:a46e58:8", "const:4:8"]]
- 00a46e58 ["CALL", null, ["callee:00c53da0:8"]]
+ 00a46eac ["INT_ADD", "register:40f0:8", ["const:a46eac:8", "const:4:8"]]
+ 00a46eac ["CALL", null, ["callee:00c53da0:8"]]
- 00a46e58 bytes aa330894
+ 00a46eac bytes bd330894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29da1d268de4a26a58d2705314fb69c0"></a>

### [`00a46ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46ed8.md) → [`00a46f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46f2c.md) FUN_00a46f2c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0082be68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082b/0082be68.md) · 呼出先 5件 [`00a46a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46a24.md) [`00a46c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46c34.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0082bec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082b/0082bec0.md) · 呼出先 5件 [`00a46a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46a78.md) [`00a46c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46c88.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a46f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46ed8.md#insn-00a46f20) · [`00a46f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46ed8.md#insn-00a46f38) · [`00a46f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46ed8.md#insn-00a46f50)
- 新版 `00a46f74`（命令位置の公開資料なし） · `00a46f8c`（命令位置の公開資料なし） · `00a46fa4`（命令位置の公開資料なし）

~~~diff
- 00a46f20 ["INT_ADD", "register:40f0:8", ["const:a46f20:8", "const:4:8"]]
- 00a46f20 ["CALL", null, ["callee:00a46a78:8"]]
+ 00a46f74 ["INT_ADD", "register:40f0:8", ["const:a46f74:8", "const:4:8"]]
+ 00a46f74 ["CALL", null, ["callee:00a46a78:8"]]
- 00a46f20 bytes c1feff97
+ 00a46f74 bytes c1feff97
- 00a46f38 ["INT_ADD", "register:40f0:8", ["const:a46f38:8", "const:4:8"]]
- 00a46f38 ["CALL", null, ["callee:00c53d70:8"]]
+ 00a46f8c ["INT_ADD", "register:40f0:8", ["const:a46f8c:8", "const:4:8"]]
+ 00a46f8c ["CALL", null, ["callee:00c53d70:8"]]
- 00a46f38 bytes 66330894
+ 00a46f8c bytes 79330894
- 00a46f50 ["INT_ADD", "register:40f0:8", ["const:a46f50:8", "const:4:8"]]
- 00a46f50 ["CALL", null, ["callee:00c53da0:8"]]
+ 00a46fa4 ["INT_ADD", "register:40f0:8", ["const:a46fa4:8", "const:4:8"]]
+ 00a46fa4 ["CALL", null, ["callee:00c53da0:8"]]
- 00a46f50 bytes 6c330894
+ 00a46fa4 bytes 7f330894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f4de8732816afe56d8c7942c12786e7"></a>

### [`00a46fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46fc0.md) → [`00a47014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47014.md) FUN_00a47014

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007ca528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007ca528.md) · 呼出先 9件 [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`00489f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f58.md) [`0048ab40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab40.md) [`0048ab48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab48.md) [`00a46a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46a24.md)
- 新版 呼出元 1件 [`007ca580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ca/007ca580.md) · 呼出先 9件 [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`00489f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f98.md) [`0048ab80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab80.md) [`0048ab88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab88.md) [`00a46a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46a78.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a47000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46fc0.md#insn-00a47000) · [`00a47018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46fc0.md#insn-00a47018) · [`00a47030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46fc0.md#insn-00a47030)
- 新版 `00a47054`（命令位置の公開資料なし） · `00a4706c`（命令位置の公開資料なし） · `00a47084`（命令位置の公開資料なし）

~~~diff
- 00a47000 ["INT_ADD", "register:40f0:8", ["const:a47000:8", "const:4:8"]]
- 00a47000 ["CALL", null, ["callee:00a46a78:8"]]
+ 00a47054 ["INT_ADD", "register:40f0:8", ["const:a47054:8", "const:4:8"]]
+ 00a47054 ["CALL", null, ["callee:00a46a78:8"]]
- 00a47000 bytes 89feff97
+ 00a47054 bytes 89feff97
- 00a47018 ["INT_ADD", "register:40f0:8", ["const:a47018:8", "const:4:8"]]
- 00a47018 ["CALL", null, ["callee:00c53d70:8"]]
+ 00a4706c ["INT_ADD", "register:40f0:8", ["const:a4706c:8", "const:4:8"]]
+ 00a4706c ["CALL", null, ["callee:00c53d70:8"]]
- 00a47018 bytes 2e330894
+ 00a4706c bytes 41330894
- 00a47030 ["INT_ADD", "register:40f0:8", ["const:a47030:8", "const:4:8"]]
- 00a47030 ["CALL", null, ["callee:00c53da0:8"]]
+ 00a47084 ["INT_ADD", "register:40f0:8", ["const:a47084:8", "const:4:8"]]
+ 00a47084 ["CALL", null, ["callee:00c53da0:8"]]
- 00a47030 bytes 34330894
+ 00a47084 bytes 47330894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f06c5415c8fc6cc1bd9a4675e062065f"></a>

### [`00a47104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47104.md) → [`00a47158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47158.md) FUN_00a47158

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0046767c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046767c.md) [`004676e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/004676e0.md) [`00467718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467718.md) [`00467824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467824.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004676bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004676bc.md) [`00467720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467720.md) [`00467758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467758.md) [`00467864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467864.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a4730c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47104.md#insn-00a4730c) · [`00a47328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47104.md#insn-00a47328) · [`00a47334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47104.md#insn-00a47334)
- 新版 `00a47360`（命令位置の公開資料なし） · `00a4737c`（命令位置の公開資料なし） · `00a47388`（命令位置の公開資料なし）

~~~diff
- 00a4730c ["INT_ADD", "register:40f0:8", ["const:a4730c:8", "const:4:8"]]
- 00a4730c ["CALL", null, ["callee:00467720:8"]]
+ 00a47360 ["INT_ADD", "register:40f0:8", ["const:a47360:8", "const:4:8"]]
+ 00a47360 ["CALL", null, ["callee:00467720:8"]]
- 00a4730c bytes f580e897
+ 00a47360 bytes f080e897
- 00a47328 ["INT_ADD", "register:40f0:8", ["const:a47328:8", "const:4:8"]]
- 00a47328 ["CALL", null, ["callee:004676bc:8"]]
+ 00a4737c ["INT_ADD", "register:40f0:8", ["const:a4737c:8", "const:4:8"]]
+ 00a4737c ["CALL", null, ["callee:004676bc:8"]]
- 00a47328 bytes d580e897
+ 00a4737c bytes d080e897
- 00a47334 ["INT_ADD", "register:40f0:8", ["const:a47334:8", "const:4:8"]]
- 00a47334 ["CALL", null, ["callee:00467758:8"]]
+ 00a47388 ["INT_ADD", "register:40f0:8", ["const:a47388:8", "const:4:8"]]
+ 00a47388 ["CALL", null, ["callee:00467758:8"]]
- 00a47334 bytes f980e897
+ 00a47388 bytes f480e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0de611f7f3cb23e47ca7a1fcd35bce4"></a>

### [`00a473f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a473f4.md) → [`00a47448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47448.md) FUN_00a47448

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`0046a9fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a9fc.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`0046aa3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046aa3c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a47418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a473f4.md#insn-00a47418) · [`00a4741c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a473f4.md#insn-00a4741c) · [`00a47450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a473f4.md#insn-00a47450)
- 新版 `00a4746c`（命令位置の公開資料なし） · `00a47470`（命令位置の公開資料なし） · `00a474a4`（命令位置の公開資料なし）

~~~diff
- 00a47418 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a47418 ["INT_ADD", "register:40f0:8", ["const:a47418:8", "const:4:8"]]
- 00a47418 ["CALLIND", null, ["register:0:8"]]
+ 00a4746c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a4746c ["INT_ADD", "register:40f0:8", ["const:a4746c:8", "const:4:8"]]
+ 00a4746c ["CALLIND", null, ["register:0:8"]]
- 00a47418 bytes 00013fd6
+ 00a4746c bytes 00013fd6
- 00a4741c ["INT_ADD", "register:40f0:8", ["const:a4741c:8", "const:4:8"]]
- 00a4741c ["CALL", null, ["callee:004678a0:8"]]
+ 00a47470 ["INT_ADD", "register:40f0:8", ["const:a47470:8", "const:4:8"]]
+ 00a47470 ["CALL", null, ["callee:004678a0:8"]]
- 00a4741c bytes 1181e897
+ 00a47470 bytes 0c81e897
- 00a47450 ["INT_ADD", "register:40f0:8", ["const:a47450:8", "const:4:8"]]
- 00a47450 ["CALL", null, ["callee:00467b6c:8"]]
+ 00a474a4 ["INT_ADD", "register:40f0:8", ["const:a474a4:8", "const:4:8"]]
+ 00a474a4 ["CALL", null, ["callee:00467b6c:8"]]
- 00a47450 bytes b781e897
+ 00a474a4 bytes b281e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a4845f78f14cbcef795c046007d51fd"></a>

### [`00a4754c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a4754c.md) → [`00a475a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a475a0.md) FUN_00a475a0

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 25件 [`005c8efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c8/005c8efc.md) [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`006064d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/006064d4.md) [`00659e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00659/00659e9c.md) [`0065be2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065b/0065be2c.md) · 呼出先 5件 [`00a46650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46650.md) [`00a46c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46c34.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 25件 [`005c8f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8f3c.md) [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00606514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606514.md) [`00659edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00659/00659edc.md) [`0065be6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065b/0065be6c.md) · 呼出先 5件 [`00a466a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a466a4.md) [`00a46c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46c88.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a47590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a4754c.md#insn-00a47590) · [`00a475a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a4754c.md#insn-00a475a8) · [`00a475c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a4754c.md#insn-00a475c0)
- 新版 `00a475e4`（命令位置の公開資料なし） · `00a475fc`（命令位置の公開資料なし） · `00a47614`（命令位置の公開資料なし）

~~~diff
- 00a47590 ["INT_ADD", "register:40f0:8", ["const:a47590:8", "const:4:8"]]
- 00a47590 ["CALL", null, ["callee:00a466a4:8"]]
+ 00a475e4 ["INT_ADD", "register:40f0:8", ["const:a475e4:8", "const:4:8"]]
+ 00a475e4 ["CALL", null, ["callee:00a466a4:8"]]
- 00a47590 bytes 30fcff97
+ 00a475e4 bytes 30fcff97
- 00a475a8 ["INT_ADD", "register:40f0:8", ["const:a475a8:8", "const:4:8"]]
- 00a475a8 ["CALL", null, ["callee:00c53d70:8"]]
+ 00a475fc ["INT_ADD", "register:40f0:8", ["const:a475fc:8", "const:4:8"]]
+ 00a475fc ["CALL", null, ["callee:00c53d70:8"]]
- 00a475a8 bytes ca310894
+ 00a475fc bytes dd310894
- 00a475c0 ["INT_ADD", "register:40f0:8", ["const:a475c0:8", "const:4:8"]]
- 00a475c0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00a47614 ["INT_ADD", "register:40f0:8", ["const:a47614:8", "const:4:8"]]
+ 00a47614 ["CALL", null, ["callee:00c53da0:8"]]
- 00a475c0 bytes d0310894
+ 00a47614 bytes e3310894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b22f5a52cdfe2dcfbdba85dd959a44f9"></a>

### [`00a47634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47634.md) → [`00a47688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47688.md) FUN_00a47688

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0046767c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046767c.md) [`004676e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/004676e0.md) [`00467718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467718.md) [`00467824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467824.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004676bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004676bc.md) [`00467720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467720.md) [`00467758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467758.md) [`00467864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467864.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a4780c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47634.md#insn-00a4780c) · [`00a47828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47634.md#insn-00a47828) · [`00a47834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47634.md#insn-00a47834)
- 新版 `00a47860`（命令位置の公開資料なし） · `00a4787c`（命令位置の公開資料なし） · `00a47888`（命令位置の公開資料なし）

~~~diff
- 00a4780c ["INT_ADD", "register:40f0:8", ["const:a4780c:8", "const:4:8"]]
- 00a4780c ["CALL", null, ["callee:00467720:8"]]
+ 00a47860 ["INT_ADD", "register:40f0:8", ["const:a47860:8", "const:4:8"]]
+ 00a47860 ["CALL", null, ["callee:00467720:8"]]
- 00a4780c bytes b57fe897
+ 00a47860 bytes b07fe897
- 00a47828 ["INT_ADD", "register:40f0:8", ["const:a47828:8", "const:4:8"]]
- 00a47828 ["CALL", null, ["callee:004676bc:8"]]
+ 00a4787c ["INT_ADD", "register:40f0:8", ["const:a4787c:8", "const:4:8"]]
+ 00a4787c ["CALL", null, ["callee:004676bc:8"]]
- 00a47828 bytes 957fe897
+ 00a4787c bytes 907fe897
- 00a47834 ["INT_ADD", "register:40f0:8", ["const:a47834:8", "const:4:8"]]
- 00a47834 ["CALL", null, ["callee:00467758:8"]]
+ 00a47888 ["INT_ADD", "register:40f0:8", ["const:a47888:8", "const:4:8"]]
+ 00a47888 ["CALL", null, ["callee:00467758:8"]]
- 00a47834 bytes b97fe897
+ 00a47888 bytes b47fe897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-881f6dc54fbf7da3f20c95f302a323e6"></a>

### [`00a478f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a478f4.md) → [`00a47948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47948.md) FUN_00a47948

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`0046965c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`0046969c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/0046969c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a47914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a478f4.md#insn-00a47914) · [`00a47918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a478f4.md#insn-00a47918) · [`00a4794c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a478f4.md#insn-00a4794c)
- 新版 `00a47968`（命令位置の公開資料なし） · `00a4796c`（命令位置の公開資料なし） · `00a479a0`（命令位置の公開資料なし）

~~~diff
- 00a47914 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a47914 ["INT_ADD", "register:40f0:8", ["const:a47914:8", "const:4:8"]]
- 00a47914 ["CALLIND", null, ["register:0:8"]]
+ 00a47968 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a47968 ["INT_ADD", "register:40f0:8", ["const:a47968:8", "const:4:8"]]
+ 00a47968 ["CALLIND", null, ["register:0:8"]]
- 00a47914 bytes 00013fd6
+ 00a47968 bytes 00013fd6
- 00a47918 ["INT_ADD", "register:40f0:8", ["const:a47918:8", "const:4:8"]]
- 00a47918 ["CALL", null, ["callee:004678a0:8"]]
+ 00a4796c ["INT_ADD", "register:40f0:8", ["const:a4796c:8", "const:4:8"]]
+ 00a4796c ["CALL", null, ["callee:004678a0:8"]]
- 00a47918 bytes d27fe897
+ 00a4796c bytes cd7fe897
- 00a4794c ["INT_ADD", "register:40f0:8", ["const:a4794c:8", "const:4:8"]]
- 00a4794c ["CALL", null, ["callee:00467b6c:8"]]
+ 00a479a0 ["INT_ADD", "register:40f0:8", ["const:a479a0:8", "const:4:8"]]
+ 00a479a0 ["CALL", null, ["callee:00467b6c:8"]]
- 00a4794c bytes 7880e897
+ 00a479a0 bytes 7380e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8979a84983b4f84514117e2515601dfd"></a>

### [`00a5e38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e38c.md) → [`00a5e3fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a5e/00a5e3fc.md) FUN_00a5e3fc

採用 · 移動量 `+0x70` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a52e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a52/00a52e30.md) · 呼出先 1件 [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md)
- 新版 呼出元 1件 [`00a52ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a52/00a52ea0.md) · 呼出先 1件 [`0046ef38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ef38.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5e3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e38c.md#insn-00a5e3a0) · [`00a5e3ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e38c.md#insn-00a5e3ac) · [`00a5e3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e38c.md#insn-00a5e3b8)
- 新版 `00a5e410`（命令位置の公開資料なし） · `00a5e41c`（命令位置の公開資料なし） · `00a5e428`（命令位置の公開資料なし）

~~~diff
- 00a5e3a0 ["INT_ADD", "register:40f0:8", ["const:a5e3a0:8", "const:4:8"]]
- 00a5e3a0 ["CALL", null, ["callee:0046ef38:8"]]
+ 00a5e410 ["INT_ADD", "register:40f0:8", ["const:a5e410:8", "const:4:8"]]
+ 00a5e410 ["CALL", null, ["callee:0046ef38:8"]]
- 00a5e3a0 bytes d642e897
+ 00a5e410 bytes ca42e897
- 00a5e3ac ["INT_ADD", "register:40f0:8", ["const:a5e3ac:8", "const:4:8"]]
- 00a5e3ac ["CALL", null, ["callee:0046ef38:8"]]
+ 00a5e41c ["INT_ADD", "register:40f0:8", ["const:a5e41c:8", "const:4:8"]]
+ 00a5e41c ["CALL", null, ["callee:0046ef38:8"]]
- 00a5e3ac bytes d342e897
+ 00a5e41c bytes c742e897
- 00a5e3b8 ["INT_ADD", "register:40f0:8", ["const:a5e3b8:8", "const:4:8"]]
- 00a5e3b8 ["CALL", null, ["callee:0046ef38:8"]]
+ 00a5e428 ["INT_ADD", "register:40f0:8", ["const:a5e428:8", "const:4:8"]]
+ 00a5e428 ["CALL", null, ["callee:0046ef38:8"]]
- 00a5e3b8 bytes d042e897
+ 00a5e428 bytes c442e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79896841eb9b951922ee907ee78f0f15"></a>

### [`00a5e4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e4c4.md) → [`00a5e534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a5e/00a5e534.md) FUN_00a5e534

採用 · 移動量 `+0x70` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a52e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a52/00a52e30.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00781044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00781/00781044.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00a52ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a52/00a52ea0.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0078109c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00781/0078109c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5e520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e4c4.md#insn-00a5e520) · [`00a5e530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e4c4.md#insn-00a5e530) · [`00a5e564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e4c4.md#insn-00a5e564)
- 新版 `00a5e590`（命令位置の公開資料なし） · `00a5e5a0`（命令位置の公開資料なし） · `00a5e5d4`（命令位置の公開資料なし）

~~~diff
- 00a5e520 ["INT_ADD", "register:40f0:8", ["const:a5e520:8", "const:4:8"]]
- 00a5e520 ["CALL", null, ["callee:0043bb60:8"]]
+ 00a5e590 ["INT_ADD", "register:40f0:8", ["const:a5e590:8", "const:4:8"]]
+ 00a5e590 ["CALL", null, ["callee:0043bb60:8"]]
- 00a5e520 bytes 8075e797
+ 00a5e590 bytes 7475e797
- 00a5e530 ["INT_ADD", "register:40f0:8", ["const:a5e530:8", "const:4:8"]]
- 00a5e530 ["CALL", null, ["callee:0043bb60:8"]]
+ 00a5e5a0 ["INT_ADD", "register:40f0:8", ["const:a5e5a0:8", "const:4:8"]]
+ 00a5e5a0 ["CALL", null, ["callee:0043bb60:8"]]
- 00a5e530 bytes 7c75e797
+ 00a5e5a0 bytes 7075e797
- 00a5e564 ["INT_ADD", "register:40f0:8", ["const:a5e564:8", "const:4:8"]]
- 00a5e564 ["CALL", null, ["callee:0078109c:8"]]
+ 00a5e5d4 ["INT_ADD", "register:40f0:8", ["const:a5e5d4:8", "const:4:8"]]
+ 00a5e5d4 ["CALL", null, ["callee:0078109c:8"]]
- 00a5e564 bytes b88af497
+ 00a5e5d4 bytes b28af497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad5ce1453b3e80c76ea9346500c6969c"></a>

### [`00a5e5f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e5f8.md) → [`00a5e668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a5e/00a5e668.md) FUN_00a5e668

採用 · 移動量 `+0x70` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a5e914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e914.md) · 呼出先 1件 [`00682218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682218.md)
- 新版 呼出元 1件 [`00a5e984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a5e/00a5e984.md) · 呼出先 1件 [`00682258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00682/00682258.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5e610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e5f8.md#insn-00a5e610) · [`00a5e61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e5f8.md#insn-00a5e61c) · [`00a5e628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e5f8.md#insn-00a5e628)
- 新版 `00a5e680`（命令位置の公開資料なし） · `00a5e68c`（命令位置の公開資料なし） · `00a5e698`（命令位置の公開資料なし）

~~~diff
- 00a5e610 ["INT_ADD", "register:40f0:8", ["const:a5e610:8", "const:4:8"]]
- 00a5e610 ["CALL", null, ["callee:00682258:8"]]
+ 00a5e680 ["INT_ADD", "register:40f0:8", ["const:a5e680:8", "const:4:8"]]
+ 00a5e680 ["CALL", null, ["callee:00682258:8"]]
- 00a5e610 bytes 028ff097
+ 00a5e680 bytes f68ef097
- 00a5e61c ["INT_ADD", "register:40f0:8", ["const:a5e61c:8", "const:4:8"]]
- 00a5e61c ["CALL", null, ["callee:00682258:8"]]
+ 00a5e68c ["INT_ADD", "register:40f0:8", ["const:a5e68c:8", "const:4:8"]]
+ 00a5e68c ["CALL", null, ["callee:00682258:8"]]
- 00a5e61c bytes ff8ef097
+ 00a5e68c bytes f38ef097
- 00a5e628 ["INT_ADD", "register:40f0:8", ["const:a5e628:8", "const:4:8"]]
- 00a5e628 ["CALL", null, ["callee:00682258:8"]]
+ 00a5e698 ["INT_ADD", "register:40f0:8", ["const:a5e698:8", "const:4:8"]]
+ 00a5e698 ["CALL", null, ["callee:00682258:8"]]
- 00a5e628 bytes fc8ef097
+ 00a5e698 bytes f08ef097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1616d63213d5f732f6eb7b6351aff3bc"></a>

### [`00a5e70c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e70c.md) → [`00a5e77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a5e/00a5e77c.md) FUN_00a5e77c

採用 · 移動量 `+0x70` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a5e914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e914.md) · 呼出先 1件 [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md)
- 新版 呼出元 1件 [`00a5e984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a5e/00a5e984.md) · 呼出先 1件 [`0046f01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f01c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5e720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e70c.md#insn-00a5e720) · [`00a5e728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e70c.md#insn-00a5e728) · [`00a5e730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e70c.md#insn-00a5e730)
- 新版 `00a5e790`（命令位置の公開資料なし） · `00a5e798`（命令位置の公開資料なし） · `00a5e7a0`（命令位置の公開資料なし）

~~~diff
- 00a5e720 ["INT_ADD", "register:40f0:8", ["const:a5e720:8", "const:4:8"]]
- 00a5e720 ["CALL", null, ["callee:0046f01c:8"]]
+ 00a5e790 ["INT_ADD", "register:40f0:8", ["const:a5e790:8", "const:4:8"]]
+ 00a5e790 ["CALL", null, ["callee:0046f01c:8"]]
- 00a5e720 bytes 2f42e897
+ 00a5e790 bytes 2342e897
- 00a5e728 ["INT_ADD", "register:40f0:8", ["const:a5e728:8", "const:4:8"]]
- 00a5e728 ["CALL", null, ["callee:0046f01c:8"]]
+ 00a5e798 ["INT_ADD", "register:40f0:8", ["const:a5e798:8", "const:4:8"]]
+ 00a5e798 ["CALL", null, ["callee:0046f01c:8"]]
- 00a5e728 bytes 2d42e897
+ 00a5e798 bytes 2142e897
- 00a5e730 ["INT_ADD", "register:40f0:8", ["const:a5e730:8", "const:4:8"]]
- 00a5e730 ["CALL", null, ["callee:0046f01c:8"]]
+ 00a5e7a0 ["INT_ADD", "register:40f0:8", ["const:a5e7a0:8", "const:4:8"]]
+ 00a5e7a0 ["CALL", null, ["callee:0046f01c:8"]]
- 00a5e730 bytes 2b42e897
+ 00a5e7a0 bytes 1f42e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb3881e5f9b7901a104ef2823b97e17e"></a>

### [`00a5e7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e7cc.md) → [`00a5e83c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a5e/00a5e83c.md) FUN_00a5e83c

採用 · 移動量 `+0x70` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0046e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e8e4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e7cc.md#insn-00a5e7e0) · [`00a5e7e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e7cc.md#insn-00a5e7e8)
- 新版 `00a5e850`（命令位置の公開資料なし） · `00a5e858`（命令位置の公開資料なし）

~~~diff
- 00a5e7e0 ["INT_ADD", "register:40f0:8", ["const:a5e7e0:8", "const:4:8"]]
- 00a5e7e0 ["CALL", null, ["callee:0046e8e4:8"]]
+ 00a5e850 ["INT_ADD", "register:40f0:8", ["const:a5e850:8", "const:4:8"]]
+ 00a5e850 ["CALL", null, ["callee:0046e8e4:8"]]
- 00a5e7e0 bytes 3140e897
+ 00a5e850 bytes 2540e897
- 00a5e7e8 ["INT_ADD", "register:40f0:8", ["const:a5e7e8:8", "const:4:8"]]
- 00a5e7e8 ["CALL", null, ["callee:0046e8e4:8"]]
+ 00a5e858 ["INT_ADD", "register:40f0:8", ["const:a5e858:8", "const:4:8"]]
+ 00a5e858 ["CALL", null, ["callee:0046e8e4:8"]]
- 00a5e7e8 bytes 2f40e897
+ 00a5e858 bytes 2340e897
~~~


<a id="compare-fd5cd5d59b91d2b2cd16ee2c0ee2864b"></a>

### [`00a5e7fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e7fc.md) → [`00a5e86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a5e/00a5e86c.md) FUN_00a5e86c

採用 · 移動量 `+0x70` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0046e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e8e4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5e810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e7fc.md#insn-00a5e810) · [`00a5e818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e7fc.md#insn-00a5e818) · [`00a5e820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e7fc.md#insn-00a5e820)
- 新版 `00a5e880`（命令位置の公開資料なし） · `00a5e888`（命令位置の公開資料なし） · `00a5e890`（命令位置の公開資料なし）

~~~diff
- 00a5e810 ["INT_ADD", "register:40f0:8", ["const:a5e810:8", "const:4:8"]]
- 00a5e810 ["CALL", null, ["callee:0046e8e4:8"]]
+ 00a5e880 ["INT_ADD", "register:40f0:8", ["const:a5e880:8", "const:4:8"]]
+ 00a5e880 ["CALL", null, ["callee:0046e8e4:8"]]
- 00a5e810 bytes 2540e897
+ 00a5e880 bytes 1940e897
- 00a5e818 ["INT_ADD", "register:40f0:8", ["const:a5e818:8", "const:4:8"]]
- 00a5e818 ["CALL", null, ["callee:0046e8e4:8"]]
+ 00a5e888 ["INT_ADD", "register:40f0:8", ["const:a5e888:8", "const:4:8"]]
+ 00a5e888 ["CALL", null, ["callee:0046e8e4:8"]]
- 00a5e818 bytes 2340e897
+ 00a5e888 bytes 1740e897
- 00a5e820 ["INT_ADD", "register:40f0:8", ["const:a5e820:8", "const:4:8"]]
- 00a5e820 ["CALL", null, ["callee:0046e8e4:8"]]
+ 00a5e890 ["INT_ADD", "register:40f0:8", ["const:a5e890:8", "const:4:8"]]
+ 00a5e890 ["CALL", null, ["callee:0046e8e4:8"]]
- 00a5e820 bytes 2140e897
+ 00a5e890 bytes 1540e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-338d599f97d2d91aace1b1c11ec793fe"></a>

### [`00a5e83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e83c.md) → [`00a5e8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a5e/00a5e8ac.md) FUN_00a5e8ac

採用 · 移動量 `+0x70` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5e874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e83c.md#insn-00a5e874) · [`00a5e888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e83c.md#insn-00a5e888) · [`00a5e890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e83c.md#insn-00a5e890)
- 新版 `00a5e8e4`（命令位置の公開資料なし） · `00a5e8f8`（命令位置の公開資料なし） · `00a5e900`（命令位置の公開資料なし）

~~~diff
- 00a5e874 ["INT_ADD", "register:40f0:8", ["const:a5e874:8", "const:4:8"]]
- 00a5e874 ["CALL", null, ["callee:00c53da0:8"]]
+ 00a5e8e4 ["INT_ADD", "register:40f0:8", ["const:a5e8e4:8", "const:4:8"]]
+ 00a5e8e4 ["CALL", null, ["callee:00c53da0:8"]]
- 00a5e874 bytes 23d50794
+ 00a5e8e4 bytes 2fd50794
- 00a5e888 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a5e888 ["INT_ADD", "register:40f0:8", ["const:a5e888:8", "const:4:8"]]
- 00a5e888 ["CALLIND", null, ["register:0:8"]]
+ 00a5e8f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a5e8f8 ["INT_ADD", "register:40f0:8", ["const:a5e8f8:8", "const:4:8"]]
+ 00a5e8f8 ["CALLIND", null, ["register:0:8"]]
- 00a5e888 bytes 00013fd6
+ 00a5e8f8 bytes 00013fd6
- 00a5e890 ["INT_ADD", "register:40f0:8", ["const:a5e890:8", "const:4:8"]]
- 00a5e890 ["CALL", null, ["callee:00c57f50:8"]]
+ 00a5e900 ["INT_ADD", "register:40f0:8", ["const:a5e900:8", "const:4:8"]]
+ 00a5e900 ["CALL", null, ["callee:00c57f50:8"]]
- 00a5e890 bytes 7ce50794
+ 00a5e900 bytes 94e50794
~~~


<a id="compare-c51ef0e1e25112c9e0a465b1fa9f19d6"></a>

### [`00a5e8a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e8a8.md) → [`00a5e918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a5e/00a5e918.md) FUN_00a5e918

採用 · 移動量 `+0x70` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5e8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e8a8.md#insn-00a5e8e0) · [`00a5e8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e8a8.md#insn-00a5e8f4) · [`00a5e8fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e8a8.md#insn-00a5e8fc)
- 新版 `00a5e950`（命令位置の公開資料なし） · `00a5e964`（命令位置の公開資料なし） · `00a5e96c`（命令位置の公開資料なし）

~~~diff
- 00a5e8e0 ["INT_ADD", "register:40f0:8", ["const:a5e8e0:8", "const:4:8"]]
- 00a5e8e0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00a5e950 ["INT_ADD", "register:40f0:8", ["const:a5e950:8", "const:4:8"]]
+ 00a5e950 ["CALL", null, ["callee:00c53da0:8"]]
- 00a5e8e0 bytes 08d50794
+ 00a5e950 bytes 14d50794
- 00a5e8f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a5e8f4 ["INT_ADD", "register:40f0:8", ["const:a5e8f4:8", "const:4:8"]]
- 00a5e8f4 ["CALLIND", null, ["register:0:8"]]
+ 00a5e964 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a5e964 ["INT_ADD", "register:40f0:8", ["const:a5e964:8", "const:4:8"]]
+ 00a5e964 ["CALLIND", null, ["register:0:8"]]
- 00a5e8f4 bytes 00013fd6
+ 00a5e964 bytes 00013fd6
- 00a5e8fc ["INT_ADD", "register:40f0:8", ["const:a5e8fc:8", "const:4:8"]]
- 00a5e8fc ["CALL", null, ["callee:00c57f50:8"]]
+ 00a5e96c ["INT_ADD", "register:40f0:8", ["const:a5e96c:8", "const:4:8"]]
+ 00a5e96c ["CALL", null, ["callee:00c57f50:8"]]
- 00a5e8fc bytes 61e50794
+ 00a5e96c bytes 79e50794
~~~


<a id="compare-108f88c583576b02c6e140a18311f388"></a>

### [`00a62238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a62/00a62238.md) → [`00a622a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a62/00a622a8.md) FUN_00a622a8

採用 · 移動量 `+0x70` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a5fce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5f/00a5fce8.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00a623e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a62/00a623e8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00a5fd58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a5f/00a5fd58.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00a62458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a62/00a62458.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a622c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a62/00a62238.md#insn-00a622c0) · [`00a62394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a62/00a62238.md#insn-00a62394) · [`00a623a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a62/00a62238.md#insn-00a623a4)
- 新版 `00a62330`（命令位置の公開資料なし） · `00a62404`（命令位置の公開資料なし） · `00a62414`（命令位置の公開資料なし）

~~~diff
- 00a622c0 ["INT_ADD", "register:40f0:8", ["const:a622c0:8", "const:4:8"]]
- 00a622c0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a62330 ["INT_ADD", "register:40f0:8", ["const:a62330:8", "const:4:8"]]
+ 00a62330 ["CALL", null, ["callee:00c57f60:8"]]
- 00a622c0 bytes f4d60794
+ 00a62330 bytes 0cd70794
- 00a62394 ["INT_ADD", "register:40f0:8", ["const:a62394:8", "const:4:8"]]
- 00a62394 ["CALL", null, ["callee:00c57f80:8"]]
+ 00a62404 ["INT_ADD", "register:40f0:8", ["const:a62404:8", "const:4:8"]]
+ 00a62404 ["CALL", null, ["callee:00c57f80:8"]]
- 00a62394 bytes c7d60794
+ 00a62404 bytes dfd60794
- 00a623a4 ["INT_ADD", "register:40f0:8", ["const:a623a4:8", "const:4:8"]]
- 00a623a4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00a62414 ["INT_ADD", "register:40f0:8", ["const:a62414:8", "const:4:8"]]
+ 00a62414 ["CALL", null, ["callee:00c57f80:8"]]
- 00a623a4 bytes c3d60794
+ 00a62414 bytes dbd60794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01008c218f44b1654bcc7e4253dc09d5"></a>

### [`00a62a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a62/00a62a18.md) → [`00a62a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a62/00a62a88.md) FUN_00a62a88

採用 · 移動量 `+0x70` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00a628fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a62/00a628fc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00a6296c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a62/00a6296c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a62a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a62/00a62a18.md#insn-00a62a28)
- 新版 `00a62a98`（命令位置の公開資料なし）

~~~diff
- 00a62a28 ["INT_ADD", "register:40f0:8", ["const:a62a28:8", "const:4:8"]]
- 00a62a28 ["CALL", null, ["callee:00a6296c:8"]]
+ 00a62a98 ["INT_ADD", "register:40f0:8", ["const:a62a98:8", "const:4:8"]]
+ 00a62a98 ["CALL", null, ["callee:00a6296c:8"]]
- 00a62a28 bytes b5ffff97
+ 00a62a98 bytes b5ffff97
~~~


<a id="compare-0f1fadb2d8593f868176a6eccb175656"></a>

### [`00a6436c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a6436c.md) → [`00a643dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a64/00a643dc.md) FUN_00a643dc

採用 · 移動量 `+0x70` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009d5cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d5/009d5cf8.md) · 呼出先 1件 [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md)
- 新版 呼出元 1件 [`009d5d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d5/009d5d4c.md) · 呼出先 1件 [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a643a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a6436c.md#insn-00a643a4) · [`00a643b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a6436c.md#insn-00a643b8)
- 新版 `00a64414`（命令位置の公開資料なし） · `00a64428`（命令位置の公開資料なし）

~~~diff
- 00a643a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a643a4 ["INT_ADD", "register:40f0:8", ["const:a643a4:8", "const:4:8"]]
- 00a643a4 ["CALLIND", null, ["register:0:8"]]
+ 00a64414 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a64414 ["INT_ADD", "register:40f0:8", ["const:a64414:8", "const:4:8"]]
+ 00a64414 ["CALLIND", null, ["register:0:8"]]
- 00a643a4 bytes 00013fd6
+ 00a64414 bytes 00013fd6
- 00a643b8 ["INT_ADD", "register:40f0:8", ["const:a643b8:8", "const:4:8"]]
- 00a643b8 ["CALL", null, ["callee:0048797c:8"]]
+ 00a64428 ["INT_ADD", "register:40f0:8", ["const:a64428:8", "const:4:8"]]
+ 00a64428 ["CALL", null, ["callee:0048797c:8"]]
- 00a643b8 bytes 618de897
+ 00a64428 bytes 558de897
~~~


<a id="compare-36a927627e3b7a39546dac8457305d89"></a>

### [`00a643f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a643f4.md) → [`00a64464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a64/00a64464.md) FUN_00a64464

採用 · 移動量 `+0x70` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a1a750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a750.md) · 呼出先 1件 [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md)
- 新版 呼出元 1件 [`00a1a7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a7a4.md) · 呼出先 1件 [`00480430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a64420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a643f4.md#insn-00a64420) · [`00a64434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a643f4.md#insn-00a64434)
- 新版 `00a64490`（命令位置の公開資料なし） · `00a644a4`（命令位置の公開資料なし）

~~~diff
- 00a64420 ["INT_ADD", "register:40f0:8", ["const:a64420:8", "const:4:8"]]
- 00a64420 ["CALL", null, ["callee:00480430:8"]]
+ 00a64490 ["INT_ADD", "register:40f0:8", ["const:a64490:8", "const:4:8"]]
+ 00a64490 ["CALL", null, ["callee:00480430:8"]]
- 00a64420 bytes f46fe897
+ 00a64490 bytes e86fe897
- 00a64434 ["INT_ADD", "register:40f0:8", ["const:a64434:8", "const:4:8"]]
- 00a64434 ["CALL", null, ["callee:00480430:8"]]
+ 00a644a4 ["INT_ADD", "register:40f0:8", ["const:a644a4:8", "const:4:8"]]
+ 00a644a4 ["CALL", null, ["callee:00480430:8"]]
- 00a64434 bytes ef6fe897
+ 00a644a4 bytes e36fe897
~~~


<a id="compare-6e4b79269043919887db634801966213"></a>

### [`00a6456c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a6456c.md) → [`00a645dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a64/00a645dc.md) FUN_00a645dc

採用 · 移動量 `+0x70` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a223d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a22/00a223d0.md) · 呼出先 1件 [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md)
- 新版 呼出元 1件 [`00a22424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a22/00a22424.md) · 呼出先 1件 [`00480e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480e68.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a64588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a6456c.md#insn-00a64588) · [`00a64594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a6456c.md#insn-00a64594) · [`00a645a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a6456c.md#insn-00a645a0)
- 新版 `00a645f8`（命令位置の公開資料なし） · `00a64604`（命令位置の公開資料なし） · `00a64610`（命令位置の公開資料なし）

~~~diff
- 00a64588 ["INT_ADD", "register:40f0:8", ["const:a64588:8", "const:4:8"]]
- 00a64588 ["CALL", null, ["callee:00480e68:8"]]
+ 00a645f8 ["INT_ADD", "register:40f0:8", ["const:a645f8:8", "const:4:8"]]
+ 00a645f8 ["CALL", null, ["callee:00480e68:8"]]
- 00a64588 bytes 2872e897
+ 00a645f8 bytes 1c72e897
- 00a64594 ["INT_ADD", "register:40f0:8", ["const:a64594:8", "const:4:8"]]
- 00a64594 ["CALL", null, ["callee:00480e68:8"]]
+ 00a64604 ["INT_ADD", "register:40f0:8", ["const:a64604:8", "const:4:8"]]
+ 00a64604 ["CALL", null, ["callee:00480e68:8"]]
- 00a64594 bytes 2572e897
+ 00a64604 bytes 1972e897
- 00a645a0 ["INT_ADD", "register:40f0:8", ["const:a645a0:8", "const:4:8"]]
- 00a645a0 ["CALL", null, ["callee:00480e68:8"]]
+ 00a64610 ["INT_ADD", "register:40f0:8", ["const:a64610:8", "const:4:8"]]
+ 00a64610 ["CALL", null, ["callee:00480e68:8"]]
- 00a645a0 bytes 2272e897
+ 00a64610 bytes 1672e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d4e8c5333f997410173eae493584cf2"></a>

### [`00a6465c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a6465c.md) → [`00a646cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a64/00a646cc.md) FUN_00a646cc

採用 · 移動量 `+0x70` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a1a750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a750.md) · 呼出先 1件 [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md)
- 新版 呼出元 1件 [`00a1a7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a7a4.md) · 呼出先 1件 [`00480430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6467c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a6465c.md#insn-00a6467c) · [`00a64688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a6465c.md#insn-00a64688) · [`00a646a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a6465c.md#insn-00a646a4)
- 新版 `00a646ec`（命令位置の公開資料なし） · `00a646f8`（命令位置の公開資料なし） · `00a64714`（命令位置の公開資料なし）

~~~diff
- 00a6467c ["INT_ADD", "register:40f0:8", ["const:a6467c:8", "const:4:8"]]
- 00a6467c ["CALL", null, ["callee:00480430:8"]]
+ 00a646ec ["INT_ADD", "register:40f0:8", ["const:a646ec:8", "const:4:8"]]
+ 00a646ec ["CALL", null, ["callee:00480430:8"]]
- 00a6467c bytes 5d6fe897
+ 00a646ec bytes 516fe897
- 00a64688 ["INT_ADD", "register:40f0:8", ["const:a64688:8", "const:4:8"]]
- 00a64688 ["CALL", null, ["callee:00480430:8"]]
+ 00a646f8 ["INT_ADD", "register:40f0:8", ["const:a646f8:8", "const:4:8"]]
+ 00a646f8 ["CALL", null, ["callee:00480430:8"]]
- 00a64688 bytes 5a6fe897
+ 00a646f8 bytes 4e6fe897
- 00a646a4 ["INT_ADD", "register:40f0:8", ["const:a646a4:8", "const:4:8"]]
- 00a646a4 ["CALL", null, ["callee:00480430:8"]]
+ 00a64714 ["INT_ADD", "register:40f0:8", ["const:a64714:8", "const:4:8"]]
+ 00a64714 ["CALL", null, ["callee:00480430:8"]]
- 00a646a4 bytes 536fe897
+ 00a64714 bytes 476fe897
~~~


<a id="compare-2829dcc1414c5b621d6940e2febe7a1f"></a>

### [`00a646c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a646c4.md) → [`00a64734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a64/00a64734.md) FUN_00a64734

採用 · 移動量 `+0x70` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a223d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a22/00a223d0.md) · 呼出先 1件 [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md)
- 新版 呼出元 1件 [`00a22424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a22/00a22424.md) · 呼出先 1件 [`00480e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480e68.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a646e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a646c4.md#insn-00a646e4) · [`00a646f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a646c4.md#insn-00a646f0)
- 新版 `00a64754`（命令位置の公開資料なし） · `00a64760`（命令位置の公開資料なし）

~~~diff
- 00a646e4 ["INT_ADD", "register:40f0:8", ["const:a646e4:8", "const:4:8"]]
- 00a646e4 ["CALL", null, ["callee:00480e68:8"]]
+ 00a64754 ["INT_ADD", "register:40f0:8", ["const:a64754:8", "const:4:8"]]
+ 00a64754 ["CALL", null, ["callee:00480e68:8"]]
- 00a646e4 bytes d171e897
+ 00a64754 bytes c571e897
- 00a646f0 ["INT_ADD", "register:40f0:8", ["const:a646f0:8", "const:4:8"]]
- 00a646f0 ["CALL", null, ["callee:00480e68:8"]]
+ 00a64760 ["INT_ADD", "register:40f0:8", ["const:a64760:8", "const:4:8"]]
+ 00a64760 ["CALL", null, ["callee:00480e68:8"]]
- 00a646f0 bytes ce71e897
+ 00a64760 bytes c271e897
~~~


<a id="compare-e8191b816a537bd8854968651d8f401e"></a>

### [`00a64a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a64a98.md) → [`00a64b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a64/00a64b08.md) FUN_00a64b08

採用 · 移動量 `+0x70` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`005e86dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e8/005e86dc.md) [`005e90d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e9/005e90d4.md) [`005ec274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ec/005ec274.md) [`005eda7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005eda7c.md) [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 9件 [`005e871c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e8/005e871c.md) [`005e9114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e9/005e9114.md) [`005ec2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ec/005ec2b4.md) [`005edabc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ed/005edabc.md) [`005ee610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ee/005ee610.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a64aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a64a98.md#insn-00a64aa0)
- 新版 `00a64b10`（命令位置の公開資料なし）

~~~diff
- 00a64aa0 ["INT_ADD", "register:40f0:8", ["const:a64aa0:8", "const:4:8"]]
- 00a64aa0 ["CALL", null, ["callee:00851550:8"]]
+ 00a64b10 ["INT_ADD", "register:40f0:8", ["const:a64b10:8", "const:4:8"]]
+ 00a64b10 ["CALL", null, ["callee:00851550:8"]]
- 00a64aa0 bytes 96b2f797
+ 00a64b10 bytes 90b2f797
~~~


<a id="compare-f6c411b24fcbfb0d0010d642e14f431c"></a>

### [`00a64ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a64ab8.md) → [`00a64b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a64/00a64b28.md) FUN_00a64b28

採用 · 移動量 `+0x70` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005ec274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ec/005ec274.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`005ec2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ec/005ec2b4.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a64ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a64ab8.md#insn-00a64ac0)
- 新版 `00a64b30`（命令位置の公開資料なし）

~~~diff
- 00a64ac0 ["INT_ADD", "register:40f0:8", ["const:a64ac0:8", "const:4:8"]]
- 00a64ac0 ["CALL", null, ["callee:00851550:8"]]
+ 00a64b30 ["INT_ADD", "register:40f0:8", ["const:a64b30:8", "const:4:8"]]
+ 00a64b30 ["CALL", null, ["callee:00851550:8"]]
- 00a64ac0 bytes 8eb2f797
+ 00a64b30 bytes 88b2f797
~~~


<a id="compare-0372b1015a820e2d45ab1afbd6944336"></a>

### [`00a67c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a67c34.md) → [`00a67ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a67/00a67ca4.md) FUN_00a67ca4

採用 · 移動量 `+0x70` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a68394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68394.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00a68404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a68/00a68404.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a67c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a67c34.md#insn-00a67c60)
- 新版 `00a67cd0`（命令位置の公開資料なし）

~~~diff
- 00a67c60 ["INT_ADD", "register:40f0:8", ["const:a67c60:8", "const:4:8"]]
- 00a67c60 ["CALL", null, ["callee:00c57f80:8"]]
+ 00a67cd0 ["INT_ADD", "register:40f0:8", ["const:a67cd0:8", "const:4:8"]]
+ 00a67cd0 ["CALL", null, ["callee:00c57f80:8"]]
- 00a67c60 bytes 94c00794
+ 00a67cd0 bytes acc00794
~~~


<a id="compare-89cb01985c40fc611cc63d5848ce38b8"></a>

### [`00a67c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a67c80.md) → [`00a67cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a67/00a67cf0.md) FUN_00a67cf0

採用 · 移動量 `+0x70` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a64f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a64f38.md) · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00869138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869138.md) [`00a6806c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a6806c.md) [`00a68394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68394.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00a64fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a64/00a64fa8.md) · 呼出先 5件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00869190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869190.md) [`00a680dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a68/00a680dc.md) [`00a68404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a68/00a68404.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a67d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a67c80.md#insn-00a67d80) · [`00a67df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a67c80.md#insn-00a67df0) · [`00a67ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a67c80.md#insn-00a67ec0)
- 新版 `00a67df0`（命令位置の公開資料なし） · `00a67e60`（命令位置の公開資料なし） · `00a67f30`（命令位置の公開資料なし）

~~~diff
- 00a67d80 ["INT_ADD", "register:40f0:8", ["const:a67d80:8", "const:4:8"]]
- 00a67d80 ["CALL", null, ["callee:00a680dc:8"]]
+ 00a67df0 ["INT_ADD", "register:40f0:8", ["const:a67df0:8", "const:4:8"]]
+ 00a67df0 ["CALL", null, ["callee:00a680dc:8"]]
- 00a67d80 bytes bb000094
+ 00a67df0 bytes bb000094
- 00a67df0 ["INT_ADD", "register:40f0:8", ["const:a67df0:8", "const:4:8"]]
- 00a67df0 ["CALL", null, ["callee:0043bbe4:8"]]
+ 00a67e60 ["INT_ADD", "register:40f0:8", ["const:a67e60:8", "const:4:8"]]
+ 00a67e60 ["CALL", null, ["callee:0043bbe4:8"]]
- 00a67df0 bytes 6d4fe797
+ 00a67e60 bytes 614fe797
- 00a67ec0 ["INT_ADD", "register:40f0:8", ["const:a67ec0:8", "const:4:8"]]
- 00a67ec0 ["CALL", null, ["callee:00869190:8"]]
+ 00a67f30 ["INT_ADD", "register:40f0:8", ["const:a67f30:8", "const:4:8"]]
+ 00a67f30 ["CALL", null, ["callee:00869190:8"]]
- 00a67ec0 bytes 9e04f897
+ 00a67f30 bytes 9804f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ceb438422061f9e44727bf3d15d64399"></a>

### [`00a68014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68014.md) → [`00a68084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a68/00a68084.md) FUN_00a68084

採用 · 移動量 `+0x70` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00869138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869138.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00869190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869190.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6802c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68014.md#insn-00a6802c)
- 新版 `00a6809c`（命令位置の公開資料なし）

~~~diff
- 00a6802c ["INT_ADD", "register:40f0:8", ["const:a6802c:8", "const:4:8"]]
- 00a6802c ["CALL", null, ["callee:00869190:8"]]
+ 00a6809c ["INT_ADD", "register:40f0:8", ["const:a6809c:8", "const:4:8"]]
+ 00a6809c ["CALL", null, ["callee:00869190:8"]]
- 00a6802c bytes 4304f897
+ 00a6809c bytes 3d04f897
~~~


<a id="compare-12748c676cf0f15373c275d42ffed7d5"></a>

### [`00a6806c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a6806c.md) → [`00a680dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a68/00a680dc.md) FUN_00a680dc

採用 · 移動量 `+0x70` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a67c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a67c80.md) · 呼出先 4件 [`006b8c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8c44.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00a67cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a67/00a67cf0.md) · 呼出先 4件 [`006b8c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b8/006b8c9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a680b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a6806c.md#insn-00a680b0) · [`00a680f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a6806c.md#insn-00a680f8) · [`00a68130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a6806c.md#insn-00a68130)
- 新版 `00a68120`（命令位置の公開資料なし） · `00a68168`（命令位置の公開資料なし） · `00a681a0`（命令位置の公開資料なし）

~~~diff
- 00a680b0 ["INT_ADD", "register:40f0:8", ["const:a680b0:8", "const:4:8"]]
- 00a680b0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00a68120 ["INT_ADD", "register:40f0:8", ["const:a68120:8", "const:4:8"]]
+ 00a68120 ["CALL", null, ["callee:00c57f80:8"]]
- 00a680b0 bytes 80bf0794
+ 00a68120 bytes 98bf0794
- 00a680f8 ["INT_ADD", "register:40f0:8", ["const:a680f8:8", "const:4:8"]]
- 00a680f8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a68168 ["INT_ADD", "register:40f0:8", ["const:a68168:8", "const:4:8"]]
+ 00a68168 ["CALL", null, ["callee:00c57f60:8"]]
- 00a680f8 bytes 66bf0794
+ 00a68168 bytes 7ebf0794
- 00a68130 ["INT_ADD", "register:40f0:8", ["const:a68130:8", "const:4:8"]]
- 00a68130 ["CALL", null, ["callee:00c580d0:8"]]
+ 00a681a0 ["INT_ADD", "register:40f0:8", ["const:a681a0:8", "const:4:8"]]
+ 00a681a0 ["CALL", null, ["callee:00c580d0:8"]]
- 00a68130 bytes b4bf0794
+ 00a681a0 bytes ccbf0794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-deeb35763a9528bec04b4e2ee2803a82"></a>

### [`00a68394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68394.md) → [`00a68404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a68/00a68404.md) FUN_00a68404

採用 · 移動量 `+0x70` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a67c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a67c80.md) · 呼出先 6件 [`006b8c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8c44.md) [`00a67c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a67c34.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00a67cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a67/00a67cf0.md) · 呼出先 6件 [`006b8c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b8/006b8c9c.md) [`00a67ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a67/00a67ca4.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a683b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68394.md#insn-00a683b8) · [`00a683f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68394.md#insn-00a683f0) · [`00a68410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68394.md#insn-00a68410)
- 新版 `00a68428`（命令位置の公開資料なし） · `00a68460`（命令位置の公開資料なし） · `00a68480`（命令位置の公開資料なし）

~~~diff
- 00a683b8 ["INT_ADD", "register:40f0:8", ["const:a683b8:8", "const:4:8"]]
- 00a683b8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a68428 ["INT_ADD", "register:40f0:8", ["const:a68428:8", "const:4:8"]]
+ 00a68428 ["CALL", null, ["callee:00c57f60:8"]]
- 00a683b8 bytes b6be0794
+ 00a68428 bytes cebe0794
- 00a683f0 ["INT_ADD", "register:40f0:8", ["const:a683f0:8", "const:4:8"]]
- 00a683f0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a68460 ["INT_ADD", "register:40f0:8", ["const:a68460:8", "const:4:8"]]
+ 00a68460 ["CALL", null, ["callee:00c57f60:8"]]
- 00a683f0 bytes a8be0794
+ 00a68460 bytes c0be0794
- 00a68410 ["INT_ADD", "register:40f0:8", ["const:a68410:8", "const:4:8"]]
- 00a68410 ["CALL", null, ["callee:00c580d0:8"]]
+ 00a68480 ["INT_ADD", "register:40f0:8", ["const:a68480:8", "const:4:8"]]
+ 00a68480 ["CALL", null, ["callee:00c580d0:8"]]
- 00a68410 bytes fcbe0794
+ 00a68480 bytes 14bf0794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b7376a7227eb64d1126b1cceae51813"></a>

### [`00a68f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68f54.md) → [`00a68fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a68/00a68fc4.md) FUN_00a68fc4

採用 · 移動量 `+0x70` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`0060eb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060e/0060eb50.md) [`00618200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/00618200.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 2件 [`00a6c0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6c/00a6c0dc.md) [`00a6c488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6c/00a6c488.md)
- 新版 呼出元 7件 [`00605294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00605/00605294.md) [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`0060eb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0060e/0060eb90.md) [`00618240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00618/00618240.md) [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) · 呼出先 2件 [`00a6c14c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a6c/00a6c14c.md) [`00a6c4f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a6c/00a6c4f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a68f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68f54.md#insn-00a68f70) · [`00a68f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68f54.md#insn-00a68f74)
- 新版 `00a68fe0`（命令位置の公開資料なし） · `00a68fe4`（命令位置の公開資料なし）

~~~diff
- 00a68f70 ["INT_ADD", "register:40f0:8", ["const:a68f70:8", "const:4:8"]]
- 00a68f70 ["CALL", null, ["callee:00a6c4f8:8"]]
+ 00a68fe0 ["INT_ADD", "register:40f0:8", ["const:a68fe0:8", "const:4:8"]]
+ 00a68fe0 ["CALL", null, ["callee:00a6c4f8:8"]]
- 00a68f70 bytes 460d0094
+ 00a68fe0 bytes 460d0094
- 00a68f74 ["INT_ADD", "register:40f0:8", ["const:a68f74:8", "const:4:8"]]
- 00a68f74 ["CALL", null, ["callee:00a6c14c:8"]]
+ 00a68fe4 ["INT_ADD", "register:40f0:8", ["const:a68fe4:8", "const:4:8"]]
+ 00a68fe4 ["CALL", null, ["callee:00a6c14c:8"]]
- 00a68f74 bytes 5a0c0094
+ 00a68fe4 bytes 5a0c0094
~~~


<a id="compare-0fb6bc171eb4f9ec060129154cf644c8"></a>

### [`00a68f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68f88.md) → [`00a68ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a68/00a68ff8.md) FUN_00a68ff8

採用 · 移動量 `+0x70` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 2件 [`00a6c0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6c/00a6c0dc.md) [`00a6c488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6c/00a6c488.md)
- 新版 呼出元 1件 [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 2件 [`00a6c14c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a6c/00a6c14c.md) [`00a6c4f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a6c/00a6c4f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a68fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68f88.md#insn-00a68fa0) · [`00a68fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68f88.md#insn-00a68fa4)
- 新版 `00a69010`（命令位置の公開資料なし） · `00a69014`（命令位置の公開資料なし）

~~~diff
- 00a68fa0 ["INT_ADD", "register:40f0:8", ["const:a68fa0:8", "const:4:8"]]
- 00a68fa0 ["CALL", null, ["callee:00a6c4f8:8"]]
+ 00a69010 ["INT_ADD", "register:40f0:8", ["const:a69010:8", "const:4:8"]]
+ 00a69010 ["CALL", null, ["callee:00a6c4f8:8"]]
- 00a68fa0 bytes 3a0d0094
+ 00a69010 bytes 3a0d0094
- 00a68fa4 ["INT_ADD", "register:40f0:8", ["const:a68fa4:8", "const:4:8"]]
- 00a68fa4 ["CALL", null, ["callee:00a6c14c:8"]]
+ 00a69014 ["INT_ADD", "register:40f0:8", ["const:a69014:8", "const:4:8"]]
+ 00a69014 ["CALL", null, ["callee:00a6c14c:8"]]
- 00a68fa4 bytes 4e0c0094
+ 00a69014 bytes 4e0c0094
~~~


<a id="compare-3329a83276784c21ac088d0de22ef124"></a>

### [`00a69104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a69104.md) → [`00a69174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a69/00a69174.md) FUN_00a69174

採用 · 移動量 `+0x70` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a69120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a69104.md#insn-00a69120) · [`00a69140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a69104.md#insn-00a69140)
- 新版 `00a69190`（命令位置の公開資料なし） · `00a691b0`（命令位置の公開資料なし）

~~~diff
- 00a69120 ["INT_ADD", "register:40f0:8", ["const:a69120:8", "const:4:8"]]
- 00a69120 ["CALL", null, ["callee:00c53da0:8"]]
+ 00a69190 ["INT_ADD", "register:40f0:8", ["const:a69190:8", "const:4:8"]]
+ 00a69190 ["CALL", null, ["callee:00c53da0:8"]]
- 00a69120 bytes f8aa0794
+ 00a69190 bytes 04ab0794
- 00a69140 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a69140 ["INT_ADD", "register:40f0:8", ["const:a69140:8", "const:4:8"]]
- 00a69140 ["CALLIND", null, ["register:0:8"]]
+ 00a691b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a691b0 ["INT_ADD", "register:40f0:8", ["const:a691b0:8", "const:4:8"]]
+ 00a691b0 ["CALLIND", null, ["register:0:8"]]
- 00a69140 bytes 00013fd6
+ 00a691b0 bytes 00013fd6
~~~


<a id="compare-7d7da7a976597e558de86082d7b7a755"></a>

### [`00a693a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a693a4.md) → [`00a69414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a69/00a69414.md) FUN_00a69414

採用 · 移動量 `+0x70` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a693c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a693a4.md#insn-00a693c0) · [`00a693e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a693a4.md#insn-00a693e0)
- 新版 `00a69430`（命令位置の公開資料なし） · `00a69450`（命令位置の公開資料なし）

~~~diff
- 00a693c0 ["INT_ADD", "register:40f0:8", ["const:a693c0:8", "const:4:8"]]
- 00a693c0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00a69430 ["INT_ADD", "register:40f0:8", ["const:a69430:8", "const:4:8"]]
+ 00a69430 ["CALL", null, ["callee:00c53da0:8"]]
- 00a693c0 bytes 50aa0794
+ 00a69430 bytes 5caa0794
- 00a693e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a693e0 ["INT_ADD", "register:40f0:8", ["const:a693e0:8", "const:4:8"]]
- 00a693e0 ["CALLIND", null, ["register:0:8"]]
+ 00a69450 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a69450 ["INT_ADD", "register:40f0:8", ["const:a69450:8", "const:4:8"]]
+ 00a69450 ["CALLIND", null, ["register:0:8"]]
- 00a693e0 bytes 00013fd6
+ 00a69450 bytes 00013fd6
~~~


<a id="compare-c937986ac2a3bd504b56d6fd1458b29a"></a>

### [`00a6947c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a6947c.md) → [`00a694ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a69/00a694ec.md) FUN_00a694ec

採用 · 移動量 `+0x70` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) · 呼出先 1件 [`0086bdb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bdb8.md)
- 新版 呼出元 1件 [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) · 呼出先 1件 [`0086be10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086be10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a69494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a6947c.md#insn-00a69494)
- 新版 `00a69504`（命令位置の公開資料なし）

~~~diff
- 00a69494 ["INT_ADD", "register:40f0:8", ["const:a69494:8", "const:4:8"]]
- 00a69494 ["CALL", null, ["callee:0086be10:8"]]
+ 00a69504 ["INT_ADD", "register:40f0:8", ["const:a69504:8", "const:4:8"]]
+ 00a69504 ["CALL", null, ["callee:0086be10:8"]]
- 00a69494 bytes 490af897
+ 00a69504 bytes 430af897
~~~


