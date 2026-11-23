# v16.0.0 → v16.0.1 · 要調査の変更候補 (25)

[一覧の目次](README.md)

<a id="compare-aaaefd9277c23e52666afed25e4cc47d"></a>

### [`007a5200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a5/007a5200.md) → [`007a5240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a5/007a5240.md) FUN_007a5240

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007a1fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a1/007a1fc4.md) [`007a82f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a8/007a82f4.md) [`007a8e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a8/007a8e2c.md) · 呼出先 10件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00597a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a4c.md) [`005a4418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4418.md) [`007a06c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a0/007a06c8.md) [`007a3538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a3/007a3538.md)
- 新版 呼出元 3件 [`007a2004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a2/007a2004.md) [`007a8334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a8/007a8334.md) [`007a8e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a8/007a8e6c.md) · 呼出先 10件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) [`007a0708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0708.md) [`007a3578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a3/007a3578.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a5274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a5/007a5200.md#insn-007a5274) · [`007a52b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a5/007a5200.md#insn-007a52b0) · [`007a52c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a5/007a5200.md#insn-007a52c8)
- 新版 `007a52b4`（命令位置の公開資料なし） · `007a52f0`（命令位置の公開資料なし） · `007a5308`（命令位置の公開資料なし）

~~~diff
- 007a5274 ["INT_ADD", "register:40f0:8", ["const:7a5274:8", "const:4:8"]]
- 007a5274 ["CALL", null, ["callee:0043bb20:8"]]
+ 007a52b4 ["INT_ADD", "register:40f0:8", ["const:7a52b4:8", "const:4:8"]]
+ 007a52b4 ["CALL", null, ["callee:0043bb20:8"]]
- 007a5274 bytes 1b5af297
+ 007a52b4 bytes 1b5af297
- 007a52b0 ["INT_ADD", "register:40f0:8", ["const:7a52b0:8", "const:4:8"]]
- 007a52b0 ["CALL", null, ["callee:00c57e90:8"]]
+ 007a52f0 ["INT_ADD", "register:40f0:8", ["const:7a52f0:8", "const:4:8"]]
+ 007a52f0 ["CALL", null, ["callee:00c57e90:8"]]
- 007a52b0 bytes f8c91294
+ 007a52f0 bytes e8ca1294
- 007a52c8 ["INT_ADD", "register:40f0:8", ["const:7a52c8:8", "const:4:8"]]
- 007a52c8 ["CALL", null, ["callee:00c58000:8"]]
+ 007a5308 ["INT_ADD", "register:40f0:8", ["const:7a5308:8", "const:4:8"]]
+ 007a5308 ["CALL", null, ["callee:00c58000:8"]]
- 007a52c8 bytes 4eca1294
+ 007a5308 bytes 3ecb1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7004ed4b61f449d25d9bb0dd10799c5"></a>

### [`007a5f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a5/007a5f58.md) → [`007a5f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a5/007a5f98.md) FUN_007a5f98

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007a1fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a1/007a1fc4.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`007a2004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a2/007a2004.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a601c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a5/007a5f58.md#insn-007a601c) · [`007a6080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a5/007a5f58.md#insn-007a6080) · [`007a60a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a5/007a5f58.md#insn-007a60a8)
- 新版 `007a605c`（命令位置の公開資料なし） · `007a60c0`（命令位置の公開資料なし） · `007a60e8`（命令位置の公開資料なし）

~~~diff
- 007a601c ["INT_ADD", "register:40f0:8", ["const:7a601c:8", "const:4:8"]]
- 007a601c ["CALL", null, ["callee:00c57eb0:8"]]
+ 007a605c ["INT_ADD", "register:40f0:8", ["const:7a605c:8", "const:4:8"]]
+ 007a605c ["CALL", null, ["callee:00c57eb0:8"]]
- 007a601c bytes a5c61294
+ 007a605c bytes 95c71294
- 007a6080 ["INT_ADD", "register:40f0:8", ["const:7a6080:8", "const:4:8"]]
- 007a6080 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007a60c0 ["INT_ADD", "register:40f0:8", ["const:7a60c0:8", "const:4:8"]]
+ 007a60c0 ["CALL", null, ["callee:00c57eb0:8"]]
- 007a6080 bytes 8cc61294
+ 007a60c0 bytes 7cc71294
- 007a60a8 ["INT_ADD", "register:40f0:8", ["const:7a60a8:8", "const:4:8"]]
- 007a60a8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007a60e8 ["INT_ADD", "register:40f0:8", ["const:7a60e8:8", "const:4:8"]]
+ 007a60e8 ["CALL", null, ["callee:00c57eb0:8"]]
- 007a60a8 bytes 82c61294
+ 007a60e8 bytes 72c71294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3530986bfbf5f1892186efdff9a7fa92"></a>

### [`007a82f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a8/007a82f4.md) → [`007a8334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a8/007a8334.md) FUN_007a8334

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007a1fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a1/007a1fc4.md) · 呼出先 13件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00597a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a4c.md) [`005a4418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4418.md) [`007a06c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a0/007a06c8.md) [`007a3538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a3/007a3538.md)
- 新版 呼出元 1件 [`007a2004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a2/007a2004.md) · 呼出先 13件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) [`007a0708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0708.md) [`007a3578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a3/007a3578.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a837c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a8/007a82f4.md#insn-007a837c) · [`007a83e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a8/007a82f4.md#insn-007a83e8) · [`007a8408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a8/007a82f4.md#insn-007a8408)
- 新版 `007a83bc`（命令位置の公開資料なし） · `007a8428`（命令位置の公開資料なし） · `007a8448`（命令位置の公開資料なし）

~~~diff
- 007a837c ["INT_ADD", "register:40f0:8", ["const:7a837c:8", "const:4:8"]]
- 007a837c ["CALL", null, ["callee:007a3708:8"]]
+ 007a83bc ["INT_ADD", "register:40f0:8", ["const:7a83bc:8", "const:4:8"]]
+ 007a83bc ["CALL", null, ["callee:007a3708:8"]]
- 007a837c bytes d3ecff97
+ 007a83bc bytes d3ecff97
- 007a83e8 ["INT_ADD", "register:40f0:8", ["const:7a83e8:8", "const:4:8"]]
- 007a83e8 ["CALL", null, ["callee:007a5240:8"]]
+ 007a8428 ["INT_ADD", "register:40f0:8", ["const:7a8428:8", "const:4:8"]]
+ 007a8428 ["CALL", null, ["callee:007a5240:8"]]
- 007a83e8 bytes 86f3ff97
+ 007a8428 bytes 86f3ff97
- 007a8408 ["INT_ADD", "register:40f0:8", ["const:7a8408:8", "const:4:8"]]
- 007a8408 ["CALL", null, ["callee:007a5240:8"]]
+ 007a8448 ["INT_ADD", "register:40f0:8", ["const:7a8448:8", "const:4:8"]]
+ 007a8448 ["CALL", null, ["callee:007a5240:8"]]
- 007a8408 bytes 7ef3ff97
+ 007a8448 bytes 7ef3ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c46c7ab18f3277e9ccb3a1dbd418fd75"></a>

### [`007a8e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a8/007a8e2c.md) → [`007a8e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a8/007a8e6c.md) FUN_007a8e6c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007a1fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a1/007a1fc4.md) [`007a36c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a3/007a36c8.md) [`007a82f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a8/007a82f4.md) · 呼出先 11件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00597a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a4c.md) [`005a4418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4418.md) [`007a06c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a0/007a06c8.md) [`007a3538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a3/007a3538.md)
- 新版 呼出元 3件 [`007a2004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a2/007a2004.md) [`007a3708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a3/007a3708.md) [`007a8334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a8/007a8334.md) · 呼出先 11件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) [`007a0708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0708.md) [`007a3578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a3/007a3578.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a8e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a8/007a8e2c.md#insn-007a8e64) · [`007a8eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a8/007a8e2c.md#insn-007a8eac) · [`007a8ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a8/007a8e2c.md#insn-007a8ee8)
- 新版 `007a8ea4`（命令位置の公開資料なし） · `007a8eec`（命令位置の公開資料なし） · `007a8f28`（命令位置の公開資料なし）

~~~diff
- 007a8e64 ["INT_ADD", "register:40f0:8", ["const:7a8e64:8", "const:4:8"]]
- 007a8e64 ["CALL", null, ["callee:007a5240:8"]]
+ 007a8ea4 ["INT_ADD", "register:40f0:8", ["const:7a8ea4:8", "const:4:8"]]
+ 007a8ea4 ["CALL", null, ["callee:007a5240:8"]]
- 007a8e64 bytes e7f0ff97
+ 007a8ea4 bytes e7f0ff97
- 007a8eac ["INT_ADD", "register:40f0:8", ["const:7a8eac:8", "const:4:8"]]
- 007a8eac ["CALL", null, ["callee:0043bb20:8"]]
+ 007a8eec ["INT_ADD", "register:40f0:8", ["const:7a8eec:8", "const:4:8"]]
+ 007a8eec ["CALL", null, ["callee:0043bb20:8"]]
- 007a8eac bytes 0d4bf297
+ 007a8eec bytes 0d4bf297
- 007a8ee8 ["INT_ADD", "register:40f0:8", ["const:7a8ee8:8", "const:4:8"]]
- 007a8ee8 ["CALL", null, ["callee:00c57e90:8"]]
+ 007a8f28 ["INT_ADD", "register:40f0:8", ["const:7a8f28:8", "const:4:8"]]
+ 007a8f28 ["CALL", null, ["callee:00c57e90:8"]]
- 007a8ee8 bytes eaba1294
+ 007a8f28 bytes dabb1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-862393f5181fc014ed46ec396471fad4"></a>

### [`007a965c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a9/007a965c.md) → [`007a969c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a9/007a969c.md) FUN_007a969c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007a419c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a4/007a419c.md) · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00597a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a4c.md) [`005a4418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4418.md) [`007a06c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a0/007a06c8.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 1件 [`007a41dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a4/007a41dc.md) · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) [`007a0708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0708.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a9728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a9/007a965c.md#insn-007a9728) · [`007a9764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a9/007a965c.md#insn-007a9764) · [`007a977c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a9/007a965c.md#insn-007a977c)
- 新版 `007a9768`（命令位置の公開資料なし） · `007a97a4`（命令位置の公開資料なし） · `007a97bc`（命令位置の公開資料なし）

~~~diff
- 007a9728 ["INT_ADD", "register:40f0:8", ["const:7a9728:8", "const:4:8"]]
- 007a9728 ["CALL", null, ["callee:0043bb20:8"]]
+ 007a9768 ["INT_ADD", "register:40f0:8", ["const:7a9768:8", "const:4:8"]]
+ 007a9768 ["CALL", null, ["callee:0043bb20:8"]]
- 007a9728 bytes ee48f297
+ 007a9768 bytes ee48f297
- 007a9764 ["INT_ADD", "register:40f0:8", ["const:7a9764:8", "const:4:8"]]
- 007a9764 ["CALL", null, ["callee:00c57e90:8"]]
+ 007a97a4 ["INT_ADD", "register:40f0:8", ["const:7a97a4:8", "const:4:8"]]
+ 007a97a4 ["CALL", null, ["callee:00c57e90:8"]]
- 007a9764 bytes cbb81294
+ 007a97a4 bytes bbb91294
- 007a977c ["INT_ADD", "register:40f0:8", ["const:7a977c:8", "const:4:8"]]
- 007a977c ["CALL", null, ["callee:00c58000:8"]]
+ 007a97bc ["INT_ADD", "register:40f0:8", ["const:7a97bc:8", "const:4:8"]]
+ 007a97bc ["CALL", null, ["callee:00c58000:8"]]
- 007a977c bytes 21b91294
+ 007a97bc bytes 11ba1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c385718203b51a1936dd615119c1244"></a>

### [`007aa738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aa738.md) → [`007aa778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa778.md) FUN_007aa778

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007abbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007abbe4.md) · 呼出先 3件 [`00aa3264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3264.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`007abc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007abc24.md) · 呼出先 3件 [`00aa3460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa3/00aa3460.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007aa764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aa738.md#insn-007aa764) · [`007aa774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aa738.md#insn-007aa774) · [`007aa7c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aa738.md#insn-007aa7c4)
- 新版 `007aa7a4`（命令位置の公開資料なし） · `007aa7b4`（命令位置の公開資料なし） · `007aa804`（命令位置の公開資料なし）

~~~diff
- 007aa764 ["INT_ADD", "register:40f0:8", ["const:7aa764:8", "const:4:8"]]
- 007aa764 ["CALL", null, ["callee:00aa3460:8"]]
+ 007aa7a4 ["INT_ADD", "register:40f0:8", ["const:7aa7a4:8", "const:4:8"]]
+ 007aa7a4 ["CALL", null, ["callee:00aa3460:8"]]
- 007aa764 bytes c0e20b94
+ 007aa7a4 bytes 2fe30b94
- 007aa774 ["INT_ADD", "register:40f0:8", ["const:7aa774:8", "const:4:8"]]
- 007aa774 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007aa7b4 ["INT_ADD", "register:40f0:8", ["const:7aa7b4:8", "const:4:8"]]
+ 007aa7b4 ["CALL", null, ["callee:00c57eb0:8"]]
- 007aa774 bytes cfb41294
+ 007aa7b4 bytes bfb51294
- 007aa7c4 ["INT_ADD", "register:40f0:8", ["const:7aa7c4:8", "const:4:8"]]
- 007aa7c4 ["CALL", null, ["callee:00c57ee0:8"]]
+ 007aa804 ["INT_ADD", "register:40f0:8", ["const:7aa804:8", "const:4:8"]]
+ 007aa804 ["CALL", null, ["callee:00c57ee0:8"]]
- 007aa7c4 bytes c7b41294
+ 007aa804 bytes b7b51294
~~~


<a id="compare-7114ee4bb5b1439df5d96170499cb1ed"></a>

### [`007ab2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007ab2f8.md) → [`007ab338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab338.md) FUN_007ab338

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) · 呼出先 2件 [`007b08dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b08dc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) · 呼出先 2件 [`007b091c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b091c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007ab30c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007ab2f8.md#insn-007ab30c) · [`007ab314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007ab2f8.md#insn-007ab314)
- 新版 `007ab34c`（命令位置の公開資料なし） · `007ab354`（命令位置の公開資料なし）

~~~diff
- 007ab30c ["INT_ADD", "register:40f0:8", ["const:7ab30c:8", "const:4:8"]]
- 007ab30c ["CALL", null, ["callee:00c57e90:8"]]
+ 007ab34c ["INT_ADD", "register:40f0:8", ["const:7ab34c:8", "const:4:8"]]
+ 007ab34c ["CALL", null, ["callee:00c57e90:8"]]
- 007ab30c bytes e1b11294
+ 007ab34c bytes d1b21294
- 007ab314 ["INT_ADD", "register:40f0:8", ["const:7ab314:8", "const:4:8"]]
- 007ab314 ["CALL", null, ["callee:007b091c:8"]]
+ 007ab354 ["INT_ADD", "register:40f0:8", ["const:7ab354:8", "const:4:8"]]
+ 007ab354 ["CALL", null, ["callee:007b091c:8"]]
- 007ab314 bytes 72150094
+ 007ab354 bytes 72150094
~~~


<a id="compare-d98fb458fc62967f190d99c39f00827f"></a>

### [`007ab33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007ab33c.md) → [`007ab37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab37c.md) FUN_007ab37c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00848534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848534.md) [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00848574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848574.md) [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007ab360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007ab33c.md#insn-007ab360)
- 新版 `007ab3a0`（命令位置の公開資料なし）

~~~diff
- 007ab360 ["COPY", "register:0:8", ["register:4040:8"]]
- 007ab360 ["INT_ADD", "register:40f0:8", ["const:7ab360:8", "const:4:8"]]
- 007ab360 ["CALLIND", null, ["register:0:8"]]
+ 007ab3a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007ab3a0 ["INT_ADD", "register:40f0:8", ["const:7ab3a0:8", "const:4:8"]]
+ 007ab3a0 ["CALLIND", null, ["register:0:8"]]
- 007ab360 bytes 00013fd6
+ 007ab3a0 bytes 00013fd6
~~~


<a id="compare-5f33938adb31fc279b38ce10f30d009d"></a>

### [`007ae734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae734.md) → [`007ae774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae774.md) FUN_007ae774

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007ab3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007ab3c4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`007ab404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab404.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007ae770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae734.md#insn-007ae770)
- 新版 `007ae7b0`（命令位置の公開資料なし）

~~~diff
- 007ae770 ["COPY", "register:0:8", ["register:4040:8"]]
- 007ae770 ["INT_ADD", "register:40f0:8", ["const:7ae770:8", "const:4:8"]]
- 007ae770 ["CALLIND", null, ["register:0:8"]]
+ 007ae7b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007ae7b0 ["INT_ADD", "register:40f0:8", ["const:7ae7b0:8", "const:4:8"]]
+ 007ae7b0 ["CALLIND", null, ["register:0:8"]]
- 007ae770 bytes 00013fd6
+ 007ae7b0 bytes 00013fd6
~~~


<a id="compare-737ff426ebded2cdebb75027a8fdbac6"></a>

### [`007aeedc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aeedc.md) → [`007aef1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aef1c.md) FUN_007aef1c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007ad944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad944.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`007ad984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad984.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007aeefc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aeedc.md#insn-007aeefc)
- 新版 `007aef3c`（命令位置の公開資料なし）

~~~diff
- 007aeefc ["INT_ADD", "register:40f0:8", ["const:7aeefc:8", "const:4:8"]]
- 007aeefc ["CALL", null, ["callee:00c57eb0:8"]]
+ 007aef3c ["INT_ADD", "register:40f0:8", ["const:7aef3c:8", "const:4:8"]]
+ 007aef3c ["CALL", null, ["callee:00c57eb0:8"]]
- 007aeefc bytes eda21294
+ 007aef3c bytes dda31294
~~~


<a id="compare-d7e44e10961d2d5e60f4f794a7ad9cc4"></a>

### [`007af43c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af43c.md) → [`007af47c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af47c.md) FUN_007af47c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007ab714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007ab714.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`007ab754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab754.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007af478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af43c.md#insn-007af478)
- 新版 `007af4b8`（命令位置の公開資料なし）

~~~diff
- 007af478 ["COPY", "register:0:8", ["register:4040:8"]]
- 007af478 ["INT_ADD", "register:40f0:8", ["const:7af478:8", "const:4:8"]]
- 007af478 ["CALLIND", null, ["register:0:8"]]
+ 007af4b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007af4b8 ["INT_ADD", "register:40f0:8", ["const:7af4b8:8", "const:4:8"]]
+ 007af4b8 ["CALLIND", null, ["register:0:8"]]
- 007af478 bytes 00013fd6
+ 007af4b8 bytes 00013fd6
~~~


<a id="compare-014b5a9ca4c16a9e41c2fd779f09f05b"></a>

### [`007af48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af48c.md) → [`007af4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af4cc.md) FUN_007af4cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007af4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af48c.md#insn-007af4c4) · [`007af4e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af48c.md#insn-007af4e4) · [`007af4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af48c.md#insn-007af4f4)
- 新版 `007af504`（命令位置の公開資料なし） · `007af524`（命令位置の公開資料なし） · `007af534`（命令位置の公開資料なし）

~~~diff
- 007af4c4 ["INT_ADD", "register:40f0:8", ["const:7af4c4:8", "const:4:8"]]
- 007af4c4 ["CALL", null, ["callee:00c53cd0:8"]]
+ 007af504 ["INT_ADD", "register:40f0:8", ["const:7af504:8", "const:4:8"]]
+ 007af504 ["CALL", null, ["callee:00c53cd0:8"]]
- 007af4c4 bytes fb901294
+ 007af504 bytes f3911294
- 007af4e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 007af4e4 ["INT_ADD", "register:40f0:8", ["const:7af4e4:8", "const:4:8"]]
- 007af4e4 ["CALLIND", null, ["register:0:8"]]
+ 007af524 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007af524 ["INT_ADD", "register:40f0:8", ["const:7af524:8", "const:4:8"]]
+ 007af524 ["CALLIND", null, ["register:0:8"]]
- 007af4e4 bytes 00013fd6
+ 007af524 bytes 00013fd6
- 007af4f4 ["INT_ADD", "register:40f0:8", ["const:7af4f4:8", "const:4:8"]]
- 007af4f4 ["CALL", null, ["callee:00c53d00:8"]]
+ 007af534 ["INT_ADD", "register:40f0:8", ["const:7af534:8", "const:4:8"]]
+ 007af534 ["CALL", null, ["callee:00c53d00:8"]]
- 007af4f4 bytes fb901294
+ 007af534 bytes f3911294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3645ff004af3ceb28b2f7566697a25e1"></a>

### [`007af59c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af59c.md) → [`007af5dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af5dc.md) FUN_007af5dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007af5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af59c.md#insn-007af5b8) · [`007af5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af59c.md#insn-007af5d8)
- 新版 `007af5f8`（命令位置の公開資料なし） · `007af618`（命令位置の公開資料なし）

~~~diff
- 007af5b8 ["INT_ADD", "register:40f0:8", ["const:7af5b8:8", "const:4:8"]]
- 007af5b8 ["CALL", null, ["callee:00c53d00:8"]]
+ 007af5f8 ["INT_ADD", "register:40f0:8", ["const:7af5f8:8", "const:4:8"]]
+ 007af5f8 ["CALL", null, ["callee:00c53d00:8"]]
- 007af5b8 bytes ca901294
+ 007af5f8 bytes c2911294
- 007af5d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 007af5d8 ["INT_ADD", "register:40f0:8", ["const:7af5d8:8", "const:4:8"]]
- 007af5d8 ["CALLIND", null, ["register:0:8"]]
+ 007af618 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007af618 ["INT_ADD", "register:40f0:8", ["const:7af618:8", "const:4:8"]]
+ 007af618 ["CALLIND", null, ["register:0:8"]]
- 007af5d8 bytes 00013fd6
+ 007af618 bytes 00013fd6
~~~


<a id="compare-9d08cbfa0a00a468e830bd3f6b89b65a"></a>

### [`007af7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af7c0.md) → [`007af800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af800.md) FUN_007af800

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007ab714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007ab714.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`007ab754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab754.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007af7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af7c0.md#insn-007af7fc)
- 新版 `007af83c`（命令位置の公開資料なし）

~~~diff
- 007af7fc ["COPY", "register:0:8", ["register:4040:8"]]
- 007af7fc ["INT_ADD", "register:40f0:8", ["const:7af7fc:8", "const:4:8"]]
- 007af7fc ["CALLIND", null, ["register:0:8"]]
+ 007af83c ["COPY", "register:0:8", ["register:4040:8"]]
+ 007af83c ["INT_ADD", "register:40f0:8", ["const:7af83c:8", "const:4:8"]]
+ 007af83c ["CALLIND", null, ["register:0:8"]]
- 007af7fc bytes 00013fd6
+ 007af83c bytes 00013fd6
~~~


<a id="compare-f5914947e987bbce69fa7cf8ab884649"></a>

### [`007af810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af810.md) → [`007af850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af850.md) FUN_007af850

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007af82c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af810.md#insn-007af82c)
- 新版 `007af86c`（命令位置の公開資料なし）

~~~diff
- 007af82c ["INT_ADD", "register:40f0:8", ["const:7af82c:8", "const:4:8"]]
- 007af82c ["CALL", null, ["callee:00459d74:8"]]
+ 007af86c ["INT_ADD", "register:40f0:8", ["const:7af86c:8", "const:4:8"]]
+ 007af86c ["CALL", null, ["callee:00459d74:8"]]
- 007af82c bytes 42a9f297
+ 007af86c bytes 42a9f297
~~~


<a id="compare-eb515901059387c8a65a782d9c35b8c9"></a>

### [`007afba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afba4.md) → [`007afbe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afbe4.md) FUN_007afbe4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007ad2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad2e4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`007ad324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad324.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007afbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afba4.md#insn-007afbe0)
- 新版 `007afc20`（命令位置の公開資料なし）

~~~diff
- 007afbe0 ["COPY", "register:0:8", ["register:4040:8"]]
- 007afbe0 ["INT_ADD", "register:40f0:8", ["const:7afbe0:8", "const:4:8"]]
- 007afbe0 ["CALLIND", null, ["register:0:8"]]
+ 007afc20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007afc20 ["INT_ADD", "register:40f0:8", ["const:7afc20:8", "const:4:8"]]
+ 007afc20 ["CALLIND", null, ["register:0:8"]]
- 007afbe0 bytes 00013fd6
+ 007afc20 bytes 00013fd6
~~~


<a id="compare-16cf812d1fc0dd89c091f2fb367c156c"></a>

### [`007afbf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afbf4.md) → [`007afc34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afc34.md) FUN_007afc34

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007afc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afbf4.md#insn-007afc10)
- 新版 `007afc50`（命令位置の公開資料なし）

~~~diff
- 007afc10 ["INT_ADD", "register:40f0:8", ["const:7afc10:8", "const:4:8"]]
- 007afc10 ["CALL", null, ["callee:00459d74:8"]]
+ 007afc50 ["INT_ADD", "register:40f0:8", ["const:7afc50:8", "const:4:8"]]
+ 007afc50 ["CALL", null, ["callee:00459d74:8"]]
- 007afc10 bytes 49a8f297
+ 007afc50 bytes 49a8f297
~~~


<a id="compare-a3ff08f8b19df6eb57cf3754f38851c1"></a>

### [`007afe10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afe10.md) → [`007afe50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afe50.md) FUN_007afe50

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007ad2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad2e4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`007ad324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad324.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007afe4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afe10.md#insn-007afe4c)
- 新版 `007afe8c`（命令位置の公開資料なし）

~~~diff
- 007afe4c ["COPY", "register:0:8", ["register:4040:8"]]
- 007afe4c ["INT_ADD", "register:40f0:8", ["const:7afe4c:8", "const:4:8"]]
- 007afe4c ["CALLIND", null, ["register:0:8"]]
+ 007afe8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 007afe8c ["INT_ADD", "register:40f0:8", ["const:7afe8c:8", "const:4:8"]]
+ 007afe8c ["CALLIND", null, ["register:0:8"]]
- 007afe4c bytes 00013fd6
+ 007afe8c bytes 00013fd6
~~~


<a id="compare-aed7279e4fc4021382ac11245917cb00"></a>

### [`007afe60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afe60.md) → [`007afea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afea0.md) FUN_007afea0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007afe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afe60.md#insn-007afe98) · [`007afecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afe60.md#insn-007afecc) · [`007afed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afe60.md#insn-007afed0)
- 新版 `007afed8`（命令位置の公開資料なし） · `007aff0c`（命令位置の公開資料なし） · `007aff10`（命令位置の公開資料なし）

~~~diff
- 007afe98 ["COPY", "register:0:8", ["register:4040:8"]]
- 007afe98 ["INT_ADD", "register:40f0:8", ["const:7afe98:8", "const:4:8"]]
- 007afe98 ["CALLIND", null, ["register:0:8"]]
+ 007afed8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007afed8 ["INT_ADD", "register:40f0:8", ["const:7afed8:8", "const:4:8"]]
+ 007afed8 ["CALLIND", null, ["register:0:8"]]
- 007afe98 bytes 00013fd6
+ 007afed8 bytes 00013fd6
- 007afecc ["INT_ADD", "register:40f0:8", ["const:7afecc:8", "const:4:8"]]
- 007afecc ["CALL", null, ["callee:00459d74:8"]]
+ 007aff0c ["INT_ADD", "register:40f0:8", ["const:7aff0c:8", "const:4:8"]]
+ 007aff0c ["CALL", null, ["callee:00459d74:8"]]
- 007afecc bytes 9aa7f297
+ 007aff0c bytes 9aa7f297
- 007afed0 ["INT_ADD", "register:40f0:8", ["const:7afed0:8", "const:4:8"]]
- 007afed0 ["CALL", null, ["callee:00c57ee0:8"]]
+ 007aff10 ["INT_ADD", "register:40f0:8", ["const:7aff10:8", "const:4:8"]]
+ 007aff10 ["CALL", null, ["callee:00c57ee0:8"]]
- 007afed0 bytes 049f1294
+ 007aff10 bytes f49f1294
~~~


<a id="compare-74935399641dd8aea50b89378cf71878"></a>

### [`007b0248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b0248.md) → [`007b0288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0288.md) FUN_007b0288

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007adedc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007adedc.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`007adf1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007adf1c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007b0284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b0248.md#insn-007b0284)
- 新版 `007b02c4`（命令位置の公開資料なし）

~~~diff
- 007b0284 ["COPY", "register:0:8", ["register:4040:8"]]
- 007b0284 ["INT_ADD", "register:40f0:8", ["const:7b0284:8", "const:4:8"]]
- 007b0284 ["CALLIND", null, ["register:0:8"]]
+ 007b02c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007b02c4 ["INT_ADD", "register:40f0:8", ["const:7b02c4:8", "const:4:8"]]
+ 007b02c4 ["CALLIND", null, ["register:0:8"]]
- 007b0284 bytes 00013fd6
+ 007b02c4 bytes 00013fd6
~~~


<a id="compare-5e110d49fd74e4edb8b89a22189782f6"></a>

### [`007b0298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b0298.md) → [`007b02d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b02d8.md) FUN_007b02d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007b02b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b0298.md#insn-007b02b4)
- 新版 `007b02f4`（命令位置の公開資料なし）

~~~diff
- 007b02b4 ["INT_ADD", "register:40f0:8", ["const:7b02b4:8", "const:4:8"]]
- 007b02b4 ["CALL", null, ["callee:00459d74:8"]]
+ 007b02f4 ["INT_ADD", "register:40f0:8", ["const:7b02f4:8", "const:4:8"]]
+ 007b02f4 ["CALL", null, ["callee:00459d74:8"]]
- 007b02b4 bytes a0a6f297
+ 007b02f4 bytes a0a6f297
~~~


<a id="compare-1a92a57cc72dea8284945dc39086fb43"></a>

### [`007b04b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b04b4.md) → [`007b04f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b04f4.md) FUN_007b04f4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007adedc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007adedc.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`007adf1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007adf1c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007b04f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b04b4.md#insn-007b04f0)
- 新版 `007b0530`（命令位置の公開資料なし）

~~~diff
- 007b04f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 007b04f0 ["INT_ADD", "register:40f0:8", ["const:7b04f0:8", "const:4:8"]]
- 007b04f0 ["CALLIND", null, ["register:0:8"]]
+ 007b0530 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007b0530 ["INT_ADD", "register:40f0:8", ["const:7b0530:8", "const:4:8"]]
+ 007b0530 ["CALLIND", null, ["register:0:8"]]
- 007b04f0 bytes 00013fd6
+ 007b0530 bytes 00013fd6
~~~


<a id="compare-baa5a827444dab45724edd04377c496b"></a>

### [`007b0504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b0504.md) → [`007b0544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0544.md) FUN_007b0544

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007b0520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b0504.md#insn-007b0520)
- 新版 `007b0560`（命令位置の公開資料なし）

~~~diff
- 007b0520 ["INT_ADD", "register:40f0:8", ["const:7b0520:8", "const:4:8"]]
- 007b0520 ["CALL", null, ["callee:00459d74:8"]]
+ 007b0560 ["INT_ADD", "register:40f0:8", ["const:7b0560:8", "const:4:8"]]
+ 007b0560 ["CALL", null, ["callee:00459d74:8"]]
- 007b0520 bytes 05a6f297
+ 007b0560 bytes 05a6f297
~~~


<a id="compare-411615cae8ee2daa5b064e4da6ced976"></a>

### [`007b08e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b08e8.md) → [`007b0928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0928.md) FUN_007b0928

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007ab388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007ab388.md) · 呼出先 1件 [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md)
- 新版 呼出元 1件 [`007ab3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab3c8.md) · 呼出先 1件 [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007b0908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b08e8.md#insn-007b0908) · [`007b0914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b08e8.md#insn-007b0914)
- 新版 `007b0948`（命令位置の公開資料なし） · `007b0954`（命令位置の公開資料なし）

~~~diff
- 007b0908 ["INT_ADD", "register:40f0:8", ["const:7b0908:8", "const:4:8"]]
- 007b0908 ["CALL", null, ["callee:00480d48:8"]]
+ 007b0948 ["INT_ADD", "register:40f0:8", ["const:7b0948:8", "const:4:8"]]
+ 007b0948 ["CALL", null, ["callee:00480d48:8"]]
- 007b0908 bytes 0041f397
+ 007b0948 bytes 0041f397
- 007b0914 ["INT_ADD", "register:40f0:8", ["const:7b0914:8", "const:4:8"]]
- 007b0914 ["CALL", null, ["callee:00480d48:8"]]
+ 007b0954 ["INT_ADD", "register:40f0:8", ["const:7b0954:8", "const:4:8"]]
+ 007b0954 ["CALL", null, ["callee:00480d48:8"]]
- 007b0914 bytes fd40f397
+ 007b0954 bytes fd40f397
~~~


<a id="compare-d147df3326282960d34280f89a66763f"></a>

### [`007b092c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b092c.md) → [`007b096c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b096c.md) FUN_007b096c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007ab390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007ab390.md) · 呼出先 1件 [`004802b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md)
- 新版 呼出元 1件 [`007ab3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab3d0.md) · 呼出先 1件 [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007b0944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b092c.md#insn-007b0944) · [`007b0954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b092c.md#insn-007b0954) · [`007b0964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b092c.md#insn-007b0964)
- 新版 `007b0984`（命令位置の公開資料なし） · `007b0994`（命令位置の公開資料なし） · `007b09a4`（命令位置の公開資料なし）

~~~diff
- 007b0944 ["INT_ADD", "register:40f0:8", ["const:7b0944:8", "const:4:8"]]
- 007b0944 ["CALL", null, ["callee:004802f8:8"]]
+ 007b0984 ["INT_ADD", "register:40f0:8", ["const:7b0984:8", "const:4:8"]]
+ 007b0984 ["CALL", null, ["callee:004802f8:8"]]
- 007b0944 bytes 5d3ef397
+ 007b0984 bytes 5d3ef397
- 007b0954 ["INT_ADD", "register:40f0:8", ["const:7b0954:8", "const:4:8"]]
- 007b0954 ["CALL", null, ["callee:004802f8:8"]]
+ 007b0994 ["INT_ADD", "register:40f0:8", ["const:7b0994:8", "const:4:8"]]
+ 007b0994 ["CALL", null, ["callee:004802f8:8"]]
- 007b0954 bytes 593ef397
+ 007b0994 bytes 593ef397
- 007b0964 ["INT_ADD", "register:40f0:8", ["const:7b0964:8", "const:4:8"]]
- 007b0964 ["CALL", null, ["callee:004802f8:8"]]
+ 007b09a4 ["INT_ADD", "register:40f0:8", ["const:7b09a4:8", "const:4:8"]]
+ 007b09a4 ["CALL", null, ["callee:004802f8:8"]]
- 007b0964 bytes 553ef397
+ 007b09a4 bytes 553ef397
~~~


<a id="compare-3adad531a702853e1b4543f79f469a91"></a>

### [`007bb9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bb9cc.md) → [`007bba0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bba0c.md) FUN_007bba0c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007bba34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bb9cc.md#insn-007bba34) · [`007bba8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bb9cc.md#insn-007bba8c)
- 新版 `007bba74`（命令位置の公開資料なし） · `007bbacc`（命令位置の公開資料なし）

~~~diff
- 007bba34 ["INT_ADD", "register:40f0:8", ["const:7bba34:8", "const:4:8"]]
- 007bba34 ["CALL", null, ["callee:00c57e90:8"]]
+ 007bba74 ["INT_ADD", "register:40f0:8", ["const:7bba74:8", "const:4:8"]]
+ 007bba74 ["CALL", null, ["callee:00c57e90:8"]]
- 007bba34 bytes 17701294
+ 007bba74 bytes 07711294
- 007bba8c ["INT_ADD", "register:40f0:8", ["const:7bba8c:8", "const:4:8"]]
- 007bba8c ["CALL", null, ["callee:0043bba4:8"]]
+ 007bbacc ["INT_ADD", "register:40f0:8", ["const:7bbacc:8", "const:4:8"]]
+ 007bbacc ["CALL", null, ["callee:0043bba4:8"]]
- 007bba8c bytes 3600f297
+ 007bbacc bytes 3600f297
~~~


<a id="compare-3d8acff69993cfe795318b76ff2cbd6e"></a>

### [`007bbab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbab4.md) → [`007bbaf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbaf4.md) FUN_007bbaf4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007b09d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b09d8.md) [`00a52c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a52/00a52c38.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`007f0c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0c58.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`007b0a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0a18.md) [`00a52e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a52/00a52e30.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`007f0c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0c98.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007bbb14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbab4.md#insn-007bbb14) · [`007bbb24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbab4.md#insn-007bbb24) · [`007bbb58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbab4.md#insn-007bbb58)
- 新版 `007bbb54`（命令位置の公開資料なし） · `007bbb64`（命令位置の公開資料なし） · `007bbb98`（命令位置の公開資料なし）

~~~diff
- 007bbb14 ["INT_ADD", "register:40f0:8", ["const:7bbb14:8", "const:4:8"]]
- 007bbb14 ["CALL", null, ["callee:0043bb20:8"]]
+ 007bbb54 ["INT_ADD", "register:40f0:8", ["const:7bbb54:8", "const:4:8"]]
+ 007bbb54 ["CALL", null, ["callee:0043bb20:8"]]
- 007bbb14 bytes f3fff197
+ 007bbb54 bytes f3fff197
- 007bbb24 ["INT_ADD", "register:40f0:8", ["const:7bbb24:8", "const:4:8"]]
- 007bbb24 ["CALL", null, ["callee:0043bb20:8"]]
+ 007bbb64 ["INT_ADD", "register:40f0:8", ["const:7bbb64:8", "const:4:8"]]
+ 007bbb64 ["CALL", null, ["callee:0043bb20:8"]]
- 007bbb24 bytes effff197
+ 007bbb64 bytes effff197
- 007bbb58 ["INT_ADD", "register:40f0:8", ["const:7bbb58:8", "const:4:8"]]
- 007bbb58 ["CALL", null, ["callee:007f0c98:8"]]
+ 007bbb98 ["INT_ADD", "register:40f0:8", ["const:7bbb98:8", "const:4:8"]]
+ 007bbb98 ["CALL", null, ["callee:007f0c98:8"]]
- 007bbb58 bytes 40d40094
+ 007bbb98 bytes 40d40094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aba966fe5b9754b114b8b6b3b5325928"></a>

### [`007bd698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd698.md) → [`007bd6d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd6d8.md) FUN_007bd6d8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007bd700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd698.md#insn-007bd700) · [`007bd738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd698.md#insn-007bd738)
- 新版 `007bd740`（命令位置の公開資料なし） · `007bd778`（命令位置の公開資料なし）

~~~diff
- 007bd700 ["INT_ADD", "register:40f0:8", ["const:7bd700:8", "const:4:8"]]
- 007bd700 ["CALL", null, ["callee:00c57e90:8"]]
+ 007bd740 ["INT_ADD", "register:40f0:8", ["const:7bd740:8", "const:4:8"]]
+ 007bd740 ["CALL", null, ["callee:00c57e90:8"]]
- 007bd700 bytes e4681294
+ 007bd740 bytes d4691294
- 007bd738 ["INT_ADD", "register:40f0:8", ["const:7bd738:8", "const:4:8"]]
- 007bd738 ["CALL", null, ["callee:0043bba4:8"]]
+ 007bd778 ["INT_ADD", "register:40f0:8", ["const:7bd778:8", "const:4:8"]]
+ 007bd778 ["CALL", null, ["callee:0043bba4:8"]]
- 007bd738 bytes 0bf9f197
+ 007bd778 bytes 0bf9f197
~~~


<a id="compare-d12f3c060c50ff6bbc8b81b583f7035b"></a>

### [`007bd760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd760.md) → [`007bd7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd7a0.md) FUN_007bd7a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007bd794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd760.md#insn-007bd794)
- 新版 `007bd7d4`（命令位置の公開資料なし）

~~~diff
- 007bd794 ["INT_ADD", "register:40f0:8", ["const:7bd794:8", "const:4:8"]]
- 007bd794 ["CALL", null, ["callee:0046e8a4:8"]]
+ 007bd7d4 ["INT_ADD", "register:40f0:8", ["const:7bd7d4:8", "const:4:8"]]
+ 007bd7d4 ["CALL", null, ["callee:0046e8a4:8"]]
- 007bd794 bytes 34c4f297
+ 007bd7d4 bytes 34c4f297
~~~


<a id="compare-5bba08f07e03a3f1be861d37b97a35ef"></a>

### [`007bd7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd7c8.md) → [`007bd808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd808.md) FUN_007bd808

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007bd800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd7c8.md#insn-007bd800) · [`007bd814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd7c8.md#insn-007bd814) · [`007bd81c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd7c8.md#insn-007bd81c)
- 新版 `007bd840`（命令位置の公開資料なし） · `007bd854`（命令位置の公開資料なし） · `007bd85c`（命令位置の公開資料なし）

~~~diff
- 007bd800 ["INT_ADD", "register:40f0:8", ["const:7bd800:8", "const:4:8"]]
- 007bd800 ["CALL", null, ["callee:00c53d00:8"]]
+ 007bd840 ["INT_ADD", "register:40f0:8", ["const:7bd840:8", "const:4:8"]]
+ 007bd840 ["CALL", null, ["callee:00c53d00:8"]]
- 007bd800 bytes 38581294
+ 007bd840 bytes 30591294
- 007bd814 ["COPY", "register:0:8", ["register:4040:8"]]
- 007bd814 ["INT_ADD", "register:40f0:8", ["const:7bd814:8", "const:4:8"]]
- 007bd814 ["CALLIND", null, ["register:0:8"]]
+ 007bd854 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007bd854 ["INT_ADD", "register:40f0:8", ["const:7bd854:8", "const:4:8"]]
+ 007bd854 ["CALLIND", null, ["register:0:8"]]
- 007bd814 bytes 00013fd6
+ 007bd854 bytes 00013fd6
- 007bd81c ["INT_ADD", "register:40f0:8", ["const:7bd81c:8", "const:4:8"]]
- 007bd81c ["CALL", null, ["callee:00c57e80:8"]]
+ 007bd85c ["INT_ADD", "register:40f0:8", ["const:7bd85c:8", "const:4:8"]]
+ 007bd85c ["CALL", null, ["callee:00c57e80:8"]]
- 007bd81c bytes 99681294
+ 007bd85c bytes 89691294
~~~


<a id="compare-2774c911b6e8ccdfc996f5f47c4e809f"></a>

### [`007bd834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd834.md) → [`007bd874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd874.md) FUN_007bd874

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007bd86c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd834.md#insn-007bd86c) · [`007bd880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd834.md#insn-007bd880) · [`007bd888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd834.md#insn-007bd888)
- 新版 `007bd8ac`（命令位置の公開資料なし） · `007bd8c0`（命令位置の公開資料なし） · `007bd8c8`（命令位置の公開資料なし）

~~~diff
- 007bd86c ["INT_ADD", "register:40f0:8", ["const:7bd86c:8", "const:4:8"]]
- 007bd86c ["CALL", null, ["callee:00c53d00:8"]]
+ 007bd8ac ["INT_ADD", "register:40f0:8", ["const:7bd8ac:8", "const:4:8"]]
+ 007bd8ac ["CALL", null, ["callee:00c53d00:8"]]
- 007bd86c bytes 1d581294
+ 007bd8ac bytes 15591294
- 007bd880 ["COPY", "register:0:8", ["register:4040:8"]]
- 007bd880 ["INT_ADD", "register:40f0:8", ["const:7bd880:8", "const:4:8"]]
- 007bd880 ["CALLIND", null, ["register:0:8"]]
+ 007bd8c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007bd8c0 ["INT_ADD", "register:40f0:8", ["const:7bd8c0:8", "const:4:8"]]
+ 007bd8c0 ["CALLIND", null, ["register:0:8"]]
- 007bd880 bytes 00013fd6
+ 007bd8c0 bytes 00013fd6
- 007bd888 ["INT_ADD", "register:40f0:8", ["const:7bd888:8", "const:4:8"]]
- 007bd888 ["CALL", null, ["callee:00c57e80:8"]]
+ 007bd8c8 ["INT_ADD", "register:40f0:8", ["const:7bd8c8:8", "const:4:8"]]
+ 007bd8c8 ["CALL", null, ["callee:00c57e80:8"]]
- 007bd888 bytes 7e681294
+ 007bd8c8 bytes 6e691294
~~~


<a id="compare-39e7aa2b10dc6178663aac5e56ad832e"></a>

### [`007bd8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd8a0.md) → [`007bd8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd8e0.md) FUN_007bd8e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007bd8bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd8a0.md#insn-007bd8bc) · [`007bd8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd8a0.md#insn-007bd8dc)
- 新版 `007bd8fc`（命令位置の公開資料なし） · `007bd91c`（命令位置の公開資料なし）

~~~diff
- 007bd8bc ["INT_ADD", "register:40f0:8", ["const:7bd8bc:8", "const:4:8"]]
- 007bd8bc ["CALL", null, ["callee:00c53d00:8"]]
+ 007bd8fc ["INT_ADD", "register:40f0:8", ["const:7bd8fc:8", "const:4:8"]]
+ 007bd8fc ["CALL", null, ["callee:00c53d00:8"]]
- 007bd8bc bytes 09581294
+ 007bd8fc bytes 01591294
- 007bd8dc ["COPY", "register:0:8", ["register:4040:8"]]
- 007bd8dc ["INT_ADD", "register:40f0:8", ["const:7bd8dc:8", "const:4:8"]]
- 007bd8dc ["CALLIND", null, ["register:0:8"]]
+ 007bd91c ["COPY", "register:0:8", ["register:4040:8"]]
+ 007bd91c ["INT_ADD", "register:40f0:8", ["const:7bd91c:8", "const:4:8"]]
+ 007bd91c ["CALLIND", null, ["register:0:8"]]
- 007bd8dc bytes 00013fd6
+ 007bd91c bytes 00013fd6
~~~


<a id="compare-3fb5bbbc9da95131f49865dbe3381593"></a>

### [`007bd8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd8f0.md) → [`007bd930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bd930.md) FUN_007bd930

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007bd958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd8f0.md#insn-007bd958) · [`007bd9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bd8f0.md#insn-007bd9dc)
- 新版 `007bd998`（命令位置の公開資料なし） · `007bda1c`（命令位置の公開資料なし）

~~~diff
- 007bd958 ["INT_ADD", "register:40f0:8", ["const:7bd958:8", "const:4:8"]]
- 007bd958 ["CALL", null, ["callee:00c57e90:8"]]
+ 007bd998 ["INT_ADD", "register:40f0:8", ["const:7bd998:8", "const:4:8"]]
+ 007bd998 ["CALL", null, ["callee:00c57e90:8"]]
- 007bd958 bytes 4e681294
+ 007bd998 bytes 3e691294
- 007bd9dc ["INT_ADD", "register:40f0:8", ["const:7bd9dc:8", "const:4:8"]]
- 007bd9dc ["CALL", null, ["callee:0043bba4:8"]]
+ 007bda1c ["INT_ADD", "register:40f0:8", ["const:7bda1c:8", "const:4:8"]]
+ 007bda1c ["CALL", null, ["callee:0043bba4:8"]]
- 007bd9dc bytes 62f8f197
+ 007bda1c bytes 62f8f197
~~~


<a id="compare-d1e911449f0db65718bdb3cc1bc5b30f"></a>

### [`007c77a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c77a8.md) → [`007c77e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c77e8.md) FUN_007c77e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`009470d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00947/009470d0.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 2件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`0094726c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00947/0094726c.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007c77cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c77a8.md#insn-007c77cc) · [`007c7814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c77a8.md#insn-007c7814) · [`007c7834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c77a8.md#insn-007c7834)
- 新版 `007c780c`（命令位置の公開資料なし） · `007c7854`（命令位置の公開資料なし） · `007c7874`（命令位置の公開資料なし）

~~~diff
- 007c77cc ["INT_ADD", "register:40f0:8", ["const:7c77cc:8", "const:4:8"]]
- 007c77cc ["CALL", null, ["callee:00c57fe0:8"]]
+ 007c780c ["INT_ADD", "register:40f0:8", ["const:7c780c:8", "const:4:8"]]
+ 007c780c ["CALL", null, ["callee:00c57fe0:8"]]
- 007c77cc bytes 05411294
+ 007c780c bytes f5411294
- 007c7814 ["INT_ADD", "register:40f0:8", ["const:7c7814:8", "const:4:8"]]
- 007c7814 ["CALL", null, ["callee:00c57e90:8"]]
+ 007c7854 ["INT_ADD", "register:40f0:8", ["const:7c7854:8", "const:4:8"]]
+ 007c7854 ["CALL", null, ["callee:00c57e90:8"]]
- 007c7814 bytes 9f401294
+ 007c7854 bytes 8f411294
- 007c7834 ["INT_ADD", "register:40f0:8", ["const:7c7834:8", "const:4:8"]]
- 007c7834 ["CALL", null, ["callee:00c57f40:8"]]
+ 007c7874 ["INT_ADD", "register:40f0:8", ["const:7c7874:8", "const:4:8"]]
+ 007c7874 ["CALL", null, ["callee:00c57f40:8"]]
- 007c7834 bytes c3401294
+ 007c7874 bytes b3411294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dfb7e5e426f213cbc3c27ea59b3ef64"></a>

### [`007c7870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7870.md) → [`007c78b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c78b0.md) FUN_007c78b0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) [`00ab2fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab2/00ab2fa8.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) [`00ab31a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab3/00ab31a4.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007c78d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7870.md#insn-007c78d8) · [`007c7910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7870.md#insn-007c7910)
- 新版 `007c7918`（命令位置の公開資料なし） · `007c7950`（命令位置の公開資料なし）

~~~diff
- 007c78d8 ["INT_ADD", "register:40f0:8", ["const:7c78d8:8", "const:4:8"]]
- 007c78d8 ["CALL", null, ["callee:00c57e90:8"]]
+ 007c7918 ["INT_ADD", "register:40f0:8", ["const:7c7918:8", "const:4:8"]]
+ 007c7918 ["CALL", null, ["callee:00c57e90:8"]]
- 007c78d8 bytes 6e401294
+ 007c7918 bytes 5e411294
- 007c7910 ["INT_ADD", "register:40f0:8", ["const:7c7910:8", "const:4:8"]]
- 007c7910 ["CALL", null, ["callee:0043bba4:8"]]
+ 007c7950 ["INT_ADD", "register:40f0:8", ["const:7c7950:8", "const:4:8"]]
+ 007c7950 ["CALL", null, ["callee:0043bba4:8"]]
- 007c7910 bytes 95d0f197
+ 007c7950 bytes 95d0f197
~~~


<a id="compare-f09a4e57d19f38418cc60f4b97862d50"></a>

### [`007c7e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7e28.md) → [`007c7e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7e68.md) FUN_007c7e68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) · 呼出先 5件 [`007f1e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1e78.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) · 呼出先 5件 [`007f1eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1eb8.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007c7e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7e28.md#insn-007c7e58) · [`007c7e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7e28.md#insn-007c7e70) · [`007c7e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7e28.md#insn-007c7e8c)
- 新版 `007c7e98`（命令位置の公開資料なし） · `007c7eb0`（命令位置の公開資料なし） · `007c7ecc`（命令位置の公開資料なし）

~~~diff
- 007c7e58 ["INT_ADD", "register:40f0:8", ["const:7c7e58:8", "const:4:8"]]
- 007c7e58 ["CALL", null, ["callee:00c57e90:8"]]
+ 007c7e98 ["INT_ADD", "register:40f0:8", ["const:7c7e98:8", "const:4:8"]]
+ 007c7e98 ["CALL", null, ["callee:00c57e90:8"]]
- 007c7e58 bytes 0e3f1294
+ 007c7e98 bytes fe3f1294
- 007c7e70 ["INT_ADD", "register:40f0:8", ["const:7c7e70:8", "const:4:8"]]
- 007c7e70 ["CALL", null, ["callee:00c58000:8"]]
+ 007c7eb0 ["INT_ADD", "register:40f0:8", ["const:7c7eb0:8", "const:4:8"]]
+ 007c7eb0 ["CALL", null, ["callee:00c58000:8"]]
- 007c7e70 bytes 643f1294
+ 007c7eb0 bytes 54401294
- 007c7e8c ["INT_ADD", "register:40f0:8", ["const:7c7e8c:8", "const:4:8"]]
- 007c7e8c ["CALL", null, ["callee:007f1eb8:8"]]
+ 007c7ecc ["INT_ADD", "register:40f0:8", ["const:7c7ecc:8", "const:4:8"]]
+ 007c7ecc ["CALL", null, ["callee:007f1eb8:8"]]
- 007c7e8c bytes fba70094
+ 007c7ecc bytes fba70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07cb4f5cd1b6f585b03adf4d0ceee373"></a>

### [`007c7eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7eb0.md) → [`007c7ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7ef0.md) FUN_007c7ef0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`007efc68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efc68.md) · 呼出先 8件 [`005e4698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e4698.md) [`005e46a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e46a0.md) [`005e486c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e486c.md) [`005e49f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e49f4.md) [`005e4a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e4a54.md)
- 新版 呼出元 2件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) · 呼出先 8件 [`005e46d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e46d8.md) [`005e46e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e46e0.md) [`005e48ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e48ac.md) [`005e4a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4a34.md) [`005e4a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4a94.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007c7ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7eb0.md#insn-007c7ec8) · [`007c7ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7eb0.md#insn-007c7ed0) · [`007c7efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7eb0.md#insn-007c7efc)
- 新版 `007c7f08`（命令位置の公開資料なし） · `007c7f10`（命令位置の公開資料なし） · `007c7f3c`（命令位置の公開資料なし）

~~~diff
- 007c7ec8 ["INT_ADD", "register:40f0:8", ["const:7c7ec8:8", "const:4:8"]]
- 007c7ec8 ["CALL", null, ["callee:005e4a34:8"]]
+ 007c7f08 ["INT_ADD", "register:40f0:8", ["const:7c7f08:8", "const:4:8"]]
+ 007c7f08 ["CALL", null, ["callee:005e4a34:8"]]
- 007c7ec8 bytes cb72f897
+ 007c7f08 bytes cb72f897
- 007c7ed0 ["INT_ADD", "register:40f0:8", ["const:7c7ed0:8", "const:4:8"]]
- 007c7ed0 ["CALL", null, ["callee:005e46d8:8"]]
+ 007c7f10 ["INT_ADD", "register:40f0:8", ["const:7c7f10:8", "const:4:8"]]
+ 007c7f10 ["CALL", null, ["callee:005e46d8:8"]]
- 007c7ed0 bytes f271f897
+ 007c7f10 bytes f271f897
- 007c7efc ["INT_ADD", "register:40f0:8", ["const:7c7efc:8", "const:4:8"]]
- 007c7efc ["CALL", null, ["callee:005e4b14:8"]]
+ 007c7f3c ["INT_ADD", "register:40f0:8", ["const:7c7f3c:8", "const:4:8"]]
+ 007c7f3c ["CALL", null, ["callee:005e4b14:8"]]
- 007c7efc bytes f672f897
+ 007c7f3c bytes f672f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5e57711ce6c7aeb61149473dbf1e507"></a>

### [`007cb548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cb/007cb548.md) → [`007cb588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb588.md) FUN_007cb588

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007cb568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cb/007cb548.md#insn-007cb568) · [`007cb578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cb/007cb548.md#insn-007cb578)
- 新版 `007cb5a8`（命令位置の公開資料なし） · `007cb5b8`（命令位置の公開資料なし）

~~~diff
- 007cb568 ["COPY", "register:0:8", ["register:4040:8"]]
- 007cb568 ["INT_ADD", "register:40f0:8", ["const:7cb568:8", "const:4:8"]]
- 007cb568 ["CALLIND", null, ["register:0:8"]]
+ 007cb5a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007cb5a8 ["INT_ADD", "register:40f0:8", ["const:7cb5a8:8", "const:4:8"]]
+ 007cb5a8 ["CALLIND", null, ["register:0:8"]]
- 007cb568 bytes 00013fd6
+ 007cb5a8 bytes 00013fd6
- 007cb578 ["INT_ADD", "register:40f0:8", ["const:7cb578:8", "const:4:8"]]
- 007cb578 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007cb5b8 ["INT_ADD", "register:40f0:8", ["const:7cb5b8:8", "const:4:8"]]
+ 007cb5b8 ["CALL", null, ["callee:00c57eb0:8"]]
- 007cb578 bytes 4e311294
+ 007cb5b8 bytes 3e321294
~~~


<a id="compare-00aba69b28400daec4238af7b46fc6b6"></a>

### [`007dcef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dc/007dcef8.md) → [`007dcf38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dc/007dcf38.md) FUN_007dcf38

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007dcf14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dc/007dcef8.md#insn-007dcf14) · [`007dcf34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dc/007dcef8.md#insn-007dcf34)
- 新版 `007dcf54`（命令位置の公開資料なし） · `007dcf74`（命令位置の公開資料なし）

~~~diff
- 007dcf14 ["INT_ADD", "register:40f0:8", ["const:7dcf14:8", "const:4:8"]]
- 007dcf14 ["CALL", null, ["callee:00c53d00:8"]]
+ 007dcf54 ["INT_ADD", "register:40f0:8", ["const:7dcf54:8", "const:4:8"]]
+ 007dcf54 ["CALL", null, ["callee:00c53d00:8"]]
- 007dcf14 bytes 73da1194
+ 007dcf54 bytes 6bdb1194
- 007dcf34 ["COPY", "register:0:8", ["register:4040:8"]]
- 007dcf34 ["INT_ADD", "register:40f0:8", ["const:7dcf34:8", "const:4:8"]]
- 007dcf34 ["CALLIND", null, ["register:0:8"]]
+ 007dcf74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007dcf74 ["INT_ADD", "register:40f0:8", ["const:7dcf74:8", "const:4:8"]]
+ 007dcf74 ["CALLIND", null, ["register:0:8"]]
- 007dcf34 bytes 00013fd6
+ 007dcf74 bytes 00013fd6
~~~


<a id="compare-654be05027b14316a1f323e3d2d89788"></a>

### [`007dcf48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dc/007dcf48.md) → [`007dcf88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dc/007dcf88.md) FUN_007dcf88

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`00914c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00914/00914c94.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 2件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00914e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00914/00914e30.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007dcf6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dc/007dcf48.md#insn-007dcf6c) · [`007dcfb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dc/007dcf48.md#insn-007dcfb4) · [`007dcfd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dc/007dcf48.md#insn-007dcfd4)
- 新版 `007dcfac`（命令位置の公開資料なし） · `007dcff4`（命令位置の公開資料なし） · `007dd014`（命令位置の公開資料なし）

~~~diff
- 007dcf6c ["INT_ADD", "register:40f0:8", ["const:7dcf6c:8", "const:4:8"]]
- 007dcf6c ["CALL", null, ["callee:00c57fe0:8"]]
+ 007dcfac ["INT_ADD", "register:40f0:8", ["const:7dcfac:8", "const:4:8"]]
+ 007dcfac ["CALL", null, ["callee:00c57fe0:8"]]
- 007dcf6c bytes 1deb1194
+ 007dcfac bytes 0dec1194
- 007dcfb4 ["INT_ADD", "register:40f0:8", ["const:7dcfb4:8", "const:4:8"]]
- 007dcfb4 ["CALL", null, ["callee:00c57e90:8"]]
+ 007dcff4 ["INT_ADD", "register:40f0:8", ["const:7dcff4:8", "const:4:8"]]
+ 007dcff4 ["CALL", null, ["callee:00c57e90:8"]]
- 007dcfb4 bytes b7ea1194
+ 007dcff4 bytes a7eb1194
- 007dcfd4 ["INT_ADD", "register:40f0:8", ["const:7dcfd4:8", "const:4:8"]]
- 007dcfd4 ["CALL", null, ["callee:00c57f40:8"]]
+ 007dd014 ["INT_ADD", "register:40f0:8", ["const:7dd014:8", "const:4:8"]]
+ 007dd014 ["CALL", null, ["callee:00c57f40:8"]]
- 007dcfd4 bytes dbea1194
+ 007dd014 bytes cbeb1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff0c01a5037504c5e6c5c0e175857c81"></a>

### [`007dd010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd010.md) → [`007dd050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd050.md) FUN_007dd050

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 5件 [`005e4e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e4e34.md) [`0066a3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a3c8.md) [`00802678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md) [`00802b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b18.md) [`00a68d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68d50.md)
- 新版 呼出元 3件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 5件 [`005e4e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4e74.md) [`0066a408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066a/0066a408.md) [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00a68f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68f48.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007dd030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd010.md#insn-007dd030) · [`007dd040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd010.md#insn-007dd040) · [`007dd054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd010.md#insn-007dd054)
- 新版 `007dd070`（命令位置の公開資料なし） · `007dd080`（命令位置の公開資料なし） · `007dd094`（命令位置の公開資料なし）

~~~diff
- 007dd030 ["INT_ADD", "register:40f0:8", ["const:7dd030:8", "const:4:8"]]
- 007dd030 ["CALL", null, ["callee:00802b58:8"]]
+ 007dd070 ["INT_ADD", "register:40f0:8", ["const:7dd070:8", "const:4:8"]]
+ 007dd070 ["CALL", null, ["callee:00802b58:8"]]
- 007dd030 bytes ba960094
+ 007dd070 bytes ba960094
- 007dd040 ["INT_ADD", "register:40f0:8", ["const:7dd040:8", "const:4:8"]]
- 007dd040 ["CALL", null, ["callee:0066a408:8"]]
+ 007dd080 ["INT_ADD", "register:40f0:8", ["const:7dd080:8", "const:4:8"]]
+ 007dd080 ["CALL", null, ["callee:0066a408:8"]]
- 007dd040 bytes e234fa97
+ 007dd080 bytes e234fa97
- 007dd054 ["INT_ADD", "register:40f0:8", ["const:7dd054:8", "const:4:8"]]
- 007dd054 ["CALL", null, ["callee:008026b8:8"]]
+ 007dd094 ["INT_ADD", "register:40f0:8", ["const:7dd094:8", "const:4:8"]]
+ 007dd094 ["CALL", null, ["callee:008026b8:8"]]
- 007dd054 bytes 89950094
+ 007dd094 bytes 89950094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f40112f57ee8a0da76c162d8a39d2338"></a>

### [`007dd0b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd0b8.md) → [`007dd0f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd0f8.md) FUN_007dd0f8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007dd0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd0b8.md#insn-007dd0dc) · [`007dd124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd0b8.md#insn-007dd124) · [`007dd144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd0b8.md#insn-007dd144)
- 新版 `007dd11c`（命令位置の公開資料なし） · `007dd164`（命令位置の公開資料なし） · `007dd184`（命令位置の公開資料なし）

~~~diff
- 007dd0dc ["INT_ADD", "register:40f0:8", ["const:7dd0dc:8", "const:4:8"]]
- 007dd0dc ["CALL", null, ["callee:00c57fe0:8"]]
+ 007dd11c ["INT_ADD", "register:40f0:8", ["const:7dd11c:8", "const:4:8"]]
+ 007dd11c ["CALL", null, ["callee:00c57fe0:8"]]
- 007dd0dc bytes c1ea1194
+ 007dd11c bytes b1eb1194
- 007dd124 ["INT_ADD", "register:40f0:8", ["const:7dd124:8", "const:4:8"]]
- 007dd124 ["CALL", null, ["callee:00c57e90:8"]]
+ 007dd164 ["INT_ADD", "register:40f0:8", ["const:7dd164:8", "const:4:8"]]
+ 007dd164 ["CALL", null, ["callee:00c57e90:8"]]
- 007dd124 bytes 5bea1194
+ 007dd164 bytes 4beb1194
- 007dd144 ["INT_ADD", "register:40f0:8", ["const:7dd144:8", "const:4:8"]]
- 007dd144 ["CALL", null, ["callee:00c57f40:8"]]
+ 007dd184 ["INT_ADD", "register:40f0:8", ["const:7dd184:8", "const:4:8"]]
+ 007dd184 ["CALL", null, ["callee:00c57f40:8"]]
- 007dd144 bytes 7fea1194
+ 007dd184 bytes 6feb1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9680ca54196c29acb01d26112a6be71f"></a>

### [`007dd180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd180.md) → [`007dd1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd1c0.md) FUN_007dd1c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007dd1a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd180.md#insn-007dd1a4) · [`007dd1ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd180.md#insn-007dd1ec) · [`007dd20c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd180.md#insn-007dd20c)
- 新版 `007dd1e4`（命令位置の公開資料なし） · `007dd22c`（命令位置の公開資料なし） · `007dd24c`（命令位置の公開資料なし）

~~~diff
- 007dd1a4 ["INT_ADD", "register:40f0:8", ["const:7dd1a4:8", "const:4:8"]]
- 007dd1a4 ["CALL", null, ["callee:00c57fe0:8"]]
+ 007dd1e4 ["INT_ADD", "register:40f0:8", ["const:7dd1e4:8", "const:4:8"]]
+ 007dd1e4 ["CALL", null, ["callee:00c57fe0:8"]]
- 007dd1a4 bytes 8fea1194
+ 007dd1e4 bytes 7feb1194
- 007dd1ec ["INT_ADD", "register:40f0:8", ["const:7dd1ec:8", "const:4:8"]]
- 007dd1ec ["CALL", null, ["callee:00c57e90:8"]]
+ 007dd22c ["INT_ADD", "register:40f0:8", ["const:7dd22c:8", "const:4:8"]]
+ 007dd22c ["CALL", null, ["callee:00c57e90:8"]]
- 007dd1ec bytes 29ea1194
+ 007dd22c bytes 19eb1194
- 007dd20c ["INT_ADD", "register:40f0:8", ["const:7dd20c:8", "const:4:8"]]
- 007dd20c ["CALL", null, ["callee:00c57f40:8"]]
+ 007dd24c ["INT_ADD", "register:40f0:8", ["const:7dd24c:8", "const:4:8"]]
+ 007dd24c ["CALL", null, ["callee:00c57f40:8"]]
- 007dd20c bytes 4dea1194
+ 007dd24c bytes 3deb1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64f0e6005eba549da0b4fb2878fdb727"></a>

### [`007dd248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd248.md) → [`007dd288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd288.md) FUN_007dd288

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007dd2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd248.md#insn-007dd2b0) · [`007dd2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd248.md#insn-007dd2fc)
- 新版 `007dd2f0`（命令位置の公開資料なし） · `007dd33c`（命令位置の公開資料なし）

~~~diff
- 007dd2b0 ["INT_ADD", "register:40f0:8", ["const:7dd2b0:8", "const:4:8"]]
- 007dd2b0 ["CALL", null, ["callee:00c57e90:8"]]
+ 007dd2f0 ["INT_ADD", "register:40f0:8", ["const:7dd2f0:8", "const:4:8"]]
+ 007dd2f0 ["CALL", null, ["callee:00c57e90:8"]]
- 007dd2b0 bytes f8e91194
+ 007dd2f0 bytes e8ea1194
- 007dd2fc ["INT_ADD", "register:40f0:8", ["const:7dd2fc:8", "const:4:8"]]
- 007dd2fc ["CALL", null, ["callee:0043bba4:8"]]
+ 007dd33c ["INT_ADD", "register:40f0:8", ["const:7dd33c:8", "const:4:8"]]
+ 007dd33c ["CALL", null, ["callee:0043bba4:8"]]
- 007dd2fc bytes 1a7af197
+ 007dd33c bytes 1a7af197
~~~


<a id="compare-2a0f3149c876ffc9af03f362af88a6c9"></a>

### [`007de4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007de/007de4e8.md) → [`007de528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007de/007de528.md) FUN_007de528

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) [`00a65bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65bf4.md) [`00ab2fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab2/00ab2fa8.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 4件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`00a65dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a65/00a65dec.md) [`00ab31a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab3/00ab31a4.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007de550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007de/007de4e8.md#insn-007de550) · [`007de594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007de/007de4e8.md#insn-007de594)
- 新版 `007de590`（命令位置の公開資料なし） · `007de5d4`（命令位置の公開資料なし）

~~~diff
- 007de550 ["INT_ADD", "register:40f0:8", ["const:7de550:8", "const:4:8"]]
- 007de550 ["CALL", null, ["callee:00c57e90:8"]]
+ 007de590 ["INT_ADD", "register:40f0:8", ["const:7de590:8", "const:4:8"]]
+ 007de590 ["CALL", null, ["callee:00c57e90:8"]]
- 007de550 bytes 50e51194
+ 007de590 bytes 40e61194
- 007de594 ["INT_ADD", "register:40f0:8", ["const:7de594:8", "const:4:8"]]
- 007de594 ["CALL", null, ["callee:0043bba4:8"]]
+ 007de5d4 ["INT_ADD", "register:40f0:8", ["const:7de5d4:8", "const:4:8"]]
+ 007de5d4 ["CALL", null, ["callee:0043bba4:8"]]
- 007de594 bytes 7475f197
+ 007de5d4 bytes 7475f197
~~~


<a id="compare-ba30538aec2181643f0daeb5f11a4d8a"></a>

### [`007de820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007de/007de820.md) → [`007de860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007de/007de860.md) FUN_007de860

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 2件 [`00903da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00903/00903da8.md) [`009e0e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0e24.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 2件 [`00903f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00903/00903f44.md) [`009e0fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0fc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007de850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007de/007de820.md#insn-007de850)
- 新版 `007de890`（命令位置の公開資料なし）

~~~diff
- 007de850 ["INT_ADD", "register:40f0:8", ["const:7de850:8", "const:4:8"]]
- 007de850 ["CALL", null, ["callee:00903f44:8"]]
+ 007de890 ["INT_ADD", "register:40f0:8", ["const:7de890:8", "const:4:8"]]
+ 007de890 ["CALL", null, ["callee:00903f44:8"]]
- 007de850 bytes 56950494
+ 007de890 bytes ad950494
~~~


<a id="compare-627d547f0da1428b7b21f22bc980daa7"></a>

### [`007ef3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007ef3b0.md) → [`007ef3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef3f0.md) FUN_007ef3f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00753490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/00753490.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`007534d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00753/007534d0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007ef458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007ef3b0.md#insn-007ef458) · [`007ef49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007ef3b0.md#insn-007ef49c) · [`007ef4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007ef3b0.md#insn-007ef4b0)
- 新版 `007ef498`（命令位置の公開資料なし） · `007ef4dc`（命令位置の公開資料なし） · `007ef4f0`（命令位置の公開資料なし）

~~~diff
- 007ef458 ["INT_ADD", "register:40f0:8", ["const:7ef458:8", "const:4:8"]]
- 007ef458 ["CALL", null, ["callee:00c57e90:8"]]
+ 007ef498 ["INT_ADD", "register:40f0:8", ["const:7ef498:8", "const:4:8"]]
+ 007ef498 ["CALL", null, ["callee:00c57e90:8"]]
- 007ef458 bytes 8ea11194
+ 007ef498 bytes 7ea21194
- 007ef49c ["INT_ADD", "register:40f0:8", ["const:7ef49c:8", "const:4:8"]]
- 007ef49c ["CALL", null, ["callee:00c58000:8"]]
+ 007ef4dc ["INT_ADD", "register:40f0:8", ["const:7ef4dc:8", "const:4:8"]]
+ 007ef4dc ["CALL", null, ["callee:00c58000:8"]]
- 007ef49c bytes d9a11194
+ 007ef4dc bytes c9a21194
- 007ef4b0 ["INT_ADD", "register:40f0:8", ["const:7ef4b0:8", "const:4:8"]]
- 007ef4b0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007ef4f0 ["INT_ADD", "register:40f0:8", ["const:7ef4f0:8", "const:4:8"]]
+ 007ef4f0 ["CALL", null, ["callee:00c57eb0:8"]]
- 007ef4b0 bytes 80a11194
+ 007ef4f0 bytes 70a21194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1592fd3bebaf25426c629f37600ff9d7"></a>

### [`007ef59c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007ef59c.md) → [`007ef5dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef5dc.md) FUN_007ef5dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 5件 [`00753490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/00753490.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 5件 [`007534d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00753/007534d0.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007ef5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007ef59c.md#insn-007ef5ec) · [`007ef604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007ef59c.md#insn-007ef604) · [`007ef620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007ef59c.md#insn-007ef620)
- 新版 `007ef62c`（命令位置の公開資料なし） · `007ef644`（命令位置の公開資料なし） · `007ef660`（命令位置の公開資料なし）

~~~diff
- 007ef5ec ["INT_ADD", "register:40f0:8", ["const:7ef5ec:8", "const:4:8"]]
- 007ef5ec ["CALL", null, ["callee:00c57e90:8"]]
+ 007ef62c ["INT_ADD", "register:40f0:8", ["const:7ef62c:8", "const:4:8"]]
+ 007ef62c ["CALL", null, ["callee:00c57e90:8"]]
- 007ef5ec bytes 29a11194
+ 007ef62c bytes 19a21194
- 007ef604 ["INT_ADD", "register:40f0:8", ["const:7ef604:8", "const:4:8"]]
- 007ef604 ["CALL", null, ["callee:00c58000:8"]]
+ 007ef644 ["INT_ADD", "register:40f0:8", ["const:7ef644:8", "const:4:8"]]
+ 007ef644 ["CALL", null, ["callee:00c58000:8"]]
- 007ef604 bytes 7fa11194
+ 007ef644 bytes 6fa21194
- 007ef620 ["INT_ADD", "register:40f0:8", ["const:7ef620:8", "const:4:8"]]
- 007ef620 ["CALL", null, ["callee:007534d0:8"]]
+ 007ef660 ["INT_ADD", "register:40f0:8", ["const:7ef660:8", "const:4:8"]]
+ 007ef660 ["CALL", null, ["callee:007534d0:8"]]
- 007ef620 bytes 9c8ffd97
+ 007ef660 bytes 9c8ffd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af24e3309c1c000a6928312350c3c3db"></a>

### [`007efa48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efa48.md) → [`007efa88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efa88.md) FUN_007efa88

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`007cb5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cb/007cb5a0.md) [`009e486c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e4/009e486c.md) [`00a60550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a60/00a60550.md) [`00ab4b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab4/00ab4b04.md) · 呼出先 5件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 4件 [`007cb5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb5e0.md) [`009e4a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e4/009e4a08.md) [`00a60748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a60/00a60748.md) [`00ab4d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab4/00ab4d00.md) · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007efa6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efa48.md#insn-007efa6c) · [`007efab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efa48.md#insn-007efab4) · [`007efad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efa48.md#insn-007efad4)
- 新版 `007efaac`（命令位置の公開資料なし） · `007efaf4`（命令位置の公開資料なし） · `007efb14`（命令位置の公開資料なし）

~~~diff
- 007efa6c ["INT_ADD", "register:40f0:8", ["const:7efa6c:8", "const:4:8"]]
- 007efa6c ["CALL", null, ["callee:00c57fe0:8"]]
+ 007efaac ["INT_ADD", "register:40f0:8", ["const:7efaac:8", "const:4:8"]]
+ 007efaac ["CALL", null, ["callee:00c57fe0:8"]]
- 007efa6c bytes 5da01194
+ 007efaac bytes 4da11194
- 007efab4 ["INT_ADD", "register:40f0:8", ["const:7efab4:8", "const:4:8"]]
- 007efab4 ["CALL", null, ["callee:00c57e90:8"]]
+ 007efaf4 ["INT_ADD", "register:40f0:8", ["const:7efaf4:8", "const:4:8"]]
+ 007efaf4 ["CALL", null, ["callee:00c57e90:8"]]
- 007efab4 bytes f79f1194
+ 007efaf4 bytes e7a01194
- 007efad4 ["INT_ADD", "register:40f0:8", ["const:7efad4:8", "const:4:8"]]
- 007efad4 ["CALL", null, ["callee:00c57f40:8"]]
+ 007efb14 ["INT_ADD", "register:40f0:8", ["const:7efb14:8", "const:4:8"]]
+ 007efb14 ["CALL", null, ["callee:00c57f40:8"]]
- 007efad4 bytes 1ba01194
+ 007efb14 bytes 0ba11194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59c062083f76bbd5bf7cd344e80c01e6"></a>

### [`007f0394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0394.md) → [`007f03d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f03d4.md) FUN_007f03d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007caa88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ca/007caa88.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`007caac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007caac8.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f0450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0394.md#insn-007f0450) · [`007f0478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0394.md#insn-007f0478) · [`007f048c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0394.md#insn-007f048c)
- 新版 `007f0490`（命令位置の公開資料なし） · `007f04b8`（命令位置の公開資料なし） · `007f04cc`（命令位置の公開資料なし）

~~~diff
- 007f0450 ["INT_ADD", "register:40f0:8", ["const:7f0450:8", "const:4:8"]]
- 007f0450 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f0490 ["INT_ADD", "register:40f0:8", ["const:7f0490:8", "const:4:8"]]
+ 007f0490 ["CALL", null, ["callee:00c57e90:8"]]
- 007f0450 bytes 909d1194
+ 007f0490 bytes 809e1194
- 007f0478 ["INT_ADD", "register:40f0:8", ["const:7f0478:8", "const:4:8"]]
- 007f0478 ["CALL", null, ["callee:00c58000:8"]]
+ 007f04b8 ["INT_ADD", "register:40f0:8", ["const:7f04b8:8", "const:4:8"]]
+ 007f04b8 ["CALL", null, ["callee:00c58000:8"]]
- 007f0478 bytes e29d1194
+ 007f04b8 bytes d29e1194
- 007f048c ["INT_ADD", "register:40f0:8", ["const:7f048c:8", "const:4:8"]]
- 007f048c ["CALL", null, ["callee:00c57eb0:8"]]
+ 007f04cc ["INT_ADD", "register:40f0:8", ["const:7f04cc:8", "const:4:8"]]
+ 007f04cc ["CALL", null, ["callee:00c57eb0:8"]]
- 007f048c bytes 899d1194
+ 007f04cc bytes 799e1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54e8a8aa112e0dfc2aeb6cf7520bed3d"></a>

### [`007f0c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0c34.md) → [`007f0c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0c74.md) FUN_007f0c74

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`007f06b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f06b4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`007f06f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f06f4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f0c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0c34.md#insn-007f0c44)
- 新版 `007f0c84`（命令位置の公開資料なし）

~~~diff
- 007f0c44 ["INT_ADD", "register:40f0:8", ["const:7f0c44:8", "const:4:8"]]
- 007f0c44 ["CALL", null, ["callee:007f06f4:8"]]
+ 007f0c84 ["INT_ADD", "register:40f0:8", ["const:7f0c84:8", "const:4:8"]]
+ 007f0c84 ["CALL", null, ["callee:007f06f4:8"]]
- 007f0c44 bytes 9cfeff97
+ 007f0c84 bytes 9cfeff97
~~~


<a id="compare-224f66bccede7c1359e4cb7cf7cc4820"></a>

### [`007f0c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0c58.md) → [`007f0c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0c98.md) FUN_007f0c98

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007bbab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbab4.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`007f0d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0d94.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`007bbaf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbaf4.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`007f0dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0dd4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f0cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0c58.md#insn-007f0cb8) · [`007f0cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0c58.md#insn-007f0cc8) · [`007f0d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0c58.md#insn-007f0d00)
- 新版 `007f0cf8`（命令位置の公開資料なし） · `007f0d08`（命令位置の公開資料なし） · `007f0d40`（命令位置の公開資料なし）

~~~diff
- 007f0cb8 ["INT_ADD", "register:40f0:8", ["const:7f0cb8:8", "const:4:8"]]
- 007f0cb8 ["CALL", null, ["callee:0043bb20:8"]]
+ 007f0cf8 ["INT_ADD", "register:40f0:8", ["const:7f0cf8:8", "const:4:8"]]
+ 007f0cf8 ["CALL", null, ["callee:0043bb20:8"]]
- 007f0cb8 bytes 8a2bf197
+ 007f0cf8 bytes 8a2bf197
- 007f0cc8 ["INT_ADD", "register:40f0:8", ["const:7f0cc8:8", "const:4:8"]]
- 007f0cc8 ["CALL", null, ["callee:0043bb20:8"]]
+ 007f0d08 ["INT_ADD", "register:40f0:8", ["const:7f0d08:8", "const:4:8"]]
+ 007f0d08 ["CALL", null, ["callee:0043bb20:8"]]
- 007f0cc8 bytes 862bf197
+ 007f0d08 bytes 862bf197
- 007f0d00 ["INT_ADD", "register:40f0:8", ["const:7f0d00:8", "const:4:8"]]
- 007f0d00 ["CALL", null, ["callee:007f0dd4:8"]]
+ 007f0d40 ["INT_ADD", "register:40f0:8", ["const:7f0d40:8", "const:4:8"]]
+ 007f0d40 ["CALL", null, ["callee:007f0dd4:8"]]
- 007f0d00 bytes 25000094
+ 007f0d40 bytes 25000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3252719c219349e1578f8a1300768a8"></a>

### [`007f1854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1854.md) → [`007f1894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1894.md) FUN_007f1894

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007bbddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbddc.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`007f1a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1a78.md) [`007f1e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1e50.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`007bbe1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbe1c.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`007f1ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ab8.md) [`007f1e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1e90.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f1914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1854.md#insn-007f1914) · [`007f193c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1854.md#insn-007f193c) · [`007f1984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1854.md#insn-007f1984)
- 新版 `007f1954`（命令位置の公開資料なし） · `007f197c`（命令位置の公開資料なし） · `007f19c4`（命令位置の公開資料なし）

~~~diff
- 007f1914 ["INT_ADD", "register:40f0:8", ["const:7f1914:8", "const:4:8"]]
- 007f1914 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f1954 ["INT_ADD", "register:40f0:8", ["const:7f1954:8", "const:4:8"]]
+ 007f1954 ["CALL", null, ["callee:00c57e90:8"]]
- 007f1914 bytes 5f981194
+ 007f1954 bytes 4f991194
- 007f193c ["INT_ADD", "register:40f0:8", ["const:7f193c:8", "const:4:8"]]
- 007f193c ["CALL", null, ["callee:007f1ab8:8"]]
+ 007f197c ["INT_ADD", "register:40f0:8", ["const:7f197c:8", "const:4:8"]]
+ 007f197c ["CALL", null, ["callee:007f1ab8:8"]]
- 007f193c bytes 4f000094
+ 007f197c bytes 4f000094
- 007f1984 ["INT_ADD", "register:40f0:8", ["const:7f1984:8", "const:4:8"]]
- 007f1984 ["CALL", null, ["callee:007f1ab8:8"]]
+ 007f19c4 ["INT_ADD", "register:40f0:8", ["const:7f19c4:8", "const:4:8"]]
+ 007f19c4 ["CALL", null, ["callee:007f1ab8:8"]]
- 007f1984 bytes 3d000094
+ 007f19c4 bytes 3d000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30b29cd62097248e439fcf309c43a468"></a>

### [`007f1a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1a78.md) → [`007f1ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ab8.md) FUN_007f1ab8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007f1854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1854.md) [`0090113c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00901/0090113c.md) · 呼出先 7件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0046e7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e7ec.md) [`00470314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470314.md) [`007f1c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1c70.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 2件 [`007f1894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1894.md) [`009012d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00901/009012d8.md) · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0046e82c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e82c.md) [`00470354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470354.md) [`007f1cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1cb0.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f1af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1a78.md#insn-007f1af0) · [`007f1b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1a78.md#insn-007f1b14) · [`007f1b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1a78.md#insn-007f1b5c)
- 新版 `007f1b30`（命令位置の公開資料なし） · `007f1b54`（命令位置の公開資料なし） · `007f1b9c`（命令位置の公開資料なし）

~~~diff
- 007f1af0 ["INT_ADD", "register:40f0:8", ["const:7f1af0:8", "const:4:8"]]
- 007f1af0 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f1b30 ["INT_ADD", "register:40f0:8", ["const:7f1b30:8", "const:4:8"]]
+ 007f1b30 ["CALL", null, ["callee:00c57e90:8"]]
- 007f1af0 bytes e8971194
+ 007f1b30 bytes d8981194
- 007f1b14 ["INT_ADD", "register:40f0:8", ["const:7f1b14:8", "const:4:8"]]
- 007f1b14 ["CALL", null, ["callee:007f1cb0:8"]]
+ 007f1b54 ["INT_ADD", "register:40f0:8", ["const:7f1b54:8", "const:4:8"]]
+ 007f1b54 ["CALL", null, ["callee:007f1cb0:8"]]
- 007f1b14 bytes 57000094
+ 007f1b54 bytes 57000094
- 007f1b5c ["INT_ADD", "register:40f0:8", ["const:7f1b5c:8", "const:4:8"]]
- 007f1b5c ["CALL", null, ["callee:0043bb20:8"]]
+ 007f1b9c ["INT_ADD", "register:40f0:8", ["const:7f1b9c:8", "const:4:8"]]
+ 007f1b9c ["CALL", null, ["callee:0043bb20:8"]]
- 007f1b5c bytes e127f197
+ 007f1b9c bytes e127f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4929a7186799be393c7751800d7320f7"></a>

### [`007f1be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1be8.md) → [`007f1c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1c28.md) FUN_007f1c28

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f1c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1be8.md#insn-007f1c4c)
- 新版 `007f1c8c`（命令位置の公開資料なし）

~~~diff
- 007f1c4c ["INT_ADD", "register:40f0:8", ["const:7f1c4c:8", "const:4:8"]]
- 007f1c4c ["CALL", null, ["callee:00c57eb0:8"]]
+ 007f1c8c ["INT_ADD", "register:40f0:8", ["const:7f1c8c:8", "const:4:8"]]
+ 007f1c8c ["CALL", null, ["callee:00c57eb0:8"]]
- 007f1c4c bytes 99971194
+ 007f1c8c bytes 89981194
~~~


<a id="compare-74b2afa2e2b99835bebcff1880df3584"></a>

### [`007f1c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1c70.md) → [`007f1cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1cb0.md) FUN_007f1cb0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`007bbddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbddc.md) [`007f1a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1a78.md) [`008ff730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ff/008ff730.md) [`00a3f154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3f/00a3f154.md) · 呼出先 7件 [`00470454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470454.md) [`007f1da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1da8.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`007bbe1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbe1c.md) [`007f1ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ab8.md) [`008ff8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff8cc.md) [`00a3f34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3f/00a3f34c.md) · 呼出先 7件 [`00470494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470494.md) [`007f1de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1de8.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f1d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1c70.md#insn-007f1d00) · [`007f1d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1c70.md#insn-007f1d18) · [`007f1d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1c70.md#insn-007f1d68)
- 新版 `007f1d40`（命令位置の公開資料なし） · `007f1d58`（命令位置の公開資料なし） · `007f1da8`（命令位置の公開資料なし）

~~~diff
- 007f1d00 ["INT_ADD", "register:40f0:8", ["const:7f1d00:8", "const:4:8"]]
- 007f1d00 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f1d40 ["INT_ADD", "register:40f0:8", ["const:7f1d40:8", "const:4:8"]]
+ 007f1d40 ["CALL", null, ["callee:00c57e90:8"]]
- 007f1d00 bytes 64971194
+ 007f1d40 bytes 54981194
- 007f1d18 ["INT_ADD", "register:40f0:8", ["const:7f1d18:8", "const:4:8"]]
- 007f1d18 ["CALL", null, ["callee:00c58000:8"]]
+ 007f1d58 ["INT_ADD", "register:40f0:8", ["const:7f1d58:8", "const:4:8"]]
+ 007f1d58 ["CALL", null, ["callee:00c58000:8"]]
- 007f1d18 bytes ba971194
+ 007f1d58 bytes aa981194
- 007f1d68 ["INT_ADD", "register:40f0:8", ["const:7f1d68:8", "const:4:8"]]
- 007f1d68 ["CALL", null, ["callee:00470494:8"]]
+ 007f1da8 ["INT_ADD", "register:40f0:8", ["const:7f1da8:8", "const:4:8"]]
+ 007f1da8 ["CALL", null, ["callee:00470494:8"]]
- 007f1d68 bytes bbf9f197
+ 007f1da8 bytes bbf9f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b996871345ed6bf5ac07b877708c0754"></a>

### [`007f1da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1da8.md) → [`007f1de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1de8.md) FUN_007f1de8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007f1c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1c70.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`007f1cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1cb0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f1de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1da8.md#insn-007f1de8)
- 新版 `007f1e28`（命令位置の公開資料なし）

~~~diff
- 007f1de8 ["INT_ADD", "register:40f0:8", ["const:7f1de8:8", "const:4:8"]]
- 007f1de8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007f1e28 ["INT_ADD", "register:40f0:8", ["const:7f1e28:8", "const:4:8"]]
+ 007f1e28 ["CALL", null, ["callee:00c57eb0:8"]]
- 007f1de8 bytes 32971194
+ 007f1e28 bytes 22981194
~~~


<a id="compare-2962bd71b59f15d973524bdafddf1ee3"></a>

### [`007f1dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1dfc.md) → [`007f1e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1e3c.md) FUN_007f1e3c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f1e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1dfc.md#insn-007f1e20)
- 新版 `007f1e60`（命令位置の公開資料なし）

~~~diff
- 007f1e20 ["INT_ADD", "register:40f0:8", ["const:7f1e20:8", "const:4:8"]]
- 007f1e20 ["CALL", null, ["callee:0046e8a4:8"]]
+ 007f1e60 ["INT_ADD", "register:40f0:8", ["const:7f1e60:8", "const:4:8"]]
+ 007f1e60 ["CALL", null, ["callee:0046e8a4:8"]]
- 007f1e20 bytes 91f2f197
+ 007f1e60 bytes 91f2f197
~~~


<a id="compare-74f42beb5535f9feeba773c52b1f3c13"></a>

### [`007f3e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3e28.md) → [`007f3e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3e68.md) FUN_007f3e68

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a480.md)
- 新版 呼出元 1件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a880.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f3e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3e28.md#insn-007f3e38)
- 新版 `007f3e78`（命令位置の公開資料なし）

~~~diff
- 007f3e38 ["INT_ADD", "register:40f0:8", ["const:7f3e38:8", "const:4:8"]]
- 007f3e38 ["CALL", null, ["callee:00c5a880:8"]]
+ 007f3e78 ["INT_ADD", "register:40f0:8", ["const:7f3e78:8", "const:4:8"]]
+ 007f3e78 ["CALL", null, ["callee:00c5a880:8"]]
- 007f3e38 bytes 92991194
+ 007f3e78 bytes 829a1194
~~~


<a id="compare-ece52b7bb8c8fceece120f995f9e3c30"></a>

### [`007f45b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f45b8.md) → [`007f45f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f45f8.md) FUN_007f45f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`008b6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ed4.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f460c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f45b8.md#insn-007f460c) · [`007f461c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f45b8.md#insn-007f461c)
- 新版 `007f464c`（命令位置の公開資料なし） · `007f465c`（命令位置の公開資料なし）

~~~diff
- 007f460c ["INT_ADD", "register:40f0:8", ["const:7f460c:8", "const:4:8"]]
- 007f460c ["CALL", null, ["callee:008b79c8:8"]]
+ 007f464c ["INT_ADD", "register:40f0:8", ["const:7f464c:8", "const:4:8"]]
+ 007f464c ["CALL", null, ["callee:008b79c8:8"]]
- 007f460c bytes de0c0394
+ 007f464c bytes df0c0394
- 007f461c ["INT_ADD", "register:40f0:8", ["const:7f461c:8", "const:4:8"]]
- 007f461c ["CALL", null, ["callee:008b79c8:8"]]
+ 007f465c ["INT_ADD", "register:40f0:8", ["const:7f465c:8", "const:4:8"]]
+ 007f465c ["CALL", null, ["callee:008b79c8:8"]]
- 007f461c bytes da0c0394
+ 007f465c bytes db0c0394
~~~


<a id="compare-3db48607e30d1fae306fcf8d26258f65"></a>

### [`007f46b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f46b8.md) → [`007f46f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f46f8.md) FUN_007f46f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`008b6a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6a18.md) [`008b6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ed4.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md)
- 新版 呼出元 0件  · 呼出先 3件 [`008b6a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6a5c.md) [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f46d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f46b8.md#insn-007f46d4) · [`007f46e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f46b8.md#insn-007f46e4) · [`007f4710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f46b8.md#insn-007f4710)
- 新版 `007f4714`（命令位置の公開資料なし） · `007f4724`（命令位置の公開資料なし） · `007f4750`（命令位置の公開資料なし）

~~~diff
- 007f46d4 ["INT_ADD", "register:40f0:8", ["const:7f46d4:8", "const:4:8"]]
- 007f46d4 ["CALL", null, ["callee:008b79c8:8"]]
+ 007f4714 ["INT_ADD", "register:40f0:8", ["const:7f4714:8", "const:4:8"]]
+ 007f4714 ["CALL", null, ["callee:008b79c8:8"]]
- 007f46d4 bytes ac0c0394
+ 007f4714 bytes ad0c0394
- 007f46e4 ["INT_ADD", "register:40f0:8", ["const:7f46e4:8", "const:4:8"]]
- 007f46e4 ["CALL", null, ["callee:008b79c8:8"]]
+ 007f4724 ["INT_ADD", "register:40f0:8", ["const:7f4724:8", "const:4:8"]]
+ 007f4724 ["CALL", null, ["callee:008b79c8:8"]]
- 007f46e4 bytes a80c0394
+ 007f4724 bytes a90c0394
- 007f4710 ["INT_ADD", "register:40f0:8", ["const:7f4710:8", "const:4:8"]]
- 007f4710 ["CALL", null, ["callee:008b6f18:8"]]
+ 007f4750 ["INT_ADD", "register:40f0:8", ["const:7f4750:8", "const:4:8"]]
+ 007f4750 ["CALL", null, ["callee:008b6f18:8"]]
- 007f4710 bytes f1090394
+ 007f4750 bytes f2090394
~~~


<a id="compare-57697d812ca2e77a912d4756ec8b6600"></a>

### [`007f47a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f47a0.md) → [`007f47e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f47e0.md) FUN_007f47e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`008b6d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6d58.md) [`008b6ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ecc.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md) [`008b924c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b924c.md)
- 新版 呼出元 0件  · 呼出先 4件 [`008b6d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6d9c.md) [`008b6f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f10.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md) [`008b9290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f47e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f47a0.md#insn-007f47e4) · [`007f47f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f47a0.md#insn-007f47f4) · [`007f4800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f47a0.md#insn-007f4800)
- 新版 `007f4824`（命令位置の公開資料なし） · `007f4834`（命令位置の公開資料なし） · `007f4840`（命令位置の公開資料なし）

~~~diff
- 007f47e4 ["INT_ADD", "register:40f0:8", ["const:7f47e4:8", "const:4:8"]]
- 007f47e4 ["CALL", null, ["callee:008b79c8:8"]]
+ 007f4824 ["INT_ADD", "register:40f0:8", ["const:7f4824:8", "const:4:8"]]
+ 007f4824 ["CALL", null, ["callee:008b79c8:8"]]
- 007f47e4 bytes 680c0394
+ 007f4824 bytes 690c0394
- 007f47f4 ["INT_ADD", "register:40f0:8", ["const:7f47f4:8", "const:4:8"]]
- 007f47f4 ["CALL", null, ["callee:008b79c8:8"]]
+ 007f4834 ["INT_ADD", "register:40f0:8", ["const:7f4834:8", "const:4:8"]]
+ 007f4834 ["CALL", null, ["callee:008b79c8:8"]]
- 007f47f4 bytes 640c0394
+ 007f4834 bytes 650c0394
- 007f4800 ["INT_ADD", "register:40f0:8", ["const:7f4800:8", "const:4:8"]]
- 007f4800 ["CALL", null, ["callee:008b9290:8"]]
+ 007f4840 ["INT_ADD", "register:40f0:8", ["const:7f4840:8", "const:4:8"]]
+ 007f4840 ["CALL", null, ["callee:008b9290:8"]]
- 007f4800 bytes 93120394
+ 007f4840 bytes 94120394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6ddf955fd557e46a05ed6c02d0b9071"></a>

### [`007f72f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f72f8.md) → [`007f7338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7338.md) FUN_007f7338

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`008b6d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6d58.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md)
- 新版 呼出元 0件  · 呼出先 2件 [`008b6d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6d9c.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f7310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f72f8.md#insn-007f7310)
- 新版 `007f7350`（命令位置の公開資料なし）

~~~diff
- 007f7310 ["INT_ADD", "register:40f0:8", ["const:7f7310:8", "const:4:8"]]
- 007f7310 ["CALL", null, ["callee:008b79c8:8"]]
+ 007f7350 ["INT_ADD", "register:40f0:8", ["const:7f7350:8", "const:4:8"]]
+ 007f7350 ["CALL", null, ["callee:008b79c8:8"]]
- 007f7310 bytes 9d010394
+ 007f7350 bytes 9e010394
~~~


<a id="compare-f332265afb8e8c0e0752c0a1a226044a"></a>

### [`007f923c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f923c.md) → [`007f927c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f927c.md) FUN_007f927c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 7件 [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00664780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664780.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b924c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b924c.md) [`008b9254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9254.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`006647c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006647c0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9290.md) [`008b9298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9298.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f9270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f923c.md#insn-007f9270) · [`007f9280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f923c.md#insn-007f9280) · [`007f9290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f923c.md#insn-007f9290)
- 新版 `007f92b0`（命令位置の公開資料なし） · `007f92c0`（命令位置の公開資料なし） · `007f92d0`（命令位置の公開資料なし）

~~~diff
- 007f9270 ["INT_ADD", "register:40f0:8", ["const:7f9270:8", "const:4:8"]]
- 007f9270 ["CALL", null, ["callee:008b9290:8"]]
+ 007f92b0 ["INT_ADD", "register:40f0:8", ["const:7f92b0:8", "const:4:8"]]
+ 007f92b0 ["CALL", null, ["callee:008b9290:8"]]
- 007f9270 bytes f7ff0294
+ 007f92b0 bytes f8ff0294
- 007f9280 ["INT_ADD", "register:40f0:8", ["const:7f9280:8", "const:4:8"]]
- 007f9280 ["CALL", null, ["callee:008b9290:8"]]
+ 007f92c0 ["INT_ADD", "register:40f0:8", ["const:7f92c0:8", "const:4:8"]]
+ 007f92c0 ["CALL", null, ["callee:008b9290:8"]]
- 007f9280 bytes f3ff0294
+ 007f92c0 bytes f4ff0294
- 007f9290 ["INT_ADD", "register:40f0:8", ["const:7f9290:8", "const:4:8"]]
- 007f9290 ["CALL", null, ["callee:008b9298:8"]]
+ 007f92d0 ["INT_ADD", "register:40f0:8", ["const:7f92d0:8", "const:4:8"]]
+ 007f92d0 ["CALL", null, ["callee:008b9298:8"]]
- 007f9290 bytes f1ff0294
+ 007f92d0 bytes f2ff0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-287db6bc766964ad64aa86100facaa67"></a>

### [`007f95a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f95a0.md) → [`007f95e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f95e0.md) FUN_007f95e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`009e22c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e22c8.md) [`009e385c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e385c.md) [`009e38e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e38e4.md) [`009e539c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e5/009e539c.md) [`00a1a508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a508.md)
- 新版 呼出元 0件  · 呼出先 5件 [`009e2464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2464.md) [`009e39f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e39f8.md) [`009e3a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e3a80.md) [`009e5538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e5/009e5538.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f95cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f95a0.md#insn-007f95cc) · [`007f95dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f95a0.md#insn-007f95dc) · [`007f95ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f95a0.md#insn-007f95ec)
- 新版 `007f960c`（命令位置の公開資料なし） · `007f961c`（命令位置の公開資料なし） · `007f962c`（命令位置の公開資料なし）

~~~diff
- 007f95cc ["INT_ADD", "register:40f0:8", ["const:7f95cc:8", "const:4:8"]]
- 007f95cc ["CALL", null, ["callee:009e2464:8"]]
+ 007f960c ["INT_ADD", "register:40f0:8", ["const:7f960c:8", "const:4:8"]]
+ 007f960c ["CALL", null, ["callee:009e2464:8"]]
- 007f95cc bytes 3fa30794
+ 007f960c bytes 96a30794
- 007f95dc ["INT_ADD", "register:40f0:8", ["const:7f95dc:8", "const:4:8"]]
- 007f95dc ["CALL", null, ["callee:009e3a80:8"]]
+ 007f961c ["INT_ADD", "register:40f0:8", ["const:7f961c:8", "const:4:8"]]
+ 007f961c ["CALL", null, ["callee:009e3a80:8"]]
- 007f95dc bytes c2a80794
+ 007f961c bytes 19a90794
- 007f95ec ["INT_ADD", "register:40f0:8", ["const:7f95ec:8", "const:4:8"]]
- 007f95ec ["CALL", null, ["callee:009e39f8:8"]]
+ 007f962c ["INT_ADD", "register:40f0:8", ["const:7f962c:8", "const:4:8"]]
+ 007f962c ["CALL", null, ["callee:009e39f8:8"]]
- 007f95ec bytes 9ca80794
+ 007f962c bytes f3a80794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8889318cbe0eea9c5dd1dd13cb629b0"></a>

### [`007f9780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9780.md) → [`007f97c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f97c0.md) FUN_007f97c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f979c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9780.md#insn-007f979c) · [`007f97bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9780.md#insn-007f97bc)
- 新版 `007f97dc`（命令位置の公開資料なし） · `007f97fc`（命令位置の公開資料なし）

~~~diff
- 007f979c ["INT_ADD", "register:40f0:8", ["const:7f979c:8", "const:4:8"]]
- 007f979c ["CALL", null, ["callee:00c53d00:8"]]
+ 007f97dc ["INT_ADD", "register:40f0:8", ["const:7f97dc:8", "const:4:8"]]
+ 007f97dc ["CALL", null, ["callee:00c53d00:8"]]
- 007f979c bytes 51681194
+ 007f97dc bytes 49691194
- 007f97bc ["COPY", "register:0:8", ["register:4040:8"]]
- 007f97bc ["INT_ADD", "register:40f0:8", ["const:7f97bc:8", "const:4:8"]]
- 007f97bc ["CALLIND", null, ["register:0:8"]]
+ 007f97fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 007f97fc ["INT_ADD", "register:40f0:8", ["const:7f97fc:8", "const:4:8"]]
+ 007f97fc ["CALLIND", null, ["register:0:8"]]
- 007f97bc bytes 00013fd6
+ 007f97fc bytes 00013fd6
~~~


<a id="compare-a8c336b1eee1eaa9039ad1448ec08c48"></a>

### [`007f97d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f97d0.md) → [`007f9810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9810.md) FUN_007f9810

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f97f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f97d0.md#insn-007f97f0) · [`007f9804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f97d0.md#insn-007f9804) · [`007f980c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f97d0.md#insn-007f980c)
- 新版 `007f9830`（命令位置の公開資料なし） · `007f9844`（命令位置の公開資料なし） · `007f984c`（命令位置の公開資料なし）

~~~diff
- 007f97f0 ["INT_ADD", "register:40f0:8", ["const:7f97f0:8", "const:4:8"]]
- 007f97f0 ["CALL", null, ["callee:00c53d00:8"]]
+ 007f9830 ["INT_ADD", "register:40f0:8", ["const:7f9830:8", "const:4:8"]]
+ 007f9830 ["CALL", null, ["callee:00c53d00:8"]]
- 007f97f0 bytes 3c681194
+ 007f9830 bytes 34691194
- 007f9804 ["COPY", "register:0:8", ["register:4040:8"]]
- 007f9804 ["INT_ADD", "register:40f0:8", ["const:7f9804:8", "const:4:8"]]
- 007f9804 ["CALLIND", null, ["register:0:8"]]
+ 007f9844 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007f9844 ["INT_ADD", "register:40f0:8", ["const:7f9844:8", "const:4:8"]]
+ 007f9844 ["CALLIND", null, ["register:0:8"]]
- 007f9804 bytes 00013fd6
+ 007f9844 bytes 00013fd6
- 007f980c ["INT_ADD", "register:40f0:8", ["const:7f980c:8", "const:4:8"]]
- 007f980c ["CALL", null, ["callee:00c57e80:8"]]
+ 007f984c ["INT_ADD", "register:40f0:8", ["const:7f984c:8", "const:4:8"]]
+ 007f984c ["CALL", null, ["callee:00c57e80:8"]]
- 007f980c bytes 9d781194
+ 007f984c bytes 8d791194
~~~


<a id="compare-07b8cf032fb6590126e69254b463477f"></a>

### [`007f9820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9820.md) → [`007f9860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9860.md) FUN_007f9860

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`007f9b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9b90.md) [`007f9e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9e44.md) [`009df900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df900.md) [`009e29a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e29a4.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`007f9bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9bd0.md) [`007f9e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9e84.md) [`009dfa9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009dfa9c.md) [`009e2b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f9868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9820.md#insn-007f9868) · [`007f9880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9820.md#insn-007f9880) · [`007f98f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9820.md#insn-007f98f0)
- 新版 `007f98a8`（命令位置の公開資料なし） · `007f98c0`（命令位置の公開資料なし） · `007f9930`（命令位置の公開資料なし）

~~~diff
- 007f9868 ["INT_ADD", "register:40f0:8", ["const:7f9868:8", "const:4:8"]]
- 007f9868 ["CALL", null, ["callee:009e3a1c:8"]]
+ 007f98a8 ["INT_ADD", "register:40f0:8", ["const:7f98a8:8", "const:4:8"]]
+ 007f98a8 ["CALL", null, ["callee:009e3a1c:8"]]
- 007f9868 bytes 06a80794
+ 007f98a8 bytes 5da80794
- 007f9880 ["INT_ADD", "register:40f0:8", ["const:7f9880:8", "const:4:8"]]
- 007f9880 ["CALL", null, ["callee:009e2f94:8"]]
+ 007f98c0 ["INT_ADD", "register:40f0:8", ["const:7f98c0:8", "const:4:8"]]
+ 007f98c0 ["CALL", null, ["callee:009e2f94:8"]]
- 007f9880 bytes 5ea50794
+ 007f98c0 bytes b5a50794
- 007f98f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 007f98f0 ["INT_ADD", "register:40f0:8", ["const:7f98f0:8", "const:4:8"]]
- 007f98f0 ["CALLIND", null, ["register:0:8"]]
+ 007f9930 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007f9930 ["INT_ADD", "register:40f0:8", ["const:7f9930:8", "const:4:8"]]
+ 007f9930 ["CALLIND", null, ["register:0:8"]]
- 007f98f0 bytes 00013fd6
+ 007f9930 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c106d034d0a83bd166d9e6e82f559a3"></a>

### [`007f9b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9b90.md) → [`007f9bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9bd0.md) FUN_007f9bd0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007f9820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9820.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`007f9e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9e44.md) [`007f9e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9e58.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`007f9860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9860.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`007f9e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9e84.md) [`007f9e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9e98.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f9c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9b90.md#insn-007f9c8c) · [`007f9cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9b90.md#insn-007f9cdc) · [`007f9cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9b90.md#insn-007f9cf0)
- 新版 `007f9ccc`（命令位置の公開資料なし） · `007f9d1c`（命令位置の公開資料なし） · `007f9d30`（命令位置の公開資料なし）

~~~diff
- 007f9c8c ["INT_ADD", "register:40f0:8", ["const:7f9c8c:8", "const:4:8"]]
- 007f9c8c ["CALL", null, ["callee:00c57e90:8"]]
+ 007f9ccc ["INT_ADD", "register:40f0:8", ["const:7f9ccc:8", "const:4:8"]]
+ 007f9ccc ["CALL", null, ["callee:00c57e90:8"]]
- 007f9c8c bytes 81771194
+ 007f9ccc bytes 71781194
- 007f9cdc ["INT_ADD", "register:40f0:8", ["const:7f9cdc:8", "const:4:8"]]
- 007f9cdc ["CALL", null, ["callee:007f9e98:8"]]
+ 007f9d1c ["INT_ADD", "register:40f0:8", ["const:7f9d1c:8", "const:4:8"]]
+ 007f9d1c ["CALL", null, ["callee:007f9e98:8"]]
- 007f9cdc bytes 5f000094
+ 007f9d1c bytes 5f000094
- 007f9cf0 ["INT_ADD", "register:40f0:8", ["const:7f9cf0:8", "const:4:8"]]
- 007f9cf0 ["CALL", null, ["callee:00c58000:8"]]
+ 007f9d30 ["INT_ADD", "register:40f0:8", ["const:7f9d30:8", "const:4:8"]]
+ 007f9d30 ["CALL", null, ["callee:00c58000:8"]]
- 007f9cf0 bytes c4771194
+ 007f9d30 bytes b4781194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34c641801a6723abfd03681874d839ad"></a>

### [`007f9e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9e58.md) → [`007f9e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9e98.md) FUN_007f9e98

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007f9b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9b90.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`007f9bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f9/007f9bd0.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007f9edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9e58.md#insn-007f9edc) · [`007f9f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9e58.md#insn-007f9f40) · [`007f9f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9e58.md#insn-007f9f8c)
- 新版 `007f9f1c`（命令位置の公開資料なし） · `007f9f80`（命令位置の公開資料なし） · `007f9fcc`（命令位置の公開資料なし）

~~~diff
- 007f9edc ["INT_ADD", "register:40f0:8", ["const:7f9edc:8", "const:4:8"]]
- 007f9edc ["CALL", null, ["callee:00c57f40:8"]]
+ 007f9f1c ["INT_ADD", "register:40f0:8", ["const:7f9f1c:8", "const:4:8"]]
+ 007f9f1c ["CALL", null, ["callee:00c57f40:8"]]
- 007f9edc bytes 19771194
+ 007f9f1c bytes 09781194
- 007f9f40 ["INT_ADD", "register:40f0:8", ["const:7f9f40:8", "const:4:8"]]
- 007f9f40 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f9f80 ["INT_ADD", "register:40f0:8", ["const:7f9f80:8", "const:4:8"]]
+ 007f9f80 ["CALL", null, ["callee:00c57e90:8"]]
- 007f9f40 bytes d4761194
+ 007f9f80 bytes c4771194
- 007f9f8c ["INT_ADD", "register:40f0:8", ["const:7f9f8c:8", "const:4:8"]]
- 007f9f8c ["CALL", null, ["callee:00c57eb0:8"]]
+ 007f9fcc ["INT_ADD", "register:40f0:8", ["const:7f9fcc:8", "const:4:8"]]
+ 007f9fcc ["CALL", null, ["callee:00c57eb0:8"]]
- 007f9f8c bytes c9761194
+ 007f9fcc bytes b9771194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-079673628c7d41421aa97735047665fd"></a>

### [`007fd14c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd14c.md) → [`007fd18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd18c.md) FUN_007fd18c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`008b924c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b924c.md) [`008b9254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9254.md) [`00a83390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a83/00a83390.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`008b9290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9290.md) [`008b9298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9298.md) [`00a83588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a83/00a83588.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007fd180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd14c.md#insn-007fd180) · [`007fd190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd14c.md#insn-007fd190) · [`007fd1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd14c.md#insn-007fd1c0)
- 新版 `007fd1c0`（命令位置の公開資料なし） · `007fd1d0`（命令位置の公開資料なし） · `007fd200`（命令位置の公開資料なし）

~~~diff
- 007fd180 ["INT_ADD", "register:40f0:8", ["const:7fd180:8", "const:4:8"]]
- 007fd180 ["CALL", null, ["callee:008b9290:8"]]
+ 007fd1c0 ["INT_ADD", "register:40f0:8", ["const:7fd1c0:8", "const:4:8"]]
+ 007fd1c0 ["CALL", null, ["callee:008b9290:8"]]
- 007fd180 bytes 33f00294
+ 007fd1c0 bytes 34f00294
- 007fd190 ["INT_ADD", "register:40f0:8", ["const:7fd190:8", "const:4:8"]]
- 007fd190 ["CALL", null, ["callee:008b9290:8"]]
+ 007fd1d0 ["INT_ADD", "register:40f0:8", ["const:7fd1d0:8", "const:4:8"]]
+ 007fd1d0 ["CALL", null, ["callee:008b9290:8"]]
- 007fd190 bytes 2ff00294
+ 007fd1d0 bytes 30f00294
- 007fd1c0 ["INT_ADD", "register:40f0:8", ["const:7fd1c0:8", "const:4:8"]]
- 007fd1c0 ["CALL", null, ["callee:008b9298:8"]]
+ 007fd200 ["INT_ADD", "register:40f0:8", ["const:7fd200:8", "const:4:8"]]
+ 007fd200 ["CALL", null, ["callee:008b9298:8"]]
- 007fd1c0 bytes 25f00294
+ 007fd200 bytes 26f00294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb4ae8f1e695354f938b64aedfdef142"></a>

### [`007fe76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe76c.md) → [`007fe7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe7ac.md) FUN_007fe7ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007cb5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cb/007cb5a0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`007cb5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb5e0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007fe78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe76c.md#insn-007fe78c)
- 新版 `007fe7cc`（命令位置の公開資料なし）

~~~diff
- 007fe78c ["INT_ADD", "register:40f0:8", ["const:7fe78c:8", "const:4:8"]]
- 007fe78c ["CALL", null, ["callee:00c57eb0:8"]]
+ 007fe7cc ["INT_ADD", "register:40f0:8", ["const:7fe7cc:8", "const:4:8"]]
+ 007fe7cc ["CALL", null, ["callee:00c57eb0:8"]]
- 007fe78c bytes c9641194
+ 007fe7cc bytes b9651194
~~~


<a id="compare-d2ed4b600a6b723d35fb2b38a57f878d"></a>

### [`007ff154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff154.md) → [`007ff194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff194.md) FUN_007ff194

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007c90dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c9/007c90dc.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`007c911c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c9/007c911c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007ff174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff154.md#insn-007ff174)
- 新版 `007ff1b4`（命令位置の公開資料なし）

~~~diff
- 007ff174 ["INT_ADD", "register:40f0:8", ["const:7ff174:8", "const:4:8"]]
- 007ff174 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007ff1b4 ["INT_ADD", "register:40f0:8", ["const:7ff1b4:8", "const:4:8"]]
+ 007ff1b4 ["CALL", null, ["callee:00c57eb0:8"]]
- 007ff174 bytes 4f621194
+ 007ff1b4 bytes 3f631194
~~~


<a id="compare-21656bf8fced0530ac701a7e5488428d"></a>

### [`007ffb08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffb08.md) → [`007ffb48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffb48.md) FUN_007ffb48

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007caa88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ca/007caa88.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`007caac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007caac8.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007ffb28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffb08.md#insn-007ffb28)
- 新版 `007ffb68`（命令位置の公開資料なし）

~~~diff
- 007ffb28 ["INT_ADD", "register:40f0:8", ["const:7ffb28:8", "const:4:8"]]
- 007ffb28 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007ffb68 ["INT_ADD", "register:40f0:8", ["const:7ffb68:8", "const:4:8"]]
+ 007ffb68 ["CALL", null, ["callee:00c57eb0:8"]]
- 007ffb28 bytes e25f1194
+ 007ffb68 bytes d2601194
~~~


<a id="compare-db7757d7c49d8d6510fd4baa65f0e5bf"></a>

### [`00801c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00801/00801c50.md) → [`00801c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00801/00801c90.md) FUN_00801c90

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) [`0078610c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/0078610c.md) [`0081de40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081d/0081de40.md) [`0082463c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/0082463c.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 8件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) [`0078614c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/0078614c.md) [`0081de80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081d/0081de80.md) [`0082467c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00824/0082467c.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00801ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00801/00801c50.md#insn-00801ce8) · [`00801d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00801/00801c50.md#insn-00801d1c)
- 新版 `00801d28`（命令位置の公開資料なし） · `00801d5c`（命令位置の公開資料なし）

~~~diff
- 00801ce8 ["INT_ADD", "register:40f0:8", ["const:801ce8:8", "const:4:8"]]
- 00801ce8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00801d28 ["INT_ADD", "register:40f0:8", ["const:801d28:8", "const:4:8"]]
+ 00801d28 ["CALL", null, ["callee:00c57e90:8"]]
- 00801ce8 bytes 6a571194
+ 00801d28 bytes 5a581194
- 00801d1c ["INT_ADD", "register:40f0:8", ["const:801d1c:8", "const:4:8"]]
- 00801d1c ["CALL", null, ["callee:0043bba4:8"]]
+ 00801d5c ["INT_ADD", "register:40f0:8", ["const:801d5c:8", "const:4:8"]]
+ 00801d5c ["CALL", null, ["callee:0043bba4:8"]]
- 00801d1c bytes 92e7f097
+ 00801d5c bytes 92e7f097
~~~


<a id="compare-c89723a6562858746724d575c32ec9eb"></a>

### [`00801da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00801/00801da0.md) → [`00801de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00801/00801de0.md) FUN_00801de0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0081de40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081d/0081de40.md) [`0082463c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/0082463c.md) [`00a9c4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9c/00a9c4f4.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`0081de80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081d/0081de80.md) [`0082467c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00824/0082467c.md) [`00a9c6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9c/00a9c6f0.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00801e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00801/00801da0.md#insn-00801e04) · [`00801e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00801/00801da0.md#insn-00801e40)
- 新版 `00801e44`（命令位置の公開資料なし） · `00801e80`（命令位置の公開資料なし）

~~~diff
- 00801e04 ["INT_ADD", "register:40f0:8", ["const:801e04:8", "const:4:8"]]
- 00801e04 ["CALL", null, ["callee:00c57e90:8"]]
+ 00801e44 ["INT_ADD", "register:40f0:8", ["const:801e44:8", "const:4:8"]]
+ 00801e44 ["CALL", null, ["callee:00c57e90:8"]]
- 00801e04 bytes 23571194
+ 00801e44 bytes 13581194
- 00801e40 ["INT_ADD", "register:40f0:8", ["const:801e40:8", "const:4:8"]]
- 00801e40 ["CALL", null, ["callee:0043bba4:8"]]
+ 00801e80 ["INT_ADD", "register:40f0:8", ["const:801e80:8", "const:4:8"]]
+ 00801e80 ["CALL", null, ["callee:0043bba4:8"]]
- 00801e40 bytes 49e7f097
+ 00801e80 bytes 49e7f097
~~~


<a id="compare-e97911f6fb213890d37fab5cbd5e7016"></a>

### [`008022d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/008022d0.md) → [`00802310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802310.md) FUN_00802310

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 1件 [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008022f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/008022d0.md#insn-008022f0)
- 新版 `00802330`（命令位置の公開資料なし）

~~~diff
- 008022f0 ["INT_ADD", "register:40f0:8", ["const:8022f0:8", "const:4:8"]]
- 008022f0 ["CALL", null, ["callee:00c58450:8"]]
+ 00802330 ["INT_ADD", "register:40f0:8", ["const:802330:8", "const:4:8"]]
+ 00802330 ["CALL", null, ["callee:00c58450:8"]]
- 008022f0 bytes 58571194
+ 00802330 bytes 48581194
~~~


<a id="compare-ab05980d0305afcf67a5e70354bbd375"></a>

### [`0080234c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/0080234c.md) → [`0080238c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/0080238c.md) FUN_0080238c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) [`00789da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md) [`008242f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/008242f0.md) [`0082449c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/0082449c.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 6件 [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) [`00789de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789de0.md) [`00824330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00824/00824330.md) [`008244dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00824/008244dc.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008023fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/0080234c.md#insn-008023fc) · [`00802430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/0080234c.md#insn-00802430)
- 新版 `0080243c`（命令位置の公開資料なし） · `00802470`（命令位置の公開資料なし）

~~~diff
- 008023fc ["INT_ADD", "register:40f0:8", ["const:8023fc:8", "const:4:8"]]
- 008023fc ["CALL", null, ["callee:00c57e90:8"]]
+ 0080243c ["INT_ADD", "register:40f0:8", ["const:80243c:8", "const:4:8"]]
+ 0080243c ["CALL", null, ["callee:00c57e90:8"]]
- 008023fc bytes a5551194
+ 0080243c bytes 95561194
- 00802430 ["INT_ADD", "register:40f0:8", ["const:802430:8", "const:4:8"]]
- 00802430 ["CALL", null, ["callee:0043bba4:8"]]
+ 00802470 ["INT_ADD", "register:40f0:8", ["const:802470:8", "const:4:8"]]
+ 00802470 ["CALL", null, ["callee:0043bba4:8"]]
- 00802430 bytes cde5f097
+ 00802470 bytes cde5f097
~~~


<a id="compare-530179ab04f2466fe824592ed08b4b6b"></a>

### [`0080246c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/0080246c.md) → [`008024ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008024ac.md) FUN_008024ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0060e084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060e084.md) [`0069a4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a4c4.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) [`00ab0300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab0/00ab0300.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)
- 新版 呼出元 5件 [`0060e0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060e/0060e0c4.md) [`0069a504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069a/0069a504.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) [`00ab04fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab0/00ab04fc.md) · 呼出先 1件 [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080248c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/0080246c.md#insn-0080248c)
- 新版 `008024cc`（命令位置の公開資料なし）

~~~diff
- 0080248c ["INT_ADD", "register:40f0:8", ["const:80248c:8", "const:4:8"]]
- 0080248c ["CALL", null, ["callee:00c58450:8"]]
+ 008024cc ["INT_ADD", "register:40f0:8", ["const:8024cc:8", "const:4:8"]]
+ 008024cc ["CALL", null, ["callee:00c58450:8"]]
- 0080248c bytes f1561194
+ 008024cc bytes e1571194
~~~


<a id="compare-d938b02bae4c2c39608f16edba038d7d"></a>

### [`008024b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/008024b0.md) → [`008024f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008024f0.md) FUN_008024f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) · 呼出先 1件 [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008024d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/008024b0.md#insn-008024d0)
- 新版 `00802510`（命令位置の公開資料なし）

~~~diff
- 008024d0 ["INT_ADD", "register:40f0:8", ["const:8024d0:8", "const:4:8"]]
- 008024d0 ["CALL", null, ["callee:00c58450:8"]]
+ 00802510 ["INT_ADD", "register:40f0:8", ["const:802510:8", "const:4:8"]]
+ 00802510 ["CALL", null, ["callee:00c58450:8"]]
- 008024d0 bytes e0561194
+ 00802510 bytes d0571194
~~~


<a id="compare-e2104e9600e607d1c95704342a4b3e8c"></a>

### [`008024f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/008024f4.md) → [`00802534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802534.md) FUN_00802534

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00affc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aff/00affc2c.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00b00054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b00054.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080258c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/008024f4.md#insn-0080258c) · [`008025c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/008024f4.md#insn-008025c0)
- 新版 `008025cc`（命令位置の公開資料なし） · `00802600`（命令位置の公開資料なし）

~~~diff
- 0080258c ["INT_ADD", "register:40f0:8", ["const:80258c:8", "const:4:8"]]
- 0080258c ["CALL", null, ["callee:00c57e90:8"]]
+ 008025cc ["INT_ADD", "register:40f0:8", ["const:8025cc:8", "const:4:8"]]
+ 008025cc ["CALL", null, ["callee:00c57e90:8"]]
- 0080258c bytes 41551194
+ 008025cc bytes 31561194
- 008025c0 ["INT_ADD", "register:40f0:8", ["const:8025c0:8", "const:4:8"]]
- 008025c0 ["CALL", null, ["callee:0043bba4:8"]]
+ 00802600 ["INT_ADD", "register:40f0:8", ["const:802600:8", "const:4:8"]]
+ 00802600 ["CALL", null, ["callee:0043bba4:8"]]
- 008025c0 bytes 69e5f097
+ 00802600 bytes 69e5f097
~~~


<a id="compare-73561f5ecaebae7329d4ad0158f08bd4"></a>

### [`008025f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/008025f0.md) → [`00802630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802630.md) FUN_00802630

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`006158d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/006158d0.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) [`0078597c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078597c.md) [`007874d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007874d8.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)
- 新版 呼出元 9件 [`00615910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615910.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) [`007859bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/007859bc.md) [`00787518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/00787518.md) · 呼出先 1件 [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00802610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/008025f0.md#insn-00802610)
- 新版 `00802650`（命令位置の公開資料なし）

~~~diff
- 00802610 ["INT_ADD", "register:40f0:8", ["const:802610:8", "const:4:8"]]
- 00802610 ["CALL", null, ["callee:00c58450:8"]]
+ 00802650 ["INT_ADD", "register:40f0:8", ["const:802650:8", "const:4:8"]]
+ 00802650 ["CALL", null, ["callee:00c58450:8"]]
- 00802610 bytes 90561194
+ 00802650 bytes 80571194
~~~


<a id="compare-58d2cdce064c37d61e4cba69f3c013c4"></a>

### [`00802634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802634.md) → [`00802674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802674.md) FUN_00802674

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00a65bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65bf4.md) [`00a662bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a662bc.md) [`00a66aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a66aa0.md) [`00a66ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a66ec4.md) [`00a67338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a67338.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)
- 新版 呼出元 6件 [`00a65dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a65/00a65dec.md) [`00a664b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a66/00a664b4.md) [`00a66c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a66/00a66c98.md) [`00a670bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a670bc.md) [`00a67530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a67530.md) · 呼出先 1件 [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00802654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802634.md#insn-00802654)
- 新版 `00802694`（命令位置の公開資料なし）

~~~diff
- 00802654 ["INT_ADD", "register:40f0:8", ["const:802654:8", "const:4:8"]]
- 00802654 ["CALL", null, ["callee:00c58450:8"]]
+ 00802694 ["INT_ADD", "register:40f0:8", ["const:802694:8", "const:4:8"]]
+ 00802694 ["CALL", null, ["callee:00c58450:8"]]
- 00802654 bytes 7f561194
+ 00802694 bytes 6f571194
~~~


<a id="compare-4e602c3eb13ea015a4e75a8db270c965"></a>

### [`00802cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802cac.md) → [`00802cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802cec.md) FUN_00802cec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`00802d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802d0c.md) [`00a06590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06590.md) · 呼出先 5件 [`0067670c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067670c.md) [`007bbd08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbd08.md) [`00802678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00a3280c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a3280c.md)
- 新版 呼出元 3件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00802d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d4c.md) [`00a0672c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a0672c.md) · 呼出先 5件 [`0067674c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/0067674c.md) [`007bbd48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbd48.md) [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00a32a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32a04.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00802cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802cac.md#insn-00802cb4) · [`00802cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802cac.md#insn-00802cc4) · [`00802ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802cac.md#insn-00802ccc)
- 新版 `00802cf4`（命令位置の公開資料なし） · `00802d04`（命令位置の公開資料なし） · `00802d0c`（命令位置の公開資料なし）

~~~diff
- 00802cb4 ["INT_ADD", "register:40f0:8", ["const:802cb4:8", "const:4:8"]]
- 00802cb4 ["CALL", null, ["callee:008514f8:8"]]
+ 00802cf4 ["INT_ADD", "register:40f0:8", ["const:802cf4:8", "const:4:8"]]
+ 00802cf4 ["CALL", null, ["callee:008514f8:8"]]
- 00802cb4 bytes 013a0194
+ 00802cf4 bytes 013a0194
- 00802cc4 ["INT_ADD", "register:40f0:8", ["const:802cc4:8", "const:4:8"]]
- 00802cc4 ["CALL", null, ["callee:0067674c:8"]]
+ 00802d04 ["INT_ADD", "register:40f0:8", ["const:802d04:8", "const:4:8"]]
+ 00802d04 ["CALL", null, ["callee:0067674c:8"]]
- 00802cc4 bytes 92cef997
+ 00802d04 bytes 92cef997
- 00802ccc ["INT_ADD", "register:40f0:8", ["const:802ccc:8", "const:4:8"]]
- 00802ccc ["CALL", null, ["callee:008514f8:8"]]
+ 00802d0c ["INT_ADD", "register:40f0:8", ["const:802d0c:8", "const:4:8"]]
+ 00802d0c ["CALL", null, ["callee:008514f8:8"]]
- 00802ccc bytes fb390194
+ 00802d0c bytes fb390194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3b219601b2d195948e6865f3d9ff750"></a>

### [`00802d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802d0c.md) → [`00802d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d4c.md) FUN_00802d4c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a06590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06590.md) · 呼出先 3件 [`008001ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008001ac.md) [`00802cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802cac.md) [`00802d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802d38.md)
- 新版 呼出元 1件 [`00a0672c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a0672c.md) · 呼出先 3件 [`008001ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001ec.md) [`00802cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802cec.md) [`00802d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d78.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00802d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802d0c.md#insn-00802d18) · [`00802d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802d0c.md#insn-00802d20)
- 新版 `00802d58`（命令位置の公開資料なし） · `00802d60`（命令位置の公開資料なし）

~~~diff
- 00802d18 ["INT_ADD", "register:40f0:8", ["const:802d18:8", "const:4:8"]]
- 00802d18 ["CALL", null, ["callee:00802cec:8"]]
+ 00802d58 ["INT_ADD", "register:40f0:8", ["const:802d58:8", "const:4:8"]]
+ 00802d58 ["CALL", null, ["callee:00802cec:8"]]
- 00802d18 bytes e5ffff97
+ 00802d58 bytes e5ffff97
- 00802d20 ["INT_ADD", "register:40f0:8", ["const:802d20:8", "const:4:8"]]
- 00802d20 ["CALL", null, ["callee:00802d78:8"]]
+ 00802d60 ["INT_ADD", "register:40f0:8", ["const:802d60:8", "const:4:8"]]
+ 00802d60 ["CALL", null, ["callee:00802d78:8"]]
- 00802d20 bytes 06000094
+ 00802d60 bytes 06000094
~~~


<a id="compare-684ef8f1e19cbc61bc472aa32049387d"></a>

### [`00803d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00803/00803d08.md) → [`00803d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00803/00803d48.md) FUN_00803d48

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`005e30d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e3/005e30d4.md) [`007b09d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b09d8.md) [`007bbddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbddc.md) [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 1件 [`00802678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md)
- 新版 呼出元 7件 [`005e3114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e3/005e3114.md) [`007b0a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0a18.md) [`007bbe1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbe1c.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 1件 [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00803d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00803/00803d08.md#insn-00803d14)
- 新版 `00803d54`（命令位置の公開資料なし）

~~~diff
- 00803d14 ["INT_ADD", "register:40f0:8", ["const:803d14:8", "const:4:8"]]
- 00803d14 ["CALL", null, ["callee:008026b8:8"]]
+ 00803d54 ["INT_ADD", "register:40f0:8", ["const:803d54:8", "const:4:8"]]
+ 00803d54 ["CALL", null, ["callee:008026b8:8"]]
- 00803d14 bytes 59faff97
+ 00803d54 bytes 59faff97
~~~


<a id="compare-a652f4d7481eaa6d5d70fa7ab12b1e8c"></a>

### [`00807d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00807/00807d20.md) → [`00807d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00807/00807d60.md) FUN_00807d60

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`0080b2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b2e4.md)
- 新版 呼出元 1件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`0080b324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b324.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00807d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00807/00807d20.md#insn-00807d3c) · [`00807d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00807/00807d20.md#insn-00807d54)
- 新版 `00807d7c`（命令位置の公開資料なし） · `00807d94`（命令位置の公開資料なし）

~~~diff
- 00807d3c ["INT_ADD", "register:40f0:8", ["const:807d3c:8", "const:4:8"]]
- 00807d3c ["CALL", null, ["callee:005c179c:8"]]
+ 00807d7c ["INT_ADD", "register:40f0:8", ["const:807d7c:8", "const:4:8"]]
+ 00807d7c ["CALL", null, ["callee:005c179c:8"]]
- 00807d3c bytes 88e6f697
+ 00807d7c bytes 88e6f697
- 00807d54 ["INT_ADD", "register:40f0:8", ["const:807d54:8", "const:4:8"]]
- 00807d54 ["CALL", null, ["callee:0080b324:8"]]
+ 00807d94 ["INT_ADD", "register:40f0:8", ["const:807d94:8", "const:4:8"]]
+ 00807d94 ["CALL", null, ["callee:0080b324:8"]]
- 00807d54 bytes 640d0094
+ 00807d94 bytes 640d0094
~~~


<a id="compare-2716bdfc94ee606a2ce9ad4745a34318"></a>

### [`0080aebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080a/0080aebc.md) → [`0080aefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080a/0080aefc.md) FUN_0080aefc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a878d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a87/00a878d8.md) · 呼出先 1件 [`0080b2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b2e4.md)
- 新版 呼出元 1件 [`00a87ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a87/00a87ad0.md) · 呼出先 1件 [`0080b324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b324.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080aed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080a/0080aebc.md#insn-0080aed4)
- 新版 `0080af14`（命令位置の公開資料なし）

~~~diff
- 0080aed4 ["INT_ADD", "register:40f0:8", ["const:80aed4:8", "const:4:8"]]
- 0080aed4 ["CALL", null, ["callee:0080b324:8"]]
+ 0080af14 ["INT_ADD", "register:40f0:8", ["const:80af14:8", "const:4:8"]]
+ 0080af14 ["CALL", null, ["callee:0080b324:8"]]
- 0080aed4 bytes 04010094
+ 0080af14 bytes 04010094
~~~


<a id="compare-b7e024f8a58571e1105e1812e02b0e53"></a>

### [`0080aeec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080a/0080aeec.md) → [`0080af2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080a/0080af2c.md) FUN_0080af2c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007c7938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7938.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`007c7978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7978.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080af84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080a/0080aeec.md#insn-0080af84) · [`0080afd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080a/0080aeec.md#insn-0080afd0)
- 新版 `0080afc4`（命令位置の公開資料なし） · `0080b010`（命令位置の公開資料なし）

~~~diff
- 0080af84 ["INT_ADD", "register:40f0:8", ["const:80af84:8", "const:4:8"]]
- 0080af84 ["CALL", null, ["callee:00c57e90:8"]]
+ 0080afc4 ["INT_ADD", "register:40f0:8", ["const:80afc4:8", "const:4:8"]]
+ 0080afc4 ["CALL", null, ["callee:00c57e90:8"]]
- 0080af84 bytes c3321194
+ 0080afc4 bytes b3331194
- 0080afd0 ["INT_ADD", "register:40f0:8", ["const:80afd0:8", "const:4:8"]]
- 0080afd0 ["CALL", null, ["callee:0043bba4:8"]]
+ 0080b010 ["INT_ADD", "register:40f0:8", ["const:80b010:8", "const:4:8"]]
+ 0080b010 ["CALL", null, ["callee:0043bba4:8"]]
- 0080afd0 bytes e5c2f097
+ 0080b010 bytes e5c2f097
~~~


<a id="compare-bb6a74e3b1cdf6fafd119878d0c2dc48"></a>

### [`0080b000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b000.md) → [`0080b040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b040.md) FUN_0080b040

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`00937924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937924.md) [`00937f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937f14.md) [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 4件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00937ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00937/00937ac0.md) [`009380b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00938/009380b0.md) [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080b098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b000.md#insn-0080b098) · [`0080b0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b000.md#insn-0080b0d4)
- 新版 `0080b0d8`（命令位置の公開資料なし） · `0080b114`（命令位置の公開資料なし）

~~~diff
- 0080b098 ["INT_ADD", "register:40f0:8", ["const:80b098:8", "const:4:8"]]
- 0080b098 ["CALL", null, ["callee:00c57e90:8"]]
+ 0080b0d8 ["INT_ADD", "register:40f0:8", ["const:80b0d8:8", "const:4:8"]]
+ 0080b0d8 ["CALL", null, ["callee:00c57e90:8"]]
- 0080b098 bytes 7e321194
+ 0080b0d8 bytes 6e331194
- 0080b0d4 ["INT_ADD", "register:40f0:8", ["const:80b0d4:8", "const:4:8"]]
- 0080b0d4 ["CALL", null, ["callee:0043bba4:8"]]
+ 0080b114 ["INT_ADD", "register:40f0:8", ["const:80b114:8", "const:4:8"]]
+ 0080b114 ["CALL", null, ["callee:0043bba4:8"]]
- 0080b0d4 bytes a4c2f097
+ 0080b114 bytes a4c2f097
~~~


<a id="compare-d48f0690dc8a4009b23321ab34334431"></a>

### [`0080b104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b104.md) → [`0080b144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b144.md) FUN_0080b144

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00480198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480198.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`004801d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004801d8.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080b130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b104.md#insn-0080b130) · [`0080b148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b104.md#insn-0080b148) · [`0080b16c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b104.md#insn-0080b16c)
- 新版 `0080b170`（命令位置の公開資料なし） · `0080b188`（命令位置の公開資料なし） · `0080b1ac`（命令位置の公開資料なし）

~~~diff
- 0080b130 ["INT_ADD", "register:40f0:8", ["const:80b130:8", "const:4:8"]]
- 0080b130 ["CALL", null, ["callee:004801d8:8"]]
+ 0080b170 ["INT_ADD", "register:40f0:8", ["const:80b170:8", "const:4:8"]]
+ 0080b170 ["CALL", null, ["callee:004801d8:8"]]
- 0080b130 bytes 1ad4f197
+ 0080b170 bytes 1ad4f197
- 0080b148 ["INT_ADD", "register:40f0:8", ["const:80b148:8", "const:4:8"]]
- 0080b148 ["CALL", null, ["callee:005c179c:8"]]
+ 0080b188 ["INT_ADD", "register:40f0:8", ["const:80b188:8", "const:4:8"]]
+ 0080b188 ["CALL", null, ["callee:005c179c:8"]]
- 0080b148 bytes 85d9f697
+ 0080b188 bytes 85d9f697
- 0080b16c ["INT_ADD", "register:40f0:8", ["const:80b16c:8", "const:4:8"]]
- 0080b16c ["CALL", null, ["callee:0043bba4:8"]]
+ 0080b1ac ["INT_ADD", "register:40f0:8", ["const:80b1ac:8", "const:4:8"]]
+ 0080b1ac ["CALL", null, ["callee:0043bba4:8"]]
- 0080b16c bytes 7ec2f097
+ 0080b1ac bytes 7ec2f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2958d6a162ed5fe006b8d058c218d90"></a>

### [`0080b248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b248.md) → [`0080b288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b288.md) FUN_0080b288

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 1件 [`00480ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ba8.md)
- 新版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 1件 [`00480be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080b26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b248.md#insn-0080b26c) · [`0080b2a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b248.md#insn-0080b2a4) · [`0080b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b248.md#insn-0080b2b0)
- 新版 `0080b2ac`（命令位置の公開資料なし） · `0080b2e4`（命令位置の公開資料なし） · `0080b2f0`（命令位置の公開資料なし）

~~~diff
- 0080b26c ["INT_ADD", "register:40f0:8", ["const:80b26c:8", "const:4:8"]]
- 0080b26c ["CALL", null, ["callee:00480be8:8"]]
+ 0080b2ac ["INT_ADD", "register:40f0:8", ["const:80b2ac:8", "const:4:8"]]
+ 0080b2ac ["CALL", null, ["callee:00480be8:8"]]
- 0080b26c bytes 4fd6f197
+ 0080b2ac bytes 4fd6f197
- 0080b2a4 ["INT_ADD", "register:40f0:8", ["const:80b2a4:8", "const:4:8"]]
- 0080b2a4 ["CALL", null, ["callee:00480be8:8"]]
+ 0080b2e4 ["INT_ADD", "register:40f0:8", ["const:80b2e4:8", "const:4:8"]]
+ 0080b2e4 ["CALL", null, ["callee:00480be8:8"]]
- 0080b2a4 bytes 41d6f197
+ 0080b2e4 bytes 41d6f197
- 0080b2b0 ["INT_ADD", "register:40f0:8", ["const:80b2b0:8", "const:4:8"]]
- 0080b2b0 ["CALL", null, ["callee:00480be8:8"]]
+ 0080b2f0 ["INT_ADD", "register:40f0:8", ["const:80b2f0:8", "const:4:8"]]
+ 0080b2f0 ["CALL", null, ["callee:00480be8:8"]]
- 0080b2b0 bytes 3ed6f197
+ 0080b2f0 bytes 3ed6f197
~~~


<a id="compare-17ac1d6066efb5ca841a0a965a50cb78"></a>

### [`0080b2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b2e4.md) → [`0080b324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b324.md) FUN_0080b324

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00807d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00807/00807d20.md) [`00809998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00809/00809998.md) [`0080aebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080a/0080aebc.md) [`0080b2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b2e4.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 2件 [`0080b2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b2e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 6件 [`00807d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00807/00807d60.md) [`008099d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00809/008099d8.md) [`0080aefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080a/0080aefc.md) [`0080b324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b324.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 2件 [`0080b324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b324.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080b304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b2e4.md#insn-0080b304) · [`0080b310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b2e4.md#insn-0080b310)
- 新版 `0080b344`（命令位置の公開資料なし） · `0080b350`（命令位置の公開資料なし）

~~~diff
- 0080b304 ["INT_ADD", "register:40f0:8", ["const:80b304:8", "const:4:8"]]
- 0080b304 ["CALL", null, ["local:b0:8"]]
+ 0080b344 ["INT_ADD", "register:40f0:8", ["const:80b344:8", "const:4:8"]]
+ 0080b344 ["CALL", null, ["local:b0:8"]]
- 0080b304 bytes f8ffff97
+ 0080b344 bytes f8ffff97
- 0080b310 ["INT_ADD", "register:40f0:8", ["const:80b310:8", "const:4:8"]]
- 0080b310 ["CALL", null, ["local:b0:8"]]
+ 0080b350 ["INT_ADD", "register:40f0:8", ["const:80b350:8", "const:4:8"]]
+ 0080b350 ["CALL", null, ["local:b0:8"]]
- 0080b310 bytes f5ffff97
+ 0080b350 bytes f5ffff97
~~~


<a id="compare-80ffb795d16e943147cfa351e11c43b0"></a>

### [`0080b328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b328.md) → [`0080b368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b368.md) FUN_0080b368

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00807d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00807/00807d6c.md) [`0080b328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b328.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849164.md) · 呼出先 2件 [`0080b328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b328.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`00807dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00807/00807dac.md) [`0080b368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b368.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008491a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008491a4.md) · 呼出先 2件 [`0080b368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b368.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080b344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b328.md#insn-0080b344) · [`0080b350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b328.md#insn-0080b350) · [`0080b360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b328.md#insn-0080b360)
- 新版 `0080b384`（命令位置の公開資料なし） · `0080b390`（命令位置の公開資料なし） · `0080b3a0`（命令位置の公開資料なし）

~~~diff
- 0080b344 ["INT_ADD", "register:40f0:8", ["const:80b344:8", "const:4:8"]]
- 0080b344 ["CALL", null, ["local:b0:8"]]
+ 0080b384 ["INT_ADD", "register:40f0:8", ["const:80b384:8", "const:4:8"]]
+ 0080b384 ["CALL", null, ["local:b0:8"]]
- 0080b344 bytes f9ffff97
+ 0080b384 bytes f9ffff97
- 0080b350 ["INT_ADD", "register:40f0:8", ["const:80b350:8", "const:4:8"]]
- 0080b350 ["CALL", null, ["local:b0:8"]]
+ 0080b390 ["INT_ADD", "register:40f0:8", ["const:80b390:8", "const:4:8"]]
+ 0080b390 ["CALL", null, ["local:b0:8"]]
- 0080b350 bytes f6ffff97
+ 0080b390 bytes f6ffff97
- 0080b360 ["INT_ADD", "register:40f0:8", ["const:80b360:8", "const:4:8"]]
- 0080b360 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0080b3a0 ["INT_ADD", "register:40f0:8", ["const:80b3a0:8", "const:4:8"]]
+ 0080b3a0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0080b360 bytes d4311194
+ 0080b3a0 bytes c4321194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af29ec932130c8c4286aac67c3bf4b91"></a>

### [`0080bc98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080bc98.md) → [`0080bcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080bcd8.md) FUN_0080bcd8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 11件 [`0047b4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b4cc.md) [`0080dbf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080dbf4.md) [`0080de14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080de14.md) [`0080e258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e258.md) [`0080e26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e26c.md)
- 新版 呼出元 1件 [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 11件 [`0047b50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b50c.md) [`0080dc34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080dc34.md) [`0080de54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080de54.md) [`0080e298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e298.md) [`0080e2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e2ac.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080bd0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080bc98.md#insn-0080bd0c) · [`0080bd48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080bc98.md#insn-0080bd48) · [`0080bd80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080bc98.md#insn-0080bd80)
- 新版 `0080bd4c`（命令位置の公開資料なし） · `0080bd88`（命令位置の公開資料なし） · `0080bdc0`（命令位置の公開資料なし）

~~~diff
- 0080bd0c ["INT_ADD", "register:40f0:8", ["const:80bd0c:8", "const:4:8"]]
- 0080bd0c ["CALL", null, ["callee:0080dc34:8"]]
+ 0080bd4c ["INT_ADD", "register:40f0:8", ["const:80bd4c:8", "const:4:8"]]
+ 0080bd4c ["CALL", null, ["callee:0080dc34:8"]]
- 0080bd0c bytes ba070094
+ 0080bd4c bytes ba070094
- 0080bd48 ["INT_ADD", "register:40f0:8", ["const:80bd48:8", "const:4:8"]]
- 0080bd48 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0080bd88 ["INT_ADD", "register:40f0:8", ["const:80bd88:8", "const:4:8"]]
+ 0080bd88 ["CALL", null, ["callee:00c57eb0:8"]]
- 0080bd48 bytes 5a2f1194
+ 0080bd88 bytes 4a301194
- 0080bd80 ["INT_ADD", "register:40f0:8", ["const:80bd80:8", "const:4:8"]]
- 0080bd80 ["CALL", null, ["callee:0080dc34:8"]]
+ 0080bdc0 ["INT_ADD", "register:40f0:8", ["const:80bdc0:8", "const:4:8"]]
+ 0080bdc0 ["CALL", null, ["callee:0080dc34:8"]]
- 0080bd80 bytes 9d070094
+ 0080bdc0 bytes 9d070094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40d573edd617782654ac8af767395d80"></a>

### [`0080c418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080c/0080c418.md) → [`0080c458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080c/0080c458.md) FUN_0080c458

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00850798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00850/00850798.md) · 呼出先 1件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 1件 [`008507d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00850/008507d8.md) · 呼出先 1件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080c510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080c/0080c418.md#insn-0080c510)
- 新版 `0080c550`（命令位置の公開資料なし）

~~~diff
- 0080c510 ["INT_ADD", "register:40f0:8", ["const:80c510:8", "const:4:8"]]
- 0080c510 ["CALL", null, ["callee:00c58090:8"]]
+ 0080c550 ["INT_ADD", "register:40f0:8", ["const:80c550:8", "const:4:8"]]
+ 0080c550 ["CALL", null, ["callee:00c58090:8"]]
- 0080c510 bytes e02d1194
+ 0080c550 bytes d02e1194
~~~


<a id="compare-d174912403d7ac66cb3d98f8131f1f4a"></a>

### [`0080c530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080c/0080c530.md) → [`0080c570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080c/0080c570.md) FUN_0080c570

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 2件 [`00480af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480af8.md) [`00480b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480b50.md)
- 新版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 2件 [`00480b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md) [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080c570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080c/0080c530.md#insn-0080c570) · [`0080c5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080c/0080c530.md#insn-0080c5bc) · [`0080c5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080c/0080c530.md#insn-0080c5e0)
- 新版 `0080c5b0`（命令位置の公開資料なし） · `0080c5fc`（命令位置の公開資料なし） · `0080c620`（命令位置の公開資料なし）

~~~diff
- 0080c570 ["INT_ADD", "register:40f0:8", ["const:80c570:8", "const:4:8"]]
- 0080c570 ["CALL", null, ["callee:00480b90:8"]]
+ 0080c5b0 ["INT_ADD", "register:40f0:8", ["const:80c5b0:8", "const:4:8"]]
+ 0080c5b0 ["CALL", null, ["callee:00480b90:8"]]
- 0080c570 bytes 78d1f197
+ 0080c5b0 bytes 78d1f197
- 0080c5bc ["INT_ADD", "register:40f0:8", ["const:80c5bc:8", "const:4:8"]]
- 0080c5bc ["CALL", null, ["callee:00480b38:8"]]
+ 0080c5fc ["INT_ADD", "register:40f0:8", ["const:80c5fc:8", "const:4:8"]]
+ 0080c5fc ["CALL", null, ["callee:00480b38:8"]]
- 0080c5bc bytes 4fd1f197
+ 0080c5fc bytes 4fd1f197
- 0080c5e0 ["INT_ADD", "register:40f0:8", ["const:80c5e0:8", "const:4:8"]]
- 0080c5e0 ["CALL", null, ["callee:00480b38:8"]]
+ 0080c620 ["INT_ADD", "register:40f0:8", ["const:80c620:8", "const:4:8"]]
+ 0080c620 ["CALL", null, ["callee:00480b38:8"]]
- 0080c5e0 bytes 46d1f197
+ 0080c620 bytes 46d1f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-828e8dca9ed261d97f1ab907fdf81624"></a>

### [`0080c6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080c/0080c6e8.md) → [`0080c728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080c/0080c728.md) FUN_0080c728

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 2件 [`004800d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004800d8.md) [`00480138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480138.md)
- 新版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 2件 [`00480118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480118.md) [`00480178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080c714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080c/0080c6e8.md#insn-0080c714) · [`0080c748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080c/0080c6e8.md#insn-0080c748) · [`0080c758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080c/0080c6e8.md#insn-0080c758)
- 新版 `0080c754`（命令位置の公開資料なし） · `0080c788`（命令位置の公開資料なし） · `0080c798`（命令位置の公開資料なし）

~~~diff
- 0080c714 ["INT_ADD", "register:40f0:8", ["const:80c714:8", "const:4:8"]]
- 0080c714 ["CALL", null, ["callee:00480178:8"]]
+ 0080c754 ["INT_ADD", "register:40f0:8", ["const:80c754:8", "const:4:8"]]
+ 0080c754 ["CALL", null, ["callee:00480178:8"]]
- 0080c714 bytes 89cef197
+ 0080c754 bytes 89cef197
- 0080c748 ["INT_ADD", "register:40f0:8", ["const:80c748:8", "const:4:8"]]
- 0080c748 ["CALL", null, ["callee:00480118:8"]]
+ 0080c788 ["INT_ADD", "register:40f0:8", ["const:80c788:8", "const:4:8"]]
+ 0080c788 ["CALL", null, ["callee:00480118:8"]]
- 0080c748 bytes 64cef197
+ 0080c788 bytes 64cef197
- 0080c758 ["INT_ADD", "register:40f0:8", ["const:80c758:8", "const:4:8"]]
- 0080c758 ["CALL", null, ["callee:00480118:8"]]
+ 0080c798 ["INT_ADD", "register:40f0:8", ["const:80c798:8", "const:4:8"]]
+ 0080c798 ["CALL", null, ["callee:00480118:8"]]
- 0080c758 bytes 60cef197
+ 0080c798 bytes 60cef197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c16700f8655b8808954e6b3ae6749b2"></a>

### [`0080c838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080c/0080c838.md) → [`0080c878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080c/0080c878.md) FUN_0080c878

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00850798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00850/00850798.md) · 呼出先 1件 [`0080e700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e700.md)
- 新版 呼出元 1件 [`008507d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00850/008507d8.md) · 呼出先 1件 [`0080e740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e740.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080c850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080c/0080c838.md#insn-0080c850)
- 新版 `0080c890`（命令位置の公開資料なし）

~~~diff
- 0080c850 ["INT_ADD", "register:40f0:8", ["const:80c850:8", "const:4:8"]]
- 0080c850 ["CALL", null, ["callee:0080e740:8"]]
+ 0080c890 ["INT_ADD", "register:40f0:8", ["const:80c890:8", "const:4:8"]]
+ 0080c890 ["CALL", null, ["callee:0080e740:8"]]
- 0080c850 bytes ac070094
+ 0080c890 bytes ac070094
~~~


<a id="compare-edcb524f654254e42f233b28c5b6775a"></a>

### [`0080d820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080d820.md) → [`0080d860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080d860.md) FUN_0080d860

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0080b7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b7e4.md) [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) [`00b1b3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1b/00b1b3c0.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00794b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794b2c.md) [`0080da1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080da1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0080b824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b824.md) [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) [`00b1b7e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1b/00b1b7e8.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00794b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794b6c.md) [`0080da5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080da5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0080d8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080d820.md#insn-0080d8c4) · [`0080d910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080d820.md#insn-0080d910) · [`0080d934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080d820.md#insn-0080d934)
- 新版 `0080d904`（命令位置の公開資料なし） · `0080d950`（命令位置の公開資料なし） · `0080d974`（命令位置の公開資料なし）

~~~diff
- 0080d8c4 ["INT_ADD", "register:40f0:8", ["const:80d8c4:8", "const:4:8"]]
- 0080d8c4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0080d904 ["INT_ADD", "register:40f0:8", ["const:80d904:8", "const:4:8"]]
+ 0080d904 ["CALL", null, ["callee:00c57e90:8"]]
- 0080d8c4 bytes 73281194
+ 0080d904 bytes 63291194
- 0080d910 ["INT_ADD", "register:40f0:8", ["const:80d910:8", "const:4:8"]]
- 0080d910 ["CALL", null, ["callee:0080da5c:8"]]
+ 0080d950 ["INT_ADD", "register:40f0:8", ["const:80d950:8", "const:4:8"]]
+ 0080d950 ["CALL", null, ["callee:0080da5c:8"]]
- 0080d910 bytes 43000094
+ 0080d950 bytes 43000094
- 0080d934 ["INT_ADD", "register:40f0:8", ["const:80d934:8", "const:4:8"]]
- 0080d934 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0080d974 ["INT_ADD", "register:40f0:8", ["const:80d974:8", "const:4:8"]]
+ 0080d974 ["CALL", null, ["callee:00c57eb0:8"]]
- 0080d934 bytes 5f281194
+ 0080d974 bytes 4f291194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

