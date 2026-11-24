# v16.0.1 → v16.0.2 · 要調査の変更候補 (23)

[一覧の目次](README.md)

<a id="compare-a97a9d3b1ee3c0f351479d3f60702f81"></a>

### [`007a1c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1c44.md) → [`007a1c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1c9c.md) FUN_007a1c9c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007a0034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0034.md) [`007a0fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0fa0.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`007a1ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1ab0.md) [`007a1e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1e6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`007a008c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a008c.md) [`007a0ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0ff8.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`007a1b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1b08.md) [`007a1ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1ec4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a1ce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1c44.md#insn-007a1ce4) · [`007a1d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1c44.md#insn-007a1d0c) · [`007a1db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1c44.md#insn-007a1db8)
- 新版 `007a1d3c`（命令位置の公開資料なし） · `007a1d64`（命令位置の公開資料なし） · `007a1e10`（命令位置の公開資料なし）

~~~diff
- 007a1ce4 ["INT_ADD", "register:40f0:8", ["const:7a1ce4:8", "const:4:8"]]
- 007a1ce4 ["CALL", null, ["callee:00c57f60:8"]]
+ 007a1d3c ["INT_ADD", "register:40f0:8", ["const:7a1d3c:8", "const:4:8"]]
+ 007a1d3c ["CALL", null, ["callee:00c57f60:8"]]
- 007a1ce4 bytes 6bd81294
+ 007a1d3c bytes 89d81294
- 007a1d0c ["INT_ADD", "register:40f0:8", ["const:7a1d0c:8", "const:4:8"]]
- 007a1d0c ["CALL", null, ["callee:007a1ec4:8"]]
+ 007a1d64 ["INT_ADD", "register:40f0:8", ["const:7a1d64:8", "const:4:8"]]
+ 007a1d64 ["CALL", null, ["callee:007a1ec4:8"]]
- 007a1d0c bytes 58000094
+ 007a1d64 bytes 58000094
- 007a1db8 ["INT_ADD", "register:40f0:8", ["const:7a1db8:8", "const:4:8"]]
- 007a1db8 ["CALL", null, ["callee:00c57f80:8"]]
+ 007a1e10 ["INT_ADD", "register:40f0:8", ["const:7a1e10:8", "const:4:8"]]
+ 007a1e10 ["CALL", null, ["callee:00c57f80:8"]]
- 007a1db8 bytes 3ed81294
+ 007a1e10 bytes 5cd81294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ccb15a74122adb45f9fdf7471ce49ba"></a>

### [`007a1e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1e6c.md) → [`007a1ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1ec4.md) FUN_007a1ec4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007a0034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0034.md) [`007a0fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0fa0.md) [`007a1c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1c44.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`007a008c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a008c.md) [`007a0ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0ff8.md) [`007a1c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1c9c.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a1ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1e6c.md#insn-007a1ecc) · [`007a1f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1e6c.md#insn-007a1f10) · [`007a1f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1e6c.md#insn-007a1f28)
- 新版 `007a1f24`（命令位置の公開資料なし） · `007a1f68`（命令位置の公開資料なし） · `007a1f80`（命令位置の公開資料なし）

~~~diff
- 007a1ecc ["INT_ADD", "register:40f0:8", ["const:7a1ecc:8", "const:4:8"]]
- 007a1ecc ["CALL", null, ["callee:0043bb60:8"]]
+ 007a1f24 ["INT_ADD", "register:40f0:8", ["const:7a1f24:8", "const:4:8"]]
+ 007a1f24 ["CALL", null, ["callee:0043bb60:8"]]
- 007a1ecc bytes 1567f297
+ 007a1f24 bytes 0f67f297
- 007a1f10 ["INT_ADD", "register:40f0:8", ["const:7a1f10:8", "const:4:8"]]
- 007a1f10 ["CALL", null, ["callee:00c57f60:8"]]
+ 007a1f68 ["INT_ADD", "register:40f0:8", ["const:7a1f68:8", "const:4:8"]]
+ 007a1f68 ["CALL", null, ["callee:00c57f60:8"]]
- 007a1f10 bytes e0d71294
+ 007a1f68 bytes fed71294
- 007a1f28 ["INT_ADD", "register:40f0:8", ["const:7a1f28:8", "const:4:8"]]
- 007a1f28 ["CALL", null, ["callee:00c580d0:8"]]
+ 007a1f80 ["INT_ADD", "register:40f0:8", ["const:7a1f80:8", "const:4:8"]]
+ 007a1f80 ["CALL", null, ["callee:00c580d0:8"]]
- 007a1f28 bytes 36d81294
+ 007a1f80 bytes 54d81294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-254247d4caed7ae9db39753943691cef"></a>

### [`007a1f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1f88.md) → [`007a1fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1fe0.md) FUN_007a1fe0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a1fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1f88.md#insn-007a1fc4) · [`007a1fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1f88.md#insn-007a1fd4)
- 新版 `007a201c`（命令位置の公開資料なし） · `007a202c`（命令位置の公開資料なし）

~~~diff
- 007a1fc4 ["INT_ADD", "register:40f0:8", ["const:7a1fc4:8", "const:4:8"]]
- 007a1fc4 ["CALL", null, ["callee:00c57f80:8"]]
+ 007a201c ["INT_ADD", "register:40f0:8", ["const:7a201c:8", "const:4:8"]]
+ 007a201c ["CALL", null, ["callee:00c57f80:8"]]
- 007a1fc4 bytes bbd71294
+ 007a201c bytes d9d71294
- 007a1fd4 ["INT_ADD", "register:40f0:8", ["const:7a1fd4:8", "const:4:8"]]
- 007a1fd4 ["CALL", null, ["callee:00c57f80:8"]]
+ 007a202c ["INT_ADD", "register:40f0:8", ["const:7a202c:8", "const:4:8"]]
+ 007a202c ["CALL", null, ["callee:00c57f80:8"]]
- 007a1fd4 bytes b7d71294
+ 007a202c bytes d5d71294
~~~


<a id="compare-6c75d3894f47a086df1f365997013828"></a>

### [`007a2004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a2/007a2004.md) → [`007a205c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a2/007a205c.md) FUN_007a205c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007a1110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1110.md) [`007a2004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a2/007a2004.md) · 呼出先 19件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) [`007a0708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0708.md) [`007a2004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a2/007a2004.md)
- 新版 呼出元 2件 [`007a1168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1168.md) [`007a205c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a2/007a205c.md) · 呼出先 19件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00597acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597acc.md) [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) [`007a0760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0760.md) [`007a205c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a2/007a205c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a20cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a2/007a2004.md#insn-007a20cc) · [`007a20f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a2/007a2004.md#insn-007a20f0) · [`007a2108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a2/007a2004.md#insn-007a2108)
- 新版 `007a2124`（命令位置の公開資料なし） · `007a2148`（命令位置の公開資料なし） · `007a2160`（命令位置の公開資料なし）

~~~diff
- 007a20cc ["INT_ADD", "register:40f0:8", ["const:7a20cc:8", "const:4:8"]]
- 007a20cc ["CALL", null, ["callee:007a5298:8"]]
+ 007a2124 ["INT_ADD", "register:40f0:8", ["const:7a2124:8", "const:4:8"]]
+ 007a2124 ["CALL", null, ["callee:007a5298:8"]]
- 007a20cc bytes 5d0c0094
+ 007a2124 bytes 5d0c0094
- 007a20f0 ["INT_ADD", "register:40f0:8", ["const:7a20f0:8", "const:4:8"]]
- 007a20f0 ["CALL", null, ["callee:007a5298:8"]]
+ 007a2148 ["INT_ADD", "register:40f0:8", ["const:7a2148:8", "const:4:8"]]
+ 007a2148 ["CALL", null, ["callee:007a5298:8"]]
- 007a20f0 bytes 540c0094
+ 007a2148 bytes 540c0094
- 007a2108 ["INT_ADD", "register:40f0:8", ["const:7a2108:8", "const:4:8"]]
- 007a2108 ["CALL", null, ["callee:007a5298:8"]]
+ 007a2160 ["INT_ADD", "register:40f0:8", ["const:7a2160:8", "const:4:8"]]
+ 007a2160 ["CALL", null, ["callee:007a5298:8"]]
- 007a2108 bytes 4e0c0094
+ 007a2160 bytes 4e0c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a90500c5abb243caee5b5081c16f22a2"></a>

### [`007a3578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a3/007a3578.md) → [`007a35d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a3/007a35d0.md) FUN_007a35d0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`007a2004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a2/007a2004.md) [`007a3708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a3/007a3708.md) [`007a41dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a4/007a41dc.md) [`007a5240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a5/007a5240.md) [`007a6128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a6/007a6128.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 8件 [`007a205c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a2/007a205c.md) [`007a3760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a3/007a3760.md) [`007a4234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a4/007a4234.md) [`007a5298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a5/007a5298.md) [`007a6180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a6/007a6180.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a363c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a3/007a3578.md#insn-007a363c) · [`007a36a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a3/007a3578.md#insn-007a36a0) · [`007a36c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a3/007a3578.md#insn-007a36c8)
- 新版 `007a3694`（命令位置の公開資料なし） · `007a36f8`（命令位置の公開資料なし） · `007a3720`（命令位置の公開資料なし）

~~~diff
- 007a363c ["INT_ADD", "register:40f0:8", ["const:7a363c:8", "const:4:8"]]
- 007a363c ["CALL", null, ["callee:00c57f80:8"]]
+ 007a3694 ["INT_ADD", "register:40f0:8", ["const:7a3694:8", "const:4:8"]]
+ 007a3694 ["CALL", null, ["callee:00c57f80:8"]]
- 007a363c bytes 1dd21294
+ 007a3694 bytes 3bd21294
- 007a36a0 ["INT_ADD", "register:40f0:8", ["const:7a36a0:8", "const:4:8"]]
- 007a36a0 ["CALL", null, ["callee:00c57f80:8"]]
+ 007a36f8 ["INT_ADD", "register:40f0:8", ["const:7a36f8:8", "const:4:8"]]
+ 007a36f8 ["CALL", null, ["callee:00c57f80:8"]]
- 007a36a0 bytes 04d21294
+ 007a36f8 bytes 22d21294
- 007a36c8 ["INT_ADD", "register:40f0:8", ["const:7a36c8:8", "const:4:8"]]
- 007a36c8 ["CALL", null, ["callee:00c57f80:8"]]
+ 007a3720 ["INT_ADD", "register:40f0:8", ["const:7a3720:8", "const:4:8"]]
+ 007a3720 ["CALL", null, ["callee:00c57f80:8"]]
- 007a36c8 bytes fad11294
+ 007a3720 bytes 18d21294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5d592a5033dd51ff171b5abec9f03fa"></a>

### [`007a3708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a3/007a3708.md) → [`007a3760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a3/007a3760.md) FUN_007a3760

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007a2004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a2/007a2004.md) [`007a8334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a8/007a8334.md) · 呼出先 11件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) [`007a0708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0708.md) [`007a3578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a3/007a3578.md)
- 新版 呼出元 2件 [`007a205c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a2/007a205c.md) [`007a838c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a8/007a838c.md) · 呼出先 11件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00597acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597acc.md) [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) [`007a0760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0760.md) [`007a35d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a3/007a35d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a3744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a3/007a3708.md#insn-007a3744) · [`007a378c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a3/007a3708.md#insn-007a378c) · [`007a37c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a3/007a3708.md#insn-007a37c8)
- 新版 `007a379c`（命令位置の公開資料なし） · `007a37e4`（命令位置の公開資料なし） · `007a3820`（命令位置の公開資料なし）

~~~diff
- 007a3744 ["INT_ADD", "register:40f0:8", ["const:7a3744:8", "const:4:8"]]
- 007a3744 ["CALL", null, ["callee:007a8ec4:8"]]
+ 007a379c ["INT_ADD", "register:40f0:8", ["const:7a379c:8", "const:4:8"]]
+ 007a379c ["CALL", null, ["callee:007a8ec4:8"]]
- 007a3744 bytes ca150094
+ 007a379c bytes ca150094
- 007a378c ["INT_ADD", "register:40f0:8", ["const:7a378c:8", "const:4:8"]]
- 007a378c ["CALL", null, ["callee:0043bb60:8"]]
+ 007a37e4 ["INT_ADD", "register:40f0:8", ["const:7a37e4:8", "const:4:8"]]
+ 007a37e4 ["CALL", null, ["callee:0043bb60:8"]]
- 007a378c bytes e560f297
+ 007a37e4 bytes df60f297
- 007a37c8 ["INT_ADD", "register:40f0:8", ["const:7a37c8:8", "const:4:8"]]
- 007a37c8 ["CALL", null, ["callee:00c57f60:8"]]
+ 007a3820 ["INT_ADD", "register:40f0:8", ["const:7a3820:8", "const:4:8"]]
+ 007a3820 ["CALL", null, ["callee:00c57f60:8"]]
- 007a37c8 bytes b2d11294
+ 007a3820 bytes d0d11294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-455c9fba648cda549c3b213e169bb588"></a>

### [`007a41dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a4/007a41dc.md) → [`007a4234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a4/007a4234.md) FUN_007a4234

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007a2004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a2/007a2004.md) · 呼出先 11件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) [`007a0708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0708.md) [`007a3578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a3/007a3578.md)
- 新版 呼出元 1件 [`007a205c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a2/007a205c.md) · 呼出先 11件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00597acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597acc.md) [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) [`007a0760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0760.md) [`007a35d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a3/007a35d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a4260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a4/007a41dc.md#insn-007a4260) · [`007a42e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a4/007a41dc.md#insn-007a42e8) · [`007a431c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a4/007a41dc.md#insn-007a431c)
- 新版 `007a42b8`（命令位置の公開資料なし） · `007a4340`（命令位置の公開資料なし） · `007a4374`（命令位置の公開資料なし）

~~~diff
- 007a4260 ["INT_ADD", "register:40f0:8", ["const:7a4260:8", "const:4:8"]]
- 007a4260 ["CALL", null, ["callee:007a96f4:8"]]
+ 007a42b8 ["INT_ADD", "register:40f0:8", ["const:7a42b8:8", "const:4:8"]]
+ 007a42b8 ["CALL", null, ["callee:007a96f4:8"]]
- 007a4260 bytes 0f150094
+ 007a42b8 bytes 0f150094
- 007a42e8 ["INT_ADD", "register:40f0:8", ["const:7a42e8:8", "const:4:8"]]
- 007a42e8 ["CALL", null, ["callee:0043bb60:8"]]
+ 007a4340 ["INT_ADD", "register:40f0:8", ["const:7a4340:8", "const:4:8"]]
+ 007a4340 ["CALL", null, ["callee:0043bb60:8"]]
- 007a42e8 bytes 0e5ef297
+ 007a4340 bytes 085ef297
- 007a431c ["INT_ADD", "register:40f0:8", ["const:7a431c:8", "const:4:8"]]
- 007a431c ["CALL", null, ["callee:00c57f60:8"]]
+ 007a4374 ["INT_ADD", "register:40f0:8", ["const:7a4374:8", "const:4:8"]]
+ 007a4374 ["CALL", null, ["callee:00c57f60:8"]]
- 007a431c bytes ddce1294
+ 007a4374 bytes fbce1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cf4b6c14b812c49f288087f396fc8bb"></a>

### [`007a5240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a5/007a5240.md) → [`007a5298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a5/007a5298.md) FUN_007a5298

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007a2004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a2/007a2004.md) [`007a8334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a8/007a8334.md) [`007a8e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a8/007a8e6c.md) · 呼出先 10件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) [`007a0708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0708.md) [`007a3578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a3/007a3578.md)
- 新版 呼出元 3件 [`007a205c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a2/007a205c.md) [`007a838c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a8/007a838c.md) [`007a8ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a8/007a8ec4.md) · 呼出先 10件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00597acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597acc.md) [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) [`007a0760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0760.md) [`007a35d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a3/007a35d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a52b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a5/007a5240.md#insn-007a52b4) · [`007a52f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a5/007a5240.md#insn-007a52f0) · [`007a5308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a5/007a5240.md#insn-007a5308)
- 新版 `007a530c`（命令位置の公開資料なし） · `007a5348`（命令位置の公開資料なし） · `007a5360`（命令位置の公開資料なし）

~~~diff
- 007a52b4 ["INT_ADD", "register:40f0:8", ["const:7a52b4:8", "const:4:8"]]
- 007a52b4 ["CALL", null, ["callee:0043bb60:8"]]
+ 007a530c ["INT_ADD", "register:40f0:8", ["const:7a530c:8", "const:4:8"]]
+ 007a530c ["CALL", null, ["callee:0043bb60:8"]]
- 007a52b4 bytes 1b5af297
+ 007a530c bytes 155af297
- 007a52f0 ["INT_ADD", "register:40f0:8", ["const:7a52f0:8", "const:4:8"]]
- 007a52f0 ["CALL", null, ["callee:00c57f60:8"]]
+ 007a5348 ["INT_ADD", "register:40f0:8", ["const:7a5348:8", "const:4:8"]]
+ 007a5348 ["CALL", null, ["callee:00c57f60:8"]]
- 007a52f0 bytes e8ca1294
+ 007a5348 bytes 06cb1294
- 007a5308 ["INT_ADD", "register:40f0:8", ["const:7a5308:8", "const:4:8"]]
- 007a5308 ["CALL", null, ["callee:00c580d0:8"]]
+ 007a5360 ["INT_ADD", "register:40f0:8", ["const:7a5360:8", "const:4:8"]]
+ 007a5360 ["CALL", null, ["callee:00c580d0:8"]]
- 007a5308 bytes 3ecb1294
+ 007a5360 bytes 5ccb1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b07e87e0bd3fa5817413a35d37bbcdbc"></a>

### [`007a5f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a5/007a5f98.md) → [`007a5ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a5/007a5ff0.md) FUN_007a5ff0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007a2004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a2/007a2004.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`007a205c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a2/007a205c.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a605c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a5/007a5f98.md#insn-007a605c) · [`007a60c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a5/007a5f98.md#insn-007a60c0) · [`007a60e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a5/007a5f98.md#insn-007a60e8)
- 新版 `007a60b4`（命令位置の公開資料なし） · `007a6118`（命令位置の公開資料なし） · `007a6140`（命令位置の公開資料なし）

~~~diff
- 007a605c ["INT_ADD", "register:40f0:8", ["const:7a605c:8", "const:4:8"]]
- 007a605c ["CALL", null, ["callee:00c57f80:8"]]
+ 007a60b4 ["INT_ADD", "register:40f0:8", ["const:7a60b4:8", "const:4:8"]]
+ 007a60b4 ["CALL", null, ["callee:00c57f80:8"]]
- 007a605c bytes 95c71294
+ 007a60b4 bytes b3c71294
- 007a60c0 ["INT_ADD", "register:40f0:8", ["const:7a60c0:8", "const:4:8"]]
- 007a60c0 ["CALL", null, ["callee:00c57f80:8"]]
+ 007a6118 ["INT_ADD", "register:40f0:8", ["const:7a6118:8", "const:4:8"]]
+ 007a6118 ["CALL", null, ["callee:00c57f80:8"]]
- 007a60c0 bytes 7cc71294
+ 007a6118 bytes 9ac71294
- 007a60e8 ["INT_ADD", "register:40f0:8", ["const:7a60e8:8", "const:4:8"]]
- 007a60e8 ["CALL", null, ["callee:00c57f80:8"]]
+ 007a6140 ["INT_ADD", "register:40f0:8", ["const:7a6140:8", "const:4:8"]]
+ 007a6140 ["CALL", null, ["callee:00c57f80:8"]]
- 007a60e8 bytes 72c71294
+ 007a6140 bytes 90c71294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1f3abde50de242473a92f9a7fd8fafd"></a>

### [`007a8334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a8/007a8334.md) → [`007a838c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a8/007a838c.md) FUN_007a838c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007a2004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a2/007a2004.md) · 呼出先 13件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) [`007a0708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0708.md) [`007a3578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a3/007a3578.md)
- 新版 呼出元 1件 [`007a205c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a2/007a205c.md) · 呼出先 13件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00597acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597acc.md) [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) [`007a0760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0760.md) [`007a35d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a3/007a35d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a83bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a8/007a8334.md#insn-007a83bc) · [`007a8428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a8/007a8334.md#insn-007a8428) · [`007a8448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a8/007a8334.md#insn-007a8448)
- 新版 `007a8414`（命令位置の公開資料なし） · `007a8480`（命令位置の公開資料なし） · `007a84a0`（命令位置の公開資料なし）

~~~diff
- 007a83bc ["INT_ADD", "register:40f0:8", ["const:7a83bc:8", "const:4:8"]]
- 007a83bc ["CALL", null, ["callee:007a3760:8"]]
+ 007a8414 ["INT_ADD", "register:40f0:8", ["const:7a8414:8", "const:4:8"]]
+ 007a8414 ["CALL", null, ["callee:007a3760:8"]]
- 007a83bc bytes d3ecff97
+ 007a8414 bytes d3ecff97
- 007a8428 ["INT_ADD", "register:40f0:8", ["const:7a8428:8", "const:4:8"]]
- 007a8428 ["CALL", null, ["callee:007a5298:8"]]
+ 007a8480 ["INT_ADD", "register:40f0:8", ["const:7a8480:8", "const:4:8"]]
+ 007a8480 ["CALL", null, ["callee:007a5298:8"]]
- 007a8428 bytes 86f3ff97
+ 007a8480 bytes 86f3ff97
- 007a8448 ["INT_ADD", "register:40f0:8", ["const:7a8448:8", "const:4:8"]]
- 007a8448 ["CALL", null, ["callee:007a5298:8"]]
+ 007a84a0 ["INT_ADD", "register:40f0:8", ["const:7a84a0:8", "const:4:8"]]
+ 007a84a0 ["CALL", null, ["callee:007a5298:8"]]
- 007a8448 bytes 7ef3ff97
+ 007a84a0 bytes 7ef3ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27c297733c5a623b78ffb3f54dbe00e6"></a>

### [`007a8e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a8/007a8e6c.md) → [`007a8ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a8/007a8ec4.md) FUN_007a8ec4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007a2004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a2/007a2004.md) [`007a3708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a3/007a3708.md) [`007a8334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a8/007a8334.md) · 呼出先 11件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) [`007a0708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0708.md) [`007a3578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a3/007a3578.md)
- 新版 呼出元 3件 [`007a205c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a2/007a205c.md) [`007a3760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a3/007a3760.md) [`007a838c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a8/007a838c.md) · 呼出先 11件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00597acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597acc.md) [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) [`007a0760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0760.md) [`007a35d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a3/007a35d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a8ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a8/007a8e6c.md#insn-007a8ea4) · [`007a8eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a8/007a8e6c.md#insn-007a8eec) · [`007a8f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a8/007a8e6c.md#insn-007a8f28)
- 新版 `007a8efc`（命令位置の公開資料なし） · `007a8f44`（命令位置の公開資料なし） · `007a8f80`（命令位置の公開資料なし）

~~~diff
- 007a8ea4 ["INT_ADD", "register:40f0:8", ["const:7a8ea4:8", "const:4:8"]]
- 007a8ea4 ["CALL", null, ["callee:007a5298:8"]]
+ 007a8efc ["INT_ADD", "register:40f0:8", ["const:7a8efc:8", "const:4:8"]]
+ 007a8efc ["CALL", null, ["callee:007a5298:8"]]
- 007a8ea4 bytes e7f0ff97
+ 007a8efc bytes e7f0ff97
- 007a8eec ["INT_ADD", "register:40f0:8", ["const:7a8eec:8", "const:4:8"]]
- 007a8eec ["CALL", null, ["callee:0043bb60:8"]]
+ 007a8f44 ["INT_ADD", "register:40f0:8", ["const:7a8f44:8", "const:4:8"]]
+ 007a8f44 ["CALL", null, ["callee:0043bb60:8"]]
- 007a8eec bytes 0d4bf297
+ 007a8f44 bytes 074bf297
- 007a8f28 ["INT_ADD", "register:40f0:8", ["const:7a8f28:8", "const:4:8"]]
- 007a8f28 ["CALL", null, ["callee:00c57f60:8"]]
+ 007a8f80 ["INT_ADD", "register:40f0:8", ["const:7a8f80:8", "const:4:8"]]
+ 007a8f80 ["CALL", null, ["callee:00c57f60:8"]]
- 007a8f28 bytes dabb1294
+ 007a8f80 bytes f8bb1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5140296a32e238fee642148ab7a017f5"></a>

### [`007a969c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a9/007a969c.md) → [`007a96f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a9/007a96f4.md) FUN_007a96f4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007a41dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a4/007a41dc.md) · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) [`007a0708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0708.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)
- 新版 呼出元 1件 [`007a4234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a4/007a4234.md) · 呼出先 9件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00597acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597acc.md) [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) [`007a0760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0760.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a9768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a9/007a969c.md#insn-007a9768) · [`007a97a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a9/007a969c.md#insn-007a97a4) · [`007a97bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a9/007a969c.md#insn-007a97bc)
- 新版 `007a97c0`（命令位置の公開資料なし） · `007a97fc`（命令位置の公開資料なし） · `007a9814`（命令位置の公開資料なし）

~~~diff
- 007a9768 ["INT_ADD", "register:40f0:8", ["const:7a9768:8", "const:4:8"]]
- 007a9768 ["CALL", null, ["callee:0043bb60:8"]]
+ 007a97c0 ["INT_ADD", "register:40f0:8", ["const:7a97c0:8", "const:4:8"]]
+ 007a97c0 ["CALL", null, ["callee:0043bb60:8"]]
- 007a9768 bytes ee48f297
+ 007a97c0 bytes e848f297
- 007a97a4 ["INT_ADD", "register:40f0:8", ["const:7a97a4:8", "const:4:8"]]
- 007a97a4 ["CALL", null, ["callee:00c57f60:8"]]
+ 007a97fc ["INT_ADD", "register:40f0:8", ["const:7a97fc:8", "const:4:8"]]
+ 007a97fc ["CALL", null, ["callee:00c57f60:8"]]
- 007a97a4 bytes bbb91294
+ 007a97fc bytes d9b91294
- 007a97bc ["INT_ADD", "register:40f0:8", ["const:7a97bc:8", "const:4:8"]]
- 007a97bc ["CALL", null, ["callee:00c580d0:8"]]
+ 007a9814 ["INT_ADD", "register:40f0:8", ["const:7a9814:8", "const:4:8"]]
+ 007a9814 ["CALL", null, ["callee:00c580d0:8"]]
- 007a97bc bytes 11ba1294
+ 007a9814 bytes 2fba1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4f656967034456c74e294b40f7d21fc"></a>

### [`007aa778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa778.md) → [`007aa7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aa7d0.md) FUN_007aa7d0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007abc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007abc24.md) · 呼出先 3件 [`00aa3460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa3/00aa3460.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`007abc7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007abc7c.md) · 呼出先 3件 [`00aa34d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aa3/00aa34d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007aa7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa778.md#insn-007aa7a4) · [`007aa7b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa778.md#insn-007aa7b4) · [`007aa804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa778.md#insn-007aa804)
- 新版 `007aa7fc`（命令位置の公開資料なし） · `007aa80c`（命令位置の公開資料なし） · `007aa85c`（命令位置の公開資料なし）

~~~diff
- 007aa7a4 ["INT_ADD", "register:40f0:8", ["const:7aa7a4:8", "const:4:8"]]
- 007aa7a4 ["CALL", null, ["callee:00aa34d0:8"]]
+ 007aa7fc ["INT_ADD", "register:40f0:8", ["const:7aa7fc:8", "const:4:8"]]
+ 007aa7fc ["CALL", null, ["callee:00aa34d0:8"]]
- 007aa7a4 bytes 2fe30b94
+ 007aa7fc bytes 35e30b94
- 007aa7b4 ["INT_ADD", "register:40f0:8", ["const:7aa7b4:8", "const:4:8"]]
- 007aa7b4 ["CALL", null, ["callee:00c57f80:8"]]
+ 007aa80c ["INT_ADD", "register:40f0:8", ["const:7aa80c:8", "const:4:8"]]
+ 007aa80c ["CALL", null, ["callee:00c57f80:8"]]
- 007aa7b4 bytes bfb51294
+ 007aa80c bytes ddb51294
- 007aa804 ["INT_ADD", "register:40f0:8", ["const:7aa804:8", "const:4:8"]]
- 007aa804 ["CALL", null, ["callee:00c57fb0:8"]]
+ 007aa85c ["INT_ADD", "register:40f0:8", ["const:7aa85c:8", "const:4:8"]]
+ 007aa85c ["CALL", null, ["callee:00c57fb0:8"]]
- 007aa804 bytes b7b51294
+ 007aa85c bytes d5b51294
~~~


<a id="compare-f29fdb4b3a9e8c16505ef9ce070fe24f"></a>

### [`007ab338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab338.md) → [`007ab390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007ab390.md) FUN_007ab390

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) · 呼出先 2件 [`007b091c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b091c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) · 呼出先 2件 [`007b0974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b0974.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007ab34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab338.md#insn-007ab34c) · [`007ab354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab338.md#insn-007ab354)
- 新版 `007ab3a4`（命令位置の公開資料なし） · `007ab3ac`（命令位置の公開資料なし）

~~~diff
- 007ab34c ["INT_ADD", "register:40f0:8", ["const:7ab34c:8", "const:4:8"]]
- 007ab34c ["CALL", null, ["callee:00c57f60:8"]]
+ 007ab3a4 ["INT_ADD", "register:40f0:8", ["const:7ab3a4:8", "const:4:8"]]
+ 007ab3a4 ["CALL", null, ["callee:00c57f60:8"]]
- 007ab34c bytes d1b21294
+ 007ab3a4 bytes efb21294
- 007ab354 ["INT_ADD", "register:40f0:8", ["const:7ab354:8", "const:4:8"]]
- 007ab354 ["CALL", null, ["callee:007b0974:8"]]
+ 007ab3ac ["INT_ADD", "register:40f0:8", ["const:7ab3ac:8", "const:4:8"]]
+ 007ab3ac ["CALL", null, ["callee:007b0974:8"]]
- 007ab354 bytes 72150094
+ 007ab3ac bytes 72150094
~~~


<a id="compare-3080ca43326868f5929513db62d0839e"></a>

### [`007ab37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab37c.md) → [`007ab3d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007ab3d4.md) FUN_007ab3d4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00848574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848574.md) [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`008485cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/008485cc.md) [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007ab3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab37c.md#insn-007ab3a0)
- 新版 `007ab3f8`（命令位置の公開資料なし）

~~~diff
- 007ab3a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 007ab3a0 ["INT_ADD", "register:40f0:8", ["const:7ab3a0:8", "const:4:8"]]
- 007ab3a0 ["CALLIND", null, ["register:0:8"]]
+ 007ab3f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007ab3f8 ["INT_ADD", "register:40f0:8", ["const:7ab3f8:8", "const:4:8"]]
+ 007ab3f8 ["CALLIND", null, ["register:0:8"]]
- 007ab3a0 bytes 00013fd6
+ 007ab3f8 bytes 00013fd6
~~~


<a id="compare-8f3e067ab3238f8ecf2b3bb17ba518e1"></a>

### [`007ae774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae774.md) → [`007ae7cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae7cc.md) FUN_007ae7cc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007ab404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab404.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`007ab45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007ab45c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007ae7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae774.md#insn-007ae7b0)
- 新版 `007ae808`（命令位置の公開資料なし）

~~~diff
- 007ae7b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 007ae7b0 ["INT_ADD", "register:40f0:8", ["const:7ae7b0:8", "const:4:8"]]
- 007ae7b0 ["CALLIND", null, ["register:0:8"]]
+ 007ae808 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007ae808 ["INT_ADD", "register:40f0:8", ["const:7ae808:8", "const:4:8"]]
+ 007ae808 ["CALLIND", null, ["register:0:8"]]
- 007ae7b0 bytes 00013fd6
+ 007ae808 bytes 00013fd6
~~~


<a id="compare-a87489edef6edf83fd5319a8e5ba7b1f"></a>

### [`007aef1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aef1c.md) → [`007aef74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aef74.md) FUN_007aef74

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007ad984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad984.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`007ad9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad9dc.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007aef3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aef1c.md#insn-007aef3c)
- 新版 `007aef94`（命令位置の公開資料なし）

~~~diff
- 007aef3c ["INT_ADD", "register:40f0:8", ["const:7aef3c:8", "const:4:8"]]
- 007aef3c ["CALL", null, ["callee:00c57f80:8"]]
+ 007aef94 ["INT_ADD", "register:40f0:8", ["const:7aef94:8", "const:4:8"]]
+ 007aef94 ["CALL", null, ["callee:00c57f80:8"]]
- 007aef3c bytes dda31294
+ 007aef94 bytes fba31294
~~~


<a id="compare-962d9552ead1c414a244032a4186ecda"></a>

### [`007af47c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af47c.md) → [`007af4d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af4d4.md) FUN_007af4d4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007ab754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab754.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`007ab7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007ab7ac.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007af4b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af47c.md#insn-007af4b8)
- 新版 `007af510`（命令位置の公開資料なし）

~~~diff
- 007af4b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 007af4b8 ["INT_ADD", "register:40f0:8", ["const:7af4b8:8", "const:4:8"]]
- 007af4b8 ["CALLIND", null, ["register:0:8"]]
+ 007af510 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007af510 ["INT_ADD", "register:40f0:8", ["const:7af510:8", "const:4:8"]]
+ 007af510 ["CALLIND", null, ["register:0:8"]]
- 007af4b8 bytes 00013fd6
+ 007af510 bytes 00013fd6
~~~


<a id="compare-ac0fffa93ea9731e69b134a47f9c3896"></a>

### [`007af4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af4cc.md) → [`007af524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af524.md) FUN_007af524

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007af504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af4cc.md#insn-007af504) · [`007af524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af4cc.md#insn-007af524) · [`007af534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af4cc.md#insn-007af534)
- 新版 `007af55c`（命令位置の公開資料なし） · `007af57c`（命令位置の公開資料なし） · `007af58c`（命令位置の公開資料なし）

~~~diff
- 007af504 ["INT_ADD", "register:40f0:8", ["const:7af504:8", "const:4:8"]]
- 007af504 ["CALL", null, ["callee:00c53d70:8"]]
+ 007af55c ["INT_ADD", "register:40f0:8", ["const:7af55c:8", "const:4:8"]]
+ 007af55c ["CALL", null, ["callee:00c53d70:8"]]
- 007af504 bytes f3911294
+ 007af55c bytes 05921294
- 007af524 ["COPY", "register:0:8", ["register:4040:8"]]
- 007af524 ["INT_ADD", "register:40f0:8", ["const:7af524:8", "const:4:8"]]
- 007af524 ["CALLIND", null, ["register:0:8"]]
+ 007af57c ["COPY", "register:0:8", ["register:4040:8"]]
+ 007af57c ["INT_ADD", "register:40f0:8", ["const:7af57c:8", "const:4:8"]]
+ 007af57c ["CALLIND", null, ["register:0:8"]]
- 007af524 bytes 00013fd6
+ 007af57c bytes 00013fd6
- 007af534 ["INT_ADD", "register:40f0:8", ["const:7af534:8", "const:4:8"]]
- 007af534 ["CALL", null, ["callee:00c53da0:8"]]
+ 007af58c ["INT_ADD", "register:40f0:8", ["const:7af58c:8", "const:4:8"]]
+ 007af58c ["CALL", null, ["callee:00c53da0:8"]]
- 007af534 bytes f3911294
+ 007af58c bytes 05921294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3db9f560e4cc69442e82f72abfdb5db"></a>

### [`007af5dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af5dc.md) → [`007af634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af634.md) FUN_007af634

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007af5f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af5dc.md#insn-007af5f8) · [`007af618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af5dc.md#insn-007af618)
- 新版 `007af650`（命令位置の公開資料なし） · `007af670`（命令位置の公開資料なし）

~~~diff
- 007af5f8 ["INT_ADD", "register:40f0:8", ["const:7af5f8:8", "const:4:8"]]
- 007af5f8 ["CALL", null, ["callee:00c53da0:8"]]
+ 007af650 ["INT_ADD", "register:40f0:8", ["const:7af650:8", "const:4:8"]]
+ 007af650 ["CALL", null, ["callee:00c53da0:8"]]
- 007af5f8 bytes c2911294
+ 007af650 bytes d4911294
- 007af618 ["COPY", "register:0:8", ["register:4040:8"]]
- 007af618 ["INT_ADD", "register:40f0:8", ["const:7af618:8", "const:4:8"]]
- 007af618 ["CALLIND", null, ["register:0:8"]]
+ 007af670 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007af670 ["INT_ADD", "register:40f0:8", ["const:7af670:8", "const:4:8"]]
+ 007af670 ["CALLIND", null, ["register:0:8"]]
- 007af618 bytes 00013fd6
+ 007af670 bytes 00013fd6
~~~


<a id="compare-a8e0e3dd73b05f576fcc1eefedd3cbdb"></a>

### [`007af800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af800.md) → [`007af858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af858.md) FUN_007af858

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007ab754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab754.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`007ab7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007ab7ac.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007af83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af800.md#insn-007af83c)
- 新版 `007af894`（命令位置の公開資料なし）

~~~diff
- 007af83c ["COPY", "register:0:8", ["register:4040:8"]]
- 007af83c ["INT_ADD", "register:40f0:8", ["const:7af83c:8", "const:4:8"]]
- 007af83c ["CALLIND", null, ["register:0:8"]]
+ 007af894 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007af894 ["INT_ADD", "register:40f0:8", ["const:7af894:8", "const:4:8"]]
+ 007af894 ["CALLIND", null, ["register:0:8"]]
- 007af83c bytes 00013fd6
+ 007af894 bytes 00013fd6
~~~


<a id="compare-988f1c7f9d6a0d97ba9213d1c7d83e25"></a>

### [`007af850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af850.md) → [`007af8a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af8a8.md) FUN_007af8a8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007af86c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af850.md#insn-007af86c)
- 新版 `007af8c4`（命令位置の公開資料なし）

~~~diff
- 007af86c ["INT_ADD", "register:40f0:8", ["const:7af86c:8", "const:4:8"]]
- 007af86c ["CALL", null, ["callee:00459db4:8"]]
+ 007af8c4 ["INT_ADD", "register:40f0:8", ["const:7af8c4:8", "const:4:8"]]
+ 007af8c4 ["CALL", null, ["callee:00459db4:8"]]
- 007af86c bytes 42a9f297
+ 007af8c4 bytes 3ca9f297
~~~


<a id="compare-12e2aeff2b6b85a5f0d35ee82bd9774a"></a>

### [`007afbe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afbe4.md) → [`007afc3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afc3c.md) FUN_007afc3c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007ad324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad324.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`007ad37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad37c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007afc20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afbe4.md#insn-007afc20)
- 新版 `007afc78`（命令位置の公開資料なし）

~~~diff
- 007afc20 ["COPY", "register:0:8", ["register:4040:8"]]
- 007afc20 ["INT_ADD", "register:40f0:8", ["const:7afc20:8", "const:4:8"]]
- 007afc20 ["CALLIND", null, ["register:0:8"]]
+ 007afc78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007afc78 ["INT_ADD", "register:40f0:8", ["const:7afc78:8", "const:4:8"]]
+ 007afc78 ["CALLIND", null, ["register:0:8"]]
- 007afc20 bytes 00013fd6
+ 007afc78 bytes 00013fd6
~~~


<a id="compare-fc29601a3c89fc5b668f8527ffe8d35a"></a>

### [`007afc34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afc34.md) → [`007afc8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afc8c.md) FUN_007afc8c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007afc50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afc34.md#insn-007afc50)
- 新版 `007afca8`（命令位置の公開資料なし）

~~~diff
- 007afc50 ["INT_ADD", "register:40f0:8", ["const:7afc50:8", "const:4:8"]]
- 007afc50 ["CALL", null, ["callee:00459db4:8"]]
+ 007afca8 ["INT_ADD", "register:40f0:8", ["const:7afca8:8", "const:4:8"]]
+ 007afca8 ["CALL", null, ["callee:00459db4:8"]]
- 007afc50 bytes 49a8f297
+ 007afca8 bytes 43a8f297
~~~


<a id="compare-dd7ea8a879e470a7ec5b80772a7ff149"></a>

### [`007afe50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afe50.md) → [`007afea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afea8.md) FUN_007afea8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007ad324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad324.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`007ad37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad37c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007afe8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afe50.md#insn-007afe8c)
- 新版 `007afee4`（命令位置の公開資料なし）

~~~diff
- 007afe8c ["COPY", "register:0:8", ["register:4040:8"]]
- 007afe8c ["INT_ADD", "register:40f0:8", ["const:7afe8c:8", "const:4:8"]]
- 007afe8c ["CALLIND", null, ["register:0:8"]]
+ 007afee4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007afee4 ["INT_ADD", "register:40f0:8", ["const:7afee4:8", "const:4:8"]]
+ 007afee4 ["CALLIND", null, ["register:0:8"]]
- 007afe8c bytes 00013fd6
+ 007afee4 bytes 00013fd6
~~~


<a id="compare-b5afa79d855cbe635f978ba80bba6516"></a>

### [`007afea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afea0.md) → [`007afef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afef8.md) FUN_007afef8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007afed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afea0.md#insn-007afed8) · [`007aff0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afea0.md#insn-007aff0c) · [`007aff10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afea0.md#insn-007aff10)
- 新版 `007aff30`（命令位置の公開資料なし） · `007aff64`（命令位置の公開資料なし） · `007aff68`（命令位置の公開資料なし）

~~~diff
- 007afed8 ["COPY", "register:0:8", ["register:4040:8"]]
- 007afed8 ["INT_ADD", "register:40f0:8", ["const:7afed8:8", "const:4:8"]]
- 007afed8 ["CALLIND", null, ["register:0:8"]]
+ 007aff30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007aff30 ["INT_ADD", "register:40f0:8", ["const:7aff30:8", "const:4:8"]]
+ 007aff30 ["CALLIND", null, ["register:0:8"]]
- 007afed8 bytes 00013fd6
+ 007aff30 bytes 00013fd6
- 007aff0c ["INT_ADD", "register:40f0:8", ["const:7aff0c:8", "const:4:8"]]
- 007aff0c ["CALL", null, ["callee:00459db4:8"]]
+ 007aff64 ["INT_ADD", "register:40f0:8", ["const:7aff64:8", "const:4:8"]]
+ 007aff64 ["CALL", null, ["callee:00459db4:8"]]
- 007aff0c bytes 9aa7f297
+ 007aff64 bytes 94a7f297
- 007aff10 ["INT_ADD", "register:40f0:8", ["const:7aff10:8", "const:4:8"]]
- 007aff10 ["CALL", null, ["callee:00c57fb0:8"]]
+ 007aff68 ["INT_ADD", "register:40f0:8", ["const:7aff68:8", "const:4:8"]]
+ 007aff68 ["CALL", null, ["callee:00c57fb0:8"]]
- 007aff10 bytes f49f1294
+ 007aff68 bytes 12a01294
~~~


<a id="compare-03170c3a7e02dadc7368ff4a3f7ae8bc"></a>

### [`007b0288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0288.md) → [`007b02e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b02e0.md) FUN_007b02e0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007adf1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007adf1c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`007adf74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007adf74.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007b02c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0288.md#insn-007b02c4)
- 新版 `007b031c`（命令位置の公開資料なし）

~~~diff
- 007b02c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 007b02c4 ["INT_ADD", "register:40f0:8", ["const:7b02c4:8", "const:4:8"]]
- 007b02c4 ["CALLIND", null, ["register:0:8"]]
+ 007b031c ["COPY", "register:0:8", ["register:4040:8"]]
+ 007b031c ["INT_ADD", "register:40f0:8", ["const:7b031c:8", "const:4:8"]]
+ 007b031c ["CALLIND", null, ["register:0:8"]]
- 007b02c4 bytes 00013fd6
+ 007b031c bytes 00013fd6
~~~


<a id="compare-5f5349632d1b1dd049b137640116e68b"></a>

### [`007b02d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b02d8.md) → [`007b0330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b0330.md) FUN_007b0330

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007b02f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b02d8.md#insn-007b02f4)
- 新版 `007b034c`（命令位置の公開資料なし）

~~~diff
- 007b02f4 ["INT_ADD", "register:40f0:8", ["const:7b02f4:8", "const:4:8"]]
- 007b02f4 ["CALL", null, ["callee:00459db4:8"]]
+ 007b034c ["INT_ADD", "register:40f0:8", ["const:7b034c:8", "const:4:8"]]
+ 007b034c ["CALL", null, ["callee:00459db4:8"]]
- 007b02f4 bytes a0a6f297
+ 007b034c bytes 9aa6f297
~~~


<a id="compare-9bf5b8490ca04d5d1f7930fedf07c0d9"></a>

### [`007b04f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b04f4.md) → [`007b054c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b054c.md) FUN_007b054c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007adf1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007adf1c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`007adf74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007adf74.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007b0530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b04f4.md#insn-007b0530)
- 新版 `007b0588`（命令位置の公開資料なし）

~~~diff
- 007b0530 ["COPY", "register:0:8", ["register:4040:8"]]
- 007b0530 ["INT_ADD", "register:40f0:8", ["const:7b0530:8", "const:4:8"]]
- 007b0530 ["CALLIND", null, ["register:0:8"]]
+ 007b0588 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007b0588 ["INT_ADD", "register:40f0:8", ["const:7b0588:8", "const:4:8"]]
+ 007b0588 ["CALLIND", null, ["register:0:8"]]
- 007b0530 bytes 00013fd6
+ 007b0588 bytes 00013fd6
~~~


<a id="compare-e9b873b1ec2eda4da22b5914990cb196"></a>

### [`007b0544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0544.md) → [`007b059c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b059c.md) FUN_007b059c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007b0560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0544.md#insn-007b0560)
- 新版 `007b05b8`（命令位置の公開資料なし）

~~~diff
- 007b0560 ["INT_ADD", "register:40f0:8", ["const:7b0560:8", "const:4:8"]]
- 007b0560 ["CALL", null, ["callee:00459db4:8"]]
+ 007b05b8 ["INT_ADD", "register:40f0:8", ["const:7b05b8:8", "const:4:8"]]
+ 007b05b8 ["CALL", null, ["callee:00459db4:8"]]
- 007b0560 bytes 05a6f297
+ 007b05b8 bytes ffa5f297
~~~


<a id="compare-b4730428b7fd225170f1d49aafca66fc"></a>

### [`007b0928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0928.md) → [`007b0980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b0980.md) FUN_007b0980

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007ab3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab3c8.md) · 呼出先 1件 [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md)
- 新版 呼出元 1件 [`007ab420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007ab420.md) · 呼出先 1件 [`00480d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480d88.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007b0948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0928.md#insn-007b0948) · [`007b0954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0928.md#insn-007b0954)
- 新版 `007b09a0`（命令位置の公開資料なし） · `007b09ac`（命令位置の公開資料なし）

~~~diff
- 007b0948 ["INT_ADD", "register:40f0:8", ["const:7b0948:8", "const:4:8"]]
- 007b0948 ["CALL", null, ["callee:00480d88:8"]]
+ 007b09a0 ["INT_ADD", "register:40f0:8", ["const:7b09a0:8", "const:4:8"]]
+ 007b09a0 ["CALL", null, ["callee:00480d88:8"]]
- 007b0948 bytes 0041f397
+ 007b09a0 bytes fa40f397
- 007b0954 ["INT_ADD", "register:40f0:8", ["const:7b0954:8", "const:4:8"]]
- 007b0954 ["CALL", null, ["callee:00480d88:8"]]
+ 007b09ac ["INT_ADD", "register:40f0:8", ["const:7b09ac:8", "const:4:8"]]
+ 007b09ac ["CALL", null, ["callee:00480d88:8"]]
- 007b0954 bytes fd40f397
+ 007b09ac bytes f740f397
~~~


<a id="compare-3fb565ef51a8859a12cffc82c8bbe7d6"></a>

### [`007b096c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b096c.md) → [`007b09c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b09c4.md) FUN_007b09c4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007ab3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab3d0.md) · 呼出先 1件 [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md)
- 新版 呼出元 1件 [`007ab428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007ab428.md) · 呼出先 1件 [`00480338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480338.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007b0984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b096c.md#insn-007b0984) · [`007b0994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b096c.md#insn-007b0994) · [`007b09a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b096c.md#insn-007b09a4)
- 新版 `007b09dc`（命令位置の公開資料なし） · `007b09ec`（命令位置の公開資料なし） · `007b09fc`（命令位置の公開資料なし）

~~~diff
- 007b0984 ["INT_ADD", "register:40f0:8", ["const:7b0984:8", "const:4:8"]]
- 007b0984 ["CALL", null, ["callee:00480338:8"]]
+ 007b09dc ["INT_ADD", "register:40f0:8", ["const:7b09dc:8", "const:4:8"]]
+ 007b09dc ["CALL", null, ["callee:00480338:8"]]
- 007b0984 bytes 5d3ef397
+ 007b09dc bytes 573ef397
- 007b0994 ["INT_ADD", "register:40f0:8", ["const:7b0994:8", "const:4:8"]]
- 007b0994 ["CALL", null, ["callee:00480338:8"]]
+ 007b09ec ["INT_ADD", "register:40f0:8", ["const:7b09ec:8", "const:4:8"]]
+ 007b09ec ["CALL", null, ["callee:00480338:8"]]
- 007b0994 bytes 593ef397
+ 007b09ec bytes 533ef397
- 007b09a4 ["INT_ADD", "register:40f0:8", ["const:7b09a4:8", "const:4:8"]]
- 007b09a4 ["CALL", null, ["callee:00480338:8"]]
+ 007b09fc ["INT_ADD", "register:40f0:8", ["const:7b09fc:8", "const:4:8"]]
+ 007b09fc ["CALL", null, ["callee:00480338:8"]]
- 007b09a4 bytes 553ef397
+ 007b09fc bytes 4f3ef397
~~~


<a id="compare-7bef165622ef96270fc6c7e3d493bb63"></a>

### [`007bba0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bba0c.md) → [`007bba64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bb/007bba64.md) FUN_007bba64

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 3件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007bba74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bba0c.md#insn-007bba74) · [`007bbacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bba0c.md#insn-007bbacc)
- 新版 `007bbacc`（命令位置の公開資料なし） · `007bbb24`（命令位置の公開資料なし）

~~~diff
- 007bba74 ["INT_ADD", "register:40f0:8", ["const:7bba74:8", "const:4:8"]]
- 007bba74 ["CALL", null, ["callee:00c57f60:8"]]
+ 007bbacc ["INT_ADD", "register:40f0:8", ["const:7bbacc:8", "const:4:8"]]
+ 007bbacc ["CALL", null, ["callee:00c57f60:8"]]
- 007bba74 bytes 07711294
+ 007bbacc bytes 25711294
- 007bbacc ["INT_ADD", "register:40f0:8", ["const:7bbacc:8", "const:4:8"]]
- 007bbacc ["CALL", null, ["callee:0043bbe4:8"]]
+ 007bbb24 ["INT_ADD", "register:40f0:8", ["const:7bbb24:8", "const:4:8"]]
+ 007bbb24 ["CALL", null, ["callee:0043bbe4:8"]]
- 007bbacc bytes 3600f297
+ 007bbb24 bytes 3000f297
~~~


<a id="compare-fceb28660664f5badd67b6aef213f30f"></a>

### [`007bbaf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbaf4.md) → [`007bbb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bb/007bbb4c.md) FUN_007bbb4c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007b0a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0a18.md) [`00a52e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a52/00a52e30.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`007f0c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0c98.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`007b0a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b0a70.md) [`00a52ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a52/00a52ea0.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`007f0cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f0/007f0cf0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007bbb54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbaf4.md#insn-007bbb54) · [`007bbb64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbaf4.md#insn-007bbb64) · [`007bbb98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbaf4.md#insn-007bbb98)
- 新版 `007bbbac`（命令位置の公開資料なし） · `007bbbbc`（命令位置の公開資料なし） · `007bbbf0`（命令位置の公開資料なし）

~~~diff
- 007bbb54 ["INT_ADD", "register:40f0:8", ["const:7bbb54:8", "const:4:8"]]
- 007bbb54 ["CALL", null, ["callee:0043bb60:8"]]
+ 007bbbac ["INT_ADD", "register:40f0:8", ["const:7bbbac:8", "const:4:8"]]
+ 007bbbac ["CALL", null, ["callee:0043bb60:8"]]
- 007bbb54 bytes f3fff197
+ 007bbbac bytes edfff197
- 007bbb64 ["INT_ADD", "register:40f0:8", ["const:7bbb64:8", "const:4:8"]]
- 007bbb64 ["CALL", null, ["callee:0043bb60:8"]]
+ 007bbbbc ["INT_ADD", "register:40f0:8", ["const:7bbbbc:8", "const:4:8"]]
+ 007bbbbc ["CALL", null, ["callee:0043bb60:8"]]
- 007bbb64 bytes effff197
+ 007bbbbc bytes e9fff197
- 007bbb98 ["INT_ADD", "register:40f0:8", ["const:7bbb98:8", "const:4:8"]]
- 007bbb98 ["CALL", null, ["callee:007f0cf0:8"]]
+ 007bbbf0 ["INT_ADD", "register:40f0:8", ["const:7bbbf0:8", "const:4:8"]]
+ 007bbbf0 ["CALL", null, ["callee:007f0cf0:8"]]
- 007bbb98 bytes 40d40094
+ 007bbbf0 bytes 40d40094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88ec472a942b51e7a3d39b0b495b7bf1"></a>

### [`007bd6d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd6d8.md) → [`007bd730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bd730.md) FUN_007bd730

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007bd740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd6d8.md#insn-007bd740) · [`007bd778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd6d8.md#insn-007bd778)
- 新版 `007bd798`（命令位置の公開資料なし） · `007bd7d0`（命令位置の公開資料なし）

~~~diff
- 007bd740 ["INT_ADD", "register:40f0:8", ["const:7bd740:8", "const:4:8"]]
- 007bd740 ["CALL", null, ["callee:00c57f60:8"]]
+ 007bd798 ["INT_ADD", "register:40f0:8", ["const:7bd798:8", "const:4:8"]]
+ 007bd798 ["CALL", null, ["callee:00c57f60:8"]]
- 007bd740 bytes d4691294
+ 007bd798 bytes f2691294
- 007bd778 ["INT_ADD", "register:40f0:8", ["const:7bd778:8", "const:4:8"]]
- 007bd778 ["CALL", null, ["callee:0043bbe4:8"]]
+ 007bd7d0 ["INT_ADD", "register:40f0:8", ["const:7bd7d0:8", "const:4:8"]]
+ 007bd7d0 ["CALL", null, ["callee:0043bbe4:8"]]
- 007bd778 bytes 0bf9f197
+ 007bd7d0 bytes 05f9f197
~~~


<a id="compare-8af16b53530283159251ad17db9524a0"></a>

### [`007bd7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd7a0.md) → [`007bd7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bd7f8.md) FUN_007bd7f8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e8e4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007bd7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd7a0.md#insn-007bd7d4)
- 新版 `007bd82c`（命令位置の公開資料なし）

~~~diff
- 007bd7d4 ["INT_ADD", "register:40f0:8", ["const:7bd7d4:8", "const:4:8"]]
- 007bd7d4 ["CALL", null, ["callee:0046e8e4:8"]]
+ 007bd82c ["INT_ADD", "register:40f0:8", ["const:7bd82c:8", "const:4:8"]]
+ 007bd82c ["CALL", null, ["callee:0046e8e4:8"]]
- 007bd7d4 bytes 34c4f297
+ 007bd82c bytes 2ec4f297
~~~


<a id="compare-f4390968ec8287e0786e7164888ff725"></a>

### [`007bd808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd808.md) → [`007bd860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bd860.md) FUN_007bd860

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007bd840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd808.md#insn-007bd840) · [`007bd854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd808.md#insn-007bd854) · [`007bd85c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd808.md#insn-007bd85c)
- 新版 `007bd898`（命令位置の公開資料なし） · `007bd8ac`（命令位置の公開資料なし） · `007bd8b4`（命令位置の公開資料なし）

~~~diff
- 007bd840 ["INT_ADD", "register:40f0:8", ["const:7bd840:8", "const:4:8"]]
- 007bd840 ["CALL", null, ["callee:00c53da0:8"]]
+ 007bd898 ["INT_ADD", "register:40f0:8", ["const:7bd898:8", "const:4:8"]]
+ 007bd898 ["CALL", null, ["callee:00c53da0:8"]]
- 007bd840 bytes 30591294
+ 007bd898 bytes 42591294
- 007bd854 ["COPY", "register:0:8", ["register:4040:8"]]
- 007bd854 ["INT_ADD", "register:40f0:8", ["const:7bd854:8", "const:4:8"]]
- 007bd854 ["CALLIND", null, ["register:0:8"]]
+ 007bd8ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 007bd8ac ["INT_ADD", "register:40f0:8", ["const:7bd8ac:8", "const:4:8"]]
+ 007bd8ac ["CALLIND", null, ["register:0:8"]]
- 007bd854 bytes 00013fd6
+ 007bd8ac bytes 00013fd6
- 007bd85c ["INT_ADD", "register:40f0:8", ["const:7bd85c:8", "const:4:8"]]
- 007bd85c ["CALL", null, ["callee:00c57f50:8"]]
+ 007bd8b4 ["INT_ADD", "register:40f0:8", ["const:7bd8b4:8", "const:4:8"]]
+ 007bd8b4 ["CALL", null, ["callee:00c57f50:8"]]
- 007bd85c bytes 89691294
+ 007bd8b4 bytes a7691294
~~~


<a id="compare-71928005c19e88dd2fb6656e2c1658cd"></a>

### [`007bd874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd874.md) → [`007bd8cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bd8cc.md) FUN_007bd8cc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007bd8ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd874.md#insn-007bd8ac) · [`007bd8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd874.md#insn-007bd8c0) · [`007bd8c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd874.md#insn-007bd8c8)
- 新版 `007bd904`（命令位置の公開資料なし） · `007bd918`（命令位置の公開資料なし） · `007bd920`（命令位置の公開資料なし）

~~~diff
- 007bd8ac ["INT_ADD", "register:40f0:8", ["const:7bd8ac:8", "const:4:8"]]
- 007bd8ac ["CALL", null, ["callee:00c53da0:8"]]
+ 007bd904 ["INT_ADD", "register:40f0:8", ["const:7bd904:8", "const:4:8"]]
+ 007bd904 ["CALL", null, ["callee:00c53da0:8"]]
- 007bd8ac bytes 15591294
+ 007bd904 bytes 27591294
- 007bd8c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 007bd8c0 ["INT_ADD", "register:40f0:8", ["const:7bd8c0:8", "const:4:8"]]
- 007bd8c0 ["CALLIND", null, ["register:0:8"]]
+ 007bd918 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007bd918 ["INT_ADD", "register:40f0:8", ["const:7bd918:8", "const:4:8"]]
+ 007bd918 ["CALLIND", null, ["register:0:8"]]
- 007bd8c0 bytes 00013fd6
+ 007bd918 bytes 00013fd6
- 007bd8c8 ["INT_ADD", "register:40f0:8", ["const:7bd8c8:8", "const:4:8"]]
- 007bd8c8 ["CALL", null, ["callee:00c57f50:8"]]
+ 007bd920 ["INT_ADD", "register:40f0:8", ["const:7bd920:8", "const:4:8"]]
+ 007bd920 ["CALL", null, ["callee:00c57f50:8"]]
- 007bd8c8 bytes 6e691294
+ 007bd920 bytes 8c691294
~~~


<a id="compare-f086b7610ef68b34e4055cb71f5018a8"></a>

### [`007bd8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd8e0.md) → [`007bd938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bd938.md) FUN_007bd938

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007bd8fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd8e0.md#insn-007bd8fc) · [`007bd91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd8e0.md#insn-007bd91c)
- 新版 `007bd954`（命令位置の公開資料なし） · `007bd974`（命令位置の公開資料なし）

~~~diff
- 007bd8fc ["INT_ADD", "register:40f0:8", ["const:7bd8fc:8", "const:4:8"]]
- 007bd8fc ["CALL", null, ["callee:00c53da0:8"]]
+ 007bd954 ["INT_ADD", "register:40f0:8", ["const:7bd954:8", "const:4:8"]]
+ 007bd954 ["CALL", null, ["callee:00c53da0:8"]]
- 007bd8fc bytes 01591294
+ 007bd954 bytes 13591294
- 007bd91c ["COPY", "register:0:8", ["register:4040:8"]]
- 007bd91c ["INT_ADD", "register:40f0:8", ["const:7bd91c:8", "const:4:8"]]
- 007bd91c ["CALLIND", null, ["register:0:8"]]
+ 007bd974 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007bd974 ["INT_ADD", "register:40f0:8", ["const:7bd974:8", "const:4:8"]]
+ 007bd974 ["CALLIND", null, ["register:0:8"]]
- 007bd91c bytes 00013fd6
+ 007bd974 bytes 00013fd6
~~~


<a id="compare-6610c1299cb209fd8826dcc5e0847aec"></a>

### [`007bd930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd930.md) → [`007bd988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bd988.md) FUN_007bd988

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007bd998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd930.md#insn-007bd998) · [`007bda1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd930.md#insn-007bda1c)
- 新版 `007bd9f0`（命令位置の公開資料なし） · `007bda74`（命令位置の公開資料なし）

~~~diff
- 007bd998 ["INT_ADD", "register:40f0:8", ["const:7bd998:8", "const:4:8"]]
- 007bd998 ["CALL", null, ["callee:00c57f60:8"]]
+ 007bd9f0 ["INT_ADD", "register:40f0:8", ["const:7bd9f0:8", "const:4:8"]]
+ 007bd9f0 ["CALL", null, ["callee:00c57f60:8"]]
- 007bd998 bytes 3e691294
+ 007bd9f0 bytes 5c691294
- 007bda1c ["INT_ADD", "register:40f0:8", ["const:7bda1c:8", "const:4:8"]]
- 007bda1c ["CALL", null, ["callee:0043bbe4:8"]]
+ 007bda74 ["INT_ADD", "register:40f0:8", ["const:7bda74:8", "const:4:8"]]
+ 007bda74 ["CALL", null, ["callee:0043bbe4:8"]]
- 007bda1c bytes 62f8f197
+ 007bda74 bytes 5cf8f197
~~~


<a id="compare-f67f11481706c0ff44d0b2ea426ceb44"></a>

### [`007c77e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c77e8.md) → [`007c7840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007c7/007c7840.md) FUN_007c7840

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`0094726c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00947/0094726c.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 2件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`009472c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00947/009472c0.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007c780c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c77e8.md#insn-007c780c) · [`007c7854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c77e8.md#insn-007c7854) · [`007c7874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c77e8.md#insn-007c7874)
- 新版 `007c7864`（命令位置の公開資料なし） · `007c78ac`（命令位置の公開資料なし） · `007c78cc`（命令位置の公開資料なし）

~~~diff
- 007c780c ["INT_ADD", "register:40f0:8", ["const:7c780c:8", "const:4:8"]]
- 007c780c ["CALL", null, ["callee:00c580b0:8"]]
+ 007c7864 ["INT_ADD", "register:40f0:8", ["const:7c7864:8", "const:4:8"]]
+ 007c7864 ["CALL", null, ["callee:00c580b0:8"]]
- 007c780c bytes f5411294
+ 007c7864 bytes 13421294
- 007c7854 ["INT_ADD", "register:40f0:8", ["const:7c7854:8", "const:4:8"]]
- 007c7854 ["CALL", null, ["callee:00c57f60:8"]]
+ 007c78ac ["INT_ADD", "register:40f0:8", ["const:7c78ac:8", "const:4:8"]]
+ 007c78ac ["CALL", null, ["callee:00c57f60:8"]]
- 007c7854 bytes 8f411294
+ 007c78ac bytes ad411294
- 007c7874 ["INT_ADD", "register:40f0:8", ["const:7c7874:8", "const:4:8"]]
- 007c7874 ["CALL", null, ["callee:00c58010:8"]]
+ 007c78cc ["INT_ADD", "register:40f0:8", ["const:7c78cc:8", "const:4:8"]]
+ 007c78cc ["CALL", null, ["callee:00c58010:8"]]
- 007c7874 bytes b3411294
+ 007c78cc bytes d1411294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-338e3e6e72a0d1e5b3a89633a054c257"></a>

### [`007c78b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c78b0.md) → [`007c7908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007c7/007c7908.md) FUN_007c7908

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) [`00ab31a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab3/00ab31a4.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 3件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`009d0374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d0/009d0374.md) [`00ab3214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ab3/00ab3214.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007c7918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c78b0.md#insn-007c7918) · [`007c7950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c78b0.md#insn-007c7950)
- 新版 `007c7970`（命令位置の公開資料なし） · `007c79a8`（命令位置の公開資料なし）

~~~diff
- 007c7918 ["INT_ADD", "register:40f0:8", ["const:7c7918:8", "const:4:8"]]
- 007c7918 ["CALL", null, ["callee:00c57f60:8"]]
+ 007c7970 ["INT_ADD", "register:40f0:8", ["const:7c7970:8", "const:4:8"]]
+ 007c7970 ["CALL", null, ["callee:00c57f60:8"]]
- 007c7918 bytes 5e411294
+ 007c7970 bytes 7c411294
- 007c7950 ["INT_ADD", "register:40f0:8", ["const:7c7950:8", "const:4:8"]]
- 007c7950 ["CALL", null, ["callee:0043bbe4:8"]]
+ 007c79a8 ["INT_ADD", "register:40f0:8", ["const:7c79a8:8", "const:4:8"]]
+ 007c79a8 ["CALL", null, ["callee:0043bbe4:8"]]
- 007c7950 bytes 95d0f197
+ 007c79a8 bytes 8fd0f197
~~~


<a id="compare-eeb293de4af6374f980a056eb815bc05"></a>

### [`007c7e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7e68.md) → [`007c7ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007c7/007c7ec0.md) FUN_007c7ec0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) · 呼出先 5件 [`007f1eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1eb8.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) · 呼出先 5件 [`007f1f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1f10.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007c7e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7e68.md#insn-007c7e98) · [`007c7eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7e68.md#insn-007c7eb0) · [`007c7ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7e68.md#insn-007c7ecc)
- 新版 `007c7ef0`（命令位置の公開資料なし） · `007c7f08`（命令位置の公開資料なし） · `007c7f24`（命令位置の公開資料なし）

~~~diff
- 007c7e98 ["INT_ADD", "register:40f0:8", ["const:7c7e98:8", "const:4:8"]]
- 007c7e98 ["CALL", null, ["callee:00c57f60:8"]]
+ 007c7ef0 ["INT_ADD", "register:40f0:8", ["const:7c7ef0:8", "const:4:8"]]
+ 007c7ef0 ["CALL", null, ["callee:00c57f60:8"]]
- 007c7e98 bytes fe3f1294
+ 007c7ef0 bytes 1c401294
- 007c7eb0 ["INT_ADD", "register:40f0:8", ["const:7c7eb0:8", "const:4:8"]]
- 007c7eb0 ["CALL", null, ["callee:00c580d0:8"]]
+ 007c7f08 ["INT_ADD", "register:40f0:8", ["const:7c7f08:8", "const:4:8"]]
+ 007c7f08 ["CALL", null, ["callee:00c580d0:8"]]
- 007c7eb0 bytes 54401294
+ 007c7f08 bytes 72401294
- 007c7ecc ["INT_ADD", "register:40f0:8", ["const:7c7ecc:8", "const:4:8"]]
- 007c7ecc ["CALL", null, ["callee:007f1f10:8"]]
+ 007c7f24 ["INT_ADD", "register:40f0:8", ["const:7c7f24:8", "const:4:8"]]
+ 007c7f24 ["CALL", null, ["callee:007f1f10:8"]]
- 007c7ecc bytes fba70094
+ 007c7f24 bytes fba70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25bef0cb2ebc0046316b95eb448a034f"></a>

### [`007c7ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7ef0.md) → [`007c7f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007c7/007c7f48.md) FUN_007c7f48

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) · 呼出先 8件 [`005e46d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e46d8.md) [`005e46e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e46e0.md) [`005e48ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e48ac.md) [`005e4a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4a34.md) [`005e4a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4a94.md)
- 新版 呼出元 2件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`007efd00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007efd00.md) · 呼出先 8件 [`005e4718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e4/005e4718.md) [`005e4720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e4/005e4720.md) [`005e48ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e4/005e48ec.md) [`005e4a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e4/005e4a74.md) [`005e4ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e4/005e4ad4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007c7f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7ef0.md#insn-007c7f08) · [`007c7f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7ef0.md#insn-007c7f10) · [`007c7f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7ef0.md#insn-007c7f3c)
- 新版 `007c7f60`（命令位置の公開資料なし） · `007c7f68`（命令位置の公開資料なし） · `007c7f94`（命令位置の公開資料なし）

~~~diff
- 007c7f08 ["INT_ADD", "register:40f0:8", ["const:7c7f08:8", "const:4:8"]]
- 007c7f08 ["CALL", null, ["callee:005e4a74:8"]]
+ 007c7f60 ["INT_ADD", "register:40f0:8", ["const:7c7f60:8", "const:4:8"]]
+ 007c7f60 ["CALL", null, ["callee:005e4a74:8"]]
- 007c7f08 bytes cb72f897
+ 007c7f60 bytes c572f897
- 007c7f10 ["INT_ADD", "register:40f0:8", ["const:7c7f10:8", "const:4:8"]]
- 007c7f10 ["CALL", null, ["callee:005e4718:8"]]
+ 007c7f68 ["INT_ADD", "register:40f0:8", ["const:7c7f68:8", "const:4:8"]]
+ 007c7f68 ["CALL", null, ["callee:005e4718:8"]]
- 007c7f10 bytes f271f897
+ 007c7f68 bytes ec71f897
- 007c7f3c ["INT_ADD", "register:40f0:8", ["const:7c7f3c:8", "const:4:8"]]
- 007c7f3c ["CALL", null, ["callee:005e4b54:8"]]
+ 007c7f94 ["INT_ADD", "register:40f0:8", ["const:7c7f94:8", "const:4:8"]]
+ 007c7f94 ["CALL", null, ["callee:005e4b54:8"]]
- 007c7f3c bytes f672f897
+ 007c7f94 bytes f072f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d80dcb1a430bb0c12d1d803cea3f681"></a>

### [`007cb588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb588.md) → [`007cb5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cb/007cb5e0.md) FUN_007cb5e0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007cb5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb588.md#insn-007cb5a8) · [`007cb5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb588.md#insn-007cb5b8)
- 新版 `007cb600`（命令位置の公開資料なし） · `007cb610`（命令位置の公開資料なし）

~~~diff
- 007cb5a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 007cb5a8 ["INT_ADD", "register:40f0:8", ["const:7cb5a8:8", "const:4:8"]]
- 007cb5a8 ["CALLIND", null, ["register:0:8"]]
+ 007cb600 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007cb600 ["INT_ADD", "register:40f0:8", ["const:7cb600:8", "const:4:8"]]
+ 007cb600 ["CALLIND", null, ["register:0:8"]]
- 007cb5a8 bytes 00013fd6
+ 007cb600 bytes 00013fd6
- 007cb5b8 ["INT_ADD", "register:40f0:8", ["const:7cb5b8:8", "const:4:8"]]
- 007cb5b8 ["CALL", null, ["callee:00c57f80:8"]]
+ 007cb610 ["INT_ADD", "register:40f0:8", ["const:7cb610:8", "const:4:8"]]
+ 007cb610 ["CALL", null, ["callee:00c57f80:8"]]
- 007cb5b8 bytes 3e321294
+ 007cb610 bytes 5c321294
~~~


<a id="compare-4b754d29052160c94e5fb6020e9b7b1c"></a>

### [`007dcf38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dc/007dcf38.md) → [`007dcf90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007dc/007dcf90.md) FUN_007dcf90

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007dcf54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dc/007dcf38.md#insn-007dcf54) · [`007dcf74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dc/007dcf38.md#insn-007dcf74)
- 新版 `007dcfac`（命令位置の公開資料なし） · `007dcfcc`（命令位置の公開資料なし）

~~~diff
- 007dcf54 ["INT_ADD", "register:40f0:8", ["const:7dcf54:8", "const:4:8"]]
- 007dcf54 ["CALL", null, ["callee:00c53da0:8"]]
+ 007dcfac ["INT_ADD", "register:40f0:8", ["const:7dcfac:8", "const:4:8"]]
+ 007dcfac ["CALL", null, ["callee:00c53da0:8"]]
- 007dcf54 bytes 6bdb1194
+ 007dcfac bytes 7ddb1194
- 007dcf74 ["COPY", "register:0:8", ["register:4040:8"]]
- 007dcf74 ["INT_ADD", "register:40f0:8", ["const:7dcf74:8", "const:4:8"]]
- 007dcf74 ["CALLIND", null, ["register:0:8"]]
+ 007dcfcc ["COPY", "register:0:8", ["register:4040:8"]]
+ 007dcfcc ["INT_ADD", "register:40f0:8", ["const:7dcfcc:8", "const:4:8"]]
+ 007dcfcc ["CALLIND", null, ["register:0:8"]]
- 007dcf74 bytes 00013fd6
+ 007dcfcc bytes 00013fd6
~~~


<a id="compare-91128f5cb1d036f3a03ab702117df0fb"></a>

### [`007dcf88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dc/007dcf88.md) → [`007dcfe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007dc/007dcfe0.md) FUN_007dcfe0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00914e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00914/00914e30.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 2件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`00914e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00914/00914e84.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007dcfac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dc/007dcf88.md#insn-007dcfac) · [`007dcff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dc/007dcf88.md#insn-007dcff4) · [`007dd014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dc/007dcf88.md#insn-007dd014)
- 新版 `007dd004`（命令位置の公開資料なし） · `007dd04c`（命令位置の公開資料なし） · `007dd06c`（命令位置の公開資料なし）

~~~diff
- 007dcfac ["INT_ADD", "register:40f0:8", ["const:7dcfac:8", "const:4:8"]]
- 007dcfac ["CALL", null, ["callee:00c580b0:8"]]
+ 007dd004 ["INT_ADD", "register:40f0:8", ["const:7dd004:8", "const:4:8"]]
+ 007dd004 ["CALL", null, ["callee:00c580b0:8"]]
- 007dcfac bytes 0dec1194
+ 007dd004 bytes 2bec1194
- 007dcff4 ["INT_ADD", "register:40f0:8", ["const:7dcff4:8", "const:4:8"]]
- 007dcff4 ["CALL", null, ["callee:00c57f60:8"]]
+ 007dd04c ["INT_ADD", "register:40f0:8", ["const:7dd04c:8", "const:4:8"]]
+ 007dd04c ["CALL", null, ["callee:00c57f60:8"]]
- 007dcff4 bytes a7eb1194
+ 007dd04c bytes c5eb1194
- 007dd014 ["INT_ADD", "register:40f0:8", ["const:7dd014:8", "const:4:8"]]
- 007dd014 ["CALL", null, ["callee:00c58010:8"]]
+ 007dd06c ["INT_ADD", "register:40f0:8", ["const:7dd06c:8", "const:4:8"]]
+ 007dd06c ["CALL", null, ["callee:00c58010:8"]]
- 007dd014 bytes cbeb1194
+ 007dd06c bytes e9eb1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9d6485e0cbbe5b4e2c6ef42c03ca0ea"></a>

### [`007dd050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd050.md) → [`007dd0a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007dd/007dd0a8.md) FUN_007dd0a8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 5件 [`005e4e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4e74.md) [`0066a408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066a/0066a408.md) [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00a68f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68f48.md)
- 新版 呼出元 3件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) [`00a47f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47f54.md) · 呼出先 5件 [`005e4eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e4/005e4eb4.md) [`0066a448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066a/0066a448.md) [`00802710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802710.md) [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md) [`00a68fb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a68/00a68fb8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007dd070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd050.md#insn-007dd070) · [`007dd080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd050.md#insn-007dd080) · [`007dd094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd050.md#insn-007dd094)
- 新版 `007dd0c8`（命令位置の公開資料なし） · `007dd0d8`（命令位置の公開資料なし） · `007dd0ec`（命令位置の公開資料なし）

~~~diff
- 007dd070 ["INT_ADD", "register:40f0:8", ["const:7dd070:8", "const:4:8"]]
- 007dd070 ["CALL", null, ["callee:00802bb0:8"]]
+ 007dd0c8 ["INT_ADD", "register:40f0:8", ["const:7dd0c8:8", "const:4:8"]]
+ 007dd0c8 ["CALL", null, ["callee:00802bb0:8"]]
- 007dd070 bytes ba960094
+ 007dd0c8 bytes ba960094
- 007dd080 ["INT_ADD", "register:40f0:8", ["const:7dd080:8", "const:4:8"]]
- 007dd080 ["CALL", null, ["callee:0066a448:8"]]
+ 007dd0d8 ["INT_ADD", "register:40f0:8", ["const:7dd0d8:8", "const:4:8"]]
+ 007dd0d8 ["CALL", null, ["callee:0066a448:8"]]
- 007dd080 bytes e234fa97
+ 007dd0d8 bytes dc34fa97
- 007dd094 ["INT_ADD", "register:40f0:8", ["const:7dd094:8", "const:4:8"]]
- 007dd094 ["CALL", null, ["callee:00802710:8"]]
+ 007dd0ec ["INT_ADD", "register:40f0:8", ["const:7dd0ec:8", "const:4:8"]]
+ 007dd0ec ["CALL", null, ["callee:00802710:8"]]
- 007dd094 bytes 89950094
+ 007dd0ec bytes 89950094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ddcb7fc11f924fea8419d7abeead4e9"></a>

### [`007dd0f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd0f8.md) → [`007dd150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007dd/007dd150.md) FUN_007dd150

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007dd11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd0f8.md#insn-007dd11c) · [`007dd164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd0f8.md#insn-007dd164) · [`007dd184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd0f8.md#insn-007dd184)
- 新版 `007dd174`（命令位置の公開資料なし） · `007dd1bc`（命令位置の公開資料なし） · `007dd1dc`（命令位置の公開資料なし）

~~~diff
- 007dd11c ["INT_ADD", "register:40f0:8", ["const:7dd11c:8", "const:4:8"]]
- 007dd11c ["CALL", null, ["callee:00c580b0:8"]]
+ 007dd174 ["INT_ADD", "register:40f0:8", ["const:7dd174:8", "const:4:8"]]
+ 007dd174 ["CALL", null, ["callee:00c580b0:8"]]
- 007dd11c bytes b1eb1194
+ 007dd174 bytes cfeb1194
- 007dd164 ["INT_ADD", "register:40f0:8", ["const:7dd164:8", "const:4:8"]]
- 007dd164 ["CALL", null, ["callee:00c57f60:8"]]
+ 007dd1bc ["INT_ADD", "register:40f0:8", ["const:7dd1bc:8", "const:4:8"]]
+ 007dd1bc ["CALL", null, ["callee:00c57f60:8"]]
- 007dd164 bytes 4beb1194
+ 007dd1bc bytes 69eb1194
- 007dd184 ["INT_ADD", "register:40f0:8", ["const:7dd184:8", "const:4:8"]]
- 007dd184 ["CALL", null, ["callee:00c58010:8"]]
+ 007dd1dc ["INT_ADD", "register:40f0:8", ["const:7dd1dc:8", "const:4:8"]]
+ 007dd1dc ["CALL", null, ["callee:00c58010:8"]]
- 007dd184 bytes 6feb1194
+ 007dd1dc bytes 8deb1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-366351642a37b76258d37790c9463306"></a>

### [`007dd1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd1c0.md) → [`007dd218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007dd/007dd218.md) FUN_007dd218

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007dd1e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd1c0.md#insn-007dd1e4) · [`007dd22c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd1c0.md#insn-007dd22c) · [`007dd24c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd1c0.md#insn-007dd24c)
- 新版 `007dd23c`（命令位置の公開資料なし） · `007dd284`（命令位置の公開資料なし） · `007dd2a4`（命令位置の公開資料なし）

~~~diff
- 007dd1e4 ["INT_ADD", "register:40f0:8", ["const:7dd1e4:8", "const:4:8"]]
- 007dd1e4 ["CALL", null, ["callee:00c580b0:8"]]
+ 007dd23c ["INT_ADD", "register:40f0:8", ["const:7dd23c:8", "const:4:8"]]
+ 007dd23c ["CALL", null, ["callee:00c580b0:8"]]
- 007dd1e4 bytes 7feb1194
+ 007dd23c bytes 9deb1194
- 007dd22c ["INT_ADD", "register:40f0:8", ["const:7dd22c:8", "const:4:8"]]
- 007dd22c ["CALL", null, ["callee:00c57f60:8"]]
+ 007dd284 ["INT_ADD", "register:40f0:8", ["const:7dd284:8", "const:4:8"]]
+ 007dd284 ["CALL", null, ["callee:00c57f60:8"]]
- 007dd22c bytes 19eb1194
+ 007dd284 bytes 37eb1194
- 007dd24c ["INT_ADD", "register:40f0:8", ["const:7dd24c:8", "const:4:8"]]
- 007dd24c ["CALL", null, ["callee:00c58010:8"]]
+ 007dd2a4 ["INT_ADD", "register:40f0:8", ["const:7dd2a4:8", "const:4:8"]]
+ 007dd2a4 ["CALL", null, ["callee:00c58010:8"]]
- 007dd24c bytes 3deb1194
+ 007dd2a4 bytes 5beb1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abada492e7e7fb15a98a4495b965844b"></a>

### [`007dd288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd288.md) → [`007dd2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007dd/007dd2e0.md) FUN_007dd2e0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007dd2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd288.md#insn-007dd2f0) · [`007dd33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd288.md#insn-007dd33c)
- 新版 `007dd348`（命令位置の公開資料なし） · `007dd394`（命令位置の公開資料なし）

~~~diff
- 007dd2f0 ["INT_ADD", "register:40f0:8", ["const:7dd2f0:8", "const:4:8"]]
- 007dd2f0 ["CALL", null, ["callee:00c57f60:8"]]
+ 007dd348 ["INT_ADD", "register:40f0:8", ["const:7dd348:8", "const:4:8"]]
+ 007dd348 ["CALL", null, ["callee:00c57f60:8"]]
- 007dd2f0 bytes e8ea1194
+ 007dd348 bytes 06eb1194
- 007dd33c ["INT_ADD", "register:40f0:8", ["const:7dd33c:8", "const:4:8"]]
- 007dd33c ["CALL", null, ["callee:0043bbe4:8"]]
+ 007dd394 ["INT_ADD", "register:40f0:8", ["const:7dd394:8", "const:4:8"]]
+ 007dd394 ["CALL", null, ["callee:0043bbe4:8"]]
- 007dd33c bytes 1a7af197
+ 007dd394 bytes 147af197
~~~


<a id="compare-70f8a146960b391c5dbc06d6fbba04fc"></a>

### [`007de528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007de/007de528.md) → [`007de580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007de/007de580.md) FUN_007de580

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`00a65dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a65/00a65dec.md) [`00ab31a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab3/00ab31a4.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 4件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) [`00a65e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a65/00a65e5c.md) [`00ab3214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ab3/00ab3214.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007de590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007de/007de528.md#insn-007de590) · [`007de5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007de/007de528.md#insn-007de5d4)
- 新版 `007de5e8`（命令位置の公開資料なし） · `007de62c`（命令位置の公開資料なし）

~~~diff
- 007de590 ["INT_ADD", "register:40f0:8", ["const:7de590:8", "const:4:8"]]
- 007de590 ["CALL", null, ["callee:00c57f60:8"]]
+ 007de5e8 ["INT_ADD", "register:40f0:8", ["const:7de5e8:8", "const:4:8"]]
+ 007de5e8 ["CALL", null, ["callee:00c57f60:8"]]
- 007de590 bytes 40e61194
+ 007de5e8 bytes 5ee61194
- 007de5d4 ["INT_ADD", "register:40f0:8", ["const:7de5d4:8", "const:4:8"]]
- 007de5d4 ["CALL", null, ["callee:0043bbe4:8"]]
+ 007de62c ["INT_ADD", "register:40f0:8", ["const:7de62c:8", "const:4:8"]]
+ 007de62c ["CALL", null, ["callee:0043bbe4:8"]]
- 007de5d4 bytes 7475f197
+ 007de62c bytes 6e75f197
~~~


<a id="compare-3d9cb2fa964d503d09152baaa62a30a4"></a>

### [`007de860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007de/007de860.md) → [`007de8b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007de/007de8b8.md) FUN_007de8b8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 2件 [`00903f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00903/00903f44.md) [`009e0fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0fc0.md)
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 2件 [`00903f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00903/00903f98.md) [`009e1014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e1/009e1014.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007de890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007de/007de860.md#insn-007de890)
- 新版 `007de8e8`（命令位置の公開資料なし）

~~~diff
- 007de890 ["INT_ADD", "register:40f0:8", ["const:7de890:8", "const:4:8"]]
- 007de890 ["CALL", null, ["callee:00903f98:8"]]
+ 007de8e8 ["INT_ADD", "register:40f0:8", ["const:7de8e8:8", "const:4:8"]]
+ 007de8e8 ["CALL", null, ["callee:00903f98:8"]]
- 007de890 bytes ad950494
+ 007de8e8 bytes ac950494
~~~


<a id="compare-58b02f7d8fc8a04fbf9fa79a327836f9"></a>

### [`007df024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df024.md) → [`007df07c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df07c.md) FUN_007df07c

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007f296c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f296c.md) · 呼出先 5件 [`00a43138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a43/00a43138.md) [`00a83260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a83/00a83260.md) [`00a8344c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a83/00a8344c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`007f29c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f2/007f29c4.md) · 呼出先 5件 [`00a4318c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a43/00a4318c.md) [`00a832d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a83/00a832d0.md) [`00a834bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a83/00a834bc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007df054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df024.md#insn-007df054) · [`007df068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df024.md#insn-007df068) · [`007df080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df024.md#insn-007df080)
- 新版 `007df0ac`（命令位置の公開資料なし） · `007df0c0`（命令位置の公開資料なし） · `007df0d8`（命令位置の公開資料なし）

~~~diff
- 007df054 ["INT_ADD", "register:40f0:8", ["const:7df054:8", "const:4:8"]]
- 007df054 ["CALL", null, ["callee:00a832d0:8"]]
+ 007df0ac ["INT_ADD", "register:40f0:8", ["const:7df0ac:8", "const:4:8"]]
+ 007df0ac ["CALL", null, ["callee:00a832d0:8"]]
- 007df054 bytes 83900a94
+ 007df0ac bytes 89900a94
- 007df068 ["INT_ADD", "register:40f0:8", ["const:7df068:8", "const:4:8"]]
- 007df068 ["CALL", null, ["callee:00a4318c:8"]]
+ 007df0c0 ["INT_ADD", "register:40f0:8", ["const:7df0c0:8", "const:4:8"]]
+ 007df0c0 ["CALL", null, ["callee:00a4318c:8"]]
- 007df068 bytes 34900994
+ 007df0c0 bytes 33900994
- 007df080 ["INT_ADD", "register:40f0:8", ["const:7df080:8", "const:4:8"]]
- 007df080 ["CALL", null, ["callee:00a834bc:8"]]
+ 007df0d8 ["INT_ADD", "register:40f0:8", ["const:7df0d8:8", "const:4:8"]]
+ 007df0d8 ["CALL", null, ["callee:00a834bc:8"]]
- 007df080 bytes f3900a94
+ 007df0d8 bytes f9900a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4f3775ad386f18ecd0169e008d89813"></a>

### [`007ef320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef320.md) → [`007ef378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007ef378.md) FUN_007ef378

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 8件 [`005e4e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4e74.md) [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`00802b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b8c.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) [`00a06674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06674.md)
- 新版 呼出元 1件 [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 8件 [`005e4eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e4/005e4eb4.md) [`00802710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802710.md) [`00802be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802be4.md) [`00802d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802d00.md) [`00a066c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a066c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007ef338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef320.md#insn-007ef338) · [`007ef344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef320.md#insn-007ef344) · [`007ef34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef320.md#insn-007ef34c)
- 新版 `007ef390`（命令位置の公開資料なし） · `007ef39c`（命令位置の公開資料なし） · `007ef3a4`（命令位置の公開資料なし）

~~~diff
- 007ef338 ["INT_ADD", "register:40f0:8", ["const:7ef338:8", "const:4:8"]]
- 007ef338 ["CALL", null, ["callee:00802710:8"]]
+ 007ef390 ["INT_ADD", "register:40f0:8", ["const:7ef390:8", "const:4:8"]]
+ 007ef390 ["CALL", null, ["callee:00802710:8"]]
- 007ef338 bytes e04c0094
+ 007ef390 bytes e04c0094
- 007ef344 ["INT_ADD", "register:40f0:8", ["const:7ef344:8", "const:4:8"]]
- 007ef344 ["CALL", null, ["callee:00802be4:8"]]
+ 007ef39c ["INT_ADD", "register:40f0:8", ["const:7ef39c:8", "const:4:8"]]
+ 007ef39c ["CALL", null, ["callee:00802be4:8"]]
- 007ef344 bytes 124e0094
+ 007ef39c bytes 124e0094
- 007ef34c ["INT_ADD", "register:40f0:8", ["const:7ef34c:8", "const:4:8"]]
- 007ef34c ["CALL", null, ["callee:00802d00:8"]]
+ 007ef3a4 ["INT_ADD", "register:40f0:8", ["const:7ef3a4:8", "const:4:8"]]
+ 007ef3a4 ["CALL", null, ["callee:00802d00:8"]]
- 007ef34c bytes 574e0094
+ 007ef3a4 bytes 574e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f3b3feb03b79c888e9adc63603fab33"></a>

### [`007ef3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef3f0.md) → [`007ef448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007ef448.md) FUN_007ef448

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`007534d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00753/007534d0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00753528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/00753528.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007ef498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef3f0.md#insn-007ef498) · [`007ef4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef3f0.md#insn-007ef4dc) · [`007ef4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef3f0.md#insn-007ef4f0)
- 新版 `007ef4f0`（命令位置の公開資料なし） · `007ef534`（命令位置の公開資料なし） · `007ef548`（命令位置の公開資料なし）

~~~diff
- 007ef498 ["INT_ADD", "register:40f0:8", ["const:7ef498:8", "const:4:8"]]
- 007ef498 ["CALL", null, ["callee:00c57f60:8"]]
+ 007ef4f0 ["INT_ADD", "register:40f0:8", ["const:7ef4f0:8", "const:4:8"]]
+ 007ef4f0 ["CALL", null, ["callee:00c57f60:8"]]
- 007ef498 bytes 7ea21194
+ 007ef4f0 bytes 9ca21194
- 007ef4dc ["INT_ADD", "register:40f0:8", ["const:7ef4dc:8", "const:4:8"]]
- 007ef4dc ["CALL", null, ["callee:00c580d0:8"]]
+ 007ef534 ["INT_ADD", "register:40f0:8", ["const:7ef534:8", "const:4:8"]]
+ 007ef534 ["CALL", null, ["callee:00c580d0:8"]]
- 007ef4dc bytes c9a21194
+ 007ef534 bytes e7a21194
- 007ef4f0 ["INT_ADD", "register:40f0:8", ["const:7ef4f0:8", "const:4:8"]]
- 007ef4f0 ["CALL", null, ["callee:00c57f80:8"]]
+ 007ef548 ["INT_ADD", "register:40f0:8", ["const:7ef548:8", "const:4:8"]]
+ 007ef548 ["CALL", null, ["callee:00c57f80:8"]]
- 007ef4f0 bytes 70a21194
+ 007ef548 bytes 8ea21194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3a662e808d0bc7dad813b4b57b21a75"></a>

### [`007ef5dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef5dc.md) → [`007ef634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007ef634.md) FUN_007ef634

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 5件 [`007534d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00753/007534d0.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 5件 [`00753528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/00753528.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007ef62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef5dc.md#insn-007ef62c) · [`007ef644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef5dc.md#insn-007ef644) · [`007ef660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef5dc.md#insn-007ef660)
- 新版 `007ef684`（命令位置の公開資料なし） · `007ef69c`（命令位置の公開資料なし） · `007ef6b8`（命令位置の公開資料なし）

~~~diff
- 007ef62c ["INT_ADD", "register:40f0:8", ["const:7ef62c:8", "const:4:8"]]
- 007ef62c ["CALL", null, ["callee:00c57f60:8"]]
+ 007ef684 ["INT_ADD", "register:40f0:8", ["const:7ef684:8", "const:4:8"]]
+ 007ef684 ["CALL", null, ["callee:00c57f60:8"]]
- 007ef62c bytes 19a21194
+ 007ef684 bytes 37a21194
- 007ef644 ["INT_ADD", "register:40f0:8", ["const:7ef644:8", "const:4:8"]]
- 007ef644 ["CALL", null, ["callee:00c580d0:8"]]
+ 007ef69c ["INT_ADD", "register:40f0:8", ["const:7ef69c:8", "const:4:8"]]
+ 007ef69c ["CALL", null, ["callee:00c580d0:8"]]
- 007ef644 bytes 6fa21194
+ 007ef69c bytes 8da21194
- 007ef660 ["INT_ADD", "register:40f0:8", ["const:7ef660:8", "const:4:8"]]
- 007ef660 ["CALL", null, ["callee:00753528:8"]]
+ 007ef6b8 ["INT_ADD", "register:40f0:8", ["const:7ef6b8:8", "const:4:8"]]
+ 007ef6b8 ["CALL", null, ["callee:00753528:8"]]
- 007ef660 bytes 9c8ffd97
+ 007ef6b8 bytes 9c8ffd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7f72547240a004b1a53b58920772a00"></a>

### [`007efa88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efa88.md) → [`007efae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007efae0.md) FUN_007efae0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`007cb5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb5e0.md) [`009e4a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e4/009e4a08.md) [`00a60748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a60/00a60748.md) [`00ab4d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab4/00ab4d00.md) · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 4件 [`007cb638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cb/007cb638.md) [`009e4a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e4/009e4a5c.md) [`00a607b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a60/00a607b8.md) [`00ab4d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ab4/00ab4d70.md) · 呼出先 5件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007efaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efa88.md#insn-007efaac) · [`007efaf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efa88.md#insn-007efaf4) · [`007efb14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efa88.md#insn-007efb14)
- 新版 `007efb04`（命令位置の公開資料なし） · `007efb4c`（命令位置の公開資料なし） · `007efb6c`（命令位置の公開資料なし）

~~~diff
- 007efaac ["INT_ADD", "register:40f0:8", ["const:7efaac:8", "const:4:8"]]
- 007efaac ["CALL", null, ["callee:00c580b0:8"]]
+ 007efb04 ["INT_ADD", "register:40f0:8", ["const:7efb04:8", "const:4:8"]]
+ 007efb04 ["CALL", null, ["callee:00c580b0:8"]]
- 007efaac bytes 4da11194
+ 007efb04 bytes 6ba11194
- 007efaf4 ["INT_ADD", "register:40f0:8", ["const:7efaf4:8", "const:4:8"]]
- 007efaf4 ["CALL", null, ["callee:00c57f60:8"]]
+ 007efb4c ["INT_ADD", "register:40f0:8", ["const:7efb4c:8", "const:4:8"]]
+ 007efb4c ["CALL", null, ["callee:00c57f60:8"]]
- 007efaf4 bytes e7a01194
+ 007efb4c bytes 05a11194
- 007efb14 ["INT_ADD", "register:40f0:8", ["const:7efb14:8", "const:4:8"]]
- 007efb14 ["CALL", null, ["callee:00c58010:8"]]
+ 007efb6c ["INT_ADD", "register:40f0:8", ["const:7efb6c:8", "const:4:8"]]
+ 007efb6c ["CALL", null, ["callee:00c58010:8"]]
- 007efb14 bytes 0ba11194
+ 007efb6c bytes 29a11194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d47ce30904cab5780c036db04199a6ee"></a>

### [`007efb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efb7c.md) → [`007efbd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007efbd4.md) FUN_007efbd4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00934078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934078.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) [`00afe40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afe40c.md) [`00aff62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aff/00aff62c.md) · 呼出先 2件 [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`00802b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b8c.md)
- 新版 呼出元 4件 [`009340cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00934/009340cc.md) [`00a47f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47f54.md) [`00afe4a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afe/00afe4a8.md) [`00aff6c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aff/00aff6c8.md) · 呼出先 2件 [`00802710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802710.md) [`00802be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802be4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007efb88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efb7c.md#insn-007efb88) · [`007efb9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efb7c.md#insn-007efb9c)
- 新版 `007efbe0`（命令位置の公開資料なし） · `007efbf4`（命令位置の公開資料なし）

~~~diff
- 007efb88 ["INT_ADD", "register:40f0:8", ["const:7efb88:8", "const:4:8"]]
- 007efb88 ["CALL", null, ["callee:00802710:8"]]
+ 007efbe0 ["INT_ADD", "register:40f0:8", ["const:7efbe0:8", "const:4:8"]]
+ 007efbe0 ["CALL", null, ["callee:00802710:8"]]
- 007efb88 bytes cc4a0094
+ 007efbe0 bytes cc4a0094
- 007efb9c ["INT_ADD", "register:40f0:8", ["const:7efb9c:8", "const:4:8"]]
- 007efb9c ["CALL", null, ["callee:00802be4:8"]]
+ 007efbf4 ["INT_ADD", "register:40f0:8", ["const:7efbf4:8", "const:4:8"]]
+ 007efbf4 ["CALL", null, ["callee:00802be4:8"]]
- 007efb9c bytes fc4b0094
+ 007efbf4 bytes fc4b0094
~~~


<a id="compare-f1fc8f7cd7618a6d9145908f080ec8d6"></a>

### [`007f03d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f03d4.md) → [`007f042c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f0/007f042c.md) FUN_007f042c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007caac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007caac8.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`007cab20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ca/007cab20.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f0490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f03d4.md#insn-007f0490) · [`007f04b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f03d4.md#insn-007f04b8) · [`007f04cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f03d4.md#insn-007f04cc)
- 新版 `007f04e8`（命令位置の公開資料なし） · `007f0510`（命令位置の公開資料なし） · `007f0524`（命令位置の公開資料なし）

~~~diff
- 007f0490 ["INT_ADD", "register:40f0:8", ["const:7f0490:8", "const:4:8"]]
- 007f0490 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f04e8 ["INT_ADD", "register:40f0:8", ["const:7f04e8:8", "const:4:8"]]
+ 007f04e8 ["CALL", null, ["callee:00c57f60:8"]]
- 007f0490 bytes 809e1194
+ 007f04e8 bytes 9e9e1194
- 007f04b8 ["INT_ADD", "register:40f0:8", ["const:7f04b8:8", "const:4:8"]]
- 007f04b8 ["CALL", null, ["callee:00c580d0:8"]]
+ 007f0510 ["INT_ADD", "register:40f0:8", ["const:7f0510:8", "const:4:8"]]
+ 007f0510 ["CALL", null, ["callee:00c580d0:8"]]
- 007f04b8 bytes d29e1194
+ 007f0510 bytes f09e1194
- 007f04cc ["INT_ADD", "register:40f0:8", ["const:7f04cc:8", "const:4:8"]]
- 007f04cc ["CALL", null, ["callee:00c57f80:8"]]
+ 007f0524 ["INT_ADD", "register:40f0:8", ["const:7f0524:8", "const:4:8"]]
+ 007f0524 ["CALL", null, ["callee:00c57f80:8"]]
- 007f04cc bytes 799e1194
+ 007f0524 bytes 979e1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18b17798a613b7d68dfc1196ea4c2f66"></a>

### [`007f0c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0c74.md) → [`007f0ccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f0/007f0ccc.md) FUN_007f0ccc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`007f06f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f06f4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`007f074c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f0/007f074c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f0c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0c74.md#insn-007f0c84)
- 新版 `007f0cdc`（命令位置の公開資料なし）

~~~diff
- 007f0c84 ["INT_ADD", "register:40f0:8", ["const:7f0c84:8", "const:4:8"]]
- 007f0c84 ["CALL", null, ["callee:007f074c:8"]]
+ 007f0cdc ["INT_ADD", "register:40f0:8", ["const:7f0cdc:8", "const:4:8"]]
+ 007f0cdc ["CALL", null, ["callee:007f074c:8"]]
- 007f0c84 bytes 9cfeff97
+ 007f0cdc bytes 9cfeff97
~~~


<a id="compare-3c0b64eeae4a4dd021719cba27ecca7d"></a>

### [`007f0c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0c98.md) → [`007f0cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f0/007f0cf0.md) FUN_007f0cf0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007bbaf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbaf4.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`007f0dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0dd4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`007bbb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bb/007bbb4c.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`007f0e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f0/007f0e2c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f0cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0c98.md#insn-007f0cf8) · [`007f0d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0c98.md#insn-007f0d08) · [`007f0d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0c98.md#insn-007f0d40)
- 新版 `007f0d50`（命令位置の公開資料なし） · `007f0d60`（命令位置の公開資料なし） · `007f0d98`（命令位置の公開資料なし）

~~~diff
- 007f0cf8 ["INT_ADD", "register:40f0:8", ["const:7f0cf8:8", "const:4:8"]]
- 007f0cf8 ["CALL", null, ["callee:0043bb60:8"]]
+ 007f0d50 ["INT_ADD", "register:40f0:8", ["const:7f0d50:8", "const:4:8"]]
+ 007f0d50 ["CALL", null, ["callee:0043bb60:8"]]
- 007f0cf8 bytes 8a2bf197
+ 007f0d50 bytes 842bf197
- 007f0d08 ["INT_ADD", "register:40f0:8", ["const:7f0d08:8", "const:4:8"]]
- 007f0d08 ["CALL", null, ["callee:0043bb60:8"]]
+ 007f0d60 ["INT_ADD", "register:40f0:8", ["const:7f0d60:8", "const:4:8"]]
+ 007f0d60 ["CALL", null, ["callee:0043bb60:8"]]
- 007f0d08 bytes 862bf197
+ 007f0d60 bytes 802bf197
- 007f0d40 ["INT_ADD", "register:40f0:8", ["const:7f0d40:8", "const:4:8"]]
- 007f0d40 ["CALL", null, ["callee:007f0e2c:8"]]
+ 007f0d98 ["INT_ADD", "register:40f0:8", ["const:7f0d98:8", "const:4:8"]]
+ 007f0d98 ["CALL", null, ["callee:007f0e2c:8"]]
- 007f0d40 bytes 25000094
+ 007f0d98 bytes 25000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89b185afb99b8385b4ea68dc0a5c82ba"></a>

### [`007f1894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1894.md) → [`007f18ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f18ec.md) FUN_007f18ec

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007bbe1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbe1c.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`007f1ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ab8.md) [`007f1e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1e90.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`007bbe74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bb/007bbe74.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e8e4.md) [`007f1b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1b10.md) [`007f1ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1ee8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f1954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1894.md#insn-007f1954) · [`007f197c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1894.md#insn-007f197c) · [`007f19c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1894.md#insn-007f19c4)
- 新版 `007f19ac`（命令位置の公開資料なし） · `007f19d4`（命令位置の公開資料なし） · `007f1a1c`（命令位置の公開資料なし）

~~~diff
- 007f1954 ["INT_ADD", "register:40f0:8", ["const:7f1954:8", "const:4:8"]]
- 007f1954 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f19ac ["INT_ADD", "register:40f0:8", ["const:7f19ac:8", "const:4:8"]]
+ 007f19ac ["CALL", null, ["callee:00c57f60:8"]]
- 007f1954 bytes 4f991194
+ 007f19ac bytes 6d991194
- 007f197c ["INT_ADD", "register:40f0:8", ["const:7f197c:8", "const:4:8"]]
- 007f197c ["CALL", null, ["callee:007f1b10:8"]]
+ 007f19d4 ["INT_ADD", "register:40f0:8", ["const:7f19d4:8", "const:4:8"]]
+ 007f19d4 ["CALL", null, ["callee:007f1b10:8"]]
- 007f197c bytes 4f000094
+ 007f19d4 bytes 4f000094
- 007f19c4 ["INT_ADD", "register:40f0:8", ["const:7f19c4:8", "const:4:8"]]
- 007f19c4 ["CALL", null, ["callee:007f1b10:8"]]
+ 007f1a1c ["INT_ADD", "register:40f0:8", ["const:7f1a1c:8", "const:4:8"]]
+ 007f1a1c ["CALL", null, ["callee:007f1b10:8"]]
- 007f19c4 bytes 3d000094
+ 007f1a1c bytes 3d000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-697255f2c35fafed2070ba79a086c135"></a>

### [`007f1ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ab8.md) → [`007f1b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1b10.md) FUN_007f1b10

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007f1894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1894.md) [`009012d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00901/009012d8.md) · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0046e82c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e82c.md) [`00470354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470354.md) [`007f1cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1cb0.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)
- 新版 呼出元 2件 [`007f18ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f18ec.md) [`0090132c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00901/0090132c.md) · 呼出先 7件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0046e86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e86c.md) [`00470394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470394.md) [`007f1d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1d08.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f1b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ab8.md#insn-007f1b30) · [`007f1b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ab8.md#insn-007f1b54) · [`007f1b9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ab8.md#insn-007f1b9c)
- 新版 `007f1b88`（命令位置の公開資料なし） · `007f1bac`（命令位置の公開資料なし） · `007f1bf4`（命令位置の公開資料なし）

~~~diff
- 007f1b30 ["INT_ADD", "register:40f0:8", ["const:7f1b30:8", "const:4:8"]]
- 007f1b30 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f1b88 ["INT_ADD", "register:40f0:8", ["const:7f1b88:8", "const:4:8"]]
+ 007f1b88 ["CALL", null, ["callee:00c57f60:8"]]
- 007f1b30 bytes d8981194
+ 007f1b88 bytes f6981194
- 007f1b54 ["INT_ADD", "register:40f0:8", ["const:7f1b54:8", "const:4:8"]]
- 007f1b54 ["CALL", null, ["callee:007f1d08:8"]]
+ 007f1bac ["INT_ADD", "register:40f0:8", ["const:7f1bac:8", "const:4:8"]]
+ 007f1bac ["CALL", null, ["callee:007f1d08:8"]]
- 007f1b54 bytes 57000094
+ 007f1bac bytes 57000094
- 007f1b9c ["INT_ADD", "register:40f0:8", ["const:7f1b9c:8", "const:4:8"]]
- 007f1b9c ["CALL", null, ["callee:0043bb60:8"]]
+ 007f1bf4 ["INT_ADD", "register:40f0:8", ["const:7f1bf4:8", "const:4:8"]]
+ 007f1bf4 ["CALL", null, ["callee:0043bb60:8"]]
- 007f1b9c bytes e127f197
+ 007f1bf4 bytes db27f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dde471d7e22103c375de209611389f5"></a>

### [`007f1c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1c28.md) → [`007f1c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1c80.md) FUN_007f1c80

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f1c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1c28.md#insn-007f1c8c)
- 新版 `007f1ce4`（命令位置の公開資料なし）

~~~diff
- 007f1c8c ["INT_ADD", "register:40f0:8", ["const:7f1c8c:8", "const:4:8"]]
- 007f1c8c ["CALL", null, ["callee:00c57f80:8"]]
+ 007f1ce4 ["INT_ADD", "register:40f0:8", ["const:7f1ce4:8", "const:4:8"]]
+ 007f1ce4 ["CALL", null, ["callee:00c57f80:8"]]
- 007f1c8c bytes 89981194
+ 007f1ce4 bytes a7981194
~~~


<a id="compare-e32ec4b7a6a5c3fba46ddb9e26f6038b"></a>

### [`007f1cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1cb0.md) → [`007f1d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1d08.md) FUN_007f1d08

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`007bbe1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbe1c.md) [`007f1ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ab8.md) [`008ff8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff8cc.md) [`00a3f34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3f/00a3f34c.md) · 呼出先 7件 [`00470494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470494.md) [`007f1de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1de8.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`007bbe74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bb/007bbe74.md) [`007f1b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1b10.md) [`008ff920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ff/008ff920.md) [`00a3f3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3f/00a3f3a0.md) · 呼出先 7件 [`004704d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004704d4.md) [`007f1e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1e40.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f1d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1cb0.md#insn-007f1d40) · [`007f1d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1cb0.md#insn-007f1d58) · [`007f1da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1cb0.md#insn-007f1da8)
- 新版 `007f1d98`（命令位置の公開資料なし） · `007f1db0`（命令位置の公開資料なし） · `007f1e00`（命令位置の公開資料なし）

~~~diff
- 007f1d40 ["INT_ADD", "register:40f0:8", ["const:7f1d40:8", "const:4:8"]]
- 007f1d40 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f1d98 ["INT_ADD", "register:40f0:8", ["const:7f1d98:8", "const:4:8"]]
+ 007f1d98 ["CALL", null, ["callee:00c57f60:8"]]
- 007f1d40 bytes 54981194
+ 007f1d98 bytes 72981194
- 007f1d58 ["INT_ADD", "register:40f0:8", ["const:7f1d58:8", "const:4:8"]]
- 007f1d58 ["CALL", null, ["callee:00c580d0:8"]]
+ 007f1db0 ["INT_ADD", "register:40f0:8", ["const:7f1db0:8", "const:4:8"]]
+ 007f1db0 ["CALL", null, ["callee:00c580d0:8"]]
- 007f1d58 bytes aa981194
+ 007f1db0 bytes c8981194
- 007f1da8 ["INT_ADD", "register:40f0:8", ["const:7f1da8:8", "const:4:8"]]
- 007f1da8 ["CALL", null, ["callee:004704d4:8"]]
+ 007f1e00 ["INT_ADD", "register:40f0:8", ["const:7f1e00:8", "const:4:8"]]
+ 007f1e00 ["CALL", null, ["callee:004704d4:8"]]
- 007f1da8 bytes bbf9f197
+ 007f1e00 bytes b5f9f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1173d104c0415b221cf1b25f75945e38"></a>

### [`007f1de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1de8.md) → [`007f1e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1e40.md) FUN_007f1e40

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007f1cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1cb0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`007f1d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1d08.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f1e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1de8.md#insn-007f1e28)
- 新版 `007f1e80`（命令位置の公開資料なし）

~~~diff
- 007f1e28 ["INT_ADD", "register:40f0:8", ["const:7f1e28:8", "const:4:8"]]
- 007f1e28 ["CALL", null, ["callee:00c57f80:8"]]
+ 007f1e80 ["INT_ADD", "register:40f0:8", ["const:7f1e80:8", "const:4:8"]]
+ 007f1e80 ["CALL", null, ["callee:00c57f80:8"]]
- 007f1e28 bytes 22981194
+ 007f1e80 bytes 40981194
~~~


<a id="compare-94233e89a29ff8c824468f5d3ee3eced"></a>

### [`007f1e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1e3c.md) → [`007f1e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1e94.md) FUN_007f1e94

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e8e4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f1e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1e3c.md#insn-007f1e60)
- 新版 `007f1eb8`（命令位置の公開資料なし）

~~~diff
- 007f1e60 ["INT_ADD", "register:40f0:8", ["const:7f1e60:8", "const:4:8"]]
- 007f1e60 ["CALL", null, ["callee:0046e8e4:8"]]
+ 007f1eb8 ["INT_ADD", "register:40f0:8", ["const:7f1eb8:8", "const:4:8"]]
+ 007f1eb8 ["CALL", null, ["callee:0046e8e4:8"]]
- 007f1e60 bytes 91f2f197
+ 007f1eb8 bytes 8bf2f197
~~~


<a id="compare-7e0db53390e0820512eda2abec92991f"></a>

### [`007f3e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3e68.md) → [`007f3ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f3ec0.md) FUN_007f3ec0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a880.md)
- 新版 呼出元 1件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a950.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f3e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3e68.md#insn-007f3e78)
- 新版 `007f3ed0`（命令位置の公開資料なし）

~~~diff
- 007f3e78 ["INT_ADD", "register:40f0:8", ["const:7f3e78:8", "const:4:8"]]
- 007f3e78 ["CALL", null, ["callee:00c5a950:8"]]
+ 007f3ed0 ["INT_ADD", "register:40f0:8", ["const:7f3ed0:8", "const:4:8"]]
+ 007f3ed0 ["CALL", null, ["callee:00c5a950:8"]]
- 007f3e78 bytes 829a1194
+ 007f3ed0 bytes a09a1194
~~~


<a id="compare-41d3e65552bf00ab50e5258b43fcb31c"></a>

### [`007f45f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f45f8.md) → [`007f4650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f4/007f4650.md) FUN_007f4650

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`008b6f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f70.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f464c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f45f8.md#insn-007f464c) · [`007f465c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f45f8.md#insn-007f465c)
- 新版 `007f46a4`（命令位置の公開資料なし） · `007f46b4`（命令位置の公開資料なし）

~~~diff
- 007f464c ["INT_ADD", "register:40f0:8", ["const:7f464c:8", "const:4:8"]]
- 007f464c ["CALL", null, ["callee:008b7a20:8"]]
+ 007f46a4 ["INT_ADD", "register:40f0:8", ["const:7f46a4:8", "const:4:8"]]
+ 007f46a4 ["CALL", null, ["callee:008b7a20:8"]]
- 007f464c bytes df0c0394
+ 007f46a4 bytes df0c0394
- 007f465c ["INT_ADD", "register:40f0:8", ["const:7f465c:8", "const:4:8"]]
- 007f465c ["CALL", null, ["callee:008b7a20:8"]]
+ 007f46b4 ["INT_ADD", "register:40f0:8", ["const:7f46b4:8", "const:4:8"]]
+ 007f46b4 ["CALL", null, ["callee:008b7a20:8"]]
- 007f465c bytes db0c0394
+ 007f46b4 bytes db0c0394
~~~


<a id="compare-7d4a7e53e864112db8daefe2c7e36000"></a>

### [`007f46f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f46f8.md) → [`007f4750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f4/007f4750.md) FUN_007f4750

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`008b6a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6a5c.md) [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)
- 新版 呼出元 0件  · 呼出先 3件 [`008b6ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6ab4.md) [`008b6f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f70.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f4714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f46f8.md#insn-007f4714) · [`007f4724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f46f8.md#insn-007f4724) · [`007f4750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f46f8.md#insn-007f4750)
- 新版 `007f476c`（命令位置の公開資料なし） · `007f477c`（命令位置の公開資料なし） · `007f47a8`（命令位置の公開資料なし）

~~~diff
- 007f4714 ["INT_ADD", "register:40f0:8", ["const:7f4714:8", "const:4:8"]]
- 007f4714 ["CALL", null, ["callee:008b7a20:8"]]
+ 007f476c ["INT_ADD", "register:40f0:8", ["const:7f476c:8", "const:4:8"]]
+ 007f476c ["CALL", null, ["callee:008b7a20:8"]]
- 007f4714 bytes ad0c0394
+ 007f476c bytes ad0c0394
- 007f4724 ["INT_ADD", "register:40f0:8", ["const:7f4724:8", "const:4:8"]]
- 007f4724 ["CALL", null, ["callee:008b7a20:8"]]
+ 007f477c ["INT_ADD", "register:40f0:8", ["const:7f477c:8", "const:4:8"]]
+ 007f477c ["CALL", null, ["callee:008b7a20:8"]]
- 007f4724 bytes a90c0394
+ 007f477c bytes a90c0394
- 007f4750 ["INT_ADD", "register:40f0:8", ["const:7f4750:8", "const:4:8"]]
- 007f4750 ["CALL", null, ["callee:008b6f70:8"]]
+ 007f47a8 ["INT_ADD", "register:40f0:8", ["const:7f47a8:8", "const:4:8"]]
+ 007f47a8 ["CALL", null, ["callee:008b6f70:8"]]
- 007f4750 bytes f2090394
+ 007f47a8 bytes f2090394
~~~


<a id="compare-f41284c8ef731a4c51d2149e4271d26a"></a>

### [`007f47e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f47e0.md) → [`007f4838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f4/007f4838.md) FUN_007f4838

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`008b6d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6d9c.md) [`008b6f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f10.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md) [`008b9290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9290.md)
- 新版 呼出元 0件  · 呼出先 4件 [`008b6df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6df4.md) [`008b6f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f68.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md) [`008b92e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b92e8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f4824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f47e0.md#insn-007f4824) · [`007f4834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f47e0.md#insn-007f4834) · [`007f4840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f47e0.md#insn-007f4840)
- 新版 `007f487c`（命令位置の公開資料なし） · `007f488c`（命令位置の公開資料なし） · `007f4898`（命令位置の公開資料なし）

~~~diff
- 007f4824 ["INT_ADD", "register:40f0:8", ["const:7f4824:8", "const:4:8"]]
- 007f4824 ["CALL", null, ["callee:008b7a20:8"]]
+ 007f487c ["INT_ADD", "register:40f0:8", ["const:7f487c:8", "const:4:8"]]
+ 007f487c ["CALL", null, ["callee:008b7a20:8"]]
- 007f4824 bytes 690c0394
+ 007f487c bytes 690c0394
- 007f4834 ["INT_ADD", "register:40f0:8", ["const:7f4834:8", "const:4:8"]]
- 007f4834 ["CALL", null, ["callee:008b7a20:8"]]
+ 007f488c ["INT_ADD", "register:40f0:8", ["const:7f488c:8", "const:4:8"]]
+ 007f488c ["CALL", null, ["callee:008b7a20:8"]]
- 007f4834 bytes 650c0394
+ 007f488c bytes 650c0394
- 007f4840 ["INT_ADD", "register:40f0:8", ["const:7f4840:8", "const:4:8"]]
- 007f4840 ["CALL", null, ["callee:008b92e8:8"]]
+ 007f4898 ["INT_ADD", "register:40f0:8", ["const:7f4898:8", "const:4:8"]]
+ 007f4898 ["CALL", null, ["callee:008b92e8:8"]]
- 007f4840 bytes 94120394
+ 007f4898 bytes 94120394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed3d41ed382c25e8fecb39ccdf2a2f22"></a>

### [`007f7338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7338.md) → [`007f7390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f7390.md) FUN_007f7390

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`008b6d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6d9c.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)
- 新版 呼出元 0件  · 呼出先 2件 [`008b6df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6df4.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f7350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7338.md#insn-007f7350)
- 新版 `007f73a8`（命令位置の公開資料なし）

~~~diff
- 007f7350 ["INT_ADD", "register:40f0:8", ["const:7f7350:8", "const:4:8"]]
- 007f7350 ["CALL", null, ["callee:008b7a20:8"]]
+ 007f73a8 ["INT_ADD", "register:40f0:8", ["const:7f73a8:8", "const:4:8"]]
+ 007f73a8 ["CALL", null, ["callee:008b7a20:8"]]
- 007f7350 bytes 9e010394
+ 007f73a8 bytes 9e010394
~~~


<a id="compare-352f4e8e116cb1afb908554a1c46954d"></a>

### [`007f927c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f927c.md) → [`007f92d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f92d4.md) FUN_007f92d4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 7件 [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`006647c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006647c0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9290.md) [`008b9298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9298.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`00664800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664800.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b92e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b92e8.md) [`008b92f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b92f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f92b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f927c.md#insn-007f92b0) · [`007f92c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f927c.md#insn-007f92c0) · [`007f92d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f927c.md#insn-007f92d0)
- 新版 `007f9308`（命令位置の公開資料なし） · `007f9318`（命令位置の公開資料なし） · `007f9328`（命令位置の公開資料なし）

~~~diff
- 007f92b0 ["INT_ADD", "register:40f0:8", ["const:7f92b0:8", "const:4:8"]]
- 007f92b0 ["CALL", null, ["callee:008b92e8:8"]]
+ 007f9308 ["INT_ADD", "register:40f0:8", ["const:7f9308:8", "const:4:8"]]
+ 007f9308 ["CALL", null, ["callee:008b92e8:8"]]
- 007f92b0 bytes f8ff0294
+ 007f9308 bytes f8ff0294
- 007f92c0 ["INT_ADD", "register:40f0:8", ["const:7f92c0:8", "const:4:8"]]
- 007f92c0 ["CALL", null, ["callee:008b92e8:8"]]
+ 007f9318 ["INT_ADD", "register:40f0:8", ["const:7f9318:8", "const:4:8"]]
+ 007f9318 ["CALL", null, ["callee:008b92e8:8"]]
- 007f92c0 bytes f4ff0294
+ 007f9318 bytes f4ff0294
- 007f92d0 ["INT_ADD", "register:40f0:8", ["const:7f92d0:8", "const:4:8"]]
- 007f92d0 ["CALL", null, ["callee:008b92f0:8"]]
+ 007f9328 ["INT_ADD", "register:40f0:8", ["const:7f9328:8", "const:4:8"]]
+ 007f9328 ["CALL", null, ["callee:008b92f0:8"]]
- 007f92d0 bytes f2ff0294
+ 007f9328 bytes f2ff0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcc9c1e66686ddd347244be4a0cffab3"></a>

### [`007f95e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f95e0.md) → [`007f9638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f9638.md) FUN_007f9638

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`009e2464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2464.md) [`009e39f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e39f8.md) [`009e3a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e3a80.md) [`009e5538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e5/009e5538.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md)
- 新版 呼出元 0件  · 呼出先 5件 [`009e24b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e2/009e24b8.md) [`009e3a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e3/009e3a4c.md) [`009e3ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e3/009e3ad4.md) [`009e558c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e5/009e558c.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f960c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f95e0.md#insn-007f960c) · [`007f961c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f95e0.md#insn-007f961c) · [`007f962c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f95e0.md#insn-007f962c)
- 新版 `007f9664`（命令位置の公開資料なし） · `007f9674`（命令位置の公開資料なし） · `007f9684`（命令位置の公開資料なし）

~~~diff
- 007f960c ["INT_ADD", "register:40f0:8", ["const:7f960c:8", "const:4:8"]]
- 007f960c ["CALL", null, ["callee:009e24b8:8"]]
+ 007f9664 ["INT_ADD", "register:40f0:8", ["const:7f9664:8", "const:4:8"]]
+ 007f9664 ["CALL", null, ["callee:009e24b8:8"]]
- 007f960c bytes 96a30794
+ 007f9664 bytes 95a30794
- 007f961c ["INT_ADD", "register:40f0:8", ["const:7f961c:8", "const:4:8"]]
- 007f961c ["CALL", null, ["callee:009e3ad4:8"]]
+ 007f9674 ["INT_ADD", "register:40f0:8", ["const:7f9674:8", "const:4:8"]]
+ 007f9674 ["CALL", null, ["callee:009e3ad4:8"]]
- 007f961c bytes 19a90794
+ 007f9674 bytes 18a90794
- 007f962c ["INT_ADD", "register:40f0:8", ["const:7f962c:8", "const:4:8"]]
- 007f962c ["CALL", null, ["callee:009e3a4c:8"]]
+ 007f9684 ["INT_ADD", "register:40f0:8", ["const:7f9684:8", "const:4:8"]]
+ 007f9684 ["CALL", null, ["callee:009e3a4c:8"]]
- 007f962c bytes f3a80794
+ 007f9684 bytes f2a80794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c506324f26a5791daa92ecd984fac65f"></a>

### [`007f97c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f97c0.md) → [`007f9818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f9818.md) FUN_007f9818

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f97dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f97c0.md#insn-007f97dc) · [`007f97fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f97c0.md#insn-007f97fc)
- 新版 `007f9834`（命令位置の公開資料なし） · `007f9854`（命令位置の公開資料なし）

~~~diff
- 007f97dc ["INT_ADD", "register:40f0:8", ["const:7f97dc:8", "const:4:8"]]
- 007f97dc ["CALL", null, ["callee:00c53da0:8"]]
+ 007f9834 ["INT_ADD", "register:40f0:8", ["const:7f9834:8", "const:4:8"]]
+ 007f9834 ["CALL", null, ["callee:00c53da0:8"]]
- 007f97dc bytes 49691194
+ 007f9834 bytes 5b691194
- 007f97fc ["COPY", "register:0:8", ["register:4040:8"]]
- 007f97fc ["INT_ADD", "register:40f0:8", ["const:7f97fc:8", "const:4:8"]]
- 007f97fc ["CALLIND", null, ["register:0:8"]]
+ 007f9854 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007f9854 ["INT_ADD", "register:40f0:8", ["const:7f9854:8", "const:4:8"]]
+ 007f9854 ["CALLIND", null, ["register:0:8"]]
- 007f97fc bytes 00013fd6
+ 007f9854 bytes 00013fd6
~~~


<a id="compare-c7cfc6030903058421149784921e2b1d"></a>

### [`007f9810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9810.md) → [`007f9868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f9868.md) FUN_007f9868

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f9830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9810.md#insn-007f9830) · [`007f9844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9810.md#insn-007f9844) · [`007f984c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9810.md#insn-007f984c)
- 新版 `007f9888`（命令位置の公開資料なし） · `007f989c`（命令位置の公開資料なし） · `007f98a4`（命令位置の公開資料なし）

~~~diff
- 007f9830 ["INT_ADD", "register:40f0:8", ["const:7f9830:8", "const:4:8"]]
- 007f9830 ["CALL", null, ["callee:00c53da0:8"]]
+ 007f9888 ["INT_ADD", "register:40f0:8", ["const:7f9888:8", "const:4:8"]]
+ 007f9888 ["CALL", null, ["callee:00c53da0:8"]]
- 007f9830 bytes 34691194
+ 007f9888 bytes 46691194
- 007f9844 ["COPY", "register:0:8", ["register:4040:8"]]
- 007f9844 ["INT_ADD", "register:40f0:8", ["const:7f9844:8", "const:4:8"]]
- 007f9844 ["CALLIND", null, ["register:0:8"]]
+ 007f989c ["COPY", "register:0:8", ["register:4040:8"]]
+ 007f989c ["INT_ADD", "register:40f0:8", ["const:7f989c:8", "const:4:8"]]
+ 007f989c ["CALLIND", null, ["register:0:8"]]
- 007f9844 bytes 00013fd6
+ 007f989c bytes 00013fd6
- 007f984c ["INT_ADD", "register:40f0:8", ["const:7f984c:8", "const:4:8"]]
- 007f984c ["CALL", null, ["callee:00c57f50:8"]]
+ 007f98a4 ["INT_ADD", "register:40f0:8", ["const:7f98a4:8", "const:4:8"]]
+ 007f98a4 ["CALL", null, ["callee:00c57f50:8"]]
- 007f984c bytes 8d791194
+ 007f98a4 bytes ab791194
~~~


<a id="compare-3d55467ce6a54fbd0cf6cf63d27b601a"></a>

### [`007f9860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9860.md) → [`007f98b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f98b8.md) FUN_007f98b8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`007f9bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9bd0.md) [`007f9e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9e84.md) [`009dfa9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009dfa9c.md) [`009e2b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2b40.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`007f9c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f9c28.md) [`007f9edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f9edc.md) [`009dfaf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009dfaf0.md) [`009e2b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e2/009e2b94.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f98a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9860.md#insn-007f98a8) · [`007f98c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9860.md#insn-007f98c0) · [`007f9930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9860.md#insn-007f9930)
- 新版 `007f9900`（命令位置の公開資料なし） · `007f9918`（命令位置の公開資料なし） · `007f9988`（命令位置の公開資料なし）

~~~diff
- 007f98a8 ["INT_ADD", "register:40f0:8", ["const:7f98a8:8", "const:4:8"]]
- 007f98a8 ["CALL", null, ["callee:009e3a70:8"]]
+ 007f9900 ["INT_ADD", "register:40f0:8", ["const:7f9900:8", "const:4:8"]]
+ 007f9900 ["CALL", null, ["callee:009e3a70:8"]]
- 007f98a8 bytes 5da80794
+ 007f9900 bytes 5ca80794
- 007f98c0 ["INT_ADD", "register:40f0:8", ["const:7f98c0:8", "const:4:8"]]
- 007f98c0 ["CALL", null, ["callee:009e2fe8:8"]]
+ 007f9918 ["INT_ADD", "register:40f0:8", ["const:7f9918:8", "const:4:8"]]
+ 007f9918 ["CALL", null, ["callee:009e2fe8:8"]]
- 007f98c0 bytes b5a50794
+ 007f9918 bytes b4a50794
- 007f9930 ["COPY", "register:0:8", ["register:4040:8"]]
- 007f9930 ["INT_ADD", "register:40f0:8", ["const:7f9930:8", "const:4:8"]]
- 007f9930 ["CALLIND", null, ["register:0:8"]]
+ 007f9988 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007f9988 ["INT_ADD", "register:40f0:8", ["const:7f9988:8", "const:4:8"]]
+ 007f9988 ["CALLIND", null, ["register:0:8"]]
- 007f9930 bytes 00013fd6
+ 007f9988 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8ca32c4b419edfaee6344c7aebdab7c"></a>

### [`007f9bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9bd0.md) → [`007f9c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f9c28.md) FUN_007f9c28

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007f9860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9860.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`007f9e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9e84.md) [`007f9e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9e98.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`007f98b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f98b8.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`007f9edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f9edc.md) [`007f9ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f9ef0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f9ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9bd0.md#insn-007f9ccc) · [`007f9d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9bd0.md#insn-007f9d1c) · [`007f9d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9bd0.md#insn-007f9d30)
- 新版 `007f9d24`（命令位置の公開資料なし） · `007f9d74`（命令位置の公開資料なし） · `007f9d88`（命令位置の公開資料なし）

~~~diff
- 007f9ccc ["INT_ADD", "register:40f0:8", ["const:7f9ccc:8", "const:4:8"]]
- 007f9ccc ["CALL", null, ["callee:00c57f60:8"]]
+ 007f9d24 ["INT_ADD", "register:40f0:8", ["const:7f9d24:8", "const:4:8"]]
+ 007f9d24 ["CALL", null, ["callee:00c57f60:8"]]
- 007f9ccc bytes 71781194
+ 007f9d24 bytes 8f781194
- 007f9d1c ["INT_ADD", "register:40f0:8", ["const:7f9d1c:8", "const:4:8"]]
- 007f9d1c ["CALL", null, ["callee:007f9ef0:8"]]
+ 007f9d74 ["INT_ADD", "register:40f0:8", ["const:7f9d74:8", "const:4:8"]]
+ 007f9d74 ["CALL", null, ["callee:007f9ef0:8"]]
- 007f9d1c bytes 5f000094
+ 007f9d74 bytes 5f000094
- 007f9d30 ["INT_ADD", "register:40f0:8", ["const:7f9d30:8", "const:4:8"]]
- 007f9d30 ["CALL", null, ["callee:00c580d0:8"]]
+ 007f9d88 ["INT_ADD", "register:40f0:8", ["const:7f9d88:8", "const:4:8"]]
+ 007f9d88 ["CALL", null, ["callee:00c580d0:8"]]
- 007f9d30 bytes b4781194
+ 007f9d88 bytes d2781194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-777773b3e4e7fff7a286a5874421b359"></a>

### [`007f9e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9e98.md) → [`007f9ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f9ef0.md) FUN_007f9ef0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007f9bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9bd0.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`007f9c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f9/007f9c28.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f9f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9e98.md#insn-007f9f1c) · [`007f9f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9e98.md#insn-007f9f80) · [`007f9fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9e98.md#insn-007f9fcc)
- 新版 `007f9f74`（命令位置の公開資料なし） · `007f9fd8`（命令位置の公開資料なし） · `007fa024`（命令位置の公開資料なし）

~~~diff
- 007f9f1c ["INT_ADD", "register:40f0:8", ["const:7f9f1c:8", "const:4:8"]]
- 007f9f1c ["CALL", null, ["callee:00c58010:8"]]
+ 007f9f74 ["INT_ADD", "register:40f0:8", ["const:7f9f74:8", "const:4:8"]]
+ 007f9f74 ["CALL", null, ["callee:00c58010:8"]]
- 007f9f1c bytes 09781194
+ 007f9f74 bytes 27781194
- 007f9f80 ["INT_ADD", "register:40f0:8", ["const:7f9f80:8", "const:4:8"]]
- 007f9f80 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f9fd8 ["INT_ADD", "register:40f0:8", ["const:7f9fd8:8", "const:4:8"]]
+ 007f9fd8 ["CALL", null, ["callee:00c57f60:8"]]
- 007f9f80 bytes c4771194
+ 007f9fd8 bytes e2771194
- 007f9fcc ["INT_ADD", "register:40f0:8", ["const:7f9fcc:8", "const:4:8"]]
- 007f9fcc ["CALL", null, ["callee:00c57f80:8"]]
+ 007fa024 ["INT_ADD", "register:40f0:8", ["const:7fa024:8", "const:4:8"]]
+ 007fa024 ["CALL", null, ["callee:00c57f80:8"]]
- 007f9fcc bytes b9771194
+ 007fa024 bytes d7771194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0885f292aaf92ad6c4ec9bc168e1443"></a>

### [`007fd18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd18c.md) → [`007fd1e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd1e4.md) FUN_007fd1e4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`008b9290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9290.md) [`008b9298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9298.md) [`00a83588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a83/00a83588.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`008b92e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b92e8.md) [`008b92f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b92f0.md) [`00a835f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a83/00a835f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007fd1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd18c.md#insn-007fd1c0) · [`007fd1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd18c.md#insn-007fd1d0) · [`007fd200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd18c.md#insn-007fd200)
- 新版 `007fd218`（命令位置の公開資料なし） · `007fd228`（命令位置の公開資料なし） · `007fd258`（命令位置の公開資料なし）

~~~diff
- 007fd1c0 ["INT_ADD", "register:40f0:8", ["const:7fd1c0:8", "const:4:8"]]
- 007fd1c0 ["CALL", null, ["callee:008b92e8:8"]]
+ 007fd218 ["INT_ADD", "register:40f0:8", ["const:7fd218:8", "const:4:8"]]
+ 007fd218 ["CALL", null, ["callee:008b92e8:8"]]
- 007fd1c0 bytes 34f00294
+ 007fd218 bytes 34f00294
- 007fd1d0 ["INT_ADD", "register:40f0:8", ["const:7fd1d0:8", "const:4:8"]]
- 007fd1d0 ["CALL", null, ["callee:008b92e8:8"]]
+ 007fd228 ["INT_ADD", "register:40f0:8", ["const:7fd228:8", "const:4:8"]]
+ 007fd228 ["CALL", null, ["callee:008b92e8:8"]]
- 007fd1d0 bytes 30f00294
+ 007fd228 bytes 30f00294
- 007fd200 ["INT_ADD", "register:40f0:8", ["const:7fd200:8", "const:4:8"]]
- 007fd200 ["CALL", null, ["callee:008b92f0:8"]]
+ 007fd258 ["INT_ADD", "register:40f0:8", ["const:7fd258:8", "const:4:8"]]
+ 007fd258 ["CALL", null, ["callee:008b92f0:8"]]
- 007fd200 bytes 26f00294
+ 007fd258 bytes 26f00294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f94a3d20ba96795ee5f82064df24dbd6"></a>

### [`007fe7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe7ac.md) → [`007fe804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fe/007fe804.md) FUN_007fe804

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007cb5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb5e0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`007cb638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cb/007cb638.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007fe7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe7ac.md#insn-007fe7cc)
- 新版 `007fe824`（命令位置の公開資料なし）

~~~diff
- 007fe7cc ["INT_ADD", "register:40f0:8", ["const:7fe7cc:8", "const:4:8"]]
- 007fe7cc ["CALL", null, ["callee:00c57f80:8"]]
+ 007fe824 ["INT_ADD", "register:40f0:8", ["const:7fe824:8", "const:4:8"]]
+ 007fe824 ["CALL", null, ["callee:00c57f80:8"]]
- 007fe7cc bytes b9651194
+ 007fe824 bytes d7651194
~~~


<a id="compare-13ea1cb23846ddc663843dfeede87dc5"></a>

### [`007ff194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff194.md) → [`007ff1ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ff/007ff1ec.md) FUN_007ff1ec

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007c911c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c9/007c911c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`007c9174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007c9/007c9174.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007ff1b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff194.md#insn-007ff1b4)
- 新版 `007ff20c`（命令位置の公開資料なし）

~~~diff
- 007ff1b4 ["INT_ADD", "register:40f0:8", ["const:7ff1b4:8", "const:4:8"]]
- 007ff1b4 ["CALL", null, ["callee:00c57f80:8"]]
+ 007ff20c ["INT_ADD", "register:40f0:8", ["const:7ff20c:8", "const:4:8"]]
+ 007ff20c ["CALL", null, ["callee:00c57f80:8"]]
- 007ff1b4 bytes 3f631194
+ 007ff20c bytes 5d631194
~~~


<a id="compare-a9bf2c5f6c8c44998d134ee8a210a644"></a>

### [`007ffb48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffb48.md) → [`007ffba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ff/007ffba0.md) FUN_007ffba0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007caac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007caac8.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`007cab20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ca/007cab20.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007ffb68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffb48.md#insn-007ffb68)
- 新版 `007ffbc0`（命令位置の公開資料なし）

~~~diff
- 007ffb68 ["INT_ADD", "register:40f0:8", ["const:7ffb68:8", "const:4:8"]]
- 007ffb68 ["CALL", null, ["callee:00c57f80:8"]]
+ 007ffbc0 ["INT_ADD", "register:40f0:8", ["const:7ffbc0:8", "const:4:8"]]
+ 007ffbc0 ["CALL", null, ["callee:00c57f80:8"]]
- 007ffb68 bytes d2601194
+ 007ffbc0 bytes f0601194
~~~


<a id="compare-babb11197b6450985a6aa032cf65b13e"></a>

### [`00801c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00801/00801c90.md) → [`00801ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00801/00801ce8.md) FUN_00801ce8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) [`0078614c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/0078614c.md) [`0081de80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081d/0081de80.md) [`0082467c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00824/0082467c.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 8件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`007738ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) [`007861a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00786/007861a4.md) [`0081ded8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081d/0081ded8.md) [`008246d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00824/008246d4.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00801d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00801/00801c90.md#insn-00801d28) · [`00801d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00801/00801c90.md#insn-00801d5c)
- 新版 `00801d80`（命令位置の公開資料なし） · `00801db4`（命令位置の公開資料なし）

~~~diff
- 00801d28 ["INT_ADD", "register:40f0:8", ["const:801d28:8", "const:4:8"]]
- 00801d28 ["CALL", null, ["callee:00c57f60:8"]]
+ 00801d80 ["INT_ADD", "register:40f0:8", ["const:801d80:8", "const:4:8"]]
+ 00801d80 ["CALL", null, ["callee:00c57f60:8"]]
- 00801d28 bytes 5a581194
+ 00801d80 bytes 78581194
- 00801d5c ["INT_ADD", "register:40f0:8", ["const:801d5c:8", "const:4:8"]]
- 00801d5c ["CALL", null, ["callee:0043bbe4:8"]]
+ 00801db4 ["INT_ADD", "register:40f0:8", ["const:801db4:8", "const:4:8"]]
+ 00801db4 ["CALL", null, ["callee:0043bbe4:8"]]
- 00801d5c bytes 92e7f097
+ 00801db4 bytes 8ce7f097
~~~


<a id="compare-9a9ddcc822dece5a0ee1eec6eb72250c"></a>

### [`00801de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00801/00801de0.md) → [`00801e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00801/00801e38.md) FUN_00801e38

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0081de80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081d/0081de80.md) [`0082467c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00824/0082467c.md) [`00a9c6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9c/00a9c6f0.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 3件 [`0081ded8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081d/0081ded8.md) [`008246d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00824/008246d4.md) [`00a9c760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a9c/00a9c760.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00801e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00801/00801de0.md#insn-00801e44) · [`00801e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00801/00801de0.md#insn-00801e80)
- 新版 `00801e9c`（命令位置の公開資料なし） · `00801ed8`（命令位置の公開資料なし）

~~~diff
- 00801e44 ["INT_ADD", "register:40f0:8", ["const:801e44:8", "const:4:8"]]
- 00801e44 ["CALL", null, ["callee:00c57f60:8"]]
+ 00801e9c ["INT_ADD", "register:40f0:8", ["const:801e9c:8", "const:4:8"]]
+ 00801e9c ["CALL", null, ["callee:00c57f60:8"]]
- 00801e44 bytes 13581194
+ 00801e9c bytes 31581194
- 00801e80 ["INT_ADD", "register:40f0:8", ["const:801e80:8", "const:4:8"]]
- 00801e80 ["CALL", null, ["callee:0043bbe4:8"]]
+ 00801ed8 ["INT_ADD", "register:40f0:8", ["const:801ed8:8", "const:4:8"]]
+ 00801ed8 ["CALL", null, ["callee:0043bbe4:8"]]
- 00801e80 bytes 49e7f097
+ 00801ed8 bytes 43e7f097
~~~


<a id="compare-bd257baca44f93f8e043c3e2dd2ed2db"></a>

### [`00802310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802310.md) → [`00802368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802368.md) FUN_00802368

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 1件 [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)
- 新版 呼出元 1件 [`00a47f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47f54.md) · 呼出先 1件 [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00802330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802310.md#insn-00802330)
- 新版 `00802388`（命令位置の公開資料なし）

~~~diff
- 00802330 ["INT_ADD", "register:40f0:8", ["const:802330:8", "const:4:8"]]
- 00802330 ["CALL", null, ["callee:00c58520:8"]]
+ 00802388 ["INT_ADD", "register:40f0:8", ["const:802388:8", "const:4:8"]]
+ 00802388 ["CALL", null, ["callee:00c58520:8"]]
- 00802330 bytes 48581194
+ 00802388 bytes 66581194
~~~


<a id="compare-4ef3190b309f52b320c46b808f9cb193"></a>

### [`0080238c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/0080238c.md) → [`008023e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/008023e4.md) FUN_008023e4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) [`00789de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789de0.md) [`00824330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00824/00824330.md) [`008244dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00824/008244dc.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 6件 [`007738ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) [`00789e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00789/00789e38.md) [`00824388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00824/00824388.md) [`00824534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00824/00824534.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080243c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/0080238c.md#insn-0080243c) · [`00802470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/0080238c.md#insn-00802470)
- 新版 `00802494`（命令位置の公開資料なし） · `008024c8`（命令位置の公開資料なし）

~~~diff
- 0080243c ["INT_ADD", "register:40f0:8", ["const:80243c:8", "const:4:8"]]
- 0080243c ["CALL", null, ["callee:00c57f60:8"]]
+ 00802494 ["INT_ADD", "register:40f0:8", ["const:802494:8", "const:4:8"]]
+ 00802494 ["CALL", null, ["callee:00c57f60:8"]]
- 0080243c bytes 95561194
+ 00802494 bytes b3561194
- 00802470 ["INT_ADD", "register:40f0:8", ["const:802470:8", "const:4:8"]]
- 00802470 ["CALL", null, ["callee:0043bbe4:8"]]
+ 008024c8 ["INT_ADD", "register:40f0:8", ["const:8024c8:8", "const:4:8"]]
+ 008024c8 ["CALL", null, ["callee:0043bbe4:8"]]
- 00802470 bytes cde5f097
+ 008024c8 bytes c7e5f097
~~~


<a id="compare-84d23ff97aa3488bf31e34a6e0cdfd9b"></a>

### [`008024ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008024ac.md) → [`00802504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802504.md) FUN_00802504

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0060e0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060e/0060e0c4.md) [`0069a504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069a/0069a504.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) [`00ab04fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab0/00ab04fc.md) · 呼出先 1件 [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)
- 新版 呼出元 5件 [`0060e104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0060e/0060e104.md) [`0069a55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069a/0069a55c.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) [`00ab056c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ab0/00ab056c.md) · 呼出先 1件 [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008024cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008024ac.md#insn-008024cc)
- 新版 `00802524`（命令位置の公開資料なし）

~~~diff
- 008024cc ["INT_ADD", "register:40f0:8", ["const:8024cc:8", "const:4:8"]]
- 008024cc ["CALL", null, ["callee:00c58520:8"]]
+ 00802524 ["INT_ADD", "register:40f0:8", ["const:802524:8", "const:4:8"]]
+ 00802524 ["CALL", null, ["callee:00c58520:8"]]
- 008024cc bytes e1571194
+ 00802524 bytes ff571194
~~~


<a id="compare-8730b245e0927249322b152523380969"></a>

### [`008024f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008024f0.md) → [`00802548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802548.md) FUN_00802548

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) · 呼出先 1件 [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)
- 新版 呼出元 1件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) · 呼出先 1件 [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00802510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008024f0.md#insn-00802510)
- 新版 `00802568`（命令位置の公開資料なし）

~~~diff
- 00802510 ["INT_ADD", "register:40f0:8", ["const:802510:8", "const:4:8"]]
- 00802510 ["CALL", null, ["callee:00c58520:8"]]
+ 00802568 ["INT_ADD", "register:40f0:8", ["const:802568:8", "const:4:8"]]
+ 00802568 ["CALL", null, ["callee:00c58520:8"]]
- 00802510 bytes d0571194
+ 00802568 bytes ee571194
~~~


<a id="compare-787969c762eba313ce63de5d3230e81a"></a>

### [`00802534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802534.md) → [`0080258c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/0080258c.md) FUN_0080258c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b00054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b00054.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00b000f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b00/00b000f0.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008025cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802534.md#insn-008025cc) · [`00802600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802534.md#insn-00802600)
- 新版 `00802624`（命令位置の公開資料なし） · `00802658`（命令位置の公開資料なし）

~~~diff
- 008025cc ["INT_ADD", "register:40f0:8", ["const:8025cc:8", "const:4:8"]]
- 008025cc ["CALL", null, ["callee:00c57f60:8"]]
+ 00802624 ["INT_ADD", "register:40f0:8", ["const:802624:8", "const:4:8"]]
+ 00802624 ["CALL", null, ["callee:00c57f60:8"]]
- 008025cc bytes 31561194
+ 00802624 bytes 4f561194
- 00802600 ["INT_ADD", "register:40f0:8", ["const:802600:8", "const:4:8"]]
- 00802600 ["CALL", null, ["callee:0043bbe4:8"]]
+ 00802658 ["INT_ADD", "register:40f0:8", ["const:802658:8", "const:4:8"]]
+ 00802658 ["CALL", null, ["callee:0043bbe4:8"]]
- 00802600 bytes 69e5f097
+ 00802658 bytes 63e5f097
~~~


<a id="compare-8b002b5e00ab31488adf9e3cecf7cfdf"></a>

### [`00802630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802630.md) → [`00802688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802688.md) FUN_00802688

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`00615910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615910.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) [`007859bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/007859bc.md) [`00787518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/00787518.md) · 呼出先 1件 [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)
- 新版 呼出元 9件 [`00615950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00615/00615950.md) [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`007738ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) [`00785a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00785/00785a14.md) [`00787570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787570.md) · 呼出先 1件 [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00802650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802630.md#insn-00802650)
- 新版 `008026a8`（命令位置の公開資料なし）

~~~diff
- 00802650 ["INT_ADD", "register:40f0:8", ["const:802650:8", "const:4:8"]]
- 00802650 ["CALL", null, ["callee:00c58520:8"]]
+ 008026a8 ["INT_ADD", "register:40f0:8", ["const:8026a8:8", "const:4:8"]]
+ 008026a8 ["CALL", null, ["callee:00c58520:8"]]
- 00802650 bytes 80571194
+ 008026a8 bytes 9e571194
~~~


<a id="compare-29b88a899dfd60be26f23b132ae81e37"></a>

### [`00802674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802674.md) → [`008026cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/008026cc.md) FUN_008026cc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00a65dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a65/00a65dec.md) [`00a664b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a66/00a664b4.md) [`00a66c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a66/00a66c98.md) [`00a670bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a670bc.md) [`00a67530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a67530.md) · 呼出先 1件 [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)
- 新版 呼出元 6件 [`00a65e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a65/00a65e5c.md) [`00a66524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a66/00a66524.md) [`00a66d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a66/00a66d08.md) [`00a6712c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a67/00a6712c.md) [`00a675a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a67/00a675a0.md) · 呼出先 1件 [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00802694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802674.md#insn-00802694)
- 新版 `008026ec`（命令位置の公開資料なし）

~~~diff
- 00802694 ["INT_ADD", "register:40f0:8", ["const:802694:8", "const:4:8"]]
- 00802694 ["CALL", null, ["callee:00c58520:8"]]
+ 008026ec ["INT_ADD", "register:40f0:8", ["const:8026ec:8", "const:4:8"]]
+ 008026ec ["CALL", null, ["callee:00c58520:8"]]
- 00802694 bytes 6f571194
+ 008026ec bytes 8d571194
~~~


<a id="compare-21fe7e7512330211add473a9f89f6f24"></a>

### [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) → [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md) FUN_00802bb0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 87件 [`005b06cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b06cc.md) [`005e2e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e2/005e2e40.md) [`005e6dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e6/005e6dfc.md) [`005e7504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7504.md) [`005e7f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7f3c.md) · 呼出先 3件 [`008001ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001ec.md) [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`00802b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b8c.md)
- 新版 呼出元 87件 [`005b070c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b0/005b070c.md) [`005e2e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e2/005e2e80.md) [`005e6e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e6/005e6e3c.md) [`005e7544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7544.md) [`005e7f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7f7c.md) · 呼出先 3件 [`00800244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800244.md) [`00802710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802710.md) [`00802be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802be4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00802b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md#insn-00802b68) · [`00802b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md#insn-00802b74)
- 新版 `00802bc0`（命令位置の公開資料なし） · `00802bcc`（命令位置の公開資料なし）

~~~diff
- 00802b68 ["INT_ADD", "register:40f0:8", ["const:802b68:8", "const:4:8"]]
- 00802b68 ["CALL", null, ["callee:00802710:8"]]
+ 00802bc0 ["INT_ADD", "register:40f0:8", ["const:802bc0:8", "const:4:8"]]
+ 00802bc0 ["CALL", null, ["callee:00802710:8"]]
- 00802b68 bytes d4feff97
+ 00802bc0 bytes d4feff97
- 00802b74 ["INT_ADD", "register:40f0:8", ["const:802b74:8", "const:4:8"]]
- 00802b74 ["CALL", null, ["callee:00802be4:8"]]
+ 00802bcc ["INT_ADD", "register:40f0:8", ["const:802bcc:8", "const:4:8"]]
+ 00802bcc ["CALL", null, ["callee:00802be4:8"]]
- 00802b74 bytes 06000094
+ 00802bcc bytes 06000094
~~~


<a id="compare-8474bb7964c05964bcf523581a1dc566"></a>

### [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) → [`00802d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802d00.md) FUN_00802d00

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 54件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00604fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00604/00604fec.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`00611e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00611/00611e60.md) · 呼出先 2件 [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 54件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`0060502c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00605/0060502c.md) [`00605294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00605/00605294.md) [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`00611ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00611/00611ea0.md) · 呼出先 2件 [`00802710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802710.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00802cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md#insn-00802cb8) · [`00802cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md#insn-00802cc0)
- 新版 `00802d10`（命令位置の公開資料なし） · `00802d18`（命令位置の公開資料なし）

~~~diff
- 00802cb8 ["INT_ADD", "register:40f0:8", ["const:802cb8:8", "const:4:8"]]
- 00802cb8 ["CALL", null, ["callee:00802710:8"]]
+ 00802d10 ["INT_ADD", "register:40f0:8", ["const:802d10:8", "const:4:8"]]
+ 00802d10 ["CALL", null, ["callee:00802710:8"]]
- 00802cb8 bytes 80feff97
+ 00802d10 bytes 80feff97
- 00802cc0 ["INT_ADD", "register:40f0:8", ["const:802cc0:8", "const:4:8"]]
- 00802cc0 ["CALL", null, ["callee:00851550:8"]]
+ 00802d18 ["INT_ADD", "register:40f0:8", ["const:802d18:8", "const:4:8"]]
+ 00802d18 ["CALL", null, ["callee:00851550:8"]]
- 00802cc0 bytes 0e3a0194
+ 00802d18 bytes 0e3a0194
~~~


<a id="compare-17775b5504d39f6b349bffc50025e623"></a>

### [`00802cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802cec.md) → [`00802d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802d44.md) FUN_00802d44

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00802d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d4c.md) [`00a0672c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a0672c.md) · 呼出先 5件 [`0067674c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/0067674c.md) [`007bbd48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbd48.md) [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00a32a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32a04.md)
- 新版 呼出元 3件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`00802da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802da4.md) [`00a06780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06780.md) · 呼出先 5件 [`0067678c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/0067678c.md) [`007bbda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bb/007bbda0.md) [`00802710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802710.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00a32a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a32/00a32a58.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00802cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802cec.md#insn-00802cf4) · [`00802d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802cec.md#insn-00802d04) · [`00802d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802cec.md#insn-00802d0c)
- 新版 `00802d4c`（命令位置の公開資料なし） · `00802d5c`（命令位置の公開資料なし） · `00802d64`（命令位置の公開資料なし）

~~~diff
- 00802cf4 ["INT_ADD", "register:40f0:8", ["const:802cf4:8", "const:4:8"]]
- 00802cf4 ["CALL", null, ["callee:00851550:8"]]
+ 00802d4c ["INT_ADD", "register:40f0:8", ["const:802d4c:8", "const:4:8"]]
+ 00802d4c ["CALL", null, ["callee:00851550:8"]]
- 00802cf4 bytes 013a0194
+ 00802d4c bytes 013a0194
- 00802d04 ["INT_ADD", "register:40f0:8", ["const:802d04:8", "const:4:8"]]
- 00802d04 ["CALL", null, ["callee:0067678c:8"]]
+ 00802d5c ["INT_ADD", "register:40f0:8", ["const:802d5c:8", "const:4:8"]]
+ 00802d5c ["CALL", null, ["callee:0067678c:8"]]
- 00802d04 bytes 92cef997
+ 00802d5c bytes 8ccef997
- 00802d0c ["INT_ADD", "register:40f0:8", ["const:802d0c:8", "const:4:8"]]
- 00802d0c ["CALL", null, ["callee:00851550:8"]]
+ 00802d64 ["INT_ADD", "register:40f0:8", ["const:802d64:8", "const:4:8"]]
+ 00802d64 ["CALL", null, ["callee:00851550:8"]]
- 00802d0c bytes fb390194
+ 00802d64 bytes fb390194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0f29a9fccba60585a7f46bac85bb702"></a>

### [`00802d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d4c.md) → [`00802da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802da4.md) FUN_00802da4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a0672c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a0672c.md) · 呼出先 3件 [`008001ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001ec.md) [`00802cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802cec.md) [`00802d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d78.md)
- 新版 呼出元 1件 [`00a06780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06780.md) · 呼出先 3件 [`00800244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800244.md) [`00802d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802d44.md) [`00802dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802dd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00802d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d4c.md#insn-00802d58) · [`00802d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d4c.md#insn-00802d60)
- 新版 `00802db0`（命令位置の公開資料なし） · `00802db8`（命令位置の公開資料なし）

~~~diff
- 00802d58 ["INT_ADD", "register:40f0:8", ["const:802d58:8", "const:4:8"]]
- 00802d58 ["CALL", null, ["callee:00802d44:8"]]
+ 00802db0 ["INT_ADD", "register:40f0:8", ["const:802db0:8", "const:4:8"]]
+ 00802db0 ["CALL", null, ["callee:00802d44:8"]]
- 00802d58 bytes e5ffff97
+ 00802db0 bytes e5ffff97
- 00802d60 ["INT_ADD", "register:40f0:8", ["const:802d60:8", "const:4:8"]]
- 00802d60 ["CALL", null, ["callee:00802dd0:8"]]
+ 00802db8 ["INT_ADD", "register:40f0:8", ["const:802db8:8", "const:4:8"]]
+ 00802db8 ["CALL", null, ["callee:00802dd0:8"]]
- 00802d60 bytes 06000094
+ 00802db8 bytes 06000094
~~~


<a id="compare-75af2b1c3dd037a19195e4dca4145995"></a>

### [`00802d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d78.md) → [`00802dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802dd0.md) FUN_00802dd0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00802d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d4c.md) [`00a0672c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a0672c.md) · 呼出先 8件 [`0067674c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/0067674c.md) [`007bbd48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbd48.md) [`008001ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001ec.md) [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`00802b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b8c.md)
- 新版 呼出元 3件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`00802da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802da4.md) [`00a06780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06780.md) · 呼出先 8件 [`0067678c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/0067678c.md) [`007bbda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bb/007bbda0.md) [`00800244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800244.md) [`00802710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802710.md) [`00802be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802be4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00802d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d78.md#insn-00802d84) · [`00802d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d78.md#insn-00802d94) · [`00802da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d78.md#insn-00802da4)
- 新版 `00802ddc`（命令位置の公開資料なし） · `00802dec`（命令位置の公開資料なし） · `00802dfc`（命令位置の公開資料なし）

~~~diff
- 00802d84 ["INT_ADD", "register:40f0:8", ["const:802d84:8", "const:4:8"]]
- 00802d84 ["CALL", null, ["callee:00851550:8"]]
+ 00802ddc ["INT_ADD", "register:40f0:8", ["const:802ddc:8", "const:4:8"]]
+ 00802ddc ["CALL", null, ["callee:00851550:8"]]
- 00802d84 bytes dd390194
+ 00802ddc bytes dd390194
- 00802d94 ["INT_ADD", "register:40f0:8", ["const:802d94:8", "const:4:8"]]
- 00802d94 ["CALL", null, ["callee:0067678c:8"]]
+ 00802dec ["INT_ADD", "register:40f0:8", ["const:802dec:8", "const:4:8"]]
+ 00802dec ["CALL", null, ["callee:0067678c:8"]]
- 00802d94 bytes 6ecef997
+ 00802dec bytes 68cef997
- 00802da4 ["INT_ADD", "register:40f0:8", ["const:802da4:8", "const:4:8"]]
- 00802da4 ["CALL", null, ["callee:00851550:8"]]
+ 00802dfc ["INT_ADD", "register:40f0:8", ["const:802dfc:8", "const:4:8"]]
+ 00802dfc ["CALL", null, ["callee:00851550:8"]]
- 00802da4 bytes d5390194
+ 00802dfc bytes d5390194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd2839866f63315e1e1291883b3397b6"></a>

### [`00802e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802e6c.md) → [`00802ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802ec4.md) FUN_00802ec4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00a0672c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a0672c.md) · 呼出先 4件 [`0067674c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/0067674c.md) [`007bbd48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbd48.md) [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`00a06780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06780.md) · 呼出先 4件 [`0067678c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/0067678c.md) [`007bbda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bb/007bbda0.md) [`00802710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802710.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00802e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802e6c.md#insn-00802e78) · [`00802e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802e6c.md#insn-00802e88) · [`00802e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802e6c.md#insn-00802e90)
- 新版 `00802ed0`（命令位置の公開資料なし） · `00802ee0`（命令位置の公開資料なし） · `00802ee8`（命令位置の公開資料なし）

~~~diff
- 00802e78 ["INT_ADD", "register:40f0:8", ["const:802e78:8", "const:4:8"]]
- 00802e78 ["CALL", null, ["callee:00851550:8"]]
+ 00802ed0 ["INT_ADD", "register:40f0:8", ["const:802ed0:8", "const:4:8"]]
+ 00802ed0 ["CALL", null, ["callee:00851550:8"]]
- 00802e78 bytes a0390194
+ 00802ed0 bytes a0390194
- 00802e88 ["INT_ADD", "register:40f0:8", ["const:802e88:8", "const:4:8"]]
- 00802e88 ["CALL", null, ["callee:0067678c:8"]]
+ 00802ee0 ["INT_ADD", "register:40f0:8", ["const:802ee0:8", "const:4:8"]]
+ 00802ee0 ["CALL", null, ["callee:0067678c:8"]]
- 00802e88 bytes 31cef997
+ 00802ee0 bytes 2bcef997
- 00802e90 ["INT_ADD", "register:40f0:8", ["const:802e90:8", "const:4:8"]]
- 00802e90 ["CALL", null, ["callee:00851550:8"]]
+ 00802ee8 ["INT_ADD", "register:40f0:8", ["const:802ee8:8", "const:4:8"]]
+ 00802ee8 ["CALL", null, ["callee:00851550:8"]]
- 00802e90 bytes 9a390194
+ 00802ee8 bytes 9a390194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffa676426ae114fda9dda4b88758c161"></a>

### [`00803d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00803/00803d0c.md) → [`00803d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00803/00803d64.md) FUN_00803d64

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00803d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00803/00803d0c.md#insn-00803d1c)
- 新版 `00803d74`（命令位置の公開資料なし）

~~~diff
- 00803d1c ["INT_ADD", "register:40f0:8", ["const:803d1c:8", "const:4:8"]]
- 00803d1c ["CALL", null, ["callee:00851550:8"]]
+ 00803d74 ["INT_ADD", "register:40f0:8", ["const:803d74:8", "const:4:8"]]
+ 00803d74 ["CALL", null, ["callee:00851550:8"]]
- 00803d1c bytes f7350194
+ 00803d74 bytes f7350194
~~~


