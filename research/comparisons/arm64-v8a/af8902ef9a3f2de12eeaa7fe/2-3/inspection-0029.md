# v16.0.0 → v16.0.1 · 要調査の変更候補 (29)

[一覧の目次](README.md)

<a id="compare-c24fa49e2934dad31f3e29bf2b6327d1"></a>

### [`0086b194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b194.md) → [`0086b1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b1d4.md) FUN_0086b1d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0086b164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b164.md) · 呼出先 7件 [`0048aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aa10.md) [`004986a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004986a4.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0086b1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b1a4.md) · 呼出先 7件 [`0048aa50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aa50.md) [`004986e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004986e4.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086b1c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b194.md#insn-0086b1c8) · [`0086b1e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b194.md#insn-0086b1e8) · [`0086b1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b194.md#insn-0086b1f8)
- 新版 `0086b208`（命令位置の公開資料なし） · `0086b228`（命令位置の公開資料なし） · `0086b238`（命令位置の公開資料なし）

~~~diff
- 0086b1c8 ["INT_ADD", "register:40f0:8", ["const:86b1c8:8", "const:4:8"]]
- 0086b1c8 ["CALL", null, ["callee:00c584f0:8"]]
+ 0086b208 ["INT_ADD", "register:40f0:8", ["const:86b208:8", "const:4:8"]]
+ 0086b208 ["CALL", null, ["callee:00c584f0:8"]]
- 0086b1c8 bytes cab30f94
+ 0086b208 bytes bab40f94
- 0086b1e8 ["INT_ADD", "register:40f0:8", ["const:86b1e8:8", "const:4:8"]]
- 0086b1e8 ["CALL", null, ["callee:0048aa50:8"]]
+ 0086b228 ["INT_ADD", "register:40f0:8", ["const:86b228:8", "const:4:8"]]
+ 0086b228 ["CALL", null, ["callee:0048aa50:8"]]
- 0086b1e8 bytes 0a7ef097
+ 0086b228 bytes 0a7ef097
- 0086b1f8 ["INT_ADD", "register:40f0:8", ["const:86b1f8:8", "const:4:8"]]
- 0086b1f8 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0086b238 ["INT_ADD", "register:40f0:8", ["const:86b238:8", "const:4:8"]]
+ 0086b238 ["CALL", null, ["callee:00c53cd0:8"]]
- 0086b1f8 bytes aea10f94
+ 0086b238 bytes a6a20f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8077de8e1d4cbc3cb0c5f7518e898d77"></a>

### [`0086b52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b52c.md) → [`0086b56c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b56c.md) FUN_0086b56c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0049883c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/0049883c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0049887c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/0049887c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086b540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b52c.md#insn-0086b540)
- 新版 `0086b580`（命令位置の公開資料なし）

~~~diff
- 0086b540 ["INT_ADD", "register:40f0:8", ["const:86b540:8", "const:4:8"]]
- 0086b540 ["CALL", null, ["callee:0049887c:8"]]
+ 0086b580 ["INT_ADD", "register:40f0:8", ["const:86b580:8", "const:4:8"]]
+ 0086b580 ["CALL", null, ["callee:0049887c:8"]]
- 0086b540 bytes bfb4f097
+ 0086b580 bytes bfb4f097
~~~


<a id="compare-906ecab405f694764bd47a12d21a1ae4"></a>

### [`0086b568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b568.md) → [`0086b5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b5a8.md) FUN_0086b5a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00498190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498190.md) [`004987c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004987c4.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004981d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004981d0.md) [`00498804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498804.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086b57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b568.md#insn-0086b57c)
- 新版 `0086b5bc`（命令位置の公開資料なし）

~~~diff
- 0086b57c ["INT_ADD", "register:40f0:8", ["const:86b57c:8", "const:4:8"]]
- 0086b57c ["CALL", null, ["callee:004981d0:8"]]
+ 0086b5bc ["INT_ADD", "register:40f0:8", ["const:86b5bc:8", "const:4:8"]]
+ 0086b5bc ["CALL", null, ["callee:004981d0:8"]]
- 0086b57c bytes 05b3f097
+ 0086b5bc bytes 05b3f097
~~~


<a id="compare-ab59e1e5da8c82522a7c0f4fcdc7fe9c"></a>

### [`0086b5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b5a0.md) → [`0086b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b5e0.md) FUN_0086b5e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0085c10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085c/0085c10c.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0054071c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`0085c14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085c/0085c14c.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0054075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054075c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086b5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b5a0.md#insn-0086b5e4) · [`0086b608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b5a0.md#insn-0086b608) · [`0086b620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b5a0.md#insn-0086b620)
- 新版 `0086b624`（命令位置の公開資料なし） · `0086b648`（命令位置の公開資料なし） · `0086b660`（命令位置の公開資料なし）

~~~diff
- 0086b5e4 ["INT_ADD", "register:40f0:8", ["const:86b5e4:8", "const:4:8"]]
- 0086b5e4 ["CALL", null, ["callee:0054075c:8"]]
+ 0086b624 ["INT_ADD", "register:40f0:8", ["const:86b624:8", "const:4:8"]]
+ 0086b624 ["CALL", null, ["callee:0054075c:8"]]
- 0086b5e4 bytes 4e54f397
+ 0086b624 bytes 4e54f397
- 0086b608 ["INT_ADD", "register:40f0:8", ["const:86b608:8", "const:4:8"]]
- 0086b608 ["CALL", null, ["callee:00c57e90:8"]]
+ 0086b648 ["INT_ADD", "register:40f0:8", ["const:86b648:8", "const:4:8"]]
+ 0086b648 ["CALL", null, ["callee:00c57e90:8"]]
- 0086b608 bytes 22b10f94
+ 0086b648 bytes 12b20f94
- 0086b620 ["INT_ADD", "register:40f0:8", ["const:86b620:8", "const:4:8"]]
- 0086b620 ["CALL", null, ["callee:00c58000:8"]]
+ 0086b660 ["INT_ADD", "register:40f0:8", ["const:86b660:8", "const:4:8"]]
+ 0086b660 ["CALL", null, ["callee:00c58000:8"]]
- 0086b620 bytes 78b10f94
+ 0086b660 bytes 68b20f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-219d32c01f2bbaa443ab8930ac175020"></a>

### [`0086b990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b990.md) → [`0086b9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b9d0.md) FUN_0086b9d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0085c10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085c/0085c10c.md) [`0086c000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c000.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0085c14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085c/0085c14c.md) [`0086c040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c040.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086b9b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b990.md#insn-0086b9b0) · [`0086b9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b990.md#insn-0086b9c0) · [`0086b9f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b990.md#insn-0086b9f8)
- 新版 `0086b9f0`（命令位置の公開資料なし） · `0086ba00`（命令位置の公開資料なし） · `0086ba38`（命令位置の公開資料なし）

~~~diff
- 0086b9b0 ["INT_ADD", "register:40f0:8", ["const:86b9b0:8", "const:4:8"]]
- 0086b9b0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086b9f0 ["INT_ADD", "register:40f0:8", ["const:86b9f0:8", "const:4:8"]]
+ 0086b9f0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086b9b0 bytes 40b00f94
+ 0086b9f0 bytes 30b10f94
- 0086b9c0 ["INT_ADD", "register:40f0:8", ["const:86b9c0:8", "const:4:8"]]
- 0086b9c0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086ba00 ["INT_ADD", "register:40f0:8", ["const:86ba00:8", "const:4:8"]]
+ 0086ba00 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086b9c0 bytes 3cb00f94
+ 0086ba00 bytes 2cb10f94
- 0086b9f8 ["INT_ADD", "register:40f0:8", ["const:86b9f8:8", "const:4:8"]]
- 0086b9f8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086ba38 ["INT_ADD", "register:40f0:8", ["const:86ba38:8", "const:4:8"]]
+ 0086ba38 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086b9f8 bytes 2eb00f94
+ 0086ba38 bytes 1eb10f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45690e87394f201d96bff9ffaa26d1c9"></a>

### [`0086bac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bac8.md) → [`0086bb08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb08.md) FUN_0086bb08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) [`0086bac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bac8.md) [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 2件 [`0086bac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bac8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) [`0086bb08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb08.md) [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 2件 [`0086bb08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb08.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086bae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bac8.md#insn-0086bae4) · [`0086baf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bac8.md#insn-0086baf0) · [`0086bafc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bac8.md#insn-0086bafc)
- 新版 `0086bb24`（命令位置の公開資料なし） · `0086bb30`（命令位置の公開資料なし） · `0086bb3c`（命令位置の公開資料なし）

~~~diff
- 0086bae4 ["INT_ADD", "register:40f0:8", ["const:86bae4:8", "const:4:8"]]
- 0086bae4 ["CALL", null, ["local:b0:8"]]
+ 0086bb24 ["INT_ADD", "register:40f0:8", ["const:86bb24:8", "const:4:8"]]
+ 0086bb24 ["CALL", null, ["local:b0:8"]]
- 0086bae4 bytes f9ffff97
+ 0086bb24 bytes f9ffff97
- 0086baf0 ["INT_ADD", "register:40f0:8", ["const:86baf0:8", "const:4:8"]]
- 0086baf0 ["CALL", null, ["local:b0:8"]]
+ 0086bb30 ["INT_ADD", "register:40f0:8", ["const:86bb30:8", "const:4:8"]]
+ 0086bb30 ["CALL", null, ["local:b0:8"]]
- 0086baf0 bytes f6ffff97
+ 0086bb30 bytes f6ffff97
- 0086bafc ["INT_ADD", "register:40f0:8", ["const:86bafc:8", "const:4:8"]]
- 0086bafc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086bb3c ["INT_ADD", "register:40f0:8", ["const:86bb3c:8", "const:4:8"]]
+ 0086bb3c ["CALL", null, ["callee:00c57eb0:8"]]
- 0086bafc bytes edaf0f94
+ 0086bb3c bytes ddb00f94
~~~


<a id="compare-09bb9495b1f334f681814c1652d6bb05"></a>

### [`0086bb14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bb14.md) → [`0086bb54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb54.md) FUN_0086bb54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849aa4.md) [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) [`0086bb14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bb14.md) [`009c31b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c3/009c31b4.md) · 呼出先 2件 [`0086bb14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bb14.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 7件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849ae4.md) [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) [`0086bb54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb54.md) [`009c3350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c3/009c3350.md) · 呼出先 2件 [`0086bb54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb54.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086bb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bb14.md#insn-0086bb34) · [`0086bb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bb14.md#insn-0086bb40)
- 新版 `0086bb74`（命令位置の公開資料なし） · `0086bb80`（命令位置の公開資料なし）

~~~diff
- 0086bb34 ["INT_ADD", "register:40f0:8", ["const:86bb34:8", "const:4:8"]]
- 0086bb34 ["CALL", null, ["local:b0:8"]]
+ 0086bb74 ["INT_ADD", "register:40f0:8", ["const:86bb74:8", "const:4:8"]]
+ 0086bb74 ["CALL", null, ["local:b0:8"]]
- 0086bb34 bytes f8ffff97
+ 0086bb74 bytes f8ffff97
- 0086bb40 ["INT_ADD", "register:40f0:8", ["const:86bb40:8", "const:4:8"]]
- 0086bb40 ["CALL", null, ["local:b0:8"]]
+ 0086bb80 ["INT_ADD", "register:40f0:8", ["const:86bb80:8", "const:4:8"]]
+ 0086bb80 ["CALL", null, ["local:b0:8"]]
- 0086bb40 bytes f5ffff97
+ 0086bb80 bytes f5ffff97
~~~


<a id="compare-dea947d39d2c208c04fd5e2b5a1d22a3"></a>

### [`0086bb58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bb58.md) → [`0086bb98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb98.md) FUN_0086bb98

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`008497d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008497d8.md) [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) [`0086bb58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bb58.md) · 呼出先 3件 [`0086bb58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bb58.md) [`0086bbb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bbb8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849818.md) [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) [`0086bb98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb98.md) · 呼出先 3件 [`0086bb98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb98.md) [`0086bbf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bbf8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086bb74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bb58.md#insn-0086bb74) · [`0086bb80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bb58.md#insn-0086bb80) · [`0086bb98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bb58.md#insn-0086bb98)
- 新版 `0086bbb4`（命令位置の公開資料なし） · `0086bbc0`（命令位置の公開資料なし） · `0086bbd8`（命令位置の公開資料なし）

~~~diff
- 0086bb74 ["INT_ADD", "register:40f0:8", ["const:86bb74:8", "const:4:8"]]
- 0086bb74 ["CALL", null, ["local:b0:8"]]
+ 0086bbb4 ["INT_ADD", "register:40f0:8", ["const:86bbb4:8", "const:4:8"]]
+ 0086bbb4 ["CALL", null, ["local:b0:8"]]
- 0086bb74 bytes f9ffff97
+ 0086bbb4 bytes f9ffff97
- 0086bb80 ["INT_ADD", "register:40f0:8", ["const:86bb80:8", "const:4:8"]]
- 0086bb80 ["CALL", null, ["local:b0:8"]]
+ 0086bbc0 ["INT_ADD", "register:40f0:8", ["const:86bbc0:8", "const:4:8"]]
+ 0086bbc0 ["CALL", null, ["local:b0:8"]]
- 0086bb80 bytes f6ffff97
+ 0086bbc0 bytes f6ffff97
- 0086bb98 ["INT_ADD", "register:40f0:8", ["const:86bb98:8", "const:4:8"]]
- 0086bb98 ["CALL", null, ["callee:0086bbf8:8"]]
+ 0086bbd8 ["INT_ADD", "register:40f0:8", ["const:86bbd8:8", "const:4:8"]]
+ 0086bbd8 ["CALL", null, ["callee:0086bbf8:8"]]
- 0086bb98 bytes 08000094
+ 0086bbd8 bytes 08000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-079824fdc84e0bcaf4054f8e96375849"></a>

### [`0086bbb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bbb8.md) → [`0086bbf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bbf8.md) FUN_0086bbf8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0086bb58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bb58.md) [`0086bbb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bbb8.md) [`00a6a0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a0a8.md) [`00a6a468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a468.md) · 呼出先 3件 [`0086bbb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bbb8.md) [`0086bc14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bc14.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0086bb98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb98.md) [`0086bbf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bbf8.md) [`00a6a2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6a2a0.md) [`00a6a660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6a660.md) · 呼出先 3件 [`0086bbf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bbf8.md) [`0086bc54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bc54.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086bbd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bbb8.md#insn-0086bbd4) · [`0086bbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bbb8.md#insn-0086bbe0) · [`0086bbf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bbb8.md#insn-0086bbf4)
- 新版 `0086bc14`（命令位置の公開資料なし） · `0086bc20`（命令位置の公開資料なし） · `0086bc34`（命令位置の公開資料なし）

~~~diff
- 0086bbd4 ["INT_ADD", "register:40f0:8", ["const:86bbd4:8", "const:4:8"]]
- 0086bbd4 ["CALL", null, ["local:b0:8"]]
+ 0086bc14 ["INT_ADD", "register:40f0:8", ["const:86bc14:8", "const:4:8"]]
+ 0086bc14 ["CALL", null, ["local:b0:8"]]
- 0086bbd4 bytes f9ffff97
+ 0086bc14 bytes f9ffff97
- 0086bbe0 ["INT_ADD", "register:40f0:8", ["const:86bbe0:8", "const:4:8"]]
- 0086bbe0 ["CALL", null, ["local:b0:8"]]
+ 0086bc20 ["INT_ADD", "register:40f0:8", ["const:86bc20:8", "const:4:8"]]
+ 0086bc20 ["CALL", null, ["local:b0:8"]]
- 0086bbe0 bytes f6ffff97
+ 0086bc20 bytes f6ffff97
- 0086bbf4 ["INT_ADD", "register:40f0:8", ["const:86bbf4:8", "const:4:8"]]
- 0086bbf4 ["CALL", null, ["callee:0086bc54:8"]]
+ 0086bc34 ["INT_ADD", "register:40f0:8", ["const:86bc34:8", "const:4:8"]]
+ 0086bc34 ["CALL", null, ["callee:0086bc54:8"]]
- 0086bbf4 bytes 08000094
+ 0086bc34 bytes 08000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b58cbf5c0f8e6540f4ef64f9dce3bd0"></a>

### [`0086bc14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bc14.md) → [`0086bc54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bc54.md) FUN_0086bc54

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0086bbb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bbb8.md) [`00a6c020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c020.md) [`00a6c254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c254.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0086bbf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bbf8.md) [`00a6c218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6c/00a6c218.md) [`00a6c44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6c/00a6c44c.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086bc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bc14.md#insn-0086bc38) · [`0086bc4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bc14.md#insn-0086bc4c) · [`0086bc54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bc14.md#insn-0086bc54)
- 新版 `0086bc78`（命令位置の公開資料なし） · `0086bc8c`（命令位置の公開資料なし） · `0086bc94`（命令位置の公開資料なし）

~~~diff
- 0086bc38 ["INT_ADD", "register:40f0:8", ["const:86bc38:8", "const:4:8"]]
- 0086bc38 ["CALL", null, ["callee:00c53d00:8"]]
+ 0086bc78 ["INT_ADD", "register:40f0:8", ["const:86bc78:8", "const:4:8"]]
+ 0086bc78 ["CALL", null, ["callee:00c53d00:8"]]
- 0086bc38 bytes 2a9f0f94
+ 0086bc78 bytes 22a00f94
- 0086bc4c ["COPY", "register:0:8", ["register:4040:8"]]
- 0086bc4c ["INT_ADD", "register:40f0:8", ["const:86bc4c:8", "const:4:8"]]
- 0086bc4c ["CALLIND", null, ["register:0:8"]]
+ 0086bc8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0086bc8c ["INT_ADD", "register:40f0:8", ["const:86bc8c:8", "const:4:8"]]
+ 0086bc8c ["CALLIND", null, ["register:0:8"]]
- 0086bc4c bytes 00013fd6
+ 0086bc8c bytes 00013fd6
- 0086bc54 ["INT_ADD", "register:40f0:8", ["const:86bc54:8", "const:4:8"]]
- 0086bc54 ["CALL", null, ["callee:00c57e80:8"]]
+ 0086bc94 ["INT_ADD", "register:40f0:8", ["const:86bc94:8", "const:4:8"]]
+ 0086bc94 ["CALL", null, ["callee:00c57e80:8"]]
- 0086bc54 bytes 8baf0f94
+ 0086bc94 bytes 7bb00f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1008a8dabb6cf2ac887b5b327103df3e"></a>

### [`0086bd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bd78.md) → [`0086bdb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bdb8.md) FUN_0086bdb8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`008497d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008497d8.md) [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) [`0086bd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bd78.md) [`00a68f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68f5c.md) · 呼出先 4件 [`0086bd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bd78.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 6件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849818.md) [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) [`0086bdb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bdb8.md) [`00a69154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a69154.md) · 呼出先 4件 [`0086bdb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bdb8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086bd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bd78.md#insn-0086bd94) · [`0086bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bd78.md#insn-0086bda0) · [`0086bdb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bd78.md#insn-0086bdb4)
- 新版 `0086bdd4`（命令位置の公開資料なし） · `0086bde0`（命令位置の公開資料なし） · `0086bdf4`（命令位置の公開資料なし）

~~~diff
- 0086bd94 ["INT_ADD", "register:40f0:8", ["const:86bd94:8", "const:4:8"]]
- 0086bd94 ["CALL", null, ["local:b0:8"]]
+ 0086bdd4 ["INT_ADD", "register:40f0:8", ["const:86bdd4:8", "const:4:8"]]
+ 0086bdd4 ["CALL", null, ["local:b0:8"]]
- 0086bd94 bytes f9ffff97
+ 0086bdd4 bytes f9ffff97
- 0086bda0 ["INT_ADD", "register:40f0:8", ["const:86bda0:8", "const:4:8"]]
- 0086bda0 ["CALL", null, ["local:b0:8"]]
+ 0086bde0 ["INT_ADD", "register:40f0:8", ["const:86bde0:8", "const:4:8"]]
+ 0086bde0 ["CALL", null, ["local:b0:8"]]
- 0086bda0 bytes f6ffff97
+ 0086bde0 bytes f6ffff97
- 0086bdb4 ["INT_ADD", "register:40f0:8", ["const:86bdb4:8", "const:4:8"]]
- 0086bdb4 ["CALL", null, ["callee:00c53d00:8"]]
+ 0086bdf4 ["INT_ADD", "register:40f0:8", ["const:86bdf4:8", "const:4:8"]]
+ 0086bdf4 ["CALL", null, ["callee:00c53d00:8"]]
- 0086bdb4 bytes cb9e0f94
+ 0086bdf4 bytes c39f0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b201d85d9b590572faff035eb12076c"></a>

### [`0086bde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bde8.md) → [`0086be28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086be28.md) FUN_0086be28

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) [`0086bde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bde8.md) [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 2件 [`0086bde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bde8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) [`0086be28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086be28.md) [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 2件 [`0086be28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086be28.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086be08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bde8.md#insn-0086be08) · [`0086be14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bde8.md#insn-0086be14)
- 新版 `0086be48`（命令位置の公開資料なし） · `0086be54`（命令位置の公開資料なし）

~~~diff
- 0086be08 ["INT_ADD", "register:40f0:8", ["const:86be08:8", "const:4:8"]]
- 0086be08 ["CALL", null, ["local:b0:8"]]
+ 0086be48 ["INT_ADD", "register:40f0:8", ["const:86be48:8", "const:4:8"]]
+ 0086be48 ["CALL", null, ["local:b0:8"]]
- 0086be08 bytes f8ffff97
+ 0086be48 bytes f8ffff97
- 0086be14 ["INT_ADD", "register:40f0:8", ["const:86be14:8", "const:4:8"]]
- 0086be14 ["CALL", null, ["local:b0:8"]]
+ 0086be54 ["INT_ADD", "register:40f0:8", ["const:86be54:8", "const:4:8"]]
+ 0086be54 ["CALL", null, ["local:b0:8"]]
- 0086be14 bytes f5ffff97
+ 0086be54 bytes f5ffff97
~~~


<a id="compare-17c536119e16a4a9d2ec9e1e5b7280c6"></a>

### [`0086be2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086be2c.md) → [`0086be6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086be6c.md) FUN_0086be6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849294.md) [`0086be2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086be2c.md) [`00a75bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a75/00a75bb4.md) [`00aa281c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa2/00aa281c.md) · 呼出先 2件 [`0086be2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086be2c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 6件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008492d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008492d4.md) [`0086be6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086be6c.md) [`00a75dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a75/00a75dac.md) [`00aa2a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa2/00aa2a18.md) · 呼出先 2件 [`0086be6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086be6c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086be4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086be2c.md#insn-0086be4c) · [`0086be58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086be2c.md#insn-0086be58)
- 新版 `0086be8c`（命令位置の公開資料なし） · `0086be98`（命令位置の公開資料なし）

~~~diff
- 0086be4c ["INT_ADD", "register:40f0:8", ["const:86be4c:8", "const:4:8"]]
- 0086be4c ["CALL", null, ["local:b0:8"]]
+ 0086be8c ["INT_ADD", "register:40f0:8", ["const:86be8c:8", "const:4:8"]]
+ 0086be8c ["CALL", null, ["local:b0:8"]]
- 0086be4c bytes f8ffff97
+ 0086be8c bytes f8ffff97
- 0086be58 ["INT_ADD", "register:40f0:8", ["const:86be58:8", "const:4:8"]]
- 0086be58 ["CALL", null, ["local:b0:8"]]
+ 0086be98 ["INT_ADD", "register:40f0:8", ["const:86be98:8", "const:4:8"]]
+ 0086be98 ["CALL", null, ["local:b0:8"]]
- 0086be58 bytes f5ffff97
+ 0086be98 bytes f5ffff97
~~~


<a id="compare-8bf6a101d74b3560dd6cbd94b08efaaa"></a>

### [`0086be70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086be70.md) → [`0086beb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086beb0.md) FUN_0086beb0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086be70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086be70.md) · 呼出先 2件 [`0086be70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086be70.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086beb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086beb0.md) · 呼出先 2件 [`0086beb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086beb0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086be8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086be70.md#insn-0086be8c) · [`0086be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086be70.md#insn-0086be98) · [`0086bea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086be70.md#insn-0086bea8)
- 新版 `0086becc`（命令位置の公開資料なし） · `0086bed8`（命令位置の公開資料なし） · `0086bee8`（命令位置の公開資料なし）

~~~diff
- 0086be8c ["INT_ADD", "register:40f0:8", ["const:86be8c:8", "const:4:8"]]
- 0086be8c ["CALL", null, ["local:b0:8"]]
+ 0086becc ["INT_ADD", "register:40f0:8", ["const:86becc:8", "const:4:8"]]
+ 0086becc ["CALL", null, ["local:b0:8"]]
- 0086be8c bytes f9ffff97
+ 0086becc bytes f9ffff97
- 0086be98 ["INT_ADD", "register:40f0:8", ["const:86be98:8", "const:4:8"]]
- 0086be98 ["CALL", null, ["local:b0:8"]]
+ 0086bed8 ["INT_ADD", "register:40f0:8", ["const:86bed8:8", "const:4:8"]]
+ 0086bed8 ["CALL", null, ["local:b0:8"]]
- 0086be98 bytes f6ffff97
+ 0086bed8 bytes f6ffff97
- 0086bea8 ["INT_ADD", "register:40f0:8", ["const:86bea8:8", "const:4:8"]]
- 0086bea8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086bee8 ["INT_ADD", "register:40f0:8", ["const:86bee8:8", "const:4:8"]]
+ 0086bee8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086bea8 bytes 02af0f94
+ 0086bee8 bytes f2af0f94
~~~


<a id="compare-a9a05c570bec9518ec235524fcb0f01b"></a>

### [`0086bec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bec0.md) → [`0086bf00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf00.md) FUN_0086bf00

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086bec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bec0.md) [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 2件 [`0086bec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bec0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086bf00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf00.md) [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 2件 [`0086bf00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086bedc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bec0.md#insn-0086bedc) · [`0086bee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bec0.md#insn-0086bee8) · [`0086bef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bec0.md#insn-0086bef8)
- 新版 `0086bf1c`（命令位置の公開資料なし） · `0086bf28`（命令位置の公開資料なし） · `0086bf38`（命令位置の公開資料なし）

~~~diff
- 0086bedc ["INT_ADD", "register:40f0:8", ["const:86bedc:8", "const:4:8"]]
- 0086bedc ["CALL", null, ["local:b0:8"]]
+ 0086bf1c ["INT_ADD", "register:40f0:8", ["const:86bf1c:8", "const:4:8"]]
+ 0086bf1c ["CALL", null, ["local:b0:8"]]
- 0086bedc bytes f9ffff97
+ 0086bf1c bytes f9ffff97
- 0086bee8 ["INT_ADD", "register:40f0:8", ["const:86bee8:8", "const:4:8"]]
- 0086bee8 ["CALL", null, ["local:b0:8"]]
+ 0086bf28 ["INT_ADD", "register:40f0:8", ["const:86bf28:8", "const:4:8"]]
+ 0086bf28 ["CALL", null, ["local:b0:8"]]
- 0086bee8 bytes f6ffff97
+ 0086bf28 bytes f6ffff97
- 0086bef8 ["INT_ADD", "register:40f0:8", ["const:86bef8:8", "const:4:8"]]
- 0086bef8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086bf38 ["INT_ADD", "register:40f0:8", ["const:86bf38:8", "const:4:8"]]
+ 0086bf38 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086bef8 bytes eeae0f94
+ 0086bf38 bytes deaf0f94
~~~


<a id="compare-2183bd27ee5353bba59baa3096ae9c30"></a>

### [`0086bf10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bf10.md) → [`0086bf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf50.md) FUN_0086bf50

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086bf10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bf10.md) · 呼出先 3件 [`0086bf10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bf10.md) [`0086bf5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bf5c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086bf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf50.md) · 呼出先 3件 [`0086bf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf50.md) [`0086bf9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf9c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086bf30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bf10.md#insn-0086bf30) · [`0086bf3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bf10.md#insn-0086bf3c) · [`0086bf44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bf10.md#insn-0086bf44)
- 新版 `0086bf70`（命令位置の公開資料なし） · `0086bf7c`（命令位置の公開資料なし） · `0086bf84`（命令位置の公開資料なし）

~~~diff
- 0086bf30 ["INT_ADD", "register:40f0:8", ["const:86bf30:8", "const:4:8"]]
- 0086bf30 ["CALL", null, ["local:b0:8"]]
+ 0086bf70 ["INT_ADD", "register:40f0:8", ["const:86bf70:8", "const:4:8"]]
+ 0086bf70 ["CALL", null, ["local:b0:8"]]
- 0086bf30 bytes f8ffff97
+ 0086bf70 bytes f8ffff97
- 0086bf3c ["INT_ADD", "register:40f0:8", ["const:86bf3c:8", "const:4:8"]]
- 0086bf3c ["CALL", null, ["local:b0:8"]]
+ 0086bf7c ["INT_ADD", "register:40f0:8", ["const:86bf7c:8", "const:4:8"]]
+ 0086bf7c ["CALL", null, ["local:b0:8"]]
- 0086bf3c bytes f5ffff97
+ 0086bf7c bytes f5ffff97
- 0086bf44 ["INT_ADD", "register:40f0:8", ["const:86bf44:8", "const:4:8"]]
- 0086bf44 ["CALL", null, ["callee:0086bf9c:8"]]
+ 0086bf84 ["INT_ADD", "register:40f0:8", ["const:86bf84:8", "const:4:8"]]
+ 0086bf84 ["CALL", null, ["callee:0086bf9c:8"]]
- 0086bf44 bytes 06000094
+ 0086bf84 bytes 06000094
~~~


<a id="compare-762967a83188c5123b0b68fd3676b554"></a>

### [`0086bf5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bf5c.md) → [`0086bf9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf9c.md) FUN_0086bf9c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0086bf10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bf10.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0086bf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf50.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086bfa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bf5c.md#insn-0086bfa8) · [`0086bfb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bf5c.md#insn-0086bfb8) · [`0086bfc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bf5c.md#insn-0086bfc4)
- 新版 `0086bfe8`（命令位置の公開資料なし） · `0086bff8`（命令位置の公開資料なし） · `0086c004`（命令位置の公開資料なし）

~~~diff
- 0086bfa8 ["INT_ADD", "register:40f0:8", ["const:86bfa8:8", "const:4:8"]]
- 0086bfa8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086bfe8 ["INT_ADD", "register:40f0:8", ["const:86bfe8:8", "const:4:8"]]
+ 0086bfe8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086bfa8 bytes c2ae0f94
+ 0086bfe8 bytes b2af0f94
- 0086bfb8 ["INT_ADD", "register:40f0:8", ["const:86bfb8:8", "const:4:8"]]
- 0086bfb8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086bff8 ["INT_ADD", "register:40f0:8", ["const:86bff8:8", "const:4:8"]]
+ 0086bff8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086bfb8 bytes beae0f94
+ 0086bff8 bytes aeaf0f94
- 0086bfc4 ["INT_ADD", "register:40f0:8", ["const:86bfc4:8", "const:4:8"]]
- 0086bfc4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086c004 ["INT_ADD", "register:40f0:8", ["const:86c004:8", "const:4:8"]]
+ 0086c004 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086bfc4 bytes bbae0f94
+ 0086c004 bytes abaf0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c12147ae99a97b6c7088e7fe385afdfe"></a>

### [`0086c000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c000.md) → [`0086c040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c040.md) FUN_0086c040

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086c000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c000.md) [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 3件 [`0086b990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b990.md) [`0086c000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c000.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086c040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c040.md) [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 3件 [`0086b9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b9d0.md) [`0086c040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c040.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c000.md#insn-0086c020) · [`0086c02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c000.md#insn-0086c02c) · [`0086c034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c000.md#insn-0086c034)
- 新版 `0086c060`（命令位置の公開資料なし） · `0086c06c`（命令位置の公開資料なし） · `0086c074`（命令位置の公開資料なし）

~~~diff
- 0086c020 ["INT_ADD", "register:40f0:8", ["const:86c020:8", "const:4:8"]]
- 0086c020 ["CALL", null, ["local:b0:8"]]
+ 0086c060 ["INT_ADD", "register:40f0:8", ["const:86c060:8", "const:4:8"]]
+ 0086c060 ["CALL", null, ["local:b0:8"]]
- 0086c020 bytes f8ffff97
+ 0086c060 bytes f8ffff97
- 0086c02c ["INT_ADD", "register:40f0:8", ["const:86c02c:8", "const:4:8"]]
- 0086c02c ["CALL", null, ["local:b0:8"]]
+ 0086c06c ["INT_ADD", "register:40f0:8", ["const:86c06c:8", "const:4:8"]]
+ 0086c06c ["CALL", null, ["local:b0:8"]]
- 0086c02c bytes f5ffff97
+ 0086c06c bytes f5ffff97
- 0086c034 ["INT_ADD", "register:40f0:8", ["const:86c034:8", "const:4:8"]]
- 0086c034 ["CALL", null, ["callee:0086b9d0:8"]]
+ 0086c074 ["INT_ADD", "register:40f0:8", ["const:86c074:8", "const:4:8"]]
+ 0086c074 ["CALL", null, ["callee:0086b9d0:8"]]
- 0086c034 bytes 57feff97
+ 0086c074 bytes 57feff97
~~~


<a id="compare-dbde8822cf2458b54bbeba7963c59b56"></a>

### [`0086c04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c04c.md) → [`0086c08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c08c.md) FUN_0086c08c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086c04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c04c.md) · 呼出先 4件 [`0086c04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c04c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086c08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c08c.md) · 呼出先 4件 [`0086c08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c08c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c06c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c04c.md#insn-0086c06c) · [`0086c078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c04c.md#insn-0086c078) · [`0086c0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c04c.md#insn-0086c0b4)
- 新版 `0086c0ac`（命令位置の公開資料なし） · `0086c0b8`（命令位置の公開資料なし） · `0086c0f4`（命令位置の公開資料なし）

~~~diff
- 0086c06c ["INT_ADD", "register:40f0:8", ["const:86c06c:8", "const:4:8"]]
- 0086c06c ["CALL", null, ["local:b0:8"]]
+ 0086c0ac ["INT_ADD", "register:40f0:8", ["const:86c0ac:8", "const:4:8"]]
+ 0086c0ac ["CALL", null, ["local:b0:8"]]
- 0086c06c bytes f8ffff97
+ 0086c0ac bytes f8ffff97
- 0086c078 ["INT_ADD", "register:40f0:8", ["const:86c078:8", "const:4:8"]]
- 0086c078 ["CALL", null, ["local:b0:8"]]
+ 0086c0b8 ["INT_ADD", "register:40f0:8", ["const:86c0b8:8", "const:4:8"]]
+ 0086c0b8 ["CALL", null, ["local:b0:8"]]
- 0086c078 bytes f5ffff97
+ 0086c0b8 bytes f5ffff97
- 0086c0b4 ["INT_ADD", "register:40f0:8", ["const:86c0b4:8", "const:4:8"]]
- 0086c0b4 ["CALL", null, ["callee:00c53d00:8"]]
+ 0086c0f4 ["INT_ADD", "register:40f0:8", ["const:86c0f4:8", "const:4:8"]]
+ 0086c0f4 ["CALL", null, ["callee:00c53d00:8"]]
- 0086c0b4 bytes 0b9e0f94
+ 0086c0f4 bytes 039f0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f67e4c19d19c488f3ae7cbdad70613a"></a>

### [`0086c0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c0fc.md) → [`0086c13c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c13c.md) FUN_0086c13c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) [`0086c0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c0fc.md) · 呼出先 2件 [`0086c0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c0fc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) [`0086c13c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c13c.md) · 呼出先 2件 [`0086c13c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c13c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c0fc.md#insn-0086c11c) · [`0086c128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c0fc.md#insn-0086c128)
- 新版 `0086c15c`（命令位置の公開資料なし） · `0086c168`（命令位置の公開資料なし）

~~~diff
- 0086c11c ["INT_ADD", "register:40f0:8", ["const:86c11c:8", "const:4:8"]]
- 0086c11c ["CALL", null, ["local:b0:8"]]
+ 0086c15c ["INT_ADD", "register:40f0:8", ["const:86c15c:8", "const:4:8"]]
+ 0086c15c ["CALL", null, ["local:b0:8"]]
- 0086c11c bytes f8ffff97
+ 0086c15c bytes f8ffff97
- 0086c128 ["INT_ADD", "register:40f0:8", ["const:86c128:8", "const:4:8"]]
- 0086c128 ["CALL", null, ["local:b0:8"]]
+ 0086c168 ["INT_ADD", "register:40f0:8", ["const:86c168:8", "const:4:8"]]
+ 0086c168 ["CALL", null, ["local:b0:8"]]
- 0086c128 bytes f5ffff97
+ 0086c168 bytes f5ffff97
~~~


<a id="compare-f1dbd5bb12857744e4a49bfea31cf1e8"></a>

### [`0086c140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c140.md) → [`0086c180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c180.md) FUN_0086c180

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) [`0086c140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c140.md) · 呼出先 2件 [`0086c140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c140.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) [`0086c180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c180.md) · 呼出先 2件 [`0086c180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c180.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c140.md#insn-0086c15c) · [`0086c168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c140.md#insn-0086c168) · [`0086c178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c140.md#insn-0086c178)
- 新版 `0086c19c`（命令位置の公開資料なし） · `0086c1a8`（命令位置の公開資料なし） · `0086c1b8`（命令位置の公開資料なし）

~~~diff
- 0086c15c ["INT_ADD", "register:40f0:8", ["const:86c15c:8", "const:4:8"]]
- 0086c15c ["CALL", null, ["local:b0:8"]]
+ 0086c19c ["INT_ADD", "register:40f0:8", ["const:86c19c:8", "const:4:8"]]
+ 0086c19c ["CALL", null, ["local:b0:8"]]
- 0086c15c bytes f9ffff97
+ 0086c19c bytes f9ffff97
- 0086c168 ["INT_ADD", "register:40f0:8", ["const:86c168:8", "const:4:8"]]
- 0086c168 ["CALL", null, ["local:b0:8"]]
+ 0086c1a8 ["INT_ADD", "register:40f0:8", ["const:86c1a8:8", "const:4:8"]]
+ 0086c1a8 ["CALL", null, ["local:b0:8"]]
- 0086c168 bytes f6ffff97
+ 0086c1a8 bytes f6ffff97
- 0086c178 ["INT_ADD", "register:40f0:8", ["const:86c178:8", "const:4:8"]]
- 0086c178 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086c1b8 ["INT_ADD", "register:40f0:8", ["const:86c1b8:8", "const:4:8"]]
+ 0086c1b8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086c178 bytes 4eae0f94
+ 0086c1b8 bytes 3eaf0f94
~~~


<a id="compare-420e86d2c07d9892a9d177ad68124eed"></a>

### [`0086c190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c190.md) → [`0086c1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c1d0.md) FUN_0086c1d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086151c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00861/0086151c.md) [`0086c190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c190.md) · 呼出先 2件 [`0086c190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c190.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086155c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00861/0086155c.md) [`0086c1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c1d0.md) · 呼出先 2件 [`0086c1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c1d0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c190.md#insn-0086c1b0) · [`0086c1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c190.md#insn-0086c1bc)
- 新版 `0086c1f0`（命令位置の公開資料なし） · `0086c1fc`（命令位置の公開資料なし）

~~~diff
- 0086c1b0 ["INT_ADD", "register:40f0:8", ["const:86c1b0:8", "const:4:8"]]
- 0086c1b0 ["CALL", null, ["local:b0:8"]]
+ 0086c1f0 ["INT_ADD", "register:40f0:8", ["const:86c1f0:8", "const:4:8"]]
+ 0086c1f0 ["CALL", null, ["local:b0:8"]]
- 0086c1b0 bytes f8ffff97
+ 0086c1f0 bytes f8ffff97
- 0086c1bc ["INT_ADD", "register:40f0:8", ["const:86c1bc:8", "const:4:8"]]
- 0086c1bc ["CALL", null, ["local:b0:8"]]
+ 0086c1fc ["INT_ADD", "register:40f0:8", ["const:86c1fc:8", "const:4:8"]]
+ 0086c1fc ["CALL", null, ["local:b0:8"]]
- 0086c1bc bytes f5ffff97
+ 0086c1fc bytes f5ffff97
~~~


<a id="compare-d2267d4da20229542dc620178222012a"></a>

### [`0086c1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c1d4.md) → [`0086c214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c214.md) FUN_0086c214

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086c1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c1d4.md) [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 2件 [`0086c1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c1d4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086c214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c214.md) [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 2件 [`0086c214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c214.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c1d4.md#insn-0086c1f0) · [`0086c1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c1d4.md#insn-0086c1fc) · [`0086c20c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c1d4.md#insn-0086c20c)
- 新版 `0086c230`（命令位置の公開資料なし） · `0086c23c`（命令位置の公開資料なし） · `0086c24c`（命令位置の公開資料なし）

~~~diff
- 0086c1f0 ["INT_ADD", "register:40f0:8", ["const:86c1f0:8", "const:4:8"]]
- 0086c1f0 ["CALL", null, ["local:b0:8"]]
+ 0086c230 ["INT_ADD", "register:40f0:8", ["const:86c230:8", "const:4:8"]]
+ 0086c230 ["CALL", null, ["local:b0:8"]]
- 0086c1f0 bytes f9ffff97
+ 0086c230 bytes f9ffff97
- 0086c1fc ["INT_ADD", "register:40f0:8", ["const:86c1fc:8", "const:4:8"]]
- 0086c1fc ["CALL", null, ["local:b0:8"]]
+ 0086c23c ["INT_ADD", "register:40f0:8", ["const:86c23c:8", "const:4:8"]]
+ 0086c23c ["CALL", null, ["local:b0:8"]]
- 0086c1fc bytes f6ffff97
+ 0086c23c bytes f6ffff97
- 0086c20c ["INT_ADD", "register:40f0:8", ["const:86c20c:8", "const:4:8"]]
- 0086c20c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086c24c ["INT_ADD", "register:40f0:8", ["const:86c24c:8", "const:4:8"]]
+ 0086c24c ["CALL", null, ["callee:00c57eb0:8"]]
- 0086c20c bytes 29ae0f94
+ 0086c24c bytes 19af0f94
~~~


<a id="compare-d02ce3a77dcea1293090873fd69d1b81"></a>

### [`0086c224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c224.md) → [`0086c264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c264.md) FUN_0086c264

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) [`008609ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00860/008609ac.md) [`0086c224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c224.md) [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 3件 [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`0086c224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c224.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 5件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) [`008609ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00860/008609ec.md) [`0086c264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c264.md) [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 3件 [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`0086c264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c264.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c224.md#insn-0086c244) · [`0086c250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c224.md#insn-0086c250) · [`0086c25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c224.md#insn-0086c25c)
- 新版 `0086c284`（命令位置の公開資料なし） · `0086c290`（命令位置の公開資料なし） · `0086c29c`（命令位置の公開資料なし）

~~~diff
- 0086c244 ["INT_ADD", "register:40f0:8", ["const:86c244:8", "const:4:8"]]
- 0086c244 ["CALL", null, ["local:b0:8"]]
+ 0086c284 ["INT_ADD", "register:40f0:8", ["const:86c284:8", "const:4:8"]]
+ 0086c284 ["CALL", null, ["local:b0:8"]]
- 0086c244 bytes f8ffff97
+ 0086c284 bytes f8ffff97
- 0086c250 ["INT_ADD", "register:40f0:8", ["const:86c250:8", "const:4:8"]]
- 0086c250 ["CALL", null, ["local:b0:8"]]
+ 0086c290 ["INT_ADD", "register:40f0:8", ["const:86c290:8", "const:4:8"]]
+ 0086c290 ["CALL", null, ["local:b0:8"]]
- 0086c250 bytes f5ffff97
+ 0086c290 bytes f5ffff97
- 0086c25c ["INT_ADD", "register:40f0:8", ["const:86c25c:8", "const:4:8"]]
- 0086c25c ["CALL", null, ["callee:00676a60:8"]]
+ 0086c29c ["INT_ADD", "register:40f0:8", ["const:86c29c:8", "const:4:8"]]
+ 0086c29c ["CALL", null, ["callee:00676a60:8"]]
- 0086c25c bytes f129f897
+ 0086c29c bytes f129f897
~~~


<a id="compare-95e6f161c1e7583451de924706bc4610"></a>

### [`0086c274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c274.md) → [`0086c2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c2b4.md) FUN_0086c2b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00850798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00850/00850798.md) [`0086c274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c274.md) [`0086c2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c2b8.md) [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 2件 [`0086c274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c274.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 7件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008507d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00850/008507d8.md) [`0086c2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c2b4.md) [`0086c2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c2f8.md) [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 2件 [`0086c2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c2b4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c274.md#insn-0086c294) · [`0086c2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c274.md#insn-0086c2a0)
- 新版 `0086c2d4`（命令位置の公開資料なし） · `0086c2e0`（命令位置の公開資料なし）

~~~diff
- 0086c294 ["INT_ADD", "register:40f0:8", ["const:86c294:8", "const:4:8"]]
- 0086c294 ["CALL", null, ["local:b0:8"]]
+ 0086c2d4 ["INT_ADD", "register:40f0:8", ["const:86c2d4:8", "const:4:8"]]
+ 0086c2d4 ["CALL", null, ["local:b0:8"]]
- 0086c294 bytes f8ffff97
+ 0086c2d4 bytes f8ffff97
- 0086c2a0 ["INT_ADD", "register:40f0:8", ["const:86c2a0:8", "const:4:8"]]
- 0086c2a0 ["CALL", null, ["local:b0:8"]]
+ 0086c2e0 ["INT_ADD", "register:40f0:8", ["const:86c2e0:8", "const:4:8"]]
+ 0086c2e0 ["CALL", null, ["local:b0:8"]]
- 0086c2a0 bytes f5ffff97
+ 0086c2e0 bytes f5ffff97
~~~


<a id="compare-b0a32dacd54affe42c8d46c3c18bf97a"></a>

### [`0086c2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c2b8.md) → [`0086c2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c2f8.md) FUN_0086c2f8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00850798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00850/00850798.md) [`0086c2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c2b8.md) [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 3件 [`0086c274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c274.md) [`0086c2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c2b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008507d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00850/008507d8.md) [`0086c2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c2f8.md) [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 3件 [`0086c2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c2b4.md) [`0086c2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c2f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c2b8.md#insn-0086c2d8) · [`0086c2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c2b8.md#insn-0086c2e4) · [`0086c2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c2b8.md#insn-0086c2f0)
- 新版 `0086c318`（命令位置の公開資料なし） · `0086c324`（命令位置の公開資料なし） · `0086c330`（命令位置の公開資料なし）

~~~diff
- 0086c2d8 ["INT_ADD", "register:40f0:8", ["const:86c2d8:8", "const:4:8"]]
- 0086c2d8 ["CALL", null, ["local:b0:8"]]
+ 0086c318 ["INT_ADD", "register:40f0:8", ["const:86c318:8", "const:4:8"]]
+ 0086c318 ["CALL", null, ["local:b0:8"]]
- 0086c2d8 bytes f8ffff97
+ 0086c318 bytes f8ffff97
- 0086c2e4 ["INT_ADD", "register:40f0:8", ["const:86c2e4:8", "const:4:8"]]
- 0086c2e4 ["CALL", null, ["local:b0:8"]]
+ 0086c324 ["INT_ADD", "register:40f0:8", ["const:86c324:8", "const:4:8"]]
+ 0086c324 ["CALL", null, ["local:b0:8"]]
- 0086c2e4 bytes f5ffff97
+ 0086c324 bytes f5ffff97
- 0086c2f0 ["INT_ADD", "register:40f0:8", ["const:86c2f0:8", "const:4:8"]]
- 0086c2f0 ["CALL", null, ["callee:0086c2b4:8"]]
+ 0086c330 ["INT_ADD", "register:40f0:8", ["const:86c330:8", "const:4:8"]]
+ 0086c330 ["CALL", null, ["callee:0086c2b4:8"]]
- 0086c2f0 bytes e1ffff97
+ 0086c330 bytes e1ffff97
~~~


<a id="compare-206aa7f29d8dae3433280bc71c8422da"></a>

### [`0086c308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c308.md) → [`0086c348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c348.md) FUN_0086c348

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086c308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c308.md) · 呼出先 2件 [`0086c308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c308.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086c348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c348.md) · 呼出先 2件 [`0086c348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c348.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c308.md#insn-0086c328) · [`0086c334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c308.md#insn-0086c334)
- 新版 `0086c368`（命令位置の公開資料なし） · `0086c374`（命令位置の公開資料なし）

~~~diff
- 0086c328 ["INT_ADD", "register:40f0:8", ["const:86c328:8", "const:4:8"]]
- 0086c328 ["CALL", null, ["local:b0:8"]]
+ 0086c368 ["INT_ADD", "register:40f0:8", ["const:86c368:8", "const:4:8"]]
+ 0086c368 ["CALL", null, ["local:b0:8"]]
- 0086c328 bytes f8ffff97
+ 0086c368 bytes f8ffff97
- 0086c334 ["INT_ADD", "register:40f0:8", ["const:86c334:8", "const:4:8"]]
- 0086c334 ["CALL", null, ["local:b0:8"]]
+ 0086c374 ["INT_ADD", "register:40f0:8", ["const:86c374:8", "const:4:8"]]
+ 0086c374 ["CALL", null, ["local:b0:8"]]
- 0086c334 bytes f5ffff97
+ 0086c374 bytes f5ffff97
~~~


<a id="compare-47a8aed7d05806943e24b617e5c42af2"></a>

### [`0086c34c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c34c.md) → [`0086c38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c38c.md) FUN_0086c38c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086c34c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c34c.md) · 呼出先 2件 [`0086c34c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c34c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086c38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c38c.md) · 呼出先 2件 [`0086c38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c38c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c36c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c34c.md#insn-0086c36c) · [`0086c378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c34c.md#insn-0086c378)
- 新版 `0086c3ac`（命令位置の公開資料なし） · `0086c3b8`（命令位置の公開資料なし）

~~~diff
- 0086c36c ["INT_ADD", "register:40f0:8", ["const:86c36c:8", "const:4:8"]]
- 0086c36c ["CALL", null, ["local:b0:8"]]
+ 0086c3ac ["INT_ADD", "register:40f0:8", ["const:86c3ac:8", "const:4:8"]]
+ 0086c3ac ["CALL", null, ["local:b0:8"]]
- 0086c36c bytes f8ffff97
+ 0086c3ac bytes f8ffff97
- 0086c378 ["INT_ADD", "register:40f0:8", ["const:86c378:8", "const:4:8"]]
- 0086c378 ["CALL", null, ["local:b0:8"]]
+ 0086c3b8 ["INT_ADD", "register:40f0:8", ["const:86c3b8:8", "const:4:8"]]
+ 0086c3b8 ["CALL", null, ["local:b0:8"]]
- 0086c378 bytes f5ffff97
+ 0086c3b8 bytes f5ffff97
~~~


<a id="compare-b8b4118b3b2734e032b3ba9978bd055c"></a>

### [`0086c390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c390.md) → [`0086c3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c3d0.md) FUN_0086c3d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086c390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c390.md) [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 3件 [`0086c390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c390.md) [`0086c3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c3e0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086c3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c3d0.md) [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 3件 [`0086c3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c3d0.md) [`0086c420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c420.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c390.md#insn-0086c3b0) · [`0086c3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c390.md#insn-0086c3bc) · [`0086c3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c390.md#insn-0086c3c8)
- 新版 `0086c3f0`（命令位置の公開資料なし） · `0086c3fc`（命令位置の公開資料なし） · `0086c408`（命令位置の公開資料なし）

~~~diff
- 0086c3b0 ["INT_ADD", "register:40f0:8", ["const:86c3b0:8", "const:4:8"]]
- 0086c3b0 ["CALL", null, ["local:b0:8"]]
+ 0086c3f0 ["INT_ADD", "register:40f0:8", ["const:86c3f0:8", "const:4:8"]]
+ 0086c3f0 ["CALL", null, ["local:b0:8"]]
- 0086c3b0 bytes f8ffff97
+ 0086c3f0 bytes f8ffff97
- 0086c3bc ["INT_ADD", "register:40f0:8", ["const:86c3bc:8", "const:4:8"]]
- 0086c3bc ["CALL", null, ["local:b0:8"]]
+ 0086c3fc ["INT_ADD", "register:40f0:8", ["const:86c3fc:8", "const:4:8"]]
+ 0086c3fc ["CALL", null, ["local:b0:8"]]
- 0086c3bc bytes f5ffff97
+ 0086c3fc bytes f5ffff97
- 0086c3c8 ["INT_ADD", "register:40f0:8", ["const:86c3c8:8", "const:4:8"]]
- 0086c3c8 ["CALL", null, ["callee:0086c420:8"]]
+ 0086c408 ["INT_ADD", "register:40f0:8", ["const:86c408:8", "const:4:8"]]
+ 0086c408 ["CALL", null, ["callee:0086c420:8"]]
- 0086c3c8 bytes 06000094
+ 0086c408 bytes 06000094
~~~


<a id="compare-95b770abec72e66e6ff718427092e518"></a>

### [`0086c3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c3e0.md) → [`0086c420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c420.md) FUN_0086c420

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0086c390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c390.md) [`0086c3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c3e0.md) [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 2件 [`0086c3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c3e0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0086c3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c3d0.md) [`0086c420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c420.md) [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 2件 [`0086c420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c420.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c3e0.md#insn-0086c400) · [`0086c40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c3e0.md#insn-0086c40c)
- 新版 `0086c440`（命令位置の公開資料なし） · `0086c44c`（命令位置の公開資料なし）

~~~diff
- 0086c400 ["INT_ADD", "register:40f0:8", ["const:86c400:8", "const:4:8"]]
- 0086c400 ["CALL", null, ["local:b0:8"]]
+ 0086c440 ["INT_ADD", "register:40f0:8", ["const:86c440:8", "const:4:8"]]
+ 0086c440 ["CALL", null, ["local:b0:8"]]
- 0086c400 bytes f8ffff97
+ 0086c440 bytes f8ffff97
- 0086c40c ["INT_ADD", "register:40f0:8", ["const:86c40c:8", "const:4:8"]]
- 0086c40c ["CALL", null, ["local:b0:8"]]
+ 0086c44c ["INT_ADD", "register:40f0:8", ["const:86c44c:8", "const:4:8"]]
+ 0086c44c ["CALL", null, ["local:b0:8"]]
- 0086c40c bytes f5ffff97
+ 0086c44c bytes f5ffff97
~~~


<a id="compare-406e93a3ddefd96baaeb344d56cc870a"></a>

### [`0086c424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c424.md) → [`0086c464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c464.md) FUN_0086c464

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c424.md#insn-0086c484) · [`0086c494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c424.md#insn-0086c494) · [`0086c4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c424.md#insn-0086c4a4)
- 新版 `0086c4c4`（命令位置の公開資料なし） · `0086c4d4`（命令位置の公開資料なし） · `0086c4e4`（命令位置の公開資料なし）

~~~diff
- 0086c484 ["INT_ADD", "register:40f0:8", ["const:86c484:8", "const:4:8"]]
- 0086c484 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086c4c4 ["INT_ADD", "register:40f0:8", ["const:86c4c4:8", "const:4:8"]]
+ 0086c4c4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086c484 bytes 8bad0f94
+ 0086c4c4 bytes 7bae0f94
- 0086c494 ["INT_ADD", "register:40f0:8", ["const:86c494:8", "const:4:8"]]
- 0086c494 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086c4d4 ["INT_ADD", "register:40f0:8", ["const:86c4d4:8", "const:4:8"]]
+ 0086c4d4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086c494 bytes 87ad0f94
+ 0086c4d4 bytes 77ae0f94
- 0086c4a4 ["INT_ADD", "register:40f0:8", ["const:86c4a4:8", "const:4:8"]]
- 0086c4a4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086c4e4 ["INT_ADD", "register:40f0:8", ["const:86c4e4:8", "const:4:8"]]
+ 0086c4e4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086c4a4 bytes 83ad0f94
+ 0086c4e4 bytes 73ae0f94
~~~


<a id="compare-eceeb01723d0a64aa1ecd26406c09a16"></a>

### [`0086c4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c4d8.md) → [`0086c518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c518.md) FUN_0086c518

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086c4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c4d8.md) · 呼出先 2件 [`0086c4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c4d8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086c518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c518.md) · 呼出先 2件 [`0086c518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c518.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c4d8.md#insn-0086c4f4) · [`0086c500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c4d8.md#insn-0086c500) · [`0086c520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c4d8.md#insn-0086c520)
- 新版 `0086c534`（命令位置の公開資料なし） · `0086c540`（命令位置の公開資料なし） · `0086c560`（命令位置の公開資料なし）

~~~diff
- 0086c4f4 ["INT_ADD", "register:40f0:8", ["const:86c4f4:8", "const:4:8"]]
- 0086c4f4 ["CALL", null, ["local:b0:8"]]
+ 0086c534 ["INT_ADD", "register:40f0:8", ["const:86c534:8", "const:4:8"]]
+ 0086c534 ["CALL", null, ["local:b0:8"]]
- 0086c4f4 bytes f9ffff97
+ 0086c534 bytes f9ffff97
- 0086c500 ["INT_ADD", "register:40f0:8", ["const:86c500:8", "const:4:8"]]
- 0086c500 ["CALL", null, ["local:b0:8"]]
+ 0086c540 ["INT_ADD", "register:40f0:8", ["const:86c540:8", "const:4:8"]]
+ 0086c540 ["CALL", null, ["local:b0:8"]]
- 0086c500 bytes f6ffff97
+ 0086c540 bytes f6ffff97
- 0086c520 ["INT_ADD", "register:40f0:8", ["const:86c520:8", "const:4:8"]]
- 0086c520 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086c560 ["INT_ADD", "register:40f0:8", ["const:86c560:8", "const:4:8"]]
+ 0086c560 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086c520 bytes 64ad0f94
+ 0086c560 bytes 54ae0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33a919b1d9e4461c5b1fd42547c99394"></a>

### [`0086dd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086dd94.md) → [`0086ddd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086ddd4.md) FUN_0086ddd4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0086d6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d6dc.md) · 呼出先 2件 [`0046475c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/0046475c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0086d71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d71c.md) · 呼出先 2件 [`0046479c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/0046479c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086ddb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086dd94.md#insn-0086ddb0)
- 新版 `0086ddf0`（命令位置の公開資料なし）

~~~diff
- 0086ddb0 ["INT_ADD", "register:40f0:8", ["const:86ddb0:8", "const:4:8"]]
- 0086ddb0 ["CALL", null, ["callee:0046479c:8"]]
+ 0086ddf0 ["INT_ADD", "register:40f0:8", ["const:86ddf0:8", "const:4:8"]]
+ 0086ddf0 ["CALL", null, ["callee:0046479c:8"]]
- 0086ddb0 bytes 6bdaef97
+ 0086ddf0 bytes 6bdaef97
~~~


<a id="compare-6ed24e09d15ce69a6e866e6ee10b69b5"></a>

### [`0086ddc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086ddc4.md) → [`0086de04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086de04.md) FUN_0086de04

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044f858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f858.md) [`00c58030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0044f898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f898.md) [`00c58430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086ddec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086ddc4.md#insn-0086ddec) · [`0086ddf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086ddc4.md#insn-0086ddf0) · [`0086ddfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086ddc4.md#insn-0086ddfc)
- 新版 `0086de2c`（命令位置の公開資料なし） · `0086de30`（命令位置の公開資料なし） · `0086de3c`（命令位置の公開資料なし）

~~~diff
- 0086ddec ["INT_ADD", "register:40f0:8", ["const:86ddec:8", "const:4:8"]]
- 0086ddec ["CALL", null, ["callee:00c58430:8"]]
+ 0086de2c ["INT_ADD", "register:40f0:8", ["const:86de2c:8", "const:4:8"]]
+ 0086de2c ["CALL", null, ["callee:00c58430:8"]]
- 0086ddec bytes 91a80f94
+ 0086de2c bytes 81a90f94
- 0086ddf0 ["INT_ADD", "register:40f0:8", ["const:86ddf0:8", "const:4:8"]]
- 0086ddf0 ["CALL", null, ["callee:0044f898:8"]]
+ 0086de30 ["INT_ADD", "register:40f0:8", ["const:86de30:8", "const:4:8"]]
+ 0086de30 ["CALL", null, ["callee:0044f898:8"]]
- 0086ddf0 bytes 9a86ef97
+ 0086de30 bytes 9a86ef97
- 0086ddfc ["COPY", "register:0:8", ["register:4040:8"]]
- 0086ddfc ["INT_ADD", "register:40f0:8", ["const:86ddfc:8", "const:4:8"]]
- 0086ddfc ["CALLIND", null, ["register:0:8"]]
+ 0086de3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0086de3c ["INT_ADD", "register:40f0:8", ["const:86de3c:8", "const:4:8"]]
+ 0086de3c ["CALLIND", null, ["register:0:8"]]
- 0086ddfc bytes 00013fd6
+ 0086de3c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5868aceb88df880e253f49d074bd1cb7"></a>

### [`00870c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870c7c.md) → [`00870cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870cbc.md) FUN_00870cbc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0085d4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085d/0085d4b4.md) [`00870c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870c7c.md) [`00870f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870f7c.md) · 呼出先 4件 [`00870c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870c7c.md) [`00870f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870f7c.md) [`00871214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871214.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 3件 [`0085d4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085d/0085d4f4.md) [`00870cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870cbc.md) [`00870fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870fbc.md) · 呼出先 4件 [`00870cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870cbc.md) [`00870fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870fbc.md) [`00871254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871254.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00870d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870c7c.md#insn-00870d00) · [`00870d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870c7c.md#insn-00870d88) · [`00870dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870c7c.md#insn-00870dcc)
- 新版 `00870d40`（命令位置の公開資料なし） · `00870dc8`（命令位置の公開資料なし） · `00870e0c`（命令位置の公開資料なし）

~~~diff
- 00870d00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00870d00 ["INT_ADD", "register:40f0:8", ["const:870d00:8", "const:4:8"]]
- 00870d00 ["CALLIND", null, ["register:0:8"]]
+ 00870d40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00870d40 ["INT_ADD", "register:40f0:8", ["const:870d40:8", "const:4:8"]]
+ 00870d40 ["CALLIND", null, ["register:0:8"]]
- 00870d00 bytes 00013fd6
+ 00870d40 bytes 00013fd6
- 00870d88 ["COPY", "register:0:8", ["register:4048:8"]]
- 00870d88 ["INT_ADD", "register:40f0:8", ["const:870d88:8", "const:4:8"]]
- 00870d88 ["CALLIND", null, ["register:0:8"]]
+ 00870dc8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00870dc8 ["INT_ADD", "register:40f0:8", ["const:870dc8:8", "const:4:8"]]
+ 00870dc8 ["CALLIND", null, ["register:0:8"]]
- 00870d88 bytes 20013fd6
+ 00870dc8 bytes 20013fd6
- 00870dcc ["COPY", "register:0:8", ["register:4040:8"]]
- 00870dcc ["INT_ADD", "register:40f0:8", ["const:870dcc:8", "const:4:8"]]
- 00870dcc ["CALLIND", null, ["register:0:8"]]
+ 00870e0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00870e0c ["INT_ADD", "register:40f0:8", ["const:870e0c:8", "const:4:8"]]
+ 00870e0c ["CALLIND", null, ["register:0:8"]]
- 00870dcc bytes 00013fd6
+ 00870e0c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46d3816349b57c2a1001a2bd9b1a1e9a"></a>

### [`00870f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870f7c.md) → [`00870fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870fbc.md) FUN_00870fbc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00870c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870c7c.md) · 呼出先 1件 [`00870c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870c7c.md)
- 新版 呼出元 1件 [`00870cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870cbc.md) · 呼出先 1件 [`00870cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870cbc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00870fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870f7c.md#insn-00870fe0) · [`0087106c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870f7c.md#insn-0087106c) · [`008710ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870f7c.md#insn-008710ac)
- 新版 `00871020`（命令位置の公開資料なし） · `008710ac`（命令位置の公開資料なし） · `008710ec`（命令位置の公開資料なし）

~~~diff
- 00870fe0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00870fe0 ["INT_ADD", "register:40f0:8", ["const:870fe0:8", "const:4:8"]]
- 00870fe0 ["CALLIND", null, ["register:0:8"]]
+ 00871020 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00871020 ["INT_ADD", "register:40f0:8", ["const:871020:8", "const:4:8"]]
+ 00871020 ["CALLIND", null, ["register:0:8"]]
- 00870fe0 bytes 00013fd6
+ 00871020 bytes 00013fd6
- 0087106c ["COPY", "register:0:8", ["register:4040:8"]]
- 0087106c ["INT_ADD", "register:40f0:8", ["const:87106c:8", "const:4:8"]]
- 0087106c ["CALLIND", null, ["register:0:8"]]
+ 008710ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 008710ac ["INT_ADD", "register:40f0:8", ["const:8710ac:8", "const:4:8"]]
+ 008710ac ["CALLIND", null, ["register:0:8"]]
- 0087106c bytes 00013fd6
+ 008710ac bytes 00013fd6
- 008710ac ["COPY", "register:0:8", ["register:4040:8"]]
- 008710ac ["INT_ADD", "register:40f0:8", ["const:8710ac:8", "const:4:8"]]
- 008710ac ["CALLIND", null, ["register:0:8"]]
+ 008710ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 008710ec ["INT_ADD", "register:40f0:8", ["const:8710ec:8", "const:4:8"]]
+ 008710ec ["CALLIND", null, ["register:0:8"]]
- 008710ac bytes 00013fd6
+ 008710ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bceb19d02f94355506adb04b1f2d5e76"></a>

### [`00871214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871214.md) → [`00871254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871254.md) FUN_00871254

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00870c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870c7c.md) [`00871214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871214.md) · 呼出先 4件 [`00871214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871214.md) [`008716cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/008716cc.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 2件 [`00870cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870cbc.md) [`00871254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871254.md) · 呼出先 4件 [`00871254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871254.md) [`0087170c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/0087170c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00871294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871214.md#insn-00871294) · [`00871320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871214.md#insn-00871320) · [`008713cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871214.md#insn-008713cc)
- 新版 `008712d4`（命令位置の公開資料なし） · `00871360`（命令位置の公開資料なし） · `0087140c`（命令位置の公開資料なし）

~~~diff
- 00871294 ["COPY", "register:0:8", ["register:4040:8"]]
- 00871294 ["INT_ADD", "register:40f0:8", ["const:871294:8", "const:4:8"]]
- 00871294 ["CALLIND", null, ["register:0:8"]]
+ 008712d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008712d4 ["INT_ADD", "register:40f0:8", ["const:8712d4:8", "const:4:8"]]
+ 008712d4 ["CALLIND", null, ["register:0:8"]]
- 00871294 bytes 00013fd6
+ 008712d4 bytes 00013fd6
- 00871320 ["COPY", "register:0:8", ["register:4040:8"]]
- 00871320 ["INT_ADD", "register:40f0:8", ["const:871320:8", "const:4:8"]]
- 00871320 ["CALLIND", null, ["register:0:8"]]
+ 00871360 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00871360 ["INT_ADD", "register:40f0:8", ["const:871360:8", "const:4:8"]]
+ 00871360 ["CALLIND", null, ["register:0:8"]]
- 00871320 bytes 00013fd6
+ 00871360 bytes 00013fd6
- 008713cc ["COPY", "register:0:8", ["register:40c8:8"]]
- 008713cc ["INT_ADD", "register:40f0:8", ["const:8713cc:8", "const:4:8"]]
- 008713cc ["CALLIND", null, ["register:0:8"]]
+ 0087140c ["COPY", "register:0:8", ["register:40c8:8"]]
+ 0087140c ["INT_ADD", "register:40f0:8", ["const:87140c:8", "const:4:8"]]
+ 0087140c ["CALLIND", null, ["register:0:8"]]
- 008713cc bytes 20033fd6
+ 0087140c bytes 20033fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c67a8a50aeca28b33c4daa87a277148"></a>

### [`008716cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/008716cc.md) → [`0087170c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/0087170c.md) FUN_0087170c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00871214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871214.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00871254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871254.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008717b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/008716cc.md#insn-008717b0) · [`00871808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/008716cc.md#insn-00871808) · [`008718ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/008716cc.md#insn-008718ec)
- 新版 `008717f0`（命令位置の公開資料なし） · `00871848`（命令位置の公開資料なし） · `0087192c`（命令位置の公開資料なし）

~~~diff
- 008717b0 ["INT_ADD", "register:40f0:8", ["const:8717b0:8", "const:4:8"]]
- 008717b0 ["CALL", null, ["callee:00c57f40:8"]]
+ 008717f0 ["INT_ADD", "register:40f0:8", ["const:8717f0:8", "const:4:8"]]
+ 008717f0 ["CALL", null, ["callee:00c57f40:8"]]
- 008717b0 bytes e4980f94
+ 008717f0 bytes d4990f94
- 00871808 ["INT_ADD", "register:40f0:8", ["const:871808:8", "const:4:8"]]
- 00871808 ["CALL", null, ["callee:00c57f40:8"]]
+ 00871848 ["INT_ADD", "register:40f0:8", ["const:871848:8", "const:4:8"]]
+ 00871848 ["CALL", null, ["callee:00c57f40:8"]]
- 00871808 bytes ce980f94
+ 00871848 bytes be990f94
- 008718ec ["INT_ADD", "register:40f0:8", ["const:8718ec:8", "const:4:8"]]
- 008718ec ["CALL", null, ["callee:00c57ee0:8"]]
+ 0087192c ["INT_ADD", "register:40f0:8", ["const:87192c:8", "const:4:8"]]
+ 0087192c ["CALL", null, ["callee:00c57ee0:8"]]
- 008718ec bytes 7d980f94
+ 0087192c bytes 6d990f94
~~~


<a id="compare-04cddfa4d6e40889c3ec68d9aeffa781"></a>

### [`00871b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871b78.md) → [`00871bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871bb8.md) FUN_00871bb8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0086151c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00861/0086151c.md) [`008fc454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fc/008fc454.md) [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) [`00a3a8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3a/00a3a8d0.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 5件 [`0086155c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00861/0086155c.md) [`008c5208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c5/008c5208.md) [`008fc5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fc/008fc5f0.md) [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) [`00a3aac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3aac8.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00871cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871b78.md#insn-00871cb8) · [`00871d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871b78.md#insn-00871d74) · [`00871d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871b78.md#insn-00871d98)
- 新版 `00871cf8`（命令位置の公開資料なし） · `00871db4`（命令位置の公開資料なし） · `00871dd8`（命令位置の公開資料なし）

~~~diff
- 00871cb8 ["INT_ADD", "register:40f0:8", ["const:871cb8:8", "const:4:8"]]
- 00871cb8 ["CALL", null, ["callee:0043bba4:8"]]
+ 00871cf8 ["INT_ADD", "register:40f0:8", ["const:871cf8:8", "const:4:8"]]
+ 00871cf8 ["CALL", null, ["callee:0043bba4:8"]]
- 00871cb8 bytes ab27ef97
+ 00871cf8 bytes ab27ef97
- 00871d74 ["INT_ADD", "register:40f0:8", ["const:871d74:8", "const:4:8"]]
- 00871d74 ["CALL", null, ["callee:005c179c:8"]]
+ 00871db4 ["INT_ADD", "register:40f0:8", ["const:871db4:8", "const:4:8"]]
+ 00871db4 ["CALL", null, ["callee:005c179c:8"]]
- 00871d74 bytes 7a3ef597
+ 00871db4 bytes 7a3ef597
- 00871d98 ["INT_ADD", "register:40f0:8", ["const:871d98:8", "const:4:8"]]
- 00871d98 ["CALL", null, ["callee:005c179c:8"]]
+ 00871dd8 ["INT_ADD", "register:40f0:8", ["const:871dd8:8", "const:4:8"]]
+ 00871dd8 ["CALL", null, ["callee:005c179c:8"]]
- 00871d98 bytes 713ef597
+ 00871dd8 bytes 713ef597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48e7f76bb2e0393ecff69f8c95a2ef5c"></a>

### [`00871fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871fac.md) → [`00871fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871fec.md) FUN_00871fec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008650d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/008650d0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00865110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865110.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00871fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871fac.md#insn-00871fcc)
- 新版 `0087200c`（命令位置の公開資料なし）

~~~diff
- 00871fcc ["INT_ADD", "register:40f0:8", ["const:871fcc:8", "const:4:8"]]
- 00871fcc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0087200c ["INT_ADD", "register:40f0:8", ["const:87200c:8", "const:4:8"]]
+ 0087200c ["CALL", null, ["callee:00c57eb0:8"]]
- 00871fcc bytes b9960f94
+ 0087200c bytes a9970f94
~~~


<a id="compare-fd368da6ac8185450dd15168c47476af"></a>

### [`008721dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008721dc.md) → [`0087221c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/0087221c.md) FUN_0087221c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008650d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/008650d0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00865110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865110.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008721fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008721dc.md#insn-008721fc)
- 新版 `0087223c`（命令位置の公開資料なし）

~~~diff
- 008721fc ["INT_ADD", "register:40f0:8", ["const:8721fc:8", "const:4:8"]]
- 008721fc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0087223c ["INT_ADD", "register:40f0:8", ["const:87223c:8", "const:4:8"]]
+ 0087223c ["CALL", null, ["callee:00c57eb0:8"]]
- 008721fc bytes 2d960f94
+ 0087223c bytes 1d970f94
~~~


<a id="compare-3a5f07ef708ed125de9cfcd2d20e87ee"></a>

### [`008729ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008729ac.md) → [`008729ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/008729ec.md) FUN_008729ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00872560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872560.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`008725a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/008725a0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008729bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008729ac.md#insn-008729bc)
- 新版 `008729fc`（命令位置の公開資料なし）

~~~diff
- 008729bc ["INT_ADD", "register:40f0:8", ["const:8729bc:8", "const:4:8"]]
- 008729bc ["CALL", null, ["callee:008725a0:8"]]
+ 008729fc ["INT_ADD", "register:40f0:8", ["const:8729fc:8", "const:4:8"]]
+ 008729fc ["CALL", null, ["callee:008725a0:8"]]
- 008729bc bytes e9feff97
+ 008729fc bytes e9feff97
~~~


<a id="compare-141d7c2cce1b17ac40e73871e21ea09f"></a>

### [`0087434c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/0087434c.md) → [`0087438c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/0087438c.md) FUN_0087438c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00874368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/0087434c.md#insn-00874368) · [`00874388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/0087434c.md#insn-00874388)
- 新版 `008743a8`（命令位置の公開資料なし） · `008743c8`（命令位置の公開資料なし）

~~~diff
- 00874368 ["INT_ADD", "register:40f0:8", ["const:874368:8", "const:4:8"]]
- 00874368 ["CALL", null, ["callee:00c53d00:8"]]
+ 008743a8 ["INT_ADD", "register:40f0:8", ["const:8743a8:8", "const:4:8"]]
+ 008743a8 ["CALL", null, ["callee:00c53d00:8"]]
- 00874368 bytes 5e7d0f94
+ 008743a8 bytes 567e0f94
- 00874388 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874388 ["INT_ADD", "register:40f0:8", ["const:874388:8", "const:4:8"]]
- 00874388 ["CALLIND", null, ["register:0:8"]]
+ 008743c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008743c8 ["INT_ADD", "register:40f0:8", ["const:8743c8:8", "const:4:8"]]
+ 008743c8 ["CALLIND", null, ["register:0:8"]]
- 00874388 bytes 00013fd6
+ 008743c8 bytes 00013fd6
~~~


<a id="compare-17a0c3f7c4a52a3ce66810aae97c139f"></a>

### [`0087439c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/0087439c.md) → [`008743dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008743dc.md) FUN_008743dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008743b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/0087439c.md#insn-008743b8) · [`008743d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/0087439c.md#insn-008743d8)
- 新版 `008743f8`（命令位置の公開資料なし） · `00874418`（命令位置の公開資料なし）

~~~diff
- 008743b8 ["INT_ADD", "register:40f0:8", ["const:8743b8:8", "const:4:8"]]
- 008743b8 ["CALL", null, ["callee:00c53d00:8"]]
+ 008743f8 ["INT_ADD", "register:40f0:8", ["const:8743f8:8", "const:4:8"]]
+ 008743f8 ["CALL", null, ["callee:00c53d00:8"]]
- 008743b8 bytes 4a7d0f94
+ 008743f8 bytes 427e0f94
- 008743d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008743d8 ["INT_ADD", "register:40f0:8", ["const:8743d8:8", "const:4:8"]]
- 008743d8 ["CALLIND", null, ["register:0:8"]]
+ 00874418 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874418 ["INT_ADD", "register:40f0:8", ["const:874418:8", "const:4:8"]]
+ 00874418 ["CALLIND", null, ["register:0:8"]]
- 008743d8 bytes 00013fd6
+ 00874418 bytes 00013fd6
~~~


<a id="compare-66c0f1fc8f2c535eef29500cc043723c"></a>

### [`00874538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874538.md) → [`00874578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874578.md) FUN_00874578

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00873a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873a68.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00873aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873aa8.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00874554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874538.md#insn-00874554) · [`00874574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874538.md#insn-00874574)
- 新版 `00874594`（命令位置の公開資料なし） · `008745b4`（命令位置の公開資料なし）

~~~diff
- 00874554 ["INT_ADD", "register:40f0:8", ["const:874554:8", "const:4:8"]]
- 00874554 ["CALL", null, ["callee:00c53d00:8"]]
+ 00874594 ["INT_ADD", "register:40f0:8", ["const:874594:8", "const:4:8"]]
+ 00874594 ["CALL", null, ["callee:00c53d00:8"]]
- 00874554 bytes e37c0f94
+ 00874594 bytes db7d0f94
- 00874574 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874574 ["INT_ADD", "register:40f0:8", ["const:874574:8", "const:4:8"]]
- 00874574 ["CALLIND", null, ["register:0:8"]]
+ 008745b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008745b4 ["INT_ADD", "register:40f0:8", ["const:8745b4:8", "const:4:8"]]
+ 008745b4 ["CALLIND", null, ["register:0:8"]]
- 00874574 bytes 00013fd6
+ 008745b4 bytes 00013fd6
~~~


<a id="compare-e585eecfbcc26c727834dc385839a9bf"></a>

### [`00874588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874588.md) → [`008745c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008745c8.md) FUN_008745c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00873a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873a68.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00873aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873aa8.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008745a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874588.md#insn-008745a8) · [`008745bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874588.md#insn-008745bc) · [`008745c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874588.md#insn-008745c4)
- 新版 `008745e8`（命令位置の公開資料なし） · `008745fc`（命令位置の公開資料なし） · `00874604`（命令位置の公開資料なし）

~~~diff
- 008745a8 ["INT_ADD", "register:40f0:8", ["const:8745a8:8", "const:4:8"]]
- 008745a8 ["CALL", null, ["callee:00c53d00:8"]]
+ 008745e8 ["INT_ADD", "register:40f0:8", ["const:8745e8:8", "const:4:8"]]
+ 008745e8 ["CALL", null, ["callee:00c53d00:8"]]
- 008745a8 bytes ce7c0f94
+ 008745e8 bytes c67d0f94
- 008745bc ["COPY", "register:0:8", ["register:4040:8"]]
- 008745bc ["INT_ADD", "register:40f0:8", ["const:8745bc:8", "const:4:8"]]
- 008745bc ["CALLIND", null, ["register:0:8"]]
+ 008745fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008745fc ["INT_ADD", "register:40f0:8", ["const:8745fc:8", "const:4:8"]]
+ 008745fc ["CALLIND", null, ["register:0:8"]]
- 008745bc bytes 00013fd6
+ 008745fc bytes 00013fd6
- 008745c4 ["INT_ADD", "register:40f0:8", ["const:8745c4:8", "const:4:8"]]
- 008745c4 ["CALL", null, ["callee:00c57e80:8"]]
+ 00874604 ["INT_ADD", "register:40f0:8", ["const:874604:8", "const:4:8"]]
+ 00874604 ["CALL", null, ["callee:00c57e80:8"]]
- 008745c4 bytes 2f8d0f94
+ 00874604 bytes 1f8e0f94
~~~


<a id="compare-50eeadb5c1dcb6344a148832e97c0fb2"></a>

### [`008745d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008745d8.md) → [`00874618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874618.md) FUN_00874618

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`008746a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008746a8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`008746e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008746e8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087461c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008745d8.md#insn-0087461c) · [`0087462c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008745d8.md#insn-0087462c) · [`0087467c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008745d8.md#insn-0087467c)
- 新版 `0087465c`（命令位置の公開資料なし） · `0087466c`（命令位置の公開資料なし） · `008746bc`（命令位置の公開資料なし）

~~~diff
- 0087461c ["INT_ADD", "register:40f0:8", ["const:87461c:8", "const:4:8"]]
- 0087461c ["CALL", null, ["callee:008746e8:8"]]
+ 0087465c ["INT_ADD", "register:40f0:8", ["const:87465c:8", "const:4:8"]]
+ 0087465c ["CALL", null, ["callee:008746e8:8"]]
- 0087461c bytes 23000094
+ 0087465c bytes 23000094
- 0087462c ["INT_ADD", "register:40f0:8", ["const:87462c:8", "const:4:8"]]
- 0087462c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0087466c ["INT_ADD", "register:40f0:8", ["const:87466c:8", "const:4:8"]]
+ 0087466c ["CALL", null, ["callee:00c57eb0:8"]]
- 0087462c bytes 218d0f94
+ 0087466c bytes 118e0f94
- 0087467c ["INT_ADD", "register:40f0:8", ["const:87467c:8", "const:4:8"]]
- 0087467c ["CALL", null, ["callee:00c57ee0:8"]]
+ 008746bc ["INT_ADD", "register:40f0:8", ["const:8746bc:8", "const:4:8"]]
+ 008746bc ["CALL", null, ["callee:00c57ee0:8"]]
- 0087467c bytes 198d0f94
+ 008746bc bytes 098e0f94
~~~


<a id="compare-8769adde9e135ece55b0561f4db246f5"></a>

### [`00874858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874858.md) → [`00874898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874898.md) FUN_00874898

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00874874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874858.md#insn-00874874) · [`00874894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874858.md#insn-00874894)
- 新版 `008748b4`（命令位置の公開資料なし） · `008748d4`（命令位置の公開資料なし）

~~~diff
- 00874874 ["INT_ADD", "register:40f0:8", ["const:874874:8", "const:4:8"]]
- 00874874 ["CALL", null, ["callee:00c53d00:8"]]
+ 008748b4 ["INT_ADD", "register:40f0:8", ["const:8748b4:8", "const:4:8"]]
+ 008748b4 ["CALL", null, ["callee:00c53d00:8"]]
- 00874874 bytes 1b7c0f94
+ 008748b4 bytes 137d0f94
- 00874894 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874894 ["INT_ADD", "register:40f0:8", ["const:874894:8", "const:4:8"]]
- 00874894 ["CALLIND", null, ["register:0:8"]]
+ 008748d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008748d4 ["INT_ADD", "register:40f0:8", ["const:8748d4:8", "const:4:8"]]
+ 008748d4 ["CALLIND", null, ["register:0:8"]]
- 00874894 bytes 00013fd6
+ 008748d4 bytes 00013fd6
~~~


<a id="compare-5648361675167e012cbbff2f438aadd7"></a>

### [`008749f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008749f4.md) → [`00874a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874a34.md) FUN_00874a34

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008746a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008746a8.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`008746e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008746e8.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00874a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008749f4.md#insn-00874a10) · [`00874a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008749f4.md#insn-00874a30)
- 新版 `00874a50`（命令位置の公開資料なし） · `00874a70`（命令位置の公開資料なし）

~~~diff
- 00874a10 ["INT_ADD", "register:40f0:8", ["const:874a10:8", "const:4:8"]]
- 00874a10 ["CALL", null, ["callee:00c53d00:8"]]
+ 00874a50 ["INT_ADD", "register:40f0:8", ["const:874a50:8", "const:4:8"]]
+ 00874a50 ["CALL", null, ["callee:00c53d00:8"]]
- 00874a10 bytes b47b0f94
+ 00874a50 bytes ac7c0f94
- 00874a30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874a30 ["INT_ADD", "register:40f0:8", ["const:874a30:8", "const:4:8"]]
- 00874a30 ["CALLIND", null, ["register:0:8"]]
+ 00874a70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874a70 ["INT_ADD", "register:40f0:8", ["const:874a70:8", "const:4:8"]]
+ 00874a70 ["CALLIND", null, ["register:0:8"]]
- 00874a30 bytes 00013fd6
+ 00874a70 bytes 00013fd6
~~~


<a id="compare-8fe0bfe353ef1faac1da8ea41eff201b"></a>

### [`00874a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874a44.md) → [`00874a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874a84.md) FUN_00874a84

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008746a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008746a8.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`008746e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008746e8.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00874a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874a44.md#insn-00874a64) · [`00874a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874a44.md#insn-00874a78) · [`00874a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874a44.md#insn-00874a80)
- 新版 `00874aa4`（命令位置の公開資料なし） · `00874ab8`（命令位置の公開資料なし） · `00874ac0`（命令位置の公開資料なし）

~~~diff
- 00874a64 ["INT_ADD", "register:40f0:8", ["const:874a64:8", "const:4:8"]]
- 00874a64 ["CALL", null, ["callee:00c53d00:8"]]
+ 00874aa4 ["INT_ADD", "register:40f0:8", ["const:874aa4:8", "const:4:8"]]
+ 00874aa4 ["CALL", null, ["callee:00c53d00:8"]]
- 00874a64 bytes 9f7b0f94
+ 00874aa4 bytes 977c0f94
- 00874a78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874a78 ["INT_ADD", "register:40f0:8", ["const:874a78:8", "const:4:8"]]
- 00874a78 ["CALLIND", null, ["register:0:8"]]
+ 00874ab8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874ab8 ["INT_ADD", "register:40f0:8", ["const:874ab8:8", "const:4:8"]]
+ 00874ab8 ["CALLIND", null, ["register:0:8"]]
- 00874a78 bytes 00013fd6
+ 00874ab8 bytes 00013fd6
- 00874a80 ["INT_ADD", "register:40f0:8", ["const:874a80:8", "const:4:8"]]
- 00874a80 ["CALL", null, ["callee:00c57e80:8"]]
+ 00874ac0 ["INT_ADD", "register:40f0:8", ["const:874ac0:8", "const:4:8"]]
+ 00874ac0 ["CALL", null, ["callee:00c57e80:8"]]
- 00874a80 bytes 008c0f94
+ 00874ac0 bytes f08c0f94
~~~


<a id="compare-1c1691db2e225b25697111b10a095437"></a>

### [`00874acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874acc.md) → [`00874b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874b0c.md) FUN_00874b0c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00874ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874acc.md#insn-00874ae8) · [`00874b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874acc.md#insn-00874b08)
- 新版 `00874b28`（命令位置の公開資料なし） · `00874b48`（命令位置の公開資料なし）

~~~diff
- 00874ae8 ["INT_ADD", "register:40f0:8", ["const:874ae8:8", "const:4:8"]]
- 00874ae8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00874b28 ["INT_ADD", "register:40f0:8", ["const:874b28:8", "const:4:8"]]
+ 00874b28 ["CALL", null, ["callee:00c53d00:8"]]
- 00874ae8 bytes 7e7b0f94
+ 00874b28 bytes 767c0f94
- 00874b08 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874b08 ["INT_ADD", "register:40f0:8", ["const:874b08:8", "const:4:8"]]
- 00874b08 ["CALLIND", null, ["register:0:8"]]
+ 00874b48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874b48 ["INT_ADD", "register:40f0:8", ["const:874b48:8", "const:4:8"]]
+ 00874b48 ["CALLIND", null, ["register:0:8"]]
- 00874b08 bytes 00013fd6
+ 00874b48 bytes 00013fd6
~~~


<a id="compare-a6a4d8ee4648d7a2f6979374a6f67a2b"></a>

### [`00874c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874c68.md) → [`00874ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874ca8.md) FUN_00874ca8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00873c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873c10.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00873c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873c50.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00874c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874c68.md#insn-00874c84) · [`00874ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874c68.md#insn-00874ca4)
- 新版 `00874cc4`（命令位置の公開資料なし） · `00874ce4`（命令位置の公開資料なし）

~~~diff
- 00874c84 ["INT_ADD", "register:40f0:8", ["const:874c84:8", "const:4:8"]]
- 00874c84 ["CALL", null, ["callee:00c53d00:8"]]
+ 00874cc4 ["INT_ADD", "register:40f0:8", ["const:874cc4:8", "const:4:8"]]
+ 00874cc4 ["CALL", null, ["callee:00c53d00:8"]]
- 00874c84 bytes 177b0f94
+ 00874cc4 bytes 0f7c0f94
- 00874ca4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874ca4 ["INT_ADD", "register:40f0:8", ["const:874ca4:8", "const:4:8"]]
- 00874ca4 ["CALLIND", null, ["register:0:8"]]
+ 00874ce4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874ce4 ["INT_ADD", "register:40f0:8", ["const:874ce4:8", "const:4:8"]]
+ 00874ce4 ["CALLIND", null, ["register:0:8"]]
- 00874ca4 bytes 00013fd6
+ 00874ce4 bytes 00013fd6
~~~


<a id="compare-c8a488f549ee077bc09a679f7fe086c1"></a>

### [`00874cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874cb8.md) → [`00874cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874cf8.md) FUN_00874cf8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00873c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873c10.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00873c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873c50.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00874cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874cb8.md#insn-00874cd8) · [`00874cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874cb8.md#insn-00874cec) · [`00874cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874cb8.md#insn-00874cf4)
- 新版 `00874d18`（命令位置の公開資料なし） · `00874d2c`（命令位置の公開資料なし） · `00874d34`（命令位置の公開資料なし）

~~~diff
- 00874cd8 ["INT_ADD", "register:40f0:8", ["const:874cd8:8", "const:4:8"]]
- 00874cd8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00874d18 ["INT_ADD", "register:40f0:8", ["const:874d18:8", "const:4:8"]]
+ 00874d18 ["CALL", null, ["callee:00c53d00:8"]]
- 00874cd8 bytes 027b0f94
+ 00874d18 bytes fa7b0f94
- 00874cec ["COPY", "register:0:8", ["register:4040:8"]]
- 00874cec ["INT_ADD", "register:40f0:8", ["const:874cec:8", "const:4:8"]]
- 00874cec ["CALLIND", null, ["register:0:8"]]
+ 00874d2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874d2c ["INT_ADD", "register:40f0:8", ["const:874d2c:8", "const:4:8"]]
+ 00874d2c ["CALLIND", null, ["register:0:8"]]
- 00874cec bytes 00013fd6
+ 00874d2c bytes 00013fd6
- 00874cf4 ["INT_ADD", "register:40f0:8", ["const:874cf4:8", "const:4:8"]]
- 00874cf4 ["CALL", null, ["callee:00c57e80:8"]]
+ 00874d34 ["INT_ADD", "register:40f0:8", ["const:874d34:8", "const:4:8"]]
+ 00874d34 ["CALL", null, ["callee:00c57e80:8"]]
- 00874cf4 bytes 638b0f94
+ 00874d34 bytes 538c0f94
~~~


<a id="compare-d6143ce0af17ea74e80080fd4f6f9ed9"></a>

### [`00874f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874f04.md) → [`00874f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874f44.md) FUN_00874f44

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00874f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874f04.md#insn-00874f20) · [`00874f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874f04.md#insn-00874f40)
- 新版 `00874f60`（命令位置の公開資料なし） · `00874f80`（命令位置の公開資料なし）

~~~diff
- 00874f20 ["INT_ADD", "register:40f0:8", ["const:874f20:8", "const:4:8"]]
- 00874f20 ["CALL", null, ["callee:00c53d00:8"]]
+ 00874f60 ["INT_ADD", "register:40f0:8", ["const:874f60:8", "const:4:8"]]
+ 00874f60 ["CALL", null, ["callee:00c53d00:8"]]
- 00874f20 bytes 707a0f94
+ 00874f60 bytes 687b0f94
- 00874f40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874f40 ["INT_ADD", "register:40f0:8", ["const:874f40:8", "const:4:8"]]
- 00874f40 ["CALLIND", null, ["register:0:8"]]
+ 00874f80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874f80 ["INT_ADD", "register:40f0:8", ["const:874f80:8", "const:4:8"]]
+ 00874f80 ["CALLIND", null, ["register:0:8"]]
- 00874f40 bytes 00013fd6
+ 00874f80 bytes 00013fd6
~~~


<a id="compare-7bcd31e8d8bdd375b070ca3215b08c75"></a>

### [`008750a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/008750a0.md) → [`008750e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008750e0.md) FUN_008750e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00873d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873d88.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00873dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873dc8.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008750bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/008750a0.md#insn-008750bc) · [`008750dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/008750a0.md#insn-008750dc)
- 新版 `008750fc`（命令位置の公開資料なし） · `0087511c`（命令位置の公開資料なし）

~~~diff
- 008750bc ["INT_ADD", "register:40f0:8", ["const:8750bc:8", "const:4:8"]]
- 008750bc ["CALL", null, ["callee:00c53d00:8"]]
+ 008750fc ["INT_ADD", "register:40f0:8", ["const:8750fc:8", "const:4:8"]]
+ 008750fc ["CALL", null, ["callee:00c53d00:8"]]
- 008750bc bytes 097a0f94
+ 008750fc bytes 017b0f94
- 008750dc ["COPY", "register:0:8", ["register:4040:8"]]
- 008750dc ["INT_ADD", "register:40f0:8", ["const:8750dc:8", "const:4:8"]]
- 008750dc ["CALLIND", null, ["register:0:8"]]
+ 0087511c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087511c ["INT_ADD", "register:40f0:8", ["const:87511c:8", "const:4:8"]]
+ 0087511c ["CALLIND", null, ["register:0:8"]]
- 008750dc bytes 00013fd6
+ 0087511c bytes 00013fd6
~~~


<a id="compare-c539dfcf1c047d40a12c0634ff843fc1"></a>

### [`008750f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/008750f0.md) → [`00875130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875130.md) FUN_00875130

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00873d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873d88.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00873dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873dc8.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00875110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/008750f0.md#insn-00875110) · [`00875124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/008750f0.md#insn-00875124) · [`0087512c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/008750f0.md#insn-0087512c)
- 新版 `00875150`（命令位置の公開資料なし） · `00875164`（命令位置の公開資料なし） · `0087516c`（命令位置の公開資料なし）

~~~diff
- 00875110 ["INT_ADD", "register:40f0:8", ["const:875110:8", "const:4:8"]]
- 00875110 ["CALL", null, ["callee:00c53d00:8"]]
+ 00875150 ["INT_ADD", "register:40f0:8", ["const:875150:8", "const:4:8"]]
+ 00875150 ["CALL", null, ["callee:00c53d00:8"]]
- 00875110 bytes f4790f94
+ 00875150 bytes ec7a0f94
- 00875124 ["COPY", "register:0:8", ["register:4040:8"]]
- 00875124 ["INT_ADD", "register:40f0:8", ["const:875124:8", "const:4:8"]]
- 00875124 ["CALLIND", null, ["register:0:8"]]
+ 00875164 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00875164 ["INT_ADD", "register:40f0:8", ["const:875164:8", "const:4:8"]]
+ 00875164 ["CALLIND", null, ["register:0:8"]]
- 00875124 bytes 00013fd6
+ 00875164 bytes 00013fd6
- 0087512c ["INT_ADD", "register:40f0:8", ["const:87512c:8", "const:4:8"]]
- 0087512c ["CALL", null, ["callee:00c57e80:8"]]
+ 0087516c ["INT_ADD", "register:40f0:8", ["const:87516c:8", "const:4:8"]]
+ 0087516c ["CALL", null, ["callee:00c57e80:8"]]
- 0087512c bytes 558a0f94
+ 0087516c bytes 458b0f94
~~~


<a id="compare-7821a2a033d870b5203831007ed3422a"></a>

### [`0087539c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/0087539c.md) → [`008753dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008753dc.md) FUN_008753dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00873f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873f00.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`008755dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/008755dc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00873f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873f40.md) · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0087561c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/0087561c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087542c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/0087539c.md#insn-0087542c) · [`00875488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/0087539c.md#insn-00875488) · [`008754d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/0087539c.md#insn-008754d8)
- 新版 `0087546c`（命令位置の公開資料なし） · `008754c8`（命令位置の公開資料なし） · `00875518`（命令位置の公開資料なし）

~~~diff
- 0087542c ["INT_ADD", "register:40f0:8", ["const:87542c:8", "const:4:8"]]
- 0087542c ["CALL", null, ["callee:00c58050:8"]]
+ 0087546c ["INT_ADD", "register:40f0:8", ["const:87546c:8", "const:4:8"]]
+ 0087546c ["CALL", null, ["callee:00c58050:8"]]
- 0087542c bytes 098a0f94
+ 0087546c bytes f98a0f94
- 00875488 ["INT_ADD", "register:40f0:8", ["const:875488:8", "const:4:8"]]
- 00875488 ["CALL", null, ["callee:00c58050:8"]]
+ 008754c8 ["INT_ADD", "register:40f0:8", ["const:8754c8:8", "const:4:8"]]
+ 008754c8 ["CALL", null, ["callee:00c58050:8"]]
- 00875488 bytes f2890f94
+ 008754c8 bytes e28a0f94
- 008754d8 ["INT_ADD", "register:40f0:8", ["const:8754d8:8", "const:4:8"]]
- 008754d8 ["CALL", null, ["callee:0087561c:8"]]
+ 00875518 ["INT_ADD", "register:40f0:8", ["const:875518:8", "const:4:8"]]
+ 00875518 ["CALL", null, ["callee:0087561c:8"]]
- 008754d8 bytes 41000094
+ 00875518 bytes 41000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14bd069512cfdad51f2dd7af9973d00e"></a>

### [`0087558c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/0087558c.md) → [`008755cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008755cc.md) FUN_008755cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008755a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/0087558c.md#insn-008755a8) · [`008755c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/0087558c.md#insn-008755c8)
- 新版 `008755e8`（命令位置の公開資料なし） · `00875608`（命令位置の公開資料なし）

~~~diff
- 008755a8 ["INT_ADD", "register:40f0:8", ["const:8755a8:8", "const:4:8"]]
- 008755a8 ["CALL", null, ["callee:00c53d00:8"]]
+ 008755e8 ["INT_ADD", "register:40f0:8", ["const:8755e8:8", "const:4:8"]]
+ 008755e8 ["CALL", null, ["callee:00c53d00:8"]]
- 008755a8 bytes ce780f94
+ 008755e8 bytes c6790f94
- 008755c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008755c8 ["INT_ADD", "register:40f0:8", ["const:8755c8:8", "const:4:8"]]
- 008755c8 ["CALLIND", null, ["register:0:8"]]
+ 00875608 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00875608 ["INT_ADD", "register:40f0:8", ["const:875608:8", "const:4:8"]]
+ 00875608 ["CALLIND", null, ["register:0:8"]]
- 008755c8 bytes 00013fd6
+ 00875608 bytes 00013fd6
~~~


<a id="compare-7d3cbb2070fec78fabe3b7d1aa1b4948"></a>

### [`008755dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/008755dc.md) → [`0087561c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/0087561c.md) FUN_0087561c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0087539c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/0087539c.md) · 呼出先 2件 [`00875878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875878.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`008753dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008753dc.md) · 呼出先 2件 [`008758b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008758b8.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00875664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/008755dc.md#insn-00875664) · [`008756b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/008755dc.md#insn-008756b8) · [`00875754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/008755dc.md#insn-00875754)
- 新版 `008756a4`（命令位置の公開資料なし） · `008756f8`（命令位置の公開資料なし） · `00875794`（命令位置の公開資料なし）

~~~diff
- 00875664 ["INT_ADD", "register:40f0:8", ["const:875664:8", "const:4:8"]]
- 00875664 ["CALL", null, ["callee:00c58050:8"]]
+ 008756a4 ["INT_ADD", "register:40f0:8", ["const:8756a4:8", "const:4:8"]]
+ 008756a4 ["CALL", null, ["callee:00c58050:8"]]
- 00875664 bytes 7b890f94
+ 008756a4 bytes 6b8a0f94
- 008756b8 ["INT_ADD", "register:40f0:8", ["const:8756b8:8", "const:4:8"]]
- 008756b8 ["CALL", null, ["callee:00c58050:8"]]
+ 008756f8 ["INT_ADD", "register:40f0:8", ["const:8756f8:8", "const:4:8"]]
+ 008756f8 ["CALL", null, ["callee:00c58050:8"]]
- 008756b8 bytes 66890f94
+ 008756f8 bytes 568a0f94
- 00875754 ["INT_ADD", "register:40f0:8", ["const:875754:8", "const:4:8"]]
- 00875754 ["CALL", null, ["callee:00c58050:8"]]
+ 00875794 ["INT_ADD", "register:40f0:8", ["const:875794:8", "const:4:8"]]
+ 00875794 ["CALL", null, ["callee:00c58050:8"]]
- 00875754 bytes 3f890f94
+ 00875794 bytes 2f8a0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd2e174efc74de6a59806c0a13b3c3b9"></a>

### [`00875878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875878.md) → [`008758b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008758b8.md) FUN_008758b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008755dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/008755dc.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`0087561c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/0087561c.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008758fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875878.md#insn-008758fc) · [`00875928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875878.md#insn-00875928)
- 新版 `0087593c`（命令位置の公開資料なし） · `00875968`（命令位置の公開資料なし）

~~~diff
- 008758fc ["INT_ADD", "register:40f0:8", ["const:8758fc:8", "const:4:8"]]
- 008758fc ["CALL", null, ["callee:00c58050:8"]]
+ 0087593c ["INT_ADD", "register:40f0:8", ["const:87593c:8", "const:4:8"]]
+ 0087593c ["CALL", null, ["callee:00c58050:8"]]
- 008758fc bytes d5880f94
+ 0087593c bytes c5890f94
- 00875928 ["INT_ADD", "register:40f0:8", ["const:875928:8", "const:4:8"]]
- 00875928 ["CALL", null, ["callee:00c58050:8"]]
+ 00875968 ["INT_ADD", "register:40f0:8", ["const:875968:8", "const:4:8"]]
+ 00875968 ["CALL", null, ["callee:00c58050:8"]]
- 00875928 bytes ca880f94
+ 00875968 bytes ba890f94
~~~


<a id="compare-096fe90b4c331ab964f7562adeea9586"></a>

### [`00875b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875b64.md) → [`00875ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875ba4.md) FUN_00875ba4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00873f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873f00.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00873f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873f40.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00875b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875b64.md#insn-00875b80) · [`00875ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875b64.md#insn-00875ba0)
- 新版 `00875bc0`（命令位置の公開資料なし） · `00875be0`（命令位置の公開資料なし）

~~~diff
- 00875b80 ["INT_ADD", "register:40f0:8", ["const:875b80:8", "const:4:8"]]
- 00875b80 ["CALL", null, ["callee:00c53d00:8"]]
+ 00875bc0 ["INT_ADD", "register:40f0:8", ["const:875bc0:8", "const:4:8"]]
+ 00875bc0 ["CALL", null, ["callee:00c53d00:8"]]
- 00875b80 bytes 58770f94
+ 00875bc0 bytes 50780f94
- 00875ba0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00875ba0 ["INT_ADD", "register:40f0:8", ["const:875ba0:8", "const:4:8"]]
- 00875ba0 ["CALLIND", null, ["register:0:8"]]
+ 00875be0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00875be0 ["INT_ADD", "register:40f0:8", ["const:875be0:8", "const:4:8"]]
+ 00875be0 ["CALLIND", null, ["register:0:8"]]
- 00875ba0 bytes 00013fd6
+ 00875be0 bytes 00013fd6
~~~


<a id="compare-c8941fad894524cc5a8dbcad05be0919"></a>

### [`00875bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875bb4.md) → [`00875bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875bf4.md) FUN_00875bf4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00873f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873f00.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00873f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873f40.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00875bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875bb4.md#insn-00875bd4) · [`00875be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875bb4.md#insn-00875be8) · [`00875bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875bb4.md#insn-00875bf0)
- 新版 `00875c14`（命令位置の公開資料なし） · `00875c28`（命令位置の公開資料なし） · `00875c30`（命令位置の公開資料なし）

~~~diff
- 00875bd4 ["INT_ADD", "register:40f0:8", ["const:875bd4:8", "const:4:8"]]
- 00875bd4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00875c14 ["INT_ADD", "register:40f0:8", ["const:875c14:8", "const:4:8"]]
+ 00875c14 ["CALL", null, ["callee:00c53d00:8"]]
- 00875bd4 bytes 43770f94
+ 00875c14 bytes 3b780f94
- 00875be8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00875be8 ["INT_ADD", "register:40f0:8", ["const:875be8:8", "const:4:8"]]
- 00875be8 ["CALLIND", null, ["register:0:8"]]
+ 00875c28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00875c28 ["INT_ADD", "register:40f0:8", ["const:875c28:8", "const:4:8"]]
+ 00875c28 ["CALLIND", null, ["register:0:8"]]
- 00875be8 bytes 00013fd6
+ 00875c28 bytes 00013fd6
- 00875bf0 ["INT_ADD", "register:40f0:8", ["const:875bf0:8", "const:4:8"]]
- 00875bf0 ["CALL", null, ["callee:00c57e80:8"]]
+ 00875c30 ["INT_ADD", "register:40f0:8", ["const:875c30:8", "const:4:8"]]
+ 00875c30 ["CALL", null, ["callee:00c57e80:8"]]
- 00875bf0 bytes a4870f94
+ 00875c30 bytes 94880f94
~~~


<a id="compare-45cb0d47d53874572b64665f3f05fca1"></a>

### [`00875ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875ddc.md) → [`00875e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875e1c.md) FUN_00875e1c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00875df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875ddc.md#insn-00875df8) · [`00875e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875ddc.md#insn-00875e18)
- 新版 `00875e38`（命令位置の公開資料なし） · `00875e58`（命令位置の公開資料なし）

~~~diff
- 00875df8 ["INT_ADD", "register:40f0:8", ["const:875df8:8", "const:4:8"]]
- 00875df8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00875e38 ["INT_ADD", "register:40f0:8", ["const:875e38:8", "const:4:8"]]
+ 00875e38 ["CALL", null, ["callee:00c53d00:8"]]
- 00875df8 bytes ba760f94
+ 00875e38 bytes b2770f94
- 00875e18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00875e18 ["INT_ADD", "register:40f0:8", ["const:875e18:8", "const:4:8"]]
- 00875e18 ["CALLIND", null, ["register:0:8"]]
+ 00875e58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00875e58 ["INT_ADD", "register:40f0:8", ["const:875e58:8", "const:4:8"]]
+ 00875e58 ["CALLIND", null, ["register:0:8"]]
- 00875e18 bytes 00013fd6
+ 00875e58 bytes 00013fd6
~~~


<a id="compare-68b511154a84eefcfc70de89dec830ec"></a>

### [`00875f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875f78.md) → [`00875fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875fb8.md) FUN_00875fb8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00875c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875c38.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00875c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875c78.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00875f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875f78.md#insn-00875f94) · [`00875fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875f78.md#insn-00875fb4)
- 新版 `00875fd4`（命令位置の公開資料なし） · `00875ff4`（命令位置の公開資料なし）

~~~diff
- 00875f94 ["INT_ADD", "register:40f0:8", ["const:875f94:8", "const:4:8"]]
- 00875f94 ["CALL", null, ["callee:00c53d00:8"]]
+ 00875fd4 ["INT_ADD", "register:40f0:8", ["const:875fd4:8", "const:4:8"]]
+ 00875fd4 ["CALL", null, ["callee:00c53d00:8"]]
- 00875f94 bytes 53760f94
+ 00875fd4 bytes 4b770f94
- 00875fb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00875fb4 ["INT_ADD", "register:40f0:8", ["const:875fb4:8", "const:4:8"]]
- 00875fb4 ["CALLIND", null, ["register:0:8"]]
+ 00875ff4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00875ff4 ["INT_ADD", "register:40f0:8", ["const:875ff4:8", "const:4:8"]]
+ 00875ff4 ["CALLIND", null, ["register:0:8"]]
- 00875fb4 bytes 00013fd6
+ 00875ff4 bytes 00013fd6
~~~


<a id="compare-e54c783acbc883536bd6cb72875d26db"></a>

### [`00875fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875fc8.md) → [`00876008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876008.md) FUN_00876008

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00875c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875c38.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00875c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875c78.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00875fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875fc8.md#insn-00875fe8) · [`00875ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875fc8.md#insn-00875ffc) · [`00876004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875fc8.md#insn-00876004)
- 新版 `00876028`（命令位置の公開資料なし） · `0087603c`（命令位置の公開資料なし） · `00876044`（命令位置の公開資料なし）

~~~diff
- 00875fe8 ["INT_ADD", "register:40f0:8", ["const:875fe8:8", "const:4:8"]]
- 00875fe8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00876028 ["INT_ADD", "register:40f0:8", ["const:876028:8", "const:4:8"]]
+ 00876028 ["CALL", null, ["callee:00c53d00:8"]]
- 00875fe8 bytes 3e760f94
+ 00876028 bytes 36770f94
- 00875ffc ["COPY", "register:0:8", ["register:4040:8"]]
- 00875ffc ["INT_ADD", "register:40f0:8", ["const:875ffc:8", "const:4:8"]]
- 00875ffc ["CALLIND", null, ["register:0:8"]]
+ 0087603c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087603c ["INT_ADD", "register:40f0:8", ["const:87603c:8", "const:4:8"]]
+ 0087603c ["CALLIND", null, ["register:0:8"]]
- 00875ffc bytes 00013fd6
+ 0087603c bytes 00013fd6
- 00876004 ["INT_ADD", "register:40f0:8", ["const:876004:8", "const:4:8"]]
- 00876004 ["CALL", null, ["callee:00c57e80:8"]]
+ 00876044 ["INT_ADD", "register:40f0:8", ["const:876044:8", "const:4:8"]]
+ 00876044 ["CALL", null, ["callee:00c57e80:8"]]
- 00876004 bytes 9f860f94
+ 00876044 bytes 8f870f94
~~~


<a id="compare-a0cfb1a030b58f2b4cdb13ed9bd8600f"></a>

### [`00876050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876050.md) → [`00876090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876090.md) FUN_00876090

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00873f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873f00.md) [`00876050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876050.md) · 呼出先 2件 [`00876050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876050.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00873f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873f40.md) [`00876090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876090.md) · 呼出先 2件 [`00876090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876090.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087606c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876050.md#insn-0087606c) · [`00876078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876050.md#insn-00876078) · [`00876088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876050.md#insn-00876088)
- 新版 `008760ac`（命令位置の公開資料なし） · `008760b8`（命令位置の公開資料なし） · `008760c8`（命令位置の公開資料なし）

~~~diff
- 0087606c ["INT_ADD", "register:40f0:8", ["const:87606c:8", "const:4:8"]]
- 0087606c ["CALL", null, ["local:b0:8"]]
+ 008760ac ["INT_ADD", "register:40f0:8", ["const:8760ac:8", "const:4:8"]]
+ 008760ac ["CALL", null, ["local:b0:8"]]
- 0087606c bytes f9ffff97
+ 008760ac bytes f9ffff97
- 00876078 ["INT_ADD", "register:40f0:8", ["const:876078:8", "const:4:8"]]
- 00876078 ["CALL", null, ["local:b0:8"]]
+ 008760b8 ["INT_ADD", "register:40f0:8", ["const:8760b8:8", "const:4:8"]]
+ 008760b8 ["CALL", null, ["local:b0:8"]]
- 00876078 bytes f6ffff97
+ 008760b8 bytes f6ffff97
- 00876088 ["INT_ADD", "register:40f0:8", ["const:876088:8", "const:4:8"]]
- 00876088 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008760c8 ["INT_ADD", "register:40f0:8", ["const:8760c8:8", "const:4:8"]]
+ 008760c8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00876088 bytes 8a860f94
+ 008760c8 bytes 7a870f94
~~~


<a id="compare-a66426934ad5e91adf236c913eb9bec1"></a>

### [`00877880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877880.md) → [`008778c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/008778c0.md) FUN_008778c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00876ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876ec4.md) · 呼出先 5件 [`00877be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877be0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c58030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58030.md)
- 新版 呼出元 1件 [`00876f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876f04.md) · 呼出先 5件 [`00877c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877c20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c58430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087789c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877880.md#insn-0087789c) · [`008778a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877880.md#insn-008778a8) · [`008778c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877880.md#insn-008778c4)
- 新版 `008778dc`（命令位置の公開資料なし） · `008778e8`（命令位置の公開資料なし） · `00877904`（命令位置の公開資料なし）

~~~diff
- 0087789c ["INT_ADD", "register:40f0:8", ["const:87789c:8", "const:4:8"]]
- 0087789c ["CALL", null, ["callee:00c58430:8"]]
+ 008778dc ["INT_ADD", "register:40f0:8", ["const:8778dc:8", "const:4:8"]]
+ 008778dc ["CALL", null, ["callee:00c58430:8"]]
- 0087789c bytes e5810f94
+ 008778dc bytes d5820f94
- 008778a8 ["INT_ADD", "register:40f0:8", ["const:8778a8:8", "const:4:8"]]
- 008778a8 ["CALL", null, ["callee:00c58430:8"]]
+ 008778e8 ["INT_ADD", "register:40f0:8", ["const:8778e8:8", "const:4:8"]]
+ 008778e8 ["CALL", null, ["callee:00c58430:8"]]
- 008778a8 bytes e2810f94
+ 008778e8 bytes d2820f94
- 008778c4 ["INT_ADD", "register:40f0:8", ["const:8778c4:8", "const:4:8"]]
- 008778c4 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00877904 ["INT_ADD", "register:40f0:8", ["const:877904:8", "const:4:8"]]
+ 00877904 ["CALL", null, ["callee:00c53cd0:8"]]
- 008778c4 bytes fb6f0f94
+ 00877904 bytes f3700f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d16934bd2a646e2b6b8d3ed1740225d8"></a>

### [`008779d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/008779d0.md) → [`00877a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877a10.md) FUN_00877a10

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00876ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876ec4.md) · 呼出先 6件 [`00446a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446a08.md) [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cd0.md) [`00c57d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d70.md)
- 新版 呼出元 1件 [`00876f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876f04.md) · 呼出先 6件 [`00446a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446a48.md) [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md) [`00c58170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58170.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008779ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/008779d0.md#insn-008779ec) · [`008779f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/008779d0.md#insn-008779f4) · [`008779fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/008779d0.md#insn-008779fc)
- 新版 `00877a2c`（命令位置の公開資料なし） · `00877a34`（命令位置の公開資料なし） · `00877a3c`（命令位置の公開資料なし）

~~~diff
- 008779ec ["INT_ADD", "register:40f0:8", ["const:8779ec:8", "const:4:8"]]
- 008779ec ["CALL", null, ["callee:00446a48:8"]]
+ 00877a2c ["INT_ADD", "register:40f0:8", ["const:877a2c:8", "const:4:8"]]
+ 00877a2c ["CALL", null, ["callee:00446a48:8"]]
- 008779ec bytes 073cef97
+ 00877a2c bytes 073cef97
- 008779f4 ["INT_ADD", "register:40f0:8", ["const:8779f4:8", "const:4:8"]]
- 008779f4 ["CALL", null, ["callee:00c58170:8"]]
+ 00877a34 ["INT_ADD", "register:40f0:8", ["const:877a34:8", "const:4:8"]]
+ 00877a34 ["CALL", null, ["callee:00c58170:8"]]
- 008779f4 bytes df800f94
+ 00877a34 bytes cf810f94
- 008779fc ["INT_ADD", "register:40f0:8", ["const:8779fc:8", "const:4:8"]]
- 008779fc ["CALL", null, ["callee:00c58180:8"]]
+ 00877a3c ["INT_ADD", "register:40f0:8", ["const:877a3c:8", "const:4:8"]]
+ 00877a3c ["CALL", null, ["callee:00c58180:8"]]
- 008779fc bytes e1800f94
+ 00877a3c bytes d1810f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0db0b3379511a8088299547e31a0ad0e"></a>

### [`00877be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877be0.md) → [`00877c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877c20.md) FUN_00877c20

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00877880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877880.md) · 呼出先 5件 [`0048b504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b504.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`008778c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/008778c0.md) · 呼出先 5件 [`0048b544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b544.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00877c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877be0.md#insn-00877c24) · [`00877c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877be0.md#insn-00877c6c) · [`00877c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877be0.md#insn-00877c94)
- 新版 `00877c64`（命令位置の公開資料なし） · `00877cac`（命令位置の公開資料なし） · `00877cd4`（命令位置の公開資料なし）

~~~diff
- 00877c24 ["INT_ADD", "register:40f0:8", ["const:877c24:8", "const:4:8"]]
- 00877c24 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00877c64 ["INT_ADD", "register:40f0:8", ["const:877c64:8", "const:4:8"]]
+ 00877c64 ["CALL", null, ["callee:00c57eb0:8"]]
- 00877c24 bytes a37f0f94
+ 00877c64 bytes 93800f94
- 00877c6c ["INT_ADD", "register:40f0:8", ["const:877c6c:8", "const:4:8"]]
- 00877c6c ["CALL", null, ["callee:00c57e90:8"]]
+ 00877cac ["INT_ADD", "register:40f0:8", ["const:877cac:8", "const:4:8"]]
+ 00877cac ["CALL", null, ["callee:00c57e90:8"]]
- 00877c6c bytes 897f0f94
+ 00877cac bytes 79800f94
- 00877c94 ["INT_ADD", "register:40f0:8", ["const:877c94:8", "const:4:8"]]
- 00877c94 ["CALL", null, ["callee:00c58000:8"]]
+ 00877cd4 ["INT_ADD", "register:40f0:8", ["const:877cd4:8", "const:4:8"]]
+ 00877cd4 ["CALL", null, ["callee:00c58000:8"]]
- 00877c94 bytes db7f0f94
+ 00877cd4 bytes cb800f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee291e09b90913cc201f8a584ef5adbc"></a>

### [`00877d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877d10.md) → [`00877d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877d50.md) FUN_00877d50

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00877a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877a30.md) · 呼出先 9件 [`00597a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a4c.md) [`00597e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e08.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0085b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b3f0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00877a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877a70.md) · 呼出先 9件 [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`00597e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597e48.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0085b430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b430.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00877d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877d10.md#insn-00877d38) · [`00877d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877d10.md#insn-00877d48) · [`00877d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877d10.md#insn-00877d54)
- 新版 `00877d78`（命令位置の公開資料なし） · `00877d88`（命令位置の公開資料なし） · `00877d94`（命令位置の公開資料なし）

~~~diff
- 00877d38 ["INT_ADD", "register:40f0:8", ["const:877d38:8", "const:4:8"]]
- 00877d38 ["CALL", null, ["callee:00c58130:8"]]
+ 00877d78 ["INT_ADD", "register:40f0:8", ["const:877d78:8", "const:4:8"]]
+ 00877d78 ["CALL", null, ["callee:00c58130:8"]]
- 00877d38 bytes fe7f0f94
+ 00877d78 bytes ee800f94
- 00877d48 ["INT_ADD", "register:40f0:8", ["const:877d48:8", "const:4:8"]]
- 00877d48 ["CALL", null, ["callee:00c58140:8"]]
+ 00877d88 ["INT_ADD", "register:40f0:8", ["const:877d88:8", "const:4:8"]]
+ 00877d88 ["CALL", null, ["callee:00c58140:8"]]
- 00877d48 bytes fe7f0f94
+ 00877d88 bytes ee800f94
- 00877d54 ["INT_ADD", "register:40f0:8", ["const:877d54:8", "const:4:8"]]
- 00877d54 ["CALL", null, ["callee:00597e48:8"]]
+ 00877d94 ["INT_ADD", "register:40f0:8", ["const:877d94:8", "const:4:8"]]
+ 00877d94 ["CALL", null, ["callee:00597e48:8"]]
- 00877d54 bytes 2d80f497
+ 00877d94 bytes 2d80f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adb5184106b7160f5cb5f1ba92b59ae1"></a>

### [`00877e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877e08.md) → [`00877e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877e48.md) FUN_00877e48

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00877e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877e08.md#insn-00877e30) · [`00877e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877e08.md#insn-00877e38)
- 新版 `00877e70`（命令位置の公開資料なし） · `00877e78`（命令位置の公開資料なし）

~~~diff
- 00877e30 ["INT_ADD", "register:40f0:8", ["const:877e30:8", "const:4:8"]]
- 00877e30 ["CALL", null, ["callee:00c58150:8"]]
+ 00877e70 ["INT_ADD", "register:40f0:8", ["const:877e70:8", "const:4:8"]]
+ 00877e70 ["CALL", null, ["callee:00c58150:8"]]
- 00877e30 bytes c87f0f94
+ 00877e70 bytes b8800f94
- 00877e38 ["INT_ADD", "register:40f0:8", ["const:877e38:8", "const:4:8"]]
- 00877e38 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00877e78 ["INT_ADD", "register:40f0:8", ["const:877e78:8", "const:4:8"]]
+ 00877e78 ["CALL", null, ["callee:00c57eb0:8"]]
- 00877e38 bytes 1e7f0f94
+ 00877e78 bytes 0e800f94
~~~


<a id="compare-b6d563a7f87e9486265ef93a04377729"></a>

### [`008781ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/008781ec.md) → [`0087822c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/0087822c.md) FUN_0087822c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00848698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848698.md) [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) [`008548ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00854/008548ac.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a540.md)
- 新版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008486d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/008486d8.md) [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) [`008548ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00854/008548ec.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a940.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008781fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/008781ec.md#insn-008781fc) · [`0087820c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/008781ec.md#insn-0087820c)
- 新版 `0087823c`（命令位置の公開資料なし） · `0087824c`（命令位置の公開資料なし）

~~~diff
- 008781fc ["INT_ADD", "register:40f0:8", ["const:8781fc:8", "const:4:8"]]
- 008781fc ["CALL", null, ["callee:00c5a940:8"]]
+ 0087823c ["INT_ADD", "register:40f0:8", ["const:87823c:8", "const:4:8"]]
+ 0087823c ["CALL", null, ["callee:00c5a940:8"]]
- 008781fc bytes d1880f94
+ 0087823c bytes c1890f94
- 0087820c ["INT_ADD", "register:40f0:8", ["const:87820c:8", "const:4:8"]]
- 0087820c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0087824c ["INT_ADD", "register:40f0:8", ["const:87824c:8", "const:4:8"]]
+ 0087824c ["CALL", null, ["callee:00c57eb0:8"]]
- 0087820c bytes 297e0f94
+ 0087824c bytes 197f0f94
~~~


<a id="compare-f831a8b25bdc9d26e5ee9ada751c8a38"></a>

### [`00878278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878278.md) → [`008782b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/008782b8.md) FUN_008782b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00768174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768174.md) [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) [`0087f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md) [`00881d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881d3c.md) · 呼出先 8件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00b3c29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c29c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 4件 [`007681b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/007681b4.md) [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) [`00881d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881d7c.md) · 呼出先 8件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00b3c6c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3c/00b3c6c4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008782a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878278.md#insn-008782a8) · [`008782f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878278.md#insn-008782f4) · [`00878314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878278.md#insn-00878314)
- 新版 `008782e8`（命令位置の公開資料なし） · `00878334`（命令位置の公開資料なし） · `00878354`（命令位置の公開資料なし）

~~~diff
- 008782a8 ["INT_ADD", "register:40f0:8", ["const:8782a8:8", "const:4:8"]]
- 008782a8 ["CALL", null, ["callee:00c57fe0:8"]]
+ 008782e8 ["INT_ADD", "register:40f0:8", ["const:8782e8:8", "const:4:8"]]
+ 008782e8 ["CALL", null, ["callee:00c57fe0:8"]]
- 008782a8 bytes 4e7e0f94
+ 008782e8 bytes 3e7f0f94
- 008782f4 ["INT_ADD", "register:40f0:8", ["const:8782f4:8", "const:4:8"]]
- 008782f4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00878334 ["INT_ADD", "register:40f0:8", ["const:878334:8", "const:4:8"]]
+ 00878334 ["CALL", null, ["callee:00c57e90:8"]]
- 008782f4 bytes e77d0f94
+ 00878334 bytes d77e0f94
- 00878314 ["INT_ADD", "register:40f0:8", ["const:878314:8", "const:4:8"]]
- 00878314 ["CALL", null, ["callee:00c58000:8"]]
+ 00878354 ["INT_ADD", "register:40f0:8", ["const:878354:8", "const:4:8"]]
+ 00878354 ["CALL", null, ["callee:00c58000:8"]]
- 00878314 bytes 3b7e0f94
+ 00878354 bytes 2b7f0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52f92f09d93bea584db70a3107c6cfff"></a>

### [`00879b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879b78.md) → [`00879bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879bb8.md) FUN_00879bb8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005b12f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b12f8.md) · 呼出先 7件 [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md) [`00879c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879c48.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005b1338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1338.md) · 呼出先 7件 [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md) [`00879c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879c88.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00879bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879b78.md#insn-00879bc0) · [`00879bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879b78.md#insn-00879bc8) · [`00879bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879b78.md#insn-00879bcc)
- 新版 `00879c00`（命令位置の公開資料なし） · `00879c08`（命令位置の公開資料なし） · `00879c0c`（命令位置の公開資料なし）

~~~diff
- 00879bc0 ["INT_ADD", "register:40f0:8", ["const:879bc0:8", "const:4:8"]]
- 00879bc0 ["CALL", null, ["callee:00588e6c:8"]]
+ 00879c00 ["INT_ADD", "register:40f0:8", ["const:879c00:8", "const:4:8"]]
+ 00879c00 ["CALL", null, ["callee:00588e6c:8"]]
- 00879bc0 bytes 9b3cf497
+ 00879c00 bytes 9b3cf497
- 00879bc8 ["INT_ADD", "register:40f0:8", ["const:879bc8:8", "const:4:8"]]
- 00879bc8 ["CALL", null, ["callee:0058915c:8"]]
+ 00879c08 ["INT_ADD", "register:40f0:8", ["const:879c08:8", "const:4:8"]]
+ 00879c08 ["CALL", null, ["callee:0058915c:8"]]
- 00879bc8 bytes 553df497
+ 00879c08 bytes 553df497
- 00879bcc ["INT_ADD", "register:40f0:8", ["const:879bcc:8", "const:4:8"]]
- 00879bcc ["CALL", null, ["callee:00589850:8"]]
+ 00879c0c ["INT_ADD", "register:40f0:8", ["const:879c0c:8", "const:4:8"]]
+ 00879c0c ["CALL", null, ["callee:00589850:8"]]
- 00879bcc bytes 113ff497
+ 00879c0c bytes 113ff497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67faeb3e8d380ae49f1cd960dda15215"></a>

### [`00879c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879c48.md) → [`00879c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879c88.md) FUN_00879c88

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`00879b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879b78.md) [`0087e594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e594.md) [`00b667d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b667d0.md) [`00b66884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66884.md) [`00b6697c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6697c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 7件 [`00879bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879bb8.md) [`0087e5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e5d4.md) [`00b66bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66bf8.md) [`00b66cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66cac.md) [`00b66da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66da4.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00879cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879c48.md#insn-00879cb0) · [`00879cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879c48.md#insn-00879cc0) · [`00879cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879c48.md#insn-00879cd0)
- 新版 `00879cf0`（命令位置の公開資料なし） · `00879d00`（命令位置の公開資料なし） · `00879d10`（命令位置の公開資料なし）

~~~diff
- 00879cb0 ["INT_ADD", "register:40f0:8", ["const:879cb0:8", "const:4:8"]]
- 00879cb0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00879cf0 ["INT_ADD", "register:40f0:8", ["const:879cf0:8", "const:4:8"]]
+ 00879cf0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00879cb0 bytes 80770f94
+ 00879cf0 bytes 70780f94
- 00879cc0 ["INT_ADD", "register:40f0:8", ["const:879cc0:8", "const:4:8"]]
- 00879cc0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00879d00 ["INT_ADD", "register:40f0:8", ["const:879d00:8", "const:4:8"]]
+ 00879d00 ["CALL", null, ["callee:00c57eb0:8"]]
- 00879cc0 bytes 7c770f94
+ 00879d00 bytes 6c780f94
- 00879cd0 ["INT_ADD", "register:40f0:8", ["const:879cd0:8", "const:4:8"]]
- 00879cd0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00879d10 ["INT_ADD", "register:40f0:8", ["const:879d10:8", "const:4:8"]]
+ 00879d10 ["CALL", null, ["callee:00c57eb0:8"]]
- 00879cd0 bytes 78770f94
+ 00879d10 bytes 68780f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc4e244c566b5fd1f99e6c3141aed7df"></a>

### [`0087a510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087a510.md) → [`0087a550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087a550.md) FUN_0087a550

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087a54c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087a510.md#insn-0087a54c)
- 新版 `0087a58c`（命令位置の公開資料なし）

~~~diff
- 0087a54c ["COPY", "register:0:8", ["register:4040:8"]]
- 0087a54c ["INT_ADD", "register:40f0:8", ["const:87a54c:8", "const:4:8"]]
- 0087a54c ["CALLIND", null, ["register:0:8"]]
+ 0087a58c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087a58c ["INT_ADD", "register:40f0:8", ["const:87a58c:8", "const:4:8"]]
+ 0087a58c ["CALLIND", null, ["register:0:8"]]
- 0087a54c bytes 00013fd6
+ 0087a58c bytes 00013fd6
~~~


<a id="compare-c4f617d9ded0d4af1794e400e90d96d6"></a>

### [`0087b37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b37c.md) → [`0087b3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b3bc.md) FUN_0087b3bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 8件 [`00879d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879d48.md) [`0087a708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087a708.md) [`0087ac18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087ac18.md) [`00b33fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33fe8.md) [`00b34a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34a7c.md) · 呼出先 4件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5a6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6a0.md)
- 新版 呼出元 8件 [`00879d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879d88.md) [`0087a748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087a748.md) [`0087ac58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087ac58.md) [`00b34410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34410.md) [`00b34ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34ea4.md) · 呼出先 4件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5aaa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aaa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087b38c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b37c.md#insn-0087b38c) · [`0087b3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b37c.md#insn-0087b3a4) · [`0087b3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b37c.md#insn-0087b3b8)
- 新版 `0087b3cc`（命令位置の公開資料なし） · `0087b3e4`（命令位置の公開資料なし） · `0087b3f8`（命令位置の公開資料なし）

~~~diff
- 0087b38c ["INT_ADD", "register:40f0:8", ["const:87b38c:8", "const:4:8"]]
- 0087b38c ["CALL", null, ["callee:00c5aa00:8"]]
+ 0087b3cc ["INT_ADD", "register:40f0:8", ["const:87b3cc:8", "const:4:8"]]
+ 0087b3cc ["CALL", null, ["callee:00c5aa00:8"]]
- 0087b38c bytes 9d7c0f94
+ 0087b3cc bytes 8d7d0f94
- 0087b3a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087b3a4 ["INT_ADD", "register:40f0:8", ["const:87b3a4:8", "const:4:8"]]
- 0087b3a4 ["CALLIND", null, ["register:0:8"]]
+ 0087b3e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087b3e4 ["INT_ADD", "register:40f0:8", ["const:87b3e4:8", "const:4:8"]]
+ 0087b3e4 ["CALLIND", null, ["register:0:8"]]
- 0087b3a4 bytes 00013fd6
+ 0087b3e4 bytes 00013fd6
- 0087b3b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087b3b8 ["INT_ADD", "register:40f0:8", ["const:87b3b8:8", "const:4:8"]]
- 0087b3b8 ["CALLIND", null, ["register:0:8"]]
+ 0087b3f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087b3f8 ["INT_ADD", "register:40f0:8", ["const:87b3f8:8", "const:4:8"]]
+ 0087b3f8 ["CALLIND", null, ["register:0:8"]]
- 0087b3b8 bytes 00013fd6
+ 0087b3f8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-884b0cc839a08fadbe571ad2d00ce8c7"></a>

### [`0087b408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b408.md) → [`0087b448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b448.md) FUN_0087b448

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0087a2c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087a2c8.md) [`0087a9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087a9d0.md) [`0087b0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b0b0.md) · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 3件 [`0087a308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087a308.md) [`0087aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087aa10.md) [`0087b0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b0f0.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087b430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b408.md#insn-0087b430) · [`0087b454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b408.md#insn-0087b454) · [`0087b478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b408.md#insn-0087b478)
- 新版 `0087b470`（命令位置の公開資料なし） · `0087b494`（命令位置の公開資料なし） · `0087b4b8`（命令位置の公開資料なし）

~~~diff
- 0087b430 ["INT_ADD", "register:40f0:8", ["const:87b430:8", "const:4:8"]]
- 0087b430 ["CALL", null, ["callee:00c5aa00:8"]]
+ 0087b470 ["INT_ADD", "register:40f0:8", ["const:87b470:8", "const:4:8"]]
+ 0087b470 ["CALL", null, ["callee:00c5aa00:8"]]
- 0087b430 bytes 747c0f94
+ 0087b470 bytes 647d0f94
- 0087b454 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087b454 ["INT_ADD", "register:40f0:8", ["const:87b454:8", "const:4:8"]]
- 0087b454 ["CALLIND", null, ["register:0:8"]]
+ 0087b494 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087b494 ["INT_ADD", "register:40f0:8", ["const:87b494:8", "const:4:8"]]
+ 0087b494 ["CALLIND", null, ["register:0:8"]]
- 0087b454 bytes 00013fd6
+ 0087b494 bytes 00013fd6
- 0087b478 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087b478 ["INT_ADD", "register:40f0:8", ["const:87b478:8", "const:4:8"]]
- 0087b478 ["CALLIND", null, ["register:0:8"]]
+ 0087b4b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087b4b8 ["INT_ADD", "register:40f0:8", ["const:87b4b8:8", "const:4:8"]]
+ 0087b4b8 ["CALLIND", null, ["register:0:8"]]
- 0087b478 bytes 00013fd6
+ 0087b4b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b8eba219c86e60c2e64f48cd2c905f4"></a>

### [`0087b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b738.md) → [`0087b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b778.md) FUN_0087b778

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0087a2c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087a2c8.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0087a308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087a308.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087b774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b738.md#insn-0087b774)
- 新版 `0087b7b4`（命令位置の公開資料なし）

~~~diff
- 0087b774 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087b774 ["INT_ADD", "register:40f0:8", ["const:87b774:8", "const:4:8"]]
- 0087b774 ["CALLIND", null, ["register:0:8"]]
+ 0087b7b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087b7b4 ["INT_ADD", "register:40f0:8", ["const:87b7b4:8", "const:4:8"]]
+ 0087b7b4 ["CALLIND", null, ["register:0:8"]]
- 0087b774 bytes 00013fd6
+ 0087b7b4 bytes 00013fd6
~~~


<a id="compare-7fff6ade06bc06152751b539727609e6"></a>

### [`0087b788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b788.md) → [`0087b7c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b7c8.md) FUN_0087b7c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087b7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b788.md#insn-0087b7a4)
- 新版 `0087b7e4`（命令位置の公開資料なし）

~~~diff
- 0087b7a4 ["INT_ADD", "register:40f0:8", ["const:87b7a4:8", "const:4:8"]]
- 0087b7a4 ["CALL", null, ["callee:00459d74:8"]]
+ 0087b7e4 ["INT_ADD", "register:40f0:8", ["const:87b7e4:8", "const:4:8"]]
+ 0087b7e4 ["CALL", null, ["callee:00459d74:8"]]
- 0087b7a4 bytes 6479ef97
+ 0087b7e4 bytes 6479ef97
~~~


<a id="compare-d2c56177573c6f8e83e6d8314ffb1424"></a>

### [`0087bb00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087bb00.md) → [`0087bb40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bb40.md) FUN_0087bb40

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087bb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087bb00.md#insn-0087bb40)
- 新版 `0087bb80`（命令位置の公開資料なし）

~~~diff
- 0087bb40 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087bb40 ["INT_ADD", "register:40f0:8", ["const:87bb40:8", "const:4:8"]]
- 0087bb40 ["CALLIND", null, ["register:0:8"]]
+ 0087bb80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087bb80 ["INT_ADD", "register:40f0:8", ["const:87bb80:8", "const:4:8"]]
+ 0087bb80 ["CALLIND", null, ["register:0:8"]]
- 0087bb40 bytes 00013fd6
+ 0087bb80 bytes 00013fd6
~~~


<a id="compare-6a8d1a28ccf9c465acd54f7f4e20f7a5"></a>

### [`0087bb84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087bb84.md) → [`0087bbc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bbc4.md) FUN_0087bbc4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00879d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879d48.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00879d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879d88.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087bbc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087bb84.md#insn-0087bbc4) · [`0087bbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087bb84.md#insn-0087bbf0)
- 新版 `0087bc04`（命令位置の公開資料なし） · `0087bc30`（命令位置の公開資料なし）

~~~diff
- 0087bbc4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087bbc4 ["INT_ADD", "register:40f0:8", ["const:87bbc4:8", "const:4:8"]]
- 0087bbc4 ["CALLIND", null, ["register:0:8"]]
+ 0087bc04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087bc04 ["INT_ADD", "register:40f0:8", ["const:87bc04:8", "const:4:8"]]
+ 0087bc04 ["CALLIND", null, ["register:0:8"]]
- 0087bbc4 bytes 00013fd6
+ 0087bc04 bytes 00013fd6
- 0087bbf0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087bbf0 ["INT_ADD", "register:40f0:8", ["const:87bbf0:8", "const:4:8"]]
- 0087bbf0 ["CALLIND", null, ["register:0:8"]]
+ 0087bc30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087bc30 ["INT_ADD", "register:40f0:8", ["const:87bc30:8", "const:4:8"]]
+ 0087bc30 ["CALLIND", null, ["register:0:8"]]
- 0087bbf0 bytes 00013fd6
+ 0087bc30 bytes 00013fd6
~~~


<a id="compare-68b397ab0dc876952c87020ea85e7e5e"></a>

### [`0087bee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087bee8.md) → [`0087bf28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bf28.md) FUN_0087bf28

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087bf28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087bee8.md#insn-0087bf28)
- 新版 `0087bf68`（命令位置の公開資料なし）

~~~diff
- 0087bf28 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087bf28 ["INT_ADD", "register:40f0:8", ["const:87bf28:8", "const:4:8"]]
- 0087bf28 ["CALLIND", null, ["register:0:8"]]
+ 0087bf68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087bf68 ["INT_ADD", "register:40f0:8", ["const:87bf68:8", "const:4:8"]]
+ 0087bf68 ["CALLIND", null, ["register:0:8"]]
- 0087bf28 bytes 00013fd6
+ 0087bf68 bytes 00013fd6
~~~


<a id="compare-3077416205b5060c7c050f26ed5c4cbd"></a>

### [`0087c138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c138.md) → [`0087c178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c178.md) FUN_0087c178

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0087a9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087a9d0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0087aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087aa10.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087c174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c138.md#insn-0087c174)
- 新版 `0087c1b4`（命令位置の公開資料なし）

~~~diff
- 0087c174 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c174 ["INT_ADD", "register:40f0:8", ["const:87c174:8", "const:4:8"]]
- 0087c174 ["CALLIND", null, ["register:0:8"]]
+ 0087c1b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c1b4 ["INT_ADD", "register:40f0:8", ["const:87c1b4:8", "const:4:8"]]
+ 0087c1b4 ["CALLIND", null, ["register:0:8"]]
- 0087c174 bytes 00013fd6
+ 0087c1b4 bytes 00013fd6
~~~


<a id="compare-92f0b0f025f29f244422af205678f35e"></a>

### [`0087c188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c188.md) → [`0087c1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c1c8.md) FUN_0087c1c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087c1a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c188.md#insn-0087c1a4)
- 新版 `0087c1e4`（命令位置の公開資料なし）

~~~diff
- 0087c1a4 ["INT_ADD", "register:40f0:8", ["const:87c1a4:8", "const:4:8"]]
- 0087c1a4 ["CALL", null, ["callee:00459d74:8"]]
+ 0087c1e4 ["INT_ADD", "register:40f0:8", ["const:87c1e4:8", "const:4:8"]]
+ 0087c1e4 ["CALL", null, ["callee:00459d74:8"]]
- 0087c1a4 bytes e476ef97
+ 0087c1e4 bytes e476ef97
~~~


<a id="compare-af79aa411e8b561e42492edad5369ed1"></a>

### [`0087c3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c3a4.md) → [`0087c3e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c3e4.md) FUN_0087c3e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0087a708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087a708.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0087a748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087a748.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087c3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c3a4.md#insn-0087c3e0)
- 新版 `0087c420`（命令位置の公開資料なし）

~~~diff
- 0087c3e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c3e0 ["INT_ADD", "register:40f0:8", ["const:87c3e0:8", "const:4:8"]]
- 0087c3e0 ["CALLIND", null, ["register:0:8"]]
+ 0087c420 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c420 ["INT_ADD", "register:40f0:8", ["const:87c420:8", "const:4:8"]]
+ 0087c420 ["CALLIND", null, ["register:0:8"]]
- 0087c3e0 bytes 00013fd6
+ 0087c420 bytes 00013fd6
~~~


<a id="compare-67ac37a62b6c014e06c216b50685b4c9"></a>

### [`0087c3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c3f4.md) → [`0087c434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c434.md) FUN_0087c434

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087c424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c3f4.md#insn-0087c424) · [`0087c43c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c3f4.md#insn-0087c43c) · [`0087c450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c3f4.md#insn-0087c450)
- 新版 `0087c464`（命令位置の公開資料なし） · `0087c47c`（命令位置の公開資料なし） · `0087c490`（命令位置の公開資料なし）

~~~diff
- 0087c424 ["INT_ADD", "register:40f0:8", ["const:87c424:8", "const:4:8"]]
- 0087c424 ["CALL", null, ["callee:00c5aa00:8"]]
+ 0087c464 ["INT_ADD", "register:40f0:8", ["const:87c464:8", "const:4:8"]]
+ 0087c464 ["CALL", null, ["callee:00c5aa00:8"]]
- 0087c424 bytes 77780f94
+ 0087c464 bytes 67790f94
- 0087c43c ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c43c ["INT_ADD", "register:40f0:8", ["const:87c43c:8", "const:4:8"]]
- 0087c43c ["CALLIND", null, ["register:0:8"]]
+ 0087c47c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c47c ["INT_ADD", "register:40f0:8", ["const:87c47c:8", "const:4:8"]]
+ 0087c47c ["CALLIND", null, ["register:0:8"]]
- 0087c43c bytes 00013fd6
+ 0087c47c bytes 00013fd6
- 0087c450 ["INT_ADD", "register:40f0:8", ["const:87c450:8", "const:4:8"]]
- 0087c450 ["CALL", null, ["callee:00c5aa10:8"]]
+ 0087c490 ["INT_ADD", "register:40f0:8", ["const:87c490:8", "const:4:8"]]
+ 0087c490 ["CALL", null, ["callee:00c5aa10:8"]]
- 0087c450 bytes 70780f94
+ 0087c490 bytes 60790f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f14552a402a4eec7960b4fab58c8fb9"></a>

### [`0087c7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c7a0.md) → [`0087c7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c7e0.md) FUN_0087c7e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0087b0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b0b0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0087b0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b0f0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087c7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c7a0.md#insn-0087c7dc)
- 新版 `0087c81c`（命令位置の公開資料なし）

~~~diff
- 0087c7dc ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c7dc ["INT_ADD", "register:40f0:8", ["const:87c7dc:8", "const:4:8"]]
- 0087c7dc ["CALLIND", null, ["register:0:8"]]
+ 0087c81c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c81c ["INT_ADD", "register:40f0:8", ["const:87c81c:8", "const:4:8"]]
+ 0087c81c ["CALLIND", null, ["register:0:8"]]
- 0087c7dc bytes 00013fd6
+ 0087c81c bytes 00013fd6
~~~


<a id="compare-df216cee1d9d230787c177cba83c526e"></a>

### [`0087c7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c7f0.md) → [`0087c830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c830.md) FUN_0087c830

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087c80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c7f0.md#insn-0087c80c)
- 新版 `0087c84c`（命令位置の公開資料なし）

~~~diff
- 0087c80c ["INT_ADD", "register:40f0:8", ["const:87c80c:8", "const:4:8"]]
- 0087c80c ["CALL", null, ["callee:00459d74:8"]]
+ 0087c84c ["INT_ADD", "register:40f0:8", ["const:87c84c:8", "const:4:8"]]
+ 0087c84c ["CALL", null, ["callee:00459d74:8"]]
- 0087c80c bytes 4a75ef97
+ 0087c84c bytes 4a75ef97
~~~


<a id="compare-8838ba7ab181c4065c2b948772986896"></a>

### [`0087cbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087cbec.md) → [`0087cc2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087cc2c.md) FUN_0087cc2c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0087ac18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087ac18.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0087ac58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087ac58.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087cc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087cbec.md#insn-0087cc2c) · [`0087cc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087cbec.md#insn-0087cc58)
- 新版 `0087cc6c`（命令位置の公開資料なし） · `0087cc98`（命令位置の公開資料なし）

~~~diff
- 0087cc2c ["COPY", "register:0:8", ["register:4040:8"]]
- 0087cc2c ["INT_ADD", "register:40f0:8", ["const:87cc2c:8", "const:4:8"]]
- 0087cc2c ["CALLIND", null, ["register:0:8"]]
+ 0087cc6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087cc6c ["INT_ADD", "register:40f0:8", ["const:87cc6c:8", "const:4:8"]]
+ 0087cc6c ["CALLIND", null, ["register:0:8"]]
- 0087cc2c bytes 00013fd6
+ 0087cc6c bytes 00013fd6
- 0087cc58 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087cc58 ["INT_ADD", "register:40f0:8", ["const:87cc58:8", "const:4:8"]]
- 0087cc58 ["CALLIND", null, ["register:0:8"]]
+ 0087cc98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087cc98 ["INT_ADD", "register:40f0:8", ["const:87cc98:8", "const:4:8"]]
+ 0087cc98 ["CALLIND", null, ["register:0:8"]]
- 0087cc58 bytes 00013fd6
+ 0087cc98 bytes 00013fd6
~~~


<a id="compare-e2e7062ce6fd9af9ca20a183575716bb"></a>

### [`0087d23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d23c.md) → [`0087d27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d27c.md) FUN_0087d27c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087d24c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d23c.md#insn-0087d24c)
- 新版 `0087d28c`（命令位置の公開資料なし）

~~~diff
- 0087d24c ["INT_ADD", "register:40f0:8", ["const:87d24c:8", "const:4:8"]]
- 0087d24c ["CALL", null, ["callee:00c5aac0:8"]]
+ 0087d28c ["INT_ADD", "register:40f0:8", ["const:87d28c:8", "const:4:8"]]
+ 0087d28c ["CALL", null, ["callee:00c5aac0:8"]]
- 0087d24c bytes 1d750f94
+ 0087d28c bytes 0d760f94
~~~


<a id="compare-342145b69c9b87862d23900bed0ea1dd"></a>

### [`0087d260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d260.md) → [`0087d2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d2a0.md) FUN_0087d2a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00493d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493d88.md) [`00575cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575cd4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00493dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493dc8.md) [`00575d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575d14.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087d2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d260.md#insn-0087d2b8) · [`0087d2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d260.md#insn-0087d2cc) · [`0087d2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d260.md#insn-0087d2e8)
- 新版 `0087d2f8`（命令位置の公開資料なし） · `0087d30c`（命令位置の公開資料なし） · `0087d328`（命令位置の公開資料なし）

~~~diff
- 0087d2b8 ["INT_ADD", "register:40f0:8", ["const:87d2b8:8", "const:4:8"]]
- 0087d2b8 ["CALL", null, ["callee:00493dc8:8"]]
+ 0087d2f8 ["INT_ADD", "register:40f0:8", ["const:87d2f8:8", "const:4:8"]]
+ 0087d2f8 ["CALL", null, ["callee:00493dc8:8"]]
- 0087d2b8 bytes b45af097
+ 0087d2f8 bytes b45af097
- 0087d2cc ["INT_ADD", "register:40f0:8", ["const:87d2cc:8", "const:4:8"]]
- 0087d2cc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0087d30c ["INT_ADD", "register:40f0:8", ["const:87d30c:8", "const:4:8"]]
+ 0087d30c ["CALL", null, ["callee:00c57eb0:8"]]
- 0087d2cc bytes f9690f94
+ 0087d30c bytes e96a0f94
- 0087d2e8 ["INT_ADD", "register:40f0:8", ["const:87d2e8:8", "const:4:8"]]
- 0087d2e8 ["CALL", null, ["callee:00575d14:8"]]
+ 0087d328 ["INT_ADD", "register:40f0:8", ["const:87d328:8", "const:4:8"]]
+ 0087d328 ["CALL", null, ["callee:00575d14:8"]]
- 0087d2e8 bytes 7be2f397
+ 0087d328 bytes 7be2f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d6f949ae13dd1f663c9ba93d4dc10af"></a>

### [`0087d340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d340.md) → [`0087d380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d380.md) FUN_0087d380

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00575c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575c64.md) [`0058ad88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058ad88.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00575ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575ca4.md) [`0058adc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058adc8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087d36c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d340.md#insn-0087d36c) · [`0087d3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d340.md#insn-0087d3b8) · [`0087d3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d340.md#insn-0087d3d8)
- 新版 `0087d3ac`（命令位置の公開資料なし） · `0087d3f8`（命令位置の公開資料なし） · `0087d418`（命令位置の公開資料なし）

~~~diff
- 0087d36c ["INT_ADD", "register:40f0:8", ["const:87d36c:8", "const:4:8"]]
- 0087d36c ["CALL", null, ["callee:00c57fe0:8"]]
+ 0087d3ac ["INT_ADD", "register:40f0:8", ["const:87d3ac:8", "const:4:8"]]
+ 0087d3ac ["CALL", null, ["callee:00c57fe0:8"]]
- 0087d36c bytes 1d6a0f94
+ 0087d3ac bytes 0d6b0f94
- 0087d3b8 ["INT_ADD", "register:40f0:8", ["const:87d3b8:8", "const:4:8"]]
- 0087d3b8 ["CALL", null, ["callee:00c57e90:8"]]
+ 0087d3f8 ["INT_ADD", "register:40f0:8", ["const:87d3f8:8", "const:4:8"]]
+ 0087d3f8 ["CALL", null, ["callee:00c57e90:8"]]
- 0087d3b8 bytes b6690f94
+ 0087d3f8 bytes a66a0f94
- 0087d3d8 ["INT_ADD", "register:40f0:8", ["const:87d3d8:8", "const:4:8"]]
- 0087d3d8 ["CALL", null, ["callee:00c58000:8"]]
+ 0087d418 ["INT_ADD", "register:40f0:8", ["const:87d418:8", "const:4:8"]]
+ 0087d418 ["CALL", null, ["callee:00c58000:8"]]
- 0087d3d8 bytes 0a6a0f94
+ 0087d418 bytes fa6a0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a8e28cfb6ea5b85494c1a7e845d6b9a"></a>

### [`0087d8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d8b0.md) → [`0087d8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d8f0.md) FUN_0087d8f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0087ea80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ea80.md) · 呼出先 5件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e30.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6f0.md) [`00c5a700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a700.md)
- 新版 呼出元 1件 [`0087eac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eac0.md) · 呼出先 5件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58230.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5aaf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aaf0.md) [`00c5ab00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ab00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087d8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d8b0.md#insn-0087d8e8) · [`0087d8f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d8b0.md#insn-0087d8f4) · [`0087d904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d8b0.md#insn-0087d904)
- 新版 `0087d928`（命令位置の公開資料なし） · `0087d934`（命令位置の公開資料なし） · `0087d944`（命令位置の公開資料なし）

~~~diff
- 0087d8e8 ["INT_ADD", "register:40f0:8", ["const:87d8e8:8", "const:4:8"]]
- 0087d8e8 ["CALL", null, ["callee:00c5aaf0:8"]]
+ 0087d928 ["INT_ADD", "register:40f0:8", ["const:87d928:8", "const:4:8"]]
+ 0087d928 ["CALL", null, ["callee:00c5aaf0:8"]]
- 0087d8e8 bytes 82730f94
+ 0087d928 bytes 72740f94
- 0087d8f4 ["INT_ADD", "register:40f0:8", ["const:87d8f4:8", "const:4:8"]]
- 0087d8f4 ["CALL", null, ["callee:00c5ab00:8"]]
+ 0087d934 ["INT_ADD", "register:40f0:8", ["const:87d934:8", "const:4:8"]]
+ 0087d934 ["CALL", null, ["callee:00c5ab00:8"]]
- 0087d8f4 bytes 83730f94
+ 0087d934 bytes 73740f94
- 0087d904 ["INT_ADD", "register:40f0:8", ["const:87d904:8", "const:4:8"]]
- 0087d904 ["CALL", null, ["callee:00c5a830:8"]]
+ 0087d944 ["INT_ADD", "register:40f0:8", ["const:87d944:8", "const:4:8"]]
+ 0087d944 ["CALL", null, ["callee:00c5a830:8"]]
- 0087d904 bytes cb720f94
+ 0087d944 bytes bb730f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efd5020669c21172f3ec7cc52c5b999c"></a>

### [`0087d984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d984.md) → [`0087d9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d9c4.md) FUN_0087d9c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0087eae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eae0.md) · 呼出先 15件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00596cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596cd0.md) [`005975c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975c8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0087eb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eb20.md) · 呼出先 15件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00596d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md) [`00597608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597608.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087d9c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d984.md#insn-0087d9c4) · [`0087d9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d984.md#insn-0087d9d0) · [`0087da08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d984.md#insn-0087da08)
- 新版 `0087da04`（命令位置の公開資料なし） · `0087da10`（命令位置の公開資料なし） · `0087da48`（命令位置の公開資料なし）

~~~diff
- 0087d9c4 ["INT_ADD", "register:40f0:8", ["const:87d9c4:8", "const:4:8"]]
- 0087d9c4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 0087da04 ["INT_ADD", "register:40f0:8", ["const:87da04:8", "const:4:8"]]
+ 0087da04 ["CALL", null, ["callee:00c5ab10:8"]]
- 0087d9c4 bytes 53730f94
+ 0087da04 bytes 43740f94
- 0087d9d0 ["INT_ADD", "register:40f0:8", ["const:87d9d0:8", "const:4:8"]]
- 0087d9d0 ["CALL", null, ["callee:00c5ab20:8"]]
+ 0087da10 ["INT_ADD", "register:40f0:8", ["const:87da10:8", "const:4:8"]]
+ 0087da10 ["CALL", null, ["callee:00c5ab20:8"]]
- 0087d9d0 bytes 54730f94
+ 0087da10 bytes 44740f94
- 0087da08 ["INT_ADD", "register:40f0:8", ["const:87da08:8", "const:4:8"]]
- 0087da08 ["CALL", null, ["callee:00c58430:8"]]
+ 0087da48 ["INT_ADD", "register:40f0:8", ["const:87da48:8", "const:4:8"]]
+ 0087da48 ["CALL", null, ["callee:00c58430:8"]]
- 0087da08 bytes 8a690f94
+ 0087da48 bytes 7a6a0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2689753ca44651a868e3005e09c88e23"></a>

### [`0087e594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e594.md) → [`0087e5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e5d4.md) FUN_0087e5d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) · 呼出先 7件 [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md) [`00879c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879c48.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) · 呼出先 7件 [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md) [`00879c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879c88.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087e5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e594.md#insn-0087e5f4) · [`0087e5fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e594.md#insn-0087e5fc) · [`0087e600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e594.md#insn-0087e600)
- 新版 `0087e634`（命令位置の公開資料なし） · `0087e63c`（命令位置の公開資料なし） · `0087e640`（命令位置の公開資料なし）

~~~diff
- 0087e5f4 ["INT_ADD", "register:40f0:8", ["const:87e5f4:8", "const:4:8"]]
- 0087e5f4 ["CALL", null, ["callee:00588e6c:8"]]
+ 0087e634 ["INT_ADD", "register:40f0:8", ["const:87e634:8", "const:4:8"]]
+ 0087e634 ["CALL", null, ["callee:00588e6c:8"]]
- 0087e5f4 bytes 0e2af497
+ 0087e634 bytes 0e2af497
- 0087e5fc ["INT_ADD", "register:40f0:8", ["const:87e5fc:8", "const:4:8"]]
- 0087e5fc ["CALL", null, ["callee:0058915c:8"]]
+ 0087e63c ["INT_ADD", "register:40f0:8", ["const:87e63c:8", "const:4:8"]]
+ 0087e63c ["CALL", null, ["callee:0058915c:8"]]
- 0087e5fc bytes c82af497
+ 0087e63c bytes c82af497
- 0087e600 ["INT_ADD", "register:40f0:8", ["const:87e600:8", "const:4:8"]]
- 0087e600 ["CALL", null, ["callee:00589850:8"]]
+ 0087e640 ["INT_ADD", "register:40f0:8", ["const:87e640:8", "const:4:8"]]
+ 0087e640 ["CALL", null, ["callee:00589850:8"]]
- 0087e600 bytes 842cf497
+ 0087e640 bytes 842cf497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64ac410e91260de9cecd0a162f40a9f7"></a>

### [`0087e69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e69c.md) → [`0087e6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e6dc.md) FUN_0087e6dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) · 呼出先 1件 [`0087eb7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eb7c.md)
- 新版 呼出元 1件 [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) · 呼出先 1件 [`0087ebbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ebbc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087e6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e69c.md#insn-0087e6b4)
- 新版 `0087e6f4`（命令位置の公開資料なし）

~~~diff
- 0087e6b4 ["INT_ADD", "register:40f0:8", ["const:87e6b4:8", "const:4:8"]]
- 0087e6b4 ["CALL", null, ["callee:0087ebbc:8"]]
+ 0087e6f4 ["INT_ADD", "register:40f0:8", ["const:87e6f4:8", "const:4:8"]]
+ 0087e6f4 ["CALL", null, ["callee:0087ebbc:8"]]
- 0087e6b4 bytes 32010094
+ 0087e6f4 bytes 32010094
~~~


<a id="compare-0c8559bb9be0860794f985a8625b30e8"></a>

### [`0087ea80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ea80.md) → [`0087eac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eac0.md) FUN_0087eac0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`0061037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00610/0061037c.md) [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`00763d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00763/00763d18.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 2件 [`0087d8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d8b0.md) [`0087ec08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ec08.md)
- 新版 呼出元 8件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`00763d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00763/00763d58.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 2件 [`0087d8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d8f0.md) [`0087ec48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ec48.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087eaa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ea80.md#insn-0087eaa0) · [`0087eab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ea80.md#insn-0087eab4)
- 新版 `0087eae0`（命令位置の公開資料なし） · `0087eaf4`（命令位置の公開資料なし）

~~~diff
- 0087eaa0 ["INT_ADD", "register:40f0:8", ["const:87eaa0:8", "const:4:8"]]
- 0087eaa0 ["CALL", null, ["callee:0087ec48:8"]]
+ 0087eae0 ["INT_ADD", "register:40f0:8", ["const:87eae0:8", "const:4:8"]]
+ 0087eae0 ["CALL", null, ["callee:0087ec48:8"]]
- 0087eaa0 bytes 5a000094
+ 0087eae0 bytes 5a000094
- 0087eab4 ["INT_ADD", "register:40f0:8", ["const:87eab4:8", "const:4:8"]]
- 0087eab4 ["CALL", null, ["callee:0087d8f0:8"]]
+ 0087eaf4 ["INT_ADD", "register:40f0:8", ["const:87eaf4:8", "const:4:8"]]
+ 0087eaf4 ["CALL", null, ["callee:0087d8f0:8"]]
- 0087eab4 bytes 7ffbff97
+ 0087eaf4 bytes 7ffbff97
~~~


<a id="compare-d7cf03d2c6580af54505ceb42a44d9bf"></a>

### [`0087eae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eae0.md) → [`0087eb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eb20.md) FUN_0087eb20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009cc4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cc/009cc4ac.md) · 呼出先 2件 [`0087d984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d984.md) [`0087ec08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ec08.md)
- 新版 呼出元 1件 [`009cc648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009cc/009cc648.md) · 呼出先 2件 [`0087d9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d9c4.md) [`0087ec48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ec48.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087eaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eae0.md#insn-0087eaf8)
- 新版 `0087eb38`（命令位置の公開資料なし）

~~~diff
- 0087eaf8 ["INT_ADD", "register:40f0:8", ["const:87eaf8:8", "const:4:8"]]
- 0087eaf8 ["CALL", null, ["callee:0087ec48:8"]]
+ 0087eb38 ["INT_ADD", "register:40f0:8", ["const:87eb38:8", "const:4:8"]]
+ 0087eb38 ["CALL", null, ["callee:0087ec48:8"]]
- 0087eaf8 bytes 44000094
+ 0087eb38 bytes 44000094
~~~


<a id="compare-24170cc8cf7d9144b745430be03acff0"></a>

### [`0087eb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eb2c.md) → [`0087eb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eb6c.md) FUN_0087eb6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087eb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eb2c.md#insn-0087eb48) · [`0087eb68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eb2c.md#insn-0087eb68)
- 新版 `0087eb88`（命令位置の公開資料なし） · `0087eba8`（命令位置の公開資料なし）

~~~diff
- 0087eb48 ["INT_ADD", "register:40f0:8", ["const:87eb48:8", "const:4:8"]]
- 0087eb48 ["CALL", null, ["callee:00c53d00:8"]]
+ 0087eb88 ["INT_ADD", "register:40f0:8", ["const:87eb88:8", "const:4:8"]]
+ 0087eb88 ["CALL", null, ["callee:00c53d00:8"]]
- 0087eb48 bytes 66530f94
+ 0087eb88 bytes 5e540f94
- 0087eb68 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087eb68 ["INT_ADD", "register:40f0:8", ["const:87eb68:8", "const:4:8"]]
- 0087eb68 ["CALLIND", null, ["register:0:8"]]
+ 0087eba8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087eba8 ["INT_ADD", "register:40f0:8", ["const:87eba8:8", "const:4:8"]]
+ 0087eba8 ["CALLIND", null, ["register:0:8"]]
- 0087eb68 bytes 00013fd6
+ 0087eba8 bytes 00013fd6
~~~


