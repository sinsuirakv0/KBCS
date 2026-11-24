# v16.0.0 → v16.0.1 · 要調査の変更候補 (43)

[一覧の目次](README.md)

<a id="compare-ed18459e8cd7d95bff067bdeb82c7453"></a>

### [`00c16bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16bb4.md) → [`00c16fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16fdc.md) _ZNKSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_RNS_8ios_baseEwPK2tmcc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e270.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e670.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c16bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16bb4.md#insn-00c16bf4) · [`00c16c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16bb4.md#insn-00c16c48)
- 新版 [`00c1701c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16fdc.md#insn-00c1701c) · [`00c17070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16fdc.md#insn-00c17070)

~~~diff
- 00c16bf4 ["INT_ADD", "register:40f0:8", ["const:c16bf4:8", "const:4:8"]]
- 00c16bf4 ["CALL", null, ["callee:00c5e670:8"]]
+ 00c1701c ["INT_ADD", "register:40f0:8", ["const:c1701c:8", "const:4:8"]]
+ 00c1701c ["CALL", null, ["callee:00c5e670:8"]]
- 00c16bf4 bytes 9f1d0194
+ 00c1701c bytes 951d0194
- 00c16c48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c16c48 ["INT_ADD", "register:40f0:8", ["const:c16c48:8", "const:4:8"]]
- 00c16c48 ["CALLIND", null, ["register:0:8"]]
+ 00c17070 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c17070 ["INT_ADD", "register:40f0:8", ["const:c17070:8", "const:4:8"]]
+ 00c17070 ["CALLIND", null, ["register:0:8"]]
- 00c16c48 bytes 00013fd6
+ 00c17070 bytes 00013fd6
~~~


<a id="compare-a0e7197b550f41db3324e99eedecb79e"></a>

### [`00c18b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c18/00c18b9c.md) → [`00c18fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c18/00c18fc4.md) FUN_00c18fc4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c188dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c18/00c188dc.md) · 呼出先 6件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c18d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c18/00c18d04.md) · 呼出先 6件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c18cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c18/00c18b9c.md#insn-00c18cd4) · [`00c18cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c18/00c18b9c.md#insn-00c18cf4) · [`00c18d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c18/00c18b9c.md#insn-00c18d50)
- 新版 [`00c190fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c18/00c18fc4.md#insn-00c190fc) · [`00c1911c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c18/00c18fc4.md#insn-00c1911c) · [`00c19178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c18/00c18fc4.md#insn-00c19178)

~~~diff
- 00c18cd4 ["INT_ADD", "register:40f0:8", ["const:c18cd4:8", "const:4:8"]]
- 00c18cd4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00c190fc ["INT_ADD", "register:40f0:8", ["const:c190fc:8", "const:4:8"]]
+ 00c190fc ["CALL", null, ["callee:00c57e90:8"]]
- 00c18cd4 bytes 6ffb0094
+ 00c190fc bytes 65fb0094
- 00c18cf4 ["INT_ADD", "register:40f0:8", ["const:c18cf4:8", "const:4:8"]]
- 00c18cf4 ["CALL", null, ["callee:00c58000:8"]]
+ 00c1911c ["INT_ADD", "register:40f0:8", ["const:c1911c:8", "const:4:8"]]
+ 00c1911c ["CALL", null, ["callee:00c58000:8"]]
- 00c18cf4 bytes c3fb0094
+ 00c1911c bytes b9fb0094
- 00c18d50 ["INT_ADD", "register:40f0:8", ["const:c18d50:8", "const:4:8"]]
- 00c18d50 ["CALL", null, ["callee:00c5b0a0:8"]]
+ 00c19178 ["INT_ADD", "register:40f0:8", ["const:c19178:8", "const:4:8"]]
+ 00c19178 ["CALL", null, ["callee:00c5b0a0:8"]]
- 00c18d50 bytes d4070194
+ 00c19178 bytes ca070194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2aa385e055230e2d5ed499c24a75a89d"></a>

### [`00c1abc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1a/00c1abc4.md) → [`00c1afec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1a/00c1afec.md) FUN_00c1afec

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c1a898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1a/00c1a898.md) · 呼出先 8件 [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00c1acc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1a/00c1acc0.md) · 呼出先 8件 [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1a/00c1abc4.md#insn-00c1acb4) · [`00c1ad30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1a/00c1abc4.md#insn-00c1ad30) · [`00c1ad60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1a/00c1abc4.md#insn-00c1ad60)
- 新版 [`00c1b0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1a/00c1afec.md#insn-00c1b0dc) · [`00c1b158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1a/00c1afec.md#insn-00c1b158) · [`00c1b188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1a/00c1afec.md#insn-00c1b188)

~~~diff
- 00c1acb4 ["INT_ADD", "register:40f0:8", ["const:c1acb4:8", "const:4:8"]]
- 00c1acb4 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00c1b0dc ["INT_ADD", "register:40f0:8", ["const:c1b0dc:8", "const:4:8"]]
+ 00c1b0dc ["CALL", null, ["callee:00c5a8a0:8"]]
- 00c1acb4 bytes fbfd0094
+ 00c1b0dc bytes f1fd0094
- 00c1ad30 ["INT_ADD", "register:40f0:8", ["const:c1ad30:8", "const:4:8"]]
- 00c1ad30 ["CALL", null, ["callee:00c57e90:8"]]
+ 00c1b158 ["INT_ADD", "register:40f0:8", ["const:c1b158:8", "const:4:8"]]
+ 00c1b158 ["CALL", null, ["callee:00c57e90:8"]]
- 00c1ad30 bytes 58f30094
+ 00c1b158 bytes 4ef30094
- 00c1ad60 ["INT_ADD", "register:40f0:8", ["const:c1ad60:8", "const:4:8"]]
- 00c1ad60 ["CALL", null, ["callee:00c58000:8"]]
+ 00c1b188 ["INT_ADD", "register:40f0:8", ["const:c1b188:8", "const:4:8"]]
+ 00c1b188 ["CALL", null, ["callee:00c58000:8"]]
- 00c1ad60 bytes a8f30094
+ 00c1b188 bytes 9ef30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17d20042e31c2da0967747839614dfbb"></a>

### [`00c1b5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b5b8.md) → [`00c1b9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b9e0.md) FUN_00c1b9e0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00c0f250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f250.md) [`00c0f6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f6e0.md) [`00c10984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10984.md) [`00c10e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10e14.md) [`00c1b10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b10c.md) · 呼出先 2件 [`00c5e170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e170.md) [`00c5e300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e300.md)
- 新版 呼出元 6件 [`00c0f678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0f678.md) [`00c0fb08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0fb08.md) [`00c10dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c10dac.md) [`00c1123c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c1123c.md) [`00c1b534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b534.md) · 呼出先 2件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5e700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e700.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1b61c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b5b8.md#insn-00c1b61c) · [`00c1b63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b5b8.md#insn-00c1b63c) · [`00c1b64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b5b8.md#insn-00c1b64c)
- 新版 [`00c1ba44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b9e0.md#insn-00c1ba44) · [`00c1ba64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b9e0.md#insn-00c1ba64) · [`00c1ba74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b9e0.md#insn-00c1ba74)

~~~diff
- 00c1b61c ["INT_ADD", "register:40f0:8", ["const:c1b61c:8", "const:4:8"]]
- 00c1b61c ["CALL", null, ["callee:00c5e570:8"]]
+ 00c1ba44 ["INT_ADD", "register:40f0:8", ["const:c1ba44:8", "const:4:8"]]
+ 00c1ba44 ["CALL", null, ["callee:00c5e570:8"]]
- 00c1b61c bytes d50a0194
+ 00c1ba44 bytes cb0a0194
- 00c1b63c ["INT_ADD", "register:40f0:8", ["const:c1b63c:8", "const:4:8"]]
- 00c1b63c ["CALL", null, ["callee:00c5e700:8"]]
+ 00c1ba64 ["INT_ADD", "register:40f0:8", ["const:c1ba64:8", "const:4:8"]]
+ 00c1ba64 ["CALL", null, ["callee:00c5e700:8"]]
- 00c1b63c bytes 310b0194
+ 00c1ba64 bytes 270b0194
- 00c1b64c ["INT_ADD", "register:40f0:8", ["const:c1b64c:8", "const:4:8"]]
- 00c1b64c ["CALL", null, ["callee:00c5e570:8"]]
+ 00c1ba74 ["INT_ADD", "register:40f0:8", ["const:c1ba74:8", "const:4:8"]]
+ 00c1ba74 ["CALL", null, ["callee:00c5e570:8"]]
- 00c1b64c bytes c90a0194
+ 00c1ba74 bytes bf0a0194
~~~


<a id="compare-141aa06f4b730cf11bec6a268dfc14cb"></a>

### [`00c1b898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b898.md) → [`00c1bcc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1bcc0.md) _ZNSt6__ndk111__money_putIcE8__formatEPcRS2_S3_jPKcS5_RKNS_5ctypeIcEEbRKNS_10money_base7patternEccRKNS_12basic_stringIcNS_11char_traitsIcEEN

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e2f0.md) · 呼出先 1件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00c5e6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e6f0.md) · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1ba34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b898.md#insn-00c1ba34) · [`00c1ba90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b898.md#insn-00c1ba90) · [`00c1baf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b898.md#insn-00c1baf4)
- 新版 [`00c1be5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1bcc0.md#insn-00c1be5c) · [`00c1beb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1bcc0.md#insn-00c1beb8) · [`00c1bf1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1bcc0.md#insn-00c1bf1c)

~~~diff
- 00c1ba34 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c1ba34 ["INT_ADD", "register:40f0:8", ["const:c1ba34:8", "const:4:8"]]
- 00c1ba34 ["CALLIND", null, ["register:0:8"]]
+ 00c1be5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c1be5c ["INT_ADD", "register:40f0:8", ["const:c1be5c:8", "const:4:8"]]
+ 00c1be5c ["CALLIND", null, ["register:0:8"]]
- 00c1ba34 bytes 00013fd6
+ 00c1be5c bytes 00013fd6
- 00c1ba90 ["INT_ADD", "register:40f0:8", ["const:c1ba90:8", "const:4:8"]]
- 00c1ba90 ["CALL", null, ["callee:00c57f40:8"]]
+ 00c1beb8 ["INT_ADD", "register:40f0:8", ["const:c1beb8:8", "const:4:8"]]
+ 00c1beb8 ["CALL", null, ["callee:00c57f40:8"]]
- 00c1ba90 bytes 2cf00094
+ 00c1beb8 bytes 22f00094
- 00c1baf4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c1baf4 ["INT_ADD", "register:40f0:8", ["const:c1baf4:8", "const:4:8"]]
- 00c1baf4 ["CALLIND", null, ["register:0:8"]]
+ 00c1bf1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c1bf1c ["INT_ADD", "register:40f0:8", ["const:c1bf1c:8", "const:4:8"]]
+ 00c1bf1c ["CALLIND", null, ["register:0:8"]]
- 00c1baf4 bytes 00013fd6
+ 00c1bf1c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-608180c46e7e3b0581afc1e1edba28b3"></a>

### [`00c1c754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1c/00c1c754.md) → [`00c1cb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1c/00c1cb7c.md) _ZNSt6__ndk111__money_putIwE8__formatEPwRS2_S3_jPKwS5_RKNS_5ctypeIwEEbRKNS_10money_base7patternEwwRKNS_12basic_stringIcNS_11char_traitsIcEEN

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e320.md) · 呼出先 1件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00c5e720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e720.md) · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1c860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1c/00c1c754.md#insn-00c1c860) · [`00c1c8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1c/00c1c754.md#insn-00c1c8e8) · [`00c1c940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1c/00c1c754.md#insn-00c1c940)
- 新版 [`00c1cc88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1c/00c1cb7c.md#insn-00c1cc88) · [`00c1cd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1c/00c1cb7c.md#insn-00c1cd10) · [`00c1cd68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1c/00c1cb7c.md#insn-00c1cd68)

~~~diff
- 00c1c860 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c1c860 ["INT_ADD", "register:40f0:8", ["const:c1c860:8", "const:4:8"]]
- 00c1c860 ["CALLIND", null, ["register:0:8"]]
+ 00c1cc88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c1cc88 ["INT_ADD", "register:40f0:8", ["const:c1cc88:8", "const:4:8"]]
+ 00c1cc88 ["CALLIND", null, ["register:0:8"]]
- 00c1c860 bytes 00013fd6
+ 00c1cc88 bytes 00013fd6
- 00c1c8e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c1c8e8 ["INT_ADD", "register:40f0:8", ["const:c1c8e8:8", "const:4:8"]]
- 00c1c8e8 ["CALLIND", null, ["register:0:8"]]
+ 00c1cd10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c1cd10 ["INT_ADD", "register:40f0:8", ["const:c1cd10:8", "const:4:8"]]
+ 00c1cd10 ["CALLIND", null, ["register:0:8"]]
- 00c1c8e8 bytes 00013fd6
+ 00c1cd10 bytes 00013fd6
- 00c1c940 ["INT_ADD", "register:40f0:8", ["const:c1c940:8", "const:4:8"]]
- 00c1c940 ["CALL", null, ["callee:00c57f40:8"]]
+ 00c1cd68 ["INT_ADD", "register:40f0:8", ["const:c1cd68:8", "const:4:8"]]
+ 00c1cd68 ["CALL", null, ["callee:00c57f40:8"]]
- 00c1c940 bytes 80ec0094
+ 00c1cd68 bytes 76ec0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6035bf8bde5e1700f6b22e7f660dc5a9"></a>

### [`00c1d008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d008.md) → [`00c1d430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d430.md) _ZNSt6__ndk114codecvt_bynameIcc9mbstate_tED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e340.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e740.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1d01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d008.md#insn-00c1d01c)
- 新版 [`00c1d444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d430.md#insn-00c1d444)

~~~diff
- 00c1d01c ["INT_ADD", "register:40f0:8", ["const:c1d01c:8", "const:4:8"]]
- 00c1d01c ["CALL", null, ["callee:00c5e740:8"]]
+ 00c1d444 ["INT_ADD", "register:40f0:8", ["const:c1d444:8", "const:4:8"]]
+ 00c1d444 ["CALL", null, ["callee:00c5e740:8"]]
- 00c1d01c bytes c9040194
+ 00c1d444 bytes bf040194
~~~


<a id="compare-a5d708b0ae104f8f211b1dc3e651ddb9"></a>

### [`00c1d03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d03c.md) → [`00c1d464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d464.md) _ZNSt6__ndk114codecvt_bynameIwc9mbstate_tED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e350.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e750.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1d050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d03c.md#insn-00c1d050)
- 新版 [`00c1d478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d464.md#insn-00c1d478)

~~~diff
- 00c1d050 ["INT_ADD", "register:40f0:8", ["const:c1d050:8", "const:4:8"]]
- 00c1d050 ["CALL", null, ["callee:00c5e750:8"]]
+ 00c1d478 ["INT_ADD", "register:40f0:8", ["const:c1d478:8", "const:4:8"]]
+ 00c1d478 ["CALL", null, ["callee:00c5e750:8"]]
- 00c1d050 bytes c0040194
+ 00c1d478 bytes b6040194
~~~


<a id="compare-7971bad4c1b67ea3d7bbb6be818c464d"></a>

### [`00c1d070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d070.md) → [`00c1d498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d498.md) _ZNSt6__ndk114codecvt_bynameIDsc9mbstate_tED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e370.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e770.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1d084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d070.md#insn-00c1d084)
- 新版 [`00c1d4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d498.md#insn-00c1d4ac)

~~~diff
- 00c1d084 ["INT_ADD", "register:40f0:8", ["const:c1d084:8", "const:4:8"]]
- 00c1d084 ["CALL", null, ["callee:00c5e770:8"]]
+ 00c1d4ac ["INT_ADD", "register:40f0:8", ["const:c1d4ac:8", "const:4:8"]]
+ 00c1d4ac ["CALL", null, ["callee:00c5e770:8"]]
- 00c1d084 bytes bb040194
+ 00c1d4ac bytes b1040194
~~~


<a id="compare-63699945ce177ac0a87cc6198edc299c"></a>

### [`00c1d0a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d0a4.md) → [`00c1d4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d4cc.md) _ZNSt6__ndk114codecvt_bynameIDic9mbstate_tED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e390.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e790.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1d0b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d0a4.md#insn-00c1d0b8)
- 新版 [`00c1d4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d4cc.md#insn-00c1d4e0)

~~~diff
- 00c1d0b8 ["INT_ADD", "register:40f0:8", ["const:c1d0b8:8", "const:4:8"]]
- 00c1d0b8 ["CALL", null, ["callee:00c5e790:8"]]
+ 00c1d4e0 ["INT_ADD", "register:40f0:8", ["const:c1d4e0:8", "const:4:8"]]
+ 00c1d4e0 ["CALL", null, ["callee:00c5e790:8"]]
- 00c1d0b8 bytes b6040194
+ 00c1d4e0 bytes ac040194
~~~


<a id="compare-b8e3855202dc39a8e098271e8045adff"></a>

### [`00c1d0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d0d8.md) → [`00c1d500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d500.md) _ZNSt6__ndk114codecvt_bynameIDsDu9mbstate_tED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e3b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e7b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1d0ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d0d8.md#insn-00c1d0ec)
- 新版 [`00c1d514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d500.md#insn-00c1d514)

~~~diff
- 00c1d0ec ["INT_ADD", "register:40f0:8", ["const:c1d0ec:8", "const:4:8"]]
- 00c1d0ec ["CALL", null, ["callee:00c5e7b0:8"]]
+ 00c1d514 ["INT_ADD", "register:40f0:8", ["const:c1d514:8", "const:4:8"]]
+ 00c1d514 ["CALL", null, ["callee:00c5e7b0:8"]]
- 00c1d0ec bytes b1040194
+ 00c1d514 bytes a7040194
~~~


<a id="compare-36802f723660e19b239ad950e4c0ecab"></a>

### [`00c1d10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d10c.md) → [`00c1d534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d534.md) _ZNSt6__ndk114codecvt_bynameIDiDu9mbstate_tED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e3d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e7d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1d120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d10c.md#insn-00c1d120)
- 新版 [`00c1d548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d534.md#insn-00c1d548)

~~~diff
- 00c1d120 ["INT_ADD", "register:40f0:8", ["const:c1d120:8", "const:4:8"]]
- 00c1d120 ["CALL", null, ["callee:00c5e7d0:8"]]
+ 00c1d548 ["INT_ADD", "register:40f0:8", ["const:c1d548:8", "const:4:8"]]
+ 00c1d548 ["CALL", null, ["callee:00c5e7d0:8"]]
- 00c1d120 bytes ac040194
+ 00c1d548 bytes a2040194
~~~


<a id="compare-63321b220a8915e7f7a37d79286f852c"></a>

### [`00c1d138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d138.md) → [`00c1d560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d560.md) FUN_00c1d560

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 2件 [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c1d228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d138.md#insn-00c1d228)
- 新版 [`00c1d650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d560.md#insn-00c1d650)

~~~diff
- 00c1d228 ["INT_ADD", "register:40f0:8", ["const:c1d228:8", "const:4:8"]]
- 00c1d228 ["CALL", null, ["callee:00c58050:8"]]
+ 00c1d650 ["INT_ADD", "register:40f0:8", ["const:c1d650:8", "const:4:8"]]
+ 00c1d650 ["CALL", null, ["callee:00c58050:8"]]
- 00c1d228 bytes 8aea0094
+ 00c1d650 bytes 80ea0094
~~~


<a id="compare-46d453b1746a0e98e887a9c185e5a76d"></a>

### [`00c24854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24854.md) → [`00c24c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c24c7c.md) FUN_00c24c7c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c24780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24780.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c24ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c24ba8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c24868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24854.md#insn-00c24868)
- 新版 [`00c24c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c24c7c.md#insn-00c24c90)

~~~diff
- 00c24868 ["INT_ADD", "register:40f0:8", ["const:c24868:8", "const:4:8"]]
- 00c24868 ["CALL", null, ["callee:00c24ba8:8"]]
+ 00c24c90 ["INT_ADD", "register:40f0:8", ["const:c24c90:8", "const:4:8"]]
+ 00c24c90 ["CALL", null, ["callee:00c24ba8:8"]]
- 00c24868 bytes c6ffff97
+ 00c24c90 bytes c6ffff97
~~~


<a id="compare-36093a2a9276ad622c558c6d7309304c"></a>

### [`00c24c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24c0c.md) → [`00c25034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25034.md) _ZNSt6__ndk16localeC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c24c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24c0c.md#insn-00c24c2c) · [`00c24c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24c0c.md#insn-00c24c3c) · [`00c24c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24c0c.md#insn-00c24c4c)
- 新版 [`00c25054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25034.md#insn-00c25054) · [`00c25064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25034.md#insn-00c25064) · [`00c25074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25034.md#insn-00c25074)

~~~diff
- 00c24c2c ["INT_ADD", "register:40f0:8", ["const:c24c2c:8", "const:4:8"]]
- 00c24c2c ["CALL", null, ["callee:00c57e90:8"]]
+ 00c25054 ["INT_ADD", "register:40f0:8", ["const:c25054:8", "const:4:8"]]
+ 00c25054 ["CALL", null, ["callee:00c57e90:8"]]
- 00c24c2c bytes 99cb0094
+ 00c25054 bytes 8fcb0094
- 00c24c3c ["INT_ADD", "register:40f0:8", ["const:c24c3c:8", "const:4:8"]]
- 00c24c3c ["CALL", null, ["callee:00c1f48c:8"]]
+ 00c25064 ["INT_ADD", "register:40f0:8", ["const:c25064:8", "const:4:8"]]
+ 00c25064 ["CALL", null, ["callee:00c1f48c:8"]]
- 00c24c3c bytes 0ae9ff97
+ 00c25064 bytes 0ae9ff97
- 00c24c4c ["INT_ADD", "register:40f0:8", ["const:c24c4c:8", "const:4:8"]]
- 00c24c4c ["CALL", null, ["callee:00c53cd0:8"]]
+ 00c25074 ["INT_ADD", "register:40f0:8", ["const:c25074:8", "const:4:8"]]
+ 00c25074 ["CALL", null, ["callee:00c53cd0:8"]]
- 00c24c4c bytes 19bb0094
+ 00c25074 bytes 17bb0094
~~~


<a id="compare-ca93a30f9af7469552f9b9ef423a2df3"></a>

### [`00c24dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24dc8.md) → [`00c251f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c251f0.md) _ZNSt6__ndk16localeC1ERKS0_RKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEi

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c24df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24dc8.md#insn-00c24df0) · [`00c24e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24dc8.md#insn-00c24e04) · [`00c24e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24dc8.md#insn-00c24e14)
- 新版 [`00c25218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c251f0.md#insn-00c25218) · [`00c2522c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c251f0.md#insn-00c2522c) · [`00c2523c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c251f0.md#insn-00c2523c)

~~~diff
- 00c24df0 ["INT_ADD", "register:40f0:8", ["const:c24df0:8", "const:4:8"]]
- 00c24df0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00c25218 ["INT_ADD", "register:40f0:8", ["const:c25218:8", "const:4:8"]]
+ 00c25218 ["CALL", null, ["callee:00c57e90:8"]]
- 00c24df0 bytes 28cb0094
+ 00c25218 bytes 1ecb0094
- 00c24e04 ["INT_ADD", "register:40f0:8", ["const:c24e04:8", "const:4:8"]]
- 00c24e04 ["CALL", null, ["callee:00c21928:8"]]
+ 00c2522c ["INT_ADD", "register:40f0:8", ["const:c2522c:8", "const:4:8"]]
+ 00c2522c ["CALL", null, ["callee:00c21928:8"]]
- 00c24e04 bytes bff1ff97
+ 00c2522c bytes bff1ff97
- 00c24e14 ["INT_ADD", "register:40f0:8", ["const:c24e14:8", "const:4:8"]]
- 00c24e14 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00c2523c ["INT_ADD", "register:40f0:8", ["const:c2523c:8", "const:4:8"]]
+ 00c2523c ["CALL", null, ["callee:00c53cd0:8"]]
- 00c24e14 bytes a7ba0094
+ 00c2523c bytes a5ba0094
~~~


<a id="compare-20984b996454c2cb93846ba67b16da82"></a>

### [`00c24e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24e40.md) → [`00c25268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25268.md) _ZNSt6__ndk16localeC1ERKS0_S2_i

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c24e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24e40.md#insn-00c24e68) · [`00c24e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24e40.md#insn-00c24e7c) · [`00c24e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24e40.md#insn-00c24e8c)
- 新版 [`00c25290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25268.md#insn-00c25290) · [`00c252a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25268.md#insn-00c252a4) · [`00c252b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25268.md#insn-00c252b4)

~~~diff
- 00c24e68 ["INT_ADD", "register:40f0:8", ["const:c24e68:8", "const:4:8"]]
- 00c24e68 ["CALL", null, ["callee:00c57e90:8"]]
+ 00c25290 ["INT_ADD", "register:40f0:8", ["const:c25290:8", "const:4:8"]]
+ 00c25290 ["CALL", null, ["callee:00c57e90:8"]]
- 00c24e68 bytes 0acb0094
+ 00c25290 bytes 00cb0094
- 00c24e7c ["INT_ADD", "register:40f0:8", ["const:c24e7c:8", "const:4:8"]]
- 00c24e7c ["CALL", null, ["callee:00c21f78:8"]]
+ 00c252a4 ["INT_ADD", "register:40f0:8", ["const:c252a4:8", "const:4:8"]]
+ 00c252a4 ["CALL", null, ["callee:00c21f78:8"]]
- 00c24e7c bytes 35f3ff97
+ 00c252a4 bytes 35f3ff97
- 00c24e8c ["INT_ADD", "register:40f0:8", ["const:c24e8c:8", "const:4:8"]]
- 00c24e8c ["CALL", null, ["callee:00c53cd0:8"]]
+ 00c252b4 ["INT_ADD", "register:40f0:8", ["const:c252b4:8", "const:4:8"]]
+ 00c252b4 ["CALL", null, ["callee:00c53cd0:8"]]
- 00c24e8c bytes 89ba0094
+ 00c252b4 bytes 87ba0094
~~~


<a id="compare-9df135db2c6c1d5483dbb89db87fe6fd"></a>

### [`00c25308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25308.md) → [`00c25730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25730.md) _ZNKSt6__ndk16localeeqERKS0_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c253b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25308.md#insn-00c253b4)
- 新版 [`00c257dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25730.md#insn-00c257dc)

~~~diff
- 00c253b4 ["INT_ADD", "register:40f0:8", ["const:c253b4:8", "const:4:8"]]
- 00c253b4 ["CALL", null, ["callee:00c58050:8"]]
+ 00c257dc ["INT_ADD", "register:40f0:8", ["const:c257dc:8", "const:4:8"]]
+ 00c257dc ["CALL", null, ["callee:00c58050:8"]]
- 00c253b4 bytes 27ca0094
+ 00c257dc bytes 1dca0094
~~~


<a id="compare-fac2ee8567b271c0b3b2a17f11d98ae1"></a>

### [`00c253f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c253f8.md) → [`00c25820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25820.md) _ZNSt6__ndk16locale5facetD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e510.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e910.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2540c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c253f8.md#insn-00c2540c)
- 新版 [`00c25834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25820.md#insn-00c25834)

~~~diff
- 00c2540c ["INT_ADD", "register:40f0:8", ["const:c2540c:8", "const:4:8"]]
- 00c2540c ["CALL", null, ["callee:00c5e910:8"]]
+ 00c25834 ["INT_ADD", "register:40f0:8", ["const:c25834:8", "const:4:8"]]
+ 00c25834 ["CALL", null, ["callee:00c5e910:8"]]
- 00c2540c bytes 41e40094
+ 00c25834 bytes 37e40094
~~~


<a id="compare-8f98787e372485f9161d7f4ab1982939"></a>

### [`00c2550c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c2550c.md) → [`00c25934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md) FUN_00c25934

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 13件 [`00c25434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25434.md) [`00c25a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25a78.md) [`00c26d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26d70.md) [`00c272e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c272e8.md) [`00c27e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27e84.md) · 呼出先 2件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c58bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bd0.md)
- 新版 呼出元 13件 [`00c2585c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c2585c.md) [`00c25ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25ea0.md) [`00c27198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27198.md) [`00c27710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27710.md) [`00c282ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c282ac.md) · 呼出先 2件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2552c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c2550c.md#insn-00c2552c) · [`00c25540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c2550c.md#insn-00c25540)
- 新版 [`00c25954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md#insn-00c25954) · [`00c25968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md#insn-00c25968)

~~~diff
- 00c2552c ["INT_ADD", "register:40f0:8", ["const:c2552c:8", "const:4:8"]]
- 00c2552c ["CALL", null, ["callee:00c57fe0:8"]]
+ 00c25954 ["INT_ADD", "register:40f0:8", ["const:c25954:8", "const:4:8"]]
+ 00c25954 ["CALL", null, ["callee:00c57fe0:8"]]
- 00c2552c bytes adc90094
+ 00c25954 bytes a3c90094
- 00c25540 ["INT_ADD", "register:40f0:8", ["const:c25540:8", "const:4:8"]]
- 00c25540 ["CALL", null, ["callee:00c58fd0:8"]]
+ 00c25968 ["INT_ADD", "register:40f0:8", ["const:c25968:8", "const:4:8"]]
+ 00c25968 ["CALL", null, ["callee:00c58fd0:8"]]
- 00c25540 bytes a4cd0094
+ 00c25968 bytes 9acd0094
~~~


<a id="compare-7a21f2761de668490230ec6b4d49a9fd"></a>

### [`00c25678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25678.md) → [`00c25aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25aa0.md) _ZNSt6__ndk114collate_bynameIcED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e520.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e920.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2568c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25678.md#insn-00c2568c)
- 新版 [`00c25ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25aa0.md#insn-00c25ab4)

~~~diff
- 00c2568c ["INT_ADD", "register:40f0:8", ["const:c2568c:8", "const:4:8"]]
- 00c2568c ["CALL", null, ["callee:00c5e920:8"]]
+ 00c25ab4 ["INT_ADD", "register:40f0:8", ["const:c25ab4:8", "const:4:8"]]
+ 00c25ab4 ["CALL", null, ["callee:00c5e920:8"]]
- 00c2568c bytes a5e30094
+ 00c25ab4 bytes 9be30094
~~~


<a id="compare-ed5b6471b8263bf0352820d5b18ee920"></a>

### [`00c256a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c256a4.md) → [`00c25acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25acc.md) _ZNKSt6__ndk114collate_bynameIcE10do_compareEPKcS3_S3_S3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5e530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e530.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5e930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e930.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c25724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c256a4.md#insn-00c25724) · [`00c2574c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c256a4.md#insn-00c2574c) · [`00c25790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c256a4.md#insn-00c25790)
- 新版 [`00c25b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25acc.md#insn-00c25b4c) · [`00c25b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25acc.md#insn-00c25b74) · [`00c25bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25acc.md#insn-00c25bb8)

~~~diff
- 00c25724 ["INT_ADD", "register:40f0:8", ["const:c25724:8", "const:4:8"]]
- 00c25724 ["CALL", null, ["callee:00c57e90:8"]]
+ 00c25b4c ["INT_ADD", "register:40f0:8", ["const:c25b4c:8", "const:4:8"]]
+ 00c25b4c ["CALL", null, ["callee:00c57e90:8"]]
- 00c25724 bytes dbc80094
+ 00c25b4c bytes d1c80094
- 00c2574c ["INT_ADD", "register:40f0:8", ["const:c2574c:8", "const:4:8"]]
- 00c2574c ["CALL", null, ["callee:00c58000:8"]]
+ 00c25b74 ["INT_ADD", "register:40f0:8", ["const:c25b74:8", "const:4:8"]]
+ 00c25b74 ["CALL", null, ["callee:00c58000:8"]]
- 00c2574c bytes 2dc90094
+ 00c25b74 bytes 23c90094
- 00c25790 ["INT_ADD", "register:40f0:8", ["const:c25790:8", "const:4:8"]]
- 00c25790 ["CALL", null, ["callee:00c58000:8"]]
+ 00c25bb8 ["INT_ADD", "register:40f0:8", ["const:c25bb8:8", "const:4:8"]]
+ 00c25bb8 ["CALL", null, ["callee:00c58000:8"]]
- 00c25790 bytes 1cc90094
+ 00c25bb8 bytes 12c90094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-933f7d1ae2c45304384d3738b214cf69"></a>

### [`00c2587c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c2587c.md) → [`00c25ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25ca4.md) _ZNKSt6__ndk114collate_bynameIcE12do_transformEPKcS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c258f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c2587c.md#insn-00c258f4) · [`00c2591c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c2587c.md#insn-00c2591c) · [`00c25948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c2587c.md#insn-00c25948)
- 新版 [`00c25d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25ca4.md#insn-00c25d1c) · [`00c25d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25ca4.md#insn-00c25d44) · [`00c25d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25ca4.md#insn-00c25d70)

~~~diff
- 00c258f4 ["INT_ADD", "register:40f0:8", ["const:c258f4:8", "const:4:8"]]
- 00c258f4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00c25d1c ["INT_ADD", "register:40f0:8", ["const:c25d1c:8", "const:4:8"]]
+ 00c25d1c ["CALL", null, ["callee:00c57e90:8"]]
- 00c258f4 bytes 67c80094
+ 00c25d1c bytes 5dc80094
- 00c2591c ["INT_ADD", "register:40f0:8", ["const:c2591c:8", "const:4:8"]]
- 00c2591c ["CALL", null, ["callee:00c58000:8"]]
+ 00c25d44 ["INT_ADD", "register:40f0:8", ["const:c25d44:8", "const:4:8"]]
+ 00c25d44 ["CALL", null, ["callee:00c58000:8"]]
- 00c2591c bytes b9c80094
+ 00c25d44 bytes afc80094
- 00c25948 ["INT_ADD", "register:40f0:8", ["const:c25948:8", "const:4:8"]]
- 00c25948 ["CALL", null, ["callee:00c5e940:8"]]
+ 00c25d70 ["INT_ADD", "register:40f0:8", ["const:c25d70:8", "const:4:8"]]
+ 00c25d70 ["CALL", null, ["callee:00c5e940:8"]]
- 00c25948 bytes fee20094
+ 00c25d70 bytes f4e20094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c872c6fd1d448fcb7aa02c4ffc63a03b"></a>

### [`00c25c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25c58.md) → [`00c26080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26080.md) _ZNSt6__ndk114collate_bynameIwED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e550.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e950.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c25c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25c58.md#insn-00c25c6c)
- 新版 [`00c26094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26080.md#insn-00c26094)

~~~diff
- 00c25c6c ["INT_ADD", "register:40f0:8", ["const:c25c6c:8", "const:4:8"]]
- 00c25c6c ["CALL", null, ["callee:00c5e950:8"]]
+ 00c26094 ["INT_ADD", "register:40f0:8", ["const:c26094:8", "const:4:8"]]
+ 00c26094 ["CALL", null, ["callee:00c5e950:8"]]
- 00c25c6c bytes 39e20094
+ 00c26094 bytes 2fe20094
~~~


<a id="compare-ca9be685db46b95a72fc7046f1d82294"></a>

### [`00c25c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25c84.md) → [`00c260ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c260ac.md) _ZNKSt6__ndk114collate_bynameIwE10do_compareEPKwS3_S3_S3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 6件 [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c25d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25c84.md#insn-00c25d18) · [`00c25d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25c84.md#insn-00c25d4c) · [`00c25da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25c84.md#insn-00c25da4)
- 新版 [`00c26140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c260ac.md#insn-00c26140) · [`00c26174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c260ac.md#insn-00c26174) · [`00c261cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c260ac.md#insn-00c261cc)

~~~diff
- 00c25d18 ["INT_ADD", "register:40f0:8", ["const:c25d18:8", "const:4:8"]]
- 00c25d18 ["CALL", null, ["callee:00c57e90:8"]]
+ 00c26140 ["INT_ADD", "register:40f0:8", ["const:c26140:8", "const:4:8"]]
+ 00c26140 ["CALL", null, ["callee:00c57e90:8"]]
- 00c25d18 bytes 5ec70094
+ 00c26140 bytes 54c70094
- 00c25d4c ["INT_ADD", "register:40f0:8", ["const:c25d4c:8", "const:4:8"]]
- 00c25d4c ["CALL", null, ["callee:00c58000:8"]]
+ 00c26174 ["INT_ADD", "register:40f0:8", ["const:c26174:8", "const:4:8"]]
+ 00c26174 ["CALL", null, ["callee:00c58000:8"]]
- 00c25d4c bytes adc70094
+ 00c26174 bytes a3c70094
- 00c25da4 ["INT_ADD", "register:40f0:8", ["const:c25da4:8", "const:4:8"]]
- 00c25da4 ["CALL", null, ["callee:00c58000:8"]]
+ 00c261cc ["INT_ADD", "register:40f0:8", ["const:c261cc:8", "const:4:8"]]
+ 00c261cc ["CALL", null, ["callee:00c58000:8"]]
- 00c25da4 bytes 97c70094
+ 00c261cc bytes 8dc70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fd88948edadfd4d54f04c6155cbaa36"></a>

### [`00c25e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25e9c.md) → [`00c262c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c262c4.md) _ZNKSt6__ndk114collate_bynameIwE12do_transformEPKwS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c25f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25e9c.md#insn-00c25f28) · [`00c25f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25e9c.md#insn-00c25f5c) · [`00c25f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25e9c.md#insn-00c25f8c)
- 新版 [`00c26350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c262c4.md#insn-00c26350) · [`00c26384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c262c4.md#insn-00c26384) · [`00c263b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c262c4.md#insn-00c263b4)

~~~diff
- 00c25f28 ["INT_ADD", "register:40f0:8", ["const:c25f28:8", "const:4:8"]]
- 00c25f28 ["CALL", null, ["callee:00c57e90:8"]]
+ 00c26350 ["INT_ADD", "register:40f0:8", ["const:c26350:8", "const:4:8"]]
+ 00c26350 ["CALL", null, ["callee:00c57e90:8"]]
- 00c25f28 bytes dac60094
+ 00c26350 bytes d0c60094
- 00c25f5c ["INT_ADD", "register:40f0:8", ["const:c25f5c:8", "const:4:8"]]
- 00c25f5c ["CALL", null, ["callee:00c58000:8"]]
+ 00c26384 ["INT_ADD", "register:40f0:8", ["const:c26384:8", "const:4:8"]]
+ 00c26384 ["CALL", null, ["callee:00c58000:8"]]
- 00c25f5c bytes 29c70094
+ 00c26384 bytes 1fc70094
- 00c25f8c ["INT_ADD", "register:40f0:8", ["const:c25f8c:8", "const:4:8"]]
- 00c25f8c ["CALL", null, ["callee:00c5e970:8"]]
+ 00c263b4 ["INT_ADD", "register:40f0:8", ["const:c263b4:8", "const:4:8"]]
+ 00c263b4 ["CALL", null, ["callee:00c5e970:8"]]
- 00c25f8c bytes 79e10094
+ 00c263b4 bytes 6fe10094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-208e23d3214b2c345286f94b4ae94c02"></a>

### [`00c260d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c260d0.md) → [`00c264f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c264f8.md) _ZNSt6__ndk15ctypeIwED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e580.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e980.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c260e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c260d0.md#insn-00c260e4)
- 新版 [`00c2650c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c264f8.md#insn-00c2650c)

~~~diff
- 00c260e4 ["INT_ADD", "register:40f0:8", ["const:c260e4:8", "const:4:8"]]
- 00c260e4 ["CALL", null, ["callee:00c5e980:8"]]
+ 00c2650c ["INT_ADD", "register:40f0:8", ["const:c2650c:8", "const:4:8"]]
+ 00c2650c ["CALL", null, ["callee:00c5e980:8"]]
- 00c260e4 bytes 27e10094
+ 00c2650c bytes 1de10094
~~~


<a id="compare-1b0504e3bbd3c0669422e926859395ed"></a>

### [`00c2686c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c2686c.md) → [`00c26c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26c94.md) _ZNSt6__ndk15ctypeIcED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e5b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e9b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c26880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c2686c.md#insn-00c26880)
- 新版 [`00c26ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26c94.md#insn-00c26ca8)

~~~diff
- 00c26880 ["INT_ADD", "register:40f0:8", ["const:c26880:8", "const:4:8"]]
- 00c26880 ["CALL", null, ["callee:00c5e9b0:8"]]
+ 00c26ca8 ["INT_ADD", "register:40f0:8", ["const:c26ca8:8", "const:4:8"]]
+ 00c26ca8 ["CALL", null, ["callee:00c5e9b0:8"]]
- 00c26880 bytes 4cdf0094
+ 00c26ca8 bytes 42df0094
~~~


<a id="compare-1299349394d78863ccfb7fa42acf390a"></a>

### [`00c26f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26f2c.md) → [`00c27354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27354.md) _ZNSt6__ndk112ctype_bynameIcED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e5e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e9e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c26f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26f2c.md#insn-00c26f40)
- 新版 [`00c27368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27354.md#insn-00c27368)

~~~diff
- 00c26f40 ["INT_ADD", "register:40f0:8", ["const:c26f40:8", "const:4:8"]]
- 00c26f40 ["CALL", null, ["callee:00c5e9e0:8"]]
+ 00c27368 ["INT_ADD", "register:40f0:8", ["const:c27368:8", "const:4:8"]]
+ 00c27368 ["CALL", null, ["callee:00c5e9e0:8"]]
- 00c26f40 bytes a8dd0094
+ 00c27368 bytes 9edd0094
~~~


<a id="compare-2f8a79121547dd81535183731366a925"></a>

### [`00c27484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27484.md) → [`00c278ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c278ac.md) _ZNSt6__ndk112ctype_bynameIwED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e620.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ea20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c27498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27484.md#insn-00c27498)
- 新版 [`00c278c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c278ac.md#insn-00c278c0)

~~~diff
- 00c27498 ["INT_ADD", "register:40f0:8", ["const:c27498:8", "const:4:8"]]
- 00c27498 ["CALL", null, ["callee:00c5ea20:8"]]
+ 00c278c0 ["INT_ADD", "register:40f0:8", ["const:c278c0:8", "const:4:8"]]
+ 00c278c0 ["CALL", null, ["callee:00c5ea20:8"]]
- 00c27498 bytes 62dc0094
+ 00c278c0 bytes 58dc0094
~~~


<a id="compare-086cf62ae31298bfcc5f3ef6ea7b4aa3"></a>

### [`00c274b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c274b0.md) → [`00c278d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c278d8.md) _ZNKSt6__ndk112ctype_bynameIwE5do_isEmw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 10件 [`00c5e590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e590.md) [`00c5e630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e630.md) [`00c5e640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e640.md) [`00c5e650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e650.md) [`00c5e660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e660.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00c5e990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e990.md) [`00c5ea30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea30.md) [`00c5ea40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea40.md) [`00c5ea50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea50.md) [`00c5ea60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c274e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c274b0.md#insn-00c274e8) · [`00c27500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c274b0.md#insn-00c27500) · [`00c27534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c274b0.md#insn-00c27534)
- 新版 [`00c27910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c278d8.md#insn-00c27910) · [`00c27928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c278d8.md#insn-00c27928) · [`00c2795c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c278d8.md#insn-00c2795c)

~~~diff
- 00c274e8 ["INT_ADD", "register:40f0:8", ["const:c274e8:8", "const:4:8"]]
- 00c274e8 ["CALL", null, ["callee:00c5ea30:8"]]
+ 00c27910 ["INT_ADD", "register:40f0:8", ["const:c27910:8", "const:4:8"]]
+ 00c27910 ["CALL", null, ["callee:00c5ea30:8"]]
- 00c274e8 bytes 52dc0094
+ 00c27910 bytes 48dc0094
- 00c27500 ["INT_ADD", "register:40f0:8", ["const:c27500:8", "const:4:8"]]
- 00c27500 ["CALL", null, ["callee:00c5ea40:8"]]
+ 00c27928 ["INT_ADD", "register:40f0:8", ["const:c27928:8", "const:4:8"]]
+ 00c27928 ["CALL", null, ["callee:00c5ea40:8"]]
- 00c27500 bytes 50dc0094
+ 00c27928 bytes 46dc0094
- 00c27534 ["INT_ADD", "register:40f0:8", ["const:c27534:8", "const:4:8"]]
- 00c27534 ["CALL", null, ["callee:00c5ea50:8"]]
+ 00c2795c ["INT_ADD", "register:40f0:8", ["const:c2795c:8", "const:4:8"]]
+ 00c2795c ["CALL", null, ["callee:00c5ea50:8"]]
- 00c27534 bytes 47dc0094
+ 00c2795c bytes 3ddc0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42057a78d34aa7fb4f69aff5d06cce89"></a>

### [`00c277a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c277a0.md) → [`00c27bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27bc8.md) _ZNKSt6__ndk112ctype_bynameIwE10do_scan_isEmPKwS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 10件 [`00c5e590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e590.md) [`00c5e630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e630.md) [`00c5e640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e640.md) [`00c5e650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e650.md) [`00c5e660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e660.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00c5e990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e990.md) [`00c5ea30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea30.md) [`00c5ea40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea40.md) [`00c5ea50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea50.md) [`00c5ea60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c277f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c277a0.md#insn-00c277f0) · [`00c27804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c277a0.md#insn-00c27804) · [`00c27818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c277a0.md#insn-00c27818)
- 新版 [`00c27c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27bc8.md#insn-00c27c18) · [`00c27c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27bc8.md#insn-00c27c2c) · [`00c27c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27bc8.md#insn-00c27c40)

~~~diff
- 00c277f0 ["INT_ADD", "register:40f0:8", ["const:c277f0:8", "const:4:8"]]
- 00c277f0 ["CALL", null, ["callee:00c5ea30:8"]]
+ 00c27c18 ["INT_ADD", "register:40f0:8", ["const:c27c18:8", "const:4:8"]]
+ 00c27c18 ["CALL", null, ["callee:00c5ea30:8"]]
- 00c277f0 bytes 90db0094
+ 00c27c18 bytes 86db0094
- 00c27804 ["INT_ADD", "register:40f0:8", ["const:c27804:8", "const:4:8"]]
- 00c27804 ["CALL", null, ["callee:00c5ea40:8"]]
+ 00c27c2c ["INT_ADD", "register:40f0:8", ["const:c27c2c:8", "const:4:8"]]
+ 00c27c2c ["CALL", null, ["callee:00c5ea40:8"]]
- 00c27804 bytes 8fdb0094
+ 00c27c2c bytes 85db0094
- 00c27818 ["INT_ADD", "register:40f0:8", ["const:c27818:8", "const:4:8"]]
- 00c27818 ["CALL", null, ["callee:00c5ea60:8"]]
+ 00c27c40 ["INT_ADD", "register:40f0:8", ["const:c27c40:8", "const:4:8"]]
+ 00c27c40 ["CALL", null, ["callee:00c5ea60:8"]]
- 00c27818 bytes 92db0094
+ 00c27c40 bytes 88db0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8241b47ff910a65575cb119c4c9f49b3"></a>

### [`00c278d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c278d0.md) → [`00c27cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27cf8.md) _ZNKSt6__ndk112ctype_bynameIwE11do_scan_notEmPKwS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 10件 [`00c5e590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e590.md) [`00c5e630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e630.md) [`00c5e640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e640.md) [`00c5e650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e650.md) [`00c5e660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e660.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00c5e990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e990.md) [`00c5ea30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea30.md) [`00c5ea40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea40.md) [`00c5ea50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea50.md) [`00c5ea60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2790c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c278d0.md#insn-00c2790c) · [`00c27934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c278d0.md#insn-00c27934) · [`00c27948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c278d0.md#insn-00c27948)
- 新版 [`00c27d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27cf8.md#insn-00c27d34) · [`00c27d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27cf8.md#insn-00c27d5c) · [`00c27d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27cf8.md#insn-00c27d70)

~~~diff
- 00c2790c ["INT_ADD", "register:40f0:8", ["const:c2790c:8", "const:4:8"]]
- 00c2790c ["CALL", null, ["callee:00c5ea30:8"]]
+ 00c27d34 ["INT_ADD", "register:40f0:8", ["const:c27d34:8", "const:4:8"]]
+ 00c27d34 ["CALL", null, ["callee:00c5ea30:8"]]
- 00c2790c bytes 49db0094
+ 00c27d34 bytes 3fdb0094
- 00c27934 ["INT_ADD", "register:40f0:8", ["const:c27934:8", "const:4:8"]]
- 00c27934 ["CALL", null, ["callee:00c5ea40:8"]]
+ 00c27d5c ["INT_ADD", "register:40f0:8", ["const:c27d5c:8", "const:4:8"]]
+ 00c27d5c ["CALL", null, ["callee:00c5ea40:8"]]
- 00c27934 bytes 43db0094
+ 00c27d5c bytes 39db0094
- 00c27948 ["INT_ADD", "register:40f0:8", ["const:c27948:8", "const:4:8"]]
- 00c27948 ["CALL", null, ["callee:00c5ea60:8"]]
+ 00c27d70 ["INT_ADD", "register:40f0:8", ["const:c27d70:8", "const:4:8"]]
+ 00c27d70 ["CALL", null, ["callee:00c5ea60:8"]]
- 00c27948 bytes 46db0094
+ 00c27d70 bytes 3cdb0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f39c31b2a960c17ca11009461e4833b5"></a>

### [`00c27a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27a14.md) → [`00c27e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27e3c.md) _ZNKSt6__ndk112ctype_bynameIwE10do_toupperEPwPKw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e6c0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5eac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c27a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27a14.md#insn-00c27a44)
- 新版 [`00c27e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27e3c.md#insn-00c27e6c)

~~~diff
- 00c27a44 ["INT_ADD", "register:40f0:8", ["const:c27a44:8", "const:4:8"]]
- 00c27a44 ["CALL", null, ["callee:00c5eac0:8"]]
+ 00c27e6c ["INT_ADD", "register:40f0:8", ["const:c27e6c:8", "const:4:8"]]
+ 00c27e6c ["CALL", null, ["callee:00c5eac0:8"]]
- 00c27a44 bytes 1fdb0094
+ 00c27e6c bytes 15db0094
~~~


<a id="compare-aba98d7e70794ea7eb0920c6a3afeab9"></a>

### [`00c27a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27a84.md) → [`00c27eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27eac.md) _ZNKSt6__ndk112ctype_bynameIwE10do_tolowerEPwPKw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e6d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ead0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ead0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c27ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27a84.md#insn-00c27ab4)
- 新版 [`00c27edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27eac.md#insn-00c27edc)

~~~diff
- 00c27ab4 ["INT_ADD", "register:40f0:8", ["const:c27ab4:8", "const:4:8"]]
- 00c27ab4 ["CALL", null, ["callee:00c5ead0:8"]]
+ 00c27edc ["INT_ADD", "register:40f0:8", ["const:c27edc:8", "const:4:8"]]
+ 00c27edc ["CALL", null, ["callee:00c5ead0:8"]]
- 00c27ab4 bytes 07db0094
+ 00c27edc bytes fdda0094
~~~


<a id="compare-4c93ca987c9bcb6ea0f66773296d1ada"></a>

### [`00c27ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27ae0.md) → [`00c27f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27f08.md) _ZNKSt6__ndk112ctype_bynameIwE8do_widenEc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e170.md) [`00c5e6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e6e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5eae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c27afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27ae0.md#insn-00c27afc) · [`00c27b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27ae0.md#insn-00c27b0c) · [`00c27b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27ae0.md#insn-00c27b1c)
- 新版 [`00c27f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27f08.md#insn-00c27f24) · [`00c27f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27f08.md#insn-00c27f34) · [`00c27f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27f08.md#insn-00c27f44)

~~~diff
- 00c27afc ["INT_ADD", "register:40f0:8", ["const:c27afc:8", "const:4:8"]]
- 00c27afc ["CALL", null, ["callee:00c5e570:8"]]
+ 00c27f24 ["INT_ADD", "register:40f0:8", ["const:c27f24:8", "const:4:8"]]
+ 00c27f24 ["CALL", null, ["callee:00c5e570:8"]]
- 00c27afc bytes 9dd90094
+ 00c27f24 bytes 93d90094
- 00c27b0c ["INT_ADD", "register:40f0:8", ["const:c27b0c:8", "const:4:8"]]
- 00c27b0c ["CALL", null, ["callee:00c5eae0:8"]]
+ 00c27f34 ["INT_ADD", "register:40f0:8", ["const:c27f34:8", "const:4:8"]]
+ 00c27f34 ["CALL", null, ["callee:00c5eae0:8"]]
- 00c27b0c bytes f5da0094
+ 00c27f34 bytes ebda0094
- 00c27b1c ["INT_ADD", "register:40f0:8", ["const:c27b1c:8", "const:4:8"]]
- 00c27b1c ["CALL", null, ["callee:00c5e570:8"]]
+ 00c27f44 ["INT_ADD", "register:40f0:8", ["const:c27f44:8", "const:4:8"]]
+ 00c27f44 ["CALL", null, ["callee:00c5e570:8"]]
- 00c27b1c bytes 95d90094
+ 00c27f44 bytes 8bd90094
~~~


<a id="compare-0c7c2fb406bae1e901c17974ef395a70"></a>

### [`00c27b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27b50.md) → [`00c27f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27f78.md) _ZNKSt6__ndk112ctype_bynameIwE8do_widenEPKcS3_Pw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e170.md) [`00c5e6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e6e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5eae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c27ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27b50.md#insn-00c27ba0) · [`00c27bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27b50.md#insn-00c27bb0) · [`00c27bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27b50.md#insn-00c27bc0)
- 新版 [`00c27fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27f78.md#insn-00c27fc8) · [`00c27fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27f78.md#insn-00c27fd8) · [`00c27fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27f78.md#insn-00c27fe8)

~~~diff
- 00c27ba0 ["INT_ADD", "register:40f0:8", ["const:c27ba0:8", "const:4:8"]]
- 00c27ba0 ["CALL", null, ["callee:00c5e570:8"]]
+ 00c27fc8 ["INT_ADD", "register:40f0:8", ["const:c27fc8:8", "const:4:8"]]
+ 00c27fc8 ["CALL", null, ["callee:00c5e570:8"]]
- 00c27ba0 bytes 74d90094
+ 00c27fc8 bytes 6ad90094
- 00c27bb0 ["INT_ADD", "register:40f0:8", ["const:c27bb0:8", "const:4:8"]]
- 00c27bb0 ["CALL", null, ["callee:00c5eae0:8"]]
+ 00c27fd8 ["INT_ADD", "register:40f0:8", ["const:c27fd8:8", "const:4:8"]]
+ 00c27fd8 ["CALL", null, ["callee:00c5eae0:8"]]
- 00c27bb0 bytes ccda0094
+ 00c27fd8 bytes c2da0094
- 00c27bc0 ["INT_ADD", "register:40f0:8", ["const:c27bc0:8", "const:4:8"]]
- 00c27bc0 ["CALL", null, ["callee:00c5e570:8"]]
+ 00c27fe8 ["INT_ADD", "register:40f0:8", ["const:c27fe8:8", "const:4:8"]]
+ 00c27fe8 ["CALL", null, ["callee:00c5e570:8"]]
- 00c27bc0 bytes 6cd90094
+ 00c27fe8 bytes 62d90094
~~~


<a id="compare-2e45741c9cb9ecb5672ec8b5f8104ef3"></a>

### [`00c27c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27c04.md) → [`00c2802c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c2802c.md) _ZNKSt6__ndk112ctype_bynameIwE9do_narrowEwc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e170.md) [`00c5e6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e6f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5eaf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eaf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c27c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27c04.md#insn-00c27c24) · [`00c27c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27c04.md#insn-00c27c34) · [`00c27c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27c04.md#insn-00c27c44)
- 新版 [`00c2804c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c2802c.md#insn-00c2804c) · [`00c2805c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c2802c.md#insn-00c2805c) · [`00c2806c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c2802c.md#insn-00c2806c)

~~~diff
- 00c27c24 ["INT_ADD", "register:40f0:8", ["const:c27c24:8", "const:4:8"]]
- 00c27c24 ["CALL", null, ["callee:00c5e570:8"]]
+ 00c2804c ["INT_ADD", "register:40f0:8", ["const:c2804c:8", "const:4:8"]]
+ 00c2804c ["CALL", null, ["callee:00c5e570:8"]]
- 00c27c24 bytes 53d90094
+ 00c2804c bytes 49d90094
- 00c27c34 ["INT_ADD", "register:40f0:8", ["const:c27c34:8", "const:4:8"]]
- 00c27c34 ["CALL", null, ["callee:00c5eaf0:8"]]
+ 00c2805c ["INT_ADD", "register:40f0:8", ["const:c2805c:8", "const:4:8"]]
+ 00c2805c ["CALL", null, ["callee:00c5eaf0:8"]]
- 00c27c34 bytes afda0094
+ 00c2805c bytes a5da0094
- 00c27c44 ["INT_ADD", "register:40f0:8", ["const:c27c44:8", "const:4:8"]]
- 00c27c44 ["CALL", null, ["callee:00c5e570:8"]]
+ 00c2806c ["INT_ADD", "register:40f0:8", ["const:c2806c:8", "const:4:8"]]
+ 00c2806c ["CALL", null, ["callee:00c5e570:8"]]
- 00c27c44 bytes 4bd90094
+ 00c2806c bytes 41d90094
~~~


<a id="compare-32e9d15051dedb716ceb986d4a3e21b4"></a>

### [`00c27c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27c7c.md) → [`00c280a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c280a4.md) _ZNKSt6__ndk112ctype_bynameIwE9do_narrowEPKwS3_cPc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e170.md) [`00c5e6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e6f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5eaf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eaf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c27cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27c7c.md#insn-00c27cd8) · [`00c27ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27c7c.md#insn-00c27ce8) · [`00c27cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27c7c.md#insn-00c27cf8)
- 新版 [`00c28100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c280a4.md#insn-00c28100) · [`00c28110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c280a4.md#insn-00c28110) · [`00c28120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c280a4.md#insn-00c28120)

~~~diff
- 00c27cd8 ["INT_ADD", "register:40f0:8", ["const:c27cd8:8", "const:4:8"]]
- 00c27cd8 ["CALL", null, ["callee:00c5e570:8"]]
+ 00c28100 ["INT_ADD", "register:40f0:8", ["const:c28100:8", "const:4:8"]]
+ 00c28100 ["CALL", null, ["callee:00c5e570:8"]]
- 00c27cd8 bytes 26d90094
+ 00c28100 bytes 1cd90094
- 00c27ce8 ["INT_ADD", "register:40f0:8", ["const:c27ce8:8", "const:4:8"]]
- 00c27ce8 ["CALL", null, ["callee:00c5eaf0:8"]]
+ 00c28110 ["INT_ADD", "register:40f0:8", ["const:c28110:8", "const:4:8"]]
+ 00c28110 ["CALL", null, ["callee:00c5eaf0:8"]]
- 00c27ce8 bytes 82da0094
+ 00c28110 bytes 78da0094
- 00c27cf8 ["INT_ADD", "register:40f0:8", ["const:c27cf8:8", "const:4:8"]]
- 00c27cf8 ["CALL", null, ["callee:00c5e570:8"]]
+ 00c28120 ["INT_ADD", "register:40f0:8", ["const:c28120:8", "const:4:8"]]
+ 00c28120 ["CALL", null, ["callee:00c5e570:8"]]
- 00c27cf8 bytes 1ed90094
+ 00c28120 bytes 14d90094
~~~


<a id="compare-8127bea76c819887b3f22c0020bd43cf"></a>

### [`00c27d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27d3c.md) → [`00c28164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28164.md) _ZNSt6__ndk17codecvtIcc9mbstate_tED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e700.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5eb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c27d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27d3c.md#insn-00c27d50)
- 新版 [`00c28178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28164.md#insn-00c28178)

~~~diff
- 00c27d50 ["INT_ADD", "register:40f0:8", ["const:c27d50:8", "const:4:8"]]
- 00c27d50 ["CALL", null, ["callee:00c5eb00:8"]]
+ 00c28178 ["INT_ADD", "register:40f0:8", ["const:c28178:8", "const:4:8"]]
+ 00c28178 ["CALL", null, ["callee:00c5eb00:8"]]
- 00c27d50 bytes 6cda0094
+ 00c28178 bytes 62da0094
~~~


<a id="compare-527d46c13786c971b5c0606d50d13e32"></a>

### [`00c27f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27f5c.md) → [`00c28384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28384.md) _ZNSt6__ndk17codecvtIwc9mbstate_tED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e710.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5eb10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c27f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27f5c.md#insn-00c27f70)
- 新版 [`00c28398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28384.md#insn-00c28398)

~~~diff
- 00c27f70 ["INT_ADD", "register:40f0:8", ["const:c27f70:8", "const:4:8"]]
- 00c27f70 ["CALL", null, ["callee:00c5eb10:8"]]
+ 00c28398 ["INT_ADD", "register:40f0:8", ["const:c28398:8", "const:4:8"]]
+ 00c28398 ["CALL", null, ["callee:00c5eb10:8"]]
- 00c27f70 bytes e8d90094
+ 00c28398 bytes ded90094
~~~


<a id="compare-14ca8ea2058b72a4746f900a73ed027a"></a>

### [`00c27f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27f88.md) → [`00c283b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c283b0.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE6do_outERS1_PKwS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5e170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e170.md) [`00c5e720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e720.md) [`00c5e730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e730.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5eb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb20.md) [`00c5eb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2803c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27f88.md#insn-00c2803c) · [`00c2805c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27f88.md#insn-00c2805c) · [`00c2806c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27f88.md#insn-00c2806c)
- 新版 [`00c28464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c283b0.md#insn-00c28464) · [`00c28484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c283b0.md#insn-00c28484) · [`00c28494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c283b0.md#insn-00c28494)

~~~diff
- 00c2803c ["INT_ADD", "register:40f0:8", ["const:c2803c:8", "const:4:8"]]
- 00c2803c ["CALL", null, ["callee:00c5e570:8"]]
+ 00c28464 ["INT_ADD", "register:40f0:8", ["const:c28464:8", "const:4:8"]]
+ 00c28464 ["CALL", null, ["callee:00c5e570:8"]]
- 00c2803c bytes 4dd80094
+ 00c28464 bytes 43d80094
- 00c2805c ["INT_ADD", "register:40f0:8", ["const:c2805c:8", "const:4:8"]]
- 00c2805c ["CALL", null, ["callee:00c5eb20:8"]]
+ 00c28484 ["INT_ADD", "register:40f0:8", ["const:c28484:8", "const:4:8"]]
+ 00c28484 ["CALL", null, ["callee:00c5eb20:8"]]
- 00c2805c bytes b1d90094
+ 00c28484 bytes a7d90094
- 00c2806c ["INT_ADD", "register:40f0:8", ["const:c2806c:8", "const:4:8"]]
- 00c2806c ["CALL", null, ["callee:00c5e570:8"]]
+ 00c28494 ["INT_ADD", "register:40f0:8", ["const:c28494:8", "const:4:8"]]
+ 00c28494 ["CALL", null, ["callee:00c5e570:8"]]
- 00c2806c bytes 41d80094
+ 00c28494 bytes 37d80094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c66956b37c05b43af8e7748673aef21"></a>

### [`00c2824c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c2824c.md) → [`00c28674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28674.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE5do_inERS1_PKcS5_RS5_PwS7_RS7_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5e170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e170.md) [`00c5e740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e740.md) [`00c5e750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e750.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5eb40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb40.md) [`00c5eb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c282ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c2824c.md#insn-00c282ec) · [`00c2830c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c2824c.md#insn-00c2830c) · [`00c2831c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c2824c.md#insn-00c2831c)
- 新版 [`00c28714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28674.md#insn-00c28714) · [`00c28734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28674.md#insn-00c28734) · [`00c28744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28674.md#insn-00c28744)

~~~diff
- 00c282ec ["INT_ADD", "register:40f0:8", ["const:c282ec:8", "const:4:8"]]
- 00c282ec ["CALL", null, ["callee:00c5e570:8"]]
+ 00c28714 ["INT_ADD", "register:40f0:8", ["const:c28714:8", "const:4:8"]]
+ 00c28714 ["CALL", null, ["callee:00c5e570:8"]]
- 00c282ec bytes a1d70094
+ 00c28714 bytes 97d70094
- 00c2830c ["INT_ADD", "register:40f0:8", ["const:c2830c:8", "const:4:8"]]
- 00c2830c ["CALL", null, ["callee:00c5eb40:8"]]
+ 00c28734 ["INT_ADD", "register:40f0:8", ["const:c28734:8", "const:4:8"]]
+ 00c28734 ["CALL", null, ["callee:00c5eb40:8"]]
- 00c2830c bytes 0dd90094
+ 00c28734 bytes 03d90094
- 00c2831c ["INT_ADD", "register:40f0:8", ["const:c2831c:8", "const:4:8"]]
- 00c2831c ["CALL", null, ["callee:00c5e570:8"]]
+ 00c28744 ["INT_ADD", "register:40f0:8", ["const:c28744:8", "const:4:8"]]
+ 00c28744 ["CALL", null, ["callee:00c5e570:8"]]
- 00c2831c bytes 95d70094
+ 00c28744 bytes 8bd70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-629149d701e6f04a79885942b1612209"></a>

### [`00c28500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c28500.md) → [`00c28928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28928.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE10do_unshiftERS1_PcS4_RS4_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e170.md) [`00c5e730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e730.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5eb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2852c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c28500.md#insn-00c2852c) · [`00c28544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c28500.md#insn-00c28544) · [`00c28554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c28500.md#insn-00c28554)
- 新版 [`00c28954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28928.md#insn-00c28954) · [`00c2896c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28928.md#insn-00c2896c) · [`00c2897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28928.md#insn-00c2897c)

~~~diff
- 00c2852c ["INT_ADD", "register:40f0:8", ["const:c2852c:8", "const:4:8"]]
- 00c2852c ["CALL", null, ["callee:00c5e570:8"]]
+ 00c28954 ["INT_ADD", "register:40f0:8", ["const:c28954:8", "const:4:8"]]
+ 00c28954 ["CALL", null, ["callee:00c5e570:8"]]
- 00c2852c bytes 11d70094
+ 00c28954 bytes 07d70094
- 00c28544 ["INT_ADD", "register:40f0:8", ["const:c28544:8", "const:4:8"]]
- 00c28544 ["CALL", null, ["callee:00c5eb30:8"]]
+ 00c2896c ["INT_ADD", "register:40f0:8", ["const:c2896c:8", "const:4:8"]]
+ 00c2896c ["CALL", null, ["callee:00c5eb30:8"]]
- 00c28544 bytes 7bd80094
+ 00c2896c bytes 71d80094
- 00c28554 ["INT_ADD", "register:40f0:8", ["const:c28554:8", "const:4:8"]]
- 00c28554 ["CALL", null, ["callee:00c5e570:8"]]
+ 00c2897c ["INT_ADD", "register:40f0:8", ["const:c2897c:8", "const:4:8"]]
+ 00c2897c ["CALL", null, ["callee:00c5e570:8"]]
- 00c28554 bytes 07d70094
+ 00c2897c bytes fdd60094
~~~


<a id="compare-3831d14bc0f81bd3e3ad62b8f13801ba"></a>

### [`00c285e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c285e0.md) → [`00c28a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28a08.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE11do_encodingEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5e170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e170.md) [`00c5e760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e760.md) [`00c5e770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e770.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5eb60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb60.md) [`00c5eb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c285fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c285e0.md#insn-00c285fc) · [`00c28614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c285e0.md#insn-00c28614) · [`00c28624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c285e0.md#insn-00c28624)
- 新版 [`00c28a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28a08.md#insn-00c28a24) · [`00c28a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28a08.md#insn-00c28a3c) · [`00c28a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28a08.md#insn-00c28a4c)

~~~diff
- 00c285fc ["INT_ADD", "register:40f0:8", ["const:c285fc:8", "const:4:8"]]
- 00c285fc ["CALL", null, ["callee:00c5e570:8"]]
+ 00c28a24 ["INT_ADD", "register:40f0:8", ["const:c28a24:8", "const:4:8"]]
+ 00c28a24 ["CALL", null, ["callee:00c5e570:8"]]
- 00c285fc bytes ddd60094
+ 00c28a24 bytes d3d60094
- 00c28614 ["INT_ADD", "register:40f0:8", ["const:c28614:8", "const:4:8"]]
- 00c28614 ["CALL", null, ["callee:00c5eb60:8"]]
+ 00c28a3c ["INT_ADD", "register:40f0:8", ["const:c28a3c:8", "const:4:8"]]
+ 00c28a3c ["CALL", null, ["callee:00c5eb60:8"]]
- 00c28614 bytes 53d80094
+ 00c28a3c bytes 49d80094
- 00c28624 ["INT_ADD", "register:40f0:8", ["const:c28624:8", "const:4:8"]]
- 00c28624 ["CALL", null, ["callee:00c5e570:8"]]
+ 00c28a4c ["INT_ADD", "register:40f0:8", ["const:c28a4c:8", "const:4:8"]]
+ 00c28a4c ["CALL", null, ["callee:00c5e570:8"]]
- 00c28624 bytes d3d60094
+ 00c28a4c bytes c9d60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62dec3942328cb4d75e809f1742ab199"></a>

### [`00c286b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c286b0.md) → [`00c28ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28ad8.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE9do_lengthERS1_PKcS5_m

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e170.md) [`00c5e780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e780.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c28704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c286b0.md#insn-00c28704) · [`00c2871c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c286b0.md#insn-00c2871c) · [`00c2872c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c286b0.md#insn-00c2872c)
- 新版 [`00c28b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28ad8.md#insn-00c28b2c) · [`00c28b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28ad8.md#insn-00c28b44) · [`00c28b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28ad8.md#insn-00c28b54)

~~~diff
- 00c28704 ["INT_ADD", "register:40f0:8", ["const:c28704:8", "const:4:8"]]
- 00c28704 ["CALL", null, ["callee:00c5e570:8"]]
+ 00c28b2c ["INT_ADD", "register:40f0:8", ["const:c28b2c:8", "const:4:8"]]
+ 00c28b2c ["CALL", null, ["callee:00c5e570:8"]]
- 00c28704 bytes 9bd60094
+ 00c28b2c bytes 91d60094
- 00c2871c ["INT_ADD", "register:40f0:8", ["const:c2871c:8", "const:4:8"]]
- 00c2871c ["CALL", null, ["callee:00c5eb80:8"]]
+ 00c28b44 ["INT_ADD", "register:40f0:8", ["const:c28b44:8", "const:4:8"]]
+ 00c28b44 ["CALL", null, ["callee:00c5eb80:8"]]
- 00c2871c bytes 19d80094
+ 00c28b44 bytes 0fd80094
- 00c2872c ["INT_ADD", "register:40f0:8", ["const:c2872c:8", "const:4:8"]]
- 00c2872c ["CALL", null, ["callee:00c5e570:8"]]
+ 00c28b54 ["INT_ADD", "register:40f0:8", ["const:c28b54:8", "const:4:8"]]
+ 00c28b54 ["CALL", null, ["callee:00c5e570:8"]]
- 00c2872c bytes 91d60094
+ 00c28b54 bytes 87d60094
~~~


<a id="compare-fb185fb387fad613626d1895dab25a3d"></a>

### [`00c287a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c287a8.md) → [`00c28bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28bd0.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE13do_max_lengthEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e170.md) [`00c5e770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e770.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5eb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c287c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c287a8.md#insn-00c287c4) · [`00c287d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c287a8.md#insn-00c287d0) · [`00c287e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c287a8.md#insn-00c287e0)
- 新版 [`00c28bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28bd0.md#insn-00c28bec) · [`00c28bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28bd0.md#insn-00c28bf8) · [`00c28c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28bd0.md#insn-00c28c08)

~~~diff
- 00c287c4 ["INT_ADD", "register:40f0:8", ["const:c287c4:8", "const:4:8"]]
- 00c287c4 ["CALL", null, ["callee:00c5e570:8"]]
+ 00c28bec ["INT_ADD", "register:40f0:8", ["const:c28bec:8", "const:4:8"]]
+ 00c28bec ["CALL", null, ["callee:00c5e570:8"]]
- 00c287c4 bytes 6bd60094
+ 00c28bec bytes 61d60094
- 00c287d0 ["INT_ADD", "register:40f0:8", ["const:c287d0:8", "const:4:8"]]
- 00c287d0 ["CALL", null, ["callee:00c5eb70:8"]]
+ 00c28bf8 ["INT_ADD", "register:40f0:8", ["const:c28bf8:8", "const:4:8"]]
+ 00c28bf8 ["CALL", null, ["callee:00c5eb70:8"]]
- 00c287d0 bytes e8d70094
+ 00c28bf8 bytes ded70094
- 00c287e0 ["INT_ADD", "register:40f0:8", ["const:c287e0:8", "const:4:8"]]
- 00c287e0 ["CALL", null, ["callee:00c5e570:8"]]
+ 00c28c08 ["INT_ADD", "register:40f0:8", ["const:c28c08:8", "const:4:8"]]
+ 00c28c08 ["CALL", null, ["callee:00c5e570:8"]]
- 00c287e0 bytes 64d60094
+ 00c28c08 bytes 5ad60094
~~~


<a id="compare-abec76679e51311f312479af37285cf8"></a>

### [`00c28820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c28820.md) → [`00c28c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28c48.md) _ZNSt6__ndk17codecvtIDsc9mbstate_tED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e790.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5eb90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c28834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c28820.md#insn-00c28834)
- 新版 [`00c28c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28c48.md#insn-00c28c5c)

~~~diff
- 00c28834 ["INT_ADD", "register:40f0:8", ["const:c28834:8", "const:4:8"]]
- 00c28834 ["CALL", null, ["callee:00c5eb90:8"]]
+ 00c28c5c ["INT_ADD", "register:40f0:8", ["const:c28c5c:8", "const:4:8"]]
+ 00c28c5c ["CALL", null, ["callee:00c5eb90:8"]]
- 00c28834 bytes d7d70094
+ 00c28c5c bytes cdd70094
~~~


<a id="compare-4d6975307adb66d06a2ca07747667c37"></a>

### [`00c2884c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c2884c.md) → [`00c28c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28c74.md) _ZNKSt6__ndk17codecvtIDsc9mbstate_tE6do_outERS1_PKDsS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c288b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c288b4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c28cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28cdc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c28890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c2884c.md#insn-00c28890)
- 新版 [`00c28cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28c74.md#insn-00c28cb8)

~~~diff
- 00c28890 ["INT_ADD", "register:40f0:8", ["const:c28890:8", "const:4:8"]]
- 00c28890 ["CALL", null, ["callee:00c28cdc:8"]]
+ 00c28cb8 ["INT_ADD", "register:40f0:8", ["const:c28cb8:8", "const:4:8"]]
+ 00c28cb8 ["CALL", null, ["callee:00c28cdc:8"]]
- 00c28890 bytes 09000094
+ 00c28cb8 bytes 09000094
~~~


<a id="compare-034135804c2fd59c5ef019b22a5a869a"></a>

### [`00c28b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c28b10.md) → [`00c28f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28f38.md) _ZNKSt6__ndk17codecvtIDsc9mbstate_tE5do_inERS1_PKcS5_RS5_PDsS7_RS7_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c28b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c28b78.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c28fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28fa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c28b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c28b10.md#insn-00c28b54)
- 新版 [`00c28f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28f38.md#insn-00c28f7c)

~~~diff
- 00c28b54 ["INT_ADD", "register:40f0:8", ["const:c28b54:8", "const:4:8"]]
- 00c28b54 ["CALL", null, ["callee:00c28fa0:8"]]
+ 00c28f7c ["INT_ADD", "register:40f0:8", ["const:c28f7c:8", "const:4:8"]]
+ 00c28f7c ["CALL", null, ["callee:00c28fa0:8"]]
- 00c28b54 bytes 09000094
+ 00c28f7c bytes 09000094
~~~


<a id="compare-b655e884c4143d5245b46742fab18eca"></a>

### [`00c2905c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c2905c.md) → [`00c29484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29484.md) _ZNSt6__ndk17codecvtIDsDu9mbstate_tED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e7a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5eba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eba0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c29070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c2905c.md#insn-00c29070)
- 新版 [`00c29498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29484.md#insn-00c29498)

~~~diff
- 00c29070 ["INT_ADD", "register:40f0:8", ["const:c29070:8", "const:4:8"]]
- 00c29070 ["CALL", null, ["callee:00c5eba0:8"]]
+ 00c29498 ["INT_ADD", "register:40f0:8", ["const:c29498:8", "const:4:8"]]
+ 00c29498 ["CALL", null, ["callee:00c5eba0:8"]]
- 00c29070 bytes ccd50094
+ 00c29498 bytes c2d50094
~~~


<a id="compare-d5f83994ac97aac4a256f0e6faf32ad0"></a>

### [`00c29088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29088.md) → [`00c294b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c294b0.md) _ZNKSt6__ndk17codecvtIDsDu9mbstate_tE6do_outERS1_PKDsS5_RS5_PDuS7_RS7_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c288b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c288b4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c28cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28cdc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c290cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29088.md#insn-00c290cc)
- 新版 [`00c294f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c294b0.md#insn-00c294f4)

~~~diff
- 00c290cc ["INT_ADD", "register:40f0:8", ["const:c290cc:8", "const:4:8"]]
- 00c290cc ["CALL", null, ["callee:00c28cdc:8"]]
+ 00c294f4 ["INT_ADD", "register:40f0:8", ["const:c294f4:8", "const:4:8"]]
+ 00c294f4 ["CALL", null, ["callee:00c28cdc:8"]]
- 00c290cc bytes fafdff97
+ 00c294f4 bytes fafdff97
~~~


<a id="compare-f27a27344642028075ece38f91b48e4e"></a>

### [`00c290f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c290f0.md) → [`00c29518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29518.md) _ZNKSt6__ndk17codecvtIDsDu9mbstate_tE5do_inERS1_PKDuS5_RS5_PDsS7_RS7_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c28b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c28b78.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c28fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28fa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c29134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c290f0.md#insn-00c29134)
- 新版 [`00c2955c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29518.md#insn-00c2955c)

~~~diff
- 00c29134 ["INT_ADD", "register:40f0:8", ["const:c29134:8", "const:4:8"]]
- 00c29134 ["CALL", null, ["callee:00c28fa0:8"]]
+ 00c2955c ["INT_ADD", "register:40f0:8", ["const:c2955c:8", "const:4:8"]]
+ 00c2955c ["CALL", null, ["callee:00c28fa0:8"]]
- 00c29134 bytes 91feff97
+ 00c2955c bytes 91feff97
~~~


<a id="compare-0d2ac98bbbbdb356bcbea0e025d5f5e7"></a>

### [`00c291a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c291a8.md) → [`00c295d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c295d0.md) _ZNSt6__ndk17codecvtIDic9mbstate_tED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e7b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ebb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ebb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c291bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c291a8.md#insn-00c291bc)
- 新版 [`00c295e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c295d0.md#insn-00c295e4)

~~~diff
- 00c291bc ["INT_ADD", "register:40f0:8", ["const:c291bc:8", "const:4:8"]]
- 00c291bc ["CALL", null, ["callee:00c5ebb0:8"]]
+ 00c295e4 ["INT_ADD", "register:40f0:8", ["const:c295e4:8", "const:4:8"]]
+ 00c295e4 ["CALL", null, ["callee:00c5ebb0:8"]]
- 00c291bc bytes 7dd50094
+ 00c295e4 bytes 73d50094
~~~


<a id="compare-5da5958c3c0c1d73c5837a7fe12f2862"></a>

### [`00c29484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29484.md) → [`00c298ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c298ac.md) _ZNKSt6__ndk17codecvtIDic9mbstate_tE5do_inERS1_PKcS5_RS5_PDiS7_RS7_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c294ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c294ec.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c29914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29914.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c294c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29484.md#insn-00c294c8)
- 新版 [`00c298f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c298ac.md#insn-00c298f0)

~~~diff
- 00c294c8 ["INT_ADD", "register:40f0:8", ["const:c294c8:8", "const:4:8"]]
- 00c294c8 ["CALL", null, ["callee:00c29914:8"]]
+ 00c298f0 ["INT_ADD", "register:40f0:8", ["const:c298f0:8", "const:4:8"]]
+ 00c298f0 ["CALL", null, ["callee:00c29914:8"]]
- 00c294c8 bytes 09000094
+ 00c298f0 bytes 09000094
~~~


<a id="compare-8c3e2d2d92871e1c009d7dff755800d9"></a>

### [`00c29964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29964.md) → [`00c29d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29d8c.md) _ZNSt6__ndk17codecvtIDiDu9mbstate_tED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e7c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ebc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ebc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c29978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29964.md#insn-00c29978)
- 新版 [`00c29da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29d8c.md#insn-00c29da0)

~~~diff
- 00c29978 ["INT_ADD", "register:40f0:8", ["const:c29978:8", "const:4:8"]]
- 00c29978 ["CALL", null, ["callee:00c5ebc0:8"]]
+ 00c29da0 ["INT_ADD", "register:40f0:8", ["const:c29da0:8", "const:4:8"]]
+ 00c29da0 ["CALL", null, ["callee:00c5ebc0:8"]]
- 00c29978 bytes 92d30094
+ 00c29da0 bytes 88d30094
~~~


<a id="compare-af103e04f12b25eb877b916f5e2dd455"></a>

### [`00c29ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29ab8.md) → [`00c29ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29ee0.md) _ZNKSt6__ndk17codecvtIDiDu9mbstate_tE5do_inERS1_PKDuS5_RS5_PDiS7_RS7_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c294ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c294ec.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c29914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29914.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c29afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29ab8.md#insn-00c29afc)
- 新版 [`00c29f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29ee0.md#insn-00c29f24)

~~~diff
- 00c29afc ["INT_ADD", "register:40f0:8", ["const:c29afc:8", "const:4:8"]]
- 00c29afc ["CALL", null, ["callee:00c29914:8"]]
+ 00c29f24 ["INT_ADD", "register:40f0:8", ["const:c29f24:8", "const:4:8"]]
+ 00c29f24 ["CALL", null, ["callee:00c29914:8"]]
- 00c29afc bytes 7cfeff97
+ 00c29f24 bytes 7cfeff97
~~~


<a id="compare-564fdf7aae936b3e0d7e344c83667b1b"></a>

### [`00c29b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29b70.md) → [`00c29f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29f98.md) _ZNKSt6__ndk114__codecvt_utf8IwE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c292fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c292fc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c29724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29724.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c29bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29b70.md#insn-00c29bbc)
- 新版 [`00c29fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29f98.md#insn-00c29fe4)

~~~diff
- 00c29bbc ["INT_ADD", "register:40f0:8", ["const:c29bbc:8", "const:4:8"]]
- 00c29bbc ["CALL", null, ["callee:00c29724:8"]]
+ 00c29fe4 ["INT_ADD", "register:40f0:8", ["const:c29fe4:8", "const:4:8"]]
+ 00c29fe4 ["CALL", null, ["callee:00c29724:8"]]
- 00c29bbc bytes d0fdff97
+ 00c29fe4 bytes d0fdff97
~~~


<a id="compare-ff18186d408cf128d0376d8cdc275060"></a>

### [`00c29be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29be0.md) → [`00c2a008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2a/00c2a008.md) _ZNKSt6__ndk114__codecvt_utf8IwE5do_inER9mbstate_tPKcS5_RS5_PwS7_RS7_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c294ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c294ec.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c29914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29914.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c29c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29be0.md#insn-00c29c2c)
- 新版 [`00c2a054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2a/00c2a008.md#insn-00c2a054)

~~~diff
- 00c29c2c ["INT_ADD", "register:40f0:8", ["const:c29c2c:8", "const:4:8"]]
- 00c29c2c ["CALL", null, ["callee:00c29914:8"]]
+ 00c2a054 ["INT_ADD", "register:40f0:8", ["const:c2a054:8", "const:4:8"]]
+ 00c2a054 ["CALL", null, ["callee:00c29914:8"]]
- 00c29c2c bytes 30feff97
+ 00c2a054 bytes 30feff97
~~~


<a id="compare-5ca40c5cf09820adb391f96415bce4c2"></a>

### [`00c2a100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2a100.md) → [`00c2a528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2a/00c2a528.md) _ZNKSt6__ndk114__codecvt_utf8IDiE6do_outER9mbstate_tPKDiS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c292fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c292fc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c29724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29724.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2a14c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2a100.md#insn-00c2a14c)
- 新版 [`00c2a574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2a/00c2a528.md#insn-00c2a574)

~~~diff
- 00c2a14c ["INT_ADD", "register:40f0:8", ["const:c2a14c:8", "const:4:8"]]
- 00c2a14c ["CALL", null, ["callee:00c29724:8"]]
+ 00c2a574 ["INT_ADD", "register:40f0:8", ["const:c2a574:8", "const:4:8"]]
+ 00c2a574 ["CALL", null, ["callee:00c29724:8"]]
- 00c2a14c bytes 6cfcff97
+ 00c2a574 bytes 6cfcff97
~~~


<a id="compare-597b02dc249267f9b3c07ad7b1d02a9b"></a>

### [`00c2a170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2a170.md) → [`00c2a598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2a/00c2a598.md) _ZNKSt6__ndk114__codecvt_utf8IDiE5do_inER9mbstate_tPKcS5_RS5_PDiS7_RS7_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c294ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c294ec.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c29914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c29/00c29914.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2a1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2a170.md#insn-00c2a1bc)
- 新版 [`00c2a5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2a/00c2a598.md#insn-00c2a5e4)

~~~diff
- 00c2a1bc ["INT_ADD", "register:40f0:8", ["const:c2a1bc:8", "const:4:8"]]
- 00c2a1bc ["CALL", null, ["callee:00c29914:8"]]
+ 00c2a5e4 ["INT_ADD", "register:40f0:8", ["const:c2a5e4:8", "const:4:8"]]
+ 00c2a5e4 ["CALL", null, ["callee:00c29914:8"]]
- 00c2a1bc bytes ccfcff97
+ 00c2a5e4 bytes ccfcff97
~~~


<a id="compare-4934d132737f9ab4793025408991ed1b"></a>

### [`00c2b114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b114.md) → [`00c2b53c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2b53c.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IwE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c2b184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b184.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c2b5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2b5ac.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2b160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b114.md#insn-00c2b160)
- 新版 [`00c2b588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2b53c.md#insn-00c2b588)

~~~diff
- 00c2b160 ["INT_ADD", "register:40f0:8", ["const:c2b160:8", "const:4:8"]]
- 00c2b160 ["CALL", null, ["callee:00c2b5ac:8"]]
+ 00c2b588 ["INT_ADD", "register:40f0:8", ["const:c2b588:8", "const:4:8"]]
+ 00c2b588 ["CALL", null, ["callee:00c2b5ac:8"]]
- 00c2b160 bytes 09000094
+ 00c2b588 bytes 09000094
~~~


<a id="compare-818af58d6a0690d5f73787ece78dc50c"></a>

### [`00c2b3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b3ac.md) → [`00c2b7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2b7d4.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IwE5do_inER9mbstate_tPKcS5_RS5_PwS7_RS7_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c2b41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b41c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c2b844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2b844.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2b3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b3ac.md#insn-00c2b3f8)
- 新版 [`00c2b820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2b7d4.md#insn-00c2b820)

~~~diff
- 00c2b3f8 ["INT_ADD", "register:40f0:8", ["const:c2b3f8:8", "const:4:8"]]
- 00c2b3f8 ["CALL", null, ["callee:00c2b844:8"]]
+ 00c2b820 ["INT_ADD", "register:40f0:8", ["const:c2b820:8", "const:4:8"]]
+ 00c2b820 ["CALL", null, ["callee:00c2b844:8"]]
- 00c2b3f8 bytes 09000094
+ 00c2b820 bytes 09000094
~~~


<a id="compare-a4fa496249c07c205a58c5bbe1e55449"></a>

### [`00c2b70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b70c.md) → [`00c2bb34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bb34.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IDsE6do_outER9mbstate_tPKDsS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c288b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c288b4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c28cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28cdc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2b758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b70c.md#insn-00c2b758)
- 新版 [`00c2bb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bb34.md#insn-00c2bb80)

~~~diff
- 00c2b758 ["INT_ADD", "register:40f0:8", ["const:c2b758:8", "const:4:8"]]
- 00c2b758 ["CALL", null, ["callee:00c28cdc:8"]]
+ 00c2bb80 ["INT_ADD", "register:40f0:8", ["const:c2bb80:8", "const:4:8"]]
+ 00c2bb80 ["CALL", null, ["callee:00c28cdc:8"]]
- 00c2b758 bytes 57f4ff97
+ 00c2bb80 bytes 57f4ff97
~~~


<a id="compare-13ff07e19ed34d49fbb1589b0718e564"></a>

### [`00c2b77c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b77c.md) → [`00c2bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bba4.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IDsE5do_inER9mbstate_tPKcS5_RS5_PDsS7_RS7_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c28b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c28b78.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c28fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28fa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2b7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b77c.md#insn-00c2b7c8)
- 新版 [`00c2bbf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bba4.md#insn-00c2bbf0)

~~~diff
- 00c2b7c8 ["INT_ADD", "register:40f0:8", ["const:c2b7c8:8", "const:4:8"]]
- 00c2b7c8 ["CALL", null, ["callee:00c28fa0:8"]]
+ 00c2bbf0 ["INT_ADD", "register:40f0:8", ["const:c2bbf0:8", "const:4:8"]]
+ 00c2bbf0 ["CALL", null, ["callee:00c28fa0:8"]]
- 00c2b7c8 bytes ecf4ff97
+ 00c2bbf0 bytes ecf4ff97
~~~


<a id="compare-94fa3a4e8e2d346bb1b284f4a50d9f5a"></a>

### [`00c2b850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b850.md) → [`00c2bc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bc78.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IDiE6do_outER9mbstate_tPKDiS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c2b184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b184.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c2b5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2b5ac.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b850.md#insn-00c2b89c)
- 新版 [`00c2bcc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bc78.md#insn-00c2bcc4)

~~~diff
- 00c2b89c ["INT_ADD", "register:40f0:8", ["const:c2b89c:8", "const:4:8"]]
- 00c2b89c ["CALL", null, ["callee:00c2b5ac:8"]]
+ 00c2bcc4 ["INT_ADD", "register:40f0:8", ["const:c2bcc4:8", "const:4:8"]]
+ 00c2bcc4 ["CALL", null, ["callee:00c2b5ac:8"]]
- 00c2b89c bytes 3afeff97
+ 00c2bcc4 bytes 3afeff97
~~~


<a id="compare-7bec6533ac302dc56a1b2c5d159605e8"></a>

### [`00c2b8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b8c0.md) → [`00c2bce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bce8.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IDiE5do_inER9mbstate_tPKcS5_RS5_PDiS7_RS7_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c2b41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b41c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c2b844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2b844.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2b90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b8c0.md#insn-00c2b90c)
- 新版 [`00c2bd34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bce8.md#insn-00c2bd34)

~~~diff
- 00c2b90c ["INT_ADD", "register:40f0:8", ["const:c2b90c:8", "const:4:8"]]
- 00c2b90c ["CALL", null, ["callee:00c2b844:8"]]
+ 00c2bd34 ["INT_ADD", "register:40f0:8", ["const:c2bd34:8", "const:4:8"]]
+ 00c2bd34 ["CALL", null, ["callee:00c2b844:8"]]
- 00c2b90c bytes c4feff97
+ 00c2bd34 bytes c4feff97
~~~


<a id="compare-d3d93a328a522d899af492bf1d78b5a7"></a>

### [`00c2b994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b994.md) → [`00c2bdbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bdbc.md) _ZNSt6__ndk116__narrow_to_utf8ILm16EED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e7d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ebd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ebd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2b9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b994.md#insn-00c2b9a8)
- 新版 [`00c2bdd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bdbc.md#insn-00c2bdd0)

~~~diff
- 00c2b9a8 ["INT_ADD", "register:40f0:8", ["const:c2b9a8:8", "const:4:8"]]
- 00c2b9a8 ["CALL", null, ["callee:00c5ebd0:8"]]
+ 00c2bdd0 ["INT_ADD", "register:40f0:8", ["const:c2bdd0:8", "const:4:8"]]
+ 00c2bdd0 ["CALL", null, ["callee:00c5ebd0:8"]]
- 00c2b9a8 bytes 8acb0094
+ 00c2bdd0 bytes 80cb0094
~~~


<a id="compare-d733db3fb82e4f539f5e3d61c8495727"></a>

### [`00c2b9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b9c0.md) → [`00c2bde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bde8.md) _ZNSt6__ndk116__narrow_to_utf8ILm32EED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e7e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ebe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ebe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2b9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b9c0.md#insn-00c2b9d4)
- 新版 [`00c2bdfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bde8.md#insn-00c2bdfc)

~~~diff
- 00c2b9d4 ["INT_ADD", "register:40f0:8", ["const:c2b9d4:8", "const:4:8"]]
- 00c2b9d4 ["CALL", null, ["callee:00c5ebe0:8"]]
+ 00c2bdfc ["INT_ADD", "register:40f0:8", ["const:c2bdfc:8", "const:4:8"]]
+ 00c2bdfc ["CALL", null, ["callee:00c5ebe0:8"]]
- 00c2b9d4 bytes 83cb0094
+ 00c2bdfc bytes 79cb0094
~~~


<a id="compare-12c9794d58dec7d9e76d961c316a5d9d"></a>

### [`00c2b9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b9ec.md) → [`00c2be14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2be14.md) _ZNSt6__ndk117__widen_from_utf8ILm16EED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e7f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ebf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ebf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2ba00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b9ec.md#insn-00c2ba00)
- 新版 [`00c2be28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2be14.md#insn-00c2be28)

~~~diff
- 00c2ba00 ["INT_ADD", "register:40f0:8", ["const:c2ba00:8", "const:4:8"]]
- 00c2ba00 ["CALL", null, ["callee:00c5ebf0:8"]]
+ 00c2be28 ["INT_ADD", "register:40f0:8", ["const:c2be28:8", "const:4:8"]]
+ 00c2be28 ["CALL", null, ["callee:00c5ebf0:8"]]
- 00c2ba00 bytes 7ccb0094
+ 00c2be28 bytes 72cb0094
~~~


<a id="compare-7d7915244370c9130d778fd333d8c59a"></a>

### [`00c2ba18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2ba18.md) → [`00c2be40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2be40.md) _ZNSt6__ndk117__widen_from_utf8ILm32EED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e800.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ec00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ec00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2ba2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2ba18.md#insn-00c2ba2c)
- 新版 [`00c2be54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2be40.md#insn-00c2be54)

~~~diff
- 00c2ba2c ["INT_ADD", "register:40f0:8", ["const:c2ba2c:8", "const:4:8"]]
- 00c2ba2c ["CALL", null, ["callee:00c5ec00:8"]]
+ 00c2be54 ["INT_ADD", "register:40f0:8", ["const:c2be54:8", "const:4:8"]]
+ 00c2be54 ["CALL", null, ["callee:00c5ec00:8"]]
- 00c2ba2c bytes 75cb0094
+ 00c2be54 bytes 6bcb0094
~~~


<a id="compare-f4843b294e7dd62f616137dc18d64c77"></a>

### [`00c2baf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2baf0.md) → [`00c2bf18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bf18.md) _ZNSt6__ndk18numpunctIcED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e820.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ec20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ec20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2bb04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2baf0.md#insn-00c2bb04)
- 新版 [`00c2bf2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bf18.md#insn-00c2bf2c)

~~~diff
- 00c2bb04 ["INT_ADD", "register:40f0:8", ["const:c2bb04:8", "const:4:8"]]
- 00c2bb04 ["CALL", null, ["callee:00c5ec20:8"]]
+ 00c2bf2c ["INT_ADD", "register:40f0:8", ["const:c2bf2c:8", "const:4:8"]]
+ 00c2bf2c ["CALL", null, ["callee:00c5ec20:8"]]
- 00c2bb04 bytes 47cb0094
+ 00c2bf2c bytes 3dcb0094
~~~


<a id="compare-9ea348ce071ddb67eb7d9b7cce56302a"></a>

### [`00c2bb6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bb6c.md) → [`00c2bf94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bf94.md) _ZNSt6__ndk18numpunctIwED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e840.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ec40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ec40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2bb80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bb6c.md#insn-00c2bb80)
- 新版 [`00c2bfa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bf94.md#insn-00c2bfa8)

~~~diff
- 00c2bb80 ["INT_ADD", "register:40f0:8", ["const:c2bb80:8", "const:4:8"]]
- 00c2bb80 ["CALL", null, ["callee:00c5ec40:8"]]
+ 00c2bfa8 ["INT_ADD", "register:40f0:8", ["const:c2bfa8:8", "const:4:8"]]
+ 00c2bfa8 ["CALL", null, ["callee:00c5ec40:8"]]
- 00c2bb80 bytes 30cb0094
+ 00c2bfa8 bytes 26cb0094
~~~


<a id="compare-4468e668624de52454c5a94651548019"></a>

### [`00c2bc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bc6c.md) → [`00c2c094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c094.md) FUN_00c2c094

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00c2de30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2de30.md) [`00c2df3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2df3c.md) [`00c2e048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e048.md) [`00c2e154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e154.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5dc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc00.md)
- 新版 呼出元 4件 [`00c2e258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e258.md) [`00c2e364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e364.md) [`00c2e470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e470.md) [`00c2e57c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e57c.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5e000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2bc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bc6c.md#insn-00c2bc8c) · [`00c2bce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bc6c.md#insn-00c2bce0) · [`00c2bd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bc6c.md#insn-00c2bd00)
- 新版 [`00c2c0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c094.md#insn-00c2c0b4) · [`00c2c108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c094.md#insn-00c2c108) · [`00c2c128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c094.md#insn-00c2c128)

~~~diff
- 00c2bc8c ["INT_ADD", "register:40f0:8", ["const:c2bc8c:8", "const:4:8"]]
- 00c2bc8c ["CALL", null, ["callee:00c5e000:8"]]
+ 00c2c0b4 ["INT_ADD", "register:40f0:8", ["const:c2c0b4:8", "const:4:8"]]
+ 00c2c0b4 ["CALL", null, ["callee:00c5e000:8"]]
- 00c2bc8c bytes ddc70094
+ 00c2c0b4 bytes d3c70094
- 00c2bce0 ["INT_ADD", "register:40f0:8", ["const:c2bce0:8", "const:4:8"]]
- 00c2bce0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00c2c108 ["INT_ADD", "register:40f0:8", ["const:c2c108:8", "const:4:8"]]
+ 00c2c108 ["CALL", null, ["callee:00c57e90:8"]]
- 00c2bce0 bytes 6caf0094
+ 00c2c108 bytes 62af0094
- 00c2bd00 ["INT_ADD", "register:40f0:8", ["const:c2bd00:8", "const:4:8"]]
- 00c2bd00 ["CALL", null, ["callee:00c57f40:8"]]
+ 00c2c128 ["INT_ADD", "register:40f0:8", ["const:c2c128:8", "const:4:8"]]
+ 00c2c128 ["CALL", null, ["callee:00c57f40:8"]]
- 00c2bd00 bytes 90af0094
+ 00c2c128 bytes 86af0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd650a8f4c1edc0b1744c3b050c07838"></a>

### [`00c2c144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c144.md) → [`00c2c56c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c56c.md) _ZNSt6__ndk115numpunct_bynameIcED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e870.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ec70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ec70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2c158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c144.md#insn-00c2c158)
- 新版 [`00c2c580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c56c.md#insn-00c2c580)

~~~diff
- 00c2c158 ["INT_ADD", "register:40f0:8", ["const:c2c158:8", "const:4:8"]]
- 00c2c158 ["CALL", null, ["callee:00c5ec70:8"]]
+ 00c2c580 ["INT_ADD", "register:40f0:8", ["const:c2c580:8", "const:4:8"]]
+ 00c2c580 ["CALL", null, ["callee:00c5ec70:8"]]
- 00c2c158 bytes c6c90094
+ 00c2c580 bytes bcc90094
~~~


<a id="compare-ae826973e87ab1bf2bbe1eb074107d91"></a>

### [`00c2c170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c170.md) → [`00c2c598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c598.md) FUN_00c2c598

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00c2c1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c1fc.md) [`00c33358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c33/00c33358.md) [`00c34054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34054.md) · 呼出先 1件 [`00c5cdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdd0.md)
- 新版 呼出元 3件 [`00c2c624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c624.md) [`00c33780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c33/00c33780.md) [`00c3447c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c3447c.md) · 呼出先 1件 [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2c184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c170.md#insn-00c2c184)
- 新版 [`00c2c5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c598.md#insn-00c2c5ac)

~~~diff
- 00c2c184 ["INT_ADD", "register:40f0:8", ["const:c2c184:8", "const:4:8"]]
- 00c2c184 ["CALL", null, ["callee:00c5d1d0:8"]]
+ 00c2c5ac ["INT_ADD", "register:40f0:8", ["const:c2c5ac:8", "const:4:8"]]
+ 00c2c5ac ["CALL", null, ["callee:00c5d1d0:8"]]
- 00c2c184 bytes 13c30094
+ 00c2c5ac bytes 09c30094
~~~


<a id="compare-d5820265b05f1aa573992d86102e8914"></a>

### [`00c2c47c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c47c.md) → [`00c2c8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c8a4.md) _ZNSt6__ndk115numpunct_bynameIwED0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e890.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ec90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ec90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2c490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c47c.md#insn-00c2c490)
- 新版 [`00c2c8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c8a4.md#insn-00c2c8b8)

~~~diff
- 00c2c490 ["INT_ADD", "register:40f0:8", ["const:c2c490:8", "const:4:8"]]
- 00c2c490 ["CALL", null, ["callee:00c5ec90:8"]]
+ 00c2c8b8 ["INT_ADD", "register:40f0:8", ["const:c2c8b8:8", "const:4:8"]]
+ 00c2c8b8 ["CALL", null, ["callee:00c5ec90:8"]]
- 00c2c490 bytes 00c90094
+ 00c2c8b8 bytes f6c80094
~~~


<a id="compare-10cc967dde7958218efece9169348148"></a>

### [`00c2e358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e358.md) → [`00c2e780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e780.md) _ZNSt6__ndk110__time_getD2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e8c0.md) · 呼出先 1件 [`00c5cdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdd0.md)
- 新版 呼出元 1件 [`00c5ecc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ecc0.md) · 呼出先 1件 [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2e368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e358.md#insn-00c2e368)
- 新版 [`00c2e790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e780.md#insn-00c2e790)

~~~diff
- 00c2e368 ["INT_ADD", "register:40f0:8", ["const:c2e368:8", "const:4:8"]]
- 00c2e368 ["CALL", null, ["callee:00c5d1d0:8"]]
+ 00c2e790 ["INT_ADD", "register:40f0:8", ["const:c2e790:8", "const:4:8"]]
+ 00c2e790 ["CALL", null, ["callee:00c5d1d0:8"]]
- 00c2e368 bytes 9aba0094
+ 00c2e790 bytes 90ba0094
~~~


<a id="compare-7f708c5dda6c0c0006ec4dd8ddcf58bd"></a>

### [`00c2e964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e964.md) → [`00c2ed8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2ed8c.md) FUN_00c2ed8c

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c2e37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e37c.md) · 呼出先 3件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md) [`00c5db80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db80.md)
- 新版 呼出元 1件 [`00c2e7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e7a4.md) · 呼出先 3件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md) [`00c5df80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2e9c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e964.md#insn-00c2e9c4) · [`00c2e9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e964.md#insn-00c2e9d4) · [`00c2ea68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e964.md#insn-00c2ea68)
- 新版 [`00c2edec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2ed8c.md#insn-00c2edec) · [`00c2edfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2ed8c.md#insn-00c2edfc) · [`00c2ee90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2ed8c.md#insn-00c2ee90)

~~~diff
- 00c2e9c4 ["INT_ADD", "register:40f0:8", ["const:c2e9c4:8", "const:4:8"]]
- 00c2e9c4 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c2edec ["INT_ADD", "register:40f0:8", ["const:c2edec:8", "const:4:8"]]
+ 00c2edec ["CALL", null, ["callee:00c5a020:8"]]
- 00c2e9c4 bytes 97ac0094
+ 00c2edec bytes 8dac0094
- 00c2e9d4 ["INT_ADD", "register:40f0:8", ["const:c2e9d4:8", "const:4:8"]]
- 00c2e9d4 ["CALL", null, ["callee:00c5df80:8"]]
+ 00c2edfc ["INT_ADD", "register:40f0:8", ["const:c2edfc:8", "const:4:8"]]
+ 00c2edfc ["CALL", null, ["callee:00c5df80:8"]]
- 00c2e9d4 bytes 6bbc0094
+ 00c2edfc bytes 61bc0094
- 00c2ea68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c2ea68 ["INT_ADD", "register:40f0:8", ["const:c2ea68:8", "const:4:8"]]
- 00c2ea68 ["CALLIND", null, ["register:0:8"]]
+ 00c2ee90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c2ee90 ["INT_ADD", "register:40f0:8", ["const:c2ee90:8", "const:4:8"]]
+ 00c2ee90 ["CALLIND", null, ["register:0:8"]]
- 00c2ea68 bytes 00013fd6
+ 00c2ee90 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eaf91b17c2a0b09706bb8f2685072153"></a>

### [`00c3031c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c30/00c3031c.md) → [`00c30744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30744.md) FUN_00c30744

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c2ec74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2ec74.md) · 呼出先 3件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md) [`00c5db80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db80.md)
- 新版 呼出元 1件 [`00c2f09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2f/00c2f09c.md) · 呼出先 3件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md) [`00c5df80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c30/00c3031c.md#insn-00c3037c) · [`00c3038c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c30/00c3031c.md#insn-00c3038c) · [`00c30434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c30/00c3031c.md#insn-00c30434)
- 新版 [`00c307a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30744.md#insn-00c307a4) · [`00c307b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30744.md#insn-00c307b4) · [`00c3085c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30744.md#insn-00c3085c)

~~~diff
- 00c3037c ["INT_ADD", "register:40f0:8", ["const:c3037c:8", "const:4:8"]]
- 00c3037c ["CALL", null, ["callee:00c5a020:8"]]
+ 00c307a4 ["INT_ADD", "register:40f0:8", ["const:c307a4:8", "const:4:8"]]
+ 00c307a4 ["CALL", null, ["callee:00c5a020:8"]]
- 00c3037c bytes 29a60094
+ 00c307a4 bytes 1fa60094
- 00c3038c ["INT_ADD", "register:40f0:8", ["const:c3038c:8", "const:4:8"]]
- 00c3038c ["CALL", null, ["callee:00c5df80:8"]]
+ 00c307b4 ["INT_ADD", "register:40f0:8", ["const:c307b4:8", "const:4:8"]]
+ 00c307b4 ["CALL", null, ["callee:00c5df80:8"]]
- 00c3038c bytes fdb50094
+ 00c307b4 bytes f3b50094
- 00c30434 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c30434 ["INT_ADD", "register:40f0:8", ["const:c30434:8", "const:4:8"]]
- 00c30434 ["CALLIND", null, ["register:0:8"]]
+ 00c3085c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3085c ["INT_ADD", "register:40f0:8", ["const:c3085c:8", "const:4:8"]]
+ 00c3085c ["CALLIND", null, ["register:0:8"]]
- 00c30434 bytes 00013fd6
+ 00c3085c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb995e6b0be4837d8467d6e9a4381691"></a>

### [`00c34808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34808.md) → [`00c34c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34c30.md) FUN_00c34c30

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a480.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a880.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3481c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34808.md#insn-00c3481c)
- 新版 [`00c34c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34c30.md#insn-00c34c44)

~~~diff
- 00c3481c ["INT_ADD", "register:40f0:8", ["const:c3481c:8", "const:4:8"]]
- 00c3481c ["CALL", null, ["callee:00c5a880:8"]]
+ 00c34c44 ["INT_ADD", "register:40f0:8", ["const:c34c44:8", "const:4:8"]]
+ 00c34c44 ["CALL", null, ["callee:00c5a880:8"]]
- 00c3481c bytes 19970094
+ 00c34c44 bytes 0f970094
~~~


<a id="compare-3cb92c45941096e690731b5ff980e5ba"></a>

### [`00c34834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34834.md) → [`00c34c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34c5c.md) FUN_00c34c5c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e360.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e760.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34834.md#insn-00c34848)
- 新版 [`00c34c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34c5c.md#insn-00c34c70)

~~~diff
- 00c34848 ["INT_ADD", "register:40f0:8", ["const:c34848:8", "const:4:8"]]
- 00c34848 ["CALL", null, ["callee:00c5e760:8"]]
+ 00c34c70 ["INT_ADD", "register:40f0:8", ["const:c34c70:8", "const:4:8"]]
+ 00c34c70 ["CALL", null, ["callee:00c5e760:8"]]
- 00c34848 bytes c6a60094
+ 00c34c70 bytes bca60094
~~~


<a id="compare-29dfbda78b477224aba8d333bf1b91be"></a>

### [`00c34860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34860.md) → [`00c34c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34c88.md) FUN_00c34c88

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e380.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e780.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34860.md#insn-00c34874)
- 新版 [`00c34c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34c88.md#insn-00c34c9c)

~~~diff
- 00c34874 ["INT_ADD", "register:40f0:8", ["const:c34874:8", "const:4:8"]]
- 00c34874 ["CALL", null, ["callee:00c5e780:8"]]
+ 00c34c9c ["INT_ADD", "register:40f0:8", ["const:c34c9c:8", "const:4:8"]]
+ 00c34c9c ["CALL", null, ["callee:00c5e780:8"]]
- 00c34874 bytes c3a60094
+ 00c34c9c bytes b9a60094
~~~


<a id="compare-6f24947b5270b298640f81bf1794d36e"></a>

### [`00c3488c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c3488c.md) → [`00c34cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34cb4.md) FUN_00c34cb4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a480.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a880.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c348a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c3488c.md#insn-00c348a0)
- 新版 [`00c34cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34cb4.md#insn-00c34cc8)

~~~diff
- 00c348a0 ["INT_ADD", "register:40f0:8", ["const:c348a0:8", "const:4:8"]]
- 00c348a0 ["CALL", null, ["callee:00c5a880:8"]]
+ 00c34cc8 ["INT_ADD", "register:40f0:8", ["const:c34cc8:8", "const:4:8"]]
+ 00c34cc8 ["CALL", null, ["callee:00c5a880:8"]]
- 00c348a0 bytes f8960094
+ 00c34cc8 bytes ee960094
~~~


<a id="compare-5e0f8b5b5e69a86a53fae105de675845"></a>

### [`00c348b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c348b8.md) → [`00c34ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34ce0.md) FUN_00c34ce0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a480.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a880.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c348cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c348b8.md#insn-00c348cc)
- 新版 [`00c34cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34ce0.md#insn-00c34cf4)

~~~diff
- 00c348cc ["INT_ADD", "register:40f0:8", ["const:c348cc:8", "const:4:8"]]
- 00c348cc ["CALL", null, ["callee:00c5a880:8"]]
+ 00c34cf4 ["INT_ADD", "register:40f0:8", ["const:c34cf4:8", "const:4:8"]]
+ 00c34cf4 ["CALL", null, ["callee:00c5a880:8"]]
- 00c348cc bytes ed960094
+ 00c34cf4 bytes e3960094
~~~


<a id="compare-a209b41223f0f88ef6e7e397ac14a265"></a>

### [`00c348e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c348e4.md) → [`00c34d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34d0c.md) FUN_00c34d0c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e360.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e760.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c348f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c348e4.md#insn-00c348f8)
- 新版 [`00c34d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34d0c.md#insn-00c34d20)

~~~diff
- 00c348f8 ["INT_ADD", "register:40f0:8", ["const:c348f8:8", "const:4:8"]]
- 00c348f8 ["CALL", null, ["callee:00c5e760:8"]]
+ 00c34d20 ["INT_ADD", "register:40f0:8", ["const:c34d20:8", "const:4:8"]]
+ 00c34d20 ["CALL", null, ["callee:00c5e760:8"]]
- 00c348f8 bytes 9aa60094
+ 00c34d20 bytes 90a60094
~~~


<a id="compare-bc172abd7375bc0439662d2bab5e5f31"></a>

### [`00c34910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34910.md) → [`00c34d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34d38.md) FUN_00c34d38

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e360.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e760.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34910.md#insn-00c34924)
- 新版 [`00c34d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34d38.md#insn-00c34d4c)

~~~diff
- 00c34924 ["INT_ADD", "register:40f0:8", ["const:c34924:8", "const:4:8"]]
- 00c34924 ["CALL", null, ["callee:00c5e760:8"]]
+ 00c34d4c ["INT_ADD", "register:40f0:8", ["const:c34d4c:8", "const:4:8"]]
+ 00c34d4c ["CALL", null, ["callee:00c5e760:8"]]
- 00c34924 bytes 8fa60094
+ 00c34d4c bytes 85a60094
~~~


<a id="compare-3b05c8e55c9a505c5d620332cb70506d"></a>

### [`00c3493c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c3493c.md) → [`00c34d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34d64.md) FUN_00c34d64

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e380.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e780.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c3493c.md#insn-00c34950)
- 新版 [`00c34d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34d64.md#insn-00c34d78)

~~~diff
- 00c34950 ["INT_ADD", "register:40f0:8", ["const:c34950:8", "const:4:8"]]
- 00c34950 ["CALL", null, ["callee:00c5e780:8"]]
+ 00c34d78 ["INT_ADD", "register:40f0:8", ["const:c34d78:8", "const:4:8"]]
+ 00c34d78 ["CALL", null, ["callee:00c5e780:8"]]
- 00c34950 bytes 8ca60094
+ 00c34d78 bytes 82a60094
~~~


<a id="compare-a170f9b9cd30f466679ef5ab28a62f59"></a>

### [`00c34968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34968.md) → [`00c34d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34d90.md) FUN_00c34d90

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e380.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e780.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3497c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34968.md#insn-00c3497c)
- 新版 [`00c34da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34d90.md#insn-00c34da4)

~~~diff
- 00c3497c ["INT_ADD", "register:40f0:8", ["const:c3497c:8", "const:4:8"]]
- 00c3497c ["CALL", null, ["callee:00c5e780:8"]]
+ 00c34da4 ["INT_ADD", "register:40f0:8", ["const:c34da4:8", "const:4:8"]]
+ 00c34da4 ["CALL", null, ["callee:00c5e780:8"]]
- 00c3497c bytes 81a60094
+ 00c34da4 bytes 77a60094
~~~


<a id="compare-f0d576aae0c2ed582b0037b2090e7ded"></a>

### [`00c34a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34a54.md) → [`00c34e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34e7c.md) FUN_00c34e7c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a480.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a880.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34a54.md#insn-00c34a68)
- 新版 [`00c34e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34e7c.md#insn-00c34e90)

~~~diff
- 00c34a68 ["INT_ADD", "register:40f0:8", ["const:c34a68:8", "const:4:8"]]
- 00c34a68 ["CALL", null, ["callee:00c5a880:8"]]
+ 00c34e90 ["INT_ADD", "register:40f0:8", ["const:c34e90:8", "const:4:8"]]
+ 00c34e90 ["CALL", null, ["callee:00c5a880:8"]]
- 00c34a68 bytes 86960094
+ 00c34e90 bytes 7c960094
~~~


<a id="compare-609e7256a58a87ba23791787c7c44e28"></a>

### [`00c34a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34a80.md) → [`00c34ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34ea8.md) FUN_00c34ea8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e380.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e780.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34a80.md#insn-00c34a94)
- 新版 [`00c34ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34ea8.md#insn-00c34ebc)

~~~diff
- 00c34a94 ["INT_ADD", "register:40f0:8", ["const:c34a94:8", "const:4:8"]]
- 00c34a94 ["CALL", null, ["callee:00c5e780:8"]]
+ 00c34ebc ["INT_ADD", "register:40f0:8", ["const:c34ebc:8", "const:4:8"]]
+ 00c34ebc ["CALL", null, ["callee:00c5e780:8"]]
- 00c34a94 bytes 3ba60094
+ 00c34ebc bytes 31a60094
~~~


<a id="compare-04e3fffe22b1ca9e562c046dd01d11e9"></a>

### [`00c34aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34aac.md) → [`00c34ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34ed4.md) FUN_00c34ed4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e360.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e760.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34aac.md#insn-00c34ac0)
- 新版 [`00c34ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34ed4.md#insn-00c34ee8)

~~~diff
- 00c34ac0 ["INT_ADD", "register:40f0:8", ["const:c34ac0:8", "const:4:8"]]
- 00c34ac0 ["CALL", null, ["callee:00c5e760:8"]]
+ 00c34ee8 ["INT_ADD", "register:40f0:8", ["const:c34ee8:8", "const:4:8"]]
+ 00c34ee8 ["CALL", null, ["callee:00c5e760:8"]]
- 00c34ac0 bytes 28a60094
+ 00c34ee8 bytes 1ea60094
~~~


<a id="compare-bfe95c574e4942c37310455b8945f74f"></a>

### [`00c34ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34ad8.md) → [`00c34f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34f00.md) FUN_00c34f00

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34ad8.md#insn-00c34aec)
- 新版 [`00c34f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34f00.md#insn-00c34f14)

~~~diff
- 00c34aec ["INT_ADD", "register:40f0:8", ["const:c34aec:8", "const:4:8"]]
- 00c34aec ["CALL", null, ["callee:00c58300:8"]]
+ 00c34f14 ["INT_ADD", "register:40f0:8", ["const:c34f14:8", "const:4:8"]]
+ 00c34f14 ["CALL", null, ["callee:00c58300:8"]]
- 00c34aec bytes 058d0094
+ 00c34f14 bytes fb8c0094
~~~


<a id="compare-c443e9b7236aaafdd0ef5ce63089cff6"></a>

### [`00c34b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34b04.md) → [`00c34f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34f2c.md) FUN_00c34f2c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34b04.md#insn-00c34b18)
- 新版 [`00c34f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34f2c.md#insn-00c34f40)

~~~diff
- 00c34b18 ["INT_ADD", "register:40f0:8", ["const:c34b18:8", "const:4:8"]]
- 00c34b18 ["CALL", null, ["callee:00c58300:8"]]
+ 00c34f40 ["INT_ADD", "register:40f0:8", ["const:c34f40:8", "const:4:8"]]
+ 00c34f40 ["CALL", null, ["callee:00c58300:8"]]
- 00c34b18 bytes fa8c0094
+ 00c34f40 bytes f08c0094
~~~


<a id="compare-3033c04ad254f7780dff2af7a97248a3"></a>

### [`00c34b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34b30.md) → [`00c34f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34f58.md) FUN_00c34f58

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34b30.md#insn-00c34b44)
- 新版 [`00c34f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34f58.md#insn-00c34f6c)

~~~diff
- 00c34b44 ["INT_ADD", "register:40f0:8", ["const:c34b44:8", "const:4:8"]]
- 00c34b44 ["CALL", null, ["callee:00c58300:8"]]
+ 00c34f6c ["INT_ADD", "register:40f0:8", ["const:c34f6c:8", "const:4:8"]]
+ 00c34f6c ["CALL", null, ["callee:00c58300:8"]]
- 00c34b44 bytes ef8c0094
+ 00c34f6c bytes e58c0094
~~~


<a id="compare-96a5794fb511bdfd12a5b3601b5f2d79"></a>

### [`00c34b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34b5c.md) → [`00c34f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34f84.md) FUN_00c34f84

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34b5c.md#insn-00c34b70)
- 新版 [`00c34f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34f84.md#insn-00c34f98)

~~~diff
- 00c34b70 ["INT_ADD", "register:40f0:8", ["const:c34b70:8", "const:4:8"]]
- 00c34b70 ["CALL", null, ["callee:00c58300:8"]]
+ 00c34f98 ["INT_ADD", "register:40f0:8", ["const:c34f98:8", "const:4:8"]]
+ 00c34f98 ["CALL", null, ["callee:00c58300:8"]]
- 00c34b70 bytes e48c0094
+ 00c34f98 bytes da8c0094
~~~


<a id="compare-fced3c9054d8ffa0a1e976882c3a20d6"></a>

### [`00c34b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34b90.md) → [`00c34fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34fb8.md) FUN_00c34fb8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34b90.md#insn-00c34ba4)
- 新版 [`00c34fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34fb8.md#insn-00c34fcc)

~~~diff
- 00c34ba4 ["INT_ADD", "register:40f0:8", ["const:c34ba4:8", "const:4:8"]]
- 00c34ba4 ["CALL", null, ["callee:00c58300:8"]]
+ 00c34fcc ["INT_ADD", "register:40f0:8", ["const:c34fcc:8", "const:4:8"]]
+ 00c34fcc ["CALL", null, ["callee:00c58300:8"]]
- 00c34ba4 bytes d78c0094
+ 00c34fcc bytes cd8c0094
~~~


<a id="compare-8a911aad393a4f1d6f0a3af4cdff30eb"></a>

### [`00c34bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34bc4.md) → [`00c34fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34fec.md) FUN_00c34fec

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34bc4.md#insn-00c34bd8)
- 新版 [`00c35000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34fec.md#insn-00c35000)

~~~diff
- 00c34bd8 ["INT_ADD", "register:40f0:8", ["const:c34bd8:8", "const:4:8"]]
- 00c34bd8 ["CALL", null, ["callee:00c58300:8"]]
+ 00c35000 ["INT_ADD", "register:40f0:8", ["const:c35000:8", "const:4:8"]]
+ 00c35000 ["CALL", null, ["callee:00c58300:8"]]
- 00c34bd8 bytes ca8c0094
+ 00c35000 bytes c08c0094
~~~


<a id="compare-5c7ad166af78777a556cc5637c0e1990"></a>

### [`00c34bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34bf0.md) → [`00c35018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35018.md) FUN_00c35018

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c36824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36824.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c36c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36c4c.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34bf0.md#insn-00c34c08)
- 新版 [`00c35030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35018.md#insn-00c35030)

~~~diff
- 00c34c08 ["INT_ADD", "register:40f0:8", ["const:c34c08:8", "const:4:8"]]
- 00c34c08 ["CALL", null, ["callee:00c36c4c:8"]]
+ 00c35030 ["INT_ADD", "register:40f0:8", ["const:c35030:8", "const:4:8"]]
+ 00c35030 ["CALL", null, ["callee:00c36c4c:8"]]
- 00c34c08 bytes 07070094
+ 00c35030 bytes 07070094
~~~


<a id="compare-a33d2e40c0024b1b06192408210a2b99"></a>

### [`00c34c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c20.md) → [`00c35048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35048.md) FUN_00c35048

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c36824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36824.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c36c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36c4c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c20.md#insn-00c34c38) · [`00c34c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c20.md#insn-00c34c40)
- 新版 [`00c35060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35048.md#insn-00c35060) · [`00c35068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35048.md#insn-00c35068)

~~~diff
- 00c34c38 ["INT_ADD", "register:40f0:8", ["const:c34c38:8", "const:4:8"]]
- 00c34c38 ["CALL", null, ["callee:00c36c4c:8"]]
+ 00c35060 ["INT_ADD", "register:40f0:8", ["const:c35060:8", "const:4:8"]]
+ 00c35060 ["CALL", null, ["callee:00c36c4c:8"]]
- 00c34c38 bytes fb060094
+ 00c35060 bytes fb060094
- 00c34c40 ["INT_ADD", "register:40f0:8", ["const:c34c40:8", "const:4:8"]]
- 00c34c40 ["CALL", null, ["callee:00c58300:8"]]
+ 00c35068 ["INT_ADD", "register:40f0:8", ["const:c35068:8", "const:4:8"]]
+ 00c35068 ["CALL", null, ["callee:00c58300:8"]]
- 00c34c40 bytes b08c0094
+ 00c35068 bytes a68c0094
~~~


