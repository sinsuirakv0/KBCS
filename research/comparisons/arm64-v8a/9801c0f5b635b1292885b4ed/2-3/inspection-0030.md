# v16.0.1 → v16.0.2 · 要調査の変更候補 (30)

[一覧の目次](README.md)

<a id="compare-af34c20317d39290111a910672388070"></a>

### [`008e5e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e5/008e5e44.md) → [`008e5e98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5e98.md) FUN_008e5e98

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e66ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e6/008e66ac.md) · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`008e6700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e6/008e6700.md) · 呼出先 3件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e5eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e5/008e5e44.md#insn-008e5eec) · [`008e5f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e5/008e5e44.md#insn-008e5f10) · [`008e5f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e5/008e5e44.md#insn-008e5f78)
- 新版 `008e5f40`（命令位置の公開資料なし） · `008e5f64`（命令位置の公開資料なし） · `008e5fcc`（命令位置の公開資料なし）

~~~diff
- 008e5eec ["INT_ADD", "register:40f0:8", ["const:8e5eec:8", "const:4:8"]]
- 008e5eec ["CALL", null, ["callee:0043bb60:8"]]
+ 008e5f40 ["INT_ADD", "register:40f0:8", ["const:8e5f40:8", "const:4:8"]]
+ 008e5f40 ["CALL", null, ["callee:0043bb60:8"]]
- 008e5eec bytes 0d57ed97
+ 008e5f40 bytes 0857ed97
- 008e5f10 ["INT_ADD", "register:40f0:8", ["const:8e5f10:8", "const:4:8"]]
- 008e5f10 ["CALL", null, ["callee:00c57f80:8"]]
+ 008e5f64 ["INT_ADD", "register:40f0:8", ["const:8e5f64:8", "const:4:8"]]
+ 008e5f64 ["CALL", null, ["callee:00c57f80:8"]]
- 008e5f10 bytes e8c70d94
+ 008e5f64 bytes 07c80d94
- 008e5f78 ["INT_ADD", "register:40f0:8", ["const:8e5f78:8", "const:4:8"]]
- 008e5f78 ["CALL", null, ["callee:00c57fb0:8"]]
+ 008e5fcc ["INT_ADD", "register:40f0:8", ["const:8e5fcc:8", "const:4:8"]]
+ 008e5fcc ["CALL", null, ["callee:00c57fb0:8"]]
- 008e5f78 bytes dac70d94
+ 008e5fcc bytes f9c70d94
~~~


<a id="compare-08c56f2a1233e5cc85d11ae6a3272a60"></a>

### [`008e8278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8278.md) → [`008e82cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e82cc.md) FUN_008e82cc

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e82c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8278.md#insn-008e82c0)
- 新版 `008e8314`（命令位置の公開資料なし）

~~~diff
- 008e82c0 ["INT_ADD", "register:40f0:8", ["const:8e82c0:8", "const:4:8"]]
- 008e82c0 ["CALL", null, ["callee:00c57f80:8"]]
+ 008e8314 ["INT_ADD", "register:40f0:8", ["const:8e8314:8", "const:4:8"]]
+ 008e8314 ["CALL", null, ["callee:00c57f80:8"]]
- 008e82c0 bytes fcbe0d94
+ 008e8314 bytes 1bbf0d94
~~~


<a id="compare-0e1d7b12f9d5df260d8152770be406a5"></a>

### [`008e82f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e82f0.md) → [`008e8344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8344.md) FUN_008e8344

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e4590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e4/008e4590.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008e45e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e45e4.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e8338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e82f0.md#insn-008e8338)
- 新版 `008e838c`（命令位置の公開資料なし）

~~~diff
- 008e8338 ["INT_ADD", "register:40f0:8", ["const:8e8338:8", "const:4:8"]]
- 008e8338 ["CALL", null, ["callee:00c57f80:8"]]
+ 008e838c ["INT_ADD", "register:40f0:8", ["const:8e838c:8", "const:4:8"]]
+ 008e838c ["CALL", null, ["callee:00c57f80:8"]]
- 008e8338 bytes debe0d94
+ 008e838c bytes fdbe0d94
~~~


<a id="compare-d277d45530d354e3fe925a15503d3d32"></a>

### [`008e8368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8368.md) → [`008e83bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e83bc.md) FUN_008e83bc

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e4590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e4/008e4590.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`008e84c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e84c4.md) [`008e854c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e854c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`008e45e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e45e4.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`008e8518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8518.md) [`008e85a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e85a0.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e83b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8368.md#insn-008e83b4) · [`008e8434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8368.md#insn-008e8434) · [`008e8484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8368.md#insn-008e8484)
- 新版 `008e8408`（命令位置の公開資料なし） · `008e8488`（命令位置の公開資料なし） · `008e84d8`（命令位置の公開資料なし）

~~~diff
- 008e83b4 ["INT_ADD", "register:40f0:8", ["const:8e83b4:8", "const:4:8"]]
- 008e83b4 ["CALL", null, ["callee:00c57f60:8"]]
+ 008e8408 ["INT_ADD", "register:40f0:8", ["const:8e8408:8", "const:4:8"]]
+ 008e8408 ["CALL", null, ["callee:00c57f60:8"]]
- 008e83b4 bytes b7be0d94
+ 008e8408 bytes d6be0d94
- 008e8434 ["INT_ADD", "register:40f0:8", ["const:8e8434:8", "const:4:8"]]
- 008e8434 ["CALL", null, ["callee:0043bb60:8"]]
+ 008e8488 ["INT_ADD", "register:40f0:8", ["const:8e8488:8", "const:4:8"]]
+ 008e8488 ["CALL", null, ["callee:0043bb60:8"]]
- 008e8434 bytes bb4ded97
+ 008e8488 bytes b64ded97
- 008e8484 ["INT_ADD", "register:40f0:8", ["const:8e8484:8", "const:4:8"]]
- 008e8484 ["CALL", null, ["callee:008e85a0:8"]]
+ 008e84d8 ["INT_ADD", "register:40f0:8", ["const:8e84d8:8", "const:4:8"]]
+ 008e84d8 ["CALL", null, ["callee:008e85a0:8"]]
- 008e8484 bytes 32000094
+ 008e84d8 bytes 32000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dca07a4004d7eb7617b986c5f800626c"></a>

### [`008e84c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e84c4.md) → [`008e8518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8518.md) FUN_008e8518

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e8368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8368.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008e83bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e83bc.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e8528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e84c4.md#insn-008e8528)
- 新版 `008e857c`（命令位置の公開資料なし）

~~~diff
- 008e8528 ["INT_ADD", "register:40f0:8", ["const:8e8528:8", "const:4:8"]]
- 008e8528 ["CALL", null, ["callee:00c57f80:8"]]
+ 008e857c ["INT_ADD", "register:40f0:8", ["const:8e857c:8", "const:4:8"]]
+ 008e857c ["CALL", null, ["callee:00c57f80:8"]]
- 008e8528 bytes 62be0d94
+ 008e857c bytes 81be0d94
~~~


<a id="compare-1295c4c68ec210534178b755cd0ae85f"></a>

### [`008e8560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8560.md) → [`008e85b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e85b4.md) FUN_008e85b4

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e85a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8560.md#insn-008e85a0)
- 新版 `008e85f4`（命令位置の公開資料なし）

~~~diff
- 008e85a0 ["INT_ADD", "register:40f0:8", ["const:8e85a0:8", "const:4:8"]]
- 008e85a0 ["CALL", null, ["callee:00c57f80:8"]]
+ 008e85f4 ["INT_ADD", "register:40f0:8", ["const:8e85f4:8", "const:4:8"]]
+ 008e85f4 ["CALL", null, ["callee:00c57f80:8"]]
- 008e85a0 bytes 44be0d94
+ 008e85f4 bytes 63be0d94
~~~


<a id="compare-ccbf15176f5ef49d17901438354e6d1d"></a>

### [`008e85b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e85b4.md) → [`008e8608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8608.md) FUN_008e8608

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e4590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e4/008e4590.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008e45e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e45e4.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e8618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e85b4.md#insn-008e8618)
- 新版 `008e866c`（命令位置の公開資料なし）

~~~diff
- 008e8618 ["INT_ADD", "register:40f0:8", ["const:8e8618:8", "const:4:8"]]
- 008e8618 ["CALL", null, ["callee:00c57f80:8"]]
+ 008e866c ["INT_ADD", "register:40f0:8", ["const:8e866c:8", "const:4:8"]]
+ 008e866c ["CALL", null, ["callee:00c57f80:8"]]
- 008e8618 bytes 26be0d94
+ 008e866c bytes 45be0d94
~~~


<a id="compare-d192adb31b423fe95719fabf96df049e"></a>

### [`008e8650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8650.md) → [`008e86a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e86a4.md) FUN_008e86a4

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e4590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e4/008e4590.md) · 呼出先 7件 [`008e8264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8264.md) [`008e87b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e87b8.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008e45e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e45e4.md) · 呼出先 7件 [`008e82b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e82b8.md) [`008e880c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e880c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e870c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8650.md#insn-008e870c) · [`008e8724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8650.md#insn-008e8724) · [`008e8778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8650.md#insn-008e8778)
- 新版 `008e8760`（命令位置の公開資料なし） · `008e8778`（命令位置の公開資料なし） · `008e87cc`（命令位置の公開資料なし）

~~~diff
- 008e870c ["INT_ADD", "register:40f0:8", ["const:8e870c:8", "const:4:8"]]
- 008e870c ["CALL", null, ["callee:00c57f60:8"]]
+ 008e8760 ["INT_ADD", "register:40f0:8", ["const:8e8760:8", "const:4:8"]]
+ 008e8760 ["CALL", null, ["callee:00c57f60:8"]]
- 008e870c bytes e1bd0d94
+ 008e8760 bytes 00be0d94
- 008e8724 ["INT_ADD", "register:40f0:8", ["const:8e8724:8", "const:4:8"]]
- 008e8724 ["CALL", null, ["callee:00c580d0:8"]]
+ 008e8778 ["INT_ADD", "register:40f0:8", ["const:8e8778:8", "const:4:8"]]
+ 008e8778 ["CALL", null, ["callee:00c580d0:8"]]
- 008e8724 bytes 37be0d94
+ 008e8778 bytes 56be0d94
- 008e8778 ["INT_ADD", "register:40f0:8", ["const:8e8778:8", "const:4:8"]]
- 008e8778 ["CALL", null, ["callee:008e82b8:8"]]
+ 008e87cc ["INT_ADD", "register:40f0:8", ["const:8e87cc:8", "const:4:8"]]
+ 008e87cc ["CALL", null, ["callee:008e82b8:8"]]
- 008e8778 bytes bbfeff97
+ 008e87cc bytes bbfeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30106eac1c637927a3b007fef38a7df7"></a>

### [`008e87b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e87b8.md) → [`008e880c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e880c.md) FUN_008e880c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e8650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8650.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008e86a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e86a4.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e87f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e87b8.md#insn-008e87f8)
- 新版 `008e884c`（命令位置の公開資料なし）

~~~diff
- 008e87f8 ["INT_ADD", "register:40f0:8", ["const:8e87f8:8", "const:4:8"]]
- 008e87f8 ["CALL", null, ["callee:00c57f80:8"]]
+ 008e884c ["INT_ADD", "register:40f0:8", ["const:8e884c:8", "const:4:8"]]
+ 008e884c ["CALL", null, ["callee:00c57f80:8"]]
- 008e87f8 bytes aebd0d94
+ 008e884c bytes cdbd0d94
~~~


<a id="compare-faeca502ef5763304a9e5564e602eb84"></a>

### [`008e8820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8820.md) → [`008e8874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8874.md) FUN_008e8874

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e4590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e4/008e4590.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`008e897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e897c.md) [`008e8a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8a04.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`008e45e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e45e4.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`008e89d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e89d0.md) [`008e8a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8a58.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e886c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8820.md#insn-008e886c) · [`008e88ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8820.md#insn-008e88ec) · [`008e893c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8820.md#insn-008e893c)
- 新版 `008e88c0`（命令位置の公開資料なし） · `008e8940`（命令位置の公開資料なし） · `008e8990`（命令位置の公開資料なし）

~~~diff
- 008e886c ["INT_ADD", "register:40f0:8", ["const:8e886c:8", "const:4:8"]]
- 008e886c ["CALL", null, ["callee:00c57f60:8"]]
+ 008e88c0 ["INT_ADD", "register:40f0:8", ["const:8e88c0:8", "const:4:8"]]
+ 008e88c0 ["CALL", null, ["callee:00c57f60:8"]]
- 008e886c bytes 89bd0d94
+ 008e88c0 bytes a8bd0d94
- 008e88ec ["INT_ADD", "register:40f0:8", ["const:8e88ec:8", "const:4:8"]]
- 008e88ec ["CALL", null, ["callee:0043bb60:8"]]
+ 008e8940 ["INT_ADD", "register:40f0:8", ["const:8e8940:8", "const:4:8"]]
+ 008e8940 ["CALL", null, ["callee:0043bb60:8"]]
- 008e88ec bytes 8d4ced97
+ 008e8940 bytes 884ced97
- 008e893c ["INT_ADD", "register:40f0:8", ["const:8e893c:8", "const:4:8"]]
- 008e893c ["CALL", null, ["callee:008e8a58:8"]]
+ 008e8990 ["INT_ADD", "register:40f0:8", ["const:8e8990:8", "const:4:8"]]
+ 008e8990 ["CALL", null, ["callee:008e8a58:8"]]
- 008e893c bytes 32000094
+ 008e8990 bytes 32000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64bd8577a8232a7c0382acf140974526"></a>

### [`008e897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e897c.md) → [`008e89d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e89d0.md) FUN_008e89d0

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e8820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8820.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008e8874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8874.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e89e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e897c.md#insn-008e89e0)
- 新版 `008e8a34`（命令位置の公開資料なし）

~~~diff
- 008e89e0 ["INT_ADD", "register:40f0:8", ["const:8e89e0:8", "const:4:8"]]
- 008e89e0 ["CALL", null, ["callee:00c57f80:8"]]
+ 008e8a34 ["INT_ADD", "register:40f0:8", ["const:8e8a34:8", "const:4:8"]]
+ 008e8a34 ["CALL", null, ["callee:00c57f80:8"]]
- 008e89e0 bytes 34bd0d94
+ 008e8a34 bytes 53bd0d94
~~~


<a id="compare-90e2b2115a748eed720b77f33e97da0c"></a>

### [`008e8a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8a18.md) → [`008e8a6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8a6c.md) FUN_008e8a6c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e8a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8a18.md#insn-008e8a58)
- 新版 `008e8aac`（命令位置の公開資料なし）

~~~diff
- 008e8a58 ["INT_ADD", "register:40f0:8", ["const:8e8a58:8", "const:4:8"]]
- 008e8a58 ["CALL", null, ["callee:00c57f80:8"]]
+ 008e8aac ["INT_ADD", "register:40f0:8", ["const:8e8aac:8", "const:4:8"]]
+ 008e8aac ["CALL", null, ["callee:00c57f80:8"]]
- 008e8a58 bytes 16bd0d94
+ 008e8aac bytes 35bd0d94
~~~


<a id="compare-41b899047e673e27a94f53742c97da5a"></a>

### [`008e8a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8a6c.md) → [`008e8ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8ac0.md) FUN_008e8ac0

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e4590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e4/008e4590.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`008e8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8bc8.md) [`008e8c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8c50.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`008e45e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e45e4.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`008e8c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8c1c.md) [`008e8ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8ca4.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e8ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8a6c.md#insn-008e8ab8) · [`008e8b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8a6c.md#insn-008e8b38) · [`008e8b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8a6c.md#insn-008e8b88)
- 新版 `008e8b0c`（命令位置の公開資料なし） · `008e8b8c`（命令位置の公開資料なし） · `008e8bdc`（命令位置の公開資料なし）

~~~diff
- 008e8ab8 ["INT_ADD", "register:40f0:8", ["const:8e8ab8:8", "const:4:8"]]
- 008e8ab8 ["CALL", null, ["callee:00c57f60:8"]]
+ 008e8b0c ["INT_ADD", "register:40f0:8", ["const:8e8b0c:8", "const:4:8"]]
+ 008e8b0c ["CALL", null, ["callee:00c57f60:8"]]
- 008e8ab8 bytes f6bc0d94
+ 008e8b0c bytes 15bd0d94
- 008e8b38 ["INT_ADD", "register:40f0:8", ["const:8e8b38:8", "const:4:8"]]
- 008e8b38 ["CALL", null, ["callee:0043bb60:8"]]
+ 008e8b8c ["INT_ADD", "register:40f0:8", ["const:8e8b8c:8", "const:4:8"]]
+ 008e8b8c ["CALL", null, ["callee:0043bb60:8"]]
- 008e8b38 bytes fa4bed97
+ 008e8b8c bytes f54bed97
- 008e8b88 ["INT_ADD", "register:40f0:8", ["const:8e8b88:8", "const:4:8"]]
- 008e8b88 ["CALL", null, ["callee:008e8ca4:8"]]
+ 008e8bdc ["INT_ADD", "register:40f0:8", ["const:8e8bdc:8", "const:4:8"]]
+ 008e8bdc ["CALL", null, ["callee:008e8ca4:8"]]
- 008e8b88 bytes 32000094
+ 008e8bdc bytes 32000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-471f95ea893a963cdb3cc1b4eeae2028"></a>

### [`008e8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8bc8.md) → [`008e8c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8c1c.md) FUN_008e8c1c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e8a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8a6c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008e8ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8ac0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e8c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8bc8.md#insn-008e8c2c)
- 新版 `008e8c80`（命令位置の公開資料なし）

~~~diff
- 008e8c2c ["INT_ADD", "register:40f0:8", ["const:8e8c2c:8", "const:4:8"]]
- 008e8c2c ["CALL", null, ["callee:00c57f80:8"]]
+ 008e8c80 ["INT_ADD", "register:40f0:8", ["const:8e8c80:8", "const:4:8"]]
+ 008e8c80 ["CALL", null, ["callee:00c57f80:8"]]
- 008e8c2c bytes a1bc0d94
+ 008e8c80 bytes c0bc0d94
~~~


<a id="compare-71bd81e1206ea548b16ef59f3340bfe4"></a>

### [`008e8c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8c64.md) → [`008e8cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8cb8.md) FUN_008e8cb8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e8ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8c64.md#insn-008e8ca4)
- 新版 `008e8cf8`（命令位置の公開資料なし）

~~~diff
- 008e8ca4 ["INT_ADD", "register:40f0:8", ["const:8e8ca4:8", "const:4:8"]]
- 008e8ca4 ["CALL", null, ["callee:00c57f80:8"]]
+ 008e8cf8 ["INT_ADD", "register:40f0:8", ["const:8e8cf8:8", "const:4:8"]]
+ 008e8cf8 ["CALL", null, ["callee:00c57f80:8"]]
- 008e8ca4 bytes 83bc0d94
+ 008e8cf8 bytes a2bc0d94
~~~


<a id="compare-bdcdd22c51d741ab0d52efb43979c39b"></a>

### [`008e8cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8cb8.md) → [`008e8d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8d0c.md) FUN_008e8d0c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e28bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e2/008e28bc.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`008e863c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e863c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008e2910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e2/008e2910.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`008e8690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8690.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e8d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8cb8.md#insn-008e8d40) · [`008e8dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8cb8.md#insn-008e8dfc) · [`008e8e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8cb8.md#insn-008e8e18)
- 新版 `008e8d94`（命令位置の公開資料なし） · `008e8e50`（命令位置の公開資料なし） · `008e8e6c`（命令位置の公開資料なし）

~~~diff
- 008e8d40 ["INT_ADD", "register:40f0:8", ["const:8e8d40:8", "const:4:8"]]
- 008e8d40 ["CALL", null, ["callee:00c57f60:8"]]
+ 008e8d94 ["INT_ADD", "register:40f0:8", ["const:8e8d94:8", "const:4:8"]]
+ 008e8d94 ["CALL", null, ["callee:00c57f60:8"]]
- 008e8d40 bytes 54bc0d94
+ 008e8d94 bytes 73bc0d94
- 008e8dfc ["INT_ADD", "register:40f0:8", ["const:8e8dfc:8", "const:4:8"]]
- 008e8dfc ["CALL", null, ["callee:00c57f80:8"]]
+ 008e8e50 ["INT_ADD", "register:40f0:8", ["const:8e8e50:8", "const:4:8"]]
+ 008e8e50 ["CALL", null, ["callee:00c57f80:8"]]
- 008e8dfc bytes 2dbc0d94
+ 008e8e50 bytes 4cbc0d94
- 008e8e18 ["INT_ADD", "register:40f0:8", ["const:8e8e18:8", "const:4:8"]]
- 008e8e18 ["CALL", null, ["callee:00c57f80:8"]]
+ 008e8e6c ["INT_ADD", "register:40f0:8", ["const:8e8e6c:8", "const:4:8"]]
+ 008e8e6c ["CALL", null, ["callee:00c57f80:8"]]
- 008e8e18 bytes 26bc0d94
+ 008e8e6c bytes 45bc0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c71e22ed446c3910b8ec230c3f7ee511"></a>

### [`008e8e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8e40.md) → [`008e8e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8e94.md) FUN_008e8e94

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e28bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e2/008e28bc.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`008e854c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e854c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008e2910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e2/008e2910.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`008e85a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e85a0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008e8ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8e40.md#insn-008e8ea8) · [`008e8f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8e40.md#insn-008e8f44) · [`008e8f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8e40.md#insn-008e8f60)
- 新版 `008e8efc`（命令位置の公開資料なし） · `008e8f98`（命令位置の公開資料なし） · `008e8fb4`（命令位置の公開資料なし）

~~~diff
- 008e8ea8 ["INT_ADD", "register:40f0:8", ["const:8e8ea8:8", "const:4:8"]]
- 008e8ea8 ["CALL", null, ["callee:00c57f60:8"]]
+ 008e8efc ["INT_ADD", "register:40f0:8", ["const:8e8efc:8", "const:4:8"]]
+ 008e8efc ["CALL", null, ["callee:00c57f60:8"]]
- 008e8ea8 bytes fabb0d94
+ 008e8efc bytes 19bc0d94
- 008e8f44 ["INT_ADD", "register:40f0:8", ["const:8e8f44:8", "const:4:8"]]
- 008e8f44 ["CALL", null, ["callee:00c57f80:8"]]
+ 008e8f98 ["INT_ADD", "register:40f0:8", ["const:8e8f98:8", "const:4:8"]]
+ 008e8f98 ["CALL", null, ["callee:00c57f80:8"]]
- 008e8f44 bytes dbbb0d94
+ 008e8f98 bytes fabb0d94
- 008e8f60 ["INT_ADD", "register:40f0:8", ["const:8e8f60:8", "const:4:8"]]
- 008e8f60 ["CALL", null, ["callee:00c57f80:8"]]
+ 008e8fb4 ["INT_ADD", "register:40f0:8", ["const:8e8fb4:8", "const:4:8"]]
+ 008e8fb4 ["CALL", null, ["callee:00c57f80:8"]]
- 008e8f60 bytes d4bb0d94
+ 008e8fb4 bytes f3bb0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-478f79f5be195de797a75e8271add762"></a>

### [`008ea39c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea39c.md) → [`008ea3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea3f0.md) FUN_008ea3f0

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e51e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e5/008e51e4.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`008e8c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8c50.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008e5238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5238.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`008e8ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8ca4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008ea420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea39c.md#insn-008ea420) · [`008ea470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea39c.md#insn-008ea470) · [`008ea4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea39c.md#insn-008ea4ec)
- 新版 `008ea474`（命令位置の公開資料なし） · `008ea4c4`（命令位置の公開資料なし） · `008ea540`（命令位置の公開資料なし）

~~~diff
- 008ea420 ["INT_ADD", "register:40f0:8", ["const:8ea420:8", "const:4:8"]]
- 008ea420 ["CALL", null, ["callee:00c57f60:8"]]
+ 008ea474 ["INT_ADD", "register:40f0:8", ["const:8ea474:8", "const:4:8"]]
+ 008ea474 ["CALL", null, ["callee:00c57f60:8"]]
- 008ea420 bytes 9cb60d94
+ 008ea474 bytes bbb60d94
- 008ea470 ["INT_ADD", "register:40f0:8", ["const:8ea470:8", "const:4:8"]]
- 008ea470 ["CALL", null, ["callee:0043bb60:8"]]
+ 008ea4c4 ["INT_ADD", "register:40f0:8", ["const:8ea4c4:8", "const:4:8"]]
+ 008ea4c4 ["CALL", null, ["callee:0043bb60:8"]]
- 008ea470 bytes ac45ed97
+ 008ea4c4 bytes a745ed97
- 008ea4ec ["INT_ADD", "register:40f0:8", ["const:8ea4ec:8", "const:4:8"]]
- 008ea4ec ["CALL", null, ["callee:00c57f80:8"]]
+ 008ea540 ["INT_ADD", "register:40f0:8", ["const:8ea540:8", "const:4:8"]]
+ 008ea540 ["CALL", null, ["callee:00c57f80:8"]]
- 008ea4ec bytes 71b60d94
+ 008ea540 bytes 90b60d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2b2cb8c9b7841a573444080fc2d7a6b"></a>

### [`008ea598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea598.md) → [`008ea5ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea5ec.md) FUN_008ea5ec

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e51e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e5/008e51e4.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`008e8a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8a04.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008e5238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5238.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`008e8a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8a58.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008ea61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea598.md#insn-008ea61c) · [`008ea66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea598.md#insn-008ea66c) · [`008ea6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008ea598.md#insn-008ea6e4)
- 新版 `008ea670`（命令位置の公開資料なし） · `008ea6c0`（命令位置の公開資料なし） · `008ea738`（命令位置の公開資料なし）

~~~diff
- 008ea61c ["INT_ADD", "register:40f0:8", ["const:8ea61c:8", "const:4:8"]]
- 008ea61c ["CALL", null, ["callee:00c57f60:8"]]
+ 008ea670 ["INT_ADD", "register:40f0:8", ["const:8ea670:8", "const:4:8"]]
+ 008ea670 ["CALL", null, ["callee:00c57f60:8"]]
- 008ea61c bytes 1db60d94
+ 008ea670 bytes 3cb60d94
- 008ea66c ["INT_ADD", "register:40f0:8", ["const:8ea66c:8", "const:4:8"]]
- 008ea66c ["CALL", null, ["callee:0043bb60:8"]]
+ 008ea6c0 ["INT_ADD", "register:40f0:8", ["const:8ea6c0:8", "const:4:8"]]
+ 008ea6c0 ["CALL", null, ["callee:0043bb60:8"]]
- 008ea66c bytes 2d45ed97
+ 008ea6c0 bytes 2845ed97
- 008ea6e4 ["INT_ADD", "register:40f0:8", ["const:8ea6e4:8", "const:4:8"]]
- 008ea6e4 ["CALL", null, ["callee:00c57f80:8"]]
+ 008ea738 ["INT_ADD", "register:40f0:8", ["const:8ea738:8", "const:4:8"]]
+ 008ea738 ["CALL", null, ["callee:00c57f80:8"]]
- 008ea6e4 bytes f3b50d94
+ 008ea738 bytes 12b60d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-691143c4439f8c786fa9067999d94ddc"></a>

### [`008ec1cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ec/008ec1cc.md) → [`008ec220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ec/008ec220.md) FUN_008ec220

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008f6ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f6/008f6ae8.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`008f6b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f6b3c.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008ec1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ec/008ec1cc.md#insn-008ec1fc) · [`008ec210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ec/008ec1cc.md#insn-008ec210) · [`008ec218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ec/008ec1cc.md#insn-008ec218)
- 新版 `008ec250`（命令位置の公開資料なし） · `008ec264`（命令位置の公開資料なし） · `008ec26c`（命令位置の公開資料なし）

~~~diff
- 008ec1fc ["INT_ADD", "register:40f0:8", ["const:8ec1fc:8", "const:4:8"]]
- 008ec1fc ["CALL", null, ["callee:00c53da0:8"]]
+ 008ec250 ["INT_ADD", "register:40f0:8", ["const:8ec250:8", "const:4:8"]]
+ 008ec250 ["CALL", null, ["callee:00c53da0:8"]]
- 008ec1fc bytes c19e0d94
+ 008ec250 bytes d49e0d94
- 008ec210 ["COPY", "register:0:8", ["register:4040:8"]]
- 008ec210 ["INT_ADD", "register:40f0:8", ["const:8ec210:8", "const:4:8"]]
- 008ec210 ["CALLIND", null, ["register:0:8"]]
+ 008ec264 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008ec264 ["INT_ADD", "register:40f0:8", ["const:8ec264:8", "const:4:8"]]
+ 008ec264 ["CALLIND", null, ["register:0:8"]]
- 008ec210 bytes 00013fd6
+ 008ec264 bytes 00013fd6
- 008ec218 ["INT_ADD", "register:40f0:8", ["const:8ec218:8", "const:4:8"]]
- 008ec218 ["CALL", null, ["callee:00c57f50:8"]]
+ 008ec26c ["INT_ADD", "register:40f0:8", ["const:8ec26c:8", "const:4:8"]]
+ 008ec26c ["CALL", null, ["callee:00c57f50:8"]]
- 008ec218 bytes 1aaf0d94
+ 008ec26c bytes 39af0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15b435aed9ff87ec47ed3c1404129d65"></a>

### [`008f5a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f5a80.md) → [`008f5ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f5/008f5ad4.md) FUN_008f5ad4

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008f53b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f53b0.md) · 呼出先 4件 [`006d7ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d7ef4.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`008f5404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f5/008f5404.md) · 呼出先 4件 [`006d7f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7f4c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008f5aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f5a80.md#insn-008f5aac) · [`008f5ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f5a80.md#insn-008f5ac4) · [`008f5ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f5a80.md#insn-008f5ad8)
- 新版 `008f5b00`（命令位置の公開資料なし） · `008f5b18`（命令位置の公開資料なし） · `008f5b2c`（命令位置の公開資料なし）

~~~diff
- 008f5aac ["INT_ADD", "register:40f0:8", ["const:8f5aac:8", "const:4:8"]]
- 008f5aac ["CALL", null, ["callee:00c53d70:8"]]
+ 008f5b00 ["INT_ADD", "register:40f0:8", ["const:8f5b00:8", "const:4:8"]]
+ 008f5b00 ["CALL", null, ["callee:00c53d70:8"]]
- 008f5aac bytes 89780d94
+ 008f5b00 bytes 9c780d94
- 008f5ac4 ["INT_ADD", "register:40f0:8", ["const:8f5ac4:8", "const:4:8"]]
- 008f5ac4 ["CALL", null, ["callee:00c53da0:8"]]
+ 008f5b18 ["INT_ADD", "register:40f0:8", ["const:8f5b18:8", "const:4:8"]]
+ 008f5b18 ["CALL", null, ["callee:00c53da0:8"]]
- 008f5ac4 bytes 8f780d94
+ 008f5b18 bytes a2780d94
- 008f5ad8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008f5ad8 ["INT_ADD", "register:40f0:8", ["const:8f5ad8:8", "const:4:8"]]
- 008f5ad8 ["CALLIND", null, ["register:0:8"]]
+ 008f5b2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 008f5b2c ["INT_ADD", "register:40f0:8", ["const:8f5b2c:8", "const:4:8"]]
+ 008f5b2c ["CALLIND", null, ["register:0:8"]]
- 008f5ad8 bytes 00013fd6
+ 008f5b2c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37efbf7838b7976f893d73d56fb1a591"></a>

### [`008f9c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f9/008f9c14.md) → [`008f9c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9c68.md) FUN_008f9c68

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`008eb51c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008eb/008eb51c.md) [`008f39a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f3/008f39a8.md) [`008f53b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f53b0.md) [`008f5be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f5be4.md) [`008f62e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f6/008f62e4.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 7件 [`008eb570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb570.md) [`008f39fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f3/008f39fc.md) [`008f5404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f5/008f5404.md) [`008f5c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f5/008f5c38.md) [`008f6338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f6338.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008f9c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f9/008f9c14.md#insn-008f9c84) · [`008f9d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f9/008f9c14.md#insn-008f9d64)
- 新版 `008f9cd8`（命令位置の公開資料なし） · `008f9db8`（命令位置の公開資料なし）

~~~diff
- 008f9c84 ["INT_ADD", "register:40f0:8", ["const:8f9c84:8", "const:4:8"]]
- 008f9c84 ["CALL", null, ["callee:00c57f60:8"]]
+ 008f9cd8 ["INT_ADD", "register:40f0:8", ["const:8f9cd8:8", "const:4:8"]]
+ 008f9cd8 ["CALL", null, ["callee:00c57f60:8"]]
- 008f9c84 bytes 83780d94
+ 008f9cd8 bytes a2780d94
- 008f9d64 ["INT_ADD", "register:40f0:8", ["const:8f9d64:8", "const:4:8"]]
- 008f9d64 ["CALL", null, ["callee:0043bbe4:8"]]
+ 008f9db8 ["INT_ADD", "register:40f0:8", ["const:8f9db8:8", "const:4:8"]]
+ 008f9db8 ["CALL", null, ["callee:0043bbe4:8"]]
- 008f9d64 bytes 9007ed97
+ 008f9db8 bytes 8b07ed97
~~~


<a id="compare-36b7884cc048a3f936412c3449bbc865"></a>

### [`008fc32c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fc/008fc32c.md) → [`008fc380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fc/008fc380.md) FUN_008fc380

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`008fc460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fc/008fc460.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`009d0374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d0/009d0374.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`008fc4b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fc/008fc4b4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008fc3d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fc/008fc32c.md#insn-008fc3d4) · [`008fc408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fc/008fc32c.md#insn-008fc408) · [`008fc454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fc/008fc32c.md#insn-008fc454)
- 新版 `008fc428`（命令位置の公開資料なし） · `008fc45c`（命令位置の公開資料なし） · `008fc4a8`（命令位置の公開資料なし）

~~~diff
- 008fc3d4 ["INT_ADD", "register:40f0:8", ["const:8fc3d4:8", "const:4:8"]]
- 008fc3d4 ["CALL", null, ["callee:00c57f60:8"]]
+ 008fc428 ["INT_ADD", "register:40f0:8", ["const:8fc428:8", "const:4:8"]]
+ 008fc428 ["CALL", null, ["callee:00c57f60:8"]]
- 008fc3d4 bytes af6e0d94
+ 008fc428 bytes ce6e0d94
- 008fc408 ["INT_ADD", "register:40f0:8", ["const:8fc408:8", "const:4:8"]]
- 008fc408 ["CALL", null, ["callee:0043bbe4:8"]]
+ 008fc45c ["INT_ADD", "register:40f0:8", ["const:8fc45c:8", "const:4:8"]]
+ 008fc45c ["CALL", null, ["callee:0043bbe4:8"]]
- 008fc408 bytes e7fdec97
+ 008fc45c bytes e2fdec97
- 008fc454 ["INT_ADD", "register:40f0:8", ["const:8fc454:8", "const:4:8"]]
- 008fc454 ["CALL", null, ["callee:008fc4b4:8"]]
+ 008fc4a8 ["INT_ADD", "register:40f0:8", ["const:8fc4a8:8", "const:4:8"]]
+ 008fc4a8 ["CALL", null, ["callee:008fc4b4:8"]]
- 008fc454 bytes 03000094
+ 008fc4a8 bytes 03000094
~~~


<a id="compare-2f1cf8ab22281f18c477e04eaf57bd4e"></a>

### [`008fc460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fc/008fc460.md) → [`008fc4b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fc/008fc4b4.md) FUN_008fc4b4

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008fc32c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fc/008fc32c.md) · 呼出先 3件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008fc380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fc/008fc380.md) · 呼出先 3件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008fc510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fc/008fc460.md#insn-008fc510) · [`008fc518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fc/008fc460.md#insn-008fc518) · [`008fc5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fc/008fc460.md#insn-008fc5cc)
- 新版 `008fc564`（命令位置の公開資料なし） · `008fc56c`（命令位置の公開資料なし） · `008fc620`（命令位置の公開資料なし）

~~~diff
- 008fc510 ["INT_ADD", "register:40f0:8", ["const:8fc510:8", "const:4:8"]]
- 008fc510 ["CALL", null, ["callee:00494650:8"]]
+ 008fc564 ["INT_ADD", "register:40f0:8", ["const:8fc564:8", "const:4:8"]]
+ 008fc564 ["CALL", null, ["callee:00494650:8"]]
- 008fc510 bytes 4060ee97
+ 008fc564 bytes 3b60ee97
- 008fc518 ["INT_ADD", "register:40f0:8", ["const:8fc518:8", "const:4:8"]]
- 008fc518 ["CALL", null, ["callee:00c57f80:8"]]
+ 008fc56c ["INT_ADD", "register:40f0:8", ["const:8fc56c:8", "const:4:8"]]
+ 008fc56c ["CALL", null, ["callee:00c57f80:8"]]
- 008fc518 bytes 666e0d94
+ 008fc56c bytes 856e0d94
- 008fc5cc ["INT_ADD", "register:40f0:8", ["const:8fc5cc:8", "const:4:8"]]
- 008fc5cc ["CALL", null, ["callee:00494650:8"]]
+ 008fc620 ["INT_ADD", "register:40f0:8", ["const:8fc620:8", "const:4:8"]]
+ 008fc620 ["CALL", null, ["callee:00494650:8"]]
- 008fc5cc bytes 1160ee97
+ 008fc620 bytes 0c60ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28301af4573260c2d49983e50304a151"></a>

### [`008fd054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fd/008fd054.md) → [`008fd0a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fd/008fd0a8.md) FUN_008fd0a8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`0086a164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a164.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`0086a1bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a1bc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008fd06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fd/008fd054.md#insn-008fd06c)
- 新版 `008fd0c0`（命令位置の公開資料なし）

~~~diff
- 008fd06c ["INT_ADD", "register:40f0:8", ["const:8fd06c:8", "const:4:8"]]
- 008fd06c ["CALL", null, ["callee:005c17dc:8"]]
+ 008fd0c0 ["INT_ADD", "register:40f0:8", ["const:8fd0c0:8", "const:4:8"]]
+ 008fd0c0 ["CALL", null, ["callee:005c17dc:8"]]
- 008fd06c bytes cc11f397
+ 008fd0c0 bytes c711f397
~~~


<a id="compare-91021c250534703e4729763bf68ee0f2"></a>

### [`008fd084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fd/008fd084.md) → [`008fd0d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fd/008fd0d8.md) FUN_008fd0d8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008fc5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fc/008fc5f0.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`008fc644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fc/008fc644.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008fd0d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fd/008fd084.md#insn-008fd0d8) · [`008fd12c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fd/008fd084.md#insn-008fd12c) · [`008fd160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fd/008fd084.md#insn-008fd160)
- 新版 `008fd12c`（命令位置の公開資料なし） · `008fd180`（命令位置の公開資料なし） · `008fd1b4`（命令位置の公開資料なし）

~~~diff
- 008fd0d8 ["INT_ADD", "register:40f0:8", ["const:8fd0d8:8", "const:4:8"]]
- 008fd0d8 ["CALL", null, ["callee:0046d7f0:8"]]
+ 008fd12c ["INT_ADD", "register:40f0:8", ["const:8fd12c:8", "const:4:8"]]
+ 008fd12c ["CALL", null, ["callee:0046d7f0:8"]]
- 008fd0d8 bytes b6c1ed97
+ 008fd12c bytes b1c1ed97
- 008fd12c ["INT_ADD", "register:40f0:8", ["const:8fd12c:8", "const:4:8"]]
- 008fd12c ["CALL", null, ["callee:00c57f60:8"]]
+ 008fd180 ["INT_ADD", "register:40f0:8", ["const:8fd180:8", "const:4:8"]]
+ 008fd180 ["CALL", null, ["callee:00c57f60:8"]]
- 008fd12c bytes 596b0d94
+ 008fd180 bytes 786b0d94
- 008fd160 ["INT_ADD", "register:40f0:8", ["const:8fd160:8", "const:4:8"]]
- 008fd160 ["CALL", null, ["callee:0043bbe4:8"]]
+ 008fd1b4 ["INT_ADD", "register:40f0:8", ["const:8fd1b4:8", "const:4:8"]]
+ 008fd1b4 ["CALL", null, ["callee:0043bbe4:8"]]
- 008fd160 bytes 91faec97
+ 008fd1b4 bytes 8cfaec97
~~~


<a id="compare-57027680e474650c8dac995117ee1766"></a>

### [`008fe584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fe/008fe584.md) → [`008fe5d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fe/008fe5d8.md) FUN_008fe5d8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008fd500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fd/008fd500.md) · 呼出先 2件 [`008ac9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ac/008ac9dc.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`008fd554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fd/008fd554.md) · 呼出先 2件 [`008aca34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ac/008aca34.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008fe5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fe/008fe584.md#insn-008fe5a8) · [`008fe5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fe/008fe584.md#insn-008fe5e0)
- 新版 `008fe5fc`（命令位置の公開資料なし） · `008fe634`（命令位置の公開資料なし）

~~~diff
- 008fe5a8 ["INT_ADD", "register:40f0:8", ["const:8fe5a8:8", "const:4:8"]]
- 008fe5a8 ["CALL", null, ["callee:008aca34:8"]]
+ 008fe5fc ["INT_ADD", "register:40f0:8", ["const:8fe5fc:8", "const:4:8"]]
+ 008fe5fc ["CALL", null, ["callee:008aca34:8"]]
- 008fe5a8 bytes 0db9fe97
+ 008fe5fc bytes 0eb9fe97
- 008fe5e0 ["INT_ADD", "register:40f0:8", ["const:8fe5e0:8", "const:4:8"]]
- 008fe5e0 ["CALL", null, ["callee:00c57fb0:8"]]
+ 008fe634 ["INT_ADD", "register:40f0:8", ["const:8fe634:8", "const:4:8"]]
+ 008fe634 ["CALL", null, ["callee:00c57fb0:8"]]
- 008fe5e0 bytes 40660d94
+ 008fe634 bytes 5f660d94
~~~


<a id="compare-c0914db7892463eb08df47db739e6152"></a>

### [`008ff3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff3d8.md) → [`008ff42c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ff/008ff42c.md) FUN_008ff42c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008ff3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff3d8.md#insn-008ff3f0) · [`008ff3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff3d8.md#insn-008ff3fc)
- 新版 `008ff444`（命令位置の公開資料なし） · `008ff450`（命令位置の公開資料なし）

~~~diff
- 008ff3f0 ["INT_ADD", "register:40f0:8", ["const:8ff3f0:8", "const:4:8"]]
- 008ff3f0 ["CALL", null, ["callee:005c17dc:8"]]
+ 008ff444 ["INT_ADD", "register:40f0:8", ["const:8ff444:8", "const:4:8"]]
+ 008ff444 ["CALL", null, ["callee:005c17dc:8"]]
- 008ff3f0 bytes eb08f397
+ 008ff444 bytes e608f397
- 008ff3fc ["INT_ADD", "register:40f0:8", ["const:8ff3fc:8", "const:4:8"]]
- 008ff3fc ["CALL", null, ["callee:005c17dc:8"]]
+ 008ff450 ["INT_ADD", "register:40f0:8", ["const:8ff450:8", "const:4:8"]]
+ 008ff450 ["CALL", null, ["callee:005c17dc:8"]]
- 008ff3fc bytes e808f397
+ 008ff450 bytes e308f397
~~~


<a id="compare-dd86e990d95fecd9813d732efeeafb3d"></a>

### [`009012b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00901/009012b4.md) → [`00901308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00901/00901308.md) FUN_00901308

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0090118c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00901/0090118c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`009011e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00901/009011e0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009012c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00901/009012b4.md#insn-009012c4)
- 新版 `00901318`（命令位置の公開資料なし）

~~~diff
- 009012c4 ["INT_ADD", "register:40f0:8", ["const:9012c4:8", "const:4:8"]]
- 009012c4 ["CALL", null, ["callee:009011e0:8"]]
+ 00901318 ["INT_ADD", "register:40f0:8", ["const:901318:8", "const:4:8"]]
+ 00901318 ["CALL", null, ["callee:009011e0:8"]]
- 009012c4 bytes b2ffff97
+ 00901318 bytes b2ffff97
~~~


<a id="compare-72fa18c2349585366719a64ab2189959"></a>

### [`009012d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00901/009012d8.md) → [`0090132c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00901/0090132c.md) FUN_0090132c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`008ff8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff8cc.md) [`00a3f34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3f/00a3f34c.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`007f1ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ab8.md) [`007f1e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1e90.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`008ff920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ff/008ff920.md) [`00a3f3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3f/00a3f3a0.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e8e4.md) [`007f1b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1b10.md) [`007f1ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1ee8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00901398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00901/009012d8.md#insn-00901398) · [`009013c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00901/009012d8.md#insn-009013c0) · [`00901408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00901/009012d8.md#insn-00901408)
- 新版 `009013ec`（命令位置の公開資料なし） · `00901414`（命令位置の公開資料なし） · `0090145c`（命令位置の公開資料なし）

~~~diff
- 00901398 ["INT_ADD", "register:40f0:8", ["const:901398:8", "const:4:8"]]
- 00901398 ["CALL", null, ["callee:00c57f60:8"]]
+ 009013ec ["INT_ADD", "register:40f0:8", ["const:9013ec:8", "const:4:8"]]
+ 009013ec ["CALL", null, ["callee:00c57f60:8"]]
- 00901398 bytes be5a0d94
+ 009013ec bytes dd5a0d94
- 009013c0 ["INT_ADD", "register:40f0:8", ["const:9013c0:8", "const:4:8"]]
- 009013c0 ["CALL", null, ["callee:007f1b10:8"]]
+ 00901414 ["INT_ADD", "register:40f0:8", ["const:901414:8", "const:4:8"]]
+ 00901414 ["CALL", null, ["callee:007f1b10:8"]]
- 009013c0 bytes bec1fb97
+ 00901414 bytes bfc1fb97
- 00901408 ["INT_ADD", "register:40f0:8", ["const:901408:8", "const:4:8"]]
- 00901408 ["CALL", null, ["callee:007f1b10:8"]]
+ 0090145c ["INT_ADD", "register:40f0:8", ["const:90145c:8", "const:4:8"]]
+ 0090145c ["CALL", null, ["callee:007f1b10:8"]]
- 00901408 bytes acc1fb97
+ 0090145c bytes adc1fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f90a5660576a0134e3a99e125443915"></a>

### [`0090397c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00903/0090397c.md) → [`009039d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00903/009039d0.md) FUN_009039d0

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 2件 [`009039a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00903/009039a0.md) [`00903c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00903/00903c70.md)
- 新版 呼出元 1件 [`00b28ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b28/00b28ff0.md) · 呼出先 2件 [`009039f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00903/009039f4.md) [`00903cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00903/00903cc4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0090398c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00903/0090397c.md#insn-0090398c)
- 新版 `009039e0`（命令位置の公開資料なし）

~~~diff
- 0090398c ["INT_ADD", "register:40f0:8", ["const:90398c:8", "const:4:8"]]
- 0090398c ["CALL", null, ["callee:009039f4:8"]]
+ 009039e0 ["INT_ADD", "register:40f0:8", ["const:9039e0:8", "const:4:8"]]
+ 009039e0 ["CALL", null, ["callee:009039f4:8"]]
- 0090398c bytes 05000094
+ 009039e0 bytes 05000094
~~~


<a id="compare-2e7122e0bcff0da5a6ea2b9ccf5ded0f"></a>

### [`00903f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00903/00903f44.md) → [`00903f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00903/00903f98.md) FUN_00903f98

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 20件 [`005afc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afc78.md) [`005afe08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afe08.md) [`006623ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/006623ec.md) [`00662490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/00662490.md) [`00662534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/00662534.md) · 呼出先 3件 [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) [`00802ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ee0.md)
- 新版 呼出元 20件 [`005afcb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005af/005afcb8.md) [`005afe48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005af/005afe48.md) [`0066242c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00662/0066242c.md) [`006624d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00662/006624d0.md) [`00662574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00662/00662574.md) · 呼出先 3件 [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md) [`00802d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802d00.md) [`00802f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802f38.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00903f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00903/00903f44.md#insn-00903f68) · [`00903f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00903/00903f44.md#insn-00903f70) · [`00903f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00903/00903f44.md#insn-00903f78)
- 新版 `00903fbc`（命令位置の公開資料なし） · `00903fc4`（命令位置の公開資料なし） · `00903fcc`（命令位置の公開資料なし）

~~~diff
- 00903f68 ["INT_ADD", "register:40f0:8", ["const:903f68:8", "const:4:8"]]
- 00903f68 ["CALL", null, ["callee:00802bb0:8"]]
+ 00903fbc ["INT_ADD", "register:40f0:8", ["const:903fbc:8", "const:4:8"]]
+ 00903fbc ["CALL", null, ["callee:00802bb0:8"]]
- 00903f68 bytes fcfafb97
+ 00903fbc bytes fdfafb97
- 00903f70 ["INT_ADD", "register:40f0:8", ["const:903f70:8", "const:4:8"]]
- 00903f70 ["CALL", null, ["callee:00802d00:8"]]
+ 00903fc4 ["INT_ADD", "register:40f0:8", ["const:903fc4:8", "const:4:8"]]
+ 00903fc4 ["CALL", null, ["callee:00802d00:8"]]
- 00903f70 bytes 4efbfb97
+ 00903fc4 bytes 4ffbfb97
- 00903f78 ["INT_ADD", "register:40f0:8", ["const:903f78:8", "const:4:8"]]
- 00903f78 ["CALL", null, ["callee:00802f38:8"]]
+ 00903fcc ["INT_ADD", "register:40f0:8", ["const:903fcc:8", "const:4:8"]]
+ 00903fcc ["CALL", null, ["callee:00802f38:8"]]
- 00903f78 bytes dafbfb97
+ 00903fcc bytes dbfbfb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96361c8e6339d119b47e325aa0f4f4e3"></a>

### [`0090401c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/0090401c.md) → [`00904070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00904/00904070.md) FUN_00904070

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 3件 [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) [`00802ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ee0.md)
- 新版 呼出元 2件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`00a47f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47f54.md) · 呼出先 3件 [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md) [`00802d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802d00.md) [`00802f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802f38.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00904044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/0090401c.md#insn-00904044) · [`0090404c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/0090401c.md#insn-0090404c) · [`00904054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/0090401c.md#insn-00904054)
- 新版 `00904098`（命令位置の公開資料なし） · `009040a0`（命令位置の公開資料なし） · `009040a8`（命令位置の公開資料なし）

~~~diff
- 00904044 ["INT_ADD", "register:40f0:8", ["const:904044:8", "const:4:8"]]
- 00904044 ["CALL", null, ["callee:00802bb0:8"]]
+ 00904098 ["INT_ADD", "register:40f0:8", ["const:904098:8", "const:4:8"]]
+ 00904098 ["CALL", null, ["callee:00802bb0:8"]]
- 00904044 bytes c5fafb97
+ 00904098 bytes c6fafb97
- 0090404c ["INT_ADD", "register:40f0:8", ["const:90404c:8", "const:4:8"]]
- 0090404c ["CALL", null, ["callee:00802d00:8"]]
+ 009040a0 ["INT_ADD", "register:40f0:8", ["const:9040a0:8", "const:4:8"]]
+ 009040a0 ["CALL", null, ["callee:00802d00:8"]]
- 0090404c bytes 17fbfb97
+ 009040a0 bytes 18fbfb97
- 00904054 ["INT_ADD", "register:40f0:8", ["const:904054:8", "const:4:8"]]
- 00904054 ["CALL", null, ["callee:00802f38:8"]]
+ 009040a8 ["INT_ADD", "register:40f0:8", ["const:9040a8:8", "const:4:8"]]
+ 009040a8 ["CALL", null, ["callee:00802f38:8"]]
- 00904054 bytes a3fbfb97
+ 009040a8 bytes a4fbfb97
~~~


<a id="compare-c54954fa1364ab63d0bbf494323a8255"></a>

### [`009040cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/009040cc.md) → [`00904120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00904/00904120.md) FUN_00904120

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 3件 [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) [`00802ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ee0.md)
- 新版 呼出元 1件 [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 3件 [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md) [`00802d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802d00.md) [`00802f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802f38.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009040f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/009040cc.md#insn-009040f0) · [`009040f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/009040cc.md#insn-009040f8) · [`00904100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/009040cc.md#insn-00904100)
- 新版 `00904144`（命令位置の公開資料なし） · `0090414c`（命令位置の公開資料なし） · `00904154`（命令位置の公開資料なし）

~~~diff
- 009040f0 ["INT_ADD", "register:40f0:8", ["const:9040f0:8", "const:4:8"]]
- 009040f0 ["CALL", null, ["callee:00802bb0:8"]]
+ 00904144 ["INT_ADD", "register:40f0:8", ["const:904144:8", "const:4:8"]]
+ 00904144 ["CALL", null, ["callee:00802bb0:8"]]
- 009040f0 bytes 9afafb97
+ 00904144 bytes 9bfafb97
- 009040f8 ["INT_ADD", "register:40f0:8", ["const:9040f8:8", "const:4:8"]]
- 009040f8 ["CALL", null, ["callee:00802d00:8"]]
+ 0090414c ["INT_ADD", "register:40f0:8", ["const:90414c:8", "const:4:8"]]
+ 0090414c ["CALL", null, ["callee:00802d00:8"]]
- 009040f8 bytes ecfafb97
+ 0090414c bytes edfafb97
- 00904100 ["INT_ADD", "register:40f0:8", ["const:904100:8", "const:4:8"]]
- 00904100 ["CALL", null, ["callee:00802f38:8"]]
+ 00904154 ["INT_ADD", "register:40f0:8", ["const:904154:8", "const:4:8"]]
+ 00904154 ["CALL", null, ["callee:00802f38:8"]]
- 00904100 bytes 78fbfb97
+ 00904154 bytes 79fbfb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b04ed296e3e7281d6350806e651ce4f5"></a>

### [`009041a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/009041a4.md) → [`009041f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00904/009041f8.md) FUN_009041f8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007cb5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb5e0.md) · 呼出先 3件 [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) [`00802ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ee0.md)
- 新版 呼出元 1件 [`007cb638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cb/007cb638.md) · 呼出先 3件 [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md) [`00802d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802d00.md) [`00802f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802f38.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009041cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/009041a4.md#insn-009041cc) · [`009041d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/009041a4.md#insn-009041d4) · [`009041dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/009041a4.md#insn-009041dc)
- 新版 `00904220`（命令位置の公開資料なし） · `00904228`（命令位置の公開資料なし） · `00904230`（命令位置の公開資料なし）

~~~diff
- 009041cc ["INT_ADD", "register:40f0:8", ["const:9041cc:8", "const:4:8"]]
- 009041cc ["CALL", null, ["callee:00802bb0:8"]]
+ 00904220 ["INT_ADD", "register:40f0:8", ["const:904220:8", "const:4:8"]]
+ 00904220 ["CALL", null, ["callee:00802bb0:8"]]
- 009041cc bytes 63fafb97
+ 00904220 bytes 64fafb97
- 009041d4 ["INT_ADD", "register:40f0:8", ["const:9041d4:8", "const:4:8"]]
- 009041d4 ["CALL", null, ["callee:00802d00:8"]]
+ 00904228 ["INT_ADD", "register:40f0:8", ["const:904228:8", "const:4:8"]]
+ 00904228 ["CALL", null, ["callee:00802d00:8"]]
- 009041d4 bytes b5fafb97
+ 00904228 bytes b6fafb97
- 009041dc ["INT_ADD", "register:40f0:8", ["const:9041dc:8", "const:4:8"]]
- 009041dc ["CALL", null, ["callee:00802f38:8"]]
+ 00904230 ["INT_ADD", "register:40f0:8", ["const:904230:8", "const:4:8"]]
+ 00904230 ["CALL", null, ["callee:00802f38:8"]]
- 009041dc bytes 41fbfb97
+ 00904230 bytes 42fbfb97
~~~


<a id="compare-1cac8a92abc20754fca6c3bd9a7d2819"></a>

### [`00904254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/00904254.md) → [`009042a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00904/009042a8.md) FUN_009042a8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) [`00789de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789de0.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`008d389c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d389c.md) [`00a92d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a92/00a92d48.md) · 呼出先 2件 [`00805fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/00805fe4.md) [`008077f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00807/008077f8.md)
- 新版 呼出元 5件 [`007738ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) [`00789e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00789/00789e38.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) [`008d38f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d3/008d38f0.md) [`00a92db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a92/00a92db8.md) · 呼出先 2件 [`0080603c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00806/0080603c.md) [`00807850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00807/00807850.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00904264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/00904254.md#insn-00904264) · [`00904284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/00904254.md#insn-00904284)
- 新版 `009042b8`（命令位置の公開資料なし） · `009042d8`（命令位置の公開資料なし）

~~~diff
- 00904264 ["INT_ADD", "register:40f0:8", ["const:904264:8", "const:4:8"]]
- 00904264 ["CALL", null, ["callee:0080603c:8"]]
+ 009042b8 ["INT_ADD", "register:40f0:8", ["const:9042b8:8", "const:4:8"]]
+ 009042b8 ["CALL", null, ["callee:0080603c:8"]]
- 00904264 bytes 6007fc97
+ 009042b8 bytes 6107fc97
- 00904284 ["INT_ADD", "register:40f0:8", ["const:904284:8", "const:4:8"]]
- 00904284 ["CALL", null, ["callee:00807850:8"]]
+ 009042d8 ["INT_ADD", "register:40f0:8", ["const:9042d8:8", "const:4:8"]]
+ 009042d8 ["CALL", null, ["callee:00807850:8"]]
- 00904284 bytes 5d0dfc97
+ 009042d8 bytes 5e0dfc97
~~~


<a id="compare-3e57e6309085348ef3e65af31e9b506e"></a>

### [`009042a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/009042a4.md) → [`009042f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00904/009042f8.md) FUN_009042f8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 1件 [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md)
- 新版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 1件 [`00480338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480338.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009042b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/009042a4.md#insn-009042b8)
- 新版 `0090430c`（命令位置の公開資料なし）

~~~diff
- 009042b8 ["INT_ADD", "register:40f0:8", ["const:9042b8:8", "const:4:8"]]
- 009042b8 ["CALL", null, ["callee:00480338:8"]]
+ 0090430c ["INT_ADD", "register:40f0:8", ["const:90430c:8", "const:4:8"]]
+ 0090430c ["CALL", null, ["callee:00480338:8"]]
- 009042b8 bytes 10f0ed97
+ 0090430c bytes 0bf0ed97
~~~


<a id="compare-3e66bad886bd1ad83a27d07a9b1a091f"></a>

### [`009042f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/009042f4.md) → [`00904348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00904/00904348.md) FUN_00904348

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009039a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00903/009039a0.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00904478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/00904478.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`009039f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00903/009039f4.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`009044cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00904/009044cc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0090437c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/009042f4.md#insn-0090437c) · [`00904434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/009042f4.md#insn-00904434) · [`00904450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/009042f4.md#insn-00904450)
- 新版 `009043d0`（命令位置の公開資料なし） · `00904488`（命令位置の公開資料なし） · `009044a4`（命令位置の公開資料なし）

~~~diff
- 0090437c ["INT_ADD", "register:40f0:8", ["const:90437c:8", "const:4:8"]]
- 0090437c ["CALL", null, ["callee:00c57f60:8"]]
+ 009043d0 ["INT_ADD", "register:40f0:8", ["const:9043d0:8", "const:4:8"]]
+ 009043d0 ["CALL", null, ["callee:00c57f60:8"]]
- 0090437c bytes c54e0d94
+ 009043d0 bytes e44e0d94
- 00904434 ["INT_ADD", "register:40f0:8", ["const:904434:8", "const:4:8"]]
- 00904434 ["CALL", null, ["callee:00c57f80:8"]]
+ 00904488 ["INT_ADD", "register:40f0:8", ["const:904488:8", "const:4:8"]]
+ 00904488 ["CALL", null, ["callee:00c57f80:8"]]
- 00904434 bytes 9f4e0d94
+ 00904488 bytes be4e0d94
- 00904450 ["INT_ADD", "register:40f0:8", ["const:904450:8", "const:4:8"]]
- 00904450 ["CALL", null, ["callee:00c57f80:8"]]
+ 009044a4 ["INT_ADD", "register:40f0:8", ["const:9044a4:8", "const:4:8"]]
+ 009044a4 ["CALL", null, ["callee:00c57f80:8"]]
- 00904450 bytes 984e0d94
+ 009044a4 bytes b74e0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1f96d5d2e299b7aa461d79b1d2d0a44"></a>

### [`0090448c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/0090448c.md) → [`009044e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00904/009044e0.md) FUN_009044e0

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00903c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00903/00903c70.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00904610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/00904610.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00903cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00903/00903cc4.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00904664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00904/00904664.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00904514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/0090448c.md#insn-00904514) · [`009045cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/0090448c.md#insn-009045cc) · [`009045e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/0090448c.md#insn-009045e8)
- 新版 `00904568`（命令位置の公開資料なし） · `00904620`（命令位置の公開資料なし） · `0090463c`（命令位置の公開資料なし）

~~~diff
- 00904514 ["INT_ADD", "register:40f0:8", ["const:904514:8", "const:4:8"]]
- 00904514 ["CALL", null, ["callee:00c57f60:8"]]
+ 00904568 ["INT_ADD", "register:40f0:8", ["const:904568:8", "const:4:8"]]
+ 00904568 ["CALL", null, ["callee:00c57f60:8"]]
- 00904514 bytes 5f4e0d94
+ 00904568 bytes 7e4e0d94
- 009045cc ["INT_ADD", "register:40f0:8", ["const:9045cc:8", "const:4:8"]]
- 009045cc ["CALL", null, ["callee:00c57f80:8"]]
+ 00904620 ["INT_ADD", "register:40f0:8", ["const:904620:8", "const:4:8"]]
+ 00904620 ["CALL", null, ["callee:00c57f80:8"]]
- 009045cc bytes 394e0d94
+ 00904620 bytes 584e0d94
- 009045e8 ["INT_ADD", "register:40f0:8", ["const:9045e8:8", "const:4:8"]]
- 009045e8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0090463c ["INT_ADD", "register:40f0:8", ["const:90463c:8", "const:4:8"]]
+ 0090463c ["CALL", null, ["callee:00c57f80:8"]]
- 009045e8 bytes 324e0d94
+ 0090463c bytes 514e0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc498abd1f9f7d7150b76fcd81474a98"></a>

### [`00909fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00909/00909fe0.md) → [`0090a034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090a/0090a034.md) FUN_0090a034

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`009049b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/009049b4.md) [`00a6fd88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6f/00a6fd88.md) [`00a73530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a73/00a73530.md) [`00a7c4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7c/00a7c4f4.md) [`00b2e4b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2e/00b2e4b8.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00920500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00920/00920500.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 5件 [`00904a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00904/00904a08.md) [`00a6fdf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a6f/00a6fdf8.md) [`00a735a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a73/00a735a0.md) [`00a7c564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7c/00a7c564.md) [`00b2e554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2e/00b2e554.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00920554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00920/00920554.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0090a034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00909/00909fe0.md#insn-0090a034) · [`0090a044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00909/00909fe0.md#insn-0090a044) · [`0090a074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00909/00909fe0.md#insn-0090a074)
- 新版 `0090a088`（命令位置の公開資料なし） · `0090a098`（命令位置の公開資料なし） · `0090a0c8`（命令位置の公開資料なし）

~~~diff
- 0090a034 ["INT_ADD", "register:40f0:8", ["const:90a034:8", "const:4:8"]]
- 0090a034 ["CALL", null, ["callee:0043bb60:8"]]
+ 0090a088 ["INT_ADD", "register:40f0:8", ["const:90a088:8", "const:4:8"]]
+ 0090a088 ["CALL", null, ["callee:0043bb60:8"]]
- 0090a034 bytes bbc6ec97
+ 0090a088 bytes b6c6ec97
- 0090a044 ["INT_ADD", "register:40f0:8", ["const:90a044:8", "const:4:8"]]
- 0090a044 ["CALL", null, ["callee:0043bb60:8"]]
+ 0090a098 ["INT_ADD", "register:40f0:8", ["const:90a098:8", "const:4:8"]]
+ 0090a098 ["CALL", null, ["callee:0043bb60:8"]]
- 0090a044 bytes b7c6ec97
+ 0090a098 bytes b2c6ec97
- 0090a074 ["INT_ADD", "register:40f0:8", ["const:90a074:8", "const:4:8"]]
- 0090a074 ["CALL", null, ["callee:00920554:8"]]
+ 0090a0c8 ["INT_ADD", "register:40f0:8", ["const:90a0c8:8", "const:4:8"]]
+ 0090a0c8 ["CALL", null, ["callee:00920554:8"]]
- 0090a074 bytes 23590094
+ 0090a0c8 bytes 23590094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c098a532f4d24a0b29096f4feed3f8b3"></a>

### [`0090a104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090a/0090a104.md) → [`0090a158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090a/0090a158.md) FUN_0090a158

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00914e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00914/00914e30.md) [`009d3af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3af4.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`00914e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00914/00914e84.md) [`009d3b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d3/009d3b48.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0090a16c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090a/0090a104.md#insn-0090a16c) · [`0090a1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090a/0090a104.md#insn-0090a1a8)
- 新版 `0090a1c0`（命令位置の公開資料なし） · `0090a1fc`（命令位置の公開資料なし）

~~~diff
- 0090a16c ["INT_ADD", "register:40f0:8", ["const:90a16c:8", "const:4:8"]]
- 0090a16c ["CALL", null, ["callee:00c57f60:8"]]
+ 0090a1c0 ["INT_ADD", "register:40f0:8", ["const:90a1c0:8", "const:4:8"]]
+ 0090a1c0 ["CALL", null, ["callee:00c57f60:8"]]
- 0090a16c bytes 49370d94
+ 0090a1c0 bytes 68370d94
- 0090a1a8 ["INT_ADD", "register:40f0:8", ["const:90a1a8:8", "const:4:8"]]
- 0090a1a8 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0090a1fc ["INT_ADD", "register:40f0:8", ["const:90a1fc:8", "const:4:8"]]
+ 0090a1fc ["CALL", null, ["callee:0043bbe4:8"]]
- 0090a1a8 bytes 7fc6ec97
+ 0090a1fc bytes 7ac6ec97
~~~


<a id="compare-1fd3cf7cf9d1ad50186fd621178ce64c"></a>

### [`0090a54c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090a/0090a54c.md) → [`0090a5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090a/0090a5a0.md) FUN_0090a5a0

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0090a584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090a/0090a54c.md#insn-0090a584) · [`0090a598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090a/0090a54c.md#insn-0090a598) · [`0090a5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090a/0090a54c.md#insn-0090a5a0)
- 新版 `0090a5d8`（命令位置の公開資料なし） · `0090a5ec`（命令位置の公開資料なし） · `0090a5f4`（命令位置の公開資料なし）

~~~diff
- 0090a584 ["INT_ADD", "register:40f0:8", ["const:90a584:8", "const:4:8"]]
- 0090a584 ["CALL", null, ["callee:00c53da0:8"]]
+ 0090a5d8 ["INT_ADD", "register:40f0:8", ["const:90a5d8:8", "const:4:8"]]
+ 0090a5d8 ["CALL", null, ["callee:00c53da0:8"]]
- 0090a584 bytes df250d94
+ 0090a5d8 bytes f2250d94
- 0090a598 ["COPY", "register:0:8", ["register:4040:8"]]
- 0090a598 ["INT_ADD", "register:40f0:8", ["const:90a598:8", "const:4:8"]]
- 0090a598 ["CALLIND", null, ["register:0:8"]]
+ 0090a5ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 0090a5ec ["INT_ADD", "register:40f0:8", ["const:90a5ec:8", "const:4:8"]]
+ 0090a5ec ["CALLIND", null, ["register:0:8"]]
- 0090a598 bytes 00013fd6
+ 0090a5ec bytes 00013fd6
- 0090a5a0 ["INT_ADD", "register:40f0:8", ["const:90a5a0:8", "const:4:8"]]
- 0090a5a0 ["CALL", null, ["callee:00c57f50:8"]]
+ 0090a5f4 ["INT_ADD", "register:40f0:8", ["const:90a5f4:8", "const:4:8"]]
+ 0090a5f4 ["CALL", null, ["callee:00c57f50:8"]]
- 0090a5a0 bytes 38360d94
+ 0090a5f4 bytes 57360d94
~~~


<a id="compare-f6eb542aa413bf6b1ea7991fc052437a"></a>

### [`009202b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00920/009202b4.md) → [`00920308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00920/00920308.md) FUN_00920308

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0091ff5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0091f/0091ff5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0091ffb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0091f/0091ffb0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009202c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00920/009202b4.md#insn-009202c4)
- 新版 `00920318`（命令位置の公開資料なし）

~~~diff
- 009202c4 ["INT_ADD", "register:40f0:8", ["const:9202c4:8", "const:4:8"]]
- 009202c4 ["CALL", null, ["callee:0091ffb0:8"]]
+ 00920318 ["INT_ADD", "register:40f0:8", ["const:920318:8", "const:4:8"]]
+ 00920318 ["CALL", null, ["callee:0091ffb0:8"]]
- 009202c4 bytes 26ffff97
+ 00920318 bytes 26ffff97
~~~


<a id="compare-1c028cfc9d2ad26bc88a220641c2b5f8"></a>

### [`009204dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00920/009204dc.md) → [`00920530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00920/00920530.md) FUN_00920530

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`009202d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00920/009202d8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0092032c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00920/0092032c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009204ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00920/009204dc.md#insn-009204ec)
- 新版 `00920540`（命令位置の公開資料なし）

~~~diff
- 009204ec ["INT_ADD", "register:40f0:8", ["const:9204ec:8", "const:4:8"]]
- 009204ec ["CALL", null, ["callee:0092032c:8"]]
+ 00920540 ["INT_ADD", "register:40f0:8", ["const:920540:8", "const:4:8"]]
+ 00920540 ["CALL", null, ["callee:0092032c:8"]]
- 009204ec bytes 7bffff97
+ 00920540 bytes 7bffff97
~~~


<a id="compare-ef871412a57e8eaa7049877e8e809126"></a>

### [`0092709c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00927/0092709c.md) → [`009270f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00927/009270f0.md) FUN_009270f0

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00926e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00926/00926e60.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00926eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00926/00926eb4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009270ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00927/0092709c.md#insn-009270ac)
- 新版 `00927100`（命令位置の公開資料なし）

~~~diff
- 009270ac ["INT_ADD", "register:40f0:8", ["const:9270ac:8", "const:4:8"]]
- 009270ac ["CALL", null, ["callee:00926eb4:8"]]
+ 00927100 ["INT_ADD", "register:40f0:8", ["const:927100:8", "const:4:8"]]
+ 00927100 ["CALL", null, ["callee:00926eb4:8"]]
- 009270ac bytes 6dffff97
+ 00927100 bytes 6dffff97
~~~


<a id="compare-870d373e96ace1a5274c98bee919a860"></a>

### [`00928118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00928/00928118.md) → [`0092816c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00928/0092816c.md) FUN_0092816c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) · 呼出先 1件 [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md)
- 新版 呼出元 2件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`007738ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) · 呼出先 1件 [`0049f430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00928140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00928/00928118.md#insn-00928140)
- 新版 `00928194`（命令位置の公開資料なし）

~~~diff
- 00928140 ["INT_ADD", "register:40f0:8", ["const:928140:8", "const:4:8"]]
- 00928140 ["CALL", null, ["callee:0049f430:8"]]
+ 00928194 ["INT_ADD", "register:40f0:8", ["const:928194:8", "const:4:8"]]
+ 00928194 ["CALL", null, ["callee:0049f430:8"]]
- 00928140 bytes acdced97
+ 00928194 bytes a7dced97
~~~


<a id="compare-34f2b6bb55a79e81bca659c7dc159c49"></a>

### [`009291f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/009291f0.md) → [`00929244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00929/00929244.md) FUN_00929244

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 3件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md)
- 新版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 3件 [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00929208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/009291f0.md#insn-00929208) · [`00929210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/009291f0.md#insn-00929210) · [`0092921c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/009291f0.md#insn-0092921c)
- 新版 `0092925c`（命令位置の公開資料なし） · `00929264`（命令位置の公開資料なし） · `00929270`（命令位置の公開資料なし）

~~~diff
- 00929208 ["INT_ADD", "register:40f0:8", ["const:929208:8", "const:4:8"]]
- 00929208 ["CALL", null, ["callee:00c581b0:8"]]
+ 0092925c ["INT_ADD", "register:40f0:8", ["const:92925c:8", "const:4:8"]]
+ 0092925c ["CALL", null, ["callee:00c581b0:8"]]
- 00929208 bytes b6bb0c94
+ 0092925c bytes d5bb0c94
- 00929210 ["INT_ADD", "register:40f0:8", ["const:929210:8", "const:4:8"]]
- 00929210 ["CALL", null, ["callee:0048cec4:8"]]
+ 00929264 ["INT_ADD", "register:40f0:8", ["const:929264:8", "const:4:8"]]
+ 00929264 ["CALL", null, ["callee:0048cec4:8"]]
- 00929210 bytes 1d8fed97
+ 00929264 bytes 188fed97
- 0092921c ["INT_ADD", "register:40f0:8", ["const:92921c:8", "const:4:8"]]
- 0092921c ["CALL", null, ["callee:00c581c0:8"]]
+ 00929270 ["INT_ADD", "register:40f0:8", ["const:929270:8", "const:4:8"]]
+ 00929270 ["CALL", null, ["callee:00c581c0:8"]]
- 0092921c bytes b5bb0c94
+ 00929270 bytes d4bb0c94
~~~


<a id="compare-be1b6bfcb4ffd475f998df0398672816"></a>

### [`00929bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929bb4.md) → [`00929c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00929/00929c08.md) FUN_00929c08

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 3件 [`00480178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md) [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md) [`00480744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md)
- 新版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 3件 [`004801b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/004801b8.md) [`00480430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480430.md) [`00480784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480784.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00929bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929bb4.md#insn-00929bcc) · [`00929bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929bb4.md#insn-00929bdc) · [`00929bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929bb4.md#insn-00929bec)
- 新版 `00929c20`（命令位置の公開資料なし） · `00929c30`（命令位置の公開資料なし） · `00929c40`（命令位置の公開資料なし）

~~~diff
- 00929bcc ["INT_ADD", "register:40f0:8", ["const:929bcc:8", "const:4:8"]]
- 00929bcc ["CALL", null, ["callee:004801b8:8"]]
+ 00929c20 ["INT_ADD", "register:40f0:8", ["const:929c20:8", "const:4:8"]]
+ 00929c20 ["CALL", null, ["callee:004801b8:8"]]
- 00929bcc bytes 6b59ed97
+ 00929c20 bytes 6659ed97
- 00929bdc ["INT_ADD", "register:40f0:8", ["const:929bdc:8", "const:4:8"]]
- 00929bdc ["CALL", null, ["callee:004801b8:8"]]
+ 00929c30 ["INT_ADD", "register:40f0:8", ["const:929c30:8", "const:4:8"]]
+ 00929c30 ["CALL", null, ["callee:004801b8:8"]]
- 00929bdc bytes 6759ed97
+ 00929c30 bytes 6259ed97
- 00929bec ["INT_ADD", "register:40f0:8", ["const:929bec:8", "const:4:8"]]
- 00929bec ["CALL", null, ["callee:00480430:8"]]
+ 00929c40 ["INT_ADD", "register:40f0:8", ["const:929c40:8", "const:4:8"]]
+ 00929c40 ["CALL", null, ["callee:00480430:8"]]
- 00929bec bytes 015aed97
+ 00929c40 bytes fc59ed97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-676d5c8b96e1e839d10a947ae0eec801"></a>

### [`0092a010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0092a/0092a010.md) → [`0092a064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0092a/0092a064.md) FUN_0092a064

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0092a050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0092a/0092a050.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`0092a0a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0092a/0092a0a4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0092a018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0092a/0092a010.md#insn-0092a018)
- 新版 `0092a06c`（命令位置の公開資料なし）

~~~diff
- 0092a018 ["INT_ADD", "register:40f0:8", ["const:92a018:8", "const:4:8"]]
- 0092a018 ["CALL", null, ["callee:00851550:8"]]
+ 0092a06c ["INT_ADD", "register:40f0:8", ["const:92a06c:8", "const:4:8"]]
+ 0092a06c ["CALL", null, ["callee:00851550:8"]]
- 0092a018 bytes 389dfc97
+ 0092a06c bytes 399dfc97
~~~


<a id="compare-9d12bafc3123f5beb627fb05f25db26d"></a>

### [`0092a3d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0092a/0092a3d4.md) → [`0092a428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0092a/0092a428.md) FUN_0092a428

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0092a050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0092a/0092a050.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`0092a0a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0092a/0092a0a4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0092a3dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0092a/0092a3d4.md#insn-0092a3dc)
- 新版 `0092a430`（命令位置の公開資料なし）

~~~diff
- 0092a3dc ["INT_ADD", "register:40f0:8", ["const:92a3dc:8", "const:4:8"]]
- 0092a3dc ["CALL", null, ["callee:00851550:8"]]
+ 0092a430 ["INT_ADD", "register:40f0:8", ["const:92a430:8", "const:4:8"]]
+ 0092a430 ["CALL", null, ["callee:00851550:8"]]
- 0092a3dc bytes 479cfc97
+ 0092a430 bytes 489cfc97
~~~


<a id="compare-766ca5e262a90e73af29614450cfa4ac"></a>

### [`00930290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00930/00930290.md) → [`009302e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00930/009302e4.md) FUN_009302e4

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0093047c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00930/0093047c.md) [`00934604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934604.md) · 呼出先 3件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)
- 新版 呼出元 2件 [`009304d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00930/009304d0.md) [`00934658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00934/00934658.md) · 呼出先 3件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f70.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009302a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00930/00930290.md#insn-009302a8) · [`009302b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00930/00930290.md#insn-009302b8) · [`009302c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00930/00930290.md#insn-009302c0)
- 新版 `009302fc`（命令位置の公開資料なし） · `0093030c`（命令位置の公開資料なし） · `00930314`（命令位置の公開資料なし）

~~~diff
- 009302a8 ["INT_ADD", "register:40f0:8", ["const:9302a8:8", "const:4:8"]]
- 009302a8 ["CALL", null, ["callee:00851550:8"]]
+ 009302fc ["INT_ADD", "register:40f0:8", ["const:9302fc:8", "const:4:8"]]
+ 009302fc ["CALL", null, ["callee:00851550:8"]]
- 009302a8 bytes 9484fc97
+ 009302fc bytes 9584fc97
- 009302b8 ["INT_ADD", "register:40f0:8", ["const:9302b8:8", "const:4:8"]]
- 009302b8 ["CALL", null, ["callee:008b7a20:8"]]
+ 0093030c ["INT_ADD", "register:40f0:8", ["const:93030c:8", "const:4:8"]]
+ 0093030c ["CALL", null, ["callee:008b7a20:8"]]
- 009302b8 bytes c41dfe97
+ 0093030c bytes c51dfe97
- 009302c0 ["INT_ADD", "register:40f0:8", ["const:9302c0:8", "const:4:8"]]
- 009302c0 ["CALL", null, ["callee:008b6f70:8"]]
+ 00930314 ["INT_ADD", "register:40f0:8", ["const:930314:8", "const:4:8"]]
+ 00930314 ["CALL", null, ["callee:008b6f70:8"]]
- 009302c0 bytes 161bfe97
+ 00930314 bytes 171bfe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e4f90bf37cb495c8eb92a8d085911b9"></a>

### [`00930394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00930/00930394.md) → [`009303e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00930/009303e8.md) FUN_009303e8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) [`00a98d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a98/00a98d4c.md) [`00a98f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a98/00a98f00.md) · 呼出先 3件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 3件 [`00a47f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47f54.md) [`00a98dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a98/00a98dbc.md) [`00a98f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a98/00a98f70.md) · 呼出先 3件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009303c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00930/00930394.md#insn-009303c0) · [`009303d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00930/00930394.md#insn-009303d8) · [`009303fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00930/00930394.md#insn-009303fc)
- 新版 `00930414`（命令位置の公開資料なし） · `0093042c`（命令位置の公開資料なし） · `00930450`（命令位置の公開資料なし）

~~~diff
- 009303c0 ["INT_ADD", "register:40f0:8", ["const:9303c0:8", "const:4:8"]]
- 009303c0 ["CALL", null, ["callee:00c53d70:8"]]
+ 00930414 ["INT_ADD", "register:40f0:8", ["const:930414:8", "const:4:8"]]
+ 00930414 ["CALL", null, ["callee:00c53d70:8"]]
- 009303c0 bytes 448e0c94
+ 00930414 bytes 578e0c94
- 009303d8 ["INT_ADD", "register:40f0:8", ["const:9303d8:8", "const:4:8"]]
- 009303d8 ["CALL", null, ["callee:00c53da0:8"]]
+ 0093042c ["INT_ADD", "register:40f0:8", ["const:93042c:8", "const:4:8"]]
+ 0093042c ["CALL", null, ["callee:00c53da0:8"]]
- 009303d8 bytes 4a8e0c94
+ 0093042c bytes 5d8e0c94
- 009303fc ["COPY", "register:0:8", ["register:4040:8"]]
- 009303fc ["INT_ADD", "register:40f0:8", ["const:9303fc:8", "const:4:8"]]
- 009303fc ["CALLIND", null, ["register:0:8"]]
+ 00930450 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00930450 ["INT_ADD", "register:40f0:8", ["const:930450:8", "const:4:8"]]
+ 00930450 ["CALLIND", null, ["register:0:8"]]
- 009303fc bytes 00013fd6
+ 00930450 bytes 00013fd6
~~~


<a id="compare-75faba79edcc0038977e7f0cf4beba09"></a>

### [`00930414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00930/00930414.md) → [`00930468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00930/00930468.md) FUN_00930468

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`00853c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853c78.md) [`00a98d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a98/00a98d4c.md) [`00a98f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a98/00a98f00.md) · 呼出先 4件 [`00726f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726f48.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0092a7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0092a/0092a7a4.md) [`0092e66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0092e/0092e66c.md)
- 新版 呼出元 4件 [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) [`00853cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00853/00853cd0.md) [`00a98dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a98/00a98dbc.md) [`00a98f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a98/00a98f70.md) · 呼出先 4件 [`00726fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/00726fa0.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`0092a7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0092a/0092a7f8.md) [`0092e6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0092e/0092e6c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0093043c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00930/00930414.md#insn-0093043c) · [`00930444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00930/00930414.md#insn-00930444)
- 新版 `00930490`（命令位置の公開資料なし） · `00930498`（命令位置の公開資料なし）

~~~diff
- 0093043c ["INT_ADD", "register:40f0:8", ["const:93043c:8", "const:4:8"]]
- 0093043c ["CALL", null, ["callee:00851550:8"]]
+ 00930490 ["INT_ADD", "register:40f0:8", ["const:930490:8", "const:4:8"]]
+ 00930490 ["CALL", null, ["callee:00851550:8"]]
- 0093043c bytes 2f84fc97
+ 00930490 bytes 3084fc97
- 00930444 ["INT_ADD", "register:40f0:8", ["const:930444:8", "const:4:8"]]
- 00930444 ["CALL", null, ["callee:00726fa0:8"]]
+ 00930498 ["INT_ADD", "register:40f0:8", ["const:930498:8", "const:4:8"]]
+ 00930498 ["CALL", null, ["callee:00726fa0:8"]]
- 00930444 bytes c1daf797
+ 00930498 bytes c2daf797
~~~


<a id="compare-21a4811b7e94633101bdf73184e90afc"></a>

### [`009314b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/009314b4.md) → [`00931508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00931/00931508.md) FUN_00931508

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009314bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/009314b4.md#insn-009314bc) · [`009314cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/009314b4.md#insn-009314cc)
- 新版 `00931510`（命令位置の公開資料なし） · `00931520`（命令位置の公開資料なし）

~~~diff
- 009314bc ["INT_ADD", "register:40f0:8", ["const:9314bc:8", "const:4:8"]]
- 009314bc ["CALL", null, ["callee:00851550:8"]]
+ 00931510 ["INT_ADD", "register:40f0:8", ["const:931510:8", "const:4:8"]]
+ 00931510 ["CALL", null, ["callee:00851550:8"]]
- 009314bc bytes 0f80fc97
+ 00931510 bytes 1080fc97
- 009314cc ["INT_ADD", "register:40f0:8", ["const:9314cc:8", "const:4:8"]]
- 009314cc ["CALL", null, ["callee:00851550:8"]]
+ 00931520 ["INT_ADD", "register:40f0:8", ["const:931520:8", "const:4:8"]]
+ 00931520 ["CALL", null, ["callee:00851550:8"]]
- 009314cc bytes 0b80fc97
+ 00931520 bytes 0c80fc97
~~~


<a id="compare-bfad16f6210ae25bc1e8492866a561ae"></a>

### [`00935cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935cf8.md) → [`00935d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00935/00935d4c.md) FUN_00935d4c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`007320c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/007320c8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00732120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00732/00732120.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00935d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935cf8.md#insn-00935d54) · [`00935db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935cf8.md#insn-00935db8) · [`00935dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935cf8.md#insn-00935dc8)
- 新版 `00935da8`（命令位置の公開資料なし） · `00935e0c`（命令位置の公開資料なし） · `00935e1c`（命令位置の公開資料なし）

~~~diff
- 00935d54 ["INT_ADD", "register:40f0:8", ["const:935d54:8", "const:4:8"]]
- 00935d54 ["CALL", null, ["callee:00c53d70:8"]]
+ 00935da8 ["INT_ADD", "register:40f0:8", ["const:935da8:8", "const:4:8"]]
+ 00935da8 ["CALL", null, ["callee:00c53d70:8"]]
- 00935d54 bytes df770c94
+ 00935da8 bytes f2770c94
- 00935db8 ["INT_ADD", "register:40f0:8", ["const:935db8:8", "const:4:8"]]
- 00935db8 ["CALL", null, ["callee:00732120:8"]]
+ 00935e0c ["INT_ADD", "register:40f0:8", ["const:935e0c:8", "const:4:8"]]
+ 00935e0c ["CALL", null, ["callee:00732120:8"]]
- 00935db8 bytes c4f0f797
+ 00935e0c bytes c5f0f797
- 00935dc8 ["INT_ADD", "register:40f0:8", ["const:935dc8:8", "const:4:8"]]
- 00935dc8 ["CALL", null, ["callee:00c53da0:8"]]
+ 00935e1c ["INT_ADD", "register:40f0:8", ["const:935e1c:8", "const:4:8"]]
+ 00935e1c ["CALL", null, ["callee:00c53da0:8"]]
- 00935dc8 bytes ce770c94
+ 00935e1c bytes e1770c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd64dd0ae83af4cf3a6767835210c147"></a>

### [`00935e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935e3c.md) → [`00935e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00935/00935e90.md) FUN_00935e90

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009b88d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b88d8.md) · 呼出先 2件 [`0057c654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c654.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`009b892c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b8/009b892c.md) · 呼出先 2件 [`0057c694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c694.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00935e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935e3c.md#insn-00935e78) · [`00935ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935e3c.md#insn-00935ea4) · [`00935eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935e3c.md#insn-00935eb4)
- 新版 `00935ecc`（命令位置の公開資料なし） · `00935ef8`（命令位置の公開資料なし） · `00935f08`（命令位置の公開資料なし）

~~~diff
- 00935e78 ["COPY", "register:0:8", ["register:4048:8"]]
- 00935e78 ["INT_ADD", "register:40f0:8", ["const:935e78:8", "const:4:8"]]
- 00935e78 ["CALLIND", null, ["register:0:8"]]
+ 00935ecc ["COPY", "register:0:8", ["register:4048:8"]]
+ 00935ecc ["INT_ADD", "register:40f0:8", ["const:935ecc:8", "const:4:8"]]
+ 00935ecc ["CALLIND", null, ["register:0:8"]]
- 00935e78 bytes 20013fd6
+ 00935ecc bytes 20013fd6
- 00935ea4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00935ea4 ["INT_ADD", "register:40f0:8", ["const:935ea4:8", "const:4:8"]]
- 00935ea4 ["CALLIND", null, ["register:0:8"]]
+ 00935ef8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00935ef8 ["INT_ADD", "register:40f0:8", ["const:935ef8:8", "const:4:8"]]
+ 00935ef8 ["CALLIND", null, ["register:0:8"]]
- 00935ea4 bytes 00013fd6
+ 00935ef8 bytes 00013fd6
- 00935eb4 ["INT_ADD", "register:40f0:8", ["const:935eb4:8", "const:4:8"]]
- 00935eb4 ["CALL", null, ["callee:0057c694:8"]]
+ 00935f08 ["INT_ADD", "register:40f0:8", ["const:935f08:8", "const:4:8"]]
+ 00935f08 ["CALL", null, ["callee:0057c694:8"]]
- 00935eb4 bytes e819f197
+ 00935f08 bytes e319f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-baadf55aa535feb54a7ff60e31c619e0"></a>

### [`00937fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00937/00937fe4.md) → [`00938038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00938/00938038.md) FUN_00938038

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 2件 [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md) [`00480be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md)
- 新版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 2件 [`00480bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480bd0.md) [`00480c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480c28.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0093800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00937/00937fe4.md#insn-0093800c) · [`00938048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00937/00937fe4.md#insn-00938048) · [`0093805c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00937/00937fe4.md#insn-0093805c)
- 新版 `00938060`（命令位置の公開資料なし） · `0093809c`（命令位置の公開資料なし） · `009380b0`（命令位置の公開資料なし）

~~~diff
- 0093800c ["INT_ADD", "register:40f0:8", ["const:93800c:8", "const:4:8"]]
- 0093800c ["CALL", null, ["callee:00480bd0:8"]]
+ 00938060 ["INT_ADD", "register:40f0:8", ["const:938060:8", "const:4:8"]]
+ 00938060 ["CALL", null, ["callee:00480bd0:8"]]
- 0093800c bytes e122ed97
+ 00938060 bytes dc22ed97
- 00938048 ["INT_ADD", "register:40f0:8", ["const:938048:8", "const:4:8"]]
- 00938048 ["CALL", null, ["callee:00480c28:8"]]
+ 0093809c ["INT_ADD", "register:40f0:8", ["const:93809c:8", "const:4:8"]]
+ 0093809c ["CALL", null, ["callee:00480c28:8"]]
- 00938048 bytes e822ed97
+ 0093809c bytes e322ed97
- 0093805c ["INT_ADD", "register:40f0:8", ["const:93805c:8", "const:4:8"]]
- 0093805c ["CALL", null, ["callee:00480bd0:8"]]
+ 009380b0 ["INT_ADD", "register:40f0:8", ["const:9380b0:8", "const:4:8"]]
+ 009380b0 ["CALL", null, ["callee:00480bd0:8"]]
- 0093805c bytes cd22ed97
+ 009380b0 bytes c822ed97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1e04a717906ec122e4881a397a69725"></a>

### [`00938500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00938/00938500.md) → [`00938554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00938/00938554.md) FUN_00938554

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009380b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00938/009380b0.md) [`00938774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00938/00938774.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)
- 新版 呼出元 2件 [`00938104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00938/00938104.md) [`009387c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00938/009387c8.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009385a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00938/00938500.md#insn-009385a0) · [`009385dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00938/00938500.md#insn-009385dc) · [`00938644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00938/00938500.md#insn-00938644)
- 新版 `009385f4`（命令位置の公開資料なし） · `00938630`（命令位置の公開資料なし） · `00938698`（命令位置の公開資料なし）

~~~diff
- 009385a0 ["INT_ADD", "register:40f0:8", ["const:9385a0:8", "const:4:8"]]
- 009385a0 ["CALL", null, ["callee:00c57f60:8"]]
+ 009385f4 ["INT_ADD", "register:40f0:8", ["const:9385f4:8", "const:4:8"]]
+ 009385f4 ["CALL", null, ["callee:00c57f60:8"]]
- 009385a0 bytes 3c7e0c94
+ 009385f4 bytes 5b7e0c94
- 009385dc ["INT_ADD", "register:40f0:8", ["const:9385dc:8", "const:4:8"]]
- 009385dc ["CALL", null, ["callee:0043bbe4:8"]]
+ 00938630 ["INT_ADD", "register:40f0:8", ["const:938630:8", "const:4:8"]]
+ 00938630 ["CALL", null, ["callee:0043bbe4:8"]]
- 009385dc bytes 720dec97
+ 00938630 bytes 6d0dec97
- 00938644 ["INT_ADD", "register:40f0:8", ["const:938644:8", "const:4:8"]]
- 00938644 ["CALL", null, ["callee:00c57f60:8"]]
+ 00938698 ["INT_ADD", "register:40f0:8", ["const:938698:8", "const:4:8"]]
+ 00938698 ["CALL", null, ["callee:00c57f60:8"]]
- 00938644 bytes 137e0c94
+ 00938698 bytes 327e0c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6c6316e1131f9e037ce023e871b3d7a"></a>

### [`0093a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093a178.md) → [`0093a1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093a/0093a1cc.md) FUN_0093a1cc

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0093a194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093a178.md#insn-0093a194)
- 新版 `0093a1e8`（命令位置の公開資料なし）

~~~diff
- 0093a194 ["INT_ADD", "register:40f0:8", ["const:93a194:8", "const:4:8"]]
- 0093a194 ["CALL", null, ["callee:00c57f80:8"]]
+ 0093a1e8 ["INT_ADD", "register:40f0:8", ["const:93a1e8:8", "const:4:8"]]
+ 0093a1e8 ["CALL", null, ["callee:00c57f80:8"]]
- 0093a194 bytes 47770c94
+ 0093a1e8 bytes 66770c94
~~~


<a id="compare-43d2f0ee85a15c870b6dab8f5699d43c"></a>

### [`0093a1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093a1bc.md) → [`0093a210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093a/0093a210.md) FUN_0093a210

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) · 呼出先 2件 [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md)
- 新版 呼出元 1件 [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) · 呼出先 2件 [`005c3ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3ebc.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0093a1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093a1bc.md#insn-0093a1d8) · [`0093a1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093a1bc.md#insn-0093a1f0)
- 新版 `0093a22c`（命令位置の公開資料なし） · `0093a244`（命令位置の公開資料なし）

~~~diff
- 0093a1d8 ["INT_ADD", "register:40f0:8", ["const:93a1d8:8", "const:4:8"]]
- 0093a1d8 ["CALL", null, ["callee:005c3ebc:8"]]
+ 0093a22c ["INT_ADD", "register:40f0:8", ["const:93a22c:8", "const:4:8"]]
+ 0093a22c ["CALL", null, ["callee:005c3ebc:8"]]
- 0093a1d8 bytes 2927f297
+ 0093a22c bytes 2427f297
- 0093a1f0 ["INT_ADD", "register:40f0:8", ["const:93a1f0:8", "const:4:8"]]
- 0093a1f0 ["CALL", null, ["callee:00676aa0:8"]]
+ 0093a244 ["INT_ADD", "register:40f0:8", ["const:93a244:8", "const:4:8"]]
+ 0093a244 ["CALL", null, ["callee:00676aa0:8"]]
- 0093a1f0 bytes 1cf2f497
+ 0093a244 bytes 17f2f497
~~~


<a id="compare-da8e3024789d0b9a9d1ab0a793fd3dee"></a>

### [`0093a208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093a208.md) → [`0093a25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093a/0093a25c.md) FUN_0093a25c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 9件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`004801d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004801d8.md) [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md)
- 新版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 9件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00480218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480218.md) [`005c3ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3ebc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0093a240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093a208.md#insn-0093a240) · [`0093a250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093a208.md#insn-0093a250) · [`0093a284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093a208.md#insn-0093a284)
- 新版 `0093a294`（命令位置の公開資料なし） · `0093a2a4`（命令位置の公開資料なし） · `0093a2d8`（命令位置の公開資料なし）

~~~diff
- 0093a240 ["INT_ADD", "register:40f0:8", ["const:93a240:8", "const:4:8"]]
- 0093a240 ["CALL", null, ["callee:005c3ebc:8"]]
+ 0093a294 ["INT_ADD", "register:40f0:8", ["const:93a294:8", "const:4:8"]]
+ 0093a294 ["CALL", null, ["callee:005c3ebc:8"]]
- 0093a240 bytes 0f27f297
+ 0093a294 bytes 0a27f297
- 0093a250 ["INT_ADD", "register:40f0:8", ["const:93a250:8", "const:4:8"]]
- 0093a250 ["CALL", null, ["callee:00480218:8"]]
+ 0093a2a4 ["INT_ADD", "register:40f0:8", ["const:93a2a4:8", "const:4:8"]]
+ 0093a2a4 ["CALL", null, ["callee:00480218:8"]]
- 0093a250 bytes e217ed97
+ 0093a2a4 bytes dd17ed97
- 0093a284 ["INT_ADD", "register:40f0:8", ["const:93a284:8", "const:4:8"]]
- 0093a284 ["CALL", null, ["callee:00480218:8"]]
+ 0093a2d8 ["INT_ADD", "register:40f0:8", ["const:93a2d8:8", "const:4:8"]]
+ 0093a2d8 ["CALL", null, ["callee:00480218:8"]]
- 0093a284 bytes d517ed97
+ 0093a2d8 bytes d017ed97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-509c8b0d791038ae7f060a5a39c295ad"></a>

### [`0093a540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093a540.md) → [`0093a594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093a/0093a594.md) FUN_0093a594

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 6件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00480be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 6件 [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00480c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480c28.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0093a584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093a540.md#insn-0093a584) · [`0093a5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093a540.md#insn-0093a5d0) · [`0093a5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093a540.md#insn-0093a5e4)
- 新版 `0093a5d8`（命令位置の公開資料なし） · `0093a624`（命令位置の公開資料なし） · `0093a638`（命令位置の公開資料なし）

~~~diff
- 0093a584 ["INT_ADD", "register:40f0:8", ["const:93a584:8", "const:4:8"]]
- 0093a584 ["CALL", null, ["callee:00480c28:8"]]
+ 0093a5d8 ["INT_ADD", "register:40f0:8", ["const:93a5d8:8", "const:4:8"]]
+ 0093a5d8 ["CALL", null, ["callee:00480c28:8"]]
- 0093a584 bytes 9919ed97
+ 0093a5d8 bytes 9419ed97
- 0093a5d0 ["INT_ADD", "register:40f0:8", ["const:93a5d0:8", "const:4:8"]]
- 0093a5d0 ["CALL", null, ["callee:00c57f60:8"]]
+ 0093a624 ["INT_ADD", "register:40f0:8", ["const:93a624:8", "const:4:8"]]
+ 0093a624 ["CALL", null, ["callee:00c57f60:8"]]
- 0093a5d0 bytes 30760c94
+ 0093a624 bytes 4f760c94
- 0093a5e4 ["INT_ADD", "register:40f0:8", ["const:93a5e4:8", "const:4:8"]]
- 0093a5e4 ["CALL", null, ["callee:00c580d0:8"]]
+ 0093a638 ["INT_ADD", "register:40f0:8", ["const:93a638:8", "const:4:8"]]
+ 0093a638 ["CALL", null, ["callee:00c580d0:8"]]
- 0093a5e4 bytes 87760c94
+ 0093a638 bytes a6760c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf7acc20c5e32a5b136a9e801c40ee24"></a>

### [`0093a7d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093a7d8.md) → [`0093a82c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093a/0093a82c.md) FUN_0093a82c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00605294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00605/00605294.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0093a870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093a7d8.md#insn-0093a870) · [`0093a8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093a7d8.md#insn-0093a8b0)
- 新版 `0093a8c4`（命令位置の公開資料なし） · `0093a904`（命令位置の公開資料なし）

~~~diff
- 0093a870 ["INT_ADD", "register:40f0:8", ["const:93a870:8", "const:4:8"]]
- 0093a870 ["CALL", null, ["callee:00c57f60:8"]]
+ 0093a8c4 ["INT_ADD", "register:40f0:8", ["const:93a8c4:8", "const:4:8"]]
+ 0093a8c4 ["CALL", null, ["callee:00c57f60:8"]]
- 0093a870 bytes 88750c94
+ 0093a8c4 bytes a7750c94
- 0093a8b0 ["INT_ADD", "register:40f0:8", ["const:93a8b0:8", "const:4:8"]]
- 0093a8b0 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0093a904 ["INT_ADD", "register:40f0:8", ["const:93a904:8", "const:4:8"]]
+ 0093a904 ["CALL", null, ["callee:0043bbe4:8"]]
- 0093a8b0 bytes bd04ec97
+ 0093a904 bytes b804ec97
~~~


<a id="compare-668b6d7c63f977bcd826191b70844baa"></a>

### [`0093a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093a8e0.md) → [`0093a934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093a/0093a934.md) FUN_0093a934

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`0061452c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00614/0061452c.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`0061456c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00614/0061456c.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0093a958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093a8e0.md#insn-0093a958) · [`0093a9cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093a8e0.md#insn-0093a9cc) · [`0093aa0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093a8e0.md#insn-0093aa0c)
- 新版 `0093a9ac`（命令位置の公開資料なし） · `0093aa20`（命令位置の公開資料なし） · `0093aa60`（命令位置の公開資料なし）

~~~diff
- 0093a958 ["INT_ADD", "register:40f0:8", ["const:93a958:8", "const:4:8"]]
- 0093a958 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0093a9ac ["INT_ADD", "register:40f0:8", ["const:93a9ac:8", "const:4:8"]]
+ 0093a9ac ["CALL", null, ["callee:0043bbe4:8"]]
- 0093a958 bytes 9304ec97
+ 0093a9ac bytes 8e04ec97
- 0093a9cc ["INT_ADD", "register:40f0:8", ["const:93a9cc:8", "const:4:8"]]
- 0093a9cc ["CALL", null, ["callee:00c57f60:8"]]
+ 0093aa20 ["INT_ADD", "register:40f0:8", ["const:93aa20:8", "const:4:8"]]
+ 0093aa20 ["CALL", null, ["callee:00c57f60:8"]]
- 0093a9cc bytes 31750c94
+ 0093aa20 bytes 50750c94
- 0093aa0c ["INT_ADD", "register:40f0:8", ["const:93aa0c:8", "const:4:8"]]
- 0093aa0c ["CALL", null, ["callee:0043bbe4:8"]]
+ 0093aa60 ["INT_ADD", "register:40f0:8", ["const:93aa60:8", "const:4:8"]]
+ 0093aa60 ["CALL", null, ["callee:0043bbe4:8"]]
- 0093aa0c bytes 6604ec97
+ 0093aa60 bytes 6104ec97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91ea6a0d823142690a0e6775f3d2d4ac"></a>

### [`0093ab84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093ab84.md) → [`0093abd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093a/0093abd8.md) FUN_0093abd8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)
- 新版 呼出元 3件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00605294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00605/00605294.md) [`0093b7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093b/0093b7c4.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0093ac24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093ab84.md#insn-0093ac24) · [`0093ac60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093ab84.md#insn-0093ac60) · [`0093acc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093ab84.md#insn-0093acc8)
- 新版 `0093ac78`（命令位置の公開資料なし） · `0093acb4`（命令位置の公開資料なし） · `0093ad1c`（命令位置の公開資料なし）

~~~diff
- 0093ac24 ["INT_ADD", "register:40f0:8", ["const:93ac24:8", "const:4:8"]]
- 0093ac24 ["CALL", null, ["callee:00c57f60:8"]]
+ 0093ac78 ["INT_ADD", "register:40f0:8", ["const:93ac78:8", "const:4:8"]]
+ 0093ac78 ["CALL", null, ["callee:00c57f60:8"]]
- 0093ac24 bytes 9b740c94
+ 0093ac78 bytes ba740c94
- 0093ac60 ["INT_ADD", "register:40f0:8", ["const:93ac60:8", "const:4:8"]]
- 0093ac60 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0093acb4 ["INT_ADD", "register:40f0:8", ["const:93acb4:8", "const:4:8"]]
+ 0093acb4 ["CALL", null, ["callee:0043bbe4:8"]]
- 0093ac60 bytes d103ec97
+ 0093acb4 bytes cc03ec97
- 0093acc8 ["INT_ADD", "register:40f0:8", ["const:93acc8:8", "const:4:8"]]
- 0093acc8 ["CALL", null, ["callee:00c57f60:8"]]
+ 0093ad1c ["INT_ADD", "register:40f0:8", ["const:93ad1c:8", "const:4:8"]]
+ 0093ad1c ["CALL", null, ["callee:00c57f60:8"]]
- 0093acc8 bytes 72740c94
+ 0093ad1c bytes 91740c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83033be1400549f73c4aba5cccdccf4d"></a>

### [`0093adf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093adf0.md) → [`0093ae44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093a/0093ae44.md) FUN_0093ae44

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) · 呼出先 8件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00605294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00605/00605294.md) · 呼出先 8件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0093ae6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093adf0.md#insn-0093ae6c) · [`0093aea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093adf0.md#insn-0093aea8) · [`0093af00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093a/0093adf0.md#insn-0093af00)
- 新版 `0093aec0`（命令位置の公開資料なし） · `0093aefc`（命令位置の公開資料なし） · `0093af54`（命令位置の公開資料なし）

~~~diff
- 0093ae6c ["INT_ADD", "register:40f0:8", ["const:93ae6c:8", "const:4:8"]]
- 0093ae6c ["CALL", null, ["callee:00c57f60:8"]]
+ 0093aec0 ["INT_ADD", "register:40f0:8", ["const:93aec0:8", "const:4:8"]]
+ 0093aec0 ["CALL", null, ["callee:00c57f60:8"]]
- 0093ae6c bytes 09740c94
+ 0093aec0 bytes 28740c94
- 0093aea8 ["INT_ADD", "register:40f0:8", ["const:93aea8:8", "const:4:8"]]
- 0093aea8 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0093aefc ["INT_ADD", "register:40f0:8", ["const:93aefc:8", "const:4:8"]]
+ 0093aefc ["CALL", null, ["callee:0043bbe4:8"]]
- 0093aea8 bytes 3f03ec97
+ 0093aefc bytes 3a03ec97
- 0093af00 ["INT_ADD", "register:40f0:8", ["const:93af00:8", "const:4:8"]]
- 0093af00 ["CALL", null, ["callee:00c57f60:8"]]
+ 0093af54 ["INT_ADD", "register:40f0:8", ["const:93af54:8", "const:4:8"]]
+ 0093af54 ["CALL", null, ["callee:00c57f60:8"]]
- 0093af00 bytes e4730c94
+ 0093af54 bytes 03740c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c4ef4fe0e6878f0449770748295bda5"></a>

### [`0093b460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b460.md) → [`0093b4b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093b/0093b4b4.md) FUN_0093b4b4

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 6件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00719738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00719/00719738.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00a694b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a694b0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`009d0374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d0/009d0374.md) · 呼出先 6件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`00719790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/00719790.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00a69520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a69/00a69520.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0093b4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b460.md#insn-0093b4d0) · [`0093b564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b460.md#insn-0093b564) · [`0093b56c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b460.md#insn-0093b56c)
- 新版 `0093b524`（命令位置の公開資料なし） · `0093b5b8`（命令位置の公開資料なし） · `0093b5c0`（命令位置の公開資料なし）

~~~diff
- 0093b4d0 ["INT_ADD", "register:40f0:8", ["const:93b4d0:8", "const:4:8"]]
- 0093b4d0 ["CALL", null, ["callee:00719790:8"]]
+ 0093b524 ["INT_ADD", "register:40f0:8", ["const:93b524:8", "const:4:8"]]
+ 0093b524 ["CALL", null, ["callee:00719790:8"]]
- 0093b4d0 bytes 9a78f797
+ 0093b524 bytes 9b78f797
- 0093b564 ["INT_ADD", "register:40f0:8", ["const:93b564:8", "const:4:8"]]
- 0093b564 ["CALL", null, ["callee:00494650:8"]]
+ 0093b5b8 ["INT_ADD", "register:40f0:8", ["const:93b5b8:8", "const:4:8"]]
+ 0093b5b8 ["CALL", null, ["callee:00494650:8"]]
- 0093b564 bytes 2b64ed97
+ 0093b5b8 bytes 2664ed97
- 0093b56c ["INT_ADD", "register:40f0:8", ["const:93b56c:8", "const:4:8"]]
- 0093b56c ["CALL", null, ["callee:00c57f80:8"]]
+ 0093b5c0 ["INT_ADD", "register:40f0:8", ["const:93b5c0:8", "const:4:8"]]
+ 0093b5c0 ["CALL", null, ["callee:00c57f80:8"]]
- 0093b56c bytes 51720c94
+ 0093b5c0 bytes 70720c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb99b49706990ad2035cb7f77b17e0ad"></a>

### [`0093b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b5e0.md) → [`0093b634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093b/0093b634.md) FUN_0093b634

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0093b644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b5e0.md#insn-0093b644) · [`0093b67c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b5e0.md#insn-0093b67c)
- 新版 `0093b698`（命令位置の公開資料なし） · `0093b6d0`（命令位置の公開資料なし）

~~~diff
- 0093b644 ["INT_ADD", "register:40f0:8", ["const:93b644:8", "const:4:8"]]
- 0093b644 ["CALL", null, ["callee:00c57f60:8"]]
+ 0093b698 ["INT_ADD", "register:40f0:8", ["const:93b698:8", "const:4:8"]]
+ 0093b698 ["CALL", null, ["callee:00c57f60:8"]]
- 0093b644 bytes 13720c94
+ 0093b698 bytes 32720c94
- 0093b67c ["INT_ADD", "register:40f0:8", ["const:93b67c:8", "const:4:8"]]
- 0093b67c ["CALL", null, ["callee:0043bbe4:8"]]
+ 0093b6d0 ["INT_ADD", "register:40f0:8", ["const:93b6d0:8", "const:4:8"]]
+ 0093b6d0 ["CALL", null, ["callee:0043bbe4:8"]]
- 0093b67c bytes 4a01ec97
+ 0093b6d0 bytes 4501ec97
~~~


<a id="compare-93bfee2b63477f8a69d75cc7328771c5"></a>

### [`0093b6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b6a4.md) → [`0093b6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093b/0093b6f8.md) FUN_0093b6f8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0093b70c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b6a4.md#insn-0093b70c) · [`0093b744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b6a4.md#insn-0093b744)
- 新版 `0093b760`（命令位置の公開資料なし） · `0093b798`（命令位置の公開資料なし）

~~~diff
- 0093b70c ["INT_ADD", "register:40f0:8", ["const:93b70c:8", "const:4:8"]]
- 0093b70c ["CALL", null, ["callee:00c57f60:8"]]
+ 0093b760 ["INT_ADD", "register:40f0:8", ["const:93b760:8", "const:4:8"]]
+ 0093b760 ["CALL", null, ["callee:00c57f60:8"]]
- 0093b70c bytes e1710c94
+ 0093b760 bytes 00720c94
- 0093b744 ["INT_ADD", "register:40f0:8", ["const:93b744:8", "const:4:8"]]
- 0093b744 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0093b798 ["INT_ADD", "register:40f0:8", ["const:93b798:8", "const:4:8"]]
+ 0093b798 ["CALL", null, ["callee:0043bbe4:8"]]
- 0093b744 bytes 1801ec97
+ 0093b798 bytes 1301ec97
~~~


<a id="compare-4ea0b1a6a6fbe304ef3ba8c66312094f"></a>

### [`0093ee40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093e/0093ee40.md) → [`0093ee94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093e/0093ee94.md) FUN_0093ee94

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) [`00ab4d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab4/00ab4d00.md) · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 2件 [`0093b7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093b/0093b7c4.md) [`00ab4d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ab4/00ab4d70.md) · 呼出先 5件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0093ee64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093e/0093ee40.md#insn-0093ee64) · [`0093eeac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093e/0093ee40.md#insn-0093eeac) · [`0093eecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093e/0093ee40.md#insn-0093eecc)
- 新版 `0093eeb8`（命令位置の公開資料なし） · `0093ef00`（命令位置の公開資料なし） · `0093ef20`（命令位置の公開資料なし）

~~~diff
- 0093ee64 ["INT_ADD", "register:40f0:8", ["const:93ee64:8", "const:4:8"]]
- 0093ee64 ["CALL", null, ["callee:00c580b0:8"]]
+ 0093eeb8 ["INT_ADD", "register:40f0:8", ["const:93eeb8:8", "const:4:8"]]
+ 0093eeb8 ["CALL", null, ["callee:00c580b0:8"]]
- 0093ee64 bytes 5f640c94
+ 0093eeb8 bytes 7e640c94
- 0093eeac ["INT_ADD", "register:40f0:8", ["const:93eeac:8", "const:4:8"]]
- 0093eeac ["CALL", null, ["callee:00c57f60:8"]]
+ 0093ef00 ["INT_ADD", "register:40f0:8", ["const:93ef00:8", "const:4:8"]]
+ 0093ef00 ["CALL", null, ["callee:00c57f60:8"]]
- 0093eeac bytes f9630c94
+ 0093ef00 bytes 18640c94
- 0093eecc ["INT_ADD", "register:40f0:8", ["const:93eecc:8", "const:4:8"]]
- 0093eecc ["CALL", null, ["callee:00c58010:8"]]
+ 0093ef20 ["INT_ADD", "register:40f0:8", ["const:93ef20:8", "const:4:8"]]
+ 0093ef20 ["CALL", null, ["callee:00c58010:8"]]
- 0093eecc bytes 1d640c94
+ 0093ef20 bytes 3c640c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9551df7adb20c16f46bb0c682841f937"></a>

### [`0093ef34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093e/0093ef34.md) → [`0093ef88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093e/0093ef88.md) FUN_0093ef88

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0093b7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093b/0093b7c4.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0093efac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093e/0093ef34.md#insn-0093efac) · [`0093efbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093e/0093ef34.md#insn-0093efbc) · [`0093efd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093e/0093ef34.md#insn-0093efd0)
- 新版 `0093f000`（命令位置の公開資料なし） · `0093f010`（命令位置の公開資料なし） · `0093f024`（命令位置の公開資料なし）

~~~diff
- 0093efac ["INT_ADD", "register:40f0:8", ["const:93efac:8", "const:4:8"]]
- 0093efac ["CALL", null, ["callee:00c57f80:8"]]
+ 0093f000 ["INT_ADD", "register:40f0:8", ["const:93f000:8", "const:4:8"]]
+ 0093f000 ["CALL", null, ["callee:00c57f80:8"]]
- 0093efac bytes c1630c94
+ 0093f000 bytes e0630c94
- 0093efbc ["INT_ADD", "register:40f0:8", ["const:93efbc:8", "const:4:8"]]
- 0093efbc ["CALL", null, ["callee:00c57f80:8"]]
+ 0093f010 ["INT_ADD", "register:40f0:8", ["const:93f010:8", "const:4:8"]]
+ 0093f010 ["CALL", null, ["callee:00c57f80:8"]]
- 0093efbc bytes bd630c94
+ 0093f010 bytes dc630c94
- 0093efd0 ["INT_ADD", "register:40f0:8", ["const:93efd0:8", "const:4:8"]]
- 0093efd0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0093f024 ["INT_ADD", "register:40f0:8", ["const:93f024:8", "const:4:8"]]
+ 0093f024 ["CALL", null, ["callee:00c57f80:8"]]
- 0093efd0 bytes b8630c94
+ 0093f024 bytes d7630c94
~~~


<a id="compare-70507a09fb83229af44c395671bf5be2"></a>

### [`0093f01c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f01c.md) → [`0093f070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093f/0093f070.md) FUN_0093f070

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0093f064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f01c.md#insn-0093f064)
- 新版 `0093f0b8`（命令位置の公開資料なし）

~~~diff
- 0093f064 ["INT_ADD", "register:40f0:8", ["const:93f064:8", "const:4:8"]]
- 0093f064 ["CALL", null, ["callee:00c57f80:8"]]
+ 0093f0b8 ["INT_ADD", "register:40f0:8", ["const:93f0b8:8", "const:4:8"]]
+ 0093f0b8 ["CALL", null, ["callee:00c57f80:8"]]
- 0093f064 bytes 93630c94
+ 0093f0b8 bytes b2630c94
~~~


<a id="compare-a6c4b141cc3d1d6bc68b942fd9e19305"></a>

### [`0093f094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f094.md) → [`0093f0e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093f/0093f0e8.md) FUN_0093f0e8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0093b7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093b/0093b7c4.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0093f0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f094.md#insn-0093f0e0) · [`0093f0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f094.md#insn-0093f0f0) · [`0093f100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f094.md#insn-0093f100)
- 新版 `0093f134`（命令位置の公開資料なし） · `0093f144`（命令位置の公開資料なし） · `0093f154`（命令位置の公開資料なし）

~~~diff
- 0093f0e0 ["INT_ADD", "register:40f0:8", ["const:93f0e0:8", "const:4:8"]]
- 0093f0e0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0093f134 ["INT_ADD", "register:40f0:8", ["const:93f134:8", "const:4:8"]]
+ 0093f134 ["CALL", null, ["callee:00c57f80:8"]]
- 0093f0e0 bytes 74630c94
+ 0093f134 bytes 93630c94
- 0093f0f0 ["INT_ADD", "register:40f0:8", ["const:93f0f0:8", "const:4:8"]]
- 0093f0f0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0093f144 ["INT_ADD", "register:40f0:8", ["const:93f144:8", "const:4:8"]]
+ 0093f144 ["CALL", null, ["callee:00c57f80:8"]]
- 0093f0f0 bytes 70630c94
+ 0093f144 bytes 8f630c94
- 0093f100 ["INT_ADD", "register:40f0:8", ["const:93f100:8", "const:4:8"]]
- 0093f100 ["CALL", null, ["callee:00c57f80:8"]]
+ 0093f154 ["INT_ADD", "register:40f0:8", ["const:93f154:8", "const:4:8"]]
+ 0093f154 ["CALL", null, ["callee:00c57f80:8"]]
- 0093f100 bytes 6c630c94
+ 0093f154 bytes 8b630c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8675cb16fef6eafde49e0e29c268acc8"></a>

### [`0093f1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f1d8.md) → [`0093f22c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093f/0093f22c.md) FUN_0093f22c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009390b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00939/009390b4.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0093f3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f3b0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00939108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00939/00939108.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0093f404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093f/0093f404.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0093f278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f1d8.md#insn-0093f278) · [`0093f35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f1d8.md#insn-0093f35c) · [`0093f36c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f1d8.md#insn-0093f36c)
- 新版 `0093f2cc`（命令位置の公開資料なし） · `0093f3b0`（命令位置の公開資料なし） · `0093f3c0`（命令位置の公開資料なし）

~~~diff
- 0093f278 ["INT_ADD", "register:40f0:8", ["const:93f278:8", "const:4:8"]]
- 0093f278 ["CALL", null, ["callee:00c57f60:8"]]
+ 0093f2cc ["INT_ADD", "register:40f0:8", ["const:93f2cc:8", "const:4:8"]]
+ 0093f2cc ["CALL", null, ["callee:00c57f60:8"]]
- 0093f278 bytes 06630c94
+ 0093f2cc bytes 25630c94
- 0093f35c ["INT_ADD", "register:40f0:8", ["const:93f35c:8", "const:4:8"]]
- 0093f35c ["CALL", null, ["callee:00c57f80:8"]]
+ 0093f3b0 ["INT_ADD", "register:40f0:8", ["const:93f3b0:8", "const:4:8"]]
+ 0093f3b0 ["CALL", null, ["callee:00c57f80:8"]]
- 0093f35c bytes d5620c94
+ 0093f3b0 bytes f4620c94
- 0093f36c ["INT_ADD", "register:40f0:8", ["const:93f36c:8", "const:4:8"]]
- 0093f36c ["CALL", null, ["callee:00c57f80:8"]]
+ 0093f3c0 ["INT_ADD", "register:40f0:8", ["const:93f3c0:8", "const:4:8"]]
+ 0093f3c0 ["CALL", null, ["callee:00c57f80:8"]]
- 0093f36c bytes d1620c94
+ 0093f3c0 bytes f0620c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7290667d65f808c0b2b95e5bec9f8a6a"></a>

### [`00943998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00943/00943998.md) → [`009439ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00943/009439ec.md) FUN_009439ec

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 1件 [`0093f3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f3c4.md) · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0094270c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/0094270c.md) [`0094288c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/0094288c.md) [`00942f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/00942f94.md) [`00944178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/00944178.md)
- 新版 呼出元 1件 [`0093f418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093f/0093f418.md) · 呼出先 7件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00942760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00942/00942760.md) [`009428e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00942/009428e0.md) [`00942fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00942/00942fe8.md) [`009441cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00944/009441cc.md)

変更の種類 constant, local_def_use, operands_and_dependencies, store_value

命令の説明率　旧版 99.78% / 新版 99.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00943fc8",
      "incomplete_value": true,
      "site": "00943fc8",
      "value": [
        "live",
        "register:4048:8"
      ]
    },
    "old": {
      "definition_site": "00943f74",
      "incomplete_value": true,
      "site": "00943f74",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:4048:8"
              ],
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 80,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00943a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00943/00943998.md#insn-00943a28) · [`00943a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00943/00943998.md#insn-00943a84) · [`00943aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00943/00943998.md#insn-00943aa4)
- 新版 `00943a7c`（命令位置の公開資料なし） · `00943ad8`（命令位置の公開資料なし） · `00943af8`（命令位置の公開資料なし）

~~~diff
- 00943a28 ["INT_ADD", "register:40f0:8", ["const:943a28:8", "const:4:8"]]
- 00943a28 ["CALL", null, ["callee:009428e0:8"]]
+ 00943a7c ["INT_ADD", "register:40f0:8", ["const:943a7c:8", "const:4:8"]]
+ 00943a7c ["CALL", null, ["callee:009428e0:8"]]
- 00943a28 bytes 99fbff97
+ 00943a7c bytes 99fbff97
- 00943a84 ["INT_ADD", "register:40f0:8", ["const:943a84:8", "const:4:8"]]
- 00943a84 ["CALL", null, ["callee:00942fe8:8"]]
+ 00943ad8 ["INT_ADD", "register:40f0:8", ["const:943ad8:8", "const:4:8"]]
+ 00943ad8 ["CALL", null, ["callee:00942fe8:8"]]
- 00943a84 bytes 44fdff97
+ 00943ad8 bytes 44fdff97
- 00943aa4 ["INT_ADD", "register:40f0:8", ["const:943aa4:8", "const:4:8"]]
- 00943aa4 ["CALL", null, ["callee:00942fe8:8"]]
+ 00943af8 ["INT_ADD", "register:40f0:8", ["const:943af8:8", "const:4:8"]]
+ 00943af8 ["CALL", null, ["callee:00942fe8:8"]]
- 00943aa4 bytes 3cfdff97
+ 00943af8 bytes 3cfdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6fcbc19a6d9d166eb30c998719339be"></a>

### [`00944178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/00944178.md) → [`009441cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00944/009441cc.md) FUN_009441cc

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0093f3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f3c4.md) [`0094288c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/0094288c.md) [`00943998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00943/00943998.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0094270c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/0094270c.md) [`00942f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/00942f94.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 3件 [`0093f418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093f/0093f418.md) [`009428e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00942/009428e0.md) [`009439ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00943/009439ec.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00942760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00942/00942760.md) [`00942fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00942/00942fe8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009441b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/00944178.md#insn-009441b0) · [`009441f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/00944178.md#insn-009441f0) · [`00944220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/00944178.md#insn-00944220)
- 新版 `00944204`（命令位置の公開資料なし） · `00944244`（命令位置の公開資料なし） · `00944274`（命令位置の公開資料なし）

~~~diff
- 009441b0 ["INT_ADD", "register:40f0:8", ["const:9441b0:8", "const:4:8"]]
- 009441b0 ["CALL", null, ["callee:00942fe8:8"]]
+ 00944204 ["INT_ADD", "register:40f0:8", ["const:944204:8", "const:4:8"]]
+ 00944204 ["CALL", null, ["callee:00942fe8:8"]]
- 009441b0 bytes 79fbff97
+ 00944204 bytes 79fbff97
- 009441f0 ["INT_ADD", "register:40f0:8", ["const:9441f0:8", "const:4:8"]]
- 009441f0 ["CALL", null, ["callee:0043bb60:8"]]
+ 00944244 ["INT_ADD", "register:40f0:8", ["const:944244:8", "const:4:8"]]
+ 00944244 ["CALL", null, ["callee:0043bb60:8"]]
- 009441f0 bytes 4cdeeb97
+ 00944244 bytes 47deeb97
- 00944220 ["INT_ADD", "register:40f0:8", ["const:944220:8", "const:4:8"]]
- 00944220 ["CALL", null, ["callee:0043bb60:8"]]
+ 00944274 ["INT_ADD", "register:40f0:8", ["const:944274:8", "const:4:8"]]
+ 00944274 ["CALL", null, ["callee:0043bb60:8"]]
- 00944220 bytes 40deeb97
+ 00944274 bytes 3bdeeb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-417a06735830b9f150549f18cd648845"></a>

### [`009446d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/009446d8.md) → [`0094472c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00944/0094472c.md) FUN_0094472c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0093b7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093b/0093b7c4.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00944744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/009446d8.md#insn-00944744) · [`00944754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/009446d8.md#insn-00944754) · [`00944764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/009446d8.md#insn-00944764)
- 新版 `00944798`（命令位置の公開資料なし） · `009447a8`（命令位置の公開資料なし） · `009447b8`（命令位置の公開資料なし）

~~~diff
- 00944744 ["INT_ADD", "register:40f0:8", ["const:944744:8", "const:4:8"]]
- 00944744 ["CALL", null, ["callee:00c57f80:8"]]
+ 00944798 ["INT_ADD", "register:40f0:8", ["const:944798:8", "const:4:8"]]
+ 00944798 ["CALL", null, ["callee:00c57f80:8"]]
- 00944744 bytes db4d0c94
+ 00944798 bytes fa4d0c94
- 00944754 ["INT_ADD", "register:40f0:8", ["const:944754:8", "const:4:8"]]
- 00944754 ["CALL", null, ["callee:00c57f80:8"]]
+ 009447a8 ["INT_ADD", "register:40f0:8", ["const:9447a8:8", "const:4:8"]]
+ 009447a8 ["CALL", null, ["callee:00c57f80:8"]]
- 00944754 bytes d74d0c94
+ 009447a8 bytes f64d0c94
- 00944764 ["INT_ADD", "register:40f0:8", ["const:944764:8", "const:4:8"]]
- 00944764 ["CALL", null, ["callee:00c57f80:8"]]
+ 009447b8 ["INT_ADD", "register:40f0:8", ["const:9447b8:8", "const:4:8"]]
+ 009447b8 ["CALL", null, ["callee:00c57f80:8"]]
- 00944764 bytes d34d0c94
+ 009447b8 bytes f24d0c94
~~~


<a id="compare-340b52f38920ac5aca3fb309d7dc8549"></a>

### [`00944fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/00944fb4.md) → [`00945008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00945/00945008.md) FUN_00945008

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`0053bcb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bcb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0093b7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093b/0093b7c4.md) · 呼出先 6件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0046d5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d5e8.md) [`0053bcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053bcf0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0094508c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/00944fb4.md#insn-0094508c) · [`009450a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/00944fb4.md#insn-009450a4) · [`009450b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/00944fb4.md#insn-009450b0)
- 新版 `009450e0`（命令位置の公開資料なし） · `009450f8`（命令位置の公開資料なし） · `00945104`（命令位置の公開資料なし）

~~~diff
- 0094508c ["INT_ADD", "register:40f0:8", ["const:94508c:8", "const:4:8"]]
- 0094508c ["CALL", null, ["callee:0046d5e8:8"]]
+ 009450e0 ["INT_ADD", "register:40f0:8", ["const:9450e0:8", "const:4:8"]]
+ 009450e0 ["CALL", null, ["callee:0046d5e8:8"]]
- 0094508c bytes 47a1ec97
+ 009450e0 bytes 42a1ec97
- 009450a4 ["INT_ADD", "register:40f0:8", ["const:9450a4:8", "const:4:8"]]
- 009450a4 ["CALL", null, ["callee:00c58500:8"]]
+ 009450f8 ["INT_ADD", "register:40f0:8", ["const:9450f8:8", "const:4:8"]]
+ 009450f8 ["CALL", null, ["callee:00c58500:8"]]
- 009450a4 bytes e34c0c94
+ 009450f8 bytes 024d0c94
- 009450b0 ["INT_ADD", "register:40f0:8", ["const:9450b0:8", "const:4:8"]]
- 009450b0 ["CALL", null, ["callee:00c58500:8"]]
+ 00945104 ["INT_ADD", "register:40f0:8", ["const:945104:8", "const:4:8"]]
+ 00945104 ["CALL", null, ["callee:00c58500:8"]]
- 009450b0 bytes e04c0c94
+ 00945104 bytes ff4c0c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-299520ae921156f2c666a958a2e1b1cf"></a>

### [`00945288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00945/00945288.md) → [`009452dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00945/009452dc.md) FUN_009452dc

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) [`00945288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00945/00945288.md) · 呼出先 7件 [`00945288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00945/00945288.md) [`00946288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946288.md) [`009465c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/009465c4.md) [`0094691c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/0094691c.md) [`00946c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946c50.md)
- 新版 呼出元 2件 [`0093b7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093b/0093b7c4.md) [`009452dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00945/009452dc.md) · 呼出先 7件 [`009452dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00945/009452dc.md) [`009462dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00946/009462dc.md) [`00946618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00946/00946618.md) [`00946970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00946/00946970.md) [`00946ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00946/00946ca4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00945360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00945/00945288.md#insn-00945360) · [`00945384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00945/00945288.md#insn-00945384) · [`00945394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00945/00945288.md#insn-00945394)
- 新版 `009453b4`（命令位置の公開資料なし） · `009453d8`（命令位置の公開資料なし） · `009453e8`（命令位置の公開資料なし）

~~~diff
- 00945360 ["INT_ADD", "register:40f0:8", ["const:945360:8", "const:4:8"]]
- 00945360 ["CALL", null, ["callee:00946618:8"]]
+ 009453b4 ["INT_ADD", "register:40f0:8", ["const:9453b4:8", "const:4:8"]]
+ 009453b4 ["CALL", null, ["callee:00946618:8"]]
- 00945360 bytes 99040094
+ 009453b4 bytes 99040094
- 00945384 ["INT_ADD", "register:40f0:8", ["const:945384:8", "const:4:8"]]
- 00945384 ["CALL", null, ["callee:00946618:8"]]
+ 009453d8 ["INT_ADD", "register:40f0:8", ["const:9453d8:8", "const:4:8"]]
+ 009453d8 ["CALL", null, ["callee:00946618:8"]]
- 00945384 bytes 90040094
+ 009453d8 bytes 90040094
- 00945394 ["INT_ADD", "register:40f0:8", ["const:945394:8", "const:4:8"]]
- 00945394 ["CALL", null, ["callee:00946618:8"]]
+ 009453e8 ["INT_ADD", "register:40f0:8", ["const:9453e8:8", "const:4:8"]]
+ 009453e8 ["CALL", null, ["callee:00946618:8"]]
- 00945394 bytes 8c040094
+ 009453e8 bytes 8c040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fa8c4be956420e4b06f5370ba4df473"></a>

### [`00946288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946288.md) → [`009462dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00946/009462dc.md) FUN_009462dc

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00945288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00945/00945288.md) [`0094691c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/0094691c.md) · 呼出先 3件 [`00946c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946c50.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`009452dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00945/009452dc.md) [`00946970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00946/00946970.md) · 呼出先 3件 [`00946ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00946/00946ca4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009462c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946288.md#insn-009462c8) · [`0094635c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946288.md#insn-0094635c) · [`0094640c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946288.md#insn-0094640c)
- 新版 `0094631c`（命令位置の公開資料なし） · `009463b0`（命令位置の公開資料なし） · `00946460`（命令位置の公開資料なし）

~~~diff
- 009462c8 ["INT_ADD", "register:40f0:8", ["const:9462c8:8", "const:4:8"]]
- 009462c8 ["CALL", null, ["callee:00946ca4:8"]]
+ 0094631c ["INT_ADD", "register:40f0:8", ["const:94631c:8", "const:4:8"]]
+ 0094631c ["CALL", null, ["callee:00946ca4:8"]]
- 009462c8 bytes 62020094
+ 0094631c bytes 62020094
- 0094635c ["INT_ADD", "register:40f0:8", ["const:94635c:8", "const:4:8"]]
- 0094635c ["CALL", null, ["callee:00c57f80:8"]]
+ 009463b0 ["INT_ADD", "register:40f0:8", ["const:9463b0:8", "const:4:8"]]
+ 009463b0 ["CALL", null, ["callee:00c57f80:8"]]
- 0094635c bytes d5460c94
+ 009463b0 bytes f4460c94
- 0094640c ["INT_ADD", "register:40f0:8", ["const:94640c:8", "const:4:8"]]
- 0094640c ["CALL", null, ["callee:00c57f80:8"]]
+ 00946460 ["INT_ADD", "register:40f0:8", ["const:946460:8", "const:4:8"]]
+ 00946460 ["CALL", null, ["callee:00c57f80:8"]]
- 0094640c bytes a9460c94
+ 00946460 bytes c8460c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50ae24efb18a45a2d217e743b40b62c9"></a>

### [`0094691c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/0094691c.md) → [`00946970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00946/00946970.md) FUN_00946970

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00945288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00945/00945288.md) · 呼出先 5件 [`00946288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946288.md) [`009465c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/009465c4.md) [`00946c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946c50.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`009452dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00945/009452dc.md) · 呼出先 5件 [`009462dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00946/009462dc.md) [`00946618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00946/00946618.md) [`00946ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00946/00946ca4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009469a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/0094691c.md#insn-009469a4) · [`00946a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/0094691c.md#insn-00946a3c) · [`00946a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/0094691c.md#insn-00946a70)
- 新版 `009469f8`（命令位置の公開資料なし） · `00946a90`（命令位置の公開資料なし） · `00946ac4`（命令位置の公開資料なし）

~~~diff
- 009469a4 ["INT_ADD", "register:40f0:8", ["const:9469a4:8", "const:4:8"]]
- 009469a4 ["CALL", null, ["callee:009462dc:8"]]
+ 009469f8 ["INT_ADD", "register:40f0:8", ["const:9469f8:8", "const:4:8"]]
+ 009469f8 ["CALL", null, ["callee:009462dc:8"]]
- 009469a4 bytes 39feff97
+ 009469f8 bytes 39feff97
- 00946a3c ["INT_ADD", "register:40f0:8", ["const:946a3c:8", "const:4:8"]]
- 00946a3c ["CALL", null, ["callee:00c57f80:8"]]
+ 00946a90 ["INT_ADD", "register:40f0:8", ["const:946a90:8", "const:4:8"]]
+ 00946a90 ["CALL", null, ["callee:00c57f80:8"]]
- 00946a3c bytes 1d450c94
+ 00946a90 bytes 3c450c94
- 00946a70 ["INT_ADD", "register:40f0:8", ["const:946a70:8", "const:4:8"]]
- 00946a70 ["CALL", null, ["callee:00946618:8"]]
+ 00946ac4 ["INT_ADD", "register:40f0:8", ["const:946ac4:8", "const:4:8"]]
+ 00946ac4 ["CALL", null, ["callee:00946618:8"]]
- 00946a70 bytes d5feff97
+ 00946ac4 bytes d5feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35143005e4554822cd7fd3bf85ca745a"></a>

### [`00946c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946c50.md) → [`00946ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00946/00946ca4.md) FUN_00946ca4

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00945288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00945/00945288.md) [`00946288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946288.md) [`0094691c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/0094691c.md) · 呼出先 3件 [`009465c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/009465c4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 3件 [`009452dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00945/009452dc.md) [`009462dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00946/009462dc.md) [`00946970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00946/00946970.md) · 呼出先 3件 [`00946618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00946/00946618.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00946c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946c50.md#insn-00946c8c) · [`00946d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946c50.md#insn-00946d20) · [`00946dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946c50.md#insn-00946dd4)
- 新版 `00946ce0`（命令位置の公開資料なし） · `00946d74`（命令位置の公開資料なし） · `00946e28`（命令位置の公開資料なし）

~~~diff
- 00946c8c ["INT_ADD", "register:40f0:8", ["const:946c8c:8", "const:4:8"]]
- 00946c8c ["CALL", null, ["callee:00946618:8"]]
+ 00946ce0 ["INT_ADD", "register:40f0:8", ["const:946ce0:8", "const:4:8"]]
+ 00946ce0 ["CALL", null, ["callee:00946618:8"]]
- 00946c8c bytes 4efeff97
+ 00946ce0 bytes 4efeff97
- 00946d20 ["INT_ADD", "register:40f0:8", ["const:946d20:8", "const:4:8"]]
- 00946d20 ["CALL", null, ["callee:00c57f80:8"]]
+ 00946d74 ["INT_ADD", "register:40f0:8", ["const:946d74:8", "const:4:8"]]
+ 00946d74 ["CALL", null, ["callee:00c57f80:8"]]
- 00946d20 bytes 64440c94
+ 00946d74 bytes 83440c94
- 00946dd4 ["INT_ADD", "register:40f0:8", ["const:946dd4:8", "const:4:8"]]
- 00946dd4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00946e28 ["INT_ADD", "register:40f0:8", ["const:946e28:8", "const:4:8"]]
+ 00946e28 ["CALL", null, ["callee:00c57f80:8"]]
- 00946dd4 bytes 37440c94
+ 00946e28 bytes 56440c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-213e8e0a92d0ccc412064bfc4d32085c"></a>

### [`00961734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00961/00961734.md) → [`00961788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00961/00961788.md) FUN_00961788

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0094726c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00947/0094726c.md) [`009617a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00961/009617a0.md) [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) · 呼出先 1件 [`005e8198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e8/005e8198.md)
- 新版 呼出元 3件 [`009472c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00947/009472c0.md) [`009617f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00961/009617f4.md) [`0098dc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0098d/0098dc5c.md) · 呼出先 1件 [`005e81d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e8/005e81d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0096178c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00961/00961734.md#insn-0096178c)
- 新版 `009617e0`（命令位置の公開資料なし）

~~~diff
- 0096178c ["INT_ADD", "register:40f0:8", ["const:96178c:8", "const:4:8"]]
- 0096178c ["CALL", null, ["callee:005e81d8:8"]]
+ 009617e0 ["INT_ADD", "register:40f0:8", ["const:9617e0:8", "const:4:8"]]
+ 009617e0 ["CALL", null, ["callee:005e81d8:8"]]
- 0096178c bytes 831af297
+ 009617e0 bytes 7e1af297
~~~


<a id="compare-9d2011efb2f5ffefd811e5f4d98f1edb"></a>

### [`00963f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00963/00963f2c.md) → [`00963f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00963/00963f80.md) FUN_00963f80

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00963f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00963/00963f2c.md#insn-00963f7c) · [`00963f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00963/00963f2c.md#insn-00963f8c) · [`00963f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00963/00963f2c.md#insn-00963f9c)
- 新版 `00963fd0`（命令位置の公開資料なし） · `00963fe0`（命令位置の公開資料なし） · `00963ff0`（命令位置の公開資料なし）

~~~diff
- 00963f7c ["INT_ADD", "register:40f0:8", ["const:963f7c:8", "const:4:8"]]
- 00963f7c ["CALL", null, ["callee:00c57f80:8"]]
+ 00963fd0 ["INT_ADD", "register:40f0:8", ["const:963fd0:8", "const:4:8"]]
+ 00963fd0 ["CALL", null, ["callee:00c57f80:8"]]
- 00963f7c bytes cdcf0b94
+ 00963fd0 bytes eccf0b94
- 00963f8c ["INT_ADD", "register:40f0:8", ["const:963f8c:8", "const:4:8"]]
- 00963f8c ["CALL", null, ["callee:00c57f80:8"]]
+ 00963fe0 ["INT_ADD", "register:40f0:8", ["const:963fe0:8", "const:4:8"]]
+ 00963fe0 ["CALL", null, ["callee:00c57f80:8"]]
- 00963f8c bytes c9cf0b94
+ 00963fe0 bytes e8cf0b94
- 00963f9c ["INT_ADD", "register:40f0:8", ["const:963f9c:8", "const:4:8"]]
- 00963f9c ["CALL", null, ["callee:00c57f80:8"]]
+ 00963ff0 ["INT_ADD", "register:40f0:8", ["const:963ff0:8", "const:4:8"]]
+ 00963ff0 ["CALL", null, ["callee:00c57f80:8"]]
- 00963f9c bytes c5cf0b94
+ 00963ff0 bytes e4cf0b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2225bd66252fd6c3ff17401c37806aaa"></a>

### [`0098079c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/0098079c.md) → [`009807f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00980/009807f0.md) FUN_009807f0

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009807b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/0098079c.md#insn-009807b8)
- 新版 `0098080c`（命令位置の公開資料なし）

~~~diff
- 009807b8 ["INT_ADD", "register:40f0:8", ["const:9807b8:8", "const:4:8"]]
- 009807b8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0098080c ["INT_ADD", "register:40f0:8", ["const:98080c:8", "const:4:8"]]
+ 0098080c ["CALL", null, ["callee:00c57f80:8"]]
- 009807b8 bytes be5d0b94
+ 0098080c bytes dd5d0b94
~~~


<a id="compare-3bb0660f7e3538c3ecc03f9e029f4acd"></a>

### [`00982118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/00982118.md) → [`0098216c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00982/0098216c.md) FUN_0098216c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00982168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/00982118.md#insn-00982168) · [`00982178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/00982118.md#insn-00982178) · [`00982188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/00982118.md#insn-00982188)
- 新版 `009821bc`（命令位置の公開資料なし） · `009821cc`（命令位置の公開資料なし） · `009821dc`（命令位置の公開資料なし）

~~~diff
- 00982168 ["INT_ADD", "register:40f0:8", ["const:982168:8", "const:4:8"]]
- 00982168 ["CALL", null, ["callee:00c57f80:8"]]
+ 009821bc ["INT_ADD", "register:40f0:8", ["const:9821bc:8", "const:4:8"]]
+ 009821bc ["CALL", null, ["callee:00c57f80:8"]]
- 00982168 bytes 52570b94
+ 009821bc bytes 71570b94
- 00982178 ["INT_ADD", "register:40f0:8", ["const:982178:8", "const:4:8"]]
- 00982178 ["CALL", null, ["callee:00c57f80:8"]]
+ 009821cc ["INT_ADD", "register:40f0:8", ["const:9821cc:8", "const:4:8"]]
+ 009821cc ["CALL", null, ["callee:00c57f80:8"]]
- 00982178 bytes 4e570b94
+ 009821cc bytes 6d570b94
- 00982188 ["INT_ADD", "register:40f0:8", ["const:982188:8", "const:4:8"]]
- 00982188 ["CALL", null, ["callee:00c57f80:8"]]
+ 009821dc ["INT_ADD", "register:40f0:8", ["const:9821dc:8", "const:4:8"]]
+ 009821dc ["CALL", null, ["callee:00c57f80:8"]]
- 00982188 bytes 4a570b94
+ 009821dc bytes 69570b94
~~~


<a id="compare-2aacf599b48b7135c7712d428371a9cf"></a>

### [`009821cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009821cc.md) → [`00982220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00982/00982220.md) FUN_00982220

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0097fb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097fb20.md) [`00980e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980e10.md) [`00981440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981440.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`009822fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009822fc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 3件 [`0097fb74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0097f/0097fb74.md) [`00980e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00980/00980e64.md) [`00981494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00981/00981494.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00982350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00982/00982350.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00982200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009821cc.md#insn-00982200) · [`00982220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009821cc.md#insn-00982220) · [`0098225c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009821cc.md#insn-0098225c)
- 新版 `00982254`（命令位置の公開資料なし） · `00982274`（命令位置の公開資料なし） · `009822b0`（命令位置の公開資料なし）

~~~diff
- 00982200 ["INT_ADD", "register:40f0:8", ["const:982200:8", "const:4:8"]]
- 00982200 ["CALL", null, ["callee:00982350:8"]]
+ 00982254 ["INT_ADD", "register:40f0:8", ["const:982254:8", "const:4:8"]]
+ 00982254 ["CALL", null, ["callee:00982350:8"]]
- 00982200 bytes 3f000094
+ 00982254 bytes 3f000094
- 00982220 ["INT_ADD", "register:40f0:8", ["const:982220:8", "const:4:8"]]
- 00982220 ["CALL", null, ["callee:00c57f60:8"]]
+ 00982274 ["INT_ADD", "register:40f0:8", ["const:982274:8", "const:4:8"]]
+ 00982274 ["CALL", null, ["callee:00c57f60:8"]]
- 00982220 bytes 1c570b94
+ 00982274 bytes 3b570b94
- 0098225c ["INT_ADD", "register:40f0:8", ["const:98225c:8", "const:4:8"]]
- 0098225c ["CALL", null, ["callee:0043bb60:8"]]
+ 009822b0 ["INT_ADD", "register:40f0:8", ["const:9822b0:8", "const:4:8"]]
+ 009822b0 ["CALL", null, ["callee:0043bb60:8"]]
- 0098225c bytes 31e6ea97
+ 009822b0 bytes 2ce6ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a11681cd2a2e17a60e84b895569439e8"></a>

### [`0098c954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098c/0098c954.md) → [`0098c9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0098c/0098c9a8.md) FUN_0098c9a8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0099703c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00997/0099703c.md) [`00ae128c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae1/00ae128c.md) · 呼出先 1件 [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md)
- 新版 呼出元 2件 [`00997090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00997/00997090.md) [`00ae1328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae1/00ae1328.md) · 呼出先 1件 [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0098c978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098c/0098c954.md#insn-0098c978)
- 新版 `0098c9cc`（命令位置の公開資料なし）

~~~diff
- 0098c978 ["INT_ADD", "register:40f0:8", ["const:98c978:8", "const:4:8"]]
- 0098c978 ["CALL", null, ["callee:00676aa0:8"]]
+ 0098c9cc ["INT_ADD", "register:40f0:8", ["const:98c9cc:8", "const:4:8"]]
+ 0098c9cc ["CALL", null, ["callee:00676aa0:8"]]
- 0098c978 bytes 3aa8f397
+ 0098c9cc bytes 35a8f397
~~~


<a id="compare-c1144967afb714219de5e52d5bc147d4"></a>

### [`009a67d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a67d4.md) → [`009a6828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6828.md) FUN_009a6828

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009a67f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a67d4.md#insn-009a67f0) · [`009a6810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a67d4.md#insn-009a6810)
- 新版 `009a6844`（命令位置の公開資料なし） · `009a6864`（命令位置の公開資料なし）

~~~diff
- 009a67f0 ["INT_ADD", "register:40f0:8", ["const:9a67f0:8", "const:4:8"]]
- 009a67f0 ["CALL", null, ["callee:00c53da0:8"]]
+ 009a6844 ["INT_ADD", "register:40f0:8", ["const:9a6844:8", "const:4:8"]]
+ 009a6844 ["CALL", null, ["callee:00c53da0:8"]]
- 009a67f0 bytes 44b50a94
+ 009a6844 bytes 57b50a94
- 009a6810 ["COPY", "register:0:8", ["register:4040:8"]]
- 009a6810 ["INT_ADD", "register:40f0:8", ["const:9a6810:8", "const:4:8"]]
- 009a6810 ["CALLIND", null, ["register:0:8"]]
+ 009a6864 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009a6864 ["INT_ADD", "register:40f0:8", ["const:9a6864:8", "const:4:8"]]
+ 009a6864 ["CALLIND", null, ["register:0:8"]]
- 009a6810 bytes 00013fd6
+ 009a6864 bytes 00013fd6
~~~


<a id="compare-128fabfac1785b7655d4debec5f7646d"></a>

### [`009a8548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a8/009a8548.md) → [`009a859c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a859c.md) FUN_009a859c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009a50c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a5/009a50c0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`009a5114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5114.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009a8588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a8/009a8548.md#insn-009a8588) · [`009a85b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a8/009a8548.md#insn-009a85b4)
- 新版 `009a85dc`（命令位置の公開資料なし） · `009a8608`（命令位置の公開資料なし）

~~~diff
- 009a8588 ["COPY", "register:0:8", ["register:4040:8"]]
- 009a8588 ["INT_ADD", "register:40f0:8", ["const:9a8588:8", "const:4:8"]]
- 009a8588 ["CALLIND", null, ["register:0:8"]]
+ 009a85dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 009a85dc ["INT_ADD", "register:40f0:8", ["const:9a85dc:8", "const:4:8"]]
+ 009a85dc ["CALLIND", null, ["register:0:8"]]
- 009a8588 bytes 00013fd6
+ 009a85dc bytes 00013fd6
- 009a85b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 009a85b4 ["INT_ADD", "register:40f0:8", ["const:9a85b4:8", "const:4:8"]]
- 009a85b4 ["CALLIND", null, ["register:0:8"]]
+ 009a8608 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009a8608 ["INT_ADD", "register:40f0:8", ["const:9a8608:8", "const:4:8"]]
+ 009a8608 ["CALLIND", null, ["register:0:8"]]
- 009a85b4 bytes 00013fd6
+ 009a8608 bytes 00013fd6
~~~


<a id="compare-85afd0efd60a1ebea895640a602ad416"></a>

### [`009a95c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a95c4.md) → [`009a9618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a9618.md) FUN_009a9618

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009b5bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b5bb8.md) [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 1件 [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md)
- 新版 呼出元 2件 [`009b5c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5c0c.md) [`00a06df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06df0.md) · 呼出先 1件 [`00480338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480338.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009a95d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a95c4.md#insn-009a95d8)
- 新版 `009a962c`（命令位置の公開資料なし）

~~~diff
- 009a95d8 ["INT_ADD", "register:40f0:8", ["const:9a95d8:8", "const:4:8"]]
- 009a95d8 ["CALL", null, ["callee:00480338:8"]]
+ 009a962c ["INT_ADD", "register:40f0:8", ["const:9a962c:8", "const:4:8"]]
+ 009a962c ["CALL", null, ["callee:00480338:8"]]
- 009a95d8 bytes 485beb97
+ 009a962c bytes 435beb97
~~~


<a id="compare-3ab79572a6e90436e3ea4eb5157dba30"></a>

### [`009ac10c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac10c.md) → [`009ac160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009ac160.md) FUN_009ac160

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`009ac144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac144.md)
- 新版 呼出元 0件  · 呼出先 1件 [`009ac198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009ac198.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009ac134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac10c.md#insn-009ac134)
- 新版 `009ac188`（命令位置の公開資料なし）

~~~diff
- 009ac134 ["INT_ADD", "register:40f0:8", ["const:9ac134:8", "const:4:8"]]
- 009ac134 ["CALL", null, ["callee:009ac198:8"]]
+ 009ac188 ["INT_ADD", "register:40f0:8", ["const:9ac188:8", "const:4:8"]]
+ 009ac188 ["CALL", null, ["callee:009ac198:8"]]
- 009ac134 bytes 04000094
+ 009ac188 bytes 04000094
~~~


<a id="compare-308776ebb949bb58b88f95ba53f7c705"></a>

### [`009ac7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac7f8.md) → [`009ac84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009ac84c.md) FUN_009ac84c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0086d244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d244.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0086d29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d29c.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009ac844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac7f8.md#insn-009ac844) · [`009ac858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac7f8.md#insn-009ac858) · [`009ac860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac7f8.md#insn-009ac860)
- 新版 `009ac898`（命令位置の公開資料なし） · `009ac8ac`（命令位置の公開資料なし） · `009ac8b4`（命令位置の公開資料なし）

~~~diff
- 009ac844 ["INT_ADD", "register:40f0:8", ["const:9ac844:8", "const:4:8"]]
- 009ac844 ["CALL", null, ["callee:00c53da0:8"]]
+ 009ac898 ["INT_ADD", "register:40f0:8", ["const:9ac898:8", "const:4:8"]]
+ 009ac898 ["CALL", null, ["callee:00c53da0:8"]]
- 009ac844 bytes 2f9d0a94
+ 009ac898 bytes 429d0a94
- 009ac858 ["COPY", "register:0:8", ["register:4040:8"]]
- 009ac858 ["INT_ADD", "register:40f0:8", ["const:9ac858:8", "const:4:8"]]
- 009ac858 ["CALLIND", null, ["register:0:8"]]
+ 009ac8ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ac8ac ["INT_ADD", "register:40f0:8", ["const:9ac8ac:8", "const:4:8"]]
+ 009ac8ac ["CALLIND", null, ["register:0:8"]]
- 009ac858 bytes 00013fd6
+ 009ac8ac bytes 00013fd6
- 009ac860 ["INT_ADD", "register:40f0:8", ["const:9ac860:8", "const:4:8"]]
- 009ac860 ["CALL", null, ["callee:00c57f50:8"]]
+ 009ac8b4 ["INT_ADD", "register:40f0:8", ["const:9ac8b4:8", "const:4:8"]]
+ 009ac8b4 ["CALL", null, ["callee:00c57f50:8"]]
- 009ac860 bytes 88ad0a94
+ 009ac8b4 bytes a7ad0a94
~~~


<a id="compare-22286fb66ade07a6cb8c992bae309ea8"></a>

### [`009ac928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac928.md) → [`009ac97c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009ac97c.md) FUN_009ac97c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 6件 [`00480b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md) [`009b5b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b5b78.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 6件 [`00480b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480b78.md) [`009b5bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5bcc.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009ac968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac928.md#insn-009ac968) · [`009ac994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac928.md#insn-009ac994) · [`009ac9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac928.md#insn-009ac9a0)
- 新版 `009ac9bc`（命令位置の公開資料なし） · `009ac9e8`（命令位置の公開資料なし） · `009ac9f4`（命令位置の公開資料なし）

~~~diff
- 009ac968 ["INT_ADD", "register:40f0:8", ["const:9ac968:8", "const:4:8"]]
- 009ac968 ["CALL", null, ["callee:00480b78:8"]]
+ 009ac9bc ["INT_ADD", "register:40f0:8", ["const:9ac9bc:8", "const:4:8"]]
+ 009ac9bc ["CALL", null, ["callee:00480b78:8"]]
- 009ac968 bytes 7450eb97
+ 009ac9bc bytes 6f50eb97
- 009ac994 ["INT_ADD", "register:40f0:8", ["const:9ac994:8", "const:4:8"]]
- 009ac994 ["CALL", null, ["callee:00c53d70:8"]]
+ 009ac9e8 ["INT_ADD", "register:40f0:8", ["const:9ac9e8:8", "const:4:8"]]
+ 009ac9e8 ["CALL", null, ["callee:00c53d70:8"]]
- 009ac994 bytes cf9c0a94
+ 009ac9e8 bytes e29c0a94
- 009ac9a0 ["INT_ADD", "register:40f0:8", ["const:9ac9a0:8", "const:4:8"]]
- 009ac9a0 ["CALL", null, ["callee:009b5bcc:8"]]
+ 009ac9f4 ["INT_ADD", "register:40f0:8", ["const:9ac9f4:8", "const:4:8"]]
+ 009ac9f4 ["CALL", null, ["callee:009b5bcc:8"]]
- 009ac9a0 bytes 76240094
+ 009ac9f4 bytes 76240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9be169fe1c38b486e19aa0f1da865d9f"></a>

### [`009aca24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009aca24.md) → [`009aca78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009aca78.md) FUN_009aca78

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009af988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009af/009af988.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`009af9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009af/009af9dc.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009aca40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009aca24.md#insn-009aca40) · [`009aca60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009aca24.md#insn-009aca60)
- 新版 `009aca94`（命令位置の公開資料なし） · `009acab4`（命令位置の公開資料なし）

~~~diff
- 009aca40 ["INT_ADD", "register:40f0:8", ["const:9aca40:8", "const:4:8"]]
- 009aca40 ["CALL", null, ["callee:00c53da0:8"]]
+ 009aca94 ["INT_ADD", "register:40f0:8", ["const:9aca94:8", "const:4:8"]]
+ 009aca94 ["CALL", null, ["callee:00c53da0:8"]]
- 009aca40 bytes b09c0a94
+ 009aca94 bytes c39c0a94
- 009aca60 ["COPY", "register:0:8", ["register:4040:8"]]
- 009aca60 ["INT_ADD", "register:40f0:8", ["const:9aca60:8", "const:4:8"]]
- 009aca60 ["CALLIND", null, ["register:0:8"]]
+ 009acab4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009acab4 ["INT_ADD", "register:40f0:8", ["const:9acab4:8", "const:4:8"]]
+ 009acab4 ["CALLIND", null, ["register:0:8"]]
- 009aca60 bytes 00013fd6
+ 009acab4 bytes 00013fd6
~~~


<a id="compare-38b9d7fe26e6789658732a56c44f7afe"></a>

### [`009adee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ad/009adee8.md) → [`009adf3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ad/009adf3c.md) FUN_009adf3c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`00613c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00613/00613c64.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 6件 [`009b5c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b5c94.md) [`009b5cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b5cb4.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 4件 [`00605294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00605/00605294.md) [`00613ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00613/00613ca4.md) [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 6件 [`009b5ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5ce8.md) [`009b5d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5d08.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009adf34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ad/009adee8.md#insn-009adf34) · [`009adf3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ad/009adee8.md#insn-009adf3c) · [`009adf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ad/009adee8.md#insn-009adf50)
- 新版 `009adf88`（命令位置の公開資料なし） · `009adf90`（命令位置の公開資料なし） · `009adfa4`（命令位置の公開資料なし）

~~~diff
- 009adf34 ["INT_ADD", "register:40f0:8", ["const:9adf34:8", "const:4:8"]]
- 009adf34 ["CALL", null, ["callee:00c53d70:8"]]
+ 009adf88 ["INT_ADD", "register:40f0:8", ["const:9adf88:8", "const:4:8"]]
+ 009adf88 ["CALL", null, ["callee:00c53d70:8"]]
- 009adf34 bytes 67970a94
+ 009adf88 bytes 7a970a94
- 009adf3c ["INT_ADD", "register:40f0:8", ["const:9adf3c:8", "const:4:8"]]
- 009adf3c ["CALL", null, ["callee:009b5ce8:8"]]
+ 009adf90 ["INT_ADD", "register:40f0:8", ["const:9adf90:8", "const:4:8"]]
+ 009adf90 ["CALL", null, ["callee:009b5ce8:8"]]
- 009adf3c bytes 561f0094
+ 009adf90 bytes 561f0094
- 009adf50 ["INT_ADD", "register:40f0:8", ["const:9adf50:8", "const:4:8"]]
- 009adf50 ["CALL", null, ["callee:00c53da0:8"]]
+ 009adfa4 ["INT_ADD", "register:40f0:8", ["const:9adfa4:8", "const:4:8"]]
+ 009adfa4 ["CALL", null, ["callee:00c53da0:8"]]
- 009adf50 bytes 6c970a94
+ 009adfa4 bytes 7f970a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf75e3e3a57ea0b50efc4ba82f914dd1"></a>

### [`009ae904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ae/009ae904.md) → [`009ae958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ae/009ae958.md) FUN_009ae958

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009ae924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ae/009ae904.md#insn-009ae924) · [`009ae938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ae/009ae904.md#insn-009ae938) · [`009ae940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ae/009ae904.md#insn-009ae940)
- 新版 `009ae978`（命令位置の公開資料なし） · `009ae98c`（命令位置の公開資料なし） · `009ae994`（命令位置の公開資料なし）

~~~diff
- 009ae924 ["INT_ADD", "register:40f0:8", ["const:9ae924:8", "const:4:8"]]
- 009ae924 ["CALL", null, ["callee:00c53da0:8"]]
+ 009ae978 ["INT_ADD", "register:40f0:8", ["const:9ae978:8", "const:4:8"]]
+ 009ae978 ["CALL", null, ["callee:00c53da0:8"]]
- 009ae924 bytes f7940a94
+ 009ae978 bytes 0a950a94
- 009ae938 ["COPY", "register:0:8", ["register:4040:8"]]
- 009ae938 ["INT_ADD", "register:40f0:8", ["const:9ae938:8", "const:4:8"]]
- 009ae938 ["CALLIND", null, ["register:0:8"]]
+ 009ae98c ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ae98c ["INT_ADD", "register:40f0:8", ["const:9ae98c:8", "const:4:8"]]
+ 009ae98c ["CALLIND", null, ["register:0:8"]]
- 009ae938 bytes 00013fd6
+ 009ae98c bytes 00013fd6
- 009ae940 ["INT_ADD", "register:40f0:8", ["const:9ae940:8", "const:4:8"]]
- 009ae940 ["CALL", null, ["callee:00c57f50:8"]]
+ 009ae994 ["INT_ADD", "register:40f0:8", ["const:9ae994:8", "const:4:8"]]
+ 009ae994 ["CALL", null, ["callee:00c57f50:8"]]
- 009ae940 bytes 50a50a94
+ 009ae994 bytes 6fa50a94
~~~


<a id="compare-648a0ce155c64f79c66524c5d1bc37c7"></a>

### [`009af124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009af/009af124.md) → [`009af178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009af/009af178.md) FUN_009af178

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 5件 [`009b5cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b5cf8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 5件 [`009b5d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5d4c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009af174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009af/009af124.md#insn-009af174) · [`009af184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009af/009af124.md#insn-009af184) · [`009af194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009af/009af124.md#insn-009af194)
- 新版 `009af1c8`（命令位置の公開資料なし） · `009af1d8`（命令位置の公開資料なし） · `009af1e8`（命令位置の公開資料なし）

~~~diff
- 009af174 ["INT_ADD", "register:40f0:8", ["const:9af174:8", "const:4:8"]]
- 009af174 ["CALL", null, ["callee:00c53d70:8"]]
+ 009af1c8 ["INT_ADD", "register:40f0:8", ["const:9af1c8:8", "const:4:8"]]
+ 009af1c8 ["CALL", null, ["callee:00c53d70:8"]]
- 009af174 bytes d7920a94
+ 009af1c8 bytes ea920a94
- 009af184 ["INT_ADD", "register:40f0:8", ["const:9af184:8", "const:4:8"]]
- 009af184 ["CALL", null, ["callee:009b5d4c:8"]]
+ 009af1d8 ["INT_ADD", "register:40f0:8", ["const:9af1d8:8", "const:4:8"]]
+ 009af1d8 ["CALL", null, ["callee:009b5d4c:8"]]
- 009af184 bytes dd1a0094
+ 009af1d8 bytes dd1a0094
- 009af194 ["INT_ADD", "register:40f0:8", ["const:9af194:8", "const:4:8"]]
- 009af194 ["CALL", null, ["callee:00c53da0:8"]]
+ 009af1e8 ["INT_ADD", "register:40f0:8", ["const:9af1e8:8", "const:4:8"]]
+ 009af1e8 ["CALL", null, ["callee:00c53da0:8"]]
- 009af194 bytes db920a94
+ 009af1e8 bytes ee920a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb0ade78d4fd0f87bdeecbf6c932f9e9"></a>

### [`009b3b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3b08.md) → [`009b3b5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b3/009b3b5c.md) FUN_009b3b5c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849334.md) [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) [`009b0bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b0/009b0bdc.md) · 呼出先 2件 [`00869ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869ef4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0084938c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/0084938c.md) [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) [`009b0c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b0/009b0c30.md) · 呼出先 2件 [`00869f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869f4c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009b3b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3b08.md#insn-009b3b30) · [`009b3b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3b08.md#insn-009b3b38) · [`009b3b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3b08.md#insn-009b3b48)
- 新版 `009b3b84`（命令位置の公開資料なし） · `009b3b8c`（命令位置の公開資料なし） · `009b3b9c`（命令位置の公開資料なし）

~~~diff
- 009b3b30 ["INT_ADD", "register:40f0:8", ["const:9b3b30:8", "const:4:8"]]
- 009b3b30 ["CALL", null, ["callee:00869f4c:8"]]
+ 009b3b84 ["INT_ADD", "register:40f0:8", ["const:9b3b84:8", "const:4:8"]]
+ 009b3b84 ["CALL", null, ["callee:00869f4c:8"]]
- 009b3b30 bytes f1d8fa97
+ 009b3b84 bytes f2d8fa97
- 009b3b38 ["INT_ADD", "register:40f0:8", ["const:9b3b38:8", "const:4:8"]]
- 009b3b38 ["CALL", null, ["callee:00c57f80:8"]]
+ 009b3b8c ["INT_ADD", "register:40f0:8", ["const:9b3b8c:8", "const:4:8"]]
+ 009b3b8c ["CALL", null, ["callee:00c57f80:8"]]
- 009b3b38 bytes de900a94
+ 009b3b8c bytes fd900a94
- 009b3b48 ["INT_ADD", "register:40f0:8", ["const:9b3b48:8", "const:4:8"]]
- 009b3b48 ["CALL", null, ["callee:00c57f80:8"]]
+ 009b3b9c ["INT_ADD", "register:40f0:8", ["const:9b3b9c:8", "const:4:8"]]
+ 009b3b9c ["CALL", null, ["callee:00c57f80:8"]]
- 009b3b48 bytes da900a94
+ 009b3b9c bytes f9900a94
~~~


<a id="compare-6ca614e790a1a346f41541f4a15fc8c2"></a>

### [`009b5c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b5c2c.md) → [`009b5c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5c80.md) FUN_009b5c80

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009ad4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ad/009ad4a4.md) · 呼出先 3件 [`009a9300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a9300.md) [`009a95f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a95f0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`009ad4f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ad/009ad4f8.md) · 呼出先 3件 [`009a9354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a9354.md) [`009a9644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a9644.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009b5c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b5c2c.md#insn-009b5c54) · [`009b5c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b5c2c.md#insn-009b5c74)
- 新版 `009b5ca8`（命令位置の公開資料なし） · `009b5cc8`（命令位置の公開資料なし）

~~~diff
- 009b5c54 ["INT_ADD", "register:40f0:8", ["const:9b5c54:8", "const:4:8"]]
- 009b5c54 ["CALL", null, ["callee:00c57f60:8"]]
+ 009b5ca8 ["INT_ADD", "register:40f0:8", ["const:9b5ca8:8", "const:4:8"]]
+ 009b5ca8 ["CALL", null, ["callee:00c57f60:8"]]
- 009b5c54 bytes 8f880a94
+ 009b5ca8 bytes ae880a94
- 009b5c74 ["INT_ADD", "register:40f0:8", ["const:9b5c74:8", "const:4:8"]]
- 009b5c74 ["CALL", null, ["callee:009a9354:8"]]
+ 009b5cc8 ["INT_ADD", "register:40f0:8", ["const:9b5cc8:8", "const:4:8"]]
+ 009b5cc8 ["CALL", null, ["callee:009a9354:8"]]
- 009b5c74 bytes a3cdff97
+ 009b5cc8 bytes a3cdff97
~~~


