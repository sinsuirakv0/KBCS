# v16.0.0 → v16.0.1 · 要調査の変更候補 (23)

[一覧の目次](README.md)

<a id="compare-89173d07c1089362953cfda387335da4"></a>

### [`00737898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/00737898.md) → [`007378d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00737/007378d8.md) FUN_007378d8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00734030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734030.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00734070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/00734070.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007378d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/00737898.md#insn-007378d8) · [`00737924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/00737898.md#insn-00737924) · [`007379b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/00737898.md#insn-007379b0)
- 新版 `00737918`（命令位置の公開資料なし） · `00737964`（命令位置の公開資料なし） · `007379f0`（命令位置の公開資料なし）

~~~diff
- 007378d8 ["INT_ADD", "register:40f0:8", ["const:7378d8:8", "const:4:8"]]
- 007378d8 ["CALL", null, ["callee:008514f8:8"]]
+ 00737918 ["INT_ADD", "register:40f0:8", ["const:737918:8", "const:4:8"]]
+ 00737918 ["CALL", null, ["callee:008514f8:8"]]
- 007378d8 bytes f8660494
+ 00737918 bytes f8660494
- 00737924 ["INT_ADD", "register:40f0:8", ["const:737924:8", "const:4:8"]]
- 00737924 ["CALL", null, ["callee:00734070:8"]]
+ 00737964 ["INT_ADD", "register:40f0:8", ["const:737964:8", "const:4:8"]]
+ 00737964 ["CALL", null, ["callee:00734070:8"]]
- 00737924 bytes c3f1ff97
+ 00737964 bytes c3f1ff97
- 007379b0 ["INT_ADD", "register:40f0:8", ["const:7379b0:8", "const:4:8"]]
- 007379b0 ["CALL", null, ["callee:00c57e90:8"]]
+ 007379f0 ["INT_ADD", "register:40f0:8", ["const:7379f0:8", "const:4:8"]]
+ 007379f0 ["CALL", null, ["callee:00c57e90:8"]]
- 007379b0 bytes 38801494
+ 007379f0 bytes 28811494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74ada10570c229cf4d26ce048f274a13"></a>

### [`00737b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/00737b24.md) → [`00737b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00737/00737b64.md) FUN_00737b64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00733e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/00733e24.md) [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 5件 [`00493958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493958.md) [`00734030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734030.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`00733e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733e64.md) [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 5件 [`00493998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493998.md) [`00734070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/00734070.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00737b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/00737b24.md#insn-00737b4c) · [`00737bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/00737b24.md#insn-00737bac) · [`00737bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/00737b24.md#insn-00737bb8)
- 新版 `00737b8c`（命令位置の公開資料なし） · `00737bec`（命令位置の公開資料なし） · `00737bf8`（命令位置の公開資料なし）

~~~diff
- 00737b4c ["INT_ADD", "register:40f0:8", ["const:737b4c:8", "const:4:8"]]
- 00737b4c ["CALL", null, ["callee:008514f8:8"]]
+ 00737b8c ["INT_ADD", "register:40f0:8", ["const:737b8c:8", "const:4:8"]]
+ 00737b8c ["CALL", null, ["callee:008514f8:8"]]
- 00737b4c bytes 5b660494
+ 00737b8c bytes 5b660494
- 00737bac ["INT_ADD", "register:40f0:8", ["const:737bac:8", "const:4:8"]]
- 00737bac ["CALL", null, ["callee:00734070:8"]]
+ 00737bec ["INT_ADD", "register:40f0:8", ["const:737bec:8", "const:4:8"]]
+ 00737bec ["CALL", null, ["callee:00734070:8"]]
- 00737bac bytes 21f1ff97
+ 00737bec bytes 21f1ff97
- 00737bb8 ["INT_ADD", "register:40f0:8", ["const:737bb8:8", "const:4:8"]]
- 00737bb8 ["CALL", null, ["callee:00493998:8"]]
+ 00737bf8 ["INT_ADD", "register:40f0:8", ["const:737bf8:8", "const:4:8"]]
+ 00737bf8 ["CALL", null, ["callee:00493998:8"]]
- 00737bb8 bytes 686ff597
+ 00737bf8 bytes 686ff597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2867ec907de8ee6069e6cfdbf46b46f8"></a>

### [`00737d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/00737d20.md) → [`00737d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00737/00737d60.md) FUN_00737d60

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00737dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/00737d20.md#insn-00737dec) · [`00737e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/00737d20.md#insn-00737e24)
- 新版 `00737e2c`（命令位置の公開資料なし） · `00737e64`（命令位置の公開資料なし）

~~~diff
- 00737dec ["INT_ADD", "register:40f0:8", ["const:737dec:8", "const:4:8"]]
- 00737dec ["CALL", null, ["callee:00c57e90:8"]]
+ 00737e2c ["INT_ADD", "register:40f0:8", ["const:737e2c:8", "const:4:8"]]
+ 00737e2c ["CALL", null, ["callee:00c57e90:8"]]
- 00737dec bytes 297f1494
+ 00737e2c bytes 19801494
- 00737e24 ["INT_ADD", "register:40f0:8", ["const:737e24:8", "const:4:8"]]
- 00737e24 ["CALL", null, ["callee:0043bba4:8"]]
+ 00737e64 ["INT_ADD", "register:40f0:8", ["const:737e64:8", "const:4:8"]]
+ 00737e64 ["CALL", null, ["callee:0043bba4:8"]]
- 00737e24 bytes 500ff497
+ 00737e64 bytes 500ff497
~~~


<a id="compare-21e02323553e53e03c9d1efbb8c3867c"></a>

### [`00737e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/00737e4c.md) → [`00737e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00737/00737e8c.md) FUN_00737e8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a14bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a14bf0.md) · 呼出先 8件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md) [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md) [`004810e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/004810e8.md) [`00739efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/00739efc.md)
- 新版 呼出元 1件 [`00a14d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14d8c.md) · 呼出先 8件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md) [`00481128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481128.md) [`00739f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00739/00739f3c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00737e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/00737e4c.md#insn-00737e88) · [`00737ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/00737e4c.md#insn-00737ef4) · [`00737f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/00737e4c.md#insn-00737f30)
- 新版 `00737ec8`（命令位置の公開資料なし） · `00737f34`（命令位置の公開資料なし） · `00737f70`（命令位置の公開資料なし）

~~~diff
- 00737e88 ["INT_ADD", "register:40f0:8", ["const:737e88:8", "const:4:8"]]
- 00737e88 ["CALL", null, ["callee:00480e28:8"]]
+ 00737ec8 ["INT_ADD", "register:40f0:8", ["const:737ec8:8", "const:4:8"]]
+ 00737ec8 ["CALL", null, ["callee:00480e28:8"]]
- 00737e88 bytes d823f597
+ 00737ec8 bytes d823f597
- 00737ef4 ["INT_ADD", "register:40f0:8", ["const:737ef4:8", "const:4:8"]]
- 00737ef4 ["CALL", null, ["callee:00739f3c:8"]]
+ 00737f34 ["INT_ADD", "register:40f0:8", ["const:737f34:8", "const:4:8"]]
+ 00737f34 ["CALL", null, ["callee:00739f3c:8"]]
- 00737ef4 bytes 02080094
+ 00737f34 bytes 02080094
- 00737f30 ["INT_ADD", "register:40f0:8", ["const:737f30:8", "const:4:8"]]
- 00737f30 ["CALL", null, ["callee:00480e28:8"]]
+ 00737f70 ["INT_ADD", "register:40f0:8", ["const:737f70:8", "const:4:8"]]
+ 00737f70 ["CALL", null, ["callee:00480e28:8"]]
- 00737f30 bytes ae23f597
+ 00737f70 bytes ae23f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdd53f18277bf8804b33ef10e529d6ad"></a>

### [`007382c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/007382c8.md) → [`00738308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/00738308.md) FUN_00738308

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a14bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a14bf0.md) · 呼出先 1件 [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md)
- 新版 呼出元 1件 [`00a14d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14d8c.md) · 呼出先 1件 [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007382e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/007382c8.md#insn-007382e0) · [`007382ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/007382c8.md#insn-007382ec)
- 新版 `00738320`（命令位置の公開資料なし） · `0073832c`（命令位置の公開資料なし）

~~~diff
- 007382e0 ["INT_ADD", "register:40f0:8", ["const:7382e0:8", "const:4:8"]]
- 007382e0 ["CALL", null, ["callee:00480e28:8"]]
+ 00738320 ["INT_ADD", "register:40f0:8", ["const:738320:8", "const:4:8"]]
+ 00738320 ["CALL", null, ["callee:00480e28:8"]]
- 007382e0 bytes c222f597
+ 00738320 bytes c222f597
- 007382ec ["INT_ADD", "register:40f0:8", ["const:7382ec:8", "const:4:8"]]
- 007382ec ["CALL", null, ["callee:00480e28:8"]]
+ 0073832c ["INT_ADD", "register:40f0:8", ["const:73832c:8", "const:4:8"]]
+ 0073832c ["CALL", null, ["callee:00480e28:8"]]
- 007382ec bytes bf22f597
+ 0073832c bytes bf22f597
~~~


<a id="compare-6fcdcf1ec02aafcd25664a6dee07744f"></a>

### [`00738304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738304.md) → [`00738344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/00738344.md) FUN_00738344

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 1件 [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md)
- 新版 呼出元 1件 [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 1件 [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00738318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738304.md#insn-00738318) · [`00738320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738304.md#insn-00738320)
- 新版 `00738358`（命令位置の公開資料なし） · `00738360`（命令位置の公開資料なし）

~~~diff
- 00738318 ["INT_ADD", "register:40f0:8", ["const:738318:8", "const:4:8"]]
- 00738318 ["CALL", null, ["callee:004803f0:8"]]
+ 00738358 ["INT_ADD", "register:40f0:8", ["const:738358:8", "const:4:8"]]
+ 00738358 ["CALL", null, ["callee:004803f0:8"]]
- 00738318 bytes 2620f597
+ 00738358 bytes 2620f597
- 00738320 ["INT_ADD", "register:40f0:8", ["const:738320:8", "const:4:8"]]
- 00738320 ["CALL", null, ["callee:004803f0:8"]]
+ 00738360 ["INT_ADD", "register:40f0:8", ["const:738360:8", "const:4:8"]]
+ 00738360 ["CALL", null, ["callee:004803f0:8"]]
- 00738320 bytes 2420f597
+ 00738360 bytes 2420f597
~~~


<a id="compare-9ff2c8e6be0e53e8ea67dea635ceffff"></a>

### [`00738334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738334.md) → [`00738374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/00738374.md) FUN_00738374

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a14bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a14bf0.md) · 呼出先 2件 [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md) [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md)
- 新版 呼出元 1件 [`00a14d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14d8c.md) · 呼出先 2件 [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00738358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738334.md#insn-00738358) · [`00738394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738334.md#insn-00738394) · [`007383a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738334.md#insn-007383a0)
- 新版 `00738398`（命令位置の公開資料なし） · `007383d4`（命令位置の公開資料なし） · `007383e0`（命令位置の公開資料なし）

~~~diff
- 00738358 ["INT_ADD", "register:40f0:8", ["const:738358:8", "const:4:8"]]
- 00738358 ["CALL", null, ["callee:00480e28:8"]]
+ 00738398 ["INT_ADD", "register:40f0:8", ["const:738398:8", "const:4:8"]]
+ 00738398 ["CALL", null, ["callee:00480e28:8"]]
- 00738358 bytes a422f597
+ 00738398 bytes a422f597
- 00738394 ["INT_ADD", "register:40f0:8", ["const:738394:8", "const:4:8"]]
- 00738394 ["CALL", null, ["callee:00480e28:8"]]
+ 007383d4 ["INT_ADD", "register:40f0:8", ["const:7383d4:8", "const:4:8"]]
+ 007383d4 ["CALL", null, ["callee:00480e28:8"]]
- 00738394 bytes 9522f597
+ 007383d4 bytes 9522f597
- 007383a0 ["INT_ADD", "register:40f0:8", ["const:7383a0:8", "const:4:8"]]
- 007383a0 ["CALL", null, ["callee:00480d48:8"]]
+ 007383e0 ["INT_ADD", "register:40f0:8", ["const:7383e0:8", "const:4:8"]]
+ 007383e0 ["CALL", null, ["callee:00480d48:8"]]
- 007383a0 bytes 5a22f597
+ 007383e0 bytes 5a22f597
~~~


<a id="compare-b033e2976f98d982b7ae0cf6119d5c30"></a>

### [`007383d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/007383d4.md) → [`00738414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/00738414.md) FUN_00738414

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004802b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md) [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md) [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073840c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/007383d4.md#insn-0073840c) · [`0073841c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/007383d4.md#insn-0073841c) · [`00738438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/007383d4.md#insn-00738438)
- 新版 `0073844c`（命令位置の公開資料なし） · `0073845c`（命令位置の公開資料なし） · `00738478`（命令位置の公開資料なし）

~~~diff
- 0073840c ["INT_ADD", "register:40f0:8", ["const:73840c:8", "const:4:8"]]
- 0073840c ["CALL", null, ["callee:00676a60:8"]]
+ 0073844c ["INT_ADD", "register:40f0:8", ["const:73844c:8", "const:4:8"]]
+ 0073844c ["CALL", null, ["callee:00676a60:8"]]
- 0073840c bytes 85f9fc97
+ 0073844c bytes 85f9fc97
- 0073841c ["INT_ADD", "register:40f0:8", ["const:73841c:8", "const:4:8"]]
- 0073841c ["CALL", null, ["callee:004803f0:8"]]
+ 0073845c ["INT_ADD", "register:40f0:8", ["const:73845c:8", "const:4:8"]]
+ 0073845c ["CALL", null, ["callee:004803f0:8"]]
- 0073841c bytes e51ff597
+ 0073845c bytes e51ff597
- 00738438 ["INT_ADD", "register:40f0:8", ["const:738438:8", "const:4:8"]]
- 00738438 ["CALL", null, ["callee:0043bba4:8"]]
+ 00738478 ["INT_ADD", "register:40f0:8", ["const:738478:8", "const:4:8"]]
+ 00738478 ["CALL", null, ["callee:0043bba4:8"]]
- 00738438 bytes cb0df497
+ 00738478 bytes cb0df497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7853c80a754e2968d10082acc0922ef4"></a>

### [`0073851c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/0073851c.md) → [`0073855c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/0073855c.md) FUN_0073855c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a14bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a14bf0.md) · 呼出先 2件 [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md) [`00481058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481058.md)
- 新版 呼出元 1件 [`00a14d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14d8c.md) · 呼出先 2件 [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) [`00481098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481098.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073853c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/0073851c.md#insn-0073853c)
- 新版 `0073857c`（命令位置の公開資料なし）

~~~diff
- 0073853c ["INT_ADD", "register:40f0:8", ["const:73853c:8", "const:4:8"]]
- 0073853c ["CALL", null, ["callee:00480d48:8"]]
+ 0073857c ["INT_ADD", "register:40f0:8", ["const:73857c:8", "const:4:8"]]
+ 0073857c ["CALL", null, ["callee:00480d48:8"]]
- 0073853c bytes f321f597
+ 0073857c bytes f321f597
~~~


<a id="compare-5f86e4c73d7de608d1146c5c5660cb1a"></a>

### [`00738554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738554.md) → [`00738594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/00738594.md) FUN_00738594

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 2件 [`004802b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md) [`00480704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md)
- 新版 呼出元 1件 [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 2件 [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md) [`00480744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073856c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738554.md#insn-0073856c) · [`0073857c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738554.md#insn-0073857c)
- 新版 `007385ac`（命令位置の公開資料なし） · `007385bc`（命令位置の公開資料なし）

~~~diff
- 0073856c ["INT_ADD", "register:40f0:8", ["const:73856c:8", "const:4:8"]]
- 0073856c ["CALL", null, ["callee:004802f8:8"]]
+ 007385ac ["INT_ADD", "register:40f0:8", ["const:7385ac:8", "const:4:8"]]
+ 007385ac ["CALL", null, ["callee:004802f8:8"]]
- 0073856c bytes 531ff597
+ 007385ac bytes 531ff597
- 0073857c ["INT_ADD", "register:40f0:8", ["const:73857c:8", "const:4:8"]]
- 0073857c ["CALL", null, ["callee:00480744:8"]]
+ 007385bc ["INT_ADD", "register:40f0:8", ["const:7385bc:8", "const:4:8"]]
+ 007385bc ["CALL", null, ["callee:00480744:8"]]
- 0073857c bytes 6220f597
+ 007385bc bytes 6220f597
~~~


<a id="compare-2927b7263841ddadbff57d432836fca9"></a>

### [`00738590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738590.md) → [`007385d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/007385d0.md) FUN_007385d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 7件 [`00480af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480af8.md) [`00480b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480b50.md) [`00480ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ba8.md) [`00480cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480cb0.md) [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md)
- 新版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 7件 [`00480b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md) [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md) [`00480be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md) [`00480cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480cf0.md) [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007385b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738590.md#insn-007385b4) · [`007385c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738590.md#insn-007385c0) · [`007385cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738590.md#insn-007385cc)
- 新版 `007385f4`（命令位置の公開資料なし） · `00738600`（命令位置の公開資料なし） · `0073860c`（命令位置の公開資料なし）

~~~diff
- 007385b4 ["INT_ADD", "register:40f0:8", ["const:7385b4:8", "const:4:8"]]
- 007385b4 ["CALL", null, ["callee:00480d48:8"]]
+ 007385f4 ["INT_ADD", "register:40f0:8", ["const:7385f4:8", "const:4:8"]]
+ 007385f4 ["CALL", null, ["callee:00480d48:8"]]
- 007385b4 bytes d521f597
+ 007385f4 bytes d521f597
- 007385c0 ["INT_ADD", "register:40f0:8", ["const:7385c0:8", "const:4:8"]]
- 007385c0 ["CALL", null, ["callee:00481098:8"]]
+ 00738600 ["INT_ADD", "register:40f0:8", ["const:738600:8", "const:4:8"]]
+ 00738600 ["CALL", null, ["callee:00481098:8"]]
- 007385c0 bytes a622f597
+ 00738600 bytes a622f597
- 007385cc ["INT_ADD", "register:40f0:8", ["const:7385cc:8", "const:4:8"]]
- 007385cc ["CALL", null, ["callee:00481098:8"]]
+ 0073860c ["INT_ADD", "register:40f0:8", ["const:73860c:8", "const:4:8"]]
+ 0073860c ["CALL", null, ["callee:00481098:8"]]
- 007385cc bytes a322f597
+ 0073860c bytes a322f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-767a9c425b9dd1f8ad373b706d9af964"></a>

### [`0073876c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/0073876c.md) → [`007387ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/007387ac.md) FUN_007387ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 10件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004800d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004800d8.md) [`00480138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480138.md) [`00480198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480198.md) [`004802b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md)
- 新版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 10件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00480118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480118.md) [`00480178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md) [`004801d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004801d8.md) [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073879c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/0073876c.md#insn-0073879c) · [`007387ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/0073876c.md#insn-007387ac) · [`007387b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/0073876c.md#insn-007387b8)
- 新版 `007387dc`（命令位置の公開資料なし） · `007387ec`（命令位置の公開資料なし） · `007387f8`（命令位置の公開資料なし）

~~~diff
- 0073879c ["INT_ADD", "register:40f0:8", ["const:73879c:8", "const:4:8"]]
- 0073879c ["CALL", null, ["callee:004802f8:8"]]
+ 007387dc ["INT_ADD", "register:40f0:8", ["const:7387dc:8", "const:4:8"]]
+ 007387dc ["CALL", null, ["callee:004802f8:8"]]
- 0073879c bytes c71ef597
+ 007387dc bytes c71ef597
- 007387ac ["INT_ADD", "register:40f0:8", ["const:7387ac:8", "const:4:8"]]
- 007387ac ["CALL", null, ["callee:00480744:8"]]
+ 007387ec ["INT_ADD", "register:40f0:8", ["const:7387ec:8", "const:4:8"]]
+ 007387ec ["CALL", null, ["callee:00480744:8"]]
- 007387ac bytes d61ff597
+ 007387ec bytes d61ff597
- 007387b8 ["INT_ADD", "register:40f0:8", ["const:7387b8:8", "const:4:8"]]
- 007387b8 ["CALL", null, ["callee:00480744:8"]]
+ 007387f8 ["INT_ADD", "register:40f0:8", ["const:7387f8:8", "const:4:8"]]
+ 007387f8 ["CALL", null, ["callee:00480744:8"]]
- 007387b8 bytes d31ff597
+ 007387f8 bytes d31ff597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53eeed23ee42eea93da4e6abde26feb9"></a>

### [`00738b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738b48.md) → [`00738b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/00738b88.md) FUN_00738b88

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00a955d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a95/00a955d0.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00736bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00736/00736bdc.md) [`0073a2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a2c4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00a957c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a95/00a957c8.md) · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00736c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00736/00736c1c.md) [`0073a304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073a304.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00738b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738b48.md#insn-00738b68) · [`00738bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738b48.md#insn-00738bd0) · [`00738c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738b48.md#insn-00738c0c)
- 新版 `00738ba8`（命令位置の公開資料なし） · `00738c10`（命令位置の公開資料なし） · `00738c4c`（命令位置の公開資料なし）

~~~diff
- 00738b68 ["INT_ADD", "register:40f0:8", ["const:738b68:8", "const:4:8"]]
- 00738b68 ["CALL", null, ["callee:0048ce84:8"]]
+ 00738ba8 ["INT_ADD", "register:40f0:8", ["const:738ba8:8", "const:4:8"]]
+ 00738ba8 ["CALL", null, ["callee:0048ce84:8"]]
- 00738b68 bytes b750f597
+ 00738ba8 bytes b750f597
- 00738bd0 ["INT_ADD", "register:40f0:8", ["const:738bd0:8", "const:4:8"]]
- 00738bd0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00738c10 ["INT_ADD", "register:40f0:8", ["const:738c10:8", "const:4:8"]]
+ 00738c10 ["CALL", null, ["callee:00c57e90:8"]]
- 00738bd0 bytes b07b1494
+ 00738c10 bytes a07c1494
- 00738c0c ["INT_ADD", "register:40f0:8", ["const:738c0c:8", "const:4:8"]]
- 00738c0c ["CALL", null, ["callee:0043bba4:8"]]
+ 00738c4c ["INT_ADD", "register:40f0:8", ["const:738c4c:8", "const:4:8"]]
+ 00738c4c ["CALL", null, ["callee:0043bba4:8"]]
- 00738c0c bytes d60bf497
+ 00738c4c bytes d60bf497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da919fbdef59ee95ed8c9c76df684511"></a>

### [`00738fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738fb8.md) → [`00738ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/00738ff8.md) FUN_00738ff8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00738fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738fb8.md#insn-00738fd0)
- 新版 `00739010`（命令位置の公開資料なし）

~~~diff
- 00738fd0 ["INT_ADD", "register:40f0:8", ["const:738fd0:8", "const:4:8"]]
- 00738fd0 ["CALL", null, ["callee:005c179c:8"]]
+ 00739010 ["INT_ADD", "register:40f0:8", ["const:739010:8", "const:4:8"]]
+ 00739010 ["CALL", null, ["callee:005c179c:8"]]
- 00738fd0 bytes e321fa97
+ 00739010 bytes e321fa97
~~~


<a id="compare-c5d21221ea608dc7610de79aec4a13a3"></a>

### [`00739330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/00739330.md) → [`00739370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00739/00739370.md) FUN_00739370

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00739304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/00739304.md) · 呼出先 1件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md)
- 新版 呼出元 1件 [`00739344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00739/00739344.md) · 呼出先 1件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00739398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/00739330.md#insn-00739398) · [`007393dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/00739330.md#insn-007393dc) · [`00739428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/00739330.md#insn-00739428)
- 新版 `007393d8`（命令位置の公開資料なし） · `0073941c`（命令位置の公開資料なし） · `00739468`（命令位置の公開資料なし）

~~~diff
- 00739398 ["INT_ADD", "register:40f0:8", ["const:739398:8", "const:4:8"]]
- 00739398 ["CALL", null, ["callee:005c179c:8"]]
+ 007393d8 ["INT_ADD", "register:40f0:8", ["const:7393d8:8", "const:4:8"]]
+ 007393d8 ["CALL", null, ["callee:005c179c:8"]]
- 00739398 bytes f120fa97
+ 007393d8 bytes f120fa97
- 007393dc ["INT_ADD", "register:40f0:8", ["const:7393dc:8", "const:4:8"]]
- 007393dc ["CALL", null, ["callee:005c179c:8"]]
+ 0073941c ["INT_ADD", "register:40f0:8", ["const:73941c:8", "const:4:8"]]
+ 0073941c ["CALL", null, ["callee:005c179c:8"]]
- 007393dc bytes e020fa97
+ 0073941c bytes e020fa97
- 00739428 ["INT_ADD", "register:40f0:8", ["const:739428:8", "const:4:8"]]
- 00739428 ["CALL", null, ["callee:005c179c:8"]]
+ 00739468 ["INT_ADD", "register:40f0:8", ["const:739468:8", "const:4:8"]]
+ 00739468 ["CALL", null, ["callee:005c179c:8"]]
- 00739428 bytes cd20fa97
+ 00739468 bytes cd20fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19b3f11b89c21356f4531e427b40fefc"></a>

### [`00739e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/00739e04.md) → [`00739e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00739/00739e44.md) FUN_00739e44

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) · 呼出先 1件 [`00727cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727cdc.md)
- 新版 呼出元 1件 [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) · 呼出先 1件 [`00727d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727d1c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00739e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/00739e04.md#insn-00739e20)
- 新版 `00739e60`（命令位置の公開資料なし）

~~~diff
- 00739e20 ["INT_ADD", "register:40f0:8", ["const:739e20:8", "const:4:8"]]
- 00739e20 ["CALL", null, ["callee:00727d1c:8"]]
+ 00739e60 ["INT_ADD", "register:40f0:8", ["const:739e60:8", "const:4:8"]]
+ 00739e60 ["CALL", null, ["callee:00727d1c:8"]]
- 00739e20 bytes afb7ff97
+ 00739e60 bytes afb7ff97
~~~


<a id="compare-e0d96bdcd0fe1dadcec89512c2c5650b"></a>

### [`00739efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/00739efc.md) → [`00739f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00739/00739f3c.md) FUN_00739f3c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00737e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/00737e4c.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0073a028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a028.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00737e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00737/00737e8c.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0073a068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073a068.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00739f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/00739efc.md#insn-00739f34) · [`00739f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/00739efc.md#insn-00739f54) · [`00739f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/00739efc.md#insn-00739f88)
- 新版 `00739f74`（命令位置の公開資料なし） · `00739f94`（命令位置の公開資料なし） · `00739fc8`（命令位置の公開資料なし）

~~~diff
- 00739f34 ["INT_ADD", "register:40f0:8", ["const:739f34:8", "const:4:8"]]
- 00739f34 ["CALL", null, ["callee:0073a068:8"]]
+ 00739f74 ["INT_ADD", "register:40f0:8", ["const:739f74:8", "const:4:8"]]
+ 00739f74 ["CALL", null, ["callee:0073a068:8"]]
- 00739f34 bytes 3d000094
+ 00739f74 bytes 3d000094
- 00739f54 ["INT_ADD", "register:40f0:8", ["const:739f54:8", "const:4:8"]]
- 00739f54 ["CALL", null, ["callee:00c57e90:8"]]
+ 00739f94 ["INT_ADD", "register:40f0:8", ["const:739f94:8", "const:4:8"]]
+ 00739f94 ["CALL", null, ["callee:00c57e90:8"]]
- 00739f54 bytes cf761494
+ 00739f94 bytes bf771494
- 00739f88 ["INT_ADD", "register:40f0:8", ["const:739f88:8", "const:4:8"]]
- 00739f88 ["CALL", null, ["callee:0043bb20:8"]]
+ 00739fc8 ["INT_ADD", "register:40f0:8", ["const:739fc8:8", "const:4:8"]]
+ 00739fc8 ["CALL", null, ["callee:0043bb20:8"]]
- 00739f88 bytes d606f497
+ 00739fc8 bytes d606f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbeaadde40bdbd86abd7309d8a0807a5"></a>

### [`0073a028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a028.md) → [`0073a068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073a068.md) FUN_0073a068

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00739efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/00739efc.md) · 呼出先 2件 [`0063947c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/0063947c.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00739f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00739/00739f3c.md) · 呼出先 2件 [`006394bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00639/006394bc.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073a0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a028.md#insn-0073a0b0) · [`0073a104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a028.md#insn-0073a104) · [`0073a1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a028.md#insn-0073a1a0)
- 新版 `0073a0f0`（命令位置の公開資料なし） · `0073a144`（命令位置の公開資料なし） · `0073a1e0`（命令位置の公開資料なし）

~~~diff
- 0073a0b0 ["INT_ADD", "register:40f0:8", ["const:73a0b0:8", "const:4:8"]]
- 0073a0b0 ["CALL", null, ["callee:00c58050:8"]]
+ 0073a0f0 ["INT_ADD", "register:40f0:8", ["const:73a0f0:8", "const:4:8"]]
+ 0073a0f0 ["CALL", null, ["callee:00c58050:8"]]
- 0073a0b0 bytes e8761494
+ 0073a0f0 bytes d8771494
- 0073a104 ["INT_ADD", "register:40f0:8", ["const:73a104:8", "const:4:8"]]
- 0073a104 ["CALL", null, ["callee:00c58050:8"]]
+ 0073a144 ["INT_ADD", "register:40f0:8", ["const:73a144:8", "const:4:8"]]
+ 0073a144 ["CALL", null, ["callee:00c58050:8"]]
- 0073a104 bytes d3761494
+ 0073a144 bytes c3771494
- 0073a1a0 ["INT_ADD", "register:40f0:8", ["const:73a1a0:8", "const:4:8"]]
- 0073a1a0 ["CALL", null, ["callee:00c58050:8"]]
+ 0073a1e0 ["INT_ADD", "register:40f0:8", ["const:73a1e0:8", "const:4:8"]]
+ 0073a1e0 ["CALL", null, ["callee:00c58050:8"]]
- 0073a1a0 bytes ac761494
+ 0073a1e0 bytes 9c771494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccb8b9c0c4849abb5a03ba15ea363d29"></a>

### [`0073a2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a2c4.md) → [`0073a304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073a304.md) FUN_0073a304

採用 · 移動量 `+0x40` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 10件 [`00737e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/00737e4c.md) [`00738b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738b48.md) [`00739464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/00739464.md) [`0073a2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a2c4.md) [`0073ae08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae08.md) · 呼出先 2件 [`0073a2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a2c4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 10件 [`00737e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00737/00737e8c.md) [`00738b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/00738b88.md) [`007394a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00739/007394a4.md) [`0073a304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073a304.md) [`0073ae48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073ae48.md) · 呼出先 2件 [`0073a304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073a304.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073a2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a2c4.md#insn-0073a2e0) · [`0073a2ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a2c4.md#insn-0073a2ec) · [`0073a2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a2c4.md#insn-0073a2fc)
- 新版 `0073a320`（命令位置の公開資料なし） · `0073a32c`（命令位置の公開資料なし） · `0073a33c`（命令位置の公開資料なし）

~~~diff
- 0073a2e0 ["INT_ADD", "register:40f0:8", ["const:73a2e0:8", "const:4:8"]]
- 0073a2e0 ["CALL", null, ["local:b0:8"]]
+ 0073a320 ["INT_ADD", "register:40f0:8", ["const:73a320:8", "const:4:8"]]
+ 0073a320 ["CALL", null, ["local:b0:8"]]
- 0073a2e0 bytes f9ffff97
+ 0073a320 bytes f9ffff97
- 0073a2ec ["INT_ADD", "register:40f0:8", ["const:73a2ec:8", "const:4:8"]]
- 0073a2ec ["CALL", null, ["local:b0:8"]]
+ 0073a32c ["INT_ADD", "register:40f0:8", ["const:73a32c:8", "const:4:8"]]
+ 0073a32c ["CALL", null, ["local:b0:8"]]
- 0073a2ec bytes f6ffff97
+ 0073a32c bytes f6ffff97
- 0073a2fc ["INT_ADD", "register:40f0:8", ["const:73a2fc:8", "const:4:8"]]
- 0073a2fc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0073a33c ["INT_ADD", "register:40f0:8", ["const:73a33c:8", "const:4:8"]]
+ 0073a33c ["CALL", null, ["callee:00c57eb0:8"]]
- 0073a2fc bytes ed751494
+ 0073a33c bytes dd761494
~~~


<a id="compare-46899ab9cff3917ab294d295a728a8a8"></a>

### [`0073ae08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae08.md) → [`0073ae48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073ae48.md) FUN_0073ae48

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00734260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734260.md) [`007380a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/007380a4.md) [`0073ae08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae08.md) [`008480e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008480e8.md) · 呼出先 3件 [`0073a2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a2c4.md) [`0073ae08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae08.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`007342a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/007342a0.md) [`007380e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/007380e4.md) [`0073ae48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073ae48.md) [`00848128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848128.md) · 呼出先 3件 [`0073a304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073a304.md) [`0073ae48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073ae48.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073ae28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae08.md#insn-0073ae28) · [`0073ae34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae08.md#insn-0073ae34) · [`0073ae40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae08.md#insn-0073ae40)
- 新版 `0073ae68`（命令位置の公開資料なし） · `0073ae74`（命令位置の公開資料なし） · `0073ae80`（命令位置の公開資料なし）

~~~diff
- 0073ae28 ["INT_ADD", "register:40f0:8", ["const:73ae28:8", "const:4:8"]]
- 0073ae28 ["CALL", null, ["local:b0:8"]]
+ 0073ae68 ["INT_ADD", "register:40f0:8", ["const:73ae68:8", "const:4:8"]]
+ 0073ae68 ["CALL", null, ["local:b0:8"]]
- 0073ae28 bytes f8ffff97
+ 0073ae68 bytes f8ffff97
- 0073ae34 ["INT_ADD", "register:40f0:8", ["const:73ae34:8", "const:4:8"]]
- 0073ae34 ["CALL", null, ["local:b0:8"]]
+ 0073ae74 ["INT_ADD", "register:40f0:8", ["const:73ae74:8", "const:4:8"]]
+ 0073ae74 ["CALL", null, ["local:b0:8"]]
- 0073ae34 bytes f5ffff97
+ 0073ae74 bytes f5ffff97
- 0073ae40 ["INT_ADD", "register:40f0:8", ["const:73ae40:8", "const:4:8"]]
- 0073ae40 ["CALL", null, ["callee:0073a304:8"]]
+ 0073ae80 ["INT_ADD", "register:40f0:8", ["const:73ae80:8", "const:4:8"]]
+ 0073ae80 ["CALL", null, ["callee:0073a304:8"]]
- 0073ae40 bytes 21fdff97
+ 0073ae80 bytes 21fdff97
~~~


<a id="compare-09c69e272d293f599f6d03ad649ce77c"></a>

### [`0073ae58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae58.md) → [`0073ae98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073ae98.md) FUN_0073ae98

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00734260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734260.md) [`0073876c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/0073876c.md) [`0073ae58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae58.md) [`008480e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008480e8.md) · 呼出先 2件 [`0073ae58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae58.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`007342a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/007342a0.md) [`007387ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/007387ac.md) [`0073ae98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073ae98.md) [`00848128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848128.md) · 呼出先 2件 [`0073ae98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073ae98.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073ae78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae58.md#insn-0073ae78) · [`0073ae84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae58.md#insn-0073ae84)
- 新版 `0073aeb8`（命令位置の公開資料なし） · `0073aec4`（命令位置の公開資料なし）

~~~diff
- 0073ae78 ["INT_ADD", "register:40f0:8", ["const:73ae78:8", "const:4:8"]]
- 0073ae78 ["CALL", null, ["local:b0:8"]]
+ 0073aeb8 ["INT_ADD", "register:40f0:8", ["const:73aeb8:8", "const:4:8"]]
+ 0073aeb8 ["CALL", null, ["local:b0:8"]]
- 0073ae78 bytes f8ffff97
+ 0073aeb8 bytes f8ffff97
- 0073ae84 ["INT_ADD", "register:40f0:8", ["const:73ae84:8", "const:4:8"]]
- 0073ae84 ["CALL", null, ["local:b0:8"]]
+ 0073aec4 ["INT_ADD", "register:40f0:8", ["const:73aec4:8", "const:4:8"]]
+ 0073aec4 ["CALL", null, ["local:b0:8"]]
- 0073ae84 bytes f5ffff97
+ 0073aec4 bytes f5ffff97
~~~


<a id="compare-40dafeaea960544f4680c0ac329aa7ec"></a>

### [`0073ae9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae9c.md) → [`0073aedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073aedc.md) FUN_0073aedc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007350b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/007350b4.md) [`0073ae9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae9c.md) [`008480e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008480e8.md) · 呼出先 2件 [`0073ae9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae9c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`007350f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/007350f4.md) [`0073aedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073aedc.md) [`00848128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848128.md) · 呼出先 2件 [`0073aedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073aedc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073aebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae9c.md#insn-0073aebc) · [`0073aec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae9c.md#insn-0073aec8)
- 新版 `0073aefc`（命令位置の公開資料なし） · `0073af08`（命令位置の公開資料なし）

~~~diff
- 0073aebc ["INT_ADD", "register:40f0:8", ["const:73aebc:8", "const:4:8"]]
- 0073aebc ["CALL", null, ["local:b0:8"]]
+ 0073aefc ["INT_ADD", "register:40f0:8", ["const:73aefc:8", "const:4:8"]]
+ 0073aefc ["CALL", null, ["local:b0:8"]]
- 0073aebc bytes f8ffff97
+ 0073aefc bytes f8ffff97
- 0073aec8 ["INT_ADD", "register:40f0:8", ["const:73aec8:8", "const:4:8"]]
- 0073aec8 ["CALL", null, ["local:b0:8"]]
+ 0073af08 ["INT_ADD", "register:40f0:8", ["const:73af08:8", "const:4:8"]]
+ 0073af08 ["CALL", null, ["local:b0:8"]]
- 0073aec8 bytes f5ffff97
+ 0073af08 bytes f5ffff97
~~~


<a id="compare-6481c019c8eeb4058bd83b303c519ba4"></a>

### [`0073af1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073af1c.md) → [`0073af5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073af5c.md) FUN_0073af5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007366c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00736/007366c4.md) [`00736bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00736/00736bdc.md) · 呼出先 3件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`0073a2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a2c4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00736704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00736/00736704.md) [`00736c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00736/00736c1c.md) · 呼出先 3件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`0073a304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073a304.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073afcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073af1c.md#insn-0073afcc) · [`0073afd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073af1c.md#insn-0073afd8) · [`0073afe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073af1c.md#insn-0073afe0)
- 新版 `0073b00c`（命令位置の公開資料なし） · `0073b018`（命令位置の公開資料なし） · `0073b020`（命令位置の公開資料なし）

~~~diff
- 0073afcc ["INT_ADD", "register:40f0:8", ["const:73afcc:8", "const:4:8"]]
- 0073afcc ["CALL", null, ["callee:00494610:8"]]
+ 0073b00c ["INT_ADD", "register:40f0:8", ["const:73b00c:8", "const:4:8"]]
+ 0073b00c ["CALL", null, ["callee:00494610:8"]]
- 0073afcc bytes 8165f597
+ 0073b00c bytes 8165f597
- 0073afd8 ["INT_ADD", "register:40f0:8", ["const:73afd8:8", "const:4:8"]]
- 0073afd8 ["CALL", null, ["callee:0073a304:8"]]
+ 0073b018 ["INT_ADD", "register:40f0:8", ["const:73b018:8", "const:4:8"]]
+ 0073b018 ["CALL", null, ["callee:0073a304:8"]]
- 0073afd8 bytes bbfcff97
+ 0073b018 bytes bbfcff97
- 0073afe0 ["INT_ADD", "register:40f0:8", ["const:73afe0:8", "const:4:8"]]
- 0073afe0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0073b020 ["INT_ADD", "register:40f0:8", ["const:73b020:8", "const:4:8"]]
+ 0073b020 ["CALL", null, ["callee:00c57eb0:8"]]
- 0073afe0 bytes b4721494
+ 0073b020 bytes a4731494
~~~


<a id="compare-27fcb7e971414bf41e8df078087e24e8"></a>

### [`0073aff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073aff4.md) → [`0073b034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b034.md) FUN_0073b034

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00738d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738d20.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`0073b228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073b/0073b228.md) [`0073b3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073b/0073b3e8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00738d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/00738d60.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`0073b268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b268.md) [`0073b428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b428.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073b0ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073aff4.md#insn-0073b0ac) · [`0073b15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073aff4.md#insn-0073b15c) · [`0073b180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073aff4.md#insn-0073b180)
- 新版 `0073b0ec`（命令位置の公開資料なし） · `0073b19c`（命令位置の公開資料なし） · `0073b1c0`（命令位置の公開資料なし）

~~~diff
- 0073b0ac ["INT_ADD", "register:40f0:8", ["const:73b0ac:8", "const:4:8"]]
- 0073b0ac ["CALL", null, ["callee:00c57e90:8"]]
+ 0073b0ec ["INT_ADD", "register:40f0:8", ["const:73b0ec:8", "const:4:8"]]
+ 0073b0ec ["CALL", null, ["callee:00c57e90:8"]]
- 0073b0ac bytes 79721494
+ 0073b0ec bytes 69731494
- 0073b15c ["INT_ADD", "register:40f0:8", ["const:73b15c:8", "const:4:8"]]
- 0073b15c ["CALL", null, ["callee:0073b268:8"]]
+ 0073b19c ["INT_ADD", "register:40f0:8", ["const:73b19c:8", "const:4:8"]]
+ 0073b19c ["CALL", null, ["callee:0073b268:8"]]
- 0073b15c bytes 33000094
+ 0073b19c bytes 33000094
- 0073b180 ["INT_ADD", "register:40f0:8", ["const:73b180:8", "const:4:8"]]
- 0073b180 ["CALL", null, ["callee:005c179c:8"]]
+ 0073b1c0 ["INT_ADD", "register:40f0:8", ["const:73b1c0:8", "const:4:8"]]
+ 0073b1c0 ["CALL", null, ["callee:005c179c:8"]]
- 0073b180 bytes 7719fa97
+ 0073b1c0 bytes 7719fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-deabea14cb8acd2326fcfb6ad391b229"></a>

### [`0073b228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073b/0073b228.md) → [`0073b268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b268.md) FUN_0073b268

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0073aff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073aff4.md) · 呼出先 1件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md)
- 新版 呼出元 1件 [`0073b034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b034.md) · 呼出先 1件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073b308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073b/0073b228.md#insn-0073b308) · [`0073b314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073b/0073b228.md#insn-0073b314)
- 新版 `0073b348`（命令位置の公開資料なし） · `0073b354`（命令位置の公開資料なし）

~~~diff
- 0073b308 ["INT_ADD", "register:40f0:8", ["const:73b308:8", "const:4:8"]]
- 0073b308 ["CALL", null, ["callee:005c179c:8"]]
+ 0073b348 ["INT_ADD", "register:40f0:8", ["const:73b348:8", "const:4:8"]]
+ 0073b348 ["CALL", null, ["callee:005c179c:8"]]
- 0073b308 bytes 1519fa97
+ 0073b348 bytes 1519fa97
- 0073b314 ["INT_ADD", "register:40f0:8", ["const:73b314:8", "const:4:8"]]
- 0073b314 ["CALL", null, ["callee:005c179c:8"]]
+ 0073b354 ["INT_ADD", "register:40f0:8", ["const:73b354:8", "const:4:8"]]
+ 0073b354 ["CALL", null, ["callee:005c179c:8"]]
- 0073b314 bytes 1219fa97
+ 0073b354 bytes 1219fa97
~~~


<a id="compare-263de4daa8553a227d0fc270f13a7313"></a>

### [`0073b374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073b/0073b374.md) → [`0073b3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b3b4.md) FUN_0073b3b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073b3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073b/0073b374.md#insn-0073b3a4) · [`0073b3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073b/0073b374.md#insn-0073b3b0)
- 新版 `0073b3e4`（命令位置の公開資料なし） · `0073b3f0`（命令位置の公開資料なし）

~~~diff
- 0073b3a4 ["INT_ADD", "register:40f0:8", ["const:73b3a4:8", "const:4:8"]]
- 0073b3a4 ["CALL", null, ["callee:005c179c:8"]]
+ 0073b3e4 ["INT_ADD", "register:40f0:8", ["const:73b3e4:8", "const:4:8"]]
+ 0073b3e4 ["CALL", null, ["callee:005c179c:8"]]
- 0073b3a4 bytes ee18fa97
+ 0073b3e4 bytes ee18fa97
- 0073b3b0 ["INT_ADD", "register:40f0:8", ["const:73b3b0:8", "const:4:8"]]
- 0073b3b0 ["CALL", null, ["callee:005c179c:8"]]
+ 0073b3f0 ["INT_ADD", "register:40f0:8", ["const:73b3f0:8", "const:4:8"]]
+ 0073b3f0 ["CALL", null, ["callee:005c179c:8"]]
- 0073b3b0 bytes eb18fa97
+ 0073b3f0 bytes eb18fa97
~~~


<a id="compare-08c08cd03d223cc768205738edf5659a"></a>

### [`0073b3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073b/0073b3fc.md) → [`0073b43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b43c.md) FUN_0073b43c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073b434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073b/0073b3fc.md#insn-0073b434) · [`0073b440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073b/0073b3fc.md#insn-0073b440)
- 新版 `0073b474`（命令位置の公開資料なし） · `0073b480`（命令位置の公開資料なし）

~~~diff
- 0073b434 ["INT_ADD", "register:40f0:8", ["const:73b434:8", "const:4:8"]]
- 0073b434 ["CALL", null, ["callee:005c179c:8"]]
+ 0073b474 ["INT_ADD", "register:40f0:8", ["const:73b474:8", "const:4:8"]]
+ 0073b474 ["CALL", null, ["callee:005c179c:8"]]
- 0073b434 bytes ca18fa97
+ 0073b474 bytes ca18fa97
- 0073b440 ["INT_ADD", "register:40f0:8", ["const:73b440:8", "const:4:8"]]
- 0073b440 ["CALL", null, ["callee:005c179c:8"]]
+ 0073b480 ["INT_ADD", "register:40f0:8", ["const:73b480:8", "const:4:8"]]
+ 0073b480 ["CALL", null, ["callee:005c179c:8"]]
- 0073b440 bytes c718fa97
+ 0073b480 bytes c718fa97
~~~


<a id="compare-dc26510f30a48e72e95f6a68d0f9a572"></a>

### [`0073b460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073b/0073b460.md) → [`0073b4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b4a0.md) FUN_0073b4a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007391b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/007391b0.md) · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`007391f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00739/007391f0.md) · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073b4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073b/0073b460.md#insn-0073b4b4) · [`0073b4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073b/0073b460.md#insn-0073b4c0)
- 新版 `0073b4f4`（命令位置の公開資料なし） · `0073b500`（命令位置の公開資料なし）

~~~diff
- 0073b4b4 ["INT_ADD", "register:40f0:8", ["const:73b4b4:8", "const:4:8"]]
- 0073b4b4 ["CALL", null, ["callee:005c179c:8"]]
+ 0073b4f4 ["INT_ADD", "register:40f0:8", ["const:73b4f4:8", "const:4:8"]]
+ 0073b4f4 ["CALL", null, ["callee:005c179c:8"]]
- 0073b4b4 bytes aa18fa97
+ 0073b4f4 bytes aa18fa97
- 0073b4c0 ["INT_ADD", "register:40f0:8", ["const:73b4c0:8", "const:4:8"]]
- 0073b4c0 ["CALL", null, ["callee:005c179c:8"]]
+ 0073b500 ["INT_ADD", "register:40f0:8", ["const:73b500:8", "const:4:8"]]
+ 0073b500 ["CALL", null, ["callee:005c179c:8"]]
- 0073b4c0 bytes a718fa97
+ 0073b500 bytes a718fa97
~~~


<a id="compare-30f3fdbda55b92f22bb4e55bb185f1fd"></a>

### [`0073b4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073b/0073b4f4.md) → [`0073b534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b534.md) FUN_0073b534

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007391b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/007391b0.md) · 呼出先 2件 [`006917c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00691/006917c0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`007391f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00739/007391f0.md) · 呼出先 2件 [`00691800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691800.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073b574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073b/0073b4f4.md#insn-0073b574) · [`0073b594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073b/0073b4f4.md#insn-0073b594) · [`0073b628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073b/0073b4f4.md#insn-0073b628)
- 新版 `0073b5b4`（命令位置の公開資料なし） · `0073b5d4`（命令位置の公開資料なし） · `0073b668`（命令位置の公開資料なし）

~~~diff
- 0073b574 ["INT_ADD", "register:40f0:8", ["const:73b574:8", "const:4:8"]]
- 0073b574 ["CALL", null, ["callee:00691800:8"]]
+ 0073b5b4 ["INT_ADD", "register:40f0:8", ["const:73b5b4:8", "const:4:8"]]
+ 0073b5b4 ["CALL", null, ["callee:00691800:8"]]
- 0073b574 bytes 9358fd97
+ 0073b5b4 bytes 9358fd97
- 0073b594 ["INT_ADD", "register:40f0:8", ["const:73b594:8", "const:4:8"]]
- 0073b594 ["CALL", null, ["callee:00691800:8"]]
+ 0073b5d4 ["INT_ADD", "register:40f0:8", ["const:73b5d4:8", "const:4:8"]]
+ 0073b5d4 ["CALL", null, ["callee:00691800:8"]]
- 0073b594 bytes 8b58fd97
+ 0073b5d4 bytes 8b58fd97
- 0073b628 ["INT_ADD", "register:40f0:8", ["const:73b628:8", "const:4:8"]]
- 0073b628 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0073b668 ["INT_ADD", "register:40f0:8", ["const:73b668:8", "const:4:8"]]
+ 0073b668 ["CALL", null, ["callee:00c57ee0:8"]]
- 0073b628 bytes 2e711494
+ 0073b668 bytes 1e721494
~~~


<a id="compare-34d2618016f31d490200ed246240366a"></a>

### [`0073c838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073c/0073c838.md) → [`0073c878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073c/0073c878.md) FUN_0073c878

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073c858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073c/0073c838.md#insn-0073c858) · [`0073c86c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073c/0073c838.md#insn-0073c86c) · [`0073c874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073c/0073c838.md#insn-0073c874)
- 新版 `0073c898`（命令位置の公開資料なし） · `0073c8ac`（命令位置の公開資料なし） · `0073c8b4`（命令位置の公開資料なし）

~~~diff
- 0073c858 ["INT_ADD", "register:40f0:8", ["const:73c858:8", "const:4:8"]]
- 0073c858 ["CALL", null, ["callee:00c53d00:8"]]
+ 0073c898 ["INT_ADD", "register:40f0:8", ["const:73c898:8", "const:4:8"]]
+ 0073c898 ["CALL", null, ["callee:00c53d00:8"]]
- 0073c858 bytes 225c1494
+ 0073c898 bytes 1a5d1494
- 0073c86c ["COPY", "register:0:8", ["register:4040:8"]]
- 0073c86c ["INT_ADD", "register:40f0:8", ["const:73c86c:8", "const:4:8"]]
- 0073c86c ["CALLIND", null, ["register:0:8"]]
+ 0073c8ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 0073c8ac ["INT_ADD", "register:40f0:8", ["const:73c8ac:8", "const:4:8"]]
+ 0073c8ac ["CALLIND", null, ["register:0:8"]]
- 0073c86c bytes 00013fd6
+ 0073c8ac bytes 00013fd6
- 0073c874 ["INT_ADD", "register:40f0:8", ["const:73c874:8", "const:4:8"]]
- 0073c874 ["CALL", null, ["callee:00c57e80:8"]]
+ 0073c8b4 ["INT_ADD", "register:40f0:8", ["const:73c8b4:8", "const:4:8"]]
+ 0073c8b4 ["CALL", null, ["callee:00c57e80:8"]]
- 0073c874 bytes 836c1494
+ 0073c8b4 bytes 736d1494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1470d21cb4047a58bc184f35e36ced56"></a>

### [`0073ed2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073e/0073ed2c.md) → [`0073ed6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073e/0073ed6c.md) FUN_0073ed6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0073d764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073d/0073d764.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 1件 [`0073d7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073d/0073d7a4.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073ed50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073e/0073ed2c.md#insn-0073ed50) · [`0073ed98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073e/0073ed2c.md#insn-0073ed98) · [`0073edb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073e/0073ed2c.md#insn-0073edb8)
- 新版 `0073ed90`（命令位置の公開資料なし） · `0073edd8`（命令位置の公開資料なし） · `0073edf8`（命令位置の公開資料なし）

~~~diff
- 0073ed50 ["INT_ADD", "register:40f0:8", ["const:73ed50:8", "const:4:8"]]
- 0073ed50 ["CALL", null, ["callee:00c57fe0:8"]]
+ 0073ed90 ["INT_ADD", "register:40f0:8", ["const:73ed90:8", "const:4:8"]]
+ 0073ed90 ["CALL", null, ["callee:00c57fe0:8"]]
- 0073ed50 bytes a4631494
+ 0073ed90 bytes 94641494
- 0073ed98 ["INT_ADD", "register:40f0:8", ["const:73ed98:8", "const:4:8"]]
- 0073ed98 ["CALL", null, ["callee:00c57e90:8"]]
+ 0073edd8 ["INT_ADD", "register:40f0:8", ["const:73edd8:8", "const:4:8"]]
+ 0073edd8 ["CALL", null, ["callee:00c57e90:8"]]
- 0073ed98 bytes 3e631494
+ 0073edd8 bytes 2e641494
- 0073edb8 ["INT_ADD", "register:40f0:8", ["const:73edb8:8", "const:4:8"]]
- 0073edb8 ["CALL", null, ["callee:00c57f40:8"]]
+ 0073edf8 ["INT_ADD", "register:40f0:8", ["const:73edf8:8", "const:4:8"]]
+ 0073edf8 ["CALL", null, ["callee:00c57f40:8"]]
- 0073edb8 bytes 62631494
+ 0073edf8 bytes 52641494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46e9ca52d98b81f6e9e38d1f4c84fab5"></a>

### [`00740fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00740/00740fc0.md) → [`00741000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00741/00741000.md) FUN_00741000

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00740e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00740/00740e28.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00740e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00740/00740e68.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00740fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00740/00740fc0.md#insn-00740fd0)
- 新版 `00741010`（命令位置の公開資料なし）

~~~diff
- 00740fd0 ["INT_ADD", "register:40f0:8", ["const:740fd0:8", "const:4:8"]]
- 00740fd0 ["CALL", null, ["callee:00740e68:8"]]
+ 00741010 ["INT_ADD", "register:40f0:8", ["const:741010:8", "const:4:8"]]
+ 00741010 ["CALL", null, ["callee:00740e68:8"]]
- 00740fd0 bytes 96ffff97
+ 00741010 bytes 96ffff97
~~~


<a id="compare-bc4ae0c5293a737186cdfb546e93cc17"></a>

### [`00740fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00740/00740fe4.md) → [`00741024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00741/00741024.md) FUN_00741024

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`0073c8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073c/0073c8f8.md) [`0073d764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073d/0073d764.md) [`0073edf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073e/0073edf4.md) [`00741590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00741/00741590.md) [`00741ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00741/00741ff8.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`005e8158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e8/005e8158.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 8件 [`0073c938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073c/0073c938.md) [`0073d7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073d/0073d7a4.md) [`0073ee34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073e/0073ee34.md) [`007415d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00741/007415d0.md) [`00742038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00742/00742038.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005e8198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e8/005e8198.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00741064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00740/00740fe4.md#insn-00741064) · [`00741098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00740/00740fe4.md#insn-00741098) · [`007410a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00740/00740fe4.md#insn-007410a4)
- 新版 `007410a4`（命令位置の公開資料なし） · `007410d8`（命令位置の公開資料なし） · `007410e4`（命令位置の公開資料なし）

~~~diff
- 00741064 ["INT_ADD", "register:40f0:8", ["const:741064:8", "const:4:8"]]
- 00741064 ["CALL", null, ["callee:00c57e90:8"]]
+ 007410a4 ["INT_ADD", "register:40f0:8", ["const:7410a4:8", "const:4:8"]]
+ 007410a4 ["CALL", null, ["callee:00c57e90:8"]]
- 00741064 bytes 8b5a1494
+ 007410a4 bytes 7b5b1494
- 00741098 ["INT_ADD", "register:40f0:8", ["const:741098:8", "const:4:8"]]
- 00741098 ["CALL", null, ["callee:005e8198:8"]]
+ 007410d8 ["INT_ADD", "register:40f0:8", ["const:7410d8:8", "const:4:8"]]
+ 007410d8 ["CALL", null, ["callee:005e8198:8"]]
- 00741098 bytes 309cfa97
+ 007410d8 bytes 309cfa97
- 007410a4 ["INT_ADD", "register:40f0:8", ["const:7410a4:8", "const:4:8"]]
- 007410a4 ["CALL", null, ["callee:005e8198:8"]]
+ 007410e4 ["INT_ADD", "register:40f0:8", ["const:7410e4:8", "const:4:8"]]
+ 007410e4 ["CALL", null, ["callee:005e8198:8"]]
- 007410a4 bytes 2d9cfa97
+ 007410e4 bytes 2d9cfa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2573fa004083f33fae78ef4c7954e5ea"></a>

### [`00741150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00741/00741150.md) → [`00741190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00741/00741190.md) FUN_00741190

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00741188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00741/00741150.md#insn-00741188)
- 新版 `007411c8`（命令位置の公開資料なし）

~~~diff
- 00741188 ["INT_ADD", "register:40f0:8", ["const:741188:8", "const:4:8"]]
- 00741188 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007411c8 ["INT_ADD", "register:40f0:8", ["const:7411c8:8", "const:4:8"]]
+ 007411c8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00741188 bytes 4a5a1494
+ 007411c8 bytes 3a5b1494
~~~


<a id="compare-935046ade97badb0664383d1083b57bf"></a>

### [`00741238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00741/00741238.md) → [`00741278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00741/00741278.md) FUN_00741278

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0073c8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073c/0073c8f8.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0063670c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/0063670c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`0073c938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073c/0073c938.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0063674c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00636/0063674c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007412a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00741/00741238.md#insn-007412a4) · [`00741314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00741/00741238.md#insn-00741314) · [`00741328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00741/00741238.md#insn-00741328)
- 新版 `007412e4`（命令位置の公開資料なし） · `00741354`（命令位置の公開資料なし） · `00741368`（命令位置の公開資料なし）

~~~diff
- 007412a4 ["INT_ADD", "register:40f0:8", ["const:7412a4:8", "const:4:8"]]
- 007412a4 ["CALL", null, ["callee:00c57e90:8"]]
+ 007412e4 ["INT_ADD", "register:40f0:8", ["const:7412e4:8", "const:4:8"]]
+ 007412e4 ["CALL", null, ["callee:00c57e90:8"]]
- 007412a4 bytes fb591494
+ 007412e4 bytes eb5a1494
- 00741314 ["INT_ADD", "register:40f0:8", ["const:741314:8", "const:4:8"]]
- 00741314 ["CALL", null, ["callee:00c53d00:8"]]
+ 00741354 ["INT_ADD", "register:40f0:8", ["const:741354:8", "const:4:8"]]
+ 00741354 ["CALL", null, ["callee:00c53d00:8"]]
- 00741314 bytes 73491494
+ 00741354 bytes 6b4a1494
- 00741328 ["COPY", "register:0:8", ["register:4040:8"]]
- 00741328 ["INT_ADD", "register:40f0:8", ["const:741328:8", "const:4:8"]]
- 00741328 ["CALLIND", null, ["register:0:8"]]
+ 00741368 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00741368 ["INT_ADD", "register:40f0:8", ["const:741368:8", "const:4:8"]]
+ 00741368 ["CALLIND", null, ["register:0:8"]]
- 00741328 bytes 00013fd6
+ 00741368 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-388843c5f220eff112be25a71e3b75f4"></a>

### [`007429a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00742/007429a0.md) → [`007429e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00742/007429e0.md) FUN_007429e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00742770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00742/00742770.md) [`007fa108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fa/007fa108.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`007427b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00742/007427b0.md) [`007fa148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa148.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00742a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00742/007429a0.md#insn-00742a44) · [`00742a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00742/007429a0.md#insn-00742a7c) · [`00742adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00742/007429a0.md#insn-00742adc)
- 新版 `00742a84`（命令位置の公開資料なし） · `00742abc`（命令位置の公開資料なし） · `00742b1c`（命令位置の公開資料なし）

~~~diff
- 00742a44 ["INT_ADD", "register:40f0:8", ["const:742a44:8", "const:4:8"]]
- 00742a44 ["CALL", null, ["callee:00c57e90:8"]]
+ 00742a84 ["INT_ADD", "register:40f0:8", ["const:742a84:8", "const:4:8"]]
+ 00742a84 ["CALL", null, ["callee:00c57e90:8"]]
- 00742a44 bytes 13541494
+ 00742a84 bytes 03551494
- 00742a7c ["INT_ADD", "register:40f0:8", ["const:742a7c:8", "const:4:8"]]
- 00742a7c ["CALL", null, ["callee:0043bba4:8"]]
+ 00742abc ["INT_ADD", "register:40f0:8", ["const:742abc:8", "const:4:8"]]
+ 00742abc ["CALL", null, ["callee:0043bba4:8"]]
- 00742a7c bytes 3ae4f397
+ 00742abc bytes 3ae4f397
- 00742adc ["INT_ADD", "register:40f0:8", ["const:742adc:8", "const:4:8"]]
- 00742adc ["CALL", null, ["callee:00c57e90:8"]]
+ 00742b1c ["INT_ADD", "register:40f0:8", ["const:742b1c:8", "const:4:8"]]
+ 00742b1c ["CALL", null, ["callee:00c57e90:8"]]
- 00742adc bytes ed531494
+ 00742b1c bytes dd541494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56f26253d8bba05bbc5e4d218c0834c8"></a>

### [`00743d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00743/00743d50.md) → [`00743d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00743/00743d90.md) FUN_00743d90

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 14件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`005c0e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0e4c.md) [`0075959c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00759/0075959c.md) [`0075a3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075a/0075a3d8.md) [`007fa108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fa/007fa108.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 14件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`005c0e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c0e8c.md) [`007595dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00759/007595dc.md) [`0075a418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075a/0075a418.md) [`007fa148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa148.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00743db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00743/00743d50.md#insn-00743db4) · [`00743dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00743/00743d50.md#insn-00743dec)
- 新版 `00743df4`（命令位置の公開資料なし） · `00743e2c`（命令位置の公開資料なし）

~~~diff
- 00743db4 ["INT_ADD", "register:40f0:8", ["const:743db4:8", "const:4:8"]]
- 00743db4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00743df4 ["INT_ADD", "register:40f0:8", ["const:743df4:8", "const:4:8"]]
+ 00743df4 ["CALL", null, ["callee:00c57e90:8"]]
- 00743db4 bytes 374f1494
+ 00743df4 bytes 27501494
- 00743dec ["INT_ADD", "register:40f0:8", ["const:743dec:8", "const:4:8"]]
- 00743dec ["CALL", null, ["callee:0043bba4:8"]]
+ 00743e2c ["INT_ADD", "register:40f0:8", ["const:743e2c:8", "const:4:8"]]
+ 00743e2c ["CALL", null, ["callee:0043bba4:8"]]
- 00743dec bytes 5edff397
+ 00743e2c bytes 5edff397
~~~


<a id="compare-3bf450171059cd60d4d6fdf3f2120dc3"></a>

### [`00743e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00743/00743e1c.md) → [`00743e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00743/00743e5c.md) FUN_00743e5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007fa950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fa/007fa950.md) [`007fbdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fb/007fbdc8.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`007fa990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa990.md) [`007fbe08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fbe08.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00743e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00743/00743e1c.md#insn-00743e84) · [`00743ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00743/00743e1c.md#insn-00743ebc)
- 新版 `00743ec4`（命令位置の公開資料なし） · `00743efc`（命令位置の公開資料なし）

~~~diff
- 00743e84 ["INT_ADD", "register:40f0:8", ["const:743e84:8", "const:4:8"]]
- 00743e84 ["CALL", null, ["callee:00c57e90:8"]]
+ 00743ec4 ["INT_ADD", "register:40f0:8", ["const:743ec4:8", "const:4:8"]]
+ 00743ec4 ["CALL", null, ["callee:00c57e90:8"]]
- 00743e84 bytes 034f1494
+ 00743ec4 bytes f34f1494
- 00743ebc ["INT_ADD", "register:40f0:8", ["const:743ebc:8", "const:4:8"]]
- 00743ebc ["CALL", null, ["callee:0043bba4:8"]]
+ 00743efc ["INT_ADD", "register:40f0:8", ["const:743efc:8", "const:4:8"]]
+ 00743efc ["CALL", null, ["callee:0043bba4:8"]]
- 00743ebc bytes 2adff397
+ 00743efc bytes 2adff397
~~~


<a id="compare-f0fff09ad029e517f26d0ea539a7d853"></a>

### [`00743eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00743/00743eec.md) → [`00743f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00743/00743f2c.md) FUN_00743f2c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`005c0e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0e4c.md) [`00ad688c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad688c.md) [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) [`00adee94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ade/00adee94.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 8件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`005c0e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c0e8c.md) [`00ad6a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6a88.md) [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) [`00adf090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00adf/00adf090.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00743f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00743/00743eec.md#insn-00743f50) · [`00743f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00743/00743eec.md#insn-00743f88)
- 新版 `00743f90`（命令位置の公開資料なし） · `00743fc8`（命令位置の公開資料なし）

~~~diff
- 00743f50 ["INT_ADD", "register:40f0:8", ["const:743f50:8", "const:4:8"]]
- 00743f50 ["CALL", null, ["callee:00c57e90:8"]]
+ 00743f90 ["INT_ADD", "register:40f0:8", ["const:743f90:8", "const:4:8"]]
+ 00743f90 ["CALL", null, ["callee:00c57e90:8"]]
- 00743f50 bytes d04e1494
+ 00743f90 bytes c04f1494
- 00743f88 ["INT_ADD", "register:40f0:8", ["const:743f88:8", "const:4:8"]]
- 00743f88 ["CALL", null, ["callee:0043bba4:8"]]
+ 00743fc8 ["INT_ADD", "register:40f0:8", ["const:743fc8:8", "const:4:8"]]
+ 00743fc8 ["CALL", null, ["callee:0043bba4:8"]]
- 00743f88 bytes f7def397
+ 00743fc8 bytes f7def397
~~~


<a id="compare-5e4f79342c57fb06b004c1f7e7d53828"></a>

### [`00743fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00743/00743fb0.md) → [`00743ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00743/00743ff0.md) FUN_00743ff0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`00ad075c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad075c.md) [`00ae9f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae9/00ae9f2c.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00ad0958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad0/00ad0958.md) [`00aea354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aea/00aea354.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00743fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00743/00743fb0.md#insn-00743fdc) · [`00744078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00743/00743fb0.md#insn-00744078) · [`007440b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00743/00743fb0.md#insn-007440b0)
- 新版 `0074401c`（命令位置の公開資料なし） · `007440b8`（命令位置の公開資料なし） · `007440f0`（命令位置の公開資料なし）

~~~diff
- 00743fdc ["INT_ADD", "register:40f0:8", ["const:743fdc:8", "const:4:8"]]
- 00743fdc ["CALL", null, ["callee:008514f8:8"]]
+ 0074401c ["INT_ADD", "register:40f0:8", ["const:74401c:8", "const:4:8"]]
+ 0074401c ["CALL", null, ["callee:008514f8:8"]]
- 00743fdc bytes 37350494
+ 0074401c bytes 37350494
- 00744078 ["INT_ADD", "register:40f0:8", ["const:744078:8", "const:4:8"]]
- 00744078 ["CALL", null, ["callee:00c57e90:8"]]
+ 007440b8 ["INT_ADD", "register:40f0:8", ["const:7440b8:8", "const:4:8"]]
+ 007440b8 ["CALL", null, ["callee:00c57e90:8"]]
- 00744078 bytes 864e1494
+ 007440b8 bytes 764f1494
- 007440b0 ["INT_ADD", "register:40f0:8", ["const:7440b0:8", "const:4:8"]]
- 007440b0 ["CALL", null, ["callee:0043bba4:8"]]
+ 007440f0 ["INT_ADD", "register:40f0:8", ["const:7440f0:8", "const:4:8"]]
+ 007440f0 ["CALL", null, ["callee:0043bba4:8"]]
- 007440b0 bytes addef397
+ 007440f0 bytes addef397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5646e1e8647a554313a3a47c448d0de5"></a>

### [`00744158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/00744158.md) → [`00744198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/00744198.md) FUN_00744198

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`007fa950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fa/007fa950.md) [`007faefc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fa/007faefc.md) [`007fb1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fb/007fb1f0.md) [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 8件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007fa990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa990.md) [`007faf3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007faf3c.md) [`007fb230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fb230.md) [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00744168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/00744158.md#insn-00744168)
- 新版 `007441a8`（命令位置の公開資料なし）

~~~diff
- 00744168 ["INT_ADD", "register:40f0:8", ["const:744168:8", "const:4:8"]]
- 00744168 ["CALL", null, ["callee:008514f8:8"]]
+ 007441a8 ["INT_ADD", "register:40f0:8", ["const:7441a8:8", "const:4:8"]]
+ 007441a8 ["CALL", null, ["callee:008514f8:8"]]
- 00744168 bytes d4340494
+ 007441a8 bytes d4340494
~~~


<a id="compare-d25f0c9fed6033b71dc6d548936db6b4"></a>

### [`007441c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/007441c8.md) → [`00744208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/00744208.md) FUN_00744208

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 60件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`005c0e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0e4c.md) [`005e46a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e46a0.md) [`005e47a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e47a4.md) [`005e4808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e4808.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 60件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`005c0e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c0e8c.md) [`005e46e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e46e0.md) [`005e47e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e47e4.md) [`005e4848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4848.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007441d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/007441c8.md#insn-007441d8)
- 新版 `00744218`（命令位置の公開資料なし）

~~~diff
- 007441d8 ["INT_ADD", "register:40f0:8", ["const:7441d8:8", "const:4:8"]]
- 007441d8 ["CALL", null, ["callee:008514f8:8"]]
+ 00744218 ["INT_ADD", "register:40f0:8", ["const:744218:8", "const:4:8"]]
+ 00744218 ["CALL", null, ["callee:008514f8:8"]]
- 007441d8 bytes b8340494
+ 00744218 bytes b8340494
~~~


<a id="compare-7e17a2e7794ec6726284d55d8d7ca39f"></a>

### [`007441fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/007441fc.md) → [`0074423c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/0074423c.md) FUN_0074423c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) [`006bea48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006be/006bea48.md) [`0078e240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e240.md) [`00a8a220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8a/00a8a220.md) [`00a913b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a91/00a913b0.md) · 呼出先 2件 [`00744238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/00744238.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 8件 [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`006bea88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006be/006bea88.md) [`0078e280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e280.md) [`00a8a418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8a/00a8a418.md) [`00a915a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a91/00a915a8.md) · 呼出先 2件 [`00744278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/00744278.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00744214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/007441fc.md#insn-00744214)
- 新版 `00744254`（命令位置の公開資料なし）

~~~diff
- 00744214 ["INT_ADD", "register:40f0:8", ["const:744214:8", "const:4:8"]]
- 00744214 ["CALL", null, ["callee:008514f8:8"]]
+ 00744254 ["INT_ADD", "register:40f0:8", ["const:744254:8", "const:4:8"]]
+ 00744254 ["CALL", null, ["callee:008514f8:8"]]
- 00744214 bytes a9340494
+ 00744254 bytes a9340494
~~~


<a id="compare-a6ec82923c4aad01041aa94808a71d42"></a>

### [`00744d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/00744d1c.md) → [`00744d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/00744d5c.md) FUN_00744d5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00744d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/00744d1c.md#insn-00744d54) · [`00744d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/00744d1c.md#insn-00744d74) · [`00744e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/00744d1c.md#insn-00744e0c)
- 新版 `00744d94`（命令位置の公開資料なし） · `00744db4`（命令位置の公開資料なし） · `00744e4c`（命令位置の公開資料なし）

~~~diff
- 00744d54 ["INT_ADD", "register:40f0:8", ["const:744d54:8", "const:4:8"]]
- 00744d54 ["CALL", null, ["callee:0043bba4:8"]]
+ 00744d94 ["INT_ADD", "register:40f0:8", ["const:744d94:8", "const:4:8"]]
+ 00744d94 ["CALL", null, ["callee:0043bba4:8"]]
- 00744d54 bytes 84dbf397
+ 00744d94 bytes 84dbf397
- 00744d74 ["INT_ADD", "register:40f0:8", ["const:744d74:8", "const:4:8"]]
- 00744d74 ["CALL", null, ["callee:008514f8:8"]]
+ 00744db4 ["INT_ADD", "register:40f0:8", ["const:744db4:8", "const:4:8"]]
+ 00744db4 ["CALL", null, ["callee:008514f8:8"]]
- 00744d74 bytes d1310494
+ 00744db4 bytes d1310494
- 00744e0c ["INT_ADD", "register:40f0:8", ["const:744e0c:8", "const:4:8"]]
- 00744e0c ["CALL", null, ["callee:00c57e90:8"]]
+ 00744e4c ["INT_ADD", "register:40f0:8", ["const:744e4c:8", "const:4:8"]]
+ 00744e4c ["CALL", null, ["callee:00c57e90:8"]]
- 00744e0c bytes 214b1494
+ 00744e4c bytes 114c1494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b5abc5fbea79f321f7b7df31f1944c9"></a>

### [`00744f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/00744f4c.md) → [`00744f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/00744f8c.md) FUN_00744f8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 12件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`004800d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004800d8.md) [`00480138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480138.md)
- 新版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 12件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00480118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480118.md) [`00480178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00744f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/00744f4c.md#insn-00744f74) · [`00744f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/00744f4c.md#insn-00744f80) · [`00744f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/00744f4c.md#insn-00744f90)
- 新版 `00744fb4`（命令位置の公開資料なし） · `00744fc0`（命令位置の公開資料なし） · `00744fd0`（命令位置の公開資料なし）

~~~diff
- 00744f74 ["INT_ADD", "register:40f0:8", ["const:744f74:8", "const:4:8"]]
- 00744f74 ["CALL", null, ["callee:004801d8:8"]]
+ 00744fb4 ["INT_ADD", "register:40f0:8", ["const:744fb4:8", "const:4:8"]]
+ 00744fb4 ["CALL", null, ["callee:004801d8:8"]]
- 00744f74 bytes 89ecf497
+ 00744fb4 bytes 89ecf497
- 00744f80 ["INT_ADD", "register:40f0:8", ["const:744f80:8", "const:4:8"]]
- 00744f80 ["CALL", null, ["callee:00480178:8"]]
+ 00744fc0 ["INT_ADD", "register:40f0:8", ["const:744fc0:8", "const:4:8"]]
+ 00744fc0 ["CALL", null, ["callee:00480178:8"]]
- 00744f80 bytes 6eecf497
+ 00744fc0 bytes 6eecf497
- 00744f90 ["INT_ADD", "register:40f0:8", ["const:744f90:8", "const:4:8"]]
- 00744f90 ["CALL", null, ["callee:00480118:8"]]
+ 00744fd0 ["INT_ADD", "register:40f0:8", ["const:744fd0:8", "const:4:8"]]
+ 00744fd0 ["CALL", null, ["callee:00480118:8"]]
- 00744f90 bytes 52ecf497
+ 00744fd0 bytes 52ecf497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5df7f1112e23962ebde5639c7d1b925e"></a>

### [`007453f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00745/007453f4.md) → [`00745434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/00745434.md) FUN_00745434

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 4件 [`00480af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480af8.md) [`00480b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480b50.md) [`00480ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ba8.md) [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md)
- 新版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 4件 [`00480b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md) [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md) [`00480be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md) [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00745418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00745/007453f4.md#insn-00745418) · [`00745424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00745/007453f4.md#insn-00745424) · [`00745430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00745/007453f4.md#insn-00745430)
- 新版 `00745458`（命令位置の公開資料なし） · `00745464`（命令位置の公開資料なし） · `00745470`（命令位置の公開資料なし）

~~~diff
- 00745418 ["INT_ADD", "register:40f0:8", ["const:745418:8", "const:4:8"]]
- 00745418 ["CALL", null, ["callee:00480be8:8"]]
+ 00745458 ["INT_ADD", "register:40f0:8", ["const:745458:8", "const:4:8"]]
+ 00745458 ["CALL", null, ["callee:00480be8:8"]]
- 00745418 bytes e4edf497
+ 00745458 bytes e4edf497
- 00745424 ["INT_ADD", "register:40f0:8", ["const:745424:8", "const:4:8"]]
- 00745424 ["CALL", null, ["callee:00480b90:8"]]
+ 00745464 ["INT_ADD", "register:40f0:8", ["const:745464:8", "const:4:8"]]
+ 00745464 ["CALL", null, ["callee:00480b90:8"]]
- 00745424 bytes cbedf497
+ 00745464 bytes cbedf497
- 00745430 ["INT_ADD", "register:40f0:8", ["const:745430:8", "const:4:8"]]
- 00745430 ["CALL", null, ["callee:00480b38:8"]]
+ 00745470 ["INT_ADD", "register:40f0:8", ["const:745470:8", "const:4:8"]]
+ 00745470 ["CALL", null, ["callee:00480b38:8"]]
- 00745430 bytes b2edf497
+ 00745470 bytes b2edf497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c20067607e0105d52031e7e6d7ab976"></a>

### [`007458f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00745/007458f0.md) → [`00745930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/00745930.md) FUN_00745930

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0074578c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00745/0074578c.md) [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 2件 [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00a33a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a33/00a33a24.md)
- 新版 呼出元 2件 [`007457cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/007457cc.md) [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) · 呼出先 2件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00a33c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33c1c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00745904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00745/007458f0.md#insn-00745904) · [`00745910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00745/007458f0.md#insn-00745910) · [`0074591c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00745/007458f0.md#insn-0074591c)
- 新版 `00745944`（命令位置の公開資料なし） · `00745950`（命令位置の公開資料なし） · `0074595c`（命令位置の公開資料なし）

~~~diff
- 00745904 ["INT_ADD", "register:40f0:8", ["const:745904:8", "const:4:8"]]
- 00745904 ["CALL", null, ["callee:0048ce84:8"]]
+ 00745944 ["INT_ADD", "register:40f0:8", ["const:745944:8", "const:4:8"]]
+ 00745944 ["CALL", null, ["callee:0048ce84:8"]]
- 00745904 bytes 501df597
+ 00745944 bytes 501df597
- 00745910 ["INT_ADD", "register:40f0:8", ["const:745910:8", "const:4:8"]]
- 00745910 ["CALL", null, ["callee:00a33c1c:8"]]
+ 00745950 ["INT_ADD", "register:40f0:8", ["const:745950:8", "const:4:8"]]
+ 00745950 ["CALL", null, ["callee:00a33c1c:8"]]
- 00745910 bytes 45b80b94
+ 00745950 bytes b3b80b94
- 0074591c ["INT_ADD", "register:40f0:8", ["const:74591c:8", "const:4:8"]]
- 0074591c ["CALL", null, ["callee:0048ce84:8"]]
+ 0074595c ["INT_ADD", "register:40f0:8", ["const:74595c:8", "const:4:8"]]
+ 0074595c ["CALL", null, ["callee:0048ce84:8"]]
- 0074591c bytes 4a1df597
+ 0074595c bytes 4a1df597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb0e952e28f0339ad9b6ea2b98558056"></a>

### [`007468ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00746/007468ac.md) → [`007468ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00746/007468ec.md) FUN_007468ec

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) [`00ae0e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0e64.md) · 呼出先 6件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00664780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664780.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 4件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`00ae128c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae1/00ae128c.md) · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`006647c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006647c0.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00746908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00746/007468ac.md#insn-00746908) · [`00746928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00746/007468ac.md#insn-00746928) · [`00746980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00746/007468ac.md#insn-00746980)
- 新版 `00746948`（命令位置の公開資料なし） · `00746968`（命令位置の公開資料なし） · `007469c0`（命令位置の公開資料なし）

~~~diff
- 00746908 ["INT_ADD", "register:40f0:8", ["const:746908:8", "const:4:8"]]
- 00746908 ["CALL", null, ["callee:0043bba4:8"]]
+ 00746948 ["INT_ADD", "register:40f0:8", ["const:746948:8", "const:4:8"]]
+ 00746948 ["CALL", null, ["callee:0043bba4:8"]]
- 00746908 bytes 97d4f397
+ 00746948 bytes 97d4f397
- 00746928 ["INT_ADD", "register:40f0:8", ["const:746928:8", "const:4:8"]]
- 00746928 ["CALL", null, ["callee:008514f8:8"]]
+ 00746968 ["INT_ADD", "register:40f0:8", ["const:746968:8", "const:4:8"]]
+ 00746968 ["CALL", null, ["callee:008514f8:8"]]
- 00746928 bytes e42a0494
+ 00746968 bytes e42a0494
- 00746980 ["INT_ADD", "register:40f0:8", ["const:746980:8", "const:4:8"]]
- 00746980 ["CALL", null, ["callee:008514f8:8"]]
+ 007469c0 ["INT_ADD", "register:40f0:8", ["const:7469c0:8", "const:4:8"]]
+ 007469c0 ["CALL", null, ["callee:008514f8:8"]]
- 00746980 bytes ce2a0494
+ 007469c0 bytes ce2a0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22fb33d3bb31aaf4c0edeb0f9af0b88a"></a>

### [`0074721c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/0074721c.md) → [`0074725c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/0074725c.md) FUN_0074725c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 6件 [`00748f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748f08.md) [`0074a614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a614.md) [`0074a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a694.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 6件 [`00748f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748f48.md) [`0074a654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a654.md) [`0074a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a6d4.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007472a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/0074721c.md#insn-007472a0) · [`007472c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/0074721c.md#insn-007472c4) · [`0074730c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/0074721c.md#insn-0074730c)
- 新版 `007472e0`（命令位置の公開資料なし） · `00747304`（命令位置の公開資料なし） · `0074734c`（命令位置の公開資料なし）

~~~diff
- 007472a0 ["INT_ADD", "register:40f0:8", ["const:7472a0:8", "const:4:8"]]
- 007472a0 ["CALL", null, ["callee:00c57e90:8"]]
+ 007472e0 ["INT_ADD", "register:40f0:8", ["const:7472e0:8", "const:4:8"]]
+ 007472e0 ["CALL", null, ["callee:00c57e90:8"]]
- 007472a0 bytes fc411494
+ 007472e0 bytes ec421494
- 007472c4 ["INT_ADD", "register:40f0:8", ["const:7472c4:8", "const:4:8"]]
- 007472c4 ["CALL", null, ["callee:0074a6d4:8"]]
+ 00747304 ["INT_ADD", "register:40f0:8", ["const:747304:8", "const:4:8"]]
+ 00747304 ["CALL", null, ["callee:0074a6d4:8"]]
- 007472c4 bytes f40c0094
+ 00747304 bytes f40c0094
- 0074730c ["INT_ADD", "register:40f0:8", ["const:74730c:8", "const:4:8"]]
- 0074730c ["CALL", null, ["callee:00748f48:8"]]
+ 0074734c ["INT_ADD", "register:40f0:8", ["const:74734c:8", "const:4:8"]]
+ 0074734c ["CALL", null, ["callee:00748f48:8"]]
- 0074730c bytes ff060094
+ 0074734c bytes ff060094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3397391d36db246bc56ce90548cf3ae"></a>

### [`007475b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/007475b0.md) → [`007475f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/007475f0.md) FUN_007475f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0060eb10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060eb10.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 9件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00468f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f0c.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aecc.md) [`0046da1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da1c.md)
- 新版 呼出元 2件 [`0060eb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060e/0060eb50.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) · 呼出先 9件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00468f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f4c.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046af0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af0c.md) [`0046da5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046da5c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007475fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/007475b0.md#insn-007475fc) · [`00747614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/007475b0.md#insn-00747614) · [`00747624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/007475b0.md#insn-00747624)
- 新版 `0074763c`（命令位置の公開資料なし） · `00747654`（命令位置の公開資料なし） · `00747664`（命令位置の公開資料なし）

~~~diff
- 007475fc ["INT_ADD", "register:40f0:8", ["const:7475fc:8", "const:4:8"]]
- 007475fc ["CALL", null, ["callee:00467860:8"]]
+ 0074763c ["INT_ADD", "register:40f0:8", ["const:74763c:8", "const:4:8"]]
+ 0074763c ["CALL", null, ["callee:00467860:8"]]
- 007475fc bytes 8980f497
+ 0074763c bytes 8980f497
- 00747614 ["INT_ADD", "register:40f0:8", ["const:747614:8", "const:4:8"]]
- 00747614 ["CALL", null, ["callee:00468f88:8"]]
+ 00747654 ["INT_ADD", "register:40f0:8", ["const:747654:8", "const:4:8"]]
+ 00747654 ["CALL", null, ["callee:00468f88:8"]]
- 00747614 bytes 4d86f497
+ 00747654 bytes 4d86f497
- 00747624 ["INT_ADD", "register:40f0:8", ["const:747624:8", "const:4:8"]]
- 00747624 ["CALL", null, ["callee:0080062c:8"]]
+ 00747664 ["INT_ADD", "register:40f0:8", ["const:747664:8", "const:4:8"]]
+ 00747664 ["CALL", null, ["callee:0080062c:8"]]
- 00747624 bytes f2e30294
+ 00747664 bytes f2e30294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a492ff47c4e70e3a1d60977a7aa2c26f"></a>

### [`007477c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/007477c4.md) → [`00747804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/00747804.md) FUN_00747804

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00742b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00742/00742b78.md) [`007477c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/007477c4.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849330.md) · 呼出先 2件 [`007477c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/007477c4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`00742bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00742/00742bb8.md) [`00747804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/00747804.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849370.md) · 呼出先 2件 [`00747804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/00747804.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007477e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/007477c4.md#insn-007477e0) · [`007477ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/007477c4.md#insn-007477ec) · [`007477fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/007477c4.md#insn-007477fc)
- 新版 `00747820`（命令位置の公開資料なし） · `0074782c`（命令位置の公開資料なし） · `0074783c`（命令位置の公開資料なし）

~~~diff
- 007477e0 ["INT_ADD", "register:40f0:8", ["const:7477e0:8", "const:4:8"]]
- 007477e0 ["CALL", null, ["local:b0:8"]]
+ 00747820 ["INT_ADD", "register:40f0:8", ["const:747820:8", "const:4:8"]]
+ 00747820 ["CALL", null, ["local:b0:8"]]
- 007477e0 bytes f9ffff97
+ 00747820 bytes f9ffff97
- 007477ec ["INT_ADD", "register:40f0:8", ["const:7477ec:8", "const:4:8"]]
- 007477ec ["CALL", null, ["local:b0:8"]]
+ 0074782c ["INT_ADD", "register:40f0:8", ["const:74782c:8", "const:4:8"]]
+ 0074782c ["CALL", null, ["local:b0:8"]]
- 007477ec bytes f6ffff97
+ 0074782c bytes f6ffff97
- 007477fc ["INT_ADD", "register:40f0:8", ["const:7477fc:8", "const:4:8"]]
- 007477fc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0074783c ["INT_ADD", "register:40f0:8", ["const:74783c:8", "const:4:8"]]
+ 0074783c ["CALL", null, ["callee:00c57eb0:8"]]
- 007477fc bytes ad401494
+ 0074783c bytes 9d411494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f788c2b7cbb46d926d2c43efdf906af6"></a>

### [`00747a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/00747a20.md) → [`00747a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/00747a60.md) FUN_00747a60

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007459e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00745/007459e4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00745a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/00745a24.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00747a5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/00747a20.md#insn-00747a5c)
- 新版 `00747a9c`（命令位置の公開資料なし）

~~~diff
- 00747a5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00747a5c ["INT_ADD", "register:40f0:8", ["const:747a5c:8", "const:4:8"]]
- 00747a5c ["CALLIND", null, ["register:0:8"]]
+ 00747a9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00747a9c ["INT_ADD", "register:40f0:8", ["const:747a9c:8", "const:4:8"]]
+ 00747a9c ["CALLIND", null, ["register:0:8"]]
- 00747a5c bytes 00013fd6
+ 00747a9c bytes 00013fd6
~~~


<a id="compare-d7ddbc23a030225cc9671c6b26294ed0"></a>

### [`00747e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/00747e9c.md) → [`00747edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/00747edc.md) FUN_00747edc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007459e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00745/007459e4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00745a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/00745a24.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00747ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/00747e9c.md#insn-00747ed8)
- 新版 `00747f18`（命令位置の公開資料なし）

~~~diff
- 00747ed8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00747ed8 ["INT_ADD", "register:40f0:8", ["const:747ed8:8", "const:4:8"]]
- 00747ed8 ["CALLIND", null, ["register:0:8"]]
+ 00747f18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00747f18 ["INT_ADD", "register:40f0:8", ["const:747f18:8", "const:4:8"]]
+ 00747f18 ["CALLIND", null, ["register:0:8"]]
- 00747ed8 bytes 00013fd6
+ 00747f18 bytes 00013fd6
~~~


<a id="compare-ecdfce75a87063dfb13ecf59c01e3f97"></a>

### [`00747eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/00747eec.md) → [`00747f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/00747f2c.md) FUN_00747f2c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00747f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/00747eec.md#insn-00747f24) · [`00747f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/00747eec.md#insn-00747f58) · [`00747f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/00747eec.md#insn-00747f5c)
- 新版 `00747f64`（命令位置の公開資料なし） · `00747f98`（命令位置の公開資料なし） · `00747f9c`（命令位置の公開資料なし）

~~~diff
- 00747f24 ["COPY", "register:0:8", ["register:4040:8"]]
- 00747f24 ["INT_ADD", "register:40f0:8", ["const:747f24:8", "const:4:8"]]
- 00747f24 ["CALLIND", null, ["register:0:8"]]
+ 00747f64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00747f64 ["INT_ADD", "register:40f0:8", ["const:747f64:8", "const:4:8"]]
+ 00747f64 ["CALLIND", null, ["register:0:8"]]
- 00747f24 bytes 00013fd6
+ 00747f64 bytes 00013fd6
- 00747f58 ["INT_ADD", "register:40f0:8", ["const:747f58:8", "const:4:8"]]
- 00747f58 ["CALL", null, ["callee:00459d74:8"]]
+ 00747f98 ["INT_ADD", "register:40f0:8", ["const:747f98:8", "const:4:8"]]
+ 00747f98 ["CALL", null, ["callee:00459d74:8"]]
- 00747f58 bytes 7747f497
+ 00747f98 bytes 7747f497
- 00747f5c ["INT_ADD", "register:40f0:8", ["const:747f5c:8", "const:4:8"]]
- 00747f5c ["CALL", null, ["callee:00c57ee0:8"]]
+ 00747f9c ["INT_ADD", "register:40f0:8", ["const:747f9c:8", "const:4:8"]]
+ 00747f9c ["CALL", null, ["callee:00c57ee0:8"]]
- 00747f5c bytes e13e1494
+ 00747f9c bytes d13f1494
~~~


<a id="compare-ab91d0d254c39ee07dc0e07ec580be15"></a>

### [`0074817c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/0074817c.md) → [`007481bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/007481bc.md) FUN_007481bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00745f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00745/00745f74.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00745fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/00745fb4.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007481b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/0074817c.md#insn-007481b8)
- 新版 `007481f8`（命令位置の公開資料なし）

~~~diff
- 007481b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 007481b8 ["INT_ADD", "register:40f0:8", ["const:7481b8:8", "const:4:8"]]
- 007481b8 ["CALLIND", null, ["register:0:8"]]
+ 007481f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007481f8 ["INT_ADD", "register:40f0:8", ["const:7481f8:8", "const:4:8"]]
+ 007481f8 ["CALLIND", null, ["register:0:8"]]
- 007481b8 bytes 00013fd6
+ 007481f8 bytes 00013fd6
~~~


<a id="compare-98cf9f0acbcf3446cd984278fba7172d"></a>

### [`00748638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748638.md) → [`00748678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748678.md) FUN_00748678

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00745f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00745/00745f74.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00745fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/00745fb4.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00748674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748638.md#insn-00748674)
- 新版 `007486b4`（命令位置の公開資料なし）

~~~diff
- 00748674 ["COPY", "register:0:8", ["register:4040:8"]]
- 00748674 ["INT_ADD", "register:40f0:8", ["const:748674:8", "const:4:8"]]
- 00748674 ["CALLIND", null, ["register:0:8"]]
+ 007486b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007486b4 ["INT_ADD", "register:40f0:8", ["const:7486b4:8", "const:4:8"]]
+ 007486b4 ["CALLIND", null, ["register:0:8"]]
- 00748674 bytes 00013fd6
+ 007486b4 bytes 00013fd6
~~~


<a id="compare-280539c27520da0ac975389565fe6fea"></a>

### [`00748688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748688.md) → [`007486c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/007486c8.md) FUN_007486c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007486c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748688.md#insn-007486c8) · [`007486fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748688.md#insn-007486fc) · [`00748700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748688.md#insn-00748700)
- 新版 `00748708`（命令位置の公開資料なし） · `0074873c`（命令位置の公開資料なし） · `00748740`（命令位置の公開資料なし）

~~~diff
- 007486c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 007486c8 ["INT_ADD", "register:40f0:8", ["const:7486c8:8", "const:4:8"]]
- 007486c8 ["CALLIND", null, ["register:0:8"]]
+ 00748708 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00748708 ["INT_ADD", "register:40f0:8", ["const:748708:8", "const:4:8"]]
+ 00748708 ["CALLIND", null, ["register:0:8"]]
- 007486c8 bytes 00013fd6
+ 00748708 bytes 00013fd6
- 007486fc ["INT_ADD", "register:40f0:8", ["const:7486fc:8", "const:4:8"]]
- 007486fc ["CALL", null, ["callee:00459d74:8"]]
+ 0074873c ["INT_ADD", "register:40f0:8", ["const:74873c:8", "const:4:8"]]
+ 0074873c ["CALL", null, ["callee:00459d74:8"]]
- 007486fc bytes 8e45f497
+ 0074873c bytes 8e45f497
- 00748700 ["INT_ADD", "register:40f0:8", ["const:748700:8", "const:4:8"]]
- 00748700 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00748740 ["INT_ADD", "register:40f0:8", ["const:748740:8", "const:4:8"]]
+ 00748740 ["CALL", null, ["callee:00c57ee0:8"]]
- 00748700 bytes f83c1494
+ 00748740 bytes e83d1494
~~~


<a id="compare-298ad398875831b07cc26c5ba31d05db"></a>

### [`00748af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748af0.md) → [`00748b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748b30.md) FUN_00748b30

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`00746cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00746/00746cac.md) [`00748ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748ce4.md) [`00748f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748f1c.md) [`0074a614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a614.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 7件 [`00746cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00746/00746cec.md) [`00748d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748d24.md) [`00748f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748f5c.md) [`0074a654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a654.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00748b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748af0.md#insn-00748b10) · [`00748b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748af0.md#insn-00748b4c) · [`00748b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748af0.md#insn-00748b5c)
- 新版 `00748b50`（命令位置の公開資料なし） · `00748b8c`（命令位置の公開資料なし） · `00748b9c`（命令位置の公開資料なし）

~~~diff
- 00748b10 ["INT_ADD", "register:40f0:8", ["const:748b10:8", "const:4:8"]]
- 00748b10 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00748b50 ["INT_ADD", "register:40f0:8", ["const:748b50:8", "const:4:8"]]
+ 00748b50 ["CALL", null, ["callee:00c57eb0:8"]]
- 00748b10 bytes e83b1494
+ 00748b50 bytes d83c1494
- 00748b4c ["INT_ADD", "register:40f0:8", ["const:748b4c:8", "const:4:8"]]
- 00748b4c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00748b8c ["INT_ADD", "register:40f0:8", ["const:748b8c:8", "const:4:8"]]
+ 00748b8c ["CALL", null, ["callee:00c57eb0:8"]]
- 00748b4c bytes d93b1494
+ 00748b8c bytes c93c1494
- 00748b5c ["INT_ADD", "register:40f0:8", ["const:748b5c:8", "const:4:8"]]
- 00748b5c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00748b9c ["INT_ADD", "register:40f0:8", ["const:748b9c:8", "const:4:8"]]
+ 00748b9c ["CALL", null, ["callee:00c57eb0:8"]]
- 00748b5c bytes d53b1494
+ 00748b9c bytes c53c1494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36e5958cfe48fe0aed8a0d0cb99d499f"></a>

### [`00748b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748b9c.md) → [`00748bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748bdc.md) FUN_00748bdc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00748bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748b9c.md#insn-00748bbc) · [`00748bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748b9c.md#insn-00748bf8) · [`00748c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748b9c.md#insn-00748c08)
- 新版 `00748bfc`（命令位置の公開資料なし） · `00748c38`（命令位置の公開資料なし） · `00748c48`（命令位置の公開資料なし）

~~~diff
- 00748bbc ["INT_ADD", "register:40f0:8", ["const:748bbc:8", "const:4:8"]]
- 00748bbc ["CALL", null, ["callee:00c57eb0:8"]]
+ 00748bfc ["INT_ADD", "register:40f0:8", ["const:748bfc:8", "const:4:8"]]
+ 00748bfc ["CALL", null, ["callee:00c57eb0:8"]]
- 00748bbc bytes bd3b1494
+ 00748bfc bytes ad3c1494
- 00748bf8 ["INT_ADD", "register:40f0:8", ["const:748bf8:8", "const:4:8"]]
- 00748bf8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00748c38 ["INT_ADD", "register:40f0:8", ["const:748c38:8", "const:4:8"]]
+ 00748c38 ["CALL", null, ["callee:00c57eb0:8"]]
- 00748bf8 bytes ae3b1494
+ 00748c38 bytes 9e3c1494
- 00748c08 ["INT_ADD", "register:40f0:8", ["const:748c08:8", "const:4:8"]]
- 00748c08 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00748c48 ["INT_ADD", "register:40f0:8", ["const:748c48:8", "const:4:8"]]
+ 00748c48 ["CALL", null, ["callee:00c57eb0:8"]]
- 00748c08 bytes aa3b1494
+ 00748c48 bytes 9a3c1494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6b5af50a31d8f8234e07991e81b706b"></a>

### [`00748c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748c48.md) → [`00748c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748c88.md) FUN_00748c88

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009aa488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009aa/009aa488.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`009aa624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009aa/009aa624.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00748c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748c48.md#insn-00748c94) · [`00748ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748c48.md#insn-00748ca4) · [`00748cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748c48.md#insn-00748cb4)
- 新版 `00748cd4`（命令位置の公開資料なし） · `00748ce4`（命令位置の公開資料なし） · `00748cf4`（命令位置の公開資料なし）

~~~diff
- 00748c94 ["INT_ADD", "register:40f0:8", ["const:748c94:8", "const:4:8"]]
- 00748c94 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00748cd4 ["INT_ADD", "register:40f0:8", ["const:748cd4:8", "const:4:8"]]
+ 00748cd4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00748c94 bytes 873b1494
+ 00748cd4 bytes 773c1494
- 00748ca4 ["INT_ADD", "register:40f0:8", ["const:748ca4:8", "const:4:8"]]
- 00748ca4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00748ce4 ["INT_ADD", "register:40f0:8", ["const:748ce4:8", "const:4:8"]]
+ 00748ce4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00748ca4 bytes 833b1494
+ 00748ce4 bytes 733c1494
- 00748cb4 ["INT_ADD", "register:40f0:8", ["const:748cb4:8", "const:4:8"]]
- 00748cb4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00748cf4 ["INT_ADD", "register:40f0:8", ["const:748cf4:8", "const:4:8"]]
+ 00748cf4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00748cb4 bytes 7f3b1494
+ 00748cf4 bytes 6f3c1494
~~~


<a id="compare-a037dbafbb8d014beeae5efb1685f641"></a>

### [`00748ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748ce4.md) → [`00748d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748d24.md) FUN_00748d24

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00749994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00749/00749994.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00748af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748af0.md) [`00748f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748f08.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`007499d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00749/007499d4.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00748b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748b30.md) [`00748f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748f48.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00748d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748ce4.md#insn-00748d84) · [`00748ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748ce4.md#insn-00748ebc) · [`00748ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748ce4.md#insn-00748ee0)
- 新版 `00748dc4`（命令位置の公開資料なし） · `00748efc`（命令位置の公開資料なし） · `00748f20`（命令位置の公開資料なし）

~~~diff
- 00748d84 ["INT_ADD", "register:40f0:8", ["const:748d84:8", "const:4:8"]]
- 00748d84 ["CALL", null, ["callee:00c57e90:8"]]
+ 00748dc4 ["INT_ADD", "register:40f0:8", ["const:748dc4:8", "const:4:8"]]
+ 00748dc4 ["CALL", null, ["callee:00c57e90:8"]]
- 00748d84 bytes 433b1494
+ 00748dc4 bytes 333c1494
- 00748ebc ["INT_ADD", "register:40f0:8", ["const:748ebc:8", "const:4:8"]]
- 00748ebc ["CALL", null, ["callee:00748b30:8"]]
+ 00748efc ["INT_ADD", "register:40f0:8", ["const:748efc:8", "const:4:8"]]
+ 00748efc ["CALL", null, ["callee:00748b30:8"]]
- 00748ebc bytes 0dffff97
+ 00748efc bytes 0dffff97
- 00748ee0 ["INT_ADD", "register:40f0:8", ["const:748ee0:8", "const:4:8"]]
- 00748ee0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00748f20 ["INT_ADD", "register:40f0:8", ["const:748f20:8", "const:4:8"]]
+ 00748f20 ["CALL", null, ["callee:00c57eb0:8"]]
- 00748ee0 bytes f43a1494
+ 00748f20 bytes e43b1494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b751b4799f3f21890bae6bbf2ae809ce"></a>

### [`00748f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748f1c.md) → [`00748f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748f5c.md) FUN_00748f5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00748af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748af0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00748b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748b30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00748f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748f1c.md#insn-00748f5c)
- 新版 `00748f9c`（命令位置の公開資料なし）

~~~diff
- 00748f5c ["INT_ADD", "register:40f0:8", ["const:748f5c:8", "const:4:8"]]
- 00748f5c ["CALL", null, ["callee:00748b30:8"]]
+ 00748f9c ["INT_ADD", "register:40f0:8", ["const:748f9c:8", "const:4:8"]]
+ 00748f9c ["CALL", null, ["callee:00748b30:8"]]
- 00748f5c bytes e5feff97
+ 00748f9c bytes e5feff97
~~~


<a id="compare-c0751e5f7934653883b5e484bec1a416"></a>

### [`00749944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00749/00749944.md) → [`00749984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00749/00749984.md) FUN_00749984

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00746cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00746/00746cac.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00746cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00746/00746cec.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00749980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00749/00749944.md#insn-00749980)
- 新版 `007499c0`（命令位置の公開資料なし）

~~~diff
- 00749980 ["COPY", "register:0:8", ["register:4040:8"]]
- 00749980 ["INT_ADD", "register:40f0:8", ["const:749980:8", "const:4:8"]]
- 00749980 ["CALLIND", null, ["register:0:8"]]
+ 007499c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007499c0 ["INT_ADD", "register:40f0:8", ["const:7499c0:8", "const:4:8"]]
+ 007499c0 ["CALLIND", null, ["register:0:8"]]
- 00749980 bytes 00013fd6
+ 007499c0 bytes 00013fd6
~~~


<a id="compare-324699e1dc79c62cfb050cdda6f9806f"></a>

### [`0074a2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a2d8.md) → [`0074a318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a318.md) FUN_0074a318

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009aa488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009aa/009aa488.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`009aa624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009aa/009aa624.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074a30c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a2d8.md#insn-0074a30c) · [`0074a328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a2d8.md#insn-0074a328) · [`0074a338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a2d8.md#insn-0074a338)
- 新版 `0074a34c`（命令位置の公開資料なし） · `0074a368`（命令位置の公開資料なし） · `0074a378`（命令位置の公開資料なし）

~~~diff
- 0074a30c ["INT_ADD", "register:40f0:8", ["const:74a30c:8", "const:4:8"]]
- 0074a30c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0074a34c ["INT_ADD", "register:40f0:8", ["const:74a34c:8", "const:4:8"]]
+ 0074a34c ["CALL", null, ["callee:00c57eb0:8"]]
- 0074a30c bytes e9351494
+ 0074a34c bytes d9361494
- 0074a328 ["INT_ADD", "register:40f0:8", ["const:74a328:8", "const:4:8"]]
- 0074a328 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0074a368 ["INT_ADD", "register:40f0:8", ["const:74a368:8", "const:4:8"]]
+ 0074a368 ["CALL", null, ["callee:00c57eb0:8"]]
- 0074a328 bytes e2351494
+ 0074a368 bytes d2361494
- 0074a338 ["INT_ADD", "register:40f0:8", ["const:74a338:8", "const:4:8"]]
- 0074a338 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0074a378 ["INT_ADD", "register:40f0:8", ["const:74a378:8", "const:4:8"]]
+ 0074a378 ["CALL", null, ["callee:00c57eb0:8"]]
- 0074a338 bytes de351494
+ 0074a378 bytes ce361494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6cc066dc2a435db5addd52030a412c9"></a>

### [`0074a53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a53c.md) → [`0074a57c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a57c.md) FUN_0074a57c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00746cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00746/00746cac.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00746cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00746/00746cec.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074a578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a53c.md#insn-0074a578)
- 新版 `0074a5b8`（命令位置の公開資料なし）

~~~diff
- 0074a578 ["COPY", "register:0:8", ["register:4040:8"]]
- 0074a578 ["INT_ADD", "register:40f0:8", ["const:74a578:8", "const:4:8"]]
- 0074a578 ["CALLIND", null, ["register:0:8"]]
+ 0074a5b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0074a5b8 ["INT_ADD", "register:40f0:8", ["const:74a5b8:8", "const:4:8"]]
+ 0074a5b8 ["CALLIND", null, ["register:0:8"]]
- 0074a578 bytes 00013fd6
+ 0074a5b8 bytes 00013fd6
~~~


<a id="compare-22d8697834d1bf316d727c181e79cb8a"></a>

### [`0074a58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a58c.md) → [`0074a5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a5cc.md) FUN_0074a5cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074a5c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a58c.md#insn-0074a5c4) · [`0074a5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a58c.md#insn-0074a5e8)
- 新版 `0074a604`（命令位置の公開資料なし） · `0074a628`（命令位置の公開資料なし）

~~~diff
- 0074a5c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0074a5c4 ["INT_ADD", "register:40f0:8", ["const:74a5c4:8", "const:4:8"]]
- 0074a5c4 ["CALLIND", null, ["register:0:8"]]
+ 0074a604 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0074a604 ["INT_ADD", "register:40f0:8", ["const:74a604:8", "const:4:8"]]
+ 0074a604 ["CALLIND", null, ["register:0:8"]]
- 0074a5c4 bytes 00013fd6
+ 0074a604 bytes 00013fd6
- 0074a5e8 ["INT_ADD", "register:40f0:8", ["const:74a5e8:8", "const:4:8"]]
- 0074a5e8 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0074a628 ["INT_ADD", "register:40f0:8", ["const:74a628:8", "const:4:8"]]
+ 0074a628 ["CALL", null, ["callee:00c57ee0:8"]]
- 0074a5e8 bytes 3e351494
+ 0074a628 bytes 2e361494
~~~


<a id="compare-aa2e766a76e8d6d92042adb3499d44e2"></a>

### [`0074a614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a614.md) → [`0074a654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a654.md) FUN_0074a654

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0074721c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/0074721c.md) · 呼出先 2件 [`00748af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748af0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0074725c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/0074725c.md) · 呼出先 2件 [`00748b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748b30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074a668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a614.md#insn-0074a668)
- 新版 `0074a6a8`（命令位置の公開資料なし）

~~~diff
- 0074a668 ["INT_ADD", "register:40f0:8", ["const:74a668:8", "const:4:8"]]
- 0074a668 ["CALL", null, ["callee:00748b30:8"]]
+ 0074a6a8 ["INT_ADD", "register:40f0:8", ["const:74a6a8:8", "const:4:8"]]
+ 0074a6a8 ["CALL", null, ["callee:00748b30:8"]]
- 0074a668 bytes 22f9ff97
+ 0074a6a8 bytes 22f9ff97
~~~


<a id="compare-a22aee79d9c0017b091ce707dfe898e4"></a>

### [`0074a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a694.md) → [`0074a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a6d4.md) FUN_0074a6d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0074721c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/0074721c.md) · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0074a794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a794.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0074725c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/0074725c.md) · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0074a7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a7d4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074a714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a694.md#insn-0074a714) · [`0074a72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a694.md#insn-0074a72c) · [`0074a790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a694.md#insn-0074a790)
- 新版 `0074a754`（命令位置の公開資料なし） · `0074a76c`（命令位置の公開資料なし） · `0074a7d0`（命令位置の公開資料なし）

~~~diff
- 0074a714 ["INT_ADD", "register:40f0:8", ["const:74a714:8", "const:4:8"]]
- 0074a714 ["CALL", null, ["callee:0074a7d4:8"]]
+ 0074a754 ["INT_ADD", "register:40f0:8", ["const:74a754:8", "const:4:8"]]
+ 0074a754 ["CALL", null, ["callee:0074a7d4:8"]]
- 0074a714 bytes 20000094
+ 0074a754 bytes 20000094
- 0074a72c ["INT_ADD", "register:40f0:8", ["const:74a72c:8", "const:4:8"]]
- 0074a72c ["CALL", null, ["callee:0043bb20:8"]]
+ 0074a76c ["INT_ADD", "register:40f0:8", ["const:74a76c:8", "const:4:8"]]
+ 0074a76c ["CALL", null, ["callee:0043bb20:8"]]
- 0074a72c bytes edc4f397
+ 0074a76c bytes edc4f397
- 0074a790 ["INT_ADD", "register:40f0:8", ["const:74a790:8", "const:4:8"]]
- 0074a790 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0074a7d0 ["INT_ADD", "register:40f0:8", ["const:74a7d0:8", "const:4:8"]]
+ 0074a7d0 ["CALL", null, ["callee:00c57ee0:8"]]
- 0074a790 bytes d4341494
+ 0074a7d0 bytes c4351494
~~~


<a id="compare-19a96771c6570dbe3ea2f878d5442383"></a>

### [`0074a794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a794.md) → [`0074a7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a7d4.md) FUN_0074a7d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0074a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a694.md) [`008a3c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3c54.md) [`009aac64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009aa/009aac64.md) [`009ac11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009ac11c.md) [`009afd0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009af/009afd0c.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0054071c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 5件 [`0074a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a6d4.md) [`008a3c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a3/008a3c98.md) [`009aae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009aa/009aae00.md) [`009ac2b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac2b8.md) [`009afea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009af/009afea8.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0054075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054075c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074a7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a794.md#insn-0074a7e8) · [`0074a814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a794.md#insn-0074a814) · [`0074a82c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a794.md#insn-0074a82c)
- 新版 `0074a828`（命令位置の公開資料なし） · `0074a854`（命令位置の公開資料なし） · `0074a86c`（命令位置の公開資料なし）

~~~diff
- 0074a7e8 ["INT_ADD", "register:40f0:8", ["const:74a7e8:8", "const:4:8"]]
- 0074a7e8 ["CALL", null, ["callee:0043bb20:8"]]
+ 0074a828 ["INT_ADD", "register:40f0:8", ["const:74a828:8", "const:4:8"]]
+ 0074a828 ["CALL", null, ["callee:0043bb20:8"]]
- 0074a7e8 bytes bec4f397
+ 0074a828 bytes bec4f397
- 0074a814 ["INT_ADD", "register:40f0:8", ["const:74a814:8", "const:4:8"]]
- 0074a814 ["CALL", null, ["callee:00c57e90:8"]]
+ 0074a854 ["INT_ADD", "register:40f0:8", ["const:74a854:8", "const:4:8"]]
+ 0074a854 ["CALL", null, ["callee:00c57e90:8"]]
- 0074a814 bytes 9f341494
+ 0074a854 bytes 8f351494
- 0074a82c ["INT_ADD", "register:40f0:8", ["const:74a82c:8", "const:4:8"]]
- 0074a82c ["CALL", null, ["callee:00c58000:8"]]
+ 0074a86c ["INT_ADD", "register:40f0:8", ["const:74a86c:8", "const:4:8"]]
+ 0074a86c ["CALL", null, ["callee:00c58000:8"]]
- 0074a82c bytes f5341494
+ 0074a86c bytes e5351494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b2c04d289a7fd98f8478874cef0dfbf"></a>

### [`00755b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00755/00755b20.md) → [`00755b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00755/00755b60.md) FUN_00755b60

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00755a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00755/00755a28.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00755a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00755/00755a68.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00755b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00755/00755b20.md#insn-00755b30)
- 新版 `00755b70`（命令位置の公開資料なし）

~~~diff
- 00755b30 ["INT_ADD", "register:40f0:8", ["const:755b30:8", "const:4:8"]]
- 00755b30 ["CALL", null, ["callee:00755a68:8"]]
+ 00755b70 ["INT_ADD", "register:40f0:8", ["const:755b70:8", "const:4:8"]]
+ 00755b70 ["CALL", null, ["callee:00755a68:8"]]
- 00755b30 bytes beffff97
+ 00755b70 bytes beffff97
~~~


<a id="compare-97ada9861b27944d5d74e9a6d7ca3404"></a>

### [`007583a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00758/007583a4.md) → [`007583e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00758/007583e4.md) FUN_007583e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`007bbddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbddc.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`007bbe1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbe1c.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0075840c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00758/007583a4.md#insn-0075840c) · [`00758490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00758/007583a4.md#insn-00758490)
- 新版 `0075844c`（命令位置の公開資料なし） · `007584d0`（命令位置の公開資料なし）

~~~diff
- 0075840c ["INT_ADD", "register:40f0:8", ["const:75840c:8", "const:4:8"]]
- 0075840c ["CALL", null, ["callee:00c57e90:8"]]
+ 0075844c ["INT_ADD", "register:40f0:8", ["const:75844c:8", "const:4:8"]]
+ 0075844c ["CALL", null, ["callee:00c57e90:8"]]
- 0075840c bytes a1fd1394
+ 0075844c bytes 91fe1394
- 00758490 ["INT_ADD", "register:40f0:8", ["const:758490:8", "const:4:8"]]
- 00758490 ["CALL", null, ["callee:0043bba4:8"]]
+ 007584d0 ["INT_ADD", "register:40f0:8", ["const:7584d0:8", "const:4:8"]]
+ 007584d0 ["CALL", null, ["callee:0043bba4:8"]]
- 00758490 bytes b58df397
+ 007584d0 bytes b58df397
~~~


<a id="compare-7eb69638f6d1e56542ea64d1ff4907ae"></a>

### [`007584b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00758/007584b8.md) → [`007584f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00758/007584f8.md) FUN_007584f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0077bb80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077bb80.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`0077bbc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077b/0077bbc0.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007584d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00758/007584b8.md#insn-007584d8) · [`007584ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00758/007584b8.md#insn-007584ec) · [`007584f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00758/007584b8.md#insn-007584f4)
- 新版 `00758518`（命令位置の公開資料なし） · `0075852c`（命令位置の公開資料なし） · `00758534`（命令位置の公開資料なし）

~~~diff
- 007584d8 ["INT_ADD", "register:40f0:8", ["const:7584d8:8", "const:4:8"]]
- 007584d8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00758518 ["INT_ADD", "register:40f0:8", ["const:758518:8", "const:4:8"]]
+ 00758518 ["CALL", null, ["callee:00c53d00:8"]]
- 007584d8 bytes 02ed1394
+ 00758518 bytes faed1394
- 007584ec ["COPY", "register:0:8", ["register:4040:8"]]
- 007584ec ["INT_ADD", "register:40f0:8", ["const:7584ec:8", "const:4:8"]]
- 007584ec ["CALLIND", null, ["register:0:8"]]
+ 0075852c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0075852c ["INT_ADD", "register:40f0:8", ["const:75852c:8", "const:4:8"]]
+ 0075852c ["CALLIND", null, ["register:0:8"]]
- 007584ec bytes 00013fd6
+ 0075852c bytes 00013fd6
- 007584f4 ["INT_ADD", "register:40f0:8", ["const:7584f4:8", "const:4:8"]]
- 007584f4 ["CALL", null, ["callee:00c57e80:8"]]
+ 00758534 ["INT_ADD", "register:40f0:8", ["const:758534:8", "const:4:8"]]
+ 00758534 ["CALL", null, ["callee:00c57e80:8"]]
- 007584f4 bytes 63fd1394
+ 00758534 bytes 53fe1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5abb42cd993565079110a42cbea0977c"></a>

### [`0075b890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b890.md) → [`0075b8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075b/0075b8d0.md) FUN_0075b8d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0075b8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b890.md#insn-0075b8ac) · [`0075b8bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b890.md#insn-0075b8bc)
- 新版 `0075b8ec`（命令位置の公開資料なし） · `0075b8fc`（命令位置の公開資料なし）

~~~diff
- 0075b8ac ["INT_ADD", "register:40f0:8", ["const:75b8ac:8", "const:4:8"]]
- 0075b8ac ["CALL", null, ["callee:00c57eb0:8"]]
+ 0075b8ec ["INT_ADD", "register:40f0:8", ["const:75b8ec:8", "const:4:8"]]
+ 0075b8ec ["CALL", null, ["callee:00c57eb0:8"]]
- 0075b8ac bytes 81f01394
+ 0075b8ec bytes 71f11394
- 0075b8bc ["INT_ADD", "register:40f0:8", ["const:75b8bc:8", "const:4:8"]]
- 0075b8bc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0075b8fc ["INT_ADD", "register:40f0:8", ["const:75b8fc:8", "const:4:8"]]
+ 0075b8fc ["CALL", null, ["callee:00c57eb0:8"]]
- 0075b8bc bytes 7df01394
+ 0075b8fc bytes 6df11394
~~~


<a id="compare-540bd81f8181cef54f60ab41e10b1904"></a>

### [`0075d548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d548.md) → [`0075d588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075d/0075d588.md) FUN_0075d588

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 12件 [`00664a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664a80.md) [`00664b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664b1c.md) [`00664b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664b8c.md) [`00664dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664dd0.md) [`00664ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664ff8.md)
- 新版 呼出元 1件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) · 呼出先 12件 [`00664ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664ac0.md) [`00664b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664b5c.md) [`00664bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664bcc.md) [`00664e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664e10.md) [`00665038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00665/00665038.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0075d598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d548.md#insn-0075d598) · [`0075d5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d548.md#insn-0075d5a4) · [`0075d5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d548.md#insn-0075d5b4)
- 新版 `0075d5d8`（命令位置の公開資料なし） · `0075d5e4`（命令位置の公開資料なし） · `0075d5f4`（命令位置の公開資料なし）

~~~diff
- 0075d598 ["INT_ADD", "register:40f0:8", ["const:75d598:8", "const:4:8"]]
- 0075d598 ["CALL", null, ["callee:00b2f880:8"]]
+ 0075d5d8 ["INT_ADD", "register:40f0:8", ["const:75d5d8:8", "const:4:8"]]
+ 0075d5d8 ["CALL", null, ["callee:00b2f880:8"]]
- 0075d598 bytes b0470f94
+ 0075d5d8 bytes aa480f94
- 0075d5a4 ["INT_ADD", "register:40f0:8", ["const:75d5a4:8", "const:4:8"]]
- 0075d5a4 ["CALL", null, ["callee:00664ac0:8"]]
+ 0075d5e4 ["INT_ADD", "register:40f0:8", ["const:75d5e4:8", "const:4:8"]]
+ 0075d5e4 ["CALL", null, ["callee:00664ac0:8"]]
- 0075d5a4 bytes 371dfc97
+ 0075d5e4 bytes 371dfc97
- 0075d5b4 ["INT_ADD", "register:40f0:8", ["const:75d5b4:8", "const:4:8"]]
- 0075d5b4 ["CALL", null, ["callee:00664ac0:8"]]
+ 0075d5f4 ["INT_ADD", "register:40f0:8", ["const:75d5f4:8", "const:4:8"]]
+ 0075d5f4 ["CALL", null, ["callee:00664ac0:8"]]
- 0075d5b4 bytes 331dfc97
+ 0075d5f4 bytes 331dfc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff329d802c16f52ffc5008eac65951ce"></a>

### [`0075e884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075e884.md) → [`0075e8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075e8c4.md) FUN_0075e8c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0075e548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075e548.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0077c8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c8d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0075e588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075e588.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0077c910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c910.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0075e8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075e884.md#insn-0075e8fc) · [`0075e910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075e884.md#insn-0075e910) · [`0075e968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075e884.md#insn-0075e968)
- 新版 `0075e93c`（命令位置の公開資料なし） · `0075e950`（命令位置の公開資料なし） · `0075e9a8`（命令位置の公開資料なし）

~~~diff
- 0075e8fc ["INT_ADD", "register:40f0:8", ["const:75e8fc:8", "const:4:8"]]
- 0075e8fc ["CALL", null, ["callee:0043bb20:8"]]
+ 0075e93c ["INT_ADD", "register:40f0:8", ["const:75e93c:8", "const:4:8"]]
+ 0075e93c ["CALL", null, ["callee:0043bb20:8"]]
- 0075e8fc bytes 7974f397
+ 0075e93c bytes 7974f397
- 0075e910 ["INT_ADD", "register:40f0:8", ["const:75e910:8", "const:4:8"]]
- 0075e910 ["CALL", null, ["callee:0043bb20:8"]]
+ 0075e950 ["INT_ADD", "register:40f0:8", ["const:75e950:8", "const:4:8"]]
+ 0075e950 ["CALL", null, ["callee:0043bb20:8"]]
- 0075e910 bytes 7474f397
+ 0075e950 bytes 7474f397
- 0075e968 ["INT_ADD", "register:40f0:8", ["const:75e968:8", "const:4:8"]]
- 0075e968 ["CALL", null, ["callee:0077c910:8"]]
+ 0075e9a8 ["INT_ADD", "register:40f0:8", ["const:75e9a8:8", "const:4:8"]]
+ 0075e9a8 ["CALL", null, ["callee:0077c910:8"]]
- 0075e968 bytes da770094
+ 0075e9a8 bytes da770094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94f245946723c1520a39c76a3abf3b29"></a>

### [`00763c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00763/00763c50.md) → [`00763c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00763/00763c90.md) FUN_00763c90

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`00a8e3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8e/00a8e3bc.md) · 呼出先 5件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0066d054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d054.md) [`00b353c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b353c0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`00a8e5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8e/00a8e5b4.md) · 呼出先 5件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0066d094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066d/0066d094.md) [`00b357e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b357e8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00763c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00763/00763c50.md#insn-00763c74) · [`00763c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00763/00763c50.md#insn-00763c88) · [`00763c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00763/00763c50.md#insn-00763c98)
- 新版 `00763cb4`（命令位置の公開資料なし） · `00763cc8`（命令位置の公開資料なし） · `00763cd8`（命令位置の公開資料なし）

~~~diff
- 00763c74 ["INT_ADD", "register:40f0:8", ["const:763c74:8", "const:4:8"]]
- 00763c74 ["CALL", null, ["callee:0066d094:8"]]
+ 00763cb4 ["INT_ADD", "register:40f0:8", ["const:763cb4:8", "const:4:8"]]
+ 00763cb4 ["CALL", null, ["callee:0066d094:8"]]
- 00763c74 bytes f824fc97
+ 00763cb4 bytes f824fc97
- 00763c88 ["INT_ADD", "register:40f0:8", ["const:763c88:8", "const:4:8"]]
- 00763c88 ["CALL", null, ["callee:00447ef4:8"]]
+ 00763cc8 ["INT_ADD", "register:40f0:8", ["const:763cc8:8", "const:4:8"]]
+ 00763cc8 ["CALL", null, ["callee:00447ef4:8"]]
- 00763c88 bytes 8b90f397
+ 00763cc8 bytes 8b90f397
- 00763c98 ["INT_ADD", "register:40f0:8", ["const:763c98:8", "const:4:8"]]
- 00763c98 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00763cd8 ["INT_ADD", "register:40f0:8", ["const:763cd8:8", "const:4:8"]]
+ 00763cd8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00763c98 bytes 86cf1394
+ 00763cd8 bytes 76d01394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5173aac523433b3a61720de66ea986c"></a>

### [`00766dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/00766dd0.md) → [`00766e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00766/00766e10.md) FUN_00766e10

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0076621c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/0076621c.md) [`00767108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767108.md) [`00769c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769c98.md) · 呼出先 8件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00550be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be8.md) [`00550cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550cec.md) [`00597e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e7c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 3件 [`0076625c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00766/0076625c.md) [`00767148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767148.md) [`00769cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769cd8.md) · 呼出先 8件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00550c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c28.md) [`00550d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550d2c.md) [`00597ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ebc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00766df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/00766dd0.md#insn-00766df4) · [`00766e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/00766dd0.md#insn-00766e04) · [`00766e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/00766dd0.md#insn-00766e0c)
- 新版 `00766e34`（命令位置の公開資料なし） · `00766e44`（命令位置の公開資料なし） · `00766e4c`（命令位置の公開資料なし）

~~~diff
- 00766df4 ["INT_ADD", "register:40f0:8", ["const:766df4:8", "const:4:8"]]
- 00766df4 ["CALL", null, ["callee:00550c28:8"]]
+ 00766e34 ["INT_ADD", "register:40f0:8", ["const:766e34:8", "const:4:8"]]
+ 00766e34 ["CALL", null, ["callee:00550c28:8"]]
- 00766df4 bytes 7da7f797
+ 00766e34 bytes 7da7f797
- 00766e04 ["INT_ADD", "register:40f0:8", ["const:766e04:8", "const:4:8"]]
- 00766e04 ["CALL", null, ["callee:0043dba4:8"]]
+ 00766e44 ["INT_ADD", "register:40f0:8", ["const:766e44:8", "const:4:8"]]
+ 00766e44 ["CALL", null, ["callee:0043dba4:8"]]
- 00766e04 bytes 585bf397
+ 00766e44 bytes 585bf397
- 00766e0c ["INT_ADD", "register:40f0:8", ["const:766e0c:8", "const:4:8"]]
- 00766e0c ["CALL", null, ["callee:00550d2c:8"]]
+ 00766e4c ["INT_ADD", "register:40f0:8", ["const:766e4c:8", "const:4:8"]]
+ 00766e4c ["CALL", null, ["callee:00550d2c:8"]]
- 00766e0c bytes b8a7f797
+ 00766e4c bytes b8a7f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-292f7d0a196b3af1fe3af43df2a3bc77"></a>

### [`00767c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767c74.md) → [`00767cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767cb4.md) FUN_00767cb4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00697250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697250.md) [`00767d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767d64.md) [`00769220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769220.md) [`007697b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/007697b4.md) · 呼出先 5件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00550be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be8.md) [`00765ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/00765ddc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 4件 [`00697290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697290.md) [`00767da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767da4.md) [`00769260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769260.md) [`007697f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/007697f4.md) · 呼出先 5件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00550c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c28.md) [`00765e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00765/00765e1c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00767cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767c74.md#insn-00767cac) · [`00767cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767c74.md#insn-00767cbc) · [`00767cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767c74.md#insn-00767cd0)
- 新版 `00767cec`（命令位置の公開資料なし） · `00767cfc`（命令位置の公開資料なし） · `00767d10`（命令位置の公開資料なし）

~~~diff
- 00767cac ["INT_ADD", "register:40f0:8", ["const:767cac:8", "const:4:8"]]
- 00767cac ["CALL", null, ["callee:00550c28:8"]]
+ 00767cec ["INT_ADD", "register:40f0:8", ["const:767cec:8", "const:4:8"]]
+ 00767cec ["CALL", null, ["callee:00550c28:8"]]
- 00767cac bytes cfa3f797
+ 00767cec bytes cfa3f797
- 00767cbc ["INT_ADD", "register:40f0:8", ["const:767cbc:8", "const:4:8"]]
- 00767cbc ["CALL", null, ["callee:0043dba4:8"]]
+ 00767cfc ["INT_ADD", "register:40f0:8", ["const:767cfc:8", "const:4:8"]]
+ 00767cfc ["CALL", null, ["callee:0043dba4:8"]]
- 00767cbc bytes aa57f397
+ 00767cfc bytes aa57f397
- 00767cd0 ["INT_ADD", "register:40f0:8", ["const:767cd0:8", "const:4:8"]]
- 00767cd0 ["CALL", null, ["callee:00765e1c:8"]]
+ 00767d10 ["INT_ADD", "register:40f0:8", ["const:767d10:8", "const:4:8"]]
+ 00767d10 ["CALL", null, ["callee:00765e1c:8"]]
- 00767cd0 bytes 43f8ff97
+ 00767d10 bytes 43f8ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2d0aebdeb8c804379adc72e3e1833a7"></a>

### [`00768d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768d24.md) → [`00768d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/00768d64.md) FUN_00768d64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00768ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768ba8.md) · 呼出先 3件 [`00449978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/00449978.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00768be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/00768be8.md) · 呼出先 3件 [`004499b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00449/004499b8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00768d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768d24.md#insn-00768d5c) · [`00768d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768d24.md#insn-00768d74) · [`00768d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768d24.md#insn-00768d9c)
- 新版 `00768d9c`（命令位置の公開資料なし） · `00768db4`（命令位置の公開資料なし） · `00768ddc`（命令位置の公開資料なし）

~~~diff
- 00768d5c ["INT_ADD", "register:40f0:8", ["const:768d5c:8", "const:4:8"]]
- 00768d5c ["CALL", null, ["callee:00c57e90:8"]]
+ 00768d9c ["INT_ADD", "register:40f0:8", ["const:768d9c:8", "const:4:8"]]
+ 00768d9c ["CALL", null, ["callee:00c57e90:8"]]
- 00768d5c bytes 4dbb1394
+ 00768d9c bytes 3dbc1394
- 00768d74 ["INT_ADD", "register:40f0:8", ["const:768d74:8", "const:4:8"]]
- 00768d74 ["CALL", null, ["callee:00c58000:8"]]
+ 00768db4 ["INT_ADD", "register:40f0:8", ["const:768db4:8", "const:4:8"]]
+ 00768db4 ["CALL", null, ["callee:00c58000:8"]]
- 00768d74 bytes a3bb1394
+ 00768db4 bytes 93bc1394
- 00768d9c ["INT_ADD", "register:40f0:8", ["const:768d9c:8", "const:4:8"]]
- 00768d9c ["CALL", null, ["callee:00c57e90:8"]]
+ 00768ddc ["INT_ADD", "register:40f0:8", ["const:768ddc:8", "const:4:8"]]
+ 00768ddc ["CALL", null, ["callee:00c57e90:8"]]
- 00768d9c bytes 3dbb1394
+ 00768ddc bytes 2dbc1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6ae21962509635b0362284c1661f5a6"></a>

### [`007696e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/007696e0.md) → [`00769720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769720.md) FUN_00769720

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00769734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/007696e0.md#insn-00769734)
- 新版 `00769774`（命令位置の公開資料なし）

~~~diff
- 00769734 ["INT_ADD", "register:40f0:8", ["const:769734:8", "const:4:8"]]
- 00769734 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00769774 ["INT_ADD", "register:40f0:8", ["const:769774:8", "const:4:8"]]
+ 00769774 ["CALL", null, ["callee:00c57eb0:8"]]
- 00769734 bytes dfb81394
+ 00769774 bytes cfb91394
~~~


<a id="compare-b7aa6b0b22286619ac4075afd2ad6d87"></a>

### [`00769764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769764.md) → [`007697a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/007697a4.md) FUN_007697a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00769780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769764.md#insn-00769780) · [`007697a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769764.md#insn-007697a0)
- 新版 `007697c0`（命令位置の公開資料なし） · `007697e0`（命令位置の公開資料なし）

~~~diff
- 00769780 ["INT_ADD", "register:40f0:8", ["const:769780:8", "const:4:8"]]
- 00769780 ["CALL", null, ["callee:00c53d00:8"]]
+ 007697c0 ["INT_ADD", "register:40f0:8", ["const:7697c0:8", "const:4:8"]]
+ 007697c0 ["CALL", null, ["callee:00c53d00:8"]]
- 00769780 bytes 58a81394
+ 007697c0 bytes 50a91394
- 007697a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 007697a0 ["INT_ADD", "register:40f0:8", ["const:7697a0:8", "const:4:8"]]
- 007697a0 ["CALLIND", null, ["register:0:8"]]
+ 007697e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007697e0 ["INT_ADD", "register:40f0:8", ["const:7697e0:8", "const:4:8"]]
+ 007697e0 ["CALLIND", null, ["register:0:8"]]
- 007697a0 bytes 00013fd6
+ 007697e0 bytes 00013fd6
~~~


<a id="compare-d6189053fb4783aa56859a2819416e9b"></a>

### [`00773554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773554.md) → [`00773594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773594.md) FUN_00773594

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`00893d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893d78.md) [`0089c00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089c/0089c00c.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 6件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`00893dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893dbc.md) [`0089bc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089bc8c.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007735b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773554.md#insn-007735b4) · [`007735c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773554.md#insn-007735c8) · [`007735f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773554.md#insn-007735f0)
- 新版 `007735f4`（命令位置の公開資料なし） · `00773608`（命令位置の公開資料なし） · `00773630`（命令位置の公開資料なし）

~~~diff
- 007735b4 ["INT_ADD", "register:40f0:8", ["const:7735b4:8", "const:4:8"]]
- 007735b4 ["CALL", null, ["callee:0043bb20:8"]]
+ 007735f4 ["INT_ADD", "register:40f0:8", ["const:7735f4:8", "const:4:8"]]
+ 007735f4 ["CALL", null, ["callee:0043bb20:8"]]
- 007735b4 bytes 4b21f397
+ 007735f4 bytes 4b21f397
- 007735c8 ["INT_ADD", "register:40f0:8", ["const:7735c8:8", "const:4:8"]]
- 007735c8 ["CALL", null, ["callee:00442b38:8"]]
+ 00773608 ["INT_ADD", "register:40f0:8", ["const:773608:8", "const:4:8"]]
+ 00773608 ["CALL", null, ["callee:00442b38:8"]]
- 007735c8 bytes 4c3df397
+ 00773608 bytes 4c3df397
- 007735f0 ["INT_ADD", "register:40f0:8", ["const:7735f0:8", "const:4:8"]]
- 007735f0 ["CALL", null, ["callee:0043bb20:8"]]
+ 00773630 ["INT_ADD", "register:40f0:8", ["const:773630:8", "const:4:8"]]
+ 00773630 ["CALL", null, ["callee:0043bb20:8"]]
- 007735f0 bytes 3c21f397
+ 00773630 bytes 3c21f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acf832683321a43024ee6da474a604ae"></a>

### [`0077365c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/0077365c.md) → [`0077369c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/0077369c.md) FUN_0077369c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 5件 [`0077c80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c80c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 5件 [`0077c84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c84c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007736c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/0077365c.md#insn-007736c0) · [`007736d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/0077365c.md#insn-007736d8) · [`007736f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/0077365c.md#insn-007736f4)
- 新版 `00773700`（命令位置の公開資料なし） · `00773718`（命令位置の公開資料なし） · `00773734`（命令位置の公開資料なし）

~~~diff
- 007736c0 ["INT_ADD", "register:40f0:8", ["const:7736c0:8", "const:4:8"]]
- 007736c0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00773700 ["INT_ADD", "register:40f0:8", ["const:773700:8", "const:4:8"]]
+ 00773700 ["CALL", null, ["callee:00c57e90:8"]]
- 007736c0 bytes f4901394
+ 00773700 bytes e4911394
- 007736d8 ["INT_ADD", "register:40f0:8", ["const:7736d8:8", "const:4:8"]]
- 007736d8 ["CALL", null, ["callee:00c58000:8"]]
+ 00773718 ["INT_ADD", "register:40f0:8", ["const:773718:8", "const:4:8"]]
+ 00773718 ["CALL", null, ["callee:00c58000:8"]]
- 007736d8 bytes 4a911394
+ 00773718 bytes 3a921394
- 007736f4 ["INT_ADD", "register:40f0:8", ["const:7736f4:8", "const:4:8"]]
- 007736f4 ["CALL", null, ["callee:0077c84c:8"]]
+ 00773734 ["INT_ADD", "register:40f0:8", ["const:773734:8", "const:4:8"]]
+ 00773734 ["CALL", null, ["callee:0077c84c:8"]]
- 007736f4 bytes 46240094
+ 00773734 bytes 46240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92478103858072b7e5c90fc5447368f7"></a>

### [`0077376c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/0077376c.md) → [`007737ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/007737ac.md) FUN_007737ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007737d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/0077376c.md#insn-007737d4) · [`0077382c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/0077376c.md#insn-0077382c)
- 新版 `00773814`（命令位置の公開資料なし） · `0077386c`（命令位置の公開資料なし）

~~~diff
- 007737d4 ["INT_ADD", "register:40f0:8", ["const:7737d4:8", "const:4:8"]]
- 007737d4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00773814 ["INT_ADD", "register:40f0:8", ["const:773814:8", "const:4:8"]]
+ 00773814 ["CALL", null, ["callee:00c57e90:8"]]
- 007737d4 bytes af901394
+ 00773814 bytes 9f911394
- 0077382c ["INT_ADD", "register:40f0:8", ["const:77382c:8", "const:4:8"]]
- 0077382c ["CALL", null, ["callee:0043bba4:8"]]
+ 0077386c ["INT_ADD", "register:40f0:8", ["const:77386c:8", "const:4:8"]]
+ 0077386c ["CALL", null, ["callee:0043bba4:8"]]
- 0077382c bytes ce20f397
+ 0077386c bytes ce20f397
~~~


<a id="compare-5eccef3d9822a6414b96b9049c4ee7aa"></a>

### [`0077acec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077a/0077acec.md) → [`0077ad2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077a/0077ad2c.md) FUN_0077ad2c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00613c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/00613c24.md) · 呼出先 7件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00468f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f0c.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aecc.md) [`0046da1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da1c.md)
- 新版 呼出元 1件 [`00613c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00613/00613c64.md) · 呼出先 7件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00468f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f4c.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046af0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af0c.md) [`0046da5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046da5c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0077ad2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077a/0077acec.md#insn-0077ad2c) · [`0077ad44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077a/0077acec.md#insn-0077ad44) · [`0077ad90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077a/0077acec.md#insn-0077ad90)
- 新版 `0077ad6c`（命令位置の公開資料なし） · `0077ad84`（命令位置の公開資料なし） · `0077add0`（命令位置の公開資料なし）

~~~diff
- 0077ad2c ["INT_ADD", "register:40f0:8", ["const:77ad2c:8", "const:4:8"]]
- 0077ad2c ["CALL", null, ["callee:00467860:8"]]
+ 0077ad6c ["INT_ADD", "register:40f0:8", ["const:77ad6c:8", "const:4:8"]]
+ 0077ad6c ["CALL", null, ["callee:00467860:8"]]
- 0077ad2c bytes bdb2f397
+ 0077ad6c bytes bdb2f397
- 0077ad44 ["INT_ADD", "register:40f0:8", ["const:77ad44:8", "const:4:8"]]
- 0077ad44 ["CALL", null, ["callee:00468f88:8"]]
+ 0077ad84 ["INT_ADD", "register:40f0:8", ["const:77ad84:8", "const:4:8"]]
+ 0077ad84 ["CALL", null, ["callee:00468f88:8"]]
- 0077ad44 bytes 81b8f397
+ 0077ad84 bytes 81b8f397
- 0077ad90 ["INT_ADD", "register:40f0:8", ["const:77ad90:8", "const:4:8"]]
- 0077ad90 ["CALL", null, ["callee:00489f4c:8"]]
+ 0077add0 ["INT_ADD", "register:40f0:8", ["const:77add0:8", "const:4:8"]]
+ 0077add0 ["CALL", null, ["callee:00489f4c:8"]]
- 0077ad90 bytes 5f3cf497
+ 0077add0 bytes 5f3cf497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb4fe9fa3d4abe3fbb9e059818b08656"></a>

### [`0077b218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077b218.md) → [`0077b258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077b/0077b258.md) FUN_0077b258

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0077b250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077b218.md#insn-0077b250) · [`0077b25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077b218.md#insn-0077b25c)
- 新版 `0077b290`（命令位置の公開資料なし） · `0077b29c`（命令位置の公開資料なし）

~~~diff
- 0077b250 ["INT_ADD", "register:40f0:8", ["const:77b250:8", "const:4:8"]]
- 0077b250 ["CALL", null, ["callee:005c179c:8"]]
+ 0077b290 ["INT_ADD", "register:40f0:8", ["const:77b290:8", "const:4:8"]]
+ 0077b290 ["CALL", null, ["callee:005c179c:8"]]
- 0077b250 bytes 4319f997
+ 0077b290 bytes 4319f997
- 0077b25c ["INT_ADD", "register:40f0:8", ["const:77b25c:8", "const:4:8"]]
- 0077b25c ["CALL", null, ["callee:005c179c:8"]]
+ 0077b29c ["INT_ADD", "register:40f0:8", ["const:77b29c:8", "const:4:8"]]
+ 0077b29c ["CALL", null, ["callee:005c179c:8"]]
- 0077b25c bytes 4019f997
+ 0077b29c bytes 4019f997
~~~


<a id="compare-f924c4f68b05580f769347076c41a0af"></a>

### [`0077bff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077bff4.md) → [`0077c034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c034.md) FUN_0077c034

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0077bb80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077bb80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0077bbc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077b/0077bbc0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0077c004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077bff4.md#insn-0077c004)
- 新版 `0077c044`（命令位置の公開資料なし）

~~~diff
- 0077c004 ["INT_ADD", "register:40f0:8", ["const:77c004:8", "const:4:8"]]
- 0077c004 ["CALL", null, ["callee:0077bbc0:8"]]
+ 0077c044 ["INT_ADD", "register:40f0:8", ["const:77c044:8", "const:4:8"]]
+ 0077c044 ["CALL", null, ["callee:0077bbc0:8"]]
- 0077c004 bytes dffeff97
+ 0077c044 bytes dffeff97
~~~


<a id="compare-52cc45a308f91ffd966d654f25cd2619"></a>

### [`0077c150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c150.md) → [`0077c190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c190.md) FUN_0077c190

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0075d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md) · 呼出先 8件 [`0072604c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/0072604c.md) [`00726060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726060.md) [`007260c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/007260c4.md) [`0077c51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c51c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 1件 [`0075d75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075d/0075d75c.md) · 呼出先 8件 [`0072608c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/0072608c.md) [`007260a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/007260a0.md) [`00726104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726104.md) [`0077c55c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c55c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0077c1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c150.md#insn-0077c1e4) · [`0077c1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c150.md#insn-0077c1f4) · [`0077c284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c150.md#insn-0077c284)
- 新版 `0077c224`（命令位置の公開資料なし） · `0077c234`（命令位置の公開資料なし） · `0077c2c4`（命令位置の公開資料なし）

~~~diff
- 0077c1e4 ["INT_ADD", "register:40f0:8", ["const:77c1e4:8", "const:4:8"]]
- 0077c1e4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0077c224 ["INT_ADD", "register:40f0:8", ["const:77c224:8", "const:4:8"]]
+ 0077c224 ["CALL", null, ["callee:00c57eb0:8"]]
- 0077c1e4 bytes 336e1394
+ 0077c224 bytes 236f1394
- 0077c1f4 ["INT_ADD", "register:40f0:8", ["const:77c1f4:8", "const:4:8"]]
- 0077c1f4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0077c234 ["INT_ADD", "register:40f0:8", ["const:77c234:8", "const:4:8"]]
+ 0077c234 ["CALL", null, ["callee:00c57eb0:8"]]
- 0077c1f4 bytes 2f6e1394
+ 0077c234 bytes 1f6f1394
- 0077c284 ["INT_ADD", "register:40f0:8", ["const:77c284:8", "const:4:8"]]
- 0077c284 ["CALL", null, ["callee:0077c55c:8"]]
+ 0077c2c4 ["INT_ADD", "register:40f0:8", ["const:77c2c4:8", "const:4:8"]]
+ 0077c2c4 ["CALL", null, ["callee:0077c55c:8"]]
- 0077c284 bytes a6000094
+ 0077c2c4 bytes a6000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dadc1bea1b48082da98cde1274e1c29f"></a>

### [`0077c51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c51c.md) → [`0077c55c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c55c.md) FUN_0077c55c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0077c150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c150.md) · 呼出先 5件 [`00726220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726220.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`0077c190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c190.md) · 呼出先 5件 [`00726260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726260.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0077c570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c51c.md#insn-0077c570) · [`0077c5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c51c.md#insn-0077c5d4) · [`0077c5fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c51c.md#insn-0077c5fc)
- 新版 `0077c5b0`（命令位置の公開資料なし） · `0077c614`（命令位置の公開資料なし） · `0077c63c`（命令位置の公開資料なし）

~~~diff
- 0077c570 ["INT_ADD", "register:40f0:8", ["const:77c570:8", "const:4:8"]]
- 0077c570 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0077c5b0 ["INT_ADD", "register:40f0:8", ["const:77c5b0:8", "const:4:8"]]
+ 0077c5b0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0077c570 bytes 506d1394
+ 0077c5b0 bytes 406e1394
- 0077c5d4 ["INT_ADD", "register:40f0:8", ["const:77c5d4:8", "const:4:8"]]
- 0077c5d4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0077c614 ["INT_ADD", "register:40f0:8", ["const:77c614:8", "const:4:8"]]
+ 0077c614 ["CALL", null, ["callee:00c57e90:8"]]
- 0077c5d4 bytes 2f6d1394
+ 0077c614 bytes 1f6e1394
- 0077c5fc ["INT_ADD", "register:40f0:8", ["const:77c5fc:8", "const:4:8"]]
- 0077c5fc ["CALL", null, ["callee:00c58000:8"]]
+ 0077c63c ["INT_ADD", "register:40f0:8", ["const:77c63c:8", "const:4:8"]]
+ 0077c63c ["CALL", null, ["callee:00c58000:8"]]
- 0077c5fc bytes 816d1394
+ 0077c63c bytes 716e1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e09171cbbbade55360c19c1400a32aa"></a>

### [`0077c680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c680.md) → [`0077c6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c6c0.md) FUN_0077c6c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00768ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768ba8.md) · 呼出先 5件 [`00449978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/00449978.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00768be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/00768be8.md) · 呼出先 5件 [`004499b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00449/004499b8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0077c6c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c680.md#insn-0077c6c4) · [`0077c6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c680.md#insn-0077c6fc) · [`0077c724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c680.md#insn-0077c724)
- 新版 `0077c704`（命令位置の公開資料なし） · `0077c73c`（命令位置の公開資料なし） · `0077c764`（命令位置の公開資料なし）

~~~diff
- 0077c6c4 ["INT_ADD", "register:40f0:8", ["const:77c6c4:8", "const:4:8"]]
- 0077c6c4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0077c704 ["INT_ADD", "register:40f0:8", ["const:77c704:8", "const:4:8"]]
+ 0077c704 ["CALL", null, ["callee:00c57eb0:8"]]
- 0077c6c4 bytes fb6c1394
+ 0077c704 bytes eb6d1394
- 0077c6fc ["INT_ADD", "register:40f0:8", ["const:77c6fc:8", "const:4:8"]]
- 0077c6fc ["CALL", null, ["callee:00c57e90:8"]]
+ 0077c73c ["INT_ADD", "register:40f0:8", ["const:77c73c:8", "const:4:8"]]
+ 0077c73c ["CALL", null, ["callee:00c57e90:8"]]
- 0077c6fc bytes e56c1394
+ 0077c73c bytes d56d1394
- 0077c724 ["INT_ADD", "register:40f0:8", ["const:77c724:8", "const:4:8"]]
- 0077c724 ["CALL", null, ["callee:00c58000:8"]]
+ 0077c764 ["INT_ADD", "register:40f0:8", ["const:77c764:8", "const:4:8"]]
+ 0077c764 ["CALL", null, ["callee:00c58000:8"]]
- 0077c724 bytes 376d1394
+ 0077c764 bytes 276e1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c97e23ef8d7f26984b56be2c6b0de81"></a>

### [`0077c7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c7e0.md) → [`0077c820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c820.md) FUN_0077c820

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0077c7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c7e0.md#insn-0077c7f4)
- 新版 `0077c834`（命令位置の公開資料なし）

~~~diff
- 0077c7f4 ["INT_ADD", "register:40f0:8", ["const:77c7f4:8", "const:4:8"]]
- 0077c7f4 ["CALL", null, ["callee:00c580d0:8"]]
+ 0077c834 ["INT_ADD", "register:40f0:8", ["const:77c834:8", "const:4:8"]]
+ 0077c834 ["CALL", null, ["callee:00c580d0:8"]]
- 0077c7f4 bytes 376d1394
+ 0077c834 bytes 276e1394
~~~


<a id="compare-179c4c06190f41805f27c66f2a6840d7"></a>

### [`0077c820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c820.md) → [`0077c860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c860.md) FUN_0077c860

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0075b8e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b8e4.md) · 呼出先 2件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0075b924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075b/0075b924.md) · 呼出先 2件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0077c884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c820.md#insn-0077c884) · [`0077c894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c820.md#insn-0077c894) · [`0077c8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c820.md#insn-0077c8a4)
- 新版 `0077c8c4`（命令位置の公開資料なし） · `0077c8d4`（命令位置の公開資料なし） · `0077c8e4`（命令位置の公開資料なし）

~~~diff
- 0077c884 ["INT_ADD", "register:40f0:8", ["const:77c884:8", "const:4:8"]]
- 0077c884 ["CALL", null, ["callee:00494610:8"]]
+ 0077c8c4 ["INT_ADD", "register:40f0:8", ["const:77c8c4:8", "const:4:8"]]
+ 0077c8c4 ["CALL", null, ["callee:00494610:8"]]
- 0077c884 bytes 535ff497
+ 0077c8c4 bytes 535ff497
- 0077c894 ["INT_ADD", "register:40f0:8", ["const:77c894:8", "const:4:8"]]
- 0077c894 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0077c8d4 ["INT_ADD", "register:40f0:8", ["const:77c8d4:8", "const:4:8"]]
+ 0077c8d4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0077c894 bytes 876c1394
+ 0077c8d4 bytes 776d1394
- 0077c8a4 ["INT_ADD", "register:40f0:8", ["const:77c8a4:8", "const:4:8"]]
- 0077c8a4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0077c8e4 ["INT_ADD", "register:40f0:8", ["const:77c8e4:8", "const:4:8"]]
+ 0077c8e4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0077c8a4 bytes 836c1394
+ 0077c8e4 bytes 736d1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-994861637073f3aff76829c8741dfd4a"></a>

### [`0077c8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c8d0.md) → [`0077c910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c910.md) FUN_0077c910

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0075e884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075e884.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0077ca54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077ca54.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0075e8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075e8c4.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0077ca94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077ca94.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0077c948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c8d0.md#insn-0077c948) · [`0077c95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c8d0.md#insn-0077c95c) · [`0077c9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c8d0.md#insn-0077c9b8)
- 新版 `0077c988`（命令位置の公開資料なし） · `0077c99c`（命令位置の公開資料なし） · `0077c9f8`（命令位置の公開資料なし）

~~~diff
- 0077c948 ["INT_ADD", "register:40f0:8", ["const:77c948:8", "const:4:8"]]
- 0077c948 ["CALL", null, ["callee:0043bb20:8"]]
+ 0077c988 ["INT_ADD", "register:40f0:8", ["const:77c988:8", "const:4:8"]]
+ 0077c988 ["CALL", null, ["callee:0043bb20:8"]]
- 0077c948 bytes 66fcf297
+ 0077c988 bytes 66fcf297
- 0077c95c ["INT_ADD", "register:40f0:8", ["const:77c95c:8", "const:4:8"]]
- 0077c95c ["CALL", null, ["callee:0043bb20:8"]]
+ 0077c99c ["INT_ADD", "register:40f0:8", ["const:77c99c:8", "const:4:8"]]
+ 0077c99c ["CALL", null, ["callee:0043bb20:8"]]
- 0077c95c bytes 61fcf297
+ 0077c99c bytes 61fcf297
- 0077c9b8 ["INT_ADD", "register:40f0:8", ["const:77c9b8:8", "const:4:8"]]
- 0077c9b8 ["CALL", null, ["callee:0077ca94:8"]]
+ 0077c9f8 ["INT_ADD", "register:40f0:8", ["const:77c9f8:8", "const:4:8"]]
+ 0077c9f8 ["CALL", null, ["callee:0077ca94:8"]]
- 0077c9b8 bytes 27000094
+ 0077c9f8 bytes 27000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e36c68aebbba0842d8c8e6816d07d313"></a>

### [`00782ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782ae0.md) → [`00782b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/00782b20.md) FUN_00782b20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00782afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782ae0.md#insn-00782afc) · [`00782b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782ae0.md#insn-00782b1c)
- 新版 `00782b3c`（命令位置の公開資料なし） · `00782b5c`（命令位置の公開資料なし）

~~~diff
- 00782afc ["INT_ADD", "register:40f0:8", ["const:782afc:8", "const:4:8"]]
- 00782afc ["CALL", null, ["callee:00c53d00:8"]]
+ 00782b3c ["INT_ADD", "register:40f0:8", ["const:782b3c:8", "const:4:8"]]
+ 00782b3c ["CALL", null, ["callee:00c53d00:8"]]
- 00782afc bytes 79431394
+ 00782b3c bytes 71441394
- 00782b1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00782b1c ["INT_ADD", "register:40f0:8", ["const:782b1c:8", "const:4:8"]]
- 00782b1c ["CALLIND", null, ["register:0:8"]]
+ 00782b5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00782b5c ["INT_ADD", "register:40f0:8", ["const:782b5c:8", "const:4:8"]]
+ 00782b5c ["CALLIND", null, ["register:0:8"]]
- 00782b1c bytes 00013fd6
+ 00782b5c bytes 00013fd6
~~~


<a id="compare-124a0e53805266ba98b6077bbc538c89"></a>

### [`00783974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783974.md) → [`007839b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/007839b4.md) FUN_007839b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00783994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783974.md#insn-00783994)
- 新版 `007839d4`（命令位置の公開資料なし）

~~~diff
- 00783994 ["INT_ADD", "register:40f0:8", ["const:783994:8", "const:4:8"]]
- 00783994 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007839d4 ["INT_ADD", "register:40f0:8", ["const:7839d4:8", "const:4:8"]]
+ 007839d4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00783994 bytes 47501394
+ 007839d4 bytes 37511394
~~~


<a id="compare-e339bc35fbf1be91bb660edaef453fe6"></a>

### [`00784240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784240.md) → [`00784280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00784/00784280.md) FUN_00784280

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 12件 [`007839a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007839a8.md) [`00796ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/00796ab8.md) [`00878718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878718.md) [`00878ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878ec8.md) [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 3件 [`00c58030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58030.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a500.md)
- 新版 呼出元 12件 [`007839e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/007839e8.md) [`00796af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00796/00796af8.md) [`00878758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878758.md) [`00878f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878f08.md) [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 3件 [`00c58430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58430.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a900.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00784278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784240.md#insn-00784278) · [`007842b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784240.md#insn-007842b0)
- 新版 `007842b8`（命令位置の公開資料なし） · `007842f0`（命令位置の公開資料なし）

~~~diff
- 00784278 ["INT_ADD", "register:40f0:8", ["const:784278:8", "const:4:8"]]
- 00784278 ["CALL", null, ["callee:00c5a830:8"]]
+ 007842b8 ["INT_ADD", "register:40f0:8", ["const:7842b8:8", "const:4:8"]]
+ 007842b8 ["CALL", null, ["callee:00c5a830:8"]]
- 00784278 bytes 6e581394
+ 007842b8 bytes 5e591394
- 007842b0 ["INT_ADD", "register:40f0:8", ["const:7842b0:8", "const:4:8"]]
- 007842b0 ["CALL", null, ["callee:00c5a830:8"]]
+ 007842f0 ["INT_ADD", "register:40f0:8", ["const:7842f0:8", "const:4:8"]]
+ 007842f0 ["CALL", null, ["callee:00c5a830:8"]]
- 007842b0 bytes 60581394
+ 007842f0 bytes 50591394
~~~


<a id="compare-9ae6102c04cb221ef75304eb4a940b26"></a>

### [`00785ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785ffc.md) → [`0078603c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/0078603c.md) FUN_0078603c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0078610c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/0078610c.md) [`007877bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007877bc.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 2件 [`0078614c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/0078614c.md) [`007877fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/007877fc.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007860a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785ffc.md#insn-007860a0) · [`007860c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785ffc.md#insn-007860c8) · [`007860dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785ffc.md#insn-007860dc)
- 新版 `007860e0`（命令位置の公開資料なし） · `00786108`（命令位置の公開資料なし） · `0078611c`（命令位置の公開資料なし）

~~~diff
- 007860a0 ["INT_ADD", "register:40f0:8", ["const:7860a0:8", "const:4:8"]]
- 007860a0 ["CALL", null, ["callee:00c57e90:8"]]
+ 007860e0 ["INT_ADD", "register:40f0:8", ["const:7860e0:8", "const:4:8"]]
+ 007860e0 ["CALL", null, ["callee:00c57e90:8"]]
- 007860a0 bytes 7c461394
+ 007860e0 bytes 6c471394
- 007860c8 ["INT_ADD", "register:40f0:8", ["const:7860c8:8", "const:4:8"]]
- 007860c8 ["CALL", null, ["callee:00c58000:8"]]
+ 00786108 ["INT_ADD", "register:40f0:8", ["const:786108:8", "const:4:8"]]
+ 00786108 ["CALL", null, ["callee:00c58000:8"]]
- 007860c8 bytes ce461394
+ 00786108 bytes be471394
- 007860dc ["INT_ADD", "register:40f0:8", ["const:7860dc:8", "const:4:8"]]
- 007860dc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0078611c ["INT_ADD", "register:40f0:8", ["const:78611c:8", "const:4:8"]]
+ 0078611c ["CALL", null, ["callee:00c57eb0:8"]]
- 007860dc bytes 75461394
+ 0078611c bytes 65471394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ab3cb7dcea35c9813058890a06a9038"></a>

### [`00786b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/00786b68.md) → [`00786ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/00786ba8.md) FUN_00786ba8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0078610c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/0078610c.md) [`007877bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007877bc.md) · 呼出先 8件 [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md) [`00a46950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46950.md) [`00a469c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a469c0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 2件 [`0078614c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/0078614c.md) [`007877fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/007877fc.md) · 呼出先 8件 [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md) [`00a46b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46b48.md) [`00a46bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46bb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00786bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/00786b68.md#insn-00786bac) · [`00786bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/00786b68.md#insn-00786bfc) · [`00786c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/00786b68.md#insn-00786c04)
- 新版 `00786bec`（命令位置の公開資料なし） · `00786c3c`（命令位置の公開資料なし） · `00786c44`（命令位置の公開資料なし）

~~~diff
- 00786bac ["INT_ADD", "register:40f0:8", ["const:786bac:8", "const:4:8"]]
- 00786bac ["CALL", null, ["callee:008b79c8:8"]]
+ 00786bec ["INT_ADD", "register:40f0:8", ["const:786bec:8", "const:4:8"]]
+ 00786bec ["CALL", null, ["callee:008b79c8:8"]]
- 00786bac bytes 76c30494
+ 00786bec bytes 77c30494
- 00786bfc ["INT_ADD", "register:40f0:8", ["const:786bfc:8", "const:4:8"]]
- 00786bfc ["CALL", null, ["callee:00c53cd0:8"]]
+ 00786c3c ["INT_ADD", "register:40f0:8", ["const:786c3c:8", "const:4:8"]]
+ 00786c3c ["CALL", null, ["callee:00c53cd0:8"]]
- 00786bfc bytes 2d331394
+ 00786c3c bytes 25341394
- 00786c04 ["INT_ADD", "register:40f0:8", ["const:786c04:8", "const:4:8"]]
- 00786c04 ["CALL", null, ["callee:008b6ea4:8"]]
+ 00786c44 ["INT_ADD", "register:40f0:8", ["const:786c44:8", "const:4:8"]]
+ 00786c44 ["CALL", null, ["callee:008b6ea4:8"]]
- 00786c04 bytes 97c00494
+ 00786c44 bytes 98c00494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27b32a378bb9b200b7be3dbb23bd2d89"></a>

### [`00787440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787440.md) → [`00787480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/00787480.md) FUN_00787480

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0078610c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/0078610c.md) [`007877bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007877bc.md) · 呼出先 4件 [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md) [`00a466f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a466f8.md) [`00a469c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a469c0.md)
- 新版 呼出元 2件 [`0078614c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/0078614c.md) [`007877fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/007877fc.md) · 呼出先 4件 [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md) [`00a468f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a468f0.md) [`00a46bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46bb8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00787478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787440.md#insn-00787478) · [`00787480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787440.md#insn-00787480) · [`00787490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787440.md#insn-00787490)
- 新版 `007874b8`（命令位置の公開資料なし） · `007874c0`（命令位置の公開資料なし） · `007874d0`（命令位置の公開資料なし）

~~~diff
- 00787478 ["INT_ADD", "register:40f0:8", ["const:787478:8", "const:4:8"]]
- 00787478 ["CALL", null, ["callee:008b79c8:8"]]
+ 007874b8 ["INT_ADD", "register:40f0:8", ["const:7874b8:8", "const:4:8"]]
+ 007874b8 ["CALL", null, ["callee:008b79c8:8"]]
- 00787478 bytes 43c10494
+ 007874b8 bytes 44c10494
- 00787480 ["INT_ADD", "register:40f0:8", ["const:787480:8", "const:4:8"]]
- 00787480 ["CALL", null, ["callee:008b6ea4:8"]]
+ 007874c0 ["INT_ADD", "register:40f0:8", ["const:7874c0:8", "const:4:8"]]
+ 007874c0 ["CALL", null, ["callee:008b6ea4:8"]]
- 00787480 bytes 78be0494
+ 007874c0 bytes 79be0494
- 00787490 ["INT_ADD", "register:40f0:8", ["const:787490:8", "const:4:8"]]
- 00787490 ["CALL", null, ["callee:00a46bb8:8"]]
+ 007874d0 ["INT_ADD", "register:40f0:8", ["const:7874d0:8", "const:4:8"]]
+ 007874d0 ["CALL", null, ["callee:00a46bb8:8"]]
- 00787490 bytes 4cfd0a94
+ 007874d0 bytes bafd0a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47b4fe0c141dc563167f26f8365696de"></a>

### [`00787ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787ec4.md) → [`00787f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/00787f04.md) FUN_00787f04

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00787d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787d74.md) · 呼出先 3件 [`00467ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467ab0.md) [`00468b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468b9c.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md)
- 新版 呼出元 1件 [`00787db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/00787db4.md) · 呼出先 3件 [`00467af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467af0.md) [`00468bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00787f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787ec4.md#insn-00787f74) · [`00787f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787ec4.md#insn-00787f90) · [`00787fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787ec4.md#insn-00787fa4)
- 新版 `00787fb4`（命令位置の公開資料なし） · `00787fd0`（命令位置の公開資料なし） · `00787fe4`（命令位置の公開資料なし）

~~~diff
- 00787f74 ["INT_ADD", "register:40f0:8", ["const:787f74:8", "const:4:8"]]
- 00787f74 ["CALL", null, ["callee:00469c04:8"]]
+ 00787fb4 ["INT_ADD", "register:40f0:8", ["const:787fb4:8", "const:4:8"]]
+ 00787fb4 ["CALL", null, ["callee:00469c04:8"]]
- 00787f74 bytes 1487f397
+ 00787fb4 bytes 1487f397
- 00787f90 ["INT_ADD", "register:40f0:8", ["const:787f90:8", "const:4:8"]]
- 00787f90 ["CALL", null, ["callee:00467af0:8"]]
+ 00787fd0 ["INT_ADD", "register:40f0:8", ["const:787fd0:8", "const:4:8"]]
+ 00787fd0 ["CALL", null, ["callee:00467af0:8"]]
- 00787f90 bytes c87ef397
+ 00787fd0 bytes c87ef397
- 00787fa4 ["INT_ADD", "register:40f0:8", ["const:787fa4:8", "const:4:8"]]
- 00787fa4 ["CALL", null, ["callee:00468bdc:8"]]
+ 00787fe4 ["INT_ADD", "register:40f0:8", ["const:787fe4:8", "const:4:8"]]
+ 00787fe4 ["CALL", null, ["callee:00468bdc:8"]]
- 00787fa4 bytes fe82f397
+ 00787fe4 bytes fe82f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

