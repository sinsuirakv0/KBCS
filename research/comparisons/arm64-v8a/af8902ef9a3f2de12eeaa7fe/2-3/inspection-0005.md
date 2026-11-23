# v16.0.0 → v16.0.1 · 要調査の変更候補 (5)

[一覧の目次](README.md)

<a id="compare-8510e6115458a12ea403427cbc403877"></a>

### [`0048f3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f3d0.md) → [`0048f410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048f/0048f410.md) FUN_0048f410

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f3d0.md#insn-0048f3ec) · [`0048f40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f3d0.md#insn-0048f40c)
- 新版 `0048f42c`（命令位置の公開資料なし） · `0048f44c`（命令位置の公開資料なし）

~~~diff
- 0048f3ec ["INT_ADD", "register:40f0:8", ["const:48f3ec:8", "const:4:8"]]
- 0048f3ec ["CALL", null, ["callee:00c53d00:8"]]
+ 0048f42c ["INT_ADD", "register:40f0:8", ["const:48f42c:8", "const:4:8"]]
+ 0048f42c ["CALL", null, ["callee:00c53d00:8"]]
- 0048f3ec bytes 3d111f94
+ 0048f42c bytes 35121f94
- 0048f40c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048f40c ["INT_ADD", "register:40f0:8", ["const:48f40c:8", "const:4:8"]]
- 0048f40c ["CALLIND", null, ["register:0:8"]]
+ 0048f44c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048f44c ["INT_ADD", "register:40f0:8", ["const:48f44c:8", "const:4:8"]]
+ 0048f44c ["CALLIND", null, ["register:0:8"]]
- 0048f40c bytes 00013fd6
+ 0048f44c bytes 00013fd6
~~~


<a id="compare-623bdd9567ec0a0a8f6c2a992829da20"></a>

### [`00492784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492784.md) → [`004927c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004927c4.md) FUN_004927c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004927d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492784.md#insn-004927d0) · [`004927e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492784.md#insn-004927e4) · [`004927ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492784.md#insn-004927ec)
- 新版 `00492810`（命令位置の公開資料なし） · `00492824`（命令位置の公開資料なし） · `0049282c`（命令位置の公開資料なし）

~~~diff
- 004927d0 ["INT_ADD", "register:40f0:8", ["const:4927d0:8", "const:4:8"]]
- 004927d0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00492810 ["INT_ADD", "register:40f0:8", ["const:492810:8", "const:4:8"]]
+ 00492810 ["CALL", null, ["callee:00c53d00:8"]]
- 004927d0 bytes 44041f94
+ 00492810 bytes 3c051f94
- 004927e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004927e4 ["INT_ADD", "register:40f0:8", ["const:4927e4:8", "const:4:8"]]
- 004927e4 ["CALLIND", null, ["register:0:8"]]
+ 00492824 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00492824 ["INT_ADD", "register:40f0:8", ["const:492824:8", "const:4:8"]]
+ 00492824 ["CALLIND", null, ["register:0:8"]]
- 004927e4 bytes 00013fd6
+ 00492824 bytes 00013fd6
- 004927ec ["INT_ADD", "register:40f0:8", ["const:4927ec:8", "const:4:8"]]
- 004927ec ["CALL", null, ["callee:00c57e80:8"]]
+ 0049282c ["INT_ADD", "register:40f0:8", ["const:49282c:8", "const:4:8"]]
+ 0049282c ["CALL", null, ["callee:00c57e80:8"]]
- 004927ec bytes a5141f94
+ 0049282c bytes 95151f94
~~~


<a id="compare-d038f427447716c590770e5d37dba752"></a>

### [`0049281c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049281c.md) → [`0049285c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/0049285c.md) FUN_0049285c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00492838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049281c.md#insn-00492838) · [`00492858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049281c.md#insn-00492858)
- 新版 `00492878`（命令位置の公開資料なし） · `00492898`（命令位置の公開資料なし）

~~~diff
- 00492838 ["INT_ADD", "register:40f0:8", ["const:492838:8", "const:4:8"]]
- 00492838 ["CALL", null, ["callee:00c53d00:8"]]
+ 00492878 ["INT_ADD", "register:40f0:8", ["const:492878:8", "const:4:8"]]
+ 00492878 ["CALL", null, ["callee:00c53d00:8"]]
- 00492838 bytes 2a041f94
+ 00492878 bytes 22051f94
- 00492858 ["COPY", "register:0:8", ["register:4040:8"]]
- 00492858 ["INT_ADD", "register:40f0:8", ["const:492858:8", "const:4:8"]]
- 00492858 ["CALLIND", null, ["register:0:8"]]
+ 00492898 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00492898 ["INT_ADD", "register:40f0:8", ["const:492898:8", "const:4:8"]]
+ 00492898 ["CALLIND", null, ["register:0:8"]]
- 00492858 bytes 00013fd6
+ 00492898 bytes 00013fd6
~~~


<a id="compare-fa53ede7daae3f8e758d7dcfdb555740"></a>

### [`00492cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492cc4.md) → [`00492d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492d04.md) FUN_00492d04

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 27件 [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`008650d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/008650d0.md) [`00871fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871fe0.md) [`00872210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872210.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00492dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492dc8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 27件 [`00851a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851a0c.md) [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`00865110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865110.md) [`00872020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872020.md) [`00872250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872250.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00492e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492e08.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00492d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492cc4.md#insn-00492d2c) · [`00492d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492cc4.md#insn-00492d3c) · [`00492d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492cc4.md#insn-00492d4c)
- 新版 `00492d6c`（命令位置の公開資料なし） · `00492d7c`（命令位置の公開資料なし） · `00492d8c`（命令位置の公開資料なし）

~~~diff
- 00492d2c ["INT_ADD", "register:40f0:8", ["const:492d2c:8", "const:4:8"]]
- 00492d2c ["CALL", null, ["callee:0043bb20:8"]]
+ 00492d6c ["INT_ADD", "register:40f0:8", ["const:492d6c:8", "const:4:8"]]
+ 00492d6c ["CALL", null, ["callee:0043bb20:8"]]
- 00492d2c bytes 6da3fe97
+ 00492d6c bytes 6da3fe97
- 00492d3c ["INT_ADD", "register:40f0:8", ["const:492d3c:8", "const:4:8"]]
- 00492d3c ["CALL", null, ["callee:00492e08:8"]]
+ 00492d7c ["INT_ADD", "register:40f0:8", ["const:492d7c:8", "const:4:8"]]
+ 00492d7c ["CALL", null, ["callee:00492e08:8"]]
- 00492d3c bytes 23000094
+ 00492d7c bytes 23000094
- 00492d4c ["INT_ADD", "register:40f0:8", ["const:492d4c:8", "const:4:8"]]
- 00492d4c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00492d8c ["INT_ADD", "register:40f0:8", ["const:492d8c:8", "const:4:8"]]
+ 00492d8c ["CALL", null, ["callee:00c57eb0:8"]]
- 00492d4c bytes 59131f94
+ 00492d8c bytes 49141f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c1432046c118b0cf0aa27adece34ce0"></a>

### [`00492dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492dc8.md) → [`00492e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492e08.md) FUN_00492e08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 96件 [`00492cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492cc4.md) [`005b9b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9b14.md) [`005c8ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8ebc.md) [`005d9f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9f0c.md) [`005e1b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1b78.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00441ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441ed4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 96件 [`00492d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492d04.md) [`005b9b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9b54.md) [`005c8efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c8/005c8efc.md) [`005d9f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d9/005d9f4c.md) [`005e1bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1bb8.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00441f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441f14.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00492e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492dc8.md#insn-00492e18) · [`00492e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492dc8.md#insn-00492e2c) · [`00492e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492dc8.md#insn-00492e58)
- 新版 `00492e58`（命令位置の公開資料なし） · `00492e6c`（命令位置の公開資料なし） · `00492e98`（命令位置の公開資料なし）

~~~diff
- 00492e18 ["INT_ADD", "register:40f0:8", ["const:492e18:8", "const:4:8"]]
- 00492e18 ["CALL", null, ["callee:0043bb20:8"]]
+ 00492e58 ["INT_ADD", "register:40f0:8", ["const:492e58:8", "const:4:8"]]
+ 00492e58 ["CALL", null, ["callee:0043bb20:8"]]
- 00492e18 bytes 32a3fe97
+ 00492e58 bytes 32a3fe97
- 00492e2c ["INT_ADD", "register:40f0:8", ["const:492e2c:8", "const:4:8"]]
- 00492e2c ["CALL", null, ["callee:0043bb20:8"]]
+ 00492e6c ["INT_ADD", "register:40f0:8", ["const:492e6c:8", "const:4:8"]]
+ 00492e6c ["CALL", null, ["callee:0043bb20:8"]]
- 00492e2c bytes 2da3fe97
+ 00492e6c bytes 2da3fe97
- 00492e58 ["INT_ADD", "register:40f0:8", ["const:492e58:8", "const:4:8"]]
- 00492e58 ["CALL", null, ["callee:00441f14:8"]]
+ 00492e98 ["INT_ADD", "register:40f0:8", ["const:492e98:8", "const:4:8"]]
+ 00492e98 ["CALL", null, ["callee:00441f14:8"]]
- 00492e58 bytes 1fbcfe97
+ 00492e98 bytes 1fbcfe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c738450325ffbbdab685b19ee4103502"></a>

### [`00492ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492ee8.md) → [`00492f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492f28.md) FUN_00492f28

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 25件 [`00482acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482acc.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`007ae958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae958.md) [`007aef10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aef10.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 5件 [`00492fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492fc8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 25件 [`00482b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482b0c.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`007ae998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae998.md) [`007aef50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aef50.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 5件 [`00493008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493008.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00492f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492ee8.md#insn-00492f28) · [`00492f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492ee8.md#insn-00492f3c) · [`00492f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492ee8.md#insn-00492f50)
- 新版 `00492f68`（命令位置の公開資料なし） · `00492f7c`（命令位置の公開資料なし） · `00492f90`（命令位置の公開資料なし）

~~~diff
- 00492f28 ["INT_ADD", "register:40f0:8", ["const:492f28:8", "const:4:8"]]
- 00492f28 ["CALL", null, ["callee:00493008:8"]]
+ 00492f68 ["INT_ADD", "register:40f0:8", ["const:492f68:8", "const:4:8"]]
+ 00492f68 ["CALL", null, ["callee:00493008:8"]]
- 00492f28 bytes 28000094
+ 00492f68 bytes 28000094
- 00492f3c ["INT_ADD", "register:40f0:8", ["const:492f3c:8", "const:4:8"]]
- 00492f3c ["CALL", null, ["callee:00c53d00:8"]]
+ 00492f7c ["INT_ADD", "register:40f0:8", ["const:492f7c:8", "const:4:8"]]
+ 00492f7c ["CALL", null, ["callee:00c53d00:8"]]
- 00492f3c bytes 69021f94
+ 00492f7c bytes 61031f94
- 00492f50 ["INT_ADD", "register:40f0:8", ["const:492f50:8", "const:4:8"]]
- 00492f50 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00492f90 ["INT_ADD", "register:40f0:8", ["const:492f90:8", "const:4:8"]]
+ 00492f90 ["CALL", null, ["callee:00c57eb0:8"]]
- 00492f50 bytes d8121f94
+ 00492f90 bytes c8131f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b3af6d4ef7af77c63706ea15628b499"></a>

### [`00493650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493650.md) → [`00493690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493690.md) FUN_00493690

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 16件 [`005b1778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1778.md) [`005b1b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1b44.md) [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`0061300c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/0061300c.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 5件 [`005509d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509d0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 16件 [`005b17b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b17b8.md) [`005b1b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1b84.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`0061304c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00613/0061304c.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 5件 [`00550a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a10.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00493694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493650.md#insn-00493694) · [`004936c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493650.md#insn-004936c0) · [`004936d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493650.md#insn-004936d0)
- 新版 `004936d4`（命令位置の公開資料なし） · `00493700`（命令位置の公開資料なし） · `00493710`（命令位置の公開資料なし）

~~~diff
- 00493694 ["INT_ADD", "register:40f0:8", ["const:493694:8", "const:4:8"]]
- 00493694 ["CALL", null, ["callee:00550a10:8"]]
+ 004936d4 ["INT_ADD", "register:40f0:8", ["const:4936d4:8", "const:4:8"]]
+ 004936d4 ["CALL", null, ["callee:00550a10:8"]]
- 00493694 bytes cff40294
+ 004936d4 bytes cff40294
- 004936c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004936c0 ["INT_ADD", "register:40f0:8", ["const:4936c0:8", "const:4:8"]]
- 004936c0 ["CALLIND", null, ["register:0:8"]]
+ 00493700 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00493700 ["INT_ADD", "register:40f0:8", ["const:493700:8", "const:4:8"]]
+ 00493700 ["CALLIND", null, ["register:0:8"]]
- 004936c0 bytes 00013fd6
+ 00493700 bytes 00013fd6
- 004936d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004936d0 ["INT_ADD", "register:40f0:8", ["const:4936d0:8", "const:4:8"]]
- 004936d0 ["CALLIND", null, ["register:0:8"]]
+ 00493710 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00493710 ["INT_ADD", "register:40f0:8", ["const:493710:8", "const:4:8"]]
+ 00493710 ["CALLIND", null, ["register:0:8"]]
- 004936d0 bytes 00013fd6
+ 00493710 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58ea658282e6e3e849e8fbec4b91cbb5"></a>

### [`00493894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493894.md) → [`004938d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004938d4.md) FUN_004938d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 8件 [`00479fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479fac.md) [`007ad808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad808.md) [`007ad944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad944.md) [`007ae814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae814.md) [`0087f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md) · 呼出先 3件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 8件 [`00479fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479fec.md) [`007ad848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad848.md) [`007ad984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad984.md) [`007ae854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae854.md) [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) · 呼出先 3件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004938c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493894.md#insn-004938c0) · [`004938d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493894.md#insn-004938d8) · [`004938ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493894.md#insn-004938ec)
- 新版 `00493900`（命令位置の公開資料なし） · `00493918`（命令位置の公開資料なし） · `0049392c`（命令位置の公開資料なし）

~~~diff
- 004938c0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004938c0 ["INT_ADD", "register:40f0:8", ["const:4938c0:8", "const:4:8"]]
- 004938c0 ["CALLIND", null, ["register:0:8"]]
+ 00493900 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00493900 ["INT_ADD", "register:40f0:8", ["const:493900:8", "const:4:8"]]
+ 00493900 ["CALLIND", null, ["register:0:8"]]
- 004938c0 bytes 20013fd6
+ 00493900 bytes 20013fd6
- 004938d8 ["INT_ADD", "register:40f0:8", ["const:4938d8:8", "const:4:8"]]
- 004938d8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00493918 ["INT_ADD", "register:40f0:8", ["const:493918:8", "const:4:8"]]
+ 00493918 ["CALL", null, ["callee:00c53d00:8"]]
- 004938d8 bytes 02001f94
+ 00493918 bytes fa001f94
- 004938ec ["COPY", "register:0:8", ["register:4040:8"]]
- 004938ec ["INT_ADD", "register:40f0:8", ["const:4938ec:8", "const:4:8"]]
- 004938ec ["CALLIND", null, ["register:0:8"]]
+ 0049392c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049392c ["INT_ADD", "register:40f0:8", ["const:49392c:8", "const:4:8"]]
+ 0049392c ["CALLIND", null, ["register:0:8"]]
- 004938ec bytes 00013fd6
+ 0049392c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56a7b165ece7b6626e41039af78c846d"></a>

### [`00493958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493958.md) → [`00493998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493998.md) FUN_00493998

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 50件 [`0043d73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043d73c.md) [`005f466c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f4/005f466c.md) [`006122a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00612/006122a4.md) [`0062ecbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062ecbc.md) [`00645254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00645/00645254.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 50件 [`0043d77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043d77c.md) [`005f46ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f4/005f46ac.md) [`006122e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00612/006122e4.md) [`0062ecfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062e/0062ecfc.md) [`00645294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00645/00645294.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004939c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493958.md#insn-004939c4)
- 新版 `00493a04`（命令位置の公開資料なし）

~~~diff
- 004939c4 ["INT_ADD", "register:40f0:8", ["const:4939c4:8", "const:4:8"]]
- 004939c4 ["CALL", null, ["callee:00c58050:8"]]
+ 00493a04 ["INT_ADD", "register:40f0:8", ["const:493a04:8", "const:4:8"]]
+ 00493a04 ["CALL", null, ["callee:00c58050:8"]]
- 004939c4 bytes a3101f94
+ 00493a04 bytes 93111f94
~~~


<a id="compare-f235f68c255b8d7357cf6624d5b2b34d"></a>

### [`00493a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493a08.md) → [`00493a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493a48.md) FUN_00493a48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`008648d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00864/008648d0.md) [`0089598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) [`0089c00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089c/0089c00c.md) [`00b2c028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2c028.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 4件 [`00864910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00864/00864910.md) [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) [`0089bc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089bc8c.md) [`00b2c450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c450.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00493a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493a08.md#insn-00493a94) · [`00493ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493a08.md#insn-00493ab4) · [`00493ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493a08.md#insn-00493ad4)
- 新版 `00493ad4`（命令位置の公開資料なし） · `00493af4`（命令位置の公開資料なし） · `00493b14`（命令位置の公開資料なし）

~~~diff
- 00493a94 ["INT_ADD", "register:40f0:8", ["const:493a94:8", "const:4:8"]]
- 00493a94 ["CALL", null, ["callee:00c57e90:8"]]
+ 00493ad4 ["INT_ADD", "register:40f0:8", ["const:493ad4:8", "const:4:8"]]
+ 00493ad4 ["CALL", null, ["callee:00c57e90:8"]]
- 00493a94 bytes ff0f1f94
+ 00493ad4 bytes ef101f94
- 00493ab4 ["INT_ADD", "register:40f0:8", ["const:493ab4:8", "const:4:8"]]
- 00493ab4 ["CALL", null, ["callee:00c57f40:8"]]
+ 00493af4 ["INT_ADD", "register:40f0:8", ["const:493af4:8", "const:4:8"]]
+ 00493af4 ["CALL", null, ["callee:00c57f40:8"]]
- 00493ab4 bytes 23101f94
+ 00493af4 bytes 13111f94
- 00493ad4 ["INT_ADD", "register:40f0:8", ["const:493ad4:8", "const:4:8"]]
- 00493ad4 ["CALL", null, ["callee:0044291c:8"]]
+ 00493b14 ["INT_ADD", "register:40f0:8", ["const:493b14:8", "const:4:8"]]
+ 00493b14 ["CALL", null, ["callee:0044291c:8"]]
- 00493ad4 bytes 82bbfe97
+ 00493b14 bytes 82bbfe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9feef660ed0152b47cae1626fb218c0"></a>

### [`00493c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493c40.md) → [`00493c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493c80.md) FUN_00493c80

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`007ac380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007ac380.md) [`008648d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00864/008648d0.md) [`00893d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893d78.md) [`0089c00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089c/0089c00c.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00493d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493d88.md)
- 新版 呼出元 7件 [`007ac3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac3c0.md) [`00864910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00864/00864910.md) [`00893dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893dbc.md) [`0089bc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089bc8c.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00493dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493dc8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00493c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493c40.md#insn-00493c54)
- 新版 `00493c94`（命令位置の公開資料なし）

~~~diff
- 00493c54 ["INT_ADD", "register:40f0:8", ["const:493c54:8", "const:4:8"]]
- 00493c54 ["CALL", null, ["callee:00493dc8:8"]]
+ 00493c94 ["INT_ADD", "register:40f0:8", ["const:493c94:8", "const:4:8"]]
+ 00493c94 ["CALL", null, ["callee:00493dc8:8"]]
- 00493c54 bytes 4d000094
+ 00493c94 bytes 4d000094
~~~


<a id="compare-52a5cef0c0443930577b03e4d06ce144"></a>

### [`00493ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493ca8.md) → [`00493ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493ce8.md) FUN_00493ce8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`007ac380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007ac380.md) [`008648d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00864/008648d0.md) [`00893d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893d78.md) [`0089c00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089c/0089c00c.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 7件 [`007ac3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac3c0.md) [`00864910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00864/00864910.md) [`00893dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893dbc.md) [`0089bc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089bc8c.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00493d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493ca8.md#insn-00493d18) · [`00493d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493ca8.md#insn-00493d40)
- 新版 `00493d58`（命令位置の公開資料なし） · `00493d80`（命令位置の公開資料なし）

~~~diff
- 00493d18 ["INT_ADD", "register:40f0:8", ["const:493d18:8", "const:4:8"]]
- 00493d18 ["CALL", null, ["callee:00c58050:8"]]
+ 00493d58 ["INT_ADD", "register:40f0:8", ["const:493d58:8", "const:4:8"]]
+ 00493d58 ["CALL", null, ["callee:00c58050:8"]]
- 00493d18 bytes ce0f1f94
+ 00493d58 bytes be101f94
- 00493d40 ["INT_ADD", "register:40f0:8", ["const:493d40:8", "const:4:8"]]
- 00493d40 ["CALL", null, ["callee:00c58050:8"]]
+ 00493d80 ["INT_ADD", "register:40f0:8", ["const:493d80:8", "const:4:8"]]
+ 00493d80 ["CALL", null, ["callee:00c58050:8"]]
- 00493d40 bytes c40f1f94
+ 00493d80 bytes b4101f94
~~~


<a id="compare-5a03c000281d77ec094d9fa07b2cc3c5"></a>

### [`00493d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493d88.md) → [`00493dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493dc8.md) FUN_00493dc8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`00493c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493c40.md) [`00563c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563c20.md) [`005cd0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd0b0.md) [`0087d260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d260.md) [`00b5987c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b5987c.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 7件 [`00493c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493c80.md) [`00563c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563c60.md) [`005cd0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd0f0.md) [`0087d2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d2a0.md) [`00b59ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b59/00b59ca4.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00493df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493d88.md#insn-00493df4) · [`00493e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493d88.md#insn-00493e50)
- 新版 `00493e34`（命令位置の公開資料なし） · `00493e90`（命令位置の公開資料なし）

~~~diff
- 00493df4 ["INT_ADD", "register:40f0:8", ["const:493df4:8", "const:4:8"]]
- 00493df4 ["CALL", null, ["callee:00c58050:8"]]
+ 00493e34 ["INT_ADD", "register:40f0:8", ["const:493e34:8", "const:4:8"]]
+ 00493e34 ["CALL", null, ["callee:00c58050:8"]]
- 00493df4 bytes 970f1f94
+ 00493e34 bytes 87101f94
- 00493e50 ["INT_ADD", "register:40f0:8", ["const:493e50:8", "const:4:8"]]
- 00493e50 ["CALL", null, ["callee:00c58050:8"]]
+ 00493e90 ["INT_ADD", "register:40f0:8", ["const:493e90:8", "const:4:8"]]
+ 00493e90 ["CALL", null, ["callee:00c58050:8"]]
- 00493e50 bytes 800f1f94
+ 00493e90 bytes 70101f94
~~~


<a id="compare-63e4cbff534f5f43d7c62c2570f2d88b"></a>

### [`004942c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004942c8.md) → [`00494308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494308.md) FUN_00494308

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00494338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004942c8.md#insn-00494338) · [`0049434c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004942c8.md#insn-0049434c) · [`00494354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004942c8.md#insn-00494354)
- 新版 `00494378`（命令位置の公開資料なし） · `0049438c`（命令位置の公開資料なし） · `00494394`（命令位置の公開資料なし）

~~~diff
- 00494338 ["INT_ADD", "register:40f0:8", ["const:494338:8", "const:4:8"]]
- 00494338 ["CALL", null, ["callee:00c53d00:8"]]
+ 00494378 ["INT_ADD", "register:40f0:8", ["const:494378:8", "const:4:8"]]
+ 00494378 ["CALL", null, ["callee:00c53d00:8"]]
- 00494338 bytes 6afd1e94
+ 00494378 bytes 62fe1e94
- 0049434c ["COPY", "register:0:8", ["register:4040:8"]]
- 0049434c ["INT_ADD", "register:40f0:8", ["const:49434c:8", "const:4:8"]]
- 0049434c ["CALLIND", null, ["register:0:8"]]
+ 0049438c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049438c ["INT_ADD", "register:40f0:8", ["const:49438c:8", "const:4:8"]]
+ 0049438c ["CALLIND", null, ["register:0:8"]]
- 0049434c bytes 00013fd6
+ 0049438c bytes 00013fd6
- 00494354 ["INT_ADD", "register:40f0:8", ["const:494354:8", "const:4:8"]]
- 00494354 ["CALL", null, ["callee:00c57e80:8"]]
+ 00494394 ["INT_ADD", "register:40f0:8", ["const:494394:8", "const:4:8"]]
+ 00494394 ["CALL", null, ["callee:00c57e80:8"]]
- 00494354 bytes cb0d1f94
+ 00494394 bytes bb0e1f94
~~~


<a id="compare-54e807e5fecf2ec5852e4a7337e6463c"></a>

### [`0049437c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049437c.md) → [`004943bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/004943bc.md) FUN_004943bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00493294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493294.md) [`0049437c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049437c.md) · 呼出先 4件 [`0049437c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049437c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`004932d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004932d4.md) [`004943bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/004943bc.md) · 呼出先 4件 [`004943bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/004943bc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00494398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049437c.md#insn-00494398) · [`004943a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049437c.md#insn-004943a4) · [`004943b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049437c.md#insn-004943b8)
- 新版 `004943d8`（命令位置の公開資料なし） · `004943e4`（命令位置の公開資料なし） · `004943f8`（命令位置の公開資料なし）

~~~diff
- 00494398 ["INT_ADD", "register:40f0:8", ["const:494398:8", "const:4:8"]]
- 00494398 ["CALL", null, ["local:b0:8"]]
+ 004943d8 ["INT_ADD", "register:40f0:8", ["const:4943d8:8", "const:4:8"]]
+ 004943d8 ["CALL", null, ["local:b0:8"]]
- 00494398 bytes f9ffff97
+ 004943d8 bytes f9ffff97
- 004943a4 ["INT_ADD", "register:40f0:8", ["const:4943a4:8", "const:4:8"]]
- 004943a4 ["CALL", null, ["local:b0:8"]]
+ 004943e4 ["INT_ADD", "register:40f0:8", ["const:4943e4:8", "const:4:8"]]
+ 004943e4 ["CALL", null, ["local:b0:8"]]
- 004943a4 bytes f6ffff97
+ 004943e4 bytes f6ffff97
- 004943b8 ["INT_ADD", "register:40f0:8", ["const:4943b8:8", "const:4:8"]]
- 004943b8 ["CALL", null, ["callee:00c53d00:8"]]
+ 004943f8 ["INT_ADD", "register:40f0:8", ["const:4943f8:8", "const:4:8"]]
+ 004943f8 ["CALL", null, ["callee:00c53d00:8"]]
- 004943b8 bytes 4afd1e94
+ 004943f8 bytes 42fe1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c394c17a05c7d7ffc7a843e464f63103"></a>

### [`004944d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004944d4.md) → [`00494514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494514.md) FUN_00494514

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0049444c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049444c.md) [`00494b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494b8c.md) · 呼出先 4件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0049448c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/0049448c.md) [`00494bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494bcc.md) · 呼出先 4件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00494584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004944d4.md#insn-00494584) · [`00494598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004944d4.md#insn-00494598) · [`004945ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004944d4.md#insn-004945ac)
- 新版 `004945c4`（命令位置の公開資料なし） · `004945d8`（命令位置の公開資料なし） · `004945ec`（命令位置の公開資料なし）

~~~diff
- 00494584 ["INT_ADD", "register:40f0:8", ["const:494584:8", "const:4:8"]]
- 00494584 ["CALL", null, ["callee:00494610:8"]]
+ 004945c4 ["INT_ADD", "register:40f0:8", ["const:4945c4:8", "const:4:8"]]
+ 004945c4 ["CALL", null, ["callee:00494610:8"]]
- 00494584 bytes 13000094
+ 004945c4 bytes 13000094
- 00494598 ["INT_ADD", "register:40f0:8", ["const:494598:8", "const:4:8"]]
- 00494598 ["CALL", null, ["callee:00c53d00:8"]]
+ 004945d8 ["INT_ADD", "register:40f0:8", ["const:4945d8:8", "const:4:8"]]
+ 004945d8 ["CALL", null, ["callee:00c53d00:8"]]
- 00494598 bytes d2fc1e94
+ 004945d8 bytes cafd1e94
- 004945ac ["COPY", "register:0:8", ["register:4040:8"]]
- 004945ac ["INT_ADD", "register:40f0:8", ["const:4945ac:8", "const:4:8"]]
- 004945ac ["CALLIND", null, ["register:0:8"]]
+ 004945ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 004945ec ["INT_ADD", "register:40f0:8", ["const:4945ec:8", "const:4:8"]]
+ 004945ec ["CALLIND", null, ["register:0:8"]]
- 004945ac bytes 00013fd6
+ 004945ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9ad9985815d25ea1b8bdb5d1c3e40bf"></a>

### [`00494b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494b3c.md) → [`00494b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494b7c.md) FUN_00494b7c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0049329c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/0049329c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`004932dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004932dc.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00494b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494b3c.md#insn-00494b78)
- 新版 `00494bb8`（命令位置の公開資料なし）

~~~diff
- 00494b78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00494b78 ["INT_ADD", "register:40f0:8", ["const:494b78:8", "const:4:8"]]
- 00494b78 ["CALLIND", null, ["register:0:8"]]
+ 00494bb8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00494bb8 ["INT_ADD", "register:40f0:8", ["const:494bb8:8", "const:4:8"]]
+ 00494bb8 ["CALLIND", null, ["register:0:8"]]
- 00494b78 bytes 00013fd6
+ 00494bb8 bytes 00013fd6
~~~


<a id="compare-748a6e3ac2f7f3b73fc6a5f8429b9d49"></a>

### [`00494c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494c3c.md) → [`00494c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494c7c.md) FUN_00494c7c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`0048e154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e154.md) [`004fe3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fe3e8.md) [`00796f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/00796f8c.md) [`007aa9e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aa9e8.md) [`008648d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00864/008648d0.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 8件 [`0048e194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e194.md) [`004fe428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004fe428.md) [`00796fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00796/00796fcc.md) [`007aaa28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aaa28.md) [`00864910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00864/00864910.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00494c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494c3c.md#insn-00494c70) · [`00494c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494c3c.md#insn-00494c90) · [`00494ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494c3c.md#insn-00494ccc)
- 新版 `00494cb0`（命令位置の公開資料なし） · `00494cd0`（命令位置の公開資料なし） · `00494d0c`（命令位置の公開資料なし）

~~~diff
- 00494c70 ["INT_ADD", "register:40f0:8", ["const:494c70:8", "const:4:8"]]
- 00494c70 ["CALL", null, ["callee:0046d5a8:8"]]
+ 00494cb0 ["INT_ADD", "register:40f0:8", ["const:494cb0:8", "const:4:8"]]
+ 00494cb0 ["CALL", null, ["callee:0046d5a8:8"]]
- 00494c70 bytes 3e62ff97
+ 00494cb0 bytes 3e62ff97
- 00494c90 ["INT_ADD", "register:40f0:8", ["const:494c90:8", "const:4:8"]]
- 00494c90 ["CALL", null, ["callee:00c57e90:8"]]
+ 00494cd0 ["INT_ADD", "register:40f0:8", ["const:494cd0:8", "const:4:8"]]
+ 00494cd0 ["CALL", null, ["callee:00c57e90:8"]]
- 00494c90 bytes 800b1f94
+ 00494cd0 bytes 700c1f94
- 00494ccc ["INT_ADD", "register:40f0:8", ["const:494ccc:8", "const:4:8"]]
- 00494ccc ["CALL", null, ["callee:0043bb20:8"]]
+ 00494d0c ["INT_ADD", "register:40f0:8", ["const:494d0c:8", "const:4:8"]]
+ 00494d0c ["CALL", null, ["callee:0043bb20:8"]]
- 00494ccc bytes 859bfe97
+ 00494d0c bytes 859bfe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0d675b5a6f1b8c2ed1e80204fe6dbf6"></a>

### [`00494d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494d6c.md) → [`00494dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494dac.md) FUN_00494dac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00494d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494d6c.md#insn-00494d98) · [`00494da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494d6c.md#insn-00494da8)
- 新版 `00494dd8`（命令位置の公開資料なし） · `00494de8`（命令位置の公開資料なし）

~~~diff
- 00494d98 ["INT_ADD", "register:40f0:8", ["const:494d98:8", "const:4:8"]]
- 00494d98 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00494dd8 ["INT_ADD", "register:40f0:8", ["const:494dd8:8", "const:4:8"]]
+ 00494dd8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00494d98 bytes 460b1f94
+ 00494dd8 bytes 360c1f94
- 00494da8 ["INT_ADD", "register:40f0:8", ["const:494da8:8", "const:4:8"]]
- 00494da8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00494de8 ["INT_ADD", "register:40f0:8", ["const:494de8:8", "const:4:8"]]
+ 00494de8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00494da8 bytes 420b1f94
+ 00494de8 bytes 320c1f94
~~~


<a id="compare-8cbf7780177c34310afa83876d0e71a6"></a>

### [`00495b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495b24.md) → [`00495b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495b64.md) FUN_00495b64

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00495b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495b24.md#insn-00495b40) · [`00495b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495b24.md#insn-00495b60)
- 新版 `00495b80`（命令位置の公開資料なし） · `00495ba0`（命令位置の公開資料なし）

~~~diff
- 00495b40 ["INT_ADD", "register:40f0:8", ["const:495b40:8", "const:4:8"]]
- 00495b40 ["CALL", null, ["callee:00c53d00:8"]]
+ 00495b80 ["INT_ADD", "register:40f0:8", ["const:495b80:8", "const:4:8"]]
+ 00495b80 ["CALL", null, ["callee:00c53d00:8"]]
- 00495b40 bytes 68f71e94
+ 00495b80 bytes 60f81e94
- 00495b60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00495b60 ["INT_ADD", "register:40f0:8", ["const:495b60:8", "const:4:8"]]
- 00495b60 ["CALLIND", null, ["register:0:8"]]
+ 00495ba0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00495ba0 ["INT_ADD", "register:40f0:8", ["const:495ba0:8", "const:4:8"]]
+ 00495ba0 ["CALLIND", null, ["register:0:8"]]
- 00495b60 bytes 00013fd6
+ 00495ba0 bytes 00013fd6
~~~


<a id="compare-821e2191055e4ff19478bd6e05402fe7"></a>

### [`00495b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495b74.md) → [`00495bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495bb4.md) FUN_00495bb4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0049523c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/0049523c.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0049527c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/0049527c.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00495bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495b74.md#insn-00495bf0) · [`00495c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495b74.md#insn-00495c04) · [`00495c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495b74.md#insn-00495c0c)
- 新版 `00495c30`（命令位置の公開資料なし） · `00495c44`（命令位置の公開資料なし） · `00495c4c`（命令位置の公開資料なし）

~~~diff
- 00495bf0 ["INT_ADD", "register:40f0:8", ["const:495bf0:8", "const:4:8"]]
- 00495bf0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00495c30 ["INT_ADD", "register:40f0:8", ["const:495c30:8", "const:4:8"]]
+ 00495c30 ["CALL", null, ["callee:00c53d00:8"]]
- 00495bf0 bytes 3cf71e94
+ 00495c30 bytes 34f81e94
- 00495c04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00495c04 ["INT_ADD", "register:40f0:8", ["const:495c04:8", "const:4:8"]]
- 00495c04 ["CALLIND", null, ["register:0:8"]]
+ 00495c44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00495c44 ["INT_ADD", "register:40f0:8", ["const:495c44:8", "const:4:8"]]
+ 00495c44 ["CALLIND", null, ["register:0:8"]]
- 00495c04 bytes 00013fd6
+ 00495c44 bytes 00013fd6
- 00495c0c ["INT_ADD", "register:40f0:8", ["const:495c0c:8", "const:4:8"]]
- 00495c0c ["CALL", null, ["callee:00c57e80:8"]]
+ 00495c4c ["INT_ADD", "register:40f0:8", ["const:495c4c:8", "const:4:8"]]
+ 00495c4c ["CALL", null, ["callee:00c57e80:8"]]
- 00495c0c bytes 9d071f94
+ 00495c4c bytes 8d081f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd554f57f6247cc2cad8312fbc4f12c1"></a>

### [`00495d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495d04.md) → [`00495d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495d44.md) FUN_00495d44

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00495394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495394.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004961c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/004961c4.md) [`0049634c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/0049634c.md) [`004964d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/004964d8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`004953d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/004953d4.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00496204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496204.md) [`0049638c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/0049638c.md) [`00496518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496518.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00495d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495d04.md#insn-00495d9c) · [`00495de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495d04.md#insn-00495de0) · [`00495df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495d04.md#insn-00495df0)
- 新版 `00495ddc`（命令位置の公開資料なし） · `00495e20`（命令位置の公開資料なし） · `00495e30`（命令位置の公開資料なし）

~~~diff
- 00495d9c ["INT_ADD", "register:40f0:8", ["const:495d9c:8", "const:4:8"]]
- 00495d9c ["CALL", null, ["callee:00c57f40:8"]]
+ 00495ddc ["INT_ADD", "register:40f0:8", ["const:495ddc:8", "const:4:8"]]
+ 00495ddc ["CALL", null, ["callee:00c57f40:8"]]
- 00495d9c bytes 69071f94
+ 00495ddc bytes 59081f94
- 00495de0 ["INT_ADD", "register:40f0:8", ["const:495de0:8", "const:4:8"]]
- 00495de0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00495e20 ["INT_ADD", "register:40f0:8", ["const:495e20:8", "const:4:8"]]
+ 00495e20 ["CALL", null, ["callee:00c57e90:8"]]
- 00495de0 bytes 2c071f94
+ 00495e20 bytes 1c081f94
- 00495df0 ["INT_ADD", "register:40f0:8", ["const:495df0:8", "const:4:8"]]
- 00495df0 ["CALL", null, ["callee:00496204:8"]]
+ 00495e30 ["INT_ADD", "register:40f0:8", ["const:495e30:8", "const:4:8"]]
+ 00495e30 ["CALL", null, ["callee:00496204:8"]]
- 00495df0 bytes f5000094
+ 00495e30 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce92cab41380e9d65f5086eb41e8a8f3"></a>

### [`004961c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/004961c4.md) → [`00496204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496204.md) FUN_00496204

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00495d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495d04.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00495d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495d44.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049622c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/004961c4.md#insn-0049622c) · [`00496264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/004961c4.md#insn-00496264) · [`00496314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/004961c4.md#insn-00496314)
- 新版 `0049626c`（命令位置の公開資料なし） · `004962a4`（命令位置の公開資料なし） · `00496354`（命令位置の公開資料なし）

~~~diff
- 0049622c ["INT_ADD", "register:40f0:8", ["const:49622c:8", "const:4:8"]]
- 0049622c ["CALL", null, ["callee:00c57f40:8"]]
+ 0049626c ["INT_ADD", "register:40f0:8", ["const:49626c:8", "const:4:8"]]
+ 0049626c ["CALL", null, ["callee:00c57f40:8"]]
- 0049622c bytes 45061f94
+ 0049626c bytes 35071f94
- 00496264 ["INT_ADD", "register:40f0:8", ["const:496264:8", "const:4:8"]]
- 00496264 ["CALL", null, ["callee:00c57e90:8"]]
+ 004962a4 ["INT_ADD", "register:40f0:8", ["const:4962a4:8", "const:4:8"]]
+ 004962a4 ["CALL", null, ["callee:00c57e90:8"]]
- 00496264 bytes 0b061f94
+ 004962a4 bytes fb061f94
- 00496314 ["INT_ADD", "register:40f0:8", ["const:496314:8", "const:4:8"]]
- 00496314 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00496354 ["INT_ADD", "register:40f0:8", ["const:496354:8", "const:4:8"]]
+ 00496354 ["CALL", null, ["callee:00c57eb0:8"]]
- 00496314 bytes e7051f94
+ 00496354 bytes d7061f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e12866e7dca75cb5024195e6bb613ae"></a>

### [`0049634c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/0049634c.md) → [`0049638c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/0049638c.md) FUN_0049638c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00495d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495d04.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00495d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495d44.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004963bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/0049634c.md#insn-004963bc) · [`004963f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/0049634c.md#insn-004963f4) · [`004964a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/0049634c.md#insn-004964a4)
- 新版 `004963fc`（命令位置の公開資料なし） · `00496434`（命令位置の公開資料なし） · `004964e4`（命令位置の公開資料なし）

~~~diff
- 004963bc ["INT_ADD", "register:40f0:8", ["const:4963bc:8", "const:4:8"]]
- 004963bc ["CALL", null, ["callee:00c57f40:8"]]
+ 004963fc ["INT_ADD", "register:40f0:8", ["const:4963fc:8", "const:4:8"]]
+ 004963fc ["CALL", null, ["callee:00c57f40:8"]]
- 004963bc bytes e1051f94
+ 004963fc bytes d1061f94
- 004963f4 ["INT_ADD", "register:40f0:8", ["const:4963f4:8", "const:4:8"]]
- 004963f4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00496434 ["INT_ADD", "register:40f0:8", ["const:496434:8", "const:4:8"]]
+ 00496434 ["CALL", null, ["callee:00c57e90:8"]]
- 004963f4 bytes a7051f94
+ 00496434 bytes 97061f94
- 004964a4 ["INT_ADD", "register:40f0:8", ["const:4964a4:8", "const:4:8"]]
- 004964a4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004964e4 ["INT_ADD", "register:40f0:8", ["const:4964e4:8", "const:4:8"]]
+ 004964e4 ["CALL", null, ["callee:00c57eb0:8"]]
- 004964a4 bytes 83051f94
+ 004964e4 bytes 73061f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f037a61ed277de31f81ca30ef944c932"></a>

### [`004964d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/004964d8.md) → [`00496518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496518.md) FUN_00496518

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00495d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495d04.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00495d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495d44.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00496548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/004964d8.md#insn-00496548) · [`00496580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/004964d8.md#insn-00496580) · [`00496630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/004964d8.md#insn-00496630)
- 新版 `00496588`（命令位置の公開資料なし） · `004965c0`（命令位置の公開資料なし） · `00496670`（命令位置の公開資料なし）

~~~diff
- 00496548 ["INT_ADD", "register:40f0:8", ["const:496548:8", "const:4:8"]]
- 00496548 ["CALL", null, ["callee:00c57f40:8"]]
+ 00496588 ["INT_ADD", "register:40f0:8", ["const:496588:8", "const:4:8"]]
+ 00496588 ["CALL", null, ["callee:00c57f40:8"]]
- 00496548 bytes 7e051f94
+ 00496588 bytes 6e061f94
- 00496580 ["INT_ADD", "register:40f0:8", ["const:496580:8", "const:4:8"]]
- 00496580 ["CALL", null, ["callee:00c57e90:8"]]
+ 004965c0 ["INT_ADD", "register:40f0:8", ["const:4965c0:8", "const:4:8"]]
+ 004965c0 ["CALL", null, ["callee:00c57e90:8"]]
- 00496580 bytes 44051f94
+ 004965c0 bytes 34061f94
- 00496630 ["INT_ADD", "register:40f0:8", ["const:496630:8", "const:4:8"]]
- 00496630 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00496670 ["INT_ADD", "register:40f0:8", ["const:496670:8", "const:4:8"]]
+ 00496670 ["CALL", null, ["callee:00c57eb0:8"]]
- 00496630 bytes 20051f94
+ 00496670 bytes 10061f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3e8fcc37e93aa8a87ccbd854d8a17b5"></a>

### [`00496e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496e34.md) → [`00496e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496e74.md) FUN_00496e74

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004974b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004974b8.md) [`004975bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004975bc.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004974f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004974f8.md) [`004975fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004975fc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00496e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496e34.md#insn-00496e48)
- 新版 `00496e88`（命令位置の公開資料なし）

~~~diff
- 00496e48 ["INT_ADD", "register:40f0:8", ["const:496e48:8", "const:4:8"]]
- 00496e48 ["CALL", null, ["callee:004974f8:8"]]
+ 00496e88 ["INT_ADD", "register:40f0:8", ["const:496e88:8", "const:4:8"]]
+ 00496e88 ["CALL", null, ["callee:004974f8:8"]]
- 00496e48 bytes 9c010094
+ 00496e88 bytes 9c010094
~~~


<a id="compare-a8c7b6a6d59eb1d55b4c7f1b77c19bfa"></a>

### [`00496e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496e78.md) → [`00496eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496eb8.md) FUN_00496eb8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00496e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496e78.md#insn-00496e8c)
- 新版 `00496ecc`（命令位置の公開資料なし）

~~~diff
- 00496e8c ["INT_ADD", "register:40f0:8", ["const:496e8c:8", "const:4:8"]]
- 00496e8c ["CALL", null, ["callee:0044108c:8"]]
+ 00496ecc ["INT_ADD", "register:40f0:8", ["const:496ecc:8", "const:4:8"]]
+ 00496ecc ["CALL", null, ["callee:0044108c:8"]]
- 00496e8c bytes 70a8fe97
+ 00496ecc bytes 70a8fe97
~~~


<a id="compare-e03b7a57c2d294cf75b3a3e4b4598700"></a>

### [`00496ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496ec4.md) → [`00496f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496f04.md) FUN_00496f04

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00496ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496ec4.md#insn-00496ed8)
- 新版 `00496f18`（命令位置の公開資料なし）

~~~diff
- 00496ed8 ["INT_ADD", "register:40f0:8", ["const:496ed8:8", "const:4:8"]]
- 00496ed8 ["CALL", null, ["callee:0044108c:8"]]
+ 00496f18 ["INT_ADD", "register:40f0:8", ["const:496f18:8", "const:4:8"]]
+ 00496f18 ["CALL", null, ["callee:0044108c:8"]]
- 00496ed8 bytes 5da8fe97
+ 00496f18 bytes 5da8fe97
~~~


<a id="compare-5b9f24914a598f7bc7c0af3c9dcc6d61"></a>

### [`00496f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496f10.md) → [`00496f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496f50.md) FUN_00496f50

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00496f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496f10.md#insn-00496f24)
- 新版 `00496f64`（命令位置の公開資料なし）

~~~diff
- 00496f24 ["INT_ADD", "register:40f0:8", ["const:496f24:8", "const:4:8"]]
- 00496f24 ["CALL", null, ["callee:0044108c:8"]]
+ 00496f64 ["INT_ADD", "register:40f0:8", ["const:496f64:8", "const:4:8"]]
+ 00496f64 ["CALL", null, ["callee:0044108c:8"]]
- 00496f24 bytes 4aa8fe97
+ 00496f64 bytes 4aa8fe97
~~~


<a id="compare-4ce6235380d2241c19c0fa7bfc81000c"></a>

### [`00496f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496f5c.md) → [`00496f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496f9c.md) FUN_00496f9c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00496f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496f5c.md#insn-00496f70) · [`00496f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496f5c.md#insn-00496f8c)
- 新版 `00496fb0`（命令位置の公開資料なし） · `00496fcc`（命令位置の公開資料なし）

~~~diff
- 00496f70 ["INT_ADD", "register:40f0:8", ["const:496f70:8", "const:4:8"]]
- 00496f70 ["CALL", null, ["callee:0044108c:8"]]
+ 00496fb0 ["INT_ADD", "register:40f0:8", ["const:496fb0:8", "const:4:8"]]
+ 00496fb0 ["CALL", null, ["callee:0044108c:8"]]
- 00496f70 bytes 37a8fe97
+ 00496fb0 bytes 37a8fe97
- 00496f8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00496f8c ["INT_ADD", "register:40f0:8", ["const:496f8c:8", "const:4:8"]]
- 00496f8c ["CALLIND", null, ["register:0:8"]]
+ 00496fcc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00496fcc ["INT_ADD", "register:40f0:8", ["const:496fcc:8", "const:4:8"]]
+ 00496fcc ["CALLIND", null, ["register:0:8"]]
- 00496f8c bytes 00013fd6
+ 00496fcc bytes 00013fd6
~~~


<a id="compare-c0b38ec02ddb7cf77569512c3c86fb89"></a>

### [`00496fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496fa4.md) → [`00496fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496fe4.md) FUN_00496fe4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00496fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496fa4.md#insn-00496fbc)
- 新版 `00496ffc`（命令位置の公開資料なし）

~~~diff
- 00496fbc ["INT_ADD", "register:40f0:8", ["const:496fbc:8", "const:4:8"]]
- 00496fbc ["CALL", null, ["callee:0044108c:8"]]
+ 00496ffc ["INT_ADD", "register:40f0:8", ["const:496ffc:8", "const:4:8"]]
+ 00496ffc ["CALL", null, ["callee:0044108c:8"]]
- 00496fbc bytes 24a8fe97
+ 00496ffc bytes 24a8fe97
~~~


<a id="compare-832fb52ec6ac31f0e1e366b0e0f97e6d"></a>

### [`004974b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004974b8.md) → [`004974f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004974f8.md) FUN_004974f8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00496e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496e34.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00496e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496e74.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00497524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004974b8.md#insn-00497524) · [`00497580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004974b8.md#insn-00497580)
- 新版 `00497564`（命令位置の公開資料なし） · `004975c0`（命令位置の公開資料なし）

~~~diff
- 00497524 ["INT_ADD", "register:40f0:8", ["const:497524:8", "const:4:8"]]
- 00497524 ["CALL", null, ["callee:00c58050:8"]]
+ 00497564 ["INT_ADD", "register:40f0:8", ["const:497564:8", "const:4:8"]]
+ 00497564 ["CALL", null, ["callee:00c58050:8"]]
- 00497524 bytes cb011f94
+ 00497564 bytes bb021f94
- 00497580 ["INT_ADD", "register:40f0:8", ["const:497580:8", "const:4:8"]]
- 00497580 ["CALL", null, ["callee:00c58050:8"]]
+ 004975c0 ["INT_ADD", "register:40f0:8", ["const:4975c0:8", "const:4:8"]]
+ 004975c0 ["CALL", null, ["callee:00c58050:8"]]
- 00497580 bytes b4011f94
+ 004975c0 bytes a4021f94
~~~


<a id="compare-299353a910c4a4187cc381394884a0b8"></a>

### [`004975bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004975bc.md) → [`004975fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004975fc.md) FUN_004975fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00496e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496e34.md) · 呼出先 2件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00496e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496e74.md) · 呼出先 2件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00497620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004975bc.md#insn-00497620) · [`00497638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004975bc.md#insn-00497638) · [`00497648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004975bc.md#insn-00497648)
- 新版 `00497660`（命令位置の公開資料なし） · `00497678`（命令位置の公開資料なし） · `00497688`（命令位置の公開資料なし）

~~~diff
- 00497620 ["INT_ADD", "register:40f0:8", ["const:497620:8", "const:4:8"]]
- 00497620 ["CALL", null, ["callee:00494610:8"]]
+ 00497660 ["INT_ADD", "register:40f0:8", ["const:497660:8", "const:4:8"]]
+ 00497660 ["CALL", null, ["callee:00494610:8"]]
- 00497620 bytes ecf3ff97
+ 00497660 bytes ecf3ff97
- 00497638 ["COPY", "register:0:8", ["register:4040:8"]]
- 00497638 ["INT_ADD", "register:40f0:8", ["const:497638:8", "const:4:8"]]
- 00497638 ["CALLIND", null, ["register:0:8"]]
+ 00497678 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00497678 ["INT_ADD", "register:40f0:8", ["const:497678:8", "const:4:8"]]
+ 00497678 ["CALLIND", null, ["register:0:8"]]
- 00497638 bytes 00013fd6
+ 00497678 bytes 00013fd6
- 00497648 ["INT_ADD", "register:40f0:8", ["const:497648:8", "const:4:8"]]
- 00497648 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00497688 ["INT_ADD", "register:40f0:8", ["const:497688:8", "const:4:8"]]
+ 00497688 ["CALL", null, ["callee:00c57eb0:8"]]
- 00497648 bytes 1a011f94
+ 00497688 bytes 0a021f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d48dcd9e7f81e20a98a744c7c9be725f"></a>

### [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) → [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) FUN_00497834

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 135件 [`00497664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497664.md) [`005788d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/005788d0.md) [`0057e49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e49c.md) [`0057e7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e7f4.md) [`0057f5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f5ec.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 135件 [`004976a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004976a4.md) [`00578910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578910.md) [`0057e4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e4dc.md) [`0057e834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e834.md) [`0057f62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f62c.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00497868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md#insn-00497868) · [`0049788c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md#insn-0049788c)
- 新版 `004978a8`（命令位置の公開資料なし） · `004978cc`（命令位置の公開資料なし）

~~~diff
- 00497868 ["COPY", "register:0:8", ["register:4040:8"]]
- 00497868 ["INT_ADD", "register:40f0:8", ["const:497868:8", "const:4:8"]]
- 00497868 ["CALLIND", null, ["register:0:8"]]
+ 004978a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004978a8 ["INT_ADD", "register:40f0:8", ["const:4978a8:8", "const:4:8"]]
+ 004978a8 ["CALLIND", null, ["register:0:8"]]
- 00497868 bytes 00013fd6
+ 004978a8 bytes 00013fd6
- 0049788c ["INT_ADD", "register:40f0:8", ["const:49788c:8", "const:4:8"]]
- 0049788c ["CALL", null, ["callee:00c57ee0:8"]]
+ 004978cc ["INT_ADD", "register:40f0:8", ["const:4978cc:8", "const:4:8"]]
+ 004978cc ["CALL", null, ["callee:00c57ee0:8"]]
- 0049788c bytes 95001f94
+ 004978cc bytes 85011f94
~~~


<a id="compare-55c090c1ccb483ad4be996ad43bf84d7"></a>

### [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) → [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) FUN_00497a48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 46件 [`00497890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497890.md) [`0049b17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b17c.md) [`005717c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005717c0.md) [`0057192c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/0057192c.md) [`005729a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/005729a4.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 46件 [`004978d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004978d0.md) [`0049b1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b1bc.md) [`00571800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571800.md) [`0057196c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/0057196c.md) [`005729e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005729e4.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00497a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md#insn-00497a7c) · [`00497aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md#insn-00497aa0)
- 新版 `00497abc`（命令位置の公開資料なし） · `00497ae0`（命令位置の公開資料なし）

~~~diff
- 00497a7c ["COPY", "register:0:8", ["register:4040:8"]]
- 00497a7c ["INT_ADD", "register:40f0:8", ["const:497a7c:8", "const:4:8"]]
- 00497a7c ["CALLIND", null, ["register:0:8"]]
+ 00497abc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00497abc ["INT_ADD", "register:40f0:8", ["const:497abc:8", "const:4:8"]]
+ 00497abc ["CALLIND", null, ["register:0:8"]]
- 00497a7c bytes 00013fd6
+ 00497abc bytes 00013fd6
- 00497aa0 ["INT_ADD", "register:40f0:8", ["const:497aa0:8", "const:4:8"]]
- 00497aa0 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00497ae0 ["INT_ADD", "register:40f0:8", ["const:497ae0:8", "const:4:8"]]
+ 00497ae0 ["CALL", null, ["callee:00c57ee0:8"]]
- 00497aa0 bytes 10001f94
+ 00497ae0 bytes 00011f94
~~~


<a id="compare-40f22e33819d354ffd1550ef2867e757"></a>

### [`00497b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497b9c.md) → [`00497bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497bdc.md) FUN_00497bdc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00497bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497b9c.md#insn-00497bb8) · [`00497bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497b9c.md#insn-00497bd8)
- 新版 `00497bf8`（命令位置の公開資料なし） · `00497c18`（命令位置の公開資料なし）

~~~diff
- 00497bb8 ["INT_ADD", "register:40f0:8", ["const:497bb8:8", "const:4:8"]]
- 00497bb8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00497bf8 ["INT_ADD", "register:40f0:8", ["const:497bf8:8", "const:4:8"]]
+ 00497bf8 ["CALL", null, ["callee:00c53d00:8"]]
- 00497bb8 bytes 4aef1e94
+ 00497bf8 bytes 42f01e94
- 00497bd8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00497bd8 ["INT_ADD", "register:40f0:8", ["const:497bd8:8", "const:4:8"]]
- 00497bd8 ["CALLIND", null, ["register:0:8"]]
+ 00497c18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00497c18 ["INT_ADD", "register:40f0:8", ["const:497c18:8", "const:4:8"]]
+ 00497c18 ["CALLIND", null, ["register:0:8"]]
- 00497bd8 bytes 00013fd6
+ 00497c18 bytes 00013fd6
~~~


<a id="compare-85fe4d36b2db0c6d94105b77bc2772ed"></a>

### [`00497bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497bec.md) → [`00497c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497c2c.md) FUN_00497c2c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00497c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497bec.md#insn-00497c08) · [`00497c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497bec.md#insn-00497c28)
- 新版 `00497c48`（命令位置の公開資料なし） · `00497c68`（命令位置の公開資料なし）

~~~diff
- 00497c08 ["INT_ADD", "register:40f0:8", ["const:497c08:8", "const:4:8"]]
- 00497c08 ["CALL", null, ["callee:00c53d00:8"]]
+ 00497c48 ["INT_ADD", "register:40f0:8", ["const:497c48:8", "const:4:8"]]
+ 00497c48 ["CALL", null, ["callee:00c53d00:8"]]
- 00497c08 bytes 36ef1e94
+ 00497c48 bytes 2ef01e94
- 00497c28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00497c28 ["INT_ADD", "register:40f0:8", ["const:497c28:8", "const:4:8"]]
- 00497c28 ["CALLIND", null, ["register:0:8"]]
+ 00497c68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00497c68 ["INT_ADD", "register:40f0:8", ["const:497c68:8", "const:4:8"]]
+ 00497c68 ["CALLIND", null, ["register:0:8"]]
- 00497c28 bytes 00013fd6
+ 00497c68 bytes 00013fd6
~~~


<a id="compare-f2986e9bb989156d92c2746582fb3864"></a>

### [`00498094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498094.md) → [`004980d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004980d4.md) FUN_004980d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00497c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497c3c.md) [`00497db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497db4.md) [`00498308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498308.md) · 呼出先 4件 [`0049975c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049975c.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`00497c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497c7c.md) [`00497df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497df4.md) [`00498348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498348.md) · 呼出先 4件 [`0049979c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/0049979c.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c58380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004980b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498094.md#insn-004980b0) · [`004980e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498094.md#insn-004980e8) · [`00498134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498094.md#insn-00498134)
- 新版 `004980f0`（命令位置の公開資料なし） · `00498128`（命令位置の公開資料なし） · `00498174`（命令位置の公開資料なし）

~~~diff
- 004980b0 ["INT_ADD", "register:40f0:8", ["const:4980b0:8", "const:4:8"]]
- 004980b0 ["CALL", null, ["callee:00c580e0:8"]]
+ 004980f0 ["INT_ADD", "register:40f0:8", ["const:4980f0:8", "const:4:8"]]
+ 004980f0 ["CALL", null, ["callee:00c580e0:8"]]
- 004980b0 bytes 0cff1e94
+ 004980f0 bytes fcff1e94
- 004980e8 ["INT_ADD", "register:40f0:8", ["const:4980e8:8", "const:4:8"]]
- 004980e8 ["CALL", null, ["callee:0049979c:8"]]
+ 00498128 ["INT_ADD", "register:40f0:8", ["const:498128:8", "const:4:8"]]
+ 00498128 ["CALL", null, ["callee:0049979c:8"]]
- 004980e8 bytes 9d050094
+ 00498128 bytes 9d050094
- 00498134 ["COPY", "register:0:8", ["register:4040:8"]]
- 00498134 ["INT_ADD", "register:40f0:8", ["const:498134:8", "const:4:8"]]
- 00498134 ["CALLIND", null, ["register:0:8"]]
+ 00498174 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00498174 ["INT_ADD", "register:40f0:8", ["const:498174:8", "const:4:8"]]
+ 00498174 ["CALLIND", null, ["register:0:8"]]
- 00498134 bytes 00013fd6
+ 00498174 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58a67b1d9e45bbfc8d611c2cf042922a"></a>

### [`004985a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004985a0.md) → [`004985e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004985e0.md) FUN_004985e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00498308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498308.md) · 呼出先 4件 [`0049a264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a264.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00498348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498348.md) · 呼出先 4件 [`0049a2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a2a4.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c58380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004985bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004985a0.md#insn-004985bc) · [`004985f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004985a0.md#insn-004985f4) · [`00498644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004985a0.md#insn-00498644)
- 新版 `004985fc`（命令位置の公開資料なし） · `00498634`（命令位置の公開資料なし） · `00498684`（命令位置の公開資料なし）

~~~diff
- 004985bc ["INT_ADD", "register:40f0:8", ["const:4985bc:8", "const:4:8"]]
- 004985bc ["CALL", null, ["callee:00c580e0:8"]]
+ 004985fc ["INT_ADD", "register:40f0:8", ["const:4985fc:8", "const:4:8"]]
+ 004985fc ["CALL", null, ["callee:00c580e0:8"]]
- 004985bc bytes c9fd1e94
+ 004985fc bytes b9fe1e94
- 004985f4 ["INT_ADD", "register:40f0:8", ["const:4985f4:8", "const:4:8"]]
- 004985f4 ["CALL", null, ["callee:0049a2a4:8"]]
+ 00498634 ["INT_ADD", "register:40f0:8", ["const:498634:8", "const:4:8"]]
+ 00498634 ["CALL", null, ["callee:0049a2a4:8"]]
- 004985f4 bytes 1c070094
+ 00498634 bytes 1c070094
- 00498644 ["COPY", "register:0:8", ["register:4040:8"]]
- 00498644 ["INT_ADD", "register:40f0:8", ["const:498644:8", "const:4:8"]]
- 00498644 ["CALLIND", null, ["register:0:8"]]
+ 00498684 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00498684 ["INT_ADD", "register:40f0:8", ["const:498684:8", "const:4:8"]]
+ 00498684 ["CALLIND", null, ["register:0:8"]]
- 00498644 bytes 00013fd6
+ 00498684 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2618e14083eb0caf6b712177e099c53"></a>

### [`004987c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004987c4.md) → [`00498804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498804.md) FUN_00498804

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 22件 [`0067fd6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067f/0067fd6c.md) [`00680dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00680/00680dc8.md) [`006b3b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3b64.md) [`006b53c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b5/006b53c4.md) [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) · 呼出先 2件 [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)
- 新版 呼出元 22件 [`0067fdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067f/0067fdac.md) [`00680e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00680/00680e08.md) [`006b3ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b3/006b3ba4.md) [`006b5404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b5/006b5404.md) [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) · 呼出先 2件 [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004987f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004987c4.md#insn-004987f0) · [`004987fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004987c4.md#insn-004987fc) · [`00498814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004987c4.md#insn-00498814)
- 新版 `00498830`（命令位置の公開資料なし） · `0049883c`（命令位置の公開資料なし） · `00498854`（命令位置の公開資料なし）

~~~diff
- 004987f0 ["INT_ADD", "register:40f0:8", ["const:4987f0:8", "const:4:8"]]
- 004987f0 ["CALL", null, ["callee:00c580e0:8"]]
+ 00498830 ["INT_ADD", "register:40f0:8", ["const:498830:8", "const:4:8"]]
+ 00498830 ["CALL", null, ["callee:00c580e0:8"]]
- 004987f0 bytes 3cfd1e94
+ 00498830 bytes 2cfe1e94
- 004987fc ["INT_ADD", "register:40f0:8", ["const:4987fc:8", "const:4:8"]]
- 004987fc ["CALL", null, ["callee:00c580f0:8"]]
+ 0049883c ["INT_ADD", "register:40f0:8", ["const:49883c:8", "const:4:8"]]
+ 0049883c ["CALL", null, ["callee:00c580f0:8"]]
- 004987fc bytes 3dfd1e94
+ 0049883c bytes 2dfe1e94
- 00498814 ["INT_ADD", "register:40f0:8", ["const:498814:8", "const:4:8"]]
- 00498814 ["CALL", null, ["callee:00c580e0:8"]]
+ 00498854 ["INT_ADD", "register:40f0:8", ["const:498854:8", "const:4:8"]]
+ 00498854 ["CALL", null, ["callee:00c580e0:8"]]
- 00498814 bytes 33fd1e94
+ 00498854 bytes 23fe1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b2e60988636260d46b5ab7766f1e950"></a>

### [`0049883c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/0049883c.md) → [`0049887c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/0049887c.md) FUN_0049887c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0086b314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b314.md) [`0086b52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b52c.md) · 呼出先 2件 [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)
- 新版 呼出元 2件 [`0086b354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b354.md) [`0086b56c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b56c.md) · 呼出先 2件 [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049885c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/0049883c.md#insn-0049885c) · [`00498868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/0049883c.md#insn-00498868) · [`00498878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/0049883c.md#insn-00498878)
- 新版 `0049889c`（命令位置の公開資料なし） · `004988a8`（命令位置の公開資料なし） · `004988b8`（命令位置の公開資料なし）

~~~diff
- 0049885c ["INT_ADD", "register:40f0:8", ["const:49885c:8", "const:4:8"]]
- 0049885c ["CALL", null, ["callee:00c580e0:8"]]
+ 0049889c ["INT_ADD", "register:40f0:8", ["const:49889c:8", "const:4:8"]]
+ 0049889c ["CALL", null, ["callee:00c580e0:8"]]
- 0049885c bytes 21fd1e94
+ 0049889c bytes 11fe1e94
- 00498868 ["INT_ADD", "register:40f0:8", ["const:498868:8", "const:4:8"]]
- 00498868 ["CALL", null, ["callee:00c580f0:8"]]
+ 004988a8 ["INT_ADD", "register:40f0:8", ["const:4988a8:8", "const:4:8"]]
+ 004988a8 ["CALL", null, ["callee:00c580f0:8"]]
- 00498868 bytes 22fd1e94
+ 004988a8 bytes 12fe1e94
- 00498878 ["INT_ADD", "register:40f0:8", ["const:498878:8", "const:4:8"]]
- 00498878 ["CALL", null, ["callee:00c580e0:8"]]
+ 004988b8 ["INT_ADD", "register:40f0:8", ["const:4988b8:8", "const:4:8"]]
+ 004988b8 ["CALL", null, ["callee:00c580e0:8"]]
- 00498878 bytes 1afd1e94
+ 004988b8 bytes 0afe1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bc97212284fd1c33bd2cfef99daf3a2"></a>

### [`004988dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004988dc.md) → [`0049891c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/0049891c.md) FUN_0049891c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00498910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498910.md) [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cd0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00498950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498950.md) [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004988f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004988dc.md#insn-004988f0) · [`004988f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004988dc.md#insn-004988f8)
- 新版 `00498930`（命令位置の公開資料なし） · `00498938`（命令位置の公開資料なし）

~~~diff
- 004988f0 ["INT_ADD", "register:40f0:8", ["const:4988f0:8", "const:4:8"]]
- 004988f0 ["CALL", null, ["callee:00c580d0:8"]]
+ 00498930 ["INT_ADD", "register:40f0:8", ["const:498930:8", "const:4:8"]]
+ 00498930 ["CALL", null, ["callee:00c580d0:8"]]
- 004988f0 bytes f8fc1e94
+ 00498930 bytes e8fd1e94
- 004988f8 ["INT_ADD", "register:40f0:8", ["const:4988f8:8", "const:4:8"]]
- 004988f8 ["CALL", null, ["callee:00c57e60:8"]]
+ 00498938 ["INT_ADD", "register:40f0:8", ["const:498938:8", "const:4:8"]]
+ 00498938 ["CALL", null, ["callee:00c57e60:8"]]
- 004988f8 bytes 5afc1e94
+ 00498938 bytes 4afd1e94
~~~


<a id="compare-5c90e5e1e7b0b16254102d417d106cc6"></a>

### [`00498910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498910.md) → [`00498950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498950.md) FUN_00498950

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004988dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004988dc.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0049891c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/0049891c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004989b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498910.md#insn-004989b0) · [`004989fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498910.md#insn-004989fc) · [`00498a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498910.md#insn-00498a48)
- 新版 `004989f0`（命令位置の公開資料なし） · `00498a3c`（命令位置の公開資料なし） · `00498a88`（命令位置の公開資料なし）

~~~diff
- 004989b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004989b0 ["INT_ADD", "register:40f0:8", ["const:4989b0:8", "const:4:8"]]
- 004989b0 ["CALLIND", null, ["register:0:8"]]
+ 004989f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004989f0 ["INT_ADD", "register:40f0:8", ["const:4989f0:8", "const:4:8"]]
+ 004989f0 ["CALLIND", null, ["register:0:8"]]
- 004989b0 bytes 00013fd6
+ 004989f0 bytes 00013fd6
- 004989fc ["INT_ADD", "register:40f0:8", ["const:4989fc:8", "const:4:8"]]
- 004989fc ["CALL", null, ["callee:00c57eb0:8"]]
+ 00498a3c ["INT_ADD", "register:40f0:8", ["const:498a3c:8", "const:4:8"]]
+ 00498a3c ["CALL", null, ["callee:00c57eb0:8"]]
- 004989fc bytes 2dfc1e94
+ 00498a3c bytes 1dfd1e94
- 00498a48 ["INT_ADD", "register:40f0:8", ["const:498a48:8", "const:4:8"]]
- 00498a48 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00498a88 ["INT_ADD", "register:40f0:8", ["const:498a88:8", "const:4:8"]]
+ 00498a88 ["CALL", null, ["callee:00c57eb0:8"]]
- 00498a48 bytes 1afc1e94
+ 00498a88 bytes 0afd1e94
~~~


<a id="compare-54fd8ea8c95c555be4012ccb247f029a"></a>

### [`00498aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498aec.md) → [`00498b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498b2c.md) FUN_00498b2c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00498b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498b20.md) [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cd0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00498b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498b60.md) [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00498b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498aec.md#insn-00498b00) · [`00498b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498aec.md#insn-00498b08)
- 新版 `00498b40`（命令位置の公開資料なし） · `00498b48`（命令位置の公開資料なし）

~~~diff
- 00498b00 ["INT_ADD", "register:40f0:8", ["const:498b00:8", "const:4:8"]]
- 00498b00 ["CALL", null, ["callee:00c580d0:8"]]
+ 00498b40 ["INT_ADD", "register:40f0:8", ["const:498b40:8", "const:4:8"]]
+ 00498b40 ["CALL", null, ["callee:00c580d0:8"]]
- 00498b00 bytes 74fc1e94
+ 00498b40 bytes 64fd1e94
- 00498b08 ["INT_ADD", "register:40f0:8", ["const:498b08:8", "const:4:8"]]
- 00498b08 ["CALL", null, ["callee:00c57e60:8"]]
+ 00498b48 ["INT_ADD", "register:40f0:8", ["const:498b48:8", "const:4:8"]]
+ 00498b48 ["CALL", null, ["callee:00c57e60:8"]]
- 00498b08 bytes d6fb1e94
+ 00498b48 bytes c6fc1e94
~~~


<a id="compare-f9fc064f439d5c4818387e93bb9cdf8c"></a>

### [`00498b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498b20.md) → [`00498b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498b60.md) FUN_00498b60

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00498aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498aec.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00498b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498b2c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00498bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498b20.md#insn-00498bc0) · [`00498c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498b20.md#insn-00498c0c) · [`00498c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498b20.md#insn-00498c58)
- 新版 `00498c00`（命令位置の公開資料なし） · `00498c4c`（命令位置の公開資料なし） · `00498c98`（命令位置の公開資料なし）

~~~diff
- 00498bc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00498bc0 ["INT_ADD", "register:40f0:8", ["const:498bc0:8", "const:4:8"]]
- 00498bc0 ["CALLIND", null, ["register:0:8"]]
+ 00498c00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00498c00 ["INT_ADD", "register:40f0:8", ["const:498c00:8", "const:4:8"]]
+ 00498c00 ["CALLIND", null, ["register:0:8"]]
- 00498bc0 bytes 00013fd6
+ 00498c00 bytes 00013fd6
- 00498c0c ["INT_ADD", "register:40f0:8", ["const:498c0c:8", "const:4:8"]]
- 00498c0c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00498c4c ["INT_ADD", "register:40f0:8", ["const:498c4c:8", "const:4:8"]]
+ 00498c4c ["CALL", null, ["callee:00c57eb0:8"]]
- 00498c0c bytes a9fb1e94
+ 00498c4c bytes 99fc1e94
- 00498c58 ["INT_ADD", "register:40f0:8", ["const:498c58:8", "const:4:8"]]
- 00498c58 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00498c98 ["INT_ADD", "register:40f0:8", ["const:498c98:8", "const:4:8"]]
+ 00498c98 ["CALL", null, ["callee:00c57eb0:8"]]
- 00498c58 bytes 96fb1e94
+ 00498c98 bytes 86fc1e94
~~~


<a id="compare-e497103a65a89a96885d20162b56dce0"></a>

### [`004991d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004991d4.md) → [`00499214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499214.md) FUN_00499214

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00499224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004991d4.md#insn-00499224) · [`00499238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004991d4.md#insn-00499238) · [`00499240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004991d4.md#insn-00499240)
- 新版 `00499264`（命令位置の公開資料なし） · `00499278`（命令位置の公開資料なし） · `00499280`（命令位置の公開資料なし）

~~~diff
- 00499224 ["COPY", "register:0:8", ["register:4040:8"]]
- 00499224 ["INT_ADD", "register:40f0:8", ["const:499224:8", "const:4:8"]]
- 00499224 ["CALLIND", null, ["register:0:8"]]
+ 00499264 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00499264 ["INT_ADD", "register:40f0:8", ["const:499264:8", "const:4:8"]]
+ 00499264 ["CALLIND", null, ["register:0:8"]]
- 00499224 bytes 00013fd6
+ 00499264 bytes 00013fd6
- 00499238 ["INT_ADD", "register:40f0:8", ["const:499238:8", "const:4:8"]]
- 00499238 ["CALL", null, ["callee:00c58150:8"]]
+ 00499278 ["INT_ADD", "register:40f0:8", ["const:499278:8", "const:4:8"]]
+ 00499278 ["CALL", null, ["callee:00c58150:8"]]
- 00499238 bytes c6fa1e94
+ 00499278 bytes b6fb1e94
- 00499240 ["INT_ADD", "register:40f0:8", ["const:499240:8", "const:4:8"]]
- 00499240 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00499280 ["INT_ADD", "register:40f0:8", ["const:499280:8", "const:4:8"]]
+ 00499280 ["CALL", null, ["callee:00c57eb0:8"]]
- 00499240 bytes 1cfa1e94
+ 00499280 bytes 0cfb1e94
~~~


<a id="compare-364b96bb848e64e55d9990b640e2e1d2"></a>

### [`00499254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499254.md) → [`00499294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499294.md) FUN_00499294

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00499270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499254.md#insn-00499270)
- 新版 `004992b0`（命令位置の公開資料なし）

~~~diff
- 00499270 ["INT_ADD", "register:40f0:8", ["const:499270:8", "const:4:8"]]
- 00499270 ["CALL", null, ["callee:00c58150:8"]]
+ 004992b0 ["INT_ADD", "register:40f0:8", ["const:4992b0:8", "const:4:8"]]
+ 004992b0 ["CALL", null, ["callee:00c58150:8"]]
- 00499270 bytes b8fa1e94
+ 004992b0 bytes a8fb1e94
~~~


<a id="compare-75f27e4bf5ba9f515962e663a4d6d0a4"></a>

### [`00499290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499290.md) → [`004992d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/004992d0.md) FUN_004992d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00498cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498cbc.md) · 呼出先 4件 [`00499430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499430.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00498cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498cfc.md) · 呼出先 4件 [`00499470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499470.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00499304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499290.md#insn-00499304) · [`0049932c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499290.md#insn-0049932c) · [`0049933c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499290.md#insn-0049933c)
- 新版 `00499344`（命令位置の公開資料なし） · `0049936c`（命令位置の公開資料なし） · `0049937c`（命令位置の公開資料なし）

~~~diff
- 00499304 ["COPY", "register:0:8", ["register:4048:8"]]
- 00499304 ["INT_ADD", "register:40f0:8", ["const:499304:8", "const:4:8"]]
- 00499304 ["CALLIND", null, ["register:0:8"]]
+ 00499344 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00499344 ["INT_ADD", "register:40f0:8", ["const:499344:8", "const:4:8"]]
+ 00499344 ["CALLIND", null, ["register:0:8"]]
- 00499304 bytes 20013fd6
+ 00499344 bytes 20013fd6
- 0049932c ["COPY", "register:0:8", ["register:4040:8"]]
- 0049932c ["INT_ADD", "register:40f0:8", ["const:49932c:8", "const:4:8"]]
- 0049932c ["CALLIND", null, ["register:0:8"]]
+ 0049936c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049936c ["INT_ADD", "register:40f0:8", ["const:49936c:8", "const:4:8"]]
+ 0049936c ["CALLIND", null, ["register:0:8"]]
- 0049932c bytes 00013fd6
+ 0049936c bytes 00013fd6
- 0049933c ["INT_ADD", "register:40f0:8", ["const:49933c:8", "const:4:8"]]
- 0049933c ["CALL", null, ["callee:00499470:8"]]
+ 0049937c ["INT_ADD", "register:40f0:8", ["const:49937c:8", "const:4:8"]]
+ 0049937c ["CALL", null, ["callee:00499470:8"]]
- 0049933c bytes 3d000094
+ 0049937c bytes 3d000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7329d484c863dbf911449ab583fcfd6"></a>

### [`00499430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499430.md) → [`00499470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499470.md) FUN_00499470

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00498cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498cbc.md) [`00499290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499290.md) [`0049a0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a0bc.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 3件 [`00498cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498cfc.md) [`004992d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/004992d0.md) [`0049a0fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a0fc.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049949c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499430.md#insn-0049949c) · [`004994ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499430.md#insn-004994ac) · [`004994cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499430.md#insn-004994cc)
- 新版 `004994dc`（命令位置の公開資料なし） · `004994ec`（命令位置の公開資料なし） · `0049950c`（命令位置の公開資料なし）

~~~diff
- 0049949c ["COPY", "register:0:8", ["register:4040:8"]]
- 0049949c ["INT_ADD", "register:40f0:8", ["const:49949c:8", "const:4:8"]]
- 0049949c ["CALLIND", null, ["register:0:8"]]
+ 004994dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004994dc ["INT_ADD", "register:40f0:8", ["const:4994dc:8", "const:4:8"]]
+ 004994dc ["CALLIND", null, ["register:0:8"]]
- 0049949c bytes 00013fd6
+ 004994dc bytes 00013fd6
- 004994ac ["COPY", "register:0:8", ["register:4040:8"]]
- 004994ac ["INT_ADD", "register:40f0:8", ["const:4994ac:8", "const:4:8"]]
- 004994ac ["CALLIND", null, ["register:0:8"]]
+ 004994ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 004994ec ["INT_ADD", "register:40f0:8", ["const:4994ec:8", "const:4:8"]]
+ 004994ec ["CALLIND", null, ["register:0:8"]]
- 004994ac bytes 00013fd6
+ 004994ec bytes 00013fd6
- 004994cc ["COPY", "register:0:8", ["register:4040:8"]]
- 004994cc ["INT_ADD", "register:40f0:8", ["const:4994cc:8", "const:4:8"]]
- 004994cc ["CALLIND", null, ["register:0:8"]]
+ 0049950c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049950c ["INT_ADD", "register:40f0:8", ["const:49950c:8", "const:4:8"]]
+ 0049950c ["CALLIND", null, ["register:0:8"]]
- 004994cc bytes 00013fd6
+ 0049950c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03a7327dc975b2c4dc9f12d65c551b3f"></a>

### [`00499604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499604.md) → [`00499644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499644.md) FUN_00499644

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00499648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499604.md#insn-00499648) · [`0049967c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499604.md#insn-0049967c) · [`00499680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499604.md#insn-00499680)
- 新版 `00499688`（命令位置の公開資料なし） · `004996bc`（命令位置の公開資料なし） · `004996c0`（命令位置の公開資料なし）

~~~diff
- 00499648 ["COPY", "register:0:8", ["register:4040:8"]]
- 00499648 ["INT_ADD", "register:40f0:8", ["const:499648:8", "const:4:8"]]
- 00499648 ["CALLIND", null, ["register:0:8"]]
+ 00499688 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00499688 ["INT_ADD", "register:40f0:8", ["const:499688:8", "const:4:8"]]
+ 00499688 ["CALLIND", null, ["register:0:8"]]
- 00499648 bytes 00013fd6
+ 00499688 bytes 00013fd6
- 0049967c ["INT_ADD", "register:40f0:8", ["const:49967c:8", "const:4:8"]]
- 0049967c ["CALL", null, ["callee:00459d74:8"]]
+ 004996bc ["INT_ADD", "register:40f0:8", ["const:4996bc:8", "const:4:8"]]
+ 004996bc ["CALL", null, ["callee:00459d74:8"]]
- 0049967c bytes ae01ff97
+ 004996bc bytes ae01ff97
- 00499680 ["INT_ADD", "register:40f0:8", ["const:499680:8", "const:4:8"]]
- 00499680 ["CALL", null, ["callee:00c57ee0:8"]]
+ 004996c0 ["INT_ADD", "register:40f0:8", ["const:4996c0:8", "const:4:8"]]
+ 004996c0 ["CALL", null, ["callee:00c57ee0:8"]]
- 00499680 bytes 18f91e94
+ 004996c0 bytes 08fa1e94
~~~


<a id="compare-e6158e85570a31c9c13c8213c0b1ef75"></a>

### [`00499708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499708.md) → [`00499748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499748.md) FUN_00499748

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00499730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499708.md#insn-00499730)
- 新版 `00499770`（命令位置の公開資料なし）

~~~diff
- 00499730 ["INT_ADD", "register:40f0:8", ["const:499730:8", "const:4:8"]]
- 00499730 ["CALL", null, ["callee:00459d74:8"]]
+ 00499770 ["INT_ADD", "register:40f0:8", ["const:499770:8", "const:4:8"]]
+ 00499770 ["CALL", null, ["callee:00459d74:8"]]
- 00499730 bytes 8101ff97
+ 00499770 bytes 8101ff97
~~~


<a id="compare-d2c1cdd839f90ce747cfc0f905f9fa00"></a>

### [`0049975c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049975c.md) → [`0049979c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/0049979c.md) FUN_0049979c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00498094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498094.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00499c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499c1c.md) [`00499da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499da4.md) [`00499f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499f30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`004980d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004980d4.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00499c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499c5c.md) [`00499de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499de4.md) [`00499f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499f70.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004997f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049975c.md#insn-004997f4) · [`00499838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049975c.md#insn-00499838) · [`00499848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049975c.md#insn-00499848)
- 新版 `00499834`（命令位置の公開資料なし） · `00499878`（命令位置の公開資料なし） · `00499888`（命令位置の公開資料なし）

~~~diff
- 004997f4 ["INT_ADD", "register:40f0:8", ["const:4997f4:8", "const:4:8"]]
- 004997f4 ["CALL", null, ["callee:00c57f40:8"]]
+ 00499834 ["INT_ADD", "register:40f0:8", ["const:499834:8", "const:4:8"]]
+ 00499834 ["CALL", null, ["callee:00c57f40:8"]]
- 004997f4 bytes d3f81e94
+ 00499834 bytes c3f91e94
- 00499838 ["INT_ADD", "register:40f0:8", ["const:499838:8", "const:4:8"]]
- 00499838 ["CALL", null, ["callee:00c57e90:8"]]
+ 00499878 ["INT_ADD", "register:40f0:8", ["const:499878:8", "const:4:8"]]
+ 00499878 ["CALL", null, ["callee:00c57e90:8"]]
- 00499838 bytes 96f81e94
+ 00499878 bytes 86f91e94
- 00499848 ["INT_ADD", "register:40f0:8", ["const:499848:8", "const:4:8"]]
- 00499848 ["CALL", null, ["callee:00499c5c:8"]]
+ 00499888 ["INT_ADD", "register:40f0:8", ["const:499888:8", "const:4:8"]]
+ 00499888 ["CALL", null, ["callee:00499c5c:8"]]
- 00499848 bytes f5000094
+ 00499888 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b721bd4fa91eb8071130927234a8946"></a>

### [`00499c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499c1c.md) → [`00499c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499c5c.md) FUN_00499c5c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049975c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049975c.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`0049979c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/0049979c.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00499c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499c1c.md#insn-00499c84) · [`00499cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499c1c.md#insn-00499cbc) · [`00499d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499c1c.md#insn-00499d6c)
- 新版 `00499cc4`（命令位置の公開資料なし） · `00499cfc`（命令位置の公開資料なし） · `00499dac`（命令位置の公開資料なし）

~~~diff
- 00499c84 ["INT_ADD", "register:40f0:8", ["const:499c84:8", "const:4:8"]]
- 00499c84 ["CALL", null, ["callee:00c57f40:8"]]
+ 00499cc4 ["INT_ADD", "register:40f0:8", ["const:499cc4:8", "const:4:8"]]
+ 00499cc4 ["CALL", null, ["callee:00c57f40:8"]]
- 00499c84 bytes aff71e94
+ 00499cc4 bytes 9ff81e94
- 00499cbc ["INT_ADD", "register:40f0:8", ["const:499cbc:8", "const:4:8"]]
- 00499cbc ["CALL", null, ["callee:00c57e90:8"]]
+ 00499cfc ["INT_ADD", "register:40f0:8", ["const:499cfc:8", "const:4:8"]]
+ 00499cfc ["CALL", null, ["callee:00c57e90:8"]]
- 00499cbc bytes 75f71e94
+ 00499cfc bytes 65f81e94
- 00499d6c ["INT_ADD", "register:40f0:8", ["const:499d6c:8", "const:4:8"]]
- 00499d6c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00499dac ["INT_ADD", "register:40f0:8", ["const:499dac:8", "const:4:8"]]
+ 00499dac ["CALL", null, ["callee:00c57eb0:8"]]
- 00499d6c bytes 51f71e94
+ 00499dac bytes 41f81e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a9d74601eecbfe6c12a73c4ac95384e"></a>

### [`00499da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499da4.md) → [`00499de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499de4.md) FUN_00499de4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049975c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049975c.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`0049979c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/0049979c.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00499e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499da4.md#insn-00499e14) · [`00499e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499da4.md#insn-00499e4c) · [`00499efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499da4.md#insn-00499efc)
- 新版 `00499e54`（命令位置の公開資料なし） · `00499e8c`（命令位置の公開資料なし） · `00499f3c`（命令位置の公開資料なし）

~~~diff
- 00499e14 ["INT_ADD", "register:40f0:8", ["const:499e14:8", "const:4:8"]]
- 00499e14 ["CALL", null, ["callee:00c57f40:8"]]
+ 00499e54 ["INT_ADD", "register:40f0:8", ["const:499e54:8", "const:4:8"]]
+ 00499e54 ["CALL", null, ["callee:00c57f40:8"]]
- 00499e14 bytes 4bf71e94
+ 00499e54 bytes 3bf81e94
- 00499e4c ["INT_ADD", "register:40f0:8", ["const:499e4c:8", "const:4:8"]]
- 00499e4c ["CALL", null, ["callee:00c57e90:8"]]
+ 00499e8c ["INT_ADD", "register:40f0:8", ["const:499e8c:8", "const:4:8"]]
+ 00499e8c ["CALL", null, ["callee:00c57e90:8"]]
- 00499e4c bytes 11f71e94
+ 00499e8c bytes 01f81e94
- 00499efc ["INT_ADD", "register:40f0:8", ["const:499efc:8", "const:4:8"]]
- 00499efc ["CALL", null, ["callee:00c57eb0:8"]]
+ 00499f3c ["INT_ADD", "register:40f0:8", ["const:499f3c:8", "const:4:8"]]
+ 00499f3c ["CALL", null, ["callee:00c57eb0:8"]]
- 00499efc bytes edf61e94
+ 00499f3c bytes ddf71e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-021601dacba0104b6e428a3fafc39cef"></a>

### [`00499f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499f30.md) → [`00499f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499f70.md) FUN_00499f70

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049975c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049975c.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`0049979c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/0049979c.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00499fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499f30.md#insn-00499fa0) · [`00499fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499f30.md#insn-00499fd8) · [`0049a088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499f30.md#insn-0049a088)
- 新版 `00499fe0`（命令位置の公開資料なし） · `0049a018`（命令位置の公開資料なし） · `0049a0c8`（命令位置の公開資料なし）

~~~diff
- 00499fa0 ["INT_ADD", "register:40f0:8", ["const:499fa0:8", "const:4:8"]]
- 00499fa0 ["CALL", null, ["callee:00c57f40:8"]]
+ 00499fe0 ["INT_ADD", "register:40f0:8", ["const:499fe0:8", "const:4:8"]]
+ 00499fe0 ["CALL", null, ["callee:00c57f40:8"]]
- 00499fa0 bytes e8f61e94
+ 00499fe0 bytes d8f71e94
- 00499fd8 ["INT_ADD", "register:40f0:8", ["const:499fd8:8", "const:4:8"]]
- 00499fd8 ["CALL", null, ["callee:00c57e90:8"]]
+ 0049a018 ["INT_ADD", "register:40f0:8", ["const:49a018:8", "const:4:8"]]
+ 0049a018 ["CALL", null, ["callee:00c57e90:8"]]
- 00499fd8 bytes aef61e94
+ 0049a018 bytes 9ef71e94
- 0049a088 ["INT_ADD", "register:40f0:8", ["const:49a088:8", "const:4:8"]]
- 0049a088 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0049a0c8 ["INT_ADD", "register:40f0:8", ["const:49a0c8:8", "const:4:8"]]
+ 0049a0c8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0049a088 bytes 8af61e94
+ 0049a0c8 bytes 7af71e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9d5922694070fecd8b4cc4e289c45c9"></a>

### [`0049a0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a0bc.md) → [`0049a0fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a0fc.md) FUN_0049a0fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00498190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498190.md) · 呼出先 4件 [`00499430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499430.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`004981d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004981d0.md) · 呼出先 4件 [`00499470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499470.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049a138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a0bc.md#insn-0049a138) · [`0049a160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a0bc.md#insn-0049a160) · [`0049a170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a0bc.md#insn-0049a170)
- 新版 `0049a178`（命令位置の公開資料なし） · `0049a1a0`（命令位置の公開資料なし） · `0049a1b0`（命令位置の公開資料なし）

~~~diff
- 0049a138 ["COPY", "register:0:8", ["register:4048:8"]]
- 0049a138 ["INT_ADD", "register:40f0:8", ["const:49a138:8", "const:4:8"]]
- 0049a138 ["CALLIND", null, ["register:0:8"]]
+ 0049a178 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0049a178 ["INT_ADD", "register:40f0:8", ["const:49a178:8", "const:4:8"]]
+ 0049a178 ["CALLIND", null, ["register:0:8"]]
- 0049a138 bytes 20013fd6
+ 0049a178 bytes 20013fd6
- 0049a160 ["COPY", "register:0:8", ["register:4040:8"]]
- 0049a160 ["INT_ADD", "register:40f0:8", ["const:49a160:8", "const:4:8"]]
- 0049a160 ["CALLIND", null, ["register:0:8"]]
+ 0049a1a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049a1a0 ["INT_ADD", "register:40f0:8", ["const:49a1a0:8", "const:4:8"]]
+ 0049a1a0 ["CALLIND", null, ["register:0:8"]]
- 0049a160 bytes 00013fd6
+ 0049a1a0 bytes 00013fd6
- 0049a170 ["INT_ADD", "register:40f0:8", ["const:49a170:8", "const:4:8"]]
- 0049a170 ["CALL", null, ["callee:00499470:8"]]
+ 0049a1b0 ["INT_ADD", "register:40f0:8", ["const:49a1b0:8", "const:4:8"]]
+ 0049a1b0 ["CALL", null, ["callee:00499470:8"]]
- 0049a170 bytes b0fcff97
+ 0049a1b0 bytes b0fcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f00d7cc4b64d1ec8c373ae1810816360"></a>

### [`0049a264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a264.md) → [`0049a2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a2a4.md) FUN_0049a2a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004985a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004985a0.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0049a724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a724.md) [`0049a8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a8ac.md) [`0049aa38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049aa38.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`004985e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004985e0.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0049a764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a764.md) [`0049a8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a8ec.md) [`0049aa78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049aa78.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049a2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a264.md#insn-0049a2fc) · [`0049a340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a264.md#insn-0049a340) · [`0049a350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a264.md#insn-0049a350)
- 新版 `0049a33c`（命令位置の公開資料なし） · `0049a380`（命令位置の公開資料なし） · `0049a390`（命令位置の公開資料なし）

~~~diff
- 0049a2fc ["INT_ADD", "register:40f0:8", ["const:49a2fc:8", "const:4:8"]]
- 0049a2fc ["CALL", null, ["callee:00c57f40:8"]]
+ 0049a33c ["INT_ADD", "register:40f0:8", ["const:49a33c:8", "const:4:8"]]
+ 0049a33c ["CALL", null, ["callee:00c57f40:8"]]
- 0049a2fc bytes 11f61e94
+ 0049a33c bytes 01f71e94
- 0049a340 ["INT_ADD", "register:40f0:8", ["const:49a340:8", "const:4:8"]]
- 0049a340 ["CALL", null, ["callee:00c57e90:8"]]
+ 0049a380 ["INT_ADD", "register:40f0:8", ["const:49a380:8", "const:4:8"]]
+ 0049a380 ["CALL", null, ["callee:00c57e90:8"]]
- 0049a340 bytes d4f51e94
+ 0049a380 bytes c4f61e94
- 0049a350 ["INT_ADD", "register:40f0:8", ["const:49a350:8", "const:4:8"]]
- 0049a350 ["CALL", null, ["callee:0049a764:8"]]
+ 0049a390 ["INT_ADD", "register:40f0:8", ["const:49a390:8", "const:4:8"]]
+ 0049a390 ["CALL", null, ["callee:0049a764:8"]]
- 0049a350 bytes f5000094
+ 0049a390 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05c66c6675ea65994d16aed4f025232b"></a>

### [`0049a724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a724.md) → [`0049a764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a764.md) FUN_0049a764

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049a264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a264.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`0049a2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a2a4.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049a78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a724.md#insn-0049a78c) · [`0049a7c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a724.md#insn-0049a7c4) · [`0049a874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a724.md#insn-0049a874)
- 新版 `0049a7cc`（命令位置の公開資料なし） · `0049a804`（命令位置の公開資料なし） · `0049a8b4`（命令位置の公開資料なし）

~~~diff
- 0049a78c ["INT_ADD", "register:40f0:8", ["const:49a78c:8", "const:4:8"]]
- 0049a78c ["CALL", null, ["callee:00c57f40:8"]]
+ 0049a7cc ["INT_ADD", "register:40f0:8", ["const:49a7cc:8", "const:4:8"]]
+ 0049a7cc ["CALL", null, ["callee:00c57f40:8"]]
- 0049a78c bytes edf41e94
+ 0049a7cc bytes ddf51e94
- 0049a7c4 ["INT_ADD", "register:40f0:8", ["const:49a7c4:8", "const:4:8"]]
- 0049a7c4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0049a804 ["INT_ADD", "register:40f0:8", ["const:49a804:8", "const:4:8"]]
+ 0049a804 ["CALL", null, ["callee:00c57e90:8"]]
- 0049a7c4 bytes b3f41e94
+ 0049a804 bytes a3f51e94
- 0049a874 ["INT_ADD", "register:40f0:8", ["const:49a874:8", "const:4:8"]]
- 0049a874 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0049a8b4 ["INT_ADD", "register:40f0:8", ["const:49a8b4:8", "const:4:8"]]
+ 0049a8b4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0049a874 bytes 8ff41e94
+ 0049a8b4 bytes 7ff51e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59907067b3b3e64bd40699f655022651"></a>

### [`0049a8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a8ac.md) → [`0049a8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a8ec.md) FUN_0049a8ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049a264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a264.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`0049a2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a2a4.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049a91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a8ac.md#insn-0049a91c) · [`0049a954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a8ac.md#insn-0049a954) · [`0049aa04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a8ac.md#insn-0049aa04)
- 新版 `0049a95c`（命令位置の公開資料なし） · `0049a994`（命令位置の公開資料なし） · `0049aa44`（命令位置の公開資料なし）

~~~diff
- 0049a91c ["INT_ADD", "register:40f0:8", ["const:49a91c:8", "const:4:8"]]
- 0049a91c ["CALL", null, ["callee:00c57f40:8"]]
+ 0049a95c ["INT_ADD", "register:40f0:8", ["const:49a95c:8", "const:4:8"]]
+ 0049a95c ["CALL", null, ["callee:00c57f40:8"]]
- 0049a91c bytes 89f41e94
+ 0049a95c bytes 79f51e94
- 0049a954 ["INT_ADD", "register:40f0:8", ["const:49a954:8", "const:4:8"]]
- 0049a954 ["CALL", null, ["callee:00c57e90:8"]]
+ 0049a994 ["INT_ADD", "register:40f0:8", ["const:49a994:8", "const:4:8"]]
+ 0049a994 ["CALL", null, ["callee:00c57e90:8"]]
- 0049a954 bytes 4ff41e94
+ 0049a994 bytes 3ff51e94
- 0049aa04 ["INT_ADD", "register:40f0:8", ["const:49aa04:8", "const:4:8"]]
- 0049aa04 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0049aa44 ["INT_ADD", "register:40f0:8", ["const:49aa44:8", "const:4:8"]]
+ 0049aa44 ["CALL", null, ["callee:00c57eb0:8"]]
- 0049aa04 bytes 2bf41e94
+ 0049aa44 bytes 1bf51e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bef672109ab8f08486bc5ba6e6a3f22d"></a>

### [`0049aa38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049aa38.md) → [`0049aa78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049aa78.md) FUN_0049aa78

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049a264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049a264.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`0049a2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a2a4.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049aaa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049aa38.md#insn-0049aaa8) · [`0049aae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049aa38.md#insn-0049aae0) · [`0049ab90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049aa38.md#insn-0049ab90)
- 新版 `0049aae8`（命令位置の公開資料なし） · `0049ab20`（命令位置の公開資料なし） · `0049abd0`（命令位置の公開資料なし）

~~~diff
- 0049aaa8 ["INT_ADD", "register:40f0:8", ["const:49aaa8:8", "const:4:8"]]
- 0049aaa8 ["CALL", null, ["callee:00c57f40:8"]]
+ 0049aae8 ["INT_ADD", "register:40f0:8", ["const:49aae8:8", "const:4:8"]]
+ 0049aae8 ["CALL", null, ["callee:00c57f40:8"]]
- 0049aaa8 bytes 26f41e94
+ 0049aae8 bytes 16f51e94
- 0049aae0 ["INT_ADD", "register:40f0:8", ["const:49aae0:8", "const:4:8"]]
- 0049aae0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0049ab20 ["INT_ADD", "register:40f0:8", ["const:49ab20:8", "const:4:8"]]
+ 0049ab20 ["CALL", null, ["callee:00c57e90:8"]]
- 0049aae0 bytes ecf31e94
+ 0049ab20 bytes dcf41e94
- 0049ab90 ["INT_ADD", "register:40f0:8", ["const:49ab90:8", "const:4:8"]]
- 0049ab90 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0049abd0 ["INT_ADD", "register:40f0:8", ["const:49abd0:8", "const:4:8"]]
+ 0049abd0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0049ab90 bytes c8f31e94
+ 0049abd0 bytes b8f41e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4a805f5314e09bb414f02c4c7eeb6a1"></a>

### [`0049acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049acb4.md) → [`0049acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049acf4.md) FUN_0049acf4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004986a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004986a4.md) · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`004986e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004986e4.md) · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049acd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049acb4.md#insn-0049acd0)
- 新版 `0049ad10`（命令位置の公開資料なし）

~~~diff
- 0049acd0 ["INT_ADD", "register:40f0:8", ["const:49acd0:8", "const:4:8"]]
- 0049acd0 ["CALL", null, ["callee:00c57e80:8"]]
+ 0049ad10 ["INT_ADD", "register:40f0:8", ["const:49ad10:8", "const:4:8"]]
+ 0049ad10 ["CALL", null, ["callee:00c57e80:8"]]
- 0049acd0 bytes 6cf31e94
+ 0049ad10 bytes 5cf41e94
~~~


<a id="compare-ac82f7edb16e097b26ffa57b4b13e062"></a>

### [`0049ace4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ace4.md) → [`0049ad24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049ad24.md) FUN_0049ad24

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00489468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489468.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c580f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580f0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004894a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004894a8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c584f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049ad10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ace4.md#insn-0049ad10) · [`0049ad2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ace4.md#insn-0049ad2c) · [`0049ad38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ace4.md#insn-0049ad38)
- 新版 `0049ad50`（命令位置の公開資料なし） · `0049ad6c`（命令位置の公開資料なし） · `0049ad78`（命令位置の公開資料なし）

~~~diff
- 0049ad10 ["INT_ADD", "register:40f0:8", ["const:49ad10:8", "const:4:8"]]
- 0049ad10 ["CALL", null, ["callee:00c584f0:8"]]
+ 0049ad50 ["INT_ADD", "register:40f0:8", ["const:49ad50:8", "const:4:8"]]
+ 0049ad50 ["CALL", null, ["callee:00c584f0:8"]]
- 0049ad10 bytes f8f41e94
+ 0049ad50 bytes e8f51e94
- 0049ad2c ["INT_ADD", "register:40f0:8", ["const:49ad2c:8", "const:4:8"]]
- 0049ad2c ["CALL", null, ["callee:004894a8:8"]]
+ 0049ad6c ["INT_ADD", "register:40f0:8", ["const:49ad6c:8", "const:4:8"]]
+ 0049ad6c ["CALL", null, ["callee:004894a8:8"]]
- 0049ad2c bytes cfb9ff97
+ 0049ad6c bytes cfb9ff97
- 0049ad38 ["INT_ADD", "register:40f0:8", ["const:49ad38:8", "const:4:8"]]
- 0049ad38 ["CALL", null, ["callee:00c53d00:8"]]
+ 0049ad78 ["INT_ADD", "register:40f0:8", ["const:49ad78:8", "const:4:8"]]
+ 0049ad78 ["CALL", null, ["callee:00c53d00:8"]]
- 0049ad38 bytes eae21e94
+ 0049ad78 bytes e2e31e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d078b55f036f95cfe6f6cd4b18da27ef"></a>

### [`0049b394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b394.md) → [`0049b3d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b3d4.md) FUN_0049b3d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049b64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b64c.md) · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 1件 [`0049b68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b68c.md) · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049b3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b394.md#insn-0049b3d0) · [`0049b3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b394.md#insn-0049b3ec)
- 新版 `0049b410`（命令位置の公開資料なし） · `0049b42c`（命令位置の公開資料なし）

~~~diff
- 0049b3d0 ["INT_ADD", "register:40f0:8", ["const:49b3d0:8", "const:4:8"]]
- 0049b3d0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0049b410 ["INT_ADD", "register:40f0:8", ["const:49b410:8", "const:4:8"]]
+ 0049b410 ["CALL", null, ["callee:00c57e90:8"]]
- 0049b3d0 bytes b0f11e94
+ 0049b410 bytes a0f21e94
- 0049b3ec ["INT_ADD", "register:40f0:8", ["const:49b3ec:8", "const:4:8"]]
- 0049b3ec ["CALL", null, ["callee:00c58090:8"]]
+ 0049b42c ["INT_ADD", "register:40f0:8", ["const:49b42c:8", "const:4:8"]]
+ 0049b42c ["CALL", null, ["callee:00c58090:8"]]
- 0049b3ec bytes 29f21e94
+ 0049b42c bytes 19f31e94
~~~


<a id="compare-ef007b97d2331ac728a66ab2f7b72907"></a>

### [`0049b56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b56c.md) → [`0049b5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b5ac.md) FUN_0049b5ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a992ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a99/00a992ac.md) · 呼出先 4件 [`0049b64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b64c.md) [`0049ff10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049ff10.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00a994a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a99/00a994a4.md) · 呼出先 4件 [`0049b68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b68c.md) [`0049ff50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049ff50.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049b598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b56c.md#insn-0049b598) · [`0049b5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b56c.md#insn-0049b5b8) · [`0049b5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b56c.md#insn-0049b5ec)
- 新版 `0049b5d8`（命令位置の公開資料なし） · `0049b5f8`（命令位置の公開資料なし） · `0049b62c`（命令位置の公開資料なし）

~~~diff
- 0049b598 ["INT_ADD", "register:40f0:8", ["const:49b598:8", "const:4:8"]]
- 0049b598 ["CALL", null, ["callee:0049ff50:8"]]
+ 0049b5d8 ["INT_ADD", "register:40f0:8", ["const:49b5d8:8", "const:4:8"]]
+ 0049b5d8 ["CALL", null, ["callee:0049ff50:8"]]
- 0049b598 bytes 5e120094
+ 0049b5d8 bytes 5e120094
- 0049b5b8 ["INT_ADD", "register:40f0:8", ["const:49b5b8:8", "const:4:8"]]
- 0049b5b8 ["CALL", null, ["callee:0049b68c:8"]]
+ 0049b5f8 ["INT_ADD", "register:40f0:8", ["const:49b5f8:8", "const:4:8"]]
+ 0049b5f8 ["CALL", null, ["callee:0049b68c:8"]]
- 0049b5b8 bytes 25000094
+ 0049b5f8 bytes 25000094
- 0049b5ec ["INT_ADD", "register:40f0:8", ["const:49b5ec:8", "const:4:8"]]
- 0049b5ec ["CALL", null, ["callee:00c57eb0:8"]]
+ 0049b62c ["INT_ADD", "register:40f0:8", ["const:49b62c:8", "const:4:8"]]
+ 0049b62c ["CALL", null, ["callee:00c57eb0:8"]]
- 0049b5ec bytes 31f11e94
+ 0049b62c bytes 21f21e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b642b7a70d58247f39765f1a1d300f5"></a>

### [`0049bba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bba8.md) → [`0049bbe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049bbe8.md) FUN_0049bbe8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049bbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bba8.md#insn-0049bbec)
- 新版 `0049bc2c`（命令位置の公開資料なし）

~~~diff
- 0049bbec ["INT_ADD", "register:40f0:8", ["const:49bbec:8", "const:4:8"]]
- 0049bbec ["CALL", null, ["callee:00c57eb0:8"]]
+ 0049bc2c ["INT_ADD", "register:40f0:8", ["const:49bc2c:8", "const:4:8"]]
+ 0049bc2c ["CALL", null, ["callee:00c57eb0:8"]]
- 0049bbec bytes b1ef1e94
+ 0049bc2c bytes a1f01e94
~~~


<a id="compare-8985b8aa7e05865e10f3efb89e35a71c"></a>

### [`0049bfe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bfe4.md) → [`0049c024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c024.md) FUN_0049c024

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049bc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md) · 呼出先 8件 [`0049d158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d158.md) [`0049d234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d234.md) [`0049d3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d3b8.md) [`0049d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d484.md) [`0049d878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d878.md)
- 新版 呼出元 1件 [`0049bc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049bc5c.md) · 呼出先 8件 [`0049d198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d198.md) [`0049d274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d274.md) [`0049d3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d3f8.md) [`0049d4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d4c4.md) [`0049d8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d8b8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049c038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bfe4.md#insn-0049c038) · [`0049c04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bfe4.md#insn-0049c04c) · [`0049c0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bfe4.md#insn-0049c0d8)
- 新版 `0049c078`（命令位置の公開資料なし） · `0049c08c`（命令位置の公開資料なし） · `0049c118`（命令位置の公開資料なし）

~~~diff
- 0049c038 ["INT_ADD", "register:40f0:8", ["const:49c038:8", "const:4:8"]]
- 0049c038 ["CALL", null, ["callee:0049d198:8"]]
+ 0049c078 ["INT_ADD", "register:40f0:8", ["const:49c078:8", "const:4:8"]]
+ 0049c078 ["CALL", null, ["callee:0049d198:8"]]
- 0049c038 bytes 48040094
+ 0049c078 bytes 48040094
- 0049c04c ["INT_ADD", "register:40f0:8", ["const:49c04c:8", "const:4:8"]]
- 0049c04c ["CALL", null, ["callee:0049d198:8"]]
+ 0049c08c ["INT_ADD", "register:40f0:8", ["const:49c08c:8", "const:4:8"]]
+ 0049c08c ["CALL", null, ["callee:0049d198:8"]]
- 0049c04c bytes 43040094
+ 0049c08c bytes 43040094
- 0049c0d8 ["INT_ADD", "register:40f0:8", ["const:49c0d8:8", "const:4:8"]]
- 0049c0d8 ["CALL", null, ["callee:0049d198:8"]]
+ 0049c118 ["INT_ADD", "register:40f0:8", ["const:49c118:8", "const:4:8"]]
+ 0049c118 ["CALL", null, ["callee:0049d198:8"]]
- 0049c0d8 bytes 20040094
+ 0049c118 bytes 20040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24df8579b0b043373576d0ae2df32dae"></a>

### [`0049d048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d048.md) → [`0049d088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d088.md) FUN_0049d088

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049bc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0049bc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049bc5c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049d088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d048.md#insn-0049d088)
- 新版 `0049d0c8`（命令位置の公開資料なし）

~~~diff
- 0049d088 ["INT_ADD", "register:40f0:8", ["const:49d088:8", "const:4:8"]]
- 0049d088 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0049d0c8 ["INT_ADD", "register:40f0:8", ["const:49d0c8:8", "const:4:8"]]
+ 0049d0c8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0049d088 bytes 8aea1e94
+ 0049d0c8 bytes 7aeb1e94
~~~


<a id="compare-1848f71679abfea4e23bc8833ecae023"></a>

### [`0049d0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d0c0.md) → [`0049d100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d100.md) FUN_0049d100

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a992ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a99/00a992ac.md) · 呼出先 2件 [`0049f3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3c4.md) [`0049f3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3d8.md)
- 新版 呼出元 1件 [`00a994a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a99/00a994a4.md) · 呼出先 2件 [`0049f404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f404.md) [`0049f418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f418.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049d150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d0c0.md#insn-0049d150) · [`0049d154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d0c0.md#insn-0049d154)
- 新版 `0049d190`（命令位置の公開資料なし） · `0049d194`（命令位置の公開資料なし）

~~~diff
- 0049d150 ["INT_ADD", "register:40f0:8", ["const:49d150:8", "const:4:8"]]
- 0049d150 ["CALL", null, ["callee:0049f404:8"]]
+ 0049d190 ["INT_ADD", "register:40f0:8", ["const:49d190:8", "const:4:8"]]
+ 0049d190 ["CALL", null, ["callee:0049f404:8"]]
- 0049d150 bytes 9d080094
+ 0049d190 bytes 9d080094
- 0049d154 ["INT_ADD", "register:40f0:8", ["const:49d154:8", "const:4:8"]]
- 0049d154 ["CALL", null, ["callee:0049f418:8"]]
+ 0049d194 ["INT_ADD", "register:40f0:8", ["const:49d194:8", "const:4:8"]]
+ 0049d194 ["CALL", null, ["callee:0049f418:8"]]
- 0049d154 bytes a1080094
+ 0049d194 bytes a1080094
~~~


<a id="compare-1bdb4b3991642908b33f230a9de27d17"></a>

### [`0049d158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d158.md) → [`0049d198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d198.md) FUN_0049d198

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0049bfe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bfe4.md) [`0049d3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d3b8.md) [`0049d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d484.md) [`0049d878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d878.md) · 呼出先 2件 [`0049f3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3c4.md) [`0049f3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3d8.md)
- 新版 呼出元 4件 [`0049c024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c024.md) [`0049d3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d3f8.md) [`0049d4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d4c4.md) [`0049d8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d8b8.md) · 呼出先 2件 [`0049f404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f404.md) [`0049f418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f418.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049d220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d158.md#insn-0049d220) · [`0049d228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d158.md#insn-0049d228) · [`0049d22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d158.md#insn-0049d22c)
- 新版 `0049d260`（命令位置の公開資料なし） · `0049d268`（命令位置の公開資料なし） · `0049d26c`（命令位置の公開資料なし）

~~~diff
- 0049d220 ["INT_ADD", "register:40f0:8", ["const:49d220:8", "const:4:8"]]
- 0049d220 ["CALL", null, ["callee:0049f404:8"]]
+ 0049d260 ["INT_ADD", "register:40f0:8", ["const:49d260:8", "const:4:8"]]
+ 0049d260 ["CALL", null, ["callee:0049f404:8"]]
- 0049d220 bytes 69080094
+ 0049d260 bytes 69080094
- 0049d228 ["INT_ADD", "register:40f0:8", ["const:49d228:8", "const:4:8"]]
- 0049d228 ["CALL", null, ["callee:0049f418:8"]]
+ 0049d268 ["INT_ADD", "register:40f0:8", ["const:49d268:8", "const:4:8"]]
+ 0049d268 ["CALL", null, ["callee:0049f418:8"]]
- 0049d228 bytes 6c080094
+ 0049d268 bytes 6c080094
- 0049d22c ["INT_ADD", "register:40f0:8", ["const:49d22c:8", "const:4:8"]]
- 0049d22c ["CALL", null, ["callee:0049f404:8"]]
+ 0049d26c ["INT_ADD", "register:40f0:8", ["const:49d26c:8", "const:4:8"]]
+ 0049d26c ["CALL", null, ["callee:0049f404:8"]]
- 0049d22c bytes 66080094
+ 0049d26c bytes 66080094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a1007f29c04012c51b70a1693675aee"></a>

### [`0049d3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d3b8.md) → [`0049d3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d3f8.md) FUN_0049d3f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049bfe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bfe4.md) · 呼出先 1件 [`0049d158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d158.md)
- 新版 呼出元 1件 [`0049c024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c024.md) · 呼出先 1件 [`0049d198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d198.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049d400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d3b8.md#insn-0049d400) · [`0049d420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d3b8.md#insn-0049d420) · [`0049d434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d3b8.md#insn-0049d434)
- 新版 `0049d440`（命令位置の公開資料なし） · `0049d460`（命令位置の公開資料なし） · `0049d474`（命令位置の公開資料なし）

~~~diff
- 0049d400 ["INT_ADD", "register:40f0:8", ["const:49d400:8", "const:4:8"]]
- 0049d400 ["CALL", null, ["callee:0049d198:8"]]
+ 0049d440 ["INT_ADD", "register:40f0:8", ["const:49d440:8", "const:4:8"]]
+ 0049d440 ["CALL", null, ["callee:0049d198:8"]]
- 0049d400 bytes 56ffff97
+ 0049d440 bytes 56ffff97
- 0049d420 ["INT_ADD", "register:40f0:8", ["const:49d420:8", "const:4:8"]]
- 0049d420 ["CALL", null, ["callee:0049d198:8"]]
+ 0049d460 ["INT_ADD", "register:40f0:8", ["const:49d460:8", "const:4:8"]]
+ 0049d460 ["CALL", null, ["callee:0049d198:8"]]
- 0049d420 bytes 4effff97
+ 0049d460 bytes 4effff97
- 0049d434 ["INT_ADD", "register:40f0:8", ["const:49d434:8", "const:4:8"]]
- 0049d434 ["CALL", null, ["callee:0049d198:8"]]
+ 0049d474 ["INT_ADD", "register:40f0:8", ["const:49d474:8", "const:4:8"]]
+ 0049d474 ["CALL", null, ["callee:0049d198:8"]]
- 0049d434 bytes 49ffff97
+ 0049d474 bytes 49ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e76cf67cd9b9781ab5dee63cad0d0cb"></a>

### [`0049d9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d9e0.md) → [`0049da20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049da20.md) FUN_0049da20

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049c338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md) · 呼出先 8件 [`0049ea6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ea6c.md) [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0049f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f8a0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0049c378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c378.md) · 呼出先 8件 [`0049eaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049eaac.md) [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0049f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f8e0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049da28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d9e0.md#insn-0049da28) · [`0049da44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d9e0.md#insn-0049da44) · [`0049da9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d9e0.md#insn-0049da9c)
- 新版 `0049da68`（命令位置の公開資料なし） · `0049da84`（命令位置の公開資料なし） · `0049dadc`（命令位置の公開資料なし）

~~~diff
- 0049da28 ["INT_ADD", "register:40f0:8", ["const:49da28:8", "const:4:8"]]
- 0049da28 ["CALL", null, ["callee:00c57e90:8"]]
+ 0049da68 ["INT_ADD", "register:40f0:8", ["const:49da68:8", "const:4:8"]]
+ 0049da68 ["CALL", null, ["callee:00c57e90:8"]]
- 0049da28 bytes 1ae81e94
+ 0049da68 bytes 0ae91e94
- 0049da44 ["INT_ADD", "register:40f0:8", ["const:49da44:8", "const:4:8"]]
- 0049da44 ["CALL", null, ["callee:00c58090:8"]]
+ 0049da84 ["INT_ADD", "register:40f0:8", ["const:49da84:8", "const:4:8"]]
+ 0049da84 ["CALL", null, ["callee:00c58090:8"]]
- 0049da44 bytes 93e81e94
+ 0049da84 bytes 83e91e94
- 0049da9c ["INT_ADD", "register:40f0:8", ["const:49da9c:8", "const:4:8"]]
- 0049da9c ["CALL", null, ["callee:00c57f40:8"]]
+ 0049dadc ["INT_ADD", "register:40f0:8", ["const:49dadc:8", "const:4:8"]]
+ 0049dadc ["CALL", null, ["callee:00c57f40:8"]]
- 0049da9c bytes 29e81e94
+ 0049dadc bytes 19e91e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d386797b6d01ce0e1442d224202463b6"></a>

### [`0049dc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049dc18.md) → [`0049dc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049dc58.md) FUN_0049dc58

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049dc64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049dc18.md#insn-0049dc64)
- 新版 `0049dca4`（命令位置の公開資料なし）

~~~diff
- 0049dc64 ["INT_ADD", "register:40f0:8", ["const:49dc64:8", "const:4:8"]]
- 0049dc64 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0049dca4 ["INT_ADD", "register:40f0:8", ["const:49dca4:8", "const:4:8"]]
+ 0049dca4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0049dc64 bytes 93e71e94
+ 0049dca4 bytes 83e81e94
~~~


<a id="compare-58b851148c0962fe692a640c84aa042f"></a>

### [`0049df00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049df00.md) → [`0049df40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049df40.md) FUN_0049df40

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049cde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049cde0.md) · 呼出先 2件 [`0049f3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3c4.md) [`0049f3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3d8.md)
- 新版 呼出元 1件 [`0049ce20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049ce20.md) · 呼出先 2件 [`0049f404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f404.md) [`0049f418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f418.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049e228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049df00.md#insn-0049e228) · [`0049e454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049df00.md#insn-0049e454) · [`0049e45c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049df00.md#insn-0049e45c)
- 新版 `0049e268`（命令位置の公開資料なし） · `0049e494`（命令位置の公開資料なし） · `0049e49c`（命令位置の公開資料なし）

~~~diff
- 0049e228 ["INT_ADD", "register:40f0:8", ["const:49e228:8", "const:4:8"]]
- 0049e228 ["CALL", null, ["callee:0049f418:8"]]
+ 0049e268 ["INT_ADD", "register:40f0:8", ["const:49e268:8", "const:4:8"]]
+ 0049e268 ["CALL", null, ["callee:0049f418:8"]]
- 0049e228 bytes 6c040094
+ 0049e268 bytes 6c040094
- 0049e454 ["INT_ADD", "register:40f0:8", ["const:49e454:8", "const:4:8"]]
- 0049e454 ["CALL", null, ["callee:0049f418:8"]]
+ 0049e494 ["INT_ADD", "register:40f0:8", ["const:49e494:8", "const:4:8"]]
+ 0049e494 ["CALL", null, ["callee:0049f418:8"]]
- 0049e454 bytes e1030094
+ 0049e494 bytes e1030094
- 0049e45c ["INT_ADD", "register:40f0:8", ["const:49e45c:8", "const:4:8"]]
- 0049e45c ["CALL", null, ["callee:0049f404:8"]]
+ 0049e49c ["INT_ADD", "register:40f0:8", ["const:49e49c:8", "const:4:8"]]
+ 0049e49c ["CALL", null, ["callee:0049f404:8"]]
- 0049e45c bytes da030094
+ 0049e49c bytes da030094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2c6046adbb98cc264c6563e07d6a99b"></a>

### [`0049e484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e484.md) → [`0049e4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e4c4.md) FUN_0049e4c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0049d234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d234.md) [`0073c8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073c/0073c8f8.md) [`008c5c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c5/008c5c08.md) [`008c79a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c7/008c79a4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 4件 [`0049d274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d274.md) [`0073c938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073c/0073c938.md) [`008c5da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c5/008c5da4.md) [`008c7b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c7/008c7b40.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049e528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e484.md#insn-0049e528) · [`0049e59c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e484.md#insn-0049e59c) · [`0049e5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e484.md#insn-0049e5d8)
- 新版 `0049e568`（命令位置の公開資料なし） · `0049e5dc`（命令位置の公開資料なし） · `0049e618`（命令位置の公開資料なし）

~~~diff
- 0049e528 ["INT_ADD", "register:40f0:8", ["const:49e528:8", "const:4:8"]]
- 0049e528 ["CALL", null, ["callee:00c57e90:8"]]
+ 0049e568 ["INT_ADD", "register:40f0:8", ["const:49e568:8", "const:4:8"]]
+ 0049e568 ["CALL", null, ["callee:00c57e90:8"]]
- 0049e528 bytes 5ae51e94
+ 0049e568 bytes 4ae61e94
- 0049e59c ["INT_ADD", "register:40f0:8", ["const:49e59c:8", "const:4:8"]]
- 0049e59c ["CALL", null, ["callee:00c57f40:8"]]
+ 0049e5dc ["INT_ADD", "register:40f0:8", ["const:49e5dc:8", "const:4:8"]]
+ 0049e5dc ["CALL", null, ["callee:00c57f40:8"]]
- 0049e59c bytes 69e51e94
+ 0049e5dc bytes 59e61e94
- 0049e5d8 ["INT_ADD", "register:40f0:8", ["const:49e5d8:8", "const:4:8"]]
- 0049e5d8 ["CALL", null, ["callee:00c57e90:8"]]
+ 0049e618 ["INT_ADD", "register:40f0:8", ["const:49e618:8", "const:4:8"]]
+ 0049e618 ["CALL", null, ["callee:00c57e90:8"]]
- 0049e5d8 bytes 2ee51e94
+ 0049e618 bytes 1ee61e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19201e14a2c888c28180b72c8a156257"></a>

### [`0049e694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e694.md) → [`0049e6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e6d4.md) FUN_0049e6d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0049d234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d234.md) [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0049f8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f8b4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0049d274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d274.md) [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0049f8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f8f4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049e74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e694.md#insn-0049e74c) · [`0049e78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e694.md#insn-0049e78c) · [`0049e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e694.md#insn-0049e7a0)
- 新版 `0049e78c`（命令位置の公開資料なし） · `0049e7cc`（命令位置の公開資料なし） · `0049e7e0`（命令位置の公開資料なし）

~~~diff
- 0049e74c ["INT_ADD", "register:40f0:8", ["const:49e74c:8", "const:4:8"]]
- 0049e74c ["CALL", null, ["callee:00c57e90:8"]]
+ 0049e78c ["INT_ADD", "register:40f0:8", ["const:49e78c:8", "const:4:8"]]
+ 0049e78c ["CALL", null, ["callee:00c57e90:8"]]
- 0049e74c bytes d1e41e94
+ 0049e78c bytes c1e51e94
- 0049e78c ["INT_ADD", "register:40f0:8", ["const:49e78c:8", "const:4:8"]]
- 0049e78c ["CALL", null, ["callee:0049f8f4:8"]]
+ 0049e7cc ["INT_ADD", "register:40f0:8", ["const:49e7cc:8", "const:4:8"]]
+ 0049e7cc ["CALL", null, ["callee:0049f8f4:8"]]
- 0049e78c bytes 4a040094
+ 0049e7cc bytes 4a040094
- 0049e7a0 ["INT_ADD", "register:40f0:8", ["const:49e7a0:8", "const:4:8"]]
- 0049e7a0 ["CALL", null, ["callee:00c58000:8"]]
+ 0049e7e0 ["INT_ADD", "register:40f0:8", ["const:49e7e0:8", "const:4:8"]]
+ 0049e7e0 ["CALL", null, ["callee:00c58000:8"]]
- 0049e7a0 bytes 18e51e94
+ 0049e7e0 bytes 08e61e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9a28dde8f2ac4dbc59c888cf3102740"></a>

### [`0049eb60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049eb60.md) → [`0049eba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049eba0.md) FUN_0049eba0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0049bc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md) [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 2件 [`0047d678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d678.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`0049bc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049bc5c.md) [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 2件 [`0047d6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d6b8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049eb9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049eb60.md#insn-0049eb9c) · [`0049ec60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049eb60.md#insn-0049ec60)
- 新版 `0049ebdc`（命令位置の公開資料なし） · `0049eca0`（命令位置の公開資料なし）

~~~diff
- 0049eb9c ["INT_ADD", "register:40f0:8", ["const:49eb9c:8", "const:4:8"]]
- 0049eb9c ["CALL", null, ["callee:00c57e90:8"]]
+ 0049ebdc ["INT_ADD", "register:40f0:8", ["const:49ebdc:8", "const:4:8"]]
+ 0049ebdc ["CALL", null, ["callee:00c57e90:8"]]
- 0049eb9c bytes bde31e94
+ 0049ebdc bytes ade41e94
- 0049ec60 ["INT_ADD", "register:40f0:8", ["const:49ec60:8", "const:4:8"]]
- 0049ec60 ["CALL", null, ["callee:0047d6b8:8"]]
+ 0049eca0 ["INT_ADD", "register:40f0:8", ["const:49eca0:8", "const:4:8"]]
+ 0049eca0 ["CALL", null, ["callee:0047d6b8:8"]]
- 0049ec60 bytes 867aff97
+ 0049eca0 bytes 867aff97
~~~


<a id="compare-f4281e3bf5afc44c4f8759ab05e30201"></a>

### [`0049ec64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ec64.md) → [`0049eca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049eca4.md) FUN_0049eca4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049b64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b64c.md) · 呼出先 7件 [`0047d574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d574.md) [`0047d678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d678.md) [`0049f13c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f13c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0049b68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b68c.md) · 呼出先 7件 [`0047d5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d5b4.md) [`0047d6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d6b8.md) [`0049f17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f17c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049edcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ec64.md#insn-0049edcc) · [`0049ee24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ec64.md#insn-0049ee24) · [`0049ee3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ec64.md#insn-0049ee3c)
- 新版 `0049ee0c`（命令位置の公開資料なし） · `0049ee64`（命令位置の公開資料なし） · `0049ee7c`（命令位置の公開資料なし）

~~~diff
- 0049edcc ["INT_ADD", "register:40f0:8", ["const:49edcc:8", "const:4:8"]]
- 0049edcc ["CALL", null, ["callee:00c57f40:8"]]
+ 0049ee0c ["INT_ADD", "register:40f0:8", ["const:49ee0c:8", "const:4:8"]]
+ 0049ee0c ["CALL", null, ["callee:00c57f40:8"]]
- 0049edcc bytes 5de31e94
+ 0049ee0c bytes 4de41e94
- 0049ee24 ["INT_ADD", "register:40f0:8", ["const:49ee24:8", "const:4:8"]]
- 0049ee24 ["CALL", null, ["callee:0049f17c:8"]]
+ 0049ee64 ["INT_ADD", "register:40f0:8", ["const:49ee64:8", "const:4:8"]]
+ 0049ee64 ["CALL", null, ["callee:0049f17c:8"]]
- 0049ee24 bytes c6000094
+ 0049ee64 bytes c6000094
- 0049ee3c ["INT_ADD", "register:40f0:8", ["const:49ee3c:8", "const:4:8"]]
- 0049ee3c ["CALL", null, ["callee:0047d5b4:8"]]
+ 0049ee7c ["INT_ADD", "register:40f0:8", ["const:49ee7c:8", "const:4:8"]]
+ 0049ee7c ["CALL", null, ["callee:0047d5b4:8"]]
- 0049ee3c bytes ce79ff97
+ 0049ee7c bytes ce79ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5447ab1f7a0cf35c46aaa93f5d51e1d"></a>

### [`0049f330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f330.md) → [`0049f370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f370.md) FUN_0049f370

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049bc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0049bc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049bc5c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049f38c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f330.md#insn-0049f38c)
- 新版 `0049f3cc`（命令位置の公開資料なし）

~~~diff
- 0049f38c ["INT_ADD", "register:40f0:8", ["const:49f38c:8", "const:4:8"]]
- 0049f38c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0049f3cc ["INT_ADD", "register:40f0:8", ["const:49f3cc:8", "const:4:8"]]
+ 0049f3cc ["CALL", null, ["callee:00c57eb0:8"]]
- 0049f38c bytes c9e11e94
+ 0049f3cc bytes b9e21e94
~~~


<a id="compare-b935c4d7cfe030dcd883e3fa93542f76"></a>

### [`0049f400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f400.md) → [`0049f440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f440.md) FUN_0049f440

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049c338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md) · 呼出先 5件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`0049c378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c378.md) · 呼出先 5件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049f480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f400.md#insn-0049f480) · [`0049f4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f400.md#insn-0049f4b4) · [`0049f5c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f400.md#insn-0049f5c4)
- 新版 `0049f4c0`（命令位置の公開資料なし） · `0049f4f4`（命令位置の公開資料なし） · `0049f604`（命令位置の公開資料なし）

~~~diff
- 0049f480 ["INT_ADD", "register:40f0:8", ["const:49f480:8", "const:4:8"]]
- 0049f480 ["CALL", null, ["callee:00c57e90:8"]]
+ 0049f4c0 ["INT_ADD", "register:40f0:8", ["const:49f4c0:8", "const:4:8"]]
+ 0049f4c0 ["CALL", null, ["callee:00c57e90:8"]]
- 0049f480 bytes 84e11e94
+ 0049f4c0 bytes 74e21e94
- 0049f4b4 ["INT_ADD", "register:40f0:8", ["const:49f4b4:8", "const:4:8"]]
- 0049f4b4 ["CALL", null, ["callee:00c57f40:8"]]
+ 0049f4f4 ["INT_ADD", "register:40f0:8", ["const:49f4f4:8", "const:4:8"]]
+ 0049f4f4 ["CALL", null, ["callee:00c57f40:8"]]
- 0049f4b4 bytes a3e11e94
+ 0049f4f4 bytes 93e21e94
- 0049f5c4 ["INT_ADD", "register:40f0:8", ["const:49f5c4:8", "const:4:8"]]
- 0049f5c4 ["CALL", null, ["callee:00c57f40:8"]]
+ 0049f604 ["INT_ADD", "register:40f0:8", ["const:49f604:8", "const:4:8"]]
+ 0049f604 ["CALL", null, ["callee:00c57f40:8"]]
- 0049f5c4 bytes 5fe11e94
+ 0049f604 bytes 4fe21e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a4185b899a03c7818a2001413459272"></a>

### [`0049f6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f6ec.md) → [`0049f72c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f72c.md) FUN_0049f72c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049c338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0049f878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f878.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0049c378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c378.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0049f8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f8b8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049f778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f6ec.md#insn-0049f778) · [`0049f830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f6ec.md#insn-0049f830) · [`0049f84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f6ec.md#insn-0049f84c)
- 新版 `0049f7b8`（命令位置の公開資料なし） · `0049f870`（命令位置の公開資料なし） · `0049f88c`（命令位置の公開資料なし）

~~~diff
- 0049f778 ["INT_ADD", "register:40f0:8", ["const:49f778:8", "const:4:8"]]
- 0049f778 ["CALL", null, ["callee:00c57e90:8"]]
+ 0049f7b8 ["INT_ADD", "register:40f0:8", ["const:49f7b8:8", "const:4:8"]]
+ 0049f7b8 ["CALL", null, ["callee:00c57e90:8"]]
- 0049f778 bytes c6e01e94
+ 0049f7b8 bytes b6e11e94
- 0049f830 ["INT_ADD", "register:40f0:8", ["const:49f830:8", "const:4:8"]]
- 0049f830 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0049f870 ["INT_ADD", "register:40f0:8", ["const:49f870:8", "const:4:8"]]
+ 0049f870 ["CALL", null, ["callee:00c57eb0:8"]]
- 0049f830 bytes a0e01e94
+ 0049f870 bytes 90e11e94
- 0049f84c ["INT_ADD", "register:40f0:8", ["const:49f84c:8", "const:4:8"]]
- 0049f84c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0049f88c ["INT_ADD", "register:40f0:8", ["const:49f88c:8", "const:4:8"]]
+ 0049f88c ["CALL", null, ["callee:00c57eb0:8"]]
- 0049f84c bytes 99e01e94
+ 0049f88c bytes 89e11e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff69b286a500ee1400f413acfb2aaa0f"></a>

### [`0049f8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f8b4.md) → [`0049f8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f8f4.md) FUN_0049f8f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049e694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e694.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`0049e6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e6d4.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049f91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f8b4.md#insn-0049f91c) · [`0049f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f8b4.md#insn-0049f954) · [`0049fa04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f8b4.md#insn-0049fa04)
- 新版 `0049f95c`（命令位置の公開資料なし） · `0049f994`（命令位置の公開資料なし） · `0049fa44`（命令位置の公開資料なし）

~~~diff
- 0049f91c ["INT_ADD", "register:40f0:8", ["const:49f91c:8", "const:4:8"]]
- 0049f91c ["CALL", null, ["callee:00c57f40:8"]]
+ 0049f95c ["INT_ADD", "register:40f0:8", ["const:49f95c:8", "const:4:8"]]
+ 0049f95c ["CALL", null, ["callee:00c57f40:8"]]
- 0049f91c bytes 89e01e94
+ 0049f95c bytes 79e11e94
- 0049f954 ["INT_ADD", "register:40f0:8", ["const:49f954:8", "const:4:8"]]
- 0049f954 ["CALL", null, ["callee:00c57e90:8"]]
+ 0049f994 ["INT_ADD", "register:40f0:8", ["const:49f994:8", "const:4:8"]]
+ 0049f994 ["CALL", null, ["callee:00c57e90:8"]]
- 0049f954 bytes 4fe01e94
+ 0049f994 bytes 3fe11e94
- 0049fa04 ["INT_ADD", "register:40f0:8", ["const:49fa04:8", "const:4:8"]]
- 0049fa04 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0049fa44 ["INT_ADD", "register:40f0:8", ["const:49fa44:8", "const:4:8"]]
+ 0049fa44 ["CALL", null, ["callee:00c57eb0:8"]]
- 0049fa04 bytes 2be01e94
+ 0049fa44 bytes 1be11e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54f424f25d9ac8a9e464c4c8c4922897"></a>

### [`004a0328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0328.md) → [`004a0368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0368.md) FUN_004a0368

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049ff10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049ff10.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004a04a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a04a8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0049ff50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049ff50.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`004a04e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a04e8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a03b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0328.md#insn-004a03b0) · [`004a0464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0328.md#insn-004a0464) · [`004a0480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0328.md#insn-004a0480)
- 新版 `004a03f0`（命令位置の公開資料なし） · `004a04a4`（命令位置の公開資料なし） · `004a04c0`（命令位置の公開資料なし）

~~~diff
- 004a03b0 ["INT_ADD", "register:40f0:8", ["const:4a03b0:8", "const:4:8"]]
- 004a03b0 ["CALL", null, ["callee:00c57e90:8"]]
+ 004a03f0 ["INT_ADD", "register:40f0:8", ["const:4a03f0:8", "const:4:8"]]
+ 004a03f0 ["CALL", null, ["callee:00c57e90:8"]]
- 004a03b0 bytes b8dd1e94
+ 004a03f0 bytes a8de1e94
- 004a0464 ["INT_ADD", "register:40f0:8", ["const:4a0464:8", "const:4:8"]]
- 004a0464 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004a04a4 ["INT_ADD", "register:40f0:8", ["const:4a04a4:8", "const:4:8"]]
+ 004a04a4 ["CALL", null, ["callee:00c57eb0:8"]]
- 004a0464 bytes 93dd1e94
+ 004a04a4 bytes 83de1e94
- 004a0480 ["INT_ADD", "register:40f0:8", ["const:4a0480:8", "const:4:8"]]
- 004a0480 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004a04c0 ["INT_ADD", "register:40f0:8", ["const:4a04c0:8", "const:4:8"]]
+ 004a04c0 ["CALL", null, ["callee:00c57eb0:8"]]
- 004a0480 bytes 8cdd1e94
+ 004a04c0 bytes 7cde1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2341770c13c464271d6abf2ebc37c68a"></a>

### [`004a1a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1a74.md) → [`004a1ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1ab4.md) _ZN5Botan7AES_1285clearEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00540a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540a48.md) [`00540b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540b38.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00540a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540a88.md) [`00540b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540b78.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a1a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1a74.md#insn-004a1a98) · [`004a1aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1a74.md#insn-004a1aa8) · [`004a1ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1a74.md#insn-004a1ac0)
- 新版 `004a1ad8`（命令位置の公開資料なし） · `004a1ae8`（命令位置の公開資料なし） · `004a1b00`（命令位置の公開資料なし）

~~~diff
- 004a1a98 ["INT_ADD", "register:40f0:8", ["const:4a1a98:8", "const:4:8"]]
- 004a1a98 ["CALL", null, ["callee:00c58090:8"]]
+ 004a1ad8 ["INT_ADD", "register:40f0:8", ["const:4a1ad8:8", "const:4:8"]]
+ 004a1ad8 ["CALL", null, ["callee:00c58090:8"]]
- 004a1a98 bytes 7ed81e94
+ 004a1ad8 bytes 6ed91e94
- 004a1aa8 ["INT_ADD", "register:40f0:8", ["const:4a1aa8:8", "const:4:8"]]
- 004a1aa8 ["CALL", null, ["callee:00540a88:8"]]
+ 004a1ae8 ["INT_ADD", "register:40f0:8", ["const:4a1ae8:8", "const:4:8"]]
+ 004a1ae8 ["CALL", null, ["callee:00540a88:8"]]
- 004a1aa8 bytes e87b0294
+ 004a1ae8 bytes e87b0294
- 004a1ac0 ["INT_ADD", "register:40f0:8", ["const:4a1ac0:8", "const:4:8"]]
- 004a1ac0 ["CALL", null, ["callee:00c58090:8"]]
+ 004a1b00 ["INT_ADD", "register:40f0:8", ["const:4a1b00:8", "const:4:8"]]
+ 004a1b00 ["CALL", null, ["callee:00c58090:8"]]
- 004a1ac0 bytes 74d81e94
+ 004a1b00 bytes 64d91e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c623db8be9fb9a317bfbefae4aedd1b"></a>

### [`004a1d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1d90.md) → [`004a1dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1dd0.md) _ZN5Botan7AES_1925clearEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00540a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540a48.md) [`00540b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540b38.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00540a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540a88.md) [`00540b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540b78.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a1db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1d90.md#insn-004a1db4) · [`004a1dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1d90.md#insn-004a1dc4) · [`004a1ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1d90.md#insn-004a1ddc)
- 新版 `004a1df4`（命令位置の公開資料なし） · `004a1e04`（命令位置の公開資料なし） · `004a1e1c`（命令位置の公開資料なし）

~~~diff
- 004a1db4 ["INT_ADD", "register:40f0:8", ["const:4a1db4:8", "const:4:8"]]
- 004a1db4 ["CALL", null, ["callee:00c58090:8"]]
+ 004a1df4 ["INT_ADD", "register:40f0:8", ["const:4a1df4:8", "const:4:8"]]
+ 004a1df4 ["CALL", null, ["callee:00c58090:8"]]
- 004a1db4 bytes b7d71e94
+ 004a1df4 bytes a7d81e94
- 004a1dc4 ["INT_ADD", "register:40f0:8", ["const:4a1dc4:8", "const:4:8"]]
- 004a1dc4 ["CALL", null, ["callee:00540a88:8"]]
+ 004a1e04 ["INT_ADD", "register:40f0:8", ["const:4a1e04:8", "const:4:8"]]
+ 004a1e04 ["CALL", null, ["callee:00540a88:8"]]
- 004a1dc4 bytes 217b0294
+ 004a1e04 bytes 217b0294
- 004a1ddc ["INT_ADD", "register:40f0:8", ["const:4a1ddc:8", "const:4:8"]]
- 004a1ddc ["CALL", null, ["callee:00c58090:8"]]
+ 004a1e1c ["INT_ADD", "register:40f0:8", ["const:4a1e1c:8", "const:4:8"]]
+ 004a1e1c ["CALL", null, ["callee:00c58090:8"]]
- 004a1ddc bytes add71e94
+ 004a1e1c bytes 9dd81e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e29c2ab4f1599b316b9a555762857a41"></a>

### [`004a20ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a20ac.md) → [`004a20ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a20ec.md) _ZN5Botan7AES_2565clearEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00540a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540a48.md) [`00540b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540b38.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00540a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540a88.md) [`00540b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540b78.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a20d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a20ac.md#insn-004a20d0) · [`004a20e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a20ac.md#insn-004a20e0) · [`004a20f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a20ac.md#insn-004a20f8)
- 新版 `004a2110`（命令位置の公開資料なし） · `004a2120`（命令位置の公開資料なし） · `004a2138`（命令位置の公開資料なし）

~~~diff
- 004a20d0 ["INT_ADD", "register:40f0:8", ["const:4a20d0:8", "const:4:8"]]
- 004a20d0 ["CALL", null, ["callee:00c58090:8"]]
+ 004a2110 ["INT_ADD", "register:40f0:8", ["const:4a2110:8", "const:4:8"]]
+ 004a2110 ["CALL", null, ["callee:00c58090:8"]]
- 004a20d0 bytes f0d61e94
+ 004a2110 bytes e0d71e94
- 004a20e0 ["INT_ADD", "register:40f0:8", ["const:4a20e0:8", "const:4:8"]]
- 004a20e0 ["CALL", null, ["callee:00540a88:8"]]
+ 004a2120 ["INT_ADD", "register:40f0:8", ["const:4a2120:8", "const:4:8"]]
+ 004a2120 ["CALL", null, ["callee:00540a88:8"]]
- 004a20e0 bytes 5a7a0294
+ 004a2120 bytes 5a7a0294
- 004a20f8 ["INT_ADD", "register:40f0:8", ["const:4a20f8:8", "const:4:8"]]
- 004a20f8 ["CALL", null, ["callee:00c58090:8"]]
+ 004a2138 ["INT_ADD", "register:40f0:8", ["const:4a2138:8", "const:4:8"]]
+ 004a2138 ["CALL", null, ["callee:00c58090:8"]]
- 004a20f8 bytes e6d61e94
+ 004a2138 bytes d6d71e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef65c295f9c8f7f7082cf2c5ff6c4810"></a>

### [`004a5158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5158.md) → [`004a5198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5198.md) _ZN5BotaneqERKNS_19AlgorithmIdentifierES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c582a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582a0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c586a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586a0.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a5228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5158.md#insn-004a5228)
- 新版 `004a5268`（命令位置の公開資料なし）

~~~diff
- 004a5228 ["INT_ADD", "register:40f0:8", ["const:4a5228:8", "const:4:8"]]
- 004a5228 ["CALL", null, ["callee:00c58050:8"]]
+ 004a5268 ["INT_ADD", "register:40f0:8", ["const:4a5268:8", "const:4:8"]]
+ 004a5268 ["CALL", null, ["callee:00c58050:8"]]
- 004a5228 bytes 8aca1e94
+ 004a5268 bytes 7acb1e94
~~~


<a id="compare-ed6295c05b26058851d1de24285c7606"></a>

### [`004a52ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a52ac.md) → [`004a52ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a52ec.md) _ZN5BotanneERKNS_19AlgorithmIdentifierES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c582a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c586a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a52b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a52ac.md#insn-004a52b4)
- 新版 `004a52f4`（命令位置の公開資料なし）

~~~diff
- 004a52b4 ["INT_ADD", "register:40f0:8", ["const:4a52b4:8", "const:4:8"]]
- 004a52b4 ["CALL", null, ["callee:00c586a0:8"]]
+ 004a52f4 ["INT_ADD", "register:40f0:8", ["const:4a52f4:8", "const:4:8"]]
+ 004a52f4 ["CALL", null, ["callee:00c586a0:8"]]
- 004a52b4 bytes fbcb1e94
+ 004a52f4 bytes ebcc1e94
~~~


<a id="compare-e46cfc088eeb42b9f1d1f0e88ee865c0"></a>

### [`004a52c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a52c8.md) → [`004a5308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5308.md) _ZNK5Botan19AlgorithmIdentifier11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c582b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582b0.md) [`00c582c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582c0.md) [`00c582d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c586b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586b0.md) [`00c586c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586c0.md) [`00c586d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a52f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a52c8.md#insn-004a52f0) · [`004a5304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a52c8.md#insn-004a5304) · [`004a5320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a52c8.md#insn-004a5320)
- 新版 `004a5330`（命令位置の公開資料なし） · `004a5344`（命令位置の公開資料なし） · `004a5360`（命令位置の公開資料なし）

~~~diff
- 004a52f0 ["INT_ADD", "register:40f0:8", ["const:4a52f0:8", "const:4:8"]]
- 004a52f0 ["CALL", null, ["callee:00c586b0:8"]]
+ 004a5330 ["INT_ADD", "register:40f0:8", ["const:4a5330:8", "const:4:8"]]
+ 004a5330 ["CALL", null, ["callee:00c586b0:8"]]
- 004a52f0 bytes f0cb1e94
+ 004a5330 bytes e0cc1e94
- 004a5304 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a5304 ["INT_ADD", "register:40f0:8", ["const:4a5304:8", "const:4:8"]]
- 004a5304 ["CALLIND", null, ["register:0:8"]]
+ 004a5344 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a5344 ["INT_ADD", "register:40f0:8", ["const:4a5344:8", "const:4:8"]]
+ 004a5344 ["CALLIND", null, ["register:0:8"]]
- 004a5304 bytes 00013fd6
+ 004a5344 bytes 00013fd6
- 004a5320 ["INT_ADD", "register:40f0:8", ["const:4a5320:8", "const:4:8"]]
- 004a5320 ["CALL", null, ["callee:00c586c0:8"]]
+ 004a5360 ["INT_ADD", "register:40f0:8", ["const:4a5360:8", "const:4:8"]]
+ 004a5360 ["CALL", null, ["callee:00c586c0:8"]]
- 004a5320 bytes e8cb1e94
+ 004a5360 bytes d8cc1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e64ee6318692ddd7051d3fb5c7031a14"></a>

### [`004a5528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5528.md) → [`004a5568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5568.md) _ZN5Botan11DER_Encoder6encodeERKNS_11ASN1_ObjectE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a5548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5528.md#insn-004a5548)
- 新版 `004a5588`（命令位置の公開資料なし）

~~~diff
- 004a5548 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a5548 ["INT_ADD", "register:40f0:8", ["const:4a5548:8", "const:4:8"]]
- 004a5548 ["CALLIND", null, ["register:0:8"]]
+ 004a5588 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a5588 ["INT_ADD", "register:40f0:8", ["const:4a5588:8", "const:4:8"]]
+ 004a5588 ["CALLIND", null, ["register:0:8"]]
- 004a5548 bytes 00013fd6
+ 004a5588 bytes 00013fd6
~~~


<a id="compare-29e97096969aa366e5e177886c3b2450"></a>

### [`004a590c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a590c.md) → [`004a594c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a594c.md) _ZN5Botan11BER_Decoder6decodeERNS_11ASN1_ObjectENS_8ASN1_TagES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a592c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a590c.md#insn-004a592c)
- 新版 `004a596c`（命令位置の公開資料なし）

~~~diff
- 004a592c ["COPY", "register:0:8", ["register:4040:8"]]
- 004a592c ["INT_ADD", "register:40f0:8", ["const:4a592c:8", "const:4:8"]]
- 004a592c ["CALLIND", null, ["register:0:8"]]
+ 004a596c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a596c ["INT_ADD", "register:40f0:8", ["const:4a596c:8", "const:4:8"]]
+ 004a596c ["CALLIND", null, ["register:0:8"]]
- 004a592c bytes 00013fd6
+ 004a596c bytes 00013fd6
~~~


<a id="compare-08ccdc5efffab86ea70a701d0bb014c0"></a>

### [`004a5940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5940.md) → [`004a5980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5980.md) FUN_004a5980

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`004a573c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a573c.md) [`004a5f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5f60.md) [`00506f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/00506f50.md) [`00509bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509bd4.md) [`0051f1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f1b4.md) · 呼出先 5件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 5件 [`004a577c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a577c.md) [`004a5fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5fa0.md) [`00506f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506f90.md) [`00509c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509c14.md) [`0051f1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f1f4.md) · 呼出先 5件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a5990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5940.md#insn-004a5990) · [`004a59c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5940.md#insn-004a59c4) · [`004a5a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5940.md#insn-004a5a08)
- 新版 `004a59d0`（命令位置の公開資料なし） · `004a5a04`（命令位置の公開資料なし） · `004a5a48`（命令位置の公開資料なし）

~~~diff
- 004a5990 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a5990 ["INT_ADD", "register:40f0:8", ["const:4a5990:8", "const:4:8"]]
- 004a5990 ["CALLIND", null, ["register:0:8"]]
+ 004a59d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a59d0 ["INT_ADD", "register:40f0:8", ["const:4a59d0:8", "const:4:8"]]
+ 004a59d0 ["CALLIND", null, ["register:0:8"]]
- 004a5990 bytes 00013fd6
+ 004a59d0 bytes 00013fd6
- 004a59c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a59c4 ["INT_ADD", "register:40f0:8", ["const:4a59c4:8", "const:4:8"]]
- 004a59c4 ["CALLIND", null, ["register:0:8"]]
+ 004a5a04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a5a04 ["INT_ADD", "register:40f0:8", ["const:4a5a04:8", "const:4:8"]]
+ 004a5a04 ["CALLIND", null, ["register:0:8"]]
- 004a59c4 bytes 00013fd6
+ 004a5a04 bytes 00013fd6
- 004a5a08 ["INT_ADD", "register:40f0:8", ["const:4a5a08:8", "const:4:8"]]
- 004a5a08 ["CALL", null, ["callee:00c57e90:8"]]
+ 004a5a48 ["INT_ADD", "register:40f0:8", ["const:4a5a48:8", "const:4:8"]]
+ 004a5a48 ["CALL", null, ["callee:00c57e90:8"]]
- 004a5a08 bytes 22c81e94
+ 004a5a48 bytes 12c91e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c91e9dd38606ebd150f0a873c39fa26"></a>

### [`004a5e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5e7c.md) → [`004a5ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5ebc.md) _ZNK5Botan9Attribute11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c582b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582b0.md) [`00c582c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582c0.md) [`00c582d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c586b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586b0.md) [`00c586c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586c0.md) [`00c586d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a5ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5e7c.md#insn-004a5ea4) · [`004a5eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5e7c.md#insn-004a5eb8) · [`004a5ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5e7c.md#insn-004a5ec8)
- 新版 `004a5ee4`（命令位置の公開資料なし） · `004a5ef8`（命令位置の公開資料なし） · `004a5f08`（命令位置の公開資料なし）

~~~diff
- 004a5ea4 ["INT_ADD", "register:40f0:8", ["const:4a5ea4:8", "const:4:8"]]
- 004a5ea4 ["CALL", null, ["callee:00c586b0:8"]]
+ 004a5ee4 ["INT_ADD", "register:40f0:8", ["const:4a5ee4:8", "const:4:8"]]
+ 004a5ee4 ["CALL", null, ["callee:00c586b0:8"]]
- 004a5ea4 bytes 03c91e94
+ 004a5ee4 bytes f3c91e94
- 004a5eb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a5eb8 ["INT_ADD", "register:40f0:8", ["const:4a5eb8:8", "const:4:8"]]
- 004a5eb8 ["CALLIND", null, ["register:0:8"]]
+ 004a5ef8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a5ef8 ["INT_ADD", "register:40f0:8", ["const:4a5ef8:8", "const:4:8"]]
+ 004a5ef8 ["CALLIND", null, ["register:0:8"]]
- 004a5eb8 bytes 00013fd6
+ 004a5ef8 bytes 00013fd6
- 004a5ec8 ["INT_ADD", "register:40f0:8", ["const:4a5ec8:8", "const:4:8"]]
- 004a5ec8 ["CALL", null, ["callee:00c586b0:8"]]
+ 004a5f08 ["INT_ADD", "register:40f0:8", ["const:4a5f08:8", "const:4:8"]]
+ 004a5f08 ["CALL", null, ["callee:00c586b0:8"]]
- 004a5ec8 bytes fac81e94
+ 004a5f08 bytes eac91e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06dd303eecb94d06ae7c2df244db3b6b"></a>

### [`004a680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) → [`004a684c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a684c.md) FUN_004a684c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 11件 [`004af444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af444.md) [`004bc378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc378.md) [`004beeec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004beeec.md) [`004d7e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7e9c.md) [`004e8dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8dc0.md) · 呼出先 1件 [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 12件 [`004af484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af484.md) [`004bc3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc3b8.md) [`004bef2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004bef2c.md) [`004d7edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7edc.md) [`004e8e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e8/004e8e00.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a6834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md#insn-004a6834)
- 新版 `004a6874`（命令位置の公開資料なし）

~~~diff
- 004a6834 ["INT_ADD", "register:40f0:8", ["const:4a6834:8", "const:4:8"]]
- 004a6834 ["CALL", null, ["callee:00c57f80:8"]]
+ 004a6874 ["INT_ADD", "register:40f0:8", ["const:4a6874:8", "const:4:8"]]
+ 004a6874 ["CALL", null, ["callee:00c57f80:8"]]
- 004a6834 bytes d3c41e94
+ 004a6874 bytes c3c51e94
~~~


<a id="compare-0b67db5432867204e330f6a86108f3a8"></a>

### [`004a7bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7bc8.md) → [`004a7c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7c08.md) _ZN5Botan3OIDpLEj

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58410.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c58810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58810.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a7c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7bc8.md#insn-004a7c44) · [`004a7c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7bc8.md#insn-004a7c70) · [`004a7c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7bc8.md#insn-004a7c84)
- 新版 `004a7c84`（命令位置の公開資料なし） · `004a7cb0`（命令位置の公開資料なし） · `004a7cc4`（命令位置の公開資料なし）

~~~diff
- 004a7c44 ["INT_ADD", "register:40f0:8", ["const:4a7c44:8", "const:4:8"]]
- 004a7c44 ["CALL", null, ["callee:00c57e90:8"]]
+ 004a7c84 ["INT_ADD", "register:40f0:8", ["const:4a7c84:8", "const:4:8"]]
+ 004a7c84 ["CALL", null, ["callee:00c57e90:8"]]
- 004a7c44 bytes 93bf1e94
+ 004a7c84 bytes 83c01e94
- 004a7c70 ["INT_ADD", "register:40f0:8", ["const:4a7c70:8", "const:4:8"]]
- 004a7c70 ["CALL", null, ["callee:00c58000:8"]]
+ 004a7cb0 ["INT_ADD", "register:40f0:8", ["const:4a7cb0:8", "const:4:8"]]
+ 004a7cb0 ["CALL", null, ["callee:00c58000:8"]]
- 004a7c70 bytes e4bf1e94
+ 004a7cb0 bytes d4c01e94
- 004a7c84 ["INT_ADD", "register:40f0:8", ["const:4a7c84:8", "const:4:8"]]
- 004a7c84 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004a7cc4 ["INT_ADD", "register:40f0:8", ["const:4a7cc4:8", "const:4:8"]]
+ 004a7cc4 ["CALL", null, ["callee:00c57eb0:8"]]
- 004a7c84 bytes 8bbf1e94
+ 004a7cc4 bytes 7bc01e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91572cb4fb9f0a006d8a8fa003775ad3"></a>

### [`004abfe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ab/004abfe8.md) → [`004ac028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac028.md) _ZN5Botan6BigInt6encodeERKS0_NS0_4BaseE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c584d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c584d0.md) · 呼出先 5件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c58540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58540.md) [`00c58550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58550.md)
- 新版 呼出元 1件 [`00c588d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c588d0.md) · 呼出先 5件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c58940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58940.md) [`00c58950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58950.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ac008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ab/004abfe8.md#insn-004ac008) · [`004ac024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ab/004abfe8.md#insn-004ac024) · [`004ac040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ab/004abfe8.md#insn-004ac040)
- 新版 `004ac048`（命令位置の公開資料なし） · `004ac064`（命令位置の公開資料なし） · `004ac080`（命令位置の公開資料なし）

~~~diff
- 004ac008 ["INT_ADD", "register:40f0:8", ["const:4ac008:8", "const:4:8"]]
- 004ac008 ["CALL", null, ["callee:00c58940:8"]]
+ 004ac048 ["INT_ADD", "register:40f0:8", ["const:4ac048:8", "const:4:8"]]
+ 004ac048 ["CALL", null, ["callee:00c58940:8"]]
- 004ac008 bytes 4eb11e94
+ 004ac048 bytes 3eb21e94
- 004ac024 ["INT_ADD", "register:40f0:8", ["const:4ac024:8", "const:4:8"]]
- 004ac024 ["CALL", null, ["callee:00c57e90:8"]]
+ 004ac064 ["INT_ADD", "register:40f0:8", ["const:4ac064:8", "const:4:8"]]
+ 004ac064 ["CALL", null, ["callee:00c57e90:8"]]
- 004ac024 bytes 9bae1e94
+ 004ac064 bytes 8baf1e94
- 004ac040 ["INT_ADD", "register:40f0:8", ["const:4ac040:8", "const:4:8"]]
- 004ac040 ["CALL", null, ["callee:00c58090:8"]]
+ 004ac080 ["INT_ADD", "register:40f0:8", ["const:4ac080:8", "const:4:8"]]
+ 004ac080 ["CALL", null, ["callee:00c58090:8"]]
- 004ac040 bytes 14af1e94
+ 004ac080 bytes 04b01e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25b1224679f9378bf82a8d879b44f7e4"></a>

### [`004ac160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac160.md) → [`004ac1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac1a0.md) FUN_004ac1a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ac17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac160.md#insn-004ac17c)
- 新版 `004ac1bc`（命令位置の公開資料なし）

~~~diff
- 004ac17c ["INT_ADD", "register:40f0:8", ["const:4ac17c:8", "const:4:8"]]
- 004ac17c ["CALL", null, ["callee:00c57eb0:8"]]
+ 004ac1bc ["INT_ADD", "register:40f0:8", ["const:4ac1bc:8", "const:4:8"]]
+ 004ac1bc ["CALL", null, ["callee:00c57eb0:8"]]
- 004ac17c bytes 4dae1e94
+ 004ac1bc bytes 3daf1e94
~~~


<a id="compare-2ee51a3fc75c9957be6f7d94267b231f"></a>

### [`004acbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004acbe4.md) → [`004acc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004acc24.md) FUN_004acc24

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00520010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520010.md) [`006e5d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5d30.md) · 呼出先 3件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 2件 [`00520050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520050.md) [`006e5d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e5/006e5d70.md) · 呼出先 3件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004acbfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004acbe4.md#insn-004acbfc) · [`004acc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004acbe4.md#insn-004acc38) · [`004acc5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004acbe4.md#insn-004acc5c)
- 新版 `004acc3c`（命令位置の公開資料なし） · `004acc78`（命令位置の公開資料なし） · `004acc9c`（命令位置の公開資料なし）

~~~diff
- 004acbfc ["INT_ADD", "register:40f0:8", ["const:4acbfc:8", "const:4:8"]]
- 004acbfc ["CALL", null, ["callee:00c57fe0:8"]]
+ 004acc3c ["INT_ADD", "register:40f0:8", ["const:4acc3c:8", "const:4:8"]]
+ 004acc3c ["CALL", null, ["callee:00c57fe0:8"]]
- 004acbfc bytes f9ab1e94
+ 004acc3c bytes e9ac1e94
- 004acc38 ["INT_ADD", "register:40f0:8", ["const:4acc38:8", "const:4:8"]]
- 004acc38 ["CALL", null, ["callee:00c58050:8"]]
+ 004acc78 ["INT_ADD", "register:40f0:8", ["const:4acc78:8", "const:4:8"]]
+ 004acc78 ["CALL", null, ["callee:00c58050:8"]]
- 004acc38 bytes 06ac1e94
+ 004acc78 bytes f6ac1e94
- 004acc5c ["INT_ADD", "register:40f0:8", ["const:4acc5c:8", "const:4:8"]]
- 004acc5c ["CALL", null, ["callee:0044291c:8"]]
+ 004acc9c ["INT_ADD", "register:40f0:8", ["const:4acc9c:8", "const:4:8"]]
+ 004acc9c ["CALL", null, ["callee:0044291c:8"]]
- 004acc5c bytes 2057fe97
+ 004acc9c bytes 2057fe97
~~~


<a id="compare-ac86e1688344d9608a0f6a4c92d4175e"></a>

### [`004af120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af120.md) → [`004af160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af160.md) _ZNK5Botan9X509_Time16to_std_timepointEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58600.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004af150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af120.md#insn-004af150) · [`004af174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af120.md#insn-004af174)
- 新版 `004af190`（命令位置の公開資料なし） · `004af1b4`（命令位置の公開資料なし）

~~~diff
- 004af150 ["INT_ADD", "register:40f0:8", ["const:4af150:8", "const:4:8"]]
- 004af150 ["CALL", null, ["callee:00c58a00:8"]]
+ 004af190 ["INT_ADD", "register:40f0:8", ["const:4af190:8", "const:4:8"]]
+ 004af190 ["CALL", null, ["callee:00c58a00:8"]]
- 004af150 bytes 2ca51e94
+ 004af190 bytes 1ca61e94
- 004af174 ["INT_ADD", "register:40f0:8", ["const:4af174:8", "const:4:8"]]
- 004af174 ["CALL", null, ["callee:00c57ee0:8"]]
+ 004af1b4 ["INT_ADD", "register:40f0:8", ["const:4af1b4:8", "const:4:8"]]
+ 004af1b4 ["CALL", null, ["callee:00c57ee0:8"]]
- 004af174 bytes 5ba21e94
+ 004af1b4 bytes 4ba31e94
~~~


<a id="compare-fb67a042c082433962d02ed36bf7a0da"></a>

### [`004af3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af3a0.md) → [`004af3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af3e0.md) _ZN5BotaneqERKNS_9X509_TimeES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c585e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c589e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004af3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af3a0.md#insn-004af3a8)
- 新版 `004af3e8`（命令位置の公開資料なし）

~~~diff
- 004af3a8 ["INT_ADD", "register:40f0:8", ["const:4af3a8:8", "const:4:8"]]
- 004af3a8 ["CALL", null, ["callee:00c589e0:8"]]
+ 004af3e8 ["INT_ADD", "register:40f0:8", ["const:4af3e8:8", "const:4:8"]]
+ 004af3e8 ["CALL", null, ["callee:00c589e0:8"]]
- 004af3a8 bytes 8ea41e94
+ 004af3e8 bytes 7ea51e94
~~~


<a id="compare-394265b22070f09ca532a7ee38121aa6"></a>

### [`004af3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af3bc.md) → [`004af3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af3fc.md) _ZN5BotanneERKNS_9X509_TimeES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c585e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c589e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004af3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af3bc.md#insn-004af3c4)
- 新版 `004af404`（命令位置の公開資料なし）

~~~diff
- 004af3c4 ["INT_ADD", "register:40f0:8", ["const:4af3c4:8", "const:4:8"]]
- 004af3c4 ["CALL", null, ["callee:00c589e0:8"]]
+ 004af404 ["INT_ADD", "register:40f0:8", ["const:4af404:8", "const:4:8"]]
+ 004af404 ["CALL", null, ["callee:00c589e0:8"]]
- 004af3c4 bytes 87a41e94
+ 004af404 bytes 77a51e94
~~~


