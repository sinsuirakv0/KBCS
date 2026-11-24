# v16.0.1 → v16.0.2 · 要調査の変更候補 (8)

[一覧の目次](README.md)

<a id="compare-4d0eb93af9ba571122f9ae47d3ad24ae"></a>

### [`00501740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501740.md) → [`00501780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501780.md) _ZNK5Botan27Certificate_Store_In_Memory12all_subjectsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`005027f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005027f8.md) [`005486f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005486f4.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00502838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502838.md) [`00548734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548734.md) [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00501774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501740.md#insn-00501774) · [`0050178c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501740.md#insn-0050178c) · [`005017a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501740.md#insn-005017a4)
- 新版 `005017b4`（命令位置の公開資料なし） · `005017cc`（命令位置の公開資料なし） · `005017e4`（命令位置の公開資料なし）

~~~diff
- 00501774 ["INT_ADD", "register:40f0:8", ["const:501774:8", "const:4:8"]]
- 00501774 ["CALL", null, ["callee:00548734:8"]]
+ 005017b4 ["INT_ADD", "register:40f0:8", ["const:5017b4:8", "const:4:8"]]
+ 005017b4 ["CALL", null, ["callee:00548734:8"]]
- 00501774 bytes e01b0194
+ 005017b4 bytes e01b0194
- 0050178c ["INT_ADD", "register:40f0:8", ["const:50178c:8", "const:4:8"]]
- 0050178c ["CALL", null, ["callee:00c59ac0:8"]]
+ 005017cc ["INT_ADD", "register:40f0:8", ["const:5017cc:8", "const:4:8"]]
+ 005017cc ["CALL", null, ["callee:00c59ac0:8"]]
- 0050178c bytes 99601d94
+ 005017cc bytes bd601d94
- 005017a4 ["INT_ADD", "register:40f0:8", ["const:5017a4:8", "const:4:8"]]
- 005017a4 ["CALL", null, ["callee:00502838:8"]]
+ 005017e4 ["INT_ADD", "register:40f0:8", ["const:5017e4:8", "const:4:8"]]
+ 005017e4 ["CALL", null, ["callee:00502838:8"]]
- 005017a4 bytes 15040094
+ 005017e4 bytes 15040094
~~~


<a id="compare-2742746891b9e425390c929c25686532"></a>

### [`005017e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/005017e0.md) → [`00501820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501820.md) _ZNK5Botan16X509_Certificate10subject_dnEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005017e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/005017e0.md#insn-005017e8)
- 新版 `00501828`（命令位置の公開資料なし）

~~~diff
- 005017e8 ["INT_ADD", "register:40f0:8", ["const:5017e8:8", "const:4:8"]]
- 005017e8 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00501828 ["INT_ADD", "register:40f0:8", ["const:501828:8", "const:4:8"]]
+ 00501828 ["CALL", null, ["callee:00c59ac0:8"]]
- 005017e8 bytes 82601d94
+ 00501828 bytes a6601d94
~~~


<a id="compare-68c3213d0227ef6abe059b89c54f7919"></a>

### [`005017f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/005017f8.md) → [`00501838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501838.md) FUN_00501838

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00501834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/005017f8.md#insn-00501834) · [`00501850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/005017f8.md#insn-00501850)
- 新版 `00501874`（命令位置の公開資料なし） · `00501890`（命令位置の公開資料なし）

~~~diff
- 00501834 ["INT_ADD", "register:40f0:8", ["const:501834:8", "const:4:8"]]
- 00501834 ["CALL", null, ["callee:0053afd0:8"]]
+ 00501874 ["INT_ADD", "register:40f0:8", ["const:501874:8", "const:4:8"]]
+ 00501874 ["CALL", null, ["callee:0053afd0:8"]]
- 00501834 bytes d7e50094
+ 00501874 bytes d7e50094
- 00501850 ["INT_ADD", "register:40f0:8", ["const:501850:8", "const:4:8"]]
- 00501850 ["CALL", null, ["callee:00c57f80:8"]]
+ 00501890 ["INT_ADD", "register:40f0:8", ["const:501890:8", "const:4:8"]]
+ 00501890 ["CALL", null, ["callee:00c57f80:8"]]
- 00501850 bytes 98591d94
+ 00501890 bytes bc591d94
~~~


<a id="compare-71e685635705fe5efbfe4eb1f8e2d8c0"></a>

### [`00501880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501880.md) → [`005018c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/005018c0.md) _ZNK5Botan27Certificate_Store_In_Memory9find_certERKNS_7X509_DNERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a00.md) · 呼出先 9件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c59ad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ad0.md) · 呼出先 9件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005018cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501880.md#insn-005018cc) · [`005018d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501880.md#insn-005018d4) · [`005018e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501880.md#insn-005018e0)
- 新版 `0050190c`（命令位置の公開資料なし） · `00501914`（命令位置の公開資料なし） · `00501920`（命令位置の公開資料なし）

~~~diff
- 005018cc ["INT_ADD", "register:40f0:8", ["const:5018cc:8", "const:4:8"]]
- 005018cc ["CALL", null, ["callee:00c57f80:8"]]
+ 0050190c ["INT_ADD", "register:40f0:8", ["const:50190c:8", "const:4:8"]]
+ 0050190c ["CALL", null, ["callee:00c57f80:8"]]
- 005018cc bytes 79591d94
+ 0050190c bytes 9d591d94
- 005018d4 ["INT_ADD", "register:40f0:8", ["const:5018d4:8", "const:4:8"]]
- 005018d4 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00501914 ["INT_ADD", "register:40f0:8", ["const:501914:8", "const:4:8"]]
+ 00501914 ["CALL", null, ["callee:00c59ac0:8"]]
- 005018d4 bytes 47601d94
+ 00501914 bytes 6b601d94
- 005018e0 ["INT_ADD", "register:40f0:8", ["const:5018e0:8", "const:4:8"]]
- 005018e0 ["CALL", null, ["callee:00c59ae0:8"]]
+ 00501920 ["INT_ADD", "register:40f0:8", ["const:501920:8", "const:4:8"]]
+ 00501920 ["CALL", null, ["callee:00c59ae0:8"]]
- 005018e0 bytes 4c601d94
+ 00501920 bytes 70601d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1031b9a60c69310ebc70fa78e275486f"></a>

### [`00501a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501a1c.md) → [`00501a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501a5c.md) _ZNK5Botan16X509_Certificate14subject_key_idEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00501a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501a1c.md#insn-00501a24)
- 新版 `00501a64`（命令位置の公開資料なし）

~~~diff
- 00501a24 ["INT_ADD", "register:40f0:8", ["const:501a24:8", "const:4:8"]]
- 00501a24 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00501a64 ["INT_ADD", "register:40f0:8", ["const:501a64:8", "const:4:8"]]
+ 00501a64 ["CALL", null, ["callee:00c59ac0:8"]]
- 00501a24 bytes f35f1d94
+ 00501a64 bytes 17601d94
~~~


<a id="compare-384978b556f73bed69bb19f82701abd8"></a>

### [`00501a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501a34.md) → [`00501a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501a74.md) _ZN5BotaneqERKNS_7X509_DNES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a10.md) · 呼出先 4件 [`00549668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549668.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c598f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c598f0.md) [`00c59a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a20.md)
- 新版 呼出元 1件 [`00c59ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ae0.md) · 呼出先 4件 [`005496a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/005496a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c599c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c599c0.md) [`00c59af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59af0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00501a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501a34.md#insn-00501a60) · [`00501a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501a34.md#insn-00501a6c) · [`00501aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501a34.md#insn-00501aec)
- 新版 `00501aa0`（命令位置の公開資料なし） · `00501aac`（命令位置の公開資料なし） · `00501b2c`（命令位置の公開資料なし）

~~~diff
- 00501a60 ["INT_ADD", "register:40f0:8", ["const:501a60:8", "const:4:8"]]
- 00501a60 ["CALL", null, ["callee:00c59af0:8"]]
+ 00501aa0 ["INT_ADD", "register:40f0:8", ["const:501aa0:8", "const:4:8"]]
+ 00501aa0 ["CALL", null, ["callee:00c59af0:8"]]
- 00501a60 bytes f05f1d94
+ 00501aa0 bytes 14601d94
- 00501a6c ["INT_ADD", "register:40f0:8", ["const:501a6c:8", "const:4:8"]]
- 00501a6c ["CALL", null, ["callee:00c59af0:8"]]
+ 00501aac ["INT_ADD", "register:40f0:8", ["const:501aac:8", "const:4:8"]]
+ 00501aac ["CALL", null, ["callee:00c59af0:8"]]
- 00501a6c bytes ed5f1d94
+ 00501aac bytes 11601d94
- 00501aec ["INT_ADD", "register:40f0:8", ["const:501aec:8", "const:4:8"]]
- 00501aec ["CALL", null, ["callee:00c599c0:8"]]
+ 00501b2c ["INT_ADD", "register:40f0:8", ["const:501b2c:8", "const:4:8"]]
+ 00501b2c ["CALL", null, ["callee:00c599c0:8"]]
- 00501aec bytes 815f1d94
+ 00501b2c bytes a55f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02ec9bb8db24a85ec0b3a439102bfb16"></a>

### [`00501bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501bec.md) → [`00501c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501c2c.md) _ZNK5Botan27Certificate_Store_In_Memory14find_all_certsERKNS_7X509_DNERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a30.md) · 呼出先 10件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00548598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548598.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c59b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b00.md) · 呼出先 10件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`005485d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/005485d8.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00501c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501bec.md#insn-00501c40) · [`00501c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501bec.md#insn-00501c60) · [`00501c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501bec.md#insn-00501c84)
- 新版 `00501c80`（命令位置の公開資料なし） · `00501ca0`（命令位置の公開資料なし） · `00501cc4`（命令位置の公開資料なし）

~~~diff
- 00501c40 ["INT_ADD", "register:40f0:8", ["const:501c40:8", "const:4:8"]]
- 00501c40 ["CALL", null, ["callee:00c57f80:8"]]
+ 00501c80 ["INT_ADD", "register:40f0:8", ["const:501c80:8", "const:4:8"]]
+ 00501c80 ["CALL", null, ["callee:00c57f80:8"]]
- 00501c40 bytes 9c581d94
+ 00501c80 bytes c0581d94
- 00501c60 ["INT_ADD", "register:40f0:8", ["const:501c60:8", "const:4:8"]]
- 00501c60 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00501ca0 ["INT_ADD", "register:40f0:8", ["const:501ca0:8", "const:4:8"]]
+ 00501ca0 ["CALL", null, ["callee:00c59ac0:8"]]
- 00501c60 bytes 645f1d94
+ 00501ca0 bytes 885f1d94
- 00501c84 ["INT_ADD", "register:40f0:8", ["const:501c84:8", "const:4:8"]]
- 00501c84 ["CALL", null, ["callee:00c57f60:8"]]
+ 00501cc4 ["INT_ADD", "register:40f0:8", ["const:501cc4:8", "const:4:8"]]
+ 00501cc4 ["CALL", null, ["callee:00c57f60:8"]]
- 00501c84 bytes 83581d94
+ 00501cc4 bytes a7581d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6d8e1f369ba3275f52217fc9c1e1752"></a>

### [`00501db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501db8.md) → [`00501df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501df8.md) FUN_00501df8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052cdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052cdf0.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0052ce30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052ce30.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00501e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501db8.md#insn-00501e04) · [`00501e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501db8.md#insn-00501e18) · [`00501e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501db8.md#insn-00501e20)
- 新版 `00501e44`（命令位置の公開資料なし） · `00501e58`（命令位置の公開資料なし） · `00501e60`（命令位置の公開資料なし）

~~~diff
- 00501e04 ["INT_ADD", "register:40f0:8", ["const:501e04:8", "const:4:8"]]
- 00501e04 ["CALL", null, ["callee:00c53da0:8"]]
+ 00501e44 ["INT_ADD", "register:40f0:8", ["const:501e44:8", "const:4:8"]]
+ 00501e44 ["CALL", null, ["callee:00c53da0:8"]]
- 00501e04 bytes bf471d94
+ 00501e44 bytes d7471d94
- 00501e18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00501e18 ["INT_ADD", "register:40f0:8", ["const:501e18:8", "const:4:8"]]
- 00501e18 ["CALLIND", null, ["register:0:8"]]
+ 00501e58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00501e58 ["INT_ADD", "register:40f0:8", ["const:501e58:8", "const:4:8"]]
+ 00501e58 ["CALLIND", null, ["register:0:8"]]
- 00501e18 bytes 00013fd6
+ 00501e58 bytes 00013fd6
- 00501e20 ["INT_ADD", "register:40f0:8", ["const:501e20:8", "const:4:8"]]
- 00501e20 ["CALL", null, ["callee:00c57f50:8"]]
+ 00501e60 ["INT_ADD", "register:40f0:8", ["const:501e60:8", "const:4:8"]]
+ 00501e60 ["CALL", null, ["callee:00c57f50:8"]]
- 00501e20 bytes 18581d94
+ 00501e60 bytes 3c581d94
~~~


<a id="compare-10f179ee3440b27a07088883d3867cdd"></a>

### [`00502150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502150.md) → [`00502190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502190.md) _ZNK5Botan16X509_Certificate28subject_public_key_bitstringEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502150.md#insn-00502158)
- 新版 `00502198`（命令位置の公開資料なし）

~~~diff
- 00502158 ["INT_ADD", "register:40f0:8", ["const:502158:8", "const:4:8"]]
- 00502158 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00502198 ["INT_ADD", "register:40f0:8", ["const:502198:8", "const:4:8"]]
+ 00502198 ["CALL", null, ["callee:00c59ac0:8"]]
- 00502158 bytes 265e1d94
+ 00502198 bytes 4a5e1d94
~~~


<a id="compare-c4aae54dee2e41e53043293ad696ebb3"></a>

### [`00502470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502470.md) → [`005024b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005024b0.md) _ZNK5Botan16X509_Certificate14raw_subject_dnEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502470.md#insn-00502478)
- 新版 `005024b8`（命令位置の公開資料なし）

~~~diff
- 00502478 ["INT_ADD", "register:40f0:8", ["const:502478:8", "const:4:8"]]
- 00502478 ["CALL", null, ["callee:00c59ac0:8"]]
+ 005024b8 ["INT_ADD", "register:40f0:8", ["const:5024b8:8", "const:4:8"]]
+ 005024b8 ["CALL", null, ["callee:00c59ac0:8"]]
- 00502478 bytes 5e5d1d94
+ 005024b8 bytes 825d1d94
~~~


<a id="compare-712e143b3e2208e6683911cd73e46119"></a>

### [`005025fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005025fc.md) → [`0050263c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/0050263c.md) _ZN5Botan27Certificate_Store_In_Memory7add_crlENSt6__ndk110shared_ptrIKNS_8X509_CRLEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a40.md) · 呼出先 11件 [`005027f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005027f8.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00548bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548bc0.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 1件 [`00c59b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b10.md) · 呼出先 11件 [`00502838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502838.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00548c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548c00.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005025fc.md#insn-00502630) · [`0050263c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005025fc.md#insn-0050263c) · [`00502654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005025fc.md#insn-00502654)
- 新版 `00502670`（命令位置の公開資料なし） · `0050267c`（命令位置の公開資料なし） · `00502694`（命令位置の公開資料なし）

~~~diff
- 00502630 ["INT_ADD", "register:40f0:8", ["const:502630:8", "const:4:8"]]
- 00502630 ["CALL", null, ["callee:00c59b20:8"]]
+ 00502670 ["INT_ADD", "register:40f0:8", ["const:502670:8", "const:4:8"]]
+ 00502670 ["CALL", null, ["callee:00c59b20:8"]]
- 00502630 bytes 085d1d94
+ 00502670 bytes 2c5d1d94
- 0050263c ["INT_ADD", "register:40f0:8", ["const:50263c:8", "const:4:8"]]
- 0050263c ["CALL", null, ["callee:00502838:8"]]
+ 0050267c ["INT_ADD", "register:40f0:8", ["const:50267c:8", "const:4:8"]]
+ 0050267c ["CALL", null, ["callee:00502838:8"]]
- 0050263c bytes 6f000094
+ 0050267c bytes 6f000094
- 00502654 ["INT_ADD", "register:40f0:8", ["const:502654:8", "const:4:8"]]
- 00502654 ["CALL", null, ["callee:00c59b20:8"]]
+ 00502694 ["INT_ADD", "register:40f0:8", ["const:502694:8", "const:4:8"]]
+ 00502694 ["CALL", null, ["callee:00c59b20:8"]]
- 00502654 bytes ff5c1d94
+ 00502694 bytes 235d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec403db5cadc27a6e5578bddf424dd17"></a>

### [`005027a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005027a4.md) → [`005027e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005027e4.md) FUN_005027e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005027c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005027a4.md#insn-005027c0) · [`005027e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005027a4.md#insn-005027e0)
- 新版 `00502800`（命令位置の公開資料なし） · `00502820`（命令位置の公開資料なし）

~~~diff
- 005027c0 ["INT_ADD", "register:40f0:8", ["const:5027c0:8", "const:4:8"]]
- 005027c0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00502800 ["INT_ADD", "register:40f0:8", ["const:502800:8", "const:4:8"]]
+ 00502800 ["CALL", null, ["callee:00c53da0:8"]]
- 005027c0 bytes 50451d94
+ 00502800 bytes 68451d94
- 005027e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005027e0 ["INT_ADD", "register:40f0:8", ["const:5027e0:8", "const:4:8"]]
- 005027e0 ["CALLIND", null, ["register:0:8"]]
+ 00502820 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00502820 ["INT_ADD", "register:40f0:8", ["const:502820:8", "const:4:8"]]
+ 00502820 ["CALLIND", null, ["register:0:8"]]
- 005027e0 bytes 00013fd6
+ 00502820 bytes 00013fd6
~~~


<a id="compare-b9cfa1c0dc2e3af85f6bd096c63f043c"></a>

### [`00502924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502924.md) → [`00502964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502964.md) _ZNK5Botan8X509_CRL11this_updateEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050292c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502924.md#insn-0050292c)
- 新版 `0050296c`（命令位置の公開資料なし）

~~~diff
- 0050292c ["INT_ADD", "register:40f0:8", ["const:50292c:8", "const:4:8"]]
- 0050292c ["CALL", null, ["callee:00c59b20:8"]]
+ 0050296c ["INT_ADD", "register:40f0:8", ["const:50296c:8", "const:4:8"]]
+ 0050296c ["CALL", null, ["callee:00c59b20:8"]]
- 0050292c bytes 495c1d94
+ 0050296c bytes 6d5c1d94
~~~


<a id="compare-401e2ffb0f99c65f0db7b2cf3bbd0118"></a>

### [`0050293c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/0050293c.md) → [`0050297c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/0050297c.md) _ZNK5Botan27Certificate_Store_In_Memory12find_crl_forERKNS_16X509_CertificateE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 10件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/0050293c.md#insn-00502978) · [`00502994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/0050293c.md#insn-00502994) · [`0050299c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/0050293c.md#insn-0050299c)
- 新版 `005029b8`（命令位置の公開資料なし） · `005029d4`（命令位置の公開資料なし） · `005029dc`（命令位置の公開資料なし）

~~~diff
- 00502978 ["INT_ADD", "register:40f0:8", ["const:502978:8", "const:4:8"]]
- 00502978 ["CALL", null, ["callee:00c59ac0:8"]]
+ 005029b8 ["INT_ADD", "register:40f0:8", ["const:5029b8:8", "const:4:8"]]
+ 005029b8 ["CALL", null, ["callee:00c59ac0:8"]]
- 00502978 bytes 1e5c1d94
+ 005029b8 bytes 425c1d94
- 00502994 ["INT_ADD", "register:40f0:8", ["const:502994:8", "const:4:8"]]
- 00502994 ["CALL", null, ["callee:00c57f80:8"]]
+ 005029d4 ["INT_ADD", "register:40f0:8", ["const:5029d4:8", "const:4:8"]]
+ 005029d4 ["CALL", null, ["callee:00c57f80:8"]]
- 00502994 bytes 47551d94
+ 005029d4 bytes 6b551d94
- 0050299c ["INT_ADD", "register:40f0:8", ["const:50299c:8", "const:4:8"]]
- 0050299c ["CALL", null, ["callee:00c59b20:8"]]
+ 005029dc ["INT_ADD", "register:40f0:8", ["const:5029dc:8", "const:4:8"]]
+ 005029dc ["CALL", null, ["callee:00c59b20:8"]]
- 0050299c bytes 2d5c1d94
+ 005029dc bytes 515c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68acf65eae9c75ca5bd55b153765eeea"></a>

### [`00502af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502af4.md) → [`00502b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502b34.md) _ZNK5Botan16X509_Certificate16authority_key_idEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502af4.md#insn-00502afc)
- 新版 `00502b3c`（命令位置の公開資料なし）

~~~diff
- 00502afc ["INT_ADD", "register:40f0:8", ["const:502afc:8", "const:4:8"]]
- 00502afc ["CALL", null, ["callee:00c59ac0:8"]]
+ 00502b3c ["INT_ADD", "register:40f0:8", ["const:502b3c:8", "const:4:8"]]
+ 00502b3c ["CALL", null, ["callee:00c59ac0:8"]]
- 00502afc bytes bd5b1d94
+ 00502b3c bytes e15b1d94
~~~


<a id="compare-720e5813c861be8143e416074f79d7f4"></a>

### [`00502b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502b0c.md) → [`00502b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502b4c.md) _ZNK5Botan8X509_CRL16authority_key_idEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502b0c.md#insn-00502b14)
- 新版 `00502b54`（命令位置の公開資料なし）

~~~diff
- 00502b14 ["INT_ADD", "register:40f0:8", ["const:502b14:8", "const:4:8"]]
- 00502b14 ["CALL", null, ["callee:00c59b20:8"]]
+ 00502b54 ["INT_ADD", "register:40f0:8", ["const:502b54:8", "const:4:8"]]
+ 00502b54 ["CALL", null, ["callee:00c59b20:8"]]
- 00502b14 bytes cf5b1d94
+ 00502b54 bytes f35b1d94
~~~


<a id="compare-497c406c998a1ab2ffb510eb9d18cfbd"></a>

### [`00502b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502b24.md) → [`00502b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502b64.md) _ZNK5Botan16X509_Certificate9issuer_dnEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502b24.md#insn-00502b2c)
- 新版 `00502b6c`（命令位置の公開資料なし）

~~~diff
- 00502b2c ["INT_ADD", "register:40f0:8", ["const:502b2c:8", "const:4:8"]]
- 00502b2c ["CALL", null, ["callee:00c59ac0:8"]]
+ 00502b6c ["INT_ADD", "register:40f0:8", ["const:502b6c:8", "const:4:8"]]
+ 00502b6c ["CALL", null, ["callee:00c59ac0:8"]]
- 00502b2c bytes b15b1d94
+ 00502b6c bytes d55b1d94
~~~


<a id="compare-fed8bbd67e0c7ff1fc07d6b93aac3c4e"></a>

### [`00502ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502ba4.md) → [`00502be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502be4.md) FUN_00502be4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502ba4.md#insn-00502bf0) · [`00502c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502ba4.md#insn-00502c04) · [`00502c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502ba4.md#insn-00502c0c)
- 新版 `00502c30`（命令位置の公開資料なし） · `00502c44`（命令位置の公開資料なし） · `00502c4c`（命令位置の公開資料なし）

~~~diff
- 00502bf0 ["INT_ADD", "register:40f0:8", ["const:502bf0:8", "const:4:8"]]
- 00502bf0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00502c30 ["INT_ADD", "register:40f0:8", ["const:502c30:8", "const:4:8"]]
+ 00502c30 ["CALL", null, ["callee:00c53da0:8"]]
- 00502bf0 bytes 44441d94
+ 00502c30 bytes 5c441d94
- 00502c04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00502c04 ["INT_ADD", "register:40f0:8", ["const:502c04:8", "const:4:8"]]
- 00502c04 ["CALLIND", null, ["register:0:8"]]
+ 00502c44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00502c44 ["INT_ADD", "register:40f0:8", ["const:502c44:8", "const:4:8"]]
+ 00502c44 ["CALLIND", null, ["register:0:8"]]
- 00502c04 bytes 00013fd6
+ 00502c44 bytes 00013fd6
- 00502c0c ["INT_ADD", "register:40f0:8", ["const:502c0c:8", "const:4:8"]]
- 00502c0c ["CALL", null, ["callee:00c57f50:8"]]
+ 00502c4c ["INT_ADD", "register:40f0:8", ["const:502c4c:8", "const:4:8"]]
+ 00502c4c ["CALL", null, ["callee:00c57f50:8"]]
- 00502c0c bytes 9d541d94
+ 00502c4c bytes c1541d94
~~~


<a id="compare-63c488bbeb6335c687df8670e9783275"></a>

### [`00502ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502ec0.md) → [`00502f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502f00.md) FUN_00502f00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502ec0.md#insn-00502edc) · [`00502efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502ec0.md#insn-00502efc)
- 新版 `00502f1c`（命令位置の公開資料なし） · `00502f3c`（命令位置の公開資料なし）

~~~diff
- 00502edc ["INT_ADD", "register:40f0:8", ["const:502edc:8", "const:4:8"]]
- 00502edc ["CALL", null, ["callee:00c53da0:8"]]
+ 00502f1c ["INT_ADD", "register:40f0:8", ["const:502f1c:8", "const:4:8"]]
+ 00502f1c ["CALL", null, ["callee:00c53da0:8"]]
- 00502edc bytes 89431d94
+ 00502f1c bytes a1431d94
- 00502efc ["COPY", "register:0:8", ["register:4040:8"]]
- 00502efc ["INT_ADD", "register:40f0:8", ["const:502efc:8", "const:4:8"]]
- 00502efc ["CALLIND", null, ["register:0:8"]]
+ 00502f3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00502f3c ["INT_ADD", "register:40f0:8", ["const:502f3c:8", "const:4:8"]]
+ 00502f3c ["CALLIND", null, ["register:0:8"]]
- 00502efc bytes 00013fd6
+ 00502f3c bytes 00013fd6
~~~


<a id="compare-7b55c4edc7187c3f3a281d39cee6de1c"></a>

### [`005034c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/005034c0.md) → [`00503500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503500.md) FUN_00503500

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005034dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/005034c0.md#insn-005034dc) · [`005034fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/005034c0.md#insn-005034fc)
- 新版 `0050351c`（命令位置の公開資料なし） · `0050353c`（命令位置の公開資料なし）

~~~diff
- 005034dc ["INT_ADD", "register:40f0:8", ["const:5034dc:8", "const:4:8"]]
- 005034dc ["CALL", null, ["callee:00c53da0:8"]]
+ 0050351c ["INT_ADD", "register:40f0:8", ["const:50351c:8", "const:4:8"]]
+ 0050351c ["CALL", null, ["callee:00c53da0:8"]]
- 005034dc bytes 09421d94
+ 0050351c bytes 21421d94
- 005034fc ["COPY", "register:0:8", ["register:4040:8"]]
- 005034fc ["INT_ADD", "register:40f0:8", ["const:5034fc:8", "const:4:8"]]
- 005034fc ["CALLIND", null, ["register:0:8"]]
+ 0050353c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050353c ["INT_ADD", "register:40f0:8", ["const:50353c:8", "const:4:8"]]
+ 0050353c ["CALLIND", null, ["register:0:8"]]
- 005034fc bytes 00013fd6
+ 0050353c bytes 00013fd6
~~~


<a id="compare-c2643ab420cdfcba78c9469ba7e5ea7a"></a>

### [`00503510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503510.md) → [`00503550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503550.md) _ZN5BotaneqERKNS_9CRL_EntryES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a90.md) · 呼出先 3件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c589e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589e0.md) [`00c59aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59aa0.md)
- 新版 呼出元 1件 [`00c59b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b60.md) · 呼出先 3件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c58ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ab0.md) [`00c59b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00503528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503510.md#insn-00503528) · [`00503534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503510.md#insn-00503534) · [`00503554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503510.md#insn-00503554)
- 新版 `00503568`（命令位置の公開資料なし） · `00503574`（命令位置の公開資料なし） · `00503594`（命令位置の公開資料なし）

~~~diff
- 00503528 ["INT_ADD", "register:40f0:8", ["const:503528:8", "const:4:8"]]
- 00503528 ["CALL", null, ["callee:00c59b70:8"]]
+ 00503568 ["INT_ADD", "register:40f0:8", ["const:503568:8", "const:4:8"]]
+ 00503568 ["CALL", null, ["callee:00c59b70:8"]]
- 00503528 bytes 5e591d94
+ 00503568 bytes 82591d94
- 00503534 ["INT_ADD", "register:40f0:8", ["const:503534:8", "const:4:8"]]
- 00503534 ["CALL", null, ["callee:00c59b70:8"]]
+ 00503574 ["INT_ADD", "register:40f0:8", ["const:503574:8", "const:4:8"]]
+ 00503574 ["CALL", null, ["callee:00c59b70:8"]]
- 00503534 bytes 5b591d94
+ 00503574 bytes 7f591d94
- 00503554 ["INT_ADD", "register:40f0:8", ["const:503554:8", "const:4:8"]]
- 00503554 ["CALL", null, ["callee:00c58120:8"]]
+ 00503594 ["INT_ADD", "register:40f0:8", ["const:503594:8", "const:4:8"]]
+ 00503594 ["CALL", null, ["callee:00c58120:8"]]
- 00503554 bytes bf521d94
+ 00503594 bytes e3521d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c21e83be4628c7b4ceb06d6cb0c9c106"></a>

### [`005035c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/005035c0.md) → [`00503600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503600.md) _ZNK5Botan9CRL_Entry11expire_timeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005035c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/005035c0.md#insn-005035c8)
- 新版 `00503608`（命令位置の公開資料なし）

~~~diff
- 005035c8 ["INT_ADD", "register:40f0:8", ["const:5035c8:8", "const:4:8"]]
- 005035c8 ["CALL", null, ["callee:00c59b70:8"]]
+ 00503608 ["INT_ADD", "register:40f0:8", ["const:503608:8", "const:4:8"]]
+ 00503608 ["CALL", null, ["callee:00c59b70:8"]]
- 005035c8 bytes 36591d94
+ 00503608 bytes 5a591d94
~~~


<a id="compare-87b17be90de1691635d5502e07d71b5d"></a>

### [`005035d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/005035d8.md) → [`00503618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503618.md) _ZNK5Botan9CRL_Entry11reason_codeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005035e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/005035d8.md#insn-005035e0)
- 新版 `00503620`（命令位置の公開資料なし）

~~~diff
- 005035e0 ["INT_ADD", "register:40f0:8", ["const:5035e0:8", "const:4:8"]]
- 005035e0 ["CALL", null, ["callee:00c59b70:8"]]
+ 00503620 ["INT_ADD", "register:40f0:8", ["const:503620:8", "const:4:8"]]
+ 00503620 ["CALL", null, ["callee:00c59b70:8"]]
- 005035e0 bytes 30591d94
+ 00503620 bytes 54591d94
~~~


<a id="compare-92024de225af228a173f95219a0e7d91"></a>

### [`005035f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/005035f0.md) → [`00503630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503630.md) _ZN5BotanneERKNS_9CRL_EntryES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005035f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/005035f0.md#insn-005035f8)
- 新版 `00503638`（命令位置の公開資料なし）

~~~diff
- 005035f8 ["INT_ADD", "register:40f0:8", ["const:5035f8:8", "const:4:8"]]
- 005035f8 ["CALL", null, ["callee:00c59b60:8"]]
+ 00503638 ["INT_ADD", "register:40f0:8", ["const:503638:8", "const:4:8"]]
+ 00503638 ["CALL", null, ["callee:00c59b60:8"]]
- 005035f8 bytes 26591d94
+ 00503638 bytes 4a591d94
~~~


<a id="compare-d3d982f79b5b7912d0371eb6cc7c5257"></a>

### [`00503754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503754.md) → [`00503794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503794.md) _ZNK5Botan9CRL_Entry10extensionsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050375c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503754.md#insn-0050375c)
- 新版 `0050379c`（命令位置の公開資料なし）

~~~diff
- 0050375c ["INT_ADD", "register:40f0:8", ["const:50375c:8", "const:4:8"]]
- 0050375c ["CALL", null, ["callee:00c59b70:8"]]
+ 0050379c ["INT_ADD", "register:40f0:8", ["const:50379c:8", "const:4:8"]]
+ 0050379c ["CALL", null, ["callee:00c59b70:8"]]
- 0050375c bytes d1581d94
+ 0050379c bytes f5581d94
~~~


<a id="compare-88675c4833df66e6d5eca080b2e14973"></a>

### [`00503d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503d98.md) → [`00503dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503dd8.md) _ZNK5Botan10Data_StoreeqERKS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00548f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548f88.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00548fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548fc8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00503de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503d98.md#insn-00503de4)
- 新版 `00503e24`（命令位置の公開資料なし）

~~~diff
- 00503de4 ["INT_ADD", "register:40f0:8", ["const:503de4:8", "const:4:8"]]
- 00503de4 ["CALL", null, ["callee:00548fc8:8"]]
+ 00503e24 ["INT_ADD", "register:40f0:8", ["const:503e24:8", "const:4:8"]]
+ 00503e24 ["CALL", null, ["callee:00548fc8:8"]]
- 00503de4 bytes 69140194
+ 00503e24 bytes 69140194
~~~


<a id="compare-c688e13899f4e7608704cb3bb935d964"></a>

### [`00503e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503e74.md) → [`00503eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503eb4.md) _ZNK5Botan10Data_Store9has_valueERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00503ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503e74.md#insn-00503ee0)
- 新版 `00503f20`（命令位置の公開資料なし）

~~~diff
- 00503ee0 ["INT_ADD", "register:40f0:8", ["const:503ee0:8", "const:4:8"]]
- 00503ee0 ["CALL", null, ["callee:00c58120:8"]]
+ 00503f20 ["INT_ADD", "register:40f0:8", ["const:503f20:8", "const:4:8"]]
+ 00503f20 ["CALL", null, ["callee:00c58120:8"]]
- 00503ee0 bytes 5c501d94
+ 00503f20 bytes 80501d94
~~~


<a id="compare-b91d16f2c2517a6014db4b0a596414b4"></a>

### [`00503f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503f34.md) → [`00503f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503f74.md) _ZNK5Botan10Data_Store10search_forENSt6__ndk18functionIFbNS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES8_EEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ad0.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`005490d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/005490d4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c59ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ba0.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00549114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/00549114.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00503fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503f34.md#insn-00503fc4) · [`00503ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503f34.md#insn-00503ff0) · [`0050400c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503f34.md#insn-0050400c)
- 新版 `00504004`（命令位置の公開資料なし） · `00504030`（命令位置の公開資料なし） · `0050404c`（命令位置の公開資料なし）

~~~diff
- 00503fc4 ["INT_ADD", "register:40f0:8", ["const:503fc4:8", "const:4:8"]]
- 00503fc4 ["CALL", null, ["callee:0043bb60:8"]]
+ 00504004 ["INT_ADD", "register:40f0:8", ["const:504004:8", "const:4:8"]]
+ 00504004 ["CALL", null, ["callee:0043bb60:8"]]
- 00503fc4 bytes d7defc97
+ 00504004 bytes d7defc97
- 00503ff0 ["INT_ADD", "register:40f0:8", ["const:503ff0:8", "const:4:8"]]
- 00503ff0 ["CALL", null, ["callee:0043bb60:8"]]
+ 00504030 ["INT_ADD", "register:40f0:8", ["const:504030:8", "const:4:8"]]
+ 00504030 ["CALL", null, ["callee:0043bb60:8"]]
- 00503ff0 bytes ccdefc97
+ 00504030 bytes ccdefc97
- 0050400c ["COPY", "register:0:8", ["register:4040:8"]]
- 0050400c ["INT_ADD", "register:40f0:8", ["const:50400c:8", "const:4:8"]]
- 0050400c ["CALLIND", null, ["register:0:8"]]
+ 0050404c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050404c ["INT_ADD", "register:40f0:8", ["const:50404c:8", "const:4:8"]]
+ 0050404c ["CALLIND", null, ["register:0:8"]]
- 0050400c bytes 00013fd6
+ 0050404c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a62d7c9400bd55cf303e9d5ad54f0ceb"></a>

### [`005041c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005041c0.md) → [`00504200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504200.md) _ZNK5Botan10Data_Store3getERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ae0.md) · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00548098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548098.md)
- 新版 呼出元 1件 [`00c59bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59bb0.md) · 呼出先 3件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md) [`005480d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/005480d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005041dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005041c0.md#insn-005041dc) · [`00504234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005041c0.md#insn-00504234) · [`00504248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005041c0.md#insn-00504248)
- 新版 `0050421c`（命令位置の公開資料なし） · `00504274`（命令位置の公開資料なし） · `00504288`（命令位置の公開資料なし）

~~~diff
- 005041dc ["INT_ADD", "register:40f0:8", ["const:5041dc:8", "const:4:8"]]
- 005041dc ["CALL", null, ["callee:005480d8:8"]]
+ 0050421c ["INT_ADD", "register:40f0:8", ["const:50421c:8", "const:4:8"]]
+ 0050421c ["CALL", null, ["callee:005480d8:8"]]
- 005041dc bytes af0f0194
+ 0050421c bytes af0f0194
- 00504234 ["INT_ADD", "register:40f0:8", ["const:504234:8", "const:4:8"]]
- 00504234 ["CALL", null, ["callee:00540dbc:8"]]
+ 00504274 ["INT_ADD", "register:40f0:8", ["const:504274:8", "const:4:8"]]
+ 00504274 ["CALL", null, ["callee:00540dbc:8"]]
- 00504234 bytes d2f20094
+ 00504274 bytes d2f20094
- 00504248 ["INT_ADD", "register:40f0:8", ["const:504248:8", "const:4:8"]]
- 00504248 ["CALL", null, ["callee:0043bb60:8"]]
+ 00504288 ["INT_ADD", "register:40f0:8", ["const:504288:8", "const:4:8"]]
+ 00504288 ["CALL", null, ["callee:0043bb60:8"]]
- 00504248 bytes 36defc97
+ 00504288 bytes 36defc97
~~~


<a id="compare-34cc1bf36fc070ceb8242c6b8fbbdd39"></a>

### [`005049c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005049c8.md) → [`00504a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504a08.md) _ZN5Botan10Data_Store3addERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEj

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58790.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58860.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005049f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005049c8.md#insn-005049f8) · [`00504a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005049c8.md#insn-00504a08) · [`00504a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005049c8.md#insn-00504a18)
- 新版 `00504a38`（命令位置の公開資料なし） · `00504a48`（命令位置の公開資料なし） · `00504a58`（命令位置の公開資料なし）

~~~diff
- 005049f8 ["INT_ADD", "register:40f0:8", ["const:5049f8:8", "const:4:8"]]
- 005049f8 ["CALL", null, ["callee:00c58860:8"]]
+ 00504a38 ["INT_ADD", "register:40f0:8", ["const:504a38:8", "const:4:8"]]
+ 00504a38 ["CALL", null, ["callee:00c58860:8"]]
- 005049f8 bytes 664f1d94
+ 00504a38 bytes 8a4f1d94
- 00504a08 ["INT_ADD", "register:40f0:8", ["const:504a08:8", "const:4:8"]]
- 00504a08 ["CALL", null, ["callee:004ff1e0:8"]]
+ 00504a48 ["INT_ADD", "register:40f0:8", ["const:504a48:8", "const:4:8"]]
+ 00504a48 ["CALL", null, ["callee:004ff1e0:8"]]
- 00504a08 bytes e6e9ff97
+ 00504a48 bytes e6e9ff97
- 00504a18 ["INT_ADD", "register:40f0:8", ["const:504a18:8", "const:4:8"]]
- 00504a18 ["CALL", null, ["callee:00c57f80:8"]]
+ 00504a58 ["INT_ADD", "register:40f0:8", ["const:504a58:8", "const:4:8"]]
+ 00504a58 ["CALL", null, ["callee:00c57f80:8"]]
- 00504a18 bytes 264d1d94
+ 00504a58 bytes 4a4d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b5750eb30c51d7c6ec713f114fda352"></a>

### [`00504d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504d90.md) → [`00504dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504dd0.md) _ZN5Botan10Data_Store3addERKNSt6__ndk18multimapINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES8_NS1_4lessIS8_EENS6_INS1_4pai

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0053bb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bb70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0053bbb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053bbb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00504dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504d90.md#insn-00504dcc)
- 新版 `00504e0c`（命令位置の公開資料なし）

~~~diff
- 00504dcc ["INT_ADD", "register:40f0:8", ["const:504dcc:8", "const:4:8"]]
- 00504dcc ["CALL", null, ["callee:0053bbb0:8"]]
+ 00504e0c ["INT_ADD", "register:40f0:8", ["const:504e0c:8", "const:4:8"]]
+ 00504e0c ["CALL", null, ["callee:0053bbb0:8"]]
- 00504dcc bytes 69db0094
+ 00504e0c bytes 69db0094
~~~


<a id="compare-131d83a8abc6026a5a524bfd94925b49"></a>

### [`00504fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504fd4.md) → [`00505014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505014.md) _ZN5Botan7X509_DN13add_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md) [`00c59b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b00.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md) [`00c59bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59bd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00505004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504fd4.md#insn-00505004) · [`00505014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504fd4.md#insn-00505014) · [`00505024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504fd4.md#insn-00505024)
- 新版 `00505044`（命令位置の公開資料なし） · `00505054`（命令位置の公開資料なし） · `00505064`（命令位置の公開資料なし）

~~~diff
- 00505004 ["INT_ADD", "register:40f0:8", ["const:505004:8", "const:4:8"]]
- 00505004 ["CALL", null, ["callee:00c58750:8"]]
+ 00505044 ["INT_ADD", "register:40f0:8", ["const:505044:8", "const:4:8"]]
+ 00505044 ["CALL", null, ["callee:00c58750:8"]]
- 00505004 bytes 9f4d1d94
+ 00505044 bytes c34d1d94
- 00505014 ["INT_ADD", "register:40f0:8", ["const:505014:8", "const:4:8"]]
- 00505014 ["CALL", null, ["callee:00c59bd0:8"]]
+ 00505054 ["INT_ADD", "register:40f0:8", ["const:505054:8", "const:4:8"]]
+ 00505054 ["CALL", null, ["callee:00c59bd0:8"]]
- 00505014 bytes bb521d94
+ 00505054 bytes df521d94
- 00505024 ["INT_ADD", "register:40f0:8", ["const:505024:8", "const:4:8"]]
- 00505024 ["CALL", null, ["callee:00c57f80:8"]]
+ 00505064 ["INT_ADD", "register:40f0:8", ["const:505064:8", "const:4:8"]]
+ 00505064 ["CALL", null, ["callee:00c57f80:8"]]
- 00505024 bytes a34b1d94
+ 00505064 bytes c74b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-777b64ed92459f7f5001efc1758850d9"></a>

### [`005052d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00505/005052d4.md) → [`00505314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505314.md) FUN_00505314

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0052d510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d510.md) [`0052e334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052e334.md) · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md)
- 新版 呼出元 2件 [`0052d550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md) [`0052e374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md) · 呼出先 2件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005052ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00505/005052d4.md#insn-005052ec)
- 新版 `0050532c`（命令位置の公開資料なし）

~~~diff
- 005052ec ["INT_ADD", "register:40f0:8", ["const:5052ec:8", "const:4:8"]]
- 005052ec ["CALL", null, ["callee:0053afd0:8"]]
+ 0050532c ["INT_ADD", "register:40f0:8", ["const:50532c:8", "const:4:8"]]
+ 0050532c ["CALL", null, ["callee:0053afd0:8"]]
- 005052ec bytes 29d70094
+ 0050532c bytes 29d70094
~~~


<a id="compare-072e616ac49025bf8676ce6fb00c6f2f"></a>

### [`00507ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507ab4.md) → [`00507af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507af4.md) _ZNK5Botan16X509_Certificate16subject_alt_nameEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0050736c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/0050736c.md) · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 1件 [`005073ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/005073ac.md) · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00507abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507ab4.md#insn-00507abc)
- 新版 `00507afc`（命令位置の公開資料なし）

~~~diff
- 00507abc ["INT_ADD", "register:40f0:8", ["const:507abc:8", "const:4:8"]]
- 00507abc ["CALL", null, ["callee:00c59ac0:8"]]
+ 00507afc ["INT_ADD", "register:40f0:8", ["const:507afc:8", "const:4:8"]]
+ 00507afc ["CALL", null, ["callee:00c59ac0:8"]]
- 00507abc bytes cd471d94
+ 00507afc bytes f1471d94
~~~


<a id="compare-75e1b70b45dd836730afefca0772db7b"></a>

### [`00507e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507e04.md) → [`00507e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507e44.md) _ZNK5Botan7X509_DN13get_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b60.md) · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`0054b274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b274.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c59c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c30.md) · 呼出先 7件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md) [`0054b2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054b2b4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00507e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507e04.md#insn-00507e38) · [`00507e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507e04.md#insn-00507e44) · [`00507e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507e04.md#insn-00507e54)
- 新版 `00507e78`（命令位置の公開資料なし） · `00507e84`（命令位置の公開資料なし） · `00507e94`（命令位置の公開資料なし）

~~~diff
- 00507e38 ["INT_ADD", "register:40f0:8", ["const:507e38:8", "const:4:8"]]
- 00507e38 ["CALL", null, ["callee:00c59c40:8"]]
+ 00507e78 ["INT_ADD", "register:40f0:8", ["const:507e78:8", "const:4:8"]]
+ 00507e78 ["CALL", null, ["callee:00c59c40:8"]]
- 00507e38 bytes 4e471d94
+ 00507e78 bytes 72471d94
- 00507e44 ["INT_ADD", "register:40f0:8", ["const:507e44:8", "const:4:8"]]
- 00507e44 ["CALL", null, ["callee:00c58750:8"]]
+ 00507e84 ["INT_ADD", "register:40f0:8", ["const:507e84:8", "const:4:8"]]
+ 00507e84 ["CALL", null, ["callee:00c58750:8"]]
- 00507e44 bytes 0f421d94
+ 00507e84 bytes 33421d94
- 00507e54 ["INT_ADD", "register:40f0:8", ["const:507e54:8", "const:4:8"]]
- 00507e54 ["CALL", null, ["callee:00c57f80:8"]]
+ 00507e94 ["INT_ADD", "register:40f0:8", ["const:507e94:8", "const:4:8"]]
+ 00507e94 ["CALL", null, ["callee:00c57f80:8"]]
- 00507e54 bytes 17401d94
+ 00507e94 bytes 3b401d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dee1fb011775d9f965ef2040e586437"></a>

### [`00508b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508b0c.md) → [`00508b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508b4c.md) _ZNK5Botan7X509_DN14get_attributesEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a20.md) · 呼出先 4件 [`0054b06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b06c.md) [`0054b19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b19c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c59af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59af0.md) · 呼出先 4件 [`0054b0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054b0ac.md) [`0054b1dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054b1dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00508b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508b0c.md#insn-00508b8c) · [`00508b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508b0c.md#insn-00508b98) · [`00508ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508b0c.md#insn-00508ba8)
- 新版 `00508bcc`（命令位置の公開資料なし） · `00508bd8`（命令位置の公開資料なし） · `00508be8`（命令位置の公開資料なし）

~~~diff
- 00508b8c ["INT_ADD", "register:40f0:8", ["const:508b8c:8", "const:4:8"]]
- 00508b8c ["CALL", null, ["callee:0054b1dc:8"]]
+ 00508bcc ["INT_ADD", "register:40f0:8", ["const:508bcc:8", "const:4:8"]]
+ 00508bcc ["CALL", null, ["callee:0054b1dc:8"]]
- 00508b8c bytes 84090194
+ 00508bcc bytes 84090194
- 00508b98 ["INT_ADD", "register:40f0:8", ["const:508b98:8", "const:4:8"]]
- 00508b98 ["CALL", null, ["callee:0054b0ac:8"]]
+ 00508bd8 ["INT_ADD", "register:40f0:8", ["const:508bd8:8", "const:4:8"]]
+ 00508bd8 ["CALL", null, ["callee:0054b0ac:8"]]
- 00508b98 bytes 35090194
+ 00508bd8 bytes 35090194
- 00508ba8 ["INT_ADD", "register:40f0:8", ["const:508ba8:8", "const:4:8"]]
- 00508ba8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00508be8 ["INT_ADD", "register:40f0:8", ["const:508be8:8", "const:4:8"]]
+ 00508be8 ["CALL", null, ["callee:00c57f80:8"]]
- 00508ba8 bytes c23c1d94
+ 00508be8 bytes e63c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67093a5febe69439d018caf735e05e80"></a>

### [`00508d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508d04.md) → [`00508d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508d44.md) FUN_00508d44

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00508d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508d04.md#insn-00508d20)
- 新版 `00508d60`（命令位置の公開資料なし）

~~~diff
- 00508d20 ["INT_ADD", "register:40f0:8", ["const:508d20:8", "const:4:8"]]
- 00508d20 ["CALL", null, ["callee:00c57f80:8"]]
+ 00508d60 ["INT_ADD", "register:40f0:8", ["const:508d60:8", "const:4:8"]]
+ 00508d60 ["CALL", null, ["callee:00c57f80:8"]]
- 00508d20 bytes 643c1d94
+ 00508d60 bytes 883c1d94
~~~


<a id="compare-f82a132ec7f115a7e81a01f236e53c23"></a>

### [`00509128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509128.md) → [`00509168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509168.md) FUN_00509168

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00509144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509128.md#insn-00509144)
- 新版 `00509184`（命令位置の公開資料なし）

~~~diff
- 00509144 ["INT_ADD", "register:40f0:8", ["const:509144:8", "const:4:8"]]
- 00509144 ["CALL", null, ["callee:00c57f80:8"]]
+ 00509184 ["INT_ADD", "register:40f0:8", ["const:509184:8", "const:4:8"]]
+ 00509184 ["CALL", null, ["callee:00c57f80:8"]]
- 00509144 bytes 5b3b1d94
+ 00509184 bytes 7f3b1d94
~~~


<a id="compare-f18c186e5ef3d261ba60f8b3971daf8e"></a>

### [`005097a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/005097a0.md) → [`005097e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005097e0.md) _ZN5BotanneERKNS_7X509_DNES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005097a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/005097a0.md#insn-005097a8)
- 新版 `005097e8`（命令位置の公開資料なし）

~~~diff
- 005097a8 ["INT_ADD", "register:40f0:8", ["const:5097a8:8", "const:4:8"]]
- 005097a8 ["CALL", null, ["callee:00c59ae0:8"]]
+ 005097e8 ["INT_ADD", "register:40f0:8", ["const:5097e8:8", "const:4:8"]]
+ 005097e8 ["CALL", null, ["callee:00c59ae0:8"]]
- 005097a8 bytes 9a401d94
+ 005097e8 bytes be401d94
~~~


<a id="compare-965993bec94d8fae9d5462cfada47773"></a>

### [`00509b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509b78.md) → [`00509bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509bb8.md) _ZNK5Botan4OCSP7Request13base64_encodeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58bd0.md) [`00c59bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59bb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ca0.md) [`00c59c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00509b9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509b78.md#insn-00509b9c) · [`00509bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509b78.md#insn-00509bac) · [`00509bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509b78.md#insn-00509bbc)
- 新版 `00509bdc`（命令位置の公開資料なし） · `00509bec`（命令位置の公開資料なし） · `00509bfc`（命令位置の公開資料なし）

~~~diff
- 00509b9c ["INT_ADD", "register:40f0:8", ["const:509b9c:8", "const:4:8"]]
- 00509b9c ["CALL", null, ["callee:00c59c80:8"]]
+ 00509bdc ["INT_ADD", "register:40f0:8", ["const:509bdc:8", "const:4:8"]]
+ 00509bdc ["CALL", null, ["callee:00c59c80:8"]]
- 00509b9c bytes 05401d94
+ 00509bdc bytes 29401d94
- 00509bac ["INT_ADD", "register:40f0:8", ["const:509bac:8", "const:4:8"]]
- 00509bac ["CALL", null, ["callee:00c58ca0:8"]]
+ 00509bec ["INT_ADD", "register:40f0:8", ["const:509bec:8", "const:4:8"]]
+ 00509bec ["CALL", null, ["callee:00c58ca0:8"]]
- 00509bac bytes 093c1d94
+ 00509bec bytes 2d3c1d94
- 00509bbc ["INT_ADD", "register:40f0:8", ["const:509bbc:8", "const:4:8"]]
- 00509bbc ["CALL", null, ["callee:00c57f80:8"]]
+ 00509bfc ["INT_ADD", "register:40f0:8", ["const:509bfc:8", "const:4:8"]]
+ 00509bfc ["CALL", null, ["callee:00c57f80:8"]]
- 00509bbc bytes bd381d94
+ 00509bfc bytes e1381d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a225e82e78926b6bb051abe8b3b7b205"></a>

### [`0050b35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b35c.md) → [`0050b39c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b39c.md) FUN_0050b39c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00510d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510d58.md) · 呼出先 2件 [`0053b424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b424.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00510d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510d98.md) · 呼出先 2件 [`0053b464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b464.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050b378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b35c.md#insn-0050b378) · [`0050b3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b35c.md#insn-0050b3b0)
- 新版 `0050b3b8`（命令位置の公開資料なし） · `0050b3f0`（命令位置の公開資料なし）

~~~diff
- 0050b378 ["INT_ADD", "register:40f0:8", ["const:50b378:8", "const:4:8"]]
- 0050b378 ["CALL", null, ["callee:0053b464:8"]]
+ 0050b3b8 ["INT_ADD", "register:40f0:8", ["const:50b3b8:8", "const:4:8"]]
+ 0050b3b8 ["CALL", null, ["callee:0053b464:8"]]
- 0050b378 bytes 2bc00094
+ 0050b3b8 bytes 2bc00094
- 0050b3b0 ["INT_ADD", "register:40f0:8", ["const:50b3b0:8", "const:4:8"]]
- 0050b3b0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0050b3f0 ["INT_ADD", "register:40f0:8", ["const:50b3f0:8", "const:4:8"]]
+ 0050b3f0 ["CALL", null, ["callee:00c57f80:8"]]
- 0050b3b0 bytes c0321d94
+ 0050b3f0 bytes e4321d94
~~~


<a id="compare-2da7cff4d76f820de1fbf40a37387b15"></a>

### [`0050b3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b3e0.md) → [`0050b420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b420.md) FUN_0050b420

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0054063c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054063c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054067c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054067c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050b418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b3e0.md#insn-0050b418)
- 新版 `0050b458`（命令位置の公開資料なし）

~~~diff
- 0050b418 ["INT_ADD", "register:40f0:8", ["const:50b418:8", "const:4:8"]]
- 0050b418 ["CALL", null, ["callee:0054067c:8"]]
+ 0050b458 ["INT_ADD", "register:40f0:8", ["const:50b458:8", "const:4:8"]]
+ 0050b458 ["CALL", null, ["callee:0054067c:8"]]
- 0050b418 bytes 89d40094
+ 0050b458 bytes 89d40094
~~~


<a id="compare-aa696676306c9fd1a2680706593c16ac"></a>

### [`0050b44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b44c.md) → [`0050b48c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b48c.md) FUN_0050b48c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050b48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b44c.md#insn-0050b48c)
- 新版 `0050b4cc`（命令位置の公開資料なし）

~~~diff
- 0050b48c ["COPY", "register:0:8", ["register:4040:8"]]
- 0050b48c ["INT_ADD", "register:40f0:8", ["const:50b48c:8", "const:4:8"]]
- 0050b48c ["CALLIND", null, ["register:0:8"]]
+ 0050b4cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050b4cc ["INT_ADD", "register:40f0:8", ["const:50b4cc:8", "const:4:8"]]
+ 0050b4cc ["CALLIND", null, ["register:0:8"]]
- 0050b48c bytes 00013fd6
+ 0050b4cc bytes 00013fd6
~~~


<a id="compare-b06b16e844ea914fdf8417643fb0a0bd"></a>

### [`0050bfd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050bfd8.md) → [`0050c018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c018.md) _ZNK5Botan16X509_Certificate13allowed_usageENS_15Key_ConstraintsE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050bfec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050bfd8.md#insn-0050bfec) · [`0050bffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050bfd8.md#insn-0050bffc)
- 新版 `0050c02c`（命令位置の公開資料なし） · `0050c03c`（命令位置の公開資料なし）

~~~diff
- 0050bfec ["INT_ADD", "register:40f0:8", ["const:50bfec:8", "const:4:8"]]
- 0050bfec ["CALL", null, ["callee:00c59ac0:8"]]
+ 0050c02c ["INT_ADD", "register:40f0:8", ["const:50c02c:8", "const:4:8"]]
+ 0050c02c ["CALL", null, ["callee:00c59ac0:8"]]
- 0050bfec bytes 81361d94
+ 0050c02c bytes a5361d94
- 0050bffc ["INT_ADD", "register:40f0:8", ["const:50bffc:8", "const:4:8"]]
- 0050bffc ["CALL", null, ["callee:00c59ac0:8"]]
+ 0050c03c ["INT_ADD", "register:40f0:8", ["const:50c03c:8", "const:4:8"]]
+ 0050c03c ["CALL", null, ["callee:00c59ac0:8"]]
- 0050bffc bytes 7d361d94
+ 0050c03c bytes a1361d94
~~~


<a id="compare-01cbbcd93a5607672f604d4327fabf48"></a>

### [`0050c020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050c020.md) → [`0050c060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c060.md) _ZNK5Botan16X509_Certificate22allowed_extended_usageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c40.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 1件 [`00c59d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d10.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md) [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050c048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050c020.md#insn-0050c048) · [`0050c050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050c020.md#insn-0050c050) · [`0050c0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050c020.md#insn-0050c0c4)
- 新版 `0050c088`（命令位置の公開資料なし） · `0050c090`（命令位置の公開資料なし） · `0050c104`（命令位置の公開資料なし）

~~~diff
- 0050c048 ["INT_ADD", "register:40f0:8", ["const:50c048:8", "const:4:8"]]
- 0050c048 ["CALL", null, ["callee:00c58750:8"]]
+ 0050c088 ["INT_ADD", "register:40f0:8", ["const:50c088:8", "const:4:8"]]
+ 0050c088 ["CALL", null, ["callee:00c58750:8"]]
- 0050c048 bytes 8e311d94
+ 0050c088 bytes b2311d94
- 0050c050 ["INT_ADD", "register:40f0:8", ["const:50c050:8", "const:4:8"]]
- 0050c050 ["CALL", null, ["callee:00c59ac0:8"]]
+ 0050c090 ["INT_ADD", "register:40f0:8", ["const:50c090:8", "const:4:8"]]
+ 0050c090 ["CALL", null, ["callee:00c59ac0:8"]]
- 0050c050 bytes 68361d94
+ 0050c090 bytes 8c361d94
- 0050c0c4 ["INT_ADD", "register:40f0:8", ["const:50c0c4:8", "const:4:8"]]
- 0050c0c4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0050c104 ["INT_ADD", "register:40f0:8", ["const:50c104:8", "const:4:8"]]
+ 0050c104 ["CALL", null, ["callee:00c57f80:8"]]
- 0050c0c4 bytes 7b2f1d94
+ 0050c104 bytes 9f2f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b799009c1bcacae79e4eaf059f302ae9"></a>

### [`0050cc0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050cc0c.md) → [`0050cc4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050cc4c.md) _ZNK5Botan16X509_Certificate13raw_issuer_dnEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050cc14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050cc0c.md#insn-0050cc14)
- 新版 `0050cc54`（命令位置の公開資料なし）

~~~diff
- 0050cc14 ["INT_ADD", "register:40f0:8", ["const:50cc14:8", "const:4:8"]]
- 0050cc14 ["CALL", null, ["callee:00c59ac0:8"]]
+ 0050cc54 ["INT_ADD", "register:40f0:8", ["const:50cc54:8", "const:4:8"]]
+ 0050cc54 ["CALL", null, ["callee:00c59ac0:8"]]
- 0050cc14 bytes 77331d94
+ 0050cc54 bytes 9b331d94
~~~


<a id="compare-e674778d8accfa81b54f89d2f50e92c6"></a>

### [`0050cc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050cc24.md) → [`0050cc64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050cc64.md) _ZNK5Botan4OCSP6CertID11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c586b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586b0.md) [`00c586d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586d0.md) [`00c58820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58820.md) [`00c58b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b10.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58780.md) [`00c587a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587a0.md) [`00c588f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588f0.md) [`00c58be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58be0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050cc44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050cc24.md#insn-0050cc44) · [`0050cc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050cc24.md#insn-0050cc58) · [`0050cc70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050cc24.md#insn-0050cc70)
- 新版 `0050cc84`（命令位置の公開資料なし） · `0050cc98`（命令位置の公開資料なし） · `0050ccb0`（命令位置の公開資料なし）

~~~diff
- 0050cc44 ["INT_ADD", "register:40f0:8", ["const:50cc44:8", "const:4:8"]]
- 0050cc44 ["CALL", null, ["callee:00c58780:8"]]
+ 0050cc84 ["INT_ADD", "register:40f0:8", ["const:50cc84:8", "const:4:8"]]
+ 0050cc84 ["CALL", null, ["callee:00c58780:8"]]
- 0050cc44 bytes 9b2e1d94
+ 0050cc84 bytes bf2e1d94
- 0050cc58 ["COPY", "register:0:8", ["register:4040:8"]]
- 0050cc58 ["INT_ADD", "register:40f0:8", ["const:50cc58:8", "const:4:8"]]
- 0050cc58 ["CALLIND", null, ["register:0:8"]]
+ 0050cc98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050cc98 ["INT_ADD", "register:40f0:8", ["const:50cc98:8", "const:4:8"]]
+ 0050cc98 ["CALLIND", null, ["register:0:8"]]
- 0050cc58 bytes 00013fd6
+ 0050cc98 bytes 00013fd6
- 0050cc70 ["INT_ADD", "register:40f0:8", ["const:50cc70:8", "const:4:8"]]
- 0050cc70 ["CALL", null, ["callee:00c588f0:8"]]
+ 0050ccb0 ["INT_ADD", "register:40f0:8", ["const:50ccb0:8", "const:4:8"]]
+ 0050ccb0 ["CALL", null, ["callee:00c588f0:8"]]
- 0050cc70 bytes ec2e1d94
+ 0050ccb0 bytes 102f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61c09b9996b34389a25f59d1a1e74502"></a>

### [`0050dd50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050dd50.md) → [`0050dd90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050dd90.md) FUN_0050dd90

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050dd6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050dd50.md#insn-0050dd6c) · [`0050dd8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050dd50.md#insn-0050dd8c)
- 新版 `0050ddac`（命令位置の公開資料なし） · `0050ddcc`（命令位置の公開資料なし）

~~~diff
- 0050dd6c ["INT_ADD", "register:40f0:8", ["const:50dd6c:8", "const:4:8"]]
- 0050dd6c ["CALL", null, ["callee:00c53da0:8"]]
+ 0050ddac ["INT_ADD", "register:40f0:8", ["const:50ddac:8", "const:4:8"]]
+ 0050ddac ["CALL", null, ["callee:00c53da0:8"]]
- 0050dd6c bytes e5171d94
+ 0050ddac bytes fd171d94
- 0050dd8c ["COPY", "register:0:8", ["register:4040:8"]]
- 0050dd8c ["INT_ADD", "register:40f0:8", ["const:50dd8c:8", "const:4:8"]]
- 0050dd8c ["CALLIND", null, ["register:0:8"]]
+ 0050ddcc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050ddcc ["INT_ADD", "register:40f0:8", ["const:50ddcc:8", "const:4:8"]]
+ 0050ddcc ["CALLIND", null, ["register:0:8"]]
- 0050dd8c bytes 00013fd6
+ 0050ddcc bytes 00013fd6
~~~


<a id="compare-24502023edface88cc1f5818582514f2"></a>

### [`0050f06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f06c.md) → [`0050f0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f0ac.md) FUN_0050f0ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0054a42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a42c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054a46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054a/0054a46c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f06c.md#insn-0050f088)
- 新版 `0050f0c8`（命令位置の公開資料なし）

~~~diff
- 0050f088 ["INT_ADD", "register:40f0:8", ["const:50f088:8", "const:4:8"]]
- 0050f088 ["CALL", null, ["callee:0054a46c:8"]]
+ 0050f0c8 ["INT_ADD", "register:40f0:8", ["const:50f0c8:8", "const:4:8"]]
+ 0050f0c8 ["CALL", null, ["callee:0054a46c:8"]]
- 0050f088 bytes e9ec0094
+ 0050f0c8 bytes e9ec0094
~~~


<a id="compare-afcbca348a4d6e574b58955adeee8d0a"></a>

### [`0050f1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f1a4.md) → [`0050f1e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f1e4.md) _ZNK5Botan14PKCS10_Request18challenge_passwordEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c59cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59cc0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c59d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f1b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f1a4.md#insn-0050f1b4)
- 新版 `0050f1f4`（命令位置の公開資料なし）

~~~diff
- 0050f1b4 ["INT_ADD", "register:40f0:8", ["const:50f1b4:8", "const:4:8"]]
- 0050f1b4 ["CALL", null, ["callee:00c59d90:8"]]
+ 0050f1f4 ["INT_ADD", "register:40f0:8", ["const:50f1f4:8", "const:4:8"]]
+ 0050f1f4 ["CALL", null, ["callee:00c59d90:8"]]
- 0050f1b4 bytes c32a1d94
+ 0050f1f4 bytes e72a1d94
~~~


<a id="compare-2276b0a442b1d91f95563b6a509c6e85"></a>

### [`0050f1f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f1f8.md) → [`0050f238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f238.md) _ZNK5Botan14PKCS10_Request14raw_public_keyEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59cc0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f1f8.md#insn-0050f200)
- 新版 `0050f240`（命令位置の公開資料なし）

~~~diff
- 0050f200 ["INT_ADD", "register:40f0:8", ["const:50f200:8", "const:4:8"]]
- 0050f200 ["CALL", null, ["callee:00c59d90:8"]]
+ 0050f240 ["INT_ADD", "register:40f0:8", ["const:50f240:8", "const:4:8"]]
+ 0050f240 ["CALL", null, ["callee:00c59d90:8"]]
- 0050f200 bytes b02a1d94
+ 0050f240 bytes d42a1d94
~~~


<a id="compare-8be414ce9046ece7f1ee9415b7e00efb"></a>

### [`0050f210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f210.md) → [`0050f250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f250.md) _ZNK5Botan14PKCS10_Request16subject_alt_nameEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59cc0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f210.md#insn-0050f218)
- 新版 `0050f258`（命令位置の公開資料なし）

~~~diff
- 0050f218 ["INT_ADD", "register:40f0:8", ["const:50f218:8", "const:4:8"]]
- 0050f218 ["CALL", null, ["callee:00c59d90:8"]]
+ 0050f258 ["INT_ADD", "register:40f0:8", ["const:50f258:8", "const:4:8"]]
+ 0050f258 ["CALL", null, ["callee:00c59d90:8"]]
- 0050f218 bytes aa2a1d94
+ 0050f258 bytes ce2a1d94
~~~


<a id="compare-f2696fb720ba4f77e39b356ad8b72258"></a>

### [`0050f228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f228.md) → [`0050f268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f268.md) _ZNK5Botan14PKCS10_Request10extensionsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59cc0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f228.md#insn-0050f230)
- 新版 `0050f270`（命令位置の公開資料なし）

~~~diff
- 0050f230 ["INT_ADD", "register:40f0:8", ["const:50f230:8", "const:4:8"]]
- 0050f230 ["CALL", null, ["callee:00c59d90:8"]]
+ 0050f270 ["INT_ADD", "register:40f0:8", ["const:50f270:8", "const:4:8"]]
+ 0050f270 ["CALL", null, ["callee:00c59d90:8"]]
- 0050f230 bytes a42a1d94
+ 0050f270 bytes c82a1d94
~~~


<a id="compare-44e5008c6c19d543606c983ebaf965af"></a>

### [`0050f3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f3b8.md) → [`0050f3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f3f8.md) _ZNK5Botan10Extensions3getERKNS_3OIDE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f3b8.md#insn-0050f3c8) · [`0050f3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f3b8.md#insn-0050f3d8)
- 新版 `0050f408`（命令位置の公開資料なし） · `0050f418`（命令位置の公開資料なし）

~~~diff
- 0050f3c8 ["INT_ADD", "register:40f0:8", ["const:50f3c8:8", "const:4:8"]]
- 0050f3c8 ["CALL", null, ["callee:00c59b90:8"]]
+ 0050f408 ["INT_ADD", "register:40f0:8", ["const:50f408:8", "const:4:8"]]
+ 0050f408 ["CALL", null, ["callee:00c59b90:8"]]
- 0050f3c8 bytes be291d94
+ 0050f408 bytes e2291d94
- 0050f3d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0050f3d8 ["INT_ADD", "register:40f0:8", ["const:50f3d8:8", "const:4:8"]]
- 0050f3d8 ["CALLIND", null, ["register:0:8"]]
+ 0050f418 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050f418 ["INT_ADD", "register:40f0:8", ["const:50f418:8", "const:4:8"]]
+ 0050f418 ["CALLIND", null, ["register:0:8"]]
- 0050f3d8 bytes 00013fd6
+ 0050f418 bytes 00013fd6
~~~


<a id="compare-ddf6dba749deed935bab02c32450e4bb"></a>

### [`0050ff10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050ff10.md) → [`0050ff50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050ff50.md) _ZNK5Botan16X509_Certificate10is_CA_certEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050ff18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050ff10.md#insn-0050ff18)
- 新版 `0050ff58`（命令位置の公開資料なし）

~~~diff
- 0050ff18 ["INT_ADD", "register:40f0:8", ["const:50ff18:8", "const:4:8"]]
- 0050ff18 ["CALL", null, ["callee:00c59ac0:8"]]
+ 0050ff58 ["INT_ADD", "register:40f0:8", ["const:50ff58:8", "const:4:8"]]
+ 0050ff58 ["CALL", null, ["callee:00c59ac0:8"]]
- 0050ff18 bytes b6261d94
+ 0050ff58 bytes da261d94
~~~


<a id="compare-21b39cfcbb617f0615824a6dffe07f73"></a>

### [`0050ff28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050ff28.md) → [`0050ff68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050ff68.md) FUN_0050ff68

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0050fa48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050fa48.md) · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`0050fa88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050fa88.md) · 呼出先 5件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050ff4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050ff28.md#insn-0050ff4c) · [`0050ff94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050ff28.md#insn-0050ff94) · [`0050ffb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050ff28.md#insn-0050ffb4)
- 新版 `0050ff8c`（命令位置の公開資料なし） · `0050ffd4`（命令位置の公開資料なし） · `0050fff4`（命令位置の公開資料なし）

~~~diff
- 0050ff4c ["INT_ADD", "register:40f0:8", ["const:50ff4c:8", "const:4:8"]]
- 0050ff4c ["CALL", null, ["callee:00c580b0:8"]]
+ 0050ff8c ["INT_ADD", "register:40f0:8", ["const:50ff8c:8", "const:4:8"]]
+ 0050ff8c ["CALL", null, ["callee:00c580b0:8"]]
- 0050ff4c bytes 25201d94
+ 0050ff8c bytes 49201d94
- 0050ff94 ["INT_ADD", "register:40f0:8", ["const:50ff94:8", "const:4:8"]]
- 0050ff94 ["CALL", null, ["callee:00c57f60:8"]]
+ 0050ffd4 ["INT_ADD", "register:40f0:8", ["const:50ffd4:8", "const:4:8"]]
+ 0050ffd4 ["CALL", null, ["callee:00c57f60:8"]]
- 0050ff94 bytes bf1f1d94
+ 0050ffd4 bytes e31f1d94
- 0050ffb4 ["INT_ADD", "register:40f0:8", ["const:50ffb4:8", "const:4:8"]]
- 0050ffb4 ["CALL", null, ["callee:00c58010:8"]]
+ 0050fff4 ["INT_ADD", "register:40f0:8", ["const:50fff4:8", "const:4:8"]]
+ 0050fff4 ["CALL", null, ["callee:00c58010:8"]]
- 0050ffb4 bytes e31f1d94
+ 0050fff4 bytes 07201d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c1e78c1c4b22d09486e09f08316621a"></a>

### [`0051001c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/0051001c.md) → [`0051005c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/0051005c.md) FUN_0051005c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`0061452c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00614/0061452c.md) [`0064ecb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064ecb8.md) [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) [`0073d7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073d/0073d7a4.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 9件 [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`0061456c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00614/0061456c.md) [`0064ecf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064ecf8.md) [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) [`0073d7fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073d/0073d7fc.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00510038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/0051001c.md#insn-00510038)
- 新版 `00510078`（命令位置の公開資料なし）

~~~diff
- 00510038 ["INT_ADD", "register:40f0:8", ["const:510038:8", "const:4:8"]]
- 00510038 ["CALL", null, ["callee:00c57f80:8"]]
+ 00510078 ["INT_ADD", "register:40f0:8", ["const:510078:8", "const:4:8"]]
+ 00510078 ["CALL", null, ["callee:00c57f80:8"]]
- 00510038 bytes 9e1f1d94
+ 00510078 bytes c21f1d94
~~~


<a id="compare-135887245be9a77ddf941fb7bdd8125b"></a>

### [`00511638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511638.md) → [`00511678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511678.md) FUN_00511678

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00510d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510d58.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00510d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510d98.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00511680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511638.md#insn-00511680)
- 新版 `005116c0`（命令位置の公開資料なし）

~~~diff
- 00511680 ["INT_ADD", "register:40f0:8", ["const:511680:8", "const:4:8"]]
- 00511680 ["CALL", null, ["callee:00c57f80:8"]]
+ 005116c0 ["INT_ADD", "register:40f0:8", ["const:5116c0:8", "const:4:8"]]
+ 005116c0 ["CALL", null, ["callee:00c57f80:8"]]
- 00511680 bytes 0c1a1d94
+ 005116c0 bytes 301a1d94
~~~


<a id="compare-1b439c0b5ca34eeb40de725bfad32aad"></a>

### [`00511cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511cc4.md) → [`00511d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511d04.md) _ZNK5Botan7X509_CA7new_crlERNS_21RandomNumberGeneratorEj

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58580.md) [`00c59d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59d70.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58650.md) [`00c59e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59e40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00511cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511cc4.md#insn-00511cf8) · [`00511d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511cc4.md#insn-00511d20) · [`00511d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511cc4.md#insn-00511d70)
- 新版 `00511d38`（命令位置の公開資料なし） · `00511d60`（命令位置の公開資料なし） · `00511db0`（命令位置の公開資料なし）

~~~diff
- 00511cf8 ["INT_ADD", "register:40f0:8", ["const:511cf8:8", "const:4:8"]]
- 00511cf8 ["CALL", null, ["callee:00c58650:8"]]
+ 00511d38 ["INT_ADD", "register:40f0:8", ["const:511d38:8", "const:4:8"]]
+ 00511d38 ["CALL", null, ["callee:00c58650:8"]]
- 00511cf8 bytes 221a1d94
+ 00511d38 bytes 461a1d94
- 00511d20 ["INT_ADD", "register:40f0:8", ["const:511d20:8", "const:4:8"]]
- 00511d20 ["CALL", null, ["callee:00c59e40:8"]]
+ 00511d60 ["INT_ADD", "register:40f0:8", ["const:511d60:8", "const:4:8"]]
+ 00511d60 ["CALL", null, ["callee:00c59e40:8"]]
- 00511d20 bytes 14201d94
+ 00511d60 bytes 38201d94
- 00511d70 ["INT_ADD", "register:40f0:8", ["const:511d70:8", "const:4:8"]]
- 00511d70 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00511db0 ["INT_ADD", "register:40f0:8", ["const:511db0:8", "const:4:8"]]
+ 00511db0 ["CALL", null, ["callee:00c57fb0:8"]]
- 00511d70 bytes 5c181d94
+ 00511db0 bytes 80181d94
~~~


<a id="compare-15950414f93c376a6284a4cc16bc7585"></a>

### [`00511d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511d74.md) → [`00511db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511db4.md) _ZNK5Botan7X509_CA7new_crlERNS_21RandomNumberGeneratorENSt6__ndk16chrono10time_pointINS4_12system_clockENS4_8durationIxNS3_5ratioILl1ELl1000

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59d70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59e40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00511dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511d74.md#insn-00511dac) · [`00511df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511d74.md#insn-00511df8)
- 新版 `00511dec`（命令位置の公開資料なし） · `00511e38`（命令位置の公開資料なし）

~~~diff
- 00511dac ["INT_ADD", "register:40f0:8", ["const:511dac:8", "const:4:8"]]
- 00511dac ["CALL", null, ["callee:00c59e40:8"]]
+ 00511dec ["INT_ADD", "register:40f0:8", ["const:511dec:8", "const:4:8"]]
+ 00511dec ["CALL", null, ["callee:00c59e40:8"]]
- 00511dac bytes f11f1d94
+ 00511dec bytes 15201d94
- 00511df8 ["INT_ADD", "register:40f0:8", ["const:511df8:8", "const:4:8"]]
- 00511df8 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00511e38 ["INT_ADD", "register:40f0:8", ["const:511e38:8", "const:4:8"]]
+ 00511e38 ["CALL", null, ["callee:00c57fb0:8"]]
- 00511df8 bytes 3a181d94
+ 00511e38 bytes 5e181d94
~~~


<a id="compare-478738bdbe92c68fbdd1fedfd0f41538"></a>

### [`00511dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511dfc.md) → [`00511e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511e3c.md) _ZNK5Botan7X509_CA10update_crlERKNS_8X509_CRLERKNSt6__ndk16vectorINS_9CRL_EntryENS4_9allocatorIS6_EEEERNS_21RandomNumberGeneratorEj

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58580.md) [`00c59d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59d80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58650.md) [`00c59e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59e50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00511e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511dfc.md#insn-00511e28)
- 新版 `00511e68`（命令位置の公開資料なし）

~~~diff
- 00511e28 ["INT_ADD", "register:40f0:8", ["const:511e28:8", "const:4:8"]]
- 00511e28 ["CALL", null, ["callee:00c58650:8"]]
+ 00511e68 ["INT_ADD", "register:40f0:8", ["const:511e68:8", "const:4:8"]]
+ 00511e68 ["CALL", null, ["callee:00c58650:8"]]
- 00511e28 bytes d6191d94
+ 00511e68 bytes fa191d94
~~~


<a id="compare-308217ca6308c50c2668ea5608528498"></a>

### [`00512690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512690.md) → [`005126d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/005126d0.md) FUN_005126d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005126dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512690.md#insn-005126dc) · [`005126f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512690.md#insn-005126f0) · [`005126f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512690.md#insn-005126f8)
- 新版 `0051271c`（命令位置の公開資料なし） · `00512730`（命令位置の公開資料なし） · `00512738`（命令位置の公開資料なし）

~~~diff
- 005126dc ["INT_ADD", "register:40f0:8", ["const:5126dc:8", "const:4:8"]]
- 005126dc ["CALL", null, ["callee:00c53da0:8"]]
+ 0051271c ["INT_ADD", "register:40f0:8", ["const:51271c:8", "const:4:8"]]
+ 0051271c ["CALL", null, ["callee:00c53da0:8"]]
- 005126dc bytes 89051d94
+ 0051271c bytes a1051d94
- 005126f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005126f0 ["INT_ADD", "register:40f0:8", ["const:5126f0:8", "const:4:8"]]
- 005126f0 ["CALLIND", null, ["register:0:8"]]
+ 00512730 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00512730 ["INT_ADD", "register:40f0:8", ["const:512730:8", "const:4:8"]]
+ 00512730 ["CALLIND", null, ["register:0:8"]]
- 005126f0 bytes 00013fd6
+ 00512730 bytes 00013fd6
- 005126f8 ["INT_ADD", "register:40f0:8", ["const:5126f8:8", "const:4:8"]]
- 005126f8 ["CALL", null, ["callee:00c57f50:8"]]
+ 00512738 ["INT_ADD", "register:40f0:8", ["const:512738:8", "const:4:8"]]
+ 00512738 ["CALL", null, ["callee:00c57f50:8"]]
- 005126f8 bytes e2151d94
+ 00512738 bytes 06161d94
~~~


<a id="compare-4a0d83cab2e35f647df09c9d39e4d9dd"></a>

### [`00512728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512728.md) → [`00512768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512768.md) _ZNK5Botan8X509_CRL11get_revokedEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00512730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512728.md#insn-00512730)
- 新版 `00512770`（命令位置の公開資料なし）

~~~diff
- 00512730 ["INT_ADD", "register:40f0:8", ["const:512730:8", "const:4:8"]]
- 00512730 ["CALL", null, ["callee:00c59b20:8"]]
+ 00512770 ["INT_ADD", "register:40f0:8", ["const:512770:8", "const:4:8"]]
+ 00512770 ["CALL", null, ["callee:00c59b20:8"]]
- 00512730 bytes c81c1d94
+ 00512770 bytes ec1c1d94
~~~


<a id="compare-3d0d47461afb680b6b2be96b3e5b8a94"></a>

### [`00512740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512740.md) → [`00512780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512780.md) _ZNK5Botan8X509_CRL10crl_numberEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00512748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512740.md#insn-00512748)
- 新版 `00512788`（命令位置の公開資料なし）

~~~diff
- 00512748 ["INT_ADD", "register:40f0:8", ["const:512748:8", "const:4:8"]]
- 00512748 ["CALL", null, ["callee:00c59b20:8"]]
+ 00512788 ["INT_ADD", "register:40f0:8", ["const:512788:8", "const:4:8"]]
+ 00512788 ["CALL", null, ["callee:00c59b20:8"]]
- 00512748 bytes c21c1d94
+ 00512788 bytes e61c1d94
~~~


<a id="compare-56a91ace8a5f8a7853931317af157cf0"></a>

### [`005127ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/005127ac.md) → [`005127ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/005127ec.md) _ZN5Botan17choose_sig_formatERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS5_11char_traitsIcEENS5_9allocatorI

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00510060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510060.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`005100a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/005100a0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005127e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/005127ac.md#insn-005127e8) · [`005127f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/005127ac.md#insn-005127f8) · [`00512848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/005127ac.md#insn-00512848)
- 新版 `00512828`（命令位置の公開資料なし） · `00512838`（命令位置の公開資料なし） · `00512888`（命令位置の公開資料なし）

~~~diff
- 005127e8 ["INT_ADD", "register:40f0:8", ["const:5127e8:8", "const:4:8"]]
- 005127e8 ["CALL", null, ["callee:005100a0:8"]]
+ 00512828 ["INT_ADD", "register:40f0:8", ["const:512828:8", "const:4:8"]]
+ 00512828 ["CALL", null, ["callee:005100a0:8"]]
- 005127e8 bytes 1ef6ff97
+ 00512828 bytes 1ef6ff97
- 005127f8 ["INT_ADD", "register:40f0:8", ["const:5127f8:8", "const:4:8"]]
- 005127f8 ["CALL", null, ["callee:0046d4d0:8"]]
+ 00512838 ["INT_ADD", "register:40f0:8", ["const:512838:8", "const:4:8"]]
+ 00512838 ["CALL", null, ["callee:0046d4d0:8"]]
- 005127f8 bytes 266bfd97
+ 00512838 bytes 266bfd97
- 00512848 ["INT_ADD", "register:40f0:8", ["const:512848:8", "const:4:8"]]
- 00512848 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00512888 ["INT_ADD", "register:40f0:8", ["const:512888:8", "const:4:8"]]
+ 00512888 ["CALL", null, ["callee:00c57fb0:8"]]
- 00512848 bytes a6151d94
+ 00512888 bytes ca151d94
~~~


<a id="compare-0ad181b574a7b529675587103d6e3c84"></a>

### [`00512a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512a14.md) → [`00512a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512a54.md) FUN_00512a54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00512a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512a14.md#insn-00512a30) · [`00512a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512a14.md#insn-00512a50)
- 新版 `00512a70`（命令位置の公開資料なし） · `00512a90`（命令位置の公開資料なし）

~~~diff
- 00512a30 ["INT_ADD", "register:40f0:8", ["const:512a30:8", "const:4:8"]]
- 00512a30 ["CALL", null, ["callee:00c53da0:8"]]
+ 00512a70 ["INT_ADD", "register:40f0:8", ["const:512a70:8", "const:4:8"]]
+ 00512a70 ["CALL", null, ["callee:00c53da0:8"]]
- 00512a30 bytes b4041d94
+ 00512a70 bytes cc041d94
- 00512a50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00512a50 ["INT_ADD", "register:40f0:8", ["const:512a50:8", "const:4:8"]]
- 00512a50 ["CALLIND", null, ["register:0:8"]]
+ 00512a90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00512a90 ["INT_ADD", "register:40f0:8", ["const:512a90:8", "const:4:8"]]
+ 00512a90 ["CALLIND", null, ["register:0:8"]]
- 00512a50 bytes 00013fd6
+ 00512a90 bytes 00013fd6
~~~


<a id="compare-411df8aac326d60309a3bb3ee90acb36"></a>

### [`00512f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512f88.md) → [`00512fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512fc8.md) _ZNK5Botan8X509_CRL10is_revokedERKNS_16X509_CertificateE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59da0.md) · 呼出先 10件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00c59e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59e70.md) · 呼出先 10件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00512fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512f88.md#insn-00512fc0) · [`00512fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512f88.md#insn-00512fcc) · [`00512fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512f88.md#insn-00512fd8)
- 新版 `00513000`（命令位置の公開資料なし） · `0051300c`（命令位置の公開資料なし） · `00513018`（命令位置の公開資料なし）

~~~diff
- 00512fc0 ["INT_ADD", "register:40f0:8", ["const:512fc0:8", "const:4:8"]]
- 00512fc0 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00513000 ["INT_ADD", "register:40f0:8", ["const:513000:8", "const:4:8"]]
+ 00513000 ["CALL", null, ["callee:00c59ac0:8"]]
- 00512fc0 bytes 8c1a1d94
+ 00513000 bytes b01a1d94
- 00512fcc ["INT_ADD", "register:40f0:8", ["const:512fcc:8", "const:4:8"]]
- 00512fcc ["CALL", null, ["callee:00c59b20:8"]]
+ 0051300c ["INT_ADD", "register:40f0:8", ["const:51300c:8", "const:4:8"]]
+ 0051300c ["CALL", null, ["callee:00c59b20:8"]]
- 00512fcc bytes a11a1d94
+ 0051300c bytes c51a1d94
- 00512fd8 ["INT_ADD", "register:40f0:8", ["const:512fd8:8", "const:4:8"]]
- 00512fd8 ["CALL", null, ["callee:00c59ae0:8"]]
+ 00513018 ["INT_ADD", "register:40f0:8", ["const:513018:8", "const:4:8"]]
+ 00513018 ["CALL", null, ["callee:00c59ae0:8"]]
- 00512fd8 bytes 8e1a1d94
+ 00513018 bytes b21a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a44c1123df4aa6b58a95734ed9e547f1"></a>

### [`00513e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/00513e14.md) → [`00513e54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/00513e54.md) FUN_00513e54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0054aa4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054aa4c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054aa8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054a/0054aa8c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00513e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/00513e14.md#insn-00513e30)
- 新版 `00513e70`（命令位置の公開資料なし）

~~~diff
- 00513e30 ["INT_ADD", "register:40f0:8", ["const:513e30:8", "const:4:8"]]
- 00513e30 ["CALL", null, ["callee:0054aa8c:8"]]
+ 00513e70 ["INT_ADD", "register:40f0:8", ["const:513e70:8", "const:4:8"]]
+ 00513e70 ["CALL", null, ["callee:0054aa8c:8"]]
- 00513e30 bytes 07db0094
+ 00513e70 bytes 07db0094
~~~


<a id="compare-bba473f7de1f52b3fc8498cc84525ad9"></a>

### [`00513f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/00513f4c.md) → [`00513f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/00513f8c.md) _ZNK5Botan8X509_CRL10extensionsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00513f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/00513f4c.md#insn-00513f54)
- 新版 `00513f94`（命令位置の公開資料なし）

~~~diff
- 00513f54 ["INT_ADD", "register:40f0:8", ["const:513f54:8", "const:4:8"]]
- 00513f54 ["CALL", null, ["callee:00c59b20:8"]]
+ 00513f94 ["INT_ADD", "register:40f0:8", ["const:513f94:8", "const:4:8"]]
+ 00513f94 ["CALL", null, ["callee:00c59b20:8"]]
- 00513f54 bytes bf161d94
+ 00513f94 bytes e3161d94
~~~


<a id="compare-7b1a7200b60daaf05cd0e19baeb955c6"></a>

### [`00513f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/00513f64.md) → [`00513fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/00513fa4.md) _ZNK5Botan8X509_CRL11next_updateEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00513f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/00513f64.md#insn-00513f6c)
- 新版 `00513fac`（命令位置の公開資料なし）

~~~diff
- 00513f6c ["INT_ADD", "register:40f0:8", ["const:513f6c:8", "const:4:8"]]
- 00513f6c ["CALL", null, ["callee:00c59b20:8"]]
+ 00513fac ["INT_ADD", "register:40f0:8", ["const:513fac:8", "const:4:8"]]
+ 00513fac ["CALL", null, ["callee:00c59b20:8"]]
- 00513f6c bytes b9161d94
+ 00513fac bytes dd161d94
~~~


<a id="compare-7d780bdfe9e0ce475206536f8c25e873"></a>

### [`00513f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/00513f7c.md) → [`00513fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/00513fbc.md) _ZNK5Botan8X509_CRL30crl_issuing_distribution_pointEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c59a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c59b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00513f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/00513f7c.md#insn-00513f8c)
- 新版 `00513fcc`（命令位置の公開資料なし）

~~~diff
- 00513f8c ["INT_ADD", "register:40f0:8", ["const:513f8c:8", "const:4:8"]]
- 00513f8c ["CALL", null, ["callee:00c59b20:8"]]
+ 00513fcc ["INT_ADD", "register:40f0:8", ["const:513fcc:8", "const:4:8"]]
+ 00513fcc ["CALL", null, ["callee:00c59b20:8"]]
- 00513f8c bytes b1161d94
+ 00513fcc bytes d5161d94
~~~


<a id="compare-c188ca44298aec4c260b16f0a658e00f"></a>

### [`005140b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/005140b8.md) → [`005140f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/005140f8.md) _ZN5Botan7X509_DN13add_attributeERKNS_3OIDERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b00.md) · 呼出先 6件 [`004ff37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff37c.md) [`0054aeac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054aeac.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00c59bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59bd0.md) · 呼出先 6件 [`004ff3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff3bc.md) [`0054aeec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054a/0054aeec.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00514108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/005140b8.md#insn-00514108) · [`0051419c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/005140b8.md#insn-0051419c) · [`005141dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/005140b8.md#insn-005141dc)
- 新版 `00514148`（命令位置の公開資料なし） · `005141dc`（命令位置の公開資料なし） · `0051421c`（命令位置の公開資料なし）

~~~diff
- 00514108 ["INT_ADD", "register:40f0:8", ["const:514108:8", "const:4:8"]]
- 00514108 ["CALL", null, ["callee:0054aeec:8"]]
+ 00514148 ["INT_ADD", "register:40f0:8", ["const:514148:8", "const:4:8"]]
+ 00514148 ["CALL", null, ["callee:0054aeec:8"]]
- 00514108 bytes 69db0094
+ 00514148 bytes 69db0094
- 0051419c ["INT_ADD", "register:40f0:8", ["const:51419c:8", "const:4:8"]]
- 0051419c ["CALL", null, ["callee:00c58120:8"]]
+ 005141dc ["INT_ADD", "register:40f0:8", ["const:5141dc:8", "const:4:8"]]
+ 005141dc ["CALL", null, ["callee:00c58120:8"]]
- 0051419c bytes ad0f1d94
+ 005141dc bytes d10f1d94
- 005141dc ["INT_ADD", "register:40f0:8", ["const:5141dc:8", "const:4:8"]]
- 005141dc ["CALL", null, ["callee:00c589c0:8"]]
+ 0051421c ["INT_ADD", "register:40f0:8", ["const:51421c:8", "const:4:8"]]
+ 0051421c ["CALL", null, ["callee:00c589c0:8"]]
- 005141dc bytes c5111d94
+ 0051421c bytes e9111d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e36cd15e27afeb9506d387b4a124d676"></a>

### [`005143cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/005143cc.md) → [`0051440c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/0051440c.md) _ZNK5Botan7X509_DN8contentsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c599b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599b0.md) · 呼出先 5件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58800.md) [`00c588b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c588b0.md)
- 新版 呼出元 1件 [`00c59a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59a80.md) · 呼出先 5件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c588d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588d0.md) [`00c58980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58980.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00514448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/005143cc.md#insn-00514448) · [`0051446c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/005143cc.md#insn-0051446c) · [`0051447c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/005143cc.md#insn-0051447c)
- 新版 `00514488`（命令位置の公開資料なし） · `005144ac`（命令位置の公開資料なし） · `005144bc`（命令位置の公開資料なし）

~~~diff
- 00514448 ["INT_ADD", "register:40f0:8", ["const:514448:8", "const:4:8"]]
- 00514448 ["CALL", null, ["callee:00c58980:8"]]
+ 00514488 ["INT_ADD", "register:40f0:8", ["const:514488:8", "const:4:8"]]
+ 00514488 ["CALL", null, ["callee:00c58980:8"]]
- 00514448 bytes 1a111d94
+ 00514488 bytes 3e111d94
- 0051446c ["INT_ADD", "register:40f0:8", ["const:51446c:8", "const:4:8"]]
- 0051446c ["CALL", null, ["callee:00c588d0:8"]]
+ 005144ac ["INT_ADD", "register:40f0:8", ["const:5144ac:8", "const:4:8"]]
+ 005144ac ["CALL", null, ["callee:00c588d0:8"]]
- 0051446c bytes e5101d94
+ 005144ac bytes 09111d94
- 0051447c ["INT_ADD", "register:40f0:8", ["const:51447c:8", "const:4:8"]]
- 0051447c ["CALL", null, ["callee:00c57f80:8"]]
+ 005144bc ["INT_ADD", "register:40f0:8", ["const:5144bc:8", "const:4:8"]]
+ 005144bc ["CALL", null, ["callee:00c57f80:8"]]
- 0051447c bytes 8d0e1d94
+ 005144bc bytes b10e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f69f538c0ea75da8de521d004acce2c"></a>

### [`00514528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514528.md) → [`00514568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514568.md) _ZNK5Botan7X509_DN9has_fieldERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dc0.md) · 呼出先 5件 [`0054b274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b274.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md) [`00c59b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b70.md)
- 新版 呼出元 1件 [`00c59e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59e90.md) · 呼出先 5件 [`0054b2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054b2b4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md) [`00c59c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00514554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514528.md#insn-00514554) · [`00514560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514528.md#insn-00514560) · [`00514570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514528.md#insn-00514570)
- 新版 `00514594`（命令位置の公開資料なし） · `005145a0`（命令位置の公開資料なし） · `005145b0`（命令位置の公開資料なし）

~~~diff
- 00514554 ["INT_ADD", "register:40f0:8", ["const:514554:8", "const:4:8"]]
- 00514554 ["CALL", null, ["callee:00c59c40:8"]]
+ 00514594 ["INT_ADD", "register:40f0:8", ["const:514594:8", "const:4:8"]]
+ 00514594 ["CALL", null, ["callee:00c59c40:8"]]
- 00514554 bytes 87151d94
+ 00514594 bytes ab151d94
- 00514560 ["INT_ADD", "register:40f0:8", ["const:514560:8", "const:4:8"]]
- 00514560 ["CALL", null, ["callee:00c58750:8"]]
+ 005145a0 ["INT_ADD", "register:40f0:8", ["const:5145a0:8", "const:4:8"]]
+ 005145a0 ["CALL", null, ["callee:00c58750:8"]]
- 00514560 bytes 48101d94
+ 005145a0 bytes 6c101d94
- 00514570 ["INT_ADD", "register:40f0:8", ["const:514570:8", "const:4:8"]]
- 00514570 ["CALL", null, ["callee:00c57f80:8"]]
+ 005145b0 ["INT_ADD", "register:40f0:8", ["const:5145b0:8", "const:4:8"]]
+ 005145b0 ["CALL", null, ["callee:00c57f80:8"]]
- 00514570 bytes 500e1d94
+ 005145b0 bytes 740e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3adbbd7738cf003e41e4903cb59dc995"></a>

### [`00514944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514944.md) → [`00514984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514984.md) _ZNK5Botan7X509_DN19get_first_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md) [`00c59b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b70.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md) [`00c59c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00514974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514944.md#insn-00514974) · [`00514980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514944.md#insn-00514980) · [`00514990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514944.md#insn-00514990)
- 新版 `005149b4`（命令位置の公開資料なし） · `005149c0`（命令位置の公開資料なし） · `005149d0`（命令位置の公開資料なし）

~~~diff
- 00514974 ["INT_ADD", "register:40f0:8", ["const:514974:8", "const:4:8"]]
- 00514974 ["CALL", null, ["callee:00c59c40:8"]]
+ 005149b4 ["INT_ADD", "register:40f0:8", ["const:5149b4:8", "const:4:8"]]
+ 005149b4 ["CALL", null, ["callee:00c59c40:8"]]
- 00514974 bytes 7f141d94
+ 005149b4 bytes a3141d94
- 00514980 ["INT_ADD", "register:40f0:8", ["const:514980:8", "const:4:8"]]
- 00514980 ["CALL", null, ["callee:00c58750:8"]]
+ 005149c0 ["INT_ADD", "register:40f0:8", ["const:5149c0:8", "const:4:8"]]
+ 005149c0 ["CALL", null, ["callee:00c58750:8"]]
- 00514980 bytes 400f1d94
+ 005149c0 bytes 640f1d94
- 00514990 ["INT_ADD", "register:40f0:8", ["const:514990:8", "const:4:8"]]
- 00514990 ["CALL", null, ["callee:00c57f80:8"]]
+ 005149d0 ["INT_ADD", "register:40f0:8", ["const:5149d0:8", "const:4:8"]]
+ 005149d0 ["CALL", null, ["callee:00c57f80:8"]]
- 00514990 bytes 480d1d94
+ 005149d0 bytes 6c0d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b21874e7ad714cba4d45b37fa1418b0"></a>

### [`00514b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514b08.md) → [`00514b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514b48.md) _ZN5BotanltERKNS_7X509_DNES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00549668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549668.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c59a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a20.md)
- 新版 呼出元 0件  · 呼出先 4件 [`005496a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/005496a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c59af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59af0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00514b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514b08.md#insn-00514b3c) · [`00514b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514b08.md#insn-00514b48) · [`00514ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514b08.md#insn-00514ca4)
- 新版 `00514b7c`（命令位置の公開資料なし） · `00514b88`（命令位置の公開資料なし） · `00514ce4`（命令位置の公開資料なし）

~~~diff
- 00514b3c ["INT_ADD", "register:40f0:8", ["const:514b3c:8", "const:4:8"]]
- 00514b3c ["CALL", null, ["callee:00c59af0:8"]]
+ 00514b7c ["INT_ADD", "register:40f0:8", ["const:514b7c:8", "const:4:8"]]
+ 00514b7c ["CALL", null, ["callee:00c59af0:8"]]
- 00514b3c bytes b9131d94
+ 00514b7c bytes dd131d94
- 00514b48 ["INT_ADD", "register:40f0:8", ["const:514b48:8", "const:4:8"]]
- 00514b48 ["CALL", null, ["callee:00c59af0:8"]]
+ 00514b88 ["INT_ADD", "register:40f0:8", ["const:514b88:8", "const:4:8"]]
+ 00514b88 ["CALL", null, ["callee:00c59af0:8"]]
- 00514b48 bytes b6131d94
+ 00514b88 bytes da131d94
- 00514ca4 ["INT_ADD", "register:40f0:8", ["const:514ca4:8", "const:4:8"]]
- 00514ca4 ["CALL", null, ["callee:00c58120:8"]]
+ 00514ce4 ["INT_ADD", "register:40f0:8", ["const:514ce4:8", "const:4:8"]]
+ 00514ce4 ["CALL", null, ["callee:00c58120:8"]]
- 00514ca4 bytes eb0c1d94
+ 00514ce4 bytes 0f0d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20f3e31f233cfbd05d9fdbbcc260ef19"></a>

### [`00515100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/00515100.md) → [`00515140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515140.md) FUN_00515140

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00514da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514da4.md) · 呼出先 7件 [`0053d3ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d3ac.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md) [`00c586b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586b0.md)
- 新版 呼出元 1件 [`00514de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514de4.md) · 呼出先 7件 [`0053d3ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053d3ec.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md) [`00c58780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58780.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00515138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/00515100.md#insn-00515138) · [`00515218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/00515100.md#insn-00515218) · [`00515238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/00515100.md#insn-00515238)
- 新版 `00515178`（命令位置の公開資料なし） · `00515258`（命令位置の公開資料なし） · `00515278`（命令位置の公開資料なし）

~~~diff
- 00515138 ["INT_ADD", "register:40f0:8", ["const:515138:8", "const:4:8"]]
- 00515138 ["CALL", null, ["callee:00c58750:8"]]
+ 00515178 ["INT_ADD", "register:40f0:8", ["const:515178:8", "const:4:8"]]
+ 00515178 ["CALL", null, ["callee:00c58750:8"]]
- 00515138 bytes 520d1d94
+ 00515178 bytes 760d1d94
- 00515218 ["INT_ADD", "register:40f0:8", ["const:515218:8", "const:4:8"]]
- 00515218 ["CALL", null, ["callee:0053d3ec:8"]]
+ 00515258 ["INT_ADD", "register:40f0:8", ["const:515258:8", "const:4:8"]]
+ 00515258 ["CALL", null, ["callee:0053d3ec:8"]]
- 00515218 bytes 65a00094
+ 00515258 bytes 65a00094
- 00515238 ["INT_ADD", "register:40f0:8", ["const:515238:8", "const:4:8"]]
- 00515238 ["CALL", null, ["callee:00c57f80:8"]]
+ 00515278 ["INT_ADD", "register:40f0:8", ["const:515278:8", "const:4:8"]]
+ 00515278 ["CALL", null, ["callee:00c57f80:8"]]
- 00515238 bytes 1e0b1d94
+ 00515278 bytes 420b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39d7c957ec4d232270ac07013242e6e9"></a>

### [`00515370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/00515370.md) → [`005153b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/005153b0.md) FUN_005153b0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00508728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508728.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)
- 新版 呼出元 1件 [`00508768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508768.md) · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005153a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/00515370.md#insn-005153a4) · [`005153e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/00515370.md#insn-005153e4) · [`0051540c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/00515370.md#insn-0051540c)
- 新版 `005153e4`（命令位置の公開資料なし） · `00515424`（命令位置の公開資料なし） · `0051544c`（命令位置の公開資料なし）

~~~diff
- 005153a4 ["INT_ADD", "register:40f0:8", ["const:5153a4:8", "const:4:8"]]
- 005153a4 ["CALL", null, ["callee:00c59ea0:8"]]
+ 005153e4 ["INT_ADD", "register:40f0:8", ["const:5153e4:8", "const:4:8"]]
+ 005153e4 ["CALL", null, ["callee:00c59ea0:8"]]
- 005153a4 bytes 8b121d94
+ 005153e4 bytes af121d94
- 005153e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005153e4 ["INT_ADD", "register:40f0:8", ["const:5153e4:8", "const:4:8"]]
- 005153e4 ["CALLIND", null, ["register:0:8"]]
+ 00515424 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00515424 ["INT_ADD", "register:40f0:8", ["const:515424:8", "const:4:8"]]
+ 00515424 ["CALLIND", null, ["register:0:8"]]
- 005153e4 bytes 00013fd6
+ 00515424 bytes 00013fd6
- 0051540c ["INT_ADD", "register:40f0:8", ["const:51540c:8", "const:4:8"]]
- 0051540c ["CALL", null, ["callee:00c58370:8"]]
+ 0051544c ["INT_ADD", "register:40f0:8", ["const:51544c:8", "const:4:8"]]
+ 0051544c ["CALL", null, ["callee:00c58370:8"]]
- 0051540c bytes a50b1d94
+ 0051544c bytes c90b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c7bf2f453d85fc31b25fe37900d5e9f"></a>

### [`005154b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005154b4.md) → [`005154f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/005154f4.md) FUN_005154f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0054f430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054f/0054f430.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0054b434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b434.md) [`0054b7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b7d0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0054f470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054f/0054f470.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0054b474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054b474.md) [`0054b810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054b810.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00515504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005154b4.md#insn-00515504) · [`00515534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005154b4.md#insn-00515534) · [`00515550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005154b4.md#insn-00515550)
- 新版 `00515544`（命令位置の公開資料なし） · `00515574`（命令位置の公開資料なし） · `00515590`（命令位置の公開資料なし）

~~~diff
- 00515504 ["INT_ADD", "register:40f0:8", ["const:515504:8", "const:4:8"]]
- 00515504 ["CALL", null, ["callee:0043bbe4:8"]]
+ 00515544 ["INT_ADD", "register:40f0:8", ["const:515544:8", "const:4:8"]]
+ 00515544 ["CALL", null, ["callee:0043bbe4:8"]]
- 00515504 bytes a899fc97
+ 00515544 bytes a899fc97
- 00515534 ["INT_ADD", "register:40f0:8", ["const:515534:8", "const:4:8"]]
- 00515534 ["CALL", null, ["callee:0054b474:8"]]
+ 00515574 ["INT_ADD", "register:40f0:8", ["const:515574:8", "const:4:8"]]
+ 00515574 ["CALL", null, ["callee:0054b474:8"]]
- 00515534 bytes c0d70094
+ 00515574 bytes c0d70094
- 00515550 ["INT_ADD", "register:40f0:8", ["const:515550:8", "const:4:8"]]
- 00515550 ["CALL", null, ["callee:0054b810:8"]]
+ 00515590 ["INT_ADD", "register:40f0:8", ["const:515590:8", "const:4:8"]]
+ 00515590 ["CALL", null, ["callee:0054b810:8"]]
- 00515550 bytes a0d80094
+ 00515590 bytes a0d80094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-678f1a855df37b4fecd3f0d8ff50649c"></a>

### [`00516bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516bc4.md) → [`00516c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516c04.md) FUN_00516c04

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005030c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/005030c4.md) [`005113cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/005113cc.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`00503104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503104.md) [`0051140c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/0051140c.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00516be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516bc4.md#insn-00516be0) · [`00516bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516bc4.md#insn-00516bf4) · [`00516c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516bc4.md#insn-00516c14)
- 新版 `00516c20`（命令位置の公開資料なし） · `00516c34`（命令位置の公開資料なし） · `00516c54`（命令位置の公開資料なし）

~~~diff
- 00516be0 ["INT_ADD", "register:40f0:8", ["const:516be0:8", "const:4:8"]]
- 00516be0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00516c20 ["INT_ADD", "register:40f0:8", ["const:516c20:8", "const:4:8"]]
+ 00516c20 ["CALL", null, ["callee:00c57f80:8"]]
- 00516be0 bytes b4041d94
+ 00516c20 bytes d8041d94
- 00516bf4 ["INT_ADD", "register:40f0:8", ["const:516bf4:8", "const:4:8"]]
- 00516bf4 ["CALL", null, ["callee:00c53da0:8"]]
+ 00516c34 ["INT_ADD", "register:40f0:8", ["const:516c34:8", "const:4:8"]]
+ 00516c34 ["CALL", null, ["callee:00c53da0:8"]]
- 00516bf4 bytes 43f41c94
+ 00516c34 bytes 5bf41c94
- 00516c14 ["COPY", "register:0:8", ["register:4040:8"]]
- 00516c14 ["INT_ADD", "register:40f0:8", ["const:516c14:8", "const:4:8"]]
- 00516c14 ["CALLIND", null, ["register:0:8"]]
+ 00516c54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00516c54 ["INT_ADD", "register:40f0:8", ["const:516c54:8", "const:4:8"]]
+ 00516c54 ["CALLIND", null, ["register:0:8"]]
- 00516c14 bytes 00013fd6
+ 00516c54 bytes 00013fd6
~~~


<a id="compare-35502585de67638d19cf9a928147f21f"></a>

### [`00517094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517094.md) → [`005170d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005170d4.md) FUN_005170d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005170e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517094.md#insn-005170e0)
- 新版 `00517120`（命令位置の公開資料なし）

~~~diff
- 005170e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005170e0 ["INT_ADD", "register:40f0:8", ["const:5170e0:8", "const:4:8"]]
- 005170e0 ["CALLIND", null, ["register:0:8"]]
+ 00517120 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00517120 ["INT_ADD", "register:40f0:8", ["const:517120:8", "const:4:8"]]
+ 00517120 ["CALLIND", null, ["register:0:8"]]
- 005170e0 bytes 00013fd6
+ 00517120 bytes 00013fd6
~~~


<a id="compare-84eb958d4b38e10c4a56fc6ce55f0449"></a>

### [`00517110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517110.md) → [`00517150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517150.md) _ZNK5Botan10Extensions14extensions_rawEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0054c298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c298.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`0054c2d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054c/0054c2d8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005171b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517110.md#insn-005171b4) · [`005171cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517110.md#insn-005171cc) · [`005171e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517110.md#insn-005171e8)
- 新版 `005171f4`（命令位置の公開資料なし） · `0051720c`（命令位置の公開資料なし） · `00517228`（命令位置の公開資料なし）

~~~diff
- 005171b4 ["INT_ADD", "register:40f0:8", ["const:5171b4:8", "const:4:8"]]
- 005171b4 ["CALL", null, ["callee:00c57f60:8"]]
+ 005171f4 ["INT_ADD", "register:40f0:8", ["const:5171f4:8", "const:4:8"]]
+ 005171f4 ["CALL", null, ["callee:00c57f60:8"]]
- 005171b4 bytes 37031d94
+ 005171f4 bytes 5b031d94
- 005171cc ["INT_ADD", "register:40f0:8", ["const:5171cc:8", "const:4:8"]]
- 005171cc ["CALL", null, ["callee:00c580d0:8"]]
+ 0051720c ["INT_ADD", "register:40f0:8", ["const:51720c:8", "const:4:8"]]
+ 0051720c ["CALL", null, ["callee:00c580d0:8"]]
- 005171cc bytes 8d031d94
+ 0051720c bytes b1031d94
- 005171e8 ["INT_ADD", "register:40f0:8", ["const:5171e8:8", "const:4:8"]]
- 005171e8 ["CALL", null, ["callee:0054c2d8:8"]]
+ 00517228 ["INT_ADD", "register:40f0:8", ["const:517228:8", "const:4:8"]]
+ 00517228 ["CALL", null, ["callee:0054c2d8:8"]]
- 005171e8 bytes 2cd40094
+ 00517228 bytes 2cd40094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93715c22730a9c98f100f44ca6f76a03"></a>

### [`005175d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/005175d4.md) → [`00517614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517614.md) FUN_00517614

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005175f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/005175d4.md#insn-005175f0) · [`00517604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/005175d4.md#insn-00517604) · [`00517630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/005175d4.md#insn-00517630)
- 新版 `00517630`（命令位置の公開資料なし） · `00517644`（命令位置の公開資料なし） · `00517670`（命令位置の公開資料なし）

~~~diff
- 005175f0 ["INT_ADD", "register:40f0:8", ["const:5175f0:8", "const:4:8"]]
- 005175f0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00517630 ["INT_ADD", "register:40f0:8", ["const:517630:8", "const:4:8"]]
+ 00517630 ["CALL", null, ["callee:00c57f80:8"]]
- 005175f0 bytes 30021d94
+ 00517630 bytes 54021d94
- 00517604 ["INT_ADD", "register:40f0:8", ["const:517604:8", "const:4:8"]]
- 00517604 ["CALL", null, ["callee:00c53da0:8"]]
+ 00517644 ["INT_ADD", "register:40f0:8", ["const:517644:8", "const:4:8"]]
+ 00517644 ["CALL", null, ["callee:00c53da0:8"]]
- 00517604 bytes bff11c94
+ 00517644 bytes d7f11c94
- 00517630 ["COPY", "register:0:8", ["register:4040:8"]]
- 00517630 ["INT_ADD", "register:40f0:8", ["const:517630:8", "const:4:8"]]
- 00517630 ["CALLIND", null, ["register:0:8"]]
+ 00517670 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00517670 ["INT_ADD", "register:40f0:8", ["const:517670:8", "const:4:8"]]
+ 00517670 ["CALLIND", null, ["register:0:8"]]
- 00517630 bytes 00013fd6
+ 00517670 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c177938664a3e1d3b71396789a0bd845"></a>

### [`005199fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/005199fc.md) → [`00519a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519a3c.md) _ZNK5Botan14Cert_Extension24Subject_Alternative_Name11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053bb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bb70.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59970.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053bbb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053bbb0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59a40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00519a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/005199fc.md#insn-00519a2c) · [`00519a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/005199fc.md#insn-00519a48) · [`00519a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/005199fc.md#insn-00519a84)
- 新版 `00519a6c`（命令位置の公開資料なし） · `00519a88`（命令位置の公開資料なし） · `00519ac4`（命令位置の公開資料なし）

~~~diff
- 00519a2c ["INT_ADD", "register:40f0:8", ["const:519a2c:8", "const:4:8"]]
- 00519a2c ["CALL", null, ["callee:00c59a40:8"]]
+ 00519a6c ["INT_ADD", "register:40f0:8", ["const:519a6c:8", "const:4:8"]]
+ 00519a6c ["CALL", null, ["callee:00c59a40:8"]]
- 00519a2c bytes d1ff1c94
+ 00519a6c bytes f5ff1c94
- 00519a48 ["INT_ADD", "register:40f0:8", ["const:519a48:8", "const:4:8"]]
- 00519a48 ["CALL", null, ["callee:0046d4d0:8"]]
+ 00519a88 ["INT_ADD", "register:40f0:8", ["const:519a88:8", "const:4:8"]]
+ 00519a88 ["CALL", null, ["callee:0046d4d0:8"]]
- 00519a48 bytes 924efd97
+ 00519a88 bytes 924efd97
- 00519a84 ["INT_ADD", "register:40f0:8", ["const:519a84:8", "const:4:8"]]
- 00519a84 ["CALL", null, ["callee:0053bbb0:8"]]
+ 00519ac4 ["INT_ADD", "register:40f0:8", ["const:519ac4:8", "const:4:8"]]
+ 00519ac4 ["CALL", null, ["callee:0053bbb0:8"]]
- 00519a84 bytes 3b880094
+ 00519ac4 bytes 3b880094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99ad54b1fb03b063b91b1c7f924f785a"></a>

### [`00519ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/00519ae4.md) → [`00519b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519b24.md) _ZNK5Botan14Cert_Extension23Issuer_Alternative_Name11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053bb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bb70.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59970.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053bbb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053bbb0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59a40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00519b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/00519ae4.md#insn-00519b14) · [`00519b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/00519ae4.md#insn-00519b30) · [`00519b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/00519ae4.md#insn-00519b6c)
- 新版 `00519b54`（命令位置の公開資料なし） · `00519b70`（命令位置の公開資料なし） · `00519bac`（命令位置の公開資料なし）

~~~diff
- 00519b14 ["INT_ADD", "register:40f0:8", ["const:519b14:8", "const:4:8"]]
- 00519b14 ["CALL", null, ["callee:00c59a40:8"]]
+ 00519b54 ["INT_ADD", "register:40f0:8", ["const:519b54:8", "const:4:8"]]
+ 00519b54 ["CALL", null, ["callee:00c59a40:8"]]
- 00519b14 bytes 97ff1c94
+ 00519b54 bytes bbff1c94
- 00519b30 ["INT_ADD", "register:40f0:8", ["const:519b30:8", "const:4:8"]]
- 00519b30 ["CALL", null, ["callee:0046d4d0:8"]]
+ 00519b70 ["INT_ADD", "register:40f0:8", ["const:519b70:8", "const:4:8"]]
+ 00519b70 ["CALL", null, ["callee:0046d4d0:8"]]
- 00519b30 bytes 584efd97
+ 00519b70 bytes 584efd97
- 00519b6c ["INT_ADD", "register:40f0:8", ["const:519b6c:8", "const:4:8"]]
- 00519b6c ["CALL", null, ["callee:0053bbb0:8"]]
+ 00519bac ["INT_ADD", "register:40f0:8", ["const:519bac:8", "const:4:8"]]
+ 00519bac ["CALL", null, ["callee:0053bbb0:8"]]
- 00519b6c bytes 01880094
+ 00519bac bytes 01880094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70481e02d9c8947eccff47cfe5c04e89"></a>

### [`0051a9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a9d4.md) → [`0051aa14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051aa14.md) FUN_0051aa14

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0051a280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a280.md) · 呼出先 7件 [`0051ada4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051ada4.md) [`0053d760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d760.md) [`0053d7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d7f8.md) [`0053d80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d80c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)
- 新版 呼出元 1件 [`0051a2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a2c0.md) · 呼出先 7件 [`0051ade4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ade4.md) [`0053d7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053d7a0.md) [`0053d838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053d838.md) [`0053d84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053d84c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051aa4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a9d4.md#insn-0051aa4c) · [`0051aa70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a9d4.md#insn-0051aa70) · [`0051aabc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a9d4.md#insn-0051aabc)
- 新版 `0051aa8c`（命令位置の公開資料なし） · `0051aab0`（命令位置の公開資料なし） · `0051aafc`（命令位置の公開資料なし）

~~~diff
- 0051aa4c ["INT_ADD", "register:40f0:8", ["const:51aa4c:8", "const:4:8"]]
- 0051aa4c ["CALL", null, ["callee:00c57f60:8"]]
+ 0051aa8c ["INT_ADD", "register:40f0:8", ["const:51aa8c:8", "const:4:8"]]
+ 0051aa8c ["CALL", null, ["callee:00c57f60:8"]]
- 0051aa4c bytes 11f51c94
+ 0051aa8c bytes 35f51c94
- 0051aa70 ["INT_ADD", "register:40f0:8", ["const:51aa70:8", "const:4:8"]]
- 0051aa70 ["CALL", null, ["callee:0053d84c:8"]]
+ 0051aab0 ["INT_ADD", "register:40f0:8", ["const:51aab0:8", "const:4:8"]]
+ 0051aab0 ["CALL", null, ["callee:0053d84c:8"]]
- 0051aa70 bytes 678b0094
+ 0051aab0 bytes 678b0094
- 0051aabc ["INT_ADD", "register:40f0:8", ["const:51aabc:8", "const:4:8"]]
- 0051aabc ["CALL", null, ["callee:00c57f60:8"]]
+ 0051aafc ["INT_ADD", "register:40f0:8", ["const:51aafc:8", "const:4:8"]]
+ 0051aafc ["CALL", null, ["callee:00c57f60:8"]]
- 0051aabc bytes f5f41c94
+ 0051aafc bytes 19f51c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1d0b8578220e66ac12e4118b5a6f87f"></a>

### [`0051ab9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051ab9c.md) → [`0051abdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051abdc.md) FUN_0051abdc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0051a280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a280.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0051a2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a2c0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051abec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051ab9c.md#insn-0051abec) · [`0051abfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051ab9c.md#insn-0051abfc) · [`0051ac0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051ab9c.md#insn-0051ac0c)
- 新版 `0051ac2c`（命令位置の公開資料なし） · `0051ac3c`（命令位置の公開資料なし） · `0051ac4c`（命令位置の公開資料なし）

~~~diff
- 0051abec ["INT_ADD", "register:40f0:8", ["const:51abec:8", "const:4:8"]]
- 0051abec ["CALL", null, ["callee:00c57f80:8"]]
+ 0051ac2c ["INT_ADD", "register:40f0:8", ["const:51ac2c:8", "const:4:8"]]
+ 0051ac2c ["CALL", null, ["callee:00c57f80:8"]]
- 0051abec bytes b1f41c94
+ 0051ac2c bytes d5f41c94
- 0051abfc ["INT_ADD", "register:40f0:8", ["const:51abfc:8", "const:4:8"]]
- 0051abfc ["CALL", null, ["callee:00c57f80:8"]]
+ 0051ac3c ["INT_ADD", "register:40f0:8", ["const:51ac3c:8", "const:4:8"]]
+ 0051ac3c ["CALL", null, ["callee:00c57f80:8"]]
- 0051abfc bytes adf41c94
+ 0051ac3c bytes d1f41c94
- 0051ac0c ["INT_ADD", "register:40f0:8", ["const:51ac0c:8", "const:4:8"]]
- 0051ac0c ["CALL", null, ["callee:00c57f80:8"]]
+ 0051ac4c ["INT_ADD", "register:40f0:8", ["const:51ac4c:8", "const:4:8"]]
+ 0051ac4c ["CALL", null, ["callee:00c57f80:8"]]
- 0051ac0c bytes a9f41c94
+ 0051ac4c bytes cdf41c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5b8f75d3a228eb9ff519fea70a15140"></a>

### [`0051acc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051acc4.md) → [`0051ad04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ad04.md) FUN_0051ad04

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0051a280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a280.md) [`00531d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531d2c.md) [`00531d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531d34.md) [`0054d4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d4a4.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0051a2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a2c0.md) [`00531d6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531d6c.md) [`00531d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531d74.md) [`0054d4e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054d/0054d4e4.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051ad0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051acc4.md#insn-0051ad0c) · [`0051ad1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051acc4.md#insn-0051ad1c) · [`0051ad2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051acc4.md#insn-0051ad2c)
- 新版 `0051ad4c`（命令位置の公開資料なし） · `0051ad5c`（命令位置の公開資料なし） · `0051ad6c`（命令位置の公開資料なし）

~~~diff
- 0051ad0c ["INT_ADD", "register:40f0:8", ["const:51ad0c:8", "const:4:8"]]
- 0051ad0c ["CALL", null, ["callee:00c57f80:8"]]
+ 0051ad4c ["INT_ADD", "register:40f0:8", ["const:51ad4c:8", "const:4:8"]]
+ 0051ad4c ["CALL", null, ["callee:00c57f80:8"]]
- 0051ad0c bytes 69f41c94
+ 0051ad4c bytes 8df41c94
- 0051ad1c ["INT_ADD", "register:40f0:8", ["const:51ad1c:8", "const:4:8"]]
- 0051ad1c ["CALL", null, ["callee:00c57f80:8"]]
+ 0051ad5c ["INT_ADD", "register:40f0:8", ["const:51ad5c:8", "const:4:8"]]
+ 0051ad5c ["CALL", null, ["callee:00c57f80:8"]]
- 0051ad1c bytes 65f41c94
+ 0051ad5c bytes 89f41c94
- 0051ad2c ["INT_ADD", "register:40f0:8", ["const:51ad2c:8", "const:4:8"]]
- 0051ad2c ["CALL", null, ["callee:00c57f80:8"]]
+ 0051ad6c ["INT_ADD", "register:40f0:8", ["const:51ad6c:8", "const:4:8"]]
+ 0051ad6c ["CALL", null, ["callee:00c57f80:8"]]
- 0051ad2c bytes 61f41c94
+ 0051ad6c bytes 85f41c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-307b8bb9cb2e49b9ca02479af2c608fa"></a>

### [`0051ada4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051ada4.md) → [`0051ade4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ade4.md) FUN_0051ade4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0051a9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a9d4.md) [`0053f910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f910.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0051aa14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051aa14.md) [`0053f950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f950.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051adec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051ada4.md#insn-0051adec) · [`0051adfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051ada4.md#insn-0051adfc)
- 新版 `0051ae2c`（命令位置の公開資料なし） · `0051ae3c`（命令位置の公開資料なし）

~~~diff
- 0051adec ["INT_ADD", "register:40f0:8", ["const:51adec:8", "const:4:8"]]
- 0051adec ["CALL", null, ["callee:00c57f80:8"]]
+ 0051ae2c ["INT_ADD", "register:40f0:8", ["const:51ae2c:8", "const:4:8"]]
+ 0051ae2c ["CALL", null, ["callee:00c57f80:8"]]
- 0051adec bytes 31f41c94
+ 0051ae2c bytes 55f41c94
- 0051adfc ["INT_ADD", "register:40f0:8", ["const:51adfc:8", "const:4:8"]]
- 0051adfc ["CALL", null, ["callee:00c57f80:8"]]
+ 0051ae3c ["INT_ADD", "register:40f0:8", ["const:51ae3c:8", "const:4:8"]]
+ 0051ae3c ["CALL", null, ["callee:00c57f80:8"]]
- 0051adfc bytes 2df41c94
+ 0051ae3c bytes 51f41c94
~~~


<a id="compare-479313957f5e73c472ae3339052c5d69"></a>

### [`0051b868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051b868.md) → [`0051b8a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051b8a8.md) _ZNK5Botan16X509_Certificate11is_criticalERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59e50.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 1件 [`00c59f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59f20.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md) [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051b88c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051b868.md#insn-0051b88c) · [`0051b89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051b868.md#insn-0051b89c) · [`0051b99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051b868.md#insn-0051b99c)
- 新版 `0051b8cc`（命令位置の公開資料なし） · `0051b8dc`（命令位置の公開資料なし） · `0051b9dc`（命令位置の公開資料なし）

~~~diff
- 0051b88c ["INT_ADD", "register:40f0:8", ["const:51b88c:8", "const:4:8"]]
- 0051b88c ["CALL", null, ["callee:00c59ac0:8"]]
+ 0051b8cc ["INT_ADD", "register:40f0:8", ["const:51b8cc:8", "const:4:8"]]
+ 0051b8cc ["CALL", null, ["callee:00c59ac0:8"]]
- 0051b88c bytes 59f81c94
+ 0051b8cc bytes 7df81c94
- 0051b89c ["INT_ADD", "register:40f0:8", ["const:51b89c:8", "const:4:8"]]
- 0051b89c ["CALL", null, ["callee:00c58750:8"]]
+ 0051b8dc ["INT_ADD", "register:40f0:8", ["const:51b8dc:8", "const:4:8"]]
+ 0051b8dc ["CALL", null, ["callee:00c58750:8"]]
- 0051b89c bytes 79f31c94
+ 0051b8dc bytes 9df31c94
- 0051b99c ["INT_ADD", "register:40f0:8", ["const:51b99c:8", "const:4:8"]]
- 0051b99c ["CALL", null, ["callee:00c57f80:8"]]
+ 0051b9dc ["INT_ADD", "register:40f0:8", ["const:51b9dc:8", "const:4:8"]]
+ 0051b9dc ["CALL", null, ["callee:00c57f80:8"]]
- 0051b99c bytes 45f11c94
+ 0051b9dc bytes 69f11c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1b7f16b20c46176b530c3551e862ce5"></a>

### [`0051b9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051b9d4.md) → [`0051ba14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051ba14.md) FUN_0051ba14

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051ba3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051b9d4.md#insn-0051ba3c) · [`0051ba70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051b9d4.md#insn-0051ba70)
- 新版 `0051ba7c`（命令位置の公開資料なし） · `0051bab0`（命令位置の公開資料なし）

~~~diff
- 0051ba3c ["INT_ADD", "register:40f0:8", ["const:51ba3c:8", "const:4:8"]]
- 0051ba3c ["CALL", null, ["callee:00c57f60:8"]]
+ 0051ba7c ["INT_ADD", "register:40f0:8", ["const:51ba7c:8", "const:4:8"]]
+ 0051ba7c ["CALL", null, ["callee:00c57f60:8"]]
- 0051ba3c bytes 15f11c94
+ 0051ba7c bytes 39f11c94
- 0051ba70 ["INT_ADD", "register:40f0:8", ["const:51ba70:8", "const:4:8"]]
- 0051ba70 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0051bab0 ["INT_ADD", "register:40f0:8", ["const:51bab0:8", "const:4:8"]]
+ 0051bab0 ["CALL", null, ["callee:0043bbe4:8"]]
- 0051ba70 bytes 4d80fc97
+ 0051bab0 bytes 4d80fc97
~~~


<a id="compare-c057723b0ad617b3e58ce9e5c3d31c20"></a>

### [`0051baa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051baa4.md) → [`0051bae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051bae4.md) FUN_0051bae4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051bac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051baa4.md#insn-0051bac0)
- 新版 `0051bb00`（命令位置の公開資料なし）

~~~diff
- 0051bac0 ["INT_ADD", "register:40f0:8", ["const:51bac0:8", "const:4:8"]]
- 0051bac0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0051bb00 ["INT_ADD", "register:40f0:8", ["const:51bb00:8", "const:4:8"]]
+ 0051bb00 ["CALL", null, ["callee:00c57f80:8"]]
- 0051bac0 bytes fcf01c94
+ 0051bb00 bytes 20f11c94
~~~


<a id="compare-a9e2b4d442f728f801a2f4a2a676754e"></a>

### [`0051bff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051bff0.md) → [`0051c030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c030.md) FUN_0051c030

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051c038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051bff0.md#insn-0051c038)
- 新版 `0051c078`（命令位置の公開資料なし）

~~~diff
- 0051c038 ["INT_ADD", "register:40f0:8", ["const:51c038:8", "const:4:8"]]
- 0051c038 ["CALL", null, ["callee:00c57f80:8"]]
+ 0051c078 ["INT_ADD", "register:40f0:8", ["const:51c078:8", "const:4:8"]]
+ 0051c078 ["CALL", null, ["callee:00c57f80:8"]]
- 0051c038 bytes 9eef1c94
+ 0051c078 bytes c2ef1c94
~~~


<a id="compare-ae44b16e0fd959d3028e055d2d643232"></a>

### [`0051c80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c80c.md) → [`0051c84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c84c.md) _ZN5Botan14Cert_Extension20Certificate_Policies8validateERKNS_16X509_CertificateES4_RKNSt6__ndk16vectorINS5_10shared_ptrIS3_EENS5_9allocator

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0051c994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c994.md) [`005408bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005408bc.md) [`0054d0ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d0ec.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0051c9d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c9d4.md) [`005408fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005408fc.md) [`0054d12c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054d/0054d12c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051c844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c80c.md#insn-0051c844) · [`0051c8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c80c.md#insn-0051c8d8) · [`0051c90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c80c.md#insn-0051c90c)
- 新版 `0051c884`（命令位置の公開資料なし） · `0051c918`（命令位置の公開資料なし） · `0051c94c`（命令位置の公開資料なし）

~~~diff
- 0051c844 ["INT_ADD", "register:40f0:8", ["const:51c844:8", "const:4:8"]]
- 0051c844 ["CALL", null, ["callee:0051c9d4:8"]]
+ 0051c884 ["INT_ADD", "register:40f0:8", ["const:51c884:8", "const:4:8"]]
+ 0051c884 ["CALL", null, ["callee:0051c9d4:8"]]
- 0051c844 bytes 54000094
+ 0051c884 bytes 54000094
- 0051c8d8 ["INT_ADD", "register:40f0:8", ["const:51c8d8:8", "const:4:8"]]
- 0051c8d8 ["CALL", null, ["callee:00c57f60:8"]]
+ 0051c918 ["INT_ADD", "register:40f0:8", ["const:51c918:8", "const:4:8"]]
+ 0051c918 ["CALL", null, ["callee:00c57f60:8"]]
- 0051c8d8 bytes 6eed1c94
+ 0051c918 bytes 92ed1c94
- 0051c90c ["INT_ADD", "register:40f0:8", ["const:51c90c:8", "const:4:8"]]
- 0051c90c ["CALL", null, ["callee:0043bbe4:8"]]
+ 0051c94c ["INT_ADD", "register:40f0:8", ["const:51c94c:8", "const:4:8"]]
+ 0051c94c ["CALL", null, ["callee:0043bbe4:8"]]
- 0051c90c bytes a67cfc97
+ 0051c94c bytes a67cfc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7757f55969b72165d66df6853d529bd"></a>

### [`0051c994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c994.md) → [`0051c9d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c9d4.md) FUN_0051c9d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0051c80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c80c.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0054cc34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054cc34.md) [`0054cfd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054cfd0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0051c84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c84c.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0054cc74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054c/0054cc74.md) [`0054d010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054d/0054d010.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051c9e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c994.md#insn-0051c9e4) · [`0051ca14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c994.md#insn-0051ca14) · [`0051ca30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c994.md#insn-0051ca30)
- 新版 `0051ca24`（命令位置の公開資料なし） · `0051ca54`（命令位置の公開資料なし） · `0051ca70`（命令位置の公開資料なし）

~~~diff
- 0051c9e4 ["INT_ADD", "register:40f0:8", ["const:51c9e4:8", "const:4:8"]]
- 0051c9e4 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0051ca24 ["INT_ADD", "register:40f0:8", ["const:51ca24:8", "const:4:8"]]
+ 0051ca24 ["CALL", null, ["callee:0043bbe4:8"]]
- 0051c9e4 bytes 707cfc97
+ 0051ca24 bytes 707cfc97
- 0051ca14 ["INT_ADD", "register:40f0:8", ["const:51ca14:8", "const:4:8"]]
- 0051ca14 ["CALL", null, ["callee:0054cc74:8"]]
+ 0051ca54 ["INT_ADD", "register:40f0:8", ["const:51ca54:8", "const:4:8"]]
+ 0051ca54 ["CALL", null, ["callee:0054cc74:8"]]
- 0051ca14 bytes 88c00094
+ 0051ca54 bytes 88c00094
- 0051ca30 ["INT_ADD", "register:40f0:8", ["const:51ca30:8", "const:4:8"]]
- 0051ca30 ["CALL", null, ["callee:0054d010:8"]]
+ 0051ca70 ["INT_ADD", "register:40f0:8", ["const:51ca70:8", "const:4:8"]]
+ 0051ca70 ["CALL", null, ["callee:0054d010:8"]]
- 0051ca30 bytes 68c10094
+ 0051ca70 bytes 68c10094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c3abe2d11a0861518e13e105f606ddd"></a>

### [`0051f048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f048.md) → [`0051f088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f088.md) _ZNK5Botan14Cert_Extension17Unknown_Extension12encode_innerEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051f078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f048.md#insn-0051f078) · [`0051f090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f048.md#insn-0051f090) · [`0051f0ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f048.md#insn-0051f0ac)
- 新版 `0051f0b8`（命令位置の公開資料なし） · `0051f0d0`（命令位置の公開資料なし） · `0051f0ec`（命令位置の公開資料なし）

~~~diff
- 0051f078 ["INT_ADD", "register:40f0:8", ["const:51f078:8", "const:4:8"]]
- 0051f078 ["CALL", null, ["callee:00c57f60:8"]]
+ 0051f0b8 ["INT_ADD", "register:40f0:8", ["const:51f0b8:8", "const:4:8"]]
+ 0051f0b8 ["CALL", null, ["callee:00c57f60:8"]]
- 0051f078 bytes 86e31c94
+ 0051f0b8 bytes aae31c94
- 0051f090 ["INT_ADD", "register:40f0:8", ["const:51f090:8", "const:4:8"]]
- 0051f090 ["CALL", null, ["callee:00c580d0:8"]]
+ 0051f0d0 ["INT_ADD", "register:40f0:8", ["const:51f0d0:8", "const:4:8"]]
+ 0051f0d0 ["CALL", null, ["callee:00c580d0:8"]]
- 0051f090 bytes dce31c94
+ 0051f0d0 bytes 00e41c94
- 0051f0ac ["INT_ADD", "register:40f0:8", ["const:51f0ac:8", "const:4:8"]]
- 0051f0ac ["CALL", null, ["callee:0049f46c:8"]]
+ 0051f0ec ["INT_ADD", "register:40f0:8", ["const:51f0ec:8", "const:4:8"]]
+ 0051f0ec ["CALL", null, ["callee:0049f46c:8"]]
- 0051f0ac bytes e000fe97
+ 0051f0ec bytes e000fe97
~~~


<a id="compare-03d7bf93897f84a7c7827aee780335f3"></a>

### [`0051f0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f0f4.md) → [`0051f134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f134.md) _ZNK5Botan11X509_Object11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c586b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586b0.md) [`00c586c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586c0.md) [`00c586d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586d0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58780.md) [`00c58790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58790.md) [`00c587a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051f11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f0f4.md#insn-0051f11c) · [`0051f12c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f0f4.md#insn-0051f12c) · [`0051f148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f0f4.md#insn-0051f148)
- 新版 `0051f15c`（命令位置の公開資料なし） · `0051f16c`（命令位置の公開資料なし） · `0051f188`（命令位置の公開資料なし）

~~~diff
- 0051f11c ["INT_ADD", "register:40f0:8", ["const:51f11c:8", "const:4:8"]]
- 0051f11c ["CALL", null, ["callee:00c58780:8"]]
+ 0051f15c ["INT_ADD", "register:40f0:8", ["const:51f15c:8", "const:4:8"]]
+ 0051f15c ["CALL", null, ["callee:00c58780:8"]]
- 0051f11c bytes 65e51c94
+ 0051f15c bytes 89e51c94
- 0051f12c ["INT_ADD", "register:40f0:8", ["const:51f12c:8", "const:4:8"]]
- 0051f12c ["CALL", null, ["callee:00c58780:8"]]
+ 0051f16c ["INT_ADD", "register:40f0:8", ["const:51f16c:8", "const:4:8"]]
+ 0051f16c ["CALL", null, ["callee:00c58780:8"]]
- 0051f12c bytes 61e51c94
+ 0051f16c bytes 85e51c94
- 0051f148 ["INT_ADD", "register:40f0:8", ["const:51f148:8", "const:4:8"]]
- 0051f148 ["CALL", null, ["callee:00c58790:8"]]
+ 0051f188 ["INT_ADD", "register:40f0:8", ["const:51f188:8", "const:4:8"]]
+ 0051f188 ["CALL", null, ["callee:00c58790:8"]]
- 0051f148 bytes 5ee51c94
+ 0051f188 bytes 82e51c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe2bd433c42b9db2d0753af78c0083c1"></a>

### [`0051f494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f494.md) → [`0051f4d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f4d4.md) _ZNK5Botan11X509_Object10PEM_encodeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59490.md) [`00c59e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59e80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59560.md) [`00c59f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051f4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f494.md#insn-0051f4c0) · [`0051f4d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f494.md#insn-0051f4d4) · [`0051f4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f494.md#insn-0051f4ec)
- 新版 `0051f500`（命令位置の公開資料なし） · `0051f514`（命令位置の公開資料なし） · `0051f52c`（命令位置の公開資料なし）

~~~diff
- 0051f4c0 ["INT_ADD", "register:40f0:8", ["const:51f4c0:8", "const:4:8"]]
- 0051f4c0 ["CALL", null, ["callee:00c59f50:8"]]
+ 0051f500 ["INT_ADD", "register:40f0:8", ["const:51f500:8", "const:4:8"]]
+ 0051f500 ["CALL", null, ["callee:00c59f50:8"]]
- 0051f4c0 bytes 70ea1c94
+ 0051f500 bytes 94ea1c94
- 0051f4d4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051f4d4 ["INT_ADD", "register:40f0:8", ["const:51f4d4:8", "const:4:8"]]
- 0051f4d4 ["CALLIND", null, ["register:0:8"]]
+ 0051f514 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051f514 ["INT_ADD", "register:40f0:8", ["const:51f514:8", "const:4:8"]]
+ 0051f514 ["CALLIND", null, ["register:0:8"]]
- 0051f4d4 bytes 20013fd6
+ 0051f514 bytes 20013fd6
- 0051f4ec ["INT_ADD", "register:40f0:8", ["const:51f4ec:8", "const:4:8"]]
- 0051f4ec ["CALL", null, ["callee:00c59560:8"]]
+ 0051f52c ["INT_ADD", "register:40f0:8", ["const:51f52c:8", "const:4:8"]]
+ 0051f52c ["CALL", null, ["callee:00c59560:8"]]
- 0051f4ec bytes e9e71c94
+ 0051f52c bytes 0de81c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5e5162221dbf456ad04f27958b6273c"></a>

### [`0051ffb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051ffb0.md) → [`0051fff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051fff0.md) FUN_0051fff0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051ffcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051ffb0.md#insn-0051ffcc) · [`0051ffdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051ffb0.md#insn-0051ffdc) · [`0051ffec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051ffb0.md#insn-0051ffec)
- 新版 `0052000c`（命令位置の公開資料なし） · `0052001c`（命令位置の公開資料なし） · `0052002c`（命令位置の公開資料なし）

~~~diff
- 0051ffcc ["INT_ADD", "register:40f0:8", ["const:51ffcc:8", "const:4:8"]]
- 0051ffcc ["CALL", null, ["callee:00c57f80:8"]]
+ 0052000c ["INT_ADD", "register:40f0:8", ["const:52000c:8", "const:4:8"]]
+ 0052000c ["CALL", null, ["callee:00c57f80:8"]]
- 0051ffcc bytes b9df1c94
+ 0052000c bytes dddf1c94
- 0051ffdc ["INT_ADD", "register:40f0:8", ["const:51ffdc:8", "const:4:8"]]
- 0051ffdc ["CALL", null, ["callee:00c57f80:8"]]
+ 0052001c ["INT_ADD", "register:40f0:8", ["const:52001c:8", "const:4:8"]]
+ 0052001c ["CALL", null, ["callee:00c57f80:8"]]
- 0051ffdc bytes b5df1c94
+ 0052001c bytes d9df1c94
- 0051ffec ["INT_ADD", "register:40f0:8", ["const:51ffec:8", "const:4:8"]]
- 0051ffec ["CALL", null, ["callee:00c57f80:8"]]
+ 0052002c ["INT_ADD", "register:40f0:8", ["const:52002c:8", "const:4:8"]]
+ 0052002c ["CALL", null, ["callee:00c57f80:8"]]
- 0051ffec bytes b1df1c94
+ 0052002c bytes d5df1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65f1e175fdab582fe46a9593455b6d0c"></a>

### [`00520034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520034.md) → [`00520074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520074.md) _ZNK5Botan11X509_Object15check_signatureERKNS_10Public_KeyE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59cb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59d80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052003c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520034.md#insn-0052003c)
- 新版 `0052007c`（命令位置の公開資料なし）

~~~diff
- 0052003c ["INT_ADD", "register:40f0:8", ["const:52003c:8", "const:4:8"]]
- 0052003c ["CALL", null, ["callee:00c59d80:8"]]
+ 0052007c ["INT_ADD", "register:40f0:8", ["const:52007c:8", "const:4:8"]]
+ 0052007c ["CALL", null, ["callee:00c59d80:8"]]
- 0052003c bytes 1de71c94
+ 0052007c bytes 41e71c94
~~~


