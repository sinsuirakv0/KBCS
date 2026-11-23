# v16.0.0 → v16.0.1 · 要調査の変更候補 (17)

[一覧の目次](README.md)

<a id="compare-9947b19d9adc532b91be779482372d9e"></a>

### [`005d44dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d44dc.md) → [`005d451c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d451c.md) FUN_005d451c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005d343c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d343c.md) · 呼出先 4件 [`00449978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/00449978.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`005d347c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d347c.md) · 呼出先 4件 [`004499b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00449/004499b8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d4508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d44dc.md#insn-005d4508) · [`005d4574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d44dc.md#insn-005d4574) · [`005d45c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d44dc.md#insn-005d45c0)
- 新版 `005d4548`（命令位置の公開資料なし） · `005d45b4`（命令位置の公開資料なし） · `005d4600`（命令位置の公開資料なし）

~~~diff
- 005d4508 ["COPY", "register:0:8", ["register:4040:8"]]
- 005d4508 ["INT_ADD", "register:40f0:8", ["const:5d4508:8", "const:4:8"]]
- 005d4508 ["CALLIND", null, ["register:0:8"]]
+ 005d4548 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d4548 ["INT_ADD", "register:40f0:8", ["const:5d4548:8", "const:4:8"]]
+ 005d4548 ["CALLIND", null, ["register:0:8"]]
- 005d4508 bytes 00013fd6
+ 005d4548 bytes 00013fd6
- 005d4574 ["INT_ADD", "register:40f0:8", ["const:5d4574:8", "const:4:8"]]
- 005d4574 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d45b4 ["INT_ADD", "register:40f0:8", ["const:5d45b4:8", "const:4:8"]]
+ 005d45b4 ["CALL", null, ["callee:00c57e90:8"]]
- 005d4574 bytes 470d1a94
+ 005d45b4 bytes 370e1a94
- 005d45c0 ["INT_ADD", "register:40f0:8", ["const:5d45c0:8", "const:4:8"]]
- 005d45c0 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d4600 ["INT_ADD", "register:40f0:8", ["const:5d4600:8", "const:4:8"]]
+ 005d4600 ["CALL", null, ["callee:00c57e90:8"]]
- 005d45c0 bytes 340d1a94
+ 005d4600 bytes 240e1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1e1d97173f774d5d27a0db4815ed938"></a>

### [`005d4638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4638.md) → [`005d4678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d4678.md) FUN_005d4678

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005d3748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3748.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005d3788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d3788.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d4708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4638.md#insn-005d4708) · [`005d4774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4638.md#insn-005d4774) · [`005d4784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4638.md#insn-005d4784)
- 新版 `005d4748`（命令位置の公開資料なし） · `005d47b4`（命令位置の公開資料なし） · `005d47c4`（命令位置の公開資料なし）

~~~diff
- 005d4708 ["INT_ADD", "register:40f0:8", ["const:5d4708:8", "const:4:8"]]
- 005d4708 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d4748 ["INT_ADD", "register:40f0:8", ["const:5d4748:8", "const:4:8"]]
+ 005d4748 ["CALL", null, ["callee:00c57e90:8"]]
- 005d4708 bytes e20c1a94
+ 005d4748 bytes d20d1a94
- 005d4774 ["COPY", "register:0:8", ["register:4050:8"]]
- 005d4774 ["INT_ADD", "register:40f0:8", ["const:5d4774:8", "const:4:8"]]
- 005d4774 ["CALLIND", null, ["register:0:8"]]
+ 005d47b4 ["COPY", "register:0:8", ["register:4050:8"]]
+ 005d47b4 ["INT_ADD", "register:40f0:8", ["const:5d47b4:8", "const:4:8"]]
+ 005d47b4 ["CALLIND", null, ["register:0:8"]]
- 005d4774 bytes 40013fd6
+ 005d47b4 bytes 40013fd6
- 005d4784 ["INT_ADD", "register:40f0:8", ["const:5d4784:8", "const:4:8"]]
- 005d4784 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d47c4 ["INT_ADD", "register:40f0:8", ["const:5d47c4:8", "const:4:8"]]
+ 005d47c4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005d4784 bytes cb0c1a94
+ 005d47c4 bytes bb0d1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbff8620a52f00ba32da8ac2a14c67a4"></a>

### [`005d4848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4848.md) → [`005d4888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d4888.md) FUN_005d4888

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d3748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3748.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005d49e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d49e8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005d3788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d3788.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005d4a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d4a28.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d48d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4848.md#insn-005d48d0) · [`005d4994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4848.md#insn-005d4994) · [`005d49a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4848.md#insn-005d49a4)
- 新版 `005d4910`（命令位置の公開資料なし） · `005d49d4`（命令位置の公開資料なし） · `005d49e4`（命令位置の公開資料なし）

~~~diff
- 005d48d0 ["INT_ADD", "register:40f0:8", ["const:5d48d0:8", "const:4:8"]]
- 005d48d0 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d4910 ["INT_ADD", "register:40f0:8", ["const:5d4910:8", "const:4:8"]]
+ 005d4910 ["CALL", null, ["callee:00c57e90:8"]]
- 005d48d0 bytes 700c1a94
+ 005d4910 bytes 600d1a94
- 005d4994 ["INT_ADD", "register:40f0:8", ["const:5d4994:8", "const:4:8"]]
- 005d4994 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d49d4 ["INT_ADD", "register:40f0:8", ["const:5d49d4:8", "const:4:8"]]
+ 005d49d4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005d4994 bytes 470c1a94
+ 005d49d4 bytes 370d1a94
- 005d49a4 ["INT_ADD", "register:40f0:8", ["const:5d49a4:8", "const:4:8"]]
- 005d49a4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d49e4 ["INT_ADD", "register:40f0:8", ["const:5d49e4:8", "const:4:8"]]
+ 005d49e4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005d49a4 bytes 430c1a94
+ 005d49e4 bytes 330d1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04a729f0ee0d00bcd7a55901f34b4053"></a>

### [`005d53c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d53c8.md) → [`005d5408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5408.md) FUN_005d5408

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005cdcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdcc0.md) [`005d51bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d51bc.md) · 呼出先 3件 [`005d4b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4b08.md) [`005d4c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4c48.md) [`005d4c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4c94.md)
- 新版 呼出元 2件 [`005cdd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cdd00.md) [`005d51fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d51fc.md) · 呼出先 3件 [`005d4b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d4b48.md) [`005d4c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d4c88.md) [`005d4cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d4cd4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d5400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d53c8.md#insn-005d5400) · [`005d55e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d53c8.md#insn-005d55e4) · [`005d55fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d53c8.md#insn-005d55fc)
- 新版 `005d5440`（命令位置の公開資料なし） · `005d5624`（命令位置の公開資料なし） · `005d563c`（命令位置の公開資料なし）

~~~diff
- 005d5400 ["INT_ADD", "register:40f0:8", ["const:5d5400:8", "const:4:8"]]
- 005d5400 ["CALL", null, ["callee:005d4b48:8"]]
+ 005d5440 ["INT_ADD", "register:40f0:8", ["const:5d5440:8", "const:4:8"]]
+ 005d5440 ["CALL", null, ["callee:005d4b48:8"]]
- 005d5400 bytes c2fdff97
+ 005d5440 bytes c2fdff97
- 005d55e4 ["INT_ADD", "register:40f0:8", ["const:5d55e4:8", "const:4:8"]]
- 005d55e4 ["CALL", null, ["callee:005d4cd4:8"]]
+ 005d5624 ["INT_ADD", "register:40f0:8", ["const:5d5624:8", "const:4:8"]]
+ 005d5624 ["CALL", null, ["callee:005d4cd4:8"]]
- 005d55e4 bytes acfdff97
+ 005d5624 bytes acfdff97
- 005d55fc ["INT_ADD", "register:40f0:8", ["const:5d55fc:8", "const:4:8"]]
- 005d55fc ["CALL", null, ["callee:005d4b48:8"]]
+ 005d563c ["INT_ADD", "register:40f0:8", ["const:5d563c:8", "const:4:8"]]
+ 005d563c ["CALL", null, ["callee:005d4b48:8"]]
- 005d55fc bytes 43fdff97
+ 005d563c bytes 43fdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d10b3293300fb631966845a50cf8609d"></a>

### [`005d57cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d57cc.md) → [`005d580c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d580c.md) FUN_005d580c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d5b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5b50.md) · 呼出先 2件 [`005d0fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0fb8.md) [`005d1004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1004.md)
- 新版 呼出元 1件 [`005d5b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5b90.md) · 呼出先 2件 [`005d0ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0ff8.md) [`005d1044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d1044.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d580c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d57cc.md#insn-005d580c) · [`005d5828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d57cc.md#insn-005d5828)
- 新版 `005d584c`（命令位置の公開資料なし） · `005d5868`（命令位置の公開資料なし）

~~~diff
- 005d580c ["INT_ADD", "register:40f0:8", ["const:5d580c:8", "const:4:8"]]
- 005d580c ["CALL", null, ["callee:005d1044:8"]]
+ 005d584c ["INT_ADD", "register:40f0:8", ["const:5d584c:8", "const:4:8"]]
+ 005d584c ["CALL", null, ["callee:005d1044:8"]]
- 005d580c bytes feedff97
+ 005d584c bytes feedff97
- 005d5828 ["INT_ADD", "register:40f0:8", ["const:5d5828:8", "const:4:8"]]
- 005d5828 ["CALL", null, ["callee:005d0ff8:8"]]
+ 005d5868 ["INT_ADD", "register:40f0:8", ["const:5d5868:8", "const:4:8"]]
+ 005d5868 ["CALL", null, ["callee:005d0ff8:8"]]
- 005d5828 bytes e4edff97
+ 005d5868 bytes e4edff97
~~~


<a id="compare-6d1b4883059aa69d3afaf3a132cf84bb"></a>

### [`005d5b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5b50.md) → [`005d5b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5b90.md) FUN_005d5b90

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d5a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5a28.md) · 呼出先 3件 [`005d0e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0e78.md) [`005d3560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3560.md) [`005d57cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d57cc.md)
- 新版 呼出元 1件 [`005d5a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5a68.md) · 呼出先 3件 [`005d0eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0eb8.md) [`005d35a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d35a0.md) [`005d580c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d580c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d5bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5b50.md#insn-005d5bbc) · [`005d5c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5b50.md#insn-005d5c04)
- 新版 `005d5bfc`（命令位置の公開資料なし） · `005d5c44`（命令位置の公開資料なし）

~~~diff
- 005d5bbc ["INT_ADD", "register:40f0:8", ["const:5d5bbc:8", "const:4:8"]]
- 005d5bbc ["CALL", null, ["callee:005d0eb8:8"]]
+ 005d5bfc ["INT_ADD", "register:40f0:8", ["const:5d5bfc:8", "const:4:8"]]
+ 005d5bfc ["CALL", null, ["callee:005d0eb8:8"]]
- 005d5bbc bytes afecff97
+ 005d5bfc bytes afecff97
- 005d5c04 ["INT_ADD", "register:40f0:8", ["const:5d5c04:8", "const:4:8"]]
- 005d5c04 ["CALL", null, ["callee:005d580c:8"]]
+ 005d5c44 ["INT_ADD", "register:40f0:8", ["const:5d5c44:8", "const:4:8"]]
+ 005d5c44 ["CALL", null, ["callee:005d580c:8"]]
- 005d5c04 bytes f2feff97
+ 005d5c44 bytes f2feff97
~~~


<a id="compare-9bfafbfd1be8cd892115f1e4c35eedf4"></a>

### [`005d5c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5c20.md) → [`005d5c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5c60.md) FUN_005d5c60

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005cd0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd0b0.md) [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 4件 [`005cf680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf680.md) [`005cfaf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfaf4.md) [`005d60d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d60d0.md) [`005d69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md)
- 新版 呼出元 2件 [`005cd0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd0f0.md) [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 4件 [`005cf6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cf6c0.md) [`005cfb34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cfb34.md) [`005d6110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d6/005d6110.md) [`005d69f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d6/005d69f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d5c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5c20.md#insn-005d5c78) · [`005d5cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5c20.md#insn-005d5cd4) · [`005d5cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5c20.md#insn-005d5cfc)
- 新版 `005d5cb8`（命令位置の公開資料なし） · `005d5d14`（命令位置の公開資料なし） · `005d5d3c`（命令位置の公開資料なし）

~~~diff
- 005d5c78 ["INT_ADD", "register:40f0:8", ["const:5d5c78:8", "const:4:8"]]
- 005d5c78 ["CALL", null, ["callee:005cfb34:8"]]
+ 005d5cb8 ["INT_ADD", "register:40f0:8", ["const:5d5cb8:8", "const:4:8"]]
+ 005d5cb8 ["CALL", null, ["callee:005cfb34:8"]]
- 005d5c78 bytes 9fe7ff97
+ 005d5cb8 bytes 9fe7ff97
- 005d5cd4 ["INT_ADD", "register:40f0:8", ["const:5d5cd4:8", "const:4:8"]]
- 005d5cd4 ["CALL", null, ["callee:005d69f0:8"]]
+ 005d5d14 ["INT_ADD", "register:40f0:8", ["const:5d5d14:8", "const:4:8"]]
+ 005d5d14 ["CALL", null, ["callee:005d69f0:8"]]
- 005d5cd4 bytes 37030094
+ 005d5d14 bytes 37030094
- 005d5cfc ["INT_ADD", "register:40f0:8", ["const:5d5cfc:8", "const:4:8"]]
- 005d5cfc ["CALL", null, ["callee:005cf6c0:8"]]
+ 005d5d3c ["INT_ADD", "register:40f0:8", ["const:5d5d3c:8", "const:4:8"]]
+ 005d5d3c ["CALL", null, ["callee:005cf6c0:8"]]
- 005d5cfc bytes 61e6ff97
+ 005d5d3c bytes 61e6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d7c4351f8f77e8e339c673eef0d175d"></a>

### [`005d5f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5f14.md) → [`005d5f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5f54.md) FUN_005d5f54

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005cd0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd0b0.md) · 呼出先 1件 [`005d851c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d851c.md)
- 新版 呼出元 1件 [`005cd0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd0f0.md) · 呼出先 1件 [`005d855c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d855c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d5f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5f14.md#insn-005d5f78)
- 新版 `005d5fb8`（命令位置の公開資料なし）

~~~diff
- 005d5f78 ["INT_ADD", "register:40f0:8", ["const:5d5f78:8", "const:4:8"]]
- 005d5f78 ["CALL", null, ["callee:005d855c:8"]]
+ 005d5fb8 ["INT_ADD", "register:40f0:8", ["const:5d5fb8:8", "const:4:8"]]
+ 005d5fb8 ["CALL", null, ["callee:005d855c:8"]]
- 005d5f78 bytes 69090094
+ 005d5fb8 bytes 69090094
~~~


<a id="compare-c03600a14b9425e937dd0d69f770f98d"></a>

### [`005d69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md) → [`005d69f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d6/005d69f0.md) FUN_005d69f0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005d5c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5c20.md) · 呼出先 13件 [`005cfcd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfcd0.md) [`005cfd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd14.md) [`005cfd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd60.md) [`005cfed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfed8.md) [`005cff24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cff24.md)
- 新版 呼出元 1件 [`005d5c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5c60.md) · 呼出先 13件 [`005cfd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cfd10.md) [`005cfd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cfd54.md) [`005cfda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cfda0.md) [`005cff18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cff18.md) [`005cff64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cff64.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d6a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md#insn-005d6a50) · [`005d6a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md#insn-005d6a68) · [`005d6a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md#insn-005d6a78)
- 新版 `005d6a90`（命令位置の公開資料なし） · `005d6aa8`（命令位置の公開資料なし） · `005d6ab8`（命令位置の公開資料なし）

~~~diff
- 005d6a50 ["INT_ADD", "register:40f0:8", ["const:5d6a50:8", "const:4:8"]]
- 005d6a50 ["CALL", null, ["callee:005cffec:8"]]
+ 005d6a90 ["INT_ADD", "register:40f0:8", ["const:5d6a90:8", "const:4:8"]]
+ 005d6a90 ["CALL", null, ["callee:005cffec:8"]]
- 005d6a50 bytes 57e5ff97
+ 005d6a90 bytes 57e5ff97
- 005d6a68 ["INT_ADD", "register:40f0:8", ["const:5d6a68:8", "const:4:8"]]
- 005d6a68 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d6aa8 ["INT_ADD", "register:40f0:8", ["const:5d6aa8:8", "const:4:8"]]
+ 005d6aa8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005d6a68 bytes 12041a94
+ 005d6aa8 bytes 02051a94
- 005d6a78 ["INT_ADD", "register:40f0:8", ["const:5d6a78:8", "const:4:8"]]
- 005d6a78 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d6ab8 ["INT_ADD", "register:40f0:8", ["const:5d6ab8:8", "const:4:8"]]
+ 005d6ab8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005d6a78 bytes 0e041a94
+ 005d6ab8 bytes fe041a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61ae958cf69318fc59474df1ba96bb6a"></a>

### [`005d6fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d6fb0.md) → [`005d6ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d6/005d6ff0.md) FUN_005d6ff0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d7100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7100.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005d7140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d7/005d7140.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d7058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d6fb0.md#insn-005d7058) · [`005d7068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d6fb0.md#insn-005d7068) · [`005d70ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d6fb0.md#insn-005d70ac)
- 新版 `005d7098`（命令位置の公開資料なし） · `005d70a8`（命令位置の公開資料なし） · `005d70ec`（命令位置の公開資料なし）

~~~diff
- 005d7058 ["INT_ADD", "register:40f0:8", ["const:5d7058:8", "const:4:8"]]
- 005d7058 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d7098 ["INT_ADD", "register:40f0:8", ["const:5d7098:8", "const:4:8"]]
+ 005d7098 ["CALL", null, ["callee:00c57eb0:8"]]
- 005d7058 bytes 96021a94
+ 005d7098 bytes 86031a94
- 005d7068 ["INT_ADD", "register:40f0:8", ["const:5d7068:8", "const:4:8"]]
- 005d7068 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d70a8 ["INT_ADD", "register:40f0:8", ["const:5d70a8:8", "const:4:8"]]
+ 005d70a8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005d7068 bytes 92021a94
+ 005d70a8 bytes 82031a94
- 005d70ac ["INT_ADD", "register:40f0:8", ["const:5d70ac:8", "const:4:8"]]
- 005d70ac ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d70ec ["INT_ADD", "register:40f0:8", ["const:5d70ec:8", "const:4:8"]]
+ 005d70ec ["CALL", null, ["callee:00c57eb0:8"]]
- 005d70ac bytes 81021a94
+ 005d70ec bytes 71031a94
~~~


<a id="compare-60cb755721c109378b894dd2e44521e5"></a>

### [`005d7100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7100.md) → [`005d7140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d7/005d7140.md) FUN_005d7140

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d60d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d60d0.md) · 呼出先 2件 [`005d6fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d6fb0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005d6110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d6/005d6110.md) · 呼出先 2件 [`005d6ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d6/005d6ff0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d7114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7100.md#insn-005d7114) · [`005d7128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7100.md#insn-005d7128)
- 新版 `005d7154`（命令位置の公開資料なし） · `005d7168`（命令位置の公開資料なし）

~~~diff
- 005d7114 ["INT_ADD", "register:40f0:8", ["const:5d7114:8", "const:4:8"]]
- 005d7114 ["CALL", null, ["callee:005d6ff0:8"]]
+ 005d7154 ["INT_ADD", "register:40f0:8", ["const:5d7154:8", "const:4:8"]]
+ 005d7154 ["CALL", null, ["callee:005d6ff0:8"]]
- 005d7114 bytes a7ffff97
+ 005d7154 bytes a7ffff97
- 005d7128 ["INT_ADD", "register:40f0:8", ["const:5d7128:8", "const:4:8"]]
- 005d7128 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d7168 ["INT_ADD", "register:40f0:8", ["const:5d7168:8", "const:4:8"]]
+ 005d7168 ["CALL", null, ["callee:00c57eb0:8"]]
- 005d7128 bytes 62021a94
+ 005d7168 bytes 52031a94
~~~


<a id="compare-e4095e3d9065137c90fd417538d9ecb5"></a>

### [`005d717c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d717c.md) → [`005d71bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d7/005d71bc.md) FUN_005d71bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d60d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d60d0.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005d763c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d763c.md) [`005d77c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d77c4.md) [`005d7950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7950.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`005d6110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d6/005d6110.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005d767c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d7/005d767c.md) [`005d7804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d7/005d7804.md) [`005d7990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d7/005d7990.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d7214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d717c.md#insn-005d7214) · [`005d7258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d717c.md#insn-005d7258) · [`005d7268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d717c.md#insn-005d7268)
- 新版 `005d7254`（命令位置の公開資料なし） · `005d7298`（命令位置の公開資料なし） · `005d72a8`（命令位置の公開資料なし）

~~~diff
- 005d7214 ["INT_ADD", "register:40f0:8", ["const:5d7214:8", "const:4:8"]]
- 005d7214 ["CALL", null, ["callee:00c57f40:8"]]
+ 005d7254 ["INT_ADD", "register:40f0:8", ["const:5d7254:8", "const:4:8"]]
+ 005d7254 ["CALL", null, ["callee:00c57f40:8"]]
- 005d7214 bytes 4b021a94
+ 005d7254 bytes 3b031a94
- 005d7258 ["INT_ADD", "register:40f0:8", ["const:5d7258:8", "const:4:8"]]
- 005d7258 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d7298 ["INT_ADD", "register:40f0:8", ["const:5d7298:8", "const:4:8"]]
+ 005d7298 ["CALL", null, ["callee:00c57e90:8"]]
- 005d7258 bytes 0e021a94
+ 005d7298 bytes fe021a94
- 005d7268 ["INT_ADD", "register:40f0:8", ["const:5d7268:8", "const:4:8"]]
- 005d7268 ["CALL", null, ["callee:005d767c:8"]]
+ 005d72a8 ["INT_ADD", "register:40f0:8", ["const:5d72a8:8", "const:4:8"]]
+ 005d72a8 ["CALL", null, ["callee:005d767c:8"]]
- 005d7268 bytes f5000094
+ 005d72a8 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-526bfe84e057822f41bc5fe321ab555e"></a>

### [`005d763c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d763c.md) → [`005d767c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d7/005d767c.md) FUN_005d767c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005d717c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d717c.md) [`005d7adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7adc.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 2件 [`005d71bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d7/005d71bc.md) [`005d7b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d7/005d7b1c.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d76a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d763c.md#insn-005d76a4) · [`005d76dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d763c.md#insn-005d76dc) · [`005d778c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d763c.md#insn-005d778c)
- 新版 `005d76e4`（命令位置の公開資料なし） · `005d771c`（命令位置の公開資料なし） · `005d77cc`（命令位置の公開資料なし）

~~~diff
- 005d76a4 ["INT_ADD", "register:40f0:8", ["const:5d76a4:8", "const:4:8"]]
- 005d76a4 ["CALL", null, ["callee:00c57f40:8"]]
+ 005d76e4 ["INT_ADD", "register:40f0:8", ["const:5d76e4:8", "const:4:8"]]
+ 005d76e4 ["CALL", null, ["callee:00c57f40:8"]]
- 005d76a4 bytes 27011a94
+ 005d76e4 bytes 17021a94
- 005d76dc ["INT_ADD", "register:40f0:8", ["const:5d76dc:8", "const:4:8"]]
- 005d76dc ["CALL", null, ["callee:00c57e90:8"]]
+ 005d771c ["INT_ADD", "register:40f0:8", ["const:5d771c:8", "const:4:8"]]
+ 005d771c ["CALL", null, ["callee:00c57e90:8"]]
- 005d76dc bytes ed001a94
+ 005d771c bytes dd011a94
- 005d778c ["INT_ADD", "register:40f0:8", ["const:5d778c:8", "const:4:8"]]
- 005d778c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d77cc ["INT_ADD", "register:40f0:8", ["const:5d77cc:8", "const:4:8"]]
+ 005d77cc ["CALL", null, ["callee:00c57eb0:8"]]
- 005d778c bytes c9001a94
+ 005d77cc bytes b9011a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9706fac334b24e539a78b7e3b952287"></a>

### [`005d77c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d77c4.md) → [`005d7804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d7/005d7804.md) FUN_005d7804

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005d717c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d717c.md) [`005d7adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7adc.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 2件 [`005d71bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d7/005d71bc.md) [`005d7b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d7/005d7b1c.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d7834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d77c4.md#insn-005d7834) · [`005d786c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d77c4.md#insn-005d786c) · [`005d791c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d77c4.md#insn-005d791c)
- 新版 `005d7874`（命令位置の公開資料なし） · `005d78ac`（命令位置の公開資料なし） · `005d795c`（命令位置の公開資料なし）

~~~diff
- 005d7834 ["INT_ADD", "register:40f0:8", ["const:5d7834:8", "const:4:8"]]
- 005d7834 ["CALL", null, ["callee:00c57f40:8"]]
+ 005d7874 ["INT_ADD", "register:40f0:8", ["const:5d7874:8", "const:4:8"]]
+ 005d7874 ["CALL", null, ["callee:00c57f40:8"]]
- 005d7834 bytes c3001a94
+ 005d7874 bytes b3011a94
- 005d786c ["INT_ADD", "register:40f0:8", ["const:5d786c:8", "const:4:8"]]
- 005d786c ["CALL", null, ["callee:00c57e90:8"]]
+ 005d78ac ["INT_ADD", "register:40f0:8", ["const:5d78ac:8", "const:4:8"]]
+ 005d78ac ["CALL", null, ["callee:00c57e90:8"]]
- 005d786c bytes 89001a94
+ 005d78ac bytes 79011a94
- 005d791c ["INT_ADD", "register:40f0:8", ["const:5d791c:8", "const:4:8"]]
- 005d791c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d795c ["INT_ADD", "register:40f0:8", ["const:5d795c:8", "const:4:8"]]
+ 005d795c ["CALL", null, ["callee:00c57eb0:8"]]
- 005d791c bytes 65001a94
+ 005d795c bytes 55011a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6526dde2c12970af7cf36742755941af"></a>

### [`005d7950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7950.md) → [`005d7990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d7/005d7990.md) FUN_005d7990

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d717c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d717c.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`005d71bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d7/005d71bc.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d79c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7950.md#insn-005d79c0) · [`005d79f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7950.md#insn-005d79f8) · [`005d7aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7950.md#insn-005d7aa8)
- 新版 `005d7a00`（命令位置の公開資料なし） · `005d7a38`（命令位置の公開資料なし） · `005d7ae8`（命令位置の公開資料なし）

~~~diff
- 005d79c0 ["INT_ADD", "register:40f0:8", ["const:5d79c0:8", "const:4:8"]]
- 005d79c0 ["CALL", null, ["callee:00c57f40:8"]]
+ 005d7a00 ["INT_ADD", "register:40f0:8", ["const:5d7a00:8", "const:4:8"]]
+ 005d7a00 ["CALL", null, ["callee:00c57f40:8"]]
- 005d79c0 bytes 60001a94
+ 005d7a00 bytes 50011a94
- 005d79f8 ["INT_ADD", "register:40f0:8", ["const:5d79f8:8", "const:4:8"]]
- 005d79f8 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d7a38 ["INT_ADD", "register:40f0:8", ["const:5d7a38:8", "const:4:8"]]
+ 005d7a38 ["CALL", null, ["callee:00c57e90:8"]]
- 005d79f8 bytes 26001a94
+ 005d7a38 bytes 16011a94
- 005d7aa8 ["INT_ADD", "register:40f0:8", ["const:5d7aa8:8", "const:4:8"]]
- 005d7aa8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d7ae8 ["INT_ADD", "register:40f0:8", ["const:5d7ae8:8", "const:4:8"]]
+ 005d7ae8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005d7aa8 bytes 02001a94
+ 005d7ae8 bytes f2001a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a93f90d2adac0865eb1e254f7ae68dc8"></a>

### [`005d7adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7adc.md) → [`005d7b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d7/005d7b1c.md) FUN_005d7b1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d60d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d60d0.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005d763c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d763c.md) [`005d77c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d77c4.md) [`005d7ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7ec0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`005d6110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d6/005d6110.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005d767c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d7/005d767c.md) [`005d7804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d7/005d7804.md) [`005d7f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d7/005d7f00.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d7b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7adc.md#insn-005d7b5c) · [`005d7b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7adc.md#insn-005d7b84) · [`005d7b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7adc.md#insn-005d7b94)
- 新版 `005d7b9c`（命令位置の公開資料なし） · `005d7bc4`（命令位置の公開資料なし） · `005d7bd4`（命令位置の公開資料なし）

~~~diff
- 005d7b5c ["INT_ADD", "register:40f0:8", ["const:5d7b5c:8", "const:4:8"]]
- 005d7b5c ["CALL", null, ["callee:005d7f00:8"]]
+ 005d7b9c ["INT_ADD", "register:40f0:8", ["const:5d7b9c:8", "const:4:8"]]
+ 005d7b9c ["CALL", null, ["callee:005d7f00:8"]]
- 005d7b5c bytes d9000094
+ 005d7b9c bytes d9000094
- 005d7b84 ["INT_ADD", "register:40f0:8", ["const:5d7b84:8", "const:4:8"]]
- 005d7b84 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d7bc4 ["INT_ADD", "register:40f0:8", ["const:5d7bc4:8", "const:4:8"]]
+ 005d7bc4 ["CALL", null, ["callee:00c57e90:8"]]
- 005d7b84 bytes c3ff1994
+ 005d7bc4 bytes b3001a94
- 005d7b94 ["INT_ADD", "register:40f0:8", ["const:5d7b94:8", "const:4:8"]]
- 005d7b94 ["CALL", null, ["callee:005d7804:8"]]
+ 005d7bd4 ["INT_ADD", "register:40f0:8", ["const:5d7bd4:8", "const:4:8"]]
+ 005d7bd4 ["CALL", null, ["callee:005d7804:8"]]
- 005d7b94 bytes 0cffff97
+ 005d7bd4 bytes 0cffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b3a6399cf0f40d473de8d20a6c6964c"></a>

### [`005d7ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7ec0.md) → [`005d7f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d7/005d7f00.md) FUN_005d7f00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d7adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7adc.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`005d7b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d7/005d7b1c.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d7f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7ec0.md#insn-005d7f30) · [`005d7f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7ec0.md#insn-005d7f68) · [`005d8018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7ec0.md#insn-005d8018)
- 新版 `005d7f70`（命令位置の公開資料なし） · `005d7fa8`（命令位置の公開資料なし） · `005d8058`（命令位置の公開資料なし）

~~~diff
- 005d7f30 ["INT_ADD", "register:40f0:8", ["const:5d7f30:8", "const:4:8"]]
- 005d7f30 ["CALL", null, ["callee:00c57f40:8"]]
+ 005d7f70 ["INT_ADD", "register:40f0:8", ["const:5d7f70:8", "const:4:8"]]
+ 005d7f70 ["CALL", null, ["callee:00c57f40:8"]]
- 005d7f30 bytes 04ff1994
+ 005d7f70 bytes f4ff1994
- 005d7f68 ["INT_ADD", "register:40f0:8", ["const:5d7f68:8", "const:4:8"]]
- 005d7f68 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d7fa8 ["INT_ADD", "register:40f0:8", ["const:5d7fa8:8", "const:4:8"]]
+ 005d7fa8 ["CALL", null, ["callee:00c57e90:8"]]
- 005d7f68 bytes cafe1994
+ 005d7fa8 bytes baff1994
- 005d8018 ["INT_ADD", "register:40f0:8", ["const:5d8018:8", "const:4:8"]]
- 005d8018 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d8058 ["INT_ADD", "register:40f0:8", ["const:5d8058:8", "const:4:8"]]
+ 005d8058 ["CALL", null, ["callee:00c57eb0:8"]]
- 005d8018 bytes a6fe1994
+ 005d8058 bytes 96ff1994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df4a978e349356de3c07197699319452"></a>

### [`005d804c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d804c.md) → [`005d808c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d808c.md) FUN_005d808c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md) · 呼出先 4件 [`005cfcbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfcbc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`005d69f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d6/005d69f0.md) · 呼出先 4件 [`005cfcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cfcfc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d809c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d804c.md#insn-005d809c) · [`005d8100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d804c.md#insn-005d8100) · [`005d814c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d804c.md#insn-005d814c)
- 新版 `005d80dc`（命令位置の公開資料なし） · `005d8140`（命令位置の公開資料なし） · `005d818c`（命令位置の公開資料なし）

~~~diff
- 005d809c ["INT_ADD", "register:40f0:8", ["const:5d809c:8", "const:4:8"]]
- 005d809c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d80dc ["INT_ADD", "register:40f0:8", ["const:5d80dc:8", "const:4:8"]]
+ 005d80dc ["CALL", null, ["callee:00c57eb0:8"]]
- 005d809c bytes 85fe1994
+ 005d80dc bytes 75ff1994
- 005d8100 ["INT_ADD", "register:40f0:8", ["const:5d8100:8", "const:4:8"]]
- 005d8100 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d8140 ["INT_ADD", "register:40f0:8", ["const:5d8140:8", "const:4:8"]]
+ 005d8140 ["CALL", null, ["callee:00c57e90:8"]]
- 005d8100 bytes 64fe1994
+ 005d8140 bytes 54ff1994
- 005d814c ["INT_ADD", "register:40f0:8", ["const:5d814c:8", "const:4:8"]]
- 005d814c ["CALL", null, ["callee:00c58000:8"]]
+ 005d818c ["INT_ADD", "register:40f0:8", ["const:5d818c:8", "const:4:8"]]
+ 005d818c ["CALL", null, ["callee:00c58000:8"]]
- 005d814c bytes adfe1994
+ 005d818c bytes 9dff1994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-152a2eee1146fb65dfd33b5b3aee35ee"></a>

### [`005d8238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8238.md) → [`005d8278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8278.md) FUN_005d8278

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md) · 呼出先 4件 [`005d05fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d05fc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`005d69f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d6/005d69f0.md) · 呼出先 4件 [`005d063c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d063c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d827c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8238.md#insn-005d827c) · [`005d82c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8238.md#insn-005d82c4) · [`005d82fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8238.md#insn-005d82fc)
- 新版 `005d82bc`（命令位置の公開資料なし） · `005d8304`（命令位置の公開資料なし） · `005d833c`（命令位置の公開資料なし）

~~~diff
- 005d827c ["INT_ADD", "register:40f0:8", ["const:5d827c:8", "const:4:8"]]
- 005d827c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d82bc ["INT_ADD", "register:40f0:8", ["const:5d82bc:8", "const:4:8"]]
+ 005d82bc ["CALL", null, ["callee:00c57eb0:8"]]
- 005d827c bytes 0dfe1994
+ 005d82bc bytes fdfe1994
- 005d82c4 ["INT_ADD", "register:40f0:8", ["const:5d82c4:8", "const:4:8"]]
- 005d82c4 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d8304 ["INT_ADD", "register:40f0:8", ["const:5d8304:8", "const:4:8"]]
+ 005d8304 ["CALL", null, ["callee:00c57e90:8"]]
- 005d82c4 bytes f3fd1994
+ 005d8304 bytes e3fe1994
- 005d82fc ["INT_ADD", "register:40f0:8", ["const:5d82fc:8", "const:4:8"]]
- 005d82fc ["CALL", null, ["callee:00c58000:8"]]
+ 005d833c ["INT_ADD", "register:40f0:8", ["const:5d833c:8", "const:4:8"]]
+ 005d833c ["CALL", null, ["callee:00c58000:8"]]
- 005d82fc bytes 41fe1994
+ 005d833c bytes 31ff1994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c1fbe439b1e7ed8a69ef5b0980cc6b8"></a>

### [`005d851c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d851c.md) → [`005d855c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d855c.md) FUN_005d855c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d5f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5f14.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005d8698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8698.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`005d5f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5f54.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005d86d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d86d8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d85c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d851c.md#insn-005d85c0) · [`005d8650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d851c.md#insn-005d8650) · [`005d8690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d851c.md#insn-005d8690)
- 新版 `005d8600`（命令位置の公開資料なし） · `005d8690`（命令位置の公開資料なし） · `005d86d0`（命令位置の公開資料なし）

~~~diff
- 005d85c0 ["INT_ADD", "register:40f0:8", ["const:5d85c0:8", "const:4:8"]]
- 005d85c0 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d8600 ["INT_ADD", "register:40f0:8", ["const:5d8600:8", "const:4:8"]]
+ 005d8600 ["CALL", null, ["callee:00c57e90:8"]]
- 005d85c0 bytes 34fd1994
+ 005d8600 bytes 24fe1994
- 005d8650 ["INT_ADD", "register:40f0:8", ["const:5d8650:8", "const:4:8"]]
- 005d8650 ["CALL", null, ["callee:00c58000:8"]]
+ 005d8690 ["INT_ADD", "register:40f0:8", ["const:5d8690:8", "const:4:8"]]
+ 005d8690 ["CALL", null, ["callee:00c58000:8"]]
- 005d8650 bytes 6cfd1994
+ 005d8690 bytes 5cfe1994
- 005d8690 ["INT_ADD", "register:40f0:8", ["const:5d8690:8", "const:4:8"]]
- 005d8690 ["CALL", null, ["callee:005d86d8:8"]]
+ 005d86d0 ["INT_ADD", "register:40f0:8", ["const:5d86d0:8", "const:4:8"]]
+ 005d86d0 ["CALL", null, ["callee:005d86d8:8"]]
- 005d8690 bytes 02000094
+ 005d86d0 bytes 02000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de2a3a676df0d347232111b7c6a5556c"></a>

### [`005d86ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d86ac.md) → [`005d86ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d86ec.md) FUN_005d86ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 11件 [`005c4918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c4918.md) [`005c8ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8ebc.md) [`00687b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00687/00687b0c.md) [`00908178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00908/00908178.md) [`00963e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00963/00963e3c.md) · 呼出先 4件 [`005d8a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8a2c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a420.md)
- 新版 呼出元 11件 [`005c4958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c4/005c4958.md) [`005c8efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c8/005c8efc.md) [`00687b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00687/00687b4c.md) [`00908314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00908/00908314.md) [`00963fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00963/00963fd8.md) · 呼出先 4件 [`005d8a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8a6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a820.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d8790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d86ac.md#insn-005d8790) · [`005d882c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d86ac.md#insn-005d882c) · [`005d8848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d86ac.md#insn-005d8848)
- 新版 `005d87d0`（命令位置の公開資料なし） · `005d886c`（命令位置の公開資料なし） · `005d8888`（命令位置の公開資料なし）

~~~diff
- 005d8790 ["INT_ADD", "register:40f0:8", ["const:5d8790:8", "const:4:8"]]
- 005d8790 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d87d0 ["INT_ADD", "register:40f0:8", ["const:5d87d0:8", "const:4:8"]]
+ 005d87d0 ["CALL", null, ["callee:00c57e90:8"]]
- 005d8790 bytes c0fc1994
+ 005d87d0 bytes b0fd1994
- 005d882c ["INT_ADD", "register:40f0:8", ["const:5d882c:8", "const:4:8"]]
- 005d882c ["CALL", null, ["callee:00c5a820:8"]]
+ 005d886c ["INT_ADD", "register:40f0:8", ["const:5d886c:8", "const:4:8"]]
+ 005d886c ["CALL", null, ["callee:00c5a820:8"]]
- 005d882c bytes fd061a94
+ 005d886c bytes ed071a94
- 005d8848 ["INT_ADD", "register:40f0:8", ["const:5d8848:8", "const:4:8"]]
- 005d8848 ["CALL", null, ["callee:005d8a6c:8"]]
+ 005d8888 ["INT_ADD", "register:40f0:8", ["const:5d8888:8", "const:4:8"]]
+ 005d8888 ["CALL", null, ["callee:005d8a6c:8"]]
- 005d8848 bytes 79000094
+ 005d8888 bytes 79000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae66b765a94cc0c7266560f026df17f3"></a>

### [`005d89c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d89c0.md) → [`005d8a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8a00.md) FUN_005d8a00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d89f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d89c0.md#insn-005d89f0) · [`005d8a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d89c0.md#insn-005d8a04) · [`005d8a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d89c0.md#insn-005d8a0c)
- 新版 `005d8a30`（命令位置の公開資料なし） · `005d8a44`（命令位置の公開資料なし） · `005d8a4c`（命令位置の公開資料なし）

~~~diff
- 005d89f0 ["INT_ADD", "register:40f0:8", ["const:5d89f0:8", "const:4:8"]]
- 005d89f0 ["CALL", null, ["callee:00c53d00:8"]]
+ 005d8a30 ["INT_ADD", "register:40f0:8", ["const:5d8a30:8", "const:4:8"]]
+ 005d8a30 ["CALL", null, ["callee:00c53d00:8"]]
- 005d89f0 bytes bceb1994
+ 005d8a30 bytes b4ec1994
- 005d8a04 ["COPY", "register:0:8", ["register:4040:8"]]
- 005d8a04 ["INT_ADD", "register:40f0:8", ["const:5d8a04:8", "const:4:8"]]
- 005d8a04 ["CALLIND", null, ["register:0:8"]]
+ 005d8a44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d8a44 ["INT_ADD", "register:40f0:8", ["const:5d8a44:8", "const:4:8"]]
+ 005d8a44 ["CALLIND", null, ["register:0:8"]]
- 005d8a04 bytes 00013fd6
+ 005d8a44 bytes 00013fd6
- 005d8a0c ["INT_ADD", "register:40f0:8", ["const:5d8a0c:8", "const:4:8"]]
- 005d8a0c ["CALL", null, ["callee:00c57e80:8"]]
+ 005d8a4c ["INT_ADD", "register:40f0:8", ["const:5d8a4c:8", "const:4:8"]]
+ 005d8a4c ["CALL", null, ["callee:00c57e80:8"]]
- 005d8a0c bytes 1dfc1994
+ 005d8a4c bytes 0dfd1994
~~~


<a id="compare-2c84a08eb76a68622bc1ce2e81ebdb29"></a>

### [`005d8a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8a2c.md) → [`005d8a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8a6c.md) FUN_005d8a6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`005d86ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d86ac.md) [`006959b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/006959b0.md) [`00695b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695b6c.md) [`00695f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695f10.md) · 呼出先 3件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`005d86ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d86ec.md) [`006959f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/006959f0.md) [`00695bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695bac.md) [`00695f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695f50.md) · 呼出先 3件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d8a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8a2c.md#insn-005d8a50) · [`005d8a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8a2c.md#insn-005d8a64) · [`005d8ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8a2c.md#insn-005d8ac4)
- 新版 `005d8a90`（命令位置の公開資料なし） · `005d8aa4`（命令位置の公開資料なし） · `005d8b04`（命令位置の公開資料なし）

~~~diff
- 005d8a50 ["INT_ADD", "register:40f0:8", ["const:5d8a50:8", "const:4:8"]]
- 005d8a50 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d8a90 ["INT_ADD", "register:40f0:8", ["const:5d8a90:8", "const:4:8"]]
+ 005d8a90 ["CALL", null, ["callee:00c57e90:8"]]
- 005d8a50 bytes 10fc1994
+ 005d8a90 bytes 00fd1994
- 005d8a64 ["INT_ADD", "register:40f0:8", ["const:5d8a64:8", "const:4:8"]]
- 005d8a64 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d8aa4 ["INT_ADD", "register:40f0:8", ["const:5d8aa4:8", "const:4:8"]]
+ 005d8aa4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005d8a64 bytes 13fc1994
+ 005d8aa4 bytes 03fd1994
- 005d8ac4 ["INT_ADD", "register:40f0:8", ["const:5d8ac4:8", "const:4:8"]]
- 005d8ac4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d8b04 ["INT_ADD", "register:40f0:8", ["const:5d8b04:8", "const:4:8"]]
+ 005d8b04 ["CALL", null, ["callee:00c57eb0:8"]]
- 005d8ac4 bytes fbfb1994
+ 005d8b04 bytes ebfc1994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52661613f520f12fc74a363a5d98d751"></a>

### [`005d8c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8c24.md) → [`005d8c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8c64.md) FUN_005d8c64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`005c8ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8ebc.md) [`005d8cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8cf4.md) [`00846cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846cd0.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`005c8efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c8/005c8efc.md) [`005d8d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8d34.md) [`00846d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/00846d10.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d8c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8c24.md#insn-005d8c40) · [`005d8c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8c24.md#insn-005d8c54) · [`005d8c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8c24.md#insn-005d8c68)
- 新版 `005d8c80`（命令位置の公開資料なし） · `005d8c94`（命令位置の公開資料なし） · `005d8ca8`（命令位置の公開資料なし）

~~~diff
- 005d8c40 ["INT_ADD", "register:40f0:8", ["const:5d8c40:8", "const:4:8"]]
- 005d8c40 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d8c80 ["INT_ADD", "register:40f0:8", ["const:5d8c80:8", "const:4:8"]]
+ 005d8c80 ["CALL", null, ["callee:00c57eb0:8"]]
- 005d8c40 bytes 9cfb1994
+ 005d8c80 bytes 8cfc1994
- 005d8c54 ["INT_ADD", "register:40f0:8", ["const:5d8c54:8", "const:4:8"]]
- 005d8c54 ["CALL", null, ["callee:00c53d00:8"]]
+ 005d8c94 ["INT_ADD", "register:40f0:8", ["const:5d8c94:8", "const:4:8"]]
+ 005d8c94 ["CALL", null, ["callee:00c53d00:8"]]
- 005d8c54 bytes 23eb1994
+ 005d8c94 bytes 1bec1994
- 005d8c68 ["COPY", "register:0:8", ["register:4040:8"]]
- 005d8c68 ["INT_ADD", "register:40f0:8", ["const:5d8c68:8", "const:4:8"]]
- 005d8c68 ["CALLIND", null, ["register:0:8"]]
+ 005d8ca8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d8ca8 ["INT_ADD", "register:40f0:8", ["const:5d8ca8:8", "const:4:8"]]
+ 005d8ca8 ["CALLIND", null, ["register:0:8"]]
- 005d8c68 bytes 00013fd6
+ 005d8ca8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f823ef1656e4ef7c9eed5239d4677ec2"></a>

### [`005d8cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8cf4.md) → [`005d8d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8d34.md) FUN_005d8d34

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005c8ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8ebc.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005d8c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8c24.md) [`005d8edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8edc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005c8efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c8/005c8efc.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005d8c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8c64.md) [`005d8f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8f1c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d8d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8cf4.md#insn-005d8d94) · [`005d8e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8cf4.md#insn-005d8e90) · [`005d8eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8cf4.md#insn-005d8eb4)
- 新版 `005d8dd4`（命令位置の公開資料なし） · `005d8ed0`（命令位置の公開資料なし） · `005d8ef4`（命令位置の公開資料なし）

~~~diff
- 005d8d94 ["INT_ADD", "register:40f0:8", ["const:5d8d94:8", "const:4:8"]]
- 005d8d94 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d8dd4 ["INT_ADD", "register:40f0:8", ["const:5d8dd4:8", "const:4:8"]]
+ 005d8dd4 ["CALL", null, ["callee:00c57e90:8"]]
- 005d8d94 bytes 3ffb1994
+ 005d8dd4 bytes 2ffc1994
- 005d8e90 ["INT_ADD", "register:40f0:8", ["const:5d8e90:8", "const:4:8"]]
- 005d8e90 ["CALL", null, ["callee:005d8c64:8"]]
+ 005d8ed0 ["INT_ADD", "register:40f0:8", ["const:5d8ed0:8", "const:4:8"]]
+ 005d8ed0 ["CALL", null, ["callee:005d8c64:8"]]
- 005d8e90 bytes 65ffff97
+ 005d8ed0 bytes 65ffff97
- 005d8eb4 ["INT_ADD", "register:40f0:8", ["const:5d8eb4:8", "const:4:8"]]
- 005d8eb4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d8ef4 ["INT_ADD", "register:40f0:8", ["const:5d8ef4:8", "const:4:8"]]
+ 005d8ef4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005d8eb4 bytes fffa1994
+ 005d8ef4 bytes effb1994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f54e312fb7feaf9ef1838cd0e32190a1"></a>

### [`005d9a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9a34.md) → [`005d9a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d9/005d9a74.md) FUN_005d9a74

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d8f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8f44.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`005d9cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9cc4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005d8f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8f84.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005d9d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d9/005d9d04.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d9a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9a34.md#insn-005d9a80) · [`005d9ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9a34.md#insn-005d9ab0) · [`005d9ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9a34.md#insn-005d9ac4)
- 新版 `005d9ac0`（命令位置の公開資料なし） · `005d9af0`（命令位置の公開資料なし） · `005d9b04`（命令位置の公開資料なし）

~~~diff
- 005d9a80 ["INT_ADD", "register:40f0:8", ["const:5d9a80:8", "const:4:8"]]
- 005d9a80 ["CALL", null, ["callee:0043bba4:8"]]
+ 005d9ac0 ["INT_ADD", "register:40f0:8", ["const:5d9ac0:8", "const:4:8"]]
+ 005d9ac0 ["CALL", null, ["callee:0043bba4:8"]]
- 005d9a80 bytes 3988f997
+ 005d9ac0 bytes 3988f997
- 005d9ab0 ["INT_ADD", "register:40f0:8", ["const:5d9ab0:8", "const:4:8"]]
- 005d9ab0 ["CALL", null, ["callee:005d9d04:8"]]
+ 005d9af0 ["INT_ADD", "register:40f0:8", ["const:5d9af0:8", "const:4:8"]]
+ 005d9af0 ["CALL", null, ["callee:005d9d04:8"]]
- 005d9ab0 bytes 85000094
+ 005d9af0 bytes 85000094
- 005d9ac4 ["INT_ADD", "register:40f0:8", ["const:5d9ac4:8", "const:4:8"]]
- 005d9ac4 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d9b04 ["INT_ADD", "register:40f0:8", ["const:5d9b04:8", "const:4:8"]]
+ 005d9b04 ["CALL", null, ["callee:00c57e90:8"]]
- 005d9ac4 bytes f3f71994
+ 005d9b04 bytes e3f81994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b657b7170c9e89f8894b2217b064cf62"></a>

### [`005d9b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9b50.md) → [`005d9b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d9/005d9b90.md) FUN_005d9b90

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d8f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8f44.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`005d8f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8f84.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d9bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9b50.md#insn-005d9bb8) · [`005d9bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9b50.md#insn-005d9bec)
- 新版 `005d9bf8`（命令位置の公開資料なし） · `005d9c2c`（命令位置の公開資料なし）

~~~diff
- 005d9bb8 ["INT_ADD", "register:40f0:8", ["const:5d9bb8:8", "const:4:8"]]
- 005d9bb8 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d9bf8 ["INT_ADD", "register:40f0:8", ["const:5d9bf8:8", "const:4:8"]]
+ 005d9bf8 ["CALL", null, ["callee:00c57e90:8"]]
- 005d9bb8 bytes b6f71994
+ 005d9bf8 bytes a6f81994
- 005d9bec ["INT_ADD", "register:40f0:8", ["const:5d9bec:8", "const:4:8"]]
- 005d9bec ["CALL", null, ["callee:0043bba4:8"]]
+ 005d9c2c ["INT_ADD", "register:40f0:8", ["const:5d9c2c:8", "const:4:8"]]
+ 005d9c2c ["CALL", null, ["callee:0043bba4:8"]]
- 005d9bec bytes de87f997
+ 005d9c2c bytes de87f997
~~~


<a id="compare-9cd87669933973eaf261956058afe2a8"></a>

### [`005d9e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9e6c.md) → [`005d9eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d9/005d9eac.md) FUN_005d9eac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005d8f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8f44.md) [`005d9e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9e6c.md) · 呼出先 2件 [`005d9e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9e6c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`005d8f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8f84.md) [`005d9eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d9/005d9eac.md) · 呼出先 2件 [`005d9eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d9/005d9eac.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d9e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9e6c.md#insn-005d9e8c) · [`005d9e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9e6c.md#insn-005d9e98)
- 新版 `005d9ecc`（命令位置の公開資料なし） · `005d9ed8`（命令位置の公開資料なし）

~~~diff
- 005d9e8c ["INT_ADD", "register:40f0:8", ["const:5d9e8c:8", "const:4:8"]]
- 005d9e8c ["CALL", null, ["local:b0:8"]]
+ 005d9ecc ["INT_ADD", "register:40f0:8", ["const:5d9ecc:8", "const:4:8"]]
+ 005d9ecc ["CALL", null, ["local:b0:8"]]
- 005d9e8c bytes f8ffff97
+ 005d9ecc bytes f8ffff97
- 005d9e98 ["INT_ADD", "register:40f0:8", ["const:5d9e98:8", "const:4:8"]]
- 005d9e98 ["CALL", null, ["local:b0:8"]]
+ 005d9ed8 ["INT_ADD", "register:40f0:8", ["const:5d9ed8:8", "const:4:8"]]
+ 005d9ed8 ["CALL", null, ["local:b0:8"]]
- 005d9e98 bytes f5ffff97
+ 005d9ed8 bytes f5ffff97
~~~


<a id="compare-4b57f7c7401e91129fe5896bd7decaa1"></a>

### [`005da544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005da544.md) → [`005da584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005da/005da584.md) FUN_005da584

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 26件 [`005d9f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9f0c.md) [`005e1b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1b78.md) [`006ab344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ab/006ab344.md) [`006ff600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff600.md) [`00749994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00749/00749994.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`005da66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005da66c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 26件 [`005d9f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d9/005d9f4c.md) [`005e1bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1bb8.md) [`006ab384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ab/006ab384.md) [`006ff640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff640.md) [`007499d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00749/007499d4.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005da6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005da/005da6ac.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005da598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005da544.md#insn-005da598) · [`005da5ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005da544.md#insn-005da5ac) · [`005da5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005da544.md#insn-005da5dc)
- 新版 `005da5d8`（命令位置の公開資料なし） · `005da5ec`（命令位置の公開資料なし） · `005da61c`（命令位置の公開資料なし）

~~~diff
- 005da598 ["INT_ADD", "register:40f0:8", ["const:5da598:8", "const:4:8"]]
- 005da598 ["CALL", null, ["callee:0043bb20:8"]]
+ 005da5d8 ["INT_ADD", "register:40f0:8", ["const:5da5d8:8", "const:4:8"]]
+ 005da5d8 ["CALL", null, ["callee:0043bb20:8"]]
- 005da598 bytes 5285f997
+ 005da5d8 bytes 5285f997
- 005da5ac ["INT_ADD", "register:40f0:8", ["const:5da5ac:8", "const:4:8"]]
- 005da5ac ["CALL", null, ["callee:0043bb20:8"]]
+ 005da5ec ["INT_ADD", "register:40f0:8", ["const:5da5ec:8", "const:4:8"]]
+ 005da5ec ["CALL", null, ["callee:0043bb20:8"]]
- 005da5ac bytes 4d85f997
+ 005da5ec bytes 4d85f997
- 005da5dc ["INT_ADD", "register:40f0:8", ["const:5da5dc:8", "const:4:8"]]
- 005da5dc ["CALL", null, ["callee:005da6ac:8"]]
+ 005da61c ["INT_ADD", "register:40f0:8", ["const:5da61c:8", "const:4:8"]]
+ 005da61c ["CALL", null, ["callee:005da6ac:8"]]
- 005da5dc bytes 24000094
+ 005da61c bytes 24000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be36cd6f495c58e474075d7665998d7a"></a>

### [`005dbcd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbcd4.md) → [`005dbd14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005db/005dbd14.md) FUN_005dbd14

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`005db880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db880.md) [`007728a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00772/007728a0.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044998c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/0044998c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 8件 [`005db8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005db/005db8c0.md) [`007728e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00772/007728e0.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00851a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851a0c.md) [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004499cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00449/004499cc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005dbd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbcd4.md#insn-005dbd30) · [`005dbd44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbcd4.md#insn-005dbd44) · [`005dbd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbcd4.md#insn-005dbd78)
- 新版 `005dbd70`（命令位置の公開資料なし） · `005dbd84`（命令位置の公開資料なし） · `005dbdb8`（命令位置の公開資料なし）

~~~diff
- 005dbd30 ["INT_ADD", "register:40f0:8", ["const:5dbd30:8", "const:4:8"]]
- 005dbd30 ["CALL", null, ["callee:0043bb20:8"]]
+ 005dbd70 ["INT_ADD", "register:40f0:8", ["const:5dbd70:8", "const:4:8"]]
+ 005dbd70 ["CALL", null, ["callee:0043bb20:8"]]
- 005dbd30 bytes 6c7ff997
+ 005dbd70 bytes 6c7ff997
- 005dbd44 ["INT_ADD", "register:40f0:8", ["const:5dbd44:8", "const:4:8"]]
- 005dbd44 ["CALL", null, ["callee:0043bb20:8"]]
+ 005dbd84 ["INT_ADD", "register:40f0:8", ["const:5dbd84:8", "const:4:8"]]
+ 005dbd84 ["CALL", null, ["callee:0043bb20:8"]]
- 005dbd44 bytes 677ff997
+ 005dbd84 bytes 677ff997
- 005dbd78 ["INT_ADD", "register:40f0:8", ["const:5dbd78:8", "const:4:8"]]
- 005dbd78 ["CALL", null, ["callee:004499cc:8"]]
+ 005dbdb8 ["INT_ADD", "register:40f0:8", ["const:5dbdb8:8", "const:4:8"]]
+ 005dbdb8 ["CALL", null, ["callee:004499cc:8"]]
- 005dbd78 bytes 05b7f997
+ 005dbdb8 bytes 05b7f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bf7cfa0f891505366879c6a0eae40b1"></a>

### [`005dcd4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dcd4c.md) → [`005dcd8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005dc/005dcd8c.md) FUN_005dcd8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005e9094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e9/005e9094.md) [`005ec234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ec/005ec234.md) · 呼出先 3件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005dd710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dd/005dd710.md) [`005dda60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dd/005dda60.md)
- 新版 呼出元 2件 [`005e90d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e9/005e90d4.md) [`005ec274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ec/005ec274.md) · 呼出先 3件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005dd750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005dd/005dd750.md) [`005ddaa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005dd/005ddaa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005dcd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dcd4c.md#insn-005dcd78) · [`005dcdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dcd4c.md#insn-005dcdb0) · [`005dcdec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dcd4c.md#insn-005dcdec)
- 新版 `005dcdb8`（命令位置の公開資料なし） · `005dcdf0`（命令位置の公開資料なし） · `005dce2c`（命令位置の公開資料なし）

~~~diff
- 005dcd78 ["INT_ADD", "register:40f0:8", ["const:5dcd78:8", "const:4:8"]]
- 005dcd78 ["CALL", null, ["callee:005c179c:8"]]
+ 005dcdb8 ["INT_ADD", "register:40f0:8", ["const:5dcdb8:8", "const:4:8"]]
+ 005dcdb8 ["CALL", null, ["callee:005c179c:8"]]
- 005dcd78 bytes 7992ff97
+ 005dcdb8 bytes 7992ff97
- 005dcdb0 ["INT_ADD", "register:40f0:8", ["const:5dcdb0:8", "const:4:8"]]
- 005dcdb0 ["CALL", null, ["callee:005dd750:8"]]
+ 005dcdf0 ["INT_ADD", "register:40f0:8", ["const:5dcdf0:8", "const:4:8"]]
+ 005dcdf0 ["CALL", null, ["callee:005dd750:8"]]
- 005dcdb0 bytes 58020094
+ 005dcdf0 bytes 58020094
- 005dcdec ["INT_ADD", "register:40f0:8", ["const:5dcdec:8", "const:4:8"]]
- 005dcdec ["CALL", null, ["callee:005ddaa0:8"]]
+ 005dce2c ["INT_ADD", "register:40f0:8", ["const:5dce2c:8", "const:4:8"]]
+ 005dce2c ["CALL", null, ["callee:005ddaa0:8"]]
- 005dcdec bytes 1d030094
+ 005dce2c bytes 1d030094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec36a07dd8d13127eebce7826c663338"></a>

### [`005de470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005de/005de470.md) → [`005de4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005de/005de4b0.md) FUN_005de4b0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005ddde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dd/005ddde8.md) · 呼出先 5件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`005dca68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dca68.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005dde28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005dd/005dde28.md) · 呼出先 5件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`005dcaa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005dc/005dcaa8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005de4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005de/005de470.md#insn-005de4cc) · [`005de4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005de/005de470.md#insn-005de4f4) · [`005de520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005de/005de470.md#insn-005de520)
- 新版 `005de50c`（命令位置の公開資料なし） · `005de534`（命令位置の公開資料なし） · `005de560`（命令位置の公開資料なし）

~~~diff
- 005de4cc ["INT_ADD", "register:40f0:8", ["const:5de4cc:8", "const:4:8"]]
- 005de4cc ["CALL", null, ["callee:0044108c:8"]]
+ 005de50c ["INT_ADD", "register:40f0:8", ["const:5de50c:8", "const:4:8"]]
+ 005de50c ["CALL", null, ["callee:0044108c:8"]]
- 005de4cc bytes e08af997
+ 005de50c bytes e08af997
- 005de4f4 ["INT_ADD", "register:40f0:8", ["const:5de4f4:8", "const:4:8"]]
- 005de4f4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005de534 ["INT_ADD", "register:40f0:8", ["const:5de534:8", "const:4:8"]]
+ 005de534 ["CALL", null, ["callee:00c57eb0:8"]]
- 005de4f4 bytes 6fe51994
+ 005de534 bytes 5fe61994
- 005de520 ["INT_ADD", "register:40f0:8", ["const:5de520:8", "const:4:8"]]
- 005de520 ["CALL", null, ["callee:0044108c:8"]]
+ 005de560 ["INT_ADD", "register:40f0:8", ["const:5de560:8", "const:4:8"]]
+ 005de560 ["CALL", null, ["callee:0044108c:8"]]
- 005de520 bytes cb8af997
+ 005de560 bytes cb8af997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-525fb358c6f0d30f9f61851c4033fded"></a>

### [`005df58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df58c.md) → [`005df5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005df/005df5cc.md) FUN_005df5cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`005df094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df094.md) [`005df78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df78c.md) [`005e94b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e9/005e94b4.md) [`005eda3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005eda3c.md) [`005ee590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ee/005ee590.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 7件 [`005df0d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005df/005df0d4.md) [`005df7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005df/005df7cc.md) [`005e94f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e9/005e94f4.md) [`005eda7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005eda7c.md) [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005df610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df58c.md#insn-005df610) · [`005df63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df58c.md#insn-005df63c)
- 新版 `005df650`（命令位置の公開資料なし） · `005df67c`（命令位置の公開資料なし）

~~~diff
- 005df610 ["INT_ADD", "register:40f0:8", ["const:5df610:8", "const:4:8"]]
- 005df610 ["CALL", null, ["callee:00c58050:8"]]
+ 005df650 ["INT_ADD", "register:40f0:8", ["const:5df650:8", "const:4:8"]]
+ 005df650 ["CALL", null, ["callee:00c58050:8"]]
- 005df610 bytes 90e11994
+ 005df650 bytes 80e21994
- 005df63c ["INT_ADD", "register:40f0:8", ["const:5df63c:8", "const:4:8"]]
- 005df63c ["CALL", null, ["callee:00c58050:8"]]
+ 005df67c ["INT_ADD", "register:40f0:8", ["const:5df67c:8", "const:4:8"]]
+ 005df67c ["CALL", null, ["callee:00c58050:8"]]
- 005df63c bytes 85e11994
+ 005df67c bytes 75e21994
~~~


<a id="compare-cb2c2480373b19464e70ac2bd0e55d4d"></a>

### [`005df690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df690.md) → [`005df6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005df/005df6d0.md) FUN_005df6d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`005df094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df094.md) [`005df78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df78c.md) [`005e94b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e9/005e94b4.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0046e784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 4件 [`005df0d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005df/005df0d4.md) [`005df7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005df/005df7cc.md) [`005e94f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e9/005e94f4.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005df6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df690.md#insn-005df6b0) · [`005df6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df690.md#insn-005df6e8) · [`005df6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df690.md#insn-005df6f0)
- 新版 `005df6f0`（命令位置の公開資料なし） · `005df728`（命令位置の公開資料なし） · `005df730`（命令位置の公開資料なし）

~~~diff
- 005df6b0 ["INT_ADD", "register:40f0:8", ["const:5df6b0:8", "const:4:8"]]
- 005df6b0 ["CALL", null, ["callee:00c57e90:8"]]
+ 005df6f0 ["INT_ADD", "register:40f0:8", ["const:5df6f0:8", "const:4:8"]]
+ 005df6f0 ["CALL", null, ["callee:00c57e90:8"]]
- 005df6b0 bytes f8e01994
+ 005df6f0 bytes e8e11994
- 005df6e8 ["INT_ADD", "register:40f0:8", ["const:5df6e8:8", "const:4:8"]]
- 005df6e8 ["CALL", null, ["callee:0043bb20:8"]]
+ 005df728 ["INT_ADD", "register:40f0:8", ["const:5df728:8", "const:4:8"]]
+ 005df728 ["CALL", null, ["callee:0043bb20:8"]]
- 005df6e8 bytes fe70f997
+ 005df728 bytes fe70f997
- 005df6f0 ["INT_ADD", "register:40f0:8", ["const:5df6f0:8", "const:4:8"]]
- 005df6f0 ["CALL", null, ["callee:0046e7c4:8"]]
+ 005df730 ["INT_ADD", "register:40f0:8", ["const:5df730:8", "const:4:8"]]
+ 005df730 ["CALL", null, ["callee:0046e7c4:8"]]
- 005df6f0 bytes 253cfa97
+ 005df730 bytes 253cfa97
~~~


<a id="compare-53a6101f1213596ed265a986ecd4dbbf"></a>

### [`005df738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df738.md) → [`005df778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005df/005df778.md) FUN_005df778

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005df75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df738.md#insn-005df75c) · [`005df76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df738.md#insn-005df76c)
- 新版 `005df79c`（命令位置の公開資料なし） · `005df7ac`（命令位置の公開資料なし）

~~~diff
- 005df75c ["INT_ADD", "register:40f0:8", ["const:5df75c:8", "const:4:8"]]
- 005df75c ["CALL", null, ["callee:0046e8a4:8"]]
+ 005df79c ["INT_ADD", "register:40f0:8", ["const:5df79c:8", "const:4:8"]]
+ 005df79c ["CALL", null, ["callee:0046e8a4:8"]]
- 005df75c bytes 423cfa97
+ 005df79c bytes 423cfa97
- 005df76c ["INT_ADD", "register:40f0:8", ["const:5df76c:8", "const:4:8"]]
- 005df76c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005df7ac ["INT_ADD", "register:40f0:8", ["const:5df7ac:8", "const:4:8"]]
+ 005df7ac ["CALL", null, ["callee:00c57eb0:8"]]
- 005df76c bytes d1e01994
+ 005df7ac bytes c1e11994
~~~


<a id="compare-2be7ea436dd8a3be393594b999fc7080"></a>

### [`005e0034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0034.md) → [`005e0074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0074.md) FUN_005e0074

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) · 呼出先 1件 [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md)
- 新版 呼出元 1件 [`00a1a750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a750.md) · 呼出先 1件 [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e004c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0034.md#insn-005e004c) · [`005e0058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0034.md#insn-005e0058) · [`005e0064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0034.md#insn-005e0064)
- 新版 `005e008c`（命令位置の公開資料なし） · `005e0098`（命令位置の公開資料なし） · `005e00a4`（命令位置の公開資料なし）

~~~diff
- 005e004c ["INT_ADD", "register:40f0:8", ["const:5e004c:8", "const:4:8"]]
- 005e004c ["CALL", null, ["callee:004803f0:8"]]
+ 005e008c ["INT_ADD", "register:40f0:8", ["const:5e008c:8", "const:4:8"]]
+ 005e008c ["CALL", null, ["callee:004803f0:8"]]
- 005e004c bytes d980fa97
+ 005e008c bytes d980fa97
- 005e0058 ["INT_ADD", "register:40f0:8", ["const:5e0058:8", "const:4:8"]]
- 005e0058 ["CALL", null, ["callee:004803f0:8"]]
+ 005e0098 ["INT_ADD", "register:40f0:8", ["const:5e0098:8", "const:4:8"]]
+ 005e0098 ["CALL", null, ["callee:004803f0:8"]]
- 005e0058 bytes d680fa97
+ 005e0098 bytes d680fa97
- 005e0064 ["INT_ADD", "register:40f0:8", ["const:5e0064:8", "const:4:8"]]
- 005e0064 ["CALL", null, ["callee:004803f0:8"]]
+ 005e00a4 ["INT_ADD", "register:40f0:8", ["const:5e00a4:8", "const:4:8"]]
+ 005e00a4 ["CALL", null, ["callee:004803f0:8"]]
- 005e0064 bytes d380fa97
+ 005e00a4 bytes d380fa97
~~~


<a id="compare-b3195f0fcb8ee7bbf6f09b33d97ddb95"></a>

### [`005e0078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0078.md) → [`005e00b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e00b8.md) FUN_005e00b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) · 呼出先 1件 [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md)
- 新版 呼出元 1件 [`00a1a750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a750.md) · 呼出先 1件 [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e0090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0078.md#insn-005e0090) · [`005e009c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0078.md#insn-005e009c) · [`005e00a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0078.md#insn-005e00a8)
- 新版 `005e00d0`（命令位置の公開資料なし） · `005e00dc`（命令位置の公開資料なし） · `005e00e8`（命令位置の公開資料なし）

~~~diff
- 005e0090 ["INT_ADD", "register:40f0:8", ["const:5e0090:8", "const:4:8"]]
- 005e0090 ["CALL", null, ["callee:004803f0:8"]]
+ 005e00d0 ["INT_ADD", "register:40f0:8", ["const:5e00d0:8", "const:4:8"]]
+ 005e00d0 ["CALL", null, ["callee:004803f0:8"]]
- 005e0090 bytes c880fa97
+ 005e00d0 bytes c880fa97
- 005e009c ["INT_ADD", "register:40f0:8", ["const:5e009c:8", "const:4:8"]]
- 005e009c ["CALL", null, ["callee:004803f0:8"]]
+ 005e00dc ["INT_ADD", "register:40f0:8", ["const:5e00dc:8", "const:4:8"]]
+ 005e00dc ["CALL", null, ["callee:004803f0:8"]]
- 005e009c bytes c580fa97
+ 005e00dc bytes c580fa97
- 005e00a8 ["INT_ADD", "register:40f0:8", ["const:5e00a8:8", "const:4:8"]]
- 005e00a8 ["CALL", null, ["callee:004803f0:8"]]
+ 005e00e8 ["INT_ADD", "register:40f0:8", ["const:5e00e8:8", "const:4:8"]]
+ 005e00e8 ["CALL", null, ["callee:004803f0:8"]]
- 005e00a8 bytes c280fa97
+ 005e00e8 bytes c280fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcac57c362c6683030d29d6629cd4b78"></a>

### [`005e00c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e00c8.md) → [`005e0108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0108.md) FUN_005e0108

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a22234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a22/00a22234.md) · 呼出先 1件 [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md)
- 新版 呼出元 1件 [`00a223d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a22/00a223d0.md) · 呼出先 1件 [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e00e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e00c8.md#insn-005e00e8) · [`005e00f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e00c8.md#insn-005e00f4) · [`005e0100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e00c8.md#insn-005e0100)
- 新版 `005e0128`（命令位置の公開資料なし） · `005e0134`（命令位置の公開資料なし） · `005e0140`（命令位置の公開資料なし）

~~~diff
- 005e00e8 ["INT_ADD", "register:40f0:8", ["const:5e00e8:8", "const:4:8"]]
- 005e00e8 ["CALL", null, ["callee:00480e28:8"]]
+ 005e0128 ["INT_ADD", "register:40f0:8", ["const:5e0128:8", "const:4:8"]]
+ 005e0128 ["CALL", null, ["callee:00480e28:8"]]
- 005e00e8 bytes 4083fa97
+ 005e0128 bytes 4083fa97
- 005e00f4 ["INT_ADD", "register:40f0:8", ["const:5e00f4:8", "const:4:8"]]
- 005e00f4 ["CALL", null, ["callee:00480e28:8"]]
+ 005e0134 ["INT_ADD", "register:40f0:8", ["const:5e0134:8", "const:4:8"]]
+ 005e0134 ["CALL", null, ["callee:00480e28:8"]]
- 005e00f4 bytes 3d83fa97
+ 005e0134 bytes 3d83fa97
- 005e0100 ["INT_ADD", "register:40f0:8", ["const:5e0100:8", "const:4:8"]]
- 005e0100 ["CALL", null, ["callee:00480e28:8"]]
+ 005e0140 ["INT_ADD", "register:40f0:8", ["const:5e0140:8", "const:4:8"]]
+ 005e0140 ["CALL", null, ["callee:00480e28:8"]]
- 005e0100 bytes 3a83fa97
+ 005e0140 bytes 3a83fa97
~~~


<a id="compare-22af331e11696c32d20fea0f5f26ead6"></a>

### [`005e0124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0124.md) → [`005e0164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0164.md) FUN_005e0164

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) · 呼出先 1件 [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md)
- 新版 呼出元 1件 [`00a1a750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a750.md) · 呼出先 1件 [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e013c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0124.md#insn-005e013c) · [`005e0148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0124.md#insn-005e0148) · [`005e0154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0124.md#insn-005e0154)
- 新版 `005e017c`（命令位置の公開資料なし） · `005e0188`（命令位置の公開資料なし） · `005e0194`（命令位置の公開資料なし）

~~~diff
- 005e013c ["INT_ADD", "register:40f0:8", ["const:5e013c:8", "const:4:8"]]
- 005e013c ["CALL", null, ["callee:004803f0:8"]]
+ 005e017c ["INT_ADD", "register:40f0:8", ["const:5e017c:8", "const:4:8"]]
+ 005e017c ["CALL", null, ["callee:004803f0:8"]]
- 005e013c bytes 9d80fa97
+ 005e017c bytes 9d80fa97
- 005e0148 ["INT_ADD", "register:40f0:8", ["const:5e0148:8", "const:4:8"]]
- 005e0148 ["CALL", null, ["callee:004803f0:8"]]
+ 005e0188 ["INT_ADD", "register:40f0:8", ["const:5e0188:8", "const:4:8"]]
+ 005e0188 ["CALL", null, ["callee:004803f0:8"]]
- 005e0148 bytes 9a80fa97
+ 005e0188 bytes 9a80fa97
- 005e0154 ["INT_ADD", "register:40f0:8", ["const:5e0154:8", "const:4:8"]]
- 005e0154 ["CALL", null, ["callee:004803f0:8"]]
+ 005e0194 ["INT_ADD", "register:40f0:8", ["const:5e0194:8", "const:4:8"]]
+ 005e0194 ["CALL", null, ["callee:004803f0:8"]]
- 005e0154 bytes 9780fa97
+ 005e0194 bytes 9780fa97
~~~


<a id="compare-2a3d317e30989f22324b4ba1d07305d5"></a>

### [`005e0168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0168.md) → [`005e01a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e01a8.md) FUN_005e01a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a22234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a22/00a22234.md) · 呼出先 1件 [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md)
- 新版 呼出元 1件 [`00a223d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a22/00a223d0.md) · 呼出先 1件 [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e0188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0168.md#insn-005e0188) · [`005e0194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0168.md#insn-005e0194)
- 新版 `005e01c8`（命令位置の公開資料なし） · `005e01d4`（命令位置の公開資料なし）

~~~diff
- 005e0188 ["INT_ADD", "register:40f0:8", ["const:5e0188:8", "const:4:8"]]
- 005e0188 ["CALL", null, ["callee:00480e28:8"]]
+ 005e01c8 ["INT_ADD", "register:40f0:8", ["const:5e01c8:8", "const:4:8"]]
+ 005e01c8 ["CALL", null, ["callee:00480e28:8"]]
- 005e0188 bytes 1883fa97
+ 005e01c8 bytes 1883fa97
- 005e0194 ["INT_ADD", "register:40f0:8", ["const:5e0194:8", "const:4:8"]]
- 005e0194 ["CALL", null, ["callee:00480e28:8"]]
+ 005e01d4 ["INT_ADD", "register:40f0:8", ["const:5e01d4:8", "const:4:8"]]
+ 005e01d4 ["CALL", null, ["callee:00480e28:8"]]
- 005e0194 bytes 1583fa97
+ 005e01d4 bytes 1583fa97
~~~


<a id="compare-fb5d2ad5b8ad8cd280e78c70b4a0b661"></a>

### [`005e01bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e01bc.md) → [`005e01fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e01fc.md) FUN_005e01fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) · 呼出先 1件 [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md)
- 新版 呼出元 1件 [`00a1a750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a750.md) · 呼出先 1件 [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e01d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e01bc.md#insn-005e01d4) · [`005e01e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e01bc.md#insn-005e01e8) · [`005e01f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e01bc.md#insn-005e01f4)
- 新版 `005e0214`（命令位置の公開資料なし） · `005e0228`（命令位置の公開資料なし） · `005e0234`（命令位置の公開資料なし）

~~~diff
- 005e01d4 ["INT_ADD", "register:40f0:8", ["const:5e01d4:8", "const:4:8"]]
- 005e01d4 ["CALL", null, ["callee:004803f0:8"]]
+ 005e0214 ["INT_ADD", "register:40f0:8", ["const:5e0214:8", "const:4:8"]]
+ 005e0214 ["CALL", null, ["callee:004803f0:8"]]
- 005e01d4 bytes 7780fa97
+ 005e0214 bytes 7780fa97
- 005e01e8 ["INT_ADD", "register:40f0:8", ["const:5e01e8:8", "const:4:8"]]
- 005e01e8 ["CALL", null, ["callee:004803f0:8"]]
+ 005e0228 ["INT_ADD", "register:40f0:8", ["const:5e0228:8", "const:4:8"]]
+ 005e0228 ["CALL", null, ["callee:004803f0:8"]]
- 005e01e8 bytes 7280fa97
+ 005e0228 bytes 7280fa97
- 005e01f4 ["INT_ADD", "register:40f0:8", ["const:5e01f4:8", "const:4:8"]]
- 005e01f4 ["CALL", null, ["callee:004803f0:8"]]
+ 005e0234 ["INT_ADD", "register:40f0:8", ["const:5e0234:8", "const:4:8"]]
+ 005e0234 ["CALL", null, ["callee:004803f0:8"]]
- 005e01f4 bytes 6f80fa97
+ 005e0234 bytes 6f80fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cabb4edd79ecc49dc23d78f1bca2c59"></a>

### [`005e0214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0214.md) → [`005e0254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0254.md) FUN_005e0254

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a22234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a22/00a22234.md) · 呼出先 1件 [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md)
- 新版 呼出元 1件 [`00a223d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a22/00a223d0.md) · 呼出先 1件 [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e0234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0214.md#insn-005e0234) · [`005e0240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0214.md#insn-005e0240) · [`005e024c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0214.md#insn-005e024c)
- 新版 `005e0274`（命令位置の公開資料なし） · `005e0280`（命令位置の公開資料なし） · `005e028c`（命令位置の公開資料なし）

~~~diff
- 005e0234 ["INT_ADD", "register:40f0:8", ["const:5e0234:8", "const:4:8"]]
- 005e0234 ["CALL", null, ["callee:00480e28:8"]]
+ 005e0274 ["INT_ADD", "register:40f0:8", ["const:5e0274:8", "const:4:8"]]
+ 005e0274 ["CALL", null, ["callee:00480e28:8"]]
- 005e0234 bytes ed82fa97
+ 005e0274 bytes ed82fa97
- 005e0240 ["INT_ADD", "register:40f0:8", ["const:5e0240:8", "const:4:8"]]
- 005e0240 ["CALL", null, ["callee:00480e28:8"]]
+ 005e0280 ["INT_ADD", "register:40f0:8", ["const:5e0280:8", "const:4:8"]]
+ 005e0280 ["CALL", null, ["callee:00480e28:8"]]
- 005e0240 bytes ea82fa97
+ 005e0280 bytes ea82fa97
- 005e024c ["INT_ADD", "register:40f0:8", ["const:5e024c:8", "const:4:8"]]
- 005e024c ["CALL", null, ["callee:00480e28:8"]]
+ 005e028c ["INT_ADD", "register:40f0:8", ["const:5e028c:8", "const:4:8"]]
+ 005e028c ["CALL", null, ["callee:00480e28:8"]]
- 005e024c bytes e782fa97
+ 005e028c bytes e782fa97
~~~


<a id="compare-cf0231dfe06dad5ea4703e1553269ef2"></a>

### [`005e0870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0870.md) → [`005e08b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e08b0.md) FUN_005e08b0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) [`00a6aa44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6aa44.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 4件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) [`00a6ac3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6ac3c.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e0878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0870.md#insn-005e0878)
- 新版 `005e08b8`（命令位置の公開資料なし）

~~~diff
- 005e0878 ["INT_ADD", "register:40f0:8", ["const:5e0878:8", "const:4:8"]]
- 005e0878 ["CALL", null, ["callee:008514f8:8"]]
+ 005e08b8 ["INT_ADD", "register:40f0:8", ["const:5e08b8:8", "const:4:8"]]
+ 005e08b8 ["CALL", null, ["callee:008514f8:8"]]
- 005e0878 bytes 10c30994
+ 005e08b8 bytes 10c30994
~~~


<a id="compare-f98d48bce3270eafc0566e26a06affe4"></a>

### [`005e0898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0898.md) → [`005e08d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e08d8.md) FUN_005e08d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`007078ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/007078ec.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`0071931c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00719/0071931c.md) [`009d5b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d5/009d5b5c.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 7件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`0070792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/0070792c.md) [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`0071935c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00719/0071935c.md) [`009d5cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d5/009d5cf8.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e08a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0898.md#insn-005e08a0)
- 新版 `005e08e0`（命令位置の公開資料なし）

~~~diff
- 005e08a0 ["INT_ADD", "register:40f0:8", ["const:5e08a0:8", "const:4:8"]]
- 005e08a0 ["CALL", null, ["callee:008514f8:8"]]
+ 005e08e0 ["INT_ADD", "register:40f0:8", ["const:5e08e0:8", "const:4:8"]]
+ 005e08e0 ["CALL", null, ["callee:008514f8:8"]]
- 005e08a0 bytes 06c30994
+ 005e08e0 bytes 06c30994
~~~


<a id="compare-e14c284acb0f26340023f4e5c622878f"></a>

### [`005e08c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e08c0.md) → [`005e0900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0900.md) FUN_005e0900

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`0071931c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00719/0071931c.md) [`009d5b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d5/009d5b5c.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 8件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`0071935c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00719/0071935c.md) [`009d5cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d5/009d5cf8.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e08c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e08c0.md#insn-005e08c8)
- 新版 `005e0908`（命令位置の公開資料なし）

~~~diff
- 005e08c8 ["INT_ADD", "register:40f0:8", ["const:5e08c8:8", "const:4:8"]]
- 005e08c8 ["CALL", null, ["callee:008514f8:8"]]
+ 005e0908 ["INT_ADD", "register:40f0:8", ["const:5e0908:8", "const:4:8"]]
+ 005e0908 ["CALL", null, ["callee:008514f8:8"]]
- 005e08c8 bytes fcc20994
+ 005e0908 bytes fcc20994
~~~


<a id="compare-ca5a921f3ee1655da5742af519e93d36"></a>

### [`005e08e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e08e0.md) → [`005e0920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0920.md) FUN_005e0920

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 12件 [`005f3250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f3/005f3250.md) [`005f7900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f7/005f7900.md) [`005fb400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fb/005fb400.md) [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) · 呼出先 2件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00af3548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3548.md)
- 新版 呼出元 12件 [`005f3290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f3/005f3290.md) [`005f7940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f7/005f7940.md) [`005fb440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fb/005fb440.md) [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) · 呼出先 2件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00af3970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3970.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e08f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e08e0.md#insn-005e08f0) · [`005e0908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e08e0.md#insn-005e0908) · [`005e0920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e08e0.md#insn-005e0920)
- 新版 `005e0930`（命令位置の公開資料なし） · `005e0948`（命令位置の公開資料なし） · `005e0960`（命令位置の公開資料なし）

~~~diff
- 005e08f0 ["INT_ADD", "register:40f0:8", ["const:5e08f0:8", "const:4:8"]]
- 005e08f0 ["CALL", null, ["callee:008514f8:8"]]
+ 005e0930 ["INT_ADD", "register:40f0:8", ["const:5e0930:8", "const:4:8"]]
+ 005e0930 ["CALL", null, ["callee:008514f8:8"]]
- 005e08f0 bytes f2c20994
+ 005e0930 bytes f2c20994
- 005e0908 ["INT_ADD", "register:40f0:8", ["const:5e0908:8", "const:4:8"]]
- 005e0908 ["CALL", null, ["callee:008514f8:8"]]
+ 005e0948 ["INT_ADD", "register:40f0:8", ["const:5e0948:8", "const:4:8"]]
+ 005e0948 ["CALL", null, ["callee:008514f8:8"]]
- 005e0908 bytes ecc20994
+ 005e0948 bytes ecc20994
- 005e0920 ["INT_ADD", "register:40f0:8", ["const:5e0920:8", "const:4:8"]]
- 005e0920 ["CALL", null, ["callee:00af3970:8"]]
+ 005e0960 ["INT_ADD", "register:40f0:8", ["const:5e0960:8", "const:4:8"]]
+ 005e0960 ["CALL", null, ["callee:00af3970:8"]]
- 005e0920 bytes 0a4b1494
+ 005e0960 bytes 044c1494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88ea944dd47badc22f9f18574070b218"></a>

### [`005e0960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0960.md) → [`005e09a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e09a0.md) FUN_005e09a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005e02e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e02e0.md) [`005e0b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0b10.md) [`00afb194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afb/00afb194.md) · 呼出先 9件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00a642f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a642f0.md) [`00a64310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64310.md) [`00a64330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64330.md) [`00af24f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af2/00af24f4.md)
- 新版 呼出元 3件 [`005e0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0320.md) [`005e0b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0b50.md) [`00afb5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afb/00afb5bc.md) · 呼出先 9件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00a644e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a644e8.md) [`00a64508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a64508.md) [`00a64528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a64528.md) [`00af291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af2/00af291c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e097c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0960.md#insn-005e097c) · [`005e0994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0960.md#insn-005e0994) · [`005e09a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0960.md#insn-005e09a0)
- 新版 `005e09bc`（命令位置の公開資料なし） · `005e09d4`（命令位置の公開資料なし） · `005e09e0`（命令位置の公開資料なし）

~~~diff
- 005e097c ["INT_ADD", "register:40f0:8", ["const:5e097c:8", "const:4:8"]]
- 005e097c ["CALL", null, ["callee:008514f8:8"]]
+ 005e09bc ["INT_ADD", "register:40f0:8", ["const:5e09bc:8", "const:4:8"]]
+ 005e09bc ["CALL", null, ["callee:008514f8:8"]]
- 005e097c bytes cfc20994
+ 005e09bc bytes cfc20994
- 005e0994 ["INT_ADD", "register:40f0:8", ["const:5e0994:8", "const:4:8"]]
- 005e0994 ["CALL", null, ["callee:00af2930:8"]]
+ 005e09d4 ["INT_ADD", "register:40f0:8", ["const:5e09d4:8", "const:4:8"]]
+ 005e09d4 ["CALL", null, ["callee:00af2930:8"]]
- 005e0994 bytes dd461494
+ 005e09d4 bytes d7471494
- 005e09a0 ["INT_ADD", "register:40f0:8", ["const:5e09a0:8", "const:4:8"]]
- 005e09a0 ["CALL", null, ["callee:00af291c:8"]]
+ 005e09e0 ["INT_ADD", "register:40f0:8", ["const:5e09e0:8", "const:4:8"]]
+ 005e09e0 ["CALL", null, ["callee:00af291c:8"]]
- 005e09a0 bytes d5461494
+ 005e09e0 bytes cf471494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e6f528a509551f97b872129cddd3532"></a>

### [`005e0b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0b10.md) → [`005e0b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0b50.md) FUN_005e0b50

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 7件 [`005e0960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0960.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00a642f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a642f0.md) [`00a64310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64310.md) [`00a64330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64330.md)
- 新版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 7件 [`005e09a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e09a0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00a644e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a644e8.md) [`00a64508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a64508.md) [`00a64528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a64528.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e0b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0b10.md#insn-005e0b2c) · [`005e0b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0b10.md#insn-005e0b44) · [`005e0b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0b10.md#insn-005e0b50)
- 新版 `005e0b6c`（命令位置の公開資料なし） · `005e0b84`（命令位置の公開資料なし） · `005e0b90`（命令位置の公開資料なし）

~~~diff
- 005e0b2c ["INT_ADD", "register:40f0:8", ["const:5e0b2c:8", "const:4:8"]]
- 005e0b2c ["CALL", null, ["callee:008514f8:8"]]
+ 005e0b6c ["INT_ADD", "register:40f0:8", ["const:5e0b6c:8", "const:4:8"]]
+ 005e0b6c ["CALL", null, ["callee:008514f8:8"]]
- 005e0b2c bytes 63c20994
+ 005e0b6c bytes 63c20994
- 005e0b44 ["INT_ADD", "register:40f0:8", ["const:5e0b44:8", "const:4:8"]]
- 005e0b44 ["CALL", null, ["callee:00af2930:8"]]
+ 005e0b84 ["INT_ADD", "register:40f0:8", ["const:5e0b84:8", "const:4:8"]]
+ 005e0b84 ["CALL", null, ["callee:00af2930:8"]]
- 005e0b44 bytes 71461494
+ 005e0b84 bytes 6b471494
- 005e0b50 ["INT_ADD", "register:40f0:8", ["const:5e0b50:8", "const:4:8"]]
- 005e0b50 ["CALL", null, ["callee:00af291c:8"]]
+ 005e0b90 ["INT_ADD", "register:40f0:8", ["const:5e0b90:8", "const:4:8"]]
+ 005e0b90 ["CALL", null, ["callee:00af291c:8"]]
- 005e0b50 bytes 69461494
+ 005e0b90 bytes 63471494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ea5359f8815f1c5a71be78a9fb384c6"></a>

### [`005e0cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0cdc.md) → [`005e0d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0d1c.md) FUN_005e0d1c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`0061037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00610/0061037c.md) [`0061300c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/0061300c.md) [`006144ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00614/006144ec.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 5件 [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) [`0061304c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00613/0061304c.md) [`0061452c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00614/0061452c.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e0ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0cdc.md#insn-005e0ce4)
- 新版 `005e0d24`（命令位置の公開資料なし）

~~~diff
- 005e0ce4 ["INT_ADD", "register:40f0:8", ["const:5e0ce4:8", "const:4:8"]]
- 005e0ce4 ["CALL", null, ["callee:008514f8:8"]]
+ 005e0d24 ["INT_ADD", "register:40f0:8", ["const:5e0d24:8", "const:4:8"]]
+ 005e0d24 ["CALL", null, ["callee:008514f8:8"]]
- 005e0ce4 bytes f5c10994
+ 005e0d24 bytes f5c10994
~~~


<a id="compare-f5d09ce03fc6525b9e085bc0c7faedee"></a>

### [`005e0cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0cfc.md) → [`005e0d3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0d3c.md) FUN_005e0d3c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`00720050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00720/00720050.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 5件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`00720090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00720/00720090.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e0d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0cfc.md#insn-005e0d0c)
- 新版 `005e0d4c`（命令位置の公開資料なし）

~~~diff
- 005e0d0c ["INT_ADD", "register:40f0:8", ["const:5e0d0c:8", "const:4:8"]]
- 005e0d0c ["CALL", null, ["callee:008514f8:8"]]
+ 005e0d4c ["INT_ADD", "register:40f0:8", ["const:5e0d4c:8", "const:4:8"]]
+ 005e0d4c ["CALL", null, ["callee:008514f8:8"]]
- 005e0d0c bytes ebc10994
+ 005e0d4c bytes ebc10994
~~~


<a id="compare-f6c2c8e91372c2f75819a8cc897888a2"></a>

### [`005e0d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0d28.md) → [`005e0d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0d68.md) FUN_005e0d68

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 18件 [`0047cd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd9c.md) [`005e6780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e6780.md) [`005f3250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f3/005f3250.md) [`005f466c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f4/005f466c.md) [`005f7564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f7/005f7564.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 18件 [`0047cddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cddc.md) [`005e67c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e6/005e67c0.md) [`005f3290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f3/005f3290.md) [`005f46ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f4/005f46ac.md) [`005f75a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f7/005f75a4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e0d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0d28.md#insn-005e0d30)
- 新版 `005e0d70`（命令位置の公開資料なし）

~~~diff
- 005e0d30 ["INT_ADD", "register:40f0:8", ["const:5e0d30:8", "const:4:8"]]
- 005e0d30 ["CALL", null, ["callee:008514f8:8"]]
+ 005e0d70 ["INT_ADD", "register:40f0:8", ["const:5e0d70:8", "const:4:8"]]
+ 005e0d70 ["CALL", null, ["callee:008514f8:8"]]
- 005e0d30 bytes e2c10994
+ 005e0d70 bytes e2c10994
~~~


<a id="compare-4301b309f4ee3f1061c0afbe0eac453f"></a>

### [`005e0d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0d48.md) → [`005e0d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0d88.md) FUN_005e0d88

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 2件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00853fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853fa8.md)
- 新版 呼出元 5件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 2件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00853fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853fe8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e0d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0d48.md#insn-005e0d58) · [`005e0d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0d48.md#insn-005e0d68)
- 新版 `005e0d98`（命令位置の公開資料なし） · `005e0da8`（命令位置の公開資料なし）

~~~diff
- 005e0d58 ["INT_ADD", "register:40f0:8", ["const:5e0d58:8", "const:4:8"]]
- 005e0d58 ["CALL", null, ["callee:008514f8:8"]]
+ 005e0d98 ["INT_ADD", "register:40f0:8", ["const:5e0d98:8", "const:4:8"]]
+ 005e0d98 ["CALL", null, ["callee:008514f8:8"]]
- 005e0d58 bytes d8c10994
+ 005e0d98 bytes d8c10994
- 005e0d68 ["INT_ADD", "register:40f0:8", ["const:5e0d68:8", "const:4:8"]]
- 005e0d68 ["CALL", null, ["callee:008514f8:8"]]
+ 005e0da8 ["INT_ADD", "register:40f0:8", ["const:5e0da8:8", "const:4:8"]]
+ 005e0da8 ["CALL", null, ["callee:008514f8:8"]]
- 005e0d68 bytes d4c10994
+ 005e0da8 bytes d4c10994
~~~


<a id="compare-3577c5a8ab5dbf03dd7c2ea1d1723ea5"></a>

### [`005e0e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0e68.md) → [`005e0ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0ea8.md) FUN_005e0ea8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`00710298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710298.md) [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 2件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00a31924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a31/00a31924.md)
- 新版 呼出元 4件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007102d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 2件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00a31b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31b1c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e0e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0e68.md#insn-005e0e70) · [`005e0e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0e68.md#insn-005e0e78) · [`005e0e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0e68.md#insn-005e0e80)
- 新版 `005e0eb0`（命令位置の公開資料なし） · `005e0eb8`（命令位置の公開資料なし） · `005e0ec0`（命令位置の公開資料なし）

~~~diff
- 005e0e70 ["INT_ADD", "register:40f0:8", ["const:5e0e70:8", "const:4:8"]]
- 005e0e70 ["CALL", null, ["callee:008514f8:8"]]
+ 005e0eb0 ["INT_ADD", "register:40f0:8", ["const:5e0eb0:8", "const:4:8"]]
+ 005e0eb0 ["CALL", null, ["callee:008514f8:8"]]
- 005e0e70 bytes 92c10994
+ 005e0eb0 bytes 92c10994
- 005e0e78 ["INT_ADD", "register:40f0:8", ["const:5e0e78:8", "const:4:8"]]
- 005e0e78 ["CALL", null, ["callee:00a31b1c:8"]]
+ 005e0eb8 ["INT_ADD", "register:40f0:8", ["const:5e0eb8:8", "const:4:8"]]
+ 005e0eb8 ["CALL", null, ["callee:00a31b1c:8"]]
- 005e0e78 bytes ab421194
+ 005e0eb8 bytes 19431194
- 005e0e80 ["INT_ADD", "register:40f0:8", ["const:5e0e80:8", "const:4:8"]]
- 005e0e80 ["CALL", null, ["callee:008514f8:8"]]
+ 005e0ec0 ["INT_ADD", "register:40f0:8", ["const:5e0ec0:8", "const:4:8"]]
+ 005e0ec0 ["CALL", null, ["callee:008514f8:8"]]
- 005e0e80 bytes 8ec10994
+ 005e0ec0 bytes 8ec10994
~~~


<a id="compare-b60e3df302070953a3f2ff5259b31140"></a>

### [`005e0eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0eac.md) → [`005e0eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0eec.md) FUN_005e0eec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 14件 [`005e7b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7b90.md) [`0066b684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b684.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) · 呼出先 2件 [`005e0f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0f50.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 14件 [`005e7bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7bd0.md) [`0066b6c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b6c4.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) · 呼出先 2件 [`005e0f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0f90.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e0f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0eac.md#insn-005e0f00) · [`005e0f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0eac.md#insn-005e0f08)
- 新版 `005e0f40`（命令位置の公開資料なし） · `005e0f48`（命令位置の公開資料なし）

~~~diff
- 005e0f00 ["INT_ADD", "register:40f0:8", ["const:5e0f00:8", "const:4:8"]]
- 005e0f00 ["CALL", null, ["callee:005e0f90:8"]]
+ 005e0f40 ["INT_ADD", "register:40f0:8", ["const:5e0f40:8", "const:4:8"]]
+ 005e0f40 ["CALL", null, ["callee:005e0f90:8"]]
- 005e0f00 bytes 14000094
+ 005e0f40 bytes 14000094
- 005e0f08 ["INT_ADD", "register:40f0:8", ["const:5e0f08:8", "const:4:8"]]
- 005e0f08 ["CALL", null, ["callee:008514f8:8"]]
+ 005e0f48 ["INT_ADD", "register:40f0:8", ["const:5e0f48:8", "const:4:8"]]
+ 005e0f48 ["CALL", null, ["callee:008514f8:8"]]
- 005e0f08 bytes 6cc10994
+ 005e0f48 bytes 6cc10994
~~~


<a id="compare-2a03373a352bb831cd682ab62b4d3ad4"></a>

### [`005e1160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1160.md) → [`005e11a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e11a0.md) FUN_005e11a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 1件 [`005e0f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0f50.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 1件 [`005e0f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0f90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e1170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1160.md#insn-005e1170) · [`005e1190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1160.md#insn-005e1190) · [`005e11a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1160.md#insn-005e11a8)
- 新版 `005e11b0`（命令位置の公開資料なし） · `005e11d0`（命令位置の公開資料なし） · `005e11e8`（命令位置の公開資料なし）

~~~diff
- 005e1170 ["INT_ADD", "register:40f0:8", ["const:5e1170:8", "const:4:8"]]
- 005e1170 ["CALL", null, ["callee:005e0f90:8"]]
+ 005e11b0 ["INT_ADD", "register:40f0:8", ["const:5e11b0:8", "const:4:8"]]
+ 005e11b0 ["CALL", null, ["callee:005e0f90:8"]]
- 005e1170 bytes 78ffff97
+ 005e11b0 bytes 78ffff97
- 005e1190 ["INT_ADD", "register:40f0:8", ["const:5e1190:8", "const:4:8"]]
- 005e1190 ["CALL", null, ["callee:005e0f90:8"]]
+ 005e11d0 ["INT_ADD", "register:40f0:8", ["const:5e11d0:8", "const:4:8"]]
+ 005e11d0 ["CALL", null, ["callee:005e0f90:8"]]
- 005e1190 bytes 70ffff97
+ 005e11d0 bytes 70ffff97
- 005e11a8 ["INT_ADD", "register:40f0:8", ["const:5e11a8:8", "const:4:8"]]
- 005e11a8 ["CALL", null, ["callee:005e0f90:8"]]
+ 005e11e8 ["INT_ADD", "register:40f0:8", ["const:5e11e8:8", "const:4:8"]]
+ 005e11e8 ["CALL", null, ["callee:005e0f90:8"]]
- 005e11a8 bytes 6affff97
+ 005e11e8 bytes 6affff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1c3b7b6199b4f2af10ec6dfeb5adfcb"></a>

### [`005e1264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1264.md) → [`005e12a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e12a4.md) FUN_005e12a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 6件 [`005e0f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0f50.md) [`005e15e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e15e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00ace960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00ace960.md) [`00acec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00acec24.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 6件 [`005e0f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0f90.md) [`005e1620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1620.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00aceb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ace/00aceb5c.md) [`00acee20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ace/00acee20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e1280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1264.md#insn-005e1280) · [`005e1290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1264.md#insn-005e1290) · [`005e1298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1264.md#insn-005e1298)
- 新版 `005e12c0`（命令位置の公開資料なし） · `005e12d0`（命令位置の公開資料なし） · `005e12d8`（命令位置の公開資料なし）

~~~diff
- 005e1280 ["INT_ADD", "register:40f0:8", ["const:5e1280:8", "const:4:8"]]
- 005e1280 ["CALL", null, ["callee:008514f8:8"]]
+ 005e12c0 ["INT_ADD", "register:40f0:8", ["const:5e12c0:8", "const:4:8"]]
+ 005e12c0 ["CALL", null, ["callee:008514f8:8"]]
- 005e1280 bytes 8ec00994
+ 005e12c0 bytes 8ec00994
- 005e1290 ["INT_ADD", "register:40f0:8", ["const:5e1290:8", "const:4:8"]]
- 005e1290 ["CALL", null, ["callee:008514f8:8"]]
+ 005e12d0 ["INT_ADD", "register:40f0:8", ["const:5e12d0:8", "const:4:8"]]
+ 005e12d0 ["CALL", null, ["callee:008514f8:8"]]
- 005e1290 bytes 8ac00994
+ 005e12d0 bytes 8ac00994
- 005e1298 ["INT_ADD", "register:40f0:8", ["const:5e1298:8", "const:4:8"]]
- 005e1298 ["CALL", null, ["callee:008514f8:8"]]
+ 005e12d8 ["INT_ADD", "register:40f0:8", ["const:5e12d8:8", "const:4:8"]]
+ 005e12d8 ["CALL", null, ["callee:008514f8:8"]]
- 005e1298 bytes 88c00994
+ 005e12d8 bytes 88c00994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57de026b31a76f8860a4f6b8c1688e15"></a>

### [`005e1710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1710.md) → [`005e1750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1750.md) FUN_005e1750

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 6件 [`005e0f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0f50.md) [`005e15e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e15e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00ace960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00ace960.md) [`00acec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00acec24.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 6件 [`005e0f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0f90.md) [`005e1620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1620.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00aceb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ace/00aceb5c.md) [`00acee20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ace/00acee20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e172c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1710.md#insn-005e172c) · [`005e173c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1710.md#insn-005e173c) · [`005e1744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1710.md#insn-005e1744)
- 新版 `005e176c`（命令位置の公開資料なし） · `005e177c`（命令位置の公開資料なし） · `005e1784`（命令位置の公開資料なし）

~~~diff
- 005e172c ["INT_ADD", "register:40f0:8", ["const:5e172c:8", "const:4:8"]]
- 005e172c ["CALL", null, ["callee:008514f8:8"]]
+ 005e176c ["INT_ADD", "register:40f0:8", ["const:5e176c:8", "const:4:8"]]
+ 005e176c ["CALL", null, ["callee:008514f8:8"]]
- 005e172c bytes 63bf0994
+ 005e176c bytes 63bf0994
- 005e173c ["INT_ADD", "register:40f0:8", ["const:5e173c:8", "const:4:8"]]
- 005e173c ["CALL", null, ["callee:008514f8:8"]]
+ 005e177c ["INT_ADD", "register:40f0:8", ["const:5e177c:8", "const:4:8"]]
+ 005e177c ["CALL", null, ["callee:008514f8:8"]]
- 005e173c bytes 5fbf0994
+ 005e177c bytes 5fbf0994
- 005e1744 ["INT_ADD", "register:40f0:8", ["const:5e1744:8", "const:4:8"]]
- 005e1744 ["CALL", null, ["callee:008514f8:8"]]
+ 005e1784 ["INT_ADD", "register:40f0:8", ["const:5e1784:8", "const:4:8"]]
+ 005e1784 ["CALL", null, ["callee:008514f8:8"]]
- 005e1744 bytes 5dbf0994
+ 005e1784 bytes 5dbf0994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb115cd3105f044d48be2a6e14308513"></a>

### [`005e1abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1abc.md) → [`005e1afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1afc.md) FUN_005e1afc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00718734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00718/00718734.md) [`00a51dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a51/00a51dcc.md) [`00a52c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a52/00a52c38.md) · 呼出先 1件 [`005e0f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0f50.md)
- 新版 呼出元 3件 [`00718774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00718/00718774.md) [`00a51fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a51/00a51fc4.md) [`00a52e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a52/00a52e30.md) · 呼出先 1件 [`005e0f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0f90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e1ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1abc.md#insn-005e1ac4)
- 新版 `005e1b04`（命令位置の公開資料なし）

~~~diff
- 005e1ac4 ["INT_ADD", "register:40f0:8", ["const:5e1ac4:8", "const:4:8"]]
- 005e1ac4 ["CALL", null, ["callee:005e0f90:8"]]
+ 005e1b04 ["INT_ADD", "register:40f0:8", ["const:5e1b04:8", "const:4:8"]]
+ 005e1b04 ["CALL", null, ["callee:005e0f90:8"]]
- 005e1ac4 bytes 23fdff97
+ 005e1b04 bytes 23fdff97
~~~


<a id="compare-c6ff84304f6c8a0a47d4690c2ee61636"></a>

### [`005e1ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1ad8.md) → [`005e1b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1b18.md) FUN_005e1b18

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 15件 [`005b068c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b068c.md) [`005e7c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7c58.md) [`005e7efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7efc.md) [`005e8020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e8/005e8020.md) [`005f5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f5/005f5750.md) · 呼出先 1件 [`005e0f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0f50.md)
- 新版 呼出元 15件 [`005b06cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b06cc.md) [`005e7c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7c98.md) [`005e7f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7f3c.md) [`005e8060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e8/005e8060.md) [`005f5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5790.md) · 呼出先 1件 [`005e0f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0f90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e1ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1ad8.md#insn-005e1ae0)
- 新版 `005e1b20`（命令位置の公開資料なし）

~~~diff
- 005e1ae0 ["INT_ADD", "register:40f0:8", ["const:5e1ae0:8", "const:4:8"]]
- 005e1ae0 ["CALL", null, ["callee:005e0f90:8"]]
+ 005e1b20 ["INT_ADD", "register:40f0:8", ["const:5e1b20:8", "const:4:8"]]
+ 005e1b20 ["CALL", null, ["callee:005e0f90:8"]]
- 005e1ae0 bytes 1cfdff97
+ 005e1b20 bytes 1cfdff97
~~~


<a id="compare-42728a9a879baed3e122672003cf1679"></a>

### [`005e2a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e2/005e2a6c.md) → [`005e2aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e2/005e2aac.md) FUN_005e2aac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 21件 [`005e30d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e3/005e30d4.md) [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 21件 [`005e3114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e3/005e3114.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`0064ecb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064ecb8.md) [`006ea588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ea/006ea588.md) [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e2a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e2/005e2a6c.md#insn-005e2a98) · [`005e2aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e2/005e2a6c.md#insn-005e2aac) · [`005e2ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e2/005e2a6c.md#insn-005e2ab4)
- 新版 `005e2ad8`（命令位置の公開資料なし） · `005e2aec`（命令位置の公開資料なし） · `005e2af4`（命令位置の公開資料なし）

~~~diff
- 005e2a98 ["INT_ADD", "register:40f0:8", ["const:5e2a98:8", "const:4:8"]]
- 005e2a98 ["CALL", null, ["callee:00c53d00:8"]]
+ 005e2ad8 ["INT_ADD", "register:40f0:8", ["const:5e2ad8:8", "const:4:8"]]
+ 005e2ad8 ["CALL", null, ["callee:00c53d00:8"]]
- 005e2a98 bytes 92c31994
+ 005e2ad8 bytes 8ac41994
- 005e2aac ["COPY", "register:0:8", ["register:4040:8"]]
- 005e2aac ["INT_ADD", "register:40f0:8", ["const:5e2aac:8", "const:4:8"]]
- 005e2aac ["CALLIND", null, ["register:0:8"]]
+ 005e2aec ["COPY", "register:0:8", ["register:4040:8"]]
+ 005e2aec ["INT_ADD", "register:40f0:8", ["const:5e2aec:8", "const:4:8"]]
+ 005e2aec ["CALLIND", null, ["register:0:8"]]
- 005e2aac bytes 00013fd6
+ 005e2aec bytes 00013fd6
- 005e2ab4 ["INT_ADD", "register:40f0:8", ["const:5e2ab4:8", "const:4:8"]]
- 005e2ab4 ["CALL", null, ["callee:00c57e80:8"]]
+ 005e2af4 ["INT_ADD", "register:40f0:8", ["const:5e2af4:8", "const:4:8"]]
+ 005e2af4 ["CALL", null, ["callee:00c57e80:8"]]
- 005e2ab4 bytes f3d31994
+ 005e2af4 bytes e3d41994
~~~


<a id="compare-cae99da70b0be9b90668cb7d22e74c5c"></a>

### [`005e4328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e4328.md) → [`005e4368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4368.md) FUN_005e4368

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005fc360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fc/005fc360.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`00718734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00718/00718734.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`005fc3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fc/005fc3a0.md) [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`00718774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00718/00718774.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e4338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e4328.md#insn-005e4338) · [`005e4350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e4328.md#insn-005e4350)
- 新版 `005e4378`（命令位置の公開資料なし） · `005e4390`（命令位置の公開資料なし）

~~~diff
- 005e4338 ["INT_ADD", "register:40f0:8", ["const:5e4338:8", "const:4:8"]]
- 005e4338 ["CALL", null, ["callee:008514f8:8"]]
+ 005e4378 ["INT_ADD", "register:40f0:8", ["const:5e4378:8", "const:4:8"]]
+ 005e4378 ["CALL", null, ["callee:008514f8:8"]]
- 005e4338 bytes 60b40994
+ 005e4378 bytes 60b40994
- 005e4350 ["INT_ADD", "register:40f0:8", ["const:5e4350:8", "const:4:8"]]
- 005e4350 ["CALL", null, ["callee:008514f8:8"]]
+ 005e4390 ["INT_ADD", "register:40f0:8", ["const:5e4390:8", "const:4:8"]]
+ 005e4390 ["CALL", null, ["callee:008514f8:8"]]
- 005e4350 bytes 5ab40994
+ 005e4390 bytes 5ab40994
~~~


<a id="compare-e1136c25d2b489df69b2c084e53e28e1"></a>

### [`005e44a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e44a8.md) → [`005e44e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e44e8.md) FUN_005e44e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005fb400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fb/005fb400.md) [`007154c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007154c0.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`005fb440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fb/005fb440.md) [`00715500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00715/00715500.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e44b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e44a8.md#insn-005e44b8)
- 新版 `005e44f8`（命令位置の公開資料なし）

~~~diff
- 005e44b8 ["INT_ADD", "register:40f0:8", ["const:5e44b8:8", "const:4:8"]]
- 005e44b8 ["CALL", null, ["callee:008514f8:8"]]
+ 005e44f8 ["INT_ADD", "register:40f0:8", ["const:5e44f8:8", "const:4:8"]]
+ 005e44f8 ["CALL", null, ["callee:008514f8:8"]]
- 005e44b8 bytes 00b40994
+ 005e44f8 bytes 00b40994
~~~


<a id="compare-58b2abb4c6239b3470a54b62cca371d3"></a>

### [`005e45b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e45b8.md) → [`005e45f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e45f8.md) FUN_005e45f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005f5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f5/005f5750.md) [`00a51dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a51/00a51dcc.md) · 呼出先 4件 [`005e0f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0f50.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00af3588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3588.md) [`00af37f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af37f4.md)
- 新版 呼出元 2件 [`005f5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5790.md) [`00a51fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a51/00a51fc4.md) · 呼出先 4件 [`005e0f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0f90.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00af39b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af39b0.md) [`00af3c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3c1c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e45d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e45b8.md#insn-005e45d4) · [`005e460c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e45b8.md#insn-005e460c) · [`005e4644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e45b8.md#insn-005e4644)
- 新版 `005e4614`（命令位置の公開資料なし） · `005e464c`（命令位置の公開資料なし） · `005e4684`（命令位置の公開資料なし）

~~~diff
- 005e45d4 ["INT_ADD", "register:40f0:8", ["const:5e45d4:8", "const:4:8"]]
- 005e45d4 ["CALL", null, ["callee:008514f8:8"]]
+ 005e4614 ["INT_ADD", "register:40f0:8", ["const:5e4614:8", "const:4:8"]]
+ 005e4614 ["CALL", null, ["callee:008514f8:8"]]
- 005e45d4 bytes b9b30994
+ 005e4614 bytes b9b30994
- 005e460c ["INT_ADD", "register:40f0:8", ["const:5e460c:8", "const:4:8"]]
- 005e460c ["CALL", null, ["callee:008514f8:8"]]
+ 005e464c ["INT_ADD", "register:40f0:8", ["const:5e464c:8", "const:4:8"]]
+ 005e464c ["CALL", null, ["callee:008514f8:8"]]
- 005e460c bytes abb30994
+ 005e464c bytes abb30994
- 005e4644 ["INT_ADD", "register:40f0:8", ["const:5e4644:8", "const:4:8"]]
- 005e4644 ["CALL", null, ["callee:005e0f90:8"]]
+ 005e4684 ["INT_ADD", "register:40f0:8", ["const:5e4684:8", "const:4:8"]]
+ 005e4684 ["CALL", null, ["callee:005e0f90:8"]]
- 005e4644 bytes 43f2ff97
+ 005e4684 bytes 43f2ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df5d7a1de6ddb51b1164928790a21100"></a>

### [`005e4f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e4f34.md) → [`005e4f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4f74.md) FUN_005e4f74

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`005e1b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1b78.md) [`005e2b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e2/005e2b04.md) [`0067f004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067f/0067f004.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`00904818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00904/00904818.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046e784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 7件 [`005e1bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1bb8.md) [`005e2b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e2/005e2b44.md) [`0067f044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067f/0067f044.md) [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`009049b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/009049b4.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e4fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e4f34.md#insn-005e4fb4) · [`005e4fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e4f34.md#insn-005e4fd4) · [`005e5000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e4f34.md#insn-005e5000)
- 新版 `005e4ff4`（命令位置の公開資料なし） · `005e5014`（命令位置の公開資料なし） · `005e5040`（命令位置の公開資料なし）

~~~diff
- 005e4fb4 ["INT_ADD", "register:40f0:8", ["const:5e4fb4:8", "const:4:8"]]
- 005e4fb4 ["CALL", null, ["callee:00c57e90:8"]]
+ 005e4ff4 ["INT_ADD", "register:40f0:8", ["const:5e4ff4:8", "const:4:8"]]
+ 005e4ff4 ["CALL", null, ["callee:00c57e90:8"]]
- 005e4fb4 bytes b7ca1994
+ 005e4ff4 bytes a7cb1994
- 005e4fd4 ["INT_ADD", "register:40f0:8", ["const:5e4fd4:8", "const:4:8"]]
- 005e4fd4 ["CALL", null, ["callee:0046e7c4:8"]]
+ 005e5014 ["INT_ADD", "register:40f0:8", ["const:5e5014:8", "const:4:8"]]
+ 005e5014 ["CALL", null, ["callee:0046e7c4:8"]]
- 005e4fd4 bytes ec25fa97
+ 005e5014 bytes ec25fa97
- 005e5000 ["INT_ADD", "register:40f0:8", ["const:5e5000:8", "const:4:8"]]
- 005e5000 ["CALL", null, ["callee:0043bba4:8"]]
+ 005e5040 ["INT_ADD", "register:40f0:8", ["const:5e5040:8", "const:4:8"]]
+ 005e5040 ["CALL", null, ["callee:0043bba4:8"]]
- 005e5000 bytes d95af997
+ 005e5040 bytes d95af997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c05b11cf336ba1272908b7dc5a755b5a"></a>

### [`005e5078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e5/005e5078.md) → [`005e50b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e5/005e50b8.md) FUN_005e50b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e509c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e5/005e5078.md#insn-005e509c)
- 新版 `005e50dc`（命令位置の公開資料なし）

~~~diff
- 005e509c ["INT_ADD", "register:40f0:8", ["const:5e509c:8", "const:4:8"]]
- 005e509c ["CALL", null, ["callee:0046e8a4:8"]]
+ 005e50dc ["INT_ADD", "register:40f0:8", ["const:5e50dc:8", "const:4:8"]]
+ 005e50dc ["CALL", null, ["callee:0046e8a4:8"]]
- 005e509c bytes f225fa97
+ 005e50dc bytes f225fa97
~~~


<a id="compare-05c4d4ca59bd14e4801460eb78411b08"></a>

### [`005e5ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e5/005e5ff8.md) → [`005e6038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e6/005e6038.md) FUN_005e6038

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005e6780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e6780.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`005e67c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e6/005e67c0.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e6060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e5/005e5ff8.md#insn-005e6060) · [`005e609c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e5/005e5ff8.md#insn-005e609c)
- 新版 `005e60a0`（命令位置の公開資料なし） · `005e60dc`（命令位置の公開資料なし）

~~~diff
- 005e6060 ["INT_ADD", "register:40f0:8", ["const:5e6060:8", "const:4:8"]]
- 005e6060 ["CALL", null, ["callee:00c57e90:8"]]
+ 005e60a0 ["INT_ADD", "register:40f0:8", ["const:5e60a0:8", "const:4:8"]]
+ 005e60a0 ["CALL", null, ["callee:00c57e90:8"]]
- 005e6060 bytes 8cc61994
+ 005e60a0 bytes 7cc71994
- 005e609c ["INT_ADD", "register:40f0:8", ["const:5e609c:8", "const:4:8"]]
- 005e609c ["CALL", null, ["callee:0043bba4:8"]]
+ 005e60dc ["INT_ADD", "register:40f0:8", ["const:5e60dc:8", "const:4:8"]]
+ 005e60dc ["CALL", null, ["callee:0043bba4:8"]]
- 005e609c bytes b256f997
+ 005e60dc bytes b256f997
~~~


<a id="compare-783e694aab317ed4dbbd8fe0387851e1"></a>

### [`005e60d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e60d4.md) → [`005e6114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e6/005e6114.md) FUN_005e6114

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005f87e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f8/005f87e0.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`005f8820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f8/005f8820.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e6174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e60d4.md#insn-005e6174) · [`005e61b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e60d4.md#insn-005e61b0) · [`005e6210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e60d4.md#insn-005e6210)
- 新版 `005e61b4`（命令位置の公開資料なし） · `005e61f0`（命令位置の公開資料なし） · `005e6250`（命令位置の公開資料なし）

~~~diff
- 005e6174 ["INT_ADD", "register:40f0:8", ["const:5e6174:8", "const:4:8"]]
- 005e6174 ["CALL", null, ["callee:00c57e90:8"]]
+ 005e61b4 ["INT_ADD", "register:40f0:8", ["const:5e61b4:8", "const:4:8"]]
+ 005e61b4 ["CALL", null, ["callee:00c57e90:8"]]
- 005e6174 bytes 47c61994
+ 005e61b4 bytes 37c71994
- 005e61b0 ["INT_ADD", "register:40f0:8", ["const:5e61b0:8", "const:4:8"]]
- 005e61b0 ["CALL", null, ["callee:0043bba4:8"]]
+ 005e61f0 ["INT_ADD", "register:40f0:8", ["const:5e61f0:8", "const:4:8"]]
+ 005e61f0 ["CALL", null, ["callee:0043bba4:8"]]
- 005e61b0 bytes 6d56f997
+ 005e61f0 bytes 6d56f997
- 005e6210 ["INT_ADD", "register:40f0:8", ["const:5e6210:8", "const:4:8"]]
- 005e6210 ["CALL", null, ["callee:00c57e90:8"]]
+ 005e6250 ["INT_ADD", "register:40f0:8", ["const:5e6250:8", "const:4:8"]]
+ 005e6250 ["CALL", null, ["callee:00c57e90:8"]]
- 005e6210 bytes 20c61994
+ 005e6250 bytes 10c71994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39c6029928bcd3f22238619523eb0287"></a>

### [`005e69a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e69a4.md) → [`005e69e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e6/005e69e4.md) FUN_005e69e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005e57dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e5/005e57dc.md) [`005e69a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e69a4.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 2件 [`005e69a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e69a4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`005e581c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e5/005e581c.md) [`005e69e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e6/005e69e4.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 2件 [`005e69e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e6/005e69e4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e69c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e69a4.md#insn-005e69c4) · [`005e69d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e69a4.md#insn-005e69d0)
- 新版 `005e6a04`（命令位置の公開資料なし） · `005e6a10`（命令位置の公開資料なし）

~~~diff
- 005e69c4 ["INT_ADD", "register:40f0:8", ["const:5e69c4:8", "const:4:8"]]
- 005e69c4 ["CALL", null, ["local:b0:8"]]
+ 005e6a04 ["INT_ADD", "register:40f0:8", ["const:5e6a04:8", "const:4:8"]]
+ 005e6a04 ["CALL", null, ["local:b0:8"]]
- 005e69c4 bytes f8ffff97
+ 005e6a04 bytes f8ffff97
- 005e69d0 ["INT_ADD", "register:40f0:8", ["const:5e69d0:8", "const:4:8"]]
- 005e69d0 ["CALL", null, ["local:b0:8"]]
+ 005e6a10 ["INT_ADD", "register:40f0:8", ["const:5e6a10:8", "const:4:8"]]
+ 005e6a10 ["CALL", null, ["local:b0:8"]]
- 005e69d0 bytes f5ffff97
+ 005e6a10 bytes f5ffff97
~~~


<a id="compare-11da48ad3063c126d43ea2888d161444"></a>

### [`005e7770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7770.md) → [`005e77b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e77b0.md) FUN_005e77b0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005f70f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f7/005f70f0.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`00718734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00718/00718734.md) · 呼出先 1件 [`005afc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afc38.md)
- 新版 呼出元 3件 [`005f7130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f7/005f7130.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`00718774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00718/00718774.md) · 呼出先 1件 [`005afc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afc78.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e7788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7770.md#insn-005e7788) · [`005e7794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7770.md#insn-005e7794) · [`005e77a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7770.md#insn-005e77a0)
- 新版 `005e77c8`（命令位置の公開資料なし） · `005e77d4`（命令位置の公開資料なし） · `005e77e0`（命令位置の公開資料なし）

~~~diff
- 005e7788 ["INT_ADD", "register:40f0:8", ["const:5e7788:8", "const:4:8"]]
- 005e7788 ["CALL", null, ["callee:005afc78:8"]]
+ 005e77c8 ["INT_ADD", "register:40f0:8", ["const:5e77c8:8", "const:4:8"]]
+ 005e77c8 ["CALL", null, ["callee:005afc78:8"]]
- 005e7788 bytes 2c21ff97
+ 005e77c8 bytes 2c21ff97
- 005e7794 ["INT_ADD", "register:40f0:8", ["const:5e7794:8", "const:4:8"]]
- 005e7794 ["CALL", null, ["callee:005afc78:8"]]
+ 005e77d4 ["INT_ADD", "register:40f0:8", ["const:5e77d4:8", "const:4:8"]]
+ 005e77d4 ["CALL", null, ["callee:005afc78:8"]]
- 005e7794 bytes 2921ff97
+ 005e77d4 bytes 2921ff97
- 005e77a0 ["INT_ADD", "register:40f0:8", ["const:5e77a0:8", "const:4:8"]]
- 005e77a0 ["CALL", null, ["callee:005afc78:8"]]
+ 005e77e0 ["INT_ADD", "register:40f0:8", ["const:5e77e0:8", "const:4:8"]]
+ 005e77e0 ["CALL", null, ["callee:005afc78:8"]]
- 005e77a0 bytes 2621ff97
+ 005e77e0 bytes 2621ff97
~~~


<a id="compare-c1472870c52bf4d4f7defc008c0dbeb6"></a>

### [`005e7824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7824.md) → [`005e7864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7864.md) FUN_005e7864

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 4件 [`005afc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afc38.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008c2ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c2ce0.md) [`00ab9080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab9080.md)
- 新版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 4件 [`005afc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afc78.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008c2d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c2/008c2d24.md) [`00ab927c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab9/00ab927c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e7838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7824.md#insn-005e7838) · [`005e78a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7824.md#insn-005e78a4) · [`005e78b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7824.md#insn-005e78b4)
- 新版 `005e7878`（命令位置の公開資料なし） · `005e78e4`（命令位置の公開資料なし） · `005e78f4`（命令位置の公開資料なし）

~~~diff
- 005e7838 ["INT_ADD", "register:40f0:8", ["const:5e7838:8", "const:4:8"]]
- 005e7838 ["CALL", null, ["callee:005afc78:8"]]
+ 005e7878 ["INT_ADD", "register:40f0:8", ["const:5e7878:8", "const:4:8"]]
+ 005e7878 ["CALL", null, ["callee:005afc78:8"]]
- 005e7838 bytes 0021ff97
+ 005e7878 bytes 0021ff97
- 005e78a4 ["INT_ADD", "register:40f0:8", ["const:5e78a4:8", "const:4:8"]]
- 005e78a4 ["CALL", null, ["callee:008514f8:8"]]
+ 005e78e4 ["INT_ADD", "register:40f0:8", ["const:5e78e4:8", "const:4:8"]]
+ 005e78e4 ["CALL", null, ["callee:008514f8:8"]]
- 005e78a4 bytes 05a70994
+ 005e78e4 bytes 05a70994
- 005e78b4 ["INT_ADD", "register:40f0:8", ["const:5e78b4:8", "const:4:8"]]
- 005e78b4 ["CALL", null, ["callee:00ab927c:8"]]
+ 005e78f4 ["INT_ADD", "register:40f0:8", ["const:5e78f4:8", "const:4:8"]]
+ 005e78f4 ["CALL", null, ["callee:00ab927c:8"]]
- 005e78b4 bytes f3451394
+ 005e78f4 bytes 62461394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-595c8be2f949de8f1f71cb25170e581c"></a>

### [`005e7900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7900.md) → [`005e7940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7940.md) FUN_005e7940

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) [`00720050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00720/00720050.md) [`009d86a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d8/009d86a4.md) [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 2件 [`005e8158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e8/005e8158.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 5件 [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`00720090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00720/00720090.md) [`009d8840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d8/009d8840.md) [`00a1a750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a750.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 2件 [`005e8198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e8/005e8198.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e7948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7900.md#insn-005e7948) · [`005e7974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7900.md#insn-005e7974)
- 新版 `005e7988`（命令位置の公開資料なし） · `005e79b4`（命令位置の公開資料なし）

~~~diff
- 005e7948 ["INT_ADD", "register:40f0:8", ["const:5e7948:8", "const:4:8"]]
- 005e7948 ["CALL", null, ["callee:005e8198:8"]]
+ 005e7988 ["INT_ADD", "register:40f0:8", ["const:5e7988:8", "const:4:8"]]
+ 005e7988 ["CALL", null, ["callee:005e8198:8"]]
- 005e7948 bytes 04020094
+ 005e7988 bytes 04020094
- 005e7974 ["INT_ADD", "register:40f0:8", ["const:5e7974:8", "const:4:8"]]
- 005e7974 ["CALL", null, ["callee:00c57ee0:8"]]
+ 005e79b4 ["INT_ADD", "register:40f0:8", ["const:5e79b4:8", "const:4:8"]]
+ 005e79b4 ["CALL", null, ["callee:00c57ee0:8"]]
- 005e7974 bytes 5bc01994
+ 005e79b4 bytes 4bc11994
~~~


<a id="compare-fa3f7322d96cae3655e0cd608052bb2f"></a>

### [`005e7b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7b90.md) → [`005e7bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7bd0.md) FUN_005e7bd0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 3件 [`005e0eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0eac.md) [`005e1af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1af0.md) [`005e7c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7c58.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e0eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0eec.md) [`005e1b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1b30.md) [`005e7c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7c98.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e7bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7b90.md#insn-005e7bb0) · [`005e7bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7b90.md#insn-005e7bc4)
- 新版 `005e7bf0`（命令位置の公開資料なし） · `005e7c04`（命令位置の公開資料なし）

~~~diff
- 005e7bb0 ["INT_ADD", "register:40f0:8", ["const:5e7bb0:8", "const:4:8"]]
- 005e7bb0 ["CALL", null, ["callee:005e0eec:8"]]
+ 005e7bf0 ["INT_ADD", "register:40f0:8", ["const:5e7bf0:8", "const:4:8"]]
+ 005e7bf0 ["CALL", null, ["callee:005e0eec:8"]]
- 005e7bb0 bytes bfe4ff97
+ 005e7bf0 bytes bfe4ff97
- 005e7bc4 ["INT_ADD", "register:40f0:8", ["const:5e7bc4:8", "const:4:8"]]
- 005e7bc4 ["CALL", null, ["callee:005e1b30:8"]]
+ 005e7c04 ["INT_ADD", "register:40f0:8", ["const:5e7c04:8", "const:4:8"]]
+ 005e7c04 ["CALL", null, ["callee:005e1b30:8"]]
- 005e7bc4 bytes cbe7ff97
+ 005e7c04 bytes cbe7ff97
~~~


<a id="compare-8ba5e3a3573acb894c30c1239bac4b0a"></a>

### [`005e7c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7c00.md) → [`005e7c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7c40.md) FUN_005e7c40

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00a51dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a51/00a51dcc.md) [`00affc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aff/00affc2c.md) · 呼出先 2件 [`005e1af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1af0.md) [`005e7c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7c58.md)
- 新版 呼出元 2件 [`00a51fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a51/00a51fc4.md) [`00b00054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b00054.md) · 呼出先 2件 [`005e1b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1b30.md) [`005e7c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7c98.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e7c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7c00.md#insn-005e7c20)
- 新版 `005e7c60`（命令位置の公開資料なし）

~~~diff
- 005e7c20 ["INT_ADD", "register:40f0:8", ["const:5e7c20:8", "const:4:8"]]
- 005e7c20 ["CALL", null, ["callee:005e1b30:8"]]
+ 005e7c60 ["INT_ADD", "register:40f0:8", ["const:5e7c60:8", "const:4:8"]]
+ 005e7c60 ["CALL", null, ["callee:005e1b30:8"]]
- 005e7c20 bytes b4e7ff97
+ 005e7c60 bytes b4e7ff97
~~~


<a id="compare-d9391a86af64fe31fc1c55a17fd25398"></a>

### [`005e7efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7efc.md) → [`005e7f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7f3c.md) FUN_005e7f3c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005f5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f5/005f5750.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 9件 [`005e1ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1ad8.md) [`0066a3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a3c8.md) [`006875e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00687/006875e8.md) [`0068770c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00687/0068770c.md) [`00687788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00687/00687788.md)
- 新版 呼出元 2件 [`005f5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5790.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 9件 [`005e1b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1b18.md) [`0066a408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066a/0066a408.md) [`00687628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00687/00687628.md) [`0068774c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00687/0068774c.md) [`006877c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00687/006877c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e7f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7efc.md#insn-005e7f18) · [`005e7f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7efc.md#insn-005e7f28) · [`005e7f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7efc.md#insn-005e7f38)
- 新版 `005e7f58`（命令位置の公開資料なし） · `005e7f68`（命令位置の公開資料なし） · `005e7f78`（命令位置の公開資料なし）

~~~diff
- 005e7f18 ["INT_ADD", "register:40f0:8", ["const:5e7f18:8", "const:4:8"]]
- 005e7f18 ["CALL", null, ["callee:008514f8:8"]]
+ 005e7f58 ["INT_ADD", "register:40f0:8", ["const:5e7f58:8", "const:4:8"]]
+ 005e7f58 ["CALL", null, ["callee:008514f8:8"]]
- 005e7f18 bytes 68a50994
+ 005e7f58 bytes 68a50994
- 005e7f28 ["INT_ADD", "register:40f0:8", ["const:5e7f28:8", "const:4:8"]]
- 005e7f28 ["CALL", null, ["callee:009e0fc0:8"]]
+ 005e7f68 ["INT_ADD", "register:40f0:8", ["const:5e7f68:8", "const:4:8"]]
+ 005e7f68 ["CALL", null, ["callee:009e0fc0:8"]]
- 005e7f28 bytes bfe30f94
+ 005e7f68 bytes 16e40f94
- 005e7f38 ["INT_ADD", "register:40f0:8", ["const:5e7f38:8", "const:4:8"]]
- 005e7f38 ["CALL", null, ["callee:005e1b18:8"]]
+ 005e7f78 ["INT_ADD", "register:40f0:8", ["const:5e7f78:8", "const:4:8"]]
+ 005e7f78 ["CALL", null, ["callee:005e1b18:8"]]
- 005e7f38 bytes e8e6ff97
+ 005e7f78 bytes e8e6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f51c38326c0e7c142732b725242b9fc0"></a>

### [`005e8020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e8/005e8020.md) → [`005e8060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e8/005e8060.md) FUN_005e8060

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005f5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f5/005f5750.md) · 呼出先 7件 [`005e1ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1ad8.md) [`005e1af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1af0.md) [`005e7c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7c58.md) [`006875e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00687/006875e8.md) [`00687788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00687/00687788.md)
- 新版 呼出元 1件 [`005f5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5790.md) · 呼出先 7件 [`005e1b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1b18.md) [`005e1b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1b30.md) [`005e7c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7c98.md) [`00687628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00687/00687628.md) [`006877c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00687/006877c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005e8050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e8/005e8020.md#insn-005e8050) · [`005e8058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e8/005e8020.md#insn-005e8058) · [`005e806c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e8/005e8020.md#insn-005e806c)
- 新版 `005e8090`（命令位置の公開資料なし） · `005e8098`（命令位置の公開資料なし） · `005e80ac`（命令位置の公開資料なし）

~~~diff
- 005e8050 ["INT_ADD", "register:40f0:8", ["const:5e8050:8", "const:4:8"]]
- 005e8050 ["CALL", null, ["callee:005e1b18:8"]]
+ 005e8090 ["INT_ADD", "register:40f0:8", ["const:5e8090:8", "const:4:8"]]
+ 005e8090 ["CALL", null, ["callee:005e1b18:8"]]
- 005e8050 bytes a2e6ff97
+ 005e8090 bytes a2e6ff97
- 005e8058 ["INT_ADD", "register:40f0:8", ["const:5e8058:8", "const:4:8"]]
- 005e8058 ["CALL", null, ["callee:008514f8:8"]]
+ 005e8098 ["INT_ADD", "register:40f0:8", ["const:5e8098:8", "const:4:8"]]
+ 005e8098 ["CALL", null, ["callee:008514f8:8"]]
- 005e8058 bytes 18a50994
+ 005e8098 bytes 18a50994
- 005e806c ["INT_ADD", "register:40f0:8", ["const:5e806c:8", "const:4:8"]]
- 005e806c ["CALL", null, ["callee:006877c8:8"]]
+ 005e80ac ["INT_ADD", "register:40f0:8", ["const:5e80ac:8", "const:4:8"]]
+ 005e80ac ["CALL", null, ["callee:006877c8:8"]]
- 005e806c bytes c77d0294
+ 005e80ac bytes c77d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b728c96a98d3c35efa5842b74eb476a"></a>

### [`005ec020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ec/005ec020.md) → [`005ec060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ec/005ec060.md) FUN_005ec060

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`005e9094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e9/005e9094.md) [`005e94b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e9/005e94b4.md) [`005f0180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0180.md) [`00848920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848920.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`005e90d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e9/005e90d4.md) [`005e94f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e9/005e94f4.md) [`005f01c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f0/005f01c0.md) [`00848960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848960.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ec03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ec/005ec020.md#insn-005ec03c) · [`005ec04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ec/005ec020.md#insn-005ec04c) · [`005ec05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ec/005ec020.md#insn-005ec05c)
- 新版 `005ec07c`（命令位置の公開資料なし） · `005ec08c`（命令位置の公開資料なし） · `005ec09c`（命令位置の公開資料なし）

~~~diff
- 005ec03c ["INT_ADD", "register:40f0:8", ["const:5ec03c:8", "const:4:8"]]
- 005ec03c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ec07c ["INT_ADD", "register:40f0:8", ["const:5ec07c:8", "const:4:8"]]
+ 005ec07c ["CALL", null, ["callee:00c57eb0:8"]]
- 005ec03c bytes 9dae1994
+ 005ec07c bytes 8daf1994
- 005ec04c ["INT_ADD", "register:40f0:8", ["const:5ec04c:8", "const:4:8"]]
- 005ec04c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ec08c ["INT_ADD", "register:40f0:8", ["const:5ec08c:8", "const:4:8"]]
+ 005ec08c ["CALL", null, ["callee:00c57eb0:8"]]
- 005ec04c bytes 99ae1994
+ 005ec08c bytes 89af1994
- 005ec05c ["INT_ADD", "register:40f0:8", ["const:5ec05c:8", "const:4:8"]]
- 005ec05c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ec09c ["INT_ADD", "register:40f0:8", ["const:5ec09c:8", "const:4:8"]]
+ 005ec09c ["CALL", null, ["callee:00c57eb0:8"]]
- 005ec05c bytes 95ae1994
+ 005ec09c bytes 85af1994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4921a7bc10b6739be94684d27143121"></a>

### [`005eff28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ef/005eff28.md) → [`005eff68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ef/005eff68.md) FUN_005eff68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005e9094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e9/005e9094.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005f0158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0158.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005e90d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e9/005e90d4.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005f0198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f0/005f0198.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005effcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ef/005eff28.md#insn-005effcc) · [`005f0104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ef/005eff28.md#insn-005f0104) · [`005f012c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ef/005eff28.md#insn-005f012c)
- 新版 `005f000c`（命令位置の公開資料なし） · `005f0144`（命令位置の公開資料なし） · `005f016c`（命令位置の公開資料なし）

~~~diff
- 005effcc ["INT_ADD", "register:40f0:8", ["const:5effcc:8", "const:4:8"]]
- 005effcc ["CALL", null, ["callee:00c57e90:8"]]
+ 005f000c ["INT_ADD", "register:40f0:8", ["const:5f000c:8", "const:4:8"]]
+ 005f000c ["CALL", null, ["callee:00c57e90:8"]]
- 005effcc bytes b19e1994
+ 005f000c bytes a19f1994
- 005f0104 ["INT_ADD", "register:40f0:8", ["const:5f0104:8", "const:4:8"]]
- 005f0104 ["CALL", null, ["callee:005c179c:8"]]
+ 005f0144 ["INT_ADD", "register:40f0:8", ["const:5f0144:8", "const:4:8"]]
+ 005f0144 ["CALL", null, ["callee:005c179c:8"]]
- 005f0104 bytes 9645ff97
+ 005f0144 bytes 9645ff97
- 005f012c ["INT_ADD", "register:40f0:8", ["const:5f012c:8", "const:4:8"]]
- 005f012c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005f016c ["INT_ADD", "register:40f0:8", ["const:5f016c:8", "const:4:8"]]
+ 005f016c ["CALL", null, ["callee:00c57eb0:8"]]
- 005f012c bytes 619e1994
+ 005f016c bytes 519f1994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f824004cbfcb121b0d472d18ab25e642"></a>

### [`005f0180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0180.md) → [`005f01c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f0/005f01c0.md) FUN_005f01c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005e94b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e9/005e94b4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005ec020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ec/005ec020.md) [`005f02d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f02d8.md) [`005f0a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0a50.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`005e94f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e9/005e94f4.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005ec060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ec/005ec060.md) [`005f0318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f0/005f0318.md) [`005f0a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f0/005f0a90.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005f0224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0180.md#insn-005f0224) · [`005f0244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0180.md#insn-005f0244) · [`005f0270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0180.md#insn-005f0270)
- 新版 `005f0264`（命令位置の公開資料なし） · `005f0284`（命令位置の公開資料なし） · `005f02b0`（命令位置の公開資料なし）

~~~diff
- 005f0224 ["INT_ADD", "register:40f0:8", ["const:5f0224:8", "const:4:8"]]
- 005f0224 ["CALL", null, ["callee:00c57e90:8"]]
+ 005f0264 ["INT_ADD", "register:40f0:8", ["const:5f0264:8", "const:4:8"]]
+ 005f0264 ["CALL", null, ["callee:00c57e90:8"]]
- 005f0224 bytes 1b9e1994
+ 005f0264 bytes 0b9f1994
- 005f0244 ["INT_ADD", "register:40f0:8", ["const:5f0244:8", "const:4:8"]]
- 005f0244 ["CALL", null, ["callee:005f0318:8"]]
+ 005f0284 ["INT_ADD", "register:40f0:8", ["const:5f0284:8", "const:4:8"]]
+ 005f0284 ["CALL", null, ["callee:005f0318:8"]]
- 005f0244 bytes 25000094
+ 005f0284 bytes 25000094
- 005f0270 ["INT_ADD", "register:40f0:8", ["const:5f0270:8", "const:4:8"]]
- 005f0270 ["CALL", null, ["callee:005f0318:8"]]
+ 005f02b0 ["INT_ADD", "register:40f0:8", ["const:5f02b0:8", "const:4:8"]]
+ 005f02b0 ["CALL", null, ["callee:005f0318:8"]]
- 005f0270 bytes 1a000094
+ 005f02b0 bytes 1a000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d82122a23e6d643dbf6712d60e215568"></a>

### [`005f0a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0a64.md) → [`005f0aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f0/005f0aa4.md) FUN_005f0aa4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005e94b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e9/005e94b4.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`005f0b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0b90.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005e94f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e9/005e94f4.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005f0bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f0/005f0bd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005f0a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0a64.md#insn-005f0a98) · [`005f0ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0a64.md#insn-005f0ab8) · [`005f0af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0a64.md#insn-005f0af4)
- 新版 `005f0ad8`（命令位置の公開資料なし） · `005f0af8`（命令位置の公開資料なし） · `005f0b34`（命令位置の公開資料なし）

~~~diff
- 005f0a98 ["INT_ADD", "register:40f0:8", ["const:5f0a98:8", "const:4:8"]]
- 005f0a98 ["CALL", null, ["callee:005f0bd0:8"]]
+ 005f0ad8 ["INT_ADD", "register:40f0:8", ["const:5f0ad8:8", "const:4:8"]]
+ 005f0ad8 ["CALL", null, ["callee:005f0bd0:8"]]
- 005f0a98 bytes 3e000094
+ 005f0ad8 bytes 3e000094
- 005f0ab8 ["INT_ADD", "register:40f0:8", ["const:5f0ab8:8", "const:4:8"]]
- 005f0ab8 ["CALL", null, ["callee:00c57e90:8"]]
+ 005f0af8 ["INT_ADD", "register:40f0:8", ["const:5f0af8:8", "const:4:8"]]
+ 005f0af8 ["CALL", null, ["callee:00c57e90:8"]]
- 005f0ab8 bytes f69b1994
+ 005f0af8 bytes e69c1994
- 005f0af4 ["INT_ADD", "register:40f0:8", ["const:5f0af4:8", "const:4:8"]]
- 005f0af4 ["CALL", null, ["callee:0043bb20:8"]]
+ 005f0b34 ["INT_ADD", "register:40f0:8", ["const:5f0b34:8", "const:4:8"]]
+ 005f0b34 ["CALL", null, ["callee:0043bb20:8"]]
- 005f0af4 bytes fb2bf997
+ 005f0b34 bytes fb2bf997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb1384502470efbe6e15273ad7b713e7"></a>

### [`005f0b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0b90.md) → [`005f0bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f0/005f0bd0.md) FUN_005f0bd0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`005eda3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005eda3c.md) [`005ee590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ee/005ee590.md) [`005ef56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ef/005ef56c.md) [`005f0a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0a64.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 4件 [`005eda7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005eda7c.md) [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) [`005ef5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ef/005ef5ac.md) [`005f0aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f0/005f0aa4.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005f0c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0b90.md#insn-005f0c14) · [`005f0c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0b90.md#insn-005f0c40)
- 新版 `005f0c54`（命令位置の公開資料なし） · `005f0c80`（命令位置の公開資料なし）

~~~diff
- 005f0c14 ["INT_ADD", "register:40f0:8", ["const:5f0c14:8", "const:4:8"]]
- 005f0c14 ["CALL", null, ["callee:00c58050:8"]]
+ 005f0c54 ["INT_ADD", "register:40f0:8", ["const:5f0c54:8", "const:4:8"]]
+ 005f0c54 ["CALL", null, ["callee:00c58050:8"]]
- 005f0c14 bytes 0f9c1994
+ 005f0c54 bytes ff9c1994
- 005f0c40 ["INT_ADD", "register:40f0:8", ["const:5f0c40:8", "const:4:8"]]
- 005f0c40 ["CALL", null, ["callee:00c58050:8"]]
+ 005f0c80 ["INT_ADD", "register:40f0:8", ["const:5f0c80:8", "const:4:8"]]
+ 005f0c80 ["CALL", null, ["callee:00c58050:8"]]
- 005f0c40 bytes 049c1994
+ 005f0c80 bytes f49c1994
~~~


<a id="compare-1d0597ff790b51c3862a0689e761b8d1"></a>

### [`005f0c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0c94.md) → [`005f0cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f0/005f0cd4.md) FUN_005f0cd4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005f0cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0c94.md#insn-005f0cc4) · [`005f0cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0c94.md#insn-005f0cd8) · [`005f0ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0c94.md#insn-005f0ce0)
- 新版 `005f0d04`（命令位置の公開資料なし） · `005f0d18`（命令位置の公開資料なし） · `005f0d20`（命令位置の公開資料なし）

~~~diff
- 005f0cc4 ["INT_ADD", "register:40f0:8", ["const:5f0cc4:8", "const:4:8"]]
- 005f0cc4 ["CALL", null, ["callee:00c53d00:8"]]
+ 005f0d04 ["INT_ADD", "register:40f0:8", ["const:5f0d04:8", "const:4:8"]]
+ 005f0d04 ["CALL", null, ["callee:00c53d00:8"]]
- 005f0cc4 bytes 078b1994
+ 005f0d04 bytes ff8b1994
- 005f0cd8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005f0cd8 ["INT_ADD", "register:40f0:8", ["const:5f0cd8:8", "const:4:8"]]
- 005f0cd8 ["CALLIND", null, ["register:0:8"]]
+ 005f0d18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005f0d18 ["INT_ADD", "register:40f0:8", ["const:5f0d18:8", "const:4:8"]]
+ 005f0d18 ["CALLIND", null, ["register:0:8"]]
- 005f0cd8 bytes 00013fd6
+ 005f0d18 bytes 00013fd6
- 005f0ce0 ["INT_ADD", "register:40f0:8", ["const:5f0ce0:8", "const:4:8"]]
- 005f0ce0 ["CALL", null, ["callee:00c57e80:8"]]
+ 005f0d20 ["INT_ADD", "register:40f0:8", ["const:5f0d20:8", "const:4:8"]]
+ 005f0d20 ["CALL", null, ["callee:00c57e80:8"]]
- 005f0ce0 bytes 689b1994
+ 005f0d20 bytes 589c1994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f77c3f3268b6b09b8b0903534b95325"></a>

### [`005f0d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0d10.md) → [`005f0d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f0/005f0d50.md) FUN_005f0d50

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`005e94b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e9/005e94b4.md) [`005eda3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005eda3c.md) [`005ee590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ee/005ee590.md) [`005ef56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ef/005ef56c.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 5件 [`005e94f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e9/005e94f4.md) [`005eda7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005eda7c.md) [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) [`005ef5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ef/005ef5ac.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005f0d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0d10.md#insn-005f0d94) · [`005f0dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0d10.md#insn-005f0dc0)
- 新版 `005f0dd4`（命令位置の公開資料なし） · `005f0e00`（命令位置の公開資料なし）

~~~diff
- 005f0d94 ["INT_ADD", "register:40f0:8", ["const:5f0d94:8", "const:4:8"]]
- 005f0d94 ["CALL", null, ["callee:00c58050:8"]]
+ 005f0dd4 ["INT_ADD", "register:40f0:8", ["const:5f0dd4:8", "const:4:8"]]
+ 005f0dd4 ["CALL", null, ["callee:00c58050:8"]]
- 005f0d94 bytes af9b1994
+ 005f0dd4 bytes 9f9c1994
- 005f0dc0 ["INT_ADD", "register:40f0:8", ["const:5f0dc0:8", "const:4:8"]]
- 005f0dc0 ["CALL", null, ["callee:00c58050:8"]]
+ 005f0e00 ["INT_ADD", "register:40f0:8", ["const:5f0e00:8", "const:4:8"]]
+ 005f0e00 ["CALL", null, ["callee:00c58050:8"]]
- 005f0dc0 bytes a49b1994
+ 005f0e00 bytes 949c1994
~~~


<a id="compare-3331b3b04de2688a1210c43a2ee7fa0a"></a>

### [`005f0e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0e14.md) → [`005f0e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f0/005f0e54.md) FUN_005f0e54

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005e94b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e9/005e94b4.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0046eeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`005e94f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e9/005e94f4.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005f0e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0e14.md#insn-005f0e34) · [`005f0e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0e14.md#insn-005f0e6c) · [`005f0e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0e14.md#insn-005f0e74)
- 新版 `005f0e74`（命令位置の公開資料なし） · `005f0eac`（命令位置の公開資料なし） · `005f0eb4`（命令位置の公開資料なし）

~~~diff
- 005f0e34 ["INT_ADD", "register:40f0:8", ["const:5f0e34:8", "const:4:8"]]
- 005f0e34 ["CALL", null, ["callee:00c57e90:8"]]
+ 005f0e74 ["INT_ADD", "register:40f0:8", ["const:5f0e74:8", "const:4:8"]]
+ 005f0e74 ["CALL", null, ["callee:00c57e90:8"]]
- 005f0e34 bytes 179b1994
+ 005f0e74 bytes 079c1994
- 005f0e6c ["INT_ADD", "register:40f0:8", ["const:5f0e6c:8", "const:4:8"]]
- 005f0e6c ["CALL", null, ["callee:0043bb20:8"]]
+ 005f0eac ["INT_ADD", "register:40f0:8", ["const:5f0eac:8", "const:4:8"]]
+ 005f0eac ["CALL", null, ["callee:0043bb20:8"]]
- 005f0e6c bytes 1d2bf997
+ 005f0eac bytes 1d2bf997
- 005f0e74 ["INT_ADD", "register:40f0:8", ["const:5f0e74:8", "const:4:8"]]
- 005f0e74 ["CALL", null, ["callee:0046eef8:8"]]
+ 005f0eb4 ["INT_ADD", "register:40f0:8", ["const:5f0eb4:8", "const:4:8"]]
+ 005f0eb4 ["CALL", null, ["callee:0046eef8:8"]]
- 005f0e74 bytes 11f8f997
+ 005f0eb4 bytes 11f8f997
~~~


<a id="compare-8f1bb0bbf57cfc831467dbff41d20506"></a>

### [`005f0ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0ebc.md) → [`005f0efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f0/005f0efc.md) FUN_005f0efc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005f0ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0ebc.md#insn-005f0ee0) · [`005f0ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0ebc.md#insn-005f0ef0)
- 新版 `005f0f20`（命令位置の公開資料なし） · `005f0f30`（命令位置の公開資料なし）

~~~diff
- 005f0ee0 ["INT_ADD", "register:40f0:8", ["const:5f0ee0:8", "const:4:8"]]
- 005f0ee0 ["CALL", null, ["callee:0046efdc:8"]]
+ 005f0f20 ["INT_ADD", "register:40f0:8", ["const:5f0f20:8", "const:4:8"]]
+ 005f0f20 ["CALL", null, ["callee:0046efdc:8"]]
- 005f0ee0 bytes 2ff8f997
+ 005f0f20 bytes 2ff8f997
- 005f0ef0 ["INT_ADD", "register:40f0:8", ["const:5f0ef0:8", "const:4:8"]]
- 005f0ef0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005f0f30 ["INT_ADD", "register:40f0:8", ["const:5f0f30:8", "const:4:8"]]
+ 005f0f30 ["CALL", null, ["callee:00c57eb0:8"]]
- 005f0ef0 bytes f09a1994
+ 005f0f30 bytes e09b1994
~~~


<a id="compare-dfc43f7f20d4148177750c26c305cf5b"></a>

### [`005f1c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f1/005f1c2c.md) → [`005f1c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f1/005f1c6c.md) FUN_005f1c6c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 1件 [`0046edc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046edc4.md)
- 新版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 1件 [`0046ee04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ee04.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005f1c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f1/005f1c2c.md#insn-005f1c7c)
- 新版 `005f1cbc`（命令位置の公開資料なし）

~~~diff
- 005f1c7c ["INT_ADD", "register:40f0:8", ["const:5f1c7c:8", "const:4:8"]]
- 005f1c7c ["CALL", null, ["callee:0046ee04:8"]]
+ 005f1cbc ["INT_ADD", "register:40f0:8", ["const:5f1cbc:8", "const:4:8"]]
+ 005f1cbc ["CALL", null, ["callee:0046ee04:8"]]
- 005f1c7c bytes 52f4f997
+ 005f1cbc bytes 52f4f997
~~~


<a id="compare-1d1671fceeaf97b28efee3f78bd9e7f3"></a>

### [`005f1d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f1/005f1d9c.md) → [`005f1ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f1/005f1ddc.md) FUN_005f1ddc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 1件 [`0046edc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046edc4.md)
- 新版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 1件 [`0046ee04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ee04.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005f1e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f1/005f1d9c.md#insn-005f1e00)
- 新版 `005f1e40`（命令位置の公開資料なし）

~~~diff
- 005f1e00 ["INT_ADD", "register:40f0:8", ["const:5f1e00:8", "const:4:8"]]
- 005f1e00 ["CALL", null, ["callee:0046ee04:8"]]
+ 005f1e40 ["INT_ADD", "register:40f0:8", ["const:5f1e40:8", "const:4:8"]]
+ 005f1e40 ["CALL", null, ["callee:0046ee04:8"]]
- 005f1e00 bytes f1f3f997
+ 005f1e40 bytes f1f3f997
~~~


<a id="compare-eca8a94d085ace578110a78b2dff8711"></a>

### [`005f1f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f1/005f1f34.md) → [`005f1f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f1/005f1f74.md) FUN_005f1f74

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 1件 [`0046edc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046edc4.md)
- 新版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 1件 [`0046ee04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ee04.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005f1f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f1/005f1f34.md#insn-005f1f98)
- 新版 `005f1fd8`（命令位置の公開資料なし）

~~~diff
- 005f1f98 ["INT_ADD", "register:40f0:8", ["const:5f1f98:8", "const:4:8"]]
- 005f1f98 ["CALL", null, ["callee:0046ee04:8"]]
+ 005f1fd8 ["INT_ADD", "register:40f0:8", ["const:5f1fd8:8", "const:4:8"]]
+ 005f1fd8 ["CALL", null, ["callee:0046ee04:8"]]
- 005f1f98 bytes 8bf3f997
+ 005f1fd8 bytes 8bf3f997
~~~


<a id="compare-95884291e93d5b4afa8d994bc5cce202"></a>

### [`005f2534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f2/005f2534.md) → [`005f2574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f2/005f2574.md) FUN_005f2574

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 2件 [`0046ed4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ed4c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 2件 [`0046ed8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ed8c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005f25a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f2/005f2534.md#insn-005f25a8) · [`005f25e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f2/005f2534.md#insn-005f25e8) · [`005f261c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f2/005f2534.md#insn-005f261c)
- 新版 `005f25e8`（命令位置の公開資料なし） · `005f2628`（命令位置の公開資料なし） · `005f265c`（命令位置の公開資料なし）

~~~diff
- 005f25a8 ["INT_ADD", "register:40f0:8", ["const:5f25a8:8", "const:4:8"]]
- 005f25a8 ["CALL", null, ["callee:0046ed8c:8"]]
+ 005f25e8 ["INT_ADD", "register:40f0:8", ["const:5f25e8:8", "const:4:8"]]
+ 005f25e8 ["CALL", null, ["callee:0046ed8c:8"]]
- 005f25a8 bytes e9f1f997
+ 005f25e8 bytes e9f1f997
- 005f25e8 ["INT_ADD", "register:40f0:8", ["const:5f25e8:8", "const:4:8"]]
- 005f25e8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005f2628 ["INT_ADD", "register:40f0:8", ["const:5f2628:8", "const:4:8"]]
+ 005f2628 ["CALL", null, ["callee:00c57eb0:8"]]
- 005f25e8 bytes 32951994
+ 005f2628 bytes 22961994
- 005f261c ["INT_ADD", "register:40f0:8", ["const:5f261c:8", "const:4:8"]]
- 005f261c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005f265c ["INT_ADD", "register:40f0:8", ["const:5f265c:8", "const:4:8"]]
+ 005f265c ["CALL", null, ["callee:00c57eb0:8"]]
- 005f261c bytes 25951994
+ 005f265c bytes 15961994
~~~


<a id="compare-babae7daa7ade0c9e5205775a35617c5"></a>

### [`005f2d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f2/005f2d28.md) → [`005f2d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f2/005f2d68.md) FUN_005f2d68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 27件 [`0046ed4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ed4c.md) [`0046edc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046edc4.md) [`00707d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707d30.md) [`0070deb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070d/0070deb0.md) [`00af5f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5f08.md)
- 新版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 27件 [`0046ed8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ed8c.md) [`0046ee04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ee04.md) [`00707d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707d70.md) [`0070def0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070d/0070def0.md) [`00af6330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6330.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005f2dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f2/005f2d28.md#insn-005f2dac) · [`005f2db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f2/005f2d28.md#insn-005f2db8) · [`005f2dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f2/005f2d28.md#insn-005f2dd0)
- 新版 `005f2dec`（命令位置の公開資料なし） · `005f2df8`（命令位置の公開資料なし） · `005f2e10`（命令位置の公開資料なし）

~~~diff
- 005f2dac ["INT_ADD", "register:40f0:8", ["const:5f2dac:8", "const:4:8"]]
- 005f2dac ["CALL", null, ["callee:00afb904:8"]]
+ 005f2dec ["INT_ADD", "register:40f0:8", ["const:5f2dec:8", "const:4:8"]]
+ 005f2dec ["CALL", null, ["callee:00afb904:8"]]
- 005f2dac bytes cc211494
+ 005f2dec bytes c6221494
- 005f2db8 ["INT_ADD", "register:40f0:8", ["const:5f2db8:8", "const:4:8"]]
- 005f2db8 ["CALL", null, ["callee:00afc65c:8"]]
+ 005f2df8 ["INT_ADD", "register:40f0:8", ["const:5f2df8:8", "const:4:8"]]
+ 005f2df8 ["CALL", null, ["callee:00afc65c:8"]]
- 005f2db8 bytes 1f251494
+ 005f2df8 bytes 19261494
- 005f2dd0 ["INT_ADD", "register:40f0:8", ["const:5f2dd0:8", "const:4:8"]]
- 005f2dd0 ["CALL", null, ["callee:00afc6e8:8"]]
+ 005f2e10 ["INT_ADD", "register:40f0:8", ["const:5f2e10:8", "const:4:8"]]
+ 005f2e10 ["CALL", null, ["callee:00afc6e8:8"]]
- 005f2dd0 bytes 3c251494
+ 005f2e10 bytes 36261494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ac1e92474f08199c7397f239918de38"></a>

### [`005f689c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f6/005f689c.md) → [`005f68dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f6/005f68dc.md) FUN_005f68dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005f5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f5/005f5750.md) [`007fb1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fb/007fb1f0.md) [`00ae0e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0e64.md) · 呼出先 3件 [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046aed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aed8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 3件 [`005f5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5790.md) [`007fb230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fb230.md) [`00ae128c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae1/00ae128c.md) · 呼出先 3件 [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046af18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af18.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005f69c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f6/005f689c.md#insn-005f69c0) · [`005f6aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f6/005f689c.md#insn-005f6aa0) · [`005f6ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f6/005f689c.md#insn-005f6ac4)
- 新版 `005f6a00`（命令位置の公開資料なし） · `005f6ae0`（命令位置の公開資料なし） · `005f6b04`（命令位置の公開資料なし）

~~~diff
- 005f69c0 ["INT_ADD", "register:40f0:8", ["const:5f69c0:8", "const:4:8"]]
- 005f69c0 ["CALL", null, ["callee:0046af18:8"]]
+ 005f6a00 ["INT_ADD", "register:40f0:8", ["const:5f6a00:8", "const:4:8"]]
+ 005f6a00 ["CALL", null, ["callee:0046af18:8"]]
- 005f69c0 bytes 46d1f997
+ 005f6a00 bytes 46d1f997
- 005f6aa0 ["INT_ADD", "register:40f0:8", ["const:5f6aa0:8", "const:4:8"]]
- 005f6aa0 ["CALL", null, ["callee:0046af18:8"]]
+ 005f6ae0 ["INT_ADD", "register:40f0:8", ["const:5f6ae0:8", "const:4:8"]]
+ 005f6ae0 ["CALL", null, ["callee:0046af18:8"]]
- 005f6aa0 bytes 0ed1f997
+ 005f6ae0 bytes 0ed1f997
- 005f6ac4 ["INT_ADD", "register:40f0:8", ["const:5f6ac4:8", "const:4:8"]]
- 005f6ac4 ["CALL", null, ["callee:00469c04:8"]]
+ 005f6b04 ["INT_ADD", "register:40f0:8", ["const:5f6b04:8", "const:4:8"]]
+ 005f6b04 ["CALL", null, ["callee:00469c04:8"]]
- 005f6ac4 bytes 40ccf997
+ 005f6b04 bytes 40ccf997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae27b9eeb449b0208cf06e5d66eca64b"></a>

### [`005f94cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f9/005f94cc.md) → [`005f950c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f9/005f950c.md) FUN_005f950c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005f94ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f9/005f94cc.md#insn-005f94ec)
- 新版 `005f952c`（命令位置の公開資料なし）

~~~diff
- 005f94ec ["INT_ADD", "register:40f0:8", ["const:5f94ec:8", "const:4:8"]]
- 005f94ec ["CALL", null, ["callee:005c179c:8"]]
+ 005f952c ["INT_ADD", "register:40f0:8", ["const:5f952c:8", "const:4:8"]]
+ 005f952c ["CALL", null, ["callee:005c179c:8"]]
- 005f94ec bytes 9c20ff97
+ 005f952c bytes 9c20ff97
~~~


<a id="compare-2297c8b51c7165b8fd637e04cd97b01e"></a>

### [`005fc294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fc/005fc294.md) → [`005fc2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fc/005fc2d4.md) FUN_005fc2d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005fb8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fb/005fb8fc.md) [`00653560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/00653560.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`005fb93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fb/005fb93c.md) [`006535a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00653/006535a0.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005fc2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fc/005fc294.md#insn-005fc2fc) · [`005fc338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fc/005fc294.md#insn-005fc338)
- 新版 `005fc33c`（命令位置の公開資料なし） · `005fc378`（命令位置の公開資料なし）

~~~diff
- 005fc2fc ["INT_ADD", "register:40f0:8", ["const:5fc2fc:8", "const:4:8"]]
- 005fc2fc ["CALL", null, ["callee:00c57e90:8"]]
+ 005fc33c ["INT_ADD", "register:40f0:8", ["const:5fc33c:8", "const:4:8"]]
+ 005fc33c ["CALL", null, ["callee:00c57e90:8"]]
- 005fc2fc bytes e56d1994
+ 005fc33c bytes d56e1994
- 005fc338 ["INT_ADD", "register:40f0:8", ["const:5fc338:8", "const:4:8"]]
- 005fc338 ["CALL", null, ["callee:0043bba4:8"]]
+ 005fc378 ["INT_ADD", "register:40f0:8", ["const:5fc378:8", "const:4:8"]]
+ 005fc378 ["CALL", null, ["callee:0043bba4:8"]]
- 005fc338 bytes 0bfef897
+ 005fc378 bytes 0bfef897
~~~


<a id="compare-3d9d2ff2e6d4ee1cfb51dd1ebcf4d931"></a>

### [`005fe1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe1b0.md) → [`005fe1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe1f0.md) FUN_005fe1f0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005f5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f5/005f5750.md) [`005fe1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe1b0.md) · 呼出先 2件 [`005fe1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe1b0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`005f5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5790.md) [`005fe1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe1f0.md) · 呼出先 2件 [`005fe1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe1f0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005fe1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe1b0.md#insn-005fe1d0) · [`005fe1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe1b0.md#insn-005fe1dc)
- 新版 `005fe210`（命令位置の公開資料なし） · `005fe21c`（命令位置の公開資料なし）

~~~diff
- 005fe1d0 ["INT_ADD", "register:40f0:8", ["const:5fe1d0:8", "const:4:8"]]
- 005fe1d0 ["CALL", null, ["local:b0:8"]]
+ 005fe210 ["INT_ADD", "register:40f0:8", ["const:5fe210:8", "const:4:8"]]
+ 005fe210 ["CALL", null, ["local:b0:8"]]
- 005fe1d0 bytes f8ffff97
+ 005fe210 bytes f8ffff97
- 005fe1dc ["INT_ADD", "register:40f0:8", ["const:5fe1dc:8", "const:4:8"]]
- 005fe1dc ["CALL", null, ["local:b0:8"]]
+ 005fe21c ["INT_ADD", "register:40f0:8", ["const:5fe21c:8", "const:4:8"]]
+ 005fe21c ["CALL", null, ["local:b0:8"]]
- 005fe1dc bytes f5ffff97
+ 005fe21c bytes f5ffff97
~~~


<a id="compare-ef27ca53343def82f0e5b00008639335"></a>

### [`005fe258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe258.md) → [`005fe298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe298.md) FUN_005fe298

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`005f9670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f9/005f9670.md) [`005fe258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe258.md) [`006bf7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bf/006bf7f4.md) [`007141dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/007141dc.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 2件 [`005fe258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe258.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 7件 [`005f96b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f9/005f96b0.md) [`005fe298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe298.md) [`006bf834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bf/006bf834.md) [`0071421c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/0071421c.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 2件 [`005fe298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe298.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005fe278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe258.md#insn-005fe278) · [`005fe284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe258.md#insn-005fe284)
- 新版 `005fe2b8`（命令位置の公開資料なし） · `005fe2c4`（命令位置の公開資料なし）

~~~diff
- 005fe278 ["INT_ADD", "register:40f0:8", ["const:5fe278:8", "const:4:8"]]
- 005fe278 ["CALL", null, ["local:b0:8"]]
+ 005fe2b8 ["INT_ADD", "register:40f0:8", ["const:5fe2b8:8", "const:4:8"]]
+ 005fe2b8 ["CALL", null, ["local:b0:8"]]
- 005fe278 bytes f8ffff97
+ 005fe2b8 bytes f8ffff97
- 005fe284 ["INT_ADD", "register:40f0:8", ["const:5fe284:8", "const:4:8"]]
- 005fe284 ["CALL", null, ["local:b0:8"]]
+ 005fe2c4 ["INT_ADD", "register:40f0:8", ["const:5fe2c4:8", "const:4:8"]]
+ 005fe2c4 ["CALL", null, ["local:b0:8"]]
- 005fe284 bytes f5ffff97
+ 005fe2c4 bytes f5ffff97
~~~


<a id="compare-dc798395b05ed203055ecd85eb52191a"></a>

### [`00604c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604c88.md) → [`00604cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00604/00604cc8.md) FUN_00604cc8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 3件 [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00604cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604c88.md#insn-00604cac) · [`00604cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604c88.md#insn-00604cf4) · [`00604d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604c88.md#insn-00604d14)
- 新版 `00604cec`（命令位置の公開資料なし） · `00604d34`（命令位置の公開資料なし） · `00604d54`（命令位置の公開資料なし）

~~~diff
- 00604cac ["INT_ADD", "register:40f0:8", ["const:604cac:8", "const:4:8"]]
- 00604cac ["CALL", null, ["callee:00c57fe0:8"]]
+ 00604cec ["INT_ADD", "register:40f0:8", ["const:604cec:8", "const:4:8"]]
+ 00604cec ["CALL", null, ["callee:00c57fe0:8"]]
- 00604cac bytes cd4b1994
+ 00604cec bytes bd4c1994
- 00604cf4 ["INT_ADD", "register:40f0:8", ["const:604cf4:8", "const:4:8"]]
- 00604cf4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00604d34 ["INT_ADD", "register:40f0:8", ["const:604d34:8", "const:4:8"]]
+ 00604d34 ["CALL", null, ["callee:00c57e90:8"]]
- 00604cf4 bytes 674b1994
+ 00604d34 bytes 574c1994
- 00604d14 ["INT_ADD", "register:40f0:8", ["const:604d14:8", "const:4:8"]]
- 00604d14 ["CALL", null, ["callee:00c57f40:8"]]
+ 00604d54 ["INT_ADD", "register:40f0:8", ["const:604d54:8", "const:4:8"]]
+ 00604d54 ["CALL", null, ["callee:00c57f40:8"]]
- 00604d14 bytes 8b4b1994
+ 00604d54 bytes 7b4c1994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cbc4c1f0b993236f348766a6af2cb20"></a>

### [`00604d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604d50.md) → [`00604d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00604/00604d90.md) FUN_00604d90

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 11件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`0073d764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073d/0073d764.md) [`0075b984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b984.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 11件 [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`0073d7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073d/0073d7a4.md) [`0075b9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075b/0075b9c4.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00604db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604d50.md#insn-00604db8) · [`00604dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604d50.md#insn-00604dec)
- 新版 `00604df8`（命令位置の公開資料なし） · `00604e2c`（命令位置の公開資料なし）

~~~diff
- 00604db8 ["INT_ADD", "register:40f0:8", ["const:604db8:8", "const:4:8"]]
- 00604db8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00604df8 ["INT_ADD", "register:40f0:8", ["const:604df8:8", "const:4:8"]]
+ 00604df8 ["CALL", null, ["callee:00c57e90:8"]]
- 00604db8 bytes 364b1994
+ 00604df8 bytes 264c1994
- 00604dec ["INT_ADD", "register:40f0:8", ["const:604dec:8", "const:4:8"]]
- 00604dec ["CALL", null, ["callee:0043bba4:8"]]
+ 00604e2c ["INT_ADD", "register:40f0:8", ["const:604e2c:8", "const:4:8"]]
+ 00604e2c ["CALL", null, ["callee:0043bba4:8"]]
- 00604dec bytes 5edbf897
+ 00604e2c bytes 5edbf897
~~~


<a id="compare-8ab3f84111bb7ebd12f44655d8600c06"></a>

### [`00604e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604e5c.md) → [`00604e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00604/00604e9c.md) FUN_00604e9c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 3件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 2件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 3件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00604e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604e5c.md#insn-00604e90) · [`00604ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604e5c.md#insn-00604ea8) · [`00604ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604e5c.md#insn-00604ec4)
- 新版 `00604ed0`（命令位置の公開資料なし） · `00604ee8`（命令位置の公開資料なし） · `00604f04`（命令位置の公開資料なし）

~~~diff
- 00604e90 ["INT_ADD", "register:40f0:8", ["const:604e90:8", "const:4:8"]]
- 00604e90 ["CALL", null, ["callee:00c57e90:8"]]
+ 00604ed0 ["INT_ADD", "register:40f0:8", ["const:604ed0:8", "const:4:8"]]
+ 00604ed0 ["CALL", null, ["callee:00c57e90:8"]]
- 00604e90 bytes 004b1994
+ 00604ed0 bytes f04b1994
- 00604ea8 ["INT_ADD", "register:40f0:8", ["const:604ea8:8", "const:4:8"]]
- 00604ea8 ["CALL", null, ["callee:00c57f40:8"]]
+ 00604ee8 ["INT_ADD", "register:40f0:8", ["const:604ee8:8", "const:4:8"]]
+ 00604ee8 ["CALL", null, ["callee:00c57f40:8"]]
- 00604ea8 bytes 264b1994
+ 00604ee8 bytes 164c1994
- 00604ec4 ["INT_ADD", "register:40f0:8", ["const:604ec4:8", "const:4:8"]]
- 00604ec4 ["CALL", null, ["callee:00470840:8"]]
+ 00604f04 ["INT_ADD", "register:40f0:8", ["const:604f04:8", "const:4:8"]]
+ 00604f04 ["CALL", null, ["callee:00470840:8"]]
- 00604ec4 bytes 4faef997
+ 00604f04 bytes 4faef997
~~~


<a id="compare-c28f93783d39fd01b6df6faad21ec24e"></a>

### [`00604ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604ee8.md) → [`00604f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00604/00604f28.md) FUN_00604f28

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00720050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00720/00720050.md) [`009470d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00947/009470d0.md) · 呼出先 1件 [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md)
- 新版 呼出元 2件 [`00720090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00720/00720090.md) [`0094726c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00947/0094726c.md) · 呼出先 1件 [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00604ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604ee8.md#insn-00604ef8)
- 新版 `00604f38`（命令位置の公開資料なし）

~~~diff
- 00604ef8 ["INT_ADD", "register:40f0:8", ["const:604ef8:8", "const:4:8"]]
- 00604ef8 ["CALL", null, ["callee:00c5a830:8"]]
+ 00604f38 ["INT_ADD", "register:40f0:8", ["const:604f38:8", "const:4:8"]]
+ 00604f38 ["CALL", null, ["callee:00c5a830:8"]]
- 00604ef8 bytes 4e551994
+ 00604f38 bytes 3e561994
~~~


<a id="compare-f4be09217b3853ba2739b9c171204c07"></a>

### [`00604f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604f08.md) → [`00604f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00604/00604f48.md) FUN_00604f48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) · 呼出先 1件 [`00615c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/00615c90.md)
- 新版 呼出元 1件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) · 呼出先 1件 [`00615cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615cd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00604f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604f08.md#insn-00604f50)
- 新版 `00604f90`（命令位置の公開資料なし）

~~~diff
- 00604f50 ["INT_ADD", "register:40f0:8", ["const:604f50:8", "const:4:8"]]
- 00604f50 ["CALL", null, ["callee:00615cd0:8"]]
+ 00604f90 ["INT_ADD", "register:40f0:8", ["const:604f90:8", "const:4:8"]]
+ 00604f90 ["CALL", null, ["callee:00615cd0:8"]]
- 00604f50 bytes 50430094
+ 00604f90 bytes 50430094
~~~


<a id="compare-93d37d72a2c54a7b070c6dc8787cd235"></a>

### [`00606448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606448.md) → [`00606488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606488.md) FUN_00606488

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 11件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 2件 [`007441c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/007441c8.md) [`00802678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md)
- 新版 呼出元 11件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 2件 [`00744208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/00744208.md) [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00606460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606448.md#insn-00606460) · [`00606480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606448.md#insn-00606480)
- 新版 `006064a0`（命令位置の公開資料なし） · `006064c0`（命令位置の公開資料なし）

~~~diff
- 00606460 ["INT_ADD", "register:40f0:8", ["const:606460:8", "const:4:8"]]
- 00606460 ["CALL", null, ["callee:00744208:8"]]
+ 006064a0 ["INT_ADD", "register:40f0:8", ["const:6064a0:8", "const:4:8"]]
+ 006064a0 ["CALL", null, ["callee:00744208:8"]]
- 00606460 bytes 5af70494
+ 006064a0 bytes 5af70494
- 00606480 ["INT_ADD", "register:40f0:8", ["const:606480:8", "const:4:8"]]
- 00606480 ["CALL", null, ["callee:008026b8:8"]]
+ 006064c0 ["INT_ADD", "register:40f0:8", ["const:6064c0:8", "const:4:8"]]
+ 006064c0 ["CALL", null, ["callee:008026b8:8"]]
- 00606480 bytes 7ef00794
+ 006064c0 bytes 7ef00794
~~~


