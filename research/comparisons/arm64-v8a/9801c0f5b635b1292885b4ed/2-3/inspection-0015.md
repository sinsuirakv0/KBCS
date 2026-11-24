# v16.0.1 → v16.0.2 · 要調査の変更候補 (15)

[一覧の目次](README.md)

<a id="compare-a3bfeaed9b3143eab9498dcc7cf80d91"></a>

### [`00597230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597230.md) → [`00597270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597270.md) FUN_00597270

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005961d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005961d4.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00458fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458fcc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00596214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596214.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0045900c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/0045900c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00597270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597230.md#insn-00597270) · [`00597290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597230.md#insn-00597290) · [`005972c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597230.md#insn-005972c4)
- 新版 `005972b0`（命令位置の公開資料なし） · `005972d0`（命令位置の公開資料なし） · `00597304`（命令位置の公開資料なし）

~~~diff
- 00597270 ["INT_ADD", "register:40f0:8", ["const:597270:8", "const:4:8"]]
- 00597270 ["CALL", null, ["callee:0045900c:8"]]
+ 005972b0 ["INT_ADD", "register:40f0:8", ["const:5972b0:8", "const:4:8"]]
+ 005972b0 ["CALL", null, ["callee:0045900c:8"]]
- 00597270 bytes 5707fb97
+ 005972b0 bytes 5707fb97
- 00597290 ["INT_ADD", "register:40f0:8", ["const:597290:8", "const:4:8"]]
- 00597290 ["CALL", null, ["callee:00c57f60:8"]]
+ 005972d0 ["INT_ADD", "register:40f0:8", ["const:5972d0:8", "const:4:8"]]
+ 005972d0 ["CALL", null, ["callee:00c57f60:8"]]
- 00597290 bytes 00031b94
+ 005972d0 bytes 24031b94
- 005972c4 ["INT_ADD", "register:40f0:8", ["const:5972c4:8", "const:4:8"]]
- 005972c4 ["CALL", null, ["callee:0043bb60:8"]]
+ 00597304 ["INT_ADD", "register:40f0:8", ["const:597304:8", "const:4:8"]]
+ 00597304 ["CALL", null, ["callee:0043bb60:8"]]
- 005972c4 bytes 1792fa97
+ 00597304 bytes 1792fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bbc741c5ba3753e184933f411a7619a"></a>

### [`0059736c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059736c.md) → [`005973ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005973ac.md) FUN_005973ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0059633c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/0059633c.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00458fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458fcc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0059637c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/0059637c.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0045900c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/0045900c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005973ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059736c.md#insn-005973ac) · [`005973cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059736c.md#insn-005973cc) · [`00597400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059736c.md#insn-00597400)
- 新版 `005973ec`（命令位置の公開資料なし） · `0059740c`（命令位置の公開資料なし） · `00597440`（命令位置の公開資料なし）

~~~diff
- 005973ac ["INT_ADD", "register:40f0:8", ["const:5973ac:8", "const:4:8"]]
- 005973ac ["CALL", null, ["callee:0045900c:8"]]
+ 005973ec ["INT_ADD", "register:40f0:8", ["const:5973ec:8", "const:4:8"]]
+ 005973ec ["CALL", null, ["callee:0045900c:8"]]
- 005973ac bytes 0807fb97
+ 005973ec bytes 0807fb97
- 005973cc ["INT_ADD", "register:40f0:8", ["const:5973cc:8", "const:4:8"]]
- 005973cc ["CALL", null, ["callee:00c57f60:8"]]
+ 0059740c ["INT_ADD", "register:40f0:8", ["const:59740c:8", "const:4:8"]]
+ 0059740c ["CALL", null, ["callee:00c57f60:8"]]
- 005973cc bytes b1021b94
+ 0059740c bytes d5021b94
- 00597400 ["INT_ADD", "register:40f0:8", ["const:597400:8", "const:4:8"]]
- 00597400 ["CALL", null, ["callee:0043bb60:8"]]
+ 00597440 ["INT_ADD", "register:40f0:8", ["const:597440:8", "const:4:8"]]
+ 00597440 ["CALL", null, ["callee:0043bb60:8"]]
- 00597400 bytes c891fa97
+ 00597440 bytes c891fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-620fca7dbcc68eedf1e92eb515738ae1"></a>

### [`005974a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005974a8.md) → [`005974e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005974e8.md) FUN_005974e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005974b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005974a8.md#insn-005974b8)
- 新版 `005974f8`（命令位置の公開資料なし）

~~~diff
- 005974b8 ["INT_ADD", "register:40f0:8", ["const:5974b8:8", "const:4:8"]]
- 005974b8 ["CALL", null, ["callee:00c57f70:8"]]
+ 005974f8 ["INT_ADD", "register:40f0:8", ["const:5974f8:8", "const:4:8"]]
+ 005974f8 ["CALL", null, ["callee:00c57f70:8"]]
- 005974b8 bytes 7a021b94
+ 005974f8 bytes 9e021b94
~~~


<a id="compare-e1245543f42cb0d9c76212eb974a2a9e"></a>

### [`00597504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597504.md) → [`00597544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597544.md) FUN_00597544

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`005a1470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1470.md) [`0076625c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00766/0076625c.md) [`00767148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767148.md) [`00798ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798ea0.md) [`00b0ea7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0ea7c.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0059721c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059721c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 5件 [`005a14b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a14b0.md) [`007662b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00766/007662b4.md) [`007671a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/007671a0.md) [`00798ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798ef8.md) [`00b0eb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0e/00b0eb18.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0059725c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059725c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00597584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597504.md#insn-00597584) · [`005975c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597504.md#insn-005975c0) · [`005975d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597504.md#insn-005975d4)
- 新版 `005975c4`（命令位置の公開資料なし） · `00597600`（命令位置の公開資料なし） · `00597614`（命令位置の公開資料なし）

~~~diff
- 00597584 ["INT_ADD", "register:40f0:8", ["const:597584:8", "const:4:8"]]
- 00597584 ["CALL", null, ["callee:00c57f60:8"]]
+ 005975c4 ["INT_ADD", "register:40f0:8", ["const:5975c4:8", "const:4:8"]]
+ 005975c4 ["CALL", null, ["callee:00c57f60:8"]]
- 00597584 bytes 43021b94
+ 005975c4 bytes 67021b94
- 005975c0 ["INT_ADD", "register:40f0:8", ["const:5975c0:8", "const:4:8"]]
- 005975c0 ["CALL", null, ["callee:00c580d0:8"]]
+ 00597600 ["INT_ADD", "register:40f0:8", ["const:597600:8", "const:4:8"]]
+ 00597600 ["CALL", null, ["callee:00c580d0:8"]]
- 005975c0 bytes 90021b94
+ 00597600 bytes b4021b94
- 005975d4 ["INT_ADD", "register:40f0:8", ["const:5975d4:8", "const:4:8"]]
- 005975d4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00597614 ["INT_ADD", "register:40f0:8", ["const:597614:8", "const:4:8"]]
+ 00597614 ["CALL", null, ["callee:00c57f80:8"]]
- 005975d4 bytes 37021b94
+ 00597614 bytes 5b021b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f8a7bf446a952b349aa59c7a7f44385"></a>

### [`0059765c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059765c.md) → [`0059769c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059769c.md) FUN_0059769c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 18件 [`0043f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f91c.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`00451ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451ed8.md) [`00479dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479dc8.md) [`00574ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574ba4.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ff0.md) [`00c5a320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a320.md)
- 新版 呼出元 18件 [`0043f95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f95c.md) [`004509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004509f0.md) [`00451f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451f18.md) [`00479e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479e08.md) [`00574be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574be4.md) · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580c0.md) [`00c5a3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00597680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059765c.md#insn-00597680) · [`005976a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059765c.md#insn-005976a0) · [`005976e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059765c.md#insn-005976e4)
- 新版 `005976c0`（命令位置の公開資料なし） · `005976e0`（命令位置の公開資料なし） · `00597724`（命令位置の公開資料なし）

~~~diff
- 00597680 ["INT_ADD", "register:40f0:8", ["const:597680:8", "const:4:8"]]
- 00597680 ["CALL", null, ["callee:00c580c0:8"]]
+ 005976c0 ["INT_ADD", "register:40f0:8", ["const:5976c0:8", "const:4:8"]]
+ 005976c0 ["CALL", null, ["callee:00c580c0:8"]]
- 00597680 bytes 5c021b94
+ 005976c0 bytes 80021b94
- 005976a0 ["INT_ADD", "register:40f0:8", ["const:5976a0:8", "const:4:8"]]
- 005976a0 ["CALL", null, ["callee:00c5a3f0:8"]]
+ 005976e0 ["INT_ADD", "register:40f0:8", ["const:5976e0:8", "const:4:8"]]
+ 005976e0 ["CALL", null, ["callee:00c5a3f0:8"]]
- 005976a0 bytes 200b1b94
+ 005976e0 bytes 440b1b94
- 005976e4 ["INT_ADD", "register:40f0:8", ["const:5976e4:8", "const:4:8"]]
- 005976e4 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00597724 ["INT_ADD", "register:40f0:8", ["const:597724:8", "const:4:8"]]
+ 00597724 ["CALL", null, ["callee:00c57fb0:8"]]
- 005976e4 bytes ff011b94
+ 00597724 bytes 23021b94
~~~


<a id="compare-e0e06b075fb8602df8a41566a7584eba"></a>

### [`005976e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005976e8.md) → [`00597728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597728.md) FUN_00597728

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 17件 [`005712e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005712e0.md) [`00579524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00579/00579524.md) [`0062c0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062c/0062c0c0.md) [`0069a504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069a/0069a504.md) [`0075d75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075d/0075d75c.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c589b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589b0.md) [`00c5a320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a320.md)
- 新版 呼出元 17件 [`00571320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571320.md) [`00579564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00579/00579564.md) [`0062c100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0062c/0062c100.md) [`0069a55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069a/0069a55c.md) [`0075d7b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075d/0075d7b4.md) · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a80.md) [`00c5a3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00597728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005976e8.md#insn-00597728) · [`00597730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005976e8.md#insn-00597730) · [`00597774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005976e8.md#insn-00597774)
- 新版 `00597768`（命令位置の公開資料なし） · `00597770`（命令位置の公開資料なし） · `005977b4`（命令位置の公開資料なし）

~~~diff
- 00597728 ["INT_ADD", "register:40f0:8", ["const:597728:8", "const:4:8"]]
- 00597728 ["CALL", null, ["callee:00c58a80:8"]]
+ 00597768 ["INT_ADD", "register:40f0:8", ["const:597768:8", "const:4:8"]]
+ 00597768 ["CALL", null, ["callee:00c58a80:8"]]
- 00597728 bytes a2041b94
+ 00597768 bytes c6041b94
- 00597730 ["INT_ADD", "register:40f0:8", ["const:597730:8", "const:4:8"]]
- 00597730 ["CALL", null, ["callee:00c5a3f0:8"]]
+ 00597770 ["INT_ADD", "register:40f0:8", ["const:597770:8", "const:4:8"]]
+ 00597770 ["CALL", null, ["callee:00c5a3f0:8"]]
- 00597730 bytes fc0a1b94
+ 00597770 bytes 200b1b94
- 00597774 ["INT_ADD", "register:40f0:8", ["const:597774:8", "const:4:8"]]
- 00597774 ["CALL", null, ["callee:00c57fb0:8"]]
+ 005977b4 ["INT_ADD", "register:40f0:8", ["const:5977b4:8", "const:4:8"]]
+ 005977b4 ["CALL", null, ["callee:00c57fb0:8"]]
- 00597774 bytes db011b94
+ 005977b4 bytes ff011b94
~~~


<a id="compare-6fb91efe8d699ef3464417036c319640"></a>

### [`00597778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597778.md) → [`005977b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005977b8.md) FUN_005977b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 20件 [`004808fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004808fc.md) [`0062c0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062c/0062c0c0.md) [`00637420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00637/00637420.md) [`0069a504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069a/0069a504.md) [`0075d75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075d/0075d75c.md) · 呼出先 1件 [`00c5a330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a330.md)
- 新版 呼出元 20件 [`0048093c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/0048093c.md) [`0062c100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0062c/0062c100.md) [`00637460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00637/00637460.md) [`0069a55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069a/0069a55c.md) [`0075d7b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075d/0075d7b4.md) · 呼出先 1件 [`00c5a400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a400.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005977a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597778.md#insn-005977a8)
- 新版 `005977e8`（命令位置の公開資料なし）

~~~diff
- 005977a8 ["INT_ADD", "register:40f0:8", ["const:5977a8:8", "const:4:8"]]
- 005977a8 ["CALL", null, ["callee:00c5a400:8"]]
+ 005977e8 ["INT_ADD", "register:40f0:8", ["const:5977e8:8", "const:4:8"]]
+ 005977e8 ["CALL", null, ["callee:00c5a400:8"]]
- 005977a8 bytes e20a1b94
+ 005977e8 bytes 060b1b94
~~~


<a id="compare-fee323b895eb2c9998ca4ae23c413655"></a>

### [`00597e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597e08.md) → [`00597e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597e48.md) FUN_00597e48

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`004766c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md) [`0075e588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075e588.md) [`008d6ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6ce0.md) [`008e47f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e4/008e47f8.md) [`00b2fa0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2fa0c.md) · 呼出先 2件 [`00c5a330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a330.md) [`00c5a340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a340.md)
- 新版 呼出元 5件 [`00476708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/00476708.md) [`0075e5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075e5e0.md) [`008d6d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d6/008d6d34.md) [`008e484c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e484c.md) [`00b2faa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2f/00b2faa8.md) · 呼出先 2件 [`00c5a400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a400.md) [`00c5a410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a410.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00597e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597e08.md#insn-00597e18) · [`00597e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597e08.md#insn-00597e24)
- 新版 `00597e58`（命令位置の公開資料なし） · `00597e64`（命令位置の公開資料なし）

~~~diff
- 00597e18 ["INT_ADD", "register:40f0:8", ["const:597e18:8", "const:4:8"]]
- 00597e18 ["CALL", null, ["callee:00c5a400:8"]]
+ 00597e58 ["INT_ADD", "register:40f0:8", ["const:597e58:8", "const:4:8"]]
+ 00597e58 ["CALL", null, ["callee:00c5a400:8"]]
- 00597e18 bytes 46091b94
+ 00597e58 bytes 6a091b94
- 00597e24 ["INT_ADD", "register:40f0:8", ["const:597e24:8", "const:4:8"]]
- 00597e24 ["CALL", null, ["callee:00c5a410:8"]]
+ 00597e64 ["INT_ADD", "register:40f0:8", ["const:597e64:8", "const:4:8"]]
+ 00597e64 ["CALL", null, ["callee:00c5a410:8"]]
- 00597e24 bytes 47091b94
+ 00597e64 bytes 6b091b94
~~~


<a id="compare-0b54d23e053ee3db3d6fd32370638beb"></a>

### [`00597e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597e48.md) → [`00597e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597e88.md) FUN_00597e88

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 16件 [`004766c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md) [`007a0fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0fa0.md) [`007a1110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1110.md) [`007abc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007abc24.md) [`007acacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007acacc.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ff0.md) [`00c5a320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a320.md)
- 新版 呼出元 16件 [`00476708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/00476708.md) [`007a0ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0ff8.md) [`007a1168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1168.md) [`007abc7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007abc7c.md) [`007acb24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007acb24.md) · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580c0.md) [`00c5a3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00597e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597e48.md#insn-00597e6c) · [`00597e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597e48.md#insn-00597e8c) · [`00597eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597e48.md#insn-00597eb8)
- 新版 `00597eac`（命令位置の公開資料なし） · `00597ecc`（命令位置の公開資料なし） · `00597ef8`（命令位置の公開資料なし）

~~~diff
- 00597e6c ["INT_ADD", "register:40f0:8", ["const:597e6c:8", "const:4:8"]]
- 00597e6c ["CALL", null, ["callee:00c580c0:8"]]
+ 00597eac ["INT_ADD", "register:40f0:8", ["const:597eac:8", "const:4:8"]]
+ 00597eac ["CALL", null, ["callee:00c580c0:8"]]
- 00597e6c bytes 61001b94
+ 00597eac bytes 85001b94
- 00597e8c ["INT_ADD", "register:40f0:8", ["const:597e8c:8", "const:4:8"]]
- 00597e8c ["CALL", null, ["callee:00c5a3f0:8"]]
+ 00597ecc ["INT_ADD", "register:40f0:8", ["const:597ecc:8", "const:4:8"]]
+ 00597ecc ["CALL", null, ["callee:00c5a3f0:8"]]
- 00597e8c bytes 25091b94
+ 00597ecc bytes 49091b94
- 00597eb8 ["INT_ADD", "register:40f0:8", ["const:597eb8:8", "const:4:8"]]
- 00597eb8 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00597ef8 ["INT_ADD", "register:40f0:8", ["const:597ef8:8", "const:4:8"]]
+ 00597ef8 ["CALL", null, ["callee:00c57fb0:8"]]
- 00597eb8 bytes 0a001b94
+ 00597ef8 bytes 2e001b94
~~~


<a id="compare-c6fdd30a1dc17f52700b6892ae8e32ea"></a>

### [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) → [`00598d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598d34.md) FUN_00598d34

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 17件 [`005b1e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1e24.md) [`005b275c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b275c.md) [`005b35f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b35f8.md) [`005b3b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3b74.md) [`005b4020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4020.md) · 呼出先 2件 [`0059a330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a330.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 17件 [`005b1e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1e64.md) [`005b279c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b279c.md) [`005b3638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3638.md) [`005b3bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3bb4.md) [`005b4060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b4/005b4060.md) · 呼出先 2件 [`0059a370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a370.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00598d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md#insn-00598d30) · [`00598d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md#insn-00598d5c) · [`00598d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md#insn-00598d6c)
- 新版 `00598d70`（命令位置の公開資料なし） · `00598d9c`（命令位置の公開資料なし） · `00598dac`（命令位置の公開資料なし）

~~~diff
- 00598d30 ["COPY", "register:0:8", ["register:4048:8"]]
- 00598d30 ["INT_ADD", "register:40f0:8", ["const:598d30:8", "const:4:8"]]
- 00598d30 ["CALLIND", null, ["register:0:8"]]
+ 00598d70 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00598d70 ["INT_ADD", "register:40f0:8", ["const:598d70:8", "const:4:8"]]
+ 00598d70 ["CALLIND", null, ["register:0:8"]]
- 00598d30 bytes 20013fd6
+ 00598d70 bytes 20013fd6
- 00598d5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00598d5c ["INT_ADD", "register:40f0:8", ["const:598d5c:8", "const:4:8"]]
- 00598d5c ["CALLIND", null, ["register:0:8"]]
+ 00598d9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00598d9c ["INT_ADD", "register:40f0:8", ["const:598d9c:8", "const:4:8"]]
+ 00598d9c ["CALLIND", null, ["register:0:8"]]
- 00598d5c bytes 00013fd6
+ 00598d9c bytes 00013fd6
- 00598d6c ["INT_ADD", "register:40f0:8", ["const:598d6c:8", "const:4:8"]]
- 00598d6c ["CALL", null, ["callee:0059a370:8"]]
+ 00598dac ["INT_ADD", "register:40f0:8", ["const:598dac:8", "const:4:8"]]
+ 00598dac ["CALL", null, ["callee:0059a370:8"]]
- 00598d6c bytes 71050094
+ 00598dac bytes 71050094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4731b5a1967400d751258f1972efcd03"></a>

### [`005991cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/005991cc.md) → [`0059920c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/0059920c.md) FUN_0059920c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005ad7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md) [`005ae8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae8e4.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 2件 [`005ad820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad820.md) [`005ae924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ae/005ae924.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005991e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/005991cc.md#insn-005991e8) · [`00599208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/005991cc.md#insn-00599208)
- 新版 `00599228`（命令位置の公開資料なし） · `00599248`（命令位置の公開資料なし）

~~~diff
- 005991e8 ["INT_ADD", "register:40f0:8", ["const:5991e8:8", "const:4:8"]]
- 005991e8 ["CALL", null, ["callee:00c53da0:8"]]
+ 00599228 ["INT_ADD", "register:40f0:8", ["const:599228:8", "const:4:8"]]
+ 00599228 ["CALL", null, ["callee:00c53da0:8"]]
- 005991e8 bytes c6ea1a94
+ 00599228 bytes deea1a94
- 00599208 ["COPY", "register:0:8", ["register:4040:8"]]
- 00599208 ["INT_ADD", "register:40f0:8", ["const:599208:8", "const:4:8"]]
- 00599208 ["CALLIND", null, ["register:0:8"]]
+ 00599248 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00599248 ["INT_ADD", "register:40f0:8", ["const:599248:8", "const:4:8"]]
+ 00599248 ["CALLIND", null, ["register:0:8"]]
- 00599208 bytes 00013fd6
+ 00599248 bytes 00013fd6
~~~


<a id="compare-2afa162a9459c6fb6a6748b9a9595868"></a>

### [`0059921c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/0059921c.md) → [`0059925c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/0059925c.md) FUN_0059925c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00598dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598dc0.md) · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00598e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598e00.md) · 呼出先 2件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00599238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/0059921c.md#insn-00599238)
- 新版 `00599278`（命令位置の公開資料なし）

~~~diff
- 00599238 ["INT_ADD", "register:40f0:8", ["const:599238:8", "const:4:8"]]
- 00599238 ["CALL", null, ["callee:00c57f80:8"]]
+ 00599278 ["INT_ADD", "register:40f0:8", ["const:599278:8", "const:4:8"]]
+ 00599278 ["CALL", null, ["callee:00c57f80:8"]]
- 00599238 bytes 1efb1a94
+ 00599278 bytes 42fb1a94
~~~


<a id="compare-a4e0d53b20581c29ba76472c3bf2942e"></a>

### [`00599650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599650.md) → [`00599690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599690.md) FUN_00599690

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059966c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599650.md#insn-0059966c) · [`00599680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599650.md#insn-00599680) · [`005996a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599650.md#insn-005996a0)
- 新版 `005996ac`（命令位置の公開資料なし） · `005996c0`（命令位置の公開資料なし） · `005996e0`（命令位置の公開資料なし）

~~~diff
- 0059966c ["INT_ADD", "register:40f0:8", ["const:59966c:8", "const:4:8"]]
- 0059966c ["CALL", null, ["callee:00c57f80:8"]]
+ 005996ac ["INT_ADD", "register:40f0:8", ["const:5996ac:8", "const:4:8"]]
+ 005996ac ["CALL", null, ["callee:00c57f80:8"]]
- 0059966c bytes 11fa1a94
+ 005996ac bytes 35fa1a94
- 00599680 ["INT_ADD", "register:40f0:8", ["const:599680:8", "const:4:8"]]
- 00599680 ["CALL", null, ["callee:00c53da0:8"]]
+ 005996c0 ["INT_ADD", "register:40f0:8", ["const:5996c0:8", "const:4:8"]]
+ 005996c0 ["CALL", null, ["callee:00c53da0:8"]]
- 00599680 bytes a0e91a94
+ 005996c0 bytes b8e91a94
- 005996a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005996a0 ["INT_ADD", "register:40f0:8", ["const:5996a0:8", "const:4:8"]]
- 005996a0 ["CALLIND", null, ["register:0:8"]]
+ 005996e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005996e0 ["INT_ADD", "register:40f0:8", ["const:5996e0:8", "const:4:8"]]
+ 005996e0 ["CALLIND", null, ["register:0:8"]]
- 005996a0 bytes 00013fd6
+ 005996e0 bytes 00013fd6
~~~


<a id="compare-8e641c06810ccb2113edc8a358bc78f8"></a>

### [`00599a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599a24.md) → [`00599a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599a64.md) FUN_00599a64

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00599a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599a24.md#insn-00599a40) · [`00599a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599a24.md#insn-00599a60)
- 新版 `00599a80`（命令位置の公開資料なし） · `00599aa0`（命令位置の公開資料なし）

~~~diff
- 00599a40 ["INT_ADD", "register:40f0:8", ["const:599a40:8", "const:4:8"]]
- 00599a40 ["CALL", null, ["callee:00c53da0:8"]]
+ 00599a80 ["INT_ADD", "register:40f0:8", ["const:599a80:8", "const:4:8"]]
+ 00599a80 ["CALL", null, ["callee:00c53da0:8"]]
- 00599a40 bytes b0e81a94
+ 00599a80 bytes c8e81a94
- 00599a60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00599a60 ["INT_ADD", "register:40f0:8", ["const:599a60:8", "const:4:8"]]
- 00599a60 ["CALLIND", null, ["register:0:8"]]
+ 00599aa0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00599aa0 ["INT_ADD", "register:40f0:8", ["const:599aa0:8", "const:4:8"]]
+ 00599aa0 ["CALLIND", null, ["register:0:8"]]
- 00599a60 bytes 00013fd6
+ 00599aa0 bytes 00013fd6
~~~


<a id="compare-38789c6c14cfbeefe140352ed5011ea6"></a>

### [`00599c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599c70.md) → [`00599cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599cb0.md) FUN_00599cb0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0059a708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a708.md) [`0059ae18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059ae18.md) · 呼出先 4件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`0059a748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a748.md) [`0059ae58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059ae58.md) · 呼出先 4件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00599ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599c70.md#insn-00599ca8) · [`00599cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599c70.md#insn-00599cc8) · [`00599ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599c70.md#insn-00599ce0)
- 新版 `00599ce8`（命令位置の公開資料なし） · `00599d08`（命令位置の公開資料なし） · `00599d20`（命令位置の公開資料なし）

~~~diff
- 00599ca8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00599ca8 ["INT_ADD", "register:40f0:8", ["const:599ca8:8", "const:4:8"]]
- 00599ca8 ["CALLIND", null, ["register:0:8"]]
+ 00599ce8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00599ce8 ["INT_ADD", "register:40f0:8", ["const:599ce8:8", "const:4:8"]]
+ 00599ce8 ["CALLIND", null, ["register:0:8"]]
- 00599ca8 bytes 20013fd6
+ 00599ce8 bytes 20013fd6
- 00599cc8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00599cc8 ["INT_ADD", "register:40f0:8", ["const:599cc8:8", "const:4:8"]]
- 00599cc8 ["CALLIND", null, ["register:0:8"]]
+ 00599d08 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00599d08 ["INT_ADD", "register:40f0:8", ["const:599d08:8", "const:4:8"]]
+ 00599d08 ["CALLIND", null, ["register:0:8"]]
- 00599cc8 bytes 20013fd6
+ 00599d08 bytes 20013fd6
- 00599ce0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00599ce0 ["INT_ADD", "register:40f0:8", ["const:599ce0:8", "const:4:8"]]
- 00599ce0 ["CALLIND", null, ["register:0:8"]]
+ 00599d20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00599d20 ["INT_ADD", "register:40f0:8", ["const:599d20:8", "const:4:8"]]
+ 00599d20 ["CALLIND", null, ["register:0:8"]]
- 00599ce0 bytes 00013fd6
+ 00599d20 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b6d62394a4da96971b690fa662d25f1"></a>

### [`00599db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599db4.md) → [`00599df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599df4.md) FUN_00599df4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005ad7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md) [`005ae8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae8e4.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 2件 [`005ad820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad820.md) [`005ae924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ae/005ae924.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00599dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599db4.md#insn-00599dd0) · [`00599df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599db4.md#insn-00599df0)
- 新版 `00599e10`（命令位置の公開資料なし） · `00599e30`（命令位置の公開資料なし）

~~~diff
- 00599dd0 ["INT_ADD", "register:40f0:8", ["const:599dd0:8", "const:4:8"]]
- 00599dd0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00599e10 ["INT_ADD", "register:40f0:8", ["const:599e10:8", "const:4:8"]]
+ 00599e10 ["CALL", null, ["callee:00c53da0:8"]]
- 00599dd0 bytes cce71a94
+ 00599e10 bytes e4e71a94
- 00599df0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00599df0 ["INT_ADD", "register:40f0:8", ["const:599df0:8", "const:4:8"]]
- 00599df0 ["CALLIND", null, ["register:0:8"]]
+ 00599e30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00599e30 ["INT_ADD", "register:40f0:8", ["const:599e30:8", "const:4:8"]]
+ 00599e30 ["CALLIND", null, ["register:0:8"]]
- 00599df0 bytes 00013fd6
+ 00599e30 bytes 00013fd6
~~~


<a id="compare-4ecdfdd66e7e1614e94b12572965b169"></a>

### [`00599e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599e04.md) → [`00599e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599e44.md) FUN_00599e44

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005ad7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md) [`005ae8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae8e4.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 2件 [`005ad820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad820.md) [`005ae924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ae/005ae924.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00599e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599e04.md#insn-00599e20) · [`00599e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599e04.md#insn-00599e40)
- 新版 `00599e60`（命令位置の公開資料なし） · `00599e80`（命令位置の公開資料なし）

~~~diff
- 00599e20 ["INT_ADD", "register:40f0:8", ["const:599e20:8", "const:4:8"]]
- 00599e20 ["CALL", null, ["callee:00c53da0:8"]]
+ 00599e60 ["INT_ADD", "register:40f0:8", ["const:599e60:8", "const:4:8"]]
+ 00599e60 ["CALL", null, ["callee:00c53da0:8"]]
- 00599e20 bytes b8e71a94
+ 00599e60 bytes d0e71a94
- 00599e40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00599e40 ["INT_ADD", "register:40f0:8", ["const:599e40:8", "const:4:8"]]
- 00599e40 ["CALLIND", null, ["register:0:8"]]
+ 00599e80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00599e80 ["INT_ADD", "register:40f0:8", ["const:599e80:8", "const:4:8"]]
+ 00599e80 ["CALLIND", null, ["register:0:8"]]
- 00599e40 bytes 00013fd6
+ 00599e80 bytes 00013fd6
~~~


<a id="compare-0419092e20b98cb8b641d3918a5f485b"></a>

### [`00599f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599f38.md) → [`00599f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599f78.md) FUN_00599f78

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00599e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599e54.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00599e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599e94.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00599f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599f38.md#insn-00599f48)
- 新版 `00599f88`（命令位置の公開資料なし）

~~~diff
- 00599f48 ["INT_ADD", "register:40f0:8", ["const:599f48:8", "const:4:8"]]
- 00599f48 ["CALL", null, ["callee:00599e94:8"]]
+ 00599f88 ["INT_ADD", "register:40f0:8", ["const:599f88:8", "const:4:8"]]
+ 00599f88 ["CALL", null, ["callee:00599e94:8"]]
- 00599f48 bytes c3ffff97
+ 00599f88 bytes c3ffff97
~~~


<a id="compare-c932ba5a2164443cca8c9f3aa0a5468b"></a>

### [`0059a130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a130.md) → [`0059a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a170.md) FUN_0059a170

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059a16c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a130.md#insn-0059a16c)
- 新版 `0059a1ac`（命令位置の公開資料なし）

~~~diff
- 0059a16c ["COPY", "register:0:8", ["register:4040:8"]]
- 0059a16c ["INT_ADD", "register:40f0:8", ["const:59a16c:8", "const:4:8"]]
- 0059a16c ["CALLIND", null, ["register:0:8"]]
+ 0059a1ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059a1ac ["INT_ADD", "register:40f0:8", ["const:59a1ac:8", "const:4:8"]]
+ 0059a1ac ["CALLIND", null, ["register:0:8"]]
- 0059a16c bytes 00013fd6
+ 0059a1ac bytes 00013fd6
~~~


<a id="compare-5dfa4bae919b70ae0fbb0db9b64caa3d"></a>

### [`0059a180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a180.md) → [`0059a1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a1c0.md) FUN_0059a1c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059a19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a180.md#insn-0059a19c)
- 新版 `0059a1dc`（命令位置の公開資料なし）

~~~diff
- 0059a19c ["INT_ADD", "register:40f0:8", ["const:59a19c:8", "const:4:8"]]
- 0059a19c ["CALL", null, ["callee:00459db4:8"]]
+ 0059a1dc ["INT_ADD", "register:40f0:8", ["const:59a1dc:8", "const:4:8"]]
+ 0059a1dc ["CALL", null, ["callee:00459db4:8"]]
- 0059a19c bytes f6fefa97
+ 0059a1dc bytes f6fefa97
~~~


<a id="compare-2db0c4ca859320a370068a00b83c3934"></a>

### [`0059a1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a1c8.md) → [`0059a208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a208.md) FUN_0059a208

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00598b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b3c.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00598b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b7c.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059a234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a1c8.md#insn-0059a234) · [`0059a244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a1c8.md#insn-0059a244) · [`0059a264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a1c8.md#insn-0059a264)
- 新版 `0059a274`（命令位置の公開資料なし） · `0059a284`（命令位置の公開資料なし） · `0059a2a4`（命令位置の公開資料なし）

~~~diff
- 0059a234 ["COPY", "register:0:8", ["register:4040:8"]]
- 0059a234 ["INT_ADD", "register:40f0:8", ["const:59a234:8", "const:4:8"]]
- 0059a234 ["CALLIND", null, ["register:0:8"]]
+ 0059a274 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059a274 ["INT_ADD", "register:40f0:8", ["const:59a274:8", "const:4:8"]]
+ 0059a274 ["CALLIND", null, ["register:0:8"]]
- 0059a234 bytes 00013fd6
+ 0059a274 bytes 00013fd6
- 0059a244 ["COPY", "register:0:8", ["register:4040:8"]]
- 0059a244 ["INT_ADD", "register:40f0:8", ["const:59a244:8", "const:4:8"]]
- 0059a244 ["CALLIND", null, ["register:0:8"]]
+ 0059a284 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059a284 ["INT_ADD", "register:40f0:8", ["const:59a284:8", "const:4:8"]]
+ 0059a284 ["CALLIND", null, ["register:0:8"]]
- 0059a244 bytes 00013fd6
+ 0059a284 bytes 00013fd6
- 0059a264 ["COPY", "register:0:8", ["register:4040:8"]]
- 0059a264 ["INT_ADD", "register:40f0:8", ["const:59a264:8", "const:4:8"]]
- 0059a264 ["CALLIND", null, ["register:0:8"]]
+ 0059a2a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059a2a4 ["INT_ADD", "register:40f0:8", ["const:59a2a4:8", "const:4:8"]]
+ 0059a2a4 ["CALLIND", null, ["register:0:8"]]
- 0059a264 bytes 00013fd6
+ 0059a2a4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ae43941e4887c15d605cb858a173070"></a>

### [`0059a330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a330.md) → [`0059a370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a370.md) FUN_0059a370

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00598d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598d34.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059a39c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a330.md#insn-0059a39c) · [`0059a3ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a330.md#insn-0059a3ac) · [`0059a3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a330.md#insn-0059a3cc)
- 新版 `0059a3dc`（命令位置の公開資料なし） · `0059a3ec`（命令位置の公開資料なし） · `0059a40c`（命令位置の公開資料なし）

~~~diff
- 0059a39c ["COPY", "register:0:8", ["register:4040:8"]]
- 0059a39c ["INT_ADD", "register:40f0:8", ["const:59a39c:8", "const:4:8"]]
- 0059a39c ["CALLIND", null, ["register:0:8"]]
+ 0059a3dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059a3dc ["INT_ADD", "register:40f0:8", ["const:59a3dc:8", "const:4:8"]]
+ 0059a3dc ["CALLIND", null, ["register:0:8"]]
- 0059a39c bytes 00013fd6
+ 0059a3dc bytes 00013fd6
- 0059a3ac ["COPY", "register:0:8", ["register:4040:8"]]
- 0059a3ac ["INT_ADD", "register:40f0:8", ["const:59a3ac:8", "const:4:8"]]
- 0059a3ac ["CALLIND", null, ["register:0:8"]]
+ 0059a3ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059a3ec ["INT_ADD", "register:40f0:8", ["const:59a3ec:8", "const:4:8"]]
+ 0059a3ec ["CALLIND", null, ["register:0:8"]]
- 0059a3ac bytes 00013fd6
+ 0059a3ec bytes 00013fd6
- 0059a3cc ["COPY", "register:0:8", ["register:4040:8"]]
- 0059a3cc ["INT_ADD", "register:40f0:8", ["const:59a3cc:8", "const:4:8"]]
- 0059a3cc ["CALLIND", null, ["register:0:8"]]
+ 0059a40c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059a40c ["INT_ADD", "register:40f0:8", ["const:59a40c:8", "const:4:8"]]
+ 0059a40c ["CALLIND", null, ["register:0:8"]]
- 0059a3cc bytes 00013fd6
+ 0059a40c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5af8bb03856b7b2fd4b93d4ca355edb"></a>

### [`0059a68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a68c.md) → [`0059a6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a6cc.md) FUN_0059a6cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059a6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a68c.md#insn-0059a6a8)
- 新版 `0059a6e8`（命令位置の公開資料なし）

~~~diff
- 0059a6a8 ["INT_ADD", "register:40f0:8", ["const:59a6a8:8", "const:4:8"]]
- 0059a6a8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0059a6e8 ["INT_ADD", "register:40f0:8", ["const:59a6e8:8", "const:4:8"]]
+ 0059a6e8 ["CALL", null, ["callee:00c57f80:8"]]
- 0059a6a8 bytes 02f61a94
+ 0059a6e8 bytes 26f61a94
~~~


<a id="compare-af07347ee015eb911259950e0b98f2d0"></a>

### [`0059a6cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a6cc.md) → [`0059a70c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a70c.md) FUN_0059a70c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00598dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598dc0.md) · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00598e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598e00.md) · 呼出先 2件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059a6e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a6cc.md#insn-0059a6e8) · [`0059a6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a6cc.md#insn-0059a6f4)
- 新版 `0059a728`（命令位置の公開資料なし） · `0059a734`（命令位置の公開資料なし）

~~~diff
- 0059a6e8 ["INT_ADD", "register:40f0:8", ["const:59a6e8:8", "const:4:8"]]
- 0059a6e8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0059a728 ["INT_ADD", "register:40f0:8", ["const:59a728:8", "const:4:8"]]
+ 0059a728 ["CALL", null, ["callee:00c57f80:8"]]
- 0059a6e8 bytes f2f51a94
+ 0059a728 bytes 16f61a94
- 0059a6f4 ["INT_ADD", "register:40f0:8", ["const:59a6f4:8", "const:4:8"]]
- 0059a6f4 ["CALL", null, ["callee:00c57f50:8"]]
+ 0059a734 ["INT_ADD", "register:40f0:8", ["const:59a734:8", "const:4:8"]]
+ 0059a734 ["CALL", null, ["callee:00c57f50:8"]]
- 0059a6f4 bytes e3f51a94
+ 0059a734 bytes 07f61a94
~~~


<a id="compare-59bfcf7ba6bd2e1361fb849cea82ff8b"></a>

### [`0059a708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a708.md) → [`0059a748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a748.md) FUN_0059a748

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00596f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596f2c.md) [`005996b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/005996b4.md) [`00599a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599a74.md) [`00599c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599c70.md) [`00795e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e24.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00596f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596f6c.md) [`005996f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/005996f4.md) [`00599ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599ab4.md) [`00599cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599cb0.md) [`00795e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795e7c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059a748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a708.md#insn-0059a748) · [`0059a770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a708.md#insn-0059a770) · [`0059a788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a708.md#insn-0059a788)
- 新版 `0059a788`（命令位置の公開資料なし） · `0059a7b0`（命令位置の公開資料なし） · `0059a7c8`（命令位置の公開資料なし）

~~~diff
- 0059a748 ["INT_ADD", "register:40f0:8", ["const:59a748:8", "const:4:8"]]
- 0059a748 ["CALL", null, ["callee:00c585c0:8"]]
+ 0059a788 ["INT_ADD", "register:40f0:8", ["const:59a788:8", "const:4:8"]]
+ 0059a788 ["CALL", null, ["callee:00c585c0:8"]]
- 0059a748 bytes 6af71a94
+ 0059a788 bytes 8ef71a94
- 0059a770 ["COPY", "register:0:8", ["register:4040:8"]]
- 0059a770 ["INT_ADD", "register:40f0:8", ["const:59a770:8", "const:4:8"]]
- 0059a770 ["CALLIND", null, ["register:0:8"]]
+ 0059a7b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059a7b0 ["INT_ADD", "register:40f0:8", ["const:59a7b0:8", "const:4:8"]]
+ 0059a7b0 ["CALLIND", null, ["register:0:8"]]
- 0059a770 bytes 00013fd6
+ 0059a7b0 bytes 00013fd6
- 0059a788 ["COPY", "register:0:8", ["register:4048:8"]]
- 0059a788 ["INT_ADD", "register:40f0:8", ["const:59a788:8", "const:4:8"]]
- 0059a788 ["CALLIND", null, ["register:0:8"]]
+ 0059a7c8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0059a7c8 ["INT_ADD", "register:40f0:8", ["const:59a7c8:8", "const:4:8"]]
+ 0059a7c8 ["CALLIND", null, ["register:0:8"]]
- 0059a788 bytes 20013fd6
+ 0059a7c8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e1a1b404ee0bacdd347fba168e5ec80"></a>

### [`0059ad54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059ad54.md) → [`0059ad94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059ad94.md) FUN_0059ad94

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059ad70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059ad54.md#insn-0059ad70) · [`0059ad84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059ad54.md#insn-0059ad84) · [`0059ada4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059ad54.md#insn-0059ada4)
- 新版 `0059adb0`（命令位置の公開資料なし） · `0059adc4`（命令位置の公開資料なし） · `0059ade4`（命令位置の公開資料なし）

~~~diff
- 0059ad70 ["INT_ADD", "register:40f0:8", ["const:59ad70:8", "const:4:8"]]
- 0059ad70 ["CALL", null, ["callee:00c57f80:8"]]
+ 0059adb0 ["INT_ADD", "register:40f0:8", ["const:59adb0:8", "const:4:8"]]
+ 0059adb0 ["CALL", null, ["callee:00c57f80:8"]]
- 0059ad70 bytes 50f41a94
+ 0059adb0 bytes 74f41a94
- 0059ad84 ["INT_ADD", "register:40f0:8", ["const:59ad84:8", "const:4:8"]]
- 0059ad84 ["CALL", null, ["callee:00c53da0:8"]]
+ 0059adc4 ["INT_ADD", "register:40f0:8", ["const:59adc4:8", "const:4:8"]]
+ 0059adc4 ["CALL", null, ["callee:00c53da0:8"]]
- 0059ad84 bytes dfe31a94
+ 0059adc4 bytes f7e31a94
- 0059ada4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0059ada4 ["INT_ADD", "register:40f0:8", ["const:59ada4:8", "const:4:8"]]
- 0059ada4 ["CALLIND", null, ["register:0:8"]]
+ 0059ade4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059ade4 ["INT_ADD", "register:40f0:8", ["const:59ade4:8", "const:4:8"]]
+ 0059ade4 ["CALLIND", null, ["register:0:8"]]
- 0059ada4 bytes 00013fd6
+ 0059ade4 bytes 00013fd6
~~~


<a id="compare-3f430b0db0a8bfb018b540930ae02bc9"></a>

### [`0059adb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059adb8.md) → [`0059adf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059adf8.md) FUN_0059adf8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0059925c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/0059925c.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0059929c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/0059929c.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059add4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059adb8.md#insn-0059add4) · [`0059ade8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059adb8.md#insn-0059ade8) · [`0059adfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059adb8.md#insn-0059adfc)
- 新版 `0059ae14`（命令位置の公開資料なし） · `0059ae28`（命令位置の公開資料なし） · `0059ae3c`（命令位置の公開資料なし）

~~~diff
- 0059add4 ["INT_ADD", "register:40f0:8", ["const:59add4:8", "const:4:8"]]
- 0059add4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0059ae14 ["INT_ADD", "register:40f0:8", ["const:59ae14:8", "const:4:8"]]
+ 0059ae14 ["CALL", null, ["callee:00c57f80:8"]]
- 0059add4 bytes 37f41a94
+ 0059ae14 bytes 5bf41a94
- 0059ade8 ["INT_ADD", "register:40f0:8", ["const:59ade8:8", "const:4:8"]]
- 0059ade8 ["CALL", null, ["callee:00c53da0:8"]]
+ 0059ae28 ["INT_ADD", "register:40f0:8", ["const:59ae28:8", "const:4:8"]]
+ 0059ae28 ["CALL", null, ["callee:00c53da0:8"]]
- 0059ade8 bytes c6e31a94
+ 0059ae28 bytes dee31a94
- 0059adfc ["COPY", "register:0:8", ["register:4040:8"]]
- 0059adfc ["INT_ADD", "register:40f0:8", ["const:59adfc:8", "const:4:8"]]
- 0059adfc ["CALLIND", null, ["register:0:8"]]
+ 0059ae3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059ae3c ["INT_ADD", "register:40f0:8", ["const:59ae3c:8", "const:4:8"]]
+ 0059ae3c ["CALLIND", null, ["register:0:8"]]
- 0059adfc bytes 00013fd6
+ 0059ae3c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66063ae480b7e6c1f0d3585922733df2"></a>

### [`0059ae18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059ae18.md) → [`0059ae58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059ae58.md) FUN_0059ae58

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00596f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596f2c.md) [`005996b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/005996b4.md) [`00599a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599a74.md) [`00599c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599c70.md) [`00795e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e24.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00596f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596f6c.md) [`005996f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/005996f4.md) [`00599ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599ab4.md) [`00599cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599cb0.md) [`00795e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795e7c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059ae5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059ae18.md#insn-0059ae5c) · [`0059ae78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059ae18.md#insn-0059ae78) · [`0059ae9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059ae18.md#insn-0059ae9c)
- 新版 `0059ae9c`（命令位置の公開資料なし） · `0059aeb8`（命令位置の公開資料なし） · `0059aedc`（命令位置の公開資料なし）

~~~diff
- 0059ae5c ["COPY", "register:0:8", ["register:4048:8"]]
- 0059ae5c ["INT_ADD", "register:40f0:8", ["const:59ae5c:8", "const:4:8"]]
- 0059ae5c ["CALLIND", null, ["register:0:8"]]
+ 0059ae9c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0059ae9c ["INT_ADD", "register:40f0:8", ["const:59ae9c:8", "const:4:8"]]
+ 0059ae9c ["CALLIND", null, ["register:0:8"]]
- 0059ae5c bytes 20013fd6
+ 0059ae9c bytes 20013fd6
- 0059ae78 ["COPY", "register:0:8", ["register:4050:8"]]
- 0059ae78 ["INT_ADD", "register:40f0:8", ["const:59ae78:8", "const:4:8"]]
- 0059ae78 ["CALLIND", null, ["register:0:8"]]
+ 0059aeb8 ["COPY", "register:0:8", ["register:4050:8"]]
+ 0059aeb8 ["INT_ADD", "register:40f0:8", ["const:59aeb8:8", "const:4:8"]]
+ 0059aeb8 ["CALLIND", null, ["register:0:8"]]
- 0059ae78 bytes 40013fd6
+ 0059aeb8 bytes 40013fd6
- 0059ae9c ["INT_ADD", "register:40f0:8", ["const:59ae9c:8", "const:4:8"]]
- 0059ae9c ["CALL", null, ["callee:00c53d70:8"]]
+ 0059aedc ["INT_ADD", "register:40f0:8", ["const:59aedc:8", "const:4:8"]]
+ 0059aedc ["CALL", null, ["callee:00c53d70:8"]]
- 0059ae9c bytes 8de31a94
+ 0059aedc bytes a5e31a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-216466993ca185e0058d8cff31cf0d57"></a>

### [`0059b340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b340.md) → [`0059b380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b380.md) FUN_0059b380

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00599804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599804.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00599844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599844.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059b35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b340.md#insn-0059b35c) · [`0059b37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b340.md#insn-0059b37c)
- 新版 `0059b39c`（命令位置の公開資料なし） · `0059b3bc`（命令位置の公開資料なし）

~~~diff
- 0059b35c ["INT_ADD", "register:40f0:8", ["const:59b35c:8", "const:4:8"]]
- 0059b35c ["CALL", null, ["callee:00c53da0:8"]]
+ 0059b39c ["INT_ADD", "register:40f0:8", ["const:59b39c:8", "const:4:8"]]
+ 0059b39c ["CALL", null, ["callee:00c53da0:8"]]
- 0059b35c bytes 69e21a94
+ 0059b39c bytes 81e21a94
- 0059b37c ["COPY", "register:0:8", ["register:4040:8"]]
- 0059b37c ["INT_ADD", "register:40f0:8", ["const:59b37c:8", "const:4:8"]]
- 0059b37c ["CALLIND", null, ["register:0:8"]]
+ 0059b3bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059b3bc ["INT_ADD", "register:40f0:8", ["const:59b3bc:8", "const:4:8"]]
+ 0059b3bc ["CALLIND", null, ["register:0:8"]]
- 0059b37c bytes 00013fd6
+ 0059b3bc bytes 00013fd6
~~~


<a id="compare-dbae13dde0cf5ec3568042a96e4839b9"></a>

### [`0059b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b390.md) → [`0059b3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b3d0.md) FUN_0059b3d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00599804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599804.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00599844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599844.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059b3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b390.md#insn-0059b3b0) · [`0059b3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b390.md#insn-0059b3c4) · [`0059b3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b390.md#insn-0059b3cc)
- 新版 `0059b3f0`（命令位置の公開資料なし） · `0059b404`（命令位置の公開資料なし） · `0059b40c`（命令位置の公開資料なし）

~~~diff
- 0059b3b0 ["INT_ADD", "register:40f0:8", ["const:59b3b0:8", "const:4:8"]]
- 0059b3b0 ["CALL", null, ["callee:00c53da0:8"]]
+ 0059b3f0 ["INT_ADD", "register:40f0:8", ["const:59b3f0:8", "const:4:8"]]
+ 0059b3f0 ["CALL", null, ["callee:00c53da0:8"]]
- 0059b3b0 bytes 54e21a94
+ 0059b3f0 bytes 6ce21a94
- 0059b3c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0059b3c4 ["INT_ADD", "register:40f0:8", ["const:59b3c4:8", "const:4:8"]]
- 0059b3c4 ["CALLIND", null, ["register:0:8"]]
+ 0059b404 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059b404 ["INT_ADD", "register:40f0:8", ["const:59b404:8", "const:4:8"]]
+ 0059b404 ["CALLIND", null, ["register:0:8"]]
- 0059b3c4 bytes 00013fd6
+ 0059b404 bytes 00013fd6
- 0059b3cc ["INT_ADD", "register:40f0:8", ["const:59b3cc:8", "const:4:8"]]
- 0059b3cc ["CALL", null, ["callee:00c57f50:8"]]
+ 0059b40c ["INT_ADD", "register:40f0:8", ["const:59b40c:8", "const:4:8"]]
+ 0059b40c ["CALL", null, ["callee:00c57f50:8"]]
- 0059b3cc bytes adf21a94
+ 0059b40c bytes d1f21a94
~~~


<a id="compare-95fdf69ad4f4c73c2cc84573d1e523bd"></a>

### [`0059d3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059d3f4.md) → [`0059d434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059d/0059d434.md) FUN_0059d434

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0059bf44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059bf44.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) [`0059bf84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059bf84.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059d420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059d3f4.md#insn-0059d420) · [`0059d450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059d3f4.md#insn-0059d450) · [`0059d460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059d3f4.md#insn-0059d460)
- 新版 `0059d460`（命令位置の公開資料なし） · `0059d490`（命令位置の公開資料なし） · `0059d4a0`（命令位置の公開資料なし）

~~~diff
- 0059d420 ["INT_ADD", "register:40f0:8", ["const:59d420:8", "const:4:8"]]
- 0059d420 ["CALL", null, ["callee:0059bf84:8"]]
+ 0059d460 ["INT_ADD", "register:40f0:8", ["const:59d460:8", "const:4:8"]]
+ 0059d460 ["CALL", null, ["callee:0059bf84:8"]]
- 0059d420 bytes c9faff97
+ 0059d460 bytes c9faff97
- 0059d450 ["INT_ADD", "register:40f0:8", ["const:59d450:8", "const:4:8"]]
- 0059d450 ["CALL", null, ["callee:004517dc:8"]]
+ 0059d490 ["INT_ADD", "register:40f0:8", ["const:59d490:8", "const:4:8"]]
+ 0059d490 ["CALL", null, ["callee:004517dc:8"]]
- 0059d450 bytes d3d0fa97
+ 0059d490 bytes d3d0fa97
- 0059d460 ["INT_ADD", "register:40f0:8", ["const:59d460:8", "const:4:8"]]
- 0059d460 ["CALL", null, ["callee:00c57f80:8"]]
+ 0059d4a0 ["INT_ADD", "register:40f0:8", ["const:59d4a0:8", "const:4:8"]]
+ 0059d4a0 ["CALL", null, ["callee:00c57f80:8"]]
- 0059d460 bytes 94ea1a94
+ 0059d4a0 bytes b8ea1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6287eddb49c9c3b3a7c10c34bfeb5492"></a>

### [`0059ebfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059ebfc.md) → [`0059ec3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059e/0059ec3c.md) FUN_0059ec3c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0059bf44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059bf44.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) [`0059bf84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059bf84.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059ec28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059ebfc.md#insn-0059ec28) · [`0059ec5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059ebfc.md#insn-0059ec5c) · [`0059ec6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059ebfc.md#insn-0059ec6c)
- 新版 `0059ec68`（命令位置の公開資料なし） · `0059ec9c`（命令位置の公開資料なし） · `0059ecac`（命令位置の公開資料なし）

~~~diff
- 0059ec28 ["INT_ADD", "register:40f0:8", ["const:59ec28:8", "const:4:8"]]
- 0059ec28 ["CALL", null, ["callee:0059bf84:8"]]
+ 0059ec68 ["INT_ADD", "register:40f0:8", ["const:59ec68:8", "const:4:8"]]
+ 0059ec68 ["CALL", null, ["callee:0059bf84:8"]]
- 0059ec28 bytes c7f4ff97
+ 0059ec68 bytes c7f4ff97
- 0059ec5c ["INT_ADD", "register:40f0:8", ["const:59ec5c:8", "const:4:8"]]
- 0059ec5c ["CALL", null, ["callee:004517dc:8"]]
+ 0059ec9c ["INT_ADD", "register:40f0:8", ["const:59ec9c:8", "const:4:8"]]
+ 0059ec9c ["CALL", null, ["callee:004517dc:8"]]
- 0059ec5c bytes d0cafa97
+ 0059ec9c bytes d0cafa97
- 0059ec6c ["INT_ADD", "register:40f0:8", ["const:59ec6c:8", "const:4:8"]]
- 0059ec6c ["CALL", null, ["callee:00c57f80:8"]]
+ 0059ecac ["INT_ADD", "register:40f0:8", ["const:59ecac:8", "const:4:8"]]
+ 0059ecac ["CALL", null, ["callee:00c57f80:8"]]
- 0059ec6c bytes 91e41a94
+ 0059ecac bytes b5e41a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0272145d8c0a010ad85b86dd68940c1"></a>

### [`0059f5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059f5a0.md) → [`0059f5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059f/0059f5e0.md) FUN_0059f5e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0059bf44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059bf44.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) [`0059bf84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059bf84.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059f5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059f5a0.md#insn-0059f5cc) · [`0059f600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059f5a0.md#insn-0059f600) · [`0059f610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059f5a0.md#insn-0059f610)
- 新版 `0059f60c`（命令位置の公開資料なし） · `0059f640`（命令位置の公開資料なし） · `0059f650`（命令位置の公開資料なし）

~~~diff
- 0059f5cc ["INT_ADD", "register:40f0:8", ["const:59f5cc:8", "const:4:8"]]
- 0059f5cc ["CALL", null, ["callee:0059bf84:8"]]
+ 0059f60c ["INT_ADD", "register:40f0:8", ["const:59f60c:8", "const:4:8"]]
+ 0059f60c ["CALL", null, ["callee:0059bf84:8"]]
- 0059f5cc bytes 5ef2ff97
+ 0059f60c bytes 5ef2ff97
- 0059f600 ["INT_ADD", "register:40f0:8", ["const:59f600:8", "const:4:8"]]
- 0059f600 ["CALL", null, ["callee:004517dc:8"]]
+ 0059f640 ["INT_ADD", "register:40f0:8", ["const:59f640:8", "const:4:8"]]
+ 0059f640 ["CALL", null, ["callee:004517dc:8"]]
- 0059f600 bytes 67c8fa97
+ 0059f640 bytes 67c8fa97
- 0059f610 ["INT_ADD", "register:40f0:8", ["const:59f610:8", "const:4:8"]]
- 0059f610 ["CALL", null, ["callee:00c57f80:8"]]
+ 0059f650 ["INT_ADD", "register:40f0:8", ["const:59f650:8", "const:4:8"]]
+ 0059f650 ["CALL", null, ["callee:00c57f80:8"]]
- 0059f610 bytes 28e21a94
+ 0059f650 bytes 4ce21a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ade6e17330a0a63bf43c0e8abe7dee3"></a>

### [`005a1350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1350.md) → [`005a1390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1390.md) FUN_005a1390

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a139c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1350.md#insn-005a139c)
- 新版 `005a13dc`（命令位置の公開資料なし）

~~~diff
- 005a139c ["INT_ADD", "register:40f0:8", ["const:5a139c:8", "const:4:8"]]
- 005a139c ["CALL", null, ["callee:00c57f80:8"]]
+ 005a13dc ["INT_ADD", "register:40f0:8", ["const:5a13dc:8", "const:4:8"]]
+ 005a13dc ["CALL", null, ["callee:00c57f80:8"]]
- 005a139c bytes c5da1a94
+ 005a13dc bytes e9da1a94
~~~


<a id="compare-387487aee1b2efbb1d17483abe5c31cc"></a>

### [`005a17d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a17d4.md) → [`005a1814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1814.md) FUN_005a1814

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005a1728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1728.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005a1768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1768.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a17e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a17d4.md#insn-005a17e4)
- 新版 `005a1824`（命令位置の公開資料なし）

~~~diff
- 005a17e4 ["INT_ADD", "register:40f0:8", ["const:5a17e4:8", "const:4:8"]]
- 005a17e4 ["CALL", null, ["callee:005a1768:8"]]
+ 005a1824 ["INT_ADD", "register:40f0:8", ["const:5a1824:8", "const:4:8"]]
+ 005a1824 ["CALL", null, ["callee:005a1768:8"]]
- 005a17e4 bytes d1ffff97
+ 005a1824 bytes d1ffff97
~~~


<a id="compare-0a16aa903d1b5540d2803c36accf781f"></a>

### [`005a1920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1920.md) → [`005a1960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1960.md) FUN_005a1960

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a1de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1de0.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005a1a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1a80.md) [`005a1b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1b0c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`005a1e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1e20.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`005a1ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1ac0.md) [`005a1b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1b4c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a197c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1920.md#insn-005a197c) · [`005a19f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1920.md#insn-005a19f0) · [`005a1a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1920.md#insn-005a1a40)
- 新版 `005a19bc`（命令位置の公開資料なし） · `005a1a30`（命令位置の公開資料なし） · `005a1a80`（命令位置の公開資料なし）

~~~diff
- 005a197c ["INT_ADD", "register:40f0:8", ["const:5a197c:8", "const:4:8"]]
- 005a197c ["CALL", null, ["callee:00c57f60:8"]]
+ 005a19bc ["INT_ADD", "register:40f0:8", ["const:5a19bc:8", "const:4:8"]]
+ 005a19bc ["CALL", null, ["callee:00c57f60:8"]]
- 005a197c bytes 45d91a94
+ 005a19bc bytes 69d91a94
- 005a19f0 ["INT_ADD", "register:40f0:8", ["const:5a19f0:8", "const:4:8"]]
- 005a19f0 ["CALL", null, ["callee:0043bb60:8"]]
+ 005a1a30 ["INT_ADD", "register:40f0:8", ["const:5a1a30:8", "const:4:8"]]
+ 005a1a30 ["CALL", null, ["callee:0043bb60:8"]]
- 005a19f0 bytes 4c68fa97
+ 005a1a30 bytes 4c68fa97
- 005a1a40 ["INT_ADD", "register:40f0:8", ["const:5a1a40:8", "const:4:8"]]
- 005a1a40 ["CALL", null, ["callee:005a1b4c:8"]]
+ 005a1a80 ["INT_ADD", "register:40f0:8", ["const:5a1a80:8", "const:4:8"]]
+ 005a1a80 ["CALL", null, ["callee:005a1b4c:8"]]
- 005a1a40 bytes 33000094
+ 005a1a80 bytes 33000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e27c2667770614422985b607f5102cb"></a>

### [`005a1a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1a80.md) → [`005a1ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1ac0.md) FUN_005a1ac0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a1920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1920.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005a1960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1960.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a1ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1a80.md#insn-005a1ae8)
- 新版 `005a1b28`（命令位置の公開資料なし）

~~~diff
- 005a1ae8 ["INT_ADD", "register:40f0:8", ["const:5a1ae8:8", "const:4:8"]]
- 005a1ae8 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a1b28 ["INT_ADD", "register:40f0:8", ["const:5a1b28:8", "const:4:8"]]
+ 005a1b28 ["CALL", null, ["callee:00c57f80:8"]]
- 005a1ae8 bytes f2d81a94
+ 005a1b28 bytes 16d91a94
~~~


<a id="compare-f8b0fd9c0b90e2daea44d6c47a4b90b6"></a>

### [`005a1b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1b20.md) → [`005a1b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1b60.md) FUN_005a1b60

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a1b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1b20.md#insn-005a1b6c)
- 新版 `005a1bac`（命令位置の公開資料なし）

~~~diff
- 005a1b6c ["INT_ADD", "register:40f0:8", ["const:5a1b6c:8", "const:4:8"]]
- 005a1b6c ["CALL", null, ["callee:00c57f80:8"]]
+ 005a1bac ["INT_ADD", "register:40f0:8", ["const:5a1bac:8", "const:4:8"]]
+ 005a1bac ["CALL", null, ["callee:00c57f80:8"]]
- 005a1b6c bytes d1d81a94
+ 005a1bac bytes f5d81a94
~~~


<a id="compare-616af47580a05078f59a6bab98e44c99"></a>

### [`005a1b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1b80.md) → [`005a1bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1bc0.md) FUN_005a1bc0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a0e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0e94.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005a1b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1b0c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005a0ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a0/005a0ed4.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`005a1b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1b4c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a1c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1b80.md#insn-005a1c24) · [`005a1c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1b80.md#insn-005a1c6c) · [`005a1cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1b80.md#insn-005a1cd0)
- 新版 `005a1c64`（命令位置の公開資料なし） · `005a1cac`（命令位置の公開資料なし） · `005a1d10`（命令位置の公開資料なし）

~~~diff
- 005a1c24 ["INT_ADD", "register:40f0:8", ["const:5a1c24:8", "const:4:8"]]
- 005a1c24 ["CALL", null, ["callee:00c57f60:8"]]
+ 005a1c64 ["INT_ADD", "register:40f0:8", ["const:5a1c64:8", "const:4:8"]]
+ 005a1c64 ["CALL", null, ["callee:00c57f60:8"]]
- 005a1c24 bytes 9bd81a94
+ 005a1c64 bytes bfd81a94
- 005a1c6c ["INT_ADD", "register:40f0:8", ["const:5a1c6c:8", "const:4:8"]]
- 005a1c6c ["CALL", null, ["callee:0043bb60:8"]]
+ 005a1cac ["INT_ADD", "register:40f0:8", ["const:5a1cac:8", "const:4:8"]]
+ 005a1cac ["CALL", null, ["callee:0043bb60:8"]]
- 005a1c6c bytes ad67fa97
+ 005a1cac bytes ad67fa97
- 005a1cd0 ["INT_ADD", "register:40f0:8", ["const:5a1cd0:8", "const:4:8"]]
- 005a1cd0 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a1d10 ["INT_ADD", "register:40f0:8", ["const:5a1d10:8", "const:4:8"]]
+ 005a1d10 ["CALL", null, ["callee:00c57f80:8"]]
- 005a1cd0 bytes 78d81a94
+ 005a1d10 bytes 9cd81a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04ede05dc9f91fe7ff8748d48d49137c"></a>

### [`005a1d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1d78.md) → [`005a1db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1db8.md) FUN_005a1db8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a1dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1d78.md#insn-005a1dc8)
- 新版 `005a1e08`（命令位置の公開資料なし）

~~~diff
- 005a1dc8 ["INT_ADD", "register:40f0:8", ["const:5a1dc8:8", "const:4:8"]]
- 005a1dc8 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a1e08 ["INT_ADD", "register:40f0:8", ["const:5a1e08:8", "const:4:8"]]
+ 005a1e08 ["CALL", null, ["callee:00c57f80:8"]]
- 005a1dc8 bytes 3ad81a94
+ 005a1e08 bytes 5ed81a94
~~~


<a id="compare-d7620d549bc562136eb66c33f2a0d717"></a>

### [`005a3e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3e6c.md) → [`005a3eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a3/005a3eac.md) FUN_005a3eac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a3e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3e6c.md#insn-005a3e88) · [`005a3eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3e6c.md#insn-005a3eb4) · [`005a3ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3e6c.md#insn-005a3ec4)
- 新版 `005a3ec8`（命令位置の公開資料なし） · `005a3ef4`（命令位置の公開資料なし） · `005a3f04`（命令位置の公開資料なし）

~~~diff
- 005a3e88 ["INT_ADD", "register:40f0:8", ["const:5a3e88:8", "const:4:8"]]
- 005a3e88 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a3ec8 ["INT_ADD", "register:40f0:8", ["const:5a3ec8:8", "const:4:8"]]
+ 005a3ec8 ["CALL", null, ["callee:00c57f80:8"]]
- 005a3e88 bytes 0ad01a94
+ 005a3ec8 bytes 2ed01a94
- 005a3eb4 ["INT_ADD", "register:40f0:8", ["const:5a3eb4:8", "const:4:8"]]
- 005a3eb4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a3ef4 ["INT_ADD", "register:40f0:8", ["const:5a3ef4:8", "const:4:8"]]
+ 005a3ef4 ["CALL", null, ["callee:00c57f80:8"]]
- 005a3eb4 bytes ffcf1a94
+ 005a3ef4 bytes 23d01a94
- 005a3ec4 ["INT_ADD", "register:40f0:8", ["const:5a3ec4:8", "const:4:8"]]
- 005a3ec4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a3f04 ["INT_ADD", "register:40f0:8", ["const:5a3f04:8", "const:4:8"]]
+ 005a3f04 ["CALL", null, ["callee:00c57f80:8"]]
- 005a3ec4 bytes fbcf1a94
+ 005a3f04 bytes 1fd01a94
~~~


<a id="compare-89d8a92f47c5e6d7f9a4e4e4b59a234b"></a>

### [`005a3ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3ee0.md) → [`005a3f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a3/005a3f20.md) FUN_005a3f20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005a4508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4508.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005a4548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4548.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a3ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3ee0.md#insn-005a3ef8)
- 新版 `005a3f38`（命令位置の公開資料なし）

~~~diff
- 005a3ef8 ["INT_ADD", "register:40f0:8", ["const:5a3ef8:8", "const:4:8"]]
- 005a3ef8 ["CALL", null, ["callee:005a4548:8"]]
+ 005a3f38 ["INT_ADD", "register:40f0:8", ["const:5a3f38:8", "const:4:8"]]
+ 005a3f38 ["CALL", null, ["callee:005a4548:8"]]
- 005a3ef8 bytes 84010094
+ 005a3f38 bytes 84010094
~~~


<a id="compare-f87bab4351cf0af0edc7daf999a65754"></a>

### [`005a40e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a40e4.md) → [`005a4124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4124.md) FUN_005a4124

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005a491c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a491c.md) [`0079a608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079a/0079a608.md) [`0079c3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079c3a0.md) · 呼出先 6件 [`005a4228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4228.md) [`005a426c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a426c.md) [`005a42a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a42a0.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 3件 [`005a495c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a495c.md) [`0079a660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a660.md) [`0079c3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c3f8.md) · 呼出先 6件 [`005a4268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4268.md) [`005a42ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a42ac.md) [`005a42e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a42e0.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a4140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a40e4.md#insn-005a4140) · [`005a4184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a40e4.md#insn-005a4184) · [`005a41e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a40e4.md#insn-005a41e8)
- 新版 `005a4180`（命令位置の公開資料なし） · `005a41c4`（命令位置の公開資料なし） · `005a4228`（命令位置の公開資料なし）

~~~diff
- 005a4140 ["INT_ADD", "register:40f0:8", ["const:5a4140:8", "const:4:8"]]
- 005a4140 ["CALL", null, ["callee:00c57f60:8"]]
+ 005a4180 ["INT_ADD", "register:40f0:8", ["const:5a4180:8", "const:4:8"]]
+ 005a4180 ["CALL", null, ["callee:00c57f60:8"]]
- 005a4140 bytes 54cf1a94
+ 005a4180 bytes 78cf1a94
- 005a4184 ["INT_ADD", "register:40f0:8", ["const:5a4184:8", "const:4:8"]]
- 005a4184 ["CALL", null, ["callee:005a42e0:8"]]
+ 005a41c4 ["INT_ADD", "register:40f0:8", ["const:5a41c4:8", "const:4:8"]]
+ 005a41c4 ["CALL", null, ["callee:005a42e0:8"]]
- 005a4184 bytes 47000094
+ 005a41c4 bytes 47000094
- 005a41e8 ["INT_ADD", "register:40f0:8", ["const:5a41e8:8", "const:4:8"]]
- 005a41e8 ["CALL", null, ["callee:005a42ac:8"]]
+ 005a4228 ["INT_ADD", "register:40f0:8", ["const:5a4228:8", "const:4:8"]]
+ 005a4228 ["CALL", null, ["callee:005a42ac:8"]]
- 005a41e8 bytes 21000094
+ 005a4228 bytes 21000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a3d8c04315f90afeec34df9ac0040e8"></a>

### [`005a4228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4228.md) → [`005a4268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4268.md) FUN_005a4268

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a40e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a40e4.md) · 呼出先 2件 [`005a4508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4508.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005a4124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4124.md) · 呼出先 2件 [`005a4548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4548.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a4254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4228.md#insn-005a4254)
- 新版 `005a4294`（命令位置の公開資料なし）

~~~diff
- 005a4254 ["INT_ADD", "register:40f0:8", ["const:5a4254:8", "const:4:8"]]
- 005a4254 ["CALL", null, ["callee:005a4548:8"]]
+ 005a4294 ["INT_ADD", "register:40f0:8", ["const:5a4294:8", "const:4:8"]]
+ 005a4294 ["CALL", null, ["callee:005a4548:8"]]
- 005a4254 bytes ad000094
+ 005a4294 bytes ad000094
~~~


<a id="compare-caeae6d47139ad1269bc883455df0a1c"></a>

### [`005a4280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4280.md) → [`005a42c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a42c0.md) FUN_005a42c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0079cc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079cc10.md) · 呼出先 1件 [`005a446c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a446c.md)
- 新版 呼出元 1件 [`0079cc68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cc68.md) · 呼出先 1件 [`005a44ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a44ac.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a4290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4280.md#insn-005a4290)
- 新版 `005a42d0`（命令位置の公開資料なし）

~~~diff
- 005a4290 ["INT_ADD", "register:40f0:8", ["const:5a4290:8", "const:4:8"]]
- 005a4290 ["CALL", null, ["callee:005a44ac:8"]]
+ 005a42d0 ["INT_ADD", "register:40f0:8", ["const:5a42d0:8", "const:4:8"]]
+ 005a42d0 ["CALL", null, ["callee:005a44ac:8"]]
- 005a4290 bytes 77000094
+ 005a42d0 bytes 77000094
~~~


<a id="compare-0b493c836129f9a5aea4605437b90420"></a>

### [`005a42a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a42a0.md) → [`005a42e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a42e0.md) FUN_005a42e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`005a3320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3320.md) [`005a40e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a40e4.md) [`005a4594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4594.md) [`00799c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00799/00799c94.md) [`0079a608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079a/0079a608.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 7件 [`005a3360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a3/005a3360.md) [`005a4124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4124.md) [`005a45d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a45d4.md) [`00799cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00799/00799cec.md) [`0079a660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a660.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a42dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a42a0.md#insn-005a42dc) · [`005a4310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a42a0.md#insn-005a4310) · [`005a4344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a42a0.md#insn-005a4344)
- 新版 `005a431c`（命令位置の公開資料なし） · `005a4350`（命令位置の公開資料なし） · `005a4384`（命令位置の公開資料なし）

~~~diff
- 005a42dc ["INT_ADD", "register:40f0:8", ["const:5a42dc:8", "const:4:8"]]
- 005a42dc ["CALL", null, ["callee:0043bb60:8"]]
+ 005a431c ["INT_ADD", "register:40f0:8", ["const:5a431c:8", "const:4:8"]]
+ 005a431c ["CALL", null, ["callee:0043bb60:8"]]
- 005a42dc bytes 115efa97
+ 005a431c bytes 115efa97
- 005a4310 ["INT_ADD", "register:40f0:8", ["const:5a4310:8", "const:4:8"]]
- 005a4310 ["CALL", null, ["callee:0043bb60:8"]]
+ 005a4350 ["INT_ADD", "register:40f0:8", ["const:5a4350:8", "const:4:8"]]
+ 005a4350 ["CALL", null, ["callee:0043bb60:8"]]
- 005a4310 bytes 045efa97
+ 005a4350 bytes 045efa97
- 005a4344 ["INT_ADD", "register:40f0:8", ["const:5a4344:8", "const:4:8"]]
- 005a4344 ["CALL", null, ["callee:0043bb60:8"]]
+ 005a4384 ["INT_ADD", "register:40f0:8", ["const:5a4384:8", "const:4:8"]]
+ 005a4384 ["CALL", null, ["callee:0043bb60:8"]]
- 005a4344 bytes f75dfa97
+ 005a4384 bytes f75dfa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58d1d50a6332663197cdbe6f06e6b393"></a>

### [`005a446c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a446c.md) → [`005a44ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a44ac.md) FUN_005a44ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a4280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4280.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005a42c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a42c0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a44b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a446c.md#insn-005a44b0) · [`005a44d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a446c.md#insn-005a44d4) · [`005a44e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a446c.md#insn-005a44e4)
- 新版 `005a44f0`（命令位置の公開資料なし） · `005a4514`（命令位置の公開資料なし） · `005a4524`（命令位置の公開資料なし）

~~~diff
- 005a44b0 ["INT_ADD", "register:40f0:8", ["const:5a44b0:8", "const:4:8"]]
- 005a44b0 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a44f0 ["INT_ADD", "register:40f0:8", ["const:5a44f0:8", "const:4:8"]]
+ 005a44f0 ["CALL", null, ["callee:00c57f80:8"]]
- 005a44b0 bytes 80ce1a94
+ 005a44f0 bytes a4ce1a94
- 005a44d4 ["INT_ADD", "register:40f0:8", ["const:5a44d4:8", "const:4:8"]]
- 005a44d4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a4514 ["INT_ADD", "register:40f0:8", ["const:5a4514:8", "const:4:8"]]
+ 005a4514 ["CALL", null, ["callee:00c57f80:8"]]
- 005a44d4 bytes 77ce1a94
+ 005a4514 bytes 9bce1a94
- 005a44e4 ["INT_ADD", "register:40f0:8", ["const:5a44e4:8", "const:4:8"]]
- 005a44e4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a4524 ["INT_ADD", "register:40f0:8", ["const:5a4524:8", "const:4:8"]]
+ 005a4524 ["CALL", null, ["callee:00c57f80:8"]]
- 005a44e4 bytes 73ce1a94
+ 005a4524 bytes 97ce1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57a3e430373adbdb71f4cbc5dc81724a"></a>

### [`005a4508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4508.md) → [`005a4548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4548.md) FUN_005a4548

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`005a3ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3ee0.md) [`005a4030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4030.md) [`005a408c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a408c.md) [`005a4228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4228.md) [`005a4a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4a3c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 8件 [`005a3f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a3/005a3f20.md) [`005a4070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4070.md) [`005a40cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a40cc.md) [`005a4268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4268.md) [`005a4a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4a7c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a4558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4508.md#insn-005a4558) · [`005a4568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4508.md#insn-005a4568) · [`005a4578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4508.md#insn-005a4578)
- 新版 `005a4598`（命令位置の公開資料なし） · `005a45a8`（命令位置の公開資料なし） · `005a45b8`（命令位置の公開資料なし）

~~~diff
- 005a4558 ["INT_ADD", "register:40f0:8", ["const:5a4558:8", "const:4:8"]]
- 005a4558 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a4598 ["INT_ADD", "register:40f0:8", ["const:5a4598:8", "const:4:8"]]
+ 005a4598 ["CALL", null, ["callee:00c57f80:8"]]
- 005a4558 bytes 56ce1a94
+ 005a4598 bytes 7ace1a94
- 005a4568 ["INT_ADD", "register:40f0:8", ["const:5a4568:8", "const:4:8"]]
- 005a4568 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a45a8 ["INT_ADD", "register:40f0:8", ["const:5a45a8:8", "const:4:8"]]
+ 005a45a8 ["CALL", null, ["callee:00c57f80:8"]]
- 005a4568 bytes 52ce1a94
+ 005a45a8 bytes 76ce1a94
- 005a4578 ["INT_ADD", "register:40f0:8", ["const:5a4578:8", "const:4:8"]]
- 005a4578 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a45b8 ["INT_ADD", "register:40f0:8", ["const:5a45b8:8", "const:4:8"]]
+ 005a45b8 ["CALL", null, ["callee:00c57f80:8"]]
- 005a4578 bytes 4ece1a94
+ 005a45b8 bytes 72ce1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f288ce47a17800bf24ea50c1737eda83"></a>

### [`005a4594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4594.md) → [`005a45d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a45d4.md) FUN_005a45d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005a3320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3320.md) [`00799c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00799/00799c94.md) [`007a0034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0034.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005a426c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a426c.md) [`005a42a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a42a0.md) [`005a4754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4754.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 3件 [`005a3360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a3/005a3360.md) [`00799cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00799/00799cec.md) [`007a008c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a008c.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`005a42ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a42ac.md) [`005a42e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a42e0.md) [`005a4794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4794.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a4634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4594.md#insn-005a4634) · [`005a465c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4594.md#insn-005a465c) · [`005a4680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4594.md#insn-005a4680)
- 新版 `005a4674`（命令位置の公開資料なし） · `005a469c`（命令位置の公開資料なし） · `005a46c0`（命令位置の公開資料なし）

~~~diff
- 005a4634 ["INT_ADD", "register:40f0:8", ["const:5a4634:8", "const:4:8"]]
- 005a4634 ["CALL", null, ["callee:00c57f60:8"]]
+ 005a4674 ["INT_ADD", "register:40f0:8", ["const:5a4674:8", "const:4:8"]]
+ 005a4674 ["CALL", null, ["callee:00c57f60:8"]]
- 005a4634 bytes 17ce1a94
+ 005a4674 bytes 3bce1a94
- 005a465c ["INT_ADD", "register:40f0:8", ["const:5a465c:8", "const:4:8"]]
- 005a465c ["CALL", null, ["callee:005a42e0:8"]]
+ 005a469c ["INT_ADD", "register:40f0:8", ["const:5a469c:8", "const:4:8"]]
+ 005a469c ["CALL", null, ["callee:005a42e0:8"]]
- 005a465c bytes 11ffff97
+ 005a469c bytes 11ffff97
- 005a4680 ["INT_ADD", "register:40f0:8", ["const:5a4680:8", "const:4:8"]]
- 005a4680 ["CALL", null, ["callee:005a4794:8"]]
+ 005a46c0 ["INT_ADD", "register:40f0:8", ["const:5a46c0:8", "const:4:8"]]
+ 005a46c0 ["CALL", null, ["callee:005a4794:8"]]
- 005a4680 bytes 35000094
+ 005a46c0 bytes 35000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72d5d9160e363deca8cf2307bff95b83"></a>

### [`005a471c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a471c.md) → [`005a475c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a475c.md) FUN_005a475c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005a4878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4878.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005a48b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a48b8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a4730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a471c.md#insn-005a4730)
- 新版 `005a4770`（命令位置の公開資料なし）

~~~diff
- 005a4730 ["INT_ADD", "register:40f0:8", ["const:5a4730:8", "const:4:8"]]
- 005a4730 ["CALL", null, ["callee:005a48b8:8"]]
+ 005a4770 ["INT_ADD", "register:40f0:8", ["const:5a4770:8", "const:4:8"]]
+ 005a4770 ["CALL", null, ["callee:005a48b8:8"]]
- 005a4730 bytes 52000094
+ 005a4770 bytes 52000094
~~~


<a id="compare-bf295cca2b8cc881f57a61caa77de620"></a>

### [`005a4754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4754.md) → [`005a4794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4794.md) FUN_005a4794

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a4594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4594.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005a45d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a45d4.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a4820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4754.md#insn-005a4820) · [`005a4844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4754.md#insn-005a4844) · [`005a4854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4754.md#insn-005a4854)
- 新版 `005a4860`（命令位置の公開資料なし） · `005a4884`（命令位置の公開資料なし） · `005a4894`（命令位置の公開資料なし）

~~~diff
- 005a4820 ["INT_ADD", "register:40f0:8", ["const:5a4820:8", "const:4:8"]]
- 005a4820 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a4860 ["INT_ADD", "register:40f0:8", ["const:5a4860:8", "const:4:8"]]
+ 005a4860 ["CALL", null, ["callee:00c57f80:8"]]
- 005a4820 bytes a4cd1a94
+ 005a4860 bytes c8cd1a94
- 005a4844 ["INT_ADD", "register:40f0:8", ["const:5a4844:8", "const:4:8"]]
- 005a4844 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a4884 ["INT_ADD", "register:40f0:8", ["const:5a4884:8", "const:4:8"]]
+ 005a4884 ["CALL", null, ["callee:00c57f80:8"]]
- 005a4844 bytes 9bcd1a94
+ 005a4884 bytes bfcd1a94
- 005a4854 ["INT_ADD", "register:40f0:8", ["const:5a4854:8", "const:4:8"]]
- 005a4854 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a4894 ["INT_ADD", "register:40f0:8", ["const:5a4894:8", "const:4:8"]]
+ 005a4894 ["CALL", null, ["callee:00c57f80:8"]]
- 005a4854 bytes 97cd1a94
+ 005a4894 bytes bbcd1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c63aea6e84aed8adea23f341d4eafe54"></a>

### [`005a4878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4878.md) → [`005a48b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a48b8.md) FUN_005a48b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a471c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a471c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005a475c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a475c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a48c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4878.md#insn-005a48c0) · [`005a48e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4878.md#insn-005a48e4) · [`005a48f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4878.md#insn-005a48f4)
- 新版 `005a4900`（命令位置の公開資料なし） · `005a4924`（命令位置の公開資料なし） · `005a4934`（命令位置の公開資料なし）

~~~diff
- 005a48c0 ["INT_ADD", "register:40f0:8", ["const:5a48c0:8", "const:4:8"]]
- 005a48c0 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a4900 ["INT_ADD", "register:40f0:8", ["const:5a4900:8", "const:4:8"]]
+ 005a4900 ["CALL", null, ["callee:00c57f80:8"]]
- 005a48c0 bytes 7ccd1a94
+ 005a4900 bytes a0cd1a94
- 005a48e4 ["INT_ADD", "register:40f0:8", ["const:5a48e4:8", "const:4:8"]]
- 005a48e4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a4924 ["INT_ADD", "register:40f0:8", ["const:5a4924:8", "const:4:8"]]
+ 005a4924 ["CALL", null, ["callee:00c57f80:8"]]
- 005a48e4 bytes 73cd1a94
+ 005a4924 bytes 97cd1a94
- 005a48f4 ["INT_ADD", "register:40f0:8", ["const:5a48f4:8", "const:4:8"]]
- 005a48f4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a4934 ["INT_ADD", "register:40f0:8", ["const:5a4934:8", "const:4:8"]]
+ 005a4934 ["CALL", null, ["callee:00c57f80:8"]]
- 005a48f4 bytes 6fcd1a94
+ 005a4934 bytes 93cd1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1d79c10eb0ae1e10e2687ddd9862eb1"></a>

### [`005a74bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a74bc.md) → [`005a74fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a74fc.md) FUN_005a74fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a7504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a74bc.md#insn-005a7504)
- 新版 `005a7544`（命令位置の公開資料なし）

~~~diff
- 005a7504 ["INT_ADD", "register:40f0:8", ["const:5a7504:8", "const:4:8"]]
- 005a7504 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a7544 ["INT_ADD", "register:40f0:8", ["const:5a7544:8", "const:4:8"]]
+ 005a7544 ["CALL", null, ["callee:00c57f80:8"]]
- 005a7504 bytes 6bc21a94
+ 005a7544 bytes 8fc21a94
~~~


<a id="compare-c07c047f656611d60331ae3f19969087"></a>

### [`005a780c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a780c.md) → [`005a784c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a784c.md) FUN_005a784c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005a7cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7cb4.md) [`009a63a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a63a0.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005a7968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7968.md) [`005a79f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a79f0.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`005a7cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a7cf4.md) [`009a63f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a63f4.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`005a79a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a79a8.md) [`005a7a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a7a30.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a7858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a780c.md#insn-005a7858) · [`005a78d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a780c.md#insn-005a78d8) · [`005a7928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a780c.md#insn-005a7928)
- 新版 `005a7898`（命令位置の公開資料なし） · `005a7918`（命令位置の公開資料なし） · `005a7968`（命令位置の公開資料なし）

~~~diff
- 005a7858 ["INT_ADD", "register:40f0:8", ["const:5a7858:8", "const:4:8"]]
- 005a7858 ["CALL", null, ["callee:00c57f60:8"]]
+ 005a7898 ["INT_ADD", "register:40f0:8", ["const:5a7898:8", "const:4:8"]]
+ 005a7898 ["CALL", null, ["callee:00c57f60:8"]]
- 005a7858 bytes 8ec11a94
+ 005a7898 bytes b2c11a94
- 005a78d8 ["INT_ADD", "register:40f0:8", ["const:5a78d8:8", "const:4:8"]]
- 005a78d8 ["CALL", null, ["callee:0043bb60:8"]]
+ 005a7918 ["INT_ADD", "register:40f0:8", ["const:5a7918:8", "const:4:8"]]
+ 005a7918 ["CALL", null, ["callee:0043bb60:8"]]
- 005a78d8 bytes 9250fa97
+ 005a7918 bytes 9250fa97
- 005a7928 ["INT_ADD", "register:40f0:8", ["const:5a7928:8", "const:4:8"]]
- 005a7928 ["CALL", null, ["callee:005a7a30:8"]]
+ 005a7968 ["INT_ADD", "register:40f0:8", ["const:5a7968:8", "const:4:8"]]
+ 005a7968 ["CALL", null, ["callee:005a7a30:8"]]
- 005a7928 bytes 32000094
+ 005a7968 bytes 32000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-120a214d068fdc22e47e4524fae025bc"></a>

### [`005a7968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7968.md) → [`005a79a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a79a8.md) FUN_005a79a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a780c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a780c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005a784c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a784c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a79cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7968.md#insn-005a79cc)
- 新版 `005a7a0c`（命令位置の公開資料なし）

~~~diff
- 005a79cc ["INT_ADD", "register:40f0:8", ["const:5a79cc:8", "const:4:8"]]
- 005a79cc ["CALL", null, ["callee:00c57f80:8"]]
+ 005a7a0c ["INT_ADD", "register:40f0:8", ["const:5a7a0c:8", "const:4:8"]]
+ 005a7a0c ["CALL", null, ["callee:00c57f80:8"]]
- 005a79cc bytes 39c11a94
+ 005a7a0c bytes 5dc11a94
~~~


<a id="compare-ad0903fb2de065c9fc3d604a05ebdd82"></a>

### [`005a7a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7a04.md) → [`005a7a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a7a44.md) FUN_005a7a44

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a7a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7a04.md#insn-005a7a44)
- 新版 `005a7a84`（命令位置の公開資料なし）

~~~diff
- 005a7a44 ["INT_ADD", "register:40f0:8", ["const:5a7a44:8", "const:4:8"]]
- 005a7a44 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a7a84 ["INT_ADD", "register:40f0:8", ["const:5a7a84:8", "const:4:8"]]
+ 005a7a84 ["CALL", null, ["callee:00c57f80:8"]]
- 005a7a44 bytes 1bc11a94
+ 005a7a84 bytes 3fc11a94
~~~


<a id="compare-06f79f2fec6de79f4be746547d23baa7"></a>

### [`005a7a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7a58.md) → [`005a7a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a7a98.md) FUN_005a7a98

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a6f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6f0c.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005a79f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a79f0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005a6f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a6/005a6f4c.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`005a7a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a7a30.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a7adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7a58.md#insn-005a7adc) · [`005a7b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7a58.md#insn-005a7b2c) · [`005a7ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7a58.md#insn-005a7ba4)
- 新版 `005a7b1c`（命令位置の公開資料なし） · `005a7b6c`（命令位置の公開資料なし） · `005a7be4`（命令位置の公開資料なし）

~~~diff
- 005a7adc ["INT_ADD", "register:40f0:8", ["const:5a7adc:8", "const:4:8"]]
- 005a7adc ["CALL", null, ["callee:00c57f60:8"]]
+ 005a7b1c ["INT_ADD", "register:40f0:8", ["const:5a7b1c:8", "const:4:8"]]
+ 005a7b1c ["CALL", null, ["callee:00c57f60:8"]]
- 005a7adc bytes edc01a94
+ 005a7b1c bytes 11c11a94
- 005a7b2c ["INT_ADD", "register:40f0:8", ["const:5a7b2c:8", "const:4:8"]]
- 005a7b2c ["CALL", null, ["callee:0043bb60:8"]]
+ 005a7b6c ["INT_ADD", "register:40f0:8", ["const:5a7b6c:8", "const:4:8"]]
+ 005a7b6c ["CALL", null, ["callee:0043bb60:8"]]
- 005a7b2c bytes fd4ffa97
+ 005a7b6c bytes fd4ffa97
- 005a7ba4 ["INT_ADD", "register:40f0:8", ["const:5a7ba4:8", "const:4:8"]]
- 005a7ba4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a7be4 ["INT_ADD", "register:40f0:8", ["const:5a7be4:8", "const:4:8"]]
+ 005a7be4 ["CALL", null, ["callee:00c57f80:8"]]
- 005a7ba4 bytes c3c01a94
+ 005a7be4 bytes e7c01a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f480364644129389b75f0599fc87b665"></a>

### [`005a7c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7c4c.md) → [`005a7c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a7c8c.md) FUN_005a7c8c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a7c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7c4c.md#insn-005a7c9c)
- 新版 `005a7cdc`（命令位置の公開資料なし）

~~~diff
- 005a7c9c ["INT_ADD", "register:40f0:8", ["const:5a7c9c:8", "const:4:8"]]
- 005a7c9c ["CALL", null, ["callee:00c57f80:8"]]
+ 005a7cdc ["INT_ADD", "register:40f0:8", ["const:5a7cdc:8", "const:4:8"]]
+ 005a7cdc ["CALL", null, ["callee:00c57f80:8"]]
- 005a7c9c bytes 85c01a94
+ 005a7cdc bytes a9c01a94
~~~


<a id="compare-c0b7d53f16a171b21f1d3e1d19d6ed91"></a>

### [`005a8684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8684.md) → [`005a86c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a8/005a86c4.md) FUN_005a86c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0059bf44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059bf44.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c581d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) [`0059bf84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059bf84.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c582a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a86b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8684.md#insn-005a86b0) · [`005a86e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8684.md#insn-005a86e0) · [`005a86f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8684.md#insn-005a86f0)
- 新版 `005a86f0`（命令位置の公開資料なし） · `005a8720`（命令位置の公開資料なし） · `005a8730`（命令位置の公開資料なし）

~~~diff
- 005a86b0 ["INT_ADD", "register:40f0:8", ["const:5a86b0:8", "const:4:8"]]
- 005a86b0 ["CALL", null, ["callee:0059bf84:8"]]
+ 005a86f0 ["INT_ADD", "register:40f0:8", ["const:5a86f0:8", "const:4:8"]]
+ 005a86f0 ["CALL", null, ["callee:0059bf84:8"]]
- 005a86b0 bytes 25ceff97
+ 005a86f0 bytes 25ceff97
- 005a86e0 ["INT_ADD", "register:40f0:8", ["const:5a86e0:8", "const:4:8"]]
- 005a86e0 ["CALL", null, ["callee:00c582a0:8"]]
+ 005a8720 ["INT_ADD", "register:40f0:8", ["const:5a8720:8", "const:4:8"]]
+ 005a8720 ["CALL", null, ["callee:00c582a0:8"]]
- 005a86e0 bytes bcbe1a94
+ 005a8720 bytes e0be1a94
- 005a86f0 ["INT_ADD", "register:40f0:8", ["const:5a86f0:8", "const:4:8"]]
- 005a86f0 ["CALL", null, ["callee:004517dc:8"]]
+ 005a8730 ["INT_ADD", "register:40f0:8", ["const:5a8730:8", "const:4:8"]]
+ 005a8730 ["CALL", null, ["callee:004517dc:8"]]
- 005a86f0 bytes 2ba4fa97
+ 005a8730 bytes 2ba4fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6253fc4376d6d624563d8d40af2f738"></a>

### [`005a96f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a96f4.md) → [`005a9734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9734.md) FUN_005a9734

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005aa184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa184.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005aa1c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa1c4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a972c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a96f4.md#insn-005a972c)
- 新版 `005a976c`（命令位置の公開資料なし）

~~~diff
- 005a972c ["INT_ADD", "register:40f0:8", ["const:5a972c:8", "const:4:8"]]
- 005a972c ["CALL", null, ["callee:005aa1c4:8"]]
+ 005a976c ["INT_ADD", "register:40f0:8", ["const:5a976c:8", "const:4:8"]]
+ 005a976c ["CALL", null, ["callee:005aa1c4:8"]]
- 005a972c bytes 96020094
+ 005a976c bytes 96020094
~~~


<a id="compare-54c79956670a58a1569cc007beeee379"></a>

### [`005a9d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9d00.md) → [`005a9d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9d40.md) FUN_005a9d40

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005a9c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9c1c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005a9c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9c5c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a9d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9d00.md#insn-005a9d10)
- 新版 `005a9d50`（命令位置の公開資料なし）

~~~diff
- 005a9d10 ["INT_ADD", "register:40f0:8", ["const:5a9d10:8", "const:4:8"]]
- 005a9d10 ["CALL", null, ["callee:005a9c5c:8"]]
+ 005a9d50 ["INT_ADD", "register:40f0:8", ["const:5a9d50:8", "const:4:8"]]
+ 005a9d50 ["CALL", null, ["callee:005a9c5c:8"]]
- 005a9d10 bytes c3ffff97
+ 005a9d50 bytes c3ffff97
~~~


<a id="compare-116dd083dbccde32141c62e32b81545b"></a>

### [`005a9d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9d24.md) → [`005a9d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9d64.md) FUN_005a9d64

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005a8c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8c9c.md) [`007499d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00749/007499d4.md) [`009b6c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6c58.md) · 呼出先 6件 [`005a9e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9e64.md) [`005a9ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9ee4.md) [`005a9f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9f54.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 3件 [`005a8cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a8/005a8cdc.md) [`00749a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/00749a2c.md) [`009b6cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6cac.md) · 呼出先 6件 [`005a9ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9ea4.md) [`005a9f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9f24.md) [`005a9f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9f94.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a9d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9d24.md#insn-005a9d7c) · [`005a9dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9d24.md#insn-005a9dc0) · [`005a9e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9d24.md#insn-005a9e24)
- 新版 `005a9dbc`（命令位置の公開資料なし） · `005a9e00`（命令位置の公開資料なし） · `005a9e64`（命令位置の公開資料なし）

~~~diff
- 005a9d7c ["INT_ADD", "register:40f0:8", ["const:5a9d7c:8", "const:4:8"]]
- 005a9d7c ["CALL", null, ["callee:00c57f60:8"]]
+ 005a9dbc ["INT_ADD", "register:40f0:8", ["const:5a9dbc:8", "const:4:8"]]
+ 005a9dbc ["CALL", null, ["callee:00c57f60:8"]]
- 005a9d7c bytes 45b81a94
+ 005a9dbc bytes 69b81a94
- 005a9dc0 ["INT_ADD", "register:40f0:8", ["const:5a9dc0:8", "const:4:8"]]
- 005a9dc0 ["CALL", null, ["callee:005a9f94:8"]]
+ 005a9e00 ["INT_ADD", "register:40f0:8", ["const:5a9e00:8", "const:4:8"]]
+ 005a9e00 ["CALL", null, ["callee:005a9f94:8"]]
- 005a9dc0 bytes 65000094
+ 005a9e00 bytes 65000094
- 005a9e24 ["INT_ADD", "register:40f0:8", ["const:5a9e24:8", "const:4:8"]]
- 005a9e24 ["CALL", null, ["callee:005a9f24:8"]]
+ 005a9e64 ["INT_ADD", "register:40f0:8", ["const:5a9e64:8", "const:4:8"]]
+ 005a9e64 ["CALL", null, ["callee:005a9f24:8"]]
- 005a9e24 bytes 30000094
+ 005a9e64 bytes 30000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-425b307d63475c2519b0ab7e2b491206"></a>

### [`005a9e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9e64.md) → [`005a9ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9ea4.md) FUN_005a9ea4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a9d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9d24.md) · 呼出先 2件 [`005aa184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa184.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005a9d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9d64.md) · 呼出先 2件 [`005aa1c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa1c4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a9eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9e64.md#insn-005a9eb8)
- 新版 `005a9ef8`（命令位置の公開資料なし）

~~~diff
- 005a9eb8 ["INT_ADD", "register:40f0:8", ["const:5a9eb8:8", "const:4:8"]]
- 005a9eb8 ["CALL", null, ["callee:005aa1c4:8"]]
+ 005a9ef8 ["INT_ADD", "register:40f0:8", ["const:5a9ef8:8", "const:4:8"]]
+ 005a9ef8 ["CALL", null, ["callee:005aa1c4:8"]]
- 005a9eb8 bytes b3000094
+ 005a9ef8 bytes b3000094
~~~


<a id="compare-3a5a6ad6e828e3e606a282119a9e5f7b"></a>

### [`005a9ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9ef8.md) → [`005a9f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9f38.md) FUN_005a9f38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`005aa184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa184.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005aa1c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa1c4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a9f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9ef8.md#insn-005a9f38)
- 新版 `005a9f78`（命令位置の公開資料なし）

~~~diff
- 005a9f38 ["INT_ADD", "register:40f0:8", ["const:5a9f38:8", "const:4:8"]]
- 005a9f38 ["CALL", null, ["callee:005aa1c4:8"]]
+ 005a9f78 ["INT_ADD", "register:40f0:8", ["const:5a9f78:8", "const:4:8"]]
+ 005a9f78 ["CALL", null, ["callee:005aa1c4:8"]]
- 005a9f38 bytes 93000094
+ 005a9f78 bytes 93000094
~~~


<a id="compare-3426d949162a64c81b63dfad8e3bc745"></a>

### [`005a9f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9f54.md) → [`005a9f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9f94.md) FUN_005a9f94

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`005a9d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9d24.md) [`007499d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00749/007499d4.md) [`009aa624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009aa/009aa624.md) [`009b3134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3134.md) [`009b5d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b5d84.md) · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005aa07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa07c.md) [`005aa170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa170.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 5件 [`005a9d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9d64.md) [`00749a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/00749a2c.md) [`009aa678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aa678.md) [`009b3188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b3/009b3188.md) [`009b5dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5dd8.md) · 呼出先 7件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`005aa0bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa0bc.md) [`005aa1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa1b0.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a9fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9f54.md#insn-005a9fa8) · [`005a9fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9f54.md#insn-005a9fec) · [`005aa004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9f54.md#insn-005aa004)
- 新版 `005a9fe8`（命令位置の公開資料なし） · `005aa02c`（命令位置の公開資料なし） · `005aa044`（命令位置の公開資料なし）

~~~diff
- 005a9fa8 ["INT_ADD", "register:40f0:8", ["const:5a9fa8:8", "const:4:8"]]
- 005a9fa8 ["CALL", null, ["callee:0043bb60:8"]]
+ 005a9fe8 ["INT_ADD", "register:40f0:8", ["const:5a9fe8:8", "const:4:8"]]
+ 005a9fe8 ["CALL", null, ["callee:0043bb60:8"]]
- 005a9fa8 bytes de46fa97
+ 005a9fe8 bytes de46fa97
- 005a9fec ["INT_ADD", "register:40f0:8", ["const:5a9fec:8", "const:4:8"]]
- 005a9fec ["CALL", null, ["callee:00c57f60:8"]]
+ 005aa02c ["INT_ADD", "register:40f0:8", ["const:5aa02c:8", "const:4:8"]]
+ 005aa02c ["CALL", null, ["callee:00c57f60:8"]]
- 005a9fec bytes a9b71a94
+ 005aa02c bytes cdb71a94
- 005aa004 ["INT_ADD", "register:40f0:8", ["const:5aa004:8", "const:4:8"]]
- 005aa004 ["CALL", null, ["callee:00c580d0:8"]]
+ 005aa044 ["INT_ADD", "register:40f0:8", ["const:5aa044:8", "const:4:8"]]
+ 005aa044 ["CALL", null, ["callee:00c580d0:8"]]
- 005aa004 bytes ffb71a94
+ 005aa044 bytes 23b81a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-214c5d82b18536f3392043562e9a636f"></a>

### [`005aa07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa07c.md) → [`005aa0bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa0bc.md) FUN_005aa0bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a9f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9f54.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)
- 新版 呼出元 1件 [`005a9f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9f94.md) · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005aa0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa07c.md#insn-005aa0b4) · [`005aa0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa07c.md#insn-005aa0e8) · [`005aa114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa07c.md#insn-005aa114)
- 新版 `005aa0f4`（命令位置の公開資料なし） · `005aa128`（命令位置の公開資料なし） · `005aa154`（命令位置の公開資料なし）

~~~diff
- 005aa0b4 ["INT_ADD", "register:40f0:8", ["const:5aa0b4:8", "const:4:8"]]
- 005aa0b4 ["CALL", null, ["callee:0043bb60:8"]]
+ 005aa0f4 ["INT_ADD", "register:40f0:8", ["const:5aa0f4:8", "const:4:8"]]
+ 005aa0f4 ["CALL", null, ["callee:0043bb60:8"]]
- 005aa0b4 bytes 9b46fa97
+ 005aa0f4 bytes 9b46fa97
- 005aa0e8 ["INT_ADD", "register:40f0:8", ["const:5aa0e8:8", "const:4:8"]]
- 005aa0e8 ["CALL", null, ["callee:0043bb60:8"]]
+ 005aa128 ["INT_ADD", "register:40f0:8", ["const:5aa128:8", "const:4:8"]]
+ 005aa128 ["CALL", null, ["callee:0043bb60:8"]]
- 005aa0e8 bytes 8e46fa97
+ 005aa128 bytes 8e46fa97
- 005aa114 ["INT_ADD", "register:40f0:8", ["const:5aa114:8", "const:4:8"]]
- 005aa114 ["CALL", null, ["callee:0043bb60:8"]]
+ 005aa154 ["INT_ADD", "register:40f0:8", ["const:5aa154:8", "const:4:8"]]
+ 005aa154 ["CALL", null, ["callee:0043bb60:8"]]
- 005aa114 bytes 8346fa97
+ 005aa154 bytes 8346fa97
~~~


<a id="compare-c859403e67bf18ffc66d6b6f1be29c1a"></a>

### [`005aa184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa184.md) → [`005aa1c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa1c4.md) FUN_005aa1c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`005a8e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8e28.md) [`005a96f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a96f4.md) [`005a9c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9c1c.md) [`005a9e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9e64.md) [`005a9ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9ef8.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 9件 [`005a8e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a8/005a8e68.md) [`005a9734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9734.md) [`005a9c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9c5c.md) [`005a9ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9ea4.md) [`005a9f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9f38.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005aa1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa184.md#insn-005aa1b8) · [`005aa1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa184.md#insn-005aa1d4) · [`005aa1e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa184.md#insn-005aa1e4)
- 新版 `005aa1f8`（命令位置の公開資料なし） · `005aa214`（命令位置の公開資料なし） · `005aa224`（命令位置の公開資料なし）

~~~diff
- 005aa1b8 ["INT_ADD", "register:40f0:8", ["const:5aa1b8:8", "const:4:8"]]
- 005aa1b8 ["CALL", null, ["callee:00c57f80:8"]]
+ 005aa1f8 ["INT_ADD", "register:40f0:8", ["const:5aa1f8:8", "const:4:8"]]
+ 005aa1f8 ["CALL", null, ["callee:00c57f80:8"]]
- 005aa1b8 bytes 3eb71a94
+ 005aa1f8 bytes 62b71a94
- 005aa1d4 ["INT_ADD", "register:40f0:8", ["const:5aa1d4:8", "const:4:8"]]
- 005aa1d4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005aa214 ["INT_ADD", "register:40f0:8", ["const:5aa214:8", "const:4:8"]]
+ 005aa214 ["CALL", null, ["callee:00c57f80:8"]]
- 005aa1d4 bytes 37b71a94
+ 005aa214 bytes 5bb71a94
- 005aa1e4 ["INT_ADD", "register:40f0:8", ["const:5aa1e4:8", "const:4:8"]]
- 005aa1e4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005aa224 ["INT_ADD", "register:40f0:8", ["const:5aa224:8", "const:4:8"]]
+ 005aa224 ["CALL", null, ["callee:00c57f80:8"]]
- 005aa1e4 bytes 33b71a94
+ 005aa224 bytes 57b71a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15a76981fade57922ec1156828eff4f6"></a>

### [`005ac29c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac29c.md) → [`005ac2dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005ac2dc.md) FUN_005ac2dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0059bf44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059bf44.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) [`0059bf84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059bf84.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ac2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac29c.md#insn-005ac2c8) · [`005ac2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac29c.md#insn-005ac2f4) · [`005ac304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac29c.md#insn-005ac304)
- 新版 `005ac308`（命令位置の公開資料なし） · `005ac334`（命令位置の公開資料なし） · `005ac344`（命令位置の公開資料なし）

~~~diff
- 005ac2c8 ["INT_ADD", "register:40f0:8", ["const:5ac2c8:8", "const:4:8"]]
- 005ac2c8 ["CALL", null, ["callee:0059bf84:8"]]
+ 005ac308 ["INT_ADD", "register:40f0:8", ["const:5ac308:8", "const:4:8"]]
+ 005ac308 ["CALL", null, ["callee:0059bf84:8"]]
- 005ac2c8 bytes 1fbfff97
+ 005ac308 bytes 1fbfff97
- 005ac2f4 ["INT_ADD", "register:40f0:8", ["const:5ac2f4:8", "const:4:8"]]
- 005ac2f4 ["CALL", null, ["callee:00c58020:8"]]
+ 005ac334 ["INT_ADD", "register:40f0:8", ["const:5ac334:8", "const:4:8"]]
+ 005ac334 ["CALL", null, ["callee:00c58020:8"]]
- 005ac2f4 bytes 17af1a94
+ 005ac334 bytes 3baf1a94
- 005ac304 ["INT_ADD", "register:40f0:8", ["const:5ac304:8", "const:4:8"]]
- 005ac304 ["CALL", null, ["callee:004517dc:8"]]
+ 005ac344 ["INT_ADD", "register:40f0:8", ["const:5ac344:8", "const:4:8"]]
+ 005ac344 ["CALL", null, ["callee:004517dc:8"]]
- 005ac304 bytes 2695fa97
+ 005ac344 bytes 2695fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76bbe92e869b5a57cd984f01ac9d0f23"></a>

### [`005ace30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ace30.md) → [`005ace70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005ace70.md) FUN_005ace70

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ace4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ace30.md#insn-005ace4c) · [`005ace6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ace30.md#insn-005ace6c)
- 新版 `005ace8c`（命令位置の公開資料なし） · `005aceac`（命令位置の公開資料なし）

~~~diff
- 005ace4c ["INT_ADD", "register:40f0:8", ["const:5ace4c:8", "const:4:8"]]
- 005ace4c ["CALL", null, ["callee:00c53da0:8"]]
+ 005ace8c ["INT_ADD", "register:40f0:8", ["const:5ace8c:8", "const:4:8"]]
+ 005ace8c ["CALL", null, ["callee:00c53da0:8"]]
- 005ace4c bytes ad9b1a94
+ 005ace8c bytes c59b1a94
- 005ace6c ["COPY", "register:0:8", ["register:4040:8"]]
- 005ace6c ["INT_ADD", "register:40f0:8", ["const:5ace6c:8", "const:4:8"]]
- 005ace6c ["CALLIND", null, ["register:0:8"]]
+ 005aceac ["COPY", "register:0:8", ["register:4040:8"]]
+ 005aceac ["INT_ADD", "register:40f0:8", ["const:5aceac:8", "const:4:8"]]
+ 005aceac ["CALLIND", null, ["register:0:8"]]
- 005ace6c bytes 00013fd6
+ 005aceac bytes 00013fd6
~~~


<a id="compare-e3983daa379691a4978591033a72359e"></a>

### [`005ace80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ace80.md) → [`005acec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005acec0.md) FUN_005acec0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005aca44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca44.md) · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005aca84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005aca84.md) · 呼出先 2件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ace9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ace80.md#insn-005ace9c)
- 新版 `005acedc`（命令位置の公開資料なし）

~~~diff
- 005ace9c ["INT_ADD", "register:40f0:8", ["const:5ace9c:8", "const:4:8"]]
- 005ace9c ["CALL", null, ["callee:00c57f80:8"]]
+ 005acedc ["INT_ADD", "register:40f0:8", ["const:5acedc:8", "const:4:8"]]
+ 005acedc ["CALL", null, ["callee:00c57f80:8"]]
- 005ace9c bytes 05ac1a94
+ 005acedc bytes 29ac1a94
~~~


<a id="compare-24b94cbc7119753c753d30c303395655"></a>

### [`005ad288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad288.md) → [`005ad2c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad2c8.md) FUN_005ad2c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ad2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad288.md#insn-005ad2a4) · [`005ad2b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad288.md#insn-005ad2b8) · [`005ad2d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad288.md#insn-005ad2d8)
- 新版 `005ad2e4`（命令位置の公開資料なし） · `005ad2f8`（命令位置の公開資料なし） · `005ad318`（命令位置の公開資料なし）

~~~diff
- 005ad2a4 ["INT_ADD", "register:40f0:8", ["const:5ad2a4:8", "const:4:8"]]
- 005ad2a4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ad2e4 ["INT_ADD", "register:40f0:8", ["const:5ad2e4:8", "const:4:8"]]
+ 005ad2e4 ["CALL", null, ["callee:00c57f80:8"]]
- 005ad2a4 bytes 03ab1a94
+ 005ad2e4 bytes 27ab1a94
- 005ad2b8 ["INT_ADD", "register:40f0:8", ["const:5ad2b8:8", "const:4:8"]]
- 005ad2b8 ["CALL", null, ["callee:00c53da0:8"]]
+ 005ad2f8 ["INT_ADD", "register:40f0:8", ["const:5ad2f8:8", "const:4:8"]]
+ 005ad2f8 ["CALL", null, ["callee:00c53da0:8"]]
- 005ad2b8 bytes 929a1a94
+ 005ad2f8 bytes aa9a1a94
- 005ad2d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005ad2d8 ["INT_ADD", "register:40f0:8", ["const:5ad2d8:8", "const:4:8"]]
- 005ad2d8 ["CALLIND", null, ["register:0:8"]]
+ 005ad318 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ad318 ["INT_ADD", "register:40f0:8", ["const:5ad318:8", "const:4:8"]]
+ 005ad318 ["CALLIND", null, ["register:0:8"]]
- 005ad2d8 bytes 00013fd6
+ 005ad318 bytes 00013fd6
~~~


<a id="compare-74e6e74f6865c8bd08e88ef87fdb55c5"></a>

### [`005ad2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad2ec.md) → [`005ad32c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad32c.md) FUN_005ad32c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b4590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4590.md) · 呼出先 2件 [`005af780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005af780.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`005b45d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b4/005b45d0.md) · 呼出先 2件 [`005af7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005af/005af7c0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ad328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad2ec.md#insn-005ad328) · [`005ad354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad2ec.md#insn-005ad354) · [`005ad364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad2ec.md#insn-005ad364)
- 新版 `005ad368`（命令位置の公開資料なし） · `005ad394`（命令位置の公開資料なし） · `005ad3a4`（命令位置の公開資料なし）

~~~diff
- 005ad328 ["COPY", "register:0:8", ["register:4048:8"]]
- 005ad328 ["INT_ADD", "register:40f0:8", ["const:5ad328:8", "const:4:8"]]
- 005ad328 ["CALLIND", null, ["register:0:8"]]
+ 005ad368 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005ad368 ["INT_ADD", "register:40f0:8", ["const:5ad368:8", "const:4:8"]]
+ 005ad368 ["CALLIND", null, ["register:0:8"]]
- 005ad328 bytes 20013fd6
+ 005ad368 bytes 20013fd6
- 005ad354 ["COPY", "register:0:8", ["register:4040:8"]]
- 005ad354 ["INT_ADD", "register:40f0:8", ["const:5ad354:8", "const:4:8"]]
- 005ad354 ["CALLIND", null, ["register:0:8"]]
+ 005ad394 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ad394 ["INT_ADD", "register:40f0:8", ["const:5ad394:8", "const:4:8"]]
+ 005ad394 ["CALLIND", null, ["register:0:8"]]
- 005ad354 bytes 00013fd6
+ 005ad394 bytes 00013fd6
- 005ad364 ["INT_ADD", "register:40f0:8", ["const:5ad364:8", "const:4:8"]]
- 005ad364 ["CALL", null, ["callee:005af7c0:8"]]
+ 005ad3a4 ["INT_ADD", "register:40f0:8", ["const:5ad3a4:8", "const:4:8"]]
+ 005ad3a4 ["CALL", null, ["callee:005af7c0:8"]]
- 005ad364 bytes 07090094
+ 005ad3a4 bytes 07090094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b3ade5b2eb38330516ef251eeec30ee"></a>

### [`005ad3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad3b8.md) → [`005ad3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad3f8.md) FUN_005ad3f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b4590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4590.md) · 呼出先 2件 [`0058f434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f434.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`005b45d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b4/005b45d0.md) · 呼出先 2件 [`0058f474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f474.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ad3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad3b8.md#insn-005ad3f4) · [`005ad420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad3b8.md#insn-005ad420) · [`005ad430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad3b8.md#insn-005ad430)
- 新版 `005ad434`（命令位置の公開資料なし） · `005ad460`（命令位置の公開資料なし） · `005ad470`（命令位置の公開資料なし）

~~~diff
- 005ad3f4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005ad3f4 ["INT_ADD", "register:40f0:8", ["const:5ad3f4:8", "const:4:8"]]
- 005ad3f4 ["CALLIND", null, ["register:0:8"]]
+ 005ad434 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005ad434 ["INT_ADD", "register:40f0:8", ["const:5ad434:8", "const:4:8"]]
+ 005ad434 ["CALLIND", null, ["register:0:8"]]
- 005ad3f4 bytes 20013fd6
+ 005ad434 bytes 20013fd6
- 005ad420 ["COPY", "register:0:8", ["register:4040:8"]]
- 005ad420 ["INT_ADD", "register:40f0:8", ["const:5ad420:8", "const:4:8"]]
- 005ad420 ["CALLIND", null, ["register:0:8"]]
+ 005ad460 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ad460 ["INT_ADD", "register:40f0:8", ["const:5ad460:8", "const:4:8"]]
+ 005ad460 ["CALLIND", null, ["register:0:8"]]
- 005ad420 bytes 00013fd6
+ 005ad460 bytes 00013fd6
- 005ad430 ["INT_ADD", "register:40f0:8", ["const:5ad430:8", "const:4:8"]]
- 005ad430 ["CALL", null, ["callee:0058f474:8"]]
+ 005ad470 ["INT_ADD", "register:40f0:8", ["const:5ad470:8", "const:4:8"]]
+ 005ad470 ["CALL", null, ["callee:0058f474:8"]]
- 005ad430 bytes 0188ff97
+ 005ad470 bytes 0188ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-707af0e27d3e5aa7c1135c924fdf3b2d"></a>

### [`005ad764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad764.md) → [`005ad7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad7a4.md) FUN_005ad7a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ad780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad764.md#insn-005ad780)
- 新版 `005ad7c0`（命令位置の公開資料なし）

~~~diff
- 005ad780 ["INT_ADD", "register:40f0:8", ["const:5ad780:8", "const:4:8"]]
- 005ad780 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ad7c0 ["INT_ADD", "register:40f0:8", ["const:5ad7c0:8", "const:4:8"]]
+ 005ad7c0 ["CALL", null, ["callee:00c57f80:8"]]
- 005ad780 bytes cca91a94
+ 005ad7c0 bytes f0a91a94
~~~


<a id="compare-d65883d00d2bea8f034eb0388afeda3b"></a>

### [`005ad7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7a4.md) → [`005ad7e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad7e4.md) FUN_005ad7e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005aca44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca44.md) · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005aca84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005aca84.md) · 呼出先 2件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ad7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7a4.md#insn-005ad7c0) · [`005ad7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7a4.md#insn-005ad7cc)
- 新版 `005ad800`（命令位置の公開資料なし） · `005ad80c`（命令位置の公開資料なし）

~~~diff
- 005ad7c0 ["INT_ADD", "register:40f0:8", ["const:5ad7c0:8", "const:4:8"]]
- 005ad7c0 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ad800 ["INT_ADD", "register:40f0:8", ["const:5ad800:8", "const:4:8"]]
+ 005ad800 ["CALL", null, ["callee:00c57f80:8"]]
- 005ad7c0 bytes bca91a94
+ 005ad800 bytes e0a91a94
- 005ad7cc ["INT_ADD", "register:40f0:8", ["const:5ad7cc:8", "const:4:8"]]
- 005ad7cc ["CALL", null, ["callee:00c57f50:8"]]
+ 005ad80c ["INT_ADD", "register:40f0:8", ["const:5ad80c:8", "const:4:8"]]
+ 005ad80c ["CALL", null, ["callee:00c57f50:8"]]
- 005ad7cc bytes ada91a94
+ 005ad80c bytes d1a91a94
~~~


<a id="compare-9ca536d395e1348f3abccb07501bc3ae"></a>

### [`005ae820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae820.md) → [`005ae860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ae/005ae860.md) FUN_005ae860

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ae83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae820.md#insn-005ae83c) · [`005ae850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae820.md#insn-005ae850) · [`005ae870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae820.md#insn-005ae870)
- 新版 `005ae87c`（命令位置の公開資料なし） · `005ae890`（命令位置の公開資料なし） · `005ae8b0`（命令位置の公開資料なし）

~~~diff
- 005ae83c ["INT_ADD", "register:40f0:8", ["const:5ae83c:8", "const:4:8"]]
- 005ae83c ["CALL", null, ["callee:00c57f80:8"]]
+ 005ae87c ["INT_ADD", "register:40f0:8", ["const:5ae87c:8", "const:4:8"]]
+ 005ae87c ["CALL", null, ["callee:00c57f80:8"]]
- 005ae83c bytes 9da51a94
+ 005ae87c bytes c1a51a94
- 005ae850 ["INT_ADD", "register:40f0:8", ["const:5ae850:8", "const:4:8"]]
- 005ae850 ["CALL", null, ["callee:00c53da0:8"]]
+ 005ae890 ["INT_ADD", "register:40f0:8", ["const:5ae890:8", "const:4:8"]]
+ 005ae890 ["CALL", null, ["callee:00c53da0:8"]]
- 005ae850 bytes 2c951a94
+ 005ae890 bytes 44951a94
- 005ae870 ["COPY", "register:0:8", ["register:4040:8"]]
- 005ae870 ["INT_ADD", "register:40f0:8", ["const:5ae870:8", "const:4:8"]]
- 005ae870 ["CALLIND", null, ["register:0:8"]]
+ 005ae8b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ae8b0 ["INT_ADD", "register:40f0:8", ["const:5ae8b0:8", "const:4:8"]]
+ 005ae8b0 ["CALLIND", null, ["register:0:8"]]
- 005ae870 bytes 00013fd6
+ 005ae8b0 bytes 00013fd6
~~~


<a id="compare-fb531e22818d1aac35a76ba1ea7c1794"></a>

### [`005ae884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae884.md) → [`005ae8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ae/005ae8c4.md) FUN_005ae8c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005acec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005acec0.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005acf00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005acf00.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ae8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae884.md#insn-005ae8a0) · [`005ae8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae884.md#insn-005ae8b4) · [`005ae8c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae884.md#insn-005ae8c8)
- 新版 `005ae8e0`（命令位置の公開資料なし） · `005ae8f4`（命令位置の公開資料なし） · `005ae908`（命令位置の公開資料なし）

~~~diff
- 005ae8a0 ["INT_ADD", "register:40f0:8", ["const:5ae8a0:8", "const:4:8"]]
- 005ae8a0 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ae8e0 ["INT_ADD", "register:40f0:8", ["const:5ae8e0:8", "const:4:8"]]
+ 005ae8e0 ["CALL", null, ["callee:00c57f80:8"]]
- 005ae8a0 bytes 84a51a94
+ 005ae8e0 bytes a8a51a94
- 005ae8b4 ["INT_ADD", "register:40f0:8", ["const:5ae8b4:8", "const:4:8"]]
- 005ae8b4 ["CALL", null, ["callee:00c53da0:8"]]
+ 005ae8f4 ["INT_ADD", "register:40f0:8", ["const:5ae8f4:8", "const:4:8"]]
+ 005ae8f4 ["CALL", null, ["callee:00c53da0:8"]]
- 005ae8b4 bytes 13951a94
+ 005ae8f4 bytes 2b951a94
- 005ae8c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005ae8c8 ["INT_ADD", "register:40f0:8", ["const:5ae8c8:8", "const:4:8"]]
- 005ae8c8 ["CALLIND", null, ["register:0:8"]]
+ 005ae908 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ae908 ["INT_ADD", "register:40f0:8", ["const:5ae908:8", "const:4:8"]]
+ 005ae908 ["CALLIND", null, ["register:0:8"]]
- 005ae8c8 bytes 00013fd6
+ 005ae908 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87266bed4fe2701e3898bdc11d4054e4"></a>

### [`005af780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005af780.md) → [`005af7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005af/005af7c0.md) FUN_005af7c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005ad2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad2ec.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`005ad32c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad32c.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005af7ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005af780.md#insn-005af7ec) · [`005af7fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005af780.md#insn-005af7fc) · [`005af81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005af780.md#insn-005af81c)
- 新版 `005af82c`（命令位置の公開資料なし） · `005af83c`（命令位置の公開資料なし） · `005af85c`（命令位置の公開資料なし）

~~~diff
- 005af7ec ["COPY", "register:0:8", ["register:4040:8"]]
- 005af7ec ["INT_ADD", "register:40f0:8", ["const:5af7ec:8", "const:4:8"]]
- 005af7ec ["CALLIND", null, ["register:0:8"]]
+ 005af82c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005af82c ["INT_ADD", "register:40f0:8", ["const:5af82c:8", "const:4:8"]]
+ 005af82c ["CALLIND", null, ["register:0:8"]]
- 005af7ec bytes 00013fd6
+ 005af82c bytes 00013fd6
- 005af7fc ["COPY", "register:0:8", ["register:4040:8"]]
- 005af7fc ["INT_ADD", "register:40f0:8", ["const:5af7fc:8", "const:4:8"]]
- 005af7fc ["CALLIND", null, ["register:0:8"]]
+ 005af83c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005af83c ["INT_ADD", "register:40f0:8", ["const:5af83c:8", "const:4:8"]]
+ 005af83c ["CALLIND", null, ["register:0:8"]]
- 005af7fc bytes 00013fd6
+ 005af83c bytes 00013fd6
- 005af81c ["COPY", "register:0:8", ["register:4040:8"]]
- 005af81c ["INT_ADD", "register:40f0:8", ["const:5af81c:8", "const:4:8"]]
- 005af81c ["CALLIND", null, ["register:0:8"]]
+ 005af85c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005af85c ["INT_ADD", "register:40f0:8", ["const:5af85c:8", "const:4:8"]]
+ 005af85c ["CALLIND", null, ["register:0:8"]]
- 005af81c bytes 00013fd6
+ 005af85c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea82adfdd07bb6b4fd2d901d48241903"></a>

### [`005afc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afc78.md) → [`005afcb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005af/005afcb8.md) FUN_005afcb8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 11件 [`005afdec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afdec.md) [`005afe08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afe08.md) [`005aff5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005aff5c.md) [`005b00c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b00c0.md) [`005b0140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0140.md) · 呼出先 7件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00903f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00903/00903f44.md) [`009e0fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0fc0.md) [`009e4704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e4/009e4704.md)
- 新版 呼出元 11件 [`005afe2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005af/005afe2c.md) [`005afe48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005af/005afe48.md) [`005aff9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005af/005aff9c.md) [`005b0100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b0/005b0100.md) [`005b0180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b0/005b0180.md) · 呼出先 7件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00903f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00903/00903f98.md) [`009e1014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e1/009e1014.md) [`009e4758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e4/009e4758.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005afc90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afc78.md#insn-005afc90) · [`005afca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afc78.md#insn-005afca4) · [`005afcac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afc78.md#insn-005afcac)
- 新版 `005afcd0`（命令位置の公開資料なし） · `005afce4`（命令位置の公開資料なし） · `005afcec`（命令位置の公開資料なし）

~~~diff
- 005afc90 ["INT_ADD", "register:40f0:8", ["const:5afc90:8", "const:4:8"]]
- 005afc90 ["CALL", null, ["callee:00851550:8"]]
+ 005afcd0 ["INT_ADD", "register:40f0:8", ["const:5afcd0:8", "const:4:8"]]
+ 005afcd0 ["CALL", null, ["callee:00851550:8"]]
- 005afc90 bytes 1a860a94
+ 005afcd0 bytes 20860a94
- 005afca4 ["INT_ADD", "register:40f0:8", ["const:5afca4:8", "const:4:8"]]
- 005afca4 ["CALL", null, ["callee:00903f98:8"]]
+ 005afce4 ["INT_ADD", "register:40f0:8", ["const:5afce4:8", "const:4:8"]]
+ 005afce4 ["CALL", null, ["callee:00903f98:8"]]
- 005afca4 bytes a8500d94
+ 005afce4 bytes ad500d94
- 005afcac ["INT_ADD", "register:40f0:8", ["const:5afcac:8", "const:4:8"]]
- 005afcac ["CALL", null, ["callee:00851550:8"]]
+ 005afcec ["INT_ADD", "register:40f0:8", ["const:5afcec:8", "const:4:8"]]
+ 005afcec ["CALL", null, ["callee:00851550:8"]]
- 005afcac bytes 13860a94
+ 005afcec bytes 19860a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ea259739ac147b244095895a3e20915"></a>

### [`005afdec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afdec.md) → [`005afe2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005af/005afe2c.md) FUN_005afe2c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 1件 [`005afc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afc78.md)
- 新版 呼出元 1件 [`00a47f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47f54.md) · 呼出先 1件 [`005afcb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005af/005afcb8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005afdf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afdec.md#insn-005afdf8)
- 新版 `005afe38`（命令位置の公開資料なし）

~~~diff
- 005afdf8 ["INT_ADD", "register:40f0:8", ["const:5afdf8:8", "const:4:8"]]
- 005afdf8 ["CALL", null, ["callee:005afcb8:8"]]
+ 005afe38 ["INT_ADD", "register:40f0:8", ["const:5afe38:8", "const:4:8"]]
+ 005afe38 ["CALL", null, ["callee:005afcb8:8"]]
- 005afdf8 bytes a0ffff97
+ 005afe38 bytes a0ffff97
~~~


<a id="compare-7e2a3f5ab36640cd8de4c22997f6e867"></a>

### [`005afe08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afe08.md) → [`005afe48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005af/005afe48.md) FUN_005afe48

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 8件 [`005afc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afc78.md) [`00662878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/00662878.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008c2d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c2/008c2d24.md) [`00903f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00903/00903f44.md)
- 新版 呼出元 1件 [`00a47f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47f54.md) · 呼出先 8件 [`005afcb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005af/005afcb8.md) [`006628b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00662/006628b8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008c2d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2d7c.md) [`00903f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00903/00903f98.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005afe18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afe08.md#insn-005afe18) · [`005afe24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afe08.md#insn-005afe24) · [`005afe48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afe08.md#insn-005afe48)
- 新版 `005afe58`（命令位置の公開資料なし） · `005afe64`（命令位置の公開資料なし） · `005afe88`（命令位置の公開資料なし）

~~~diff
- 005afe18 ["INT_ADD", "register:40f0:8", ["const:5afe18:8", "const:4:8"]]
- 005afe18 ["CALL", null, ["callee:005afcb8:8"]]
+ 005afe58 ["INT_ADD", "register:40f0:8", ["const:5afe58:8", "const:4:8"]]
+ 005afe58 ["CALL", null, ["callee:005afcb8:8"]]
- 005afe18 bytes 98ffff97
+ 005afe58 bytes 98ffff97
- 005afe24 ["INT_ADD", "register:40f0:8", ["const:5afe24:8", "const:4:8"]]
- 005afe24 ["CALL", null, ["callee:005afcb8:8"]]
+ 005afe64 ["INT_ADD", "register:40f0:8", ["const:5afe64:8", "const:4:8"]]
+ 005afe64 ["CALL", null, ["callee:005afcb8:8"]]
- 005afe24 bytes 95ffff97
+ 005afe64 bytes 95ffff97
- 005afe48 ["INT_ADD", "register:40f0:8", ["const:5afe48:8", "const:4:8"]]
- 005afe48 ["CALL", null, ["callee:005afcb8:8"]]
+ 005afe88 ["INT_ADD", "register:40f0:8", ["const:5afe88:8", "const:4:8"]]
+ 005afe88 ["CALL", null, ["callee:005afcb8:8"]]
- 005afe48 bytes 8cffff97
+ 005afe88 bytes 8cffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e57c68eb7944a7a6711fddbc8a23c0ac"></a>

### [`005b0064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0064.md) → [`005b00a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b0/005b00a4.md) FUN_005b00a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 2件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008c2d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c2/008c2d24.md)
- 新版 呼出元 1件 [`00a47f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47f54.md) · 呼出先 2件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008c2d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2d7c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b0074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0064.md#insn-005b0074) · [`005b0088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0064.md#insn-005b0088)
- 新版 `005b00b4`（命令位置の公開資料なし） · `005b00c8`（命令位置の公開資料なし）

~~~diff
- 005b0074 ["INT_ADD", "register:40f0:8", ["const:5b0074:8", "const:4:8"]]
- 005b0074 ["CALL", null, ["callee:00851550:8"]]
+ 005b00b4 ["INT_ADD", "register:40f0:8", ["const:5b00b4:8", "const:4:8"]]
+ 005b00b4 ["CALL", null, ["callee:00851550:8"]]
- 005b0074 bytes 21850a94
+ 005b00b4 bytes 27850a94
- 005b0088 ["INT_ADD", "register:40f0:8", ["const:5b0088:8", "const:4:8"]]
- 005b0088 ["CALL", null, ["callee:008c2d7c:8"]]
+ 005b00c8 ["INT_ADD", "register:40f0:8", ["const:5b00c8:8", "const:4:8"]]
+ 005b00c8 ["CALL", null, ["callee:008c2d7c:8"]]
- 005b0088 bytes 274b0c94
+ 005b00c8 bytes 2d4b0c94
~~~


<a id="compare-c3dd89273f67f3e6e629b7bc6581cbf7"></a>

### [`005b00c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b00c0.md) → [`005b0100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b0/005b0100.md) FUN_005b0100

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 4件 [`005afc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afc78.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008c2d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c2/008c2d24.md) [`00ab927c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab9/00ab927c.md)
- 新版 呼出元 1件 [`00a47f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47f54.md) · 呼出先 4件 [`005afcb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005af/005afcb8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008c2d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2d7c.md) [`00ab92ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ab9/00ab92ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b00d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b00c0.md#insn-005b00d0) · [`005b00dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b00c0.md#insn-005b00dc) · [`005b00ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b00c0.md#insn-005b00ec)
- 新版 `005b0110`（命令位置の公開資料なし） · `005b011c`（命令位置の公開資料なし） · `005b012c`（命令位置の公開資料なし）

~~~diff
- 005b00d0 ["INT_ADD", "register:40f0:8", ["const:5b00d0:8", "const:4:8"]]
- 005b00d0 ["CALL", null, ["callee:005afcb8:8"]]
+ 005b0110 ["INT_ADD", "register:40f0:8", ["const:5b0110:8", "const:4:8"]]
+ 005b0110 ["CALL", null, ["callee:005afcb8:8"]]
- 005b00d0 bytes eafeff97
+ 005b0110 bytes eafeff97
- 005b00dc ["INT_ADD", "register:40f0:8", ["const:5b00dc:8", "const:4:8"]]
- 005b00dc ["CALL", null, ["callee:00851550:8"]]
+ 005b011c ["INT_ADD", "register:40f0:8", ["const:5b011c:8", "const:4:8"]]
+ 005b011c ["CALL", null, ["callee:00851550:8"]]
- 005b00dc bytes 07850a94
+ 005b011c bytes 0d850a94
- 005b00ec ["INT_ADD", "register:40f0:8", ["const:5b00ec:8", "const:4:8"]]
- 005b00ec ["CALL", null, ["callee:00ab92ec:8"]]
+ 005b012c ["INT_ADD", "register:40f0:8", ["const:5b012c:8", "const:4:8"]]
+ 005b012c ["CALL", null, ["callee:00ab92ec:8"]]
- 005b00ec bytes 64241494
+ 005b012c bytes 70241494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00795995d675b5fe28b917f8b05c0e20"></a>

### [`005b06cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b06cc.md) → [`005b070c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b0/005b070c.md) FUN_005b070c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`005f65cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f6/005f65cc.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) [`00a51fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a51/00a51fc4.md) · 呼出先 11件 [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`005afc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afc78.md) [`005e1b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1b18.md) [`005e1b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1b30.md) [`006647c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006647c0.md)
- 新版 呼出元 4件 [`005f660c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f6/005f660c.md) [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) [`00a47f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47f54.md) [`00a52034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a52/00a52034.md) · 呼出先 11件 [`0049f430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f430.md) [`005afcb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005af/005afcb8.md) [`005e1b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e1b58.md) [`005e1b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e1b70.md) [`00664800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664800.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b06e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b06cc.md#insn-005b06e8) · [`005b06f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b06cc.md#insn-005b06f4) · [`005b0704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b06cc.md#insn-005b0704)
- 新版 `005b0728`（命令位置の公開資料なし） · `005b0734`（命令位置の公開資料なし） · `005b0744`（命令位置の公開資料なし）

~~~diff
- 005b06e8 ["INT_ADD", "register:40f0:8", ["const:5b06e8:8", "const:4:8"]]
- 005b06e8 ["CALL", null, ["callee:00851550:8"]]
+ 005b0728 ["INT_ADD", "register:40f0:8", ["const:5b0728:8", "const:4:8"]]
+ 005b0728 ["CALL", null, ["callee:00851550:8"]]
- 005b06e8 bytes 84830a94
+ 005b0728 bytes 8a830a94
- 005b06f4 ["INT_ADD", "register:40f0:8", ["const:5b06f4:8", "const:4:8"]]
- 005b06f4 ["CALL", null, ["callee:00802bb0:8"]]
+ 005b0734 ["INT_ADD", "register:40f0:8", ["const:5b0734:8", "const:4:8"]]
+ 005b0734 ["CALL", null, ["callee:00802bb0:8"]]
- 005b06f4 bytes 19490994
+ 005b0734 bytes 1f490994
- 005b0704 ["INT_ADD", "register:40f0:8", ["const:5b0704:8", "const:4:8"]]
- 005b0704 ["CALL", null, ["callee:0066a65c:8"]]
+ 005b0744 ["INT_ADD", "register:40f0:8", ["const:5b0744:8", "const:4:8"]]
+ 005b0744 ["CALL", null, ["callee:0066a65c:8"]]
- 005b0704 bytes c6e70294
+ 005b0744 bytes c6e70294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dacc56d28921a9522fe098fdc547c8e"></a>

### [`005b0bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0bdc.md) → [`005b0c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b0/005b0c1c.md) FUN_005b0c1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005b212c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b212c.md) [`005b3140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3140.md) [`005b6918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6918.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005b0c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0c48.md)
- 新版 呼出元 3件 [`005b216c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b216c.md) [`005b3180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3180.md) [`005b6958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6958.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`005b0c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b0/005b0c88.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b0c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0bdc.md#insn-005b0c14) · [`005b0c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0bdc.md#insn-005b0c1c)
- 新版 `005b0c54`（命令位置の公開資料なし） · `005b0c5c`（命令位置の公開資料なし）

~~~diff
- 005b0c14 ["INT_ADD", "register:40f0:8", ["const:5b0c14:8", "const:4:8"]]
- 005b0c14 ["CALL", null, ["callee:0043bb60:8"]]
+ 005b0c54 ["INT_ADD", "register:40f0:8", ["const:5b0c54:8", "const:4:8"]]
+ 005b0c54 ["CALL", null, ["callee:0043bb60:8"]]
- 005b0c14 bytes c32bfa97
+ 005b0c54 bytes c32bfa97
- 005b0c1c ["INT_ADD", "register:40f0:8", ["const:5b0c1c:8", "const:4:8"]]
- 005b0c1c ["CALL", null, ["callee:005b0c88:8"]]
+ 005b0c5c ["INT_ADD", "register:40f0:8", ["const:5b0c5c:8", "const:4:8"]]
+ 005b0c5c ["CALL", null, ["callee:005b0c88:8"]]
- 005b0c1c bytes 0b000094
+ 005b0c5c bytes 0b000094
~~~


<a id="compare-f25518b6791d6807094a50c0cc3e0509"></a>

### [`005b1338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1338.md) → [`005b1378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1378.md) FUN_005b1378

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) · 呼出先 2件 [`00879bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879bb8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) · 呼出先 2件 [`00879c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879c10.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b134c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1338.md#insn-005b134c) · [`005b1354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1338.md#insn-005b1354)
- 新版 `005b138c`（命令位置の公開資料なし） · `005b1394`（命令位置の公開資料なし）

~~~diff
- 005b134c ["INT_ADD", "register:40f0:8", ["const:5b134c:8", "const:4:8"]]
- 005b134c ["CALL", null, ["callee:00c57f60:8"]]
+ 005b138c ["INT_ADD", "register:40f0:8", ["const:5b138c:8", "const:4:8"]]
+ 005b138c ["CALL", null, ["callee:00c57f60:8"]]
- 005b134c bytes d19a1a94
+ 005b138c bytes f59a1a94
- 005b1354 ["INT_ADD", "register:40f0:8", ["const:5b1354:8", "const:4:8"]]
- 005b1354 ["CALL", null, ["callee:00879c10:8"]]
+ 005b1394 ["INT_ADD", "register:40f0:8", ["const:5b1394:8", "const:4:8"]]
+ 005b1394 ["CALL", null, ["callee:00879c10:8"]]
- 005b1354 bytes 19220b94
+ 005b1394 bytes 1f220b94
~~~


<a id="compare-2baacde591c15f3fe0593bb25afb9368"></a>

### [`005b13a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b13a8.md) → [`005b13e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b13e8.md) FUN_005b13e8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008485ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/008485ec.md) [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) · 呼出先 4件 [`005b5220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5220.md) [`005b5290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5290.md) [`00879d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879d7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00848644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848644.md) [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) · 呼出先 4件 [`005b5260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5260.md) [`005b52d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b52d0.md) [`00879dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879dd4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b13c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b13a8.md#insn-005b13c4) · [`005b13f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b13a8.md#insn-005b13f4) · [`005b1400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b13a8.md#insn-005b1400)
- 新版 `005b1404`（命令位置の公開資料なし） · `005b1434`（命令位置の公開資料なし） · `005b1440`（命令位置の公開資料なし）

~~~diff
- 005b13c4 ["INT_ADD", "register:40f0:8", ["const:5b13c4:8", "const:4:8"]]
- 005b13c4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005b1404 ["INT_ADD", "register:40f0:8", ["const:5b1404:8", "const:4:8"]]
+ 005b1404 ["CALL", null, ["callee:00c57f80:8"]]
- 005b13c4 bytes bb9a1a94
+ 005b1404 bytes df9a1a94
- 005b13f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b13f4 ["INT_ADD", "register:40f0:8", ["const:5b13f4:8", "const:4:8"]]
- 005b13f4 ["CALLIND", null, ["register:0:8"]]
+ 005b1434 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b1434 ["INT_ADD", "register:40f0:8", ["const:5b1434:8", "const:4:8"]]
+ 005b1434 ["CALLIND", null, ["register:0:8"]]
- 005b13f4 bytes 00013fd6
+ 005b1434 bytes 00013fd6
- 005b1400 ["INT_ADD", "register:40f0:8", ["const:5b1400:8", "const:4:8"]]
- 005b1400 ["CALL", null, ["callee:005b52d0:8"]]
+ 005b1440 ["INT_ADD", "register:40f0:8", ["const:5b1440:8", "const:4:8"]]
+ 005b1440 ["CALL", null, ["callee:005b52d0:8"]]
- 005b1400 bytes a40f0094
+ 005b1440 bytes a40f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-540451d961668ec5fb3882b31a4ebef6"></a>

### [`005b1440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1440.md) → [`005b1480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1480.md) FUN_005b1480

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a8d008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8d/00a8d008.md) · 呼出先 2件 [`005b5220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5220.md) [`005b5290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5290.md)
- 新版 呼出元 1件 [`00a8a488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a8a/00a8a488.md) · 呼出先 2件 [`005b5260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5260.md) [`005b52d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b52d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b1478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1440.md#insn-005b1478) · [`005b1490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1440.md#insn-005b1490)
- 新版 `005b14b8`（命令位置の公開資料なし） · `005b14d0`（命令位置の公開資料なし）

~~~diff
- 005b1478 ["INT_ADD", "register:40f0:8", ["const:5b1478:8", "const:4:8"]]
- 005b1478 ["CALL", null, ["callee:005b5260:8"]]
+ 005b14b8 ["INT_ADD", "register:40f0:8", ["const:5b14b8:8", "const:4:8"]]
+ 005b14b8 ["CALL", null, ["callee:005b5260:8"]]
- 005b1478 bytes 6a0f0094
+ 005b14b8 bytes 6a0f0094
- 005b1490 ["INT_ADD", "register:40f0:8", ["const:5b1490:8", "const:4:8"]]
- 005b1490 ["CALL", null, ["callee:005b52d0:8"]]
+ 005b14d0 ["INT_ADD", "register:40f0:8", ["const:5b14d0:8", "const:4:8"]]
+ 005b14d0 ["CALL", null, ["callee:005b52d0:8"]]
- 005b1490 bytes 800f0094
+ 005b14d0 bytes 800f0094
~~~


<a id="compare-dee9a56c6e13afe1b7320550fb8867dc"></a>

### [`005b22a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b22a0.md) → [`005b22e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b22e0.md) FUN_005b22e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b22bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b22a0.md#insn-005b22bc) · [`005b22dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b22a0.md#insn-005b22dc)
- 新版 `005b22fc`（命令位置の公開資料なし） · `005b231c`（命令位置の公開資料なし）

~~~diff
- 005b22bc ["INT_ADD", "register:40f0:8", ["const:5b22bc:8", "const:4:8"]]
- 005b22bc ["CALL", null, ["callee:00c53da0:8"]]
+ 005b22fc ["INT_ADD", "register:40f0:8", ["const:5b22fc:8", "const:4:8"]]
+ 005b22fc ["CALL", null, ["callee:00c53da0:8"]]
- 005b22bc bytes 91861a94
+ 005b22fc bytes a9861a94
- 005b22dc ["COPY", "register:0:8", ["register:4040:8"]]
- 005b22dc ["INT_ADD", "register:40f0:8", ["const:5b22dc:8", "const:4:8"]]
- 005b22dc ["CALLIND", null, ["register:0:8"]]
+ 005b231c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b231c ["INT_ADD", "register:40f0:8", ["const:5b231c:8", "const:4:8"]]
+ 005b231c ["CALLIND", null, ["register:0:8"]]
- 005b22dc bytes 00013fd6
+ 005b231c bytes 00013fd6
~~~


<a id="compare-0adfdd86119ce1023280d559817d8fee"></a>

### [`005b2c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2c90.md) → [`005b2cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b2cd0.md) FUN_005b2cd0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`005b2b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2b08.md) [`00865110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865110.md) [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) [`008a72a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a72a8.md) · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`005b9398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9398.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`005b2b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b2b48.md) [`00865168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865168.md) [`00895a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00895/00895a28.md) [`008a7300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a7/008a7300.md) · 呼出先 6件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`005b93d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b93d8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b2d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2c90.md#insn-005b2d6c) · [`005b2d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2c90.md#insn-005b2d9c) · [`005b2da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2c90.md#insn-005b2da4)
- 新版 `005b2dac`（命令位置の公開資料なし） · `005b2ddc`（命令位置の公開資料なし） · `005b2de4`（命令位置の公開資料なし）

~~~diff
- 005b2d6c ["INT_ADD", "register:40f0:8", ["const:5b2d6c:8", "const:4:8"]]
- 005b2d6c ["CALL", null, ["callee:00494650:8"]]
+ 005b2dac ["INT_ADD", "register:40f0:8", ["const:5b2dac:8", "const:4:8"]]
+ 005b2dac ["CALL", null, ["callee:00494650:8"]]
- 005b2d6c bytes 2986fb97
+ 005b2dac bytes 2986fb97
- 005b2d9c ["COPY", "register:0:8", ["register:4040:8"]]
- 005b2d9c ["INT_ADD", "register:40f0:8", ["const:5b2d9c:8", "const:4:8"]]
- 005b2d9c ["CALLIND", null, ["register:0:8"]]
+ 005b2ddc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b2ddc ["INT_ADD", "register:40f0:8", ["const:5b2ddc:8", "const:4:8"]]
+ 005b2ddc ["CALLIND", null, ["register:0:8"]]
- 005b2d9c bytes 00013fd6
+ 005b2ddc bytes 00013fd6
- 005b2da4 ["INT_ADD", "register:40f0:8", ["const:5b2da4:8", "const:4:8"]]
- 005b2da4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005b2de4 ["INT_ADD", "register:40f0:8", ["const:5b2de4:8", "const:4:8"]]
+ 005b2de4 ["CALL", null, ["callee:00c57f80:8"]]
- 005b2da4 bytes 43941a94
+ 005b2de4 bytes 67941a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fc684b57e875756b23c4ff3270b2493"></a>

### [`005b2ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2ee8.md) → [`005b2f28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b2f28.md) FUN_005b2f28

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`005b2b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2b08.md) [`00865110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865110.md) [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) [`008a72a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a72a8.md) · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`005b9500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9500.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`005b2b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b2b48.md) [`00865168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865168.md) [`00895a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00895/00895a28.md) [`008a7300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a7/008a7300.md) · 呼出先 6件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`005b9540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9540.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b2fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2ee8.md#insn-005b2fc4) · [`005b2ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2ee8.md#insn-005b2ff4) · [`005b2ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2ee8.md#insn-005b2ffc)
- 新版 `005b3004`（命令位置の公開資料なし） · `005b3034`（命令位置の公開資料なし） · `005b303c`（命令位置の公開資料なし）

~~~diff
- 005b2fc4 ["INT_ADD", "register:40f0:8", ["const:5b2fc4:8", "const:4:8"]]
- 005b2fc4 ["CALL", null, ["callee:00494650:8"]]
+ 005b3004 ["INT_ADD", "register:40f0:8", ["const:5b3004:8", "const:4:8"]]
+ 005b3004 ["CALL", null, ["callee:00494650:8"]]
- 005b2fc4 bytes 9385fb97
+ 005b3004 bytes 9385fb97
- 005b2ff4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b2ff4 ["INT_ADD", "register:40f0:8", ["const:5b2ff4:8", "const:4:8"]]
- 005b2ff4 ["CALLIND", null, ["register:0:8"]]
+ 005b3034 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b3034 ["INT_ADD", "register:40f0:8", ["const:5b3034:8", "const:4:8"]]
+ 005b3034 ["CALLIND", null, ["register:0:8"]]
- 005b2ff4 bytes 00013fd6
+ 005b3034 bytes 00013fd6
- 005b2ffc ["INT_ADD", "register:40f0:8", ["const:5b2ffc:8", "const:4:8"]]
- 005b2ffc ["CALL", null, ["callee:00c57f80:8"]]
+ 005b303c ["INT_ADD", "register:40f0:8", ["const:5b303c:8", "const:4:8"]]
+ 005b303c ["CALL", null, ["callee:00c57f80:8"]]
- 005b2ffc bytes ad931a94
+ 005b303c bytes d1931a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cf33ee8ac7ae0b609c4ee8cec92ab43"></a>

### [`005b4e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4e54.md) → [`005b4e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b4/005b4e94.md) FUN_005b4e94

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005b1e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1e24.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0059c89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059c/0059c89c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`005b1e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1e64.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0059c8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059c/0059c8dc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b4e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4e54.md#insn-005b4e8c) · [`005b4eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4e54.md#insn-005b4eb8) · [`005b4ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4e54.md#insn-005b4ee4)
- 新版 `005b4ecc`（命令位置の公開資料なし） · `005b4ef8`（命令位置の公開資料なし） · `005b4f24`（命令位置の公開資料なし）

~~~diff
- 005b4e8c ["INT_ADD", "register:40f0:8", ["const:5b4e8c:8", "const:4:8"]]
- 005b4e8c ["CALL", null, ["callee:00c57f60:8"]]
+ 005b4ecc ["INT_ADD", "register:40f0:8", ["const:5b4ecc:8", "const:4:8"]]
+ 005b4ecc ["CALL", null, ["callee:00c57f60:8"]]
- 005b4e8c bytes 018c1a94
+ 005b4ecc bytes 258c1a94
- 005b4eb8 ["INT_ADD", "register:40f0:8", ["const:5b4eb8:8", "const:4:8"]]
- 005b4eb8 ["CALL", null, ["callee:0043bb60:8"]]
+ 005b4ef8 ["INT_ADD", "register:40f0:8", ["const:5b4ef8:8", "const:4:8"]]
+ 005b4ef8 ["CALL", null, ["callee:0043bb60:8"]]
- 005b4eb8 bytes 1a1bfa97
+ 005b4ef8 bytes 1a1bfa97
- 005b4ee4 ["INT_ADD", "register:40f0:8", ["const:5b4ee4:8", "const:4:8"]]
- 005b4ee4 ["CALL", null, ["callee:0043bb60:8"]]
+ 005b4f24 ["INT_ADD", "register:40f0:8", ["const:5b4f24:8", "const:4:8"]]
+ 005b4f24 ["CALL", null, ["callee:0043bb60:8"]]
- 005b4ee4 bytes 0f1bfa97
+ 005b4f24 bytes 0f1bfa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04dd77759a44e3442e2343897cc84937"></a>

### [`005b5220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5220.md) → [`005b5260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5260.md) FUN_005b5260

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`005b13a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b13a8.md) [`005b1440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1440.md) [`005b5220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5220.md) · 呼出先 2件 [`005b5220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5220.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`005b13e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b13e8.md) [`005b1480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1480.md) [`005b5260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5260.md) · 呼出先 2件 [`005b5260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5260.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b523c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5220.md#insn-005b523c) · [`005b5248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5220.md#insn-005b5248) · [`005b527c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5220.md#insn-005b527c)
- 新版 `005b527c`（命令位置の公開資料なし） · `005b5288`（命令位置の公開資料なし） · `005b52bc`（命令位置の公開資料なし）

~~~diff
- 005b523c ["INT_ADD", "register:40f0:8", ["const:5b523c:8", "const:4:8"]]
- 005b523c ["CALL", null, ["local:b0:8"]]
+ 005b527c ["INT_ADD", "register:40f0:8", ["const:5b527c:8", "const:4:8"]]
+ 005b527c ["CALL", null, ["local:b0:8"]]
- 005b523c bytes f9ffff97
+ 005b527c bytes f9ffff97
- 005b5248 ["INT_ADD", "register:40f0:8", ["const:5b5248:8", "const:4:8"]]
- 005b5248 ["CALL", null, ["local:b0:8"]]
+ 005b5288 ["INT_ADD", "register:40f0:8", ["const:5b5288:8", "const:4:8"]]
+ 005b5288 ["CALL", null, ["local:b0:8"]]
- 005b5248 bytes f6ffff97
+ 005b5288 bytes f6ffff97
- 005b527c ["COPY", "register:0:8", ["register:4040:8"]]
- 005b527c ["INT_ADD", "register:40f0:8", ["const:5b527c:8", "const:4:8"]]
- 005b527c ["CALLIND", null, ["register:0:8"]]
+ 005b52bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b52bc ["INT_ADD", "register:40f0:8", ["const:5b52bc:8", "const:4:8"]]
+ 005b52bc ["CALLIND", null, ["register:0:8"]]
- 005b527c bytes 00013fd6
+ 005b52bc bytes 00013fd6
~~~


<a id="compare-c600c157c88bdd8ebc1e7b94711e35bb"></a>

### [`005b5290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5290.md) → [`005b52d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b52d0.md) FUN_005b52d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`005b13a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b13a8.md) [`005b1440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1440.md) [`005b5290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5290.md) · 呼出先 2件 [`005b5290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5290.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`005b13e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b13e8.md) [`005b1480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1480.md) [`005b52d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b52d0.md) · 呼出先 2件 [`005b52d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b52d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b52ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5290.md#insn-005b52ac) · [`005b52b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5290.md#insn-005b52b8) · [`005b52ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5290.md#insn-005b52ec)
- 新版 `005b52ec`（命令位置の公開資料なし） · `005b52f8`（命令位置の公開資料なし） · `005b532c`（命令位置の公開資料なし）

~~~diff
- 005b52ac ["INT_ADD", "register:40f0:8", ["const:5b52ac:8", "const:4:8"]]
- 005b52ac ["CALL", null, ["local:b0:8"]]
+ 005b52ec ["INT_ADD", "register:40f0:8", ["const:5b52ec:8", "const:4:8"]]
+ 005b52ec ["CALL", null, ["local:b0:8"]]
- 005b52ac bytes f9ffff97
+ 005b52ec bytes f9ffff97
- 005b52b8 ["INT_ADD", "register:40f0:8", ["const:5b52b8:8", "const:4:8"]]
- 005b52b8 ["CALL", null, ["local:b0:8"]]
+ 005b52f8 ["INT_ADD", "register:40f0:8", ["const:5b52f8:8", "const:4:8"]]
+ 005b52f8 ["CALL", null, ["local:b0:8"]]
- 005b52b8 bytes f6ffff97
+ 005b52f8 bytes f6ffff97
- 005b52ec ["COPY", "register:0:8", ["register:4040:8"]]
- 005b52ec ["INT_ADD", "register:40f0:8", ["const:5b52ec:8", "const:4:8"]]
- 005b52ec ["CALLIND", null, ["register:0:8"]]
+ 005b532c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b532c ["INT_ADD", "register:40f0:8", ["const:5b532c:8", "const:4:8"]]
+ 005b532c ["CALLIND", null, ["register:0:8"]]
- 005b52ec bytes 00013fd6
+ 005b532c bytes 00013fd6
~~~


<a id="compare-8c19052c87fb75d21166e7f31cdd60db"></a>

### [`005b5564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5564.md) → [`005b55a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b55a4.md) FUN_005b55a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005b18d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b18d0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005b1910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1910.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b5584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5564.md#insn-005b5584)
- 新版 `005b55c4`（命令位置の公開資料なし）

~~~diff
- 005b5584 ["INT_ADD", "register:40f0:8", ["const:5b5584:8", "const:4:8"]]
- 005b5584 ["CALL", null, ["callee:00c57f80:8"]]
+ 005b55c4 ["INT_ADD", "register:40f0:8", ["const:5b55c4:8", "const:4:8"]]
+ 005b55c4 ["CALL", null, ["callee:00c57f80:8"]]
- 005b5584 bytes 4b8a1a94
+ 005b55c4 bytes 6f8a1a94
~~~


<a id="compare-f5f12c34fdd7efd6e7feccb536d055ec"></a>

### [`005b59e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b59e4.md) → [`005b5a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5a24.md) FUN_005b5a24

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b5a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b59e4.md#insn-005b5a00) · [`005b5a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b59e4.md#insn-005b5a20)
- 新版 `005b5a40`（命令位置の公開資料なし） · `005b5a60`（命令位置の公開資料なし）

~~~diff
- 005b5a00 ["INT_ADD", "register:40f0:8", ["const:5b5a00:8", "const:4:8"]]
- 005b5a00 ["CALL", null, ["callee:00c53da0:8"]]
+ 005b5a40 ["INT_ADD", "register:40f0:8", ["const:5b5a40:8", "const:4:8"]]
+ 005b5a40 ["CALL", null, ["callee:00c53da0:8"]]
- 005b5a00 bytes c0781a94
+ 005b5a40 bytes d8781a94
- 005b5a20 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b5a20 ["INT_ADD", "register:40f0:8", ["const:5b5a20:8", "const:4:8"]]
- 005b5a20 ["CALLIND", null, ["register:0:8"]]
+ 005b5a60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b5a60 ["INT_ADD", "register:40f0:8", ["const:5b5a60:8", "const:4:8"]]
+ 005b5a60 ["CALLIND", null, ["register:0:8"]]
- 005b5a20 bytes 00013fd6
+ 005b5a60 bytes 00013fd6
~~~


<a id="compare-0a9af3ceff3d13678a67ba0b2afd39f5"></a>

### [`005b5ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ce0.md) → [`005b5d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5d20.md) FUN_005b5d20

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b5d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ce0.md#insn-005b5d50) · [`005b5d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ce0.md#insn-005b5d84) · [`005b5d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ce0.md#insn-005b5d88)
- 新版 `005b5d90`（命令位置の公開資料なし） · `005b5dc4`（命令位置の公開資料なし） · `005b5dc8`（命令位置の公開資料なし）

~~~diff
- 005b5d50 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b5d50 ["INT_ADD", "register:40f0:8", ["const:5b5d50:8", "const:4:8"]]
- 005b5d50 ["CALLIND", null, ["register:0:8"]]
+ 005b5d90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b5d90 ["INT_ADD", "register:40f0:8", ["const:5b5d90:8", "const:4:8"]]
+ 005b5d90 ["CALLIND", null, ["register:0:8"]]
- 005b5d50 bytes 00013fd6
+ 005b5d90 bytes 00013fd6
- 005b5d84 ["INT_ADD", "register:40f0:8", ["const:5b5d84:8", "const:4:8"]]
- 005b5d84 ["CALL", null, ["callee:00459db4:8"]]
+ 005b5dc4 ["INT_ADD", "register:40f0:8", ["const:5b5dc4:8", "const:4:8"]]
+ 005b5dc4 ["CALL", null, ["callee:00459db4:8"]]
- 005b5d84 bytes fc8ffa97
+ 005b5dc4 bytes fc8ffa97
- 005b5d88 ["INT_ADD", "register:40f0:8", ["const:5b5d88:8", "const:4:8"]]
- 005b5d88 ["CALL", null, ["callee:00c57fb0:8"]]
+ 005b5dc8 ["INT_ADD", "register:40f0:8", ["const:5b5dc8:8", "const:4:8"]]
+ 005b5dc8 ["CALL", null, ["callee:00c57fb0:8"]]
- 005b5d88 bytes 56881a94
+ 005b5dc8 bytes 7a881a94
~~~


<a id="compare-70bc2df8486b3dcb9cfff683a937f178"></a>

### [`005b5ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ffc.md) → [`005b603c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b603c.md) FUN_005b603c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`005b3348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3348.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`005b3388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3388.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b60a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ffc.md#insn-005b60a4) · [`005b60d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ffc.md#insn-005b60d8) · [`005b60dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ffc.md#insn-005b60dc)
- 新版 `005b60e4`（命令位置の公開資料なし） · `005b6118`（命令位置の公開資料なし） · `005b611c`（命令位置の公開資料なし）

~~~diff
- 005b60a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b60a4 ["INT_ADD", "register:40f0:8", ["const:5b60a4:8", "const:4:8"]]
- 005b60a4 ["CALLIND", null, ["register:0:8"]]
+ 005b60e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b60e4 ["INT_ADD", "register:40f0:8", ["const:5b60e4:8", "const:4:8"]]
+ 005b60e4 ["CALLIND", null, ["register:0:8"]]
- 005b60a4 bytes 00013fd6
+ 005b60e4 bytes 00013fd6
- 005b60d8 ["INT_ADD", "register:40f0:8", ["const:5b60d8:8", "const:4:8"]]
- 005b60d8 ["CALL", null, ["callee:00459db4:8"]]
+ 005b6118 ["INT_ADD", "register:40f0:8", ["const:5b6118:8", "const:4:8"]]
+ 005b6118 ["CALL", null, ["callee:00459db4:8"]]
- 005b60d8 bytes 278ffa97
+ 005b6118 bytes 278ffa97
- 005b60dc ["INT_ADD", "register:40f0:8", ["const:5b60dc:8", "const:4:8"]]
- 005b60dc ["CALL", null, ["callee:00c57fb0:8"]]
+ 005b611c ["INT_ADD", "register:40f0:8", ["const:5b611c:8", "const:4:8"]]
+ 005b611c ["CALL", null, ["callee:00c57fb0:8"]]
- 005b60dc bytes 81871a94
+ 005b611c bytes a5871a94
~~~


<a id="compare-df9642937d6810a50c32ad6a431f8be7"></a>

### [`005b62a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b62a8.md) → [`005b62e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b62e8.md) FUN_005b62e8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b6318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b62a8.md#insn-005b6318) · [`005b634c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b62a8.md#insn-005b634c) · [`005b6350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b62a8.md#insn-005b6350)
- 新版 `005b6358`（命令位置の公開資料なし） · `005b638c`（命令位置の公開資料なし） · `005b6390`（命令位置の公開資料なし）

~~~diff
- 005b6318 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b6318 ["INT_ADD", "register:40f0:8", ["const:5b6318:8", "const:4:8"]]
- 005b6318 ["CALLIND", null, ["register:0:8"]]
+ 005b6358 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b6358 ["INT_ADD", "register:40f0:8", ["const:5b6358:8", "const:4:8"]]
+ 005b6358 ["CALLIND", null, ["register:0:8"]]
- 005b6318 bytes 00013fd6
+ 005b6358 bytes 00013fd6
- 005b634c ["INT_ADD", "register:40f0:8", ["const:5b634c:8", "const:4:8"]]
- 005b634c ["CALL", null, ["callee:00459db4:8"]]
+ 005b638c ["INT_ADD", "register:40f0:8", ["const:5b638c:8", "const:4:8"]]
+ 005b638c ["CALL", null, ["callee:00459db4:8"]]
- 005b634c bytes 8a8efa97
+ 005b638c bytes 8a8efa97
- 005b6350 ["INT_ADD", "register:40f0:8", ["const:5b6350:8", "const:4:8"]]
- 005b6350 ["CALL", null, ["callee:00c57fb0:8"]]
+ 005b6390 ["INT_ADD", "register:40f0:8", ["const:5b6390:8", "const:4:8"]]
+ 005b6390 ["CALL", null, ["callee:00c57fb0:8"]]
- 005b6350 bytes e4861a94
+ 005b6390 bytes 08871a94
~~~


<a id="compare-aa7946d8bf3c53261d6ca95476feec33"></a>

### [`005b65fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b65fc.md) → [`005b663c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b663c.md) FUN_005b663c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b6618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b65fc.md#insn-005b6618) · [`005b6638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b65fc.md#insn-005b6638)
- 新版 `005b6658`（命令位置の公開資料なし） · `005b6678`（命令位置の公開資料なし）

~~~diff
- 005b6618 ["INT_ADD", "register:40f0:8", ["const:5b6618:8", "const:4:8"]]
- 005b6618 ["CALL", null, ["callee:00c53da0:8"]]
+ 005b6658 ["INT_ADD", "register:40f0:8", ["const:5b6658:8", "const:4:8"]]
+ 005b6658 ["CALL", null, ["callee:00c53da0:8"]]
- 005b6618 bytes ba751a94
+ 005b6658 bytes d2751a94
- 005b6638 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b6638 ["INT_ADD", "register:40f0:8", ["const:5b6638:8", "const:4:8"]]
- 005b6638 ["CALLIND", null, ["register:0:8"]]
+ 005b6678 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b6678 ["INT_ADD", "register:40f0:8", ["const:5b6678:8", "const:4:8"]]
+ 005b6678 ["CALLIND", null, ["register:0:8"]]
- 005b6638 bytes 00013fd6
+ 005b6678 bytes 00013fd6
~~~


