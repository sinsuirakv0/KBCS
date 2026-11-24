# v16.0.0 → v16.0.1 · 要調査の変更候補 (13)

[一覧の目次](README.md)

<a id="compare-dec8e62b66345920d60b2a1d5d1106db"></a>

### [`0056d230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d230.md) → [`0056d270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d270.md) FUN_0056d270

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) [`005692f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005692f4.md) · 呼出先 1件 [`00c59c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c70.md)
- 新版 呼出元 2件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) [`00569334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569334.md) · 呼出先 1件 [`00c5a070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a070.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056d268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d230.md#insn-0056d268)
- 新版 [`0056d2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d270.md#insn-0056d2a8)

~~~diff
- 0056d268 ["INT_ADD", "register:40f0:8", ["const:56d268:8", "const:4:8"]]
- 0056d268 ["CALL", null, ["callee:00c5a070:8"]]
+ 0056d2a8 ["INT_ADD", "register:40f0:8", ["const:56d2a8:8", "const:4:8"]]
+ 0056d2a8 ["CALL", null, ["callee:00c5a070:8"]]
- 0056d268 bytes 82b21b94
+ 0056d2a8 bytes 72b31b94
~~~


<a id="compare-b0967e99becd507c7418e7b36e2db336"></a>

### [`0056d2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d2a0.md) → [`0056d2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d2e0.md) FUN_0056d2e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) [`0056893c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/0056893c.md) [`005692f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005692f4.md) [`0056d02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d02c.md) [`0056d16c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d16c.md) · 呼出先 2件 [`0056d3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d3f8.md) [`00c59c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c70.md)
- 新版 呼出元 6件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) [`0056897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/0056897c.md) [`00569334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569334.md) [`0056d06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d06c.md) [`0056d1ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d1ac.md) · 呼出先 2件 [`0056d438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d438.md) [`00c5a070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a070.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056d2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d2a0.md#insn-0056d2e0) · [`0056d328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d2a0.md#insn-0056d328) · [`0056d370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d2a0.md#insn-0056d370)
- 新版 [`0056d320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d2e0.md#insn-0056d320) · [`0056d368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d2e0.md#insn-0056d368) · [`0056d3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d2e0.md#insn-0056d3b0)

~~~diff
- 0056d2e0 ["INT_ADD", "register:40f0:8", ["const:56d2e0:8", "const:4:8"]]
- 0056d2e0 ["CALL", null, ["callee:00c5a070:8"]]
+ 0056d320 ["INT_ADD", "register:40f0:8", ["const:56d320:8", "const:4:8"]]
+ 0056d320 ["CALL", null, ["callee:00c5a070:8"]]
- 0056d2e0 bytes 64b21b94
+ 0056d320 bytes 54b31b94
- 0056d328 ["INT_ADD", "register:40f0:8", ["const:56d328:8", "const:4:8"]]
- 0056d328 ["CALL", null, ["callee:00c5a070:8"]]
+ 0056d368 ["INT_ADD", "register:40f0:8", ["const:56d368:8", "const:4:8"]]
+ 0056d368 ["CALL", null, ["callee:00c5a070:8"]]
- 0056d328 bytes 52b21b94
+ 0056d368 bytes 42b31b94
- 0056d370 ["INT_ADD", "register:40f0:8", ["const:56d370:8", "const:4:8"]]
- 0056d370 ["CALL", null, ["callee:00c5a070:8"]]
+ 0056d3b0 ["INT_ADD", "register:40f0:8", ["const:56d3b0:8", "const:4:8"]]
+ 0056d3b0 ["CALL", null, ["callee:00c5a070:8"]]
- 0056d370 bytes 40b21b94
+ 0056d3b0 bytes 30b31b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9eb09706e56232e808aca9fdd9388fc"></a>

### [`0056d794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d794.md) → [`0056d7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d7d4.md) FUN_0056d7d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00565a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565a18.md) [`0056d93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d93c.md) [`0056ef10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056e/0056ef10.md) [`0056f164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f164.md) · 呼出先 1件 [`0056d02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d02c.md)
- 新版 呼出元 4件 [`00565a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md) [`0056d97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d97c.md) [`0056ef50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056e/0056ef50.md) [`0056f1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f1a4.md) · 呼出先 1件 [`0056d06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d06c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056d7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d794.md#insn-0056d7d0)
- 新版 [`0056d810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d7d4.md#insn-0056d810)

~~~diff
- 0056d7d0 ["INT_ADD", "register:40f0:8", ["const:56d7d0:8", "const:4:8"]]
- 0056d7d0 ["CALL", null, ["callee:0056d06c:8"]]
+ 0056d810 ["INT_ADD", "register:40f0:8", ["const:56d810:8", "const:4:8"]]
+ 0056d810 ["CALL", null, ["callee:0056d06c:8"]]
- 0056d7d0 bytes 17feff97
+ 0056d810 bytes 17feff97
~~~


<a id="compare-c64f0741dd5671023a4ed0b38191a620"></a>

### [`0056d93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d93c.md) → [`0056d97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d97c.md) FUN_0056d97c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00565a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565a18.md) · 呼出先 6件 [`0056d02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d02c.md) [`0056d794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d794.md) [`0056ef10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056e/0056ef10.md) [`0056f164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f164.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00565a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md) · 呼出先 6件 [`0056d06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d06c.md) [`0056d7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d7d4.md) [`0056ef50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056e/0056ef50.md) [`0056f1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f1a4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d93c.md#insn-0056dac0) · [`0056dc3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d93c.md#insn-0056dc3c) · [`0056ddb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d93c.md#insn-0056ddb0)
- 新版 [`0056db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d97c.md#insn-0056db00) · [`0056dc7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d97c.md#insn-0056dc7c) · [`0056ddf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d97c.md#insn-0056ddf0)

~~~diff
- 0056dac0 ["INT_ADD", "register:40f0:8", ["const:56dac0:8", "const:4:8"]]
- 0056dac0 ["CALL", null, ["callee:00c58090:8"]]
+ 0056db00 ["INT_ADD", "register:40f0:8", ["const:56db00:8", "const:4:8"]]
+ 0056db00 ["CALL", null, ["callee:00c58090:8"]]
- 0056dac0 bytes 74a81b94
+ 0056db00 bytes 64a91b94
- 0056dc3c ["INT_ADD", "register:40f0:8", ["const:56dc3c:8", "const:4:8"]]
- 0056dc3c ["CALL", null, ["callee:0056f1a4:8"]]
+ 0056dc7c ["INT_ADD", "register:40f0:8", ["const:56dc7c:8", "const:4:8"]]
+ 0056dc7c ["CALL", null, ["callee:0056f1a4:8"]]
- 0056dc3c bytes 4a050094
+ 0056dc7c bytes 4a050094
- 0056ddb0 ["INT_ADD", "register:40f0:8", ["const:56ddb0:8", "const:4:8"]]
- 0056ddb0 ["CALL", null, ["callee:0056f1a4:8"]]
+ 0056ddf0 ["INT_ADD", "register:40f0:8", ["const:56ddf0:8", "const:4:8"]]
+ 0056ddf0 ["CALL", null, ["callee:0056f1a4:8"]]
- 0056ddb0 bytes ed040094
+ 0056ddf0 bytes ed040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8452c6ef578b8eb35aef75610cb8c382"></a>

### [`0056ef10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056e/0056ef10.md) → [`0056ef50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056e/0056ef50.md) FUN_0056ef50

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056d93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d93c.md) · 呼出先 2件 [`0056d02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d02c.md) [`0056d794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d794.md)
- 新版 呼出元 1件 [`0056d97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d97c.md) · 呼出先 2件 [`0056d06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d06c.md) [`0056d7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d7d4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056efac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056e/0056ef10.md#insn-0056efac) · [`0056f01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056e/0056ef10.md#insn-0056f01c)
- 新版 [`0056efec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056e/0056ef50.md#insn-0056efec) · [`0056f05c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056e/0056ef50.md#insn-0056f05c)

~~~diff
- 0056efac ["INT_ADD", "register:40f0:8", ["const:56efac:8", "const:4:8"]]
- 0056efac ["CALL", null, ["callee:0056d06c:8"]]
+ 0056efec ["INT_ADD", "register:40f0:8", ["const:56efec:8", "const:4:8"]]
+ 0056efec ["CALL", null, ["callee:0056d06c:8"]]
- 0056efac bytes 20f8ff97
+ 0056efec bytes 20f8ff97
- 0056f01c ["INT_ADD", "register:40f0:8", ["const:56f01c:8", "const:4:8"]]
- 0056f01c ["CALL", null, ["callee:0056d7d4:8"]]
+ 0056f05c ["INT_ADD", "register:40f0:8", ["const:56f05c:8", "const:4:8"]]
+ 0056f05c ["CALL", null, ["callee:0056d7d4:8"]]
- 0056f01c bytes def9ff97
+ 0056f05c bytes def9ff97
~~~


<a id="compare-1d70474093e67ee167f09f4d24d3d8da"></a>

### [`0056f164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f164.md) → [`0056f1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f1a4.md) FUN_0056f1a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056d93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d93c.md) · 呼出先 2件 [`0056d02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d02c.md) [`0056d794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d794.md)
- 新版 呼出元 1件 [`0056d97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d97c.md) · 呼出先 2件 [`0056d06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d06c.md) [`0056d7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d7d4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056f1a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f164.md#insn-0056f1a8) · [`0056f228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f164.md#insn-0056f228)
- 新版 [`0056f1e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f1a4.md#insn-0056f1e8) · [`0056f268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f1a4.md#insn-0056f268)

~~~diff
- 0056f1a8 ["INT_ADD", "register:40f0:8", ["const:56f1a8:8", "const:4:8"]]
- 0056f1a8 ["CALL", null, ["callee:0056d06c:8"]]
+ 0056f1e8 ["INT_ADD", "register:40f0:8", ["const:56f1e8:8", "const:4:8"]]
+ 0056f1e8 ["CALL", null, ["callee:0056d06c:8"]]
- 0056f1a8 bytes a1f7ff97
+ 0056f1e8 bytes a1f7ff97
- 0056f228 ["INT_ADD", "register:40f0:8", ["const:56f228:8", "const:4:8"]]
- 0056f228 ["CALL", null, ["callee:0056d7d4:8"]]
+ 0056f268 ["INT_ADD", "register:40f0:8", ["const:56f268:8", "const:4:8"]]
+ 0056f268 ["CALL", null, ["callee:0056d7d4:8"]]
- 0056f228 bytes 5bf9ff97
+ 0056f268 bytes 5bf9ff97
~~~


<a id="compare-dc56098a1c939b378e90e2e00ebe45b1"></a>

### [`0056f4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f4f8.md) → [`0056f538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f538.md) FUN_0056f538

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) · 呼出先 1件 [`0056d2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d2a0.md)
- 新版 呼出元 1件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) · 呼出先 1件 [`0056d2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d2e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056f518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f4f8.md#insn-0056f518)
- 新版 [`0056f558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f538.md#insn-0056f558)

~~~diff
- 0056f518 ["INT_ADD", "register:40f0:8", ["const:56f518:8", "const:4:8"]]
- 0056f518 ["CALL", null, ["callee:0056d2e0:8"]]
+ 0056f558 ["INT_ADD", "register:40f0:8", ["const:56f558:8", "const:4:8"]]
+ 0056f558 ["CALL", null, ["callee:0056d2e0:8"]]
- 0056f518 bytes 62f7ff97
+ 0056f558 bytes 62f7ff97
~~~


<a id="compare-0b005310dea5f538a0d0961f86a21617"></a>

### [`0056f558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f558.md) → [`0056f598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f598.md) FUN_0056f598

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) · 呼出先 1件 [`0056d02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d02c.md)
- 新版 呼出元 1件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) · 呼出先 1件 [`0056d06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d06c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056f568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f558.md#insn-0056f568) · [`0056f578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f558.md#insn-0056f578) · [`0056f588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f558.md#insn-0056f588)
- 新版 [`0056f5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f598.md#insn-0056f5a8) · [`0056f5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f598.md#insn-0056f5b8) · [`0056f5c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f598.md#insn-0056f5c8)

~~~diff
- 0056f568 ["INT_ADD", "register:40f0:8", ["const:56f568:8", "const:4:8"]]
- 0056f568 ["CALL", null, ["callee:0056d06c:8"]]
+ 0056f5a8 ["INT_ADD", "register:40f0:8", ["const:56f5a8:8", "const:4:8"]]
+ 0056f5a8 ["CALL", null, ["callee:0056d06c:8"]]
- 0056f568 bytes b1f6ff97
+ 0056f5a8 bytes b1f6ff97
- 0056f578 ["INT_ADD", "register:40f0:8", ["const:56f578:8", "const:4:8"]]
- 0056f578 ["CALL", null, ["callee:0056d06c:8"]]
+ 0056f5b8 ["INT_ADD", "register:40f0:8", ["const:56f5b8:8", "const:4:8"]]
+ 0056f5b8 ["CALL", null, ["callee:0056d06c:8"]]
- 0056f578 bytes adf6ff97
+ 0056f5b8 bytes adf6ff97
- 0056f588 ["INT_ADD", "register:40f0:8", ["const:56f588:8", "const:4:8"]]
- 0056f588 ["CALL", null, ["callee:0056d06c:8"]]
+ 0056f5c8 ["INT_ADD", "register:40f0:8", ["const:56f5c8:8", "const:4:8"]]
+ 0056f5c8 ["CALL", null, ["callee:0056d06c:8"]]
- 0056f588 bytes a9f6ff97
+ 0056f5c8 bytes a9f6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58521f07e99dd15cb7279368728f8928"></a>

### [`0056f604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f604.md) → [`0056f644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f644.md) FUN_0056f644

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) · 呼出先 2件 [`00c59c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c50.md) [`00c59c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c60.md)
- 新版 呼出元 1件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) · 呼出先 2件 [`00c5a050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a050.md) [`00c5a060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056f650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056f604.md#insn-0056f650)
- 新版 [`0056f690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056f644.md#insn-0056f690)

~~~diff
- 0056f650 ["INT_ADD", "register:40f0:8", ["const:56f650:8", "const:4:8"]]
- 0056f650 ["CALL", null, ["callee:00c5a050:8"]]
+ 0056f690 ["INT_ADD", "register:40f0:8", ["const:56f690:8", "const:4:8"]]
+ 0056f690 ["CALL", null, ["callee:00c5a050:8"]]
- 0056f650 bytes 80a91b94
+ 0056f690 bytes 70aa1b94
~~~


<a id="compare-ed948b7a5b1b2397717555e7b02400dd"></a>

### [`0056fbbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056fbbc.md) → [`0056fbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056fbfc.md) FUN_0056fbfc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) · 呼出先 1件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 1件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) · 呼出先 1件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056fbdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056fbbc.md#insn-0056fbdc)
- 新版 [`0056fc1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056fbfc.md#insn-0056fc1c)

~~~diff
- 0056fbdc ["INT_ADD", "register:40f0:8", ["const:56fbdc:8", "const:4:8"]]
- 0056fbdc ["CALL", null, ["callee:00c58090:8"]]
+ 0056fc1c ["INT_ADD", "register:40f0:8", ["const:56fc1c:8", "const:4:8"]]
+ 0056fc1c ["CALL", null, ["callee:00c58090:8"]]
- 0056fbdc bytes 2da01b94
+ 0056fc1c bytes 1da11b94
~~~


<a id="compare-f25d412d4f7e71b764ccbcb4f25f8f24"></a>

### [`0056fc88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056fc88.md) → [`0056fcc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056fcc8.md) FUN_0056fcc8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) · 呼出先 3件 [`00c58040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58040.md) [`00c59be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59be0.md) [`00c59d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d10.md)
- 新版 呼出元 1件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) · 呼出先 3件 [`00c58440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58440.md) [`00c59fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59fe0.md) [`00c5a110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0056fcac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056fc88.md#insn-0056fcac) · [`0056fcb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056fc88.md#insn-0056fcb8) · [`0056fce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056fc88.md#insn-0056fce0)
- 新版 [`0056fcec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056fcc8.md#insn-0056fcec) · [`0056fcf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056fcc8.md#insn-0056fcf8) · [`0056fd20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056fcc8.md#insn-0056fd20)

~~~diff
- 0056fcac ["INT_ADD", "register:40f0:8", ["const:56fcac:8", "const:4:8"]]
- 0056fcac ["CALL", null, ["callee:00c59fe0:8"]]
+ 0056fcec ["INT_ADD", "register:40f0:8", ["const:56fcec:8", "const:4:8"]]
+ 0056fcec ["CALL", null, ["callee:00c59fe0:8"]]
- 0056fcac bytes cda71b94
+ 0056fcec bytes bda81b94
- 0056fcb8 ["INT_ADD", "register:40f0:8", ["const:56fcb8:8", "const:4:8"]]
- 0056fcb8 ["CALL", null, ["callee:00c5a110:8"]]
+ 0056fcf8 ["INT_ADD", "register:40f0:8", ["const:56fcf8:8", "const:4:8"]]
+ 0056fcf8 ["CALL", null, ["callee:00c5a110:8"]]
- 0056fcb8 bytes 16a81b94
+ 0056fcf8 bytes 06a91b94
- 0056fce0 ["INT_ADD", "register:40f0:8", ["const:56fce0:8", "const:4:8"]]
- 0056fce0 ["CALL", null, ["callee:00c58440:8"]]
+ 0056fd20 ["INT_ADD", "register:40f0:8", ["const:56fd20:8", "const:4:8"]]
+ 0056fd20 ["CALL", null, ["callee:00c58440:8"]]
- 0056fce0 bytes d8a01b94
+ 0056fd20 bytes c8a11b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62fd3eec6e7b0931bbe846303f998676"></a>

### [`00570908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570908.md) → [`00570948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570948.md) FUN_00570948

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0056893c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/0056893c.md) · 呼出先 6件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c10.md) [`00c59c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c50.md) [`00c59c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c60.md) [`00c59c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c80.md)
- 新版 呼出元 1件 [`0056897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/0056897c.md) · 呼出先 6件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a010.md) [`00c5a050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a050.md) [`00c5a060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a060.md) [`00c5a080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a080.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00570960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570908.md#insn-00570960) · [`005709b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570908.md#insn-005709b0) · [`00570a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570908.md#insn-00570a44)
- 新版 [`005709a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570948.md#insn-005709a0) · [`005709f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570948.md#insn-005709f0) · [`00570a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570948.md#insn-00570a84)

~~~diff
- 00570960 ["INT_ADD", "register:40f0:8", ["const:570960:8", "const:4:8"]]
- 00570960 ["CALL", null, ["callee:00c5a050:8"]]
+ 005709a0 ["INT_ADD", "register:40f0:8", ["const:5709a0:8", "const:4:8"]]
+ 005709a0 ["CALL", null, ["callee:00c5a050:8"]]
- 00570960 bytes bca41b94
+ 005709a0 bytes aca51b94
- 005709b0 ["INT_ADD", "register:40f0:8", ["const:5709b0:8", "const:4:8"]]
- 005709b0 ["CALL", null, ["callee:00c5a080:8"]]
+ 005709f0 ["INT_ADD", "register:40f0:8", ["const:5709f0:8", "const:4:8"]]
+ 005709f0 ["CALL", null, ["callee:00c5a080:8"]]
- 005709b0 bytes b4a41b94
+ 005709f0 bytes a4a51b94
- 00570a44 ["INT_ADD", "register:40f0:8", ["const:570a44:8", "const:4:8"]]
- 00570a44 ["CALL", null, ["callee:00c5a130:8"]]
+ 00570a84 ["INT_ADD", "register:40f0:8", ["const:570a84:8", "const:4:8"]]
+ 00570a84 ["CALL", null, ["callee:00c5a130:8"]]
- 00570a44 bytes bba41b94
+ 00570a84 bytes aba51b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d73e83459204b1fbf67398a9784c829"></a>

### [`00570e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570e04.md) → [`00570e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570e44.md) FUN_00570e44

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056ab28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056ab28.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00570f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570f60.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0056ab68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056ab68.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00570fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570fa0.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00570e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570e04.md#insn-00570e70) · [`00570e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570e04.md#insn-00570e9c) · [`00570efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570e04.md#insn-00570efc)
- 新版 [`00570eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570e44.md#insn-00570eb0) · [`00570edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570e44.md#insn-00570edc) · [`00570f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570e44.md#insn-00570f3c)

~~~diff
- 00570e70 ["INT_ADD", "register:40f0:8", ["const:570e70:8", "const:4:8"]]
- 00570e70 ["CALL", null, ["callee:00c57e90:8"]]
+ 00570eb0 ["INT_ADD", "register:40f0:8", ["const:570eb0:8", "const:4:8"]]
+ 00570eb0 ["CALL", null, ["callee:00c57e90:8"]]
- 00570e70 bytes 089b1b94
+ 00570eb0 bytes f89b1b94
- 00570e9c ["INT_ADD", "register:40f0:8", ["const:570e9c:8", "const:4:8"]]
- 00570e9c ["CALL", null, ["callee:00c53cd0:8"]]
+ 00570edc ["INT_ADD", "register:40f0:8", ["const:570edc:8", "const:4:8"]]
+ 00570edc ["CALL", null, ["callee:00c53cd0:8"]]
- 00570e9c bytes 858a1b94
+ 00570edc bytes 7d8b1b94
- 00570efc ["INT_ADD", "register:40f0:8", ["const:570efc:8", "const:4:8"]]
- 00570efc ["CALL", null, ["callee:00c53d00:8"]]
+ 00570f3c ["INT_ADD", "register:40f0:8", ["const:570f3c:8", "const:4:8"]]
+ 00570f3c ["CALL", null, ["callee:00c53d00:8"]]
- 00570efc bytes 798a1b94
+ 00570f3c bytes 718b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-268a40957bc82be26d3a1137b00b1c54"></a>

### [`00571034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571034.md) → [`00571074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571074.md) FUN_00571074

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0056b690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b690.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0056b6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b6d0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00571048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571034.md#insn-00571048) · [`0057105c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571034.md#insn-0057105c) · [`0057107c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571034.md#insn-0057107c)
- 新版 [`00571088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571074.md#insn-00571088) · [`0057109c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571074.md#insn-0057109c) · [`005710bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571074.md#insn-005710bc)

~~~diff
- 00571048 ["INT_ADD", "register:40f0:8", ["const:571048:8", "const:4:8"]]
- 00571048 ["CALL", null, ["callee:0056b6d0:8"]]
+ 00571088 ["INT_ADD", "register:40f0:8", ["const:571088:8", "const:4:8"]]
+ 00571088 ["CALL", null, ["callee:0056b6d0:8"]]
- 00571048 bytes 92e9ff97
+ 00571088 bytes 92e9ff97
- 0057105c ["INT_ADD", "register:40f0:8", ["const:57105c:8", "const:4:8"]]
- 0057105c ["CALL", null, ["callee:00c53d00:8"]]
+ 0057109c ["INT_ADD", "register:40f0:8", ["const:57109c:8", "const:4:8"]]
+ 0057109c ["CALL", null, ["callee:00c53d00:8"]]
- 0057105c bytes 218a1b94
+ 0057109c bytes 198b1b94
- 0057107c ["COPY", "register:0:8", ["register:4040:8"]]
- 0057107c ["INT_ADD", "register:40f0:8", ["const:57107c:8", "const:4:8"]]
- 0057107c ["CALLIND", null, ["register:0:8"]]
+ 005710bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005710bc ["INT_ADD", "register:40f0:8", ["const:5710bc:8", "const:4:8"]]
+ 005710bc ["CALLIND", null, ["register:0:8"]]
- 0057107c bytes 00013fd6
+ 005710bc bytes 00013fd6
~~~


<a id="compare-59598b01e724eed8ee9fdf3237df1de5"></a>

### [`00571174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571174.md) → [`005711b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005711b4.md) FUN_005711b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0056b690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b690.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0056b6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b6d0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00571188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571174.md#insn-00571188) · [`0057119c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571174.md#insn-0057119c) · [`005711bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571174.md#insn-005711bc)
- 新版 [`005711c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005711b4.md#insn-005711c8) · [`005711dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005711b4.md#insn-005711dc) · [`005711fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005711b4.md#insn-005711fc)

~~~diff
- 00571188 ["INT_ADD", "register:40f0:8", ["const:571188:8", "const:4:8"]]
- 00571188 ["CALL", null, ["callee:0056b6d0:8"]]
+ 005711c8 ["INT_ADD", "register:40f0:8", ["const:5711c8:8", "const:4:8"]]
+ 005711c8 ["CALL", null, ["callee:0056b6d0:8"]]
- 00571188 bytes 42e9ff97
+ 005711c8 bytes 42e9ff97
- 0057119c ["INT_ADD", "register:40f0:8", ["const:57119c:8", "const:4:8"]]
- 0057119c ["CALL", null, ["callee:00c53d00:8"]]
+ 005711dc ["INT_ADD", "register:40f0:8", ["const:5711dc:8", "const:4:8"]]
+ 005711dc ["CALL", null, ["callee:00c53d00:8"]]
- 0057119c bytes d1891b94
+ 005711dc bytes c98a1b94
- 005711bc ["COPY", "register:0:8", ["register:4040:8"]]
- 005711bc ["INT_ADD", "register:40f0:8", ["const:5711bc:8", "const:4:8"]]
- 005711bc ["CALLIND", null, ["register:0:8"]]
+ 005711fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005711fc ["INT_ADD", "register:40f0:8", ["const:5711fc:8", "const:4:8"]]
+ 005711fc ["CALLIND", null, ["register:0:8"]]
- 005711bc bytes 00013fd6
+ 005711fc bytes 00013fd6
~~~


<a id="compare-8ea7f2ae873f34dfa239536d4552c54e"></a>

### [`005717c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005717c0.md) → [`00571800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571800.md) FUN_00571800

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0055094c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/0055094c.md) · 呼出先 8件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`0055098c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/0055098c.md) · 呼出先 8件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005717e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005717c0.md#insn-005717e0) · [`005717e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005717c0.md#insn-005717e8) · [`0057182c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005717c0.md#insn-0057182c)
- 新版 [`00571820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571800.md#insn-00571820) · [`00571828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571800.md#insn-00571828) · [`0057186c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571800.md#insn-0057186c)

~~~diff
- 005717e0 ["INT_ADD", "register:40f0:8", ["const:5717e0:8", "const:4:8"]]
- 005717e0 ["CALL", null, ["callee:00588e6c:8"]]
+ 00571820 ["INT_ADD", "register:40f0:8", ["const:571820:8", "const:4:8"]]
+ 00571820 ["CALL", null, ["callee:00588e6c:8"]]
- 005717e0 bytes 935d0094
+ 00571820 bytes 935d0094
- 005717e8 ["INT_ADD", "register:40f0:8", ["const:5717e8:8", "const:4:8"]]
- 005717e8 ["CALL", null, ["callee:0058915c:8"]]
+ 00571828 ["INT_ADD", "register:40f0:8", ["const:571828:8", "const:4:8"]]
+ 00571828 ["CALL", null, ["callee:0058915c:8"]]
- 005717e8 bytes 4d5e0094
+ 00571828 bytes 4d5e0094
- 0057182c ["INT_ADD", "register:40f0:8", ["const:57182c:8", "const:4:8"]]
- 0057182c ["CALL", null, ["callee:00589320:8"]]
+ 0057186c ["INT_ADD", "register:40f0:8", ["const:57186c:8", "const:4:8"]]
+ 0057186c ["CALL", null, ["callee:00589320:8"]]
- 0057182c bytes ad5e0094
+ 0057186c bytes ad5e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78d510da210b1d70e636187be9348008"></a>

### [`00572824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572824.md) → [`00572864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572864.md) FUN_00572864

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00572840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572824.md#insn-00572840) · [`00572860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572824.md#insn-00572860)
- 新版 [`00572880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572864.md#insn-00572880) · [`005728a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572864.md#insn-005728a0)

~~~diff
- 00572840 ["INT_ADD", "register:40f0:8", ["const:572840:8", "const:4:8"]]
- 00572840 ["CALL", null, ["callee:00c53d00:8"]]
+ 00572880 ["INT_ADD", "register:40f0:8", ["const:572880:8", "const:4:8"]]
+ 00572880 ["CALL", null, ["callee:00c53d00:8"]]
- 00572840 bytes 28841b94
+ 00572880 bytes 20851b94
- 00572860 ["COPY", "register:0:8", ["register:4040:8"]]
- 00572860 ["INT_ADD", "register:40f0:8", ["const:572860:8", "const:4:8"]]
- 00572860 ["CALLIND", null, ["register:0:8"]]
+ 005728a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005728a0 ["INT_ADD", "register:40f0:8", ["const:5728a0:8", "const:4:8"]]
+ 005728a0 ["CALLIND", null, ["register:0:8"]]
- 00572860 bytes 00013fd6
+ 005728a0 bytes 00013fd6
~~~


<a id="compare-c21b9351f6c11e5225abdf0950e5ec74"></a>

### [`005743e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005743e4.md) → [`00574424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574424.md) FUN_00574424

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005746e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005746e8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00574728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574728.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057440c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005743e4.md#insn-0057440c) · [`00574430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005743e4.md#insn-00574430)
- 新版 [`0057444c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574424.md#insn-0057444c) · [`00574470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574424.md#insn-00574470)

~~~diff
- 0057440c ["INT_ADD", "register:40f0:8", ["const:57440c:8", "const:4:8"]]
- 0057440c ["CALL", null, ["callee:00574728:8"]]
+ 0057444c ["INT_ADD", "register:40f0:8", ["const:57444c:8", "const:4:8"]]
+ 0057444c ["CALL", null, ["callee:00574728:8"]]
- 0057440c bytes b7000094
+ 0057444c bytes b7000094
- 00574430 ["INT_ADD", "register:40f0:8", ["const:574430:8", "const:4:8"]]
- 00574430 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00574470 ["INT_ADD", "register:40f0:8", ["const:574470:8", "const:4:8"]]
+ 00574470 ["CALL", null, ["callee:00c57ee0:8"]]
- 00574430 bytes ac8d1b94
+ 00574470 bytes 9c8e1b94
~~~


<a id="compare-9c40a3b0f3e2e5b2b44e8dc644b4973e"></a>

### [`005747c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005747c8.md) → [`00574808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574808.md) FUN_00574808

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00574a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574a8c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00574acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574acc.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005747f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005747c8.md#insn-005747f0) · [`00574814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005747c8.md#insn-00574814)
- 新版 [`00574830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574808.md#insn-00574830) · [`00574854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574808.md#insn-00574854)

~~~diff
- 005747f0 ["INT_ADD", "register:40f0:8", ["const:5747f0:8", "const:4:8"]]
- 005747f0 ["CALL", null, ["callee:00574acc:8"]]
+ 00574830 ["INT_ADD", "register:40f0:8", ["const:574830:8", "const:4:8"]]
+ 00574830 ["CALL", null, ["callee:00574acc:8"]]
- 005747f0 bytes a7000094
+ 00574830 bytes a7000094
- 00574814 ["INT_ADD", "register:40f0:8", ["const:574814:8", "const:4:8"]]
- 00574814 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00574854 ["INT_ADD", "register:40f0:8", ["const:574854:8", "const:4:8"]]
+ 00574854 ["CALL", null, ["callee:00c57ee0:8"]]
- 00574814 bytes b38c1b94
+ 00574854 bytes a38d1b94
~~~


<a id="compare-b6792394dfafa1868e3169e40a5e0fbc"></a>

### [`00574a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574a2c.md) → [`00574a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574a6c.md) FUN_00574a6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574a2c.md#insn-00574a48)
- 新版 [`00574a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574a6c.md#insn-00574a88)

~~~diff
- 00574a48 ["INT_ADD", "register:40f0:8", ["const:574a48:8", "const:4:8"]]
- 00574a48 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00574a88 ["INT_ADD", "register:40f0:8", ["const:574a88:8", "const:4:8"]]
+ 00574a88 ["CALL", null, ["callee:00c53cd0:8"]]
- 00574a48 bytes 9a7b1b94
+ 00574a88 bytes 927c1b94
~~~


<a id="compare-8a1c4e02e21f9ae03a953dbc48f1a9f2"></a>

### [`00574a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574a54.md) → [`00574a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574a94.md) FUN_00574a94

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574a54.md#insn-00574a70)
- 新版 [`00574ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574a94.md#insn-00574ab0)

~~~diff
- 00574a70 ["INT_ADD", "register:40f0:8", ["const:574a70:8", "const:4:8"]]
- 00574a70 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00574ab0 ["INT_ADD", "register:40f0:8", ["const:574ab0:8", "const:4:8"]]
+ 00574ab0 ["CALL", null, ["callee:00c53cd0:8"]]
- 00574a70 bytes 907b1b94
+ 00574ab0 bytes 887c1b94
~~~


<a id="compare-5abda78c54f7c398469cb90f1c6a78c6"></a>

### [`00574c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574c3c.md) → [`00574c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574c7c.md) FUN_00574c7c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005717b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005717b8.md) [`00574c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574c3c.md) · 呼出先 2件 [`00574c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574c3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`005717f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005717f8.md) [`00574c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574c7c.md) · 呼出先 2件 [`00574c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574c7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574c3c.md#insn-00574c58) · [`00574c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574c3c.md#insn-00574c64) · [`00574c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574c3c.md#insn-00574c98)
- 新版 [`00574c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574c7c.md#insn-00574c98) · [`00574ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574c7c.md#insn-00574ca4) · [`00574cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574c7c.md#insn-00574cd8)

~~~diff
- 00574c58 ["INT_ADD", "register:40f0:8", ["const:574c58:8", "const:4:8"]]
- 00574c58 ["CALL", null, ["local:b0:8"]]
+ 00574c98 ["INT_ADD", "register:40f0:8", ["const:574c98:8", "const:4:8"]]
+ 00574c98 ["CALL", null, ["local:b0:8"]]
- 00574c58 bytes f9ffff97
+ 00574c98 bytes f9ffff97
- 00574c64 ["INT_ADD", "register:40f0:8", ["const:574c64:8", "const:4:8"]]
- 00574c64 ["CALL", null, ["local:b0:8"]]
+ 00574ca4 ["INT_ADD", "register:40f0:8", ["const:574ca4:8", "const:4:8"]]
+ 00574ca4 ["CALL", null, ["local:b0:8"]]
- 00574c64 bytes f6ffff97
+ 00574ca4 bytes f6ffff97
- 00574c98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00574c98 ["INT_ADD", "register:40f0:8", ["const:574c98:8", "const:4:8"]]
- 00574c98 ["CALLIND", null, ["register:0:8"]]
+ 00574cd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574cd8 ["INT_ADD", "register:40f0:8", ["const:574cd8:8", "const:4:8"]]
+ 00574cd8 ["CALLIND", null, ["register:0:8"]]
- 00574c98 bytes 00013fd6
+ 00574cd8 bytes 00013fd6
~~~


<a id="compare-906cde9c2de37a88a25feb03bd8113fc"></a>

### [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) → [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) FUN_00574cec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 96件 [`00571ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571ab4.md) [`00571dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571dd8.md) [`005720b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/005720b8.md) [`0057226c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/0057226c.md) [`00572420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572420.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 96件 [`00571af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571af4.md) [`00571e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571e18.md) [`005720f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005720f8.md) [`005722ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005722ac.md) [`00572460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572460.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md#insn-00574d20) · [`00574d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md#insn-00574d44)
- 新版 [`00574d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md#insn-00574d60) · [`00574d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md#insn-00574d84)

~~~diff
- 00574d20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00574d20 ["INT_ADD", "register:40f0:8", ["const:574d20:8", "const:4:8"]]
- 00574d20 ["CALLIND", null, ["register:0:8"]]
+ 00574d60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574d60 ["INT_ADD", "register:40f0:8", ["const:574d60:8", "const:4:8"]]
+ 00574d60 ["CALLIND", null, ["register:0:8"]]
- 00574d20 bytes 00013fd6
+ 00574d60 bytes 00013fd6
- 00574d44 ["INT_ADD", "register:40f0:8", ["const:574d44:8", "const:4:8"]]
- 00574d44 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00574d84 ["INT_ADD", "register:40f0:8", ["const:574d84:8", "const:4:8"]]
+ 00574d84 ["CALL", null, ["callee:00c57ee0:8"]]
- 00574d44 bytes 678b1b94
+ 00574d84 bytes 578c1b94
~~~


<a id="compare-b651666936a61e521a849f4acf318f82"></a>

### [`00574d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574d48.md) → [`00574d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574d88.md) FUN_00574d88

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00572420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572420.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00572460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572460.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574d48.md#insn-00574db4) · [`00574dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574d48.md#insn-00574dc4) · [`00574de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574d48.md#insn-00574de4)
- 新版 [`00574df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574d88.md#insn-00574df4) · [`00574e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574d88.md#insn-00574e04) · [`00574e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574d88.md#insn-00574e24)

~~~diff
- 00574db4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00574db4 ["INT_ADD", "register:40f0:8", ["const:574db4:8", "const:4:8"]]
- 00574db4 ["CALLIND", null, ["register:0:8"]]
+ 00574df4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574df4 ["INT_ADD", "register:40f0:8", ["const:574df4:8", "const:4:8"]]
+ 00574df4 ["CALLIND", null, ["register:0:8"]]
- 00574db4 bytes 00013fd6
+ 00574df4 bytes 00013fd6
- 00574dc4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00574dc4 ["INT_ADD", "register:40f0:8", ["const:574dc4:8", "const:4:8"]]
- 00574dc4 ["CALLIND", null, ["register:0:8"]]
+ 00574e04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574e04 ["INT_ADD", "register:40f0:8", ["const:574e04:8", "const:4:8"]]
+ 00574e04 ["CALLIND", null, ["register:0:8"]]
- 00574dc4 bytes 00013fd6
+ 00574e04 bytes 00013fd6
- 00574de4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00574de4 ["INT_ADD", "register:40f0:8", ["const:574de4:8", "const:4:8"]]
- 00574de4 ["CALLIND", null, ["register:0:8"]]
+ 00574e24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574e24 ["INT_ADD", "register:40f0:8", ["const:574e24:8", "const:4:8"]]
+ 00574e24 ["CALLIND", null, ["register:0:8"]]
- 00574de4 bytes 00013fd6
+ 00574e24 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efbe8434130e2fe86dbbe66eda220e40"></a>

### [`00574eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574eb0.md) → [`00574ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574ef0.md) FUN_00574ef0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00572b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572b60.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00572ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572ba0.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574eb0.md#insn-00574f1c) · [`00574f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574eb0.md#insn-00574f2c) · [`00574f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574eb0.md#insn-00574f4c)
- 新版 [`00574f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574ef0.md#insn-00574f5c) · [`00574f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574ef0.md#insn-00574f6c) · [`00574f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574ef0.md#insn-00574f8c)

~~~diff
- 00574f1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00574f1c ["INT_ADD", "register:40f0:8", ["const:574f1c:8", "const:4:8"]]
- 00574f1c ["CALLIND", null, ["register:0:8"]]
+ 00574f5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574f5c ["INT_ADD", "register:40f0:8", ["const:574f5c:8", "const:4:8"]]
+ 00574f5c ["CALLIND", null, ["register:0:8"]]
- 00574f1c bytes 00013fd6
+ 00574f5c bytes 00013fd6
- 00574f2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00574f2c ["INT_ADD", "register:40f0:8", ["const:574f2c:8", "const:4:8"]]
- 00574f2c ["CALLIND", null, ["register:0:8"]]
+ 00574f6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574f6c ["INT_ADD", "register:40f0:8", ["const:574f6c:8", "const:4:8"]]
+ 00574f6c ["CALLIND", null, ["register:0:8"]]
- 00574f2c bytes 00013fd6
+ 00574f6c bytes 00013fd6
- 00574f4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00574f4c ["INT_ADD", "register:40f0:8", ["const:574f4c:8", "const:4:8"]]
- 00574f4c ["CALLIND", null, ["register:0:8"]]
+ 00574f8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00574f8c ["INT_ADD", "register:40f0:8", ["const:574f8c:8", "const:4:8"]]
+ 00574f8c ["CALLIND", null, ["register:0:8"]]
- 00574f4c bytes 00013fd6
+ 00574f8c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44014ad251b71e021a2d67ea9cec9ded"></a>

### [`00575018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575018.md) → [`00575058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575058.md) FUN_00575058

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057506c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575018.md#insn-0057506c) · [`00575080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575018.md#insn-00575080) · [`00575088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575018.md#insn-00575088)
- 新版 [`005750ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575058.md#insn-005750ac) · [`005750c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575058.md#insn-005750c0) · [`005750c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575058.md#insn-005750c8)

~~~diff
- 0057506c ["INT_ADD", "register:40f0:8", ["const:57506c:8", "const:4:8"]]
- 0057506c ["CALL", null, ["callee:00c53d00:8"]]
+ 005750ac ["INT_ADD", "register:40f0:8", ["const:5750ac:8", "const:4:8"]]
+ 005750ac ["CALL", null, ["callee:00c53d00:8"]]
- 0057506c bytes 1d7a1b94
+ 005750ac bytes 157b1b94
- 00575080 ["COPY", "register:0:8", ["register:4040:8"]]
- 00575080 ["INT_ADD", "register:40f0:8", ["const:575080:8", "const:4:8"]]
- 00575080 ["CALLIND", null, ["register:0:8"]]
+ 005750c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005750c0 ["INT_ADD", "register:40f0:8", ["const:5750c0:8", "const:4:8"]]
+ 005750c0 ["CALLIND", null, ["register:0:8"]]
- 00575080 bytes 00013fd6
+ 005750c0 bytes 00013fd6
- 00575088 ["INT_ADD", "register:40f0:8", ["const:575088:8", "const:4:8"]]
- 00575088 ["CALL", null, ["callee:00c57e80:8"]]
+ 005750c8 ["INT_ADD", "register:40f0:8", ["const:5750c8:8", "const:4:8"]]
+ 005750c8 ["CALL", null, ["callee:00c57e80:8"]]
- 00575088 bytes 7e8a1b94
+ 005750c8 bytes 6e8b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca7d0fbfe01827c99f27138f9fb7f102"></a>

### [`005750c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005750c0.md) → [`00575100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575100.md) FUN_00575100

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005750d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005750c0.md#insn-005750d0)
- 新版 [`00575110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575100.md#insn-00575110)

~~~diff
- 005750d0 ["INT_ADD", "register:40f0:8", ["const:5750d0:8", "const:4:8"]]
- 005750d0 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00575110 ["INT_ADD", "register:40f0:8", ["const:575110:8", "const:4:8"]]
+ 00575110 ["CALL", null, ["callee:00c57ea0:8"]]
- 005750d0 bytes 748a1b94
+ 00575110 bytes 648b1b94
~~~


<a id="compare-9162f6ff666756511fece23c4a9eefa4"></a>

### [`005750e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005750e4.md) → [`00575124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575124.md) FUN_00575124

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00572c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572c28.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00572c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572c68.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00575134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005750e4.md#insn-00575134) · [`00575148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005750e4.md#insn-00575148) · [`00575150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005750e4.md#insn-00575150)
- 新版 [`00575174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575124.md#insn-00575174) · [`00575188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575124.md#insn-00575188) · [`00575190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575124.md#insn-00575190)

~~~diff
- 00575134 ["INT_ADD", "register:40f0:8", ["const:575134:8", "const:4:8"]]
- 00575134 ["CALL", null, ["callee:00c53d00:8"]]
+ 00575174 ["INT_ADD", "register:40f0:8", ["const:575174:8", "const:4:8"]]
+ 00575174 ["CALL", null, ["callee:00c53d00:8"]]
- 00575134 bytes eb791b94
+ 00575174 bytes e37a1b94
- 00575148 ["COPY", "register:0:8", ["register:4040:8"]]
- 00575148 ["INT_ADD", "register:40f0:8", ["const:575148:8", "const:4:8"]]
- 00575148 ["CALLIND", null, ["register:0:8"]]
+ 00575188 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00575188 ["INT_ADD", "register:40f0:8", ["const:575188:8", "const:4:8"]]
+ 00575188 ["CALLIND", null, ["register:0:8"]]
- 00575148 bytes 00013fd6
+ 00575188 bytes 00013fd6
- 00575150 ["INT_ADD", "register:40f0:8", ["const:575150:8", "const:4:8"]]
- 00575150 ["CALL", null, ["callee:00c57e80:8"]]
+ 00575190 ["INT_ADD", "register:40f0:8", ["const:575190:8", "const:4:8"]]
+ 00575190 ["CALL", null, ["callee:00c57e80:8"]]
- 00575150 bytes 4c8a1b94
+ 00575190 bytes 3c8b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2480a90434fef644ea150f2ab326df9b"></a>

### [`005751a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005751a8.md) → [`005751e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005751e8.md) FUN_005751e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00572c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572c28.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00575304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575304.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00572c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572c68.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00575344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575344.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00575214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005751a8.md#insn-00575214) · [`00575240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005751a8.md#insn-00575240) · [`005752a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005751a8.md#insn-005752a0)
- 新版 [`00575254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005751e8.md#insn-00575254) · [`00575280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005751e8.md#insn-00575280) · [`005752e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005751e8.md#insn-005752e0)

~~~diff
- 00575214 ["INT_ADD", "register:40f0:8", ["const:575214:8", "const:4:8"]]
- 00575214 ["CALL", null, ["callee:00c57e90:8"]]
+ 00575254 ["INT_ADD", "register:40f0:8", ["const:575254:8", "const:4:8"]]
+ 00575254 ["CALL", null, ["callee:00c57e90:8"]]
- 00575214 bytes 1f8a1b94
+ 00575254 bytes 0f8b1b94
- 00575240 ["INT_ADD", "register:40f0:8", ["const:575240:8", "const:4:8"]]
- 00575240 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00575280 ["INT_ADD", "register:40f0:8", ["const:575280:8", "const:4:8"]]
+ 00575280 ["CALL", null, ["callee:00c53cd0:8"]]
- 00575240 bytes 9c791b94
+ 00575280 bytes 947a1b94
- 005752a0 ["INT_ADD", "register:40f0:8", ["const:5752a0:8", "const:4:8"]]
- 005752a0 ["CALL", null, ["callee:00c53d00:8"]]
+ 005752e0 ["INT_ADD", "register:40f0:8", ["const:5752e0:8", "const:4:8"]]
+ 005752e0 ["CALL", null, ["callee:00c53d00:8"]]
- 005752a0 bytes 90791b94
+ 005752e0 bytes 887a1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4a4e8a91738b54678edd24b74501d3e"></a>

### [`00575d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575d4c.md) → [`00575d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575d8c.md) FUN_00575d8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00575548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575548.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 1件 [`00575588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575588.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00575d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575d4c.md#insn-00575d80) · [`00575dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575d4c.md#insn-00575dc8) · [`00575de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575d4c.md#insn-00575de8)
- 新版 [`00575dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575d8c.md#insn-00575dc0) · [`00575e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575d8c.md#insn-00575e08) · [`00575e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575d8c.md#insn-00575e28)

~~~diff
- 00575d80 ["INT_ADD", "register:40f0:8", ["const:575d80:8", "const:4:8"]]
- 00575d80 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00575dc0 ["INT_ADD", "register:40f0:8", ["const:575dc0:8", "const:4:8"]]
+ 00575dc0 ["CALL", null, ["callee:00c57fe0:8"]]
- 00575d80 bytes 98871b94
+ 00575dc0 bytes 88881b94
- 00575dc8 ["INT_ADD", "register:40f0:8", ["const:575dc8:8", "const:4:8"]]
- 00575dc8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00575e08 ["INT_ADD", "register:40f0:8", ["const:575e08:8", "const:4:8"]]
+ 00575e08 ["CALL", null, ["callee:00c57e90:8"]]
- 00575dc8 bytes 32871b94
+ 00575e08 bytes 22881b94
- 00575de8 ["INT_ADD", "register:40f0:8", ["const:575de8:8", "const:4:8"]]
- 00575de8 ["CALL", null, ["callee:00c57f40:8"]]
+ 00575e28 ["INT_ADD", "register:40f0:8", ["const:575e28:8", "const:4:8"]]
+ 00575e28 ["CALL", null, ["callee:00c57f40:8"]]
- 00575de8 bytes 56871b94
+ 00575e28 bytes 46881b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e747329b6446f47253dbbf4571cafb1"></a>

### [`00575f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575f58.md) → [`00575f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575f98.md) FUN_00575f98

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00575548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575548.md) · 呼出先 5件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 1件 [`00575588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575588.md) · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00575f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575f58.md#insn-00575f8c) · [`00575fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575f58.md#insn-00575fd4) · [`00575ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575f58.md#insn-00575ff4)
- 新版 [`00575fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575f98.md#insn-00575fcc) · [`00576014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575f98.md#insn-00576014) · [`00576034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575f98.md#insn-00576034)

~~~diff
- 00575f8c ["INT_ADD", "register:40f0:8", ["const:575f8c:8", "const:4:8"]]
- 00575f8c ["CALL", null, ["callee:00c57fe0:8"]]
+ 00575fcc ["INT_ADD", "register:40f0:8", ["const:575fcc:8", "const:4:8"]]
+ 00575fcc ["CALL", null, ["callee:00c57fe0:8"]]
- 00575f8c bytes 15871b94
+ 00575fcc bytes 05881b94
- 00575fd4 ["INT_ADD", "register:40f0:8", ["const:575fd4:8", "const:4:8"]]
- 00575fd4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00576014 ["INT_ADD", "register:40f0:8", ["const:576014:8", "const:4:8"]]
+ 00576014 ["CALL", null, ["callee:00c57e90:8"]]
- 00575fd4 bytes af861b94
+ 00576014 bytes 9f871b94
- 00575ff4 ["INT_ADD", "register:40f0:8", ["const:575ff4:8", "const:4:8"]]
- 00575ff4 ["CALL", null, ["callee:00c57f40:8"]]
+ 00576034 ["INT_ADD", "register:40f0:8", ["const:576034:8", "const:4:8"]]
+ 00576034 ["CALL", null, ["callee:00c57f40:8"]]
- 00575ff4 bytes d3861b94
+ 00576034 bytes c3871b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-584aadb3f9ea8bdbe5c6fd766dc1ed35"></a>

### [`00576110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576110.md) → [`00576150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576150.md) FUN_00576150

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00575790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575790.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005757d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005757d0.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057617c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576110.md#insn-0057617c) · [`0057618c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576110.md#insn-0057618c) · [`005761ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576110.md#insn-005761ac)
- 新版 [`005761bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576150.md#insn-005761bc) · [`005761cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576150.md#insn-005761cc) · [`005761ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576150.md#insn-005761ec)

~~~diff
- 0057617c ["COPY", "register:0:8", ["register:4040:8"]]
- 0057617c ["INT_ADD", "register:40f0:8", ["const:57617c:8", "const:4:8"]]
- 0057617c ["CALLIND", null, ["register:0:8"]]
+ 005761bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005761bc ["INT_ADD", "register:40f0:8", ["const:5761bc:8", "const:4:8"]]
+ 005761bc ["CALLIND", null, ["register:0:8"]]
- 0057617c bytes 00013fd6
+ 005761bc bytes 00013fd6
- 0057618c ["COPY", "register:0:8", ["register:4040:8"]]
- 0057618c ["INT_ADD", "register:40f0:8", ["const:57618c:8", "const:4:8"]]
- 0057618c ["CALLIND", null, ["register:0:8"]]
+ 005761cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005761cc ["INT_ADD", "register:40f0:8", ["const:5761cc:8", "const:4:8"]]
+ 005761cc ["CALLIND", null, ["register:0:8"]]
- 0057618c bytes 00013fd6
+ 005761cc bytes 00013fd6
- 005761ac ["COPY", "register:0:8", ["register:4040:8"]]
- 005761ac ["INT_ADD", "register:40f0:8", ["const:5761ac:8", "const:4:8"]]
- 005761ac ["CALLIND", null, ["register:0:8"]]
+ 005761ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 005761ec ["INT_ADD", "register:40f0:8", ["const:5761ec:8", "const:4:8"]]
+ 005761ec ["CALLIND", null, ["register:0:8"]]
- 005761ac bytes 00013fd6
+ 005761ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f45c40c49b10ae11e64f1b1e19f668f"></a>

### [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) → [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) FUN_005762b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 26件 [`0057695c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057695c.md) [`005772d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005772d8.md) [`005778a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005778a0.md) [`00577c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577c40.md) [`0057a6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a6fc.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 26件 [`0057699c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/0057699c.md) [`00577318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577318.md) [`005778e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005778e0.md) [`00577c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577c80.md) [`0057a73c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a73c.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005762ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md#insn-005762ec) · [`00576310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md#insn-00576310)
- 新版 [`0057632c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md#insn-0057632c) · [`00576350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md#insn-00576350)

~~~diff
- 005762ec ["COPY", "register:0:8", ["register:4040:8"]]
- 005762ec ["INT_ADD", "register:40f0:8", ["const:5762ec:8", "const:4:8"]]
- 005762ec ["CALLIND", null, ["register:0:8"]]
+ 0057632c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057632c ["INT_ADD", "register:40f0:8", ["const:57632c:8", "const:4:8"]]
+ 0057632c ["CALLIND", null, ["register:0:8"]]
- 005762ec bytes 00013fd6
+ 0057632c bytes 00013fd6
- 00576310 ["INT_ADD", "register:40f0:8", ["const:576310:8", "const:4:8"]]
- 00576310 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00576350 ["INT_ADD", "register:40f0:8", ["const:576350:8", "const:4:8"]]
+ 00576350 ["CALL", null, ["callee:00c57ee0:8"]]
- 00576310 bytes f4851b94
+ 00576350 bytes e4861b94
~~~


<a id="compare-c790c46c50432a2d76468d052bef4e39"></a>

### [`005767e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/005767e8.md) → [`00576828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576828.md) FUN_00576828

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005766c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/005766c0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00576700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576700.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005767f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/005767e8.md#insn-005767f8)
- 新版 [`00576838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576828.md#insn-00576838)

~~~diff
- 005767f8 ["INT_ADD", "register:40f0:8", ["const:5767f8:8", "const:4:8"]]
- 005767f8 ["CALL", null, ["callee:00576700:8"]]
+ 00576838 ["INT_ADD", "register:40f0:8", ["const:576838:8", "const:4:8"]]
+ 00576838 ["CALL", null, ["callee:00576700:8"]]
- 005767f8 bytes b2ffff97
+ 00576838 bytes b2ffff97
~~~


<a id="compare-d3d606ee856ba8f5a7dec7e4aadd6e85"></a>

### [`00577040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577040.md) → [`00577080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577080.md) FUN_00577080

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`005772d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005772d8.md) [`005778a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005778a0.md) [`00577c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577c40.md) · 呼出先 2件 [`0057be68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057be68.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 3件 [`00577318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577318.md) [`005778e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005778e0.md) [`00577c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577c80.md) · 呼出先 2件 [`0057bea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057707c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577040.md#insn-0057707c) · [`005770a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577040.md#insn-005770a8) · [`005770b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577040.md#insn-005770b8)
- 新版 [`005770bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577080.md#insn-005770bc) · [`005770e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577080.md#insn-005770e8) · [`005770f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577080.md#insn-005770f8)

~~~diff
- 0057707c ["COPY", "register:0:8", ["register:4048:8"]]
- 0057707c ["INT_ADD", "register:40f0:8", ["const:57707c:8", "const:4:8"]]
- 0057707c ["CALLIND", null, ["register:0:8"]]
+ 005770bc ["COPY", "register:0:8", ["register:4048:8"]]
+ 005770bc ["INT_ADD", "register:40f0:8", ["const:5770bc:8", "const:4:8"]]
+ 005770bc ["CALLIND", null, ["register:0:8"]]
- 0057707c bytes 20013fd6
+ 005770bc bytes 20013fd6
- 005770a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005770a8 ["INT_ADD", "register:40f0:8", ["const:5770a8:8", "const:4:8"]]
- 005770a8 ["CALLIND", null, ["register:0:8"]]
+ 005770e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005770e8 ["INT_ADD", "register:40f0:8", ["const:5770e8:8", "const:4:8"]]
+ 005770e8 ["CALLIND", null, ["register:0:8"]]
- 005770a8 bytes 00013fd6
+ 005770e8 bytes 00013fd6
- 005770b8 ["INT_ADD", "register:40f0:8", ["const:5770b8:8", "const:4:8"]]
- 005770b8 ["CALL", null, ["callee:0057bea8:8"]]
+ 005770f8 ["INT_ADD", "register:40f0:8", ["const:5770f8:8", "const:4:8"]]
+ 005770f8 ["CALL", null, ["callee:0057bea8:8"]]
- 005770b8 bytes 6c130094
+ 005770f8 bytes 6c130094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5fe724354ff80b372ae94fd786a0a2a"></a>

### [`00577288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577288.md) → [`005772c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005772c8.md) FUN_005772c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005772a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577288.md#insn-005772a4) · [`005772c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577288.md#insn-005772c4)
- 新版 [`005772e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005772c8.md#insn-005772e4) · [`00577304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005772c8.md#insn-00577304)

~~~diff
- 005772a4 ["INT_ADD", "register:40f0:8", ["const:5772a4:8", "const:4:8"]]
- 005772a4 ["CALL", null, ["callee:00c53d00:8"]]
+ 005772e4 ["INT_ADD", "register:40f0:8", ["const:5772e4:8", "const:4:8"]]
+ 005772e4 ["CALL", null, ["callee:00c53d00:8"]]
- 005772a4 bytes 8f711b94
+ 005772e4 bytes 87721b94
- 005772c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005772c4 ["INT_ADD", "register:40f0:8", ["const:5772c4:8", "const:4:8"]]
- 005772c4 ["CALLIND", null, ["register:0:8"]]
+ 00577304 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00577304 ["INT_ADD", "register:40f0:8", ["const:577304:8", "const:4:8"]]
+ 00577304 ["CALLIND", null, ["register:0:8"]]
- 005772c4 bytes 00013fd6
+ 00577304 bytes 00013fd6
~~~


<a id="compare-6af97d73233f4d6b286890acf15590ae"></a>

### [`00577850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577850.md) → [`00577890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577890.md) FUN_00577890

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057786c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577850.md#insn-0057786c) · [`0057788c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577850.md#insn-0057788c)
- 新版 [`005778ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577890.md#insn-005778ac) · [`005778cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577890.md#insn-005778cc)

~~~diff
- 0057786c ["INT_ADD", "register:40f0:8", ["const:57786c:8", "const:4:8"]]
- 0057786c ["CALL", null, ["callee:00c53d00:8"]]
+ 005778ac ["INT_ADD", "register:40f0:8", ["const:5778ac:8", "const:4:8"]]
+ 005778ac ["CALL", null, ["callee:00c53d00:8"]]
- 0057786c bytes 1d701b94
+ 005778ac bytes 15711b94
- 0057788c ["COPY", "register:0:8", ["register:4040:8"]]
- 0057788c ["INT_ADD", "register:40f0:8", ["const:57788c:8", "const:4:8"]]
- 0057788c ["CALLIND", null, ["register:0:8"]]
+ 005778cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005778cc ["INT_ADD", "register:40f0:8", ["const:5778cc:8", "const:4:8"]]
+ 005778cc ["CALLIND", null, ["register:0:8"]]
- 0057788c bytes 00013fd6
+ 005778cc bytes 00013fd6
~~~


<a id="compare-856872c0cf932c50a239c67a37c8fd6a"></a>

### [`00578184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578184.md) → [`005781c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/005781c4.md) FUN_005781c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00577fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577fe0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00578020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578020.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00578194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578184.md#insn-00578194)
- 新版 [`005781d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/005781c4.md#insn-005781d4)

~~~diff
- 00578194 ["INT_ADD", "register:40f0:8", ["const:578194:8", "const:4:8"]]
- 00578194 ["CALL", null, ["callee:00578020:8"]]
+ 005781d4 ["INT_ADD", "register:40f0:8", ["const:5781d4:8", "const:4:8"]]
+ 005781d4 ["CALL", null, ["callee:00578020:8"]]
- 00578194 bytes 93ffff97
+ 005781d4 bytes 93ffff97
~~~


<a id="compare-dd236d285f7e227e3eeab365f837020c"></a>

### [`0057a264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a264.md) → [`0057a2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a2a4.md) FUN_0057a2a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0057c2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c2dc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0057c31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c31c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057a2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a264.md#insn-0057a2b8)
- 新版 [`0057a2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a2a4.md#insn-0057a2f8)

~~~diff
- 0057a2b8 ["INT_ADD", "register:40f0:8", ["const:57a2b8:8", "const:4:8"]]
- 0057a2b8 ["CALL", null, ["callee:0057c31c:8"]]
+ 0057a2f8 ["INT_ADD", "register:40f0:8", ["const:57a2f8:8", "const:4:8"]]
+ 0057a2f8 ["CALL", null, ["callee:0057c31c:8"]]
- 0057a2b8 bytes 09080094
+ 0057a2f8 bytes 09080094
~~~


<a id="compare-012582c0cf95f95edb880f98851e29aa"></a>

### [`0057a2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a2bc.md) → [`0057a2fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a2fc.md) FUN_0057a2fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0057c2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c2dc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0057c31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c31c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057a300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a2bc.md#insn-0057a300)
- 新版 [`0057a340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a2fc.md#insn-0057a340)

~~~diff
- 0057a300 ["INT_ADD", "register:40f0:8", ["const:57a300:8", "const:4:8"]]
- 0057a300 ["CALL", null, ["callee:0057c31c:8"]]
+ 0057a340 ["INT_ADD", "register:40f0:8", ["const:57a340:8", "const:4:8"]]
+ 0057a340 ["CALL", null, ["callee:0057c31c:8"]]
- 0057a300 bytes f7070094
+ 0057a340 bytes f7070094
~~~


<a id="compare-e4e3b1c4ff109f3e3e6af0619540f38a"></a>

### [`0057a304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a304.md) → [`0057a344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a344.md) FUN_0057a344

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0057c2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c2dc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0057c31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c31c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057a348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a304.md#insn-0057a348)
- 新版 [`0057a388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a344.md#insn-0057a388)

~~~diff
- 0057a348 ["INT_ADD", "register:40f0:8", ["const:57a348:8", "const:4:8"]]
- 0057a348 ["CALL", null, ["callee:0057c31c:8"]]
+ 0057a388 ["INT_ADD", "register:40f0:8", ["const:57a388:8", "const:4:8"]]
+ 0057a388 ["CALL", null, ["callee:0057c31c:8"]]
- 0057a348 bytes e5070094
+ 0057a388 bytes e5070094
~~~


<a id="compare-6218a662c39b8761fca43b3a600df8c9"></a>

### [`0057bc4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bc4c.md) → [`0057bc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bc8c.md) FUN_0057bc8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0057656c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057656c.md) [`0057bc4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bc4c.md) · 呼出先 2件 [`0057bc4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bc4c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`005765ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005765ac.md) [`0057bc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bc8c.md) · 呼出先 2件 [`0057bc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bc8c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057bc68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bc4c.md#insn-0057bc68) · [`0057bc74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bc4c.md#insn-0057bc74) · [`0057bcac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bc4c.md#insn-0057bcac)
- 新版 [`0057bca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bc8c.md#insn-0057bca8) · [`0057bcb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bc8c.md#insn-0057bcb4) · [`0057bcec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bc8c.md#insn-0057bcec)

~~~diff
- 0057bc68 ["INT_ADD", "register:40f0:8", ["const:57bc68:8", "const:4:8"]]
- 0057bc68 ["CALL", null, ["local:b0:8"]]
+ 0057bca8 ["INT_ADD", "register:40f0:8", ["const:57bca8:8", "const:4:8"]]
+ 0057bca8 ["CALL", null, ["local:b0:8"]]
- 0057bc68 bytes f9ffff97
+ 0057bca8 bytes f9ffff97
- 0057bc74 ["INT_ADD", "register:40f0:8", ["const:57bc74:8", "const:4:8"]]
- 0057bc74 ["CALL", null, ["local:b0:8"]]
+ 0057bcb4 ["INT_ADD", "register:40f0:8", ["const:57bcb4:8", "const:4:8"]]
+ 0057bcb4 ["CALL", null, ["local:b0:8"]]
- 0057bc74 bytes f6ffff97
+ 0057bcb4 bytes f6ffff97
- 0057bcac ["COPY", "register:0:8", ["register:4040:8"]]
- 0057bcac ["INT_ADD", "register:40f0:8", ["const:57bcac:8", "const:4:8"]]
- 0057bcac ["CALLIND", null, ["register:0:8"]]
+ 0057bcec ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057bcec ["INT_ADD", "register:40f0:8", ["const:57bcec:8", "const:4:8"]]
+ 0057bcec ["CALLIND", null, ["register:0:8"]]
- 0057bcac bytes 00013fd6
+ 0057bcec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e470a4eb009f1861c80949543e94453"></a>

### [`0057bcec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bcec.md) → [`0057bd2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd2c.md) FUN_0057bd2c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00576574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576574.md) [`0057bcec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bcec.md) · 呼出先 2件 [`0057bcec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bcec.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`005765b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005765b4.md) [`0057bd2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd2c.md) · 呼出先 2件 [`0057bd2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd2c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057bd08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bcec.md#insn-0057bd08) · [`0057bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bcec.md#insn-0057bd14) · [`0057bd48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bcec.md#insn-0057bd48)
- 新版 [`0057bd48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd2c.md#insn-0057bd48) · [`0057bd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd2c.md#insn-0057bd54) · [`0057bd88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd2c.md#insn-0057bd88)

~~~diff
- 0057bd08 ["INT_ADD", "register:40f0:8", ["const:57bd08:8", "const:4:8"]]
- 0057bd08 ["CALL", null, ["local:b0:8"]]
+ 0057bd48 ["INT_ADD", "register:40f0:8", ["const:57bd48:8", "const:4:8"]]
+ 0057bd48 ["CALL", null, ["local:b0:8"]]
- 0057bd08 bytes f9ffff97
+ 0057bd48 bytes f9ffff97
- 0057bd14 ["INT_ADD", "register:40f0:8", ["const:57bd14:8", "const:4:8"]]
- 0057bd14 ["CALL", null, ["local:b0:8"]]
+ 0057bd54 ["INT_ADD", "register:40f0:8", ["const:57bd54:8", "const:4:8"]]
+ 0057bd54 ["CALL", null, ["local:b0:8"]]
- 0057bd14 bytes f6ffff97
+ 0057bd54 bytes f6ffff97
- 0057bd48 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057bd48 ["INT_ADD", "register:40f0:8", ["const:57bd48:8", "const:4:8"]]
- 0057bd48 ["CALLIND", null, ["register:0:8"]]
+ 0057bd88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057bd88 ["INT_ADD", "register:40f0:8", ["const:57bd88:8", "const:4:8"]]
+ 0057bd88 ["CALLIND", null, ["register:0:8"]]
- 0057bd48 bytes 00013fd6
+ 0057bd88 bytes 00013fd6
~~~


<a id="compare-523e759e742e30a20fa70581c3b6cf15"></a>

### [`0057bd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bd5c.md) → [`0057bd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd9c.md) FUN_0057bd9c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005766b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/005766b8.md) [`0057bd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bd5c.md) · 呼出先 4件 [`0057bd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bd5c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`005766f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005766f8.md) [`0057bd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd9c.md) · 呼出先 4件 [`0057bd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd9c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057bd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bd5c.md#insn-0057bd78) · [`0057bd84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bd5c.md#insn-0057bd84) · [`0057bd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bd5c.md#insn-0057bd98)
- 新版 [`0057bdb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd9c.md#insn-0057bdb8) · [`0057bdc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd9c.md#insn-0057bdc4) · [`0057bdd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bd9c.md#insn-0057bdd8)

~~~diff
- 0057bd78 ["INT_ADD", "register:40f0:8", ["const:57bd78:8", "const:4:8"]]
- 0057bd78 ["CALL", null, ["local:b0:8"]]
+ 0057bdb8 ["INT_ADD", "register:40f0:8", ["const:57bdb8:8", "const:4:8"]]
+ 0057bdb8 ["CALL", null, ["local:b0:8"]]
- 0057bd78 bytes f9ffff97
+ 0057bdb8 bytes f9ffff97
- 0057bd84 ["INT_ADD", "register:40f0:8", ["const:57bd84:8", "const:4:8"]]
- 0057bd84 ["CALL", null, ["local:b0:8"]]
+ 0057bdc4 ["INT_ADD", "register:40f0:8", ["const:57bdc4:8", "const:4:8"]]
+ 0057bdc4 ["CALL", null, ["local:b0:8"]]
- 0057bd84 bytes f6ffff97
+ 0057bdc4 bytes f6ffff97
- 0057bd98 ["INT_ADD", "register:40f0:8", ["const:57bd98:8", "const:4:8"]]
- 0057bd98 ["CALL", null, ["callee:00c53d00:8"]]
+ 0057bdd8 ["INT_ADD", "register:40f0:8", ["const:57bdd8:8", "const:4:8"]]
+ 0057bdd8 ["CALL", null, ["callee:00c53d00:8"]]
- 0057bd98 bytes d25e1b94
+ 0057bdd8 bytes ca5f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8898b8fdcef48728336b868aa5e70a6f"></a>

### [`0057bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md) → [`0057be0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057be0c.md) FUN_0057be0c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 11件 [`0057695c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057695c.md) [`0057ecb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ecb0.md) [`0057ee28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ee28.md) [`0057ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ef9c.md) [`0057f11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f11c.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 11件 [`0057699c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/0057699c.md) [`0057ecf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ecf0.md) [`0057ee68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ee68.md) [`0057efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057efdc.md) [`0057f15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f15c.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057be40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md#insn-0057be40) · [`0057be64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md#insn-0057be64)
- 新版 [`0057be80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057be0c.md#insn-0057be80) · [`0057bea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057be0c.md#insn-0057bea4)

~~~diff
- 0057be40 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057be40 ["INT_ADD", "register:40f0:8", ["const:57be40:8", "const:4:8"]]
- 0057be40 ["CALLIND", null, ["register:0:8"]]
+ 0057be80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057be80 ["INT_ADD", "register:40f0:8", ["const:57be80:8", "const:4:8"]]
+ 0057be80 ["CALLIND", null, ["register:0:8"]]
- 0057be40 bytes 00013fd6
+ 0057be80 bytes 00013fd6
- 0057be64 ["INT_ADD", "register:40f0:8", ["const:57be64:8", "const:4:8"]]
- 0057be64 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0057bea4 ["INT_ADD", "register:40f0:8", ["const:57bea4:8", "const:4:8"]]
+ 0057bea4 ["CALL", null, ["callee:00c57ee0:8"]]
- 0057be64 bytes 1f6f1b94
+ 0057bea4 bytes 0f701b94
~~~


<a id="compare-9815f1bb473e41e8f31ad35137c45301"></a>

### [`0057be68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057be68.md) → [`0057bea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md) FUN_0057bea8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 16件 [`00577040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577040.md) [`0057a974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a974.md) [`0058c784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c784.md) [`006c3c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3c44.md) [`006d1fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1fa4.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 16件 [`00577080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577080.md) [`0057a9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a9b4.md) [`0058c7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c7c4.md) [`006c3c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c3/006c3c84.md) [`006d1fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d1/006d1fe4.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057bed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057be68.md#insn-0057bed4) · [`0057bee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057be68.md#insn-0057bee4) · [`0057bf04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057be68.md#insn-0057bf04)
- 新版 [`0057bf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md#insn-0057bf14) · [`0057bf24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md#insn-0057bf24) · [`0057bf44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md#insn-0057bf44)

~~~diff
- 0057bed4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057bed4 ["INT_ADD", "register:40f0:8", ["const:57bed4:8", "const:4:8"]]
- 0057bed4 ["CALLIND", null, ["register:0:8"]]
+ 0057bf14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057bf14 ["INT_ADD", "register:40f0:8", ["const:57bf14:8", "const:4:8"]]
+ 0057bf14 ["CALLIND", null, ["register:0:8"]]
- 0057bed4 bytes 00013fd6
+ 0057bf14 bytes 00013fd6
- 0057bee4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057bee4 ["INT_ADD", "register:40f0:8", ["const:57bee4:8", "const:4:8"]]
- 0057bee4 ["CALLIND", null, ["register:0:8"]]
+ 0057bf24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057bf24 ["INT_ADD", "register:40f0:8", ["const:57bf24:8", "const:4:8"]]
+ 0057bf24 ["CALLIND", null, ["register:0:8"]]
- 0057bee4 bytes 00013fd6
+ 0057bf24 bytes 00013fd6
- 0057bf04 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057bf04 ["INT_ADD", "register:40f0:8", ["const:57bf04:8", "const:4:8"]]
- 0057bf04 ["CALLIND", null, ["register:0:8"]]
+ 0057bf44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057bf44 ["INT_ADD", "register:40f0:8", ["const:57bf44:8", "const:4:8"]]
+ 0057bf44 ["CALLIND", null, ["register:0:8"]]
- 0057bf04 bytes 00013fd6
+ 0057bf44 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08a4b0e81c18c7efab1ca85703fa5dfd"></a>

### [`0057c070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c070.md) → [`0057c0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c0b0.md) FUN_0057c0b0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005778a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005778a0.md) [`00577c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577c40.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0057c1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c1cc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`005778e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005778e0.md) [`00577c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577c80.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0057c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c20c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057c0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c070.md#insn-0057c0dc) · [`0057c108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c070.md#insn-0057c108) · [`0057c168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c070.md#insn-0057c168)
- 新版 [`0057c11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c0b0.md#insn-0057c11c) · [`0057c148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c0b0.md#insn-0057c148) · [`0057c1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c0b0.md#insn-0057c1a8)

~~~diff
- 0057c0dc ["INT_ADD", "register:40f0:8", ["const:57c0dc:8", "const:4:8"]]
- 0057c0dc ["CALL", null, ["callee:00c57e90:8"]]
+ 0057c11c ["INT_ADD", "register:40f0:8", ["const:57c11c:8", "const:4:8"]]
+ 0057c11c ["CALL", null, ["callee:00c57e90:8"]]
- 0057c0dc bytes 6d6e1b94
+ 0057c11c bytes 5d6f1b94
- 0057c108 ["INT_ADD", "register:40f0:8", ["const:57c108:8", "const:4:8"]]
- 0057c108 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0057c148 ["INT_ADD", "register:40f0:8", ["const:57c148:8", "const:4:8"]]
+ 0057c148 ["CALL", null, ["callee:00c53cd0:8"]]
- 0057c108 bytes ea5d1b94
+ 0057c148 bytes e25e1b94
- 0057c168 ["INT_ADD", "register:40f0:8", ["const:57c168:8", "const:4:8"]]
- 0057c168 ["CALL", null, ["callee:00c53d00:8"]]
+ 0057c1a8 ["INT_ADD", "register:40f0:8", ["const:57c1a8:8", "const:4:8"]]
+ 0057c1a8 ["CALL", null, ["callee:00c53d00:8"]]
- 0057c168 bytes de5d1b94
+ 0057c1a8 bytes d65e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-806df606106076c14ed8ff96e906d138"></a>

### [`0057c1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c1e0.md) → [`0057c220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c220.md) FUN_0057c220

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00577fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577fe0.md) · 呼出先 4件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00578020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578020.md) · 呼出先 4件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057c290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c1e0.md#insn-0057c290) · [`0057c2a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c1e0.md#insn-0057c2a4) · [`0057c2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c1e0.md#insn-0057c2b8)
- 新版 [`0057c2d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c220.md#insn-0057c2d0) · [`0057c2e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c220.md#insn-0057c2e4) · [`0057c2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c220.md#insn-0057c2f8)

~~~diff
- 0057c290 ["INT_ADD", "register:40f0:8", ["const:57c290:8", "const:4:8"]]
- 0057c290 ["CALL", null, ["callee:00494610:8"]]
+ 0057c2d0 ["INT_ADD", "register:40f0:8", ["const:57c2d0:8", "const:4:8"]]
+ 0057c2d0 ["CALL", null, ["callee:00494610:8"]]
- 0057c290 bytes d060fc97
+ 0057c2d0 bytes d060fc97
- 0057c2a4 ["INT_ADD", "register:40f0:8", ["const:57c2a4:8", "const:4:8"]]
- 0057c2a4 ["CALL", null, ["callee:00c53d00:8"]]
+ 0057c2e4 ["INT_ADD", "register:40f0:8", ["const:57c2e4:8", "const:4:8"]]
+ 0057c2e4 ["CALL", null, ["callee:00c53d00:8"]]
- 0057c2a4 bytes 8f5d1b94
+ 0057c2e4 bytes 875e1b94
- 0057c2b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057c2b8 ["INT_ADD", "register:40f0:8", ["const:57c2b8:8", "const:4:8"]]
- 0057c2b8 ["CALLIND", null, ["register:0:8"]]
+ 0057c2f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c2f8 ["INT_ADD", "register:40f0:8", ["const:57c2f8:8", "const:4:8"]]
+ 0057c2f8 ["CALLIND", null, ["register:0:8"]]
- 0057c2b8 bytes 00013fd6
+ 0057c2f8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-661fae24ae8f473497a4b496469a842f"></a>

### [`0057c2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c2f0.md) → [`0057c330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c330.md) FUN_0057c330

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0057a5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a5bc.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0057c1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c1cc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0057a5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a5fc.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0057c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c20c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057c35c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c2f0.md#insn-0057c35c) · [`0057c388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c2f0.md#insn-0057c388) · [`0057c3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c2f0.md#insn-0057c3e8)
- 新版 [`0057c39c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c330.md#insn-0057c39c) · [`0057c3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c330.md#insn-0057c3c8) · [`0057c428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c330.md#insn-0057c428)

~~~diff
- 0057c35c ["INT_ADD", "register:40f0:8", ["const:57c35c:8", "const:4:8"]]
- 0057c35c ["CALL", null, ["callee:00c57e90:8"]]
+ 0057c39c ["INT_ADD", "register:40f0:8", ["const:57c39c:8", "const:4:8"]]
+ 0057c39c ["CALL", null, ["callee:00c57e90:8"]]
- 0057c35c bytes cd6d1b94
+ 0057c39c bytes bd6e1b94
- 0057c388 ["INT_ADD", "register:40f0:8", ["const:57c388:8", "const:4:8"]]
- 0057c388 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0057c3c8 ["INT_ADD", "register:40f0:8", ["const:57c3c8:8", "const:4:8"]]
+ 0057c3c8 ["CALL", null, ["callee:00c53cd0:8"]]
- 0057c388 bytes 4a5d1b94
+ 0057c3c8 bytes 425e1b94
- 0057c3e8 ["INT_ADD", "register:40f0:8", ["const:57c3e8:8", "const:4:8"]]
- 0057c3e8 ["CALL", null, ["callee:00c53d00:8"]]
+ 0057c428 ["INT_ADD", "register:40f0:8", ["const:57c428:8", "const:4:8"]]
+ 0057c428 ["CALL", null, ["callee:00c53d00:8"]]
- 0057c3e8 bytes 3e5d1b94
+ 0057c428 bytes 365e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44e84632cfbe3d3414ff6a0a43a4aaef"></a>

### [`0057c4ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c4ec.md) → [`0057c52c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c52c.md) FUN_0057c52c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0057a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a910.md) [`0057c4ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c4ec.md) · 呼出先 2件 [`0057c4ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c4ec.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0057a950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a950.md) [`0057c52c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c52c.md) · 呼出先 2件 [`0057c52c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c52c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057c508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c4ec.md#insn-0057c508) · [`0057c514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c4ec.md#insn-0057c514) · [`0057c548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c4ec.md#insn-0057c548)
- 新版 [`0057c548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c52c.md#insn-0057c548) · [`0057c554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c52c.md#insn-0057c554) · [`0057c588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c52c.md#insn-0057c588)

~~~diff
- 0057c508 ["INT_ADD", "register:40f0:8", ["const:57c508:8", "const:4:8"]]
- 0057c508 ["CALL", null, ["local:b0:8"]]
+ 0057c548 ["INT_ADD", "register:40f0:8", ["const:57c548:8", "const:4:8"]]
+ 0057c548 ["CALL", null, ["local:b0:8"]]
- 0057c508 bytes f9ffff97
+ 0057c548 bytes f9ffff97
- 0057c514 ["INT_ADD", "register:40f0:8", ["const:57c514:8", "const:4:8"]]
- 0057c514 ["CALL", null, ["local:b0:8"]]
+ 0057c554 ["INT_ADD", "register:40f0:8", ["const:57c554:8", "const:4:8"]]
+ 0057c554 ["CALL", null, ["local:b0:8"]]
- 0057c514 bytes f6ffff97
+ 0057c554 bytes f6ffff97
- 0057c548 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057c548 ["INT_ADD", "register:40f0:8", ["const:57c548:8", "const:4:8"]]
- 0057c548 ["CALLIND", null, ["register:0:8"]]
+ 0057c588 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c588 ["INT_ADD", "register:40f0:8", ["const:57c588:8", "const:4:8"]]
+ 0057c588 ["CALLIND", null, ["register:0:8"]]
- 0057c548 bytes 00013fd6
+ 0057c588 bytes 00013fd6
~~~


<a id="compare-976d75a3316e3485925f1846b7cdfffd"></a>

### [`0057c55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c55c.md) → [`0057c59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c59c.md) FUN_0057c59c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0057a918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a918.md) [`0057c55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c55c.md) [`0058c3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c3e8.md) · 呼出先 2件 [`0057c55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c55c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0057a958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a958.md) [`0057c59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c59c.md) [`0058c428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c428.md) · 呼出先 2件 [`0057c59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c59c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057c578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c55c.md#insn-0057c578) · [`0057c584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c55c.md#insn-0057c584) · [`0057c5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c55c.md#insn-0057c5b8)
- 新版 [`0057c5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c59c.md#insn-0057c5b8) · [`0057c5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c59c.md#insn-0057c5c4) · [`0057c5f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c59c.md#insn-0057c5f8)

~~~diff
- 0057c578 ["INT_ADD", "register:40f0:8", ["const:57c578:8", "const:4:8"]]
- 0057c578 ["CALL", null, ["local:b0:8"]]
+ 0057c5b8 ["INT_ADD", "register:40f0:8", ["const:57c5b8:8", "const:4:8"]]
+ 0057c5b8 ["CALL", null, ["local:b0:8"]]
- 0057c578 bytes f9ffff97
+ 0057c5b8 bytes f9ffff97
- 0057c584 ["INT_ADD", "register:40f0:8", ["const:57c584:8", "const:4:8"]]
- 0057c584 ["CALL", null, ["local:b0:8"]]
+ 0057c5c4 ["INT_ADD", "register:40f0:8", ["const:57c5c4:8", "const:4:8"]]
+ 0057c5c4 ["CALL", null, ["local:b0:8"]]
- 0057c584 bytes f6ffff97
+ 0057c5c4 bytes f6ffff97
- 0057c5b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057c5b8 ["INT_ADD", "register:40f0:8", ["const:57c5b8:8", "const:4:8"]]
- 0057c5b8 ["CALLIND", null, ["register:0:8"]]
+ 0057c5f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c5f8 ["INT_ADD", "register:40f0:8", ["const:57c5f8:8", "const:4:8"]]
+ 0057c5f8 ["CALLIND", null, ["register:0:8"]]
- 0057c5b8 bytes 00013fd6
+ 0057c5f8 bytes 00013fd6
~~~


<a id="compare-333c984753b51e5a4da37c88751c0dff"></a>

### [`0057c614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c614.md) → [`0057c654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c654.md) FUN_0057c654

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0057b124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b124.md) [`00935ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935ca0.md) [`00ac894c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac894c.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 3件 [`0057b164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b164.md) [`00935e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935e3c.md) [`00ac8b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac8b48.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057c680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c614.md#insn-0057c680) · [`0057c690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c614.md#insn-0057c690) · [`0057c6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c614.md#insn-0057c6b0)
- 新版 [`0057c6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c654.md#insn-0057c6c0) · [`0057c6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c654.md#insn-0057c6d0) · [`0057c6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c654.md#insn-0057c6f0)

~~~diff
- 0057c680 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057c680 ["INT_ADD", "register:40f0:8", ["const:57c680:8", "const:4:8"]]
- 0057c680 ["CALLIND", null, ["register:0:8"]]
+ 0057c6c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c6c0 ["INT_ADD", "register:40f0:8", ["const:57c6c0:8", "const:4:8"]]
+ 0057c6c0 ["CALLIND", null, ["register:0:8"]]
- 0057c680 bytes 00013fd6
+ 0057c6c0 bytes 00013fd6
- 0057c690 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057c690 ["INT_ADD", "register:40f0:8", ["const:57c690:8", "const:4:8"]]
- 0057c690 ["CALLIND", null, ["register:0:8"]]
+ 0057c6d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c6d0 ["INT_ADD", "register:40f0:8", ["const:57c6d0:8", "const:4:8"]]
+ 0057c6d0 ["CALLIND", null, ["register:0:8"]]
- 0057c690 bytes 00013fd6
+ 0057c6d0 bytes 00013fd6
- 0057c6b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057c6b0 ["INT_ADD", "register:40f0:8", ["const:57c6b0:8", "const:4:8"]]
- 0057c6b0 ["CALLIND", null, ["register:0:8"]]
+ 0057c6f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057c6f0 ["INT_ADD", "register:40f0:8", ["const:57c6f0:8", "const:4:8"]]
+ 0057c6f0 ["CALLIND", null, ["register:0:8"]]
- 0057c6b0 bytes 00013fd6
+ 0057c6f0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c5e4e75673870aea2b0067807e2073e"></a>

### [`0057cc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057cc94.md) → [`0057ccd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057ccd4.md) FUN_0057ccd4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057ccac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057cc94.md#insn-0057ccac)
- 新版 [`0057ccec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057ccd4.md#insn-0057ccec)

~~~diff
- 0057ccac ["INT_ADD", "register:40f0:8", ["const:57ccac:8", "const:4:8"]]
- 0057ccac ["CALL", null, ["callee:00c5a140:8"]]
+ 0057ccec ["INT_ADD", "register:40f0:8", ["const:57ccec:8", "const:4:8"]]
+ 0057ccec ["CALL", null, ["callee:00c5a140:8"]]
- 0057ccac bytes 25741b94
+ 0057ccec bytes 15751b94
~~~


<a id="compare-f94101d6ff76909a7f7d12537ea8aa57"></a>

### [`0057cd20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057cd20.md) → [`0057cd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057cd60.md) FUN_0057cd60

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057cd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057cd20.md#insn-0057cd40) · [`0057cd54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057cd20.md#insn-0057cd54)
- 新版 [`0057cd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057cd60.md#insn-0057cd80) · [`0057cd94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057cd60.md#insn-0057cd94)

~~~diff
- 0057cd40 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057cd40 ["INT_ADD", "register:40f0:8", ["const:57cd40:8", "const:4:8"]]
- 0057cd40 ["CALLIND", null, ["register:0:8"]]
+ 0057cd80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057cd80 ["INT_ADD", "register:40f0:8", ["const:57cd80:8", "const:4:8"]]
+ 0057cd80 ["CALLIND", null, ["register:0:8"]]
- 0057cd40 bytes 00013fd6
+ 0057cd80 bytes 00013fd6
- 0057cd54 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057cd54 ["INT_ADD", "register:40f0:8", ["const:57cd54:8", "const:4:8"]]
- 0057cd54 ["CALLIND", null, ["register:0:8"]]
+ 0057cd94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057cd94 ["INT_ADD", "register:40f0:8", ["const:57cd94:8", "const:4:8"]]
+ 0057cd94 ["CALLIND", null, ["register:0:8"]]
- 0057cd54 bytes 00013fd6
+ 0057cd94 bytes 00013fd6
~~~


<a id="compare-98d2e1b753dd460a5a90c078c6e248e3"></a>

### [`0057ce28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057ce28.md) → [`0057ce68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057ce68.md) FUN_0057ce68

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a170.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057ce28.md#insn-0057ce44)
- 新版 [`0057ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057ce68.md#insn-0057ce84)

~~~diff
- 0057ce44 ["INT_ADD", "register:40f0:8", ["const:57ce44:8", "const:4:8"]]
- 0057ce44 ["CALL", null, ["callee:00c5a170:8"]]
+ 0057ce84 ["INT_ADD", "register:40f0:8", ["const:57ce84:8", "const:4:8"]]
+ 0057ce84 ["CALL", null, ["callee:00c5a170:8"]]
- 0057ce44 bytes cb731b94
+ 0057ce84 bytes bb741b94
~~~


<a id="compare-ed0fb4c14c05eb1bdfa541095c5921b2"></a>

### [`0057d0ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d0ec.md) → [`0057d12c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d12c.md) FUN_0057d12c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d50.md) [`00c59d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a150.md) [`00c5a170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a170.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d0ec.md#insn-0057d104) · [`0057d114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d0ec.md#insn-0057d114)
- 新版 [`0057d144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d12c.md#insn-0057d144) · [`0057d154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d12c.md#insn-0057d154)

~~~diff
- 0057d104 ["INT_ADD", "register:40f0:8", ["const:57d104:8", "const:4:8"]]
- 0057d104 ["CALL", null, ["callee:00c5a150:8"]]
+ 0057d144 ["INT_ADD", "register:40f0:8", ["const:57d144:8", "const:4:8"]]
+ 0057d144 ["CALL", null, ["callee:00c5a150:8"]]
- 0057d104 bytes 13731b94
+ 0057d144 bytes 03741b94
- 0057d114 ["INT_ADD", "register:40f0:8", ["const:57d114:8", "const:4:8"]]
- 0057d114 ["CALL", null, ["callee:00c5a170:8"]]
+ 0057d154 ["INT_ADD", "register:40f0:8", ["const:57d154:8", "const:4:8"]]
+ 0057d154 ["CALL", null, ["callee:00c5a170:8"]]
- 0057d114 bytes 17731b94
+ 0057d154 bytes 07741b94
~~~


<a id="compare-71b8a2cf8ae40a0a756a3a88fea752b0"></a>

### [`0057d178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d178.md) → [`0057d1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d1b8.md) FUN_0057d1b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d178.md#insn-0057d190)
- 新版 [`0057d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d1b8.md#insn-0057d1d0)

~~~diff
- 0057d190 ["INT_ADD", "register:40f0:8", ["const:57d190:8", "const:4:8"]]
- 0057d190 ["CALL", null, ["callee:00c5a000:8"]]
+ 0057d1d0 ["INT_ADD", "register:40f0:8", ["const:57d1d0:8", "const:4:8"]]
+ 0057d1d0 ["CALL", null, ["callee:00c5a000:8"]]
- 0057d190 bytes 9c721b94
+ 0057d1d0 bytes 8c731b94
~~~


<a id="compare-57e3e2457a8fc4d564c527bf9ee6bcec"></a>

### [`0057d1ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d1ac.md) → [`0057d1ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d1ec.md) FUN_0057d1ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c59dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59dc0.md) [`00c59dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59dd0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5a1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1c0.md) [`00c5a1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d1c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d1ac.md#insn-0057d1c4) · [`0057d1d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d1ac.md#insn-0057d1d8) · [`0057d1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d1ac.md#insn-0057d1dc)
- 新版 [`0057d204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d1ec.md#insn-0057d204) · [`0057d218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d1ec.md#insn-0057d218) · [`0057d21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d1ec.md#insn-0057d21c)

~~~diff
- 0057d1c4 ["INT_ADD", "register:40f0:8", ["const:57d1c4:8", "const:4:8"]]
- 0057d1c4 ["CALL", null, ["callee:00c5a1b0:8"]]
+ 0057d204 ["INT_ADD", "register:40f0:8", ["const:57d204:8", "const:4:8"]]
+ 0057d204 ["CALL", null, ["callee:00c5a1b0:8"]]
- 0057d1c4 bytes fb721b94
+ 0057d204 bytes eb731b94
- 0057d1d8 ["INT_ADD", "register:40f0:8", ["const:57d1d8:8", "const:4:8"]]
- 0057d1d8 ["CALL", null, ["callee:00c5a1c0:8"]]
+ 0057d218 ["INT_ADD", "register:40f0:8", ["const:57d218:8", "const:4:8"]]
+ 0057d218 ["CALL", null, ["callee:00c5a1c0:8"]]
- 0057d1d8 bytes fa721b94
+ 0057d218 bytes ea731b94
- 0057d1dc ["INT_ADD", "register:40f0:8", ["const:57d1dc:8", "const:4:8"]]
- 0057d1dc ["CALL", null, ["callee:00c5a1d0:8"]]
+ 0057d21c ["INT_ADD", "register:40f0:8", ["const:57d21c:8", "const:4:8"]]
+ 0057d21c ["CALL", null, ["callee:00c5a1d0:8"]]
- 0057d1dc bytes fd721b94
+ 0057d21c bytes ed731b94
~~~


<a id="compare-2f78ca240e8fa80954d3f68e6e64c179"></a>

### [`0057d1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d1f4.md) → [`0057d234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d234.md) FUN_0057d234

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59dc0.md) [`00c59de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59de0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1c0.md) [`00c5a1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d1f4.md#insn-0057d218) · [`0057d220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d1f4.md#insn-0057d220) · [`0057d254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d1f4.md#insn-0057d254)
- 新版 [`0057d258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d234.md#insn-0057d258) · [`0057d260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d234.md#insn-0057d260) · [`0057d294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d234.md#insn-0057d294)

~~~diff
- 0057d218 ["INT_ADD", "register:40f0:8", ["const:57d218:8", "const:4:8"]]
- 0057d218 ["CALL", null, ["callee:00c5a1c0:8"]]
+ 0057d258 ["INT_ADD", "register:40f0:8", ["const:57d258:8", "const:4:8"]]
+ 0057d258 ["CALL", null, ["callee:00c5a1c0:8"]]
- 0057d218 bytes ea721b94
+ 0057d258 bytes da731b94
- 0057d220 ["INT_ADD", "register:40f0:8", ["const:57d220:8", "const:4:8"]]
- 0057d220 ["CALL", null, ["callee:00c5a1e0:8"]]
+ 0057d260 ["INT_ADD", "register:40f0:8", ["const:57d260:8", "const:4:8"]]
+ 0057d260 ["CALL", null, ["callee:00c5a1e0:8"]]
- 0057d220 bytes f0721b94
+ 0057d260 bytes e0731b94
- 0057d254 ["INT_ADD", "register:40f0:8", ["const:57d254:8", "const:4:8"]]
- 0057d254 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0057d294 ["INT_ADD", "register:40f0:8", ["const:57d294:8", "const:4:8"]]
+ 0057d294 ["CALL", null, ["callee:00c57ee0:8"]]
- 0057d254 bytes 236a1b94
+ 0057d294 bytes 136b1b94
~~~


<a id="compare-c7a77c12b89915cf031b4a8f11d001a6"></a>

### [`0057d28c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d28c.md) → [`0057d2cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d2cc.md) FUN_0057d2cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59dc0.md) [`00c59de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59de0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1c0.md) [`00c5a1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d28c.md#insn-0057d2b0) · [`0057d2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d28c.md#insn-0057d2b8) · [`0057d2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d28c.md#insn-0057d2e0)
- 新版 [`0057d2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d2cc.md#insn-0057d2f0) · [`0057d2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d2cc.md#insn-0057d2f8) · [`0057d320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d2cc.md#insn-0057d320)

~~~diff
- 0057d2b0 ["INT_ADD", "register:40f0:8", ["const:57d2b0:8", "const:4:8"]]
- 0057d2b0 ["CALL", null, ["callee:00c5a1c0:8"]]
+ 0057d2f0 ["INT_ADD", "register:40f0:8", ["const:57d2f0:8", "const:4:8"]]
+ 0057d2f0 ["CALL", null, ["callee:00c5a1c0:8"]]
- 0057d2b0 bytes c4721b94
+ 0057d2f0 bytes b4731b94
- 0057d2b8 ["INT_ADD", "register:40f0:8", ["const:57d2b8:8", "const:4:8"]]
- 0057d2b8 ["CALL", null, ["callee:00c5a1e0:8"]]
+ 0057d2f8 ["INT_ADD", "register:40f0:8", ["const:57d2f8:8", "const:4:8"]]
+ 0057d2f8 ["CALL", null, ["callee:00c5a1e0:8"]]
- 0057d2b8 bytes ca721b94
+ 0057d2f8 bytes ba731b94
- 0057d2e0 ["INT_ADD", "register:40f0:8", ["const:57d2e0:8", "const:4:8"]]
- 0057d2e0 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0057d320 ["INT_ADD", "register:40f0:8", ["const:57d320:8", "const:4:8"]]
+ 0057d320 ["CALL", null, ["callee:00c57ee0:8"]]
- 0057d2e0 bytes 006a1b94
+ 0057d320 bytes f06a1b94
~~~


<a id="compare-8ad0d1dbffd40a0e8df8d9a0df0250df"></a>

### [`0057d3dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d3dc.md) → [`0057d41c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d41c.md) FUN_0057d41c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d3dc.md#insn-0057d404) · [`0057d418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d3dc.md#insn-0057d418)
- 新版 [`0057d444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d41c.md#insn-0057d444) · [`0057d458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d41c.md#insn-0057d458)

~~~diff
- 0057d404 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057d404 ["INT_ADD", "register:40f0:8", ["const:57d404:8", "const:4:8"]]
- 0057d404 ["CALLIND", null, ["register:0:8"]]
+ 0057d444 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057d444 ["INT_ADD", "register:40f0:8", ["const:57d444:8", "const:4:8"]]
+ 0057d444 ["CALLIND", null, ["register:0:8"]]
- 0057d404 bytes 00013fd6
+ 0057d444 bytes 00013fd6
- 0057d418 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057d418 ["INT_ADD", "register:40f0:8", ["const:57d418:8", "const:4:8"]]
- 0057d418 ["CALLIND", null, ["register:0:8"]]
+ 0057d458 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057d458 ["INT_ADD", "register:40f0:8", ["const:57d458:8", "const:4:8"]]
+ 0057d458 ["CALLIND", null, ["register:0:8"]]
- 0057d418 bytes 00013fd6
+ 0057d458 bytes 00013fd6
~~~


<a id="compare-0766efa1efff1c94f5c9c006261be6a6"></a>

### [`0057d6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d6a4.md) → [`0057d6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d6e4.md) FUN_0057d6e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d6a4.md#insn-0057d6b4)
- 新版 [`0057d6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d6e4.md#insn-0057d6f4)

~~~diff
- 0057d6b4 ["INT_ADD", "register:40f0:8", ["const:57d6b4:8", "const:4:8"]]
- 0057d6b4 ["CALL", null, ["callee:00c5a060:8"]]
+ 0057d6f4 ["INT_ADD", "register:40f0:8", ["const:57d6f4:8", "const:4:8"]]
+ 0057d6f4 ["CALL", null, ["callee:00c5a060:8"]]
- 0057d6b4 bytes 6b711b94
+ 0057d6f4 bytes 5b721b94
~~~


<a id="compare-57bf55a96ef6f534cd3a589df4367765"></a>

### [`0057d6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d6c8.md) → [`0057d708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d708.md) FUN_0057d708

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d6c8.md#insn-0057d6e4)
- 新版 [`0057d724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d708.md#insn-0057d724)

~~~diff
- 0057d6e4 ["INT_ADD", "register:40f0:8", ["const:57d6e4:8", "const:4:8"]]
- 0057d6e4 ["CALL", null, ["callee:00c5a200:8"]]
+ 0057d724 ["INT_ADD", "register:40f0:8", ["const:57d724:8", "const:4:8"]]
+ 0057d724 ["CALL", null, ["callee:00c5a200:8"]]
- 0057d6e4 bytes c7711b94
+ 0057d724 bytes b7721b94
~~~


<a id="compare-e140a850857529647adcc95a00145244"></a>

### [`0057d784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d784.md) → [`0057d7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d7c4.md) FUN_0057d7c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d784.md#insn-0057d7c0)
- 新版 [`0057d800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d7c4.md#insn-0057d800)

~~~diff
- 0057d7c0 ["INT_ADD", "register:40f0:8", ["const:57d7c0:8", "const:4:8"]]
- 0057d7c0 ["CALL", null, ["callee:00c5a220:8"]]
+ 0057d800 ["INT_ADD", "register:40f0:8", ["const:57d800:8", "const:4:8"]]
+ 0057d800 ["CALL", null, ["callee:00c5a220:8"]]
- 0057d7c0 bytes 98711b94
+ 0057d800 bytes 88721b94
~~~


<a id="compare-21fe2abe29e893f1f55d034f52d613d3"></a>

### [`0057d7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d7e0.md) → [`0057d820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d820.md) FUN_0057d820

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d7e0.md#insn-0057d808)
- 新版 [`0057d848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d820.md#insn-0057d848)

~~~diff
- 0057d808 ["COPY", "register:0:8", ["register:4048:8"]]
- 0057d808 ["INT_ADD", "register:40f0:8", ["const:57d808:8", "const:4:8"]]
- 0057d808 ["CALLIND", null, ["register:0:8"]]
+ 0057d848 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0057d848 ["INT_ADD", "register:40f0:8", ["const:57d848:8", "const:4:8"]]
+ 0057d848 ["CALLIND", null, ["register:0:8"]]
- 0057d808 bytes 20013fd6
+ 0057d848 bytes 20013fd6
~~~


<a id="compare-cbb6ee7d0d09cb489ee50e9f9abb7ec2"></a>

### [`0057d834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d834.md) → [`0057d874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d874.md) FUN_0057d874

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d834.md#insn-0057d864) · [`0057d888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d834.md#insn-0057d888) · [`0057d898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d834.md#insn-0057d898)
- 新版 [`0057d8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d874.md#insn-0057d8a4) · [`0057d8c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d874.md#insn-0057d8c8) · [`0057d8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d874.md#insn-0057d8d8)

~~~diff
- 0057d864 ["COPY", "register:0:8", ["register:4048:8"]]
- 0057d864 ["INT_ADD", "register:40f0:8", ["const:57d864:8", "const:4:8"]]
- 0057d864 ["CALLIND", null, ["register:0:8"]]
+ 0057d8a4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0057d8a4 ["INT_ADD", "register:40f0:8", ["const:57d8a4:8", "const:4:8"]]
+ 0057d8a4 ["CALLIND", null, ["register:0:8"]]
- 0057d864 bytes 20013fd6
+ 0057d8a4 bytes 20013fd6
- 0057d888 ["COPY", "register:0:8", ["register:4048:8"]]
- 0057d888 ["INT_ADD", "register:40f0:8", ["const:57d888:8", "const:4:8"]]
- 0057d888 ["CALLIND", null, ["register:0:8"]]
+ 0057d8c8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0057d8c8 ["INT_ADD", "register:40f0:8", ["const:57d8c8:8", "const:4:8"]]
+ 0057d8c8 ["CALLIND", null, ["register:0:8"]]
- 0057d888 bytes 20013fd6
+ 0057d8c8 bytes 20013fd6
- 0057d898 ["INT_ADD", "register:40f0:8", ["const:57d898:8", "const:4:8"]]
- 0057d898 ["CALL", null, ["callee:00c5a220:8"]]
+ 0057d8d8 ["INT_ADD", "register:40f0:8", ["const:57d8d8:8", "const:4:8"]]
+ 0057d8d8 ["CALL", null, ["callee:00c5a220:8"]]
- 0057d898 bytes 62711b94
+ 0057d8d8 bytes 52721b94
~~~


<a id="compare-91cc817dab946b233262fc7c47ef8f06"></a>

### [`0057d8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d8c4.md) → [`0057d904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d904.md) FUN_0057d904

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59dc0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d8e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d8c4.md#insn-0057d8e4)
- 新版 [`0057d924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d904.md#insn-0057d924)

~~~diff
- 0057d8e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057d8e4 ["INT_ADD", "register:40f0:8", ["const:57d8e4:8", "const:4:8"]]
- 0057d8e4 ["CALLIND", null, ["register:0:8"]]
+ 0057d924 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057d924 ["INT_ADD", "register:40f0:8", ["const:57d924:8", "const:4:8"]]
+ 0057d924 ["CALLIND", null, ["register:0:8"]]
- 0057d8e4 bytes 00013fd6
+ 0057d924 bytes 00013fd6
~~~


<a id="compare-6f62c5204502caed069d1b29d0d69384"></a>

### [`0057d914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d914.md) → [`0057d954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d954.md) FUN_0057d954

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59dc0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057d938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d914.md#insn-0057d938)
- 新版 [`0057d978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d954.md#insn-0057d978)

~~~diff
- 0057d938 ["COPY", "register:0:8", ["register:4040:8"]]
- 0057d938 ["INT_ADD", "register:40f0:8", ["const:57d938:8", "const:4:8"]]
- 0057d938 ["CALLIND", null, ["register:0:8"]]
+ 0057d978 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057d978 ["INT_ADD", "register:40f0:8", ["const:57d978:8", "const:4:8"]]
+ 0057d978 ["CALLIND", null, ["register:0:8"]]
- 0057d938 bytes 00013fd6
+ 0057d978 bytes 00013fd6
~~~


<a id="compare-c40fb5f6eb8e85b634f6e57b37eaaea0"></a>

### [`0057dc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dc94.md) → [`0057dcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dcd4.md) FUN_0057dcd4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c59e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e30.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5a230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a230.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057dcbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dc94.md#insn-0057dcbc) · [`0057dd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dc94.md#insn-0057dd30) · [`0057dd50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dc94.md#insn-0057dd50)
- 新版 [`0057dcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dcd4.md#insn-0057dcfc) · [`0057dd70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dcd4.md#insn-0057dd70) · [`0057dd90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dcd4.md#insn-0057dd90)

~~~diff
- 0057dcbc ["INT_ADD", "register:40f0:8", ["const:57dcbc:8", "const:4:8"]]
- 0057dcbc ["CALL", null, ["callee:00c5a230:8"]]
+ 0057dcfc ["INT_ADD", "register:40f0:8", ["const:57dcfc:8", "const:4:8"]]
+ 0057dcfc ["CALL", null, ["callee:00c5a230:8"]]
- 0057dcbc bytes 5d701b94
+ 0057dcfc bytes 4d711b94
- 0057dd30 ["INT_ADD", "register:40f0:8", ["const:57dd30:8", "const:4:8"]]
- 0057dd30 ["CALL", null, ["callee:00c57e90:8"]]
+ 0057dd70 ["INT_ADD", "register:40f0:8", ["const:57dd70:8", "const:4:8"]]
+ 0057dd70 ["CALL", null, ["callee:00c57e90:8"]]
- 0057dd30 bytes 58671b94
+ 0057dd70 bytes 48681b94
- 0057dd50 ["INT_ADD", "register:40f0:8", ["const:57dd50:8", "const:4:8"]]
- 0057dd50 ["CALL", null, ["callee:00c57f40:8"]]
+ 0057dd90 ["INT_ADD", "register:40f0:8", ["const:57dd90:8", "const:4:8"]]
+ 0057dd90 ["CALL", null, ["callee:00c57f40:8"]]
- 0057dd50 bytes 7c671b94
+ 0057dd90 bytes 6c681b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9de7d174861a1ba31ecc3a3002255466"></a>

### [`0057dda8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dda8.md) → [`0057dde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dde8.md) FUN_0057dde8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00580464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580464.md) · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 1件 [`005804a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/005804a4.md) · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057ddc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dda8.md#insn-0057ddc4)
- 新版 [`0057de04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dde8.md#insn-0057de04)

~~~diff
- 0057ddc4 ["INT_ADD", "register:40f0:8", ["const:57ddc4:8", "const:4:8"]]
- 0057ddc4 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0057de04 ["INT_ADD", "register:40f0:8", ["const:57de04:8", "const:4:8"]]
+ 0057de04 ["CALL", null, ["callee:00c53cd0:8"]]
- 0057ddc4 bytes bb561b94
+ 0057de04 bytes b3571b94
~~~


<a id="compare-cea55beb37397cb0064a5679abbddece"></a>

### [`0057e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e000.md) → [`0057e040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e040.md) FUN_0057e040

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057e01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e000.md#insn-0057e01c) · [`0057e03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e000.md#insn-0057e03c)
- 新版 [`0057e05c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e040.md#insn-0057e05c) · [`0057e07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e040.md#insn-0057e07c)

~~~diff
- 0057e01c ["INT_ADD", "register:40f0:8", ["const:57e01c:8", "const:4:8"]]
- 0057e01c ["CALL", null, ["callee:00c53d00:8"]]
+ 0057e05c ["INT_ADD", "register:40f0:8", ["const:57e05c:8", "const:4:8"]]
+ 0057e05c ["CALL", null, ["callee:00c53d00:8"]]
- 0057e01c bytes 31561b94
+ 0057e05c bytes 29571b94
- 0057e03c ["COPY", "register:0:8", ["register:4040:8"]]
- 0057e03c ["INT_ADD", "register:40f0:8", ["const:57e03c:8", "const:4:8"]]
- 0057e03c ["CALLIND", null, ["register:0:8"]]
+ 0057e07c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057e07c ["INT_ADD", "register:40f0:8", ["const:57e07c:8", "const:4:8"]]
+ 0057e07c ["CALLIND", null, ["register:0:8"]]
- 0057e03c bytes 00013fd6
+ 0057e07c bytes 00013fd6
~~~


<a id="compare-b8ad40e2bd871e09173f0c7f866857ce"></a>

### [`0057e3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e3a8.md) → [`0057e3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e3e8.md) FUN_0057e3e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00550bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bdc.md) · 呼出先 1件 [`00c59e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e50.md)
- 新版 呼出元 1件 [`00550c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c1c.md) · 呼出先 1件 [`00c5a250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a250.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057e3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e3a8.md#insn-0057e3c4)
- 新版 [`0057e404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e3e8.md#insn-0057e404)

~~~diff
- 0057e3c4 ["INT_ADD", "register:40f0:8", ["const:57e3c4:8", "const:4:8"]]
- 0057e3c4 ["CALL", null, ["callee:00c5a250:8"]]
+ 0057e404 ["INT_ADD", "register:40f0:8", ["const:57e404:8", "const:4:8"]]
+ 0057e404 ["CALL", null, ["callee:00c5a250:8"]]
- 0057e3c4 bytes a36e1b94
+ 0057e404 bytes 936f1b94
~~~


<a id="compare-223eaf5648e9bea2ccd561a8bb212656"></a>

### [`0057e3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e3d8.md) → [`0057e418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e418.md) FUN_0057e418

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00550be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be0.md) · 呼出先 5件 [`00550b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550b64.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59460.md)
- 新版 呼出元 1件 [`00550c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c20.md) · 呼出先 5件 [`00550ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550ba4.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59860.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057e410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e3d8.md#insn-0057e410) · [`0057e424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e3d8.md#insn-0057e424) · [`0057e440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e3d8.md#insn-0057e440)
- 新版 [`0057e450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e418.md#insn-0057e450) · [`0057e464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e418.md#insn-0057e464) · [`0057e480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e418.md#insn-0057e480)

~~~diff
- 0057e410 ["INT_ADD", "register:40f0:8", ["const:57e410:8", "const:4:8"]]
- 0057e410 ["CALL", null, ["callee:00c59860:8"]]
+ 0057e450 ["INT_ADD", "register:40f0:8", ["const:57e450:8", "const:4:8"]]
+ 0057e450 ["CALL", null, ["callee:00c59860:8"]]
- 0057e410 bytes 146c1b94
+ 0057e450 bytes 046d1b94
- 0057e424 ["INT_ADD", "register:40f0:8", ["const:57e424:8", "const:4:8"]]
- 0057e424 ["CALL", null, ["callee:00550ba4:8"]]
+ 0057e464 ["INT_ADD", "register:40f0:8", ["const:57e464:8", "const:4:8"]]
+ 0057e464 ["CALL", null, ["callee:00550ba4:8"]]
- 0057e424 bytes d049ff97
+ 0057e464 bytes d049ff97
- 0057e440 ["INT_ADD", "register:40f0:8", ["const:57e440:8", "const:4:8"]]
- 0057e440 ["CALL", null, ["callee:00c53d00:8"]]
+ 0057e480 ["INT_ADD", "register:40f0:8", ["const:57e480:8", "const:4:8"]]
+ 0057e480 ["CALL", null, ["callee:00c53d00:8"]]
- 0057e440 bytes 28551b94
+ 0057e480 bytes 20561b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-707e2cbd1947516cc4ce6b4520072fc2"></a>

### [`0057eb4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057eb4c.md) → [`0057eb8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057eb8c.md) FUN_0057eb8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00550bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bf0.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59460.md)
- 新版 呼出元 1件 [`00550c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c30.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59860.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057eb7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057eb4c.md#insn-0057eb7c) · [`0057ebac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057eb4c.md#insn-0057ebac)
- 新版 [`0057ebbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057eb8c.md#insn-0057ebbc) · [`0057ebec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057eb8c.md#insn-0057ebec)

~~~diff
- 0057eb7c ["INT_ADD", "register:40f0:8", ["const:57eb7c:8", "const:4:8"]]
- 0057eb7c ["CALL", null, ["callee:00c59860:8"]]
+ 0057ebbc ["INT_ADD", "register:40f0:8", ["const:57ebbc:8", "const:4:8"]]
+ 0057ebbc ["CALL", null, ["callee:00c59860:8"]]
- 0057eb7c bytes 396a1b94
+ 0057ebbc bytes 296b1b94
- 0057ebac ["INT_ADD", "register:40f0:8", ["const:57ebac:8", "const:4:8"]]
- 0057ebac ["CALL", null, ["callee:00c57ee0:8"]]
+ 0057ebec ["INT_ADD", "register:40f0:8", ["const:57ebec:8", "const:4:8"]]
+ 0057ebec ["CALL", null, ["callee:00c57ee0:8"]]
- 0057ebac bytes cd631b94
+ 0057ebec bytes bd641b94
~~~


<a id="compare-f2a6c25ae7acd80b3230b94a0d01a9b0"></a>

### [`0057ebb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ebb4.md) → [`0057ebf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ebf4.md) FUN_0057ebf4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00550cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550cec.md) · 呼出先 1件 [`00c59e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e60.md)
- 新版 呼出元 1件 [`00550d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550d2c.md) · 呼出先 1件 [`00c5a260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a260.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057ebcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ebb4.md#insn-0057ebcc)
- 新版 [`0057ec0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ebf4.md#insn-0057ec0c)

~~~diff
- 0057ebcc ["INT_ADD", "register:40f0:8", ["const:57ebcc:8", "const:4:8"]]
- 0057ebcc ["CALL", null, ["callee:00c5a260:8"]]
+ 0057ec0c ["INT_ADD", "register:40f0:8", ["const:57ec0c:8", "const:4:8"]]
+ 0057ec0c ["CALL", null, ["callee:00c5a260:8"]]
- 0057ebcc bytes a56c1b94
+ 0057ec0c bytes 956d1b94
~~~


<a id="compare-eef8364dfb00e02805f2847afe0ede23"></a>

### [`0057ebe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ebe0.md) → [`0057ec20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ec20.md) FUN_0057ec20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00550cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550cf0.md) · 呼出先 1件 [`00c59e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e90.md)
- 新版 呼出元 1件 [`00550d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550d30.md) · 呼出先 1件 [`00c5a290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057ec08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ebe0.md#insn-0057ec08)
- 新版 [`0057ec48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ec20.md#insn-0057ec48)

~~~diff
- 0057ec08 ["INT_ADD", "register:40f0:8", ["const:57ec08:8", "const:4:8"]]
- 0057ec08 ["CALL", null, ["callee:00c5a290:8"]]
+ 0057ec48 ["INT_ADD", "register:40f0:8", ["const:57ec48:8", "const:4:8"]]
+ 0057ec48 ["CALL", null, ["callee:00c5a290:8"]]
- 0057ec08 bytes a26c1b94
+ 0057ec48 bytes 926d1b94
~~~


<a id="compare-6897639b627c1ffaf99b2bf347c8d886"></a>

### [`0057ec1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ec1c.md) → [`0057ec5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ec5c.md) FUN_0057ec5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00550cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550cf4.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ea0.md)
- 新版 呼出元 1件 [`00550d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550d34.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a2a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057ec4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ec1c.md#insn-0057ec4c) · [`0057ec84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ec1c.md#insn-0057ec84)
- 新版 [`0057ec8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ec5c.md#insn-0057ec8c) · [`0057ecc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ec5c.md#insn-0057ecc4)

~~~diff
- 0057ec4c ["INT_ADD", "register:40f0:8", ["const:57ec4c:8", "const:4:8"]]
- 0057ec4c ["CALL", null, ["callee:00c5a2a0:8"]]
+ 0057ec8c ["INT_ADD", "register:40f0:8", ["const:57ec8c:8", "const:4:8"]]
+ 0057ec8c ["CALL", null, ["callee:00c5a2a0:8"]]
- 0057ec4c bytes 956c1b94
+ 0057ec8c bytes 856d1b94
- 0057ec84 ["INT_ADD", "register:40f0:8", ["const:57ec84:8", "const:4:8"]]
- 0057ec84 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0057ecc4 ["INT_ADD", "register:40f0:8", ["const:57ecc4:8", "const:4:8"]]
+ 0057ecc4 ["CALL", null, ["callee:00c57ee0:8"]]
- 0057ec84 bytes 97631b94
+ 0057ecc4 bytes 87641b94
~~~


<a id="compare-2ff9607f44b0922bb828846d0e53346a"></a>

### [`0057ec8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ec8c.md) → [`0057eccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057eccc.md) FUN_0057eccc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00555254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555254.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00555294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555294.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057ec9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ec8c.md#insn-0057ec9c)
- 新版 [`0057ecdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057eccc.md#insn-0057ecdc)

~~~diff
- 0057ec9c ["INT_ADD", "register:40f0:8", ["const:57ec9c:8", "const:4:8"]]
- 0057ec9c ["CALL", null, ["callee:00555294:8"]]
+ 0057ecdc ["INT_ADD", "register:40f0:8", ["const:57ecdc:8", "const:4:8"]]
+ 0057ecdc ["CALL", null, ["callee:00555294:8"]]
- 0057ec9c bytes 6e59ff97
+ 0057ecdc bytes 6e59ff97
~~~


<a id="compare-62af1e8be48346cc138a27cd58bef0c2"></a>

### [`0057fce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fce0.md) → [`0057fd20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fd20.md) FUN_0057fd20

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0055525c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/0055525c.md) · 呼出先 3件 [`0057facc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057facc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0055529c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/0055529c.md) · 呼出先 3件 [`0057fb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fb0c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057fd04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fce0.md#insn-0057fd04) · [`0057fd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fce0.md#insn-0057fd14) · [`0057fd64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fce0.md#insn-0057fd64)
- 新版 [`0057fd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fd20.md#insn-0057fd44) · [`0057fd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fd20.md#insn-0057fd54) · [`0057fda4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fd20.md#insn-0057fda4)

~~~diff
- 0057fd04 ["INT_ADD", "register:40f0:8", ["const:57fd04:8", "const:4:8"]]
- 0057fd04 ["CALL", null, ["callee:0057fb0c:8"]]
+ 0057fd44 ["INT_ADD", "register:40f0:8", ["const:57fd44:8", "const:4:8"]]
+ 0057fd44 ["CALL", null, ["callee:0057fb0c:8"]]
- 0057fd04 bytes 72ffff97
+ 0057fd44 bytes 72ffff97
- 0057fd14 ["INT_ADD", "register:40f0:8", ["const:57fd14:8", "const:4:8"]]
- 0057fd14 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0057fd54 ["INT_ADD", "register:40f0:8", ["const:57fd54:8", "const:4:8"]]
+ 0057fd54 ["CALL", null, ["callee:00c57eb0:8"]]
- 0057fd14 bytes 675f1b94
+ 0057fd54 bytes 57601b94
- 0057fd64 ["INT_ADD", "register:40f0:8", ["const:57fd64:8", "const:4:8"]]
- 0057fd64 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0057fda4 ["INT_ADD", "register:40f0:8", ["const:57fda4:8", "const:4:8"]]
+ 0057fda4 ["CALL", null, ["callee:00c57ee0:8"]]
- 0057fd64 bytes 5f5f1b94
+ 0057fda4 bytes 4f601b94
~~~


<a id="compare-db13e3a1a73c78a07009b34ae43f09fe"></a>

### [`0057febc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057febc.md) → [`0057fefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fefc.md) FUN_0057fefc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00555268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555268.md) · 呼出先 3件 [`0057facc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057facc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005552a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/005552a8.md) · 呼出先 3件 [`0057fb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fb0c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057fefc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057febc.md#insn-0057fefc) · [`0057ff0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057febc.md#insn-0057ff0c) · [`0057ff5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057febc.md#insn-0057ff5c)
- 新版 [`0057ff3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fefc.md#insn-0057ff3c) · [`0057ff4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fefc.md#insn-0057ff4c) · [`0057ff9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fefc.md#insn-0057ff9c)

~~~diff
- 0057fefc ["INT_ADD", "register:40f0:8", ["const:57fefc:8", "const:4:8"]]
- 0057fefc ["CALL", null, ["callee:0057fb0c:8"]]
+ 0057ff3c ["INT_ADD", "register:40f0:8", ["const:57ff3c:8", "const:4:8"]]
+ 0057ff3c ["CALL", null, ["callee:0057fb0c:8"]]
- 0057fefc bytes f4feff97
+ 0057ff3c bytes f4feff97
- 0057ff0c ["INT_ADD", "register:40f0:8", ["const:57ff0c:8", "const:4:8"]]
- 0057ff0c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0057ff4c ["INT_ADD", "register:40f0:8", ["const:57ff4c:8", "const:4:8"]]
+ 0057ff4c ["CALL", null, ["callee:00c57eb0:8"]]
- 0057ff0c bytes e95e1b94
+ 0057ff4c bytes d95f1b94
- 0057ff5c ["INT_ADD", "register:40f0:8", ["const:57ff5c:8", "const:4:8"]]
- 0057ff5c ["CALL", null, ["callee:00c57ee0:8"]]
+ 0057ff9c ["INT_ADD", "register:40f0:8", ["const:57ff9c:8", "const:4:8"]]
+ 0057ff9c ["CALL", null, ["callee:00c57ee0:8"]]
- 0057ff5c bytes e15e1b94
+ 0057ff9c bytes d15f1b94
~~~


<a id="compare-da78af89df086d9b564efa3b48f8f24c"></a>

### [`005807a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/005807a8.md) → [`005807e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/005807e8.md) FUN_005807e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005807c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/005807a8.md#insn-005807c4) · [`005807e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/005807a8.md#insn-005807e4)
- 新版 [`00580804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/005807e8.md#insn-00580804) · [`00580824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/005807e8.md#insn-00580824)

~~~diff
- 005807c4 ["INT_ADD", "register:40f0:8", ["const:5807c4:8", "const:4:8"]]
- 005807c4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00580804 ["INT_ADD", "register:40f0:8", ["const:580804:8", "const:4:8"]]
+ 00580804 ["CALL", null, ["callee:00c53d00:8"]]
- 005807c4 bytes 474c1b94
+ 00580804 bytes 3f4d1b94
- 005807e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005807e4 ["INT_ADD", "register:40f0:8", ["const:5807e4:8", "const:4:8"]]
- 005807e4 ["CALLIND", null, ["register:0:8"]]
+ 00580824 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00580824 ["INT_ADD", "register:40f0:8", ["const:580824:8", "const:4:8"]]
+ 00580824 ["CALLIND", null, ["register:0:8"]]
- 005807e4 bytes 00013fd6
+ 00580824 bytes 00013fd6
~~~


<a id="compare-5cf5c5d54bb8501229f31b223a6d296c"></a>

### [`005807f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/005807f8.md) → [`00580838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580838.md) FUN_00580838

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00580814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/005807f8.md#insn-00580814) · [`00580834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/005807f8.md#insn-00580834)
- 新版 [`00580854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580838.md#insn-00580854) · [`00580874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580838.md#insn-00580874)

~~~diff
- 00580814 ["INT_ADD", "register:40f0:8", ["const:580814:8", "const:4:8"]]
- 00580814 ["CALL", null, ["callee:00c53d00:8"]]
+ 00580854 ["INT_ADD", "register:40f0:8", ["const:580854:8", "const:4:8"]]
+ 00580854 ["CALL", null, ["callee:00c53d00:8"]]
- 00580814 bytes 334c1b94
+ 00580854 bytes 2b4d1b94
- 00580834 ["COPY", "register:0:8", ["register:4040:8"]]
- 00580834 ["INT_ADD", "register:40f0:8", ["const:580834:8", "const:4:8"]]
- 00580834 ["CALLIND", null, ["register:0:8"]]
+ 00580874 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00580874 ["INT_ADD", "register:40f0:8", ["const:580874:8", "const:4:8"]]
+ 00580874 ["CALLIND", null, ["register:0:8"]]
- 00580834 bytes 00013fd6
+ 00580874 bytes 00013fd6
~~~


<a id="compare-ffdd015394ec9b86b7f8ed34cab4649f"></a>

### [`00580a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580a48.md) → [`00580a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580a88.md) FUN_00580a88

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00560418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560418.md) · 呼出先 2件 [`00c587a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587a0.md) [`00c587d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587d0.md)
- 新版 呼出元 1件 [`00560458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560458.md) · 呼出先 2件 [`00c58ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ba0.md) [`00c58bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58bd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00580a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580a48.md#insn-00580a74) · [`00580a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580a48.md#insn-00580a88) · [`00580aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580a48.md#insn-00580aa0)
- 新版 [`00580ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580a88.md#insn-00580ab4) · [`00580ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580a88.md#insn-00580ac8) · [`00580ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580a88.md#insn-00580ae0)

~~~diff
- 00580a74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00580a74 ["INT_ADD", "register:40f0:8", ["const:580a74:8", "const:4:8"]]
- 00580a74 ["CALLIND", null, ["register:0:8"]]
+ 00580ab4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00580ab4 ["INT_ADD", "register:40f0:8", ["const:580ab4:8", "const:4:8"]]
+ 00580ab4 ["CALLIND", null, ["register:0:8"]]
- 00580a74 bytes 00013fd6
+ 00580ab4 bytes 00013fd6
- 00580a88 ["COPY", "register:0:8", ["register:4040:8"]]
- 00580a88 ["INT_ADD", "register:40f0:8", ["const:580a88:8", "const:4:8"]]
- 00580a88 ["CALLIND", null, ["register:0:8"]]
+ 00580ac8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00580ac8 ["INT_ADD", "register:40f0:8", ["const:580ac8:8", "const:4:8"]]
+ 00580ac8 ["CALLIND", null, ["register:0:8"]]
- 00580a88 bytes 00013fd6
+ 00580ac8 bytes 00013fd6
- 00580aa0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00580aa0 ["INT_ADD", "register:40f0:8", ["const:580aa0:8", "const:4:8"]]
- 00580aa0 ["CALLIND", null, ["register:0:8"]]
+ 00580ae0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00580ae0 ["INT_ADD", "register:40f0:8", ["const:580ae0:8", "const:4:8"]]
+ 00580ae0 ["CALLIND", null, ["register:0:8"]]
- 00580aa0 bytes 20013fd6
+ 00580ae0 bytes 20013fd6
~~~


<a id="compare-a4b94d824fbe52c181b958e4b2dec3ee"></a>

### [`00580f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580f68.md) → [`00580fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580fa8.md) FUN_00580fa8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00580f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580f68.md#insn-00580f84) · [`00580fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580f68.md#insn-00580fa4)
- 新版 [`00580fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580fa8.md#insn-00580fc4) · [`00580fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580fa8.md#insn-00580fe4)

~~~diff
- 00580f84 ["INT_ADD", "register:40f0:8", ["const:580f84:8", "const:4:8"]]
- 00580f84 ["CALL", null, ["callee:00c53d00:8"]]
+ 00580fc4 ["INT_ADD", "register:40f0:8", ["const:580fc4:8", "const:4:8"]]
+ 00580fc4 ["CALL", null, ["callee:00c53d00:8"]]
- 00580f84 bytes 574a1b94
+ 00580fc4 bytes 4f4b1b94
- 00580fa4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00580fa4 ["INT_ADD", "register:40f0:8", ["const:580fa4:8", "const:4:8"]]
- 00580fa4 ["CALLIND", null, ["register:0:8"]]
+ 00580fe4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00580fe4 ["INT_ADD", "register:40f0:8", ["const:580fe4:8", "const:4:8"]]
+ 00580fe4 ["CALLIND", null, ["register:0:8"]]
- 00580fa4 bytes 00013fd6
+ 00580fe4 bytes 00013fd6
~~~


<a id="compare-bfcc8f299920618439171f02e81b4aff"></a>

### [`00580fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580fb8.md) → [`00580ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580ff8.md) FUN_00580ff8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00580fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580fb8.md#insn-00580fd4) · [`00580ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580fb8.md#insn-00580ff4)
- 新版 [`00581014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580ff8.md#insn-00581014) · [`00581034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580ff8.md#insn-00581034)

~~~diff
- 00580fd4 ["INT_ADD", "register:40f0:8", ["const:580fd4:8", "const:4:8"]]
- 00580fd4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00581014 ["INT_ADD", "register:40f0:8", ["const:581014:8", "const:4:8"]]
+ 00581014 ["CALL", null, ["callee:00c53d00:8"]]
- 00580fd4 bytes 434a1b94
+ 00581014 bytes 3b4b1b94
- 00580ff4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00580ff4 ["INT_ADD", "register:40f0:8", ["const:580ff4:8", "const:4:8"]]
- 00580ff4 ["CALLIND", null, ["register:0:8"]]
+ 00581034 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00581034 ["INT_ADD", "register:40f0:8", ["const:581034:8", "const:4:8"]]
+ 00581034 ["CALLIND", null, ["register:0:8"]]
- 00580ff4 bytes 00013fd6
+ 00581034 bytes 00013fd6
~~~


<a id="compare-54a59ed180c029694df2afa062417907"></a>

### [`00581bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581bb8.md) → [`00581bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581bf8.md) FUN_00581bf8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00560424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560424.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c60.md) [`00c58200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58200.md)
- 新版 呼出元 1件 [`00560464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560464.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58060.md) [`00c58600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58600.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00581c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581bb8.md#insn-00581c34) · [`00581cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581bb8.md#insn-00581cf4) · [`00581d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581bb8.md#insn-00581d00)
- 新版 [`00581c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581bf8.md#insn-00581c74) · [`00581d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581bf8.md#insn-00581d34) · [`00581d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581bf8.md#insn-00581d40)

~~~diff
- 00581c34 ["INT_ADD", "register:40f0:8", ["const:581c34:8", "const:4:8"]]
- 00581c34 ["CALL", null, ["callee:00c58600:8"]]
+ 00581c74 ["INT_ADD", "register:40f0:8", ["const:581c74:8", "const:4:8"]]
+ 00581c74 ["CALL", null, ["callee:00c58600:8"]]
- 00581c34 bytes 73591b94
+ 00581c74 bytes 635a1b94
- 00581cf4 ["INT_ADD", "register:40f0:8", ["const:581cf4:8", "const:4:8"]]
- 00581cf4 ["CALL", null, ["callee:00c58060:8"]]
+ 00581d34 ["INT_ADD", "register:40f0:8", ["const:581d34:8", "const:4:8"]]
+ 00581d34 ["CALL", null, ["callee:00c58060:8"]]
- 00581cf4 bytes db571b94
+ 00581d34 bytes cb581b94
- 00581d00 ["INT_ADD", "register:40f0:8", ["const:581d00:8", "const:4:8"]]
- 00581d00 ["CALL", null, ["callee:00c58600:8"]]
+ 00581d40 ["INT_ADD", "register:40f0:8", ["const:581d40:8", "const:4:8"]]
+ 00581d40 ["CALL", null, ["callee:00c58600:8"]]
- 00581d00 bytes 40591b94
+ 00581d40 bytes 305a1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aefffaa4eab94a0d5d58eaa9ab94581b"></a>

### [`00581ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581ef4.md) → [`00581f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581f34.md) FUN_00581f34

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00581f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581ef4.md#insn-00581f14)
- 新版 [`00581f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581f34.md#insn-00581f54)

~~~diff
- 00581f14 ["COPY", "register:0:8", ["register:4050:8"]]
- 00581f14 ["INT_ADD", "register:40f0:8", ["const:581f14:8", "const:4:8"]]
- 00581f14 ["CALLIND", null, ["register:0:8"]]
+ 00581f54 ["COPY", "register:0:8", ["register:4050:8"]]
+ 00581f54 ["INT_ADD", "register:40f0:8", ["const:581f54:8", "const:4:8"]]
+ 00581f54 ["CALLIND", null, ["register:0:8"]]
- 00581f14 bytes 40013fd6
+ 00581f54 bytes 40013fd6
~~~


<a id="compare-3401e5d209c2a588fb167d2365c145b4"></a>

### [`00582af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582af8.md) → [`00582b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582b38.md) FUN_00582b38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`005975cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975cc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0059760c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059760c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00582b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582af8.md#insn-00582b30) · [`00582b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582af8.md#insn-00582b4c) · [`00582b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582af8.md#insn-00582b68)
- 新版 [`00582b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582b38.md#insn-00582b70) · [`00582b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582b38.md#insn-00582b8c) · [`00582ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582b38.md#insn-00582ba8)

~~~diff
- 00582b30 ["COPY", "register:0:8", ["register:4048:8"]]
- 00582b30 ["INT_ADD", "register:40f0:8", ["const:582b30:8", "const:4:8"]]
- 00582b30 ["CALLIND", null, ["register:0:8"]]
+ 00582b70 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00582b70 ["INT_ADD", "register:40f0:8", ["const:582b70:8", "const:4:8"]]
+ 00582b70 ["CALLIND", null, ["register:0:8"]]
- 00582b30 bytes 20013fd6
+ 00582b70 bytes 20013fd6
- 00582b4c ["INT_ADD", "register:40f0:8", ["const:582b4c:8", "const:4:8"]]
- 00582b4c ["CALL", null, ["callee:00c57e90:8"]]
+ 00582b8c ["INT_ADD", "register:40f0:8", ["const:582b8c:8", "const:4:8"]]
+ 00582b8c ["CALL", null, ["callee:00c57e90:8"]]
- 00582b4c bytes d1531b94
+ 00582b8c bytes c1541b94
- 00582b68 ["INT_ADD", "register:40f0:8", ["const:582b68:8", "const:4:8"]]
- 00582b68 ["CALL", null, ["callee:00c58090:8"]]
+ 00582ba8 ["INT_ADD", "register:40f0:8", ["const:582ba8:8", "const:4:8"]]
+ 00582ba8 ["CALL", null, ["callee:00c58090:8"]]
- 00582b68 bytes 4a541b94
+ 00582ba8 bytes 3a551b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b7c071af0b3ac21cb91ec3696bc5dea"></a>

### [`00583184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583184.md) → [`005831c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005831c4.md) FUN_005831c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`005975cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975cc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0059760c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059760c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005831bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583184.md#insn-005831bc) · [`005831d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583184.md#insn-005831d8) · [`005831f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583184.md#insn-005831f4)
- 新版 [`005831fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005831c4.md#insn-005831fc) · [`00583218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005831c4.md#insn-00583218) · [`00583234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005831c4.md#insn-00583234)

~~~diff
- 005831bc ["COPY", "register:0:8", ["register:4048:8"]]
- 005831bc ["INT_ADD", "register:40f0:8", ["const:5831bc:8", "const:4:8"]]
- 005831bc ["CALLIND", null, ["register:0:8"]]
+ 005831fc ["COPY", "register:0:8", ["register:4048:8"]]
+ 005831fc ["INT_ADD", "register:40f0:8", ["const:5831fc:8", "const:4:8"]]
+ 005831fc ["CALLIND", null, ["register:0:8"]]
- 005831bc bytes 20013fd6
+ 005831fc bytes 20013fd6
- 005831d8 ["INT_ADD", "register:40f0:8", ["const:5831d8:8", "const:4:8"]]
- 005831d8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00583218 ["INT_ADD", "register:40f0:8", ["const:583218:8", "const:4:8"]]
+ 00583218 ["CALL", null, ["callee:00c57e90:8"]]
- 005831d8 bytes 2e521b94
+ 00583218 bytes 1e531b94
- 005831f4 ["INT_ADD", "register:40f0:8", ["const:5831f4:8", "const:4:8"]]
- 005831f4 ["CALL", null, ["callee:00c58090:8"]]
+ 00583234 ["INT_ADD", "register:40f0:8", ["const:583234:8", "const:4:8"]]
+ 00583234 ["CALL", null, ["callee:00c58090:8"]]
- 005831f4 bytes a7521b94
+ 00583234 bytes 97531b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4da2d80cc7d095395b948f9d2cd91cb"></a>

### [`0058335c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058335c.md) → [`0058339c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058339c.md) FUN_0058339c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c59ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c5a2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a2e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005833ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058335c.md#insn-005833ac) · [`005833e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058335c.md#insn-005833e8)
- 新版 [`005833ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058339c.md#insn-005833ec) · [`00583428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058339c.md#insn-00583428)

~~~diff
- 005833ac ["INT_ADD", "register:40f0:8", ["const:5833ac:8", "const:4:8"]]
- 005833ac ["CALL", null, ["callee:00c5a2e0:8"]]
+ 005833ec ["INT_ADD", "register:40f0:8", ["const:5833ec:8", "const:4:8"]]
+ 005833ec ["CALL", null, ["callee:00c5a2e0:8"]]
- 005833ac bytes cd5a1b94
+ 005833ec bytes bd5b1b94
- 005833e8 ["INT_ADD", "register:40f0:8", ["const:5833e8:8", "const:4:8"]]
- 005833e8 ["CALL", null, ["callee:00c5a2e0:8"]]
+ 00583428 ["INT_ADD", "register:40f0:8", ["const:583428:8", "const:4:8"]]
+ 00583428 ["CALL", null, ["callee:00c5a2e0:8"]]
- 005833e8 bytes be5a1b94
+ 00583428 bytes ae5b1b94
~~~


<a id="compare-756ad000ac2e34055abfef240658ae35"></a>

### [`0058367c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058367c.md) → [`005836bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005836bc.md) FUN_005836bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00583698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058367c.md#insn-00583698) · [`005836b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058367c.md#insn-005836b8)
- 新版 [`005836d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005836bc.md#insn-005836d8) · [`005836f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005836bc.md#insn-005836f8)

~~~diff
- 00583698 ["INT_ADD", "register:40f0:8", ["const:583698:8", "const:4:8"]]
- 00583698 ["CALL", null, ["callee:00c53d00:8"]]
+ 005836d8 ["INT_ADD", "register:40f0:8", ["const:5836d8:8", "const:4:8"]]
+ 005836d8 ["CALL", null, ["callee:00c53d00:8"]]
- 00583698 bytes 92401b94
+ 005836d8 bytes 8a411b94
- 005836b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005836b8 ["INT_ADD", "register:40f0:8", ["const:5836b8:8", "const:4:8"]]
- 005836b8 ["CALLIND", null, ["register:0:8"]]
+ 005836f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005836f8 ["INT_ADD", "register:40f0:8", ["const:5836f8:8", "const:4:8"]]
+ 005836f8 ["CALLIND", null, ["register:0:8"]]
- 005836b8 bytes 00013fd6
+ 005836f8 bytes 00013fd6
~~~


<a id="compare-bae5531085373dbcfab82519b9947a16"></a>

### [`005836cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/005836cc.md) → [`0058370c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058370c.md) FUN_0058370c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00549094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549094.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005490d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/005490d4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058371c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/005836cc.md#insn-0058371c) · [`00583748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/005836cc.md#insn-00583748) · [`00583754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/005836cc.md#insn-00583754)
- 新版 [`0058375c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058370c.md#insn-0058375c) · [`00583788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058370c.md#insn-00583788) · [`00583794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058370c.md#insn-00583794)

~~~diff
- 0058371c ["INT_ADD", "register:40f0:8", ["const:58371c:8", "const:4:8"]]
- 0058371c ["CALL", null, ["callee:0043bb20:8"]]
+ 0058375c ["INT_ADD", "register:40f0:8", ["const:58375c:8", "const:4:8"]]
+ 0058375c ["CALL", null, ["callee:0043bb20:8"]]
- 0058371c bytes f1e0fa97
+ 0058375c bytes f1e0fa97
- 00583748 ["INT_ADD", "register:40f0:8", ["const:583748:8", "const:4:8"]]
- 00583748 ["CALL", null, ["callee:0043bb20:8"]]
+ 00583788 ["INT_ADD", "register:40f0:8", ["const:583788:8", "const:4:8"]]
+ 00583788 ["CALL", null, ["callee:0043bb20:8"]]
- 00583748 bytes e6e0fa97
+ 00583788 bytes e6e0fa97
- 00583754 ["INT_ADD", "register:40f0:8", ["const:583754:8", "const:4:8"]]
- 00583754 ["CALL", null, ["callee:005490d4:8"]]
+ 00583794 ["INT_ADD", "register:40f0:8", ["const:583794:8", "const:4:8"]]
+ 00583794 ["CALL", null, ["callee:005490d4:8"]]
- 00583754 bytes 5016ff97
+ 00583794 bytes 5016ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5084f9af3fe7d393bbefb8d79a0702bd"></a>

### [`005837dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/005837dc.md) → [`0058381c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058381c.md) FUN_0058381c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005837f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/005837dc.md#insn-005837f8)
- 新版 [`00583838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058381c.md#insn-00583838)

~~~diff
- 005837f8 ["INT_ADD", "register:40f0:8", ["const:5837f8:8", "const:4:8"]]
- 005837f8 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00583838 ["INT_ADD", "register:40f0:8", ["const:583838:8", "const:4:8"]]
+ 00583838 ["CALL", null, ["callee:00c53cd0:8"]]
- 005837f8 bytes 2e401b94
+ 00583838 bytes 26411b94
~~~


<a id="compare-df7507a968a747b93b266ba5487ed9a8"></a>

### [`00584790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584790.md) → [`005847d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005847d0.md) FUN_005847d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005847cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584790.md#insn-005847cc) · [`00584800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584790.md#insn-00584800)
- 新版 [`0058480c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005847d0.md#insn-0058480c) · [`00584840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005847d0.md#insn-00584840)

~~~diff
- 005847cc ["COPY", "register:0:8", ["register:4040:8"]]
- 005847cc ["INT_ADD", "register:40f0:8", ["const:5847cc:8", "const:4:8"]]
- 005847cc ["CALLIND", null, ["register:0:8"]]
+ 0058480c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058480c ["INT_ADD", "register:40f0:8", ["const:58480c:8", "const:4:8"]]
+ 0058480c ["CALLIND", null, ["register:0:8"]]
- 005847cc bytes 00013fd6
+ 0058480c bytes 00013fd6
- 00584800 ["COPY", "register:0:8", ["register:4040:8"]]
- 00584800 ["INT_ADD", "register:40f0:8", ["const:584800:8", "const:4:8"]]
- 00584800 ["CALLIND", null, ["register:0:8"]]
+ 00584840 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00584840 ["INT_ADD", "register:40f0:8", ["const:584840:8", "const:4:8"]]
+ 00584840 ["CALLIND", null, ["register:0:8"]]
- 00584800 bytes 00013fd6
+ 00584840 bytes 00013fd6
~~~


<a id="compare-a6a699641197ae79e2fff5c5287cbfbe"></a>

### [`00584b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584b80.md) → [`00584bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584bc0.md) FUN_00584bc0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00584b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584b80.md#insn-00584b9c) · [`00584bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584b80.md#insn-00584bbc)
- 新版 [`00584bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584bc0.md#insn-00584bdc) · [`00584bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584bc0.md#insn-00584bfc)

~~~diff
- 00584b9c ["INT_ADD", "register:40f0:8", ["const:584b9c:8", "const:4:8"]]
- 00584b9c ["CALL", null, ["callee:00c53d00:8"]]
+ 00584bdc ["INT_ADD", "register:40f0:8", ["const:584bdc:8", "const:4:8"]]
+ 00584bdc ["CALL", null, ["callee:00c53d00:8"]]
- 00584b9c bytes 513b1b94
+ 00584bdc bytes 493c1b94
- 00584bbc ["COPY", "register:0:8", ["register:4040:8"]]
- 00584bbc ["INT_ADD", "register:40f0:8", ["const:584bbc:8", "const:4:8"]]
- 00584bbc ["CALLIND", null, ["register:0:8"]]
+ 00584bfc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00584bfc ["INT_ADD", "register:40f0:8", ["const:584bfc:8", "const:4:8"]]
+ 00584bfc ["CALLIND", null, ["register:0:8"]]
- 00584bbc bytes 00013fd6
+ 00584bfc bytes 00013fd6
~~~


<a id="compare-db98d73e71388f961636fd8af53bea90"></a>

### [`00584bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584bd0.md) → [`00584c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584c10.md) FUN_00584c10

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00584bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584bd0.md#insn-00584bec) · [`00584c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584bd0.md#insn-00584c0c)
- 新版 [`00584c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584c10.md#insn-00584c2c) · [`00584c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584c10.md#insn-00584c4c)

~~~diff
- 00584bec ["INT_ADD", "register:40f0:8", ["const:584bec:8", "const:4:8"]]
- 00584bec ["CALL", null, ["callee:00c53d00:8"]]
+ 00584c2c ["INT_ADD", "register:40f0:8", ["const:584c2c:8", "const:4:8"]]
+ 00584c2c ["CALL", null, ["callee:00c53d00:8"]]
- 00584bec bytes 3d3b1b94
+ 00584c2c bytes 353c1b94
- 00584c0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00584c0c ["INT_ADD", "register:40f0:8", ["const:584c0c:8", "const:4:8"]]
- 00584c0c ["CALLIND", null, ["register:0:8"]]
+ 00584c4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00584c4c ["INT_ADD", "register:40f0:8", ["const:584c4c:8", "const:4:8"]]
+ 00584c4c ["CALLIND", null, ["register:0:8"]]
- 00584c0c bytes 00013fd6
+ 00584c4c bytes 00013fd6
~~~


<a id="compare-6a35a6308f5f68d84aa366940e7cbcfe"></a>

### [`00584c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584c20.md) → [`00584c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584c60.md) FUN_00584c60

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00584c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584c20.md#insn-00584c44) · [`00584c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584c20.md#insn-00584c5c) · [`00584c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584c20.md#insn-00584c80)
- 新版 [`00584c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584c60.md#insn-00584c84) · [`00584c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584c60.md#insn-00584c9c) · [`00584cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584c60.md#insn-00584cc0)

~~~diff
- 00584c44 ["INT_ADD", "register:40f0:8", ["const:584c44:8", "const:4:8"]]
- 00584c44 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00584c84 ["INT_ADD", "register:40f0:8", ["const:584c84:8", "const:4:8"]]
+ 00584c84 ["CALL", null, ["callee:00c53cd0:8"]]
- 00584c44 bytes 1b3b1b94
+ 00584c84 bytes 133c1b94
- 00584c5c ["INT_ADD", "register:40f0:8", ["const:584c5c:8", "const:4:8"]]
- 00584c5c ["CALL", null, ["callee:00c53d00:8"]]
+ 00584c9c ["INT_ADD", "register:40f0:8", ["const:584c9c:8", "const:4:8"]]
+ 00584c9c ["CALL", null, ["callee:00c53d00:8"]]
- 00584c5c bytes 213b1b94
+ 00584c9c bytes 193c1b94
- 00584c80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00584c80 ["INT_ADD", "register:40f0:8", ["const:584c80:8", "const:4:8"]]
- 00584c80 ["CALLIND", null, ["register:0:8"]]
+ 00584cc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00584cc0 ["INT_ADD", "register:40f0:8", ["const:584cc0:8", "const:4:8"]]
+ 00584cc0 ["CALLIND", null, ["register:0:8"]]
- 00584c80 bytes 00013fd6
+ 00584cc0 bytes 00013fd6
~~~


<a id="compare-7348ee319a82440620e1860192290ff8"></a>

### [`00584c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584c98.md) → [`00584cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584cd8.md) FUN_00584cd8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`005975c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975c8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00597608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597608.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00584cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584c98.md#insn-00584cc4) · [`00584ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584c98.md#insn-00584ce4) · [`00584cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584c98.md#insn-00584cf8)
- 新版 [`00584d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584cd8.md#insn-00584d04) · [`00584d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584cd8.md#insn-00584d24) · [`00584d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584cd8.md#insn-00584d38)

~~~diff
- 00584cc4 ["INT_ADD", "register:40f0:8", ["const:584cc4:8", "const:4:8"]]
- 00584cc4 ["CALL", null, ["callee:00597608:8"]]
+ 00584d04 ["INT_ADD", "register:40f0:8", ["const:584d04:8", "const:4:8"]]
+ 00584d04 ["CALL", null, ["callee:00597608:8"]]
- 00584cc4 bytes 414a0094
+ 00584d04 bytes 414a0094
- 00584ce4 ["INT_ADD", "register:40f0:8", ["const:584ce4:8", "const:4:8"]]
- 00584ce4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00584d24 ["INT_ADD", "register:40f0:8", ["const:584d24:8", "const:4:8"]]
+ 00584d24 ["CALL", null, ["callee:00c53d00:8"]]
- 00584ce4 bytes ff3a1b94
+ 00584d24 bytes f73b1b94
- 00584cf8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00584cf8 ["INT_ADD", "register:40f0:8", ["const:584cf8:8", "const:4:8"]]
- 00584cf8 ["CALLIND", null, ["register:0:8"]]
+ 00584d38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00584d38 ["INT_ADD", "register:40f0:8", ["const:584d38:8", "const:4:8"]]
+ 00584d38 ["CALLIND", null, ["register:0:8"]]
- 00584cf8 bytes 00013fd6
+ 00584d38 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-409552bee23f9d2b55a97c4d38b4129d"></a>

### [`00584d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584d5c.md) → [`00584d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584d9c.md) FUN_00584d9c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0058ad2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058ad2c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0058ad6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058ad6c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00584da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584d5c.md#insn-00584da0) · [`00584db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584d5c.md#insn-00584db8) · [`00584dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584d5c.md#insn-00584dc8)
- 新版 [`00584de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584d9c.md#insn-00584de0) · [`00584df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584d9c.md#insn-00584df8) · [`00584e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584d9c.md#insn-00584e08)

~~~diff
- 00584da0 ["INT_ADD", "register:40f0:8", ["const:584da0:8", "const:4:8"]]
- 00584da0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00584de0 ["INT_ADD", "register:40f0:8", ["const:584de0:8", "const:4:8"]]
+ 00584de0 ["CALL", null, ["callee:00c57e90:8"]]
- 00584da0 bytes 3c4b1b94
+ 00584de0 bytes 2c4c1b94
- 00584db8 ["INT_ADD", "register:40f0:8", ["const:584db8:8", "const:4:8"]]
- 00584db8 ["CALL", null, ["callee:00c58000:8"]]
+ 00584df8 ["INT_ADD", "register:40f0:8", ["const:584df8:8", "const:4:8"]]
+ 00584df8 ["CALL", null, ["callee:00c58000:8"]]
- 00584db8 bytes 924b1b94
+ 00584df8 bytes 824c1b94
- 00584dc8 ["INT_ADD", "register:40f0:8", ["const:584dc8:8", "const:4:8"]]
- 00584dc8 ["CALL", null, ["callee:0058ad6c:8"]]
+ 00584e08 ["INT_ADD", "register:40f0:8", ["const:584e08:8", "const:4:8"]]
+ 00584e08 ["CALL", null, ["callee:0058ad6c:8"]]
- 00584dc8 bytes d9170094
+ 00584e08 bytes d9170094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecfcbcd70b1f8c6c9de0ce5a1dbc90ad"></a>

### [`00584ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584ec0.md) → [`00584f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584f00.md) FUN_00584f00

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00547b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b70.md) [`00549094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549094.md) [`005642a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/005642a0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00547bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547bb0.md) [`005490d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/005490d4.md) [`005642e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005642e0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00584ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584ec0.md#insn-00584ef4) · [`00584f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584ec0.md#insn-00584f10) · [`00584f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584ec0.md#insn-00584f44)
- 新版 [`00584f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584f00.md#insn-00584f34) · [`00584f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584f00.md#insn-00584f50) · [`00584f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584f00.md#insn-00584f84)

~~~diff
- 00584ef4 ["INT_ADD", "register:40f0:8", ["const:584ef4:8", "const:4:8"]]
- 00584ef4 ["CALL", null, ["callee:00547bb0:8"]]
+ 00584f34 ["INT_ADD", "register:40f0:8", ["const:584f34:8", "const:4:8"]]
+ 00584f34 ["CALL", null, ["callee:00547bb0:8"]]
- 00584ef4 bytes 1f0bff97
+ 00584f34 bytes 1f0bff97
- 00584f10 ["INT_ADD", "register:40f0:8", ["const:584f10:8", "const:4:8"]]
- 00584f10 ["CALL", null, ["callee:005642e0:8"]]
+ 00584f50 ["INT_ADD", "register:40f0:8", ["const:584f50:8", "const:4:8"]]
+ 00584f50 ["CALL", null, ["callee:005642e0:8"]]
- 00584f10 bytes e47cff97
+ 00584f50 bytes e47cff97
- 00584f44 ["INT_ADD", "register:40f0:8", ["const:584f44:8", "const:4:8"]]
- 00584f44 ["CALL", null, ["callee:0043bb20:8"]]
+ 00584f84 ["INT_ADD", "register:40f0:8", ["const:584f84:8", "const:4:8"]]
+ 00584f84 ["CALL", null, ["callee:0043bb20:8"]]
- 00584f44 bytes e7dafa97
+ 00584f84 bytes e7dafa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

