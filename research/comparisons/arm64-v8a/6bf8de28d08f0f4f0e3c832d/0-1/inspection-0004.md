# v16.0.0 → v16.0.1 · 要調査の変更候補 (4)

[一覧の目次](README.md)

<a id="compare-de267790f6039215ddf5bf2b05405f07"></a>

### [`00480198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480198.md) → [`004801d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004801d8.md) FUN_004801d8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 19件 [`0066b92c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b92c.md) [`006a48bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a4/006a48bc.md) [`006dc708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc708.md) [`0073876c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/0073876c.md) [`00744f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/00744f4c.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 19件 [`0066b96c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b96c.md) [`006a48fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a4/006a48fc.md) [`006dc748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006dc/006dc748.md) [`007387ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/007387ac.md) [`00744f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/00744f8c.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004801c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480198.md#insn-004801c4) · [`004801f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480198.md#insn-004801f4)
- 新版 [`00480204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004801d8.md#insn-00480204) · [`00480234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004801d8.md#insn-00480234)

~~~diff
- 004801c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004801c4 ["INT_ADD", "register:40f0:8", ["const:4801c4:8", "const:4:8"]]
- 004801c4 ["CALLIND", null, ["register:0:8"]]
+ 00480204 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480204 ["INT_ADD", "register:40f0:8", ["const:480204:8", "const:4:8"]]
+ 00480204 ["CALLIND", null, ["register:0:8"]]
- 004801c4 bytes 00013fd6
+ 00480204 bytes 00013fd6
- 004801f4 ["INT_ADD", "register:40f0:8", ["const:4801f4:8", "const:4:8"]]
- 004801f4 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00480234 ["INT_ADD", "register:40f0:8", ["const:480234:8", "const:4:8"]]
+ 00480234 ["CALL", null, ["callee:00c57ee0:8"]]
- 004801f4 bytes 3b5e1f94
+ 00480234 bytes 2b5f1f94
~~~


<a id="compare-4b6297c18539797b157d87c26014d021"></a>

### [`004801f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004801f8.md) → [`00480238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480238.md) FUN_00480238

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004801f8.md#insn-00480224) · [`00480254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004801f8.md#insn-00480254)
- 新版 [`00480264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480238.md#insn-00480264) · [`00480294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480238.md#insn-00480294)

~~~diff
- 00480224 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480224 ["INT_ADD", "register:40f0:8", ["const:480224:8", "const:4:8"]]
- 00480224 ["CALLIND", null, ["register:0:8"]]
+ 00480264 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480264 ["INT_ADD", "register:40f0:8", ["const:480264:8", "const:4:8"]]
+ 00480264 ["CALLIND", null, ["register:0:8"]]
- 00480224 bytes 00013fd6
+ 00480264 bytes 00013fd6
- 00480254 ["INT_ADD", "register:40f0:8", ["const:480254:8", "const:4:8"]]
- 00480254 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00480294 ["INT_ADD", "register:40f0:8", ["const:480294:8", "const:4:8"]]
+ 00480294 ["CALL", null, ["callee:00c57ee0:8"]]
- 00480254 bytes 235e1f94
+ 00480294 bytes 135f1f94
~~~


<a id="compare-09dc1a396b58012a6e047c3c0c5a5915"></a>

### [`00480258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480258.md) → [`00480298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480298.md) FUN_00480298

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480258.md#insn-00480284) · [`004802b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480258.md#insn-004802b4)
- 新版 [`004802c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480298.md#insn-004802c4) · [`004802f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480298.md#insn-004802f4)

~~~diff
- 00480284 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480284 ["INT_ADD", "register:40f0:8", ["const:480284:8", "const:4:8"]]
- 00480284 ["CALLIND", null, ["register:0:8"]]
+ 004802c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004802c4 ["INT_ADD", "register:40f0:8", ["const:4802c4:8", "const:4:8"]]
+ 004802c4 ["CALLIND", null, ["register:0:8"]]
- 00480284 bytes 00013fd6
+ 004802c4 bytes 00013fd6
- 004802b4 ["INT_ADD", "register:40f0:8", ["const:4802b4:8", "const:4:8"]]
- 004802b4 ["CALL", null, ["callee:00c57ee0:8"]]
+ 004802f4 ["INT_ADD", "register:40f0:8", ["const:4802f4:8", "const:4:8"]]
+ 004802f4 ["CALL", null, ["callee:00c57ee0:8"]]
- 004802b4 bytes 0b5e1f94
+ 004802f4 bytes fb5e1f94
~~~


<a id="compare-e26e075480552366178cd3ec86d23d64"></a>

### [`004802b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md) → [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md) FUN_004802f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 32件 [`005b9a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9a10.md) [`0066b324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b324.md) [`006db02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006db02c.md) [`0072ece8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ece8.md) [`00732904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732904.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 32件 [`005b9a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9a50.md) [`0066b364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b364.md) [`006db06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006db/006db06c.md) [`0072ed28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072e/0072ed28.md) [`00732944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732944.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004802e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md#insn-004802e4) · [`00480318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md#insn-00480318)
- 新版 [`00480324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md#insn-00480324) · [`00480358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md#insn-00480358)

~~~diff
- 004802e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004802e4 ["INT_ADD", "register:40f0:8", ["const:4802e4:8", "const:4:8"]]
- 004802e4 ["CALLIND", null, ["register:0:8"]]
+ 00480324 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480324 ["INT_ADD", "register:40f0:8", ["const:480324:8", "const:4:8"]]
+ 00480324 ["CALLIND", null, ["register:0:8"]]
- 004802e4 bytes 00013fd6
+ 00480324 bytes 00013fd6
- 00480318 ["INT_ADD", "register:40f0:8", ["const:480318:8", "const:4:8"]]
- 00480318 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00480358 ["INT_ADD", "register:40f0:8", ["const:480358:8", "const:4:8"]]
+ 00480358 ["CALL", null, ["callee:00c57ee0:8"]]
- 00480318 bytes f25d1f94
+ 00480358 bytes e25e1f94
~~~


<a id="compare-1ebc38bdf2dc80a0f17b92439c974ebe"></a>

### [`0048031c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/0048031c.md) → [`0048035c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/0048035c.md) FUN_0048035c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 3件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f4dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f4dc.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 3件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f51c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f51c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/0048031c.md#insn-00480350) · [`00480364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/0048031c.md#insn-00480364) · [`00480384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/0048031c.md#insn-00480384)
- 新版 [`00480390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/0048035c.md#insn-00480390) · [`004803a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/0048035c.md#insn-004803a4) · [`004803c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/0048035c.md#insn-004803c4)

~~~diff
- 00480350 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480350 ["INT_ADD", "register:40f0:8", ["const:480350:8", "const:4:8"]]
- 00480350 ["CALLIND", null, ["register:0:8"]]
+ 00480390 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480390 ["INT_ADD", "register:40f0:8", ["const:480390:8", "const:4:8"]]
+ 00480390 ["CALLIND", null, ["register:0:8"]]
- 00480350 bytes 00013fd6
+ 00480390 bytes 00013fd6
- 00480364 ["INT_ADD", "register:40f0:8", ["const:480364:8", "const:4:8"]]
- 00480364 ["CALL", null, ["callee:0055f4c4:8"]]
+ 004803a4 ["INT_ADD", "register:40f0:8", ["const:4803a4:8", "const:4:8"]]
+ 004803a4 ["CALL", null, ["callee:0055f4c4:8"]]
- 00480364 bytes 487c0394
+ 004803a4 bytes 487c0394
- 00480384 ["INT_ADD", "register:40f0:8", ["const:480384:8", "const:4:8"]]
- 00480384 ["CALL", null, ["callee:0055f51c:8"]]
+ 004803c4 ["INT_ADD", "register:40f0:8", ["const:4803c4:8", "const:4:8"]]
+ 004803c4 ["CALL", null, ["callee:0055f51c:8"]]
- 00480384 bytes 567c0394
+ 004803c4 bytes 567c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfc67bbe0b0cb881574f21d8c53faeb1"></a>

### [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md) → [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md) FUN_004803f0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 36件 [`005b9a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9a10.md) [`005e0034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0034.md) [`005e0078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0078.md) [`005e0124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0124.md) [`005e01bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e01bc.md) · 呼出先 3件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f4f8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 36件 [`005b9a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9a50.md) [`005e0074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0074.md) [`005e00b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e00b8.md) [`005e0164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0164.md) [`005e01fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e01fc.md) · 呼出先 3件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f538.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004803e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md#insn-004803e4) · [`004803f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md#insn-004803f8) · [`00480418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md#insn-00480418)
- 新版 [`00480424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md#insn-00480424) · [`00480438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md#insn-00480438) · [`00480458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md#insn-00480458)

~~~diff
- 004803e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004803e4 ["INT_ADD", "register:40f0:8", ["const:4803e4:8", "const:4:8"]]
- 004803e4 ["CALLIND", null, ["register:0:8"]]
+ 00480424 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480424 ["INT_ADD", "register:40f0:8", ["const:480424:8", "const:4:8"]]
+ 00480424 ["CALLIND", null, ["register:0:8"]]
- 004803e4 bytes 00013fd6
+ 00480424 bytes 00013fd6
- 004803f8 ["INT_ADD", "register:40f0:8", ["const:4803f8:8", "const:4:8"]]
- 004803f8 ["CALL", null, ["callee:0055f4c4:8"]]
+ 00480438 ["INT_ADD", "register:40f0:8", ["const:480438:8", "const:4:8"]]
+ 00480438 ["CALL", null, ["callee:0055f4c4:8"]]
- 004803f8 bytes 237c0394
+ 00480438 bytes 237c0394
- 00480418 ["INT_ADD", "register:40f0:8", ["const:480418:8", "const:4:8"]]
- 00480418 ["CALL", null, ["callee:0055f538:8"]]
+ 00480458 ["INT_ADD", "register:40f0:8", ["const:480458:8", "const:4:8"]]
+ 00480458 ["CALL", null, ["callee:0055f538:8"]]
- 00480418 bytes 387c0394
+ 00480458 bytes 387c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7225b38b872f25b42ca88c59e60b288"></a>

### [`00480444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480444.md) → [`00480484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480484.md) FUN_00480484

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 3件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f4f8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 3件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f538.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480444.md#insn-00480478) · [`0048048c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480444.md#insn-0048048c) · [`004804ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480444.md#insn-004804ac)
- 新版 [`004804b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480484.md#insn-004804b8) · [`004804cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480484.md#insn-004804cc) · [`004804ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480484.md#insn-004804ec)

~~~diff
- 00480478 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480478 ["INT_ADD", "register:40f0:8", ["const:480478:8", "const:4:8"]]
- 00480478 ["CALLIND", null, ["register:0:8"]]
+ 004804b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004804b8 ["INT_ADD", "register:40f0:8", ["const:4804b8:8", "const:4:8"]]
+ 004804b8 ["CALLIND", null, ["register:0:8"]]
- 00480478 bytes 00013fd6
+ 004804b8 bytes 00013fd6
- 0048048c ["INT_ADD", "register:40f0:8", ["const:48048c:8", "const:4:8"]]
- 0048048c ["CALL", null, ["callee:0055f4c4:8"]]
+ 004804cc ["INT_ADD", "register:40f0:8", ["const:4804cc:8", "const:4:8"]]
+ 004804cc ["CALL", null, ["callee:0055f4c4:8"]]
- 0048048c bytes fe7b0394
+ 004804cc bytes fe7b0394
- 004804ac ["INT_ADD", "register:40f0:8", ["const:4804ac:8", "const:4:8"]]
- 004804ac ["CALL", null, ["callee:0055f538:8"]]
+ 004804ec ["INT_ADD", "register:40f0:8", ["const:4804ec:8", "const:4:8"]]
+ 004804ec ["CALL", null, ["callee:0055f538:8"]]
- 004804ac bytes 137c0394
+ 004804ec bytes 137c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9c8406053d6498aae56381a67a6ace5"></a>

### [`004804d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004804d8.md) → [`00480518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480518.md) FUN_00480518

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008395ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/008395ac.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`008395ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00839/008395ec.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048050c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004804d8.md#insn-0048050c) · [`0048053c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004804d8.md#insn-0048053c) · [`00480570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004804d8.md#insn-00480570)
- 新版 [`0048054c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480518.md#insn-0048054c) · [`0048057c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480518.md#insn-0048057c) · [`004805b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480518.md#insn-004805b0)

~~~diff
- 0048050c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048050c ["INT_ADD", "register:40f0:8", ["const:48050c:8", "const:4:8"]]
- 0048050c ["CALLIND", null, ["register:0:8"]]
+ 0048054c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048054c ["INT_ADD", "register:40f0:8", ["const:48054c:8", "const:4:8"]]
+ 0048054c ["CALLIND", null, ["register:0:8"]]
- 0048050c bytes 00013fd6
+ 0048054c bytes 00013fd6
- 0048053c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048053c ["INT_ADD", "register:40f0:8", ["const:48053c:8", "const:4:8"]]
- 0048053c ["CALLIND", null, ["register:0:8"]]
+ 0048057c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048057c ["INT_ADD", "register:40f0:8", ["const:48057c:8", "const:4:8"]]
+ 0048057c ["CALLIND", null, ["register:0:8"]]
- 0048053c bytes 00013fd6
+ 0048057c bytes 00013fd6
- 00480570 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480570 ["INT_ADD", "register:40f0:8", ["const:480570:8", "const:4:8"]]
- 00480570 ["CALLIND", null, ["register:0:8"]]
+ 004805b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004805b0 ["INT_ADD", "register:40f0:8", ["const:4805b0:8", "const:4:8"]]
+ 004805b0 ["CALLIND", null, ["register:0:8"]]
- 00480570 bytes 00013fd6
+ 004805b0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d78f687fc9c2fdb90bee2fff9dcf6b98"></a>

### [`004805e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004805e8.md) → [`00480628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480628.md) FUN_00480628

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 3件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f518.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 3件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f558.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048061c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004805e8.md#insn-0048061c) · [`00480630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004805e8.md#insn-00480630) · [`00480650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004805e8.md#insn-00480650)
- 新版 [`0048065c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480628.md#insn-0048065c) · [`00480670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480628.md#insn-00480670) · [`00480690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480628.md#insn-00480690)

~~~diff
- 0048061c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048061c ["INT_ADD", "register:40f0:8", ["const:48061c:8", "const:4:8"]]
- 0048061c ["CALLIND", null, ["register:0:8"]]
+ 0048065c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048065c ["INT_ADD", "register:40f0:8", ["const:48065c:8", "const:4:8"]]
+ 0048065c ["CALLIND", null, ["register:0:8"]]
- 0048061c bytes 00013fd6
+ 0048065c bytes 00013fd6
- 00480630 ["INT_ADD", "register:40f0:8", ["const:480630:8", "const:4:8"]]
- 00480630 ["CALL", null, ["callee:0055f4c4:8"]]
+ 00480670 ["INT_ADD", "register:40f0:8", ["const:480670:8", "const:4:8"]]
+ 00480670 ["CALL", null, ["callee:0055f4c4:8"]]
- 00480630 bytes 957b0394
+ 00480670 bytes 957b0394
- 00480650 ["INT_ADD", "register:40f0:8", ["const:480650:8", "const:4:8"]]
- 00480650 ["CALL", null, ["callee:0055f558:8"]]
+ 00480690 ["INT_ADD", "register:40f0:8", ["const:480690:8", "const:4:8"]]
+ 00480690 ["CALL", null, ["callee:0055f558:8"]]
- 00480650 bytes b27b0394
+ 00480690 bytes b27b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-849706b8309da1cab4b8e61318b718dc"></a>

### [`0048067c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/0048067c.md) → [`004806bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004806bc.md) FUN_004806bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) · 呼出先 3件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f508.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00a1a750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a750.md) · 呼出先 3件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f548.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004806b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/0048067c.md#insn-004806b0) · [`004806c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/0048067c.md#insn-004806c8) · [`004806d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/0048067c.md#insn-004806d8)
- 新版 [`004806f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004806bc.md#insn-004806f0) · [`00480708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004806bc.md#insn-00480708) · [`00480718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004806bc.md#insn-00480718)

~~~diff
- 004806b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004806b0 ["INT_ADD", "register:40f0:8", ["const:4806b0:8", "const:4:8"]]
- 004806b0 ["CALLIND", null, ["register:0:8"]]
+ 004806f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004806f0 ["INT_ADD", "register:40f0:8", ["const:4806f0:8", "const:4:8"]]
+ 004806f0 ["CALLIND", null, ["register:0:8"]]
- 004806b0 bytes 00013fd6
+ 004806f0 bytes 00013fd6
- 004806c8 ["INT_ADD", "register:40f0:8", ["const:4806c8:8", "const:4:8"]]
- 004806c8 ["CALL", null, ["callee:0055f4c4:8"]]
+ 00480708 ["INT_ADD", "register:40f0:8", ["const:480708:8", "const:4:8"]]
+ 00480708 ["CALL", null, ["callee:0055f4c4:8"]]
- 004806c8 bytes 6f7b0394
+ 00480708 bytes 6f7b0394
- 004806d8 ["INT_ADD", "register:40f0:8", ["const:4806d8:8", "const:4:8"]]
- 004806d8 ["CALL", null, ["callee:0055f548:8"]]
+ 00480718 ["INT_ADD", "register:40f0:8", ["const:480718:8", "const:4:8"]]
+ 00480718 ["CALL", null, ["callee:0055f548:8"]]
- 004806d8 bytes 8c7b0394
+ 00480718 bytes 8c7b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc0dc2c4e4b341f0b33116ecefeb71a8"></a>

### [`00480704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md) → [`00480744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md) FUN_00480744

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 27件 [`005b9a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9a10.md) [`00675b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00675/00675b54.md) [`006db02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006db02c.md) [`0072ece8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ece8.md) [`00732904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732904.md) · 呼出先 3件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f528.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 27件 [`005b9a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9a50.md) [`00675b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00675/00675b94.md) [`006db06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006db/006db06c.md) [`0072ed28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072e/0072ed28.md) [`00732944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732944.md) · 呼出先 3件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f568.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md#insn-00480738) · [`00480750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md#insn-00480750) · [`00480760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md#insn-00480760)
- 新版 [`00480778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md#insn-00480778) · [`00480790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md#insn-00480790) · [`004807a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md#insn-004807a0)

~~~diff
- 00480738 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480738 ["INT_ADD", "register:40f0:8", ["const:480738:8", "const:4:8"]]
- 00480738 ["CALLIND", null, ["register:0:8"]]
+ 00480778 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480778 ["INT_ADD", "register:40f0:8", ["const:480778:8", "const:4:8"]]
+ 00480778 ["CALLIND", null, ["register:0:8"]]
- 00480738 bytes 00013fd6
+ 00480778 bytes 00013fd6
- 00480750 ["INT_ADD", "register:40f0:8", ["const:480750:8", "const:4:8"]]
- 00480750 ["CALL", null, ["callee:0055f4c4:8"]]
+ 00480790 ["INT_ADD", "register:40f0:8", ["const:480790:8", "const:4:8"]]
+ 00480790 ["CALL", null, ["callee:0055f4c4:8"]]
- 00480750 bytes 4d7b0394
+ 00480790 bytes 4d7b0394
- 00480760 ["INT_ADD", "register:40f0:8", ["const:480760:8", "const:4:8"]]
- 00480760 ["CALL", null, ["callee:0055f568:8"]]
+ 004807a0 ["INT_ADD", "register:40f0:8", ["const:4807a0:8", "const:4:8"]]
+ 004807a0 ["CALL", null, ["callee:0055f568:8"]]
- 00480760 bytes 727b0394
+ 004807a0 bytes 727b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c346811d32c8409e5eefbf9dc87ebd7"></a>

### [`0048078c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/0048078c.md) → [`004807cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004807cc.md) FUN_004807cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`007380a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/007380a4.md) [`0079fff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079fff4.md) [`009812a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009812a4.md) [`009a92a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a92a8.md) [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 5件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f4f8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 6件 [`007380e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/007380e4.md) [`007a0034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0034.md) [`00981440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981440.md) [`009a9444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a9444.md) [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 5件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f538.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004807c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/0048078c.md#insn-004807c8) · [`004807dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/0048078c.md#insn-004807dc) · [`004807ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/0048078c.md#insn-004807ec)
- 新版 [`00480808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004807cc.md#insn-00480808) · [`0048081c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004807cc.md#insn-0048081c) · [`0048082c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004807cc.md#insn-0048082c)

~~~diff
- 004807c8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004807c8 ["INT_ADD", "register:40f0:8", ["const:4807c8:8", "const:4:8"]]
- 004807c8 ["CALLIND", null, ["register:0:8"]]
+ 00480808 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00480808 ["INT_ADD", "register:40f0:8", ["const:480808:8", "const:4:8"]]
+ 00480808 ["CALLIND", null, ["register:0:8"]]
- 004807c8 bytes 20013fd6
+ 00480808 bytes 20013fd6
- 004807dc ["INT_ADD", "register:40f0:8", ["const:4807dc:8", "const:4:8"]]
- 004807dc ["CALL", null, ["callee:0055f4c4:8"]]
+ 0048081c ["INT_ADD", "register:40f0:8", ["const:48081c:8", "const:4:8"]]
+ 0048081c ["CALL", null, ["callee:0055f4c4:8"]]
- 004807dc bytes 2a7b0394
+ 0048081c bytes 2a7b0394
- 004807ec ["INT_ADD", "register:40f0:8", ["const:4807ec:8", "const:4:8"]]
- 004807ec ["CALL", null, ["callee:0055f538:8"]]
+ 0048082c ["INT_ADD", "register:40f0:8", ["const:48082c:8", "const:4:8"]]
+ 0048082c ["CALL", null, ["callee:0055f538:8"]]
- 004807ec bytes 437b0394
+ 0048082c bytes 437b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-495ec4d2df3c670934f7c8d16ef06987"></a>

### [`004808bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004808bc.md) → [`004808fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004808fc.md) FUN_004808fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0079fff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079fff4.md) [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 4件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f4f8.md) [`00597738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597738.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`007a0034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0034.md) [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 4件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f538.md) [`00597778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597778.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004808bc.md#insn-00480904) · [`00480918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004808bc.md#insn-00480918) · [`00480928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004808bc.md#insn-00480928)
- 新版 [`00480944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004808fc.md#insn-00480944) · [`00480958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004808fc.md#insn-00480958) · [`00480968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004808fc.md#insn-00480968)

~~~diff
- 00480904 ["COPY", "register:0:8", ["register:4048:8"]]
- 00480904 ["INT_ADD", "register:40f0:8", ["const:480904:8", "const:4:8"]]
- 00480904 ["CALLIND", null, ["register:0:8"]]
+ 00480944 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00480944 ["INT_ADD", "register:40f0:8", ["const:480944:8", "const:4:8"]]
+ 00480944 ["CALLIND", null, ["register:0:8"]]
- 00480904 bytes 20013fd6
+ 00480944 bytes 20013fd6
- 00480918 ["INT_ADD", "register:40f0:8", ["const:480918:8", "const:4:8"]]
- 00480918 ["CALL", null, ["callee:0055f4c4:8"]]
+ 00480958 ["INT_ADD", "register:40f0:8", ["const:480958:8", "const:4:8"]]
+ 00480958 ["CALL", null, ["callee:0055f4c4:8"]]
- 00480918 bytes db7a0394
+ 00480958 bytes db7a0394
- 00480928 ["INT_ADD", "register:40f0:8", ["const:480928:8", "const:4:8"]]
- 00480928 ["CALL", null, ["callee:0055f538:8"]]
+ 00480968 ["INT_ADD", "register:40f0:8", ["const:480968:8", "const:4:8"]]
+ 00480968 ["CALL", null, ["callee:0055f538:8"]]
- 00480928 bytes f47a0394
+ 00480968 bytes f47a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bde91b33845320eaf44e45b694f79eae"></a>

### [`00480af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480af8.md) → [`00480b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md) FUN_00480b38

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 21件 [`005c0d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0d84.md) [`0066b4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b4ac.md) [`006dafdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006dafdc.md) [`00738590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738590.md) [`007453f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00745/007453f4.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 21件 [`005c0dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c0dc4.md) [`0066b4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b4ec.md) [`006db01c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006db/006db01c.md) [`007385d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/007385d0.md) [`00745434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/00745434.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480af8.md#insn-00480b28) · [`00480b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480af8.md#insn-00480b4c)
- 新版 [`00480b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md#insn-00480b68) · [`00480b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md#insn-00480b8c)

~~~diff
- 00480b28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480b28 ["INT_ADD", "register:40f0:8", ["const:480b28:8", "const:4:8"]]
- 00480b28 ["CALLIND", null, ["register:0:8"]]
+ 00480b68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480b68 ["INT_ADD", "register:40f0:8", ["const:480b68:8", "const:4:8"]]
+ 00480b68 ["CALLIND", null, ["register:0:8"]]
- 00480b28 bytes 00013fd6
+ 00480b68 bytes 00013fd6
- 00480b4c ["INT_ADD", "register:40f0:8", ["const:480b4c:8", "const:4:8"]]
- 00480b4c ["CALL", null, ["callee:00c57ee0:8"]]
+ 00480b8c ["INT_ADD", "register:40f0:8", ["const:480b8c:8", "const:4:8"]]
+ 00480b8c ["CALL", null, ["callee:00c57ee0:8"]]
- 00480b4c bytes e55b1f94
+ 00480b8c bytes d55c1f94
~~~


<a id="compare-8f951f7885ac5d50548e9e74da77f794"></a>

### [`00480b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480b50.md) → [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md) FUN_00480b90

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 26件 [`005c0d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0d84.md) [`00675e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00675/00675e90.md) [`006a4d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a4/006a4d30.md) [`006dafdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006dafdc.md) [`00738590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738590.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 26件 [`005c0dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c0dc4.md) [`00675ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00675/00675ed0.md) [`006a4d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a4/006a4d70.md) [`006db01c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006db/006db01c.md) [`007385d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/007385d0.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480b50.md#insn-00480b80) · [`00480ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480b50.md#insn-00480ba4)
- 新版 [`00480bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md#insn-00480bc0) · [`00480be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md#insn-00480be4)

~~~diff
- 00480b80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480b80 ["INT_ADD", "register:40f0:8", ["const:480b80:8", "const:4:8"]]
- 00480b80 ["CALLIND", null, ["register:0:8"]]
+ 00480bc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480bc0 ["INT_ADD", "register:40f0:8", ["const:480bc0:8", "const:4:8"]]
+ 00480bc0 ["CALLIND", null, ["register:0:8"]]
- 00480b80 bytes 00013fd6
+ 00480bc0 bytes 00013fd6
- 00480ba4 ["INT_ADD", "register:40f0:8", ["const:480ba4:8", "const:4:8"]]
- 00480ba4 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00480be4 ["INT_ADD", "register:40f0:8", ["const:480be4:8", "const:4:8"]]
+ 00480be4 ["CALL", null, ["callee:00c57ee0:8"]]
- 00480ba4 bytes cf5b1f94
+ 00480be4 bytes bf5c1f94
~~~


<a id="compare-f2b5adeb232824e15d40f2ce1b249f5d"></a>

### [`00480ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ba8.md) → [`00480be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md) FUN_00480be8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 23件 [`0066b4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b4ac.md) [`0066b964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b964.md) [`006a4d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a4/006a4d30.md) [`006dc66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc66c.md) [`00738590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738590.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 23件 [`0066b4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b4ec.md) [`0066b9a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b9a4.md) [`006a4d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a4/006a4d70.md) [`006dc6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006dc/006dc6ac.md) [`007385d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/007385d0.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ba8.md#insn-00480bd8) · [`00480bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ba8.md#insn-00480bfc)
- 新版 [`00480c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md#insn-00480c18) · [`00480c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md#insn-00480c3c)

~~~diff
- 00480bd8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480bd8 ["INT_ADD", "register:40f0:8", ["const:480bd8:8", "const:4:8"]]
- 00480bd8 ["CALLIND", null, ["register:0:8"]]
+ 00480c18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480c18 ["INT_ADD", "register:40f0:8", ["const:480c18:8", "const:4:8"]]
+ 00480c18 ["CALLIND", null, ["register:0:8"]]
- 00480bd8 bytes 00013fd6
+ 00480c18 bytes 00013fd6
- 00480bfc ["INT_ADD", "register:40f0:8", ["const:480bfc:8", "const:4:8"]]
- 00480bfc ["CALL", null, ["callee:00c57ee0:8"]]
+ 00480c3c ["INT_ADD", "register:40f0:8", ["const:480c3c:8", "const:4:8"]]
+ 00480c3c ["CALL", null, ["callee:00c57ee0:8"]]
- 00480bfc bytes b95b1f94
+ 00480c3c bytes a95c1f94
~~~


<a id="compare-87679667fa62177d1ad4e73f48a5edea"></a>

### [`00480c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480c00.md) → [`00480c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480c40.md) FUN_00480c40

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480c00.md#insn-00480c30) · [`00480c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480c00.md#insn-00480c54)
- 新版 [`00480c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480c40.md#insn-00480c70) · [`00480c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480c40.md#insn-00480c94)

~~~diff
- 00480c30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480c30 ["INT_ADD", "register:40f0:8", ["const:480c30:8", "const:4:8"]]
- 00480c30 ["CALLIND", null, ["register:0:8"]]
+ 00480c70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480c70 ["INT_ADD", "register:40f0:8", ["const:480c70:8", "const:4:8"]]
+ 00480c70 ["CALLIND", null, ["register:0:8"]]
- 00480c30 bytes 00013fd6
+ 00480c70 bytes 00013fd6
- 00480c54 ["INT_ADD", "register:40f0:8", ["const:480c54:8", "const:4:8"]]
- 00480c54 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00480c94 ["INT_ADD", "register:40f0:8", ["const:480c94:8", "const:4:8"]]
+ 00480c94 ["CALL", null, ["callee:00c57ee0:8"]]
- 00480c54 bytes a35b1f94
+ 00480c94 bytes 935c1f94
~~~


<a id="compare-43b5e4d2306b29bbf47652b7e590e4b3"></a>

### [`00480c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480c58.md) → [`00480c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480c98.md) FUN_00480c98

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480c58.md#insn-00480c88) · [`00480cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480c58.md#insn-00480cac)
- 新版 [`00480cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480c98.md#insn-00480cc8) · [`00480cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480c98.md#insn-00480cec)

~~~diff
- 00480c88 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480c88 ["INT_ADD", "register:40f0:8", ["const:480c88:8", "const:4:8"]]
- 00480c88 ["CALLIND", null, ["register:0:8"]]
+ 00480cc8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480cc8 ["INT_ADD", "register:40f0:8", ["const:480cc8:8", "const:4:8"]]
+ 00480cc8 ["CALLIND", null, ["register:0:8"]]
- 00480c88 bytes 00013fd6
+ 00480cc8 bytes 00013fd6
- 00480cac ["INT_ADD", "register:40f0:8", ["const:480cac:8", "const:4:8"]]
- 00480cac ["CALL", null, ["callee:00c57ee0:8"]]
+ 00480cec ["INT_ADD", "register:40f0:8", ["const:480cec:8", "const:4:8"]]
+ 00480cec ["CALL", null, ["callee:00c57ee0:8"]]
- 00480cac bytes 8d5b1f94
+ 00480cec bytes 7d5c1f94
~~~


<a id="compare-d0fd2d5e857d150bd2b04726b41b5f40"></a>

### [`00480cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480cb0.md) → [`00480cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480cf0.md) FUN_00480cf0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`0072ef2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ef2c.md) [`00732abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732abc.md) [`00738590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738590.md) [`00a14bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a14bf0.md) [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 5件 [`0072ef6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072e/0072ef6c.md) [`00732afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732afc.md) [`007385d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/007385d0.md) [`00a14d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14d8c.md) [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480cb0.md#insn-00480ce0) · [`00480d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480cb0.md#insn-00480d04)
- 新版 [`00480d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480cf0.md#insn-00480d20) · [`00480d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480cf0.md#insn-00480d44)

~~~diff
- 00480ce0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480ce0 ["INT_ADD", "register:40f0:8", ["const:480ce0:8", "const:4:8"]]
- 00480ce0 ["CALLIND", null, ["register:0:8"]]
+ 00480d20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480d20 ["INT_ADD", "register:40f0:8", ["const:480d20:8", "const:4:8"]]
+ 00480d20 ["CALLIND", null, ["register:0:8"]]
- 00480ce0 bytes 00013fd6
+ 00480d20 bytes 00013fd6
- 00480d04 ["INT_ADD", "register:40f0:8", ["const:480d04:8", "const:4:8"]]
- 00480d04 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00480d44 ["INT_ADD", "register:40f0:8", ["const:480d44:8", "const:4:8"]]
+ 00480d44 ["CALL", null, ["callee:00c57ee0:8"]]
- 00480d04 bytes 775b1f94
+ 00480d44 bytes 675c1f94
~~~


<a id="compare-1496b8499d651f2f489765503453fc79"></a>

### [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md) → [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) FUN_00480d48

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 32件 [`005b99cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b99cc.md) [`0066b4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b4ac.md) [`006dafdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006dafdc.md) [`0072ef2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ef2c.md) [`00732abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732abc.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 32件 [`005b9a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9a0c.md) [`0066b4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b4ec.md) [`006db01c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006db/006db01c.md) [`0072ef6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072e/0072ef6c.md) [`00732afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732afc.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md#insn-00480d38) · [`00480d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md#insn-00480d5c)
- 新版 [`00480d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md#insn-00480d78) · [`00480d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md#insn-00480d9c)

~~~diff
- 00480d38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480d38 ["INT_ADD", "register:40f0:8", ["const:480d38:8", "const:4:8"]]
- 00480d38 ["CALLIND", null, ["register:0:8"]]
+ 00480d78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480d78 ["INT_ADD", "register:40f0:8", ["const:480d78:8", "const:4:8"]]
+ 00480d78 ["CALLIND", null, ["register:0:8"]]
- 00480d38 bytes 00013fd6
+ 00480d78 bytes 00013fd6
- 00480d5c ["INT_ADD", "register:40f0:8", ["const:480d5c:8", "const:4:8"]]
- 00480d5c ["CALL", null, ["callee:00c57ee0:8"]]
+ 00480d9c ["INT_ADD", "register:40f0:8", ["const:480d9c:8", "const:4:8"]]
+ 00480d9c ["CALL", null, ["callee:00c57ee0:8"]]
- 00480d5c bytes 615b1f94
+ 00480d9c bytes 515c1f94
~~~


<a id="compare-5ffdfc0b28c454688f6bd6eb3e6deea6"></a>

### [`00480d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d60.md) → [`00480da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480da0.md) FUN_00480da0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00a14bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a14bf0.md) [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 3件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f4dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f4dc.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`00a14d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14d8c.md) [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 3件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f51c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f51c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d60.md#insn-00480d8c) · [`00480d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d60.md#insn-00480d9c) · [`00480dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d60.md#insn-00480dbc)
- 新版 [`00480dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480da0.md#insn-00480dcc) · [`00480ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480da0.md#insn-00480ddc) · [`00480dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480da0.md#insn-00480dfc)

~~~diff
- 00480d8c ["INT_ADD", "register:40f0:8", ["const:480d8c:8", "const:4:8"]]
- 00480d8c ["CALL", null, ["callee:0055f4c4:8"]]
+ 00480dcc ["INT_ADD", "register:40f0:8", ["const:480dcc:8", "const:4:8"]]
+ 00480dcc ["CALL", null, ["callee:0055f4c4:8"]]
- 00480d8c bytes be790394
+ 00480dcc bytes be790394
- 00480d9c ["INT_ADD", "register:40f0:8", ["const:480d9c:8", "const:4:8"]]
- 00480d9c ["CALL", null, ["callee:0055f51c:8"]]
+ 00480ddc ["INT_ADD", "register:40f0:8", ["const:480ddc:8", "const:4:8"]]
+ 00480ddc ["CALL", null, ["callee:0055f51c:8"]]
- 00480d9c bytes d0790394
+ 00480ddc bytes d0790394
- 00480dbc ["COPY", "register:0:8", ["register:4040:8"]]
- 00480dbc ["INT_ADD", "register:40f0:8", ["const:480dbc:8", "const:4:8"]]
- 00480dbc ["CALLIND", null, ["register:0:8"]]
+ 00480dfc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480dfc ["INT_ADD", "register:40f0:8", ["const:480dfc:8", "const:4:8"]]
+ 00480dfc ["CALLIND", null, ["register:0:8"]]
- 00480dbc bytes 00013fd6
+ 00480dfc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca9e1652f60d392f5d6de0eeca273a17"></a>

### [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md) → [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md) FUN_00480e28

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 29件 [`005b99cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b99cc.md) [`005e00c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e00c8.md) [`005e0168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0168.md) [`005e0214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0214.md) [`006dc66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc66c.md) · 呼出先 3件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f4f8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 29件 [`005b9a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9a0c.md) [`005e0108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0108.md) [`005e01a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e01a8.md) [`005e0254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0254.md) [`006dc6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006dc/006dc6ac.md) · 呼出先 3件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f538.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md#insn-00480e14) · [`00480e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md#insn-00480e24) · [`00480e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md#insn-00480e44)
- 新版 [`00480e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md#insn-00480e54) · [`00480e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md#insn-00480e64) · [`00480e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md#insn-00480e84)

~~~diff
- 00480e14 ["INT_ADD", "register:40f0:8", ["const:480e14:8", "const:4:8"]]
- 00480e14 ["CALL", null, ["callee:0055f4c4:8"]]
+ 00480e54 ["INT_ADD", "register:40f0:8", ["const:480e54:8", "const:4:8"]]
+ 00480e54 ["CALL", null, ["callee:0055f4c4:8"]]
- 00480e14 bytes 9c790394
+ 00480e54 bytes 9c790394
- 00480e24 ["INT_ADD", "register:40f0:8", ["const:480e24:8", "const:4:8"]]
- 00480e24 ["CALL", null, ["callee:0055f538:8"]]
+ 00480e64 ["INT_ADD", "register:40f0:8", ["const:480e64:8", "const:4:8"]]
+ 00480e64 ["CALL", null, ["callee:0055f538:8"]]
- 00480e24 bytes b5790394
+ 00480e64 bytes b5790394
- 00480e44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480e44 ["INT_ADD", "register:40f0:8", ["const:480e44:8", "const:4:8"]]
- 00480e44 ["CALLIND", null, ["register:0:8"]]
+ 00480e84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480e84 ["INT_ADD", "register:40f0:8", ["const:480e84:8", "const:4:8"]]
+ 00480e84 ["CALLIND", null, ["register:0:8"]]
- 00480e44 bytes 00013fd6
+ 00480e84 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1569436490efd934eba830aba7caa5b"></a>

### [`00480e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480e70.md) → [`00480eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480eb0.md) FUN_00480eb0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a14bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a14bf0.md) · 呼出先 3件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f500.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00a14d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14d8c.md) · 呼出先 3件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f540.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480e70.md#insn-00480e9c) · [`00480eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480e70.md#insn-00480eac) · [`00480ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480e70.md#insn-00480ecc)
- 新版 [`00480edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480eb0.md#insn-00480edc) · [`00480eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480eb0.md#insn-00480eec) · [`00480f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480eb0.md#insn-00480f0c)

~~~diff
- 00480e9c ["INT_ADD", "register:40f0:8", ["const:480e9c:8", "const:4:8"]]
- 00480e9c ["CALL", null, ["callee:0055f4c4:8"]]
+ 00480edc ["INT_ADD", "register:40f0:8", ["const:480edc:8", "const:4:8"]]
+ 00480edc ["CALL", null, ["callee:0055f4c4:8"]]
- 00480e9c bytes 7a790394
+ 00480edc bytes 7a790394
- 00480eac ["INT_ADD", "register:40f0:8", ["const:480eac:8", "const:4:8"]]
- 00480eac ["CALL", null, ["callee:0055f540:8"]]
+ 00480eec ["INT_ADD", "register:40f0:8", ["const:480eec:8", "const:4:8"]]
+ 00480eec ["CALL", null, ["callee:0055f540:8"]]
- 00480eac bytes 95790394
+ 00480eec bytes 95790394
- 00480ecc ["COPY", "register:0:8", ["register:4040:8"]]
- 00480ecc ["INT_ADD", "register:40f0:8", ["const:480ecc:8", "const:4:8"]]
- 00480ecc ["CALLIND", null, ["register:0:8"]]
+ 00480f0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480f0c ["INT_ADD", "register:40f0:8", ["const:480f0c:8", "const:4:8"]]
+ 00480f0c ["CALLIND", null, ["register:0:8"]]
- 00480ecc bytes 00013fd6
+ 00480f0c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-316b9461ce7f234ad21c951bce539087"></a>

### [`00480ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ef8.md) → [`00480f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480f38.md) FUN_00480f38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008397ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/008397ac.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`008397ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00839/008397ec.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ef8.md#insn-00480f90) · [`00480fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ef8.md#insn-00480fc4)
- 新版 [`00480fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480f38.md#insn-00480fd0) · [`00481004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480f38.md#insn-00481004)

~~~diff
- 00480f90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480f90 ["INT_ADD", "register:40f0:8", ["const:480f90:8", "const:4:8"]]
- 00480f90 ["CALLIND", null, ["register:0:8"]]
+ 00480fd0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480fd0 ["INT_ADD", "register:40f0:8", ["const:480fd0:8", "const:4:8"]]
+ 00480fd0 ["CALLIND", null, ["register:0:8"]]
- 00480f90 bytes 00013fd6
+ 00480fd0 bytes 00013fd6
- 00480fc4 ["INT_ADD", "register:40f0:8", ["const:480fc4:8", "const:4:8"]]
- 00480fc4 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00481004 ["INT_ADD", "register:40f0:8", ["const:481004:8", "const:4:8"]]
+ 00481004 ["CALL", null, ["callee:00c57ee0:8"]]
- 00480fc4 bytes c75a1f94
+ 00481004 bytes b75b1f94
~~~


<a id="compare-4093a6c5fab255e812e4dfbff9d2b77d"></a>

### [`00480fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480fc8.md) → [`00481008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481008.md) FUN_00481008

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a22234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a22/00a22234.md) · 呼出先 3件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f508.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00a223d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a22/00a223d0.md) · 呼出先 3件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f548.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480fc8.md#insn-00480ff8) · [`00481008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480fc8.md#insn-00481008) · [`00481028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480fc8.md#insn-00481028)
- 新版 [`00481038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481008.md#insn-00481038) · [`00481048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481008.md#insn-00481048) · [`00481068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481008.md#insn-00481068)

~~~diff
- 00480ff8 ["INT_ADD", "register:40f0:8", ["const:480ff8:8", "const:4:8"]]
- 00480ff8 ["CALL", null, ["callee:0055f4c4:8"]]
+ 00481038 ["INT_ADD", "register:40f0:8", ["const:481038:8", "const:4:8"]]
+ 00481038 ["CALL", null, ["callee:0055f4c4:8"]]
- 00480ff8 bytes 23790394
+ 00481038 bytes 23790394
- 00481008 ["INT_ADD", "register:40f0:8", ["const:481008:8", "const:4:8"]]
- 00481008 ["CALL", null, ["callee:0055f548:8"]]
+ 00481048 ["INT_ADD", "register:40f0:8", ["const:481048:8", "const:4:8"]]
+ 00481048 ["CALL", null, ["callee:0055f548:8"]]
- 00481008 bytes 40790394
+ 00481048 bytes 40790394
- 00481028 ["COPY", "register:0:8", ["register:4040:8"]]
- 00481028 ["INT_ADD", "register:40f0:8", ["const:481028:8", "const:4:8"]]
- 00481028 ["CALLIND", null, ["register:0:8"]]
+ 00481068 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00481068 ["INT_ADD", "register:40f0:8", ["const:481068:8", "const:4:8"]]
+ 00481068 ["CALLIND", null, ["register:0:8"]]
- 00481028 bytes 00013fd6
+ 00481068 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb1d545b7292bebfeb8869171c91f2f8"></a>

### [`00481058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481058.md) → [`00481098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481098.md) FUN_00481098

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 25件 [`005b99cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b99cc.md) [`00675e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00675/00675e90.md) [`006dafdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006dafdc.md) [`0072ef2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ef2c.md) [`00732abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732abc.md) · 呼出先 3件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f528.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 25件 [`005b9a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9a0c.md) [`00675ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00675/00675ed0.md) [`006db01c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006db/006db01c.md) [`0072ef6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072e/0072ef6c.md) [`00732afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732afc.md) · 呼出先 3件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f568.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00481088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481058.md#insn-00481088) · [`00481098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481058.md#insn-00481098) · [`004810b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481058.md#insn-004810b8)
- 新版 [`004810c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481098.md#insn-004810c8) · [`004810d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481098.md#insn-004810d8) · [`004810f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481098.md#insn-004810f8)

~~~diff
- 00481088 ["INT_ADD", "register:40f0:8", ["const:481088:8", "const:4:8"]]
- 00481088 ["CALL", null, ["callee:0055f4c4:8"]]
+ 004810c8 ["INT_ADD", "register:40f0:8", ["const:4810c8:8", "const:4:8"]]
+ 004810c8 ["CALL", null, ["callee:0055f4c4:8"]]
- 00481088 bytes ff780394
+ 004810c8 bytes ff780394
- 00481098 ["INT_ADD", "register:40f0:8", ["const:481098:8", "const:4:8"]]
- 00481098 ["CALL", null, ["callee:0055f568:8"]]
+ 004810d8 ["INT_ADD", "register:40f0:8", ["const:4810d8:8", "const:4:8"]]
+ 004810d8 ["CALL", null, ["callee:0055f568:8"]]
- 00481098 bytes 24790394
+ 004810d8 bytes 24790394
- 004810b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004810b8 ["INT_ADD", "register:40f0:8", ["const:4810b8:8", "const:4:8"]]
- 004810b8 ["CALLIND", null, ["register:0:8"]]
+ 004810f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004810f8 ["INT_ADD", "register:40f0:8", ["const:4810f8:8", "const:4:8"]]
+ 004810f8 ["CALLIND", null, ["register:0:8"]]
- 004810b8 bytes 00013fd6
+ 004810f8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09908279b37f8bb9e3c90100a093bff8"></a>

### [`004810e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/004810e8.md) → [`00481128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481128.md) FUN_00481128

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`00737e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/00737e4c.md) [`0079fe08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079fe08.md) [`009813e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009813e0.md) [`009a91c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a91c8.md) [`00a14bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a14bf0.md) · 呼出先 6件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f4f8.md) [`005975c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975c8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 6件 [`00737e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00737/00737e8c.md) [`0079fe48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079fe48.md) [`0098157c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/0098157c.md) [`009a9364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a9364.md) [`00a14d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14d8c.md) · 呼出先 6件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f538.md) [`00597608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597608.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048112c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/004810e8.md#insn-0048112c) · [`0048113c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/004810e8.md#insn-0048113c) · [`0048115c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/004810e8.md#insn-0048115c)
- 新版 [`0048116c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481128.md#insn-0048116c) · [`0048117c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481128.md#insn-0048117c) · [`0048119c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481128.md#insn-0048119c)

~~~diff
- 0048112c ["INT_ADD", "register:40f0:8", ["const:48112c:8", "const:4:8"]]
- 0048112c ["CALL", null, ["callee:0055f4c4:8"]]
+ 0048116c ["INT_ADD", "register:40f0:8", ["const:48116c:8", "const:4:8"]]
+ 0048116c ["CALL", null, ["callee:0055f4c4:8"]]
- 0048112c bytes d6780394
+ 0048116c bytes d6780394
- 0048113c ["INT_ADD", "register:40f0:8", ["const:48113c:8", "const:4:8"]]
- 0048113c ["CALL", null, ["callee:0055f538:8"]]
+ 0048117c ["INT_ADD", "register:40f0:8", ["const:48117c:8", "const:4:8"]]
+ 0048117c ["CALL", null, ["callee:0055f538:8"]]
- 0048113c bytes ef780394
+ 0048117c bytes ef780394
- 0048115c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048115c ["INT_ADD", "register:40f0:8", ["const:48115c:8", "const:4:8"]]
- 0048115c ["CALLIND", null, ["register:0:8"]]
+ 0048119c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048119c ["INT_ADD", "register:40f0:8", ["const:48119c:8", "const:4:8"]]
+ 0048119c ["CALLIND", null, ["register:0:8"]]
- 0048115c bytes 00013fd6
+ 0048119c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-942ae38a0e38085cb10183cd7a92dc62"></a>

### [`00481200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481200.md) → [`00481240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481240.md) FUN_00481240

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0079fe08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079fe08.md) [`00a14bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a14bf0.md) · 呼出先 9件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f4f8.md) [`00597a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a0c.md) [`00597a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a18.md) [`00597a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a24.md)
- 新版 呼出元 2件 [`0079fe48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079fe48.md) [`00a14d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14d8c.md) · 呼出先 9件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f538.md) [`00597a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a4c.md) [`00597a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a58.md) [`00597a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a64.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00481230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481200.md#insn-00481230) · [`0048123c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481200.md#insn-0048123c) · [`0048124c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481200.md#insn-0048124c)
- 新版 [`00481270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481240.md#insn-00481270) · [`0048127c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481240.md#insn-0048127c) · [`0048128c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481240.md#insn-0048128c)

~~~diff
- 00481230 ["INT_ADD", "register:40f0:8", ["const:481230:8", "const:4:8"]]
- 00481230 ["CALL", null, ["callee:00597a4c:8"]]
+ 00481270 ["INT_ADD", "register:40f0:8", ["const:481270:8", "const:4:8"]]
+ 00481270 ["CALL", null, ["callee:00597a4c:8"]]
- 00481230 bytes f7590494
+ 00481270 bytes f7590494
- 0048123c ["INT_ADD", "register:40f0:8", ["const:48123c:8", "const:4:8"]]
- 0048123c ["CALL", null, ["callee:0055f4c4:8"]]
+ 0048127c ["INT_ADD", "register:40f0:8", ["const:48127c:8", "const:4:8"]]
+ 0048127c ["CALL", null, ["callee:0055f4c4:8"]]
- 0048123c bytes 92780394
+ 0048127c bytes 92780394
- 0048124c ["INT_ADD", "register:40f0:8", ["const:48124c:8", "const:4:8"]]
- 0048124c ["CALL", null, ["callee:0055f538:8"]]
+ 0048128c ["INT_ADD", "register:40f0:8", ["const:48128c:8", "const:4:8"]]
+ 0048128c ["CALL", null, ["callee:0055f538:8"]]
- 0048124c bytes ab780394
+ 0048128c bytes ab780394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d77cd656891625f7b3a129627d3d714a"></a>

### [`00481e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481e40.md) → [`00481e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481e80.md) FUN_00481e80

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 11件 [`00482acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482acc.md) [`004b3ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b3ea4.md) [`005ad7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad7a0.md) [`006e5d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5d30.md) [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 11件 [`00482b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482b0c.md) [`004b3ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3ee4.md) [`005ad7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md) [`006e5d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e5/006e5d70.md) [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00481e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481e40.md#insn-00481e7c) · [`00481ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481e40.md#insn-00481ed0) · [`00481f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481e40.md#insn-00481f04)
- 新版 [`00481ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481e80.md#insn-00481ebc) · [`00481f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481e80.md#insn-00481f10) · [`00481f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481e80.md#insn-00481f44)

~~~diff
- 00481e7c ["INT_ADD", "register:40f0:8", ["const:481e7c:8", "const:4:8"]]
- 00481e7c ["CALL", null, ["callee:00c57fe0:8"]]
+ 00481ebc ["INT_ADD", "register:40f0:8", ["const:481ebc:8", "const:4:8"]]
+ 00481ebc ["CALL", null, ["callee:00c57fe0:8"]]
- 00481e7c bytes 59571f94
+ 00481ebc bytes 49581f94
- 00481ed0 ["INT_ADD", "register:40f0:8", ["const:481ed0:8", "const:4:8"]]
- 00481ed0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00481f10 ["INT_ADD", "register:40f0:8", ["const:481f10:8", "const:4:8"]]
+ 00481f10 ["CALL", null, ["callee:00c57e90:8"]]
- 00481ed0 bytes f0561f94
+ 00481f10 bytes e0571f94
- 00481f04 ["INT_ADD", "register:40f0:8", ["const:481f04:8", "const:4:8"]]
- 00481f04 ["CALL", null, ["callee:00c57f40:8"]]
+ 00481f44 ["INT_ADD", "register:40f0:8", ["const:481f44:8", "const:4:8"]]
+ 00481f44 ["CALL", null, ["callee:00c57f40:8"]]
- 00481f04 bytes 0f571f94
+ 00481f44 bytes ff571f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9afb3c0343756eab339d0711a85dcf8"></a>

### [`00481f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481f44.md) → [`00481f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481f84.md) FUN_00481f84

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 8件 [`0043ec20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ec20.md) [`0043f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f8dc.md) [`00470ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md) [`0048469c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/0048469c.md) [`00484780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484780.md) · 呼出先 5件 [`00550b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550b64.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58030.md)
- 新版 呼出元 8件 [`0043ec60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ec60.md) [`0043f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f91c.md) [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) [`004846dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004846dc.md) [`004847c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004847c0.md) · 呼出先 5件 [`00550ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550ba4.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00481f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481f44.md#insn-00481f80) · [`00481fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481f44.md#insn-00481fa0) · [`00481fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481f44.md#insn-00481fb4)
- 新版 [`00481fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481f84.md#insn-00481fc0) · [`00481fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481f84.md#insn-00481fe0) · [`00481ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481f84.md#insn-00481ff4)

~~~diff
- 00481f80 ["INT_ADD", "register:40f0:8", ["const:481f80:8", "const:4:8"]]
- 00481f80 ["CALL", null, ["callee:00550ba4:8"]]
+ 00481fc0 ["INT_ADD", "register:40f0:8", ["const:481fc0:8", "const:4:8"]]
+ 00481fc0 ["CALL", null, ["callee:00550ba4:8"]]
- 00481f80 bytes f93a0394
+ 00481fc0 bytes f93a0394
- 00481fa0 ["INT_ADD", "register:40f0:8", ["const:481fa0:8", "const:4:8"]]
- 00481fa0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00481fe0 ["INT_ADD", "register:40f0:8", ["const:481fe0:8", "const:4:8"]]
+ 00481fe0 ["CALL", null, ["callee:00c53d00:8"]]
- 00481fa0 bytes 50461f94
+ 00481fe0 bytes 48471f94
- 00481fb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00481fb4 ["INT_ADD", "register:40f0:8", ["const:481fb4:8", "const:4:8"]]
- 00481fb4 ["CALLIND", null, ["register:0:8"]]
+ 00481ff4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00481ff4 ["INT_ADD", "register:40f0:8", ["const:481ff4:8", "const:4:8"]]
+ 00481ff4 ["CALLIND", null, ["register:0:8"]]
- 00481fb4 bytes 00013fd6
+ 00481ff4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2819e4fdcd6973ccbb217f62966ba5a6"></a>

### [`004820a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/004820a0.md) → [`004820e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004820e0.md) FUN_004820e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004820dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/004820a0.md#insn-004820dc) · [`004820ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/004820a0.md#insn-004820ec) · [`00482100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/004820a0.md#insn-00482100)
- 新版 [`0048211c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004820e0.md#insn-0048211c) · [`0048212c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004820e0.md#insn-0048212c) · [`00482140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004820e0.md#insn-00482140)

~~~diff
- 004820dc ["COPY", "register:0:8", ["register:4048:8"]]
- 004820dc ["INT_ADD", "register:40f0:8", ["const:4820dc:8", "const:4:8"]]
- 004820dc ["CALLIND", null, ["register:0:8"]]
+ 0048211c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0048211c ["INT_ADD", "register:40f0:8", ["const:48211c:8", "const:4:8"]]
+ 0048211c ["CALLIND", null, ["register:0:8"]]
- 004820dc bytes 20013fd6
+ 0048211c bytes 20013fd6
- 004820ec ["COPY", "register:0:8", ["register:4040:8"]]
- 004820ec ["INT_ADD", "register:40f0:8", ["const:4820ec:8", "const:4:8"]]
- 004820ec ["CALLIND", null, ["register:0:8"]]
+ 0048212c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048212c ["INT_ADD", "register:40f0:8", ["const:48212c:8", "const:4:8"]]
+ 0048212c ["CALLIND", null, ["register:0:8"]]
- 004820ec bytes 00013fd6
+ 0048212c bytes 00013fd6
- 00482100 ["COPY", "register:0:8", ["register:4040:8"]]
- 00482100 ["INT_ADD", "register:40f0:8", ["const:482100:8", "const:4:8"]]
- 00482100 ["CALLIND", null, ["register:0:8"]]
+ 00482140 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00482140 ["INT_ADD", "register:40f0:8", ["const:482140:8", "const:4:8"]]
+ 00482140 ["CALLIND", null, ["register:0:8"]]
- 00482100 bytes 00013fd6
+ 00482140 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d70665d5508e9c84b7d5c4025b42a51d"></a>

### [`00482210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482210.md) → [`00482250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482250.md) FUN_00482250

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00a14bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a14bf0.md) [`00a22234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a22/00a22234.md) · 呼出先 8件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00550be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be8.md) [`005975d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975d0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`00a14d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14d8c.md) [`00a223d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a22/00a223d0.md) · 呼出先 8件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00550c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c28.md) [`00597610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597610.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048228c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482210.md#insn-0048228c) · [`004822ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482210.md#insn-004822ac) · [`004822c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482210.md#insn-004822c0)
- 新版 [`004822cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482250.md#insn-004822cc) · [`004822ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482250.md#insn-004822ec) · [`00482300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482250.md#insn-00482300)

~~~diff
- 0048228c ["INT_ADD", "register:40f0:8", ["const:48228c:8", "const:4:8"]]
- 0048228c ["CALL", null, ["callee:00597610:8"]]
+ 004822cc ["INT_ADD", "register:40f0:8", ["const:4822cc:8", "const:4:8"]]
+ 004822cc ["CALL", null, ["callee:00597610:8"]]
- 0048228c bytes d1540494
+ 004822cc bytes d1540494
- 004822ac ["INT_ADD", "register:40f0:8", ["const:4822ac:8", "const:4:8"]]
- 004822ac ["CALL", null, ["callee:00c53d00:8"]]
+ 004822ec ["INT_ADD", "register:40f0:8", ["const:4822ec:8", "const:4:8"]]
+ 004822ec ["CALL", null, ["callee:00c53d00:8"]]
- 004822ac bytes 8d451f94
+ 004822ec bytes 85461f94
- 004822c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004822c0 ["INT_ADD", "register:40f0:8", ["const:4822c0:8", "const:4:8"]]
- 004822c0 ["CALLIND", null, ["register:0:8"]]
+ 00482300 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00482300 ["INT_ADD", "register:40f0:8", ["const:482300:8", "const:4:8"]]
+ 00482300 ["CALLIND", null, ["register:0:8"]]
- 004822c0 bytes 00013fd6
+ 00482300 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56d9587cb9299f51a3c4aa60a2cf8906"></a>

### [`004823bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/004823bc.md) → [`004823fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004823fc.md) FUN_004823fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`0063a1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a1c0.md) [`009816dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009816dc.md) · 呼出先 5件 [`005975d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975d0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58030.md)
- 新版 呼出元 3件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`0063a200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063a/0063a200.md) [`00981878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981878.md) · 呼出先 5件 [`00597610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597610.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00482438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/004823bc.md#insn-00482438) · [`00482458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/004823bc.md#insn-00482458) · [`0048246c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/004823bc.md#insn-0048246c)
- 新版 [`00482478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004823fc.md#insn-00482478) · [`00482498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004823fc.md#insn-00482498) · [`004824ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004823fc.md#insn-004824ac)

~~~diff
- 00482438 ["INT_ADD", "register:40f0:8", ["const:482438:8", "const:4:8"]]
- 00482438 ["CALL", null, ["callee:00597610:8"]]
+ 00482478 ["INT_ADD", "register:40f0:8", ["const:482478:8", "const:4:8"]]
+ 00482478 ["CALL", null, ["callee:00597610:8"]]
- 00482438 bytes 66540494
+ 00482478 bytes 66540494
- 00482458 ["INT_ADD", "register:40f0:8", ["const:482458:8", "const:4:8"]]
- 00482458 ["CALL", null, ["callee:00c53d00:8"]]
+ 00482498 ["INT_ADD", "register:40f0:8", ["const:482498:8", "const:4:8"]]
+ 00482498 ["CALL", null, ["callee:00c53d00:8"]]
- 00482458 bytes 22451f94
+ 00482498 bytes 1a461f94
- 0048246c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048246c ["INT_ADD", "register:40f0:8", ["const:48246c:8", "const:4:8"]]
- 0048246c ["CALLIND", null, ["register:0:8"]]
+ 004824ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 004824ac ["INT_ADD", "register:40f0:8", ["const:4824ac:8", "const:4:8"]]
+ 004824ac ["CALLIND", null, ["register:0:8"]]
- 0048246c bytes 00013fd6
+ 004824ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a80f6cedb3a10ad83b6e8cd4de23830"></a>

### [`004824f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/004824f8.md) → [`00482538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482538.md) FUN_00482538

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`0063a1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a1c0.md) [`009816dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009816dc.md) · 呼出先 0件 
- 新版 呼出元 3件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`0063a200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063a/0063a200.md) [`00981878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981878.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00482520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/004824f8.md#insn-00482520)
- 新版 [`00482560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482538.md#insn-00482560)

~~~diff
- 00482520 ["COPY", "register:0:8", ["register:4048:8"]]
- 00482520 ["INT_ADD", "register:40f0:8", ["const:482520:8", "const:4:8"]]
- 00482520 ["CALLIND", null, ["register:0:8"]]
+ 00482560 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00482560 ["INT_ADD", "register:40f0:8", ["const:482560:8", "const:4:8"]]
+ 00482560 ["CALLIND", null, ["register:0:8"]]
- 00482520 bytes 20013fd6
+ 00482560 bytes 20013fd6
~~~


<a id="compare-c3de0f1a5672af5845015b15b6b0572b"></a>

### [`004825a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/004825a0.md) → [`004825e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004825e0.md) FUN_004825e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 8件 [`0043ec20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ec20.md) [`0043f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f8dc.md) [`00637810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00637/00637810.md) [`00881718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881718.md) [`0097f984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f984.md) · 呼出先 11件 [`0055e830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e830.md) [`00560418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560418.md) [`00597e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e7c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 8件 [`0043ec60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ec60.md) [`0043f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f91c.md) [`00637850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00637/00637850.md) [`00881758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881758.md) [`0097fb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097fb20.md) · 呼出先 11件 [`0055e870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e870.md) [`00560458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560458.md) [`00597ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ebc.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004825e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/004825a0.md#insn-004825e0) · [`00482600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/004825a0.md#insn-00482600) · [`00482610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/004825a0.md#insn-00482610)
- 新版 [`00482620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004825e0.md#insn-00482620) · [`00482640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004825e0.md#insn-00482640) · [`00482650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004825e0.md#insn-00482650)

~~~diff
- 004825e0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004825e0 ["INT_ADD", "register:40f0:8", ["const:4825e0:8", "const:4:8"]]
- 004825e0 ["CALLIND", null, ["register:0:8"]]
+ 00482620 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00482620 ["INT_ADD", "register:40f0:8", ["const:482620:8", "const:4:8"]]
+ 00482620 ["CALLIND", null, ["register:0:8"]]
- 004825e0 bytes 20013fd6
+ 00482620 bytes 20013fd6
- 00482600 ["COPY", "register:0:8", ["register:4040:8"]]
- 00482600 ["INT_ADD", "register:40f0:8", ["const:482600:8", "const:4:8"]]
- 00482600 ["CALLIND", null, ["register:0:8"]]
+ 00482640 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00482640 ["INT_ADD", "register:40f0:8", ["const:482640:8", "const:4:8"]]
+ 00482640 ["CALLIND", null, ["register:0:8"]]
- 00482600 bytes 00013fd6
+ 00482640 bytes 00013fd6
- 00482610 ["COPY", "register:0:8", ["register:4040:8"]]
- 00482610 ["INT_ADD", "register:40f0:8", ["const:482610:8", "const:4:8"]]
- 00482610 ["CALLIND", null, ["register:0:8"]]
+ 00482650 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00482650 ["INT_ADD", "register:40f0:8", ["const:482650:8", "const:4:8"]]
+ 00482650 ["CALLIND", null, ["register:0:8"]]
- 00482610 bytes 00013fd6
+ 00482650 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-733ea0b5b4e44d90904f97ab44b72310"></a>

### [`0048384c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/0048384c.md) → [`0048388c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/0048388c.md) FUN_0048388c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00482acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482acc.md) [`0064b168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064b/0064b168.md) · 呼出先 1件 [`00485638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485638.md)
- 新版 呼出元 2件 [`00482b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482b0c.md) [`0064b1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064b/0064b1a8.md) · 呼出先 1件 [`00485678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485678.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00483868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/0048384c.md#insn-00483868)
- 新版 [`004838a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/0048388c.md#insn-004838a8)

~~~diff
- 00483868 ["INT_ADD", "register:40f0:8", ["const:483868:8", "const:4:8"]]
- 00483868 ["CALL", null, ["callee:00485678:8"]]
+ 004838a8 ["INT_ADD", "register:40f0:8", ["const:4838a8:8", "const:4:8"]]
+ 004838a8 ["CALL", null, ["callee:00485678:8"]]
- 00483868 bytes 74070094
+ 004838a8 bytes 74070094
~~~


<a id="compare-380b9102fd268d6bd0600eb7827bb737"></a>

### [`00483e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/00483e70.md) → [`00483eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483eb0.md) FUN_00483eb0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00483e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/00483e70.md#insn-00483e8c) · [`00483eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/00483e70.md#insn-00483eac)
- 新版 [`00483ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483eb0.md#insn-00483ecc) · [`00483eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483eb0.md#insn-00483eec)

~~~diff
- 00483e8c ["INT_ADD", "register:40f0:8", ["const:483e8c:8", "const:4:8"]]
- 00483e8c ["CALL", null, ["callee:00c53d00:8"]]
+ 00483ecc ["INT_ADD", "register:40f0:8", ["const:483ecc:8", "const:4:8"]]
+ 00483ecc ["CALL", null, ["callee:00c53d00:8"]]
- 00483e8c bytes 953e1f94
+ 00483ecc bytes 8d3f1f94
- 00483eac ["COPY", "register:0:8", ["register:4040:8"]]
- 00483eac ["INT_ADD", "register:40f0:8", ["const:483eac:8", "const:4:8"]]
- 00483eac ["CALLIND", null, ["register:0:8"]]
+ 00483eec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00483eec ["INT_ADD", "register:40f0:8", ["const:483eec:8", "const:4:8"]]
+ 00483eec ["CALLIND", null, ["register:0:8"]]
- 00483eac bytes 00013fd6
+ 00483eec bytes 00013fd6
~~~


<a id="compare-41928d2c3d318d18299aca02e5d10cf7"></a>

### [`00483ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/00483ec0.md) → [`00483f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483f00.md) FUN_00483f00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00483edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/00483ec0.md#insn-00483edc) · [`00483efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/00483ec0.md#insn-00483efc)
- 新版 [`00483f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483f00.md#insn-00483f1c) · [`00483f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483f00.md#insn-00483f3c)

~~~diff
- 00483edc ["INT_ADD", "register:40f0:8", ["const:483edc:8", "const:4:8"]]
- 00483edc ["CALL", null, ["callee:00c53d00:8"]]
+ 00483f1c ["INT_ADD", "register:40f0:8", ["const:483f1c:8", "const:4:8"]]
+ 00483f1c ["CALL", null, ["callee:00c53d00:8"]]
- 00483edc bytes 813e1f94
+ 00483f1c bytes 793f1f94
- 00483efc ["COPY", "register:0:8", ["register:4040:8"]]
- 00483efc ["INT_ADD", "register:40f0:8", ["const:483efc:8", "const:4:8"]]
- 00483efc ["CALLIND", null, ["register:0:8"]]
+ 00483f3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00483f3c ["INT_ADD", "register:40f0:8", ["const:483f3c:8", "const:4:8"]]
+ 00483f3c ["CALLIND", null, ["register:0:8"]]
- 00483efc bytes 00013fd6
+ 00483f3c bytes 00013fd6
~~~


<a id="compare-74d0f2c89d9cf4d5288fd07e8c40f068"></a>

### [`00483f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/00483f10.md) → [`00483f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483f50.md) FUN_00483f50

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00483f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/00483f10.md#insn-00483f2c) · [`00483f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/00483f10.md#insn-00483f4c)
- 新版 [`00483f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483f50.md#insn-00483f6c) · [`00483f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483f50.md#insn-00483f8c)

~~~diff
- 00483f2c ["INT_ADD", "register:40f0:8", ["const:483f2c:8", "const:4:8"]]
- 00483f2c ["CALL", null, ["callee:00c53d00:8"]]
+ 00483f6c ["INT_ADD", "register:40f0:8", ["const:483f6c:8", "const:4:8"]]
+ 00483f6c ["CALL", null, ["callee:00c53d00:8"]]
- 00483f2c bytes 6d3e1f94
+ 00483f6c bytes 653f1f94
- 00483f4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00483f4c ["INT_ADD", "register:40f0:8", ["const:483f4c:8", "const:4:8"]]
- 00483f4c ["CALLIND", null, ["register:0:8"]]
+ 00483f8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00483f8c ["INT_ADD", "register:40f0:8", ["const:483f8c:8", "const:4:8"]]
+ 00483f8c ["CALLIND", null, ["register:0:8"]]
- 00483f4c bytes 00013fd6
+ 00483f8c bytes 00013fd6
~~~


<a id="compare-528fba49d1b948364163beb406c70792"></a>

### [`00483f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/00483f60.md) → [`00483fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483fa0.md) FUN_00483fa0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00483f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/00483f60.md#insn-00483f7c) · [`00483f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/00483f60.md#insn-00483f9c)
- 新版 [`00483fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483fa0.md#insn-00483fbc) · [`00483fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483fa0.md#insn-00483fdc)

~~~diff
- 00483f7c ["INT_ADD", "register:40f0:8", ["const:483f7c:8", "const:4:8"]]
- 00483f7c ["CALL", null, ["callee:00c53d00:8"]]
+ 00483fbc ["INT_ADD", "register:40f0:8", ["const:483fbc:8", "const:4:8"]]
+ 00483fbc ["CALL", null, ["callee:00c53d00:8"]]
- 00483f7c bytes 593e1f94
+ 00483fbc bytes 513f1f94
- 00483f9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00483f9c ["INT_ADD", "register:40f0:8", ["const:483f9c:8", "const:4:8"]]
- 00483f9c ["CALLIND", null, ["register:0:8"]]
+ 00483fdc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00483fdc ["INT_ADD", "register:40f0:8", ["const:483fdc:8", "const:4:8"]]
+ 00483fdc ["CALLIND", null, ["register:0:8"]]
- 00483f9c bytes 00013fd6
+ 00483fdc bytes 00013fd6
~~~


<a id="compare-94428d772c3ae0b845bf280bea557a46"></a>

### [`00483fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/00483fb0.md) → [`00483ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483ff0.md) FUN_00483ff0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) · 呼出先 9件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00550be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be0.md) [`00550be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be8.md) [`00597e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e7c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00a1a750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a750.md) · 呼出先 9件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00550c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c20.md) [`00550c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c28.md) [`00597ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ebc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048401c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/00483fb0.md#insn-0048401c) · [`00484080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/00483fb0.md#insn-00484080) · [`00484090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/00483fb0.md#insn-00484090)
- 新版 [`0048405c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483ff0.md#insn-0048405c) · [`004840c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483ff0.md#insn-004840c0) · [`004840d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483ff0.md#insn-004840d0)

~~~diff
- 0048401c ["INT_ADD", "register:40f0:8", ["const:48401c:8", "const:4:8"]]
- 0048401c ["CALL", null, ["callee:00c57fd0:8"]]
+ 0048405c ["INT_ADD", "register:40f0:8", ["const:48405c:8", "const:4:8"]]
+ 0048405c ["CALL", null, ["callee:00c57fd0:8"]]
- 0048401c bytes ed4e1f94
+ 0048405c bytes dd4f1f94
- 00484080 ["INT_ADD", "register:40f0:8", ["const:484080:8", "const:4:8"]]
- 00484080 ["CALL", null, ["callee:00597ebc:8"]]
+ 004840c0 ["INT_ADD", "register:40f0:8", ["const:4840c0:8", "const:4:8"]]
+ 004840c0 ["CALL", null, ["callee:00597ebc:8"]]
- 00484080 bytes 7f4f0494
+ 004840c0 bytes 7f4f0494
- 00484090 ["INT_ADD", "register:40f0:8", ["const:484090:8", "const:4:8"]]
- 00484090 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004840d0 ["INT_ADD", "register:40f0:8", ["const:4840d0:8", "const:4:8"]]
+ 004840d0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00484090 bytes 884e1f94
+ 004840d0 bytes 784f1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a801bd71394954cf1e9921e4b85b891b"></a>

### [`004841d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/004841d0.md) → [`00484210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484210.md) FUN_00484210

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0087f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md) [`00881370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881370.md) [`00881544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881544.md) · 呼出先 12件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`00550be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be0.md)
- 新版 呼出元 3件 [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) [`008813b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/008813b0.md) [`00881584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881584.md) · 呼出先 12件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`00550c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00484200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/004841d0.md#insn-00484200) · [`00484210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/004841d0.md#insn-00484210) · [`00484220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/004841d0.md#insn-00484220)
- 新版 [`00484240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484210.md#insn-00484240) · [`00484250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484210.md#insn-00484250) · [`00484260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484210.md#insn-00484260)

~~~diff
- 00484200 ["INT_ADD", "register:40f0:8", ["const:484200:8", "const:4:8"]]
- 00484200 ["CALL", null, ["callee:00550c28:8"]]
+ 00484240 ["INT_ADD", "register:40f0:8", ["const:484240:8", "const:4:8"]]
+ 00484240 ["CALL", null, ["callee:00550c28:8"]]
- 00484200 bytes 7a320394
+ 00484240 bytes 7a320394
- 00484210 ["INT_ADD", "register:40f0:8", ["const:484210:8", "const:4:8"]]
- 00484210 ["CALL", null, ["callee:0043dba4:8"]]
+ 00484250 ["INT_ADD", "register:40f0:8", ["const:484250:8", "const:4:8"]]
+ 00484250 ["CALL", null, ["callee:0043dba4:8"]]
- 00484210 bytes 55e6fe97
+ 00484250 bytes 55e6fe97
- 00484220 ["INT_ADD", "register:40f0:8", ["const:484220:8", "const:4:8"]]
- 00484220 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00484260 ["INT_ADD", "register:40f0:8", ["const:484260:8", "const:4:8"]]
+ 00484260 ["CALL", null, ["callee:00c57eb0:8"]]
- 00484220 bytes 244e1f94
+ 00484260 bytes 144f1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-131831a757a427632968127a4779b909"></a>

### [`0048469c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/0048469c.md) → [`004846dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004846dc.md) FUN_004846dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b10cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10cc4.md) · 呼出先 5件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00481f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481f44.md) [`00550be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00b110ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b110ec.md) · 呼出先 5件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00481f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481f84.md) [`00550c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c24.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004846cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/0048469c.md#insn-004846cc) · [`004846dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/0048469c.md#insn-004846dc) · [`004846ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/0048469c.md#insn-004846ec)
- 新版 [`0048470c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004846dc.md#insn-0048470c) · [`0048471c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004846dc.md#insn-0048471c) · [`0048472c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004846dc.md#insn-0048472c)

~~~diff
- 004846cc ["INT_ADD", "register:40f0:8", ["const:4846cc:8", "const:4:8"]]
- 004846cc ["CALL", null, ["callee:00550c24:8"]]
+ 0048470c ["INT_ADD", "register:40f0:8", ["const:48470c:8", "const:4:8"]]
+ 0048470c ["CALL", null, ["callee:00550c24:8"]]
- 004846cc bytes 46310394
+ 0048470c bytes 46310394
- 004846dc ["INT_ADD", "register:40f0:8", ["const:4846dc:8", "const:4:8"]]
- 004846dc ["CALL", null, ["callee:0043dba4:8"]]
+ 0048471c ["INT_ADD", "register:40f0:8", ["const:48471c:8", "const:4:8"]]
+ 0048471c ["CALL", null, ["callee:0043dba4:8"]]
- 004846dc bytes 22e5fe97
+ 0048471c bytes 22e5fe97
- 004846ec ["INT_ADD", "register:40f0:8", ["const:4846ec:8", "const:4:8"]]
- 004846ec ["CALL", null, ["callee:00c57eb0:8"]]
+ 0048472c ["INT_ADD", "register:40f0:8", ["const:48472c:8", "const:4:8"]]
+ 0048472c ["CALL", null, ["callee:00c57eb0:8"]]
- 004846ec bytes f14c1f94
+ 0048472c bytes e14d1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67b4e8d5d729ffac1b93bbfe46b32c45"></a>

### [`00484dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484dbc.md) → [`00484dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484dfc.md) FUN_00484dfc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0087f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md) [`00a148e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a148e4.md) · 呼出先 4件 [`005975d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975d8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) [`00a14a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14a80.md) · 呼出先 4件 [`00597618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597618.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00484df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484dbc.md#insn-00484df4) · [`00484e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484dbc.md#insn-00484e14) · [`00484e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484dbc.md#insn-00484e28)
- 新版 [`00484e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484dfc.md#insn-00484e34) · [`00484e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484dfc.md#insn-00484e54) · [`00484e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484dfc.md#insn-00484e68)

~~~diff
- 00484df4 ["INT_ADD", "register:40f0:8", ["const:484df4:8", "const:4:8"]]
- 00484df4 ["CALL", null, ["callee:00597618:8"]]
+ 00484e34 ["INT_ADD", "register:40f0:8", ["const:484e34:8", "const:4:8"]]
+ 00484e34 ["CALL", null, ["callee:00597618:8"]]
- 00484df4 bytes f9490494
+ 00484e34 bytes f9490494
- 00484e14 ["INT_ADD", "register:40f0:8", ["const:484e14:8", "const:4:8"]]
- 00484e14 ["CALL", null, ["callee:00c53d00:8"]]
+ 00484e54 ["INT_ADD", "register:40f0:8", ["const:484e54:8", "const:4:8"]]
+ 00484e54 ["CALL", null, ["callee:00c53d00:8"]]
- 00484e14 bytes b33a1f94
+ 00484e54 bytes ab3b1f94
- 00484e28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00484e28 ["INT_ADD", "register:40f0:8", ["const:484e28:8", "const:4:8"]]
- 00484e28 ["CALLIND", null, ["register:0:8"]]
+ 00484e68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00484e68 ["INT_ADD", "register:40f0:8", ["const:484e68:8", "const:4:8"]]
+ 00484e68 ["CALLIND", null, ["register:0:8"]]
- 00484e28 bytes 00013fd6
+ 00484e68 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e63ef3b00d61da55fb7aa96c2c4838f"></a>

### [`00484ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484ea8.md) → [`00484ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484ee8.md) FUN_00484ee8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`005975cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975cc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0059760c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059760c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00484edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484ea8.md#insn-00484edc) · [`00484ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484ea8.md#insn-00484ef8) · [`00484f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484ea8.md#insn-00484f10)
- 新版 [`00484f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484ee8.md#insn-00484f1c) · [`00484f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484ee8.md#insn-00484f38) · [`00484f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484ee8.md#insn-00484f50)

~~~diff
- 00484edc ["COPY", "register:0:8", ["register:4040:8"]]
- 00484edc ["INT_ADD", "register:40f0:8", ["const:484edc:8", "const:4:8"]]
- 00484edc ["CALLIND", null, ["register:0:8"]]
+ 00484f1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00484f1c ["INT_ADD", "register:40f0:8", ["const:484f1c:8", "const:4:8"]]
+ 00484f1c ["CALLIND", null, ["register:0:8"]]
- 00484edc bytes 00013fd6
+ 00484f1c bytes 00013fd6
- 00484ef8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00484ef8 ["INT_ADD", "register:40f0:8", ["const:484ef8:8", "const:4:8"]]
- 00484ef8 ["CALLIND", null, ["register:0:8"]]
+ 00484f38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00484f38 ["INT_ADD", "register:40f0:8", ["const:484f38:8", "const:4:8"]]
+ 00484f38 ["CALLIND", null, ["register:0:8"]]
- 00484ef8 bytes 00013fd6
+ 00484f38 bytes 00013fd6
- 00484f10 ["COPY", "register:0:8", ["register:4048:8"]]
- 00484f10 ["INT_ADD", "register:40f0:8", ["const:484f10:8", "const:4:8"]]
- 00484f10 ["CALLIND", null, ["register:0:8"]]
+ 00484f50 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00484f50 ["INT_ADD", "register:40f0:8", ["const:484f50:8", "const:4:8"]]
+ 00484f50 ["CALLIND", null, ["register:0:8"]]
- 00484f10 bytes 20013fd6
+ 00484f50 bytes 20013fd6
~~~


<a id="compare-d61ab64b96020451b204c864cb67a6cc"></a>

### [`00484f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484f34.md) → [`00484f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484f74.md) FUN_00484f74

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00484f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484f34.md#insn-00484f60) · [`00484f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484f34.md#insn-00484f80) · [`00484f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484f34.md#insn-00484f98)
- 新版 [`00484fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484f74.md#insn-00484fa0) · [`00484fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484f74.md#insn-00484fc0) · [`00484fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484f74.md#insn-00484fd8)

~~~diff
- 00484f60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00484f60 ["INT_ADD", "register:40f0:8", ["const:484f60:8", "const:4:8"]]
- 00484f60 ["CALLIND", null, ["register:0:8"]]
+ 00484fa0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00484fa0 ["INT_ADD", "register:40f0:8", ["const:484fa0:8", "const:4:8"]]
+ 00484fa0 ["CALLIND", null, ["register:0:8"]]
- 00484f60 bytes 00013fd6
+ 00484fa0 bytes 00013fd6
- 00484f80 ["COPY", "register:0:8", ["register:4048:8"]]
- 00484f80 ["INT_ADD", "register:40f0:8", ["const:484f80:8", "const:4:8"]]
- 00484f80 ["CALLIND", null, ["register:0:8"]]
+ 00484fc0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00484fc0 ["INT_ADD", "register:40f0:8", ["const:484fc0:8", "const:4:8"]]
+ 00484fc0 ["CALLIND", null, ["register:0:8"]]
- 00484f80 bytes 20013fd6
+ 00484fc0 bytes 20013fd6
- 00484f98 ["COPY", "register:0:8", ["register:4048:8"]]
- 00484f98 ["INT_ADD", "register:40f0:8", ["const:484f98:8", "const:4:8"]]
- 00484f98 ["CALLIND", null, ["register:0:8"]]
+ 00484fd8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00484fd8 ["INT_ADD", "register:40f0:8", ["const:484fd8:8", "const:4:8"]]
+ 00484fd8 ["CALLIND", null, ["register:0:8"]]
- 00484f98 bytes 20013fd6
+ 00484fd8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a2d00722338c016b7ec42c701e24edb"></a>

### [`0048503c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/0048503c.md) → [`0048507c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/0048507c.md) FUN_0048507c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0087f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md) · 呼出先 9件 [`0055e830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e830.md) [`00560418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560418.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) · 呼出先 9件 [`0055e870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e870.md) [`00560458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560458.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048506c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/0048503c.md#insn-0048506c) · [`00485080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/0048503c.md#insn-00485080) · [`00485098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/0048503c.md#insn-00485098)
- 新版 [`004850ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/0048507c.md#insn-004850ac) · [`004850c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/0048507c.md#insn-004850c0) · [`004850d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/0048507c.md#insn-004850d8)

~~~diff
- 0048506c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048506c ["INT_ADD", "register:40f0:8", ["const:48506c:8", "const:4:8"]]
- 0048506c ["CALLIND", null, ["register:0:8"]]
+ 004850ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 004850ac ["INT_ADD", "register:40f0:8", ["const:4850ac:8", "const:4:8"]]
+ 004850ac ["CALLIND", null, ["register:0:8"]]
- 0048506c bytes 00013fd6
+ 004850ac bytes 00013fd6
- 00485080 ["INT_ADD", "register:40f0:8", ["const:485080:8", "const:4:8"]]
- 00485080 ["CALL", null, ["callee:0055e870:8"]]
+ 004850c0 ["INT_ADD", "register:40f0:8", ["const:4850c0:8", "const:4:8"]]
+ 004850c0 ["CALL", null, ["callee:0055e870:8"]]
- 00485080 bytes ec650394
+ 004850c0 bytes ec650394
- 00485098 ["COPY", "register:0:8", ["register:4048:8"]]
- 00485098 ["INT_ADD", "register:40f0:8", ["const:485098:8", "const:4:8"]]
- 00485098 ["CALLIND", null, ["register:0:8"]]
+ 004850d8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004850d8 ["INT_ADD", "register:40f0:8", ["const:4850d8:8", "const:4:8"]]
+ 004850d8 ["CALLIND", null, ["register:0:8"]]
- 00485098 bytes 20013fd6
+ 004850d8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30a1bb90a5a20e2f9e904167415f3a7d"></a>

### [`004855e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/004855e0.md) → [`00485620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485620.md) FUN_00485620

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0087f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md) · 呼出先 3件 [`00485370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485370.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) · 呼出先 3件 [`004853b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/004853b0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004855f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/004855e0.md#insn-004855f0) · [`00485608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/004855e0.md#insn-00485608) · [`0048561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/004855e0.md#insn-0048561c)
- 新版 [`00485630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485620.md#insn-00485630) · [`00485648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485620.md#insn-00485648) · [`0048565c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485620.md#insn-0048565c)

~~~diff
- 004855f0 ["INT_ADD", "register:40f0:8", ["const:4855f0:8", "const:4:8"]]
- 004855f0 ["CALL", null, ["callee:004853b0:8"]]
+ 00485630 ["INT_ADD", "register:40f0:8", ["const:485630:8", "const:4:8"]]
+ 00485630 ["CALL", null, ["callee:004853b0:8"]]
- 004855f0 bytes 60ffff97
+ 00485630 bytes 60ffff97
- 00485608 ["INT_ADD", "register:40f0:8", ["const:485608:8", "const:4:8"]]
- 00485608 ["CALL", null, ["callee:00c53d00:8"]]
+ 00485648 ["INT_ADD", "register:40f0:8", ["const:485648:8", "const:4:8"]]
+ 00485648 ["CALL", null, ["callee:00c53d00:8"]]
- 00485608 bytes b6381f94
+ 00485648 bytes ae391f94
- 0048561c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048561c ["INT_ADD", "register:40f0:8", ["const:48561c:8", "const:4:8"]]
- 0048561c ["CALLIND", null, ["register:0:8"]]
+ 0048565c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048565c ["INT_ADD", "register:40f0:8", ["const:48565c:8", "const:4:8"]]
+ 0048565c ["CALLIND", null, ["register:0:8"]]
- 0048561c bytes 00013fd6
+ 0048565c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a124bb97e2950e194582c8f0fd9480ee"></a>

### [`00485638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485638.md) → [`00485678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485678.md) FUN_00485678

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00482acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482acc.md) [`0048384c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/0048384c.md) [`0048e154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e154.md) [`0064b168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064b/0064b168.md) [`0089d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089d/0089d484.md) · 呼出先 6件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0048586c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/0048586c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 5件 [`00482b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482b0c.md) [`0048388c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/0048388c.md) [`0048e194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e194.md) [`0064b1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064b/0064b1a8.md) [`0089d4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089d/0089d4c8.md) · 呼出先 6件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`004858ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/004858ac.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048569c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485638.md#insn-0048569c) · [`004856d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485638.md#insn-004856d8) · [`00485778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485638.md#insn-00485778)
- 新版 [`004856dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485678.md#insn-004856dc) · [`00485718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485678.md#insn-00485718) · [`004857b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485678.md#insn-004857b8)

~~~diff
- 0048569c ["INT_ADD", "register:40f0:8", ["const:48569c:8", "const:4:8"]]
- 0048569c ["CALL", null, ["callee:00c57eb0:8"]]
+ 004856dc ["INT_ADD", "register:40f0:8", ["const:4856dc:8", "const:4:8"]]
+ 004856dc ["CALL", null, ["callee:00c57eb0:8"]]
- 0048569c bytes 05491f94
+ 004856dc bytes f5491f94
- 004856d8 ["INT_ADD", "register:40f0:8", ["const:4856d8:8", "const:4:8"]]
- 004856d8 ["CALL", null, ["callee:00c57fd0:8"]]
+ 00485718 ["INT_ADD", "register:40f0:8", ["const:485718:8", "const:4:8"]]
+ 00485718 ["CALL", null, ["callee:00c57fd0:8"]]
- 004856d8 bytes 3e491f94
+ 00485718 bytes 2e4a1f94
- 00485778 ["INT_ADD", "register:40f0:8", ["const:485778:8", "const:4:8"]]
- 00485778 ["CALL", null, ["callee:004858ac:8"]]
+ 004857b8 ["INT_ADD", "register:40f0:8", ["const:4857b8:8", "const:4:8"]]
+ 004857b8 ["CALL", null, ["callee:004858ac:8"]]
- 00485778 bytes 3d000094
+ 004857b8 bytes 3d000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8613450a3e6b0e3c7ad35ace964d7b95"></a>

### [`0048586c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/0048586c.md) → [`004858ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/004858ac.md) FUN_004858ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00485638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485638.md) · 呼出先 7件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00485678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485678.md) · 呼出先 7件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00485914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/0048586c.md#insn-00485914) · [`004859d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/0048586c.md#insn-004859d0) · [`00485a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/0048586c.md#insn-00485a28)
- 新版 [`00485954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/004858ac.md#insn-00485954) · [`00485a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/004858ac.md#insn-00485a10) · [`00485a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/004858ac.md#insn-00485a68)

~~~diff
- 00485914 ["INT_ADD", "register:40f0:8", ["const:485914:8", "const:4:8"]]
- 00485914 ["CALL", null, ["callee:00c57e90:8"]]
+ 00485954 ["INT_ADD", "register:40f0:8", ["const:485954:8", "const:4:8"]]
+ 00485954 ["CALL", null, ["callee:00c57e90:8"]]
- 00485914 bytes 5f481f94
+ 00485954 bytes 4f491f94
- 004859d0 ["INT_ADD", "register:40f0:8", ["const:4859d0:8", "const:4:8"]]
- 004859d0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00485a10 ["INT_ADD", "register:40f0:8", ["const:485a10:8", "const:4:8"]]
+ 00485a10 ["CALL", null, ["callee:00c57e90:8"]]
- 004859d0 bytes 30481f94
+ 00485a10 bytes 20491f94
- 00485a28 ["INT_ADD", "register:40f0:8", ["const:485a28:8", "const:4:8"]]
- 00485a28 ["CALL", null, ["callee:00c58000:8"]]
+ 00485a68 ["INT_ADD", "register:40f0:8", ["const:485a68:8", "const:4:8"]]
+ 00485a68 ["CALL", null, ["callee:00c58000:8"]]
- 00485a28 bytes 76481f94
+ 00485a68 bytes 66491f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8a0e721e4fa29f64c119fe0aa03e1b9"></a>

### [`00486dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486dec.md) → [`00486e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486e2c.md) FUN_00486e2c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00486e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486dec.md#insn-00486e14)
- 新版 [`00486e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486e2c.md#insn-00486e54)

~~~diff
- 00486e14 ["COPY", "register:0:8", ["register:4048:8"]]
- 00486e14 ["INT_ADD", "register:40f0:8", ["const:486e14:8", "const:4:8"]]
- 00486e14 ["CALLIND", null, ["register:0:8"]]
+ 00486e54 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00486e54 ["INT_ADD", "register:40f0:8", ["const:486e54:8", "const:4:8"]]
+ 00486e54 ["CALLIND", null, ["register:0:8"]]
- 00486e14 bytes 20013fd6
+ 00486e54 bytes 20013fd6
~~~


<a id="compare-66e049b2f4202743bd3bc99b7dfbaff8"></a>

### [`00486f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486f04.md) → [`00486f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486f44.md) FUN_00486f44

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00486f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486f04.md#insn-00486f20) · [`00486f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486f04.md#insn-00486f40)
- 新版 [`00486f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486f44.md#insn-00486f60) · [`00486f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486f44.md#insn-00486f80)

~~~diff
- 00486f20 ["INT_ADD", "register:40f0:8", ["const:486f20:8", "const:4:8"]]
- 00486f20 ["CALL", null, ["callee:00c53d00:8"]]
+ 00486f60 ["INT_ADD", "register:40f0:8", ["const:486f60:8", "const:4:8"]]
+ 00486f60 ["CALL", null, ["callee:00c53d00:8"]]
- 00486f20 bytes 70321f94
+ 00486f60 bytes 68331f94
- 00486f40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00486f40 ["INT_ADD", "register:40f0:8", ["const:486f40:8", "const:4:8"]]
- 00486f40 ["CALLIND", null, ["register:0:8"]]
+ 00486f80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00486f80 ["INT_ADD", "register:40f0:8", ["const:486f80:8", "const:4:8"]]
+ 00486f80 ["CALLIND", null, ["register:0:8"]]
- 00486f40 bytes 00013fd6
+ 00486f80 bytes 00013fd6
~~~


<a id="compare-2bb8bfa8832677cc08736075f74668df"></a>

### [`00486f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486f54.md) → [`00486f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486f94.md) FUN_00486f94

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00486f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486f54.md#insn-00486f94) · [`00486fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486f54.md#insn-00486fb0) · [`00486fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486f54.md#insn-00486fd0)
- 新版 [`00486fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486f94.md#insn-00486fd4) · [`00486ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486f94.md#insn-00486ff0) · [`00487010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486f94.md#insn-00487010)

~~~diff
- 00486f94 ["COPY", "register:0:8", ["register:4048:8"]]
- 00486f94 ["INT_ADD", "register:40f0:8", ["const:486f94:8", "const:4:8"]]
- 00486f94 ["CALLIND", null, ["register:0:8"]]
+ 00486fd4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00486fd4 ["INT_ADD", "register:40f0:8", ["const:486fd4:8", "const:4:8"]]
+ 00486fd4 ["CALLIND", null, ["register:0:8"]]
- 00486f94 bytes 20013fd6
+ 00486fd4 bytes 20013fd6
- 00486fb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00486fb0 ["INT_ADD", "register:40f0:8", ["const:486fb0:8", "const:4:8"]]
- 00486fb0 ["CALLIND", null, ["register:0:8"]]
+ 00486ff0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00486ff0 ["INT_ADD", "register:40f0:8", ["const:486ff0:8", "const:4:8"]]
+ 00486ff0 ["CALLIND", null, ["register:0:8"]]
- 00486fb0 bytes 00013fd6
+ 00486ff0 bytes 00013fd6
- 00486fd0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00486fd0 ["INT_ADD", "register:40f0:8", ["const:486fd0:8", "const:4:8"]]
- 00486fd0 ["CALLIND", null, ["register:0:8"]]
+ 00487010 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00487010 ["INT_ADD", "register:40f0:8", ["const:487010:8", "const:4:8"]]
+ 00487010 ["CALLIND", null, ["register:0:8"]]
- 00486fd0 bytes 20013fd6
+ 00487010 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a054e74d64eee30a5cd5d7dd7fd8e4f4"></a>

### [`00487360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487360.md) → [`004873a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/004873a0.md) FUN_004873a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00487398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487360.md#insn-00487398) · [`004873b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487360.md#insn-004873b4) · [`004873c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487360.md#insn-004873c8)
- 新版 [`004873d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/004873a0.md#insn-004873d8) · [`004873f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/004873a0.md#insn-004873f4) · [`00487408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/004873a0.md#insn-00487408)

~~~diff
- 00487398 ["COPY", "register:0:8", ["register:4040:8"]]
- 00487398 ["INT_ADD", "register:40f0:8", ["const:487398:8", "const:4:8"]]
- 00487398 ["CALLIND", null, ["register:0:8"]]
+ 004873d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004873d8 ["INT_ADD", "register:40f0:8", ["const:4873d8:8", "const:4:8"]]
+ 004873d8 ["CALLIND", null, ["register:0:8"]]
- 00487398 bytes 00013fd6
+ 004873d8 bytes 00013fd6
- 004873b4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004873b4 ["INT_ADD", "register:40f0:8", ["const:4873b4:8", "const:4:8"]]
- 004873b4 ["CALLIND", null, ["register:0:8"]]
+ 004873f4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004873f4 ["INT_ADD", "register:40f0:8", ["const:4873f4:8", "const:4:8"]]
+ 004873f4 ["CALLIND", null, ["register:0:8"]]
- 004873b4 bytes 20013fd6
+ 004873f4 bytes 20013fd6
- 004873c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004873c8 ["INT_ADD", "register:40f0:8", ["const:4873c8:8", "const:4:8"]]
- 004873c8 ["CALLIND", null, ["register:0:8"]]
+ 00487408 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00487408 ["INT_ADD", "register:40f0:8", ["const:487408:8", "const:4:8"]]
+ 00487408 ["CALLIND", null, ["register:0:8"]]
- 004873c8 bytes 00013fd6
+ 00487408 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d9c5610912cc0f7a0b56f0728f12a95"></a>

### [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) → [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) FUN_0048793c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 132件 [`00444b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444b98.md) [`00444de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md) [`0046f074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md) [`00470ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58190.md)
- 新版 呼出元 132件 [`00444bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444bd8.md) [`00444e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444e20.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) [`0046f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md) [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58590.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00487920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md#insn-00487920) · [`00487934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md#insn-00487934) · [`00487958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md#insn-00487958)
- 新版 [`00487960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md#insn-00487960) · [`00487974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md#insn-00487974) · [`00487998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md#insn-00487998)

~~~diff
- 00487920 ["COPY", "register:0:8", ["register:4040:8"]]
- 00487920 ["INT_ADD", "register:40f0:8", ["const:487920:8", "const:4:8"]]
- 00487920 ["CALLIND", null, ["register:0:8"]]
+ 00487960 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00487960 ["INT_ADD", "register:40f0:8", ["const:487960:8", "const:4:8"]]
+ 00487960 ["CALLIND", null, ["register:0:8"]]
- 00487920 bytes 00013fd6
+ 00487960 bytes 00013fd6
- 00487934 ["INT_ADD", "register:40f0:8", ["const:487934:8", "const:4:8"]]
- 00487934 ["CALL", null, ["callee:00c58590:8"]]
+ 00487974 ["INT_ADD", "register:40f0:8", ["const:487974:8", "const:4:8"]]
+ 00487974 ["CALL", null, ["callee:00c58590:8"]]
- 00487934 bytes 17421f94
+ 00487974 bytes 07431f94
- 00487958 ["INT_ADD", "register:40f0:8", ["const:487958:8", "const:4:8"]]
- 00487958 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00487998 ["INT_ADD", "register:40f0:8", ["const:487998:8", "const:4:8"]]
+ 00487998 ["CALL", null, ["callee:00c57ee0:8"]]
- 00487958 bytes 62401f94
+ 00487998 bytes 52411f94
~~~


<a id="compare-5efe78b336f8387b402178ddd21c6927"></a>

### [`0048795c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/0048795c.md) → [`0048799c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048799c.md) FUN_0048799c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`006dfd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006df/006dfd88.md) [`006e29b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e2/006e29b0.md) [`00812e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00812/00812e8c.md) [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c581b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c581b0.md)
- 新版 呼出元 4件 [`006dfdc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006df/006dfdc8.md) [`006e29f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e2/006e29f0.md) [`00812ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00812/00812ecc.md) [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c585b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00487980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/0048795c.md#insn-00487980) · [`00487990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/0048795c.md#insn-00487990) · [`004879bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/0048795c.md#insn-004879bc)
- 新版 [`004879c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048799c.md#insn-004879c0) · [`004879d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048799c.md#insn-004879d0) · [`004879fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048799c.md#insn-004879fc)

~~~diff
- 00487980 ["COPY", "register:0:8", ["register:4040:8"]]
- 00487980 ["INT_ADD", "register:40f0:8", ["const:487980:8", "const:4:8"]]
- 00487980 ["CALLIND", null, ["register:0:8"]]
+ 004879c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004879c0 ["INT_ADD", "register:40f0:8", ["const:4879c0:8", "const:4:8"]]
+ 004879c0 ["CALLIND", null, ["register:0:8"]]
- 00487980 bytes 00013fd6
+ 004879c0 bytes 00013fd6
- 00487990 ["INT_ADD", "register:40f0:8", ["const:487990:8", "const:4:8"]]
- 00487990 ["CALL", null, ["callee:00c585b0:8"]]
+ 004879d0 ["INT_ADD", "register:40f0:8", ["const:4879d0:8", "const:4:8"]]
+ 004879d0 ["CALL", null, ["callee:00c585b0:8"]]
- 00487990 bytes 08421f94
+ 004879d0 bytes f8421f94
- 004879bc ["INT_ADD", "register:40f0:8", ["const:4879bc:8", "const:4:8"]]
- 004879bc ["CALL", null, ["callee:00c57ee0:8"]]
+ 004879fc ["INT_ADD", "register:40f0:8", ["const:4879fc:8", "const:4:8"]]
+ 004879fc ["CALL", null, ["callee:00c57ee0:8"]]
- 004879bc bytes 49401f94
+ 004879fc bytes 39411f94
~~~


<a id="compare-61630f431b5fb75b6ad9e10ad266fa6c"></a>

### [`004879c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004879c0.md) → [`00487a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a00.md) FUN_00487a00

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00726780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726780.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c581c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c581c0.md)
- 新版 呼出元 1件 [`007267c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/007267c0.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c585c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004879e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004879c0.md#insn-004879e4) · [`004879f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004879c0.md#insn-004879f4) · [`00487a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004879c0.md#insn-00487a20)
- 新版 [`00487a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a00.md#insn-00487a24) · [`00487a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a00.md#insn-00487a34) · [`00487a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a00.md#insn-00487a60)

~~~diff
- 004879e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004879e4 ["INT_ADD", "register:40f0:8", ["const:4879e4:8", "const:4:8"]]
- 004879e4 ["CALLIND", null, ["register:0:8"]]
+ 00487a24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00487a24 ["INT_ADD", "register:40f0:8", ["const:487a24:8", "const:4:8"]]
+ 00487a24 ["CALLIND", null, ["register:0:8"]]
- 004879e4 bytes 00013fd6
+ 00487a24 bytes 00013fd6
- 004879f4 ["INT_ADD", "register:40f0:8", ["const:4879f4:8", "const:4:8"]]
- 004879f4 ["CALL", null, ["callee:00c585c0:8"]]
+ 00487a34 ["INT_ADD", "register:40f0:8", ["const:487a34:8", "const:4:8"]]
+ 00487a34 ["CALL", null, ["callee:00c585c0:8"]]
- 004879f4 bytes f3411f94
+ 00487a34 bytes e3421f94
- 00487a20 ["INT_ADD", "register:40f0:8", ["const:487a20:8", "const:4:8"]]
- 00487a20 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00487a60 ["INT_ADD", "register:40f0:8", ["const:487a60:8", "const:4:8"]]
+ 00487a60 ["CALL", null, ["callee:00c57ee0:8"]]
- 00487a20 bytes 30401f94
+ 00487a60 bytes 20411f94
~~~


<a id="compare-458ac5c4d38fabc72745a55469fd3ba3"></a>

### [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md) → [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md) FUN_00487a64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 63件 [`00444b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444b98.md) [`0046d0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d0e0.md) [`00470ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md) [`005b9b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9b14.md) [`005c62c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c62c0.md) · 呼出先 2件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 63件 [`00444bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444bd8.md) [`0046d120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d120.md) [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) [`005b9b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9b54.md) [`005c6300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c6/005c6300.md) · 呼出先 2件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00487a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md#insn-00487a40) · [`00487aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md#insn-00487aa4) · [`00487b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md#insn-00487b3c)
- 新版 [`00487a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md#insn-00487a80) · [`00487ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md#insn-00487ae4) · [`00487b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md#insn-00487b7c)

~~~diff
- 00487a40 ["COPY", "register:0:8", ["register:4048:8"]]
- 00487a40 ["INT_ADD", "register:40f0:8", ["const:487a40:8", "const:4:8"]]
- 00487a40 ["CALLIND", null, ["register:0:8"]]
+ 00487a80 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00487a80 ["INT_ADD", "register:40f0:8", ["const:487a80:8", "const:4:8"]]
+ 00487a80 ["CALLIND", null, ["register:0:8"]]
- 00487a40 bytes 20013fd6
+ 00487a80 bytes 20013fd6
- 00487aa4 ["INT_ADD", "register:40f0:8", ["const:487aa4:8", "const:4:8"]]
- 00487aa4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00487ae4 ["INT_ADD", "register:40f0:8", ["const:487ae4:8", "const:4:8"]]
+ 00487ae4 ["CALL", null, ["callee:00c57e90:8"]]
- 00487aa4 bytes fb3f1f94
+ 00487ae4 bytes eb401f94
- 00487b3c ["INT_ADD", "register:40f0:8", ["const:487b3c:8", "const:4:8"]]
- 00487b3c ["CALL", null, ["callee:0043b764:8"]]
+ 00487b7c ["INT_ADD", "register:40f0:8", ["const:487b7c:8", "const:4:8"]]
+ 00487b7c ["CALL", null, ["callee:0043b764:8"]]
- 00487b3c bytes facefe97
+ 00487b7c bytes facefe97
~~~


<a id="compare-1f351c7be27b7199fe7675255488c3e6"></a>

### [`00487b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487b40.md) → [`00487b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487b80.md) FUN_00487b80

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 29件 [`005bb344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bb344.md) [`005bbed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bbed4.md) [`005bc1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc1f8.md) [`005bc4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc4d8.md) [`005e57dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e5/005e57dc.md) · 呼出先 7件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b50.md)
- 新版 呼出元 29件 [`005bb384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bb/005bb384.md) [`005bbf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bb/005bbf14.md) [`005bc238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc238.md) [`005bc518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc518.md) [`005e581c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e5/005e581c.md) · 呼出先 7件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00487b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487b40.md#insn-00487b74) · [`00487b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487b40.md#insn-00487b90) · [`00487c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487b40.md#insn-00487c08)
- 新版 [`00487bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487b80.md#insn-00487bb4) · [`00487bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487b80.md#insn-00487bd0) · [`00487c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487b80.md#insn-00487c48)

~~~diff
- 00487b74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00487b74 ["INT_ADD", "register:40f0:8", ["const:487b74:8", "const:4:8"]]
- 00487b74 ["CALLIND", null, ["register:0:8"]]
+ 00487bb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00487bb4 ["INT_ADD", "register:40f0:8", ["const:487bb4:8", "const:4:8"]]
+ 00487bb4 ["CALLIND", null, ["register:0:8"]]
- 00487b74 bytes 00013fd6
+ 00487bb4 bytes 00013fd6
- 00487b90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00487b90 ["INT_ADD", "register:40f0:8", ["const:487b90:8", "const:4:8"]]
- 00487b90 ["CALLIND", null, ["register:0:8"]]
+ 00487bd0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00487bd0 ["INT_ADD", "register:40f0:8", ["const:487bd0:8", "const:4:8"]]
+ 00487bd0 ["CALLIND", null, ["register:0:8"]]
- 00487b90 bytes 00013fd6
+ 00487bd0 bytes 00013fd6
- 00487c08 ["INT_ADD", "register:40f0:8", ["const:487c08:8", "const:4:8"]]
- 00487c08 ["CALL", null, ["callee:00c57e90:8"]]
+ 00487c48 ["INT_ADD", "register:40f0:8", ["const:487c48:8", "const:4:8"]]
+ 00487c48 ["CALL", null, ["callee:00c57e90:8"]]
- 00487c08 bytes a23f1f94
+ 00487c48 bytes 92401f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8807599f831e10e26bccc1452b20031"></a>

### [`00487f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487f28.md) → [`00487f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487f68.md) FUN_00487f68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00488014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488014.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c581d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c581d0.md)
- 新版 呼出元 1件 [`00488054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488054.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c585d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00487f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487f28.md#insn-00487f50) · [`00487f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487f28.md#insn-00487f74) · [`00487fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487f28.md#insn-00487fcc)
- 新版 [`00487f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487f68.md#insn-00487f90) · [`00487fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487f68.md#insn-00487fb4) · [`0048800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487f68.md#insn-0048800c)

~~~diff
- 00487f50 ["INT_ADD", "register:40f0:8", ["const:487f50:8", "const:4:8"]]
- 00487f50 ["CALL", null, ["callee:00c585d0:8"]]
+ 00487f90 ["INT_ADD", "register:40f0:8", ["const:487f90:8", "const:4:8"]]
+ 00487f90 ["CALL", null, ["callee:00c585d0:8"]]
- 00487f50 bytes a0401f94
+ 00487f90 bytes 90411f94
- 00487f74 ["INT_ADD", "register:40f0:8", ["const:487f74:8", "const:4:8"]]
- 00487f74 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00487fb4 ["INT_ADD", "register:40f0:8", ["const:487fb4:8", "const:4:8"]]
+ 00487fb4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00487f74 bytes cf3e1f94
+ 00487fb4 bytes bf3f1f94
- 00487fcc ["INT_ADD", "register:40f0:8", ["const:487fcc:8", "const:4:8"]]
- 00487fcc ["CALL", null, ["callee:00c582a0:8"]]
+ 0048800c ["INT_ADD", "register:40f0:8", ["const:48800c:8", "const:4:8"]]
+ 0048800c ["CALL", null, ["callee:00c582a0:8"]]
- 00487fcc bytes b53f1f94
+ 0048800c bytes a5401f94
~~~


<a id="compare-5791c3264f92abcb012938d68e01c4ba"></a>

### [`00488014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488014.md) → [`00488054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488054.md) FUN_00488054

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`0043d73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043d73c.md) [`00470ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md) [`00488750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488750.md) [`00a37f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37f10.md) [`00b10cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10cc4.md) · 呼出先 4件 [`00487f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487f28.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md)
- 新版 呼出元 5件 [`0043d77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043d77c.md) [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) [`00488790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488790.md) [`00a38108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38108.md) [`00b110ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b110ec.md) · 呼出先 4件 [`00487f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487f68.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00488050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488014.md#insn-00488050) · [`0048805c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488014.md#insn-0048805c) · [`0048806c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488014.md#insn-0048806c)
- 新版 [`00488090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488054.md#insn-00488090) · [`0048809c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488054.md#insn-0048809c) · [`004880ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488054.md#insn-004880ac)

~~~diff
- 00488050 ["COPY", "register:0:8", ["register:4048:8"]]
- 00488050 ["INT_ADD", "register:40f0:8", ["const:488050:8", "const:4:8"]]
- 00488050 ["CALLIND", null, ["register:0:8"]]
+ 00488090 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00488090 ["INT_ADD", "register:40f0:8", ["const:488090:8", "const:4:8"]]
+ 00488090 ["CALLIND", null, ["register:0:8"]]
- 00488050 bytes 20013fd6
+ 00488090 bytes 20013fd6
- 0048805c ["INT_ADD", "register:40f0:8", ["const:48805c:8", "const:4:8"]]
- 0048805c ["CALL", null, ["callee:00487f68:8"]]
+ 0048809c ["INT_ADD", "register:40f0:8", ["const:48809c:8", "const:4:8"]]
+ 0048809c ["CALL", null, ["callee:00487f68:8"]]
- 0048805c bytes b3ffff97
+ 0048809c bytes b3ffff97
- 0048806c ["INT_ADD", "register:40f0:8", ["const:48806c:8", "const:4:8"]]
- 0048806c ["CALL", null, ["callee:00c57eb0:8"]]
+ 004880ac ["INT_ADD", "register:40f0:8", ["const:4880ac:8", "const:4:8"]]
+ 004880ac ["CALL", null, ["callee:00c57eb0:8"]]
- 0048806c bytes 913e1f94
+ 004880ac bytes 813f1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3207b1b53a2695e483e559a0dab5857"></a>

### [`00488138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488138.md) → [`00488178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488178.md) FUN_00488178

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 14件 [`0043d73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043d73c.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md) [`0046f074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md) [`0047aed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047aed0.md) [`00489184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489184.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md)
- 新版 呼出元 14件 [`0043d77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043d77c.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) [`0046f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md) [`0047af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047af10.md) [`004891c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004891c4.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00488180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488138.md#insn-00488180) · [`004881cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488138.md#insn-004881cc) · [`00488228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488138.md#insn-00488228)
- 新版 [`004881c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488178.md#insn-004881c0) · [`0048820c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488178.md#insn-0048820c) · [`00488268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488178.md#insn-00488268)

~~~diff
- 00488180 ["INT_ADD", "register:40f0:8", ["const:488180:8", "const:4:8"]]
- 00488180 ["CALL", null, ["callee:00c57fd0:8"]]
+ 004881c0 ["INT_ADD", "register:40f0:8", ["const:4881c0:8", "const:4:8"]]
+ 004881c0 ["CALL", null, ["callee:00c57fd0:8"]]
- 00488180 bytes 943e1f94
+ 004881c0 bytes 843f1f94
- 004881cc ["INT_ADD", "register:40f0:8", ["const:4881cc:8", "const:4:8"]]
- 004881cc ["CALL", null, ["callee:00c57fd0:8"]]
+ 0048820c ["INT_ADD", "register:40f0:8", ["const:48820c:8", "const:4:8"]]
+ 0048820c ["CALL", null, ["callee:00c57fd0:8"]]
- 004881cc bytes 813e1f94
+ 0048820c bytes 713f1f94
- 00488228 ["INT_ADD", "register:40f0:8", ["const:488228:8", "const:4:8"]]
- 00488228 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00488268 ["INT_ADD", "register:40f0:8", ["const:488268:8", "const:4:8"]]
+ 00488268 ["CALL", null, ["callee:00c57ee0:8"]]
- 00488228 bytes 2e3e1f94
+ 00488268 bytes 1e3f1f94
~~~


<a id="compare-a59a0f42eb32f61b6ae934e43ce8d256"></a>

### [`0048822c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/0048822c.md) → [`0048826c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/0048826c.md) FUN_0048826c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 15件 [`005c62c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c62c0.md) [`0063dcd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063dcd0.md) [`00677a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00677/00677a00.md) [`0080b7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b7e4.md) [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) · 呼出先 2件 [`004882ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/004882ac.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 15件 [`005c6300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c6/005c6300.md) [`0063dd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063d/0063dd10.md) [`00677a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00677/00677a40.md) [`0080b824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b824.md) [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) · 呼出先 2件 [`004882ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004882ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00488264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/0048822c.md#insn-00488264) · [`0048827c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/0048822c.md#insn-0048827c) · [`004882a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/0048822c.md#insn-004882a8)
- 新版 [`004882a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/0048826c.md#insn-004882a4) · [`004882bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/0048826c.md#insn-004882bc) · [`004882e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/0048826c.md#insn-004882e8)

~~~diff
- 00488264 ["COPY", "register:0:8", ["register:4040:8"]]
- 00488264 ["INT_ADD", "register:40f0:8", ["const:488264:8", "const:4:8"]]
- 00488264 ["CALLIND", null, ["register:0:8"]]
+ 004882a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004882a4 ["INT_ADD", "register:40f0:8", ["const:4882a4:8", "const:4:8"]]
+ 004882a4 ["CALLIND", null, ["register:0:8"]]
- 00488264 bytes 00013fd6
+ 004882a4 bytes 00013fd6
- 0048827c ["INT_ADD", "register:40f0:8", ["const:48827c:8", "const:4:8"]]
- 0048827c ["CALL", null, ["callee:004882ec:8"]]
+ 004882bc ["INT_ADD", "register:40f0:8", ["const:4882bc:8", "const:4:8"]]
+ 004882bc ["CALL", null, ["callee:004882ec:8"]]
- 0048827c bytes 0c000094
+ 004882bc bytes 0c000094
- 004882a8 ["INT_ADD", "register:40f0:8", ["const:4882a8:8", "const:4:8"]]
- 004882a8 ["CALL", null, ["callee:00c57ee0:8"]]
+ 004882e8 ["INT_ADD", "register:40f0:8", ["const:4882e8:8", "const:4:8"]]
+ 004882e8 ["CALL", null, ["callee:00c57ee0:8"]]
- 004882a8 bytes 0e3e1f94
+ 004882e8 bytes fe3e1f94
~~~


<a id="compare-fd91f490cbec1f5bf171dd9fd217c927"></a>

### [`004882ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/004882ac.md) → [`004882ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004882ec.md) FUN_004882ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0048822c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/0048822c.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00488d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488d84.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md)
- 新版 呼出元 1件 [`0048826c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/0048826c.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00488dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488dc4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004882fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/004882ac.md#insn-004882fc) · [`00488368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/004882ac.md#insn-00488368) · [`00488394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/004882ac.md#insn-00488394)
- 新版 [`0048833c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004882ec.md#insn-0048833c) · [`004883a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004882ec.md#insn-004883a8) · [`004883d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004882ec.md#insn-004883d4)

~~~diff
- 004882fc ["INT_ADD", "register:40f0:8", ["const:4882fc:8", "const:4:8"]]
- 004882fc ["CALL", null, ["callee:00c57fd0:8"]]
+ 0048833c ["INT_ADD", "register:40f0:8", ["const:48833c:8", "const:4:8"]]
+ 0048833c ["CALL", null, ["callee:00c57fd0:8"]]
- 004882fc bytes 353e1f94
+ 0048833c bytes 253f1f94
- 00488368 ["INT_ADD", "register:40f0:8", ["const:488368:8", "const:4:8"]]
- 00488368 ["CALL", null, ["callee:00c57e90:8"]]
+ 004883a8 ["INT_ADD", "register:40f0:8", ["const:4883a8:8", "const:4:8"]]
+ 004883a8 ["CALL", null, ["callee:00c57e90:8"]]
- 00488368 bytes ca3d1f94
+ 004883a8 bytes ba3e1f94
- 00488394 ["INT_ADD", "register:40f0:8", ["const:488394:8", "const:4:8"]]
- 00488394 ["CALL", null, ["callee:00c58000:8"]]
+ 004883d4 ["INT_ADD", "register:40f0:8", ["const:4883d4:8", "const:4:8"]]
+ 004883d4 ["CALL", null, ["callee:00c58000:8"]]
- 00488394 bytes 1b3e1f94
+ 004883d4 bytes 0b3f1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-133edbccd1387340ce645b00790582d1"></a>

### [`004883f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/004883f4.md) → [`00488434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488434.md) FUN_00488434

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 28件 [`005e94b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e9/005e94b4.md) [`00662db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/00662db4.md) [`00668db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00668/00668db0.md) [`00685aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685aa4.md) [`006a3d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a3/006a3d84.md) · 呼出先 2件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 28件 [`005e94f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e9/005e94f4.md) [`00662df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/00662df4.md) [`00668df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00668/00668df0.md) [`00685ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685ae4.md) [`006a3dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a3/006a3dc4.md) · 呼出先 2件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00488474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/004883f4.md#insn-00488474) · [`00488514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/004883f4.md#insn-00488514)
- 新版 [`004884b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488434.md#insn-004884b4) · [`00488554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488434.md#insn-00488554)

~~~diff
- 00488474 ["INT_ADD", "register:40f0:8", ["const:488474:8", "const:4:8"]]
- 00488474 ["CALL", null, ["callee:00c57e90:8"]]
+ 004884b4 ["INT_ADD", "register:40f0:8", ["const:4884b4:8", "const:4:8"]]
+ 004884b4 ["CALL", null, ["callee:00c57e90:8"]]
- 00488474 bytes 873d1f94
+ 004884b4 bytes 773e1f94
- 00488514 ["INT_ADD", "register:40f0:8", ["const:488514:8", "const:4:8"]]
- 00488514 ["CALL", null, ["callee:0043b764:8"]]
+ 00488554 ["INT_ADD", "register:40f0:8", ["const:488554:8", "const:4:8"]]
+ 00488554 ["CALL", null, ["callee:0043b764:8"]]
- 00488514 bytes 84ccfe97
+ 00488554 bytes 84ccfe97
~~~


<a id="compare-ab2f1355598482c9d71be0b3f64c4057"></a>

### [`00488564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488564.md) → [`004885a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004885a4.md) FUN_004885a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048858c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488564.md#insn-0048858c) · [`004885ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488564.md#insn-004885ac) · [`004885bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488564.md#insn-004885bc)
- 新版 [`004885cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004885a4.md#insn-004885cc) · [`004885ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004885a4.md#insn-004885ec) · [`004885fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004885a4.md#insn-004885fc)

~~~diff
- 0048858c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048858c ["INT_ADD", "register:40f0:8", ["const:48858c:8", "const:4:8"]]
- 0048858c ["CALLIND", null, ["register:0:8"]]
+ 004885cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004885cc ["INT_ADD", "register:40f0:8", ["const:4885cc:8", "const:4:8"]]
+ 004885cc ["CALLIND", null, ["register:0:8"]]
- 0048858c bytes 00013fd6
+ 004885cc bytes 00013fd6
- 004885ac ["COPY", "register:0:8", ["register:4040:8"]]
- 004885ac ["INT_ADD", "register:40f0:8", ["const:4885ac:8", "const:4:8"]]
- 004885ac ["CALLIND", null, ["register:0:8"]]
+ 004885ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 004885ec ["INT_ADD", "register:40f0:8", ["const:4885ec:8", "const:4:8"]]
+ 004885ec ["CALLIND", null, ["register:0:8"]]
- 004885ac bytes 00013fd6
+ 004885ec bytes 00013fd6
- 004885bc ["INT_ADD", "register:40f0:8", ["const:4885bc:8", "const:4:8"]]
- 004885bc ["CALL", null, ["callee:00c57eb0:8"]]
+ 004885fc ["INT_ADD", "register:40f0:8", ["const:4885fc:8", "const:4:8"]]
+ 004885fc ["CALL", null, ["callee:00c57eb0:8"]]
- 004885bc bytes 3d3d1f94
+ 004885fc bytes 2d3e1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1714e446791ac9ca3b63ee3f18b77ee"></a>

### [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md) → [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md) FUN_00488658

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 144件 [`0043d73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043d73c.md) [`00444b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444b98.md) [`00444de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) [`0046d0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d0e0.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md) · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md)
- 新版 呼出元 144件 [`0043d77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043d77c.md) [`00444bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444bd8.md) [`00444e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444e20.md) [`0046d120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d120.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) · 呼出先 1件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00488638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md#insn-00488638)
- 新版 [`00488678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md#insn-00488678)

~~~diff
- 00488638 ["INT_ADD", "register:40f0:8", ["const:488638:8", "const:4:8"]]
- 00488638 ["CALL", null, ["callee:00c582a0:8"]]
+ 00488678 ["INT_ADD", "register:40f0:8", ["const:488678:8", "const:4:8"]]
+ 00488678 ["CALL", null, ["callee:00c582a0:8"]]
- 00488638 bytes 1a3e1f94
+ 00488678 bytes 0a3f1f94
~~~


<a id="compare-fdf246f69970a3fae26bd9698294996d"></a>

### [`00488684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488684.md) → [`004886c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004886c4.md) FUN_004886c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00550cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550cf8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57db0.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00550d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550d38.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c581b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581b0.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004886c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488684.md#insn-004886c4) · [`004886d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488684.md#insn-004886d0) · [`004886e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488684.md#insn-004886e0)
- 新版 [`00488704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004886c4.md#insn-00488704) · [`00488710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004886c4.md#insn-00488710) · [`00488720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004886c4.md#insn-00488720)

~~~diff
- 004886c4 ["INT_ADD", "register:40f0:8", ["const:4886c4:8", "const:4:8"]]
- 004886c4 ["CALL", null, ["callee:00c581b0:8"]]
+ 00488704 ["INT_ADD", "register:40f0:8", ["const:488704:8", "const:4:8"]]
+ 00488704 ["CALL", null, ["callee:00c581b0:8"]]
- 004886c4 bytes bb3d1f94
+ 00488704 bytes ab3e1f94
- 004886d0 ["INT_ADD", "register:40f0:8", ["const:4886d0:8", "const:4:8"]]
- 004886d0 ["CALL", null, ["callee:00550d38:8"]]
+ 00488710 ["INT_ADD", "register:40f0:8", ["const:488710:8", "const:4:8"]]
+ 00488710 ["CALL", null, ["callee:00550d38:8"]]
- 004886d0 bytes 8a210394
+ 00488710 bytes 8a210394
- 004886e0 ["INT_ADD", "register:40f0:8", ["const:4886e0:8", "const:4:8"]]
- 004886e0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00488720 ["INT_ADD", "register:40f0:8", ["const:488720:8", "const:4:8"]]
+ 00488720 ["CALL", null, ["callee:00c57eb0:8"]]
- 004886e0 bytes f43c1f94
+ 00488720 bytes e43d1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-373d5560d0fe9664b288dccd7f0e48df"></a>

### [`00488d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488d60.md) → [`00488da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488da0.md) FUN_00488da0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00488c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488c88.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00488cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488cc8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00488d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488d60.md#insn-00488d70)
- 新版 [`00488db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488da0.md#insn-00488db0)

~~~diff
- 00488d70 ["INT_ADD", "register:40f0:8", ["const:488d70:8", "const:4:8"]]
- 00488d70 ["CALL", null, ["callee:00488cc8:8"]]
+ 00488db0 ["INT_ADD", "register:40f0:8", ["const:488db0:8", "const:4:8"]]
+ 00488db0 ["CALL", null, ["callee:00488cc8:8"]]
- 00488d70 bytes c6ffff97
+ 00488db0 bytes c6ffff97
~~~


<a id="compare-c42f4ab8025dceac0214b6c99782e714"></a>

### [`00489154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489154.md) → [`00489194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489194.md) FUN_00489194

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`00629d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00629/00629d80.md) [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) · 呼出先 2件 [`00489184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489184.md) [`00489468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489468.md)
- 新版 呼出元 3件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`00629dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00629/00629dc0.md) [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) · 呼出先 2件 [`004891c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004891c4.md) [`004894a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004894a8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00489164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489154.md#insn-00489164) · [`00489170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489154.md#insn-00489170)
- 新版 [`004891a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489194.md#insn-004891a4) · [`004891b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489194.md#insn-004891b0)

~~~diff
- 00489164 ["INT_ADD", "register:40f0:8", ["const:489164:8", "const:4:8"]]
- 00489164 ["CALL", null, ["callee:004891c4:8"]]
+ 004891a4 ["INT_ADD", "register:40f0:8", ["const:4891a4:8", "const:4:8"]]
+ 004891a4 ["CALL", null, ["callee:004891c4:8"]]
- 00489164 bytes 08000094
+ 004891a4 bytes 08000094
- 00489170 ["INT_ADD", "register:40f0:8", ["const:489170:8", "const:4:8"]]
- 00489170 ["CALL", null, ["callee:004894a8:8"]]
+ 004891b0 ["INT_ADD", "register:40f0:8", ["const:4891b0:8", "const:4:8"]]
+ 004891b0 ["CALL", null, ["callee:004894a8:8"]]
- 00489170 bytes be000094
+ 004891b0 bytes be000094
~~~


<a id="compare-db79f231cf3e9d03dd551bab5036f3d1"></a>

### [`00489468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489468.md) → [`004894a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004894a8.md) FUN_004894a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`00489154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489154.md) [`0048a7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a7c8.md) [`0048abe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048abe0.md) [`00498190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498190.md) [`0049ace4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ace4.md) · 呼出先 6件 [`0055c320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c320.md) [`0055e5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e5d4.md) [`0055e5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e5dc.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 6件 [`00489194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489194.md) [`0048a808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a808.md) [`0048ac20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ac20.md) [`004981d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004981d0.md) [`0049ad24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049ad24.md) · 呼出先 6件 [`0055c360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c360.md) [`0055e614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e614.md) [`0055e61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e61c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00489498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489468.md#insn-00489498) · [`004894b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489468.md#insn-004894b8) · [`004894cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489468.md#insn-004894cc)
- 新版 [`004894d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004894a8.md#insn-004894d8) · [`004894f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004894a8.md#insn-004894f8) · [`0048950c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004894a8.md#insn-0048950c)

~~~diff
- 00489498 ["INT_ADD", "register:40f0:8", ["const:489498:8", "const:4:8"]]
- 00489498 ["CALL", null, ["callee:0055c360:8"]]
+ 004894d8 ["INT_ADD", "register:40f0:8", ["const:4894d8:8", "const:4:8"]]
+ 004894d8 ["CALL", null, ["callee:0055c360:8"]]
- 00489498 bytes a24b0394
+ 004894d8 bytes a24b0394
- 004894b8 ["INT_ADD", "register:40f0:8", ["const:4894b8:8", "const:4:8"]]
- 004894b8 ["CALL", null, ["callee:00c53d00:8"]]
+ 004894f8 ["INT_ADD", "register:40f0:8", ["const:4894f8:8", "const:4:8"]]
+ 004894f8 ["CALL", null, ["callee:00c53d00:8"]]
- 004894b8 bytes 0a291f94
+ 004894f8 bytes 022a1f94
- 004894cc ["COPY", "register:0:8", ["register:4040:8"]]
- 004894cc ["INT_ADD", "register:40f0:8", ["const:4894cc:8", "const:4:8"]]
- 004894cc ["CALLIND", null, ["register:0:8"]]
+ 0048950c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048950c ["INT_ADD", "register:40f0:8", ["const:48950c:8", "const:4:8"]]
+ 0048950c ["CALLIND", null, ["register:0:8"]]
- 004894cc bytes 00013fd6
+ 0048950c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08325a6f493f4446781f5595d988727a"></a>

### [`00489584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489584.md) → [`004895c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004895c4.md) FUN_004895c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00489184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489184.md) [`00489e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489e5c.md) [`00498190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498190.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 3件 [`004891c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004891c4.md) [`00489e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489e9c.md) [`004981d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004981d0.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004895b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489584.md#insn-004895b0) · [`004895c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489584.md#insn-004895c4) · [`004895cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489584.md#insn-004895cc)
- 新版 [`004895f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004895c4.md#insn-004895f0) · [`00489604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004895c4.md#insn-00489604) · [`0048960c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004895c4.md#insn-0048960c)

~~~diff
- 004895b0 ["INT_ADD", "register:40f0:8", ["const:4895b0:8", "const:4:8"]]
- 004895b0 ["CALL", null, ["callee:00c53d00:8"]]
+ 004895f0 ["INT_ADD", "register:40f0:8", ["const:4895f0:8", "const:4:8"]]
+ 004895f0 ["CALL", null, ["callee:00c53d00:8"]]
- 004895b0 bytes cc281f94
+ 004895f0 bytes c4291f94
- 004895c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004895c4 ["INT_ADD", "register:40f0:8", ["const:4895c4:8", "const:4:8"]]
- 004895c4 ["CALLIND", null, ["register:0:8"]]
+ 00489604 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00489604 ["INT_ADD", "register:40f0:8", ["const:489604:8", "const:4:8"]]
+ 00489604 ["CALLIND", null, ["register:0:8"]]
- 004895c4 bytes 00013fd6
+ 00489604 bytes 00013fd6
- 004895cc ["INT_ADD", "register:40f0:8", ["const:4895cc:8", "const:4:8"]]
- 004895cc ["CALL", null, ["callee:00c57e80:8"]]
+ 0048960c ["INT_ADD", "register:40f0:8", ["const:48960c:8", "const:4:8"]]
+ 0048960c ["CALL", null, ["callee:00c57e80:8"]]
- 004895cc bytes 2d391f94
+ 0048960c bytes 1d3a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b37dbfcc2cf813fc3644f1435cccbfa8"></a>

### [`00489e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489e0c.md) → [`00489e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489e4c.md) FUN_00489e4c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00489e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489e0c.md#insn-00489e28) · [`00489e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489e0c.md#insn-00489e48)
- 新版 [`00489e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489e4c.md#insn-00489e68) · [`00489e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489e4c.md#insn-00489e88)

~~~diff
- 00489e28 ["INT_ADD", "register:40f0:8", ["const:489e28:8", "const:4:8"]]
- 00489e28 ["CALL", null, ["callee:00c53d00:8"]]
+ 00489e68 ["INT_ADD", "register:40f0:8", ["const:489e68:8", "const:4:8"]]
+ 00489e68 ["CALL", null, ["callee:00c53d00:8"]]
- 00489e28 bytes ae261f94
+ 00489e68 bytes a6271f94
- 00489e48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00489e48 ["INT_ADD", "register:40f0:8", ["const:489e48:8", "const:4:8"]]
- 00489e48 ["CALLIND", null, ["register:0:8"]]
+ 00489e88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00489e88 ["INT_ADD", "register:40f0:8", ["const:489e88:8", "const:4:8"]]
+ 00489e88 ["CALLIND", null, ["register:0:8"]]
- 00489e48 bytes 00013fd6
+ 00489e88 bytes 00013fd6
~~~


<a id="compare-6d4fad57ae33d9763f762aebb9613f00"></a>

### [`00489e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489e5c.md) → [`00489e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489e9c.md) FUN_00489e9c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a992ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a99/00a992ac.md) · 呼出先 7件 [`00489584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489584.md) [`0055e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e5cc.md) [`0055e5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e5d4.md) [`0055e5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e5dc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 1件 [`00a994a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a99/00a994a4.md) · 呼出先 7件 [`004895c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004895c4.md) [`0055e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e60c.md) [`0055e614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e614.md) [`0055e61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e61c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00489e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489e5c.md#insn-00489e78) · [`00489e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489e5c.md#insn-00489e8c) · [`00489ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489e5c.md#insn-00489ea4)
- 新版 [`00489eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489e9c.md#insn-00489eb8) · [`00489ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489e9c.md#insn-00489ecc) · [`00489ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489e9c.md#insn-00489ee4)

~~~diff
- 00489e78 ["INT_ADD", "register:40f0:8", ["const:489e78:8", "const:4:8"]]
- 00489e78 ["CALL", null, ["callee:004895c4:8"]]
+ 00489eb8 ["INT_ADD", "register:40f0:8", ["const:489eb8:8", "const:4:8"]]
+ 00489eb8 ["CALL", null, ["callee:004895c4:8"]]
- 00489e78 bytes c3fdff97
+ 00489eb8 bytes c3fdff97
- 00489e8c ["INT_ADD", "register:40f0:8", ["const:489e8c:8", "const:4:8"]]
- 00489e8c ["CALL", null, ["callee:00c53cd0:8"]]
+ 00489ecc ["INT_ADD", "register:40f0:8", ["const:489ecc:8", "const:4:8"]]
+ 00489ecc ["CALL", null, ["callee:00c53cd0:8"]]
- 00489e8c bytes 89261f94
+ 00489ecc bytes 81271f94
- 00489ea4 ["INT_ADD", "register:40f0:8", ["const:489ea4:8", "const:4:8"]]
- 00489ea4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00489ee4 ["INT_ADD", "register:40f0:8", ["const:489ee4:8", "const:4:8"]]
+ 00489ee4 ["CALL", null, ["callee:00c53d00:8"]]
- 00489ea4 bytes 8f261f94
+ 00489ee4 bytes 87271f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdcef8d4affb592745cf013fad31bc27"></a>

### [`0048a650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a650.md) → [`0048a690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a690.md) FUN_0048a690

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00489f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f30.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00489f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f70.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048a67c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a650.md#insn-0048a67c) · [`0048a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a650.md#insn-0048a690) · [`0048a698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a650.md#insn-0048a698)
- 新版 [`0048a6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a690.md#insn-0048a6bc) · [`0048a6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a690.md#insn-0048a6d0) · [`0048a6d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a690.md#insn-0048a6d8)

~~~diff
- 0048a67c ["INT_ADD", "register:40f0:8", ["const:48a67c:8", "const:4:8"]]
- 0048a67c ["CALL", null, ["callee:00c53d00:8"]]
+ 0048a6bc ["INT_ADD", "register:40f0:8", ["const:48a6bc:8", "const:4:8"]]
+ 0048a6bc ["CALL", null, ["callee:00c53d00:8"]]
- 0048a67c bytes 99241f94
+ 0048a6bc bytes 91251f94
- 0048a690 ["COPY", "register:0:8", ["register:4040:8"]]
- 0048a690 ["INT_ADD", "register:40f0:8", ["const:48a690:8", "const:4:8"]]
- 0048a690 ["CALLIND", null, ["register:0:8"]]
+ 0048a6d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048a6d0 ["INT_ADD", "register:40f0:8", ["const:48a6d0:8", "const:4:8"]]
+ 0048a6d0 ["CALLIND", null, ["register:0:8"]]
- 0048a690 bytes 00013fd6
+ 0048a6d0 bytes 00013fd6
- 0048a698 ["INT_ADD", "register:40f0:8", ["const:48a698:8", "const:4:8"]]
- 0048a698 ["CALL", null, ["callee:00c57e80:8"]]
+ 0048a6d8 ["INT_ADD", "register:40f0:8", ["const:48a6d8:8", "const:4:8"]]
+ 0048a6d8 ["CALL", null, ["callee:00c57e80:8"]]
- 0048a698 bytes fa341f94
+ 0048a6d8 bytes ea351f94
~~~


<a id="compare-cf215193df388eec419a739db2921cd4"></a>

### [`0048a6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a6ac.md) → [`0048a6ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a6ec.md) FUN_0048a6ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00489f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f30.md) [`00590cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590cd8.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`00489f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f70.md) [`00590d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590d18.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048a6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a6ac.md#insn-0048a6c8) · [`0048a6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a6ac.md#insn-0048a6e8)
- 新版 [`0048a708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a6ec.md#insn-0048a708) · [`0048a728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a6ec.md#insn-0048a728)

~~~diff
- 0048a6c8 ["INT_ADD", "register:40f0:8", ["const:48a6c8:8", "const:4:8"]]
- 0048a6c8 ["CALL", null, ["callee:00c53d00:8"]]
+ 0048a708 ["INT_ADD", "register:40f0:8", ["const:48a708:8", "const:4:8"]]
+ 0048a708 ["CALL", null, ["callee:00c53d00:8"]]
- 0048a6c8 bytes 86241f94
+ 0048a708 bytes 7e251f94
- 0048a6e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0048a6e8 ["INT_ADD", "register:40f0:8", ["const:48a6e8:8", "const:4:8"]]
- 0048a6e8 ["CALLIND", null, ["register:0:8"]]
+ 0048a728 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048a728 ["INT_ADD", "register:40f0:8", ["const:48a728:8", "const:4:8"]]
+ 0048a728 ["CALLIND", null, ["register:0:8"]]
- 0048a6e8 bytes 00013fd6
+ 0048a728 bytes 00013fd6
~~~


<a id="compare-6845bc112cfa28fafb0858e2d87fddb0"></a>

### [`0048a7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a7c8.md) → [`0048a808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a808.md) FUN_0048a808

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) · 呼出先 2件 [`00489468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489468.md) [`0048a7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a7f4.md)
- 新版 呼出元 2件 [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) · 呼出先 2件 [`004894a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004894a8.md) [`0048a834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a834.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048a7d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a7c8.md#insn-0048a7d8) · [`0048a7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a7c8.md#insn-0048a7e0)
- 新版 [`0048a818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a808.md#insn-0048a818) · [`0048a820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a808.md#insn-0048a820)

~~~diff
- 0048a7d8 ["INT_ADD", "register:40f0:8", ["const:48a7d8:8", "const:4:8"]]
- 0048a7d8 ["CALL", null, ["callee:0048a834:8"]]
+ 0048a818 ["INT_ADD", "register:40f0:8", ["const:48a818:8", "const:4:8"]]
+ 0048a818 ["CALL", null, ["callee:0048a834:8"]]
- 0048a7d8 bytes 07000094
+ 0048a818 bytes 07000094
- 0048a7e0 ["INT_ADD", "register:40f0:8", ["const:48a7e0:8", "const:4:8"]]
- 0048a7e0 ["CALL", null, ["callee:004894a8:8"]]
+ 0048a820 ["INT_ADD", "register:40f0:8", ["const:48a820:8", "const:4:8"]]
+ 0048a820 ["CALL", null, ["callee:004894a8:8"]]
- 0048a7e0 bytes 22fbff97
+ 0048a820 bytes 22fbff97
~~~


<a id="compare-19cf1018a25254e6d68161359b03323a"></a>

### [`0048aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aa10.md) → [`0048aa50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aa50.md) FUN_0048aa50

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0048abe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048abe0.md) [`0086b194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b194.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`0048ac20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ac20.md) [`0086b1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b1d4.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048aa58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aa10.md#insn-0048aa58) · [`0048aa78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aa10.md#insn-0048aa78) · [`0048aa8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aa10.md#insn-0048aa8c)
- 新版 [`0048aa98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aa50.md#insn-0048aa98) · [`0048aab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aa50.md#insn-0048aab8) · [`0048aacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aa50.md#insn-0048aacc)

~~~diff
- 0048aa58 ["COPY", "register:0:8", ["register:4048:8"]]
- 0048aa58 ["INT_ADD", "register:40f0:8", ["const:48aa58:8", "const:4:8"]]
- 0048aa58 ["CALLIND", null, ["register:0:8"]]
+ 0048aa98 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0048aa98 ["INT_ADD", "register:40f0:8", ["const:48aa98:8", "const:4:8"]]
+ 0048aa98 ["CALLIND", null, ["register:0:8"]]
- 0048aa58 bytes 20013fd6
+ 0048aa98 bytes 20013fd6
- 0048aa78 ["INT_ADD", "register:40f0:8", ["const:48aa78:8", "const:4:8"]]
- 0048aa78 ["CALL", null, ["callee:00c53d00:8"]]
+ 0048aab8 ["INT_ADD", "register:40f0:8", ["const:48aab8:8", "const:4:8"]]
+ 0048aab8 ["CALL", null, ["callee:00c53d00:8"]]
- 0048aa78 bytes 9a231f94
+ 0048aab8 bytes 92241f94
- 0048aa8c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048aa8c ["INT_ADD", "register:40f0:8", ["const:48aa8c:8", "const:4:8"]]
- 0048aa8c ["CALLIND", null, ["register:0:8"]]
+ 0048aacc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048aacc ["INT_ADD", "register:40f0:8", ["const:48aacc:8", "const:4:8"]]
+ 0048aacc ["CALLIND", null, ["register:0:8"]]
- 0048aa8c bytes 00013fd6
+ 0048aacc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec4cf6f0a61e3c8d1fc585f793e95db3"></a>

### [`0048ac50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ac50.md) → [`0048ac90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ac90.md) FUN_0048ac90

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00468cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468cc8.md) · 呼出先 6件 [`0046c178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c178.md) [`0046c1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c1f0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md) · 呼出先 6件 [`0046c1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c1b8.md) [`0046c230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c230.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048adf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ac50.md#insn-0048adf4) · [`0048ae00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ac50.md#insn-0048ae00) · [`0048ae14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ac50.md#insn-0048ae14)
- 新版 [`0048ae34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ac90.md#insn-0048ae34) · [`0048ae40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ac90.md#insn-0048ae40) · [`0048ae54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ac90.md#insn-0048ae54)

~~~diff
- 0048adf4 ["INT_ADD", "register:40f0:8", ["const:48adf4:8", "const:4:8"]]
- 0048adf4 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0048ae34 ["INT_ADD", "register:40f0:8", ["const:48ae34:8", "const:4:8"]]
+ 0048ae34 ["CALL", null, ["callee:00c53cd0:8"]]
- 0048adf4 bytes af221f94
+ 0048ae34 bytes a7231f94
- 0048ae00 ["INT_ADD", "register:40f0:8", ["const:48ae00:8", "const:4:8"]]
- 0048ae00 ["CALL", null, ["callee:0046c1b8:8"]]
+ 0048ae40 ["INT_ADD", "register:40f0:8", ["const:48ae40:8", "const:4:8"]]
+ 0048ae40 ["CALL", null, ["callee:0046c1b8:8"]]
- 0048ae00 bytes de84ff97
+ 0048ae40 bytes de84ff97
- 0048ae14 ["INT_ADD", "register:40f0:8", ["const:48ae14:8", "const:4:8"]]
- 0048ae14 ["CALL", null, ["callee:00c53d00:8"]]
+ 0048ae54 ["INT_ADD", "register:40f0:8", ["const:48ae54:8", "const:4:8"]]
+ 0048ae54 ["CALL", null, ["callee:00c53d00:8"]]
- 0048ae14 bytes b3221f94
+ 0048ae54 bytes ab231f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4850179d894495e6f7c81dc8cb726c0"></a>

### [`0048ae98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ae98.md) → [`0048aed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aed8.md) FUN_0048aed8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00468de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468de0.md) · 呼出先 6件 [`0046c178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c178.md) [`0046c1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c1f0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00468e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468e20.md) · 呼出先 6件 [`0046c1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c1b8.md) [`0046c230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c230.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048aff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ae98.md#insn-0048aff8) · [`0048b004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ae98.md#insn-0048b004) · [`0048b018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ae98.md#insn-0048b018)
- 新版 [`0048b038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aed8.md#insn-0048b038) · [`0048b044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aed8.md#insn-0048b044) · [`0048b058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aed8.md#insn-0048b058)

~~~diff
- 0048aff8 ["INT_ADD", "register:40f0:8", ["const:48aff8:8", "const:4:8"]]
- 0048aff8 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0048b038 ["INT_ADD", "register:40f0:8", ["const:48b038:8", "const:4:8"]]
+ 0048b038 ["CALL", null, ["callee:00c53cd0:8"]]
- 0048aff8 bytes 2e221f94
+ 0048b038 bytes 26231f94
- 0048b004 ["INT_ADD", "register:40f0:8", ["const:48b004:8", "const:4:8"]]
- 0048b004 ["CALL", null, ["callee:0046c1b8:8"]]
+ 0048b044 ["INT_ADD", "register:40f0:8", ["const:48b044:8", "const:4:8"]]
+ 0048b044 ["CALL", null, ["callee:0046c1b8:8"]]
- 0048b004 bytes 5d84ff97
+ 0048b044 bytes 5d84ff97
- 0048b018 ["INT_ADD", "register:40f0:8", ["const:48b018:8", "const:4:8"]]
- 0048b018 ["CALL", null, ["callee:00c53d00:8"]]
+ 0048b058 ["INT_ADD", "register:40f0:8", ["const:48b058:8", "const:4:8"]]
+ 0048b058 ["CALL", null, ["callee:00c53d00:8"]]
- 0048b018 bytes 32221f94
+ 0048b058 bytes 2a231f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-579fd8ef7e8003786276699dfdba5f71"></a>

### [`0048b09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b09c.md) → [`0048b0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b0dc.md) FUN_0048b0dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0046a9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a9bc.md) [`0046ac60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046ac60.md) · 呼出先 6件 [`0046c178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c178.md) [`0046c1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c1f0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`0046a9fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a9fc.md) [`0046aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046aca0.md) · 呼出先 6件 [`0046c1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c1b8.md) [`0046c230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c230.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048b16c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b09c.md#insn-0048b16c) · [`0048b178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b09c.md#insn-0048b178) · [`0048b18c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b09c.md#insn-0048b18c)
- 新版 [`0048b1ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b0dc.md#insn-0048b1ac) · [`0048b1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b0dc.md#insn-0048b1b8) · [`0048b1cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b0dc.md#insn-0048b1cc)

~~~diff
- 0048b16c ["INT_ADD", "register:40f0:8", ["const:48b16c:8", "const:4:8"]]
- 0048b16c ["CALL", null, ["callee:00c53cd0:8"]]
+ 0048b1ac ["INT_ADD", "register:40f0:8", ["const:48b1ac:8", "const:4:8"]]
+ 0048b1ac ["CALL", null, ["callee:00c53cd0:8"]]
- 0048b16c bytes d1211f94
+ 0048b1ac bytes c9221f94
- 0048b178 ["INT_ADD", "register:40f0:8", ["const:48b178:8", "const:4:8"]]
- 0048b178 ["CALL", null, ["callee:0046c1b8:8"]]
+ 0048b1b8 ["INT_ADD", "register:40f0:8", ["const:48b1b8:8", "const:4:8"]]
+ 0048b1b8 ["CALL", null, ["callee:0046c1b8:8"]]
- 0048b178 bytes 0084ff97
+ 0048b1b8 bytes 0084ff97
- 0048b18c ["INT_ADD", "register:40f0:8", ["const:48b18c:8", "const:4:8"]]
- 0048b18c ["CALL", null, ["callee:00c53d00:8"]]
+ 0048b1cc ["INT_ADD", "register:40f0:8", ["const:48b1cc:8", "const:4:8"]]
+ 0048b1cc ["CALL", null, ["callee:00c53d00:8"]]
- 0048b18c bytes d5211f94
+ 0048b1cc bytes cd221f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e318b4f796956dd0fb1b61f7b1646e1"></a>

### [`0048b210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b210.md) → [`0048b250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b250.md) FUN_0048b250

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0046ab08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046ab08.md) · 呼出先 6件 [`0046c178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c178.md) [`0046c1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c1f0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0046ab48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046ab48.md) · 呼出先 6件 [`0046c1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c1b8.md) [`0046c230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c230.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048b2ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b210.md#insn-0048b2ac) · [`0048b2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b210.md#insn-0048b2b8) · [`0048b2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b210.md#insn-0048b2cc)
- 新版 [`0048b2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b250.md#insn-0048b2ec) · [`0048b2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b250.md#insn-0048b2f8) · [`0048b30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b250.md#insn-0048b30c)

~~~diff
- 0048b2ac ["INT_ADD", "register:40f0:8", ["const:48b2ac:8", "const:4:8"]]
- 0048b2ac ["CALL", null, ["callee:00c53cd0:8"]]
+ 0048b2ec ["INT_ADD", "register:40f0:8", ["const:48b2ec:8", "const:4:8"]]
+ 0048b2ec ["CALL", null, ["callee:00c53cd0:8"]]
- 0048b2ac bytes 81211f94
+ 0048b2ec bytes 79221f94
- 0048b2b8 ["INT_ADD", "register:40f0:8", ["const:48b2b8:8", "const:4:8"]]
- 0048b2b8 ["CALL", null, ["callee:0046c1b8:8"]]
+ 0048b2f8 ["INT_ADD", "register:40f0:8", ["const:48b2f8:8", "const:4:8"]]
+ 0048b2f8 ["CALL", null, ["callee:0046c1b8:8"]]
- 0048b2b8 bytes b083ff97
+ 0048b2f8 bytes b083ff97
- 0048b2cc ["INT_ADD", "register:40f0:8", ["const:48b2cc:8", "const:4:8"]]
- 0048b2cc ["CALL", null, ["callee:00c53d00:8"]]
+ 0048b30c ["INT_ADD", "register:40f0:8", ["const:48b30c:8", "const:4:8"]]
+ 0048b30c ["CALL", null, ["callee:00c53d00:8"]]
- 0048b2cc bytes 85211f94
+ 0048b30c bytes 7d221f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4b377650ca84d94865074755b9eb497"></a>

### [`0048b390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b390.md) → [`0048b3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b3d0.md) FUN_0048b3d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00489184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489184.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046daac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046daac.md) [`0048b504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b504.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`004891c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004891c4.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046daec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daec.md) [`0048b544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b544.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048b408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b390.md#insn-0048b408) · [`0048b428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b390.md#insn-0048b428) · [`0048b460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b390.md#insn-0048b460)
- 新版 [`0048b448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b3d0.md#insn-0048b448) · [`0048b468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b3d0.md#insn-0048b468) · [`0048b4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b3d0.md#insn-0048b4a0)

~~~diff
- 0048b408 ["INT_ADD", "register:40f0:8", ["const:48b408:8", "const:4:8"]]
- 0048b408 ["CALL", null, ["callee:00c57e90:8"]]
+ 0048b448 ["INT_ADD", "register:40f0:8", ["const:48b448:8", "const:4:8"]]
+ 0048b448 ["CALL", null, ["callee:00c57e90:8"]]
- 0048b408 bytes a2311f94
+ 0048b448 bytes 92321f94
- 0048b428 ["INT_ADD", "register:40f0:8", ["const:48b428:8", "const:4:8"]]
- 0048b428 ["CALL", null, ["callee:0046daec:8"]]
+ 0048b468 ["INT_ADD", "register:40f0:8", ["const:48b468:8", "const:4:8"]]
+ 0048b468 ["CALL", null, ["callee:0046daec:8"]]
- 0048b428 bytes a189ff97
+ 0048b468 bytes a189ff97
- 0048b460 ["INT_ADD", "register:40f0:8", ["const:48b460:8", "const:4:8"]]
- 0048b460 ["CALL", null, ["callee:0046daec:8"]]
+ 0048b4a0 ["INT_ADD", "register:40f0:8", ["const:48b4a0:8", "const:4:8"]]
+ 0048b4a0 ["CALL", null, ["callee:0046daec:8"]]
- 0048b460 bytes 9389ff97
+ 0048b4a0 bytes 9389ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cedda542a524aaaab79a413c94214638"></a>

### [`0048b518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b518.md) → [`0048b558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b558.md) FUN_0048b558

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00489f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f28.md) [`0048b518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b518.md) · 呼出先 4件 [`0048b518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b518.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00489f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f68.md) [`0048b558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b558.md) · 呼出先 4件 [`0048b558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b558.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048b534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b518.md#insn-0048b534) · [`0048b540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b518.md#insn-0048b540) · [`0048b554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b518.md#insn-0048b554)
- 新版 [`0048b574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b558.md#insn-0048b574) · [`0048b580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b558.md#insn-0048b580) · [`0048b594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b558.md#insn-0048b594)

~~~diff
- 0048b534 ["INT_ADD", "register:40f0:8", ["const:48b534:8", "const:4:8"]]
- 0048b534 ["CALL", null, ["local:b0:8"]]
+ 0048b574 ["INT_ADD", "register:40f0:8", ["const:48b574:8", "const:4:8"]]
+ 0048b574 ["CALL", null, ["local:b0:8"]]
- 0048b534 bytes f9ffff97
+ 0048b574 bytes f9ffff97
- 0048b540 ["INT_ADD", "register:40f0:8", ["const:48b540:8", "const:4:8"]]
- 0048b540 ["CALL", null, ["local:b0:8"]]
+ 0048b580 ["INT_ADD", "register:40f0:8", ["const:48b580:8", "const:4:8"]]
+ 0048b580 ["CALL", null, ["local:b0:8"]]
- 0048b540 bytes f6ffff97
+ 0048b580 bytes f6ffff97
- 0048b554 ["INT_ADD", "register:40f0:8", ["const:48b554:8", "const:4:8"]]
- 0048b554 ["CALL", null, ["callee:00c53d00:8"]]
+ 0048b594 ["INT_ADD", "register:40f0:8", ["const:48b594:8", "const:4:8"]]
+ 0048b594 ["CALL", null, ["callee:00c53d00:8"]]
- 0048b554 bytes e3201f94
+ 0048b594 bytes db211f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ca4533527a12dd3b0394bd9e683a283"></a>

### [`0048b5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b5a4.md) → [`0048b5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b5e4.md) FUN_0048b5e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00489f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f30.md) · 呼出先 2件 [`0048b69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b69c.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00489f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f70.md) · 呼出先 2件 [`0048b6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b6dc.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048b5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b5a4.md#insn-0048b5cc) · [`0048b624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b5a4.md#insn-0048b624) · [`0048b66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b5a4.md#insn-0048b66c)
- 新版 [`0048b60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b5e4.md#insn-0048b60c) · [`0048b664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b5e4.md#insn-0048b664) · [`0048b6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b5e4.md#insn-0048b6ac)

~~~diff
- 0048b5cc ["INT_ADD", "register:40f0:8", ["const:48b5cc:8", "const:4:8"]]
- 0048b5cc ["CALL", null, ["callee:0048b6dc:8"]]
+ 0048b60c ["INT_ADD", "register:40f0:8", ["const:48b60c:8", "const:4:8"]]
+ 0048b60c ["CALL", null, ["callee:0048b6dc:8"]]
- 0048b5cc bytes 34000094
+ 0048b60c bytes 34000094
- 0048b624 ["INT_ADD", "register:40f0:8", ["const:48b624:8", "const:4:8"]]
- 0048b624 ["CALL", null, ["callee:00c58050:8"]]
+ 0048b664 ["INT_ADD", "register:40f0:8", ["const:48b664:8", "const:4:8"]]
+ 0048b664 ["CALL", null, ["callee:00c58050:8"]]
- 0048b624 bytes 8b311f94
+ 0048b664 bytes 7b321f94
- 0048b66c ["INT_ADD", "register:40f0:8", ["const:48b66c:8", "const:4:8"]]
- 0048b66c ["CALL", null, ["callee:00c58050:8"]]
+ 0048b6ac ["INT_ADD", "register:40f0:8", ["const:48b6ac:8", "const:4:8"]]
+ 0048b6ac ["CALL", null, ["callee:00c58050:8"]]
- 0048b66c bytes 79311f94
+ 0048b6ac bytes 69321f94
~~~


<a id="compare-08b1119b8c77e0d2dd471f4fc5b9790c"></a>

### [`0048b69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b69c.md) → [`0048b6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b6dc.md) FUN_0048b6dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0048b5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b5a4.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`0048b5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b5e4.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b69c.md#insn-0048b724) · [`0048b750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b69c.md#insn-0048b750)
- 新版 [`0048b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b6dc.md#insn-0048b764) · [`0048b790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b6dc.md#insn-0048b790)

~~~diff
- 0048b724 ["INT_ADD", "register:40f0:8", ["const:48b724:8", "const:4:8"]]
- 0048b724 ["CALL", null, ["callee:00c58050:8"]]
+ 0048b764 ["INT_ADD", "register:40f0:8", ["const:48b764:8", "const:4:8"]]
+ 0048b764 ["CALL", null, ["callee:00c58050:8"]]
- 0048b724 bytes 4b311f94
+ 0048b764 bytes 3b321f94
- 0048b750 ["INT_ADD", "register:40f0:8", ["const:48b750:8", "const:4:8"]]
- 0048b750 ["CALL", null, ["callee:00c58050:8"]]
+ 0048b790 ["INT_ADD", "register:40f0:8", ["const:48b790:8", "const:4:8"]]
+ 0048b790 ["CALL", null, ["callee:00c58050:8"]]
- 0048b750 bytes 40311f94
+ 0048b790 bytes 30321f94
~~~


<a id="compare-b462cf07052babb22c972cac2225e641"></a>

### [`0048b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b7b8.md) → [`0048b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b7f8.md) FUN_0048b7f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00489f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f30.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0048b8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b8ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00489f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f70.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048b92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b92c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048b7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b7b8.md#insn-0048b7ec) · [`0048b80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b7b8.md#insn-0048b80c) · [`0048b848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b7b8.md#insn-0048b848)
- 新版 [`0048b82c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b7f8.md#insn-0048b82c) · [`0048b84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b7f8.md#insn-0048b84c) · [`0048b888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b7f8.md#insn-0048b888)

~~~diff
- 0048b7ec ["INT_ADD", "register:40f0:8", ["const:48b7ec:8", "const:4:8"]]
- 0048b7ec ["CALL", null, ["callee:0048b92c:8"]]
+ 0048b82c ["INT_ADD", "register:40f0:8", ["const:48b82c:8", "const:4:8"]]
+ 0048b82c ["CALL", null, ["callee:0048b92c:8"]]
- 0048b7ec bytes 40000094
+ 0048b82c bytes 40000094
- 0048b80c ["INT_ADD", "register:40f0:8", ["const:48b80c:8", "const:4:8"]]
- 0048b80c ["CALL", null, ["callee:00c57e90:8"]]
+ 0048b84c ["INT_ADD", "register:40f0:8", ["const:48b84c:8", "const:4:8"]]
+ 0048b84c ["CALL", null, ["callee:00c57e90:8"]]
- 0048b80c bytes a1301f94
+ 0048b84c bytes 91311f94
- 0048b848 ["INT_ADD", "register:40f0:8", ["const:48b848:8", "const:4:8"]]
- 0048b848 ["CALL", null, ["callee:0043bb20:8"]]
+ 0048b888 ["INT_ADD", "register:40f0:8", ["const:48b888:8", "const:4:8"]]
+ 0048b888 ["CALL", null, ["callee:0043bb20:8"]]
- 0048b848 bytes a6c0fe97
+ 0048b888 bytes a6c0fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6891a147efce306293bac065d380bfcd"></a>

### [`0048b8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b8ec.md) → [`0048b92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b92c.md) FUN_0048b92c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0048b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b7b8.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`0048b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b7f8.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048b978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b8ec.md#insn-0048b978) · [`0048b9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b8ec.md#insn-0048b9a0) · [`0048b9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b8ec.md#insn-0048b9dc)
- 新版 [`0048b9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b92c.md#insn-0048b9b8) · [`0048b9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b92c.md#insn-0048b9e0) · [`0048ba1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b92c.md#insn-0048ba1c)

~~~diff
- 0048b978 ["INT_ADD", "register:40f0:8", ["const:48b978:8", "const:4:8"]]
- 0048b978 ["CALL", null, ["callee:00c58050:8"]]
+ 0048b9b8 ["INT_ADD", "register:40f0:8", ["const:48b9b8:8", "const:4:8"]]
+ 0048b9b8 ["CALL", null, ["callee:00c58050:8"]]
- 0048b978 bytes b6301f94
+ 0048b9b8 bytes a6311f94
- 0048b9a0 ["INT_ADD", "register:40f0:8", ["const:48b9a0:8", "const:4:8"]]
- 0048b9a0 ["CALL", null, ["callee:00c58050:8"]]
+ 0048b9e0 ["INT_ADD", "register:40f0:8", ["const:48b9e0:8", "const:4:8"]]
+ 0048b9e0 ["CALL", null, ["callee:00c58050:8"]]
- 0048b9a0 bytes ac301f94
+ 0048b9e0 bytes 9c311f94
- 0048b9dc ["INT_ADD", "register:40f0:8", ["const:48b9dc:8", "const:4:8"]]
- 0048b9dc ["CALL", null, ["callee:00c58050:8"]]
+ 0048ba1c ["INT_ADD", "register:40f0:8", ["const:48ba1c:8", "const:4:8"]]
+ 0048ba1c ["CALL", null, ["callee:00c58050:8"]]
- 0048b9dc bytes 9d301f94
+ 0048ba1c bytes 8d311f94
~~~


<a id="compare-ac0816d6c70d8d0c7995aa972cdd1377"></a>

### [`0048ba34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048ba34.md) → [`0048ba74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048ba74.md) FUN_0048ba74

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048ba64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048ba34.md#insn-0048ba64) · [`0048ba78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048ba34.md#insn-0048ba78) · [`0048ba80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048ba34.md#insn-0048ba80)
- 新版 [`0048baa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048ba74.md#insn-0048baa4) · [`0048bab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048ba74.md#insn-0048bab8) · [`0048bac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048ba74.md#insn-0048bac0)

~~~diff
- 0048ba64 ["INT_ADD", "register:40f0:8", ["const:48ba64:8", "const:4:8"]]
- 0048ba64 ["CALL", null, ["callee:00c53d00:8"]]
+ 0048baa4 ["INT_ADD", "register:40f0:8", ["const:48baa4:8", "const:4:8"]]
+ 0048baa4 ["CALL", null, ["callee:00c53d00:8"]]
- 0048ba64 bytes 9f1f1f94
+ 0048baa4 bytes 97201f94
- 0048ba78 ["COPY", "register:0:8", ["register:4040:8"]]
- 0048ba78 ["INT_ADD", "register:40f0:8", ["const:48ba78:8", "const:4:8"]]
- 0048ba78 ["CALLIND", null, ["register:0:8"]]
+ 0048bab8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048bab8 ["INT_ADD", "register:40f0:8", ["const:48bab8:8", "const:4:8"]]
+ 0048bab8 ["CALLIND", null, ["register:0:8"]]
- 0048ba78 bytes 00013fd6
+ 0048bab8 bytes 00013fd6
- 0048ba80 ["INT_ADD", "register:40f0:8", ["const:48ba80:8", "const:4:8"]]
- 0048ba80 ["CALL", null, ["callee:00c57e80:8"]]
+ 0048bac0 ["INT_ADD", "register:40f0:8", ["const:48bac0:8", "const:4:8"]]
+ 0048bac0 ["CALL", null, ["callee:00c57e80:8"]]
- 0048ba80 bytes 00301f94
+ 0048bac0 bytes f0301f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23724c8e4758b21d5f5157c3c94c03de"></a>

### [`0048cd34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048cd34.md) → [`0048cd74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048cd74.md) FUN_0048cd74

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048dc78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dc78.md) [`0048dd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dd00.md) [`0048e4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e4b0.md) [`0048e8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e8c0.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 6件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048dcb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dcb8.md) [`0048dd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dd40.md) [`0048e4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e4f0.md) [`0048e900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e900.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048cd54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048cd34.md#insn-0048cd54) · [`0048cd68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048cd34.md#insn-0048cd68) · [`0048cd70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048cd34.md#insn-0048cd70)
- 新版 [`0048cd94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048cd74.md#insn-0048cd94) · [`0048cda8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048cd74.md#insn-0048cda8) · [`0048cdb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048cd74.md#insn-0048cdb0)

~~~diff
- 0048cd54 ["INT_ADD", "register:40f0:8", ["const:48cd54:8", "const:4:8"]]
- 0048cd54 ["CALL", null, ["callee:00c53d00:8"]]
+ 0048cd94 ["INT_ADD", "register:40f0:8", ["const:48cd94:8", "const:4:8"]]
+ 0048cd94 ["CALL", null, ["callee:00c53d00:8"]]
- 0048cd54 bytes e31a1f94
+ 0048cd94 bytes db1b1f94
- 0048cd68 ["COPY", "register:0:8", ["register:4040:8"]]
- 0048cd68 ["INT_ADD", "register:40f0:8", ["const:48cd68:8", "const:4:8"]]
- 0048cd68 ["CALLIND", null, ["register:0:8"]]
+ 0048cda8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048cda8 ["INT_ADD", "register:40f0:8", ["const:48cda8:8", "const:4:8"]]
+ 0048cda8 ["CALLIND", null, ["register:0:8"]]
- 0048cd68 bytes 00013fd6
+ 0048cda8 bytes 00013fd6
- 0048cd70 ["INT_ADD", "register:40f0:8", ["const:48cd70:8", "const:4:8"]]
- 0048cd70 ["CALL", null, ["callee:00c57e80:8"]]
+ 0048cdb0 ["INT_ADD", "register:40f0:8", ["const:48cdb0:8", "const:4:8"]]
+ 0048cdb0 ["CALL", null, ["callee:00c57e80:8"]]
- 0048cd70 bytes 442b1f94
+ 0048cdb0 bytes 342c1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a48a5f864b4d2701ba6304fd9f14ac85"></a>

### [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) → [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) FUN_0048ce54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 369件 [`0047a140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a140.md) [`00489184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489184.md) [`005b1778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1778.md) [`005b1b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1b44.md) [`005b9b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9b14.md) · 呼出先 2件 [`0046d064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d064.md) [`0046d3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d3bc.md)
- 新版 呼出元 368件 [`0047a180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a180.md) [`004891c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004891c4.md) [`005b17b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b17b8.md) [`005b1b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1b84.md) [`005b9b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9b54.md) · 呼出先 2件 [`0046d0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d0a4.md) [`0046d3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d3fc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048ce28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md#insn-0048ce28)
- 新版 [`0048ce68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md#insn-0048ce68)

~~~diff
- 0048ce28 ["INT_ADD", "register:40f0:8", ["const:48ce28:8", "const:4:8"]]
- 0048ce28 ["CALL", null, ["callee:0046d0a4:8"]]
+ 0048ce68 ["INT_ADD", "register:40f0:8", ["const:48ce68:8", "const:4:8"]]
+ 0048ce68 ["CALL", null, ["callee:0046d0a4:8"]]
- 0048ce28 bytes 8f80ff97
+ 0048ce68 bytes 8f80ff97
~~~


<a id="compare-53235cf11f232ea29477cf17d3669c1e"></a>

### [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) → [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) FUN_0048ce84

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 108件 [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`0043d574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043d574.md) [`0043ec20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ec20.md) [`00444de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) [`005b9a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9a58.md) · 呼出先 1件 [`00c58180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58180.md)
- 新版 呼出元 108件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`0043d5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043d5b4.md) [`0043ec60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ec60.md) [`00444e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444e20.md) [`005b9a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9a98.md) · 呼出先 1件 [`00c58580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048ce4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md#insn-0048ce4c)
- 新版 [`0048ce8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md#insn-0048ce8c)

~~~diff
- 0048ce4c ["INT_ADD", "register:40f0:8", ["const:48ce4c:8", "const:4:8"]]
- 0048ce4c ["CALL", null, ["callee:00c58580:8"]]
+ 0048ce8c ["INT_ADD", "register:40f0:8", ["const:48ce8c:8", "const:4:8"]]
+ 0048ce8c ["CALL", null, ["callee:00c58580:8"]]
- 0048ce4c bytes cd2c1f94
+ 0048ce8c bytes bd2d1f94
~~~


<a id="compare-6425c6b4c2189671d7dbc87efc08a59b"></a>

### [`0048ce78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce78.md) → [`0048ceb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ceb8.md) FUN_0048ceb8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0074e344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074e/0074e344.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 4件 [`004782d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/004782d4.md) [`00478650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478650.md) [`00478bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478bd4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`0074e384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074e/0074e384.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 4件 [`00478314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478314.md) [`00478690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478690.md) [`00478c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c14.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048cea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce78.md#insn-0048cea0) · [`0048cec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce78.md#insn-0048cec4) · [`0048ced0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce78.md#insn-0048ced0)
- 新版 [`0048cee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ceb8.md#insn-0048cee0) · [`0048cf04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ceb8.md#insn-0048cf04) · [`0048cf10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ceb8.md#insn-0048cf10)

~~~diff
- 0048cea0 ["INT_ADD", "register:40f0:8", ["const:48cea0:8", "const:4:8"]]
- 0048cea0 ["CALL", null, ["callee:00478690:8"]]
+ 0048cee0 ["INT_ADD", "register:40f0:8", ["const:48cee0:8", "const:4:8"]]
+ 0048cee0 ["CALL", null, ["callee:00478690:8"]]
- 0048cea0 bytes ecadff97
+ 0048cee0 bytes ecadff97
- 0048cec4 ["INT_ADD", "register:40f0:8", ["const:48cec4:8", "const:4:8"]]
- 0048cec4 ["CALL", null, ["callee:00478314:8"]]
+ 0048cf04 ["INT_ADD", "register:40f0:8", ["const:48cf04:8", "const:4:8"]]
+ 0048cf04 ["CALL", null, ["callee:00478314:8"]]
- 0048cec4 bytes 04adff97
+ 0048cf04 bytes 04adff97
- 0048ced0 ["INT_ADD", "register:40f0:8", ["const:48ced0:8", "const:4:8"]]
- 0048ced0 ["CALL", null, ["callee:00478c14:8"]]
+ 0048cf10 ["INT_ADD", "register:40f0:8", ["const:48cf10:8", "const:4:8"]]
+ 0048cf10 ["CALL", null, ["callee:00478c14:8"]]
- 0048ced0 bytes 41afff97
+ 0048cf10 bytes 41afff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba576563ae51dbdae0efe816defaddf3"></a>

### [`0048d27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d27c.md) → [`0048d2bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d2bc.md) FUN_0048d2bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00484780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484780.md) · 呼出先 5件 [`0055e834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e834.md) [`00560418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560418.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`004847c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004847c0.md) · 呼出先 5件 [`0055e874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e874.md) [`00560458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560458.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048d2a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d27c.md#insn-0048d2a4) · [`0048d2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d27c.md#insn-0048d2b4) · [`0048d2c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d27c.md#insn-0048d2c8)
- 新版 [`0048d2e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d2bc.md#insn-0048d2e4) · [`0048d2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d2bc.md#insn-0048d2f4) · [`0048d308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d2bc.md#insn-0048d308)

~~~diff
- 0048d2a4 ["INT_ADD", "register:40f0:8", ["const:48d2a4:8", "const:4:8"]]
- 0048d2a4 ["CALL", null, ["callee:0055e874:8"]]
+ 0048d2e4 ["INT_ADD", "register:40f0:8", ["const:48d2e4:8", "const:4:8"]]
+ 0048d2e4 ["CALL", null, ["callee:0055e874:8"]]
- 0048d2a4 bytes 64450394
+ 0048d2e4 bytes 64450394
- 0048d2b4 ["INT_ADD", "register:40f0:8", ["const:48d2b4:8", "const:4:8"]]
- 0048d2b4 ["CALL", null, ["callee:00560458:8"]]
+ 0048d2f4 ["INT_ADD", "register:40f0:8", ["const:48d2f4:8", "const:4:8"]]
+ 0048d2f4 ["CALL", null, ["callee:00560458:8"]]
- 0048d2b4 bytes 594c0394
+ 0048d2f4 bytes 594c0394
- 0048d2c8 ["INT_ADD", "register:40f0:8", ["const:48d2c8:8", "const:4:8"]]
- 0048d2c8 ["CALL", null, ["callee:00c53d00:8"]]
+ 0048d308 ["INT_ADD", "register:40f0:8", ["const:48d308:8", "const:4:8"]]
+ 0048d308 ["CALL", null, ["callee:00c53d00:8"]]
- 0048d2c8 bytes 86191f94
+ 0048d308 bytes 7e1a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f09d080a542f0bdb83c6c072134ecdef"></a>

### [`0048d330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d330.md) → [`0048d370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d370.md) FUN_0048d370

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 15件 [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`0043ec20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ec20.md) [`0043f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f8dc.md) [`00470ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md) [`00488750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488750.md) · 呼出先 5件 [`0055e710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e710.md) [`00560418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560418.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 15件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`0043ec60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ec60.md) [`0043f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f91c.md) [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) [`00488790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488790.md) · 呼出先 5件 [`0055e750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e750.md) [`00560458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560458.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048d358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d330.md#insn-0048d358) · [`0048d368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d330.md#insn-0048d368) · [`0048d37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d330.md#insn-0048d37c)
- 新版 [`0048d398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d370.md#insn-0048d398) · [`0048d3a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d370.md#insn-0048d3a8) · [`0048d3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d370.md#insn-0048d3bc)

~~~diff
- 0048d358 ["INT_ADD", "register:40f0:8", ["const:48d358:8", "const:4:8"]]
- 0048d358 ["CALL", null, ["callee:0055e750:8"]]
+ 0048d398 ["INT_ADD", "register:40f0:8", ["const:48d398:8", "const:4:8"]]
+ 0048d398 ["CALL", null, ["callee:0055e750:8"]]
- 0048d358 bytes ee440394
+ 0048d398 bytes ee440394
- 0048d368 ["INT_ADD", "register:40f0:8", ["const:48d368:8", "const:4:8"]]
- 0048d368 ["CALL", null, ["callee:00560458:8"]]
+ 0048d3a8 ["INT_ADD", "register:40f0:8", ["const:48d3a8:8", "const:4:8"]]
+ 0048d3a8 ["CALL", null, ["callee:00560458:8"]]
- 0048d368 bytes 2c4c0394
+ 0048d3a8 bytes 2c4c0394
- 0048d37c ["INT_ADD", "register:40f0:8", ["const:48d37c:8", "const:4:8"]]
- 0048d37c ["CALL", null, ["callee:00c53d00:8"]]
+ 0048d3bc ["INT_ADD", "register:40f0:8", ["const:48d3bc:8", "const:4:8"]]
+ 0048d3bc ["CALL", null, ["callee:00c53d00:8"]]
- 0048d37c bytes 59191f94
+ 0048d3bc bytes 511a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f21c7e4fe46dc8a510d75e59b5b556cc"></a>

### [`0048d3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d3e4.md) → [`0048d424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d424.md) FUN_0048d424

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`009816dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009816dc.md) · 呼出先 5件 [`0055ecc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055ecc8.md) [`005975c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975c8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`00981878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981878.md) · 呼出先 5件 [`0055ed08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055ed08.md) [`00597608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597608.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048d410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d3e4.md#insn-0048d410) · [`0048d42c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d3e4.md#insn-0048d42c) · [`0048d44c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d3e4.md#insn-0048d44c)
- 新版 [`0048d450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d424.md#insn-0048d450) · [`0048d46c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d424.md#insn-0048d46c) · [`0048d48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d424.md#insn-0048d48c)

~~~diff
- 0048d410 ["INT_ADD", "register:40f0:8", ["const:48d410:8", "const:4:8"]]
- 0048d410 ["CALL", null, ["callee:00597608:8"]]
+ 0048d450 ["INT_ADD", "register:40f0:8", ["const:48d450:8", "const:4:8"]]
+ 0048d450 ["CALL", null, ["callee:00597608:8"]]
- 0048d410 bytes 6e280494
+ 0048d450 bytes 6e280494
- 0048d42c ["INT_ADD", "register:40f0:8", ["const:48d42c:8", "const:4:8"]]
- 0048d42c ["CALL", null, ["callee:0055ed08:8"]]
+ 0048d46c ["INT_ADD", "register:40f0:8", ["const:48d46c:8", "const:4:8"]]
+ 0048d46c ["CALL", null, ["callee:0055ed08:8"]]
- 0048d42c bytes 27460394
+ 0048d46c bytes 27460394
- 0048d44c ["INT_ADD", "register:40f0:8", ["const:48d44c:8", "const:4:8"]]
- 0048d44c ["CALL", null, ["callee:00c53d00:8"]]
+ 0048d48c ["INT_ADD", "register:40f0:8", ["const:48d48c:8", "const:4:8"]]
+ 0048d48c ["CALL", null, ["callee:00c53d00:8"]]
- 0048d44c bytes 25191f94
+ 0048d48c bytes 1d1a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f1c8492b5a1f5e19b20b597b745d9e1"></a>

### [`0048d7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d7dc.md) → [`0048d81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d81c.md) FUN_0048d81c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`0043f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f8dc.md) [`00470ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md) [`00488750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488750.md) [`0048965c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/0048965c.md) [`00637810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00637/00637810.md) · 呼出先 5件 [`0055f058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f058.md) [`005975c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975c8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 7件 [`0043f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f91c.md) [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) [`00488790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488790.md) [`0048969c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/0048969c.md) [`00637850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00637/00637850.md) · 呼出先 5件 [`0055f098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f098.md) [`00597608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597608.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048d808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d7dc.md#insn-0048d808) · [`0048d824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d7dc.md#insn-0048d824) · [`0048d838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d7dc.md#insn-0048d838)
- 新版 [`0048d848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d81c.md#insn-0048d848) · [`0048d864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d81c.md#insn-0048d864) · [`0048d878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d81c.md#insn-0048d878)

~~~diff
- 0048d808 ["INT_ADD", "register:40f0:8", ["const:48d808:8", "const:4:8"]]
- 0048d808 ["CALL", null, ["callee:00597608:8"]]
+ 0048d848 ["INT_ADD", "register:40f0:8", ["const:48d848:8", "const:4:8"]]
+ 0048d848 ["CALL", null, ["callee:00597608:8"]]
- 0048d808 bytes 70270494
+ 0048d848 bytes 70270494
- 0048d824 ["INT_ADD", "register:40f0:8", ["const:48d824:8", "const:4:8"]]
- 0048d824 ["CALL", null, ["callee:0055f098:8"]]
+ 0048d864 ["INT_ADD", "register:40f0:8", ["const:48d864:8", "const:4:8"]]
+ 0048d864 ["CALL", null, ["callee:0055f098:8"]]
- 0048d824 bytes 0d460394
+ 0048d864 bytes 0d460394
- 0048d838 ["INT_ADD", "register:40f0:8", ["const:48d838:8", "const:4:8"]]
- 0048d838 ["CALL", null, ["callee:00c53d00:8"]]
+ 0048d878 ["INT_ADD", "register:40f0:8", ["const:48d878:8", "const:4:8"]]
+ 0048d878 ["CALL", null, ["callee:00c53d00:8"]]
- 0048d838 bytes 2a181f94
+ 0048d878 bytes 22191f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13342595255b7060d6032a8009397d0a"></a>

### [`0048dc28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dc28.md) → [`0048dc68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dc68.md) FUN_0048dc68

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00494dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494dc8.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00494e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494e08.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048dc44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dc28.md#insn-0048dc44) · [`0048dc64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dc28.md#insn-0048dc64)
- 新版 [`0048dc84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dc68.md#insn-0048dc84) · [`0048dca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dc68.md#insn-0048dca4)

~~~diff
- 0048dc44 ["INT_ADD", "register:40f0:8", ["const:48dc44:8", "const:4:8"]]
- 0048dc44 ["CALL", null, ["callee:00c53d00:8"]]
+ 0048dc84 ["INT_ADD", "register:40f0:8", ["const:48dc84:8", "const:4:8"]]
+ 0048dc84 ["CALL", null, ["callee:00c53d00:8"]]
- 0048dc44 bytes 27171f94
+ 0048dc84 bytes 1f181f94
- 0048dc64 ["COPY", "register:0:8", ["register:4040:8"]]
- 0048dc64 ["INT_ADD", "register:40f0:8", ["const:48dc64:8", "const:4:8"]]
- 0048dc64 ["CALLIND", null, ["register:0:8"]]
+ 0048dca4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048dca4 ["INT_ADD", "register:40f0:8", ["const:48dca4:8", "const:4:8"]]
+ 0048dca4 ["CALLIND", null, ["register:0:8"]]
- 0048dc64 bytes 00013fd6
+ 0048dca4 bytes 00013fd6
~~~


<a id="compare-9fd77532d895f4cad1fa233a682c24cf"></a>

### [`0048e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md) → [`0048e0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e0b8.md) FUN_0048e0b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 24件 [`0048dd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dd00.md) [`0048e8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e8c0.md) [`0048eeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048eeb0.md) [`00490134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490134.md) [`0049065c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/0049065c.md) · 呼出先 2件 [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 23件 [`0048dd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dd40.md) [`0048e900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e900.md) [`0048eef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048eef0.md) [`00490174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/00490174.md) [`0049069c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/0049069c.md) · 呼出先 2件 [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048e124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md#insn-0048e124) · [`0048e138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md#insn-0048e138)
- 新版 [`0048e164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e0b8.md#insn-0048e164) · [`0048e178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e0b8.md#insn-0048e178)

~~~diff
- 0048e124 ["INT_ADD", "register:40f0:8", ["const:48e124:8", "const:4:8"]]
- 0048e124 ["CALL", null, ["callee:00c57fd0:8"]]
+ 0048e164 ["INT_ADD", "register:40f0:8", ["const:48e164:8", "const:4:8"]]
+ 0048e164 ["CALL", null, ["callee:00c57fd0:8"]]
- 0048e124 bytes ab261f94
+ 0048e164 bytes 9b271f94
- 0048e138 ["INT_ADD", "register:40f0:8", ["const:48e138:8", "const:4:8"]]
- 0048e138 ["CALL", null, ["callee:00c58050:8"]]
+ 0048e178 ["INT_ADD", "register:40f0:8", ["const:48e178:8", "const:4:8"]]
+ 0048e178 ["CALL", null, ["callee:00c58050:8"]]
- 0048e138 bytes c6261f94
+ 0048e178 bytes b6271f94
~~~


<a id="compare-e033b33150adc32775ab74b5dd6cd446"></a>

### [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md) → [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) FUN_0048e7e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 44件 [`005b57d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b57d4.md) [`005b5aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5aa0.md) [`0061e668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e668.md) [`006269f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/006269f4.md) [`00783234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783234.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 44件 [`005b5814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5814.md) [`005b5ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ae0.md) [`0061e6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e6a8.md) [`00626a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/00626a34.md) [`00783274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/00783274.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048e7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md#insn-0048e7e4) · [`0048e7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md#insn-0048e7fc) · [`0048e810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md#insn-0048e810)
- 新版 [`0048e824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md#insn-0048e824) · [`0048e83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md#insn-0048e83c) · [`0048e850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md#insn-0048e850)

~~~diff
- 0048e7e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0048e7e4 ["INT_ADD", "register:40f0:8", ["const:48e7e4:8", "const:4:8"]]
- 0048e7e4 ["CALLIND", null, ["register:0:8"]]
+ 0048e824 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048e824 ["INT_ADD", "register:40f0:8", ["const:48e824:8", "const:4:8"]]
+ 0048e824 ["CALLIND", null, ["register:0:8"]]
- 0048e7e4 bytes 00013fd6
+ 0048e824 bytes 00013fd6
- 0048e7fc ["INT_ADD", "register:40f0:8", ["const:48e7fc:8", "const:4:8"]]
- 0048e7fc ["CALL", null, ["callee:00c53d00:8"]]
+ 0048e83c ["INT_ADD", "register:40f0:8", ["const:48e83c:8", "const:4:8"]]
+ 0048e83c ["CALL", null, ["callee:00c53d00:8"]]
- 0048e7fc bytes 39141f94
+ 0048e83c bytes 31151f94
- 0048e810 ["COPY", "register:0:8", ["register:4040:8"]]
- 0048e810 ["INT_ADD", "register:40f0:8", ["const:48e810:8", "const:4:8"]]
- 0048e810 ["CALLIND", null, ["register:0:8"]]
+ 0048e850 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048e850 ["INT_ADD", "register:40f0:8", ["const:48e850:8", "const:4:8"]]
+ 0048e850 ["CALLIND", null, ["register:0:8"]]
- 0048e810 bytes 00013fd6
+ 0048e850 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

