# v16.0.0 → v16.0.1 · 要調査の変更候補 (15)

[一覧の目次](README.md)

<a id="compare-f4938b92ebb6848fc07c9eedb66d6265"></a>

### [`00597468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597468.md) → [`005974a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005974a8.md) FUN_005974a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00597478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597468.md#insn-00597478)
- 新版 `005974b8`（命令位置の公開資料なし）

~~~diff
- 00597478 ["INT_ADD", "register:40f0:8", ["const:597478:8", "const:4:8"]]
- 00597478 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005974b8 ["INT_ADD", "register:40f0:8", ["const:5974b8:8", "const:4:8"]]
+ 005974b8 ["CALL", null, ["callee:00c57ea0:8"]]
- 00597478 bytes 8a011b94
+ 005974b8 bytes 7a021b94
~~~


<a id="compare-f4cc2585c761a494ac03f7ced81db3e1"></a>

### [`005974c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005974c4.md) → [`00597504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597504.md) FUN_00597504

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`005a1430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1430.md) [`0076621c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/0076621c.md) [`00767108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767108.md) [`00798e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798e60.md) [`00b0e654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e654.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005971dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005971dc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 5件 [`005a1470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1470.md) [`0076625c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00766/0076625c.md) [`00767148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767148.md) [`00798ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798ea0.md) [`00b0ea7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0ea7c.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0059721c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059721c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00597544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005974c4.md#insn-00597544) · [`00597580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005974c4.md#insn-00597580) · [`00597594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005974c4.md#insn-00597594)
- 新版 `00597584`（命令位置の公開資料なし） · `005975c0`（命令位置の公開資料なし） · `005975d4`（命令位置の公開資料なし）

~~~diff
- 00597544 ["INT_ADD", "register:40f0:8", ["const:597544:8", "const:4:8"]]
- 00597544 ["CALL", null, ["callee:00c57e90:8"]]
+ 00597584 ["INT_ADD", "register:40f0:8", ["const:597584:8", "const:4:8"]]
+ 00597584 ["CALL", null, ["callee:00c57e90:8"]]
- 00597544 bytes 53011b94
+ 00597584 bytes 43021b94
- 00597580 ["INT_ADD", "register:40f0:8", ["const:597580:8", "const:4:8"]]
- 00597580 ["CALL", null, ["callee:00c58000:8"]]
+ 005975c0 ["INT_ADD", "register:40f0:8", ["const:5975c0:8", "const:4:8"]]
+ 005975c0 ["CALL", null, ["callee:00c58000:8"]]
- 00597580 bytes a0011b94
+ 005975c0 bytes 90021b94
- 00597594 ["INT_ADD", "register:40f0:8", ["const:597594:8", "const:4:8"]]
- 00597594 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005975d4 ["INT_ADD", "register:40f0:8", ["const:5975d4:8", "const:4:8"]]
+ 005975d4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00597594 bytes 47011b94
+ 005975d4 bytes 37021b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbd94406cd80cb85994797a4fef04888"></a>

### [`0059761c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059761c.md) → [`0059765c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059765c.md) FUN_0059765c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 18件 [`0043f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f8dc.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`00451e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451e98.md) [`00479d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479d88.md) [`00574b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574b64.md) · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bf0.md) [`00c59f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f20.md)
- 新版 呼出元 18件 [`0043f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f91c.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`00451ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451ed8.md) [`00479dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479dc8.md) [`00574ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574ba4.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ff0.md) [`00c5a320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00597640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059761c.md#insn-00597640) · [`00597660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059761c.md#insn-00597660) · [`005976a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059761c.md#insn-005976a4)
- 新版 `00597680`（命令位置の公開資料なし） · `005976a0`（命令位置の公開資料なし） · `005976e4`（命令位置の公開資料なし）

~~~diff
- 00597640 ["INT_ADD", "register:40f0:8", ["const:597640:8", "const:4:8"]]
- 00597640 ["CALL", null, ["callee:00c57ff0:8"]]
+ 00597680 ["INT_ADD", "register:40f0:8", ["const:597680:8", "const:4:8"]]
+ 00597680 ["CALL", null, ["callee:00c57ff0:8"]]
- 00597640 bytes 6c011b94
+ 00597680 bytes 5c021b94
- 00597660 ["INT_ADD", "register:40f0:8", ["const:597660:8", "const:4:8"]]
- 00597660 ["CALL", null, ["callee:00c5a320:8"]]
+ 005976a0 ["INT_ADD", "register:40f0:8", ["const:5976a0:8", "const:4:8"]]
+ 005976a0 ["CALL", null, ["callee:00c5a320:8"]]
- 00597660 bytes 300a1b94
+ 005976a0 bytes 200b1b94
- 005976a4 ["INT_ADD", "register:40f0:8", ["const:5976a4:8", "const:4:8"]]
- 005976a4 ["CALL", null, ["callee:00c57ee0:8"]]
+ 005976e4 ["INT_ADD", "register:40f0:8", ["const:5976e4:8", "const:4:8"]]
+ 005976e4 ["CALL", null, ["callee:00c57ee0:8"]]
- 005976a4 bytes 0f011b94
+ 005976e4 bytes ff011b94
~~~


<a id="compare-4a5ee967dff5a212a5b32e3b50ed27ea"></a>

### [`005976a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005976a8.md) → [`005976e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005976e8.md) FUN_005976e8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 17件 [`005712a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005712a0.md) [`005794e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00579/005794e4.md) [`0062c080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062c/0062c080.md) [`0069a4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a4c4.md) [`0075d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md) · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c585b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585b0.md) [`00c59f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f20.md)
- 新版 呼出元 17件 [`005712e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005712e0.md) [`00579524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00579/00579524.md) [`0062c0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062c/0062c0c0.md) [`0069a504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069a/0069a504.md) [`0075d75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075d/0075d75c.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c589b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589b0.md) [`00c5a320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005976e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005976a8.md#insn-005976e8) · [`005976f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005976a8.md#insn-005976f0) · [`00597734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005976a8.md#insn-00597734)
- 新版 `00597728`（命令位置の公開資料なし） · `00597730`（命令位置の公開資料なし） · `00597774`（命令位置の公開資料なし）

~~~diff
- 005976e8 ["INT_ADD", "register:40f0:8", ["const:5976e8:8", "const:4:8"]]
- 005976e8 ["CALL", null, ["callee:00c589b0:8"]]
+ 00597728 ["INT_ADD", "register:40f0:8", ["const:597728:8", "const:4:8"]]
+ 00597728 ["CALL", null, ["callee:00c589b0:8"]]
- 005976e8 bytes b2031b94
+ 00597728 bytes a2041b94
- 005976f0 ["INT_ADD", "register:40f0:8", ["const:5976f0:8", "const:4:8"]]
- 005976f0 ["CALL", null, ["callee:00c5a320:8"]]
+ 00597730 ["INT_ADD", "register:40f0:8", ["const:597730:8", "const:4:8"]]
+ 00597730 ["CALL", null, ["callee:00c5a320:8"]]
- 005976f0 bytes 0c0a1b94
+ 00597730 bytes fc0a1b94
- 00597734 ["INT_ADD", "register:40f0:8", ["const:597734:8", "const:4:8"]]
- 00597734 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00597774 ["INT_ADD", "register:40f0:8", ["const:597774:8", "const:4:8"]]
+ 00597774 ["CALL", null, ["callee:00c57ee0:8"]]
- 00597734 bytes eb001b94
+ 00597774 bytes db011b94
~~~


<a id="compare-5f0a2abf724697be6f0bafee18aa0606"></a>

### [`00597738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597738.md) → [`00597778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597778.md) FUN_00597778

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 20件 [`004808bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004808bc.md) [`0062c080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062c/0062c080.md) [`006373e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00637/006373e0.md) [`0069a4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a4c4.md) [`0075d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md) · 呼出先 1件 [`00c59f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f30.md)
- 新版 呼出元 20件 [`004808fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004808fc.md) [`0062c0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062c/0062c0c0.md) [`00637420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00637/00637420.md) [`0069a504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069a/0069a504.md) [`0075d75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075d/0075d75c.md) · 呼出先 1件 [`00c5a330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a330.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00597768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597738.md#insn-00597768)
- 新版 `005977a8`（命令位置の公開資料なし）

~~~diff
- 00597768 ["INT_ADD", "register:40f0:8", ["const:597768:8", "const:4:8"]]
- 00597768 ["CALL", null, ["callee:00c5a330:8"]]
+ 005977a8 ["INT_ADD", "register:40f0:8", ["const:5977a8:8", "const:4:8"]]
+ 005977a8 ["CALL", null, ["callee:00c5a330:8"]]
- 00597768 bytes f2091b94
+ 005977a8 bytes e20a1b94
~~~


<a id="compare-8fc82ebd9a956f128f58da3a07963136"></a>

### [`00597dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597dc8.md) → [`00597e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597e08.md) FUN_00597e08

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00476688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md) [`0075e548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075e548.md) [`008d6b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d6/008d6b44.md) [`008e465c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e465c.md) [`00b2f5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f5e4.md) · 呼出先 2件 [`00c59f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f30.md) [`00c59f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f40.md)
- 新版 呼出元 5件 [`004766c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md) [`0075e588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075e588.md) [`008d6ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6ce0.md) [`008e47f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e4/008e47f8.md) [`00b2fa0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2fa0c.md) · 呼出先 2件 [`00c5a330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a330.md) [`00c5a340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00597dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597dc8.md#insn-00597dd8) · [`00597de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597dc8.md#insn-00597de4)
- 新版 `00597e18`（命令位置の公開資料なし） · `00597e24`（命令位置の公開資料なし）

~~~diff
- 00597dd8 ["INT_ADD", "register:40f0:8", ["const:597dd8:8", "const:4:8"]]
- 00597dd8 ["CALL", null, ["callee:00c5a330:8"]]
+ 00597e18 ["INT_ADD", "register:40f0:8", ["const:597e18:8", "const:4:8"]]
+ 00597e18 ["CALL", null, ["callee:00c5a330:8"]]
- 00597dd8 bytes 56081b94
+ 00597e18 bytes 46091b94
- 00597de4 ["INT_ADD", "register:40f0:8", ["const:597de4:8", "const:4:8"]]
- 00597de4 ["CALL", null, ["callee:00c5a340:8"]]
+ 00597e24 ["INT_ADD", "register:40f0:8", ["const:597e24:8", "const:4:8"]]
+ 00597e24 ["CALL", null, ["callee:00c5a340:8"]]
- 00597de4 bytes 57081b94
+ 00597e24 bytes 47091b94
~~~


<a id="compare-03032482ded03d7b71283f1870cfd124"></a>

### [`00597e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e08.md) → [`00597e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597e48.md) FUN_00597e48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 16件 [`00476688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md) [`007a0f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a0/007a0f60.md) [`007a10d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a1/007a10d0.md) [`007abbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007abbe4.md) [`007aca8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007aca8c.md) · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bf0.md) [`00c59f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f20.md)
- 新版 呼出元 16件 [`004766c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md) [`007a0fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0fa0.md) [`007a1110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1110.md) [`007abc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007abc24.md) [`007acacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007acacc.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ff0.md) [`00c5a320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00597e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e08.md#insn-00597e2c) · [`00597e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e08.md#insn-00597e4c) · [`00597e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e08.md#insn-00597e78)
- 新版 `00597e6c`（命令位置の公開資料なし） · `00597e8c`（命令位置の公開資料なし） · `00597eb8`（命令位置の公開資料なし）

~~~diff
- 00597e2c ["INT_ADD", "register:40f0:8", ["const:597e2c:8", "const:4:8"]]
- 00597e2c ["CALL", null, ["callee:00c57ff0:8"]]
+ 00597e6c ["INT_ADD", "register:40f0:8", ["const:597e6c:8", "const:4:8"]]
+ 00597e6c ["CALL", null, ["callee:00c57ff0:8"]]
- 00597e2c bytes 71ff1a94
+ 00597e6c bytes 61001b94
- 00597e4c ["INT_ADD", "register:40f0:8", ["const:597e4c:8", "const:4:8"]]
- 00597e4c ["CALL", null, ["callee:00c5a320:8"]]
+ 00597e8c ["INT_ADD", "register:40f0:8", ["const:597e8c:8", "const:4:8"]]
+ 00597e8c ["CALL", null, ["callee:00c5a320:8"]]
- 00597e4c bytes 35081b94
+ 00597e8c bytes 25091b94
- 00597e78 ["INT_ADD", "register:40f0:8", ["const:597e78:8", "const:4:8"]]
- 00597e78 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00597eb8 ["INT_ADD", "register:40f0:8", ["const:597eb8:8", "const:4:8"]]
+ 00597eb8 ["CALL", null, ["callee:00c57ee0:8"]]
- 00597e78 bytes 1aff1a94
+ 00597eb8 bytes 0a001b94
~~~


<a id="compare-64928673a78c0ef60dd69614feac5473"></a>

### [`00598cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598cb4.md) → [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) FUN_00598cf4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 17件 [`005b1de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1de4.md) [`005b271c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b271c.md) [`005b35b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b35b8.md) [`005b3b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3b34.md) [`005b3fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3fe0.md) · 呼出先 2件 [`0059a2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a2f0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 17件 [`005b1e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1e24.md) [`005b275c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b275c.md) [`005b35f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b35f8.md) [`005b3b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3b74.md) [`005b4020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4020.md) · 呼出先 2件 [`0059a330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a330.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00598cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598cb4.md#insn-00598cf0) · [`00598d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598cb4.md#insn-00598d1c) · [`00598d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598cb4.md#insn-00598d2c)
- 新版 `00598d30`（命令位置の公開資料なし） · `00598d5c`（命令位置の公開資料なし） · `00598d6c`（命令位置の公開資料なし）

~~~diff
- 00598cf0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00598cf0 ["INT_ADD", "register:40f0:8", ["const:598cf0:8", "const:4:8"]]
- 00598cf0 ["CALLIND", null, ["register:0:8"]]
+ 00598d30 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00598d30 ["INT_ADD", "register:40f0:8", ["const:598d30:8", "const:4:8"]]
+ 00598d30 ["CALLIND", null, ["register:0:8"]]
- 00598cf0 bytes 20013fd6
+ 00598d30 bytes 20013fd6
- 00598d1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00598d1c ["INT_ADD", "register:40f0:8", ["const:598d1c:8", "const:4:8"]]
- 00598d1c ["CALLIND", null, ["register:0:8"]]
+ 00598d5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00598d5c ["INT_ADD", "register:40f0:8", ["const:598d5c:8", "const:4:8"]]
+ 00598d5c ["CALLIND", null, ["register:0:8"]]
- 00598d1c bytes 00013fd6
+ 00598d5c bytes 00013fd6
- 00598d2c ["INT_ADD", "register:40f0:8", ["const:598d2c:8", "const:4:8"]]
- 00598d2c ["CALL", null, ["callee:0059a330:8"]]
+ 00598d6c ["INT_ADD", "register:40f0:8", ["const:598d6c:8", "const:4:8"]]
+ 00598d6c ["CALL", null, ["callee:0059a330:8"]]
- 00598d2c bytes 71050094
+ 00598d6c bytes 71050094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37dbc7b12fa2e4901a2edb3175e8026b"></a>

### [`0059918c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/0059918c.md) → [`005991cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/005991cc.md) FUN_005991cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005ad7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad7a0.md) [`005ae8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae8a4.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`005ad7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md) [`005ae8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae8e4.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005991a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/0059918c.md#insn-005991a8) · [`005991c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/0059918c.md#insn-005991c8)
- 新版 `005991e8`（命令位置の公開資料なし） · `00599208`（命令位置の公開資料なし）

~~~diff
- 005991a8 ["INT_ADD", "register:40f0:8", ["const:5991a8:8", "const:4:8"]]
- 005991a8 ["CALL", null, ["callee:00c53d00:8"]]
+ 005991e8 ["INT_ADD", "register:40f0:8", ["const:5991e8:8", "const:4:8"]]
+ 005991e8 ["CALL", null, ["callee:00c53d00:8"]]
- 005991a8 bytes cee91a94
+ 005991e8 bytes c6ea1a94
- 005991c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005991c8 ["INT_ADD", "register:40f0:8", ["const:5991c8:8", "const:4:8"]]
- 005991c8 ["CALLIND", null, ["register:0:8"]]
+ 00599208 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00599208 ["INT_ADD", "register:40f0:8", ["const:599208:8", "const:4:8"]]
+ 00599208 ["CALLIND", null, ["register:0:8"]]
- 005991c8 bytes 00013fd6
+ 00599208 bytes 00013fd6
~~~


<a id="compare-b11b0271485f5dff530365c126995e34"></a>

### [`005991dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005991dc.md) → [`0059921c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/0059921c.md) FUN_0059921c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00598d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598d80.md) · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00598dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598dc0.md) · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005991f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005991dc.md#insn-005991f8)
- 新版 `00599238`（命令位置の公開資料なし）

~~~diff
- 005991f8 ["INT_ADD", "register:40f0:8", ["const:5991f8:8", "const:4:8"]]
- 005991f8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00599238 ["INT_ADD", "register:40f0:8", ["const:599238:8", "const:4:8"]]
+ 00599238 ["CALL", null, ["callee:00c57eb0:8"]]
- 005991f8 bytes 2efa1a94
+ 00599238 bytes 1efb1a94
~~~


<a id="compare-ecf5ccd06a67763847318c644ee100a7"></a>

### [`00599610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599610.md) → [`00599650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599650.md) FUN_00599650

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059962c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599610.md#insn-0059962c) · [`00599640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599610.md#insn-00599640) · [`00599660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599610.md#insn-00599660)
- 新版 `0059966c`（命令位置の公開資料なし） · `00599680`（命令位置の公開資料なし） · `005996a0`（命令位置の公開資料なし）

~~~diff
- 0059962c ["INT_ADD", "register:40f0:8", ["const:59962c:8", "const:4:8"]]
- 0059962c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059966c ["INT_ADD", "register:40f0:8", ["const:59966c:8", "const:4:8"]]
+ 0059966c ["CALL", null, ["callee:00c57eb0:8"]]
- 0059962c bytes 21f91a94
+ 0059966c bytes 11fa1a94
- 00599640 ["INT_ADD", "register:40f0:8", ["const:599640:8", "const:4:8"]]
- 00599640 ["CALL", null, ["callee:00c53d00:8"]]
+ 00599680 ["INT_ADD", "register:40f0:8", ["const:599680:8", "const:4:8"]]
+ 00599680 ["CALL", null, ["callee:00c53d00:8"]]
- 00599640 bytes a8e81a94
+ 00599680 bytes a0e91a94
- 00599660 ["COPY", "register:0:8", ["register:4040:8"]]
- 00599660 ["INT_ADD", "register:40f0:8", ["const:599660:8", "const:4:8"]]
- 00599660 ["CALLIND", null, ["register:0:8"]]
+ 005996a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005996a0 ["INT_ADD", "register:40f0:8", ["const:5996a0:8", "const:4:8"]]
+ 005996a0 ["CALLIND", null, ["register:0:8"]]
- 00599660 bytes 00013fd6
+ 005996a0 bytes 00013fd6
~~~


<a id="compare-a0be6f16f0ce95d1e92ffcc0ceb10284"></a>

### [`005999e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005999e4.md) → [`00599a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599a24.md) FUN_00599a24

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00599a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005999e4.md#insn-00599a00) · [`00599a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005999e4.md#insn-00599a20)
- 新版 `00599a40`（命令位置の公開資料なし） · `00599a60`（命令位置の公開資料なし）

~~~diff
- 00599a00 ["INT_ADD", "register:40f0:8", ["const:599a00:8", "const:4:8"]]
- 00599a00 ["CALL", null, ["callee:00c53d00:8"]]
+ 00599a40 ["INT_ADD", "register:40f0:8", ["const:599a40:8", "const:4:8"]]
+ 00599a40 ["CALL", null, ["callee:00c53d00:8"]]
- 00599a00 bytes b8e71a94
+ 00599a40 bytes b0e81a94
- 00599a20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00599a20 ["INT_ADD", "register:40f0:8", ["const:599a20:8", "const:4:8"]]
- 00599a20 ["CALLIND", null, ["register:0:8"]]
+ 00599a60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00599a60 ["INT_ADD", "register:40f0:8", ["const:599a60:8", "const:4:8"]]
+ 00599a60 ["CALLIND", null, ["register:0:8"]]
- 00599a20 bytes 00013fd6
+ 00599a60 bytes 00013fd6
~~~


<a id="compare-55018de7e38a4d820041cc34c2850c9e"></a>

### [`00599c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599c30.md) → [`00599c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599c70.md) FUN_00599c70

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0059a6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a6c8.md) [`0059add8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059add8.md) · 呼出先 4件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`0059a708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a708.md) [`0059ae18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059ae18.md) · 呼出先 4件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00599c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599c30.md#insn-00599c68) · [`00599c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599c30.md#insn-00599c88) · [`00599ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599c30.md#insn-00599ca0)
- 新版 `00599ca8`（命令位置の公開資料なし） · `00599cc8`（命令位置の公開資料なし） · `00599ce0`（命令位置の公開資料なし）

~~~diff
- 00599c68 ["COPY", "register:0:8", ["register:4048:8"]]
- 00599c68 ["INT_ADD", "register:40f0:8", ["const:599c68:8", "const:4:8"]]
- 00599c68 ["CALLIND", null, ["register:0:8"]]
+ 00599ca8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00599ca8 ["INT_ADD", "register:40f0:8", ["const:599ca8:8", "const:4:8"]]
+ 00599ca8 ["CALLIND", null, ["register:0:8"]]
- 00599c68 bytes 20013fd6
+ 00599ca8 bytes 20013fd6
- 00599c88 ["COPY", "register:0:8", ["register:4048:8"]]
- 00599c88 ["INT_ADD", "register:40f0:8", ["const:599c88:8", "const:4:8"]]
- 00599c88 ["CALLIND", null, ["register:0:8"]]
+ 00599cc8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00599cc8 ["INT_ADD", "register:40f0:8", ["const:599cc8:8", "const:4:8"]]
+ 00599cc8 ["CALLIND", null, ["register:0:8"]]
- 00599c88 bytes 20013fd6
+ 00599cc8 bytes 20013fd6
- 00599ca0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00599ca0 ["INT_ADD", "register:40f0:8", ["const:599ca0:8", "const:4:8"]]
- 00599ca0 ["CALLIND", null, ["register:0:8"]]
+ 00599ce0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00599ce0 ["INT_ADD", "register:40f0:8", ["const:599ce0:8", "const:4:8"]]
+ 00599ce0 ["CALLIND", null, ["register:0:8"]]
- 00599ca0 bytes 00013fd6
+ 00599ce0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01fc6da0e162b55ced9b9c58e128e38e"></a>

### [`00599d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599d74.md) → [`00599db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599db4.md) FUN_00599db4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005ad7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad7a0.md) [`005ae8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae8a4.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`005ad7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md) [`005ae8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae8e4.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00599d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599d74.md#insn-00599d90) · [`00599db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599d74.md#insn-00599db0)
- 新版 `00599dd0`（命令位置の公開資料なし） · `00599df0`（命令位置の公開資料なし）

~~~diff
- 00599d90 ["INT_ADD", "register:40f0:8", ["const:599d90:8", "const:4:8"]]
- 00599d90 ["CALL", null, ["callee:00c53d00:8"]]
+ 00599dd0 ["INT_ADD", "register:40f0:8", ["const:599dd0:8", "const:4:8"]]
+ 00599dd0 ["CALL", null, ["callee:00c53d00:8"]]
- 00599d90 bytes d4e61a94
+ 00599dd0 bytes cce71a94
- 00599db0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00599db0 ["INT_ADD", "register:40f0:8", ["const:599db0:8", "const:4:8"]]
- 00599db0 ["CALLIND", null, ["register:0:8"]]
+ 00599df0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00599df0 ["INT_ADD", "register:40f0:8", ["const:599df0:8", "const:4:8"]]
+ 00599df0 ["CALLIND", null, ["register:0:8"]]
- 00599db0 bytes 00013fd6
+ 00599df0 bytes 00013fd6
~~~


<a id="compare-17a18ca2add8790049b0c83129a468bf"></a>

### [`00599dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599dc4.md) → [`00599e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599e04.md) FUN_00599e04

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005ad7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad7a0.md) [`005ae8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae8a4.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`005ad7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md) [`005ae8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae8e4.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00599de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599dc4.md#insn-00599de0) · [`00599e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599dc4.md#insn-00599e00)
- 新版 `00599e20`（命令位置の公開資料なし） · `00599e40`（命令位置の公開資料なし）

~~~diff
- 00599de0 ["INT_ADD", "register:40f0:8", ["const:599de0:8", "const:4:8"]]
- 00599de0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00599e20 ["INT_ADD", "register:40f0:8", ["const:599e20:8", "const:4:8"]]
+ 00599e20 ["CALL", null, ["callee:00c53d00:8"]]
- 00599de0 bytes c0e61a94
+ 00599e20 bytes b8e71a94
- 00599e00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00599e00 ["INT_ADD", "register:40f0:8", ["const:599e00:8", "const:4:8"]]
- 00599e00 ["CALLIND", null, ["register:0:8"]]
+ 00599e40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00599e40 ["INT_ADD", "register:40f0:8", ["const:599e40:8", "const:4:8"]]
+ 00599e40 ["CALLIND", null, ["register:0:8"]]
- 00599e00 bytes 00013fd6
+ 00599e40 bytes 00013fd6
~~~


<a id="compare-c9ae1bfb75fdbfb9bf3413681778c6d3"></a>

### [`00599ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599ef8.md) → [`00599f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599f38.md) FUN_00599f38

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00599e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599e14.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00599e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599e54.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00599f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599ef8.md#insn-00599f08)
- 新版 `00599f48`（命令位置の公開資料なし）

~~~diff
- 00599f08 ["INT_ADD", "register:40f0:8", ["const:599f08:8", "const:4:8"]]
- 00599f08 ["CALL", null, ["callee:00599e54:8"]]
+ 00599f48 ["INT_ADD", "register:40f0:8", ["const:599f48:8", "const:4:8"]]
+ 00599f48 ["CALL", null, ["callee:00599e54:8"]]
- 00599f08 bytes c3ffff97
+ 00599f48 bytes c3ffff97
~~~


<a id="compare-bc5c8457c6e0fa7f0c0bd7f89474f2da"></a>

### [`0059a0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a0f0.md) → [`0059a130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a130.md) FUN_0059a130

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059a12c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a0f0.md#insn-0059a12c)
- 新版 `0059a16c`（命令位置の公開資料なし）

~~~diff
- 0059a12c ["COPY", "register:0:8", ["register:4040:8"]]
- 0059a12c ["INT_ADD", "register:40f0:8", ["const:59a12c:8", "const:4:8"]]
- 0059a12c ["CALLIND", null, ["register:0:8"]]
+ 0059a16c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059a16c ["INT_ADD", "register:40f0:8", ["const:59a16c:8", "const:4:8"]]
+ 0059a16c ["CALLIND", null, ["register:0:8"]]
- 0059a12c bytes 00013fd6
+ 0059a16c bytes 00013fd6
~~~


<a id="compare-92c1c4eb2cf66914ddbb4b77765afe2c"></a>

### [`0059a140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a140.md) → [`0059a180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a180.md) FUN_0059a180

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059a15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a140.md#insn-0059a15c)
- 新版 `0059a19c`（命令位置の公開資料なし）

~~~diff
- 0059a15c ["INT_ADD", "register:40f0:8", ["const:59a15c:8", "const:4:8"]]
- 0059a15c ["CALL", null, ["callee:00459d74:8"]]
+ 0059a19c ["INT_ADD", "register:40f0:8", ["const:59a19c:8", "const:4:8"]]
+ 0059a19c ["CALL", null, ["callee:00459d74:8"]]
- 0059a15c bytes f6fefa97
+ 0059a19c bytes f6fefa97
~~~


<a id="compare-407b8451dafb8eeeb5999072d56472e4"></a>

### [`0059a188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a188.md) → [`0059a1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a1c8.md) FUN_0059a1c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00598afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598afc.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00598b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b3c.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059a1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a188.md#insn-0059a1f4) · [`0059a204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a188.md#insn-0059a204) · [`0059a224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a188.md#insn-0059a224)
- 新版 `0059a234`（命令位置の公開資料なし） · `0059a244`（命令位置の公開資料なし） · `0059a264`（命令位置の公開資料なし）

~~~diff
- 0059a1f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0059a1f4 ["INT_ADD", "register:40f0:8", ["const:59a1f4:8", "const:4:8"]]
- 0059a1f4 ["CALLIND", null, ["register:0:8"]]
+ 0059a234 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059a234 ["INT_ADD", "register:40f0:8", ["const:59a234:8", "const:4:8"]]
+ 0059a234 ["CALLIND", null, ["register:0:8"]]
- 0059a1f4 bytes 00013fd6
+ 0059a234 bytes 00013fd6
- 0059a204 ["COPY", "register:0:8", ["register:4040:8"]]
- 0059a204 ["INT_ADD", "register:40f0:8", ["const:59a204:8", "const:4:8"]]
- 0059a204 ["CALLIND", null, ["register:0:8"]]
+ 0059a244 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059a244 ["INT_ADD", "register:40f0:8", ["const:59a244:8", "const:4:8"]]
+ 0059a244 ["CALLIND", null, ["register:0:8"]]
- 0059a204 bytes 00013fd6
+ 0059a244 bytes 00013fd6
- 0059a224 ["COPY", "register:0:8", ["register:4040:8"]]
- 0059a224 ["INT_ADD", "register:40f0:8", ["const:59a224:8", "const:4:8"]]
- 0059a224 ["CALLIND", null, ["register:0:8"]]
+ 0059a264 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059a264 ["INT_ADD", "register:40f0:8", ["const:59a264:8", "const:4:8"]]
+ 0059a264 ["CALLIND", null, ["register:0:8"]]
- 0059a224 bytes 00013fd6
+ 0059a264 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f9b1c8eb9c0bb9ed0ea50e03ec31dc2"></a>

### [`0059a2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a2f0.md) → [`0059a330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a330.md) FUN_0059a330

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00598cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598cb4.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059a35c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a2f0.md#insn-0059a35c) · [`0059a36c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a2f0.md#insn-0059a36c) · [`0059a38c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a2f0.md#insn-0059a38c)
- 新版 `0059a39c`（命令位置の公開資料なし） · `0059a3ac`（命令位置の公開資料なし） · `0059a3cc`（命令位置の公開資料なし）

~~~diff
- 0059a35c ["COPY", "register:0:8", ["register:4040:8"]]
- 0059a35c ["INT_ADD", "register:40f0:8", ["const:59a35c:8", "const:4:8"]]
- 0059a35c ["CALLIND", null, ["register:0:8"]]
+ 0059a39c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059a39c ["INT_ADD", "register:40f0:8", ["const:59a39c:8", "const:4:8"]]
+ 0059a39c ["CALLIND", null, ["register:0:8"]]
- 0059a35c bytes 00013fd6
+ 0059a39c bytes 00013fd6
- 0059a36c ["COPY", "register:0:8", ["register:4040:8"]]
- 0059a36c ["INT_ADD", "register:40f0:8", ["const:59a36c:8", "const:4:8"]]
- 0059a36c ["CALLIND", null, ["register:0:8"]]
+ 0059a3ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059a3ac ["INT_ADD", "register:40f0:8", ["const:59a3ac:8", "const:4:8"]]
+ 0059a3ac ["CALLIND", null, ["register:0:8"]]
- 0059a36c bytes 00013fd6
+ 0059a3ac bytes 00013fd6
- 0059a38c ["COPY", "register:0:8", ["register:4040:8"]]
- 0059a38c ["INT_ADD", "register:40f0:8", ["const:59a38c:8", "const:4:8"]]
- 0059a38c ["CALLIND", null, ["register:0:8"]]
+ 0059a3cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059a3cc ["INT_ADD", "register:40f0:8", ["const:59a3cc:8", "const:4:8"]]
+ 0059a3cc ["CALLIND", null, ["register:0:8"]]
- 0059a38c bytes 00013fd6
+ 0059a3cc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-779017e05286c5d99f8f4c976bc52391"></a>

### [`0059a64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a64c.md) → [`0059a68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a68c.md) FUN_0059a68c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059a668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a64c.md#insn-0059a668)
- 新版 `0059a6a8`（命令位置の公開資料なし）

~~~diff
- 0059a668 ["INT_ADD", "register:40f0:8", ["const:59a668:8", "const:4:8"]]
- 0059a668 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059a6a8 ["INT_ADD", "register:40f0:8", ["const:59a6a8:8", "const:4:8"]]
+ 0059a6a8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059a668 bytes 12f51a94
+ 0059a6a8 bytes 02f61a94
~~~


<a id="compare-2bec102fe90cde221c54890f064409ac"></a>

### [`0059a68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a68c.md) → [`0059a6cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a6cc.md) FUN_0059a6cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00598d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598d80.md) · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00598dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598dc0.md) · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059a6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a68c.md#insn-0059a6a8) · [`0059a6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a68c.md#insn-0059a6b4)
- 新版 `0059a6e8`（命令位置の公開資料なし） · `0059a6f4`（命令位置の公開資料なし）

~~~diff
- 0059a6a8 ["INT_ADD", "register:40f0:8", ["const:59a6a8:8", "const:4:8"]]
- 0059a6a8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059a6e8 ["INT_ADD", "register:40f0:8", ["const:59a6e8:8", "const:4:8"]]
+ 0059a6e8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059a6a8 bytes 02f51a94
+ 0059a6e8 bytes f2f51a94
- 0059a6b4 ["INT_ADD", "register:40f0:8", ["const:59a6b4:8", "const:4:8"]]
- 0059a6b4 ["CALL", null, ["callee:00c57e80:8"]]
+ 0059a6f4 ["INT_ADD", "register:40f0:8", ["const:59a6f4:8", "const:4:8"]]
+ 0059a6f4 ["CALL", null, ["callee:00c57e80:8"]]
- 0059a6b4 bytes f3f41a94
+ 0059a6f4 bytes e3f51a94
~~~


<a id="compare-c135aab28dbace6299ff7eabdeb08142"></a>

### [`0059a6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a6c8.md) → [`0059a708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a708.md) FUN_0059a708

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00596eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596eec.md) [`00599674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599674.md) [`00599a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599a34.md) [`00599c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599c30.md) [`00795de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795de4.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00596f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596f2c.md) [`005996b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/005996b4.md) [`00599a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599a74.md) [`00599c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599c70.md) [`00795e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e24.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059a708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a6c8.md#insn-0059a708) · [`0059a730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a6c8.md#insn-0059a730) · [`0059a748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a6c8.md#insn-0059a748)
- 新版 `0059a748`（命令位置の公開資料なし） · `0059a770`（命令位置の公開資料なし） · `0059a788`（命令位置の公開資料なし）

~~~diff
- 0059a708 ["INT_ADD", "register:40f0:8", ["const:59a708:8", "const:4:8"]]
- 0059a708 ["CALL", null, ["callee:00c584f0:8"]]
+ 0059a748 ["INT_ADD", "register:40f0:8", ["const:59a748:8", "const:4:8"]]
+ 0059a748 ["CALL", null, ["callee:00c584f0:8"]]
- 0059a708 bytes 7af61a94
+ 0059a748 bytes 6af71a94
- 0059a730 ["COPY", "register:0:8", ["register:4040:8"]]
- 0059a730 ["INT_ADD", "register:40f0:8", ["const:59a730:8", "const:4:8"]]
- 0059a730 ["CALLIND", null, ["register:0:8"]]
+ 0059a770 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059a770 ["INT_ADD", "register:40f0:8", ["const:59a770:8", "const:4:8"]]
+ 0059a770 ["CALLIND", null, ["register:0:8"]]
- 0059a730 bytes 00013fd6
+ 0059a770 bytes 00013fd6
- 0059a748 ["COPY", "register:0:8", ["register:4048:8"]]
- 0059a748 ["INT_ADD", "register:40f0:8", ["const:59a748:8", "const:4:8"]]
- 0059a748 ["CALLIND", null, ["register:0:8"]]
+ 0059a788 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0059a788 ["INT_ADD", "register:40f0:8", ["const:59a788:8", "const:4:8"]]
+ 0059a788 ["CALLIND", null, ["register:0:8"]]
- 0059a748 bytes 20013fd6
+ 0059a788 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb500cd9ab37da62ab0cc2bacb09f96f"></a>

### [`0059ad14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059ad14.md) → [`0059ad54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059ad54.md) FUN_0059ad54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059ad30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059ad14.md#insn-0059ad30) · [`0059ad44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059ad14.md#insn-0059ad44) · [`0059ad64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059ad14.md#insn-0059ad64)
- 新版 `0059ad70`（命令位置の公開資料なし） · `0059ad84`（命令位置の公開資料なし） · `0059ada4`（命令位置の公開資料なし）

~~~diff
- 0059ad30 ["INT_ADD", "register:40f0:8", ["const:59ad30:8", "const:4:8"]]
- 0059ad30 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059ad70 ["INT_ADD", "register:40f0:8", ["const:59ad70:8", "const:4:8"]]
+ 0059ad70 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059ad30 bytes 60f31a94
+ 0059ad70 bytes 50f41a94
- 0059ad44 ["INT_ADD", "register:40f0:8", ["const:59ad44:8", "const:4:8"]]
- 0059ad44 ["CALL", null, ["callee:00c53d00:8"]]
+ 0059ad84 ["INT_ADD", "register:40f0:8", ["const:59ad84:8", "const:4:8"]]
+ 0059ad84 ["CALL", null, ["callee:00c53d00:8"]]
- 0059ad44 bytes e7e21a94
+ 0059ad84 bytes dfe31a94
- 0059ad64 ["COPY", "register:0:8", ["register:4040:8"]]
- 0059ad64 ["INT_ADD", "register:40f0:8", ["const:59ad64:8", "const:4:8"]]
- 0059ad64 ["CALLIND", null, ["register:0:8"]]
+ 0059ada4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059ada4 ["INT_ADD", "register:40f0:8", ["const:59ada4:8", "const:4:8"]]
+ 0059ada4 ["CALLIND", null, ["register:0:8"]]
- 0059ad64 bytes 00013fd6
+ 0059ada4 bytes 00013fd6
~~~


<a id="compare-8b8846318fdafc9d6fccda40ba3d6c32"></a>

### [`0059ad78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059ad78.md) → [`0059adb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059adb8.md) FUN_0059adb8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0059921c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/0059921c.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0059925c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/0059925c.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059ad94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059ad78.md#insn-0059ad94) · [`0059ada8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059ad78.md#insn-0059ada8) · [`0059adbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059ad78.md#insn-0059adbc)
- 新版 `0059add4`（命令位置の公開資料なし） · `0059ade8`（命令位置の公開資料なし） · `0059adfc`（命令位置の公開資料なし）

~~~diff
- 0059ad94 ["INT_ADD", "register:40f0:8", ["const:59ad94:8", "const:4:8"]]
- 0059ad94 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059add4 ["INT_ADD", "register:40f0:8", ["const:59add4:8", "const:4:8"]]
+ 0059add4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059ad94 bytes 47f31a94
+ 0059add4 bytes 37f41a94
- 0059ada8 ["INT_ADD", "register:40f0:8", ["const:59ada8:8", "const:4:8"]]
- 0059ada8 ["CALL", null, ["callee:00c53d00:8"]]
+ 0059ade8 ["INT_ADD", "register:40f0:8", ["const:59ade8:8", "const:4:8"]]
+ 0059ade8 ["CALL", null, ["callee:00c53d00:8"]]
- 0059ada8 bytes cee21a94
+ 0059ade8 bytes c6e31a94
- 0059adbc ["COPY", "register:0:8", ["register:4040:8"]]
- 0059adbc ["INT_ADD", "register:40f0:8", ["const:59adbc:8", "const:4:8"]]
- 0059adbc ["CALLIND", null, ["register:0:8"]]
+ 0059adfc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059adfc ["INT_ADD", "register:40f0:8", ["const:59adfc:8", "const:4:8"]]
+ 0059adfc ["CALLIND", null, ["register:0:8"]]
- 0059adbc bytes 00013fd6
+ 0059adfc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1890986a8da50f5583085efbfc28899"></a>

### [`0059add8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059add8.md) → [`0059ae18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059ae18.md) FUN_0059ae18

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00596eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596eec.md) [`00599674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599674.md) [`00599a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599a34.md) [`00599c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599c30.md) [`00795de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795de4.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00596f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596f2c.md) [`005996b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/005996b4.md) [`00599a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599a74.md) [`00599c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599c70.md) [`00795e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e24.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059ae1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059add8.md#insn-0059ae1c) · [`0059ae38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059add8.md#insn-0059ae38) · [`0059ae5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059add8.md#insn-0059ae5c)
- 新版 `0059ae5c`（命令位置の公開資料なし） · `0059ae78`（命令位置の公開資料なし） · `0059ae9c`（命令位置の公開資料なし）

~~~diff
- 0059ae1c ["COPY", "register:0:8", ["register:4048:8"]]
- 0059ae1c ["INT_ADD", "register:40f0:8", ["const:59ae1c:8", "const:4:8"]]
- 0059ae1c ["CALLIND", null, ["register:0:8"]]
+ 0059ae5c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0059ae5c ["INT_ADD", "register:40f0:8", ["const:59ae5c:8", "const:4:8"]]
+ 0059ae5c ["CALLIND", null, ["register:0:8"]]
- 0059ae1c bytes 20013fd6
+ 0059ae5c bytes 20013fd6
- 0059ae38 ["COPY", "register:0:8", ["register:4050:8"]]
- 0059ae38 ["INT_ADD", "register:40f0:8", ["const:59ae38:8", "const:4:8"]]
- 0059ae38 ["CALLIND", null, ["register:0:8"]]
+ 0059ae78 ["COPY", "register:0:8", ["register:4050:8"]]
+ 0059ae78 ["INT_ADD", "register:40f0:8", ["const:59ae78:8", "const:4:8"]]
+ 0059ae78 ["CALLIND", null, ["register:0:8"]]
- 0059ae38 bytes 40013fd6
+ 0059ae78 bytes 40013fd6
- 0059ae5c ["INT_ADD", "register:40f0:8", ["const:59ae5c:8", "const:4:8"]]
- 0059ae5c ["CALL", null, ["callee:00c53cd0:8"]]
+ 0059ae9c ["INT_ADD", "register:40f0:8", ["const:59ae9c:8", "const:4:8"]]
+ 0059ae9c ["CALL", null, ["callee:00c53cd0:8"]]
- 0059ae5c bytes 95e21a94
+ 0059ae9c bytes 8de31a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63ae3d4be65777058a11431e676d44d0"></a>

### [`0059b300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b300.md) → [`0059b340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b340.md) FUN_0059b340

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005997c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005997c4.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00599804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599804.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059b31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b300.md#insn-0059b31c) · [`0059b33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b300.md#insn-0059b33c)
- 新版 `0059b35c`（命令位置の公開資料なし） · `0059b37c`（命令位置の公開資料なし）

~~~diff
- 0059b31c ["INT_ADD", "register:40f0:8", ["const:59b31c:8", "const:4:8"]]
- 0059b31c ["CALL", null, ["callee:00c53d00:8"]]
+ 0059b35c ["INT_ADD", "register:40f0:8", ["const:59b35c:8", "const:4:8"]]
+ 0059b35c ["CALL", null, ["callee:00c53d00:8"]]
- 0059b31c bytes 71e11a94
+ 0059b35c bytes 69e21a94
- 0059b33c ["COPY", "register:0:8", ["register:4040:8"]]
- 0059b33c ["INT_ADD", "register:40f0:8", ["const:59b33c:8", "const:4:8"]]
- 0059b33c ["CALLIND", null, ["register:0:8"]]
+ 0059b37c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059b37c ["INT_ADD", "register:40f0:8", ["const:59b37c:8", "const:4:8"]]
+ 0059b37c ["CALLIND", null, ["register:0:8"]]
- 0059b33c bytes 00013fd6
+ 0059b37c bytes 00013fd6
~~~


<a id="compare-df58c2755fbe45842f9d4a3047057336"></a>

### [`0059b350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b350.md) → [`0059b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b390.md) FUN_0059b390

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005997c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005997c4.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00599804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599804.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059b370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b350.md#insn-0059b370) · [`0059b384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b350.md#insn-0059b384) · [`0059b38c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b350.md#insn-0059b38c)
- 新版 `0059b3b0`（命令位置の公開資料なし） · `0059b3c4`（命令位置の公開資料なし） · `0059b3cc`（命令位置の公開資料なし）

~~~diff
- 0059b370 ["INT_ADD", "register:40f0:8", ["const:59b370:8", "const:4:8"]]
- 0059b370 ["CALL", null, ["callee:00c53d00:8"]]
+ 0059b3b0 ["INT_ADD", "register:40f0:8", ["const:59b3b0:8", "const:4:8"]]
+ 0059b3b0 ["CALL", null, ["callee:00c53d00:8"]]
- 0059b370 bytes 5ce11a94
+ 0059b3b0 bytes 54e21a94
- 0059b384 ["COPY", "register:0:8", ["register:4040:8"]]
- 0059b384 ["INT_ADD", "register:40f0:8", ["const:59b384:8", "const:4:8"]]
- 0059b384 ["CALLIND", null, ["register:0:8"]]
+ 0059b3c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059b3c4 ["INT_ADD", "register:40f0:8", ["const:59b3c4:8", "const:4:8"]]
+ 0059b3c4 ["CALLIND", null, ["register:0:8"]]
- 0059b384 bytes 00013fd6
+ 0059b3c4 bytes 00013fd6
- 0059b38c ["INT_ADD", "register:40f0:8", ["const:59b38c:8", "const:4:8"]]
- 0059b38c ["CALL", null, ["callee:00c57e80:8"]]
+ 0059b3cc ["INT_ADD", "register:40f0:8", ["const:59b3cc:8", "const:4:8"]]
+ 0059b3cc ["CALL", null, ["callee:00c57e80:8"]]
- 0059b38c bytes bdf11a94
+ 0059b3cc bytes adf21a94
~~~


<a id="compare-97ca1341c15a7faf82a78750ea83bbbb"></a>

### [`0059d3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d3b4.md) → [`0059d3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059d3f4.md) FUN_0059d3f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`0059bf04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059bf04.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0059bf44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059bf44.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059d3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d3b4.md#insn-0059d3e0) · [`0059d410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d3b4.md#insn-0059d410) · [`0059d420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d3b4.md#insn-0059d420)
- 新版 `0059d420`（命令位置の公開資料なし） · `0059d450`（命令位置の公開資料なし） · `0059d460`（命令位置の公開資料なし）

~~~diff
- 0059d3e0 ["INT_ADD", "register:40f0:8", ["const:59d3e0:8", "const:4:8"]]
- 0059d3e0 ["CALL", null, ["callee:0059bf44:8"]]
+ 0059d420 ["INT_ADD", "register:40f0:8", ["const:59d420:8", "const:4:8"]]
+ 0059d420 ["CALL", null, ["callee:0059bf44:8"]]
- 0059d3e0 bytes c9faff97
+ 0059d420 bytes c9faff97
- 0059d410 ["INT_ADD", "register:40f0:8", ["const:59d410:8", "const:4:8"]]
- 0059d410 ["CALL", null, ["callee:0045179c:8"]]
+ 0059d450 ["INT_ADD", "register:40f0:8", ["const:59d450:8", "const:4:8"]]
+ 0059d450 ["CALL", null, ["callee:0045179c:8"]]
- 0059d410 bytes d3d0fa97
+ 0059d450 bytes d3d0fa97
- 0059d420 ["INT_ADD", "register:40f0:8", ["const:59d420:8", "const:4:8"]]
- 0059d420 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059d460 ["INT_ADD", "register:40f0:8", ["const:59d460:8", "const:4:8"]]
+ 0059d460 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059d420 bytes a4e91a94
+ 0059d460 bytes 94ea1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27bf1dc55b4a5441d17061c67f7d7229"></a>

### [`0059ebbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ebbc.md) → [`0059ebfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059ebfc.md) FUN_0059ebfc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`0059bf04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059bf04.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0059bf44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059bf44.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059ebe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ebbc.md#insn-0059ebe8) · [`0059ec1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ebbc.md#insn-0059ec1c) · [`0059ec2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ebbc.md#insn-0059ec2c)
- 新版 `0059ec28`（命令位置の公開資料なし） · `0059ec5c`（命令位置の公開資料なし） · `0059ec6c`（命令位置の公開資料なし）

~~~diff
- 0059ebe8 ["INT_ADD", "register:40f0:8", ["const:59ebe8:8", "const:4:8"]]
- 0059ebe8 ["CALL", null, ["callee:0059bf44:8"]]
+ 0059ec28 ["INT_ADD", "register:40f0:8", ["const:59ec28:8", "const:4:8"]]
+ 0059ec28 ["CALL", null, ["callee:0059bf44:8"]]
- 0059ebe8 bytes c7f4ff97
+ 0059ec28 bytes c7f4ff97
- 0059ec1c ["INT_ADD", "register:40f0:8", ["const:59ec1c:8", "const:4:8"]]
- 0059ec1c ["CALL", null, ["callee:0045179c:8"]]
+ 0059ec5c ["INT_ADD", "register:40f0:8", ["const:59ec5c:8", "const:4:8"]]
+ 0059ec5c ["CALL", null, ["callee:0045179c:8"]]
- 0059ec1c bytes d0cafa97
+ 0059ec5c bytes d0cafa97
- 0059ec2c ["INT_ADD", "register:40f0:8", ["const:59ec2c:8", "const:4:8"]]
- 0059ec2c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059ec6c ["INT_ADD", "register:40f0:8", ["const:59ec6c:8", "const:4:8"]]
+ 0059ec6c ["CALL", null, ["callee:00c57eb0:8"]]
- 0059ec2c bytes a1e31a94
+ 0059ec6c bytes 91e41a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d73eab5694c433be771ea2ec8d95ce49"></a>

### [`0059f560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f560.md) → [`0059f5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059f5a0.md) FUN_0059f5a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`0059bf04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059bf04.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0059bf44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059bf44.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059f58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f560.md#insn-0059f58c) · [`0059f5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f560.md#insn-0059f5c0) · [`0059f5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f560.md#insn-0059f5d0)
- 新版 `0059f5cc`（命令位置の公開資料なし） · `0059f600`（命令位置の公開資料なし） · `0059f610`（命令位置の公開資料なし）

~~~diff
- 0059f58c ["INT_ADD", "register:40f0:8", ["const:59f58c:8", "const:4:8"]]
- 0059f58c ["CALL", null, ["callee:0059bf44:8"]]
+ 0059f5cc ["INT_ADD", "register:40f0:8", ["const:59f5cc:8", "const:4:8"]]
+ 0059f5cc ["CALL", null, ["callee:0059bf44:8"]]
- 0059f58c bytes 5ef2ff97
+ 0059f5cc bytes 5ef2ff97
- 0059f5c0 ["INT_ADD", "register:40f0:8", ["const:59f5c0:8", "const:4:8"]]
- 0059f5c0 ["CALL", null, ["callee:0045179c:8"]]
+ 0059f600 ["INT_ADD", "register:40f0:8", ["const:59f600:8", "const:4:8"]]
+ 0059f600 ["CALL", null, ["callee:0045179c:8"]]
- 0059f5c0 bytes 67c8fa97
+ 0059f600 bytes 67c8fa97
- 0059f5d0 ["INT_ADD", "register:40f0:8", ["const:59f5d0:8", "const:4:8"]]
- 0059f5d0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059f610 ["INT_ADD", "register:40f0:8", ["const:59f610:8", "const:4:8"]]
+ 0059f610 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059f5d0 bytes 38e11a94
+ 0059f610 bytes 28e21a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ea5bff3c9a0a89fb7e09247e830ad1f"></a>

### [`005a1310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1310.md) → [`005a1350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1350.md) FUN_005a1350

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a135c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1310.md#insn-005a135c)
- 新版 `005a139c`（命令位置の公開資料なし）

~~~diff
- 005a135c ["INT_ADD", "register:40f0:8", ["const:5a135c:8", "const:4:8"]]
- 005a135c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a139c ["INT_ADD", "register:40f0:8", ["const:5a139c:8", "const:4:8"]]
+ 005a139c ["CALL", null, ["callee:00c57eb0:8"]]
- 005a135c bytes d5d91a94
+ 005a139c bytes c5da1a94
~~~


<a id="compare-e7acf1b5496dba9b6423a0911757e137"></a>

### [`005a1794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1794.md) → [`005a17d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a17d4.md) FUN_005a17d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005a16e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a16e8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005a1728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1728.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a17a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1794.md#insn-005a17a4)
- 新版 `005a17e4`（命令位置の公開資料なし）

~~~diff
- 005a17a4 ["INT_ADD", "register:40f0:8", ["const:5a17a4:8", "const:4:8"]]
- 005a17a4 ["CALL", null, ["callee:005a1728:8"]]
+ 005a17e4 ["INT_ADD", "register:40f0:8", ["const:5a17e4:8", "const:4:8"]]
+ 005a17e4 ["CALL", null, ["callee:005a1728:8"]]
- 005a17a4 bytes d1ffff97
+ 005a17e4 bytes d1ffff97
~~~


<a id="compare-d821d1e6dac46373793f2a7e9548b83b"></a>

### [`005a18e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a18e0.md) → [`005a1920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1920.md) FUN_005a1920

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a1da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1da0.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`005a1a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1a40.md) [`005a1acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1acc.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`005a1de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1de0.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005a1a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1a80.md) [`005a1b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1b0c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a193c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a18e0.md#insn-005a193c) · [`005a19b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a18e0.md#insn-005a19b0) · [`005a1a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a18e0.md#insn-005a1a00)
- 新版 `005a197c`（命令位置の公開資料なし） · `005a19f0`（命令位置の公開資料なし） · `005a1a40`（命令位置の公開資料なし）

~~~diff
- 005a193c ["INT_ADD", "register:40f0:8", ["const:5a193c:8", "const:4:8"]]
- 005a193c ["CALL", null, ["callee:00c57e90:8"]]
+ 005a197c ["INT_ADD", "register:40f0:8", ["const:5a197c:8", "const:4:8"]]
+ 005a197c ["CALL", null, ["callee:00c57e90:8"]]
- 005a193c bytes 55d81a94
+ 005a197c bytes 45d91a94
- 005a19b0 ["INT_ADD", "register:40f0:8", ["const:5a19b0:8", "const:4:8"]]
- 005a19b0 ["CALL", null, ["callee:0043bb20:8"]]
+ 005a19f0 ["INT_ADD", "register:40f0:8", ["const:5a19f0:8", "const:4:8"]]
+ 005a19f0 ["CALL", null, ["callee:0043bb20:8"]]
- 005a19b0 bytes 4c68fa97
+ 005a19f0 bytes 4c68fa97
- 005a1a00 ["INT_ADD", "register:40f0:8", ["const:5a1a00:8", "const:4:8"]]
- 005a1a00 ["CALL", null, ["callee:005a1b0c:8"]]
+ 005a1a40 ["INT_ADD", "register:40f0:8", ["const:5a1a40:8", "const:4:8"]]
+ 005a1a40 ["CALL", null, ["callee:005a1b0c:8"]]
- 005a1a00 bytes 33000094
+ 005a1a40 bytes 33000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-827f98ec300c7de71132fb8a8fc6c68f"></a>

### [`005a1a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1a40.md) → [`005a1a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1a80.md) FUN_005a1a80

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a18e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a18e0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005a1920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1920.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a1aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1a40.md#insn-005a1aa8)
- 新版 `005a1ae8`（命令位置の公開資料なし）

~~~diff
- 005a1aa8 ["INT_ADD", "register:40f0:8", ["const:5a1aa8:8", "const:4:8"]]
- 005a1aa8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a1ae8 ["INT_ADD", "register:40f0:8", ["const:5a1ae8:8", "const:4:8"]]
+ 005a1ae8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a1aa8 bytes 02d81a94
+ 005a1ae8 bytes f2d81a94
~~~


<a id="compare-0c79ed79a8e233b79a9f501a18b391b4"></a>

### [`005a1ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1ae0.md) → [`005a1b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1b20.md) FUN_005a1b20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a1b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1ae0.md#insn-005a1b2c)
- 新版 `005a1b6c`（命令位置の公開資料なし）

~~~diff
- 005a1b2c ["INT_ADD", "register:40f0:8", ["const:5a1b2c:8", "const:4:8"]]
- 005a1b2c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a1b6c ["INT_ADD", "register:40f0:8", ["const:5a1b6c:8", "const:4:8"]]
+ 005a1b6c ["CALL", null, ["callee:00c57eb0:8"]]
- 005a1b2c bytes e1d71a94
+ 005a1b6c bytes d1d81a94
~~~


<a id="compare-1cc99318418521e30ef2e94d9e1959d9"></a>

### [`005a1b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1b40.md) → [`005a1b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1b80.md) FUN_005a1b80

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a0e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0e54.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005a1acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1acc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005a0e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0e94.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005a1b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1b0c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a1be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1b40.md#insn-005a1be4) · [`005a1c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1b40.md#insn-005a1c2c) · [`005a1c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1b40.md#insn-005a1c90)
- 新版 `005a1c24`（命令位置の公開資料なし） · `005a1c6c`（命令位置の公開資料なし） · `005a1cd0`（命令位置の公開資料なし）

~~~diff
- 005a1be4 ["INT_ADD", "register:40f0:8", ["const:5a1be4:8", "const:4:8"]]
- 005a1be4 ["CALL", null, ["callee:00c57e90:8"]]
+ 005a1c24 ["INT_ADD", "register:40f0:8", ["const:5a1c24:8", "const:4:8"]]
+ 005a1c24 ["CALL", null, ["callee:00c57e90:8"]]
- 005a1be4 bytes abd71a94
+ 005a1c24 bytes 9bd81a94
- 005a1c2c ["INT_ADD", "register:40f0:8", ["const:5a1c2c:8", "const:4:8"]]
- 005a1c2c ["CALL", null, ["callee:0043bb20:8"]]
+ 005a1c6c ["INT_ADD", "register:40f0:8", ["const:5a1c6c:8", "const:4:8"]]
+ 005a1c6c ["CALL", null, ["callee:0043bb20:8"]]
- 005a1c2c bytes ad67fa97
+ 005a1c6c bytes ad67fa97
- 005a1c90 ["INT_ADD", "register:40f0:8", ["const:5a1c90:8", "const:4:8"]]
- 005a1c90 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a1cd0 ["INT_ADD", "register:40f0:8", ["const:5a1cd0:8", "const:4:8"]]
+ 005a1cd0 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a1c90 bytes 88d71a94
+ 005a1cd0 bytes 78d81a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09dab06fae4700526a83dc9ae393d97b"></a>

### [`005a1d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1d38.md) → [`005a1d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1d78.md) FUN_005a1d78

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a1d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1d38.md#insn-005a1d88)
- 新版 `005a1dc8`（命令位置の公開資料なし）

~~~diff
- 005a1d88 ["INT_ADD", "register:40f0:8", ["const:5a1d88:8", "const:4:8"]]
- 005a1d88 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a1dc8 ["INT_ADD", "register:40f0:8", ["const:5a1dc8:8", "const:4:8"]]
+ 005a1dc8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a1d88 bytes 4ad71a94
+ 005a1dc8 bytes 3ad81a94
~~~


<a id="compare-539fb98aed2f670c756788776f4d3e7b"></a>

### [`005a3e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3e2c.md) → [`005a3e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3e6c.md) FUN_005a3e6c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a3e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3e2c.md#insn-005a3e48) · [`005a3e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3e2c.md#insn-005a3e74) · [`005a3e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3e2c.md#insn-005a3e84)
- 新版 `005a3e88`（命令位置の公開資料なし） · `005a3eb4`（命令位置の公開資料なし） · `005a3ec4`（命令位置の公開資料なし）

~~~diff
- 005a3e48 ["INT_ADD", "register:40f0:8", ["const:5a3e48:8", "const:4:8"]]
- 005a3e48 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a3e88 ["INT_ADD", "register:40f0:8", ["const:5a3e88:8", "const:4:8"]]
+ 005a3e88 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a3e48 bytes 1acf1a94
+ 005a3e88 bytes 0ad01a94
- 005a3e74 ["INT_ADD", "register:40f0:8", ["const:5a3e74:8", "const:4:8"]]
- 005a3e74 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a3eb4 ["INT_ADD", "register:40f0:8", ["const:5a3eb4:8", "const:4:8"]]
+ 005a3eb4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a3e74 bytes 0fcf1a94
+ 005a3eb4 bytes ffcf1a94
- 005a3e84 ["INT_ADD", "register:40f0:8", ["const:5a3e84:8", "const:4:8"]]
- 005a3e84 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a3ec4 ["INT_ADD", "register:40f0:8", ["const:5a3ec4:8", "const:4:8"]]
+ 005a3ec4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a3e84 bytes 0bcf1a94
+ 005a3ec4 bytes fbcf1a94
~~~


<a id="compare-bac555c72421dc21f21db3fd3d3fbd19"></a>

### [`005a3ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3ea0.md) → [`005a3ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3ee0.md) FUN_005a3ee0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005a44c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a44c8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005a4508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4508.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a3eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3ea0.md#insn-005a3eb8)
- 新版 `005a3ef8`（命令位置の公開資料なし）

~~~diff
- 005a3eb8 ["INT_ADD", "register:40f0:8", ["const:5a3eb8:8", "const:4:8"]]
- 005a3eb8 ["CALL", null, ["callee:005a4508:8"]]
+ 005a3ef8 ["INT_ADD", "register:40f0:8", ["const:5a3ef8:8", "const:4:8"]]
+ 005a3ef8 ["CALL", null, ["callee:005a4508:8"]]
- 005a3eb8 bytes 84010094
+ 005a3ef8 bytes 84010094
~~~


<a id="compare-7a443eefae5395a3cab66b5c50978536"></a>

### [`005a40a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a40a4.md) → [`005a40e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a40e4.md) FUN_005a40e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005a48dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a48dc.md) [`0079a5c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079a/0079a5c8.md) [`0079c360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079c360.md) · 呼出先 6件 [`005a41e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a41e8.md) [`005a422c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a422c.md) [`005a4260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4260.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`005a491c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a491c.md) [`0079a608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079a/0079a608.md) [`0079c3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079c3a0.md) · 呼出先 6件 [`005a4228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4228.md) [`005a426c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a426c.md) [`005a42a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a42a0.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a4100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a40a4.md#insn-005a4100) · [`005a4144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a40a4.md#insn-005a4144) · [`005a41a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a40a4.md#insn-005a41a8)
- 新版 `005a4140`（命令位置の公開資料なし） · `005a4184`（命令位置の公開資料なし） · `005a41e8`（命令位置の公開資料なし）

~~~diff
- 005a4100 ["INT_ADD", "register:40f0:8", ["const:5a4100:8", "const:4:8"]]
- 005a4100 ["CALL", null, ["callee:00c57e90:8"]]
+ 005a4140 ["INT_ADD", "register:40f0:8", ["const:5a4140:8", "const:4:8"]]
+ 005a4140 ["CALL", null, ["callee:00c57e90:8"]]
- 005a4100 bytes 64ce1a94
+ 005a4140 bytes 54cf1a94
- 005a4144 ["INT_ADD", "register:40f0:8", ["const:5a4144:8", "const:4:8"]]
- 005a4144 ["CALL", null, ["callee:005a42a0:8"]]
+ 005a4184 ["INT_ADD", "register:40f0:8", ["const:5a4184:8", "const:4:8"]]
+ 005a4184 ["CALL", null, ["callee:005a42a0:8"]]
- 005a4144 bytes 47000094
+ 005a4184 bytes 47000094
- 005a41a8 ["INT_ADD", "register:40f0:8", ["const:5a41a8:8", "const:4:8"]]
- 005a41a8 ["CALL", null, ["callee:005a426c:8"]]
+ 005a41e8 ["INT_ADD", "register:40f0:8", ["const:5a41e8:8", "const:4:8"]]
+ 005a41e8 ["CALL", null, ["callee:005a426c:8"]]
- 005a41a8 bytes 21000094
+ 005a41e8 bytes 21000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-015541855d99e33f6e23978510a08f4d"></a>

### [`005a41e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a41e8.md) → [`005a4228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4228.md) FUN_005a4228

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a40a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a40a4.md) · 呼出先 2件 [`005a44c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a44c8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005a40e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a40e4.md) · 呼出先 2件 [`005a4508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4508.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a4214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a41e8.md#insn-005a4214)
- 新版 `005a4254`（命令位置の公開資料なし）

~~~diff
- 005a4214 ["INT_ADD", "register:40f0:8", ["const:5a4214:8", "const:4:8"]]
- 005a4214 ["CALL", null, ["callee:005a4508:8"]]
+ 005a4254 ["INT_ADD", "register:40f0:8", ["const:5a4254:8", "const:4:8"]]
+ 005a4254 ["CALL", null, ["callee:005a4508:8"]]
- 005a4214 bytes ad000094
+ 005a4254 bytes ad000094
~~~


<a id="compare-cfca3f76df5f75c4d1fcbd36da5f0467"></a>

### [`005a4240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4240.md) → [`005a4280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4280.md) FUN_005a4280

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0079cbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079cbd0.md) · 呼出先 1件 [`005a442c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a442c.md)
- 新版 呼出元 1件 [`0079cc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079cc10.md) · 呼出先 1件 [`005a446c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a446c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a4250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4240.md#insn-005a4250)
- 新版 `005a4290`（命令位置の公開資料なし）

~~~diff
- 005a4250 ["INT_ADD", "register:40f0:8", ["const:5a4250:8", "const:4:8"]]
- 005a4250 ["CALL", null, ["callee:005a446c:8"]]
+ 005a4290 ["INT_ADD", "register:40f0:8", ["const:5a4290:8", "const:4:8"]]
+ 005a4290 ["CALL", null, ["callee:005a446c:8"]]
- 005a4250 bytes 77000094
+ 005a4290 bytes 77000094
~~~


<a id="compare-064f09ff7f60cb81c10f00d217582948"></a>

### [`005a4260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4260.md) → [`005a42a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a42a0.md) FUN_005a42a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`005a32e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a32e0.md) [`005a40a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a40a4.md) [`005a4554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4554.md) [`00799c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00799/00799c54.md) [`0079a5c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079a/0079a5c8.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`005a4418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4418.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 7件 [`005a3320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3320.md) [`005a40e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a40e4.md) [`005a4594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4594.md) [`00799c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00799/00799c94.md) [`0079a608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079a/0079a608.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a429c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4260.md#insn-005a429c) · [`005a42d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4260.md#insn-005a42d0) · [`005a4304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4260.md#insn-005a4304)
- 新版 `005a42dc`（命令位置の公開資料なし） · `005a4310`（命令位置の公開資料なし） · `005a4344`（命令位置の公開資料なし）

~~~diff
- 005a429c ["INT_ADD", "register:40f0:8", ["const:5a429c:8", "const:4:8"]]
- 005a429c ["CALL", null, ["callee:0043bb20:8"]]
+ 005a42dc ["INT_ADD", "register:40f0:8", ["const:5a42dc:8", "const:4:8"]]
+ 005a42dc ["CALL", null, ["callee:0043bb20:8"]]
- 005a429c bytes 115efa97
+ 005a42dc bytes 115efa97
- 005a42d0 ["INT_ADD", "register:40f0:8", ["const:5a42d0:8", "const:4:8"]]
- 005a42d0 ["CALL", null, ["callee:0043bb20:8"]]
+ 005a4310 ["INT_ADD", "register:40f0:8", ["const:5a4310:8", "const:4:8"]]
+ 005a4310 ["CALL", null, ["callee:0043bb20:8"]]
- 005a42d0 bytes 045efa97
+ 005a4310 bytes 045efa97
- 005a4304 ["INT_ADD", "register:40f0:8", ["const:5a4304:8", "const:4:8"]]
- 005a4304 ["CALL", null, ["callee:0043bb20:8"]]
+ 005a4344 ["INT_ADD", "register:40f0:8", ["const:5a4344:8", "const:4:8"]]
+ 005a4344 ["CALL", null, ["callee:0043bb20:8"]]
- 005a4304 bytes f75dfa97
+ 005a4344 bytes f75dfa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-deddbcc158f89762a04effa7fd365e7a"></a>

### [`005a442c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a442c.md) → [`005a446c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a446c.md) FUN_005a446c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a4240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4240.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005a4280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4280.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a4470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a442c.md#insn-005a4470) · [`005a4494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a442c.md#insn-005a4494) · [`005a44a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a442c.md#insn-005a44a4)
- 新版 `005a44b0`（命令位置の公開資料なし） · `005a44d4`（命令位置の公開資料なし） · `005a44e4`（命令位置の公開資料なし）

~~~diff
- 005a4470 ["INT_ADD", "register:40f0:8", ["const:5a4470:8", "const:4:8"]]
- 005a4470 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a44b0 ["INT_ADD", "register:40f0:8", ["const:5a44b0:8", "const:4:8"]]
+ 005a44b0 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a4470 bytes 90cd1a94
+ 005a44b0 bytes 80ce1a94
- 005a4494 ["INT_ADD", "register:40f0:8", ["const:5a4494:8", "const:4:8"]]
- 005a4494 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a44d4 ["INT_ADD", "register:40f0:8", ["const:5a44d4:8", "const:4:8"]]
+ 005a44d4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a4494 bytes 87cd1a94
+ 005a44d4 bytes 77ce1a94
- 005a44a4 ["INT_ADD", "register:40f0:8", ["const:5a44a4:8", "const:4:8"]]
- 005a44a4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a44e4 ["INT_ADD", "register:40f0:8", ["const:5a44e4:8", "const:4:8"]]
+ 005a44e4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a44a4 bytes 83cd1a94
+ 005a44e4 bytes 73ce1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afdb5f28b4a3fcd587a2f4c6eec9fcb2"></a>

### [`005a44c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a44c8.md) → [`005a4508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4508.md) FUN_005a4508

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`005a3ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3ea0.md) [`005a3ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3ff0.md) [`005a404c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a404c.md) [`005a41e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a41e8.md) [`005a49fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a49fc.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 8件 [`005a3ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3ee0.md) [`005a4030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4030.md) [`005a408c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a408c.md) [`005a4228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4228.md) [`005a4a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4a3c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a4518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a44c8.md#insn-005a4518) · [`005a4528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a44c8.md#insn-005a4528) · [`005a4538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a44c8.md#insn-005a4538)
- 新版 `005a4558`（命令位置の公開資料なし） · `005a4568`（命令位置の公開資料なし） · `005a4578`（命令位置の公開資料なし）

~~~diff
- 005a4518 ["INT_ADD", "register:40f0:8", ["const:5a4518:8", "const:4:8"]]
- 005a4518 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a4558 ["INT_ADD", "register:40f0:8", ["const:5a4558:8", "const:4:8"]]
+ 005a4558 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a4518 bytes 66cd1a94
+ 005a4558 bytes 56ce1a94
- 005a4528 ["INT_ADD", "register:40f0:8", ["const:5a4528:8", "const:4:8"]]
- 005a4528 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a4568 ["INT_ADD", "register:40f0:8", ["const:5a4568:8", "const:4:8"]]
+ 005a4568 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a4528 bytes 62cd1a94
+ 005a4568 bytes 52ce1a94
- 005a4538 ["INT_ADD", "register:40f0:8", ["const:5a4538:8", "const:4:8"]]
- 005a4538 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a4578 ["INT_ADD", "register:40f0:8", ["const:5a4578:8", "const:4:8"]]
+ 005a4578 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a4538 bytes 5ecd1a94
+ 005a4578 bytes 4ece1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a48272fcf5713df5052a6b357e85aea"></a>

### [`005a4554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4554.md) → [`005a4594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4594.md) FUN_005a4594

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005a32e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a32e0.md) [`00799c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00799/00799c54.md) [`0079fff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079fff4.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005a422c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a422c.md) [`005a4260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4260.md) [`005a4714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4714.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`005a3320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3320.md) [`00799c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00799/00799c94.md) [`007a0034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0034.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005a426c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a426c.md) [`005a42a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a42a0.md) [`005a4754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4754.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a45f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4554.md#insn-005a45f4) · [`005a461c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4554.md#insn-005a461c) · [`005a4640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4554.md#insn-005a4640)
- 新版 `005a4634`（命令位置の公開資料なし） · `005a465c`（命令位置の公開資料なし） · `005a4680`（命令位置の公開資料なし）

~~~diff
- 005a45f4 ["INT_ADD", "register:40f0:8", ["const:5a45f4:8", "const:4:8"]]
- 005a45f4 ["CALL", null, ["callee:00c57e90:8"]]
+ 005a4634 ["INT_ADD", "register:40f0:8", ["const:5a4634:8", "const:4:8"]]
+ 005a4634 ["CALL", null, ["callee:00c57e90:8"]]
- 005a45f4 bytes 27cd1a94
+ 005a4634 bytes 17ce1a94
- 005a461c ["INT_ADD", "register:40f0:8", ["const:5a461c:8", "const:4:8"]]
- 005a461c ["CALL", null, ["callee:005a42a0:8"]]
+ 005a465c ["INT_ADD", "register:40f0:8", ["const:5a465c:8", "const:4:8"]]
+ 005a465c ["CALL", null, ["callee:005a42a0:8"]]
- 005a461c bytes 11ffff97
+ 005a465c bytes 11ffff97
- 005a4640 ["INT_ADD", "register:40f0:8", ["const:5a4640:8", "const:4:8"]]
- 005a4640 ["CALL", null, ["callee:005a4754:8"]]
+ 005a4680 ["INT_ADD", "register:40f0:8", ["const:5a4680:8", "const:4:8"]]
+ 005a4680 ["CALL", null, ["callee:005a4754:8"]]
- 005a4640 bytes 35000094
+ 005a4680 bytes 35000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-302ce0563ea3a4176885a7ee2f512e2d"></a>

### [`005a46dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a46dc.md) → [`005a471c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a471c.md) FUN_005a471c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005a4838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4838.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005a4878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4878.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a46f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a46dc.md#insn-005a46f0)
- 新版 `005a4730`（命令位置の公開資料なし）

~~~diff
- 005a46f0 ["INT_ADD", "register:40f0:8", ["const:5a46f0:8", "const:4:8"]]
- 005a46f0 ["CALL", null, ["callee:005a4878:8"]]
+ 005a4730 ["INT_ADD", "register:40f0:8", ["const:5a4730:8", "const:4:8"]]
+ 005a4730 ["CALL", null, ["callee:005a4878:8"]]
- 005a46f0 bytes 52000094
+ 005a4730 bytes 52000094
~~~


<a id="compare-e8392086b11ebf972b2514ede4f816ed"></a>

### [`005a4714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4714.md) → [`005a4754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4754.md) FUN_005a4754

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a4554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4554.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005a4594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4594.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a47e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4714.md#insn-005a47e0) · [`005a4804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4714.md#insn-005a4804) · [`005a4814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4714.md#insn-005a4814)
- 新版 `005a4820`（命令位置の公開資料なし） · `005a4844`（命令位置の公開資料なし） · `005a4854`（命令位置の公開資料なし）

~~~diff
- 005a47e0 ["INT_ADD", "register:40f0:8", ["const:5a47e0:8", "const:4:8"]]
- 005a47e0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a4820 ["INT_ADD", "register:40f0:8", ["const:5a4820:8", "const:4:8"]]
+ 005a4820 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a47e0 bytes b4cc1a94
+ 005a4820 bytes a4cd1a94
- 005a4804 ["INT_ADD", "register:40f0:8", ["const:5a4804:8", "const:4:8"]]
- 005a4804 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a4844 ["INT_ADD", "register:40f0:8", ["const:5a4844:8", "const:4:8"]]
+ 005a4844 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a4804 bytes abcc1a94
+ 005a4844 bytes 9bcd1a94
- 005a4814 ["INT_ADD", "register:40f0:8", ["const:5a4814:8", "const:4:8"]]
- 005a4814 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a4854 ["INT_ADD", "register:40f0:8", ["const:5a4854:8", "const:4:8"]]
+ 005a4854 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a4814 bytes a7cc1a94
+ 005a4854 bytes 97cd1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-958cb89ef134de7eaf597c3fcaeaaae7"></a>

### [`005a4838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4838.md) → [`005a4878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4878.md) FUN_005a4878

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a46dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a46dc.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005a471c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a471c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a4880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4838.md#insn-005a4880) · [`005a48a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4838.md#insn-005a48a4) · [`005a48b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4838.md#insn-005a48b4)
- 新版 `005a48c0`（命令位置の公開資料なし） · `005a48e4`（命令位置の公開資料なし） · `005a48f4`（命令位置の公開資料なし）

~~~diff
- 005a4880 ["INT_ADD", "register:40f0:8", ["const:5a4880:8", "const:4:8"]]
- 005a4880 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a48c0 ["INT_ADD", "register:40f0:8", ["const:5a48c0:8", "const:4:8"]]
+ 005a48c0 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a4880 bytes 8ccc1a94
+ 005a48c0 bytes 7ccd1a94
- 005a48a4 ["INT_ADD", "register:40f0:8", ["const:5a48a4:8", "const:4:8"]]
- 005a48a4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a48e4 ["INT_ADD", "register:40f0:8", ["const:5a48e4:8", "const:4:8"]]
+ 005a48e4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a48a4 bytes 83cc1a94
+ 005a48e4 bytes 73cd1a94
- 005a48b4 ["INT_ADD", "register:40f0:8", ["const:5a48b4:8", "const:4:8"]]
- 005a48b4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a48f4 ["INT_ADD", "register:40f0:8", ["const:5a48f4:8", "const:4:8"]]
+ 005a48f4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a48b4 bytes 7fcc1a94
+ 005a48f4 bytes 6fcd1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-636d8a5c1f5ae81940b981e1a1775391"></a>

### [`005a747c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a747c.md) → [`005a74bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a74bc.md) FUN_005a74bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a74c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a747c.md#insn-005a74c4)
- 新版 `005a7504`（命令位置の公開資料なし）

~~~diff
- 005a74c4 ["INT_ADD", "register:40f0:8", ["const:5a74c4:8", "const:4:8"]]
- 005a74c4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a7504 ["INT_ADD", "register:40f0:8", ["const:5a7504:8", "const:4:8"]]
+ 005a7504 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a74c4 bytes 7bc11a94
+ 005a7504 bytes 6bc21a94
~~~


<a id="compare-e462c2dbc8dbd5d932d2e591367ca42c"></a>

### [`005a77cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a77cc.md) → [`005a780c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a780c.md) FUN_005a780c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005a7c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7c74.md) [`009a6204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a6/009a6204.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`005a7928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7928.md) [`005a79b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a79b0.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`005a7cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7cb4.md) [`009a63a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a63a0.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005a7968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7968.md) [`005a79f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a79f0.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a7818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a77cc.md#insn-005a7818) · [`005a7898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a77cc.md#insn-005a7898) · [`005a78e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a77cc.md#insn-005a78e8)
- 新版 `005a7858`（命令位置の公開資料なし） · `005a78d8`（命令位置の公開資料なし） · `005a7928`（命令位置の公開資料なし）

~~~diff
- 005a7818 ["INT_ADD", "register:40f0:8", ["const:5a7818:8", "const:4:8"]]
- 005a7818 ["CALL", null, ["callee:00c57e90:8"]]
+ 005a7858 ["INT_ADD", "register:40f0:8", ["const:5a7858:8", "const:4:8"]]
+ 005a7858 ["CALL", null, ["callee:00c57e90:8"]]
- 005a7818 bytes 9ec01a94
+ 005a7858 bytes 8ec11a94
- 005a7898 ["INT_ADD", "register:40f0:8", ["const:5a7898:8", "const:4:8"]]
- 005a7898 ["CALL", null, ["callee:0043bb20:8"]]
+ 005a78d8 ["INT_ADD", "register:40f0:8", ["const:5a78d8:8", "const:4:8"]]
+ 005a78d8 ["CALL", null, ["callee:0043bb20:8"]]
- 005a7898 bytes 9250fa97
+ 005a78d8 bytes 9250fa97
- 005a78e8 ["INT_ADD", "register:40f0:8", ["const:5a78e8:8", "const:4:8"]]
- 005a78e8 ["CALL", null, ["callee:005a79f0:8"]]
+ 005a7928 ["INT_ADD", "register:40f0:8", ["const:5a7928:8", "const:4:8"]]
+ 005a7928 ["CALL", null, ["callee:005a79f0:8"]]
- 005a78e8 bytes 32000094
+ 005a7928 bytes 32000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b01061744214550bc92431e02f06817"></a>

### [`005a7928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7928.md) → [`005a7968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7968.md) FUN_005a7968

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a77cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a77cc.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005a780c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a780c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7928.md#insn-005a798c)
- 新版 `005a79cc`（命令位置の公開資料なし）

~~~diff
- 005a798c ["INT_ADD", "register:40f0:8", ["const:5a798c:8", "const:4:8"]]
- 005a798c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a79cc ["INT_ADD", "register:40f0:8", ["const:5a79cc:8", "const:4:8"]]
+ 005a79cc ["CALL", null, ["callee:00c57eb0:8"]]
- 005a798c bytes 49c01a94
+ 005a79cc bytes 39c11a94
~~~


<a id="compare-f756db82cc88b47c4a27901c60cd009d"></a>

### [`005a79c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a79c4.md) → [`005a7a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7a04.md) FUN_005a7a04

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a7a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a79c4.md#insn-005a7a04)
- 新版 `005a7a44`（命令位置の公開資料なし）

~~~diff
- 005a7a04 ["INT_ADD", "register:40f0:8", ["const:5a7a04:8", "const:4:8"]]
- 005a7a04 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a7a44 ["INT_ADD", "register:40f0:8", ["const:5a7a44:8", "const:4:8"]]
+ 005a7a44 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a7a04 bytes 2bc01a94
+ 005a7a44 bytes 1bc11a94
~~~


<a id="compare-bdac3eeab0f9496b76156c800f6855e8"></a>

### [`005a7a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7a18.md) → [`005a7a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7a58.md) FUN_005a7a58

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a6ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6ecc.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005a79b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a79b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005a6f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6f0c.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005a79f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a79f0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a7a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7a18.md#insn-005a7a9c) · [`005a7aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7a18.md#insn-005a7aec) · [`005a7b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7a18.md#insn-005a7b64)
- 新版 `005a7adc`（命令位置の公開資料なし） · `005a7b2c`（命令位置の公開資料なし） · `005a7ba4`（命令位置の公開資料なし）

~~~diff
- 005a7a9c ["INT_ADD", "register:40f0:8", ["const:5a7a9c:8", "const:4:8"]]
- 005a7a9c ["CALL", null, ["callee:00c57e90:8"]]
+ 005a7adc ["INT_ADD", "register:40f0:8", ["const:5a7adc:8", "const:4:8"]]
+ 005a7adc ["CALL", null, ["callee:00c57e90:8"]]
- 005a7a9c bytes fdbf1a94
+ 005a7adc bytes edc01a94
- 005a7aec ["INT_ADD", "register:40f0:8", ["const:5a7aec:8", "const:4:8"]]
- 005a7aec ["CALL", null, ["callee:0043bb20:8"]]
+ 005a7b2c ["INT_ADD", "register:40f0:8", ["const:5a7b2c:8", "const:4:8"]]
+ 005a7b2c ["CALL", null, ["callee:0043bb20:8"]]
- 005a7aec bytes fd4ffa97
+ 005a7b2c bytes fd4ffa97
- 005a7b64 ["INT_ADD", "register:40f0:8", ["const:5a7b64:8", "const:4:8"]]
- 005a7b64 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a7ba4 ["INT_ADD", "register:40f0:8", ["const:5a7ba4:8", "const:4:8"]]
+ 005a7ba4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a7b64 bytes d3bf1a94
+ 005a7ba4 bytes c3c01a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95dee609f90db9e19ff0dd6685ea72bb"></a>

### [`005a7c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7c0c.md) → [`005a7c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7c4c.md) FUN_005a7c4c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a7c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7c0c.md#insn-005a7c5c)
- 新版 `005a7c9c`（命令位置の公開資料なし）

~~~diff
- 005a7c5c ["INT_ADD", "register:40f0:8", ["const:5a7c5c:8", "const:4:8"]]
- 005a7c5c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a7c9c ["INT_ADD", "register:40f0:8", ["const:5a7c9c:8", "const:4:8"]]
+ 005a7c9c ["CALL", null, ["callee:00c57eb0:8"]]
- 005a7c5c bytes 95bf1a94
+ 005a7c9c bytes 85c01a94
~~~


<a id="compare-9931e9f516e7bc7c63d827c322d8f669"></a>

### [`005a8644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8644.md) → [`005a8684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8684.md) FUN_005a8684

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`0059bf04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059bf04.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57dd0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0059bf44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059bf44.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c581d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a8670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8644.md#insn-005a8670) · [`005a86a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8644.md#insn-005a86a0) · [`005a86b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8644.md#insn-005a86b0)
- 新版 `005a86b0`（命令位置の公開資料なし） · `005a86e0`（命令位置の公開資料なし） · `005a86f0`（命令位置の公開資料なし）

~~~diff
- 005a8670 ["INT_ADD", "register:40f0:8", ["const:5a8670:8", "const:4:8"]]
- 005a8670 ["CALL", null, ["callee:0059bf44:8"]]
+ 005a86b0 ["INT_ADD", "register:40f0:8", ["const:5a86b0:8", "const:4:8"]]
+ 005a86b0 ["CALL", null, ["callee:0059bf44:8"]]
- 005a8670 bytes 25ceff97
+ 005a86b0 bytes 25ceff97
- 005a86a0 ["INT_ADD", "register:40f0:8", ["const:5a86a0:8", "const:4:8"]]
- 005a86a0 ["CALL", null, ["callee:00c581d0:8"]]
+ 005a86e0 ["INT_ADD", "register:40f0:8", ["const:5a86e0:8", "const:4:8"]]
+ 005a86e0 ["CALL", null, ["callee:00c581d0:8"]]
- 005a86a0 bytes ccbd1a94
+ 005a86e0 bytes bcbe1a94
- 005a86b0 ["INT_ADD", "register:40f0:8", ["const:5a86b0:8", "const:4:8"]]
- 005a86b0 ["CALL", null, ["callee:0045179c:8"]]
+ 005a86f0 ["INT_ADD", "register:40f0:8", ["const:5a86f0:8", "const:4:8"]]
+ 005a86f0 ["CALL", null, ["callee:0045179c:8"]]
- 005a86b0 bytes 2ba4fa97
+ 005a86f0 bytes 2ba4fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bf643d5af12cf67d4dc804f5e6ff987"></a>

### [`005a96b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a96b4.md) → [`005a96f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a96f4.md) FUN_005a96f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005aa144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa144.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005aa184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa184.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a96ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a96b4.md#insn-005a96ec)
- 新版 `005a972c`（命令位置の公開資料なし）

~~~diff
- 005a96ec ["INT_ADD", "register:40f0:8", ["const:5a96ec:8", "const:4:8"]]
- 005a96ec ["CALL", null, ["callee:005aa184:8"]]
+ 005a972c ["INT_ADD", "register:40f0:8", ["const:5a972c:8", "const:4:8"]]
+ 005a972c ["CALL", null, ["callee:005aa184:8"]]
- 005a96ec bytes 96020094
+ 005a972c bytes 96020094
~~~


<a id="compare-c572ef554f2a68950c0cf8fd4f937147"></a>

### [`005a9cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9cc0.md) → [`005a9d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9d00.md) FUN_005a9d00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005a9bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9bdc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005a9c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9c1c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a9cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9cc0.md#insn-005a9cd0)
- 新版 `005a9d10`（命令位置の公開資料なし）

~~~diff
- 005a9cd0 ["INT_ADD", "register:40f0:8", ["const:5a9cd0:8", "const:4:8"]]
- 005a9cd0 ["CALL", null, ["callee:005a9c1c:8"]]
+ 005a9d10 ["INT_ADD", "register:40f0:8", ["const:5a9d10:8", "const:4:8"]]
+ 005a9d10 ["CALL", null, ["callee:005a9c1c:8"]]
- 005a9cd0 bytes c3ffff97
+ 005a9d10 bytes c3ffff97
~~~


<a id="compare-bb35d088501460d8cc6ae3b874c2b3af"></a>

### [`005a9ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ce4.md) → [`005a9d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9d24.md) FUN_005a9d24

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005a8c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8c5c.md) [`00749994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00749/00749994.md) [`009b6abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6abc.md) · 呼出先 6件 [`005a9e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9e24.md) [`005a9ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ea4.md) [`005a9f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9f14.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`005a8c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8c9c.md) [`007499d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00749/007499d4.md) [`009b6c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6c58.md) · 呼出先 6件 [`005a9e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9e64.md) [`005a9ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9ee4.md) [`005a9f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9f54.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a9d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ce4.md#insn-005a9d3c) · [`005a9d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ce4.md#insn-005a9d80) · [`005a9de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ce4.md#insn-005a9de4)
- 新版 `005a9d7c`（命令位置の公開資料なし） · `005a9dc0`（命令位置の公開資料なし） · `005a9e24`（命令位置の公開資料なし）

~~~diff
- 005a9d3c ["INT_ADD", "register:40f0:8", ["const:5a9d3c:8", "const:4:8"]]
- 005a9d3c ["CALL", null, ["callee:00c57e90:8"]]
+ 005a9d7c ["INT_ADD", "register:40f0:8", ["const:5a9d7c:8", "const:4:8"]]
+ 005a9d7c ["CALL", null, ["callee:00c57e90:8"]]
- 005a9d3c bytes 55b71a94
+ 005a9d7c bytes 45b81a94
- 005a9d80 ["INT_ADD", "register:40f0:8", ["const:5a9d80:8", "const:4:8"]]
- 005a9d80 ["CALL", null, ["callee:005a9f54:8"]]
+ 005a9dc0 ["INT_ADD", "register:40f0:8", ["const:5a9dc0:8", "const:4:8"]]
+ 005a9dc0 ["CALL", null, ["callee:005a9f54:8"]]
- 005a9d80 bytes 65000094
+ 005a9dc0 bytes 65000094
- 005a9de4 ["INT_ADD", "register:40f0:8", ["const:5a9de4:8", "const:4:8"]]
- 005a9de4 ["CALL", null, ["callee:005a9ee4:8"]]
+ 005a9e24 ["INT_ADD", "register:40f0:8", ["const:5a9e24:8", "const:4:8"]]
+ 005a9e24 ["CALL", null, ["callee:005a9ee4:8"]]
- 005a9de4 bytes 30000094
+ 005a9e24 bytes 30000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5301524803f2979035e9e25f4afb630d"></a>

### [`005a9e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9e24.md) → [`005a9e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9e64.md) FUN_005a9e64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a9ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ce4.md) · 呼出先 2件 [`005aa144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa144.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005a9d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9d24.md) · 呼出先 2件 [`005aa184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa184.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a9e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9e24.md#insn-005a9e78)
- 新版 `005a9eb8`（命令位置の公開資料なし）

~~~diff
- 005a9e78 ["INT_ADD", "register:40f0:8", ["const:5a9e78:8", "const:4:8"]]
- 005a9e78 ["CALL", null, ["callee:005aa184:8"]]
+ 005a9eb8 ["INT_ADD", "register:40f0:8", ["const:5a9eb8:8", "const:4:8"]]
+ 005a9eb8 ["CALL", null, ["callee:005aa184:8"]]
- 005a9e78 bytes b3000094
+ 005a9eb8 bytes b3000094
~~~


<a id="compare-218aece6d99e1e2208a953e7068aa206"></a>

### [`005a9eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9eb8.md) → [`005a9ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9ef8.md) FUN_005a9ef8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`005aa144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa144.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005aa184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa184.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a9ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9eb8.md#insn-005a9ef8)
- 新版 `005a9f38`（命令位置の公開資料なし）

~~~diff
- 005a9ef8 ["INT_ADD", "register:40f0:8", ["const:5a9ef8:8", "const:4:8"]]
- 005a9ef8 ["CALL", null, ["callee:005aa184:8"]]
+ 005a9f38 ["INT_ADD", "register:40f0:8", ["const:5a9f38:8", "const:4:8"]]
+ 005a9f38 ["CALL", null, ["callee:005aa184:8"]]
- 005a9ef8 bytes 93000094
+ 005a9f38 bytes 93000094
~~~


<a id="compare-ab7636b338bfd9bbc9048ec4e23ac41a"></a>

### [`005a9f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9f14.md) → [`005a9f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9f54.md) FUN_005a9f54

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`005a9ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ce4.md) [`00749994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00749/00749994.md) [`009aa488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009aa/009aa488.md) [`009b2f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2f98.md) [`009b5be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5be8.md) · 呼出先 7件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`005aa03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa03c.md) [`005aa130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa130.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 5件 [`005a9d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9d24.md) [`007499d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00749/007499d4.md) [`009aa624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009aa/009aa624.md) [`009b3134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3134.md) [`009b5d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b5d84.md) · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005aa07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa07c.md) [`005aa170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa170.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a9f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9f14.md#insn-005a9f68) · [`005a9fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9f14.md#insn-005a9fac) · [`005a9fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9f14.md#insn-005a9fc4)
- 新版 `005a9fa8`（命令位置の公開資料なし） · `005a9fec`（命令位置の公開資料なし） · `005aa004`（命令位置の公開資料なし）

~~~diff
- 005a9f68 ["INT_ADD", "register:40f0:8", ["const:5a9f68:8", "const:4:8"]]
- 005a9f68 ["CALL", null, ["callee:0043bb20:8"]]
+ 005a9fa8 ["INT_ADD", "register:40f0:8", ["const:5a9fa8:8", "const:4:8"]]
+ 005a9fa8 ["CALL", null, ["callee:0043bb20:8"]]
- 005a9f68 bytes de46fa97
+ 005a9fa8 bytes de46fa97
- 005a9fac ["INT_ADD", "register:40f0:8", ["const:5a9fac:8", "const:4:8"]]
- 005a9fac ["CALL", null, ["callee:00c57e90:8"]]
+ 005a9fec ["INT_ADD", "register:40f0:8", ["const:5a9fec:8", "const:4:8"]]
+ 005a9fec ["CALL", null, ["callee:00c57e90:8"]]
- 005a9fac bytes b9b61a94
+ 005a9fec bytes a9b71a94
- 005a9fc4 ["INT_ADD", "register:40f0:8", ["const:5a9fc4:8", "const:4:8"]]
- 005a9fc4 ["CALL", null, ["callee:00c58000:8"]]
+ 005aa004 ["INT_ADD", "register:40f0:8", ["const:5aa004:8", "const:4:8"]]
+ 005aa004 ["CALL", null, ["callee:00c58000:8"]]
- 005a9fc4 bytes 0fb71a94
+ 005aa004 bytes ffb71a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a34a68a4ea2ba2010b09b4975ad5d22"></a>

### [`005aa03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa03c.md) → [`005aa07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa07c.md) FUN_005aa07c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a9f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9f14.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 1件 [`005a9f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9f54.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005aa074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa03c.md#insn-005aa074) · [`005aa0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa03c.md#insn-005aa0a8) · [`005aa0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa03c.md#insn-005aa0d4)
- 新版 `005aa0b4`（命令位置の公開資料なし） · `005aa0e8`（命令位置の公開資料なし） · `005aa114`（命令位置の公開資料なし）

~~~diff
- 005aa074 ["INT_ADD", "register:40f0:8", ["const:5aa074:8", "const:4:8"]]
- 005aa074 ["CALL", null, ["callee:0043bb20:8"]]
+ 005aa0b4 ["INT_ADD", "register:40f0:8", ["const:5aa0b4:8", "const:4:8"]]
+ 005aa0b4 ["CALL", null, ["callee:0043bb20:8"]]
- 005aa074 bytes 9b46fa97
+ 005aa0b4 bytes 9b46fa97
- 005aa0a8 ["INT_ADD", "register:40f0:8", ["const:5aa0a8:8", "const:4:8"]]
- 005aa0a8 ["CALL", null, ["callee:0043bb20:8"]]
+ 005aa0e8 ["INT_ADD", "register:40f0:8", ["const:5aa0e8:8", "const:4:8"]]
+ 005aa0e8 ["CALL", null, ["callee:0043bb20:8"]]
- 005aa0a8 bytes 8e46fa97
+ 005aa0e8 bytes 8e46fa97
- 005aa0d4 ["INT_ADD", "register:40f0:8", ["const:5aa0d4:8", "const:4:8"]]
- 005aa0d4 ["CALL", null, ["callee:0043bb20:8"]]
+ 005aa114 ["INT_ADD", "register:40f0:8", ["const:5aa114:8", "const:4:8"]]
+ 005aa114 ["CALL", null, ["callee:0043bb20:8"]]
- 005aa0d4 bytes 8346fa97
+ 005aa114 bytes 8346fa97
~~~


<a id="compare-17b7b6125eda7204e95851b325d47773"></a>

### [`005aa144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa144.md) → [`005aa184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa184.md) FUN_005aa184

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`005a8de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8de8.md) [`005a96b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a96b4.md) [`005a9bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9bdc.md) [`005a9e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9e24.md) [`005a9eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9eb8.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 9件 [`005a8e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8e28.md) [`005a96f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a96f4.md) [`005a9c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9c1c.md) [`005a9e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9e64.md) [`005a9ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9ef8.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005aa178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa144.md#insn-005aa178) · [`005aa194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa144.md#insn-005aa194) · [`005aa1a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa144.md#insn-005aa1a4)
- 新版 `005aa1b8`（命令位置の公開資料なし） · `005aa1d4`（命令位置の公開資料なし） · `005aa1e4`（命令位置の公開資料なし）

~~~diff
- 005aa178 ["INT_ADD", "register:40f0:8", ["const:5aa178:8", "const:4:8"]]
- 005aa178 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005aa1b8 ["INT_ADD", "register:40f0:8", ["const:5aa1b8:8", "const:4:8"]]
+ 005aa1b8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005aa178 bytes 4eb61a94
+ 005aa1b8 bytes 3eb71a94
- 005aa194 ["INT_ADD", "register:40f0:8", ["const:5aa194:8", "const:4:8"]]
- 005aa194 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005aa1d4 ["INT_ADD", "register:40f0:8", ["const:5aa1d4:8", "const:4:8"]]
+ 005aa1d4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005aa194 bytes 47b61a94
+ 005aa1d4 bytes 37b71a94
- 005aa1a4 ["INT_ADD", "register:40f0:8", ["const:5aa1a4:8", "const:4:8"]]
- 005aa1a4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005aa1e4 ["INT_ADD", "register:40f0:8", ["const:5aa1e4:8", "const:4:8"]]
+ 005aa1e4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005aa1a4 bytes 43b61a94
+ 005aa1e4 bytes 33b71a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b2fc01c5549a4bd75fbb6cfe689c2a7"></a>

### [`005ac25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac25c.md) → [`005ac29c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac29c.md) FUN_005ac29c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`0059bf04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059bf04.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b50.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0059bf44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059bf44.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ac288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac25c.md#insn-005ac288) · [`005ac2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac25c.md#insn-005ac2b4) · [`005ac2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac25c.md#insn-005ac2c4)
- 新版 `005ac2c8`（命令位置の公開資料なし） · `005ac2f4`（命令位置の公開資料なし） · `005ac304`（命令位置の公開資料なし）

~~~diff
- 005ac288 ["INT_ADD", "register:40f0:8", ["const:5ac288:8", "const:4:8"]]
- 005ac288 ["CALL", null, ["callee:0059bf44:8"]]
+ 005ac2c8 ["INT_ADD", "register:40f0:8", ["const:5ac2c8:8", "const:4:8"]]
+ 005ac2c8 ["CALL", null, ["callee:0059bf44:8"]]
- 005ac288 bytes 1fbfff97
+ 005ac2c8 bytes 1fbfff97
- 005ac2b4 ["INT_ADD", "register:40f0:8", ["const:5ac2b4:8", "const:4:8"]]
- 005ac2b4 ["CALL", null, ["callee:00c57f50:8"]]
+ 005ac2f4 ["INT_ADD", "register:40f0:8", ["const:5ac2f4:8", "const:4:8"]]
+ 005ac2f4 ["CALL", null, ["callee:00c57f50:8"]]
- 005ac2b4 bytes 27ae1a94
+ 005ac2f4 bytes 17af1a94
- 005ac2c4 ["INT_ADD", "register:40f0:8", ["const:5ac2c4:8", "const:4:8"]]
- 005ac2c4 ["CALL", null, ["callee:0045179c:8"]]
+ 005ac304 ["INT_ADD", "register:40f0:8", ["const:5ac304:8", "const:4:8"]]
+ 005ac304 ["CALL", null, ["callee:0045179c:8"]]
- 005ac2c4 bytes 2695fa97
+ 005ac304 bytes 2695fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a078f524172c2defcad97b23b9399443"></a>

### [`005acdf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005acdf0.md) → [`005ace30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ace30.md) FUN_005ace30

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ace0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005acdf0.md#insn-005ace0c) · [`005ace2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005acdf0.md#insn-005ace2c)
- 新版 `005ace4c`（命令位置の公開資料なし） · `005ace6c`（命令位置の公開資料なし）

~~~diff
- 005ace0c ["INT_ADD", "register:40f0:8", ["const:5ace0c:8", "const:4:8"]]
- 005ace0c ["CALL", null, ["callee:00c53d00:8"]]
+ 005ace4c ["INT_ADD", "register:40f0:8", ["const:5ace4c:8", "const:4:8"]]
+ 005ace4c ["CALL", null, ["callee:00c53d00:8"]]
- 005ace0c bytes b59a1a94
+ 005ace4c bytes ad9b1a94
- 005ace2c ["COPY", "register:0:8", ["register:4040:8"]]
- 005ace2c ["INT_ADD", "register:40f0:8", ["const:5ace2c:8", "const:4:8"]]
- 005ace2c ["CALLIND", null, ["register:0:8"]]
+ 005ace6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ace6c ["INT_ADD", "register:40f0:8", ["const:5ace6c:8", "const:4:8"]]
+ 005ace6c ["CALLIND", null, ["register:0:8"]]
- 005ace2c bytes 00013fd6
+ 005ace6c bytes 00013fd6
~~~


<a id="compare-781d361316cbd16b5f3e318c69e2ae33"></a>

### [`005ace40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ace40.md) → [`005ace80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ace80.md) FUN_005ace80

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005aca04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005aca04.md) · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005aca44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca44.md) · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ace5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ace40.md#insn-005ace5c)
- 新版 `005ace9c`（命令位置の公開資料なし）

~~~diff
- 005ace5c ["INT_ADD", "register:40f0:8", ["const:5ace5c:8", "const:4:8"]]
- 005ace5c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ace9c ["INT_ADD", "register:40f0:8", ["const:5ace9c:8", "const:4:8"]]
+ 005ace9c ["CALL", null, ["callee:00c57eb0:8"]]
- 005ace5c bytes 15ab1a94
+ 005ace9c bytes 05ac1a94
~~~


<a id="compare-36346feda525de9ba0d3c955298e75e9"></a>

### [`005ad248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad248.md) → [`005ad288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad288.md) FUN_005ad288

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ad264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad248.md#insn-005ad264) · [`005ad278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad248.md#insn-005ad278) · [`005ad298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad248.md#insn-005ad298)
- 新版 `005ad2a4`（命令位置の公開資料なし） · `005ad2b8`（命令位置の公開資料なし） · `005ad2d8`（命令位置の公開資料なし）

~~~diff
- 005ad264 ["INT_ADD", "register:40f0:8", ["const:5ad264:8", "const:4:8"]]
- 005ad264 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ad2a4 ["INT_ADD", "register:40f0:8", ["const:5ad2a4:8", "const:4:8"]]
+ 005ad2a4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ad264 bytes 13aa1a94
+ 005ad2a4 bytes 03ab1a94
- 005ad278 ["INT_ADD", "register:40f0:8", ["const:5ad278:8", "const:4:8"]]
- 005ad278 ["CALL", null, ["callee:00c53d00:8"]]
+ 005ad2b8 ["INT_ADD", "register:40f0:8", ["const:5ad2b8:8", "const:4:8"]]
+ 005ad2b8 ["CALL", null, ["callee:00c53d00:8"]]
- 005ad278 bytes 9a991a94
+ 005ad2b8 bytes 929a1a94
- 005ad298 ["COPY", "register:0:8", ["register:4040:8"]]
- 005ad298 ["INT_ADD", "register:40f0:8", ["const:5ad298:8", "const:4:8"]]
- 005ad298 ["CALLIND", null, ["register:0:8"]]
+ 005ad2d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ad2d8 ["INT_ADD", "register:40f0:8", ["const:5ad2d8:8", "const:4:8"]]
+ 005ad2d8 ["CALLIND", null, ["register:0:8"]]
- 005ad298 bytes 00013fd6
+ 005ad2d8 bytes 00013fd6
~~~


<a id="compare-c3015b34378ee530bcef4fcf4c74851e"></a>

### [`005ad2ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad2ac.md) → [`005ad2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad2ec.md) FUN_005ad2ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b4550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4550.md) · 呼出先 2件 [`005af740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005af740.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005b4590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4590.md) · 呼出先 2件 [`005af780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005af780.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ad2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad2ac.md#insn-005ad2e8) · [`005ad314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad2ac.md#insn-005ad314) · [`005ad324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad2ac.md#insn-005ad324)
- 新版 `005ad328`（命令位置の公開資料なし） · `005ad354`（命令位置の公開資料なし） · `005ad364`（命令位置の公開資料なし）

~~~diff
- 005ad2e8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005ad2e8 ["INT_ADD", "register:40f0:8", ["const:5ad2e8:8", "const:4:8"]]
- 005ad2e8 ["CALLIND", null, ["register:0:8"]]
+ 005ad328 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005ad328 ["INT_ADD", "register:40f0:8", ["const:5ad328:8", "const:4:8"]]
+ 005ad328 ["CALLIND", null, ["register:0:8"]]
- 005ad2e8 bytes 20013fd6
+ 005ad328 bytes 20013fd6
- 005ad314 ["COPY", "register:0:8", ["register:4040:8"]]
- 005ad314 ["INT_ADD", "register:40f0:8", ["const:5ad314:8", "const:4:8"]]
- 005ad314 ["CALLIND", null, ["register:0:8"]]
+ 005ad354 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ad354 ["INT_ADD", "register:40f0:8", ["const:5ad354:8", "const:4:8"]]
+ 005ad354 ["CALLIND", null, ["register:0:8"]]
- 005ad314 bytes 00013fd6
+ 005ad354 bytes 00013fd6
- 005ad324 ["INT_ADD", "register:40f0:8", ["const:5ad324:8", "const:4:8"]]
- 005ad324 ["CALL", null, ["callee:005af780:8"]]
+ 005ad364 ["INT_ADD", "register:40f0:8", ["const:5ad364:8", "const:4:8"]]
+ 005ad364 ["CALL", null, ["callee:005af780:8"]]
- 005ad324 bytes 07090094
+ 005ad364 bytes 07090094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d9eaff9073d61aadb2f7464d17d4e77"></a>

### [`005ad378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad378.md) → [`005ad3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad3b8.md) FUN_005ad3b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b4550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4550.md) · 呼出先 2件 [`0058f3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f3f4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005b4590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4590.md) · 呼出先 2件 [`0058f434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f434.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ad3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad378.md#insn-005ad3b4) · [`005ad3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad378.md#insn-005ad3e0) · [`005ad3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad378.md#insn-005ad3f0)
- 新版 `005ad3f4`（命令位置の公開資料なし） · `005ad420`（命令位置の公開資料なし） · `005ad430`（命令位置の公開資料なし）

~~~diff
- 005ad3b4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005ad3b4 ["INT_ADD", "register:40f0:8", ["const:5ad3b4:8", "const:4:8"]]
- 005ad3b4 ["CALLIND", null, ["register:0:8"]]
+ 005ad3f4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005ad3f4 ["INT_ADD", "register:40f0:8", ["const:5ad3f4:8", "const:4:8"]]
+ 005ad3f4 ["CALLIND", null, ["register:0:8"]]
- 005ad3b4 bytes 20013fd6
+ 005ad3f4 bytes 20013fd6
- 005ad3e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005ad3e0 ["INT_ADD", "register:40f0:8", ["const:5ad3e0:8", "const:4:8"]]
- 005ad3e0 ["CALLIND", null, ["register:0:8"]]
+ 005ad420 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ad420 ["INT_ADD", "register:40f0:8", ["const:5ad420:8", "const:4:8"]]
+ 005ad420 ["CALLIND", null, ["register:0:8"]]
- 005ad3e0 bytes 00013fd6
+ 005ad420 bytes 00013fd6
- 005ad3f0 ["INT_ADD", "register:40f0:8", ["const:5ad3f0:8", "const:4:8"]]
- 005ad3f0 ["CALL", null, ["callee:0058f434:8"]]
+ 005ad430 ["INT_ADD", "register:40f0:8", ["const:5ad430:8", "const:4:8"]]
+ 005ad430 ["CALL", null, ["callee:0058f434:8"]]
- 005ad3f0 bytes 0188ff97
+ 005ad430 bytes 0188ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c29da48b96bf8faf551d9dc46d4a6a5"></a>

### [`005ad724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad724.md) → [`005ad764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad764.md) FUN_005ad764

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ad740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad724.md#insn-005ad740)
- 新版 `005ad780`（命令位置の公開資料なし）

~~~diff
- 005ad740 ["INT_ADD", "register:40f0:8", ["const:5ad740:8", "const:4:8"]]
- 005ad740 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ad780 ["INT_ADD", "register:40f0:8", ["const:5ad780:8", "const:4:8"]]
+ 005ad780 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ad740 bytes dca81a94
+ 005ad780 bytes cca91a94
~~~


<a id="compare-bb9ca8b185a8b9c884de5c905b2b9e2c"></a>

### [`005ad764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad764.md) → [`005ad7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7a4.md) FUN_005ad7a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005aca04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005aca04.md) · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005aca44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca44.md) · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ad780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad764.md#insn-005ad780) · [`005ad78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad764.md#insn-005ad78c)
- 新版 `005ad7c0`（命令位置の公開資料なし） · `005ad7cc`（命令位置の公開資料なし）

~~~diff
- 005ad780 ["INT_ADD", "register:40f0:8", ["const:5ad780:8", "const:4:8"]]
- 005ad780 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ad7c0 ["INT_ADD", "register:40f0:8", ["const:5ad7c0:8", "const:4:8"]]
+ 005ad7c0 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ad780 bytes cca81a94
+ 005ad7c0 bytes bca91a94
- 005ad78c ["INT_ADD", "register:40f0:8", ["const:5ad78c:8", "const:4:8"]]
- 005ad78c ["CALL", null, ["callee:00c57e80:8"]]
+ 005ad7cc ["INT_ADD", "register:40f0:8", ["const:5ad7cc:8", "const:4:8"]]
+ 005ad7cc ["CALL", null, ["callee:00c57e80:8"]]
- 005ad78c bytes bda81a94
+ 005ad7cc bytes ada91a94
~~~


<a id="compare-cbbfc1ab74c6deb91010c283605beaee"></a>

### [`005ae7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae7e0.md) → [`005ae820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae820.md) FUN_005ae820

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ae7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae7e0.md#insn-005ae7fc) · [`005ae810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae7e0.md#insn-005ae810) · [`005ae830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae7e0.md#insn-005ae830)
- 新版 `005ae83c`（命令位置の公開資料なし） · `005ae850`（命令位置の公開資料なし） · `005ae870`（命令位置の公開資料なし）

~~~diff
- 005ae7fc ["INT_ADD", "register:40f0:8", ["const:5ae7fc:8", "const:4:8"]]
- 005ae7fc ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ae83c ["INT_ADD", "register:40f0:8", ["const:5ae83c:8", "const:4:8"]]
+ 005ae83c ["CALL", null, ["callee:00c57eb0:8"]]
- 005ae7fc bytes ada41a94
+ 005ae83c bytes 9da51a94
- 005ae810 ["INT_ADD", "register:40f0:8", ["const:5ae810:8", "const:4:8"]]
- 005ae810 ["CALL", null, ["callee:00c53d00:8"]]
+ 005ae850 ["INT_ADD", "register:40f0:8", ["const:5ae850:8", "const:4:8"]]
+ 005ae850 ["CALL", null, ["callee:00c53d00:8"]]
- 005ae810 bytes 34941a94
+ 005ae850 bytes 2c951a94
- 005ae830 ["COPY", "register:0:8", ["register:4040:8"]]
- 005ae830 ["INT_ADD", "register:40f0:8", ["const:5ae830:8", "const:4:8"]]
- 005ae830 ["CALLIND", null, ["register:0:8"]]
+ 005ae870 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ae870 ["INT_ADD", "register:40f0:8", ["const:5ae870:8", "const:4:8"]]
+ 005ae870 ["CALLIND", null, ["register:0:8"]]
- 005ae830 bytes 00013fd6
+ 005ae870 bytes 00013fd6
~~~


<a id="compare-8ea448fcf2c8c498233c09e12d618286"></a>

### [`005ae844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae844.md) → [`005ae884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae884.md) FUN_005ae884

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005ace80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ace80.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005acec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005acec0.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ae860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae844.md#insn-005ae860) · [`005ae874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae844.md#insn-005ae874) · [`005ae888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae844.md#insn-005ae888)
- 新版 `005ae8a0`（命令位置の公開資料なし） · `005ae8b4`（命令位置の公開資料なし） · `005ae8c8`（命令位置の公開資料なし）

~~~diff
- 005ae860 ["INT_ADD", "register:40f0:8", ["const:5ae860:8", "const:4:8"]]
- 005ae860 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ae8a0 ["INT_ADD", "register:40f0:8", ["const:5ae8a0:8", "const:4:8"]]
+ 005ae8a0 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ae860 bytes 94a41a94
+ 005ae8a0 bytes 84a51a94
- 005ae874 ["INT_ADD", "register:40f0:8", ["const:5ae874:8", "const:4:8"]]
- 005ae874 ["CALL", null, ["callee:00c53d00:8"]]
+ 005ae8b4 ["INT_ADD", "register:40f0:8", ["const:5ae8b4:8", "const:4:8"]]
+ 005ae8b4 ["CALL", null, ["callee:00c53d00:8"]]
- 005ae874 bytes 1b941a94
+ 005ae8b4 bytes 13951a94
- 005ae888 ["COPY", "register:0:8", ["register:4040:8"]]
- 005ae888 ["INT_ADD", "register:40f0:8", ["const:5ae888:8", "const:4:8"]]
- 005ae888 ["CALLIND", null, ["register:0:8"]]
+ 005ae8c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ae8c8 ["INT_ADD", "register:40f0:8", ["const:5ae8c8:8", "const:4:8"]]
+ 005ae8c8 ["CALLIND", null, ["register:0:8"]]
- 005ae888 bytes 00013fd6
+ 005ae8c8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a63f562c4a104ed15fcafc6771c04169"></a>

### [`005af740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005af740.md) → [`005af780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005af780.md) FUN_005af780

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005ad2ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad2ac.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005ad2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad2ec.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005af7ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005af740.md#insn-005af7ac) · [`005af7bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005af740.md#insn-005af7bc) · [`005af7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005af740.md#insn-005af7dc)
- 新版 `005af7ec`（命令位置の公開資料なし） · `005af7fc`（命令位置の公開資料なし） · `005af81c`（命令位置の公開資料なし）

~~~diff
- 005af7ac ["COPY", "register:0:8", ["register:4040:8"]]
- 005af7ac ["INT_ADD", "register:40f0:8", ["const:5af7ac:8", "const:4:8"]]
- 005af7ac ["CALLIND", null, ["register:0:8"]]
+ 005af7ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 005af7ec ["INT_ADD", "register:40f0:8", ["const:5af7ec:8", "const:4:8"]]
+ 005af7ec ["CALLIND", null, ["register:0:8"]]
- 005af7ac bytes 00013fd6
+ 005af7ec bytes 00013fd6
- 005af7bc ["COPY", "register:0:8", ["register:4040:8"]]
- 005af7bc ["INT_ADD", "register:40f0:8", ["const:5af7bc:8", "const:4:8"]]
- 005af7bc ["CALLIND", null, ["register:0:8"]]
+ 005af7fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005af7fc ["INT_ADD", "register:40f0:8", ["const:5af7fc:8", "const:4:8"]]
+ 005af7fc ["CALLIND", null, ["register:0:8"]]
- 005af7bc bytes 00013fd6
+ 005af7fc bytes 00013fd6
- 005af7dc ["COPY", "register:0:8", ["register:4040:8"]]
- 005af7dc ["INT_ADD", "register:40f0:8", ["const:5af7dc:8", "const:4:8"]]
- 005af7dc ["CALLIND", null, ["register:0:8"]]
+ 005af81c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005af81c ["INT_ADD", "register:40f0:8", ["const:5af81c:8", "const:4:8"]]
+ 005af81c ["CALLIND", null, ["register:0:8"]]
- 005af7dc bytes 00013fd6
+ 005af81c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d749c103e3fbd1bf674888f9b6d74000"></a>

### [`005afc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afc38.md) → [`005afc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afc78.md) FUN_005afc78

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 11件 [`005afdac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afdac.md) [`005afdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afdc8.md) [`005aff1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005aff1c.md) [`005b0080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0080.md) [`005b0100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0100.md) · 呼出先 7件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00903da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00903/00903da8.md) [`009e0e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0e24.md) [`009e4568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e4/009e4568.md)
- 新版 呼出元 11件 [`005afdec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afdec.md) [`005afe08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afe08.md) [`005aff5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005aff5c.md) [`005b00c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b00c0.md) [`005b0140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0140.md) · 呼出先 7件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00903f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00903/00903f44.md) [`009e0fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0fc0.md) [`009e4704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e4/009e4704.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005afc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afc38.md#insn-005afc50) · [`005afc64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afc38.md#insn-005afc64) · [`005afc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afc38.md#insn-005afc6c)
- 新版 `005afc90`（命令位置の公開資料なし） · `005afca4`（命令位置の公開資料なし） · `005afcac`（命令位置の公開資料なし）

~~~diff
- 005afc50 ["INT_ADD", "register:40f0:8", ["const:5afc50:8", "const:4:8"]]
- 005afc50 ["CALL", null, ["callee:008514f8:8"]]
+ 005afc90 ["INT_ADD", "register:40f0:8", ["const:5afc90:8", "const:4:8"]]
+ 005afc90 ["CALL", null, ["callee:008514f8:8"]]
- 005afc50 bytes 1a860a94
+ 005afc90 bytes 1a860a94
- 005afc64 ["INT_ADD", "register:40f0:8", ["const:5afc64:8", "const:4:8"]]
- 005afc64 ["CALL", null, ["callee:00903f44:8"]]
+ 005afca4 ["INT_ADD", "register:40f0:8", ["const:5afca4:8", "const:4:8"]]
+ 005afca4 ["CALL", null, ["callee:00903f44:8"]]
- 005afc64 bytes 51500d94
+ 005afca4 bytes a8500d94
- 005afc6c ["INT_ADD", "register:40f0:8", ["const:5afc6c:8", "const:4:8"]]
- 005afc6c ["CALL", null, ["callee:008514f8:8"]]
+ 005afcac ["INT_ADD", "register:40f0:8", ["const:5afcac:8", "const:4:8"]]
+ 005afcac ["CALL", null, ["callee:008514f8:8"]]
- 005afc6c bytes 13860a94
+ 005afcac bytes 13860a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8feedc73867189f350c82bc29c9f3956"></a>

### [`005afdac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afdac.md) → [`005afdec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afdec.md) FUN_005afdec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 1件 [`005afc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afc38.md)
- 新版 呼出元 1件 [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 1件 [`005afc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afc78.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005afdb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afdac.md#insn-005afdb8)
- 新版 `005afdf8`（命令位置の公開資料なし）

~~~diff
- 005afdb8 ["INT_ADD", "register:40f0:8", ["const:5afdb8:8", "const:4:8"]]
- 005afdb8 ["CALL", null, ["callee:005afc78:8"]]
+ 005afdf8 ["INT_ADD", "register:40f0:8", ["const:5afdf8:8", "const:4:8"]]
+ 005afdf8 ["CALL", null, ["callee:005afc78:8"]]
- 005afdb8 bytes a0ffff97
+ 005afdf8 bytes a0ffff97
~~~


<a id="compare-555a29509972086b3ce12bbfa5ff9f73"></a>

### [`005afdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afdc8.md) → [`005afe08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afe08.md) FUN_005afe08

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 8件 [`005afc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afc38.md) [`00662838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/00662838.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008c2ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c2ce0.md) [`00903da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00903/00903da8.md)
- 新版 呼出元 1件 [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 8件 [`005afc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afc78.md) [`00662878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/00662878.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008c2d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c2/008c2d24.md) [`00903f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00903/00903f44.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005afdd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afdc8.md#insn-005afdd8) · [`005afde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afdc8.md#insn-005afde4) · [`005afe08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afdc8.md#insn-005afe08)
- 新版 `005afe18`（命令位置の公開資料なし） · `005afe24`（命令位置の公開資料なし） · `005afe48`（命令位置の公開資料なし）

~~~diff
- 005afdd8 ["INT_ADD", "register:40f0:8", ["const:5afdd8:8", "const:4:8"]]
- 005afdd8 ["CALL", null, ["callee:005afc78:8"]]
+ 005afe18 ["INT_ADD", "register:40f0:8", ["const:5afe18:8", "const:4:8"]]
+ 005afe18 ["CALL", null, ["callee:005afc78:8"]]
- 005afdd8 bytes 98ffff97
+ 005afe18 bytes 98ffff97
- 005afde4 ["INT_ADD", "register:40f0:8", ["const:5afde4:8", "const:4:8"]]
- 005afde4 ["CALL", null, ["callee:005afc78:8"]]
+ 005afe24 ["INT_ADD", "register:40f0:8", ["const:5afe24:8", "const:4:8"]]
+ 005afe24 ["CALL", null, ["callee:005afc78:8"]]
- 005afde4 bytes 95ffff97
+ 005afe24 bytes 95ffff97
- 005afe08 ["INT_ADD", "register:40f0:8", ["const:5afe08:8", "const:4:8"]]
- 005afe08 ["CALL", null, ["callee:005afc78:8"]]
+ 005afe48 ["INT_ADD", "register:40f0:8", ["const:5afe48:8", "const:4:8"]]
+ 005afe48 ["CALL", null, ["callee:005afc78:8"]]
- 005afe08 bytes 8cffff97
+ 005afe48 bytes 8cffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93625e2bd5ff1b9ff1e43619b423d1d6"></a>

### [`005b0b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0b9c.md) → [`005b0bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0bdc.md) FUN_005b0bdc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005b20ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b20ec.md) [`005b3100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3100.md) [`005b68d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b68d8.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`005b0c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0c08.md)
- 新版 呼出元 3件 [`005b212c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b212c.md) [`005b3140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3140.md) [`005b6918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6918.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005b0c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0c48.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b0bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0b9c.md#insn-005b0bd4) · [`005b0bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0b9c.md#insn-005b0bdc)
- 新版 `005b0c14`（命令位置の公開資料なし） · `005b0c1c`（命令位置の公開資料なし）

~~~diff
- 005b0bd4 ["INT_ADD", "register:40f0:8", ["const:5b0bd4:8", "const:4:8"]]
- 005b0bd4 ["CALL", null, ["callee:0043bb20:8"]]
+ 005b0c14 ["INT_ADD", "register:40f0:8", ["const:5b0c14:8", "const:4:8"]]
+ 005b0c14 ["CALL", null, ["callee:0043bb20:8"]]
- 005b0bd4 bytes c32bfa97
+ 005b0c14 bytes c32bfa97
- 005b0bdc ["INT_ADD", "register:40f0:8", ["const:5b0bdc:8", "const:4:8"]]
- 005b0bdc ["CALL", null, ["callee:005b0c48:8"]]
+ 005b0c1c ["INT_ADD", "register:40f0:8", ["const:5b0c1c:8", "const:4:8"]]
+ 005b0c1c ["CALL", null, ["callee:005b0c48:8"]]
- 005b0bdc bytes 0b000094
+ 005b0c1c bytes 0b000094
~~~


<a id="compare-b81b3810f6bfb48cf404d281d26407a0"></a>

### [`005b12f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b12f8.md) → [`005b1338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1338.md) FUN_005b1338

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) · 呼出先 2件 [`00879b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879b78.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) · 呼出先 2件 [`00879bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879bb8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b130c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b12f8.md#insn-005b130c) · [`005b1314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b12f8.md#insn-005b1314)
- 新版 `005b134c`（命令位置の公開資料なし） · `005b1354`（命令位置の公開資料なし）

~~~diff
- 005b130c ["INT_ADD", "register:40f0:8", ["const:5b130c:8", "const:4:8"]]
- 005b130c ["CALL", null, ["callee:00c57e90:8"]]
+ 005b134c ["INT_ADD", "register:40f0:8", ["const:5b134c:8", "const:4:8"]]
+ 005b134c ["CALL", null, ["callee:00c57e90:8"]]
- 005b130c bytes e1991a94
+ 005b134c bytes d19a1a94
- 005b1314 ["INT_ADD", "register:40f0:8", ["const:5b1314:8", "const:4:8"]]
- 005b1314 ["CALL", null, ["callee:00879bb8:8"]]
+ 005b1354 ["INT_ADD", "register:40f0:8", ["const:5b1354:8", "const:4:8"]]
+ 005b1354 ["CALL", null, ["callee:00879bb8:8"]]
- 005b1314 bytes 19220b94
+ 005b1354 bytes 19220b94
~~~


<a id="compare-2af0ac7e497c45efc6c6851255e2bfff"></a>

### [`005b1368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1368.md) → [`005b13a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b13a8.md) FUN_005b13a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`008485ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008485ac.md) [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) · 呼出先 4件 [`005b51e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b51e0.md) [`005b5250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5250.md) [`00879d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879d3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008485ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/008485ec.md) [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) · 呼出先 4件 [`005b5220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5220.md) [`005b5290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5290.md) [`00879d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879d7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b1384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1368.md#insn-005b1384) · [`005b13b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1368.md#insn-005b13b4) · [`005b13c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1368.md#insn-005b13c0)
- 新版 `005b13c4`（命令位置の公開資料なし） · `005b13f4`（命令位置の公開資料なし） · `005b1400`（命令位置の公開資料なし）

~~~diff
- 005b1384 ["INT_ADD", "register:40f0:8", ["const:5b1384:8", "const:4:8"]]
- 005b1384 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b13c4 ["INT_ADD", "register:40f0:8", ["const:5b13c4:8", "const:4:8"]]
+ 005b13c4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005b1384 bytes cb991a94
+ 005b13c4 bytes bb9a1a94
- 005b13b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b13b4 ["INT_ADD", "register:40f0:8", ["const:5b13b4:8", "const:4:8"]]
- 005b13b4 ["CALLIND", null, ["register:0:8"]]
+ 005b13f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b13f4 ["INT_ADD", "register:40f0:8", ["const:5b13f4:8", "const:4:8"]]
+ 005b13f4 ["CALLIND", null, ["register:0:8"]]
- 005b13b4 bytes 00013fd6
+ 005b13f4 bytes 00013fd6
- 005b13c0 ["INT_ADD", "register:40f0:8", ["const:5b13c0:8", "const:4:8"]]
- 005b13c0 ["CALL", null, ["callee:005b5290:8"]]
+ 005b1400 ["INT_ADD", "register:40f0:8", ["const:5b1400:8", "const:4:8"]]
+ 005b1400 ["CALL", null, ["callee:005b5290:8"]]
- 005b13c0 bytes a40f0094
+ 005b1400 bytes a40f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c53ed110f6a5aa9c6f4370708179961e"></a>

### [`005b1400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1400.md) → [`005b1440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1440.md) FUN_005b1440

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a8a220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8a/00a8a220.md) · 呼出先 2件 [`005b51e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b51e0.md) [`005b5250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5250.md)
- 新版 呼出元 1件 [`00a8d008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8d/00a8d008.md) · 呼出先 2件 [`005b5220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5220.md) [`005b5290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b1438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1400.md#insn-005b1438) · [`005b1450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1400.md#insn-005b1450)
- 新版 `005b1478`（命令位置の公開資料なし） · `005b1490`（命令位置の公開資料なし）

~~~diff
- 005b1438 ["INT_ADD", "register:40f0:8", ["const:5b1438:8", "const:4:8"]]
- 005b1438 ["CALL", null, ["callee:005b5220:8"]]
+ 005b1478 ["INT_ADD", "register:40f0:8", ["const:5b1478:8", "const:4:8"]]
+ 005b1478 ["CALL", null, ["callee:005b5220:8"]]
- 005b1438 bytes 6a0f0094
+ 005b1478 bytes 6a0f0094
- 005b1450 ["INT_ADD", "register:40f0:8", ["const:5b1450:8", "const:4:8"]]
- 005b1450 ["CALL", null, ["callee:005b5290:8"]]
+ 005b1490 ["INT_ADD", "register:40f0:8", ["const:5b1490:8", "const:4:8"]]
+ 005b1490 ["CALL", null, ["callee:005b5290:8"]]
- 005b1450 bytes 800f0094
+ 005b1490 bytes 800f0094
~~~


<a id="compare-8079b7b1afe499394903ac2e0b137fbc"></a>

### [`005b2260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2260.md) → [`005b22a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b22a0.md) FUN_005b22a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b227c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2260.md#insn-005b227c) · [`005b229c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2260.md#insn-005b229c)
- 新版 `005b22bc`（命令位置の公開資料なし） · `005b22dc`（命令位置の公開資料なし）

~~~diff
- 005b227c ["INT_ADD", "register:40f0:8", ["const:5b227c:8", "const:4:8"]]
- 005b227c ["CALL", null, ["callee:00c53d00:8"]]
+ 005b22bc ["INT_ADD", "register:40f0:8", ["const:5b22bc:8", "const:4:8"]]
+ 005b22bc ["CALL", null, ["callee:00c53d00:8"]]
- 005b227c bytes 99851a94
+ 005b22bc bytes 91861a94
- 005b229c ["COPY", "register:0:8", ["register:4040:8"]]
- 005b229c ["INT_ADD", "register:40f0:8", ["const:5b229c:8", "const:4:8"]]
- 005b229c ["CALLIND", null, ["register:0:8"]]
+ 005b22dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b22dc ["INT_ADD", "register:40f0:8", ["const:5b22dc:8", "const:4:8"]]
+ 005b22dc ["CALLIND", null, ["register:0:8"]]
- 005b229c bytes 00013fd6
+ 005b22dc bytes 00013fd6
~~~


<a id="compare-714e231f7d2abf729c9e8414c43187f0"></a>

### [`005b2c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2c50.md) → [`005b2c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2c90.md) FUN_005b2c90

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`005b2ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2ac8.md) [`008650d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/008650d0.md) [`0089598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) [`008a7264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7264.md) · 呼出先 6件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`005b9358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9358.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`005b2b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2b08.md) [`00865110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865110.md) [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) [`008a72a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a72a8.md) · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`005b9398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9398.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b2d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2c50.md#insn-005b2d2c) · [`005b2d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2c50.md#insn-005b2d5c) · [`005b2d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2c50.md#insn-005b2d64)
- 新版 `005b2d6c`（命令位置の公開資料なし） · `005b2d9c`（命令位置の公開資料なし） · `005b2da4`（命令位置の公開資料なし）

~~~diff
- 005b2d2c ["INT_ADD", "register:40f0:8", ["const:5b2d2c:8", "const:4:8"]]
- 005b2d2c ["CALL", null, ["callee:00494610:8"]]
+ 005b2d6c ["INT_ADD", "register:40f0:8", ["const:5b2d6c:8", "const:4:8"]]
+ 005b2d6c ["CALL", null, ["callee:00494610:8"]]
- 005b2d2c bytes 2986fb97
+ 005b2d6c bytes 2986fb97
- 005b2d5c ["COPY", "register:0:8", ["register:4040:8"]]
- 005b2d5c ["INT_ADD", "register:40f0:8", ["const:5b2d5c:8", "const:4:8"]]
- 005b2d5c ["CALLIND", null, ["register:0:8"]]
+ 005b2d9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b2d9c ["INT_ADD", "register:40f0:8", ["const:5b2d9c:8", "const:4:8"]]
+ 005b2d9c ["CALLIND", null, ["register:0:8"]]
- 005b2d5c bytes 00013fd6
+ 005b2d9c bytes 00013fd6
- 005b2d64 ["INT_ADD", "register:40f0:8", ["const:5b2d64:8", "const:4:8"]]
- 005b2d64 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b2da4 ["INT_ADD", "register:40f0:8", ["const:5b2da4:8", "const:4:8"]]
+ 005b2da4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005b2d64 bytes 53931a94
+ 005b2da4 bytes 43941a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1da111b96eafd517bd6a392b0eb9344d"></a>

### [`005b2ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2ea8.md) → [`005b2ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2ee8.md) FUN_005b2ee8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`005b2ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2ac8.md) [`008650d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/008650d0.md) [`0089598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) [`008a7264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7264.md) · 呼出先 6件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`005b94c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b94c0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`005b2b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2b08.md) [`00865110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865110.md) [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) [`008a72a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a72a8.md) · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`005b9500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9500.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b2f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2ea8.md#insn-005b2f84) · [`005b2fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2ea8.md#insn-005b2fb4) · [`005b2fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2ea8.md#insn-005b2fbc)
- 新版 `005b2fc4`（命令位置の公開資料なし） · `005b2ff4`（命令位置の公開資料なし） · `005b2ffc`（命令位置の公開資料なし）

~~~diff
- 005b2f84 ["INT_ADD", "register:40f0:8", ["const:5b2f84:8", "const:4:8"]]
- 005b2f84 ["CALL", null, ["callee:00494610:8"]]
+ 005b2fc4 ["INT_ADD", "register:40f0:8", ["const:5b2fc4:8", "const:4:8"]]
+ 005b2fc4 ["CALL", null, ["callee:00494610:8"]]
- 005b2f84 bytes 9385fb97
+ 005b2fc4 bytes 9385fb97
- 005b2fb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b2fb4 ["INT_ADD", "register:40f0:8", ["const:5b2fb4:8", "const:4:8"]]
- 005b2fb4 ["CALLIND", null, ["register:0:8"]]
+ 005b2ff4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b2ff4 ["INT_ADD", "register:40f0:8", ["const:5b2ff4:8", "const:4:8"]]
+ 005b2ff4 ["CALLIND", null, ["register:0:8"]]
- 005b2fb4 bytes 00013fd6
+ 005b2ff4 bytes 00013fd6
- 005b2fbc ["INT_ADD", "register:40f0:8", ["const:5b2fbc:8", "const:4:8"]]
- 005b2fbc ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b2ffc ["INT_ADD", "register:40f0:8", ["const:5b2ffc:8", "const:4:8"]]
+ 005b2ffc ["CALL", null, ["callee:00c57eb0:8"]]
- 005b2fbc bytes bd921a94
+ 005b2ffc bytes ad931a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68f50f590c69e0c2c76d2c9b91b46a7f"></a>

### [`005b4e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4e14.md) → [`005b4e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4e54.md) FUN_005b4e54

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005b1de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1de4.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0059c85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c85c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005b1e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1e24.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0059c89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059c/0059c89c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b4e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4e14.md#insn-005b4e4c) · [`005b4e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4e14.md#insn-005b4e78) · [`005b4ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4e14.md#insn-005b4ea4)
- 新版 `005b4e8c`（命令位置の公開資料なし） · `005b4eb8`（命令位置の公開資料なし） · `005b4ee4`（命令位置の公開資料なし）

~~~diff
- 005b4e4c ["INT_ADD", "register:40f0:8", ["const:5b4e4c:8", "const:4:8"]]
- 005b4e4c ["CALL", null, ["callee:00c57e90:8"]]
+ 005b4e8c ["INT_ADD", "register:40f0:8", ["const:5b4e8c:8", "const:4:8"]]
+ 005b4e8c ["CALL", null, ["callee:00c57e90:8"]]
- 005b4e4c bytes 118b1a94
+ 005b4e8c bytes 018c1a94
- 005b4e78 ["INT_ADD", "register:40f0:8", ["const:5b4e78:8", "const:4:8"]]
- 005b4e78 ["CALL", null, ["callee:0043bb20:8"]]
+ 005b4eb8 ["INT_ADD", "register:40f0:8", ["const:5b4eb8:8", "const:4:8"]]
+ 005b4eb8 ["CALL", null, ["callee:0043bb20:8"]]
- 005b4e78 bytes 1a1bfa97
+ 005b4eb8 bytes 1a1bfa97
- 005b4ea4 ["INT_ADD", "register:40f0:8", ["const:5b4ea4:8", "const:4:8"]]
- 005b4ea4 ["CALL", null, ["callee:0043bb20:8"]]
+ 005b4ee4 ["INT_ADD", "register:40f0:8", ["const:5b4ee4:8", "const:4:8"]]
+ 005b4ee4 ["CALL", null, ["callee:0043bb20:8"]]
- 005b4ea4 bytes 0f1bfa97
+ 005b4ee4 bytes 0f1bfa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b211ff482443ade9e0401fd5dd111c9"></a>

### [`005b51e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b51e0.md) → [`005b5220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5220.md) FUN_005b5220

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`005b1368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1368.md) [`005b1400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1400.md) [`005b51e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b51e0.md) · 呼出先 2件 [`005b51e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b51e0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`005b13a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b13a8.md) [`005b1440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1440.md) [`005b5220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5220.md) · 呼出先 2件 [`005b5220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5220.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b51fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b51e0.md#insn-005b51fc) · [`005b5208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b51e0.md#insn-005b5208) · [`005b523c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b51e0.md#insn-005b523c)
- 新版 `005b523c`（命令位置の公開資料なし） · `005b5248`（命令位置の公開資料なし） · `005b527c`（命令位置の公開資料なし）

~~~diff
- 005b51fc ["INT_ADD", "register:40f0:8", ["const:5b51fc:8", "const:4:8"]]
- 005b51fc ["CALL", null, ["local:b0:8"]]
+ 005b523c ["INT_ADD", "register:40f0:8", ["const:5b523c:8", "const:4:8"]]
+ 005b523c ["CALL", null, ["local:b0:8"]]
- 005b51fc bytes f9ffff97
+ 005b523c bytes f9ffff97
- 005b5208 ["INT_ADD", "register:40f0:8", ["const:5b5208:8", "const:4:8"]]
- 005b5208 ["CALL", null, ["local:b0:8"]]
+ 005b5248 ["INT_ADD", "register:40f0:8", ["const:5b5248:8", "const:4:8"]]
+ 005b5248 ["CALL", null, ["local:b0:8"]]
- 005b5208 bytes f6ffff97
+ 005b5248 bytes f6ffff97
- 005b523c ["COPY", "register:0:8", ["register:4040:8"]]
- 005b523c ["INT_ADD", "register:40f0:8", ["const:5b523c:8", "const:4:8"]]
- 005b523c ["CALLIND", null, ["register:0:8"]]
+ 005b527c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b527c ["INT_ADD", "register:40f0:8", ["const:5b527c:8", "const:4:8"]]
+ 005b527c ["CALLIND", null, ["register:0:8"]]
- 005b523c bytes 00013fd6
+ 005b527c bytes 00013fd6
~~~


<a id="compare-a417da677c3c4577d44568f0ce64724f"></a>

### [`005b5250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5250.md) → [`005b5290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5290.md) FUN_005b5290

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`005b1368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1368.md) [`005b1400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1400.md) [`005b5250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5250.md) · 呼出先 2件 [`005b5250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5250.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`005b13a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b13a8.md) [`005b1440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1440.md) [`005b5290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5290.md) · 呼出先 2件 [`005b5290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5290.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b526c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5250.md#insn-005b526c) · [`005b5278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5250.md#insn-005b5278) · [`005b52ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5250.md#insn-005b52ac)
- 新版 `005b52ac`（命令位置の公開資料なし） · `005b52b8`（命令位置の公開資料なし） · `005b52ec`（命令位置の公開資料なし）

~~~diff
- 005b526c ["INT_ADD", "register:40f0:8", ["const:5b526c:8", "const:4:8"]]
- 005b526c ["CALL", null, ["local:b0:8"]]
+ 005b52ac ["INT_ADD", "register:40f0:8", ["const:5b52ac:8", "const:4:8"]]
+ 005b52ac ["CALL", null, ["local:b0:8"]]
- 005b526c bytes f9ffff97
+ 005b52ac bytes f9ffff97
- 005b5278 ["INT_ADD", "register:40f0:8", ["const:5b5278:8", "const:4:8"]]
- 005b5278 ["CALL", null, ["local:b0:8"]]
+ 005b52b8 ["INT_ADD", "register:40f0:8", ["const:5b52b8:8", "const:4:8"]]
+ 005b52b8 ["CALL", null, ["local:b0:8"]]
- 005b5278 bytes f6ffff97
+ 005b52b8 bytes f6ffff97
- 005b52ac ["COPY", "register:0:8", ["register:4040:8"]]
- 005b52ac ["INT_ADD", "register:40f0:8", ["const:5b52ac:8", "const:4:8"]]
- 005b52ac ["CALLIND", null, ["register:0:8"]]
+ 005b52ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b52ec ["INT_ADD", "register:40f0:8", ["const:5b52ec:8", "const:4:8"]]
+ 005b52ec ["CALLIND", null, ["register:0:8"]]
- 005b52ac bytes 00013fd6
+ 005b52ec bytes 00013fd6
~~~


<a id="compare-e96558bf8199a9ef0b977611ee9f44e0"></a>

### [`005b5524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5524.md) → [`005b5564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5564.md) FUN_005b5564

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005b1890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1890.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005b18d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b18d0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b5544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5524.md#insn-005b5544)
- 新版 `005b5584`（命令位置の公開資料なし）

~~~diff
- 005b5544 ["INT_ADD", "register:40f0:8", ["const:5b5544:8", "const:4:8"]]
- 005b5544 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b5584 ["INT_ADD", "register:40f0:8", ["const:5b5584:8", "const:4:8"]]
+ 005b5584 ["CALL", null, ["callee:00c57eb0:8"]]
- 005b5544 bytes 5b891a94
+ 005b5584 bytes 4b8a1a94
~~~


<a id="compare-3e9faa0f69d62885af37d6ce8f0b5753"></a>

### [`005b59a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b59a4.md) → [`005b59e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b59e4.md) FUN_005b59e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b59c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b59a4.md#insn-005b59c0) · [`005b59e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b59a4.md#insn-005b59e0)
- 新版 `005b5a00`（命令位置の公開資料なし） · `005b5a20`（命令位置の公開資料なし）

~~~diff
- 005b59c0 ["INT_ADD", "register:40f0:8", ["const:5b59c0:8", "const:4:8"]]
- 005b59c0 ["CALL", null, ["callee:00c53d00:8"]]
+ 005b5a00 ["INT_ADD", "register:40f0:8", ["const:5b5a00:8", "const:4:8"]]
+ 005b5a00 ["CALL", null, ["callee:00c53d00:8"]]
- 005b59c0 bytes c8771a94
+ 005b5a00 bytes c0781a94
- 005b59e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b59e0 ["INT_ADD", "register:40f0:8", ["const:5b59e0:8", "const:4:8"]]
- 005b59e0 ["CALLIND", null, ["register:0:8"]]
+ 005b5a20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b5a20 ["INT_ADD", "register:40f0:8", ["const:5b5a20:8", "const:4:8"]]
+ 005b5a20 ["CALLIND", null, ["register:0:8"]]
- 005b59e0 bytes 00013fd6
+ 005b5a20 bytes 00013fd6
~~~


<a id="compare-c02dcb9e5585dcae1eec210d67ad3b04"></a>

### [`005b5ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5ca0.md) → [`005b5ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ce0.md) FUN_005b5ce0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b5d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5ca0.md#insn-005b5d10) · [`005b5d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5ca0.md#insn-005b5d44) · [`005b5d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5ca0.md#insn-005b5d48)
- 新版 `005b5d50`（命令位置の公開資料なし） · `005b5d84`（命令位置の公開資料なし） · `005b5d88`（命令位置の公開資料なし）

~~~diff
- 005b5d10 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b5d10 ["INT_ADD", "register:40f0:8", ["const:5b5d10:8", "const:4:8"]]
- 005b5d10 ["CALLIND", null, ["register:0:8"]]
+ 005b5d50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b5d50 ["INT_ADD", "register:40f0:8", ["const:5b5d50:8", "const:4:8"]]
+ 005b5d50 ["CALLIND", null, ["register:0:8"]]
- 005b5d10 bytes 00013fd6
+ 005b5d50 bytes 00013fd6
- 005b5d44 ["INT_ADD", "register:40f0:8", ["const:5b5d44:8", "const:4:8"]]
- 005b5d44 ["CALL", null, ["callee:00459d74:8"]]
+ 005b5d84 ["INT_ADD", "register:40f0:8", ["const:5b5d84:8", "const:4:8"]]
+ 005b5d84 ["CALL", null, ["callee:00459d74:8"]]
- 005b5d44 bytes fc8ffa97
+ 005b5d84 bytes fc8ffa97
- 005b5d48 ["INT_ADD", "register:40f0:8", ["const:5b5d48:8", "const:4:8"]]
- 005b5d48 ["CALL", null, ["callee:00c57ee0:8"]]
+ 005b5d88 ["INT_ADD", "register:40f0:8", ["const:5b5d88:8", "const:4:8"]]
+ 005b5d88 ["CALL", null, ["callee:00c57ee0:8"]]
- 005b5d48 bytes 66871a94
+ 005b5d88 bytes 56881a94
~~~


<a id="compare-e0cbb160dbe82287dc12e6df26e7ae60"></a>

### [`005b5e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5e68.md) → [`005b5ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ea8.md) FUN_005b5ea8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`005b3100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3100.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005b3140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3140.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b5ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5e68.md#insn-005b5ebc) · [`005b5ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5e68.md#insn-005b5ecc) · [`005b5edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5e68.md#insn-005b5edc)
- 新版 `005b5efc`（命令位置の公開資料なし） · `005b5f0c`（命令位置の公開資料なし） · `005b5f1c`（命令位置の公開資料なし）

~~~diff
- 005b5ebc ["INT_ADD", "register:40f0:8", ["const:5b5ebc:8", "const:4:8"]]
- 005b5ebc ["CALL", null, ["callee:0043bb20:8"]]
+ 005b5efc ["INT_ADD", "register:40f0:8", ["const:5b5efc:8", "const:4:8"]]
+ 005b5efc ["CALL", null, ["callee:0043bb20:8"]]
- 005b5ebc bytes 0917fa97
+ 005b5efc bytes 0917fa97
- 005b5ecc ["INT_ADD", "register:40f0:8", ["const:5b5ecc:8", "const:4:8"]]
- 005b5ecc ["CALL", null, ["callee:005b3140:8"]]
+ 005b5f0c ["INT_ADD", "register:40f0:8", ["const:5b5f0c:8", "const:4:8"]]
+ 005b5f0c ["CALL", null, ["callee:005b3140:8"]]
- 005b5ecc bytes 8df4ff97
+ 005b5f0c bytes 8df4ff97
- 005b5edc ["INT_ADD", "register:40f0:8", ["const:5b5edc:8", "const:4:8"]]
- 005b5edc ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b5f1c ["INT_ADD", "register:40f0:8", ["const:5b5f1c:8", "const:4:8"]]
+ 005b5f1c ["CALL", null, ["callee:00c57eb0:8"]]
- 005b5edc bytes f5861a94
+ 005b5f1c bytes e5871a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8dc70f832fb863c408a16e0824de63b"></a>

### [`005b5fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5fbc.md) → [`005b5ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ffc.md) FUN_005b5ffc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`005b3308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3308.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`005b3348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3348.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b6064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5fbc.md#insn-005b6064) · [`005b6098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5fbc.md#insn-005b6098) · [`005b609c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5fbc.md#insn-005b609c)
- 新版 `005b60a4`（命令位置の公開資料なし） · `005b60d8`（命令位置の公開資料なし） · `005b60dc`（命令位置の公開資料なし）

~~~diff
- 005b6064 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b6064 ["INT_ADD", "register:40f0:8", ["const:5b6064:8", "const:4:8"]]
- 005b6064 ["CALLIND", null, ["register:0:8"]]
+ 005b60a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b60a4 ["INT_ADD", "register:40f0:8", ["const:5b60a4:8", "const:4:8"]]
+ 005b60a4 ["CALLIND", null, ["register:0:8"]]
- 005b6064 bytes 00013fd6
+ 005b60a4 bytes 00013fd6
- 005b6098 ["INT_ADD", "register:40f0:8", ["const:5b6098:8", "const:4:8"]]
- 005b6098 ["CALL", null, ["callee:00459d74:8"]]
+ 005b60d8 ["INT_ADD", "register:40f0:8", ["const:5b60d8:8", "const:4:8"]]
+ 005b60d8 ["CALL", null, ["callee:00459d74:8"]]
- 005b6098 bytes 278ffa97
+ 005b60d8 bytes 278ffa97
- 005b609c ["INT_ADD", "register:40f0:8", ["const:5b609c:8", "const:4:8"]]
- 005b609c ["CALL", null, ["callee:00c57ee0:8"]]
+ 005b60dc ["INT_ADD", "register:40f0:8", ["const:5b60dc:8", "const:4:8"]]
+ 005b60dc ["CALL", null, ["callee:00c57ee0:8"]]
- 005b609c bytes 91861a94
+ 005b60dc bytes 81871a94
~~~


<a id="compare-0ffe60edfcba542a08833286dc53a092"></a>

### [`005b6268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6268.md) → [`005b62a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b62a8.md) FUN_005b62a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b62d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6268.md#insn-005b62d8) · [`005b630c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6268.md#insn-005b630c) · [`005b6310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6268.md#insn-005b6310)
- 新版 `005b6318`（命令位置の公開資料なし） · `005b634c`（命令位置の公開資料なし） · `005b6350`（命令位置の公開資料なし）

~~~diff
- 005b62d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b62d8 ["INT_ADD", "register:40f0:8", ["const:5b62d8:8", "const:4:8"]]
- 005b62d8 ["CALLIND", null, ["register:0:8"]]
+ 005b6318 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b6318 ["INT_ADD", "register:40f0:8", ["const:5b6318:8", "const:4:8"]]
+ 005b6318 ["CALLIND", null, ["register:0:8"]]
- 005b62d8 bytes 00013fd6
+ 005b6318 bytes 00013fd6
- 005b630c ["INT_ADD", "register:40f0:8", ["const:5b630c:8", "const:4:8"]]
- 005b630c ["CALL", null, ["callee:00459d74:8"]]
+ 005b634c ["INT_ADD", "register:40f0:8", ["const:5b634c:8", "const:4:8"]]
+ 005b634c ["CALL", null, ["callee:00459d74:8"]]
- 005b630c bytes 8a8efa97
+ 005b634c bytes 8a8efa97
- 005b6310 ["INT_ADD", "register:40f0:8", ["const:5b6310:8", "const:4:8"]]
- 005b6310 ["CALL", null, ["callee:00c57ee0:8"]]
+ 005b6350 ["INT_ADD", "register:40f0:8", ["const:5b6350:8", "const:4:8"]]
+ 005b6350 ["CALL", null, ["callee:00c57ee0:8"]]
- 005b6310 bytes f4851a94
+ 005b6350 bytes e4861a94
~~~


<a id="compare-a24c734ceea55311c48c87cec10c4957"></a>

### [`005b65bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b65bc.md) → [`005b65fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b65fc.md) FUN_005b65fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b65d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b65bc.md#insn-005b65d8) · [`005b65f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b65bc.md#insn-005b65f8)
- 新版 `005b6618`（命令位置の公開資料なし） · `005b6638`（命令位置の公開資料なし）

~~~diff
- 005b65d8 ["INT_ADD", "register:40f0:8", ["const:5b65d8:8", "const:4:8"]]
- 005b65d8 ["CALL", null, ["callee:00c53d00:8"]]
+ 005b6618 ["INT_ADD", "register:40f0:8", ["const:5b6618:8", "const:4:8"]]
+ 005b6618 ["CALL", null, ["callee:00c53d00:8"]]
- 005b65d8 bytes c2741a94
+ 005b6618 bytes ba751a94
- 005b65f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b65f8 ["INT_ADD", "register:40f0:8", ["const:5b65f8:8", "const:4:8"]]
- 005b65f8 ["CALLIND", null, ["register:0:8"]]
+ 005b6638 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b6638 ["INT_ADD", "register:40f0:8", ["const:5b6638:8", "const:4:8"]]
+ 005b6638 ["CALLIND", null, ["register:0:8"]]
- 005b65f8 bytes 00013fd6
+ 005b6638 bytes 00013fd6
~~~


<a id="compare-1b37ed5c829d733b01b41ff46c513701"></a>

### [`005b664c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b664c.md) → [`005b668c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b668c.md) FUN_005b668c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005b6428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6428.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005b6468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6468.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b6698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b664c.md#insn-005b6698)
- 新版 `005b66d8`（命令位置の公開資料なし）

~~~diff
- 005b6698 ["INT_ADD", "register:40f0:8", ["const:5b6698:8", "const:4:8"]]
- 005b6698 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b66d8 ["INT_ADD", "register:40f0:8", ["const:5b66d8:8", "const:4:8"]]
+ 005b66d8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005b6698 bytes 06851a94
+ 005b66d8 bytes f6851a94
~~~


<a id="compare-bf0e04046be4a10ccb1975dc4f1a1b99"></a>

### [`005b6d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6d1c.md) → [`005b6d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6d5c.md) FUN_005b6d5c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b6d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6d1c.md#insn-005b6d38) · [`005b6d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6d1c.md#insn-005b6d58)
- 新版 `005b6d78`（命令位置の公開資料なし） · `005b6d98`（命令位置の公開資料なし）

~~~diff
- 005b6d38 ["INT_ADD", "register:40f0:8", ["const:5b6d38:8", "const:4:8"]]
- 005b6d38 ["CALL", null, ["callee:00c53d00:8"]]
+ 005b6d78 ["INT_ADD", "register:40f0:8", ["const:5b6d78:8", "const:4:8"]]
+ 005b6d78 ["CALL", null, ["callee:00c53d00:8"]]
- 005b6d38 bytes ea721a94
+ 005b6d78 bytes e2731a94
- 005b6d58 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b6d58 ["INT_ADD", "register:40f0:8", ["const:5b6d58:8", "const:4:8"]]
- 005b6d58 ["CALLIND", null, ["register:0:8"]]
+ 005b6d98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b6d98 ["INT_ADD", "register:40f0:8", ["const:5b6d98:8", "const:4:8"]]
+ 005b6d98 ["CALLIND", null, ["register:0:8"]]
- 005b6d58 bytes 00013fd6
+ 005b6d98 bytes 00013fd6
~~~


<a id="compare-900d718918d720f17ead0b63c36312e8"></a>

### [`005b6dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6dac.md) → [`005b6dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6dec.md) FUN_005b6dec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b6af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6af8.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005b6b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6b38.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b6ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6dac.md#insn-005b6ddc) · [`005b6dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6dac.md#insn-005b6dec) · [`005b6e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6dac.md#insn-005b6e00)
- 新版 `005b6e1c`（命令位置の公開資料なし） · `005b6e2c`（命令位置の公開資料なし） · `005b6e40`（命令位置の公開資料なし）

~~~diff
- 005b6ddc ["INT_ADD", "register:40f0:8", ["const:5b6ddc:8", "const:4:8"]]
- 005b6ddc ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b6e1c ["INT_ADD", "register:40f0:8", ["const:5b6e1c:8", "const:4:8"]]
+ 005b6e1c ["CALL", null, ["callee:00c57eb0:8"]]
- 005b6ddc bytes 35831a94
+ 005b6e1c bytes 25841a94
- 005b6dec ["INT_ADD", "register:40f0:8", ["const:5b6dec:8", "const:4:8"]]
- 005b6dec ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b6e2c ["INT_ADD", "register:40f0:8", ["const:5b6e2c:8", "const:4:8"]]
+ 005b6e2c ["CALL", null, ["callee:00c57eb0:8"]]
- 005b6dec bytes 31831a94
+ 005b6e2c bytes 21841a94
- 005b6e00 ["INT_ADD", "register:40f0:8", ["const:5b6e00:8", "const:4:8"]]
- 005b6e00 ["CALL", null, ["callee:00c53d00:8"]]
+ 005b6e40 ["INT_ADD", "register:40f0:8", ["const:5b6e40:8", "const:4:8"]]
+ 005b6e40 ["CALL", null, ["callee:00c53d00:8"]]
- 005b6e00 bytes b8721a94
+ 005b6e40 bytes b0731a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e65197adba18767fc484e6a4f403a84"></a>

### [`005b6fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6fd8.md) → [`005b7018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7018.md) FUN_005b7018

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b7048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6fd8.md#insn-005b7048) · [`005b707c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6fd8.md#insn-005b707c) · [`005b7080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6fd8.md#insn-005b7080)
- 新版 `005b7088`（命令位置の公開資料なし） · `005b70bc`（命令位置の公開資料なし） · `005b70c0`（命令位置の公開資料なし）

~~~diff
- 005b7048 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b7048 ["INT_ADD", "register:40f0:8", ["const:5b7048:8", "const:4:8"]]
- 005b7048 ["CALLIND", null, ["register:0:8"]]
+ 005b7088 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b7088 ["INT_ADD", "register:40f0:8", ["const:5b7088:8", "const:4:8"]]
+ 005b7088 ["CALLIND", null, ["register:0:8"]]
- 005b7048 bytes 00013fd6
+ 005b7088 bytes 00013fd6
- 005b707c ["INT_ADD", "register:40f0:8", ["const:5b707c:8", "const:4:8"]]
- 005b707c ["CALL", null, ["callee:00459d74:8"]]
+ 005b70bc ["INT_ADD", "register:40f0:8", ["const:5b70bc:8", "const:4:8"]]
+ 005b70bc ["CALL", null, ["callee:00459d74:8"]]
- 005b707c bytes 2e8bfa97
+ 005b70bc bytes 2e8bfa97
- 005b7080 ["INT_ADD", "register:40f0:8", ["const:5b7080:8", "const:4:8"]]
- 005b7080 ["CALL", null, ["callee:00c57ee0:8"]]
+ 005b70c0 ["INT_ADD", "register:40f0:8", ["const:5b70c0:8", "const:4:8"]]
+ 005b70c0 ["CALL", null, ["callee:00c57ee0:8"]]
- 005b7080 bytes 98821a94
+ 005b70c0 bytes 88831a94
~~~


