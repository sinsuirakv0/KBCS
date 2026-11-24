# v16.0.0 → v16.0.1 · 要調査の変更候補 (3)

[一覧の目次](README.md)

<a id="compare-eb9ce03ecd19b40e52e48d98b37dc267"></a>

### [`00470124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470124.md) → [`00470164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470164.md) FUN_00470164

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470314.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 1件 [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470354.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004701cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470124.md#insn-004701cc) · [`0047020c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470124.md#insn-0047020c) · [`00470250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470124.md#insn-00470250)
- 新版 [`0047020c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470164.md#insn-0047020c) · [`0047024c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470164.md#insn-0047024c) · [`00470290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470164.md#insn-00470290)

~~~diff
- 004701cc ["INT_ADD", "register:40f0:8", ["const:4701cc:8", "const:4:8"]]
- 004701cc ["CALL", null, ["callee:00c57e90:8"]]
+ 0047020c ["INT_ADD", "register:40f0:8", ["const:47020c:8", "const:4:8"]]
+ 0047020c ["CALL", null, ["callee:00c57e90:8"]]
- 004701cc bytes 319e1f94
+ 0047020c bytes 219f1f94
- 0047020c ["INT_ADD", "register:40f0:8", ["const:47020c:8", "const:4:8"]]
- 0047020c ["CALL", null, ["callee:00c58090:8"]]
+ 0047024c ["INT_ADD", "register:40f0:8", ["const:47024c:8", "const:4:8"]]
+ 0047024c ["CALL", null, ["callee:00c58090:8"]]
- 0047020c bytes a19e1f94
+ 0047024c bytes 919f1f94
- 00470250 ["INT_ADD", "register:40f0:8", ["const:470250:8", "const:4:8"]]
- 00470250 ["CALL", null, ["callee:00c58090:8"]]
+ 00470290 ["INT_ADD", "register:40f0:8", ["const:470290:8", "const:4:8"]]
+ 00470290 ["CALL", null, ["callee:00c58090:8"]]
- 00470250 bytes 909e1f94
+ 00470290 bytes 809f1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3c7fc84920a0680e20af158d22ea315"></a>

### [`00470328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470328.md) → [`00470368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470368.md) FUN_00470368

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470454.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470494.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004703a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470328.md#insn-004703a0) · [`004703c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470328.md#insn-004703c4) · [`004703f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470328.md#insn-004703f0)
- 新版 [`004703e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470368.md#insn-004703e0) · [`00470404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470368.md#insn-00470404) · [`00470430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470368.md#insn-00470430)

~~~diff
- 004703a0 ["INT_ADD", "register:40f0:8", ["const:4703a0:8", "const:4:8"]]
- 004703a0 ["CALL", null, ["callee:00c57e90:8"]]
+ 004703e0 ["INT_ADD", "register:40f0:8", ["const:4703e0:8", "const:4:8"]]
+ 004703e0 ["CALL", null, ["callee:00c57e90:8"]]
- 004703a0 bytes bc9d1f94
+ 004703e0 bytes ac9e1f94
- 004703c4 ["INT_ADD", "register:40f0:8", ["const:4703c4:8", "const:4:8"]]
- 004703c4 ["CALL", null, ["callee:00c58090:8"]]
+ 00470404 ["INT_ADD", "register:40f0:8", ["const:470404:8", "const:4:8"]]
+ 00470404 ["CALL", null, ["callee:00c58090:8"]]
- 004703c4 bytes 339e1f94
+ 00470404 bytes 239f1f94
- 004703f0 ["INT_ADD", "register:40f0:8", ["const:4703f0:8", "const:4:8"]]
- 004703f0 ["CALL", null, ["callee:00c58090:8"]]
+ 00470430 ["INT_ADD", "register:40f0:8", ["const:470430:8", "const:4:8"]]
+ 00470430 ["CALL", null, ["callee:00c58090:8"]]
- 004703f0 bytes 289e1f94
+ 00470430 bytes 189f1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eba0601a7ebffcd016e033135d0eaadc"></a>

### [`004706d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004706d4.md) → [`00470714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470714.md) FUN_00470714

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0046f074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md) [`0047aed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047aed0.md) [`009e3d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e3d0c.md) [`00a3539c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a3539c.md) [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 5件 [`0046f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md) [`0047af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047af10.md) [`009e3ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e3ea8.md) [`00a35594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a35594.md) [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047074c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004706d4.md#insn-0047074c) · [`00470770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004706d4.md#insn-00470770) · [`0047079c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004706d4.md#insn-0047079c)
- 新版 [`0047078c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470714.md#insn-0047078c) · [`004707b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470714.md#insn-004707b0) · [`004707dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470714.md#insn-004707dc)

~~~diff
- 0047074c ["INT_ADD", "register:40f0:8", ["const:47074c:8", "const:4:8"]]
- 0047074c ["CALL", null, ["callee:00c57e90:8"]]
+ 0047078c ["INT_ADD", "register:40f0:8", ["const:47078c:8", "const:4:8"]]
+ 0047078c ["CALL", null, ["callee:00c57e90:8"]]
- 0047074c bytes d19c1f94
+ 0047078c bytes c19d1f94
- 00470770 ["INT_ADD", "register:40f0:8", ["const:470770:8", "const:4:8"]]
- 00470770 ["CALL", null, ["callee:00c58090:8"]]
+ 004707b0 ["INT_ADD", "register:40f0:8", ["const:4707b0:8", "const:4:8"]]
+ 004707b0 ["CALL", null, ["callee:00c58090:8"]]
- 00470770 bytes 489d1f94
+ 004707b0 bytes 389e1f94
- 0047079c ["INT_ADD", "register:40f0:8", ["const:47079c:8", "const:4:8"]]
- 0047079c ["CALL", null, ["callee:00c58090:8"]]
+ 004707dc ["INT_ADD", "register:40f0:8", ["const:4707dc:8", "const:4:8"]]
+ 004707dc ["CALL", null, ["callee:00c58090:8"]]
- 0047079c bytes 3d9d1f94
+ 004707dc bytes 2d9e1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-541c4e395e41d9e505d3103ff2665747"></a>

### [`00470814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470814.md) → [`00470854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470854.md) FUN_00470854

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0046f074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470940.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`0046f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470980.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047088c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470814.md#insn-0047088c) · [`004708b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470814.md#insn-004708b0) · [`004708dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470814.md#insn-004708dc)
- 新版 [`004708cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470854.md#insn-004708cc) · [`004708f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470854.md#insn-004708f0) · [`0047091c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470854.md#insn-0047091c)

~~~diff
- 0047088c ["INT_ADD", "register:40f0:8", ["const:47088c:8", "const:4:8"]]
- 0047088c ["CALL", null, ["callee:00c57e90:8"]]
+ 004708cc ["INT_ADD", "register:40f0:8", ["const:4708cc:8", "const:4:8"]]
+ 004708cc ["CALL", null, ["callee:00c57e90:8"]]
- 0047088c bytes 819c1f94
+ 004708cc bytes 719d1f94
- 004708b0 ["INT_ADD", "register:40f0:8", ["const:4708b0:8", "const:4:8"]]
- 004708b0 ["CALL", null, ["callee:00c58090:8"]]
+ 004708f0 ["INT_ADD", "register:40f0:8", ["const:4708f0:8", "const:4:8"]]
+ 004708f0 ["CALL", null, ["callee:00c58090:8"]]
- 004708b0 bytes f89c1f94
+ 004708f0 bytes e89d1f94
- 004708dc ["INT_ADD", "register:40f0:8", ["const:4708dc:8", "const:4:8"]]
- 004708dc ["CALL", null, ["callee:00c58090:8"]]
+ 0047091c ["INT_ADD", "register:40f0:8", ["const:47091c:8", "const:4:8"]]
+ 0047091c ["CALL", null, ["callee:00c58090:8"]]
- 004708dc bytes ed9c1f94
+ 0047091c bytes dd9d1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9f85b09bcefb4676af62e60b89a7b31"></a>

### [`00470954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470954.md) → [`00470994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470994.md) FUN_00470994

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 19件 [`0046f71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f71c.md) [`006416ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/006416ac.md) [`006847bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/006847bc.md) [`0068adf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068a/0068adf0.md) [`0068c5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068c/0068c5d0.md) · 呼出先 5件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 19件 [`0046f75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f75c.md) [`006416ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/006416ec.md) [`006847fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00684/006847fc.md) [`0068ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068ae30.md) [`0068c610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068c/0068c610.md) · 呼出先 5件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00470998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470954.md#insn-00470998) · [`004709e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470954.md#insn-004709e0) · [`00470a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470954.md#insn-00470a08)
- 新版 [`004709d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470994.md#insn-004709d8) · [`00470a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470994.md#insn-00470a20) · [`00470a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470994.md#insn-00470a48)

~~~diff
- 00470998 ["INT_ADD", "register:40f0:8", ["const:470998:8", "const:4:8"]]
- 00470998 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004709d8 ["INT_ADD", "register:40f0:8", ["const:4709d8:8", "const:4:8"]]
+ 004709d8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00470998 bytes 469c1f94
+ 004709d8 bytes 369d1f94
- 004709e0 ["INT_ADD", "register:40f0:8", ["const:4709e0:8", "const:4:8"]]
- 004709e0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00470a20 ["INT_ADD", "register:40f0:8", ["const:470a20:8", "const:4:8"]]
+ 00470a20 ["CALL", null, ["callee:00c57e90:8"]]
- 004709e0 bytes 2c9c1f94
+ 00470a20 bytes 1c9d1f94
- 00470a08 ["INT_ADD", "register:40f0:8", ["const:470a08:8", "const:4:8"]]
- 00470a08 ["CALL", null, ["callee:00c58000:8"]]
+ 00470a48 ["INT_ADD", "register:40f0:8", ["const:470a48:8", "const:4:8"]]
+ 00470a48 ["CALL", null, ["callee:00c58000:8"]]
- 00470a08 bytes 7e9c1f94
+ 00470a48 bytes 6e9d1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdd2b60c43d1c0abf808c73726dd4f2b"></a>

### [`00470eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470eb0.md) → [`00470ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470ef0.md) FUN_00470ef0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00470e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470e14.md) · 呼出先 3件 [`00471bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471bf0.md) [`00471c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471c7c.md) [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md)
- 新版 呼出元 1件 [`00470e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470e54.md) · 呼出先 3件 [`00471c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471c30.md) [`00471cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471cbc.md) [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00470ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470eb0.md#insn-00470ec4) · [`00470ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470eb0.md#insn-00470ed0) · [`00470edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470eb0.md#insn-00470edc)
- 新版 [`00470f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470ef0.md#insn-00470f04) · [`00470f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470ef0.md#insn-00470f10) · [`00470f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470ef0.md#insn-00470f1c)

~~~diff
- 00470ec4 ["INT_ADD", "register:40f0:8", ["const:470ec4:8", "const:4:8"]]
- 00470ec4 ["CALL", null, ["callee:00c57e60:8"]]
+ 00470f04 ["INT_ADD", "register:40f0:8", ["const:470f04:8", "const:4:8"]]
+ 00470f04 ["CALL", null, ["callee:00c57e60:8"]]
- 00470ec4 bytes e79a1f94
+ 00470f04 bytes d79b1f94
- 00470ed0 ["INT_ADD", "register:40f0:8", ["const:470ed0:8", "const:4:8"]]
- 00470ed0 ["CALL", null, ["callee:00471c30:8"]]
+ 00470f10 ["INT_ADD", "register:40f0:8", ["const:470f10:8", "const:4:8"]]
+ 00470f10 ["CALL", null, ["callee:00471c30:8"]]
- 00470ed0 bytes 48030094
+ 00470f10 bytes 48030094
- 00470edc ["INT_ADD", "register:40f0:8", ["const:470edc:8", "const:4:8"]]
- 00470edc ["CALL", null, ["callee:00471c30:8"]]
+ 00470f1c ["INT_ADD", "register:40f0:8", ["const:470f1c:8", "const:4:8"]]
+ 00470f1c ["CALL", null, ["callee:00471c30:8"]]
- 00470edc bytes 45030094
+ 00470f1c bytes 45030094
~~~


<a id="compare-6a7da0a8fb1a8e7e2c0f2e75c66c1b7e"></a>

### [`00471694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471694.md) → [`004716d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/004716d4.md) FUN_004716d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004716b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471694.md#insn-004716b0) · [`004716d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471694.md#insn-004716d0)
- 新版 [`004716f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/004716d4.md#insn-004716f0) · [`00471710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/004716d4.md#insn-00471710)

~~~diff
- 004716b0 ["INT_ADD", "register:40f0:8", ["const:4716b0:8", "const:4:8"]]
- 004716b0 ["CALL", null, ["callee:00c53d00:8"]]
+ 004716f0 ["INT_ADD", "register:40f0:8", ["const:4716f0:8", "const:4:8"]]
+ 004716f0 ["CALL", null, ["callee:00c53d00:8"]]
- 004716b0 bytes 8c881f94
+ 004716f0 bytes 84891f94
- 004716d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004716d0 ["INT_ADD", "register:40f0:8", ["const:4716d0:8", "const:4:8"]]
- 004716d0 ["CALLIND", null, ["register:0:8"]]
+ 00471710 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00471710 ["INT_ADD", "register:40f0:8", ["const:471710:8", "const:4:8"]]
+ 00471710 ["CALLIND", null, ["register:0:8"]]
- 004716d0 bytes 00013fd6
+ 00471710 bytes 00013fd6
~~~


<a id="compare-0d37b7653821e65404e9f88906bfc266"></a>

### [`00471bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471bc4.md) → [`00471c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471c04.md) FUN_00471c04

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00926414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00926/00926414.md) · 呼出先 1件 [`0047252c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/0047252c.md)
- 新版 呼出元 1件 [`009265b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00926/009265b0.md) · 呼出先 1件 [`0047256c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/0047256c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00471bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471bc4.md#insn-00471bd4)
- 新版 [`00471c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471c04.md#insn-00471c14)

~~~diff
- 00471bd4 ["INT_ADD", "register:40f0:8", ["const:471bd4:8", "const:4:8"]]
- 00471bd4 ["CALL", null, ["callee:0047256c:8"]]
+ 00471c14 ["INT_ADD", "register:40f0:8", ["const:471c14:8", "const:4:8"]]
+ 00471c14 ["CALL", null, ["callee:0047256c:8"]]
- 00471bd4 bytes 56020094
+ 00471c14 bytes 56020094
~~~


<a id="compare-e9cc37d2a49750cf85d0534899c91eae"></a>

### [`00471bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471bf0.md) → [`00471c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471c30.md) FUN_00471c30

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00470eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470eb0.md) [`00471bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471bf0.md) · 呼出先 4件 [`00471bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471bf0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00470ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470ef0.md) [`00471c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471c30.md) · 呼出先 4件 [`00471c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471c30.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00471c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471bf0.md#insn-00471c0c) · [`00471c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471bf0.md#insn-00471c18) · [`00471c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471bf0.md#insn-00471c2c)
- 新版 [`00471c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471c30.md#insn-00471c4c) · [`00471c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471c30.md#insn-00471c58) · [`00471c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471c30.md#insn-00471c6c)

~~~diff
- 00471c0c ["INT_ADD", "register:40f0:8", ["const:471c0c:8", "const:4:8"]]
- 00471c0c ["CALL", null, ["local:b0:8"]]
+ 00471c4c ["INT_ADD", "register:40f0:8", ["const:471c4c:8", "const:4:8"]]
+ 00471c4c ["CALL", null, ["local:b0:8"]]
- 00471c0c bytes f9ffff97
+ 00471c4c bytes f9ffff97
- 00471c18 ["INT_ADD", "register:40f0:8", ["const:471c18:8", "const:4:8"]]
- 00471c18 ["CALL", null, ["local:b0:8"]]
+ 00471c58 ["INT_ADD", "register:40f0:8", ["const:471c58:8", "const:4:8"]]
+ 00471c58 ["CALL", null, ["local:b0:8"]]
- 00471c18 bytes f6ffff97
+ 00471c58 bytes f6ffff97
- 00471c2c ["INT_ADD", "register:40f0:8", ["const:471c2c:8", "const:4:8"]]
- 00471c2c ["CALL", null, ["callee:00c53d00:8"]]
+ 00471c6c ["INT_ADD", "register:40f0:8", ["const:471c6c:8", "const:4:8"]]
+ 00471c6c ["CALL", null, ["callee:00c53d00:8"]]
- 00471c2c bytes 2d871f94
+ 00471c6c bytes 25881f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b8ab3bb0c4b67931dcff57be28bf32b"></a>

### [`00471c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471c7c.md) → [`00471cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471cbc.md) FUN_00471cbc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00470eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470eb0.md) [`00471c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471c7c.md) · 呼出先 2件 [`00471c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471c7c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00470ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470ef0.md) [`00471cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471cbc.md) · 呼出先 2件 [`00471cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471cbc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00471c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471c7c.md#insn-00471c98) · [`00471ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471c7c.md#insn-00471ca4) · [`00471cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471c7c.md#insn-00471cb4)
- 新版 [`00471cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471cbc.md#insn-00471cd8) · [`00471ce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471cbc.md#insn-00471ce4) · [`00471cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471cbc.md#insn-00471cf4)

~~~diff
- 00471c98 ["INT_ADD", "register:40f0:8", ["const:471c98:8", "const:4:8"]]
- 00471c98 ["CALL", null, ["local:b0:8"]]
+ 00471cd8 ["INT_ADD", "register:40f0:8", ["const:471cd8:8", "const:4:8"]]
+ 00471cd8 ["CALL", null, ["local:b0:8"]]
- 00471c98 bytes f9ffff97
+ 00471cd8 bytes f9ffff97
- 00471ca4 ["INT_ADD", "register:40f0:8", ["const:471ca4:8", "const:4:8"]]
- 00471ca4 ["CALL", null, ["local:b0:8"]]
+ 00471ce4 ["INT_ADD", "register:40f0:8", ["const:471ce4:8", "const:4:8"]]
+ 00471ce4 ["CALL", null, ["local:b0:8"]]
- 00471ca4 bytes f6ffff97
+ 00471ce4 bytes f6ffff97
- 00471cb4 ["INT_ADD", "register:40f0:8", ["const:471cb4:8", "const:4:8"]]
- 00471cb4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00471cf4 ["INT_ADD", "register:40f0:8", ["const:471cf4:8", "const:4:8"]]
+ 00471cf4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00471cb4 bytes 7f971f94
+ 00471cf4 bytes 6f981f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fa18a317dfa63c35e758a5edfc76cb8"></a>

### [`00471cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471cdc.md) → [`00471d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471d1c.md) FUN_00471d1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00470ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00471e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471e14.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00471e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471e54.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00471d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471cdc.md#insn-00471d10) · [`00471d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471cdc.md#insn-00471d30) · [`00471d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471cdc.md#insn-00471d6c)
- 新版 [`00471d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471d1c.md#insn-00471d50) · [`00471d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471d1c.md#insn-00471d70) · [`00471dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471d1c.md#insn-00471dac)

~~~diff
- 00471d10 ["INT_ADD", "register:40f0:8", ["const:471d10:8", "const:4:8"]]
- 00471d10 ["CALL", null, ["callee:00471e54:8"]]
+ 00471d50 ["INT_ADD", "register:40f0:8", ["const:471d50:8", "const:4:8"]]
+ 00471d50 ["CALL", null, ["callee:00471e54:8"]]
- 00471d10 bytes 41000094
+ 00471d50 bytes 41000094
- 00471d30 ["INT_ADD", "register:40f0:8", ["const:471d30:8", "const:4:8"]]
- 00471d30 ["CALL", null, ["callee:00c57e90:8"]]
+ 00471d70 ["INT_ADD", "register:40f0:8", ["const:471d70:8", "const:4:8"]]
+ 00471d70 ["CALL", null, ["callee:00c57e90:8"]]
- 00471d30 bytes 58971f94
+ 00471d70 bytes 48981f94
- 00471d6c ["INT_ADD", "register:40f0:8", ["const:471d6c:8", "const:4:8"]]
- 00471d6c ["CALL", null, ["callee:0043bb20:8"]]
+ 00471dac ["INT_ADD", "register:40f0:8", ["const:471dac:8", "const:4:8"]]
+ 00471dac ["CALL", null, ["callee:0043bb20:8"]]
- 00471d6c bytes 5d27ff97
+ 00471dac bytes 5d27ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccab1ce0045257682d72c93948924ff5"></a>

### [`00471e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471e14.md) → [`00471e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471e54.md) FUN_00471e54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00471cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471cdc.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00471d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471d1c.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00471e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471e14.md#insn-00471e98) · [`00471ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471e14.md#insn-00471ec4)
- 新版 [`00471ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471e54.md#insn-00471ed8) · [`00471f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471e54.md#insn-00471f04)

~~~diff
- 00471e98 ["INT_ADD", "register:40f0:8", ["const:471e98:8", "const:4:8"]]
- 00471e98 ["CALL", null, ["callee:00c58050:8"]]
+ 00471ed8 ["INT_ADD", "register:40f0:8", ["const:471ed8:8", "const:4:8"]]
+ 00471ed8 ["CALL", null, ["callee:00c58050:8"]]
- 00471e98 bytes 6e971f94
+ 00471ed8 bytes 5e981f94
- 00471ec4 ["INT_ADD", "register:40f0:8", ["const:471ec4:8", "const:4:8"]]
- 00471ec4 ["CALL", null, ["callee:00c58050:8"]]
+ 00471f04 ["INT_ADD", "register:40f0:8", ["const:471f04:8", "const:4:8"]]
+ 00471f04 ["CALL", null, ["callee:00c58050:8"]]
- 00471ec4 bytes 63971f94
+ 00471f04 bytes 53981f94
~~~


<a id="compare-9d0658772262dbd85c55d2da0bdcd365"></a>

### [`00471f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471f18.md) → [`00471f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471f58.md) FUN_00471f58

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00471f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471f18.md#insn-00471f44) · [`00471f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471f18.md#insn-00471f54)
- 新版 [`00471f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471f58.md#insn-00471f84) · [`00471f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471f58.md#insn-00471f94)

~~~diff
- 00471f44 ["INT_ADD", "register:40f0:8", ["const:471f44:8", "const:4:8"]]
- 00471f44 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00471f84 ["INT_ADD", "register:40f0:8", ["const:471f84:8", "const:4:8"]]
+ 00471f84 ["CALL", null, ["callee:00c57eb0:8"]]
- 00471f44 bytes db961f94
+ 00471f84 bytes cb971f94
- 00471f54 ["INT_ADD", "register:40f0:8", ["const:471f54:8", "const:4:8"]]
- 00471f54 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00471f94 ["INT_ADD", "register:40f0:8", ["const:471f94:8", "const:4:8"]]
+ 00471f94 ["CALL", null, ["callee:00c57eb0:8"]]
- 00471f54 bytes d7961f94
+ 00471f94 bytes c7971f94
~~~


<a id="compare-9ee3f007b433ad00661be78b55e9bf40"></a>

### [`00471f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471f74.md) → [`00471fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471fb4.md) FUN_00471fb4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00470ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md) [`004718f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004718f0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 2件 [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) [`00471930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471930.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00471fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471f74.md#insn-00471fe0) · [`0047203c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471f74.md#insn-0047203c)
- 新版 [`00472020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471fb4.md#insn-00472020) · [`0047207c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471fb4.md#insn-0047207c)

~~~diff
- 00471fe0 ["INT_ADD", "register:40f0:8", ["const:471fe0:8", "const:4:8"]]
- 00471fe0 ["CALL", null, ["callee:00c58050:8"]]
+ 00472020 ["INT_ADD", "register:40f0:8", ["const:472020:8", "const:4:8"]]
+ 00472020 ["CALL", null, ["callee:00c58050:8"]]
- 00471fe0 bytes 1c971f94
+ 00472020 bytes 0c981f94
- 0047203c ["INT_ADD", "register:40f0:8", ["const:47203c:8", "const:4:8"]]
- 0047203c ["CALL", null, ["callee:00c58050:8"]]
+ 0047207c ["INT_ADD", "register:40f0:8", ["const:47207c:8", "const:4:8"]]
+ 0047207c ["CALL", null, ["callee:00c58050:8"]]
- 0047203c bytes 05971f94
+ 0047207c bytes f5971f94
~~~


<a id="compare-f6573eb12079c64b04e8e78c7e3b8266"></a>

### [`00472078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472078.md) → [`004720b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004720b8.md) FUN_004720b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00470ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md) [`004718f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004718f0.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004721a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/004721a4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) [`00471930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471930.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`004721e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004721e4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004720ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472078.md#insn-004720ac) · [`004720cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472078.md#insn-004720cc) · [`00472108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472078.md#insn-00472108)
- 新版 [`004720ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004720b8.md#insn-004720ec) · [`0047210c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004720b8.md#insn-0047210c) · [`00472148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004720b8.md#insn-00472148)

~~~diff
- 004720ac ["INT_ADD", "register:40f0:8", ["const:4720ac:8", "const:4:8"]]
- 004720ac ["CALL", null, ["callee:004721e4:8"]]
+ 004720ec ["INT_ADD", "register:40f0:8", ["const:4720ec:8", "const:4:8"]]
+ 004720ec ["CALL", null, ["callee:004721e4:8"]]
- 004720ac bytes 3e000094
+ 004720ec bytes 3e000094
- 004720cc ["INT_ADD", "register:40f0:8", ["const:4720cc:8", "const:4:8"]]
- 004720cc ["CALL", null, ["callee:00c57e90:8"]]
+ 0047210c ["INT_ADD", "register:40f0:8", ["const:47210c:8", "const:4:8"]]
+ 0047210c ["CALL", null, ["callee:00c57e90:8"]]
- 004720cc bytes 71961f94
+ 0047210c bytes 61971f94
- 00472108 ["INT_ADD", "register:40f0:8", ["const:472108:8", "const:4:8"]]
- 00472108 ["CALL", null, ["callee:0043bb20:8"]]
+ 00472148 ["INT_ADD", "register:40f0:8", ["const:472148:8", "const:4:8"]]
+ 00472148 ["CALL", null, ["callee:0043bb20:8"]]
- 00472108 bytes 7626ff97
+ 00472148 bytes 7626ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c233cca3d9ab5b65f775a5642f966cd4"></a>

### [`004721a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/004721a4.md) → [`004721e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004721e4.md) FUN_004721e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00472078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472078.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`004720b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004720b8.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/004721a4.md#insn-00472228) · [`00472254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/004721a4.md#insn-00472254)
- 新版 [`00472268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004721e4.md#insn-00472268) · [`00472294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004721e4.md#insn-00472294)

~~~diff
- 00472228 ["INT_ADD", "register:40f0:8", ["const:472228:8", "const:4:8"]]
- 00472228 ["CALL", null, ["callee:00c58050:8"]]
+ 00472268 ["INT_ADD", "register:40f0:8", ["const:472268:8", "const:4:8"]]
+ 00472268 ["CALL", null, ["callee:00c58050:8"]]
- 00472228 bytes 8a961f94
+ 00472268 bytes 7a971f94
- 00472254 ["INT_ADD", "register:40f0:8", ["const:472254:8", "const:4:8"]]
- 00472254 ["CALL", null, ["callee:00c58050:8"]]
+ 00472294 ["INT_ADD", "register:40f0:8", ["const:472294:8", "const:4:8"]]
+ 00472294 ["CALL", null, ["callee:00c58050:8"]]
- 00472254 bytes 7f961f94
+ 00472294 bytes 6f971f94
~~~


<a id="compare-9a1fc45c8d49fded183ae182aaace22f"></a>

### [`004722a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/004722a8.md) → [`004722e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004722e8.md) FUN_004722e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004722d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/004722a8.md#insn-004722d8) · [`004722ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/004722a8.md#insn-004722ec) · [`004722f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/004722a8.md#insn-004722f4)
- 新版 [`00472318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004722e8.md#insn-00472318) · [`0047232c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004722e8.md#insn-0047232c) · [`00472334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004722e8.md#insn-00472334)

~~~diff
- 004722d8 ["INT_ADD", "register:40f0:8", ["const:4722d8:8", "const:4:8"]]
- 004722d8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00472318 ["INT_ADD", "register:40f0:8", ["const:472318:8", "const:4:8"]]
+ 00472318 ["CALL", null, ["callee:00c53d00:8"]]
- 004722d8 bytes 82851f94
+ 00472318 bytes 7a861f94
- 004722ec ["COPY", "register:0:8", ["register:4040:8"]]
- 004722ec ["INT_ADD", "register:40f0:8", ["const:4722ec:8", "const:4:8"]]
- 004722ec ["CALLIND", null, ["register:0:8"]]
+ 0047232c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047232c ["INT_ADD", "register:40f0:8", ["const:47232c:8", "const:4:8"]]
+ 0047232c ["CALLIND", null, ["register:0:8"]]
- 004722ec bytes 00013fd6
+ 0047232c bytes 00013fd6
- 004722f4 ["INT_ADD", "register:40f0:8", ["const:4722f4:8", "const:4:8"]]
- 004722f4 ["CALL", null, ["callee:00c57e80:8"]]
+ 00472334 ["INT_ADD", "register:40f0:8", ["const:472334:8", "const:4:8"]]
+ 00472334 ["CALL", null, ["callee:00c57e80:8"]]
- 004722f4 bytes e3951f94
+ 00472334 bytes d3961f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-808b5861af142bffdaf641154ffec95f"></a>

### [`00472324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472324.md) → [`00472364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472364.md) FUN_00472364

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004716e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004716e4.md) [`004718f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004718f0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 2件 [`00471724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471724.md) [`00471930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471930.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472324.md#insn-00472390) · [`004723ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472324.md#insn-004723ec)
- 新版 [`004723d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472364.md#insn-004723d0) · [`0047242c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472364.md#insn-0047242c)

~~~diff
- 00472390 ["INT_ADD", "register:40f0:8", ["const:472390:8", "const:4:8"]]
- 00472390 ["CALL", null, ["callee:00c58050:8"]]
+ 004723d0 ["INT_ADD", "register:40f0:8", ["const:4723d0:8", "const:4:8"]]
+ 004723d0 ["CALL", null, ["callee:00c58050:8"]]
- 00472390 bytes 30961f94
+ 004723d0 bytes 20971f94
- 004723ec ["INT_ADD", "register:40f0:8", ["const:4723ec:8", "const:4:8"]]
- 004723ec ["CALL", null, ["callee:00c58050:8"]]
+ 0047242c ["INT_ADD", "register:40f0:8", ["const:47242c:8", "const:4:8"]]
+ 0047242c ["CALL", null, ["callee:00c58050:8"]]
- 004723ec bytes 19961f94
+ 0047242c bytes 09971f94
~~~


<a id="compare-3f6dca10af84cf260fca74cd77ccad5d"></a>

### [`00472428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472428.md) → [`00472468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472468.md) FUN_00472468

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004716e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004716e4.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00471724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471724.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472428.md#insn-00472494) · [`004724f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472428.md#insn-004724f0)
- 新版 [`004724d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472468.md#insn-004724d4) · [`00472530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472468.md#insn-00472530)

~~~diff
- 00472494 ["INT_ADD", "register:40f0:8", ["const:472494:8", "const:4:8"]]
- 00472494 ["CALL", null, ["callee:00c58050:8"]]
+ 004724d4 ["INT_ADD", "register:40f0:8", ["const:4724d4:8", "const:4:8"]]
+ 004724d4 ["CALL", null, ["callee:00c58050:8"]]
- 00472494 bytes ef951f94
+ 004724d4 bytes df961f94
- 004724f0 ["INT_ADD", "register:40f0:8", ["const:4724f0:8", "const:4:8"]]
- 004724f0 ["CALL", null, ["callee:00c58050:8"]]
+ 00472530 ["INT_ADD", "register:40f0:8", ["const:472530:8", "const:4:8"]]
+ 00472530 ["CALL", null, ["callee:00c58050:8"]]
- 004724f0 bytes d8951f94
+ 00472530 bytes c8961f94
~~~


<a id="compare-6ecd09b37ebeddfd09139cc890c636a5"></a>

### [`0047252c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/0047252c.md) → [`0047256c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/0047256c.md) FUN_0047256c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00471bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471bc4.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00471c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471c04.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/0047252c.md#insn-00472598) · [`004725f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/0047252c.md#insn-004725f4)
- 新版 [`004725d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/0047256c.md#insn-004725d8) · [`00472634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/0047256c.md#insn-00472634)

~~~diff
- 00472598 ["INT_ADD", "register:40f0:8", ["const:472598:8", "const:4:8"]]
- 00472598 ["CALL", null, ["callee:00c58050:8"]]
+ 004725d8 ["INT_ADD", "register:40f0:8", ["const:4725d8:8", "const:4:8"]]
+ 004725d8 ["CALL", null, ["callee:00c58050:8"]]
- 00472598 bytes ae951f94
+ 004725d8 bytes 9e961f94
- 004725f4 ["INT_ADD", "register:40f0:8", ["const:4725f4:8", "const:4:8"]]
- 004725f4 ["CALL", null, ["callee:00c58050:8"]]
+ 00472634 ["INT_ADD", "register:40f0:8", ["const:472634:8", "const:4:8"]]
+ 00472634 ["CALL", null, ["callee:00c58050:8"]]
- 004725f4 bytes 97951f94
+ 00472634 bytes 87961f94
~~~


<a id="compare-4ca489085b1c14fe59f53ecc162c44f6"></a>

### [`004729cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/004729cc.md) → [`00472a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472a0c.md) FUN_00472a0c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/004729cc.md#insn-00472a1c) · [`00472a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/004729cc.md#insn-00472a30) · [`00472a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/004729cc.md#insn-00472a38)
- 新版 [`00472a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472a0c.md#insn-00472a5c) · [`00472a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472a0c.md#insn-00472a70) · [`00472a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472a0c.md#insn-00472a78)

~~~diff
- 00472a1c ["INT_ADD", "register:40f0:8", ["const:472a1c:8", "const:4:8"]]
- 00472a1c ["CALL", null, ["callee:00c53d00:8"]]
+ 00472a5c ["INT_ADD", "register:40f0:8", ["const:472a5c:8", "const:4:8"]]
+ 00472a5c ["CALL", null, ["callee:00c53d00:8"]]
- 00472a1c bytes b1831f94
+ 00472a5c bytes a9841f94
- 00472a30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00472a30 ["INT_ADD", "register:40f0:8", ["const:472a30:8", "const:4:8"]]
- 00472a30 ["CALLIND", null, ["register:0:8"]]
+ 00472a70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00472a70 ["INT_ADD", "register:40f0:8", ["const:472a70:8", "const:4:8"]]
+ 00472a70 ["CALLIND", null, ["register:0:8"]]
- 00472a30 bytes 00013fd6
+ 00472a70 bytes 00013fd6
- 00472a38 ["INT_ADD", "register:40f0:8", ["const:472a38:8", "const:4:8"]]
- 00472a38 ["CALL", null, ["callee:00c57e80:8"]]
+ 00472a78 ["INT_ADD", "register:40f0:8", ["const:472a78:8", "const:4:8"]]
+ 00472a78 ["CALL", null, ["callee:00c57e80:8"]]
- 00472a38 bytes 12941f94
+ 00472a78 bytes 02951f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85d010098c98d9a551b5d6d03d570d19"></a>

### [`00472ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472ab8.md) → [`00472af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472af8.md) FUN_00472af8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0088c0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c0e0.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0088c120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c120.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472ab8.md#insn-00472b00) · [`00472b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472ab8.md#insn-00472b14) · [`00472b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472ab8.md#insn-00472b1c)
- 新版 [`00472b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472af8.md#insn-00472b40) · [`00472b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472af8.md#insn-00472b54) · [`00472b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472af8.md#insn-00472b5c)

~~~diff
- 00472b00 ["INT_ADD", "register:40f0:8", ["const:472b00:8", "const:4:8"]]
- 00472b00 ["CALL", null, ["callee:00c53d00:8"]]
+ 00472b40 ["INT_ADD", "register:40f0:8", ["const:472b40:8", "const:4:8"]]
+ 00472b40 ["CALL", null, ["callee:00c53d00:8"]]
- 00472b00 bytes 78831f94
+ 00472b40 bytes 70841f94
- 00472b14 ["COPY", "register:0:8", ["register:4040:8"]]
- 00472b14 ["INT_ADD", "register:40f0:8", ["const:472b14:8", "const:4:8"]]
- 00472b14 ["CALLIND", null, ["register:0:8"]]
+ 00472b54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00472b54 ["INT_ADD", "register:40f0:8", ["const:472b54:8", "const:4:8"]]
+ 00472b54 ["CALLIND", null, ["register:0:8"]]
- 00472b14 bytes 00013fd6
+ 00472b54 bytes 00013fd6
- 00472b1c ["INT_ADD", "register:40f0:8", ["const:472b1c:8", "const:4:8"]]
- 00472b1c ["CALL", null, ["callee:00c57e80:8"]]
+ 00472b5c ["INT_ADD", "register:40f0:8", ["const:472b5c:8", "const:4:8"]]
+ 00472b5c ["CALL", null, ["callee:00c57e80:8"]]
- 00472b1c bytes d9931f94
+ 00472b5c bytes c9941f94
~~~


<a id="compare-d1b2b0958a0076a96a4fa415e6bb998b"></a>

### [`00472b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472b7c.md) → [`00472bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472bbc.md) FUN_00472bbc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0088c0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c0e0.md) [`00893d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893d78.md) [`0089d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089d/0089d484.md) · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 3件 [`0088c120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c120.md) [`00893dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893dbc.md) [`0089d4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089d/0089d4c8.md) · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472b7c.md#insn-00472ba0)
- 新版 [`00472be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472bbc.md#insn-00472be0)

~~~diff
- 00472ba0 ["INT_ADD", "register:40f0:8", ["const:472ba0:8", "const:4:8"]]
- 00472ba0 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00472be0 ["INT_ADD", "register:40f0:8", ["const:472be0:8", "const:4:8"]]
+ 00472be0 ["CALL", null, ["callee:00c53cd0:8"]]
- 00472ba0 bytes 44831f94
+ 00472be0 bytes 3c841f94
~~~


<a id="compare-e4ffd52add7797c349f2a38b32458380"></a>

### [`00472bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472bac.md) → [`00472bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472bec.md) FUN_00472bec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 4件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 4件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472bac.md#insn-00472c00) · [`00472c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472bac.md#insn-00472c0c) · [`00472c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472bac.md#insn-00472c30)
- 新版 [`00472c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472bec.md#insn-00472c40) · [`00472c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472bec.md#insn-00472c4c) · [`00472c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472bec.md#insn-00472c70)

~~~diff
- 00472c00 ["INT_ADD", "register:40f0:8", ["const:472c00:8", "const:4:8"]]
- 00472c00 ["CALL", null, ["callee:00c58050:8"]]
+ 00472c40 ["INT_ADD", "register:40f0:8", ["const:472c40:8", "const:4:8"]]
+ 00472c40 ["CALL", null, ["callee:00c58050:8"]]
- 00472c00 bytes 14941f94
+ 00472c40 bytes 04951f94
- 00472c0c ["INT_ADD", "register:40f0:8", ["const:472c0c:8", "const:4:8"]]
- 00472c0c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00472c4c ["INT_ADD", "register:40f0:8", ["const:472c4c:8", "const:4:8"]]
+ 00472c4c ["CALL", null, ["callee:00c57eb0:8"]]
- 00472c0c bytes a9931f94
+ 00472c4c bytes 99941f94
- 00472c30 ["COPY", "register:0:8", ["register:4048:8"]]
- 00472c30 ["INT_ADD", "register:40f0:8", ["const:472c30:8", "const:4:8"]]
- 00472c30 ["CALLIND", null, ["register:0:8"]]
+ 00472c70 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00472c70 ["INT_ADD", "register:40f0:8", ["const:472c70:8", "const:4:8"]]
+ 00472c70 ["CALLIND", null, ["register:0:8"]]
- 00472c30 bytes 20013fd6
+ 00472c70 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f977ece27faead0eb2b1d2e283591a7"></a>

### [`00472ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472ef8.md) → [`00472f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472f38.md) FUN_00472f38

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472ef8.md#insn-00472f14) · [`00472f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472ef8.md#insn-00472f34)
- 新版 [`00472f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472f38.md#insn-00472f54) · [`00472f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472f38.md#insn-00472f74)

~~~diff
- 00472f14 ["INT_ADD", "register:40f0:8", ["const:472f14:8", "const:4:8"]]
- 00472f14 ["CALL", null, ["callee:00c53d00:8"]]
+ 00472f54 ["INT_ADD", "register:40f0:8", ["const:472f54:8", "const:4:8"]]
+ 00472f54 ["CALL", null, ["callee:00c53d00:8"]]
- 00472f14 bytes 73821f94
+ 00472f54 bytes 6b831f94
- 00472f34 ["COPY", "register:0:8", ["register:4040:8"]]
- 00472f34 ["INT_ADD", "register:40f0:8", ["const:472f34:8", "const:4:8"]]
- 00472f34 ["CALLIND", null, ["register:0:8"]]
+ 00472f74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00472f74 ["INT_ADD", "register:40f0:8", ["const:472f74:8", "const:4:8"]]
+ 00472f74 ["CALLIND", null, ["register:0:8"]]
- 00472f34 bytes 00013fd6
+ 00472f74 bytes 00013fd6
~~~


<a id="compare-01614899fb8fc960214178bf1fb47c08"></a>

### [`00472f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472f48.md) → [`00472f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472f88.md) FUN_00472f88

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472f48.md#insn-00472f64) · [`00472f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472f48.md#insn-00472f84)
- 新版 [`00472fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472f88.md#insn-00472fa4) · [`00472fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472f88.md#insn-00472fc4)

~~~diff
- 00472f64 ["INT_ADD", "register:40f0:8", ["const:472f64:8", "const:4:8"]]
- 00472f64 ["CALL", null, ["callee:00c53d00:8"]]
+ 00472fa4 ["INT_ADD", "register:40f0:8", ["const:472fa4:8", "const:4:8"]]
+ 00472fa4 ["CALL", null, ["callee:00c53d00:8"]]
- 00472f64 bytes 5f821f94
+ 00472fa4 bytes 57831f94
- 00472f84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00472f84 ["INT_ADD", "register:40f0:8", ["const:472f84:8", "const:4:8"]]
- 00472f84 ["CALLIND", null, ["register:0:8"]]
+ 00472fc4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00472fc4 ["INT_ADD", "register:40f0:8", ["const:472fc4:8", "const:4:8"]]
+ 00472fc4 ["CALLIND", null, ["register:0:8"]]
- 00472f84 bytes 00013fd6
+ 00472fc4 bytes 00013fd6
~~~


<a id="compare-62c9fcd4e9b287b01c7b7da61ad641d4"></a>

### [`00472f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472f98.md) → [`00472fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472fd8.md) FUN_00472fd8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00472fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472f98.md#insn-00472fb4) · [`00472fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472f98.md#insn-00472fd4)
- 新版 [`00472ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472fd8.md#insn-00472ff4) · [`00473014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472fd8.md#insn-00473014)

~~~diff
- 00472fb4 ["INT_ADD", "register:40f0:8", ["const:472fb4:8", "const:4:8"]]
- 00472fb4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00472ff4 ["INT_ADD", "register:40f0:8", ["const:472ff4:8", "const:4:8"]]
+ 00472ff4 ["CALL", null, ["callee:00c53d00:8"]]
- 00472fb4 bytes 4b821f94
+ 00472ff4 bytes 43831f94
- 00472fd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00472fd4 ["INT_ADD", "register:40f0:8", ["const:472fd4:8", "const:4:8"]]
- 00472fd4 ["CALLIND", null, ["register:0:8"]]
+ 00473014 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00473014 ["INT_ADD", "register:40f0:8", ["const:473014:8", "const:4:8"]]
+ 00473014 ["CALLIND", null, ["register:0:8"]]
- 00472fd4 bytes 00013fd6
+ 00473014 bytes 00013fd6
~~~


<a id="compare-abd9de4238224f1d491401a50afe8190"></a>

### [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) → [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) FUN_00473540

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 33件 [`00473354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473354.md) [`00481420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481420.md) [`004841d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/004841d0.md) [`004bc0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc0d4.md) [`004c3afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3afc.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`004795e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004795e4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 33件 [`00473394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473394.md) [`00481460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481460.md) [`00484210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484210.md) [`004bc114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc114.md) [`004c3b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c3b3c.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00479624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479624.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00473564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md#insn-00473564) · [`004735c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md#insn-004735c4) · [`00473610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md#insn-00473610)
- 新版 [`004735a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md#insn-004735a4) · [`00473604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md#insn-00473604) · [`00473650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md#insn-00473650)

~~~diff
- 00473564 ["INT_ADD", "register:40f0:8", ["const:473564:8", "const:4:8"]]
- 00473564 ["CALL", null, ["callee:00c57e90:8"]]
+ 004735a4 ["INT_ADD", "register:40f0:8", ["const:4735a4:8", "const:4:8"]]
+ 004735a4 ["CALL", null, ["callee:00c57e90:8"]]
- 00473564 bytes 4b911f94
+ 004735a4 bytes 3b921f94
- 004735c4 ["INT_ADD", "register:40f0:8", ["const:4735c4:8", "const:4:8"]]
- 004735c4 ["CALL", null, ["callee:0043bb20:8"]]
+ 00473604 ["INT_ADD", "register:40f0:8", ["const:473604:8", "const:4:8"]]
+ 00473604 ["CALL", null, ["callee:0043bb20:8"]]
- 004735c4 bytes 4721ff97
+ 00473604 bytes 4721ff97
- 00473610 ["INT_ADD", "register:40f0:8", ["const:473610:8", "const:4:8"]]
- 00473610 ["CALL", null, ["callee:00440f5c:8"]]
+ 00473650 ["INT_ADD", "register:40f0:8", ["const:473650:8", "const:4:8"]]
+ 00473650 ["CALL", null, ["callee:00440f5c:8"]]
- 00473610 bytes 4336ff97
+ 00473650 bytes 4336ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c313dca1b42cf3f7e289b8f7f39495ce"></a>

### [`00473e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473e2c.md) → [`00473e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473e6c.md) FUN_00473e6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00473e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473e2c.md#insn-00473e48) · [`00473e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473e2c.md#insn-00473e68)
- 新版 [`00473e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473e6c.md#insn-00473e88) · [`00473ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473e6c.md#insn-00473ea8)

~~~diff
- 00473e48 ["INT_ADD", "register:40f0:8", ["const:473e48:8", "const:4:8"]]
- 00473e48 ["CALL", null, ["callee:00c53d00:8"]]
+ 00473e88 ["INT_ADD", "register:40f0:8", ["const:473e88:8", "const:4:8"]]
+ 00473e88 ["CALL", null, ["callee:00c53d00:8"]]
- 00473e48 bytes a67e1f94
+ 00473e88 bytes 9e7f1f94
- 00473e68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00473e68 ["INT_ADD", "register:40f0:8", ["const:473e68:8", "const:4:8"]]
- 00473e68 ["CALLIND", null, ["register:0:8"]]
+ 00473ea8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00473ea8 ["INT_ADD", "register:40f0:8", ["const:473ea8:8", "const:4:8"]]
+ 00473ea8 ["CALLIND", null, ["register:0:8"]]
- 00473e68 bytes 00013fd6
+ 00473ea8 bytes 00013fd6
~~~


<a id="compare-0cd076e0a5725f0b4b8a00655059e871"></a>

### [`00473e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473e7c.md) → [`00473ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473ebc.md) FUN_00473ebc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00473e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473e7c.md#insn-00473e98) · [`00473eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473e7c.md#insn-00473eac) · [`00473ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473e7c.md#insn-00473ecc)
- 新版 [`00473ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473ebc.md#insn-00473ed8) · [`00473eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473ebc.md#insn-00473eec) · [`00473f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473ebc.md#insn-00473f0c)

~~~diff
- 00473e98 ["INT_ADD", "register:40f0:8", ["const:473e98:8", "const:4:8"]]
- 00473e98 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00473ed8 ["INT_ADD", "register:40f0:8", ["const:473ed8:8", "const:4:8"]]
+ 00473ed8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00473e98 bytes 068f1f94
+ 00473ed8 bytes f68f1f94
- 00473eac ["INT_ADD", "register:40f0:8", ["const:473eac:8", "const:4:8"]]
- 00473eac ["CALL", null, ["callee:00c53d00:8"]]
+ 00473eec ["INT_ADD", "register:40f0:8", ["const:473eec:8", "const:4:8"]]
+ 00473eec ["CALL", null, ["callee:00c53d00:8"]]
- 00473eac bytes 8d7e1f94
+ 00473eec bytes 857f1f94
- 00473ecc ["COPY", "register:0:8", ["register:4040:8"]]
- 00473ecc ["INT_ADD", "register:40f0:8", ["const:473ecc:8", "const:4:8"]]
- 00473ecc ["CALLIND", null, ["register:0:8"]]
+ 00473f0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00473f0c ["INT_ADD", "register:40f0:8", ["const:473f0c:8", "const:4:8"]]
+ 00473f0c ["CALLIND", null, ["register:0:8"]]
- 00473ecc bytes 00013fd6
+ 00473f0c bytes 00013fd6
~~~


<a id="compare-3fcf1dfc6179739e23da1658aa5b4b1c"></a>

### [`00473ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473ee0.md) → [`00473f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473f20.md) FUN_00473f20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00473efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473ee0.md#insn-00473efc) · [`00473f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473ee0.md#insn-00473f1c)
- 新版 [`00473f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473f20.md#insn-00473f3c) · [`00473f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473f20.md#insn-00473f5c)

~~~diff
- 00473efc ["INT_ADD", "register:40f0:8", ["const:473efc:8", "const:4:8"]]
- 00473efc ["CALL", null, ["callee:00c53d00:8"]]
+ 00473f3c ["INT_ADD", "register:40f0:8", ["const:473f3c:8", "const:4:8"]]
+ 00473f3c ["CALL", null, ["callee:00c53d00:8"]]
- 00473efc bytes 797e1f94
+ 00473f3c bytes 717f1f94
- 00473f1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00473f1c ["INT_ADD", "register:40f0:8", ["const:473f1c:8", "const:4:8"]]
- 00473f1c ["CALLIND", null, ["register:0:8"]]
+ 00473f5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00473f5c ["INT_ADD", "register:40f0:8", ["const:473f5c:8", "const:4:8"]]
+ 00473f5c ["CALLIND", null, ["register:0:8"]]
- 00473f1c bytes 00013fd6
+ 00473f5c bytes 00013fd6
~~~


<a id="compare-7eb06879b4363cc93e12c33373e59f2f"></a>

### [`00473f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473f30.md) → [`00473f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473f70.md) FUN_00473f70

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`00a8e3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8e/00a8e3bc.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`00a8e5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8e/00a8e5b4.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00473f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473f30.md#insn-00473f4c) · [`00473f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473f30.md#insn-00473f6c)
- 新版 [`00473f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473f70.md#insn-00473f8c) · [`00473fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473f70.md#insn-00473fac)

~~~diff
- 00473f4c ["INT_ADD", "register:40f0:8", ["const:473f4c:8", "const:4:8"]]
- 00473f4c ["CALL", null, ["callee:00c53d00:8"]]
+ 00473f8c ["INT_ADD", "register:40f0:8", ["const:473f8c:8", "const:4:8"]]
+ 00473f8c ["CALL", null, ["callee:00c53d00:8"]]
- 00473f4c bytes 657e1f94
+ 00473f8c bytes 5d7f1f94
- 00473f6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00473f6c ["INT_ADD", "register:40f0:8", ["const:473f6c:8", "const:4:8"]]
- 00473f6c ["CALLIND", null, ["register:0:8"]]
+ 00473fac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00473fac ["INT_ADD", "register:40f0:8", ["const:473fac:8", "const:4:8"]]
+ 00473fac ["CALLIND", null, ["register:0:8"]]
- 00473f6c bytes 00013fd6
+ 00473fac bytes 00013fd6
~~~


<a id="compare-45ba06d33b8d8f458ad91cf565b5524d"></a>

### [`00473f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473f80.md) → [`00473fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473fc0.md) FUN_00473fc0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`00a8e3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8e/00a8e3bc.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`00a8e5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8e/00a8e5b4.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00473f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473f80.md#insn-00473f9c) · [`00473fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473f80.md#insn-00473fbc)
- 新版 [`00473fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473fc0.md#insn-00473fdc) · [`00473ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473fc0.md#insn-00473ffc)

~~~diff
- 00473f9c ["INT_ADD", "register:40f0:8", ["const:473f9c:8", "const:4:8"]]
- 00473f9c ["CALL", null, ["callee:00c53d00:8"]]
+ 00473fdc ["INT_ADD", "register:40f0:8", ["const:473fdc:8", "const:4:8"]]
+ 00473fdc ["CALL", null, ["callee:00c53d00:8"]]
- 00473f9c bytes 517e1f94
+ 00473fdc bytes 497f1f94
- 00473fbc ["COPY", "register:0:8", ["register:4040:8"]]
- 00473fbc ["INT_ADD", "register:40f0:8", ["const:473fbc:8", "const:4:8"]]
- 00473fbc ["CALLIND", null, ["register:0:8"]]
+ 00473ffc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00473ffc ["INT_ADD", "register:40f0:8", ["const:473ffc:8", "const:4:8"]]
+ 00473ffc ["CALLIND", null, ["register:0:8"]]
- 00473fbc bytes 00013fd6
+ 00473ffc bytes 00013fd6
~~~


<a id="compare-6240aea7998a98286c0a34c01b840498"></a>

### [`00473fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473fd0.md) → [`00474010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474010.md) FUN_00474010

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 6件 [`0047a7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a7d0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 6件 [`0047a810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a810.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00474008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473fd0.md#insn-00474008) · [`00474014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473fd0.md#insn-00474014) · [`00474020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473fd0.md#insn-00474020)
- 新版 [`00474048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474010.md#insn-00474048) · [`00474054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474010.md#insn-00474054) · [`00474060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474010.md#insn-00474060)

~~~diff
- 00474008 ["INT_ADD", "register:40f0:8", ["const:474008:8", "const:4:8"]]
- 00474008 ["CALL", null, ["callee:00c580e0:8"]]
+ 00474048 ["INT_ADD", "register:40f0:8", ["const:474048:8", "const:4:8"]]
+ 00474048 ["CALL", null, ["callee:00c580e0:8"]]
- 00474008 bytes 368f1f94
+ 00474048 bytes 26901f94
- 00474014 ["INT_ADD", "register:40f0:8", ["const:474014:8", "const:4:8"]]
- 00474014 ["CALL", null, ["callee:0047a810:8"]]
+ 00474054 ["INT_ADD", "register:40f0:8", ["const:474054:8", "const:4:8"]]
+ 00474054 ["CALL", null, ["callee:0047a810:8"]]
- 00474014 bytes ef190094
+ 00474054 bytes ef190094
- 00474020 ["INT_ADD", "register:40f0:8", ["const:474020:8", "const:4:8"]]
- 00474020 ["CALL", null, ["callee:00c580f0:8"]]
+ 00474060 ["INT_ADD", "register:40f0:8", ["const:474060:8", "const:4:8"]]
+ 00474060 ["CALL", null, ["callee:00c580f0:8"]]
- 00474020 bytes 348f1f94
+ 00474060 bytes 24901f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f82babb5c2ea6c4c8ccb098bda0ffe7"></a>

### [`00474108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474108.md) → [`00474148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474148.md) FUN_00474148

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00474124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474108.md#insn-00474124) · [`00474144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474108.md#insn-00474144)
- 新版 [`00474164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474148.md#insn-00474164) · [`00474184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474148.md#insn-00474184)

~~~diff
- 00474124 ["INT_ADD", "register:40f0:8", ["const:474124:8", "const:4:8"]]
- 00474124 ["CALL", null, ["callee:00c53d00:8"]]
+ 00474164 ["INT_ADD", "register:40f0:8", ["const:474164:8", "const:4:8"]]
+ 00474164 ["CALL", null, ["callee:00c53d00:8"]]
- 00474124 bytes ef7d1f94
+ 00474164 bytes e77e1f94
- 00474144 ["COPY", "register:0:8", ["register:4040:8"]]
- 00474144 ["INT_ADD", "register:40f0:8", ["const:474144:8", "const:4:8"]]
- 00474144 ["CALLIND", null, ["register:0:8"]]
+ 00474184 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00474184 ["INT_ADD", "register:40f0:8", ["const:474184:8", "const:4:8"]]
+ 00474184 ["CALLIND", null, ["register:0:8"]]
- 00474144 bytes 00013fd6
+ 00474184 bytes 00013fd6
~~~


<a id="compare-42765489ab194827b366bc8374aea66d"></a>

### [`00474ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474ab8.md) → [`00474af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474af8.md) FUN_00474af8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00474aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474aec.md) [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cd0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00474b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474b2c.md) [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00474acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474ab8.md#insn-00474acc) · [`00474ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474ab8.md#insn-00474ad4)
- 新版 [`00474b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474af8.md#insn-00474b0c) · [`00474b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474af8.md#insn-00474b14)

~~~diff
- 00474acc ["INT_ADD", "register:40f0:8", ["const:474acc:8", "const:4:8"]]
- 00474acc ["CALL", null, ["callee:00c580d0:8"]]
+ 00474b0c ["INT_ADD", "register:40f0:8", ["const:474b0c:8", "const:4:8"]]
+ 00474b0c ["CALL", null, ["callee:00c580d0:8"]]
- 00474acc bytes 818c1f94
+ 00474b0c bytes 718d1f94
- 00474ad4 ["INT_ADD", "register:40f0:8", ["const:474ad4:8", "const:4:8"]]
- 00474ad4 ["CALL", null, ["callee:00c57e60:8"]]
+ 00474b14 ["INT_ADD", "register:40f0:8", ["const:474b14:8", "const:4:8"]]
+ 00474b14 ["CALL", null, ["callee:00c57e60:8"]]
- 00474ad4 bytes e38b1f94
+ 00474b14 bytes d38c1f94
~~~


<a id="compare-d837f2712b8096575365e71e164cf1ae"></a>

### [`00474aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474aec.md) → [`00474b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474b2c.md) FUN_00474b2c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00474ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474ab8.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00474af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474af8.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00474b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474aec.md#insn-00474b68) · [`00474b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474aec.md#insn-00474b7c) · [`00474b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474aec.md#insn-00474b84)
- 新版 [`00474ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474b2c.md#insn-00474ba8) · [`00474bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474b2c.md#insn-00474bbc) · [`00474bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474b2c.md#insn-00474bc4)

~~~diff
- 00474b68 ["INT_ADD", "register:40f0:8", ["const:474b68:8", "const:4:8"]]
- 00474b68 ["CALL", null, ["callee:00c53d00:8"]]
+ 00474ba8 ["INT_ADD", "register:40f0:8", ["const:474ba8:8", "const:4:8"]]
+ 00474ba8 ["CALL", null, ["callee:00c53d00:8"]]
- 00474b68 bytes 5e7b1f94
+ 00474ba8 bytes 567c1f94
- 00474b7c ["COPY", "register:0:8", ["register:4040:8"]]
- 00474b7c ["INT_ADD", "register:40f0:8", ["const:474b7c:8", "const:4:8"]]
- 00474b7c ["CALLIND", null, ["register:0:8"]]
+ 00474bbc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00474bbc ["INT_ADD", "register:40f0:8", ["const:474bbc:8", "const:4:8"]]
+ 00474bbc ["CALLIND", null, ["register:0:8"]]
- 00474b7c bytes 00013fd6
+ 00474bbc bytes 00013fd6
- 00474b84 ["INT_ADD", "register:40f0:8", ["const:474b84:8", "const:4:8"]]
- 00474b84 ["CALL", null, ["callee:00c57e80:8"]]
+ 00474bc4 ["INT_ADD", "register:40f0:8", ["const:474bc4:8", "const:4:8"]]
+ 00474bc4 ["CALL", null, ["callee:00c57e80:8"]]
- 00474b84 bytes bf8b1f94
+ 00474bc4 bytes af8c1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42f0c7caa77981e2a02ad3a1493a60ef"></a>

### [`00474cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474cbc.md) → [`00474cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474cfc.md) FUN_00474cfc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00474cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474cf0.md) [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cd0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00474d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474d30.md) [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00474cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474cbc.md#insn-00474cd0) · [`00474cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474cbc.md#insn-00474cd8)
- 新版 [`00474d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474cfc.md#insn-00474d10) · [`00474d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474cfc.md#insn-00474d18)

~~~diff
- 00474cd0 ["INT_ADD", "register:40f0:8", ["const:474cd0:8", "const:4:8"]]
- 00474cd0 ["CALL", null, ["callee:00c580d0:8"]]
+ 00474d10 ["INT_ADD", "register:40f0:8", ["const:474d10:8", "const:4:8"]]
+ 00474d10 ["CALL", null, ["callee:00c580d0:8"]]
- 00474cd0 bytes 008c1f94
+ 00474d10 bytes f08c1f94
- 00474cd8 ["INT_ADD", "register:40f0:8", ["const:474cd8:8", "const:4:8"]]
- 00474cd8 ["CALL", null, ["callee:00c57e60:8"]]
+ 00474d18 ["INT_ADD", "register:40f0:8", ["const:474d18:8", "const:4:8"]]
+ 00474d18 ["CALL", null, ["callee:00c57e60:8"]]
- 00474cd8 bytes 628b1f94
+ 00474d18 bytes 528c1f94
~~~


<a id="compare-5289aa797d6fa47546e4d2d60d93efc6"></a>

### [`00474cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474cf0.md) → [`00474d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474d30.md) FUN_00474d30

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00474cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474cbc.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00474cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474cfc.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00474d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474cf0.md#insn-00474d74) · [`00474d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474cf0.md#insn-00474d88) · [`00474d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474cf0.md#insn-00474d90)
- 新版 [`00474db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474d30.md#insn-00474db4) · [`00474dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474d30.md#insn-00474dc8) · [`00474dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474d30.md#insn-00474dd0)

~~~diff
- 00474d74 ["INT_ADD", "register:40f0:8", ["const:474d74:8", "const:4:8"]]
- 00474d74 ["CALL", null, ["callee:00c53d00:8"]]
+ 00474db4 ["INT_ADD", "register:40f0:8", ["const:474db4:8", "const:4:8"]]
+ 00474db4 ["CALL", null, ["callee:00c53d00:8"]]
- 00474d74 bytes db7a1f94
+ 00474db4 bytes d37b1f94
- 00474d88 ["COPY", "register:0:8", ["register:4040:8"]]
- 00474d88 ["INT_ADD", "register:40f0:8", ["const:474d88:8", "const:4:8"]]
- 00474d88 ["CALLIND", null, ["register:0:8"]]
+ 00474dc8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00474dc8 ["INT_ADD", "register:40f0:8", ["const:474dc8:8", "const:4:8"]]
+ 00474dc8 ["CALLIND", null, ["register:0:8"]]
- 00474d88 bytes 00013fd6
+ 00474dc8 bytes 00013fd6
- 00474d90 ["INT_ADD", "register:40f0:8", ["const:474d90:8", "const:4:8"]]
- 00474d90 ["CALL", null, ["callee:00c57e80:8"]]
+ 00474dd0 ["INT_ADD", "register:40f0:8", ["const:474dd0:8", "const:4:8"]]
+ 00474dd0 ["CALL", null, ["callee:00c57e80:8"]]
- 00474d90 bytes 3c8b1f94
+ 00474dd0 bytes 2c8c1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdd6195653bda03c2a921a5204af103e"></a>

### [`00474e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474e88.md) → [`00474ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ec8.md) FUN_00474ec8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00472fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472fe8.md) [`00475840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475840.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00475348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475348.md) [`004754d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/004754d0.md) [`0047565c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/0047565c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`00473028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473028.md) [`00475880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475880.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00475388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475388.md) [`00475510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475510.md) [`0047569c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/0047569c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00474f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474e88.md#insn-00474f20) · [`00474f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474e88.md#insn-00474f64) · [`00474f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474e88.md#insn-00474f74)
- 新版 [`00474f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ec8.md#insn-00474f60) · [`00474fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ec8.md#insn-00474fa4) · [`00474fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ec8.md#insn-00474fb4)

~~~diff
- 00474f20 ["INT_ADD", "register:40f0:8", ["const:474f20:8", "const:4:8"]]
- 00474f20 ["CALL", null, ["callee:00c57f40:8"]]
+ 00474f60 ["INT_ADD", "register:40f0:8", ["const:474f60:8", "const:4:8"]]
+ 00474f60 ["CALL", null, ["callee:00c57f40:8"]]
- 00474f20 bytes 088b1f94
+ 00474f60 bytes f88b1f94
- 00474f64 ["INT_ADD", "register:40f0:8", ["const:474f64:8", "const:4:8"]]
- 00474f64 ["CALL", null, ["callee:00c57e90:8"]]
+ 00474fa4 ["INT_ADD", "register:40f0:8", ["const:474fa4:8", "const:4:8"]]
+ 00474fa4 ["CALL", null, ["callee:00c57e90:8"]]
- 00474f64 bytes cb8a1f94
+ 00474fa4 bytes bb8b1f94
- 00474f74 ["INT_ADD", "register:40f0:8", ["const:474f74:8", "const:4:8"]]
- 00474f74 ["CALL", null, ["callee:00475388:8"]]
+ 00474fb4 ["INT_ADD", "register:40f0:8", ["const:474fb4:8", "const:4:8"]]
+ 00474fb4 ["CALL", null, ["callee:00475388:8"]]
- 00474f74 bytes f5000094
+ 00474fb4 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-222a239f5cd53d217834476fc3b04a6a"></a>

### [`00475348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475348.md) → [`00475388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475388.md) FUN_00475388

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00474e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474e88.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00474ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ec8.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004753b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475348.md#insn-004753b0) · [`004753e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475348.md#insn-004753e8) · [`00475498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475348.md#insn-00475498)
- 新版 [`004753f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475388.md#insn-004753f0) · [`00475428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475388.md#insn-00475428) · [`004754d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475388.md#insn-004754d8)

~~~diff
- 004753b0 ["INT_ADD", "register:40f0:8", ["const:4753b0:8", "const:4:8"]]
- 004753b0 ["CALL", null, ["callee:00c57f40:8"]]
+ 004753f0 ["INT_ADD", "register:40f0:8", ["const:4753f0:8", "const:4:8"]]
+ 004753f0 ["CALL", null, ["callee:00c57f40:8"]]
- 004753b0 bytes e4891f94
+ 004753f0 bytes d48a1f94
- 004753e8 ["INT_ADD", "register:40f0:8", ["const:4753e8:8", "const:4:8"]]
- 004753e8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00475428 ["INT_ADD", "register:40f0:8", ["const:475428:8", "const:4:8"]]
+ 00475428 ["CALL", null, ["callee:00c57e90:8"]]
- 004753e8 bytes aa891f94
+ 00475428 bytes 9a8a1f94
- 00475498 ["INT_ADD", "register:40f0:8", ["const:475498:8", "const:4:8"]]
- 00475498 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004754d8 ["INT_ADD", "register:40f0:8", ["const:4754d8:8", "const:4:8"]]
+ 004754d8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00475498 bytes 86891f94
+ 004754d8 bytes 768a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ede76dae04600bb9bb8be6f028e9293f"></a>

### [`004754d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/004754d0.md) → [`00475510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475510.md) FUN_00475510

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00474e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474e88.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00474ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ec8.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00475540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/004754d0.md#insn-00475540) · [`00475578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/004754d0.md#insn-00475578) · [`00475628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/004754d0.md#insn-00475628)
- 新版 [`00475580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475510.md#insn-00475580) · [`004755b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475510.md#insn-004755b8) · [`00475668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475510.md#insn-00475668)

~~~diff
- 00475540 ["INT_ADD", "register:40f0:8", ["const:475540:8", "const:4:8"]]
- 00475540 ["CALL", null, ["callee:00c57f40:8"]]
+ 00475580 ["INT_ADD", "register:40f0:8", ["const:475580:8", "const:4:8"]]
+ 00475580 ["CALL", null, ["callee:00c57f40:8"]]
- 00475540 bytes 80891f94
+ 00475580 bytes 708a1f94
- 00475578 ["INT_ADD", "register:40f0:8", ["const:475578:8", "const:4:8"]]
- 00475578 ["CALL", null, ["callee:00c57e90:8"]]
+ 004755b8 ["INT_ADD", "register:40f0:8", ["const:4755b8:8", "const:4:8"]]
+ 004755b8 ["CALL", null, ["callee:00c57e90:8"]]
- 00475578 bytes 46891f94
+ 004755b8 bytes 368a1f94
- 00475628 ["INT_ADD", "register:40f0:8", ["const:475628:8", "const:4:8"]]
- 00475628 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00475668 ["INT_ADD", "register:40f0:8", ["const:475668:8", "const:4:8"]]
+ 00475668 ["CALL", null, ["callee:00c57eb0:8"]]
- 00475628 bytes 22891f94
+ 00475668 bytes 128a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7c6fbdaa5e335917e9ac7b5d83f9778"></a>

### [`0047565c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/0047565c.md) → [`0047569c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/0047569c.md) FUN_0047569c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00474e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474e88.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00474ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ec8.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004756cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/0047565c.md#insn-004756cc) · [`00475704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/0047565c.md#insn-00475704) · [`004757b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/0047565c.md#insn-004757b4)
- 新版 [`0047570c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/0047569c.md#insn-0047570c) · [`00475744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/0047569c.md#insn-00475744) · [`004757f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/0047569c.md#insn-004757f4)

~~~diff
- 004756cc ["INT_ADD", "register:40f0:8", ["const:4756cc:8", "const:4:8"]]
- 004756cc ["CALL", null, ["callee:00c57f40:8"]]
+ 0047570c ["INT_ADD", "register:40f0:8", ["const:47570c:8", "const:4:8"]]
+ 0047570c ["CALL", null, ["callee:00c57f40:8"]]
- 004756cc bytes 1d891f94
+ 0047570c bytes 0d8a1f94
- 00475704 ["INT_ADD", "register:40f0:8", ["const:475704:8", "const:4:8"]]
- 00475704 ["CALL", null, ["callee:00c57e90:8"]]
+ 00475744 ["INT_ADD", "register:40f0:8", ["const:475744:8", "const:4:8"]]
+ 00475744 ["CALL", null, ["callee:00c57e90:8"]]
- 00475704 bytes e3881f94
+ 00475744 bytes d3891f94
- 004757b4 ["INT_ADD", "register:40f0:8", ["const:4757b4:8", "const:4:8"]]
- 004757b4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004757f4 ["INT_ADD", "register:40f0:8", ["const:4757f4:8", "const:4:8"]]
+ 004757f4 ["CALL", null, ["callee:00c57eb0:8"]]
- 004757b4 bytes bf881f94
+ 004757f4 bytes af891f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-686c17fbd9f63b5901962e4b257d00ee"></a>

### [`00475840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475840.md) → [`00475880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475880.md) FUN_00475880

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00474e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474e88.md) [`00475ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475ae8.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00474ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ec8.md) [`00475b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475b28.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00475880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475840.md#insn-00475880) · [`004758a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475840.md#insn-004758a0) · [`004758b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475840.md#insn-004758b4)
- 新版 [`004758c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475880.md#insn-004758c0) · [`004758e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475880.md#insn-004758e0) · [`004758f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475880.md#insn-004758f4)

~~~diff
- 00475880 ["COPY", "register:0:8", ["register:4040:8"]]
- 00475880 ["INT_ADD", "register:40f0:8", ["const:475880:8", "const:4:8"]]
- 00475880 ["CALLIND", null, ["register:0:8"]]
+ 004758c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004758c0 ["INT_ADD", "register:40f0:8", ["const:4758c0:8", "const:4:8"]]
+ 004758c0 ["CALLIND", null, ["register:0:8"]]
- 00475880 bytes 00013fd6
+ 004758c0 bytes 00013fd6
- 004758a0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004758a0 ["INT_ADD", "register:40f0:8", ["const:4758a0:8", "const:4:8"]]
- 004758a0 ["CALLIND", null, ["register:0:8"]]
+ 004758e0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004758e0 ["INT_ADD", "register:40f0:8", ["const:4758e0:8", "const:4:8"]]
+ 004758e0 ["CALLIND", null, ["register:0:8"]]
- 004758a0 bytes 20013fd6
+ 004758e0 bytes 20013fd6
- 004758b4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004758b4 ["INT_ADD", "register:40f0:8", ["const:4758b4:8", "const:4:8"]]
- 004758b4 ["CALLIND", null, ["register:0:8"]]
+ 004758f4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004758f4 ["INT_ADD", "register:40f0:8", ["const:4758f4:8", "const:4:8"]]
+ 004758f4 ["CALLIND", null, ["register:0:8"]]
- 004758b4 bytes 20013fd6
+ 004758f4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-054a9d1b17be274671b858d1dc21d55c"></a>

### [`00475ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475ae8.md) → [`00475b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475b28.md) FUN_00475b28

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00475840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475840.md) · 呼出先 8件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00475880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475880.md) · 呼出先 8件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00475b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475ae8.md#insn-00475b34) · [`00475b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475ae8.md#insn-00475b40) · [`00475b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475ae8.md#insn-00475b54)
- 新版 [`00475b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475b28.md#insn-00475b74) · [`00475b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475b28.md#insn-00475b80) · [`00475b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475b28.md#insn-00475b94)

~~~diff
- 00475b34 ["INT_ADD", "register:40f0:8", ["const:475b34:8", "const:4:8"]]
- 00475b34 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00475b74 ["INT_ADD", "register:40f0:8", ["const:475b74:8", "const:4:8"]]
+ 00475b74 ["CALL", null, ["callee:00c53cd0:8"]]
- 00475b34 bytes 5f771f94
+ 00475b74 bytes 57781f94
- 00475b40 ["INT_ADD", "register:40f0:8", ["const:475b40:8", "const:4:8"]]
- 00475b40 ["CALL", null, ["callee:00c53d00:8"]]
+ 00475b80 ["INT_ADD", "register:40f0:8", ["const:475b80:8", "const:4:8"]]
+ 00475b80 ["CALL", null, ["callee:00c53d00:8"]]
- 00475b40 bytes 68771f94
+ 00475b80 bytes 60781f94
- 00475b54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00475b54 ["INT_ADD", "register:40f0:8", ["const:475b54:8", "const:4:8"]]
- 00475b54 ["CALLIND", null, ["register:0:8"]]
+ 00475b94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00475b94 ["INT_ADD", "register:40f0:8", ["const:475b94:8", "const:4:8"]]
+ 00475b94 ["CALLIND", null, ["register:0:8"]]
- 00475b54 bytes 00013fd6
+ 00475b94 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d21a2c8b99cc8c0a9c9385ceb7f13b31"></a>

### [`00476114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476114.md) → [`00476154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476154.md) FUN_00476154

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047613c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476114.md#insn-0047613c) · [`00476144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476114.md#insn-00476144)
- 新版 [`0047617c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476154.md#insn-0047617c) · [`00476184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476154.md#insn-00476184)

~~~diff
- 0047613c ["INT_ADD", "register:40f0:8", ["const:47613c:8", "const:4:8"]]
- 0047613c ["CALL", null, ["callee:00c58150:8"]]
+ 0047617c ["INT_ADD", "register:40f0:8", ["const:47617c:8", "const:4:8"]]
+ 0047617c ["CALL", null, ["callee:00c58150:8"]]
- 0047613c bytes 05871f94
+ 0047617c bytes f5871f94
- 00476144 ["INT_ADD", "register:40f0:8", ["const:476144:8", "const:4:8"]]
- 00476144 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00476184 ["INT_ADD", "register:40f0:8", ["const:476184:8", "const:4:8"]]
+ 00476184 ["CALL", null, ["callee:00c57eb0:8"]]
- 00476144 bytes 5b861f94
+ 00476184 bytes 4b871f94
~~~


<a id="compare-ca6be85a534ccec84ea1c8bdc35185fc"></a>

### [`004764f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/004764f8.md) → [`00476538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476538.md) FUN_00476538

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00476514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/004764f8.md#insn-00476514) · [`00476534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/004764f8.md#insn-00476534)
- 新版 [`00476554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476538.md#insn-00476554) · [`00476574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476538.md#insn-00476574)

~~~diff
- 00476514 ["INT_ADD", "register:40f0:8", ["const:476514:8", "const:4:8"]]
- 00476514 ["CALL", null, ["callee:00c53d00:8"]]
+ 00476554 ["INT_ADD", "register:40f0:8", ["const:476554:8", "const:4:8"]]
+ 00476554 ["CALL", null, ["callee:00c53d00:8"]]
- 00476514 bytes f3741f94
+ 00476554 bytes eb751f94
- 00476534 ["COPY", "register:0:8", ["register:4040:8"]]
- 00476534 ["INT_ADD", "register:40f0:8", ["const:476534:8", "const:4:8"]]
- 00476534 ["CALLIND", null, ["register:0:8"]]
+ 00476574 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00476574 ["INT_ADD", "register:40f0:8", ["const:476574:8", "const:4:8"]]
+ 00476574 ["CALLIND", null, ["register:0:8"]]
- 00476534 bytes 00013fd6
+ 00476574 bytes 00013fd6
~~~


<a id="compare-095f395c3dcd7652488f0b81bcfc8140"></a>

### [`00478108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478108.md) → [`00478148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478148.md) FUN_00478148

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00476688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md) [`0047798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/0047798c.md) · 呼出先 8件 [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md)
- 新版 呼出元 2件 [`004766c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md) [`004779cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/004779cc.md) · 呼出先 8件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00478144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478108.md#insn-00478144) · [`00478150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478108.md#insn-00478150) · [`00478164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478108.md#insn-00478164)
- 新版 [`00478184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478148.md#insn-00478184) · [`00478190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478148.md#insn-00478190) · [`004781a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478148.md#insn-004781a4)

~~~diff
- 00478144 ["INT_ADD", "register:40f0:8", ["const:478144:8", "const:4:8"]]
- 00478144 ["CALL", null, ["callee:00c580e0:8"]]
+ 00478184 ["INT_ADD", "register:40f0:8", ["const:478184:8", "const:4:8"]]
+ 00478184 ["CALL", null, ["callee:00c580e0:8"]]
- 00478144 bytes e77e1f94
+ 00478184 bytes d77f1f94
- 00478150 ["INT_ADD", "register:40f0:8", ["const:478150:8", "const:4:8"]]
- 00478150 ["CALL", null, ["callee:00c584a0:8"]]
+ 00478190 ["INT_ADD", "register:40f0:8", ["const:478190:8", "const:4:8"]]
+ 00478190 ["CALL", null, ["callee:00c584a0:8"]]
- 00478150 bytes d47f1f94
+ 00478190 bytes c4801f94
- 00478164 ["INT_ADD", "register:40f0:8", ["const:478164:8", "const:4:8"]]
- 00478164 ["CALL", null, ["callee:00c582f0:8"]]
+ 004781a4 ["INT_ADD", "register:40f0:8", ["const:4781a4:8", "const:4:8"]]
+ 004781a4 ["CALL", null, ["callee:00c582f0:8"]]
- 00478164 bytes 637f1f94
+ 004781a4 bytes 53801f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4f4bd4b63dd59c65a810faf1f11e275"></a>

### [`00478234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478234.md) → [`00478274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478274.md) FUN_00478274

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00478250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478234.md#insn-00478250) · [`00478270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478234.md#insn-00478270)
- 新版 [`00478290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478274.md#insn-00478290) · [`004782b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478274.md#insn-004782b0)

~~~diff
- 00478250 ["INT_ADD", "register:40f0:8", ["const:478250:8", "const:4:8"]]
- 00478250 ["CALL", null, ["callee:00c53d00:8"]]
+ 00478290 ["INT_ADD", "register:40f0:8", ["const:478290:8", "const:4:8"]]
+ 00478290 ["CALL", null, ["callee:00c53d00:8"]]
- 00478250 bytes a46d1f94
+ 00478290 bytes 9c6e1f94
- 00478270 ["COPY", "register:0:8", ["register:4040:8"]]
- 00478270 ["INT_ADD", "register:40f0:8", ["const:478270:8", "const:4:8"]]
- 00478270 ["CALLIND", null, ["register:0:8"]]
+ 004782b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004782b0 ["INT_ADD", "register:40f0:8", ["const:4782b0:8", "const:4:8"]]
+ 004782b0 ["CALLIND", null, ["register:0:8"]]
- 00478270 bytes 00013fd6
+ 004782b0 bytes 00013fd6
~~~


<a id="compare-1097e5bc6f33e75239f0f6cd7b421d0c"></a>

### [`00478284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478284.md) → [`004782c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/004782c4.md) FUN_004782c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004782a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478284.md#insn-004782a0) · [`004782c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478284.md#insn-004782c0)
- 新版 [`004782e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/004782c4.md#insn-004782e0) · [`00478300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/004782c4.md#insn-00478300)

~~~diff
- 004782a0 ["INT_ADD", "register:40f0:8", ["const:4782a0:8", "const:4:8"]]
- 004782a0 ["CALL", null, ["callee:00c53d00:8"]]
+ 004782e0 ["INT_ADD", "register:40f0:8", ["const:4782e0:8", "const:4:8"]]
+ 004782e0 ["CALL", null, ["callee:00c53d00:8"]]
- 004782a0 bytes 906d1f94
+ 004782e0 bytes 886e1f94
- 004782c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004782c0 ["INT_ADD", "register:40f0:8", ["const:4782c0:8", "const:4:8"]]
- 004782c0 ["CALLIND", null, ["register:0:8"]]
+ 00478300 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00478300 ["INT_ADD", "register:40f0:8", ["const:478300:8", "const:4:8"]]
+ 00478300 ["CALLIND", null, ["register:0:8"]]
- 004782c0 bytes 00013fd6
+ 00478300 bytes 00013fd6
~~~


<a id="compare-9c159f7c07b57cb60302cd396e79c4bd"></a>

### [`00478bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478bd4.md) → [`00478c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c14.md) FUN_00478c14

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00476b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476b10.md) [`00478b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478b50.md) [`00478bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478bd4.md) [`0048ce78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce78.md) · 呼出先 2件 [`00478bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478bd4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`00476b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476b50.md) [`00478b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478b90.md) [`00478c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c14.md) [`0048ceb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ceb8.md) · 呼出先 2件 [`00478c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c14.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00478bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478bd4.md#insn-00478bf4) · [`00478c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478bd4.md#insn-00478c00)
- 新版 [`00478c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c14.md#insn-00478c34) · [`00478c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c14.md#insn-00478c40)

~~~diff
- 00478bf4 ["INT_ADD", "register:40f0:8", ["const:478bf4:8", "const:4:8"]]
- 00478bf4 ["CALL", null, ["local:b0:8"]]
+ 00478c34 ["INT_ADD", "register:40f0:8", ["const:478c34:8", "const:4:8"]]
+ 00478c34 ["CALL", null, ["local:b0:8"]]
- 00478bf4 bytes f8ffff97
+ 00478c34 bytes f8ffff97
- 00478c00 ["INT_ADD", "register:40f0:8", ["const:478c00:8", "const:4:8"]]
- 00478c00 ["CALL", null, ["local:b0:8"]]
+ 00478c40 ["INT_ADD", "register:40f0:8", ["const:478c40:8", "const:4:8"]]
+ 00478c40 ["CALL", null, ["local:b0:8"]]
- 00478c00 bytes f5ffff97
+ 00478c40 bytes f5ffff97
~~~


<a id="compare-d2c989822372f9aced12d83fe3e78956"></a>

### [`00478c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c84.md) → [`00478cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478cc4.md) FUN_00478cc4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00475d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475d60.md) [`00476688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md) [`0047798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/0047798c.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00479144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479144.md) [`004792cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004792cc.md) [`00479458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479458.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`00475da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475da0.md) [`004766c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md) [`004779cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/004779cc.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00479184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479184.md) [`0047930c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/0047930c.md) [`00479498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479498.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00478d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c84.md#insn-00478d1c) · [`00478d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c84.md#insn-00478d60) · [`00478d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c84.md#insn-00478d70)
- 新版 [`00478d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478cc4.md#insn-00478d5c) · [`00478da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478cc4.md#insn-00478da0) · [`00478db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478cc4.md#insn-00478db0)

~~~diff
- 00478d1c ["INT_ADD", "register:40f0:8", ["const:478d1c:8", "const:4:8"]]
- 00478d1c ["CALL", null, ["callee:00c57f40:8"]]
+ 00478d5c ["INT_ADD", "register:40f0:8", ["const:478d5c:8", "const:4:8"]]
+ 00478d5c ["CALL", null, ["callee:00c57f40:8"]]
- 00478d1c bytes 897b1f94
+ 00478d5c bytes 797c1f94
- 00478d60 ["INT_ADD", "register:40f0:8", ["const:478d60:8", "const:4:8"]]
- 00478d60 ["CALL", null, ["callee:00c57e90:8"]]
+ 00478da0 ["INT_ADD", "register:40f0:8", ["const:478da0:8", "const:4:8"]]
+ 00478da0 ["CALL", null, ["callee:00c57e90:8"]]
- 00478d60 bytes 4c7b1f94
+ 00478da0 bytes 3c7c1f94
- 00478d70 ["INT_ADD", "register:40f0:8", ["const:478d70:8", "const:4:8"]]
- 00478d70 ["CALL", null, ["callee:00479184:8"]]
+ 00478db0 ["INT_ADD", "register:40f0:8", ["const:478db0:8", "const:4:8"]]
+ 00478db0 ["CALL", null, ["callee:00479184:8"]]
- 00478d70 bytes f5000094
+ 00478db0 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49187047084f8ab62de58a7ffc4850d6"></a>

### [`00479144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479144.md) → [`00479184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479184.md) FUN_00479184

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00478c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c84.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00478cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478cc4.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004791ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479144.md#insn-004791ac) · [`004791e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479144.md#insn-004791e4) · [`00479294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479144.md#insn-00479294)
- 新版 [`004791ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479184.md#insn-004791ec) · [`00479224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479184.md#insn-00479224) · [`004792d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479184.md#insn-004792d4)

~~~diff
- 004791ac ["INT_ADD", "register:40f0:8", ["const:4791ac:8", "const:4:8"]]
- 004791ac ["CALL", null, ["callee:00c57f40:8"]]
+ 004791ec ["INT_ADD", "register:40f0:8", ["const:4791ec:8", "const:4:8"]]
+ 004791ec ["CALL", null, ["callee:00c57f40:8"]]
- 004791ac bytes 657a1f94
+ 004791ec bytes 557b1f94
- 004791e4 ["INT_ADD", "register:40f0:8", ["const:4791e4:8", "const:4:8"]]
- 004791e4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00479224 ["INT_ADD", "register:40f0:8", ["const:479224:8", "const:4:8"]]
+ 00479224 ["CALL", null, ["callee:00c57e90:8"]]
- 004791e4 bytes 2b7a1f94
+ 00479224 bytes 1b7b1f94
- 00479294 ["INT_ADD", "register:40f0:8", ["const:479294:8", "const:4:8"]]
- 00479294 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004792d4 ["INT_ADD", "register:40f0:8", ["const:4792d4:8", "const:4:8"]]
+ 004792d4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00479294 bytes 077a1f94
+ 004792d4 bytes f77a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88eedc825c9832dcd421a0ebc4a15ffc"></a>

### [`004792cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004792cc.md) → [`0047930c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/0047930c.md) FUN_0047930c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00478c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c84.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00478cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478cc4.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047933c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004792cc.md#insn-0047933c) · [`00479374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004792cc.md#insn-00479374) · [`00479424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004792cc.md#insn-00479424)
- 新版 [`0047937c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/0047930c.md#insn-0047937c) · [`004793b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/0047930c.md#insn-004793b4) · [`00479464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/0047930c.md#insn-00479464)

~~~diff
- 0047933c ["INT_ADD", "register:40f0:8", ["const:47933c:8", "const:4:8"]]
- 0047933c ["CALL", null, ["callee:00c57f40:8"]]
+ 0047937c ["INT_ADD", "register:40f0:8", ["const:47937c:8", "const:4:8"]]
+ 0047937c ["CALL", null, ["callee:00c57f40:8"]]
- 0047933c bytes 017a1f94
+ 0047937c bytes f17a1f94
- 00479374 ["INT_ADD", "register:40f0:8", ["const:479374:8", "const:4:8"]]
- 00479374 ["CALL", null, ["callee:00c57e90:8"]]
+ 004793b4 ["INT_ADD", "register:40f0:8", ["const:4793b4:8", "const:4:8"]]
+ 004793b4 ["CALL", null, ["callee:00c57e90:8"]]
- 00479374 bytes c7791f94
+ 004793b4 bytes b77a1f94
- 00479424 ["INT_ADD", "register:40f0:8", ["const:479424:8", "const:4:8"]]
- 00479424 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00479464 ["INT_ADD", "register:40f0:8", ["const:479464:8", "const:4:8"]]
+ 00479464 ["CALL", null, ["callee:00c57eb0:8"]]
- 00479424 bytes a3791f94
+ 00479464 bytes 937a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-271f6ae7836dc134538bdb346e277d64"></a>

### [`00479458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479458.md) → [`00479498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479498.md) FUN_00479498

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00478c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c84.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00478cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478cc4.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004794c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479458.md#insn-004794c8) · [`00479500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479458.md#insn-00479500) · [`004795b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479458.md#insn-004795b0)
- 新版 [`00479508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479498.md#insn-00479508) · [`00479540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479498.md#insn-00479540) · [`004795f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479498.md#insn-004795f0)

~~~diff
- 004794c8 ["INT_ADD", "register:40f0:8", ["const:4794c8:8", "const:4:8"]]
- 004794c8 ["CALL", null, ["callee:00c57f40:8"]]
+ 00479508 ["INT_ADD", "register:40f0:8", ["const:479508:8", "const:4:8"]]
+ 00479508 ["CALL", null, ["callee:00c57f40:8"]]
- 004794c8 bytes 9e791f94
+ 00479508 bytes 8e7a1f94
- 00479500 ["INT_ADD", "register:40f0:8", ["const:479500:8", "const:4:8"]]
- 00479500 ["CALL", null, ["callee:00c57e90:8"]]
+ 00479540 ["INT_ADD", "register:40f0:8", ["const:479540:8", "const:4:8"]]
+ 00479540 ["CALL", null, ["callee:00c57e90:8"]]
- 00479500 bytes 64791f94
+ 00479540 bytes 547a1f94
- 004795b0 ["INT_ADD", "register:40f0:8", ["const:4795b0:8", "const:4:8"]]
- 004795b0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004795f0 ["INT_ADD", "register:40f0:8", ["const:4795f0:8", "const:4:8"]]
+ 004795f0 ["CALL", null, ["callee:00c57eb0:8"]]
- 004795b0 bytes 40791f94
+ 004795f0 bytes 307a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e081b2eb5a0c2e7377da75642b632e12"></a>

### [`004795e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004795e4.md) → [`00479624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479624.md) FUN_00479624

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`0054071c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`0054075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054075c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047964c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004795e4.md#insn-0047964c)
- 新版 [`0047968c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479624.md#insn-0047968c)

~~~diff
- 0047964c ["INT_ADD", "register:40f0:8", ["const:47964c:8", "const:4:8"]]
- 0047964c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0047968c ["INT_ADD", "register:40f0:8", ["const:47968c:8", "const:4:8"]]
+ 0047968c ["CALL", null, ["callee:00c57eb0:8"]]
- 0047964c bytes 19791f94
+ 0047968c bytes 097a1f94
~~~


<a id="compare-99c0992c852e3bdb8864d9ce94e32a79"></a>

### [`00479670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479670.md) → [`004796b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004796b0.md) FUN_004796b0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0053efd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053efd8.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0053f018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f018.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004796bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479670.md#insn-004796bc)
- 新版 [`004796fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004796b0.md#insn-004796fc)

~~~diff
- 004796bc ["INT_ADD", "register:40f0:8", ["const:4796bc:8", "const:4:8"]]
- 004796bc ["CALL", null, ["callee:00c57eb0:8"]]
+ 004796fc ["INT_ADD", "register:40f0:8", ["const:4796fc:8", "const:4:8"]]
+ 004796fc ["CALL", null, ["callee:00c57eb0:8"]]
- 004796bc bytes fd781f94
+ 004796fc bytes ed791f94
~~~


<a id="compare-8e706e3e45d96c8047f40842a29c75f7"></a>

### [`00479a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479a44.md) → [`00479a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479a84.md) FUN_00479a84

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00479a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479a44.md#insn-00479a60) · [`00479a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479a44.md#insn-00479a74) · [`00479a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479a44.md#insn-00479a94)
- 新版 [`00479aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479a84.md#insn-00479aa0) · [`00479ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479a84.md#insn-00479ab4) · [`00479ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479a84.md#insn-00479ad4)

~~~diff
- 00479a60 ["INT_ADD", "register:40f0:8", ["const:479a60:8", "const:4:8"]]
- 00479a60 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00479aa0 ["INT_ADD", "register:40f0:8", ["const:479aa0:8", "const:4:8"]]
+ 00479aa0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00479a60 bytes 14781f94
+ 00479aa0 bytes 04791f94
- 00479a74 ["INT_ADD", "register:40f0:8", ["const:479a74:8", "const:4:8"]]
- 00479a74 ["CALL", null, ["callee:00c53d00:8"]]
+ 00479ab4 ["INT_ADD", "register:40f0:8", ["const:479ab4:8", "const:4:8"]]
+ 00479ab4 ["CALL", null, ["callee:00c53d00:8"]]
- 00479a74 bytes 9b671f94
+ 00479ab4 bytes 93681f94
- 00479a94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00479a94 ["INT_ADD", "register:40f0:8", ["const:479a94:8", "const:4:8"]]
- 00479a94 ["CALLIND", null, ["register:0:8"]]
+ 00479ad4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00479ad4 ["INT_ADD", "register:40f0:8", ["const:479ad4:8", "const:4:8"]]
+ 00479ad4 ["CALLIND", null, ["register:0:8"]]
- 00479a94 bytes 00013fd6
+ 00479ad4 bytes 00013fd6
~~~


<a id="compare-83b68f216efad642507e463fde69f25e"></a>

### [`00479aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479aa8.md) → [`00479ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479ae8.md) FUN_00479ae8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0047377c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047377c.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00479ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479aa8.md#insn-00479ac4) · [`00479ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479aa8.md#insn-00479ad8) · [`00479aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479aa8.md#insn-00479aec)
- 新版 [`00479b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479ae8.md#insn-00479b04) · [`00479b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479ae8.md#insn-00479b18) · [`00479b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479ae8.md#insn-00479b2c)

~~~diff
- 00479ac4 ["INT_ADD", "register:40f0:8", ["const:479ac4:8", "const:4:8"]]
- 00479ac4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00479b04 ["INT_ADD", "register:40f0:8", ["const:479b04:8", "const:4:8"]]
+ 00479b04 ["CALL", null, ["callee:00c57eb0:8"]]
- 00479ac4 bytes fb771f94
+ 00479b04 bytes eb781f94
- 00479ad8 ["INT_ADD", "register:40f0:8", ["const:479ad8:8", "const:4:8"]]
- 00479ad8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00479b18 ["INT_ADD", "register:40f0:8", ["const:479b18:8", "const:4:8"]]
+ 00479b18 ["CALL", null, ["callee:00c53d00:8"]]
- 00479ad8 bytes 82671f94
+ 00479b18 bytes 7a681f94
- 00479aec ["COPY", "register:0:8", ["register:4040:8"]]
- 00479aec ["INT_ADD", "register:40f0:8", ["const:479aec:8", "const:4:8"]]
- 00479aec ["CALLIND", null, ["register:0:8"]]
+ 00479b2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00479b2c ["INT_ADD", "register:40f0:8", ["const:479b2c:8", "const:4:8"]]
+ 00479b2c ["CALLIND", null, ["register:0:8"]]
- 00479aec bytes 00013fd6
+ 00479b2c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1541cc0275da05534f263d8318102d76"></a>

### [`00479cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479cd8.md) → [`00479d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479d18.md) FUN_00479d18

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00479cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479cd8.md#insn-00479cf4) · [`00479d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479cd8.md#insn-00479d14)
- 新版 [`00479d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479d18.md#insn-00479d34) · [`00479d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479d18.md#insn-00479d54)

~~~diff
- 00479cf4 ["INT_ADD", "register:40f0:8", ["const:479cf4:8", "const:4:8"]]
- 00479cf4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00479d34 ["INT_ADD", "register:40f0:8", ["const:479d34:8", "const:4:8"]]
+ 00479d34 ["CALL", null, ["callee:00c53d00:8"]]
- 00479cf4 bytes fb661f94
+ 00479d34 bytes f3671f94
- 00479d14 ["COPY", "register:0:8", ["register:4040:8"]]
- 00479d14 ["INT_ADD", "register:40f0:8", ["const:479d14:8", "const:4:8"]]
- 00479d14 ["CALLIND", null, ["register:0:8"]]
+ 00479d54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00479d54 ["INT_ADD", "register:40f0:8", ["const:479d54:8", "const:4:8"]]
+ 00479d54 ["CALLIND", null, ["register:0:8"]]
- 00479d14 bytes 00013fd6
+ 00479d54 bytes 00013fd6
~~~


<a id="compare-c05b7ae73df3b88c8c52cb0020acbd6b"></a>

### [`00479f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479f0c.md) → [`00479f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479f4c.md) FUN_00479f4c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0047377c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047377c.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00479f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479f0c.md#insn-00479f28) · [`00479f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479f0c.md#insn-00479f48)
- 新版 [`00479f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479f4c.md#insn-00479f68) · [`00479f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479f4c.md#insn-00479f88)

~~~diff
- 00479f28 ["INT_ADD", "register:40f0:8", ["const:479f28:8", "const:4:8"]]
- 00479f28 ["CALL", null, ["callee:00c53d00:8"]]
+ 00479f68 ["INT_ADD", "register:40f0:8", ["const:479f68:8", "const:4:8"]]
+ 00479f68 ["CALL", null, ["callee:00c53d00:8"]]
- 00479f28 bytes 6e661f94
+ 00479f68 bytes 66671f94
- 00479f48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00479f48 ["INT_ADD", "register:40f0:8", ["const:479f48:8", "const:4:8"]]
- 00479f48 ["CALLIND", null, ["register:0:8"]]
+ 00479f88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00479f88 ["INT_ADD", "register:40f0:8", ["const:479f88:8", "const:4:8"]]
+ 00479f88 ["CALLIND", null, ["register:0:8"]]
- 00479f48 bytes 00013fd6
+ 00479f88 bytes 00013fd6
~~~


<a id="compare-9e78e06fe02126b5d42924b99d65bc65"></a>

### [`00479f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479f5c.md) → [`00479f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479f9c.md) FUN_00479f9c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0047377c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047377c.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00479f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479f5c.md#insn-00479f7c) · [`00479f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479f5c.md#insn-00479f90) · [`00479f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479f5c.md#insn-00479f98)
- 新版 [`00479fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479f9c.md#insn-00479fbc) · [`00479fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479f9c.md#insn-00479fd0) · [`00479fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479f9c.md#insn-00479fd8)

~~~diff
- 00479f7c ["INT_ADD", "register:40f0:8", ["const:479f7c:8", "const:4:8"]]
- 00479f7c ["CALL", null, ["callee:00c53d00:8"]]
+ 00479fbc ["INT_ADD", "register:40f0:8", ["const:479fbc:8", "const:4:8"]]
+ 00479fbc ["CALL", null, ["callee:00c53d00:8"]]
- 00479f7c bytes 59661f94
+ 00479fbc bytes 51671f94
- 00479f90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00479f90 ["INT_ADD", "register:40f0:8", ["const:479f90:8", "const:4:8"]]
- 00479f90 ["CALLIND", null, ["register:0:8"]]
+ 00479fd0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00479fd0 ["INT_ADD", "register:40f0:8", ["const:479fd0:8", "const:4:8"]]
+ 00479fd0 ["CALLIND", null, ["register:0:8"]]
- 00479f90 bytes 00013fd6
+ 00479fd0 bytes 00013fd6
- 00479f98 ["INT_ADD", "register:40f0:8", ["const:479f98:8", "const:4:8"]]
- 00479f98 ["CALL", null, ["callee:00c57e80:8"]]
+ 00479fd8 ["INT_ADD", "register:40f0:8", ["const:479fd8:8", "const:4:8"]]
+ 00479fd8 ["CALL", null, ["callee:00c57e80:8"]]
- 00479f98 bytes ba761f94
+ 00479fd8 bytes aa771f94
~~~


<a id="compare-72819c8c849f09b8d4415bba5e7f3094"></a>

### [`0047a528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a528.md) → [`0047a568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a568.md) FUN_0047a568

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047a544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a528.md#insn-0047a544) · [`0047a564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a528.md#insn-0047a564)
- 新版 [`0047a584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a568.md#insn-0047a584) · [`0047a5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a568.md#insn-0047a5a4)

~~~diff
- 0047a544 ["INT_ADD", "register:40f0:8", ["const:47a544:8", "const:4:8"]]
- 0047a544 ["CALL", null, ["callee:00c53d00:8"]]
+ 0047a584 ["INT_ADD", "register:40f0:8", ["const:47a584:8", "const:4:8"]]
+ 0047a584 ["CALL", null, ["callee:00c53d00:8"]]
- 0047a544 bytes e7641f94
+ 0047a584 bytes df651f94
- 0047a564 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047a564 ["INT_ADD", "register:40f0:8", ["const:47a564:8", "const:4:8"]]
- 0047a564 ["CALLIND", null, ["register:0:8"]]
+ 0047a5a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047a5a4 ["INT_ADD", "register:40f0:8", ["const:47a5a4:8", "const:4:8"]]
+ 0047a5a4 ["CALLIND", null, ["register:0:8"]]
- 0047a564 bytes 00013fd6
+ 0047a5a4 bytes 00013fd6
~~~


<a id="compare-769643d14fdabd1d697aee00a1c3966a"></a>

### [`0047a578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a578.md) → [`0047a5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a5b8.md) FUN_0047a5b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`00914c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00914/00914c94.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`00914e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00914/00914e30.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047a594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a578.md#insn-0047a594) · [`0047a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a578.md#insn-0047a5b4)
- 新版 [`0047a5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a5b8.md#insn-0047a5d4) · [`0047a5f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a5b8.md#insn-0047a5f4)

~~~diff
- 0047a594 ["INT_ADD", "register:40f0:8", ["const:47a594:8", "const:4:8"]]
- 0047a594 ["CALL", null, ["callee:00c53d00:8"]]
+ 0047a5d4 ["INT_ADD", "register:40f0:8", ["const:47a5d4:8", "const:4:8"]]
+ 0047a5d4 ["CALL", null, ["callee:00c53d00:8"]]
- 0047a594 bytes d3641f94
+ 0047a5d4 bytes cb651f94
- 0047a5b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047a5b4 ["INT_ADD", "register:40f0:8", ["const:47a5b4:8", "const:4:8"]]
- 0047a5b4 ["CALLIND", null, ["register:0:8"]]
+ 0047a5f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047a5f4 ["INT_ADD", "register:40f0:8", ["const:47a5f4:8", "const:4:8"]]
+ 0047a5f4 ["CALLIND", null, ["register:0:8"]]
- 0047a5b4 bytes 00013fd6
+ 0047a5f4 bytes 00013fd6
~~~


<a id="compare-1eee259ac91d9e44d7647e18a1c7f5f6"></a>

### [`0047a704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a704.md) → [`0047a744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a744.md) FUN_0047a744

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047a140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a140.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0047a180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a180.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047a720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a704.md#insn-0047a720) · [`0047a740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a704.md#insn-0047a740)
- 新版 [`0047a760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a744.md#insn-0047a760) · [`0047a780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a744.md#insn-0047a780)

~~~diff
- 0047a720 ["INT_ADD", "register:40f0:8", ["const:47a720:8", "const:4:8"]]
- 0047a720 ["CALL", null, ["callee:00c53d00:8"]]
+ 0047a760 ["INT_ADD", "register:40f0:8", ["const:47a760:8", "const:4:8"]]
+ 0047a760 ["CALL", null, ["callee:00c53d00:8"]]
- 0047a720 bytes 70641f94
+ 0047a760 bytes 68651f94
- 0047a740 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047a740 ["INT_ADD", "register:40f0:8", ["const:47a740:8", "const:4:8"]]
- 0047a740 ["CALLIND", null, ["register:0:8"]]
+ 0047a780 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047a780 ["INT_ADD", "register:40f0:8", ["const:47a780:8", "const:4:8"]]
+ 0047a780 ["CALLIND", null, ["register:0:8"]]
- 0047a740 bytes 00013fd6
+ 0047a780 bytes 00013fd6
~~~


<a id="compare-c8196841eac3528b797982ef1aea79fa"></a>

### [`0047a754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a754.md) → [`0047a794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a794.md) FUN_0047a794

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047a140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a140.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0047a180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a180.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047a774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a754.md#insn-0047a774) · [`0047a788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a754.md#insn-0047a788) · [`0047a790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a754.md#insn-0047a790)
- 新版 [`0047a7b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a794.md#insn-0047a7b4) · [`0047a7c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a794.md#insn-0047a7c8) · [`0047a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a794.md#insn-0047a7d0)

~~~diff
- 0047a774 ["INT_ADD", "register:40f0:8", ["const:47a774:8", "const:4:8"]]
- 0047a774 ["CALL", null, ["callee:00c53d00:8"]]
+ 0047a7b4 ["INT_ADD", "register:40f0:8", ["const:47a7b4:8", "const:4:8"]]
+ 0047a7b4 ["CALL", null, ["callee:00c53d00:8"]]
- 0047a774 bytes 5b641f94
+ 0047a7b4 bytes 53651f94
- 0047a788 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047a788 ["INT_ADD", "register:40f0:8", ["const:47a788:8", "const:4:8"]]
- 0047a788 ["CALLIND", null, ["register:0:8"]]
+ 0047a7c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047a7c8 ["INT_ADD", "register:40f0:8", ["const:47a7c8:8", "const:4:8"]]
+ 0047a7c8 ["CALLIND", null, ["register:0:8"]]
- 0047a788 bytes 00013fd6
+ 0047a7c8 bytes 00013fd6
- 0047a790 ["INT_ADD", "register:40f0:8", ["const:47a790:8", "const:4:8"]]
- 0047a790 ["CALL", null, ["callee:00c57e80:8"]]
+ 0047a7d0 ["INT_ADD", "register:40f0:8", ["const:47a7d0:8", "const:4:8"]]
+ 0047a7d0 ["CALL", null, ["callee:00c57e80:8"]]
- 0047a790 bytes bc741f94
+ 0047a7d0 bytes ac751f94
~~~


<a id="compare-15eddfb86cf760b21d3d8e609b3ba5b4"></a>

### [`0047ad64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047ad64.md) → [`0047ada4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047ada4.md) FUN_0047ada4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047fa0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fa0c.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047fa4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fa4c.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047ad84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047ad64.md#insn-0047ad84) · [`0047ad90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047ad64.md#insn-0047ad90) · [`0047ada4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047ad64.md#insn-0047ada4)
- 新版 [`0047adc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047ada4.md#insn-0047adc4) · [`0047add0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047ada4.md#insn-0047add0) · [`0047ade4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047ada4.md#insn-0047ade4)

~~~diff
- 0047ad84 ["INT_ADD", "register:40f0:8", ["const:47ad84:8", "const:4:8"]]
- 0047ad84 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0047adc4 ["INT_ADD", "register:40f0:8", ["const:47adc4:8", "const:4:8"]]
+ 0047adc4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0047ad84 bytes 4b731f94
+ 0047adc4 bytes 3b741f94
- 0047ad90 ["INT_ADD", "register:40f0:8", ["const:47ad90:8", "const:4:8"]]
- 0047ad90 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0047add0 ["INT_ADD", "register:40f0:8", ["const:47add0:8", "const:4:8"]]
+ 0047add0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0047ad90 bytes 48731f94
+ 0047add0 bytes 38741f94
- 0047ada4 ["INT_ADD", "register:40f0:8", ["const:47ada4:8", "const:4:8"]]
- 0047ada4 ["CALL", null, ["callee:00c53d00:8"]]
+ 0047ade4 ["INT_ADD", "register:40f0:8", ["const:47ade4:8", "const:4:8"]]
+ 0047ade4 ["CALL", null, ["callee:00c53d00:8"]]
- 0047ada4 bytes cf621f94
+ 0047ade4 bytes c7631f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1d79b5335809ce6e4bfd4a52bb851e5"></a>

### [`0047b4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b4cc.md) → [`0047b50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b50c.md) FUN_0047b50c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0047aed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047aed0.md) [`007c7938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7938.md) [`0080bc98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080bc98.md) [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 7件 [`0047d574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d574.md) [`0047d678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d678.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 4件 [`0047af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047af10.md) [`007c7978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7978.md) [`0080bcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080bcd8.md) [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 7件 [`0047d5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d5b4.md) [`0047d6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d6b8.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047b578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b4cc.md#insn-0047b578) · [`0047b5ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b4cc.md#insn-0047b5ac) · [`0047b610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b4cc.md#insn-0047b610)
- 新版 [`0047b5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b50c.md#insn-0047b5b8) · [`0047b5ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b50c.md#insn-0047b5ec) · [`0047b650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b50c.md#insn-0047b650)

~~~diff
- 0047b578 ["INT_ADD", "register:40f0:8", ["const:47b578:8", "const:4:8"]]
- 0047b578 ["CALL", null, ["callee:0047d5b4:8"]]
+ 0047b5b8 ["INT_ADD", "register:40f0:8", ["const:47b5b8:8", "const:4:8"]]
+ 0047b5b8 ["CALL", null, ["callee:0047d5b4:8"]]
- 0047b578 bytes ff070094
+ 0047b5b8 bytes ff070094
- 0047b5ac ["INT_ADD", "register:40f0:8", ["const:47b5ac:8", "const:4:8"]]
- 0047b5ac ["CALL", null, ["callee:00c57f40:8"]]
+ 0047b5ec ["INT_ADD", "register:40f0:8", ["const:47b5ec:8", "const:4:8"]]
+ 0047b5ec ["CALL", null, ["callee:00c57f40:8"]]
- 0047b5ac bytes 65711f94
+ 0047b5ec bytes 55721f94
- 0047b610 ["INT_ADD", "register:40f0:8", ["const:47b610:8", "const:4:8"]]
- 0047b610 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0047b650 ["INT_ADD", "register:40f0:8", ["const:47b650:8", "const:4:8"]]
+ 0047b650 ["CALL", null, ["callee:00c57eb0:8"]]
- 0047b610 bytes 28711f94
+ 0047b650 bytes 18721f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9d08a5ae5d71a927bfdbabf39be418a"></a>

### [`0047b78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b78c.md) → [`0047b7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b7cc.md) FUN_0047b7cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b2bffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bffc.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00b2c424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c424.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047b7c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b78c.md#insn-0047b7c4) · [`0047b7d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b78c.md#insn-0047b7d8) · [`0047b7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b78c.md#insn-0047b7e0)
- 新版 [`0047b804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b7cc.md#insn-0047b804) · [`0047b818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b7cc.md#insn-0047b818) · [`0047b820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b7cc.md#insn-0047b820)

~~~diff
- 0047b7c4 ["INT_ADD", "register:40f0:8", ["const:47b7c4:8", "const:4:8"]]
- 0047b7c4 ["CALL", null, ["callee:00c53d00:8"]]
+ 0047b804 ["INT_ADD", "register:40f0:8", ["const:47b804:8", "const:4:8"]]
+ 0047b804 ["CALL", null, ["callee:00c53d00:8"]]
- 0047b7c4 bytes 47601f94
+ 0047b804 bytes 3f611f94
- 0047b7d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047b7d8 ["INT_ADD", "register:40f0:8", ["const:47b7d8:8", "const:4:8"]]
- 0047b7d8 ["CALLIND", null, ["register:0:8"]]
+ 0047b818 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047b818 ["INT_ADD", "register:40f0:8", ["const:47b818:8", "const:4:8"]]
+ 0047b818 ["CALLIND", null, ["register:0:8"]]
- 0047b7d8 bytes 00013fd6
+ 0047b818 bytes 00013fd6
- 0047b7e0 ["INT_ADD", "register:40f0:8", ["const:47b7e0:8", "const:4:8"]]
- 0047b7e0 ["CALL", null, ["callee:00c57e80:8"]]
+ 0047b820 ["INT_ADD", "register:40f0:8", ["const:47b820:8", "const:4:8"]]
+ 0047b820 ["CALL", null, ["callee:00c57e80:8"]]
- 0047b7e0 bytes a8701f94
+ 0047b820 bytes 98711f94
~~~


<a id="compare-bc8f1f36c7763b5156dfdf44a2a3fa09"></a>

### [`0047c928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c928.md) → [`0047c968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c968.md) FUN_0047c968

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 27件 [`0047c008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c008.md) [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`0061300c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/0061300c.md) [`006312b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00631/006312b4.md) [`00632cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00632/00632cd4.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0047d820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d820.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 27件 [`0047c048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c048.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`0061304c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00613/0061304c.md) [`006312f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00631/006312f4.md) [`00632d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00632/00632d14.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0047d860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d860.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047c97c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c928.md#insn-0047c97c) · [`0047c98c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c928.md#insn-0047c98c) · [`0047c9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c928.md#insn-0047c9bc)
- 新版 [`0047c9bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c968.md#insn-0047c9bc) · [`0047c9cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c968.md#insn-0047c9cc) · [`0047c9fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c968.md#insn-0047c9fc)

~~~diff
- 0047c97c ["INT_ADD", "register:40f0:8", ["const:47c97c:8", "const:4:8"]]
- 0047c97c ["CALL", null, ["callee:0043bb20:8"]]
+ 0047c9bc ["INT_ADD", "register:40f0:8", ["const:47c9bc:8", "const:4:8"]]
+ 0047c9bc ["CALL", null, ["callee:0043bb20:8"]]
- 0047c97c bytes 59fcfe97
+ 0047c9bc bytes 59fcfe97
- 0047c98c ["INT_ADD", "register:40f0:8", ["const:47c98c:8", "const:4:8"]]
- 0047c98c ["CALL", null, ["callee:0043bb20:8"]]
+ 0047c9cc ["INT_ADD", "register:40f0:8", ["const:47c9cc:8", "const:4:8"]]
+ 0047c9cc ["CALL", null, ["callee:0043bb20:8"]]
- 0047c98c bytes 55fcfe97
+ 0047c9cc bytes 55fcfe97
- 0047c9bc ["INT_ADD", "register:40f0:8", ["const:47c9bc:8", "const:4:8"]]
- 0047c9bc ["CALL", null, ["callee:0047d860:8"]]
+ 0047c9fc ["INT_ADD", "register:40f0:8", ["const:47c9fc:8", "const:4:8"]]
+ 0047c9fc ["CALL", null, ["callee:0047d860:8"]]
- 0047c9bc bytes 99030094
+ 0047c9fc bytes 99030094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a216ed1ab31c9beff0ec21aa054f466f"></a>

### [`0047ca4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047ca4c.md) → [`0047ca8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ca8c.md) FUN_0047ca8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 27件 [`0047c008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c008.md) [`005e6dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e6dbc.md) [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`0064e33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064e33c.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 27件 [`0047c048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c048.md) [`005e6dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e6/005e6dfc.md) [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`0064e37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064e37c.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047cb7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047ca4c.md#insn-0047cb7c) · [`0047cb9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047ca4c.md#insn-0047cb9c) · [`0047cbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047ca4c.md#insn-0047cbb0)
- 新版 [`0047cbbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ca8c.md#insn-0047cbbc) · [`0047cbdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ca8c.md#insn-0047cbdc) · [`0047cbf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ca8c.md#insn-0047cbf0)

~~~diff
- 0047cb7c ["COPY", "register:0:8", ["register:4040:8"]]
- 0047cb7c ["INT_ADD", "register:40f0:8", ["const:47cb7c:8", "const:4:8"]]
- 0047cb7c ["CALLIND", null, ["register:0:8"]]
+ 0047cbbc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047cbbc ["INT_ADD", "register:40f0:8", ["const:47cbbc:8", "const:4:8"]]
+ 0047cbbc ["CALLIND", null, ["register:0:8"]]
- 0047cb7c bytes 00013fd6
+ 0047cbbc bytes 00013fd6
- 0047cb9c ["INT_ADD", "register:40f0:8", ["const:47cb9c:8", "const:4:8"]]
- 0047cb9c ["CALL", null, ["callee:00c53d00:8"]]
+ 0047cbdc ["INT_ADD", "register:40f0:8", ["const:47cbdc:8", "const:4:8"]]
+ 0047cbdc ["CALL", null, ["callee:00c53d00:8"]]
- 0047cb9c bytes 515b1f94
+ 0047cbdc bytes 495c1f94
- 0047cbb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047cbb0 ["INT_ADD", "register:40f0:8", ["const:47cbb0:8", "const:4:8"]]
- 0047cbb0 ["CALLIND", null, ["register:0:8"]]
+ 0047cbf0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047cbf0 ["INT_ADD", "register:40f0:8", ["const:47cbf0:8", "const:4:8"]]
+ 0047cbf0 ["CALLIND", null, ["register:0:8"]]
- 0047cbb0 bytes 00013fd6
+ 0047cbf0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee7fcc2675a3754c3cc9308751d7eab1"></a>

### [`0047cce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cce8.md) → [`0047cd28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cd28.md) FUN_0047cd28

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047c008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c008.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0047c048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c048.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047cd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cce8.md#insn-0047cd14) · [`0047cd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cce8.md#insn-0047cd28) · [`0047cd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cce8.md#insn-0047cd30)
- 新版 [`0047cd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cd28.md#insn-0047cd54) · [`0047cd68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cd28.md#insn-0047cd68) · [`0047cd70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cd28.md#insn-0047cd70)

~~~diff
- 0047cd14 ["INT_ADD", "register:40f0:8", ["const:47cd14:8", "const:4:8"]]
- 0047cd14 ["CALL", null, ["callee:00c53d00:8"]]
+ 0047cd54 ["INT_ADD", "register:40f0:8", ["const:47cd54:8", "const:4:8"]]
+ 0047cd54 ["CALL", null, ["callee:00c53d00:8"]]
- 0047cd14 bytes f35a1f94
+ 0047cd54 bytes eb5b1f94
- 0047cd28 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047cd28 ["INT_ADD", "register:40f0:8", ["const:47cd28:8", "const:4:8"]]
- 0047cd28 ["CALLIND", null, ["register:0:8"]]
+ 0047cd68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047cd68 ["INT_ADD", "register:40f0:8", ["const:47cd68:8", "const:4:8"]]
+ 0047cd68 ["CALLIND", null, ["register:0:8"]]
- 0047cd28 bytes 00013fd6
+ 0047cd68 bytes 00013fd6
- 0047cd30 ["INT_ADD", "register:40f0:8", ["const:47cd30:8", "const:4:8"]]
- 0047cd30 ["CALL", null, ["callee:00c57e80:8"]]
+ 0047cd70 ["INT_ADD", "register:40f0:8", ["const:47cd70:8", "const:4:8"]]
+ 0047cd70 ["CALL", null, ["callee:00c57e80:8"]]
- 0047cd30 bytes 546b1f94
+ 0047cd70 bytes 446c1f94
~~~


<a id="compare-4790d269248224c799f940a1dc89b5c1"></a>

### [`0047cd44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd44.md) → [`0047cd84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cd84.md) FUN_0047cd84

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047c008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c008.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0047c048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c048.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047cd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd44.md#insn-0047cd60) · [`0047cd80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd44.md#insn-0047cd80)
- 新版 [`0047cda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cd84.md#insn-0047cda0) · [`0047cdc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cd84.md#insn-0047cdc0)

~~~diff
- 0047cd60 ["INT_ADD", "register:40f0:8", ["const:47cd60:8", "const:4:8"]]
- 0047cd60 ["CALL", null, ["callee:00c53d00:8"]]
+ 0047cda0 ["INT_ADD", "register:40f0:8", ["const:47cda0:8", "const:4:8"]]
+ 0047cda0 ["CALL", null, ["callee:00c53d00:8"]]
- 0047cd60 bytes e05a1f94
+ 0047cda0 bytes d85b1f94
- 0047cd80 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047cd80 ["INT_ADD", "register:40f0:8", ["const:47cd80:8", "const:4:8"]]
- 0047cd80 ["CALLIND", null, ["register:0:8"]]
+ 0047cdc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047cdc0 ["INT_ADD", "register:40f0:8", ["const:47cdc0:8", "const:4:8"]]
+ 0047cdc0 ["CALLIND", null, ["register:0:8"]]
- 0047cd80 bytes 00013fd6
+ 0047cdc0 bytes 00013fd6
~~~


<a id="compare-3952b0919c2f24aa78ae91dae24051f7"></a>

### [`0047cd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd9c.md) → [`0047cddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cddc.md) FUN_0047cddc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`005f1a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f1/005f1a94.md) [`005f20cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f2/005f20cc.md) [`005f2300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f2/005f2300.md) [`005f2758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f2/005f2758.md) [`005f87e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f8/005f87e0.md) · 呼出先 2件 [`0047c008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c008.md) [`005e0d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0d28.md)
- 新版 呼出元 9件 [`005f1ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f1/005f1ad4.md) [`005f210c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f2/005f210c.md) [`005f2340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f2/005f2340.md) [`005f2798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f2/005f2798.md) [`005f8820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f8/005f8820.md) · 呼出先 2件 [`0047c048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c048.md) [`005e0d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0d68.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd9c.md#insn-0047cdb0)
- 新版 [`0047cdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cddc.md#insn-0047cdf0)

~~~diff
- 0047cdb0 ["INT_ADD", "register:40f0:8", ["const:47cdb0:8", "const:4:8"]]
- 0047cdb0 ["CALL", null, ["callee:005e0d68:8"]]
+ 0047cdf0 ["INT_ADD", "register:40f0:8", ["const:47cdf0:8", "const:4:8"]]
+ 0047cdf0 ["CALL", null, ["callee:005e0d68:8"]]
- 0047cdb0 bytes de8f0594
+ 0047cdf0 bytes de8f0594
~~~


<a id="compare-b317893aca9d636742724c0eb9a05ac7"></a>

### [`0047cde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cde8.md) → [`0047ce28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ce28.md) FUN_0047ce28

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`006166dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/006166dc.md) [`006ff2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff2d8.md) [`007fd33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd33c.md) [`008545cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00854/008545cc.md) [`00891f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891f1c.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 6件 [`0061671c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/0061671c.md) [`006ff318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff318.md) [`007fd37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd37c.md) [`0085460c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00854/0085460c.md) [`00891f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891f60.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047ce18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cde8.md#insn-0047ce18) · [`0047ce70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cde8.md#insn-0047ce70) · [`0047ce90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cde8.md#insn-0047ce90)
- 新版 [`0047ce58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ce28.md#insn-0047ce58) · [`0047ceb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ce28.md#insn-0047ceb0) · [`0047ced0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ce28.md#insn-0047ced0)

~~~diff
- 0047ce18 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047ce18 ["INT_ADD", "register:40f0:8", ["const:47ce18:8", "const:4:8"]]
- 0047ce18 ["CALLIND", null, ["register:0:8"]]
+ 0047ce58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047ce58 ["INT_ADD", "register:40f0:8", ["const:47ce58:8", "const:4:8"]]
+ 0047ce58 ["CALLIND", null, ["register:0:8"]]
- 0047ce18 bytes 00013fd6
+ 0047ce58 bytes 00013fd6
- 0047ce70 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047ce70 ["INT_ADD", "register:40f0:8", ["const:47ce70:8", "const:4:8"]]
- 0047ce70 ["CALLIND", null, ["register:0:8"]]
+ 0047ceb0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047ceb0 ["INT_ADD", "register:40f0:8", ["const:47ceb0:8", "const:4:8"]]
+ 0047ceb0 ["CALLIND", null, ["register:0:8"]]
- 0047ce70 bytes 00013fd6
+ 0047ceb0 bytes 00013fd6
- 0047ce90 ["INT_ADD", "register:40f0:8", ["const:47ce90:8", "const:4:8"]]
- 0047ce90 ["CALL", null, ["callee:00c53d00:8"]]
+ 0047ced0 ["INT_ADD", "register:40f0:8", ["const:47ced0:8", "const:4:8"]]
+ 0047ced0 ["CALL", null, ["callee:00c53d00:8"]]
- 0047ce90 bytes 945a1f94
+ 0047ced0 bytes 8c5b1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b36b5da622e0308602b4fdd736836e0"></a>

### [`0047cec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cec8.md) → [`0047cf08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cf08.md) FUN_0047cf08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`005ba758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba758.md) [`00616910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616910.md) [`006ff600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff600.md) [`007fd5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd5b0.md) [`00853c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853c38.md) · 呼出先 1件 [`0047c008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c008.md)
- 新版 呼出元 7件 [`005ba798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005ba798.md) [`00616950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616950.md) [`006ff640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff640.md) [`007fd5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd5f0.md) [`00853c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853c78.md) · 呼出先 1件 [`0047c048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c048.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047cf30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cec8.md#insn-0047cf30)
- 新版 [`0047cf70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cf08.md#insn-0047cf70)

~~~diff
- 0047cf30 ["INT_ADD", "register:40f0:8", ["const:47cf30:8", "const:4:8"]]
- 0047cf30 ["CALL", null, ["callee:0047c048:8"]]
+ 0047cf70 ["INT_ADD", "register:40f0:8", ["const:47cf70:8", "const:4:8"]]
+ 0047cf70 ["CALL", null, ["callee:0047c048:8"]]
- 0047cf30 bytes 36fcff97
+ 0047cf70 bytes 36fcff97
~~~


<a id="compare-0e75e03d91d0077786fadcfd88dd60c7"></a>

### [`0047cf78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cf78.md) → [`0047cfb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cfb8.md) FUN_0047cfb8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`008803fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/008803fc.md) [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 3件 [`0088043c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/0088043c.md) [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047cfec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cf78.md#insn-0047cfec) · [`0047d00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cf78.md#insn-0047d00c) · [`0047d020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cf78.md#insn-0047d020)
- 新版 [`0047d02c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cfb8.md#insn-0047d02c) · [`0047d04c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cfb8.md#insn-0047d04c) · [`0047d060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cfb8.md#insn-0047d060)

~~~diff
- 0047cfec ["COPY", "register:0:8", ["register:4040:8"]]
- 0047cfec ["INT_ADD", "register:40f0:8", ["const:47cfec:8", "const:4:8"]]
- 0047cfec ["CALLIND", null, ["register:0:8"]]
+ 0047d02c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047d02c ["INT_ADD", "register:40f0:8", ["const:47d02c:8", "const:4:8"]]
+ 0047d02c ["CALLIND", null, ["register:0:8"]]
- 0047cfec bytes 00013fd6
+ 0047d02c bytes 00013fd6
- 0047d00c ["INT_ADD", "register:40f0:8", ["const:47d00c:8", "const:4:8"]]
- 0047d00c ["CALL", null, ["callee:00c53d00:8"]]
+ 0047d04c ["INT_ADD", "register:40f0:8", ["const:47d04c:8", "const:4:8"]]
+ 0047d04c ["CALL", null, ["callee:00c53d00:8"]]
- 0047d00c bytes 355a1f94
+ 0047d04c bytes 2d5b1f94
- 0047d020 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047d020 ["INT_ADD", "register:40f0:8", ["const:47d020:8", "const:4:8"]]
- 0047d020 ["CALLIND", null, ["register:0:8"]]
+ 0047d060 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047d060 ["INT_ADD", "register:40f0:8", ["const:47d060:8", "const:4:8"]]
+ 0047d060 ["CALLIND", null, ["register:0:8"]]
- 0047d020 bytes 00013fd6
+ 0047d060 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f406ea542a6805fcb71202be5c0b1019"></a>

### [`0047d0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d0dc.md) → [`0047d11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d11c.md) FUN_0047d11c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`009334e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/009334e8.md) [`00933dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933dbc.md) [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 0件 
- 新版 呼出元 3件 [`00933684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933684.md) [`00933f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933f58.md) [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047d160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d0dc.md#insn-0047d160)
- 新版 [`0047d1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d11c.md#insn-0047d1a0)

~~~diff
- 0047d160 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047d160 ["INT_ADD", "register:40f0:8", ["const:47d160:8", "const:4:8"]]
- 0047d160 ["CALLIND", null, ["register:0:8"]]
+ 0047d1a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047d1a0 ["INT_ADD", "register:40f0:8", ["const:47d1a0:8", "const:4:8"]]
+ 0047d1a0 ["CALLIND", null, ["register:0:8"]]
- 0047d160 bytes 00013fd6
+ 0047d1a0 bytes 00013fd6
~~~


<a id="compare-42014d4138c12a9bd7ef322dc59b6a10"></a>

### [`0047d23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d23c.md) → [`0047d27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d27c.md) FUN_0047d27c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047aed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047aed0.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0047d3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d3c4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`0047af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047af10.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0047d404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d404.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047d2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d23c.md#insn-0047d2b4) · [`0047d2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d23c.md#insn-0047d2d8) · [`0047d304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d23c.md#insn-0047d304)
- 新版 [`0047d2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d27c.md#insn-0047d2f4) · [`0047d318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d27c.md#insn-0047d318) · [`0047d344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d27c.md#insn-0047d344)

~~~diff
- 0047d2b4 ["INT_ADD", "register:40f0:8", ["const:47d2b4:8", "const:4:8"]]
- 0047d2b4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0047d2f4 ["INT_ADD", "register:40f0:8", ["const:47d2f4:8", "const:4:8"]]
+ 0047d2f4 ["CALL", null, ["callee:00c57e90:8"]]
- 0047d2b4 bytes f7691f94
+ 0047d2f4 bytes e76a1f94
- 0047d2d8 ["INT_ADD", "register:40f0:8", ["const:47d2d8:8", "const:4:8"]]
- 0047d2d8 ["CALL", null, ["callee:00c58090:8"]]
+ 0047d318 ["INT_ADD", "register:40f0:8", ["const:47d318:8", "const:4:8"]]
+ 0047d318 ["CALL", null, ["callee:00c58090:8"]]
- 0047d2d8 bytes 6e6a1f94
+ 0047d318 bytes 5e6b1f94
- 0047d304 ["INT_ADD", "register:40f0:8", ["const:47d304:8", "const:4:8"]]
- 0047d304 ["CALL", null, ["callee:00c58090:8"]]
+ 0047d344 ["INT_ADD", "register:40f0:8", ["const:47d344:8", "const:4:8"]]
+ 0047d344 ["CALL", null, ["callee:00c58090:8"]]
- 0047d304 bytes 636a1f94
+ 0047d344 bytes 536b1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d8dc1070beefec02c1b1fb792470a89"></a>

### [`0047d3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d3d8.md) → [`0047d418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d418.md) FUN_0047d418

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047aed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047aed0.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0047d560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d560.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`0047af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047af10.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0047d5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d5a0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d3d8.md#insn-0047d450) · [`0047d474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d3d8.md#insn-0047d474) · [`0047d4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d3d8.md#insn-0047d4a0)
- 新版 [`0047d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d418.md#insn-0047d490) · [`0047d4b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d418.md#insn-0047d4b4) · [`0047d4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d418.md#insn-0047d4e0)

~~~diff
- 0047d450 ["INT_ADD", "register:40f0:8", ["const:47d450:8", "const:4:8"]]
- 0047d450 ["CALL", null, ["callee:00c57e90:8"]]
+ 0047d490 ["INT_ADD", "register:40f0:8", ["const:47d490:8", "const:4:8"]]
+ 0047d490 ["CALL", null, ["callee:00c57e90:8"]]
- 0047d450 bytes 90691f94
+ 0047d490 bytes 806a1f94
- 0047d474 ["INT_ADD", "register:40f0:8", ["const:47d474:8", "const:4:8"]]
- 0047d474 ["CALL", null, ["callee:00c58090:8"]]
+ 0047d4b4 ["INT_ADD", "register:40f0:8", ["const:47d4b4:8", "const:4:8"]]
+ 0047d4b4 ["CALL", null, ["callee:00c58090:8"]]
- 0047d474 bytes 076a1f94
+ 0047d4b4 bytes f76a1f94
- 0047d4a0 ["INT_ADD", "register:40f0:8", ["const:47d4a0:8", "const:4:8"]]
- 0047d4a0 ["CALL", null, ["callee:00c58090:8"]]
+ 0047d4e0 ["INT_ADD", "register:40f0:8", ["const:47d4e0:8", "const:4:8"]]
+ 0047d4e0 ["CALL", null, ["callee:00c58090:8"]]
- 0047d4a0 bytes fc691f94
+ 0047d4e0 bytes ec6a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-984f47486fa0abb89bc81f0de04585b2"></a>

### [`0047d574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d574.md) → [`0047d5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d5b4.md) FUN_0047d5b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0047b4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b4cc.md) [`0049b460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b460.md) [`0049ec64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ec64.md) [`0080f0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080f/0080f0e8.md) [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 3件 [`0047d678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d678.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 5件 [`0047b50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b50c.md) [`0049b4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b4a0.md) [`0049eca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049eca4.md) [`0080f128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080f128.md) [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 3件 [`0047d6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d6b8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047d5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d574.md#insn-0047d5a4) · [`0047d674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d574.md#insn-0047d674)
- 新版 [`0047d5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d5b4.md#insn-0047d5e4) · [`0047d6b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d5b4.md#insn-0047d6b4)

~~~diff
- 0047d5a4 ["INT_ADD", "register:40f0:8", ["const:47d5a4:8", "const:4:8"]]
- 0047d5a4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0047d5e4 ["INT_ADD", "register:40f0:8", ["const:47d5e4:8", "const:4:8"]]
+ 0047d5e4 ["CALL", null, ["callee:00c57e90:8"]]
- 0047d5a4 bytes 3b691f94
+ 0047d5e4 bytes 2b6a1f94
- 0047d674 ["INT_ADD", "register:40f0:8", ["const:47d674:8", "const:4:8"]]
- 0047d674 ["CALL", null, ["callee:0047d6b8:8"]]
+ 0047d6b4 ["INT_ADD", "register:40f0:8", ["const:47d6b4:8", "const:4:8"]]
+ 0047d6b4 ["CALL", null, ["callee:0047d6b8:8"]]
- 0047d674 bytes 01000094
+ 0047d6b4 bytes 01000094
~~~


<a id="compare-a69e62440f5968b31b0ec8628df71ef6"></a>

### [`0047d6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d6e4.md) → [`0047d724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d724.md) FUN_0047d724

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047bda0.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0047bde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047bde0.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047d73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d6e4.md#insn-0047d73c) · [`0047d758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d6e4.md#insn-0047d758) · [`0047d76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d6e4.md#insn-0047d76c)
- 新版 [`0047d77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d724.md#insn-0047d77c) · [`0047d798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d724.md#insn-0047d798) · [`0047d7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d724.md#insn-0047d7ac)

~~~diff
- 0047d73c ["COPY", "register:0:8", ["register:4040:8"]]
- 0047d73c ["INT_ADD", "register:40f0:8", ["const:47d73c:8", "const:4:8"]]
- 0047d73c ["CALLIND", null, ["register:0:8"]]
+ 0047d77c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047d77c ["INT_ADD", "register:40f0:8", ["const:47d77c:8", "const:4:8"]]
+ 0047d77c ["CALLIND", null, ["register:0:8"]]
- 0047d73c bytes 00013fd6
+ 0047d77c bytes 00013fd6
- 0047d758 ["INT_ADD", "register:40f0:8", ["const:47d758:8", "const:4:8"]]
- 0047d758 ["CALL", null, ["callee:00c53d00:8"]]
+ 0047d798 ["INT_ADD", "register:40f0:8", ["const:47d798:8", "const:4:8"]]
+ 0047d798 ["CALL", null, ["callee:00c53d00:8"]]
- 0047d758 bytes 62581f94
+ 0047d798 bytes 5a591f94
- 0047d76c ["COPY", "register:0:8", ["register:4040:8"]]
- 0047d76c ["INT_ADD", "register:40f0:8", ["const:47d76c:8", "const:4:8"]]
- 0047d76c ["CALLIND", null, ["register:0:8"]]
+ 0047d7ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047d7ac ["INT_ADD", "register:40f0:8", ["const:47d7ac:8", "const:4:8"]]
+ 0047d7ac ["CALLIND", null, ["register:0:8"]]
- 0047d76c bytes 00013fd6
+ 0047d7ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a657c624ae5587f22946d208a0d482d"></a>

### [`0047eca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047eca4.md) → [`0047ece4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ece4.md) FUN_0047ece4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047f694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f694.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c580e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047f6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f6d4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c584e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047ecd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047eca4.md#insn-0047ecd0) · [`0047ece8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047eca4.md#insn-0047ece8) · [`0047ecf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047eca4.md#insn-0047ecf0)
- 新版 [`0047ed10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ece4.md#insn-0047ed10) · [`0047ed28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ece4.md#insn-0047ed28) · [`0047ed30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ece4.md#insn-0047ed30)

~~~diff
- 0047ecd0 ["INT_ADD", "register:40f0:8", ["const:47ecd0:8", "const:4:8"]]
- 0047ecd0 ["CALL", null, ["callee:0047f6d4:8"]]
+ 0047ed10 ["INT_ADD", "register:40f0:8", ["const:47ed10:8", "const:4:8"]]
+ 0047ed10 ["CALL", null, ["callee:0047f6d4:8"]]
- 0047ecd0 bytes 71020094
+ 0047ed10 bytes 71020094
- 0047ece8 ["INT_ADD", "register:40f0:8", ["const:47ece8:8", "const:4:8"]]
- 0047ece8 ["CALL", null, ["callee:00c584e0:8"]]
+ 0047ed28 ["INT_ADD", "register:40f0:8", ["const:47ed28:8", "const:4:8"]]
+ 0047ed28 ["CALL", null, ["callee:00c584e0:8"]]
- 0047ece8 bytes fe641f94
+ 0047ed28 bytes ee651f94
- 0047ecf0 ["INT_ADD", "register:40f0:8", ["const:47ecf0:8", "const:4:8"]]
- 0047ecf0 ["CALL", null, ["callee:00c584e0:8"]]
+ 0047ed30 ["INT_ADD", "register:40f0:8", ["const:47ed30:8", "const:4:8"]]
+ 0047ed30 ["CALL", null, ["callee:00c584e0:8"]]
- 0047ecf0 bytes fc641f94
+ 0047ed30 bytes ec651f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-246a361b1650c018ce0d539b95283f1a"></a>

### [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) → [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) FUN_0047edb4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 207件 [`0047e1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e1cc.md) [`005ba2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba2d0.md) [`005c421c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c421c.md) [`005cc174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc174.md) [`005e1b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1b78.md) · 呼出先 4件 [`0047edc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047edc0.md) [`0047ee70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ee70.md) [`00497c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497c3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 213件 [`0047e20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e20c.md) [`005ba310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005ba310.md) [`005c425c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c4/005c425c.md) [`005cc1b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cc/005cc1b4.md) [`005e1bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1bb8.md) · 呼出先 4件 [`0047ee00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ee00.md) [`0047eeb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047eeb0.md) [`00497c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497c7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047ed94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md#insn-0047ed94) · [`0047ed9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md#insn-0047ed9c) · [`0047eda8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md#insn-0047eda8)
- 新版 [`0047edd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md#insn-0047edd4) · [`0047eddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md#insn-0047eddc) · [`0047ede8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md#insn-0047ede8)

~~~diff
- 0047ed94 ["INT_ADD", "register:40f0:8", ["const:47ed94:8", "const:4:8"]]
- 0047ed94 ["CALL", null, ["callee:00497c7c:8"]]
+ 0047edd4 ["INT_ADD", "register:40f0:8", ["const:47edd4:8", "const:4:8"]]
+ 0047edd4 ["CALL", null, ["callee:00497c7c:8"]]
- 0047ed94 bytes aa630094
+ 0047edd4 bytes aa630094
- 0047ed9c ["INT_ADD", "register:40f0:8", ["const:47ed9c:8", "const:4:8"]]
- 0047ed9c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0047eddc ["INT_ADD", "register:40f0:8", ["const:47eddc:8", "const:4:8"]]
+ 0047eddc ["CALL", null, ["callee:00c57eb0:8"]]
- 0047ed9c bytes 45631f94
+ 0047eddc bytes 35641f94
- 0047eda8 ["INT_ADD", "register:40f0:8", ["const:47eda8:8", "const:4:8"]]
- 0047eda8 ["CALL", null, ["callee:0047ee00:8"]]
+ 0047ede8 ["INT_ADD", "register:40f0:8", ["const:47ede8:8", "const:4:8"]]
+ 0047ede8 ["CALL", null, ["callee:0047ee00:8"]]
- 0047eda8 bytes 06000094
+ 0047ede8 bytes 06000094
~~~


<a id="compare-14e25abcd99fd9481245b7bbf48fe263"></a>

### [`0047edc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047edc0.md) → [`0047ee00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ee00.md) FUN_0047ee00

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0047edc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047edc0.md) · 呼出先 3件 [`0047edc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047edc0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0047ee00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ee00.md) · 呼出先 3件 [`0047ee00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ee00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047eddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047edc0.md#insn-0047eddc) · [`0047ede8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047edc0.md#insn-0047ede8) · [`0047edf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047edc0.md#insn-0047edf4)
- 新版 [`0047ee1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ee00.md#insn-0047ee1c) · [`0047ee28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ee00.md#insn-0047ee28) · [`0047ee34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ee00.md#insn-0047ee34)

~~~diff
- 0047eddc ["INT_ADD", "register:40f0:8", ["const:47eddc:8", "const:4:8"]]
- 0047eddc ["CALL", null, ["local:b0:8"]]
+ 0047ee1c ["INT_ADD", "register:40f0:8", ["const:47ee1c:8", "const:4:8"]]
+ 0047ee1c ["CALL", null, ["local:b0:8"]]
- 0047eddc bytes f9ffff97
+ 0047ee1c bytes f9ffff97
- 0047ede8 ["INT_ADD", "register:40f0:8", ["const:47ede8:8", "const:4:8"]]
- 0047ede8 ["CALL", null, ["local:b0:8"]]
+ 0047ee28 ["INT_ADD", "register:40f0:8", ["const:47ee28:8", "const:4:8"]]
+ 0047ee28 ["CALL", null, ["local:b0:8"]]
- 0047ede8 bytes f6ffff97
+ 0047ee28 bytes f6ffff97
- 0047edf4 ["INT_ADD", "register:40f0:8", ["const:47edf4:8", "const:4:8"]]
- 0047edf4 ["CALL", null, ["callee:00c57e80:8"]]
+ 0047ee34 ["INT_ADD", "register:40f0:8", ["const:47ee34:8", "const:4:8"]]
+ 0047ee34 ["CALL", null, ["callee:00c57e80:8"]]
- 0047edf4 bytes 23631f94
+ 0047ee34 bytes 13641f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afddf414b3130933e00d6623b1effaf8"></a>

### [`0047ee2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ee2c.md) → [`0047ee6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ee6c.md) FUN_0047ee6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047ee48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ee2c.md#insn-0047ee48)
- 新版 [`0047ee88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ee6c.md#insn-0047ee88)

~~~diff
- 0047ee48 ["INT_ADD", "register:40f0:8", ["const:47ee48:8", "const:4:8"]]
- 0047ee48 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0047ee88 ["INT_ADD", "register:40f0:8", ["const:47ee88:8", "const:4:8"]]
+ 0047ee88 ["CALL", null, ["callee:00c57eb0:8"]]
- 0047ee48 bytes 1a631f94
+ 0047ee88 bytes 0a641f94
~~~


<a id="compare-1e148cbef9b70a2a3370be632bc7ab82"></a>

### [`0047ee70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ee70.md) → [`0047eeb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047eeb0.md) FUN_0047eeb0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0047ee70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ee70.md) · 呼出先 3件 [`0047ee70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ee70.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0047eeb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047eeb0.md) · 呼出先 3件 [`0047eeb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047eeb0.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047ee8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ee70.md#insn-0047ee8c) · [`0047ee98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ee70.md#insn-0047ee98) · [`0047eea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ee70.md#insn-0047eea4)
- 新版 [`0047eecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047eeb0.md#insn-0047eecc) · [`0047eed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047eeb0.md#insn-0047eed8) · [`0047eee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047eeb0.md#insn-0047eee4)

~~~diff
- 0047ee8c ["INT_ADD", "register:40f0:8", ["const:47ee8c:8", "const:4:8"]]
- 0047ee8c ["CALL", null, ["local:b0:8"]]
+ 0047eecc ["INT_ADD", "register:40f0:8", ["const:47eecc:8", "const:4:8"]]
+ 0047eecc ["CALL", null, ["local:b0:8"]]
- 0047ee8c bytes f9ffff97
+ 0047eecc bytes f9ffff97
- 0047ee98 ["INT_ADD", "register:40f0:8", ["const:47ee98:8", "const:4:8"]]
- 0047ee98 ["CALL", null, ["local:b0:8"]]
+ 0047eed8 ["INT_ADD", "register:40f0:8", ["const:47eed8:8", "const:4:8"]]
+ 0047eed8 ["CALL", null, ["local:b0:8"]]
- 0047ee98 bytes f6ffff97
+ 0047eed8 bytes f6ffff97
- 0047eea4 ["INT_ADD", "register:40f0:8", ["const:47eea4:8", "const:4:8"]]
- 0047eea4 ["CALL", null, ["callee:00c57e80:8"]]
+ 0047eee4 ["INT_ADD", "register:40f0:8", ["const:47eee4:8", "const:4:8"]]
+ 0047eee4 ["CALL", null, ["callee:00c57e80:8"]]
- 0047eea4 bytes f7621f94
+ 0047eee4 bytes e7631f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2eb5c3f367e9cd90eae4a6c461d3de99"></a>

### [`0047eecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047eecc.md) → [`0047ef0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ef0c.md) FUN_0047ef0c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`00633334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633334.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 2件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`00633374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/00633374.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047ef38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047eecc.md#insn-0047ef38) · [`0047ef94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047eecc.md#insn-0047ef94)
- 新版 [`0047ef78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ef0c.md#insn-0047ef78) · [`0047efd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ef0c.md#insn-0047efd4)

~~~diff
- 0047ef38 ["INT_ADD", "register:40f0:8", ["const:47ef38:8", "const:4:8"]]
- 0047ef38 ["CALL", null, ["callee:00c58050:8"]]
+ 0047ef78 ["INT_ADD", "register:40f0:8", ["const:47ef78:8", "const:4:8"]]
+ 0047ef78 ["CALL", null, ["callee:00c58050:8"]]
- 0047ef38 bytes 46631f94
+ 0047ef78 bytes 36641f94
- 0047ef94 ["INT_ADD", "register:40f0:8", ["const:47ef94:8", "const:4:8"]]
- 0047ef94 ["CALL", null, ["callee:00c58050:8"]]
+ 0047efd4 ["INT_ADD", "register:40f0:8", ["const:47efd4:8", "const:4:8"]]
+ 0047efd4 ["CALL", null, ["callee:00c58050:8"]]
- 0047ef94 bytes 2f631f94
+ 0047efd4 bytes 1f641f94
~~~


<a id="compare-899cd7a2aa7a6fda3f627466ed4a2d15"></a>

### [`0047f01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f01c.md) → [`0047f05c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f05c.md) FUN_0047f05c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047f010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f010.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0047f050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f050.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047f03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f01c.md#insn-0047f03c) · [`0047f050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f01c.md#insn-0047f050) · [`0047f058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f01c.md#insn-0047f058)
- 新版 [`0047f07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f05c.md#insn-0047f07c) · [`0047f090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f05c.md#insn-0047f090) · [`0047f098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f05c.md#insn-0047f098)

~~~diff
- 0047f03c ["INT_ADD", "register:40f0:8", ["const:47f03c:8", "const:4:8"]]
- 0047f03c ["CALL", null, ["callee:00c53d00:8"]]
+ 0047f07c ["INT_ADD", "register:40f0:8", ["const:47f07c:8", "const:4:8"]]
+ 0047f07c ["CALL", null, ["callee:00c53d00:8"]]
- 0047f03c bytes 29521f94
+ 0047f07c bytes 21531f94
- 0047f050 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047f050 ["INT_ADD", "register:40f0:8", ["const:47f050:8", "const:4:8"]]
- 0047f050 ["CALLIND", null, ["register:0:8"]]
+ 0047f090 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047f090 ["INT_ADD", "register:40f0:8", ["const:47f090:8", "const:4:8"]]
+ 0047f090 ["CALLIND", null, ["register:0:8"]]
- 0047f050 bytes 00013fd6
+ 0047f090 bytes 00013fd6
- 0047f058 ["INT_ADD", "register:40f0:8", ["const:47f058:8", "const:4:8"]]
- 0047f058 ["CALL", null, ["callee:00c57e80:8"]]
+ 0047f098 ["INT_ADD", "register:40f0:8", ["const:47f098:8", "const:4:8"]]
+ 0047f098 ["CALL", null, ["callee:00c57e80:8"]]
- 0047f058 bytes 8a621f94
+ 0047f098 bytes 7a631f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2eb2664b919911d6026e0b6515762ad3"></a>

### [`0047f10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f10c.md) → [`0047f14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f14c.md) FUN_0047f14c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`00633334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633334.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 2件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`00633374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/00633374.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047f190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f10c.md#insn-0047f190) · [`0047f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f10c.md#insn-0047f1bc)
- 新版 [`0047f1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f14c.md#insn-0047f1d0) · [`0047f1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f14c.md#insn-0047f1fc)

~~~diff
- 0047f190 ["INT_ADD", "register:40f0:8", ["const:47f190:8", "const:4:8"]]
- 0047f190 ["CALL", null, ["callee:00c58050:8"]]
+ 0047f1d0 ["INT_ADD", "register:40f0:8", ["const:47f1d0:8", "const:4:8"]]
+ 0047f1d0 ["CALL", null, ["callee:00c58050:8"]]
- 0047f190 bytes b0621f94
+ 0047f1d0 bytes a0631f94
- 0047f1bc ["INT_ADD", "register:40f0:8", ["const:47f1bc:8", "const:4:8"]]
- 0047f1bc ["CALL", null, ["callee:00c58050:8"]]
+ 0047f1fc ["INT_ADD", "register:40f0:8", ["const:47f1fc:8", "const:4:8"]]
+ 0047f1fc ["CALL", null, ["callee:00c58050:8"]]
- 0047f1bc bytes a5621f94
+ 0047f1fc bytes 95631f94
~~~


<a id="compare-29a6facf2026c1c6f06841043f96ae85"></a>

### [`0047f210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f210.md) → [`0047f250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f250.md) FUN_0047f250

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047f41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f41c.md) [`006337a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/006337a4.md) · 呼出先 3件 [`0047f31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f31c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 3件 [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047f45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f45c.md) [`006337e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/006337e4.md) · 呼出先 3件 [`0047f35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f35c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047f284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f210.md#insn-0047f284) · [`0047f2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f210.md#insn-0047f2b4) · [`0047f2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f210.md#insn-0047f2e4)
- 新版 [`0047f2c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f250.md#insn-0047f2c4) · [`0047f2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f250.md#insn-0047f2f4) · [`0047f324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f250.md#insn-0047f324)

~~~diff
- 0047f284 ["INT_ADD", "register:40f0:8", ["const:47f284:8", "const:4:8"]]
- 0047f284 ["CALL", null, ["callee:00c58050:8"]]
+ 0047f2c4 ["INT_ADD", "register:40f0:8", ["const:47f2c4:8", "const:4:8"]]
+ 0047f2c4 ["CALL", null, ["callee:00c58050:8"]]
- 0047f284 bytes 73621f94
+ 0047f2c4 bytes 63631f94
- 0047f2b4 ["INT_ADD", "register:40f0:8", ["const:47f2b4:8", "const:4:8"]]
- 0047f2b4 ["CALL", null, ["callee:00c58050:8"]]
+ 0047f2f4 ["INT_ADD", "register:40f0:8", ["const:47f2f4:8", "const:4:8"]]
+ 0047f2f4 ["CALL", null, ["callee:00c58050:8"]]
- 0047f2b4 bytes 67621f94
+ 0047f2f4 bytes 57631f94
- 0047f2e4 ["INT_ADD", "register:40f0:8", ["const:47f2e4:8", "const:4:8"]]
- 0047f2e4 ["CALL", null, ["callee:0047f35c:8"]]
+ 0047f324 ["INT_ADD", "register:40f0:8", ["const:47f324:8", "const:4:8"]]
+ 0047f324 ["CALL", null, ["callee:0047f35c:8"]]
- 0047f2e4 bytes 0e000094
+ 0047f324 bytes 0e000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b329b64724c6940888424eb5500df76"></a>

### [`0047f31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f31c.md) → [`0047f35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f35c.md) FUN_0047f35c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0047f210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f210.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`0047f250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f250.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047f388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f31c.md#insn-0047f388) · [`0047f3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f31c.md#insn-0047f3b8)
- 新版 [`0047f3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f35c.md#insn-0047f3c8) · [`0047f3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f35c.md#insn-0047f3f8)

~~~diff
- 0047f388 ["INT_ADD", "register:40f0:8", ["const:47f388:8", "const:4:8"]]
- 0047f388 ["CALL", null, ["callee:00c58050:8"]]
+ 0047f3c8 ["INT_ADD", "register:40f0:8", ["const:47f3c8:8", "const:4:8"]]
+ 0047f3c8 ["CALL", null, ["callee:00c58050:8"]]
- 0047f388 bytes 32621f94
+ 0047f3c8 bytes 22631f94
- 0047f3b8 ["INT_ADD", "register:40f0:8", ["const:47f3b8:8", "const:4:8"]]
- 0047f3b8 ["CALL", null, ["callee:00c58050:8"]]
+ 0047f3f8 ["INT_ADD", "register:40f0:8", ["const:47f3f8:8", "const:4:8"]]
+ 0047f3f8 ["CALL", null, ["callee:00c58050:8"]]
- 0047f3b8 bytes 26621f94
+ 0047f3f8 bytes 16631f94
~~~


<a id="compare-41dd7cf093e3b616bb8ba708bc6a63f0"></a>

### [`0047f41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f41c.md) → [`0047f45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f45c.md) FUN_0047f45c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`006337a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/006337a4.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0047f210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f210.md) [`0047f54c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f54c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`006337e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/006337e4.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0047f250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f250.md) [`0047f58c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f58c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f41c.md#insn-0047f484) · [`0047f498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f41c.md#insn-0047f498) · [`0047f4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f41c.md#insn-0047f4c8)
- 新版 [`0047f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f45c.md#insn-0047f4c4) · [`0047f4d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f45c.md#insn-0047f4d8) · [`0047f508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f45c.md#insn-0047f508)

~~~diff
- 0047f484 ["INT_ADD", "register:40f0:8", ["const:47f484:8", "const:4:8"]]
- 0047f484 ["CALL", null, ["callee:0047f250:8"]]
+ 0047f4c4 ["INT_ADD", "register:40f0:8", ["const:47f4c4:8", "const:4:8"]]
+ 0047f4c4 ["CALL", null, ["callee:0047f250:8"]]
- 0047f484 bytes 63ffff97
+ 0047f4c4 bytes 63ffff97
- 0047f498 ["INT_ADD", "register:40f0:8", ["const:47f498:8", "const:4:8"]]
- 0047f498 ["CALL", null, ["callee:0047f250:8"]]
+ 0047f4d8 ["INT_ADD", "register:40f0:8", ["const:47f4d8:8", "const:4:8"]]
+ 0047f4d8 ["CALL", null, ["callee:0047f250:8"]]
- 0047f498 bytes 5effff97
+ 0047f4d8 bytes 5effff97
- 0047f4c8 ["INT_ADD", "register:40f0:8", ["const:47f4c8:8", "const:4:8"]]
- 0047f4c8 ["CALL", null, ["callee:0047f58c:8"]]
+ 0047f508 ["INT_ADD", "register:40f0:8", ["const:47f508:8", "const:4:8"]]
+ 0047f508 ["CALL", null, ["callee:0047f58c:8"]]
- 0047f4c8 bytes 21000094
+ 0047f508 bytes 21000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d489a3d65e735aec3bb59faa60dd51d3"></a>

### [`0047f54c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f54c.md) → [`0047f58c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f58c.md) FUN_0047f58c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0047f41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f41c.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`0047f45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f45c.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047f56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f54c.md#insn-0047f56c) · [`0047f5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f54c.md#insn-0047f5a4) · [`0047f5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f54c.md#insn-0047f5d0)
- 新版 [`0047f5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f58c.md#insn-0047f5ac) · [`0047f5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f58c.md#insn-0047f5e4) · [`0047f610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f58c.md#insn-0047f610)

~~~diff
- 0047f56c ["INT_ADD", "register:40f0:8", ["const:47f56c:8", "const:4:8"]]
- 0047f56c ["CALL", null, ["callee:00c57e90:8"]]
+ 0047f5ac ["INT_ADD", "register:40f0:8", ["const:47f5ac:8", "const:4:8"]]
+ 0047f5ac ["CALL", null, ["callee:00c57e90:8"]]
- 0047f56c bytes 49611f94
+ 0047f5ac bytes 39621f94
- 0047f5a4 ["INT_ADD", "register:40f0:8", ["const:47f5a4:8", "const:4:8"]]
- 0047f5a4 ["CALL", null, ["callee:0043bb20:8"]]
+ 0047f5e4 ["INT_ADD", "register:40f0:8", ["const:47f5e4:8", "const:4:8"]]
+ 0047f5e4 ["CALL", null, ["callee:0043bb20:8"]]
- 0047f5a4 bytes 4ff1fe97
+ 0047f5e4 bytes 4ff1fe97
- 0047f5d0 ["INT_ADD", "register:40f0:8", ["const:47f5d0:8", "const:4:8"]]
- 0047f5d0 ["CALL", null, ["callee:0043bb20:8"]]
+ 0047f610 ["INT_ADD", "register:40f0:8", ["const:47f610:8", "const:4:8"]]
+ 0047f610 ["CALL", null, ["callee:0043bb20:8"]]
- 0047f5d0 bytes 44f1fe97
+ 0047f610 bytes 44f1fe97
~~~


<a id="compare-383136d38a9accd7ce6a0c581c228bd0"></a>

### [`0047f62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f62c.md) → [`0047f66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f66c.md) FUN_0047f66c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047f654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f62c.md#insn-0047f654) · [`0047f664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f62c.md#insn-0047f664) · [`0047f674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f62c.md#insn-0047f674)
- 新版 [`0047f694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f66c.md#insn-0047f694) · [`0047f6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f66c.md#insn-0047f6a4) · [`0047f6b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f66c.md#insn-0047f6b4)

~~~diff
- 0047f654 ["INT_ADD", "register:40f0:8", ["const:47f654:8", "const:4:8"]]
- 0047f654 ["CALL", null, ["callee:00c57e80:8"]]
+ 0047f694 ["INT_ADD", "register:40f0:8", ["const:47f694:8", "const:4:8"]]
+ 0047f694 ["CALL", null, ["callee:00c57e80:8"]]
- 0047f654 bytes 0b611f94
+ 0047f694 bytes fb611f94
- 0047f664 ["INT_ADD", "register:40f0:8", ["const:47f664:8", "const:4:8"]]
- 0047f664 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0047f6a4 ["INT_ADD", "register:40f0:8", ["const:47f6a4:8", "const:4:8"]]
+ 0047f6a4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0047f664 bytes 13611f94
+ 0047f6a4 bytes 03621f94
- 0047f674 ["INT_ADD", "register:40f0:8", ["const:47f674:8", "const:4:8"]]
- 0047f674 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0047f6b4 ["INT_ADD", "register:40f0:8", ["const:47f6b4:8", "const:4:8"]]
+ 0047f6b4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0047f674 bytes 0f611f94
+ 0047f6b4 bytes ff611f94
~~~


<a id="compare-c5174d932e641b12fd135fae9a724255"></a>

### [`0047f93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f93c.md) → [`0047f97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f97c.md) FUN_0047f97c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0047f694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f694.md) · 呼出先 2件 [`00c58130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58130.md) [`00c58140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58140.md)
- 新版 呼出元 1件 [`0047f6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f6d4.md) · 呼出先 2件 [`00c58530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58530.md) [`00c58540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58540.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047f94c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f93c.md#insn-0047f94c)
- 新版 [`0047f98c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f97c.md#insn-0047f98c)

~~~diff
- 0047f94c ["INT_ADD", "register:40f0:8", ["const:47f94c:8", "const:4:8"]]
- 0047f94c ["CALL", null, ["callee:00c58530:8"]]
+ 0047f98c ["INT_ADD", "register:40f0:8", ["const:47f98c:8", "const:4:8"]]
+ 0047f98c ["CALL", null, ["callee:00c58530:8"]]
- 0047f94c bytes f9611f94
+ 0047f98c bytes e9621f94
~~~


<a id="compare-f8f930e167589fbe7e9c9368d1681419"></a>

### [`0047fc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fc2c.md) → [`0047fc6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fc6c.md) FUN_0047fc6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047f7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f7dc.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d30.md) [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c57d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d50.md)
- 新版 呼出元 1件 [`0047f81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f81c.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58130.md) [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047fc54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fc2c.md#insn-0047fc54) · [`0047fc64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fc2c.md#insn-0047fc64) · [`0047fc80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fc2c.md#insn-0047fc80)
- 新版 [`0047fc94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fc6c.md#insn-0047fc94) · [`0047fca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fc6c.md#insn-0047fca4) · [`0047fcc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fc6c.md#insn-0047fcc0)

~~~diff
- 0047fc54 ["INT_ADD", "register:40f0:8", ["const:47fc54:8", "const:4:8"]]
- 0047fc54 ["CALL", null, ["callee:00c58130:8"]]
+ 0047fc94 ["INT_ADD", "register:40f0:8", ["const:47fc94:8", "const:4:8"]]
+ 0047fc94 ["CALL", null, ["callee:00c58130:8"]]
- 0047fc54 bytes 37601f94
+ 0047fc94 bytes 27611f94
- 0047fc64 ["INT_ADD", "register:40f0:8", ["const:47fc64:8", "const:4:8"]]
- 0047fc64 ["CALL", null, ["callee:00c58140:8"]]
+ 0047fca4 ["INT_ADD", "register:40f0:8", ["const:47fca4:8", "const:4:8"]]
+ 0047fca4 ["CALL", null, ["callee:00c58140:8"]]
- 0047fc64 bytes 37601f94
+ 0047fca4 bytes 27611f94
- 0047fc80 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047fc80 ["INT_ADD", "register:40f0:8", ["const:47fc80:8", "const:4:8"]]
- 0047fc80 ["CALLIND", null, ["register:0:8"]]
+ 0047fcc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047fcc0 ["INT_ADD", "register:40f0:8", ["const:47fcc0:8", "const:4:8"]]
+ 0047fcc0 ["CALLIND", null, ["register:0:8"]]
- 0047fc80 bytes 00013fd6
+ 0047fcc0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac100d6a3aeceb1d8b6842f39dcde33d"></a>

### [`0047fcf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fcf8.md) → [`0047fd38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fd38.md) FUN_0047fd38

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0047fd20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fcf8.md#insn-0047fd20) · [`0047fd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fcf8.md#insn-0047fd28)
- 新版 [`0047fd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fd38.md#insn-0047fd60) · [`0047fd68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fd38.md#insn-0047fd68)

~~~diff
- 0047fd20 ["INT_ADD", "register:40f0:8", ["const:47fd20:8", "const:4:8"]]
- 0047fd20 ["CALL", null, ["callee:00c58150:8"]]
+ 0047fd60 ["INT_ADD", "register:40f0:8", ["const:47fd60:8", "const:4:8"]]
+ 0047fd60 ["CALL", null, ["callee:00c58150:8"]]
- 0047fd20 bytes 0c601f94
+ 0047fd60 bytes fc601f94
- 0047fd28 ["INT_ADD", "register:40f0:8", ["const:47fd28:8", "const:4:8"]]
- 0047fd28 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0047fd68 ["INT_ADD", "register:40f0:8", ["const:47fd68:8", "const:4:8"]]
+ 0047fd68 ["CALL", null, ["callee:00c57eb0:8"]]
- 0047fd28 bytes 625f1f94
+ 0047fd68 bytes 52601f94
~~~


<a id="compare-98e281e4c275bdec3729af0f2c4bce6c"></a>

### [`004800d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004800d8.md) → [`00480118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480118.md) FUN_00480118

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 23件 [`005c0b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0b58.md) [`0066b324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b324.md) [`006db02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006db02c.md) [`0072ece8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ece8.md) [`00732904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732904.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 23件 [`005c0b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c0b98.md) [`0066b364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b364.md) [`006db06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006db/006db06c.md) [`0072ed28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072e/0072ed28.md) [`00732944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732944.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004800d8.md#insn-00480104) · [`00480134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004800d8.md#insn-00480134)
- 新版 [`00480144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480118.md#insn-00480144) · [`00480174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480118.md#insn-00480174)

~~~diff
- 00480104 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480104 ["INT_ADD", "register:40f0:8", ["const:480104:8", "const:4:8"]]
- 00480104 ["CALLIND", null, ["register:0:8"]]
+ 00480144 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480144 ["INT_ADD", "register:40f0:8", ["const:480144:8", "const:4:8"]]
+ 00480144 ["CALLIND", null, ["register:0:8"]]
- 00480104 bytes 00013fd6
+ 00480144 bytes 00013fd6
- 00480134 ["INT_ADD", "register:40f0:8", ["const:480134:8", "const:4:8"]]
- 00480134 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00480174 ["INT_ADD", "register:40f0:8", ["const:480174:8", "const:4:8"]]
+ 00480174 ["CALL", null, ["callee:00c57ee0:8"]]
- 00480134 bytes 6b5e1f94
+ 00480174 bytes 5b5f1f94
~~~


<a id="compare-311c7432a828734e0d691842583de851"></a>

### [`00480138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480138.md) → [`00480178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md) FUN_00480178

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 26件 [`005c0b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0b58.md) [`00675b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00675/00675b54.md) [`006a48bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a4/006a48bc.md) [`006db02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006db02c.md) [`0073876c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/0073876c.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 26件 [`005c0b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c0b98.md) [`00675b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00675/00675b94.md) [`006a48fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a4/006a48fc.md) [`006db06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006db/006db06c.md) [`007387ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/007387ac.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480138.md#insn-00480164) · [`00480194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480138.md#insn-00480194)
- 新版 [`004801a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md#insn-004801a4) · [`004801d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md#insn-004801d4)

~~~diff
- 00480164 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480164 ["INT_ADD", "register:40f0:8", ["const:480164:8", "const:4:8"]]
- 00480164 ["CALLIND", null, ["register:0:8"]]
+ 004801a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004801a4 ["INT_ADD", "register:40f0:8", ["const:4801a4:8", "const:4:8"]]
+ 004801a4 ["CALLIND", null, ["register:0:8"]]
- 00480164 bytes 00013fd6
+ 004801a4 bytes 00013fd6
- 00480194 ["INT_ADD", "register:40f0:8", ["const:480194:8", "const:4:8"]]
- 00480194 ["CALL", null, ["callee:00c57ee0:8"]]
+ 004801d4 ["INT_ADD", "register:40f0:8", ["const:4801d4:8", "const:4:8"]]
+ 004801d4 ["CALL", null, ["callee:00c57ee0:8"]]
- 00480194 bytes 535e1f94
+ 004801d4 bytes 435f1f94
~~~


