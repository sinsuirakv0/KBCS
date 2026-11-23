# v16.0.0 → v16.0.1 · 要調査の変更候補 (8)

[一覧の目次](README.md)

<a id="compare-3aa07adf4e89ca2252d566b86e7b05e1"></a>

### [`005017a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/005017a0.md) → [`005017e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/005017e0.md) _ZNK5Botan16X509_Certificate10subject_dnEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005017a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/005017a0.md#insn-005017a8)
- 新版 `005017e8`（命令位置の公開資料なし）

~~~diff
- 005017a8 ["INT_ADD", "register:40f0:8", ["const:5017a8:8", "const:4:8"]]
- 005017a8 ["CALL", null, ["callee:00c599f0:8"]]
+ 005017e8 ["INT_ADD", "register:40f0:8", ["const:5017e8:8", "const:4:8"]]
+ 005017e8 ["CALL", null, ["callee:00c599f0:8"]]
- 005017a8 bytes 925f1d94
+ 005017e8 bytes 82601d94
~~~


<a id="compare-4cd120aa1f97fe9ab3b85d8588147560"></a>

### [`005017b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/005017b8.md) → [`005017f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/005017f8.md) FUN_005017f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005017f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/005017b8.md#insn-005017f4) · [`00501810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/005017b8.md#insn-00501810)
- 新版 `00501834`（命令位置の公開資料なし） · `00501850`（命令位置の公開資料なし）

~~~diff
- 005017f4 ["INT_ADD", "register:40f0:8", ["const:5017f4:8", "const:4:8"]]
- 005017f4 ["CALL", null, ["callee:0053af90:8"]]
+ 00501834 ["INT_ADD", "register:40f0:8", ["const:501834:8", "const:4:8"]]
+ 00501834 ["CALL", null, ["callee:0053af90:8"]]
- 005017f4 bytes d7e50094
+ 00501834 bytes d7e50094
- 00501810 ["INT_ADD", "register:40f0:8", ["const:501810:8", "const:4:8"]]
- 00501810 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00501850 ["INT_ADD", "register:40f0:8", ["const:501850:8", "const:4:8"]]
+ 00501850 ["CALL", null, ["callee:00c57eb0:8"]]
- 00501810 bytes a8581d94
+ 00501850 bytes 98591d94
~~~


<a id="compare-de96de2b54d51d216f0ff8a6eefddfc7"></a>

### [`00501840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501840.md) → [`00501880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501880.md) _ZNK5Botan27Certificate_Store_In_Memory9find_certERKNS_7X509_DNERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59600.md) · 呼出先 9件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c59a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a00.md) · 呼出先 9件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050188c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501840.md#insn-0050188c) · [`00501894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501840.md#insn-00501894) · [`005018a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501840.md#insn-005018a0)
- 新版 `005018cc`（命令位置の公開資料なし） · `005018d4`（命令位置の公開資料なし） · `005018e0`（命令位置の公開資料なし）

~~~diff
- 0050188c ["INT_ADD", "register:40f0:8", ["const:50188c:8", "const:4:8"]]
- 0050188c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005018cc ["INT_ADD", "register:40f0:8", ["const:5018cc:8", "const:4:8"]]
+ 005018cc ["CALL", null, ["callee:00c57eb0:8"]]
- 0050188c bytes 89581d94
+ 005018cc bytes 79591d94
- 00501894 ["INT_ADD", "register:40f0:8", ["const:501894:8", "const:4:8"]]
- 00501894 ["CALL", null, ["callee:00c599f0:8"]]
+ 005018d4 ["INT_ADD", "register:40f0:8", ["const:5018d4:8", "const:4:8"]]
+ 005018d4 ["CALL", null, ["callee:00c599f0:8"]]
- 00501894 bytes 575f1d94
+ 005018d4 bytes 47601d94
- 005018a0 ["INT_ADD", "register:40f0:8", ["const:5018a0:8", "const:4:8"]]
- 005018a0 ["CALL", null, ["callee:00c59a10:8"]]
+ 005018e0 ["INT_ADD", "register:40f0:8", ["const:5018e0:8", "const:4:8"]]
+ 005018e0 ["CALL", null, ["callee:00c59a10:8"]]
- 005018a0 bytes 5c5f1d94
+ 005018e0 bytes 4c601d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3767d340b9e6d193ddbfe1f07b521ccd"></a>

### [`005019dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/005019dc.md) → [`00501a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501a1c.md) _ZNK5Botan16X509_Certificate14subject_key_idEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005019e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/005019dc.md#insn-005019e4)
- 新版 `00501a24`（命令位置の公開資料なし）

~~~diff
- 005019e4 ["INT_ADD", "register:40f0:8", ["const:5019e4:8", "const:4:8"]]
- 005019e4 ["CALL", null, ["callee:00c599f0:8"]]
+ 00501a24 ["INT_ADD", "register:40f0:8", ["const:501a24:8", "const:4:8"]]
+ 00501a24 ["CALL", null, ["callee:00c599f0:8"]]
- 005019e4 bytes 035f1d94
+ 00501a24 bytes f35f1d94
~~~


<a id="compare-cc65857a3e5b97b7c9929c764063a78a"></a>

### [`005019f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/005019f4.md) → [`00501a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501a34.md) _ZN5BotaneqERKNS_7X509_DNES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59610.md) · 呼出先 4件 [`00549628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549628.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c594f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c594f0.md) [`00c59620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59620.md)
- 新版 呼出元 1件 [`00c59a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a10.md) · 呼出先 4件 [`00549668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549668.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c598f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c598f0.md) [`00c59a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00501a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/005019f4.md#insn-00501a20) · [`00501a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/005019f4.md#insn-00501a2c) · [`00501aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/005019f4.md#insn-00501aac)
- 新版 `00501a60`（命令位置の公開資料なし） · `00501a6c`（命令位置の公開資料なし） · `00501aec`（命令位置の公開資料なし）

~~~diff
- 00501a20 ["INT_ADD", "register:40f0:8", ["const:501a20:8", "const:4:8"]]
- 00501a20 ["CALL", null, ["callee:00c59a20:8"]]
+ 00501a60 ["INT_ADD", "register:40f0:8", ["const:501a60:8", "const:4:8"]]
+ 00501a60 ["CALL", null, ["callee:00c59a20:8"]]
- 00501a20 bytes 005f1d94
+ 00501a60 bytes f05f1d94
- 00501a2c ["INT_ADD", "register:40f0:8", ["const:501a2c:8", "const:4:8"]]
- 00501a2c ["CALL", null, ["callee:00c59a20:8"]]
+ 00501a6c ["INT_ADD", "register:40f0:8", ["const:501a6c:8", "const:4:8"]]
+ 00501a6c ["CALL", null, ["callee:00c59a20:8"]]
- 00501a2c bytes fd5e1d94
+ 00501a6c bytes ed5f1d94
- 00501aac ["INT_ADD", "register:40f0:8", ["const:501aac:8", "const:4:8"]]
- 00501aac ["CALL", null, ["callee:00c598f0:8"]]
+ 00501aec ["INT_ADD", "register:40f0:8", ["const:501aec:8", "const:4:8"]]
+ 00501aec ["CALL", null, ["callee:00c598f0:8"]]
- 00501aac bytes 915e1d94
+ 00501aec bytes 815f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ab46796874dbbea708b0a2647d12fc2"></a>

### [`00501bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501bac.md) → [`00501bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501bec.md) _ZNK5Botan27Certificate_Store_In_Memory14find_all_certsERKNS_7X509_DNERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59630.md) · 呼出先 10件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00548558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548558.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c59a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a30.md) · 呼出先 10件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00548598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548598.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00501c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501bac.md#insn-00501c00) · [`00501c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501bac.md#insn-00501c20) · [`00501c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501bac.md#insn-00501c44)
- 新版 `00501c40`（命令位置の公開資料なし） · `00501c60`（命令位置の公開資料なし） · `00501c84`（命令位置の公開資料なし）

~~~diff
- 00501c00 ["INT_ADD", "register:40f0:8", ["const:501c00:8", "const:4:8"]]
- 00501c00 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00501c40 ["INT_ADD", "register:40f0:8", ["const:501c40:8", "const:4:8"]]
+ 00501c40 ["CALL", null, ["callee:00c57eb0:8"]]
- 00501c00 bytes ac571d94
+ 00501c40 bytes 9c581d94
- 00501c20 ["INT_ADD", "register:40f0:8", ["const:501c20:8", "const:4:8"]]
- 00501c20 ["CALL", null, ["callee:00c599f0:8"]]
+ 00501c60 ["INT_ADD", "register:40f0:8", ["const:501c60:8", "const:4:8"]]
+ 00501c60 ["CALL", null, ["callee:00c599f0:8"]]
- 00501c20 bytes 745e1d94
+ 00501c60 bytes 645f1d94
- 00501c44 ["INT_ADD", "register:40f0:8", ["const:501c44:8", "const:4:8"]]
- 00501c44 ["CALL", null, ["callee:00c57e90:8"]]
+ 00501c84 ["INT_ADD", "register:40f0:8", ["const:501c84:8", "const:4:8"]]
+ 00501c84 ["CALL", null, ["callee:00c57e90:8"]]
- 00501c44 bytes 93571d94
+ 00501c84 bytes 83581d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90aa49d2692d867a7d73a76919c0a618"></a>

### [`00501d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501d78.md) → [`00501db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501db8.md) FUN_00501db8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052cdb0.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0052cdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052cdf0.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00501dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501d78.md#insn-00501dc4) · [`00501dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501d78.md#insn-00501dd8) · [`00501de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501d78.md#insn-00501de0)
- 新版 `00501e04`（命令位置の公開資料なし） · `00501e18`（命令位置の公開資料なし） · `00501e20`（命令位置の公開資料なし）

~~~diff
- 00501dc4 ["INT_ADD", "register:40f0:8", ["const:501dc4:8", "const:4:8"]]
- 00501dc4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00501e04 ["INT_ADD", "register:40f0:8", ["const:501e04:8", "const:4:8"]]
+ 00501e04 ["CALL", null, ["callee:00c53d00:8"]]
- 00501dc4 bytes c7461d94
+ 00501e04 bytes bf471d94
- 00501dd8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00501dd8 ["INT_ADD", "register:40f0:8", ["const:501dd8:8", "const:4:8"]]
- 00501dd8 ["CALLIND", null, ["register:0:8"]]
+ 00501e18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00501e18 ["INT_ADD", "register:40f0:8", ["const:501e18:8", "const:4:8"]]
+ 00501e18 ["CALLIND", null, ["register:0:8"]]
- 00501dd8 bytes 00013fd6
+ 00501e18 bytes 00013fd6
- 00501de0 ["INT_ADD", "register:40f0:8", ["const:501de0:8", "const:4:8"]]
- 00501de0 ["CALL", null, ["callee:00c57e80:8"]]
+ 00501e20 ["INT_ADD", "register:40f0:8", ["const:501e20:8", "const:4:8"]]
+ 00501e20 ["CALL", null, ["callee:00c57e80:8"]]
- 00501de0 bytes 28571d94
+ 00501e20 bytes 18581d94
~~~


<a id="compare-73d99a5d36f310a52d14f12bd8f909fc"></a>

### [`00502110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502110.md) → [`00502150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502150.md) _ZNK5Botan16X509_Certificate28subject_public_key_bitstringEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502110.md#insn-00502118)
- 新版 `00502158`（命令位置の公開資料なし）

~~~diff
- 00502118 ["INT_ADD", "register:40f0:8", ["const:502118:8", "const:4:8"]]
- 00502118 ["CALL", null, ["callee:00c599f0:8"]]
+ 00502158 ["INT_ADD", "register:40f0:8", ["const:502158:8", "const:4:8"]]
+ 00502158 ["CALL", null, ["callee:00c599f0:8"]]
- 00502118 bytes 365d1d94
+ 00502158 bytes 265e1d94
~~~


<a id="compare-8609310f7a115bbee8eb4b63045792ba"></a>

### [`00502430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502430.md) → [`00502470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502470.md) _ZNK5Botan16X509_Certificate14raw_subject_dnEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502430.md#insn-00502438)
- 新版 `00502478`（命令位置の公開資料なし）

~~~diff
- 00502438 ["INT_ADD", "register:40f0:8", ["const:502438:8", "const:4:8"]]
- 00502438 ["CALL", null, ["callee:00c599f0:8"]]
+ 00502478 ["INT_ADD", "register:40f0:8", ["const:502478:8", "const:4:8"]]
+ 00502478 ["CALL", null, ["callee:00c599f0:8"]]
- 00502438 bytes 6e5c1d94
+ 00502478 bytes 5e5d1d94
~~~


<a id="compare-238e88431d19f0c1543497a66f154f8f"></a>

### [`005025bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005025bc.md) → [`005025fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005025fc.md) _ZN5Botan27Certificate_Store_In_Memory7add_crlENSt6__ndk110shared_ptrIKNS_8X509_CRLEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59640.md) · 呼出先 11件 [`005027b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005027b8.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00548b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548b80.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c59a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a40.md) · 呼出先 11件 [`005027f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005027f8.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00548bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548bc0.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005025f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005025bc.md#insn-005025f0) · [`005025fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005025bc.md#insn-005025fc) · [`00502614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005025bc.md#insn-00502614)
- 新版 `00502630`（命令位置の公開資料なし） · `0050263c`（命令位置の公開資料なし） · `00502654`（命令位置の公開資料なし）

~~~diff
- 005025f0 ["INT_ADD", "register:40f0:8", ["const:5025f0:8", "const:4:8"]]
- 005025f0 ["CALL", null, ["callee:00c59a50:8"]]
+ 00502630 ["INT_ADD", "register:40f0:8", ["const:502630:8", "const:4:8"]]
+ 00502630 ["CALL", null, ["callee:00c59a50:8"]]
- 005025f0 bytes 185c1d94
+ 00502630 bytes 085d1d94
- 005025fc ["INT_ADD", "register:40f0:8", ["const:5025fc:8", "const:4:8"]]
- 005025fc ["CALL", null, ["callee:005027f8:8"]]
+ 0050263c ["INT_ADD", "register:40f0:8", ["const:50263c:8", "const:4:8"]]
+ 0050263c ["CALL", null, ["callee:005027f8:8"]]
- 005025fc bytes 6f000094
+ 0050263c bytes 6f000094
- 00502614 ["INT_ADD", "register:40f0:8", ["const:502614:8", "const:4:8"]]
- 00502614 ["CALL", null, ["callee:00c59a50:8"]]
+ 00502654 ["INT_ADD", "register:40f0:8", ["const:502654:8", "const:4:8"]]
+ 00502654 ["CALL", null, ["callee:00c59a50:8"]]
- 00502614 bytes 0f5c1d94
+ 00502654 bytes ff5c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-847a1c82603cf7dd75b7290b3168141e"></a>

### [`00502764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502764.md) → [`005027a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005027a4.md) FUN_005027a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502764.md#insn-00502780) · [`005027a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502764.md#insn-005027a0)
- 新版 `005027c0`（命令位置の公開資料なし） · `005027e0`（命令位置の公開資料なし）

~~~diff
- 00502780 ["INT_ADD", "register:40f0:8", ["const:502780:8", "const:4:8"]]
- 00502780 ["CALL", null, ["callee:00c53d00:8"]]
+ 005027c0 ["INT_ADD", "register:40f0:8", ["const:5027c0:8", "const:4:8"]]
+ 005027c0 ["CALL", null, ["callee:00c53d00:8"]]
- 00502780 bytes 58441d94
+ 005027c0 bytes 50451d94
- 005027a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005027a0 ["INT_ADD", "register:40f0:8", ["const:5027a0:8", "const:4:8"]]
- 005027a0 ["CALLIND", null, ["register:0:8"]]
+ 005027e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005027e0 ["INT_ADD", "register:40f0:8", ["const:5027e0:8", "const:4:8"]]
+ 005027e0 ["CALLIND", null, ["register:0:8"]]
- 005027a0 bytes 00013fd6
+ 005027e0 bytes 00013fd6
~~~


<a id="compare-3a8711a1ccca7968786e102f4867b5f4"></a>

### [`005028e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005028e4.md) → [`00502924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502924.md) _ZNK5Botan8X509_CRL11this_updateEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59650.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005028ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005028e4.md#insn-005028ec)
- 新版 `0050292c`（命令位置の公開資料なし）

~~~diff
- 005028ec ["INT_ADD", "register:40f0:8", ["const:5028ec:8", "const:4:8"]]
- 005028ec ["CALL", null, ["callee:00c59a50:8"]]
+ 0050292c ["INT_ADD", "register:40f0:8", ["const:50292c:8", "const:4:8"]]
+ 0050292c ["CALL", null, ["callee:00c59a50:8"]]
- 005028ec bytes 595b1d94
+ 0050292c bytes 495c1d94
~~~


<a id="compare-13e26620135d11a6bf5d9c377428c4af"></a>

### [`005028fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005028fc.md) → [`0050293c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/0050293c.md) _ZNK5Botan27Certificate_Store_In_Memory12find_crl_forERKNS_16X509_CertificateE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 10件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005028fc.md#insn-00502938) · [`00502954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005028fc.md#insn-00502954) · [`0050295c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005028fc.md#insn-0050295c)
- 新版 `00502978`（命令位置の公開資料なし） · `00502994`（命令位置の公開資料なし） · `0050299c`（命令位置の公開資料なし）

~~~diff
- 00502938 ["INT_ADD", "register:40f0:8", ["const:502938:8", "const:4:8"]]
- 00502938 ["CALL", null, ["callee:00c599f0:8"]]
+ 00502978 ["INT_ADD", "register:40f0:8", ["const:502978:8", "const:4:8"]]
+ 00502978 ["CALL", null, ["callee:00c599f0:8"]]
- 00502938 bytes 2e5b1d94
+ 00502978 bytes 1e5c1d94
- 00502954 ["INT_ADD", "register:40f0:8", ["const:502954:8", "const:4:8"]]
- 00502954 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00502994 ["INT_ADD", "register:40f0:8", ["const:502994:8", "const:4:8"]]
+ 00502994 ["CALL", null, ["callee:00c57eb0:8"]]
- 00502954 bytes 57541d94
+ 00502994 bytes 47551d94
- 0050295c ["INT_ADD", "register:40f0:8", ["const:50295c:8", "const:4:8"]]
- 0050295c ["CALL", null, ["callee:00c59a50:8"]]
+ 0050299c ["INT_ADD", "register:40f0:8", ["const:50299c:8", "const:4:8"]]
+ 0050299c ["CALL", null, ["callee:00c59a50:8"]]
- 0050295c bytes 3d5b1d94
+ 0050299c bytes 2d5c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b26133b49d1cfe61dd536bacad6c145d"></a>

### [`00502ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502ab4.md) → [`00502af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502af4.md) _ZNK5Botan16X509_Certificate16authority_key_idEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502ab4.md#insn-00502abc)
- 新版 `00502afc`（命令位置の公開資料なし）

~~~diff
- 00502abc ["INT_ADD", "register:40f0:8", ["const:502abc:8", "const:4:8"]]
- 00502abc ["CALL", null, ["callee:00c599f0:8"]]
+ 00502afc ["INT_ADD", "register:40f0:8", ["const:502afc:8", "const:4:8"]]
+ 00502afc ["CALL", null, ["callee:00c599f0:8"]]
- 00502abc bytes cd5a1d94
+ 00502afc bytes bd5b1d94
~~~


<a id="compare-e3091c174a2c5014f4d2e6e1f78b1b72"></a>

### [`00502acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502acc.md) → [`00502b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502b0c.md) _ZNK5Botan8X509_CRL16authority_key_idEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59650.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502acc.md#insn-00502ad4)
- 新版 `00502b14`（命令位置の公開資料なし）

~~~diff
- 00502ad4 ["INT_ADD", "register:40f0:8", ["const:502ad4:8", "const:4:8"]]
- 00502ad4 ["CALL", null, ["callee:00c59a50:8"]]
+ 00502b14 ["INT_ADD", "register:40f0:8", ["const:502b14:8", "const:4:8"]]
+ 00502b14 ["CALL", null, ["callee:00c59a50:8"]]
- 00502ad4 bytes df5a1d94
+ 00502b14 bytes cf5b1d94
~~~


<a id="compare-59015510a56f2010fb446ed1fe096c60"></a>

### [`00502ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502ae4.md) → [`00502b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502b24.md) _ZNK5Botan16X509_Certificate9issuer_dnEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502ae4.md#insn-00502aec)
- 新版 `00502b2c`（命令位置の公開資料なし）

~~~diff
- 00502aec ["INT_ADD", "register:40f0:8", ["const:502aec:8", "const:4:8"]]
- 00502aec ["CALL", null, ["callee:00c599f0:8"]]
+ 00502b2c ["INT_ADD", "register:40f0:8", ["const:502b2c:8", "const:4:8"]]
+ 00502b2c ["CALL", null, ["callee:00c599f0:8"]]
- 00502aec bytes c15a1d94
+ 00502b2c bytes b15b1d94
~~~


<a id="compare-08a499aae664233577bd5c60b1fc68c8"></a>

### [`00502b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502b64.md) → [`00502ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502ba4.md) FUN_00502ba4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502b64.md#insn-00502bb0) · [`00502bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502b64.md#insn-00502bc4) · [`00502bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502b64.md#insn-00502bcc)
- 新版 `00502bf0`（命令位置の公開資料なし） · `00502c04`（命令位置の公開資料なし） · `00502c0c`（命令位置の公開資料なし）

~~~diff
- 00502bb0 ["INT_ADD", "register:40f0:8", ["const:502bb0:8", "const:4:8"]]
- 00502bb0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00502bf0 ["INT_ADD", "register:40f0:8", ["const:502bf0:8", "const:4:8"]]
+ 00502bf0 ["CALL", null, ["callee:00c53d00:8"]]
- 00502bb0 bytes 4c431d94
+ 00502bf0 bytes 44441d94
- 00502bc4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00502bc4 ["INT_ADD", "register:40f0:8", ["const:502bc4:8", "const:4:8"]]
- 00502bc4 ["CALLIND", null, ["register:0:8"]]
+ 00502c04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00502c04 ["INT_ADD", "register:40f0:8", ["const:502c04:8", "const:4:8"]]
+ 00502c04 ["CALLIND", null, ["register:0:8"]]
- 00502bc4 bytes 00013fd6
+ 00502c04 bytes 00013fd6
- 00502bcc ["INT_ADD", "register:40f0:8", ["const:502bcc:8", "const:4:8"]]
- 00502bcc ["CALL", null, ["callee:00c57e80:8"]]
+ 00502c0c ["INT_ADD", "register:40f0:8", ["const:502c0c:8", "const:4:8"]]
+ 00502c0c ["CALL", null, ["callee:00c57e80:8"]]
- 00502bcc bytes ad531d94
+ 00502c0c bytes 9d541d94
~~~


<a id="compare-47fbc6604071ef0c863966502adbcecb"></a>

### [`00502e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502e80.md) → [`00502ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502ec0.md) FUN_00502ec0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00502e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502e80.md#insn-00502e9c) · [`00502ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502e80.md#insn-00502ebc)
- 新版 `00502edc`（命令位置の公開資料なし） · `00502efc`（命令位置の公開資料なし）

~~~diff
- 00502e9c ["INT_ADD", "register:40f0:8", ["const:502e9c:8", "const:4:8"]]
- 00502e9c ["CALL", null, ["callee:00c53d00:8"]]
+ 00502edc ["INT_ADD", "register:40f0:8", ["const:502edc:8", "const:4:8"]]
+ 00502edc ["CALL", null, ["callee:00c53d00:8"]]
- 00502e9c bytes 91421d94
+ 00502edc bytes 89431d94
- 00502ebc ["COPY", "register:0:8", ["register:4040:8"]]
- 00502ebc ["INT_ADD", "register:40f0:8", ["const:502ebc:8", "const:4:8"]]
- 00502ebc ["CALLIND", null, ["register:0:8"]]
+ 00502efc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00502efc ["INT_ADD", "register:40f0:8", ["const:502efc:8", "const:4:8"]]
+ 00502efc ["CALLIND", null, ["register:0:8"]]
- 00502ebc bytes 00013fd6
+ 00502efc bytes 00013fd6
~~~


<a id="compare-0248141fbe6697234c35a11ba6ce6241"></a>

### [`00503480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503480.md) → [`005034c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/005034c0.md) FUN_005034c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050349c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503480.md#insn-0050349c) · [`005034bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503480.md#insn-005034bc)
- 新版 `005034dc`（命令位置の公開資料なし） · `005034fc`（命令位置の公開資料なし）

~~~diff
- 0050349c ["INT_ADD", "register:40f0:8", ["const:50349c:8", "const:4:8"]]
- 0050349c ["CALL", null, ["callee:00c53d00:8"]]
+ 005034dc ["INT_ADD", "register:40f0:8", ["const:5034dc:8", "const:4:8"]]
+ 005034dc ["CALL", null, ["callee:00c53d00:8"]]
- 0050349c bytes 11411d94
+ 005034dc bytes 09421d94
- 005034bc ["COPY", "register:0:8", ["register:4040:8"]]
- 005034bc ["INT_ADD", "register:40f0:8", ["const:5034bc:8", "const:4:8"]]
- 005034bc ["CALLIND", null, ["register:0:8"]]
+ 005034fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005034fc ["INT_ADD", "register:40f0:8", ["const:5034fc:8", "const:4:8"]]
+ 005034fc ["CALLIND", null, ["register:0:8"]]
- 005034bc bytes 00013fd6
+ 005034fc bytes 00013fd6
~~~


<a id="compare-3294a015128a7fe131c7aba26860b33c"></a>

### [`005034d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/005034d0.md) → [`00503510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503510.md) _ZN5BotaneqERKNS_9CRL_EntryES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59690.md) · 呼出先 3件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c585e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585e0.md) [`00c596a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596a0.md)
- 新版 呼出元 1件 [`00c59a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a90.md) · 呼出先 3件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c589e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589e0.md) [`00c59aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59aa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005034e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/005034d0.md#insn-005034e8) · [`005034f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/005034d0.md#insn-005034f4) · [`00503514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/005034d0.md#insn-00503514)
- 新版 `00503528`（命令位置の公開資料なし） · `00503534`（命令位置の公開資料なし） · `00503554`（命令位置の公開資料なし）

~~~diff
- 005034e8 ["INT_ADD", "register:40f0:8", ["const:5034e8:8", "const:4:8"]]
- 005034e8 ["CALL", null, ["callee:00c59aa0:8"]]
+ 00503528 ["INT_ADD", "register:40f0:8", ["const:503528:8", "const:4:8"]]
+ 00503528 ["CALL", null, ["callee:00c59aa0:8"]]
- 005034e8 bytes 6e581d94
+ 00503528 bytes 5e591d94
- 005034f4 ["INT_ADD", "register:40f0:8", ["const:5034f4:8", "const:4:8"]]
- 005034f4 ["CALL", null, ["callee:00c59aa0:8"]]
+ 00503534 ["INT_ADD", "register:40f0:8", ["const:503534:8", "const:4:8"]]
+ 00503534 ["CALL", null, ["callee:00c59aa0:8"]]
- 005034f4 bytes 6b581d94
+ 00503534 bytes 5b591d94
- 00503514 ["INT_ADD", "register:40f0:8", ["const:503514:8", "const:4:8"]]
- 00503514 ["CALL", null, ["callee:00c58050:8"]]
+ 00503554 ["INT_ADD", "register:40f0:8", ["const:503554:8", "const:4:8"]]
+ 00503554 ["CALL", null, ["callee:00c58050:8"]]
- 00503514 bytes cf511d94
+ 00503554 bytes bf521d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-841cce9996bfde19ffb3635df918d68d"></a>

### [`00503580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503580.md) → [`005035c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/005035c0.md) _ZNK5Botan9CRL_Entry11expire_timeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c596a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59aa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00503588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503580.md#insn-00503588)
- 新版 `005035c8`（命令位置の公開資料なし）

~~~diff
- 00503588 ["INT_ADD", "register:40f0:8", ["const:503588:8", "const:4:8"]]
- 00503588 ["CALL", null, ["callee:00c59aa0:8"]]
+ 005035c8 ["INT_ADD", "register:40f0:8", ["const:5035c8:8", "const:4:8"]]
+ 005035c8 ["CALL", null, ["callee:00c59aa0:8"]]
- 00503588 bytes 46581d94
+ 005035c8 bytes 36591d94
~~~


<a id="compare-332aaec3a1a41c6491ec6b5bc96a112b"></a>

### [`00503598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503598.md) → [`005035d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/005035d8.md) _ZNK5Botan9CRL_Entry11reason_codeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c596a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59aa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005035a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503598.md#insn-005035a0)
- 新版 `005035e0`（命令位置の公開資料なし）

~~~diff
- 005035a0 ["INT_ADD", "register:40f0:8", ["const:5035a0:8", "const:4:8"]]
- 005035a0 ["CALL", null, ["callee:00c59aa0:8"]]
+ 005035e0 ["INT_ADD", "register:40f0:8", ["const:5035e0:8", "const:4:8"]]
+ 005035e0 ["CALL", null, ["callee:00c59aa0:8"]]
- 005035a0 bytes 40581d94
+ 005035e0 bytes 30591d94
~~~


<a id="compare-9cdefe69aa0b7c26dd9db995ac4fb528"></a>

### [`005035b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/005035b0.md) → [`005035f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/005035f0.md) _ZN5BotanneERKNS_9CRL_EntryES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59690.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005035b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/005035b0.md#insn-005035b8)
- 新版 `005035f8`（命令位置の公開資料なし）

~~~diff
- 005035b8 ["INT_ADD", "register:40f0:8", ["const:5035b8:8", "const:4:8"]]
- 005035b8 ["CALL", null, ["callee:00c59a90:8"]]
+ 005035f8 ["INT_ADD", "register:40f0:8", ["const:5035f8:8", "const:4:8"]]
+ 005035f8 ["CALL", null, ["callee:00c59a90:8"]]
- 005035b8 bytes 36581d94
+ 005035f8 bytes 26591d94
~~~


<a id="compare-1fcef68206226582872189dd7388811a"></a>

### [`00503714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503714.md) → [`00503754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503754.md) _ZNK5Botan9CRL_Entry10extensionsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c596a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59aa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050371c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503714.md#insn-0050371c)
- 新版 `0050375c`（命令位置の公開資料なし）

~~~diff
- 0050371c ["INT_ADD", "register:40f0:8", ["const:50371c:8", "const:4:8"]]
- 0050371c ["CALL", null, ["callee:00c59aa0:8"]]
+ 0050375c ["INT_ADD", "register:40f0:8", ["const:50375c:8", "const:4:8"]]
+ 0050375c ["CALL", null, ["callee:00c59aa0:8"]]
- 0050371c bytes e1571d94
+ 0050375c bytes d1581d94
~~~


<a id="compare-f36cff0d1422e9f90e2bc2365749f231"></a>

### [`00503d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503d58.md) → [`00503d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503d98.md) _ZNK5Botan10Data_StoreeqERKS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00548f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548f48.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00548f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548f88.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00503da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503d58.md#insn-00503da4)
- 新版 `00503de4`（命令位置の公開資料なし）

~~~diff
- 00503da4 ["INT_ADD", "register:40f0:8", ["const:503da4:8", "const:4:8"]]
- 00503da4 ["CALL", null, ["callee:00548f88:8"]]
+ 00503de4 ["INT_ADD", "register:40f0:8", ["const:503de4:8", "const:4:8"]]
+ 00503de4 ["CALL", null, ["callee:00548f88:8"]]
- 00503da4 bytes 69140194
+ 00503de4 bytes 69140194
~~~


<a id="compare-d3edfeb3f69dff272d51706e14a82627"></a>

### [`00503e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503e34.md) → [`00503e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503e74.md) _ZNK5Botan10Data_Store9has_valueERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00503ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503e34.md#insn-00503ea0)
- 新版 `00503ee0`（命令位置の公開資料なし）

~~~diff
- 00503ea0 ["INT_ADD", "register:40f0:8", ["const:503ea0:8", "const:4:8"]]
- 00503ea0 ["CALL", null, ["callee:00c58050:8"]]
+ 00503ee0 ["INT_ADD", "register:40f0:8", ["const:503ee0:8", "const:4:8"]]
+ 00503ee0 ["CALL", null, ["callee:00c58050:8"]]
- 00503ea0 bytes 6c4f1d94
+ 00503ee0 bytes 5c501d94
~~~


<a id="compare-aaff021d13a395cb0965fb5fbb893b91"></a>

### [`00503ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503ef4.md) → [`00503f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503f34.md) _ZNK5Botan10Data_Store10search_forENSt6__ndk18functionIFbNS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES8_EEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c596d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596d0.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00549094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549094.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c59ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ad0.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`005490d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/005490d4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00503f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503ef4.md#insn-00503f84) · [`00503fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503ef4.md#insn-00503fb0) · [`00503fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503ef4.md#insn-00503fcc)
- 新版 `00503fc4`（命令位置の公開資料なし） · `00503ff0`（命令位置の公開資料なし） · `0050400c`（命令位置の公開資料なし）

~~~diff
- 00503f84 ["INT_ADD", "register:40f0:8", ["const:503f84:8", "const:4:8"]]
- 00503f84 ["CALL", null, ["callee:0043bb20:8"]]
+ 00503fc4 ["INT_ADD", "register:40f0:8", ["const:503fc4:8", "const:4:8"]]
+ 00503fc4 ["CALL", null, ["callee:0043bb20:8"]]
- 00503f84 bytes d7defc97
+ 00503fc4 bytes d7defc97
- 00503fb0 ["INT_ADD", "register:40f0:8", ["const:503fb0:8", "const:4:8"]]
- 00503fb0 ["CALL", null, ["callee:0043bb20:8"]]
+ 00503ff0 ["INT_ADD", "register:40f0:8", ["const:503ff0:8", "const:4:8"]]
+ 00503ff0 ["CALL", null, ["callee:0043bb20:8"]]
- 00503fb0 bytes ccdefc97
+ 00503ff0 bytes ccdefc97
- 00503fcc ["COPY", "register:0:8", ["register:4040:8"]]
- 00503fcc ["INT_ADD", "register:40f0:8", ["const:503fcc:8", "const:4:8"]]
- 00503fcc ["CALLIND", null, ["register:0:8"]]
+ 0050400c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050400c ["INT_ADD", "register:40f0:8", ["const:50400c:8", "const:4:8"]]
+ 0050400c ["CALLIND", null, ["register:0:8"]]
- 00503fcc bytes 00013fd6
+ 0050400c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4049cf49ef6c8d515d6988354487a4ca"></a>

### [`00504180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504180.md) → [`005041c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005041c0.md) _ZNK5Botan10Data_Store3getERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c596e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596e0.md) · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00548058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548058.md)
- 新版 呼出元 1件 [`00c59ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ae0.md) · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00548098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548098.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050419c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504180.md#insn-0050419c) · [`005041f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504180.md#insn-005041f4) · [`00504208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504180.md#insn-00504208)
- 新版 `005041dc`（命令位置の公開資料なし） · `00504234`（命令位置の公開資料なし） · `00504248`（命令位置の公開資料なし）

~~~diff
- 0050419c ["INT_ADD", "register:40f0:8", ["const:50419c:8", "const:4:8"]]
- 0050419c ["CALL", null, ["callee:00548098:8"]]
+ 005041dc ["INT_ADD", "register:40f0:8", ["const:5041dc:8", "const:4:8"]]
+ 005041dc ["CALL", null, ["callee:00548098:8"]]
- 0050419c bytes af0f0194
+ 005041dc bytes af0f0194
- 005041f4 ["INT_ADD", "register:40f0:8", ["const:5041f4:8", "const:4:8"]]
- 005041f4 ["CALL", null, ["callee:00540d7c:8"]]
+ 00504234 ["INT_ADD", "register:40f0:8", ["const:504234:8", "const:4:8"]]
+ 00504234 ["CALL", null, ["callee:00540d7c:8"]]
- 005041f4 bytes d2f20094
+ 00504234 bytes d2f20094
- 00504208 ["INT_ADD", "register:40f0:8", ["const:504208:8", "const:4:8"]]
- 00504208 ["CALL", null, ["callee:0043bb20:8"]]
+ 00504248 ["INT_ADD", "register:40f0:8", ["const:504248:8", "const:4:8"]]
+ 00504248 ["CALL", null, ["callee:0043bb20:8"]]
- 00504208 bytes 36defc97
+ 00504248 bytes 36defc97
~~~


<a id="compare-d0817ce66f6ee73094d2519f1114d0aa"></a>

### [`00504988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504988.md) → [`005049c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005049c8.md) _ZN5Botan10Data_Store3addERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEj

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`004ff160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58390.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58790.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005049b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504988.md#insn-005049b8) · [`005049c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504988.md#insn-005049c8) · [`005049d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504988.md#insn-005049d8)
- 新版 `005049f8`（命令位置の公開資料なし） · `00504a08`（命令位置の公開資料なし） · `00504a18`（命令位置の公開資料なし）

~~~diff
- 005049b8 ["INT_ADD", "register:40f0:8", ["const:5049b8:8", "const:4:8"]]
- 005049b8 ["CALL", null, ["callee:00c58790:8"]]
+ 005049f8 ["INT_ADD", "register:40f0:8", ["const:5049f8:8", "const:4:8"]]
+ 005049f8 ["CALL", null, ["callee:00c58790:8"]]
- 005049b8 bytes 764e1d94
+ 005049f8 bytes 664f1d94
- 005049c8 ["INT_ADD", "register:40f0:8", ["const:5049c8:8", "const:4:8"]]
- 005049c8 ["CALL", null, ["callee:004ff1a0:8"]]
+ 00504a08 ["INT_ADD", "register:40f0:8", ["const:504a08:8", "const:4:8"]]
+ 00504a08 ["CALL", null, ["callee:004ff1a0:8"]]
- 005049c8 bytes e6e9ff97
+ 00504a08 bytes e6e9ff97
- 005049d8 ["INT_ADD", "register:40f0:8", ["const:5049d8:8", "const:4:8"]]
- 005049d8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00504a18 ["INT_ADD", "register:40f0:8", ["const:504a18:8", "const:4:8"]]
+ 00504a18 ["CALL", null, ["callee:00c57eb0:8"]]
- 005049d8 bytes 364c1d94
+ 00504a18 bytes 264d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bda8320d879fefaf4c7e53ac83dcd062"></a>

### [`00504d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504d50.md) → [`00504d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504d90.md) _ZN5Botan10Data_Store3addERKNSt6__ndk18multimapINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES8_NS1_4lessIS8_EENS6_INS1_4pai

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0053bb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bb30.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0053bb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bb70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00504d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504d50.md#insn-00504d8c)
- 新版 `00504dcc`（命令位置の公開資料なし）

~~~diff
- 00504d8c ["INT_ADD", "register:40f0:8", ["const:504d8c:8", "const:4:8"]]
- 00504d8c ["CALL", null, ["callee:0053bb70:8"]]
+ 00504dcc ["INT_ADD", "register:40f0:8", ["const:504dcc:8", "const:4:8"]]
+ 00504dcc ["CALL", null, ["callee:0053bb70:8"]]
- 00504d8c bytes 69db0094
+ 00504dcc bytes 69db0094
~~~


<a id="compare-34a6a5bf1229daabda042e90cea32e46"></a>

### [`00504f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504f94.md) → [`00504fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504fd4.md) _ZN5Botan7X509_DN13add_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md) [`00c59700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59700.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md) [`00c59b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00504fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504f94.md#insn-00504fc4) · [`00504fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504f94.md#insn-00504fd4) · [`00504fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504f94.md#insn-00504fe4)
- 新版 `00505004`（命令位置の公開資料なし） · `00505014`（命令位置の公開資料なし） · `00505024`（命令位置の公開資料なし）

~~~diff
- 00504fc4 ["INT_ADD", "register:40f0:8", ["const:504fc4:8", "const:4:8"]]
- 00504fc4 ["CALL", null, ["callee:00c58680:8"]]
+ 00505004 ["INT_ADD", "register:40f0:8", ["const:505004:8", "const:4:8"]]
+ 00505004 ["CALL", null, ["callee:00c58680:8"]]
- 00504fc4 bytes af4c1d94
+ 00505004 bytes 9f4d1d94
- 00504fd4 ["INT_ADD", "register:40f0:8", ["const:504fd4:8", "const:4:8"]]
- 00504fd4 ["CALL", null, ["callee:00c59b00:8"]]
+ 00505014 ["INT_ADD", "register:40f0:8", ["const:505014:8", "const:4:8"]]
+ 00505014 ["CALL", null, ["callee:00c59b00:8"]]
- 00504fd4 bytes cb511d94
+ 00505014 bytes bb521d94
- 00504fe4 ["INT_ADD", "register:40f0:8", ["const:504fe4:8", "const:4:8"]]
- 00504fe4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00505024 ["INT_ADD", "register:40f0:8", ["const:505024:8", "const:4:8"]]
+ 00505024 ["CALL", null, ["callee:00c57eb0:8"]]
- 00504fe4 bytes b34a1d94
+ 00505024 bytes a34b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14d297acf556447c9a7a480d2b5deb56"></a>

### [`00505294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/00505294.md) → [`005052d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00505/005052d4.md) FUN_005052d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0052d4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d4d0.md) [`0052e2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e2f4.md) · 呼出先 2件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md)
- 新版 呼出元 2件 [`0052d510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d510.md) [`0052e334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052e334.md) · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005052ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/00505294.md#insn-005052ac)
- 新版 `005052ec`（命令位置の公開資料なし）

~~~diff
- 005052ac ["INT_ADD", "register:40f0:8", ["const:5052ac:8", "const:4:8"]]
- 005052ac ["CALL", null, ["callee:0053af90:8"]]
+ 005052ec ["INT_ADD", "register:40f0:8", ["const:5052ec:8", "const:4:8"]]
+ 005052ec ["CALL", null, ["callee:0053af90:8"]]
- 005052ac bytes 29d70094
+ 005052ec bytes 29d70094
~~~


<a id="compare-dca3c11c158f0bf7215de66fa9bf9357"></a>

### [`00507a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507a74.md) → [`00507ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507ab4.md) _ZNK5Botan16X509_Certificate16subject_alt_nameEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0050732c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/0050732c.md) · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 1件 [`0050736c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/0050736c.md) · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00507a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507a74.md#insn-00507a7c)
- 新版 `00507abc`（命令位置の公開資料なし）

~~~diff
- 00507a7c ["INT_ADD", "register:40f0:8", ["const:507a7c:8", "const:4:8"]]
- 00507a7c ["CALL", null, ["callee:00c599f0:8"]]
+ 00507abc ["INT_ADD", "register:40f0:8", ["const:507abc:8", "const:4:8"]]
+ 00507abc ["CALL", null, ["callee:00c599f0:8"]]
- 00507a7c bytes dd461d94
+ 00507abc bytes cd471d94
~~~


<a id="compare-c53ce86ae6269d04ae1c131d2776d431"></a>

### [`00507dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507dc4.md) → [`00507e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507e04.md) _ZNK5Botan7X509_DN13get_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59760.md) · 呼出先 7件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`0054b234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b234.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c59b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b60.md) · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`0054b274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b274.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00507df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507dc4.md#insn-00507df8) · [`00507e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507dc4.md#insn-00507e04) · [`00507e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507dc4.md#insn-00507e14)
- 新版 `00507e38`（命令位置の公開資料なし） · `00507e44`（命令位置の公開資料なし） · `00507e54`（命令位置の公開資料なし）

~~~diff
- 00507df8 ["INT_ADD", "register:40f0:8", ["const:507df8:8", "const:4:8"]]
- 00507df8 ["CALL", null, ["callee:00c59b70:8"]]
+ 00507e38 ["INT_ADD", "register:40f0:8", ["const:507e38:8", "const:4:8"]]
+ 00507e38 ["CALL", null, ["callee:00c59b70:8"]]
- 00507df8 bytes 5e461d94
+ 00507e38 bytes 4e471d94
- 00507e04 ["INT_ADD", "register:40f0:8", ["const:507e04:8", "const:4:8"]]
- 00507e04 ["CALL", null, ["callee:00c58680:8"]]
+ 00507e44 ["INT_ADD", "register:40f0:8", ["const:507e44:8", "const:4:8"]]
+ 00507e44 ["CALL", null, ["callee:00c58680:8"]]
- 00507e04 bytes 1f411d94
+ 00507e44 bytes 0f421d94
- 00507e14 ["INT_ADD", "register:40f0:8", ["const:507e14:8", "const:4:8"]]
- 00507e14 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00507e54 ["INT_ADD", "register:40f0:8", ["const:507e54:8", "const:4:8"]]
+ 00507e54 ["CALL", null, ["callee:00c57eb0:8"]]
- 00507e14 bytes 273f1d94
+ 00507e54 bytes 17401d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3323723aa1f2b209271c0ae62c46944f"></a>

### [`00508acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508acc.md) → [`00508b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508b0c.md) _ZNK5Botan7X509_DN14get_attributesEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59620.md) · 呼出先 4件 [`0054b02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b02c.md) [`0054b15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b15c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c59a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a20.md) · 呼出先 4件 [`0054b06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b06c.md) [`0054b19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b19c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00508b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508acc.md#insn-00508b4c) · [`00508b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508acc.md#insn-00508b58) · [`00508b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508acc.md#insn-00508b68)
- 新版 `00508b8c`（命令位置の公開資料なし） · `00508b98`（命令位置の公開資料なし） · `00508ba8`（命令位置の公開資料なし）

~~~diff
- 00508b4c ["INT_ADD", "register:40f0:8", ["const:508b4c:8", "const:4:8"]]
- 00508b4c ["CALL", null, ["callee:0054b19c:8"]]
+ 00508b8c ["INT_ADD", "register:40f0:8", ["const:508b8c:8", "const:4:8"]]
+ 00508b8c ["CALL", null, ["callee:0054b19c:8"]]
- 00508b4c bytes 84090194
+ 00508b8c bytes 84090194
- 00508b58 ["INT_ADD", "register:40f0:8", ["const:508b58:8", "const:4:8"]]
- 00508b58 ["CALL", null, ["callee:0054b06c:8"]]
+ 00508b98 ["INT_ADD", "register:40f0:8", ["const:508b98:8", "const:4:8"]]
+ 00508b98 ["CALL", null, ["callee:0054b06c:8"]]
- 00508b58 bytes 35090194
+ 00508b98 bytes 35090194
- 00508b68 ["INT_ADD", "register:40f0:8", ["const:508b68:8", "const:4:8"]]
- 00508b68 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00508ba8 ["INT_ADD", "register:40f0:8", ["const:508ba8:8", "const:4:8"]]
+ 00508ba8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00508b68 bytes d23b1d94
+ 00508ba8 bytes c23c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2868e7ea11ba8e4a8efe22be360a3ac1"></a>

### [`00508cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508cc4.md) → [`00508d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508d04.md) FUN_00508d04

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00508ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508cc4.md#insn-00508ce0)
- 新版 `00508d20`（命令位置の公開資料なし）

~~~diff
- 00508ce0 ["INT_ADD", "register:40f0:8", ["const:508ce0:8", "const:4:8"]]
- 00508ce0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00508d20 ["INT_ADD", "register:40f0:8", ["const:508d20:8", "const:4:8"]]
+ 00508d20 ["CALL", null, ["callee:00c57eb0:8"]]
- 00508ce0 bytes 743b1d94
+ 00508d20 bytes 643c1d94
~~~


<a id="compare-a64f64e6aa6eda48c1c5ad16bc9bd025"></a>

### [`005090e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/005090e8.md) → [`00509128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509128.md) FUN_00509128

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00509104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/005090e8.md#insn-00509104)
- 新版 `00509144`（命令位置の公開資料なし）

~~~diff
- 00509104 ["INT_ADD", "register:40f0:8", ["const:509104:8", "const:4:8"]]
- 00509104 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00509144 ["INT_ADD", "register:40f0:8", ["const:509144:8", "const:4:8"]]
+ 00509144 ["CALL", null, ["callee:00c57eb0:8"]]
- 00509104 bytes 6b3a1d94
+ 00509144 bytes 5b3b1d94
~~~


<a id="compare-2600c4c3c141f6ccd152dd0e27217e49"></a>

### [`00509760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509760.md) → [`005097a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/005097a0.md) _ZN5BotanneERKNS_7X509_DNES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59610.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00509768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509760.md#insn-00509768)
- 新版 `005097a8`（命令位置の公開資料なし）

~~~diff
- 00509768 ["INT_ADD", "register:40f0:8", ["const:509768:8", "const:4:8"]]
- 00509768 ["CALL", null, ["callee:00c59a10:8"]]
+ 005097a8 ["INT_ADD", "register:40f0:8", ["const:5097a8:8", "const:4:8"]]
+ 005097a8 ["CALL", null, ["callee:00c59a10:8"]]
- 00509768 bytes aa3f1d94
+ 005097a8 bytes 9a401d94
~~~


<a id="compare-8f17df45d9de062b771df085cebaec71"></a>

### [`00509b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509b38.md) → [`00509b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509b78.md) _ZNK5Botan4OCSP7Request13base64_encodeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c587d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587d0.md) [`00c597b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c597b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58bd0.md) [`00c59bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59bb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00509b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509b38.md#insn-00509b5c) · [`00509b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509b38.md#insn-00509b6c) · [`00509b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509b38.md#insn-00509b7c)
- 新版 `00509b9c`（命令位置の公開資料なし） · `00509bac`（命令位置の公開資料なし） · `00509bbc`（命令位置の公開資料なし）

~~~diff
- 00509b5c ["INT_ADD", "register:40f0:8", ["const:509b5c:8", "const:4:8"]]
- 00509b5c ["CALL", null, ["callee:00c59bb0:8"]]
+ 00509b9c ["INT_ADD", "register:40f0:8", ["const:509b9c:8", "const:4:8"]]
+ 00509b9c ["CALL", null, ["callee:00c59bb0:8"]]
- 00509b5c bytes 153f1d94
+ 00509b9c bytes 05401d94
- 00509b6c ["INT_ADD", "register:40f0:8", ["const:509b6c:8", "const:4:8"]]
- 00509b6c ["CALL", null, ["callee:00c58bd0:8"]]
+ 00509bac ["INT_ADD", "register:40f0:8", ["const:509bac:8", "const:4:8"]]
+ 00509bac ["CALL", null, ["callee:00c58bd0:8"]]
- 00509b6c bytes 193b1d94
+ 00509bac bytes 093c1d94
- 00509b7c ["INT_ADD", "register:40f0:8", ["const:509b7c:8", "const:4:8"]]
- 00509b7c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00509bbc ["INT_ADD", "register:40f0:8", ["const:509bbc:8", "const:4:8"]]
+ 00509bbc ["CALL", null, ["callee:00c57eb0:8"]]
- 00509b7c bytes cd371d94
+ 00509bbc bytes bd381d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f0c305c7e6f5e141df2a49446bd8d9c"></a>

### [`0050b31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b31c.md) → [`0050b35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b35c.md) FUN_0050b35c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00510d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510d18.md) · 呼出先 2件 [`0053b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00510d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510d58.md) · 呼出先 2件 [`0053b424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b424.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050b338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b31c.md#insn-0050b338) · [`0050b370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b31c.md#insn-0050b370)
- 新版 `0050b378`（命令位置の公開資料なし） · `0050b3b0`（命令位置の公開資料なし）

~~~diff
- 0050b338 ["INT_ADD", "register:40f0:8", ["const:50b338:8", "const:4:8"]]
- 0050b338 ["CALL", null, ["callee:0053b424:8"]]
+ 0050b378 ["INT_ADD", "register:40f0:8", ["const:50b378:8", "const:4:8"]]
+ 0050b378 ["CALL", null, ["callee:0053b424:8"]]
- 0050b338 bytes 2bc00094
+ 0050b378 bytes 2bc00094
- 0050b370 ["INT_ADD", "register:40f0:8", ["const:50b370:8", "const:4:8"]]
- 0050b370 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0050b3b0 ["INT_ADD", "register:40f0:8", ["const:50b3b0:8", "const:4:8"]]
+ 0050b3b0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0050b370 bytes d0311d94
+ 0050b3b0 bytes c0321d94
~~~


<a id="compare-4a6473a9cd692b7b944d388abd03f5c1"></a>

### [`0050b3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b3a0.md) → [`0050b3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b3e0.md) FUN_0050b3e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005405fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005405fc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054063c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054063c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050b3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b3a0.md#insn-0050b3d8)
- 新版 `0050b418`（命令位置の公開資料なし）

~~~diff
- 0050b3d8 ["INT_ADD", "register:40f0:8", ["const:50b3d8:8", "const:4:8"]]
- 0050b3d8 ["CALL", null, ["callee:0054063c:8"]]
+ 0050b418 ["INT_ADD", "register:40f0:8", ["const:50b418:8", "const:4:8"]]
+ 0050b418 ["CALL", null, ["callee:0054063c:8"]]
- 0050b3d8 bytes 89d40094
+ 0050b418 bytes 89d40094
~~~


<a id="compare-2b23c5c6d437d2e96871e1b7df4a1739"></a>

### [`0050b40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b40c.md) → [`0050b44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b44c.md) FUN_0050b44c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050b44c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b40c.md#insn-0050b44c)
- 新版 `0050b48c`（命令位置の公開資料なし）

~~~diff
- 0050b44c ["COPY", "register:0:8", ["register:4040:8"]]
- 0050b44c ["INT_ADD", "register:40f0:8", ["const:50b44c:8", "const:4:8"]]
- 0050b44c ["CALLIND", null, ["register:0:8"]]
+ 0050b48c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050b48c ["INT_ADD", "register:40f0:8", ["const:50b48c:8", "const:4:8"]]
+ 0050b48c ["CALLIND", null, ["register:0:8"]]
- 0050b44c bytes 00013fd6
+ 0050b48c bytes 00013fd6
~~~


<a id="compare-6cb94b0b288fa5262c934a31ac6f6830"></a>

### [`0050bf98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050bf98.md) → [`0050bfd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050bfd8.md) _ZNK5Botan16X509_Certificate13allowed_usageENS_15Key_ConstraintsE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050bfac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050bf98.md#insn-0050bfac) · [`0050bfbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050bf98.md#insn-0050bfbc)
- 新版 `0050bfec`（命令位置の公開資料なし） · `0050bffc`（命令位置の公開資料なし）

~~~diff
- 0050bfac ["INT_ADD", "register:40f0:8", ["const:50bfac:8", "const:4:8"]]
- 0050bfac ["CALL", null, ["callee:00c599f0:8"]]
+ 0050bfec ["INT_ADD", "register:40f0:8", ["const:50bfec:8", "const:4:8"]]
+ 0050bfec ["CALL", null, ["callee:00c599f0:8"]]
- 0050bfac bytes 91351d94
+ 0050bfec bytes 81361d94
- 0050bfbc ["INT_ADD", "register:40f0:8", ["const:50bfbc:8", "const:4:8"]]
- 0050bfbc ["CALL", null, ["callee:00c599f0:8"]]
+ 0050bffc ["INT_ADD", "register:40f0:8", ["const:50bffc:8", "const:4:8"]]
+ 0050bffc ["CALL", null, ["callee:00c599f0:8"]]
- 0050bfbc bytes 8d351d94
+ 0050bffc bytes 7d361d94
~~~


<a id="compare-d6826adfeaac49d50c8473094677d617"></a>

### [`0050bfe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050bfe0.md) → [`0050c020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050c020.md) _ZNK5Botan16X509_Certificate22allowed_extended_usageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59840.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md) [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 1件 [`00c59c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c40.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050c008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050bfe0.md#insn-0050c008) · [`0050c010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050bfe0.md#insn-0050c010) · [`0050c084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050bfe0.md#insn-0050c084)
- 新版 `0050c048`（命令位置の公開資料なし） · `0050c050`（命令位置の公開資料なし） · `0050c0c4`（命令位置の公開資料なし）

~~~diff
- 0050c008 ["INT_ADD", "register:40f0:8", ["const:50c008:8", "const:4:8"]]
- 0050c008 ["CALL", null, ["callee:00c58680:8"]]
+ 0050c048 ["INT_ADD", "register:40f0:8", ["const:50c048:8", "const:4:8"]]
+ 0050c048 ["CALL", null, ["callee:00c58680:8"]]
- 0050c008 bytes 9e301d94
+ 0050c048 bytes 8e311d94
- 0050c010 ["INT_ADD", "register:40f0:8", ["const:50c010:8", "const:4:8"]]
- 0050c010 ["CALL", null, ["callee:00c599f0:8"]]
+ 0050c050 ["INT_ADD", "register:40f0:8", ["const:50c050:8", "const:4:8"]]
+ 0050c050 ["CALL", null, ["callee:00c599f0:8"]]
- 0050c010 bytes 78351d94
+ 0050c050 bytes 68361d94
- 0050c084 ["INT_ADD", "register:40f0:8", ["const:50c084:8", "const:4:8"]]
- 0050c084 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0050c0c4 ["INT_ADD", "register:40f0:8", ["const:50c0c4:8", "const:4:8"]]
+ 0050c0c4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0050c084 bytes 8b2e1d94
+ 0050c0c4 bytes 7b2f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab78842f9e2a7a866e43c4e0c986adc6"></a>

### [`0050cbcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050cbcc.md) → [`0050cc0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050cc0c.md) _ZNK5Botan16X509_Certificate13raw_issuer_dnEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050cbd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050cbcc.md#insn-0050cbd4)
- 新版 `0050cc14`（命令位置の公開資料なし）

~~~diff
- 0050cbd4 ["INT_ADD", "register:40f0:8", ["const:50cbd4:8", "const:4:8"]]
- 0050cbd4 ["CALL", null, ["callee:00c599f0:8"]]
+ 0050cc14 ["INT_ADD", "register:40f0:8", ["const:50cc14:8", "const:4:8"]]
+ 0050cc14 ["CALL", null, ["callee:00c599f0:8"]]
- 0050cbd4 bytes 87321d94
+ 0050cc14 bytes 77331d94
~~~


<a id="compare-27ffc8f0485947637b825042a428d138"></a>

### [`0050cbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050cbe4.md) → [`0050cc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050cc24.md) _ZNK5Botan4OCSP6CertID11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c582b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582b0.md) [`00c582d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582d0.md) [`00c58420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58420.md) [`00c58710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58710.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c586b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586b0.md) [`00c586d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586d0.md) [`00c58820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58820.md) [`00c58b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050cc04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050cbe4.md#insn-0050cc04) · [`0050cc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050cbe4.md#insn-0050cc18) · [`0050cc30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050cbe4.md#insn-0050cc30)
- 新版 `0050cc44`（命令位置の公開資料なし） · `0050cc58`（命令位置の公開資料なし） · `0050cc70`（命令位置の公開資料なし）

~~~diff
- 0050cc04 ["INT_ADD", "register:40f0:8", ["const:50cc04:8", "const:4:8"]]
- 0050cc04 ["CALL", null, ["callee:00c586b0:8"]]
+ 0050cc44 ["INT_ADD", "register:40f0:8", ["const:50cc44:8", "const:4:8"]]
+ 0050cc44 ["CALL", null, ["callee:00c586b0:8"]]
- 0050cc04 bytes ab2d1d94
+ 0050cc44 bytes 9b2e1d94
- 0050cc18 ["COPY", "register:0:8", ["register:4040:8"]]
- 0050cc18 ["INT_ADD", "register:40f0:8", ["const:50cc18:8", "const:4:8"]]
- 0050cc18 ["CALLIND", null, ["register:0:8"]]
+ 0050cc58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050cc58 ["INT_ADD", "register:40f0:8", ["const:50cc58:8", "const:4:8"]]
+ 0050cc58 ["CALLIND", null, ["register:0:8"]]
- 0050cc18 bytes 00013fd6
+ 0050cc58 bytes 00013fd6
- 0050cc30 ["INT_ADD", "register:40f0:8", ["const:50cc30:8", "const:4:8"]]
- 0050cc30 ["CALL", null, ["callee:00c58820:8"]]
+ 0050cc70 ["INT_ADD", "register:40f0:8", ["const:50cc70:8", "const:4:8"]]
+ 0050cc70 ["CALL", null, ["callee:00c58820:8"]]
- 0050cc30 bytes fc2d1d94
+ 0050cc70 bytes ec2e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfbdefcf773b2ecdf13b89c1c2df29b1"></a>

### [`0050dd10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050dd10.md) → [`0050dd50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050dd50.md) FUN_0050dd50

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050dd2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050dd10.md#insn-0050dd2c) · [`0050dd4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050dd10.md#insn-0050dd4c)
- 新版 `0050dd6c`（命令位置の公開資料なし） · `0050dd8c`（命令位置の公開資料なし）

~~~diff
- 0050dd2c ["INT_ADD", "register:40f0:8", ["const:50dd2c:8", "const:4:8"]]
- 0050dd2c ["CALL", null, ["callee:00c53d00:8"]]
+ 0050dd6c ["INT_ADD", "register:40f0:8", ["const:50dd6c:8", "const:4:8"]]
+ 0050dd6c ["CALL", null, ["callee:00c53d00:8"]]
- 0050dd2c bytes ed161d94
+ 0050dd6c bytes e5171d94
- 0050dd4c ["COPY", "register:0:8", ["register:4040:8"]]
- 0050dd4c ["INT_ADD", "register:40f0:8", ["const:50dd4c:8", "const:4:8"]]
- 0050dd4c ["CALLIND", null, ["register:0:8"]]
+ 0050dd8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050dd8c ["INT_ADD", "register:40f0:8", ["const:50dd8c:8", "const:4:8"]]
+ 0050dd8c ["CALLIND", null, ["register:0:8"]]
- 0050dd4c bytes 00013fd6
+ 0050dd8c bytes 00013fd6
~~~


<a id="compare-47ef71ec5901b32ce3be836ba836c093"></a>

### [`0050f02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f02c.md) → [`0050f06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f06c.md) FUN_0050f06c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0054a3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a3ec.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054a42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a42c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f02c.md#insn-0050f048)
- 新版 `0050f088`（命令位置の公開資料なし）

~~~diff
- 0050f048 ["INT_ADD", "register:40f0:8", ["const:50f048:8", "const:4:8"]]
- 0050f048 ["CALL", null, ["callee:0054a42c:8"]]
+ 0050f088 ["INT_ADD", "register:40f0:8", ["const:50f088:8", "const:4:8"]]
+ 0050f088 ["CALL", null, ["callee:0054a42c:8"]]
- 0050f048 bytes e9ec0094
+ 0050f088 bytes e9ec0094
~~~


<a id="compare-af102171b4e2eb0dde5f841c6801376c"></a>

### [`0050f164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f164.md) → [`0050f1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f1a4.md) _ZNK5Botan14PKCS10_Request18challenge_passwordEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c598c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c59cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59cc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f164.md#insn-0050f174)
- 新版 `0050f1b4`（命令位置の公開資料なし）

~~~diff
- 0050f174 ["INT_ADD", "register:40f0:8", ["const:50f174:8", "const:4:8"]]
- 0050f174 ["CALL", null, ["callee:00c59cc0:8"]]
+ 0050f1b4 ["INT_ADD", "register:40f0:8", ["const:50f1b4:8", "const:4:8"]]
+ 0050f1b4 ["CALL", null, ["callee:00c59cc0:8"]]
- 0050f174 bytes d3291d94
+ 0050f1b4 bytes c32a1d94
~~~


<a id="compare-76c67f4f226862b8754565f53076b9d9"></a>

### [`0050f1b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f1b8.md) → [`0050f1f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f1f8.md) _ZNK5Botan14PKCS10_Request14raw_public_keyEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c598c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598c0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59cc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f1b8.md#insn-0050f1c0)
- 新版 `0050f200`（命令位置の公開資料なし）

~~~diff
- 0050f1c0 ["INT_ADD", "register:40f0:8", ["const:50f1c0:8", "const:4:8"]]
- 0050f1c0 ["CALL", null, ["callee:00c59cc0:8"]]
+ 0050f200 ["INT_ADD", "register:40f0:8", ["const:50f200:8", "const:4:8"]]
+ 0050f200 ["CALL", null, ["callee:00c59cc0:8"]]
- 0050f1c0 bytes c0291d94
+ 0050f200 bytes b02a1d94
~~~


<a id="compare-d98f52ebe3d4599a7b78721a69d67397"></a>

### [`0050f1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f1d0.md) → [`0050f210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f210.md) _ZNK5Botan14PKCS10_Request16subject_alt_nameEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c598c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598c0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59cc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f1d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f1d0.md#insn-0050f1d8)
- 新版 `0050f218`（命令位置の公開資料なし）

~~~diff
- 0050f1d8 ["INT_ADD", "register:40f0:8", ["const:50f1d8:8", "const:4:8"]]
- 0050f1d8 ["CALL", null, ["callee:00c59cc0:8"]]
+ 0050f218 ["INT_ADD", "register:40f0:8", ["const:50f218:8", "const:4:8"]]
+ 0050f218 ["CALL", null, ["callee:00c59cc0:8"]]
- 0050f1d8 bytes ba291d94
+ 0050f218 bytes aa2a1d94
~~~


<a id="compare-0d3add773b104c95d317a147e22f5f63"></a>

### [`0050f1e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f1e8.md) → [`0050f228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f228.md) _ZNK5Botan14PKCS10_Request10extensionsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c598c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598c0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59cc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f1e8.md#insn-0050f1f0)
- 新版 `0050f230`（命令位置の公開資料なし）

~~~diff
- 0050f1f0 ["INT_ADD", "register:40f0:8", ["const:50f1f0:8", "const:4:8"]]
- 0050f1f0 ["CALL", null, ["callee:00c59cc0:8"]]
+ 0050f230 ["INT_ADD", "register:40f0:8", ["const:50f230:8", "const:4:8"]]
+ 0050f230 ["CALL", null, ["callee:00c59cc0:8"]]
- 0050f1f0 bytes b4291d94
+ 0050f230 bytes a42a1d94
~~~


<a id="compare-832d9061312d9bb9bcebdabc5c858389"></a>

### [`0050f378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f378.md) → [`0050f3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f3b8.md) _ZNK5Botan10Extensions3getERKNS_3OIDE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c596c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596c0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f378.md#insn-0050f388) · [`0050f398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f378.md#insn-0050f398)
- 新版 `0050f3c8`（命令位置の公開資料なし） · `0050f3d8`（命令位置の公開資料なし）

~~~diff
- 0050f388 ["INT_ADD", "register:40f0:8", ["const:50f388:8", "const:4:8"]]
- 0050f388 ["CALL", null, ["callee:00c59ac0:8"]]
+ 0050f3c8 ["INT_ADD", "register:40f0:8", ["const:50f3c8:8", "const:4:8"]]
+ 0050f3c8 ["CALL", null, ["callee:00c59ac0:8"]]
- 0050f388 bytes ce281d94
+ 0050f3c8 bytes be291d94
- 0050f398 ["COPY", "register:0:8", ["register:4040:8"]]
- 0050f398 ["INT_ADD", "register:40f0:8", ["const:50f398:8", "const:4:8"]]
- 0050f398 ["CALLIND", null, ["register:0:8"]]
+ 0050f3d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050f3d8 ["INT_ADD", "register:40f0:8", ["const:50f3d8:8", "const:4:8"]]
+ 0050f3d8 ["CALLIND", null, ["register:0:8"]]
- 0050f398 bytes 00013fd6
+ 0050f3d8 bytes 00013fd6
~~~


<a id="compare-078df50a0b00308e6c05eec86ff60d0b"></a>

### [`0050fed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fed0.md) → [`0050ff10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050ff10.md) _ZNK5Botan16X509_Certificate10is_CA_certEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050fed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fed0.md#insn-0050fed8)
- 新版 `0050ff18`（命令位置の公開資料なし）

~~~diff
- 0050fed8 ["INT_ADD", "register:40f0:8", ["const:50fed8:8", "const:4:8"]]
- 0050fed8 ["CALL", null, ["callee:00c599f0:8"]]
+ 0050ff18 ["INT_ADD", "register:40f0:8", ["const:50ff18:8", "const:4:8"]]
+ 0050ff18 ["CALL", null, ["callee:00c599f0:8"]]
- 0050fed8 bytes c6251d94
+ 0050ff18 bytes b6261d94
~~~


<a id="compare-55b548716580f242446724759beceda1"></a>

### [`0050fee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fee8.md) → [`0050ff28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050ff28.md) FUN_0050ff28

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0050fa08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fa08.md) · 呼出先 5件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 1件 [`0050fa48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050fa48.md) · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050ff0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fee8.md#insn-0050ff0c) · [`0050ff54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fee8.md#insn-0050ff54) · [`0050ff74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fee8.md#insn-0050ff74)
- 新版 `0050ff4c`（命令位置の公開資料なし） · `0050ff94`（命令位置の公開資料なし） · `0050ffb4`（命令位置の公開資料なし）

~~~diff
- 0050ff0c ["INT_ADD", "register:40f0:8", ["const:50ff0c:8", "const:4:8"]]
- 0050ff0c ["CALL", null, ["callee:00c57fe0:8"]]
+ 0050ff4c ["INT_ADD", "register:40f0:8", ["const:50ff4c:8", "const:4:8"]]
+ 0050ff4c ["CALL", null, ["callee:00c57fe0:8"]]
- 0050ff0c bytes 351f1d94
+ 0050ff4c bytes 25201d94
- 0050ff54 ["INT_ADD", "register:40f0:8", ["const:50ff54:8", "const:4:8"]]
- 0050ff54 ["CALL", null, ["callee:00c57e90:8"]]
+ 0050ff94 ["INT_ADD", "register:40f0:8", ["const:50ff94:8", "const:4:8"]]
+ 0050ff94 ["CALL", null, ["callee:00c57e90:8"]]
- 0050ff54 bytes cf1e1d94
+ 0050ff94 bytes bf1f1d94
- 0050ff74 ["INT_ADD", "register:40f0:8", ["const:50ff74:8", "const:4:8"]]
- 0050ff74 ["CALL", null, ["callee:00c57f40:8"]]
+ 0050ffb4 ["INT_ADD", "register:40f0:8", ["const:50ffb4:8", "const:4:8"]]
+ 0050ffb4 ["CALL", null, ["callee:00c57f40:8"]]
- 0050ff74 bytes f31e1d94
+ 0050ffb4 bytes e31f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-beacb1a7f58b15164e6c94a7f72675b6"></a>

### [`0050ffdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050ffdc.md) → [`0051001c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/0051001c.md) FUN_0051001c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`006144ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00614/006144ec.md) [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) [`0073d764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073d/0073d764.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 9件 [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`0061452c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00614/0061452c.md) [`0064ecb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064ecb8.md) [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) [`0073d7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073d/0073d7a4.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050fff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050ffdc.md#insn-0050fff8)
- 新版 `00510038`（命令位置の公開資料なし）

~~~diff
- 0050fff8 ["INT_ADD", "register:40f0:8", ["const:50fff8:8", "const:4:8"]]
- 0050fff8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00510038 ["INT_ADD", "register:40f0:8", ["const:510038:8", "const:4:8"]]
+ 00510038 ["CALL", null, ["callee:00c57eb0:8"]]
- 0050fff8 bytes ae1e1d94
+ 00510038 bytes 9e1f1d94
~~~


<a id="compare-423252403f7f012b6beb661c28afdaa2"></a>

### [`005115f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/005115f8.md) → [`00511638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511638.md) FUN_00511638

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00510d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510d18.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00510d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510d58.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00511640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/005115f8.md#insn-00511640)
- 新版 `00511680`（命令位置の公開資料なし）

~~~diff
- 00511640 ["INT_ADD", "register:40f0:8", ["const:511640:8", "const:4:8"]]
- 00511640 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00511680 ["INT_ADD", "register:40f0:8", ["const:511680:8", "const:4:8"]]
+ 00511680 ["CALL", null, ["callee:00c57eb0:8"]]
- 00511640 bytes 1c191d94
+ 00511680 bytes 0c1a1d94
~~~


<a id="compare-ee8ad359723aab44d846d70fa9fe7788"></a>

### [`00511c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511c84.md) → [`00511cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511cc4.md) _ZNK5Botan7X509_CA7new_crlERNS_21RandomNumberGeneratorEj

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58180.md) [`00c59970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59970.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58580.md) [`00c59d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00511cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511c84.md#insn-00511cb8) · [`00511ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511c84.md#insn-00511ce0) · [`00511d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511c84.md#insn-00511d30)
- 新版 `00511cf8`（命令位置の公開資料なし） · `00511d20`（命令位置の公開資料なし） · `00511d70`（命令位置の公開資料なし）

~~~diff
- 00511cb8 ["INT_ADD", "register:40f0:8", ["const:511cb8:8", "const:4:8"]]
- 00511cb8 ["CALL", null, ["callee:00c58580:8"]]
+ 00511cf8 ["INT_ADD", "register:40f0:8", ["const:511cf8:8", "const:4:8"]]
+ 00511cf8 ["CALL", null, ["callee:00c58580:8"]]
- 00511cb8 bytes 32191d94
+ 00511cf8 bytes 221a1d94
- 00511ce0 ["INT_ADD", "register:40f0:8", ["const:511ce0:8", "const:4:8"]]
- 00511ce0 ["CALL", null, ["callee:00c59d70:8"]]
+ 00511d20 ["INT_ADD", "register:40f0:8", ["const:511d20:8", "const:4:8"]]
+ 00511d20 ["CALL", null, ["callee:00c59d70:8"]]
- 00511ce0 bytes 241f1d94
+ 00511d20 bytes 14201d94
- 00511d30 ["INT_ADD", "register:40f0:8", ["const:511d30:8", "const:4:8"]]
- 00511d30 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00511d70 ["INT_ADD", "register:40f0:8", ["const:511d70:8", "const:4:8"]]
+ 00511d70 ["CALL", null, ["callee:00c57ee0:8"]]
- 00511d30 bytes 6c171d94
+ 00511d70 bytes 5c181d94
~~~


<a id="compare-9c241ccd7862d220d3c0eba730f2667f"></a>

### [`00511d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511d34.md) → [`00511d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511d74.md) _ZNK5Botan7X509_CA7new_crlERNS_21RandomNumberGeneratorENSt6__ndk16chrono10time_pointINS4_12system_clockENS4_8durationIxNS3_5ratioILl1ELl1000

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59970.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00511d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511d34.md#insn-00511d6c) · [`00511db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511d34.md#insn-00511db8)
- 新版 `00511dac`（命令位置の公開資料なし） · `00511df8`（命令位置の公開資料なし）

~~~diff
- 00511d6c ["INT_ADD", "register:40f0:8", ["const:511d6c:8", "const:4:8"]]
- 00511d6c ["CALL", null, ["callee:00c59d70:8"]]
+ 00511dac ["INT_ADD", "register:40f0:8", ["const:511dac:8", "const:4:8"]]
+ 00511dac ["CALL", null, ["callee:00c59d70:8"]]
- 00511d6c bytes 011f1d94
+ 00511dac bytes f11f1d94
- 00511db8 ["INT_ADD", "register:40f0:8", ["const:511db8:8", "const:4:8"]]
- 00511db8 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00511df8 ["INT_ADD", "register:40f0:8", ["const:511df8:8", "const:4:8"]]
+ 00511df8 ["CALL", null, ["callee:00c57ee0:8"]]
- 00511db8 bytes 4a171d94
+ 00511df8 bytes 3a181d94
~~~


<a id="compare-ca0600c033f34df5dcc7234a0f952da6"></a>

### [`00511dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511dbc.md) → [`00511dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511dfc.md) _ZNK5Botan7X509_CA10update_crlERKNS_8X509_CRLERKNSt6__ndk16vectorINS_9CRL_EntryENS4_9allocatorIS6_EEEERNS_21RandomNumberGeneratorEj

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58180.md) [`00c59980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59980.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58580.md) [`00c59d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59d80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00511de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511dbc.md#insn-00511de8)
- 新版 `00511e28`（命令位置の公開資料なし）

~~~diff
- 00511de8 ["INT_ADD", "register:40f0:8", ["const:511de8:8", "const:4:8"]]
- 00511de8 ["CALL", null, ["callee:00c58580:8"]]
+ 00511e28 ["INT_ADD", "register:40f0:8", ["const:511e28:8", "const:4:8"]]
+ 00511e28 ["CALL", null, ["callee:00c58580:8"]]
- 00511de8 bytes e6181d94
+ 00511e28 bytes d6191d94
~~~


<a id="compare-af3fb0982e2aea6233cb0129dc071872"></a>

### [`00512650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512650.md) → [`00512690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512690.md) FUN_00512690

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051269c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512650.md#insn-0051269c) · [`005126b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512650.md#insn-005126b0) · [`005126b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512650.md#insn-005126b8)
- 新版 `005126dc`（命令位置の公開資料なし） · `005126f0`（命令位置の公開資料なし） · `005126f8`（命令位置の公開資料なし）

~~~diff
- 0051269c ["INT_ADD", "register:40f0:8", ["const:51269c:8", "const:4:8"]]
- 0051269c ["CALL", null, ["callee:00c53d00:8"]]
+ 005126dc ["INT_ADD", "register:40f0:8", ["const:5126dc:8", "const:4:8"]]
+ 005126dc ["CALL", null, ["callee:00c53d00:8"]]
- 0051269c bytes 91041d94
+ 005126dc bytes 89051d94
- 005126b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005126b0 ["INT_ADD", "register:40f0:8", ["const:5126b0:8", "const:4:8"]]
- 005126b0 ["CALLIND", null, ["register:0:8"]]
+ 005126f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005126f0 ["INT_ADD", "register:40f0:8", ["const:5126f0:8", "const:4:8"]]
+ 005126f0 ["CALLIND", null, ["register:0:8"]]
- 005126b0 bytes 00013fd6
+ 005126f0 bytes 00013fd6
- 005126b8 ["INT_ADD", "register:40f0:8", ["const:5126b8:8", "const:4:8"]]
- 005126b8 ["CALL", null, ["callee:00c57e80:8"]]
+ 005126f8 ["INT_ADD", "register:40f0:8", ["const:5126f8:8", "const:4:8"]]
+ 005126f8 ["CALL", null, ["callee:00c57e80:8"]]
- 005126b8 bytes f2141d94
+ 005126f8 bytes e2151d94
~~~


<a id="compare-2ee7149b753e449ff489c0e526d9ec66"></a>

### [`005126e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/005126e8.md) → [`00512728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512728.md) _ZNK5Botan8X509_CRL11get_revokedEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59650.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005126f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/005126e8.md#insn-005126f0)
- 新版 `00512730`（命令位置の公開資料なし）

~~~diff
- 005126f0 ["INT_ADD", "register:40f0:8", ["const:5126f0:8", "const:4:8"]]
- 005126f0 ["CALL", null, ["callee:00c59a50:8"]]
+ 00512730 ["INT_ADD", "register:40f0:8", ["const:512730:8", "const:4:8"]]
+ 00512730 ["CALL", null, ["callee:00c59a50:8"]]
- 005126f0 bytes d81b1d94
+ 00512730 bytes c81c1d94
~~~


<a id="compare-be9a764c623b774d410d776508aaff34"></a>

### [`00512700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512700.md) → [`00512740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512740.md) _ZNK5Botan8X509_CRL10crl_numberEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59650.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00512708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512700.md#insn-00512708)
- 新版 `00512748`（命令位置の公開資料なし）

~~~diff
- 00512708 ["INT_ADD", "register:40f0:8", ["const:512708:8", "const:4:8"]]
- 00512708 ["CALL", null, ["callee:00c59a50:8"]]
+ 00512748 ["INT_ADD", "register:40f0:8", ["const:512748:8", "const:4:8"]]
+ 00512748 ["CALL", null, ["callee:00c59a50:8"]]
- 00512708 bytes d21b1d94
+ 00512748 bytes c21c1d94
~~~


<a id="compare-af1d0357367bd91635b26176724c5551"></a>

### [`0051276c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/0051276c.md) → [`005127ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/005127ac.md) _ZN5Botan17choose_sig_formatERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS5_11char_traitsIcEENS5_9allocatorI

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00510020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510020.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00510060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510060.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005127a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/0051276c.md#insn-005127a8) · [`005127b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/0051276c.md#insn-005127b8) · [`00512808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/0051276c.md#insn-00512808)
- 新版 `005127e8`（命令位置の公開資料なし） · `005127f8`（命令位置の公開資料なし） · `00512848`（命令位置の公開資料なし）

~~~diff
- 005127a8 ["INT_ADD", "register:40f0:8", ["const:5127a8:8", "const:4:8"]]
- 005127a8 ["CALL", null, ["callee:00510060:8"]]
+ 005127e8 ["INT_ADD", "register:40f0:8", ["const:5127e8:8", "const:4:8"]]
+ 005127e8 ["CALL", null, ["callee:00510060:8"]]
- 005127a8 bytes 1ef6ff97
+ 005127e8 bytes 1ef6ff97
- 005127b8 ["INT_ADD", "register:40f0:8", ["const:5127b8:8", "const:4:8"]]
- 005127b8 ["CALL", null, ["callee:0046d490:8"]]
+ 005127f8 ["INT_ADD", "register:40f0:8", ["const:5127f8:8", "const:4:8"]]
+ 005127f8 ["CALL", null, ["callee:0046d490:8"]]
- 005127b8 bytes 266bfd97
+ 005127f8 bytes 266bfd97
- 00512808 ["INT_ADD", "register:40f0:8", ["const:512808:8", "const:4:8"]]
- 00512808 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00512848 ["INT_ADD", "register:40f0:8", ["const:512848:8", "const:4:8"]]
+ 00512848 ["CALL", null, ["callee:00c57ee0:8"]]
- 00512808 bytes b6141d94
+ 00512848 bytes a6151d94
~~~


<a id="compare-182fc026342d637c6aba42ccc945fd34"></a>

### [`005129d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/005129d4.md) → [`00512a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512a14.md) FUN_00512a14

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005129f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/005129d4.md#insn-005129f0) · [`00512a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/005129d4.md#insn-00512a10)
- 新版 `00512a30`（命令位置の公開資料なし） · `00512a50`（命令位置の公開資料なし）

~~~diff
- 005129f0 ["INT_ADD", "register:40f0:8", ["const:5129f0:8", "const:4:8"]]
- 005129f0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00512a30 ["INT_ADD", "register:40f0:8", ["const:512a30:8", "const:4:8"]]
+ 00512a30 ["CALL", null, ["callee:00c53d00:8"]]
- 005129f0 bytes bc031d94
+ 00512a30 bytes b4041d94
- 00512a10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00512a10 ["INT_ADD", "register:40f0:8", ["const:512a10:8", "const:4:8"]]
- 00512a10 ["CALLIND", null, ["register:0:8"]]
+ 00512a50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00512a50 ["INT_ADD", "register:40f0:8", ["const:512a50:8", "const:4:8"]]
+ 00512a50 ["CALLIND", null, ["register:0:8"]]
- 00512a10 bytes 00013fd6
+ 00512a50 bytes 00013fd6
~~~


<a id="compare-fd8f688e5dc6c18fba1bb6be66829319"></a>

### [`00512f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512f48.md) → [`00512f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512f88.md) _ZNK5Botan8X509_CRL10is_revokedERKNS_16X509_CertificateE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c599a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599a0.md) · 呼出先 10件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c59da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59da0.md) · 呼出先 10件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00512f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512f48.md#insn-00512f80) · [`00512f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512f48.md#insn-00512f8c) · [`00512f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512f48.md#insn-00512f98)
- 新版 `00512fc0`（命令位置の公開資料なし） · `00512fcc`（命令位置の公開資料なし） · `00512fd8`（命令位置の公開資料なし）

~~~diff
- 00512f80 ["INT_ADD", "register:40f0:8", ["const:512f80:8", "const:4:8"]]
- 00512f80 ["CALL", null, ["callee:00c599f0:8"]]
+ 00512fc0 ["INT_ADD", "register:40f0:8", ["const:512fc0:8", "const:4:8"]]
+ 00512fc0 ["CALL", null, ["callee:00c599f0:8"]]
- 00512f80 bytes 9c191d94
+ 00512fc0 bytes 8c1a1d94
- 00512f8c ["INT_ADD", "register:40f0:8", ["const:512f8c:8", "const:4:8"]]
- 00512f8c ["CALL", null, ["callee:00c59a50:8"]]
+ 00512fcc ["INT_ADD", "register:40f0:8", ["const:512fcc:8", "const:4:8"]]
+ 00512fcc ["CALL", null, ["callee:00c59a50:8"]]
- 00512f8c bytes b1191d94
+ 00512fcc bytes a11a1d94
- 00512f98 ["INT_ADD", "register:40f0:8", ["const:512f98:8", "const:4:8"]]
- 00512f98 ["CALL", null, ["callee:00c59a10:8"]]
+ 00512fd8 ["INT_ADD", "register:40f0:8", ["const:512fd8:8", "const:4:8"]]
+ 00512fd8 ["CALL", null, ["callee:00c59a10:8"]]
- 00512f98 bytes 9e191d94
+ 00512fd8 bytes 8e1a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c0e9b49ba941c6ca038c9710fbb2e4f"></a>

### [`00513dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513dd4.md) → [`00513e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/00513e14.md) FUN_00513e14

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0054aa0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054aa0c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054aa4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054aa4c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00513df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513dd4.md#insn-00513df0)
- 新版 `00513e30`（命令位置の公開資料なし）

~~~diff
- 00513df0 ["INT_ADD", "register:40f0:8", ["const:513df0:8", "const:4:8"]]
- 00513df0 ["CALL", null, ["callee:0054aa4c:8"]]
+ 00513e30 ["INT_ADD", "register:40f0:8", ["const:513e30:8", "const:4:8"]]
+ 00513e30 ["CALL", null, ["callee:0054aa4c:8"]]
- 00513df0 bytes 07db0094
+ 00513e30 bytes 07db0094
~~~


<a id="compare-74e2160ac00ff46e48c500bcc605f866"></a>

### [`00513f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513f0c.md) → [`00513f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/00513f4c.md) _ZNK5Botan8X509_CRL10extensionsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59650.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00513f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513f0c.md#insn-00513f14)
- 新版 `00513f54`（命令位置の公開資料なし）

~~~diff
- 00513f14 ["INT_ADD", "register:40f0:8", ["const:513f14:8", "const:4:8"]]
- 00513f14 ["CALL", null, ["callee:00c59a50:8"]]
+ 00513f54 ["INT_ADD", "register:40f0:8", ["const:513f54:8", "const:4:8"]]
+ 00513f54 ["CALL", null, ["callee:00c59a50:8"]]
- 00513f14 bytes cf151d94
+ 00513f54 bytes bf161d94
~~~


<a id="compare-abaf37203888d8d680b739e4d68ea17c"></a>

### [`00513f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513f24.md) → [`00513f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/00513f64.md) _ZNK5Botan8X509_CRL11next_updateEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59650.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00513f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513f24.md#insn-00513f2c)
- 新版 `00513f6c`（命令位置の公開資料なし）

~~~diff
- 00513f2c ["INT_ADD", "register:40f0:8", ["const:513f2c:8", "const:4:8"]]
- 00513f2c ["CALL", null, ["callee:00c59a50:8"]]
+ 00513f6c ["INT_ADD", "register:40f0:8", ["const:513f6c:8", "const:4:8"]]
+ 00513f6c ["CALL", null, ["callee:00c59a50:8"]]
- 00513f2c bytes c9151d94
+ 00513f6c bytes b9161d94
~~~


<a id="compare-83af0a78dfb11a37c14739ffb2cff732"></a>

### [`00513f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513f3c.md) → [`00513f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/00513f7c.md) _ZNK5Botan8X509_CRL30crl_issuing_distribution_pointEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c59650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59650.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c59a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00513f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513f3c.md#insn-00513f4c)
- 新版 `00513f8c`（命令位置の公開資料なし）

~~~diff
- 00513f4c ["INT_ADD", "register:40f0:8", ["const:513f4c:8", "const:4:8"]]
- 00513f4c ["CALL", null, ["callee:00c59a50:8"]]
+ 00513f8c ["INT_ADD", "register:40f0:8", ["const:513f8c:8", "const:4:8"]]
+ 00513f8c ["CALL", null, ["callee:00c59a50:8"]]
- 00513f4c bytes c1151d94
+ 00513f8c bytes b1161d94
~~~


<a id="compare-b08642baa3d1c7702ad31e17769df2b9"></a>

### [`00514078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514078.md) → [`005140b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/005140b8.md) _ZN5Botan7X509_DN13add_attributeERKNS_3OIDERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59700.md) · 呼出先 6件 [`004ff33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff33c.md) [`0054ae6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054ae6c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c59b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b00.md) · 呼出先 6件 [`004ff37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff37c.md) [`0054aeac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054aeac.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005140c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514078.md#insn-005140c8) · [`0051415c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514078.md#insn-0051415c) · [`0051419c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514078.md#insn-0051419c)
- 新版 `00514108`（命令位置の公開資料なし） · `0051419c`（命令位置の公開資料なし） · `005141dc`（命令位置の公開資料なし）

~~~diff
- 005140c8 ["INT_ADD", "register:40f0:8", ["const:5140c8:8", "const:4:8"]]
- 005140c8 ["CALL", null, ["callee:0054aeac:8"]]
+ 00514108 ["INT_ADD", "register:40f0:8", ["const:514108:8", "const:4:8"]]
+ 00514108 ["CALL", null, ["callee:0054aeac:8"]]
- 005140c8 bytes 69db0094
+ 00514108 bytes 69db0094
- 0051415c ["INT_ADD", "register:40f0:8", ["const:51415c:8", "const:4:8"]]
- 0051415c ["CALL", null, ["callee:00c58050:8"]]
+ 0051419c ["INT_ADD", "register:40f0:8", ["const:51419c:8", "const:4:8"]]
+ 0051419c ["CALL", null, ["callee:00c58050:8"]]
- 0051415c bytes bd0e1d94
+ 0051419c bytes ad0f1d94
- 0051419c ["INT_ADD", "register:40f0:8", ["const:51419c:8", "const:4:8"]]
- 0051419c ["CALL", null, ["callee:00c588f0:8"]]
+ 005141dc ["INT_ADD", "register:40f0:8", ["const:5141dc:8", "const:4:8"]]
+ 005141dc ["CALL", null, ["callee:00c588f0:8"]]
- 0051419c bytes d5101d94
+ 005141dc bytes c5111d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57eddd1004b31903431ef82615e696e2"></a>

### [`0051438c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/0051438c.md) → [`005143cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/005143cc.md) _ZNK5Botan7X509_DN8contentsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c595b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595b0.md) · 呼出先 5件 [`004ff160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58400.md) [`00c584b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c584b0.md)
- 新版 呼出元 1件 [`00c599b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599b0.md) · 呼出先 5件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58800.md) [`00c588b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c588b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00514408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/0051438c.md#insn-00514408) · [`0051442c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/0051438c.md#insn-0051442c) · [`0051443c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/0051438c.md#insn-0051443c)
- 新版 `00514448`（命令位置の公開資料なし） · `0051446c`（命令位置の公開資料なし） · `0051447c`（命令位置の公開資料なし）

~~~diff
- 00514408 ["INT_ADD", "register:40f0:8", ["const:514408:8", "const:4:8"]]
- 00514408 ["CALL", null, ["callee:00c588b0:8"]]
+ 00514448 ["INT_ADD", "register:40f0:8", ["const:514448:8", "const:4:8"]]
+ 00514448 ["CALL", null, ["callee:00c588b0:8"]]
- 00514408 bytes 2a101d94
+ 00514448 bytes 1a111d94
- 0051442c ["INT_ADD", "register:40f0:8", ["const:51442c:8", "const:4:8"]]
- 0051442c ["CALL", null, ["callee:00c58800:8"]]
+ 0051446c ["INT_ADD", "register:40f0:8", ["const:51446c:8", "const:4:8"]]
+ 0051446c ["CALL", null, ["callee:00c58800:8"]]
- 0051442c bytes f50f1d94
+ 0051446c bytes e5101d94
- 0051443c ["INT_ADD", "register:40f0:8", ["const:51443c:8", "const:4:8"]]
- 0051443c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0051447c ["INT_ADD", "register:40f0:8", ["const:51447c:8", "const:4:8"]]
+ 0051447c ["CALL", null, ["callee:00c57eb0:8"]]
- 0051443c bytes 9d0d1d94
+ 0051447c bytes 8d0e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-daeb650825a83ce0a2b77ef1cd7f7ae5"></a>

### [`005144e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/005144e8.md) → [`00514528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514528.md) _ZNK5Botan7X509_DN9has_fieldERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c599c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599c0.md) · 呼出先 5件 [`0054b234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b234.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md) [`00c59770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59770.md)
- 新版 呼出元 1件 [`00c59dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dc0.md) · 呼出先 5件 [`0054b274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b274.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md) [`00c59b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00514514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/005144e8.md#insn-00514514) · [`00514520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/005144e8.md#insn-00514520) · [`00514530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/005144e8.md#insn-00514530)
- 新版 `00514554`（命令位置の公開資料なし） · `00514560`（命令位置の公開資料なし） · `00514570`（命令位置の公開資料なし）

~~~diff
- 00514514 ["INT_ADD", "register:40f0:8", ["const:514514:8", "const:4:8"]]
- 00514514 ["CALL", null, ["callee:00c59b70:8"]]
+ 00514554 ["INT_ADD", "register:40f0:8", ["const:514554:8", "const:4:8"]]
+ 00514554 ["CALL", null, ["callee:00c59b70:8"]]
- 00514514 bytes 97141d94
+ 00514554 bytes 87151d94
- 00514520 ["INT_ADD", "register:40f0:8", ["const:514520:8", "const:4:8"]]
- 00514520 ["CALL", null, ["callee:00c58680:8"]]
+ 00514560 ["INT_ADD", "register:40f0:8", ["const:514560:8", "const:4:8"]]
+ 00514560 ["CALL", null, ["callee:00c58680:8"]]
- 00514520 bytes 580f1d94
+ 00514560 bytes 48101d94
- 00514530 ["INT_ADD", "register:40f0:8", ["const:514530:8", "const:4:8"]]
- 00514530 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00514570 ["INT_ADD", "register:40f0:8", ["const:514570:8", "const:4:8"]]
+ 00514570 ["CALL", null, ["callee:00c57eb0:8"]]
- 00514530 bytes 600d1d94
+ 00514570 bytes 500e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd179dcac16e044d3eef4d73ddbaa902"></a>

### [`00514904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514904.md) → [`00514944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514944.md) _ZNK5Botan7X509_DN19get_first_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md) [`00c59770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59770.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md) [`00c59b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00514934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514904.md#insn-00514934) · [`00514940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514904.md#insn-00514940) · [`00514950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514904.md#insn-00514950)
- 新版 `00514974`（命令位置の公開資料なし） · `00514980`（命令位置の公開資料なし） · `00514990`（命令位置の公開資料なし）

~~~diff
- 00514934 ["INT_ADD", "register:40f0:8", ["const:514934:8", "const:4:8"]]
- 00514934 ["CALL", null, ["callee:00c59b70:8"]]
+ 00514974 ["INT_ADD", "register:40f0:8", ["const:514974:8", "const:4:8"]]
+ 00514974 ["CALL", null, ["callee:00c59b70:8"]]
- 00514934 bytes 8f131d94
+ 00514974 bytes 7f141d94
- 00514940 ["INT_ADD", "register:40f0:8", ["const:514940:8", "const:4:8"]]
- 00514940 ["CALL", null, ["callee:00c58680:8"]]
+ 00514980 ["INT_ADD", "register:40f0:8", ["const:514980:8", "const:4:8"]]
+ 00514980 ["CALL", null, ["callee:00c58680:8"]]
- 00514940 bytes 500e1d94
+ 00514980 bytes 400f1d94
- 00514950 ["INT_ADD", "register:40f0:8", ["const:514950:8", "const:4:8"]]
- 00514950 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00514990 ["INT_ADD", "register:40f0:8", ["const:514990:8", "const:4:8"]]
+ 00514990 ["CALL", null, ["callee:00c57eb0:8"]]
- 00514950 bytes 580c1d94
+ 00514990 bytes 480d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b12fe00a630151f803faa55053bc271e"></a>

### [`00514ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514ac8.md) → [`00514b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514b08.md) _ZN5BotanltERKNS_7X509_DNES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00549628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549628.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c59620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59620.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00549668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549668.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c59a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00514afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514ac8.md#insn-00514afc) · [`00514b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514ac8.md#insn-00514b08) · [`00514c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514ac8.md#insn-00514c64)
- 新版 `00514b3c`（命令位置の公開資料なし） · `00514b48`（命令位置の公開資料なし） · `00514ca4`（命令位置の公開資料なし）

~~~diff
- 00514afc ["INT_ADD", "register:40f0:8", ["const:514afc:8", "const:4:8"]]
- 00514afc ["CALL", null, ["callee:00c59a20:8"]]
+ 00514b3c ["INT_ADD", "register:40f0:8", ["const:514b3c:8", "const:4:8"]]
+ 00514b3c ["CALL", null, ["callee:00c59a20:8"]]
- 00514afc bytes c9121d94
+ 00514b3c bytes b9131d94
- 00514b08 ["INT_ADD", "register:40f0:8", ["const:514b08:8", "const:4:8"]]
- 00514b08 ["CALL", null, ["callee:00c59a20:8"]]
+ 00514b48 ["INT_ADD", "register:40f0:8", ["const:514b48:8", "const:4:8"]]
+ 00514b48 ["CALL", null, ["callee:00c59a20:8"]]
- 00514b08 bytes c6121d94
+ 00514b48 bytes b6131d94
- 00514c64 ["INT_ADD", "register:40f0:8", ["const:514c64:8", "const:4:8"]]
- 00514c64 ["CALL", null, ["callee:00c58050:8"]]
+ 00514ca4 ["INT_ADD", "register:40f0:8", ["const:514ca4:8", "const:4:8"]]
+ 00514ca4 ["CALL", null, ["callee:00c58050:8"]]
- 00514c64 bytes fb0b1d94
+ 00514ca4 bytes eb0c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-002b36bcca85fda97be8368271d41202"></a>

### [`005150c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/005150c0.md) → [`00515100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/00515100.md) FUN_00515100

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00514d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514d64.md) · 呼出先 7件 [`0053d36c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d36c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md) [`00c582b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582b0.md)
- 新版 呼出元 1件 [`00514da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514da4.md) · 呼出先 7件 [`0053d3ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d3ac.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md) [`00c586b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005150f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/005150c0.md#insn-005150f8) · [`005151d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/005150c0.md#insn-005151d8) · [`005151f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/005150c0.md#insn-005151f8)
- 新版 `00515138`（命令位置の公開資料なし） · `00515218`（命令位置の公開資料なし） · `00515238`（命令位置の公開資料なし）

~~~diff
- 005150f8 ["INT_ADD", "register:40f0:8", ["const:5150f8:8", "const:4:8"]]
- 005150f8 ["CALL", null, ["callee:00c58680:8"]]
+ 00515138 ["INT_ADD", "register:40f0:8", ["const:515138:8", "const:4:8"]]
+ 00515138 ["CALL", null, ["callee:00c58680:8"]]
- 005150f8 bytes 620c1d94
+ 00515138 bytes 520d1d94
- 005151d8 ["INT_ADD", "register:40f0:8", ["const:5151d8:8", "const:4:8"]]
- 005151d8 ["CALL", null, ["callee:0053d3ac:8"]]
+ 00515218 ["INT_ADD", "register:40f0:8", ["const:515218:8", "const:4:8"]]
+ 00515218 ["CALL", null, ["callee:0053d3ac:8"]]
- 005151d8 bytes 65a00094
+ 00515218 bytes 65a00094
- 005151f8 ["INT_ADD", "register:40f0:8", ["const:5151f8:8", "const:4:8"]]
- 005151f8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00515238 ["INT_ADD", "register:40f0:8", ["const:515238:8", "const:4:8"]]
+ 00515238 ["CALL", null, ["callee:00c57eb0:8"]]
- 005151f8 bytes 2e0a1d94
+ 00515238 bytes 1e0b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad6f10044ad2ddc5aabb538b3d72e4f6"></a>

### [`00515330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515330.md) → [`00515370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/00515370.md) FUN_00515370

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005086e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/005086e8.md) · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 1件 [`00508728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508728.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00515364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515330.md#insn-00515364) · [`005153a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515330.md#insn-005153a4) · [`005153cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515330.md#insn-005153cc)
- 新版 `005153a4`（命令位置の公開資料なし） · `005153e4`（命令位置の公開資料なし） · `0051540c`（命令位置の公開資料なし）

~~~diff
- 00515364 ["INT_ADD", "register:40f0:8", ["const:515364:8", "const:4:8"]]
- 00515364 ["CALL", null, ["callee:00c59dd0:8"]]
+ 005153a4 ["INT_ADD", "register:40f0:8", ["const:5153a4:8", "const:4:8"]]
+ 005153a4 ["CALL", null, ["callee:00c59dd0:8"]]
- 00515364 bytes 9b111d94
+ 005153a4 bytes 8b121d94
- 005153a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005153a4 ["INT_ADD", "register:40f0:8", ["const:5153a4:8", "const:4:8"]]
- 005153a4 ["CALLIND", null, ["register:0:8"]]
+ 005153e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005153e4 ["INT_ADD", "register:40f0:8", ["const:5153e4:8", "const:4:8"]]
+ 005153e4 ["CALLIND", null, ["register:0:8"]]
- 005153a4 bytes 00013fd6
+ 005153e4 bytes 00013fd6
- 005153cc ["INT_ADD", "register:40f0:8", ["const:5153cc:8", "const:4:8"]]
- 005153cc ["CALL", null, ["callee:00c582a0:8"]]
+ 0051540c ["INT_ADD", "register:40f0:8", ["const:51540c:8", "const:4:8"]]
+ 0051540c ["CALL", null, ["callee:00c582a0:8"]]
- 005153cc bytes b50a1d94
+ 0051540c bytes a50b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e738ca3d2b41c6fdac3753082fb83e52"></a>

### [`00515474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515474.md) → [`005154b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005154b4.md) FUN_005154b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0054f3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f3f0.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0054b3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b3f4.md) [`0054b790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b790.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0054f430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054f/0054f430.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0054b434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b434.md) [`0054b7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b7d0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005154c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515474.md#insn-005154c4) · [`005154f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515474.md#insn-005154f4) · [`00515510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515474.md#insn-00515510)
- 新版 `00515504`（命令位置の公開資料なし） · `00515534`（命令位置の公開資料なし） · `00515550`（命令位置の公開資料なし）

~~~diff
- 005154c4 ["INT_ADD", "register:40f0:8", ["const:5154c4:8", "const:4:8"]]
- 005154c4 ["CALL", null, ["callee:0043bba4:8"]]
+ 00515504 ["INT_ADD", "register:40f0:8", ["const:515504:8", "const:4:8"]]
+ 00515504 ["CALL", null, ["callee:0043bba4:8"]]
- 005154c4 bytes a899fc97
+ 00515504 bytes a899fc97
- 005154f4 ["INT_ADD", "register:40f0:8", ["const:5154f4:8", "const:4:8"]]
- 005154f4 ["CALL", null, ["callee:0054b434:8"]]
+ 00515534 ["INT_ADD", "register:40f0:8", ["const:515534:8", "const:4:8"]]
+ 00515534 ["CALL", null, ["callee:0054b434:8"]]
- 005154f4 bytes c0d70094
+ 00515534 bytes c0d70094
- 00515510 ["INT_ADD", "register:40f0:8", ["const:515510:8", "const:4:8"]]
- 00515510 ["CALL", null, ["callee:0054b7d0:8"]]
+ 00515550 ["INT_ADD", "register:40f0:8", ["const:515550:8", "const:4:8"]]
+ 00515550 ["CALL", null, ["callee:0054b7d0:8"]]
- 00515510 bytes a0d80094
+ 00515550 bytes a0d80094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4e8af8dbc3b95d7d1e2f6b1329d5caa"></a>

### [`00516b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516b84.md) → [`00516bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516bc4.md) FUN_00516bc4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00503084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503084.md) [`0051138c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/0051138c.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`005030c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/005030c4.md) [`005113cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/005113cc.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00516ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516b84.md#insn-00516ba0) · [`00516bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516b84.md#insn-00516bb4) · [`00516bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516b84.md#insn-00516bd4)
- 新版 `00516be0`（命令位置の公開資料なし） · `00516bf4`（命令位置の公開資料なし） · `00516c14`（命令位置の公開資料なし）

~~~diff
- 00516ba0 ["INT_ADD", "register:40f0:8", ["const:516ba0:8", "const:4:8"]]
- 00516ba0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00516be0 ["INT_ADD", "register:40f0:8", ["const:516be0:8", "const:4:8"]]
+ 00516be0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00516ba0 bytes c4031d94
+ 00516be0 bytes b4041d94
- 00516bb4 ["INT_ADD", "register:40f0:8", ["const:516bb4:8", "const:4:8"]]
- 00516bb4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00516bf4 ["INT_ADD", "register:40f0:8", ["const:516bf4:8", "const:4:8"]]
+ 00516bf4 ["CALL", null, ["callee:00c53d00:8"]]
- 00516bb4 bytes 4bf31c94
+ 00516bf4 bytes 43f41c94
- 00516bd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00516bd4 ["INT_ADD", "register:40f0:8", ["const:516bd4:8", "const:4:8"]]
- 00516bd4 ["CALLIND", null, ["register:0:8"]]
+ 00516c14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00516c14 ["INT_ADD", "register:40f0:8", ["const:516c14:8", "const:4:8"]]
+ 00516c14 ["CALLIND", null, ["register:0:8"]]
- 00516bd4 bytes 00013fd6
+ 00516c14 bytes 00013fd6
~~~


<a id="compare-79dd92f0bbe0695bbf60dd052dcf3cdd"></a>

### [`00517054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517054.md) → [`00517094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517094.md) FUN_00517094

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005170a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517054.md#insn-005170a0)
- 新版 `005170e0`（命令位置の公開資料なし）

~~~diff
- 005170a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005170a0 ["INT_ADD", "register:40f0:8", ["const:5170a0:8", "const:4:8"]]
- 005170a0 ["CALLIND", null, ["register:0:8"]]
+ 005170e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005170e0 ["INT_ADD", "register:40f0:8", ["const:5170e0:8", "const:4:8"]]
+ 005170e0 ["CALLIND", null, ["register:0:8"]]
- 005170a0 bytes 00013fd6
+ 005170e0 bytes 00013fd6
~~~


<a id="compare-50b0634491aadb22966c78b05ca5951b"></a>

### [`005170d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/005170d0.md) → [`00517110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517110.md) _ZNK5Botan10Extensions14extensions_rawEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0054c258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c258.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0054c298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c298.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00517174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/005170d0.md#insn-00517174) · [`0051718c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/005170d0.md#insn-0051718c) · [`005171a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/005170d0.md#insn-005171a8)
- 新版 `005171b4`（命令位置の公開資料なし） · `005171cc`（命令位置の公開資料なし） · `005171e8`（命令位置の公開資料なし）

~~~diff
- 00517174 ["INT_ADD", "register:40f0:8", ["const:517174:8", "const:4:8"]]
- 00517174 ["CALL", null, ["callee:00c57e90:8"]]
+ 005171b4 ["INT_ADD", "register:40f0:8", ["const:5171b4:8", "const:4:8"]]
+ 005171b4 ["CALL", null, ["callee:00c57e90:8"]]
- 00517174 bytes 47021d94
+ 005171b4 bytes 37031d94
- 0051718c ["INT_ADD", "register:40f0:8", ["const:51718c:8", "const:4:8"]]
- 0051718c ["CALL", null, ["callee:00c58000:8"]]
+ 005171cc ["INT_ADD", "register:40f0:8", ["const:5171cc:8", "const:4:8"]]
+ 005171cc ["CALL", null, ["callee:00c58000:8"]]
- 0051718c bytes 9d021d94
+ 005171cc bytes 8d031d94
- 005171a8 ["INT_ADD", "register:40f0:8", ["const:5171a8:8", "const:4:8"]]
- 005171a8 ["CALL", null, ["callee:0054c298:8"]]
+ 005171e8 ["INT_ADD", "register:40f0:8", ["const:5171e8:8", "const:4:8"]]
+ 005171e8 ["CALL", null, ["callee:0054c298:8"]]
- 005171a8 bytes 2cd40094
+ 005171e8 bytes 2cd40094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bec57ef6f361049cd2b61d324287a268"></a>

### [`00517594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517594.md) → [`005175d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/005175d4.md) FUN_005175d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005175b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517594.md#insn-005175b0) · [`005175c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517594.md#insn-005175c4) · [`005175f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517594.md#insn-005175f0)
- 新版 `005175f0`（命令位置の公開資料なし） · `00517604`（命令位置の公開資料なし） · `00517630`（命令位置の公開資料なし）

~~~diff
- 005175b0 ["INT_ADD", "register:40f0:8", ["const:5175b0:8", "const:4:8"]]
- 005175b0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005175f0 ["INT_ADD", "register:40f0:8", ["const:5175f0:8", "const:4:8"]]
+ 005175f0 ["CALL", null, ["callee:00c57eb0:8"]]
- 005175b0 bytes 40011d94
+ 005175f0 bytes 30021d94
- 005175c4 ["INT_ADD", "register:40f0:8", ["const:5175c4:8", "const:4:8"]]
- 005175c4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00517604 ["INT_ADD", "register:40f0:8", ["const:517604:8", "const:4:8"]]
+ 00517604 ["CALL", null, ["callee:00c53d00:8"]]
- 005175c4 bytes c7f01c94
+ 00517604 bytes bff11c94
- 005175f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005175f0 ["INT_ADD", "register:40f0:8", ["const:5175f0:8", "const:4:8"]]
- 005175f0 ["CALLIND", null, ["register:0:8"]]
+ 00517630 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00517630 ["INT_ADD", "register:40f0:8", ["const:517630:8", "const:4:8"]]
+ 00517630 ["CALLIND", null, ["register:0:8"]]
- 005175f0 bytes 00013fd6
+ 00517630 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd7c1cb55680ea78f73f15e06d881c6d"></a>

### [`005199bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/005199bc.md) → [`005199fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/005199fc.md) _ZNK5Botan14Cert_Extension24Subject_Alternative_Name11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053bb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bb30.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59570.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053bb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bb70.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59970.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005199ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/005199bc.md#insn-005199ec) · [`00519a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/005199bc.md#insn-00519a08) · [`00519a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/005199bc.md#insn-00519a44)
- 新版 `00519a2c`（命令位置の公開資料なし） · `00519a48`（命令位置の公開資料なし） · `00519a84`（命令位置の公開資料なし）

~~~diff
- 005199ec ["INT_ADD", "register:40f0:8", ["const:5199ec:8", "const:4:8"]]
- 005199ec ["CALL", null, ["callee:00c59970:8"]]
+ 00519a2c ["INT_ADD", "register:40f0:8", ["const:519a2c:8", "const:4:8"]]
+ 00519a2c ["CALL", null, ["callee:00c59970:8"]]
- 005199ec bytes e1fe1c94
+ 00519a2c bytes d1ff1c94
- 00519a08 ["INT_ADD", "register:40f0:8", ["const:519a08:8", "const:4:8"]]
- 00519a08 ["CALL", null, ["callee:0046d490:8"]]
+ 00519a48 ["INT_ADD", "register:40f0:8", ["const:519a48:8", "const:4:8"]]
+ 00519a48 ["CALL", null, ["callee:0046d490:8"]]
- 00519a08 bytes 924efd97
+ 00519a48 bytes 924efd97
- 00519a44 ["INT_ADD", "register:40f0:8", ["const:519a44:8", "const:4:8"]]
- 00519a44 ["CALL", null, ["callee:0053bb70:8"]]
+ 00519a84 ["INT_ADD", "register:40f0:8", ["const:519a84:8", "const:4:8"]]
+ 00519a84 ["CALL", null, ["callee:0053bb70:8"]]
- 00519a44 bytes 3b880094
+ 00519a84 bytes 3b880094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdbf8e6fde6e007e71f6cc12c38eeb5a"></a>

### [`00519aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/00519aa4.md) → [`00519ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/00519ae4.md) _ZNK5Botan14Cert_Extension23Issuer_Alternative_Name11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053bb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bb30.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59570.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053bb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bb70.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59970.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00519ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/00519aa4.md#insn-00519ad4) · [`00519af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/00519aa4.md#insn-00519af0) · [`00519b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/00519aa4.md#insn-00519b2c)
- 新版 `00519b14`（命令位置の公開資料なし） · `00519b30`（命令位置の公開資料なし） · `00519b6c`（命令位置の公開資料なし）

~~~diff
- 00519ad4 ["INT_ADD", "register:40f0:8", ["const:519ad4:8", "const:4:8"]]
- 00519ad4 ["CALL", null, ["callee:00c59970:8"]]
+ 00519b14 ["INT_ADD", "register:40f0:8", ["const:519b14:8", "const:4:8"]]
+ 00519b14 ["CALL", null, ["callee:00c59970:8"]]
- 00519ad4 bytes a7fe1c94
+ 00519b14 bytes 97ff1c94
- 00519af0 ["INT_ADD", "register:40f0:8", ["const:519af0:8", "const:4:8"]]
- 00519af0 ["CALL", null, ["callee:0046d490:8"]]
+ 00519b30 ["INT_ADD", "register:40f0:8", ["const:519b30:8", "const:4:8"]]
+ 00519b30 ["CALL", null, ["callee:0046d490:8"]]
- 00519af0 bytes 584efd97
+ 00519b30 bytes 584efd97
- 00519b2c ["INT_ADD", "register:40f0:8", ["const:519b2c:8", "const:4:8"]]
- 00519b2c ["CALL", null, ["callee:0053bb70:8"]]
+ 00519b6c ["INT_ADD", "register:40f0:8", ["const:519b6c:8", "const:4:8"]]
+ 00519b6c ["CALL", null, ["callee:0053bb70:8"]]
- 00519b2c bytes 01880094
+ 00519b6c bytes 01880094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1715300b10ea0e99f5b3042f35985dc"></a>

### [`0051a994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a994.md) → [`0051a9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a9d4.md) FUN_0051a9d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0051a240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a240.md) · 呼出先 7件 [`0051ad64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ad64.md) [`0053d720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d720.md) [`0053d7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d7b8.md) [`0053d7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d7cc.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 1件 [`0051a280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a280.md) · 呼出先 7件 [`0051ada4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051ada4.md) [`0053d760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d760.md) [`0053d7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d7f8.md) [`0053d80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d80c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051aa0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a994.md#insn-0051aa0c) · [`0051aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a994.md#insn-0051aa30) · [`0051aa7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a994.md#insn-0051aa7c)
- 新版 `0051aa4c`（命令位置の公開資料なし） · `0051aa70`（命令位置の公開資料なし） · `0051aabc`（命令位置の公開資料なし）

~~~diff
- 0051aa0c ["INT_ADD", "register:40f0:8", ["const:51aa0c:8", "const:4:8"]]
- 0051aa0c ["CALL", null, ["callee:00c57e90:8"]]
+ 0051aa4c ["INT_ADD", "register:40f0:8", ["const:51aa4c:8", "const:4:8"]]
+ 0051aa4c ["CALL", null, ["callee:00c57e90:8"]]
- 0051aa0c bytes 21f41c94
+ 0051aa4c bytes 11f51c94
- 0051aa30 ["INT_ADD", "register:40f0:8", ["const:51aa30:8", "const:4:8"]]
- 0051aa30 ["CALL", null, ["callee:0053d80c:8"]]
+ 0051aa70 ["INT_ADD", "register:40f0:8", ["const:51aa70:8", "const:4:8"]]
+ 0051aa70 ["CALL", null, ["callee:0053d80c:8"]]
- 0051aa30 bytes 678b0094
+ 0051aa70 bytes 678b0094
- 0051aa7c ["INT_ADD", "register:40f0:8", ["const:51aa7c:8", "const:4:8"]]
- 0051aa7c ["CALL", null, ["callee:00c57e90:8"]]
+ 0051aabc ["INT_ADD", "register:40f0:8", ["const:51aabc:8", "const:4:8"]]
+ 0051aabc ["CALL", null, ["callee:00c57e90:8"]]
- 0051aa7c bytes 05f41c94
+ 0051aabc bytes f5f41c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fed8fedf17478fb53230b426e4e8b52"></a>

### [`0051ab5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ab5c.md) → [`0051ab9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051ab9c.md) FUN_0051ab9c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0051a240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a240.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0051a280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a280.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051abac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ab5c.md#insn-0051abac) · [`0051abbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ab5c.md#insn-0051abbc) · [`0051abcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ab5c.md#insn-0051abcc)
- 新版 `0051abec`（命令位置の公開資料なし） · `0051abfc`（命令位置の公開資料なし） · `0051ac0c`（命令位置の公開資料なし）

~~~diff
- 0051abac ["INT_ADD", "register:40f0:8", ["const:51abac:8", "const:4:8"]]
- 0051abac ["CALL", null, ["callee:00c57eb0:8"]]
+ 0051abec ["INT_ADD", "register:40f0:8", ["const:51abec:8", "const:4:8"]]
+ 0051abec ["CALL", null, ["callee:00c57eb0:8"]]
- 0051abac bytes c1f31c94
+ 0051abec bytes b1f41c94
- 0051abbc ["INT_ADD", "register:40f0:8", ["const:51abbc:8", "const:4:8"]]
- 0051abbc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0051abfc ["INT_ADD", "register:40f0:8", ["const:51abfc:8", "const:4:8"]]
+ 0051abfc ["CALL", null, ["callee:00c57eb0:8"]]
- 0051abbc bytes bdf31c94
+ 0051abfc bytes adf41c94
- 0051abcc ["INT_ADD", "register:40f0:8", ["const:51abcc:8", "const:4:8"]]
- 0051abcc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0051ac0c ["INT_ADD", "register:40f0:8", ["const:51ac0c:8", "const:4:8"]]
+ 0051ac0c ["CALL", null, ["callee:00c57eb0:8"]]
- 0051abcc bytes b9f31c94
+ 0051ac0c bytes a9f41c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1624ed54c33fb9d6a5de6dee70362325"></a>

### [`0051ac84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ac84.md) → [`0051acc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051acc4.md) FUN_0051acc4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0051a240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a240.md) [`00531cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531cec.md) [`00531cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531cf4.md) [`0054d464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d464.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0051a280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a280.md) [`00531d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531d2c.md) [`00531d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531d34.md) [`0054d4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d4a4.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051accc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ac84.md#insn-0051accc) · [`0051acdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ac84.md#insn-0051acdc) · [`0051acec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ac84.md#insn-0051acec)
- 新版 `0051ad0c`（命令位置の公開資料なし） · `0051ad1c`（命令位置の公開資料なし） · `0051ad2c`（命令位置の公開資料なし）

~~~diff
- 0051accc ["INT_ADD", "register:40f0:8", ["const:51accc:8", "const:4:8"]]
- 0051accc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0051ad0c ["INT_ADD", "register:40f0:8", ["const:51ad0c:8", "const:4:8"]]
+ 0051ad0c ["CALL", null, ["callee:00c57eb0:8"]]
- 0051accc bytes 79f31c94
+ 0051ad0c bytes 69f41c94
- 0051acdc ["INT_ADD", "register:40f0:8", ["const:51acdc:8", "const:4:8"]]
- 0051acdc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0051ad1c ["INT_ADD", "register:40f0:8", ["const:51ad1c:8", "const:4:8"]]
+ 0051ad1c ["CALL", null, ["callee:00c57eb0:8"]]
- 0051acdc bytes 75f31c94
+ 0051ad1c bytes 65f41c94
- 0051acec ["INT_ADD", "register:40f0:8", ["const:51acec:8", "const:4:8"]]
- 0051acec ["CALL", null, ["callee:00c57eb0:8"]]
+ 0051ad2c ["INT_ADD", "register:40f0:8", ["const:51ad2c:8", "const:4:8"]]
+ 0051ad2c ["CALL", null, ["callee:00c57eb0:8"]]
- 0051acec bytes 71f31c94
+ 0051ad2c bytes 61f41c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21a3a97df58d040e6c5e505564de6682"></a>

### [`0051ad64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ad64.md) → [`0051ada4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051ada4.md) FUN_0051ada4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0051a994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a994.md) [`0053f8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f8d0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0051a9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a9d4.md) [`0053f910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f910.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051adac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ad64.md#insn-0051adac) · [`0051adbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ad64.md#insn-0051adbc)
- 新版 `0051adec`（命令位置の公開資料なし） · `0051adfc`（命令位置の公開資料なし）

~~~diff
- 0051adac ["INT_ADD", "register:40f0:8", ["const:51adac:8", "const:4:8"]]
- 0051adac ["CALL", null, ["callee:00c57eb0:8"]]
+ 0051adec ["INT_ADD", "register:40f0:8", ["const:51adec:8", "const:4:8"]]
+ 0051adec ["CALL", null, ["callee:00c57eb0:8"]]
- 0051adac bytes 41f31c94
+ 0051adec bytes 31f41c94
- 0051adbc ["INT_ADD", "register:40f0:8", ["const:51adbc:8", "const:4:8"]]
- 0051adbc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0051adfc ["INT_ADD", "register:40f0:8", ["const:51adfc:8", "const:4:8"]]
+ 0051adfc ["CALL", null, ["callee:00c57eb0:8"]]
- 0051adbc bytes 3df31c94
+ 0051adfc bytes 2df41c94
~~~


<a id="compare-808ed93b8c466f1c5efd4f34da465fb4"></a>

### [`0051b828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051b828.md) → [`0051b868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051b868.md) _ZNK5Botan16X509_Certificate11is_criticalERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59a50.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md) [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 1件 [`00c59e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59e50.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051b84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051b828.md#insn-0051b84c) · [`0051b85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051b828.md#insn-0051b85c) · [`0051b95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051b828.md#insn-0051b95c)
- 新版 `0051b88c`（命令位置の公開資料なし） · `0051b89c`（命令位置の公開資料なし） · `0051b99c`（命令位置の公開資料なし）

~~~diff
- 0051b84c ["INT_ADD", "register:40f0:8", ["const:51b84c:8", "const:4:8"]]
- 0051b84c ["CALL", null, ["callee:00c599f0:8"]]
+ 0051b88c ["INT_ADD", "register:40f0:8", ["const:51b88c:8", "const:4:8"]]
+ 0051b88c ["CALL", null, ["callee:00c599f0:8"]]
- 0051b84c bytes 69f71c94
+ 0051b88c bytes 59f81c94
- 0051b85c ["INT_ADD", "register:40f0:8", ["const:51b85c:8", "const:4:8"]]
- 0051b85c ["CALL", null, ["callee:00c58680:8"]]
+ 0051b89c ["INT_ADD", "register:40f0:8", ["const:51b89c:8", "const:4:8"]]
+ 0051b89c ["CALL", null, ["callee:00c58680:8"]]
- 0051b85c bytes 89f21c94
+ 0051b89c bytes 79f31c94
- 0051b95c ["INT_ADD", "register:40f0:8", ["const:51b95c:8", "const:4:8"]]
- 0051b95c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0051b99c ["INT_ADD", "register:40f0:8", ["const:51b99c:8", "const:4:8"]]
+ 0051b99c ["CALL", null, ["callee:00c57eb0:8"]]
- 0051b95c bytes 55f01c94
+ 0051b99c bytes 45f11c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71cee3d111ed7c8c9da0da3e82e74d94"></a>

### [`0051b994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051b994.md) → [`0051b9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051b9d4.md) FUN_0051b9d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051b9fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051b994.md#insn-0051b9fc) · [`0051ba30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051b994.md#insn-0051ba30)
- 新版 `0051ba3c`（命令位置の公開資料なし） · `0051ba70`（命令位置の公開資料なし）

~~~diff
- 0051b9fc ["INT_ADD", "register:40f0:8", ["const:51b9fc:8", "const:4:8"]]
- 0051b9fc ["CALL", null, ["callee:00c57e90:8"]]
+ 0051ba3c ["INT_ADD", "register:40f0:8", ["const:51ba3c:8", "const:4:8"]]
+ 0051ba3c ["CALL", null, ["callee:00c57e90:8"]]
- 0051b9fc bytes 25f01c94
+ 0051ba3c bytes 15f11c94
- 0051ba30 ["INT_ADD", "register:40f0:8", ["const:51ba30:8", "const:4:8"]]
- 0051ba30 ["CALL", null, ["callee:0043bba4:8"]]
+ 0051ba70 ["INT_ADD", "register:40f0:8", ["const:51ba70:8", "const:4:8"]]
+ 0051ba70 ["CALL", null, ["callee:0043bba4:8"]]
- 0051ba30 bytes 4d80fc97
+ 0051ba70 bytes 4d80fc97
~~~


<a id="compare-56c5e70f484743c870d5c10efede4b04"></a>

### [`0051ba64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051ba64.md) → [`0051baa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051baa4.md) FUN_0051baa4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051ba80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051ba64.md#insn-0051ba80)
- 新版 `0051bac0`（命令位置の公開資料なし）

~~~diff
- 0051ba80 ["INT_ADD", "register:40f0:8", ["const:51ba80:8", "const:4:8"]]
- 0051ba80 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0051bac0 ["INT_ADD", "register:40f0:8", ["const:51bac0:8", "const:4:8"]]
+ 0051bac0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0051ba80 bytes 0cf01c94
+ 0051bac0 bytes fcf01c94
~~~


<a id="compare-b4de0321674b685248bc17871b90d520"></a>

### [`0051bfb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051bfb0.md) → [`0051bff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051bff0.md) FUN_0051bff0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051bff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051bfb0.md#insn-0051bff8)
- 新版 `0051c038`（命令位置の公開資料なし）

~~~diff
- 0051bff8 ["INT_ADD", "register:40f0:8", ["const:51bff8:8", "const:4:8"]]
- 0051bff8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0051c038 ["INT_ADD", "register:40f0:8", ["const:51c038:8", "const:4:8"]]
+ 0051c038 ["CALL", null, ["callee:00c57eb0:8"]]
- 0051bff8 bytes aeee1c94
+ 0051c038 bytes 9eef1c94
~~~


<a id="compare-fc52642383d61b9e07019074c2aabaa1"></a>

### [`0051c7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c7cc.md) → [`0051c80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c80c.md) _ZN5Botan14Cert_Extension20Certificate_Policies8validateERKNS_16X509_CertificateES4_RKNSt6__ndk16vectorINS5_10shared_ptrIS3_EENS5_9allocator

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0051c954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c954.md) [`0054087c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054087c.md) [`0054d0ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d0ac.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0051c994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c994.md) [`005408bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005408bc.md) [`0054d0ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d0ec.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051c804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c7cc.md#insn-0051c804) · [`0051c898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c7cc.md#insn-0051c898) · [`0051c8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c7cc.md#insn-0051c8cc)
- 新版 `0051c844`（命令位置の公開資料なし） · `0051c8d8`（命令位置の公開資料なし） · `0051c90c`（命令位置の公開資料なし）

~~~diff
- 0051c804 ["INT_ADD", "register:40f0:8", ["const:51c804:8", "const:4:8"]]
- 0051c804 ["CALL", null, ["callee:0051c994:8"]]
+ 0051c844 ["INT_ADD", "register:40f0:8", ["const:51c844:8", "const:4:8"]]
+ 0051c844 ["CALL", null, ["callee:0051c994:8"]]
- 0051c804 bytes 54000094
+ 0051c844 bytes 54000094
- 0051c898 ["INT_ADD", "register:40f0:8", ["const:51c898:8", "const:4:8"]]
- 0051c898 ["CALL", null, ["callee:00c57e90:8"]]
+ 0051c8d8 ["INT_ADD", "register:40f0:8", ["const:51c8d8:8", "const:4:8"]]
+ 0051c8d8 ["CALL", null, ["callee:00c57e90:8"]]
- 0051c898 bytes 7eec1c94
+ 0051c8d8 bytes 6eed1c94
- 0051c8cc ["INT_ADD", "register:40f0:8", ["const:51c8cc:8", "const:4:8"]]
- 0051c8cc ["CALL", null, ["callee:0043bba4:8"]]
+ 0051c90c ["INT_ADD", "register:40f0:8", ["const:51c90c:8", "const:4:8"]]
+ 0051c90c ["CALL", null, ["callee:0043bba4:8"]]
- 0051c8cc bytes a67cfc97
+ 0051c90c bytes a67cfc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-199e347d78eeaf9cfd80beb804b1f6f2"></a>

### [`0051c954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c954.md) → [`0051c994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c994.md) FUN_0051c994

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0051c7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c7cc.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0054cbf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cbf4.md) [`0054cf90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cf90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0051c80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c80c.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0054cc34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054cc34.md) [`0054cfd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054cfd0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051c9a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c954.md#insn-0051c9a4) · [`0051c9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c954.md#insn-0051c9d4) · [`0051c9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c954.md#insn-0051c9f0)
- 新版 `0051c9e4`（命令位置の公開資料なし） · `0051ca14`（命令位置の公開資料なし） · `0051ca30`（命令位置の公開資料なし）

~~~diff
- 0051c9a4 ["INT_ADD", "register:40f0:8", ["const:51c9a4:8", "const:4:8"]]
- 0051c9a4 ["CALL", null, ["callee:0043bba4:8"]]
+ 0051c9e4 ["INT_ADD", "register:40f0:8", ["const:51c9e4:8", "const:4:8"]]
+ 0051c9e4 ["CALL", null, ["callee:0043bba4:8"]]
- 0051c9a4 bytes 707cfc97
+ 0051c9e4 bytes 707cfc97
- 0051c9d4 ["INT_ADD", "register:40f0:8", ["const:51c9d4:8", "const:4:8"]]
- 0051c9d4 ["CALL", null, ["callee:0054cc34:8"]]
+ 0051ca14 ["INT_ADD", "register:40f0:8", ["const:51ca14:8", "const:4:8"]]
+ 0051ca14 ["CALL", null, ["callee:0054cc34:8"]]
- 0051c9d4 bytes 88c00094
+ 0051ca14 bytes 88c00094
- 0051c9f0 ["INT_ADD", "register:40f0:8", ["const:51c9f0:8", "const:4:8"]]
- 0051c9f0 ["CALL", null, ["callee:0054cfd0:8"]]
+ 0051ca30 ["INT_ADD", "register:40f0:8", ["const:51ca30:8", "const:4:8"]]
+ 0051ca30 ["CALL", null, ["callee:0054cfd0:8"]]
- 0051c9f0 bytes 68c10094
+ 0051ca30 bytes 68c10094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-747ab219574990166ddd719884faa600"></a>

### [`0051f008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f008.md) → [`0051f048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f048.md) _ZNK5Botan14Cert_Extension17Unknown_Extension12encode_innerEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051f038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f008.md#insn-0051f038) · [`0051f050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f008.md#insn-0051f050) · [`0051f06c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f008.md#insn-0051f06c)
- 新版 `0051f078`（命令位置の公開資料なし） · `0051f090`（命令位置の公開資料なし） · `0051f0ac`（命令位置の公開資料なし）

~~~diff
- 0051f038 ["INT_ADD", "register:40f0:8", ["const:51f038:8", "const:4:8"]]
- 0051f038 ["CALL", null, ["callee:00c57e90:8"]]
+ 0051f078 ["INT_ADD", "register:40f0:8", ["const:51f078:8", "const:4:8"]]
+ 0051f078 ["CALL", null, ["callee:00c57e90:8"]]
- 0051f038 bytes 96e21c94
+ 0051f078 bytes 86e31c94
- 0051f050 ["INT_ADD", "register:40f0:8", ["const:51f050:8", "const:4:8"]]
- 0051f050 ["CALL", null, ["callee:00c58000:8"]]
+ 0051f090 ["INT_ADD", "register:40f0:8", ["const:51f090:8", "const:4:8"]]
+ 0051f090 ["CALL", null, ["callee:00c58000:8"]]
- 0051f050 bytes ece21c94
+ 0051f090 bytes dce31c94
- 0051f06c ["INT_ADD", "register:40f0:8", ["const:51f06c:8", "const:4:8"]]
- 0051f06c ["CALL", null, ["callee:0049f42c:8"]]
+ 0051f0ac ["INT_ADD", "register:40f0:8", ["const:51f0ac:8", "const:4:8"]]
+ 0051f0ac ["CALL", null, ["callee:0049f42c:8"]]
- 0051f06c bytes e000fe97
+ 0051f0ac bytes e000fe97
~~~


<a id="compare-d0568ab5d71fde404fe4db02ef5411d2"></a>

### [`0051f0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f0b4.md) → [`0051f0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f0f4.md) _ZNK5Botan11X509_Object11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c582b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582b0.md) [`00c582c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582c0.md) [`00c582d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582d0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c586b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586b0.md) [`00c586c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586c0.md) [`00c586d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051f0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f0b4.md#insn-0051f0dc) · [`0051f0ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f0b4.md#insn-0051f0ec) · [`0051f108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f0b4.md#insn-0051f108)
- 新版 `0051f11c`（命令位置の公開資料なし） · `0051f12c`（命令位置の公開資料なし） · `0051f148`（命令位置の公開資料なし）

~~~diff
- 0051f0dc ["INT_ADD", "register:40f0:8", ["const:51f0dc:8", "const:4:8"]]
- 0051f0dc ["CALL", null, ["callee:00c586b0:8"]]
+ 0051f11c ["INT_ADD", "register:40f0:8", ["const:51f11c:8", "const:4:8"]]
+ 0051f11c ["CALL", null, ["callee:00c586b0:8"]]
- 0051f0dc bytes 75e41c94
+ 0051f11c bytes 65e51c94
- 0051f0ec ["INT_ADD", "register:40f0:8", ["const:51f0ec:8", "const:4:8"]]
- 0051f0ec ["CALL", null, ["callee:00c586b0:8"]]
+ 0051f12c ["INT_ADD", "register:40f0:8", ["const:51f12c:8", "const:4:8"]]
+ 0051f12c ["CALL", null, ["callee:00c586b0:8"]]
- 0051f0ec bytes 71e41c94
+ 0051f12c bytes 61e51c94
- 0051f108 ["INT_ADD", "register:40f0:8", ["const:51f108:8", "const:4:8"]]
- 0051f108 ["CALL", null, ["callee:00c586c0:8"]]
+ 0051f148 ["INT_ADD", "register:40f0:8", ["const:51f148:8", "const:4:8"]]
+ 0051f148 ["CALL", null, ["callee:00c586c0:8"]]
- 0051f108 bytes 6ee41c94
+ 0051f148 bytes 5ee51c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b02cf8688f260604ab6b282fc4643233"></a>

### [`0051f454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f454.md) → [`0051f494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f494.md) _ZNK5Botan11X509_Object10PEM_encodeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59090.md) [`00c59a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59a80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59490.md) [`00c59e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051f480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f454.md#insn-0051f480) · [`0051f494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f454.md#insn-0051f494) · [`0051f4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f454.md#insn-0051f4ac)
- 新版 `0051f4c0`（命令位置の公開資料なし） · `0051f4d4`（命令位置の公開資料なし） · `0051f4ec`（命令位置の公開資料なし）

~~~diff
- 0051f480 ["INT_ADD", "register:40f0:8", ["const:51f480:8", "const:4:8"]]
- 0051f480 ["CALL", null, ["callee:00c59e80:8"]]
+ 0051f4c0 ["INT_ADD", "register:40f0:8", ["const:51f4c0:8", "const:4:8"]]
+ 0051f4c0 ["CALL", null, ["callee:00c59e80:8"]]
- 0051f480 bytes 80e91c94
+ 0051f4c0 bytes 70ea1c94
- 0051f494 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051f494 ["INT_ADD", "register:40f0:8", ["const:51f494:8", "const:4:8"]]
- 0051f494 ["CALLIND", null, ["register:0:8"]]
+ 0051f4d4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051f4d4 ["INT_ADD", "register:40f0:8", ["const:51f4d4:8", "const:4:8"]]
+ 0051f4d4 ["CALLIND", null, ["register:0:8"]]
- 0051f494 bytes 20013fd6
+ 0051f4d4 bytes 20013fd6
- 0051f4ac ["INT_ADD", "register:40f0:8", ["const:51f4ac:8", "const:4:8"]]
- 0051f4ac ["CALL", null, ["callee:00c59490:8"]]
+ 0051f4ec ["INT_ADD", "register:40f0:8", ["const:51f4ec:8", "const:4:8"]]
+ 0051f4ec ["CALL", null, ["callee:00c59490:8"]]
- 0051f4ac bytes f9e61c94
+ 0051f4ec bytes e9e71c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00fec7d32edc7e73b527cc4ae48fbcc3"></a>

### [`0051ff70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051ff70.md) → [`0051ffb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051ffb0.md) FUN_0051ffb0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051ff8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051ff70.md#insn-0051ff8c) · [`0051ff9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051ff70.md#insn-0051ff9c) · [`0051ffac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051ff70.md#insn-0051ffac)
- 新版 `0051ffcc`（命令位置の公開資料なし） · `0051ffdc`（命令位置の公開資料なし） · `0051ffec`（命令位置の公開資料なし）

~~~diff
- 0051ff8c ["INT_ADD", "register:40f0:8", ["const:51ff8c:8", "const:4:8"]]
- 0051ff8c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0051ffcc ["INT_ADD", "register:40f0:8", ["const:51ffcc:8", "const:4:8"]]
+ 0051ffcc ["CALL", null, ["callee:00c57eb0:8"]]
- 0051ff8c bytes c9de1c94
+ 0051ffcc bytes b9df1c94
- 0051ff9c ["INT_ADD", "register:40f0:8", ["const:51ff9c:8", "const:4:8"]]
- 0051ff9c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0051ffdc ["INT_ADD", "register:40f0:8", ["const:51ffdc:8", "const:4:8"]]
+ 0051ffdc ["CALL", null, ["callee:00c57eb0:8"]]
- 0051ff9c bytes c5de1c94
+ 0051ffdc bytes b5df1c94
- 0051ffac ["INT_ADD", "register:40f0:8", ["const:51ffac:8", "const:4:8"]]
- 0051ffac ["CALL", null, ["callee:00c57eb0:8"]]
+ 0051ffec ["INT_ADD", "register:40f0:8", ["const:51ffec:8", "const:4:8"]]
+ 0051ffec ["CALL", null, ["callee:00c57eb0:8"]]
- 0051ffac bytes c1de1c94
+ 0051ffec bytes b1df1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b10f91fa1083a9c6434270e616af13dd"></a>

### [`0051fff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051fff4.md) → [`00520034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520034.md) _ZNK5Botan11X509_Object15check_signatureERKNS_10Public_KeyE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c598b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59cb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051fffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051fff4.md#insn-0051fffc)
- 新版 `0052003c`（命令位置の公開資料なし）

~~~diff
- 0051fffc ["INT_ADD", "register:40f0:8", ["const:51fffc:8", "const:4:8"]]
- 0051fffc ["CALL", null, ["callee:00c59cb0:8"]]
+ 0052003c ["INT_ADD", "register:40f0:8", ["const:52003c:8", "const:4:8"]]
+ 0052003c ["CALL", null, ["callee:00c59cb0:8"]]
- 0051fffc bytes 2de61c94
+ 0052003c bytes 1de71c94
~~~


<a id="compare-890c75691ef5ffe53104868585e1f72c"></a>

### [`00520b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520b7c.md) → [`00520bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520bbc.md) FUN_00520bbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00520b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520b7c.md#insn-00520b98) · [`00520bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520b7c.md#insn-00520bb8)
- 新版 `00520bd8`（命令位置の公開資料なし） · `00520bf8`（命令位置の公開資料なし）

~~~diff
- 00520b98 ["INT_ADD", "register:40f0:8", ["const:520b98:8", "const:4:8"]]
- 00520b98 ["CALL", null, ["callee:00c53d00:8"]]
+ 00520bd8 ["INT_ADD", "register:40f0:8", ["const:520bd8:8", "const:4:8"]]
+ 00520bd8 ["CALL", null, ["callee:00c53d00:8"]]
- 00520b98 bytes 52cb1c94
+ 00520bd8 bytes 4acc1c94
- 00520bb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00520bb8 ["INT_ADD", "register:40f0:8", ["const:520bb8:8", "const:4:8"]]
- 00520bb8 ["CALLIND", null, ["register:0:8"]]
+ 00520bf8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00520bf8 ["INT_ADD", "register:40f0:8", ["const:520bf8:8", "const:4:8"]]
+ 00520bf8 ["CALLIND", null, ["register:0:8"]]
- 00520bb8 bytes 00013fd6
+ 00520bf8 bytes 00013fd6
~~~


