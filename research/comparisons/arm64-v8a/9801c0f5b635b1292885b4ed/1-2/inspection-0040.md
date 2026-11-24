# v16.0.0 → v16.0.1 · 要調査の変更候補 (40)

[一覧の目次](README.md)

<a id="compare-6af46eadb6328a7d2c7258231c635bde"></a>

### [`00bf12c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf12c0.md) → [`00bf16e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf16e8.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEcm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c581d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c581d0.md) · 呼出先 1件 [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md)
- 新版 呼出元 1件 [`00c585d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585d0.md) · 呼出先 1件 [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf12c0.md#insn-00bf1308)
- 新版 [`00bf1730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf16e8.md#insn-00bf1730)

~~~diff
- 00bf1308 ["INT_ADD", "register:40f0:8", ["const:bf1308:8", "const:4:8"]]
- 00bf1308 ["CALL", null, ["callee:00c57fd0:8"]]
+ 00bf1730 ["INT_ADD", "register:40f0:8", ["const:bf1730:8", "const:4:8"]]
+ 00bf1730 ["CALL", null, ["callee:00c57fd0:8"]]
- 00bf1308 bytes 329a0194
+ 00bf1730 bytes 289a0194
~~~


<a id="compare-679c5851ce05c785d76393fa55238e68"></a>

### [`00bf1330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1330.md) → [`00bf1758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1758.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEmc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf138c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1330.md#insn-00bf138c) · [`00bf13ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1330.md#insn-00bf13ac) · [`00bf13cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1330.md#insn-00bf13cc)
- 新版 [`00bf17b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1758.md#insn-00bf17b4) · [`00bf17d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1758.md#insn-00bf17d4) · [`00bf17f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1758.md#insn-00bf17f4)

~~~diff
- 00bf138c ["INT_ADD", "register:40f0:8", ["const:bf138c:8", "const:4:8"]]
- 00bf138c ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf17b4 ["INT_ADD", "register:40f0:8", ["const:bf17b4:8", "const:4:8"]]
+ 00bf17b4 ["CALL", null, ["callee:00c57e90:8"]]
- 00bf138c bytes c1990194
+ 00bf17b4 bytes b7990194
- 00bf13ac ["INT_ADD", "register:40f0:8", ["const:bf13ac:8", "const:4:8"]]
- 00bf13ac ["CALL", null, ["callee:00c58090:8"]]
+ 00bf17d4 ["INT_ADD", "register:40f0:8", ["const:bf17d4:8", "const:4:8"]]
+ 00bf17d4 ["CALL", null, ["callee:00c58090:8"]]
- 00bf13ac bytes 399a0194
+ 00bf17d4 bytes 2f9a0194
- 00bf13cc ["INT_ADD", "register:40f0:8", ["const:bf13cc:8", "const:4:8"]]
- 00bf13cc ["CALL", null, ["callee:0043b764:8"]]
+ 00bf17f4 ["INT_ADD", "register:40f0:8", ["const:bf17f4:8", "const:4:8"]]
+ 00bf17f4 ["CALL", null, ["callee:0043b764:8"]]
- 00bf13cc bytes d628e197
+ 00bf17f4 bytes dc27e197
~~~


<a id="compare-813655622ea9f85ba14f9dd29d2a106a"></a>

### [`00bf13d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf13d0.md) → [`00bf17f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf17f8.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) · 呼出先 2件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c58bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bd0.md)
- 新版 呼出元 1件 [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) · 呼出先 2件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf13f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf13d0.md#insn-00bf13f4)
- 新版 [`00bf181c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf17f8.md#insn-00bf181c)

~~~diff
- 00bf13f4 ["INT_ADD", "register:40f0:8", ["const:bf13f4:8", "const:4:8"]]
- 00bf13f4 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00bf181c ["INT_ADD", "register:40f0:8", ["const:bf181c:8", "const:4:8"]]
+ 00bf181c ["CALL", null, ["callee:00c57fe0:8"]]
- 00bf13f4 bytes fb990194
+ 00bf181c bytes f1990194
~~~


<a id="compare-834b0005bfd5c2d4794f433aeaeb414f"></a>

### [`00bf141c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf141c.md) → [`00bf1844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1844.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE12find_last_ofEPKcmm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf141c.md#insn-00bf1478)
- 新版 [`00bf18a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1844.md#insn-00bf18a0)

~~~diff
- 00bf1478 ["INT_ADD", "register:40f0:8", ["const:bf1478:8", "const:4:8"]]
- 00bf1478 ["CALL", null, ["callee:00c57fd0:8"]]
+ 00bf18a0 ["INT_ADD", "register:40f0:8", ["const:bf18a0:8", "const:4:8"]]
+ 00bf18a0 ["CALL", null, ["callee:00c57fd0:8"]]
- 00bf1478 bytes d6990194
+ 00bf18a0 bytes cc990194
~~~


<a id="compare-385e2fc3d7b88383260ef3c64018c430"></a>

### [`00bf14a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf14a4.md) → [`00bf18cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf18cc.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9push_backEc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58200.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00c58600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58600.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf14a4.md#insn-00bf1570) · [`00bf1580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf14a4.md#insn-00bf1580) · [`00bf1590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf14a4.md#insn-00bf1590)
- 新版 [`00bf1998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf18cc.md#insn-00bf1998) · [`00bf19a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf18cc.md#insn-00bf19a8) · [`00bf19b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf18cc.md#insn-00bf19b8)

~~~diff
- 00bf1570 ["INT_ADD", "register:40f0:8", ["const:bf1570:8", "const:4:8"]]
- 00bf1570 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf1998 ["INT_ADD", "register:40f0:8", ["const:bf1998:8", "const:4:8"]]
+ 00bf1998 ["CALL", null, ["callee:00c57e90:8"]]
- 00bf1570 bytes 48990194
+ 00bf1998 bytes 3e990194
- 00bf1580 ["INT_ADD", "register:40f0:8", ["const:bf1580:8", "const:4:8"]]
- 00bf1580 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf19a8 ["INT_ADD", "register:40f0:8", ["const:bf19a8:8", "const:4:8"]]
+ 00bf19a8 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf1580 bytes 70990194
+ 00bf19a8 bytes 66990194
- 00bf1590 ["INT_ADD", "register:40f0:8", ["const:bf1590:8", "const:4:8"]]
- 00bf1590 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bf19b8 ["INT_ADD", "register:40f0:8", ["const:bf19b8:8", "const:4:8"]]
+ 00bf19b8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00bf1590 bytes 48990194
+ 00bf19b8 bytes 3e990194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea2a22742766afe9f8af979a576c60d1"></a>

### [`00bf1628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1628.md) → [`00bf1a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1a50.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEmc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a2e0.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 1件 [`00c5a6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a6e0.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1628.md#insn-00bf1704) · [`00bf1714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1628.md#insn-00bf1714) · [`00bf1730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1628.md#insn-00bf1730)
- 新版 [`00bf1b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1a50.md#insn-00bf1b2c) · [`00bf1b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1a50.md#insn-00bf1b3c) · [`00bf1b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1a50.md#insn-00bf1b58)

~~~diff
- 00bf1704 ["INT_ADD", "register:40f0:8", ["const:bf1704:8", "const:4:8"]]
- 00bf1704 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf1b2c ["INT_ADD", "register:40f0:8", ["const:bf1b2c:8", "const:4:8"]]
+ 00bf1b2c ["CALL", null, ["callee:00c57e90:8"]]
- 00bf1704 bytes e3980194
+ 00bf1b2c bytes d9980194
- 00bf1714 ["INT_ADD", "register:40f0:8", ["const:bf1714:8", "const:4:8"]]
- 00bf1714 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bf1b3c ["INT_ADD", "register:40f0:8", ["const:bf1b3c:8", "const:4:8"]]
+ 00bf1b3c ["CALL", null, ["callee:00c57eb0:8"]]
- 00bf1714 bytes e7980194
+ 00bf1b3c bytes dd980194
- 00bf1730 ["INT_ADD", "register:40f0:8", ["const:bf1730:8", "const:4:8"]]
- 00bf1730 ["CALL", null, ["callee:00c58090:8"]]
+ 00bf1b58 ["INT_ADD", "register:40f0:8", ["const:bf1b58:8", "const:4:8"]]
+ 00bf1b58 ["CALL", null, ["callee:00c58090:8"]]
- 00bf1730 bytes 58990194
+ 00bf1b58 bytes 4e990194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-266a27b699f9ca98a9a07f09af995d46"></a>

### [`00bf176c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf176c.md) → [`00bf1b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1b94.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE5eraseEmm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59530.md) · 呼出先 2件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00bf17e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf17e4.md)
- 新版 呼出元 1件 [`00c59930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59930.md) · 呼出先 2件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00bf1c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1c0c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf17a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf176c.md#insn-00bf17a4) · [`00bf17e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf176c.md#insn-00bf17e0)
- 新版 [`00bf1bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1b94.md#insn-00bf1bcc) · [`00bf1c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1b94.md#insn-00bf1c08)

~~~diff
- 00bf17a4 ["INT_ADD", "register:40f0:8", ["const:bf17a4:8", "const:4:8"]]
- 00bf17a4 ["CALL", null, ["callee:00bf1c0c:8"]]
+ 00bf1bcc ["INT_ADD", "register:40f0:8", ["const:bf1bcc:8", "const:4:8"]]
+ 00bf1bcc ["CALL", null, ["callee:00bf1c0c:8"]]
- 00bf17a4 bytes 10000094
+ 00bf1bcc bytes 10000094
- 00bf17e0 ["INT_ADD", "register:40f0:8", ["const:bf17e0:8", "const:4:8"]]
- 00bf17e0 ["CALL", null, ["callee:0044291c:8"]]
+ 00bf1c08 ["INT_ADD", "register:40f0:8", ["const:bf1c08:8", "const:4:8"]]
+ 00bf1c08 ["CALL", null, ["callee:0044291c:8"]]
- 00bf17e0 bytes 3f44e197
+ 00bf1c08 bytes 4543e197
~~~


<a id="compare-ae3ac39e799bab10a43c7a39abdc9cb5"></a>

### [`00bf17e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf17e4.md) → [`00bf1c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1c0c.md) FUN_00bf1c0c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bf176c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf176c.md) [`00c35c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35c90.md) · 呼出先 1件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 2件 [`00bf1b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1b94.md) [`00c360b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c360b8.md) · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf183c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf17e4.md#insn-00bf183c)
- 新版 [`00bf1c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1c0c.md#insn-00bf1c64)

~~~diff
- 00bf183c ["INT_ADD", "register:40f0:8", ["const:bf183c:8", "const:4:8"]]
- 00bf183c ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf1c64 ["INT_ADD", "register:40f0:8", ["const:bf1c64:8", "const:4:8"]]
+ 00bf1c64 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf183c bytes c1980194
+ 00bf1c64 bytes b7980194
~~~


<a id="compare-2d77925b6abc716a7d3cc8ab4ddb419f"></a>

### [`00bf1878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1878.md) → [`00bf1ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1ca0.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendERKS5_mm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5aca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aca0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5b0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1878.md#insn-00bf1914) · [`00bf193c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1878.md#insn-00bf193c) · [`00bf197c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1878.md#insn-00bf197c)
- 新版 [`00bf1d3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1ca0.md#insn-00bf1d3c) · [`00bf1d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1ca0.md#insn-00bf1d64) · [`00bf1da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1ca0.md#insn-00bf1da4)

~~~diff
- 00bf1914 ["INT_ADD", "register:40f0:8", ["const:bf1914:8", "const:4:8"]]
- 00bf1914 ["CALL", null, ["callee:00c5b0a0:8"]]
+ 00bf1d3c ["INT_ADD", "register:40f0:8", ["const:bf1d3c:8", "const:4:8"]]
+ 00bf1d3c ["CALL", null, ["callee:00c5b0a0:8"]]
- 00bf1914 bytes e3a40194
+ 00bf1d3c bytes d9a40194
- 00bf193c ["INT_ADD", "register:40f0:8", ["const:bf193c:8", "const:4:8"]]
- 00bf193c ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf1d64 ["INT_ADD", "register:40f0:8", ["const:bf1d64:8", "const:4:8"]]
+ 00bf1d64 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf193c bytes 81980194
+ 00bf1d64 bytes 77980194
- 00bf197c ["INT_ADD", "register:40f0:8", ["const:bf197c:8", "const:4:8"]]
- 00bf197c ["CALL", null, ["callee:0044291c:8"]]
+ 00bf1da4 ["INT_ADD", "register:40f0:8", ["const:bf1da4:8", "const:4:8"]]
+ 00bf1da4 ["CALL", null, ["callee:0044291c:8"]]
- 00bf197c bytes d843e197
+ 00bf1da4 bytes de42e197
~~~


<a id="compare-f2a819ee00434e6aaf772c96dd3aa119"></a>

### [`00bf1980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1980.md) → [`00bf1da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1da8.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf199c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1980.md#insn-00bf199c) · [`00bf19d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1980.md#insn-00bf19d8) · [`00bf19f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1980.md#insn-00bf19f8)
- 新版 [`00bf1dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1da8.md#insn-00bf1dc4) · [`00bf1e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1da8.md#insn-00bf1e00) · [`00bf1e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1da8.md#insn-00bf1e20)

~~~diff
- 00bf199c ["INT_ADD", "register:40f0:8", ["const:bf199c:8", "const:4:8"]]
- 00bf199c ["CALL", null, ["callee:00c57fe0:8"]]
+ 00bf1dc4 ["INT_ADD", "register:40f0:8", ["const:bf1dc4:8", "const:4:8"]]
+ 00bf1dc4 ["CALL", null, ["callee:00c57fe0:8"]]
- 00bf199c bytes 91980194
+ 00bf1dc4 bytes 87980194
- 00bf19d8 ["INT_ADD", "register:40f0:8", ["const:bf19d8:8", "const:4:8"]]
- 00bf19d8 ["CALL", null, ["callee:00c58050:8"]]
+ 00bf1e00 ["INT_ADD", "register:40f0:8", ["const:bf1e00:8", "const:4:8"]]
+ 00bf1e00 ["CALL", null, ["callee:00c58050:8"]]
- 00bf19d8 bytes 9e980194
+ 00bf1e00 bytes 94980194
- 00bf19f8 ["INT_ADD", "register:40f0:8", ["const:bf19f8:8", "const:4:8"]]
- 00bf19f8 ["CALL", null, ["callee:0044291c:8"]]
+ 00bf1e20 ["INT_ADD", "register:40f0:8", ["const:bf1e20:8", "const:4:8"]]
+ 00bf1e20 ["CALL", null, ["callee:0044291c:8"]]
- 00bf19f8 bytes b943e197
+ 00bf1e20 bytes bf42e197
~~~


<a id="compare-d852b83d50fad7662d42237a3b7b9dfa"></a>

### [`00bf1a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1a00.md) → [`00bf1e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1e28.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmPKcm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1a00.md#insn-00bf1a60) · [`00bf1a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1a00.md#insn-00bf1a7c)
- 新版 [`00bf1e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1e28.md#insn-00bf1e88) · [`00bf1ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1e28.md#insn-00bf1ea4)

~~~diff
- 00bf1a60 ["INT_ADD", "register:40f0:8", ["const:bf1a60:8", "const:4:8"]]
- 00bf1a60 ["CALL", null, ["callee:00c58050:8"]]
+ 00bf1e88 ["INT_ADD", "register:40f0:8", ["const:bf1e88:8", "const:4:8"]]
+ 00bf1e88 ["CALL", null, ["callee:00c58050:8"]]
- 00bf1a60 bytes 7c980194
+ 00bf1e88 bytes 72980194
- 00bf1a7c ["INT_ADD", "register:40f0:8", ["const:bf1a7c:8", "const:4:8"]]
- 00bf1a7c ["CALL", null, ["callee:0044291c:8"]]
+ 00bf1ea4 ["INT_ADD", "register:40f0:8", ["const:bf1ea4:8", "const:4:8"]]
+ 00bf1ea4 ["CALL", null, ["callee:0044291c:8"]]
- 00bf1a7c bytes 9843e197
+ 00bf1ea4 bytes 9e42e197
~~~


<a id="compare-47446450a1e7fdaffa288fbfdcdf57d5"></a>

### [`00bf1a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1a80.md) → [`00bf1ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1ea8.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1a80.md#insn-00bf1aa8) · [`00bf1afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1a80.md#insn-00bf1afc) · [`00bf1b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1a80.md#insn-00bf1b20)
- 新版 [`00bf1ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1ea8.md#insn-00bf1ed0) · [`00bf1f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1ea8.md#insn-00bf1f24) · [`00bf1f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1ea8.md#insn-00bf1f48)

~~~diff
- 00bf1aa8 ["INT_ADD", "register:40f0:8", ["const:bf1aa8:8", "const:4:8"]]
- 00bf1aa8 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00bf1ed0 ["INT_ADD", "register:40f0:8", ["const:bf1ed0:8", "const:4:8"]]
+ 00bf1ed0 ["CALL", null, ["callee:00c57fe0:8"]]
- 00bf1aa8 bytes 4e980194
+ 00bf1ed0 bytes 44980194
- 00bf1afc ["INT_ADD", "register:40f0:8", ["const:bf1afc:8", "const:4:8"]]
- 00bf1afc ["CALL", null, ["callee:00c58050:8"]]
+ 00bf1f24 ["INT_ADD", "register:40f0:8", ["const:bf1f24:8", "const:4:8"]]
+ 00bf1f24 ["CALL", null, ["callee:00c58050:8"]]
- 00bf1afc bytes 55980194
+ 00bf1f24 bytes 4b980194
- 00bf1b20 ["INT_ADD", "register:40f0:8", ["const:bf1b20:8", "const:4:8"]]
- 00bf1b20 ["CALL", null, ["callee:0044291c:8"]]
+ 00bf1f48 ["INT_ADD", "register:40f0:8", ["const:bf1f48:8", "const:4:8"]]
+ 00bf1f48 ["CALL", null, ["callee:0044291c:8"]]
- 00bf1b20 bytes 6f43e197
+ 00bf1f48 bytes 7542e197
~~~


<a id="compare-75295f14c973620b5f8879c6bdf561fd"></a>

### [`00bf1b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1b24.md) → [`00bf1f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f4c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE2atEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1b24.md#insn-00bf1b64)
- 新版 [`00bf1f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f4c.md#insn-00bf1f8c)

~~~diff
- 00bf1b64 ["INT_ADD", "register:40f0:8", ["const:bf1b64:8", "const:4:8"]]
- 00bf1b64 ["CALL", null, ["callee:0044291c:8"]]
+ 00bf1f8c ["INT_ADD", "register:40f0:8", ["const:bf1f8c:8", "const:4:8"]]
+ 00bf1f8c ["CALL", null, ["callee:0044291c:8"]]
- 00bf1b64 bytes 5e43e197
+ 00bf1f8c bytes 6442e197
~~~


<a id="compare-6f32780a4897bf3cb4d44f772d0a4b1c"></a>

### [`00bf1b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1b70.md) → [`00bf1f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f98.md) FUN_00bf1f98

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`00bf1b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1b68.md) [`00c2be00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2be00.md) [`00c2c1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c1fc.md) [`00c30648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c30/00c30648.md) [`00c3265c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c32/00c3265c.md) · 呼出先 2件 [`00bf0fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0fd8.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 8件 [`00bf1f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f90.md) [`00c2c228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c228.md) [`00c2c624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c624.md) [`00c30a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30a70.md) [`00c32a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c32a84.md) · 呼出先 2件 [`00bf1400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1400.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1b70.md#insn-00bf1b8c)
- 新版 [`00bf1fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f98.md#insn-00bf1fb4)

~~~diff
- 00bf1b8c ["INT_ADD", "register:40f0:8", ["const:bf1b8c:8", "const:4:8"]]
- 00bf1b8c ["CALL", null, ["callee:00c57fe0:8"]]
+ 00bf1fb4 ["INT_ADD", "register:40f0:8", ["const:bf1fb4:8", "const:4:8"]]
+ 00bf1fb4 ["CALL", null, ["callee:00c57fe0:8"]]
- 00bf1b8c bytes 15980194
+ 00bf1fb4 bytes 0b980194
~~~


<a id="compare-bf12d058324b2ff54b2d9297f1ebd484"></a>

### [`00bf1bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1bac.md) → [`00bf1fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1fd4.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEPKcmm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1bac.md#insn-00bf1c4c) · [`00bf1c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1bac.md#insn-00bf1c60)
- 新版 [`00bf2074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1fd4.md#insn-00bf2074) · [`00bf2088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1fd4.md#insn-00bf2088)

~~~diff
- 00bf1c4c ["INT_ADD", "register:40f0:8", ["const:bf1c4c:8", "const:4:8"]]
- 00bf1c4c ["CALL", null, ["callee:00c57fd0:8"]]
+ 00bf2074 ["INT_ADD", "register:40f0:8", ["const:bf2074:8", "const:4:8"]]
+ 00bf2074 ["CALL", null, ["callee:00c57fd0:8"]]
- 00bf1c4c bytes e1970194
+ 00bf2074 bytes d7970194
- 00bf1c60 ["INT_ADD", "register:40f0:8", ["const:bf1c60:8", "const:4:8"]]
- 00bf1c60 ["CALL", null, ["callee:00c58050:8"]]
+ 00bf2088 ["INT_ADD", "register:40f0:8", ["const:bf2088:8", "const:4:8"]]
+ 00bf2088 ["CALL", null, ["callee:00c58050:8"]]
- 00bf1c60 bytes fc970194
+ 00bf2088 bytes f2970194
~~~


<a id="compare-8e0a7d13c7b6e5bdbe047bcba9ee5345"></a>

### [`00bf1d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1d80.md) → [`00bf21a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf21a8.md) FUN_00bf21a8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bf1d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1d2c.md) [`00c04d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04d58.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 2件 [`00bf2154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2154.md) [`00c05180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05180.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1d80.md#insn-00bf1dc0) · [`00bf1dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1d80.md#insn-00bf1dec) · [`00bf1dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1d80.md#insn-00bf1dfc)
- 新版 [`00bf21e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf21a8.md#insn-00bf21e8) · [`00bf2214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf21a8.md#insn-00bf2214) · [`00bf2224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf21a8.md#insn-00bf2224)

~~~diff
- 00bf1dc0 ["INT_ADD", "register:40f0:8", ["const:bf1dc0:8", "const:4:8"]]
- 00bf1dc0 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf21e8 ["INT_ADD", "register:40f0:8", ["const:bf21e8:8", "const:4:8"]]
+ 00bf21e8 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf1dc0 bytes 60970194
+ 00bf21e8 bytes 56970194
- 00bf1dec ["INT_ADD", "register:40f0:8", ["const:bf1dec:8", "const:4:8"]]
- 00bf1dec ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf2214 ["INT_ADD", "register:40f0:8", ["const:bf2214:8", "const:4:8"]]
+ 00bf2214 ["CALL", null, ["callee:00c57e90:8"]]
- 00bf1dec bytes 29970194
+ 00bf2214 bytes 1f970194
- 00bf1dfc ["INT_ADD", "register:40f0:8", ["const:bf1dfc:8", "const:4:8"]]
- 00bf1dfc ["CALL", null, ["callee:00c58000:8"]]
+ 00bf2224 ["INT_ADD", "register:40f0:8", ["const:bf2224:8", "const:4:8"]]
+ 00bf2224 ["CALL", null, ["callee:00c58000:8"]]
- 00bf1dfc bytes 81970194
+ 00bf2224 bytes 77970194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2f77db890fe8f8337fef0e72a725a4b"></a>

### [`00bf1e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1e34.md) → [`00bf225c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf225c.md) FUN_00bf225c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bf1d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1d2c.md) [`00c04d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04d58.md) · 呼出先 5件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 2件 [`00bf2154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2154.md) [`00c05180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05180.md) · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1e34.md#insn-00bf1e78) · [`00bf1f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1e34.md#insn-00bf1f00) · [`00bf1f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1e34.md#insn-00bf1f18)
- 新版 [`00bf22a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf225c.md#insn-00bf22a0) · [`00bf2328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf225c.md#insn-00bf2328) · [`00bf2340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf225c.md#insn-00bf2340)

~~~diff
- 00bf1e78 ["INT_ADD", "register:40f0:8", ["const:bf1e78:8", "const:4:8"]]
- 00bf1e78 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf22a0 ["INT_ADD", "register:40f0:8", ["const:bf22a0:8", "const:4:8"]]
+ 00bf22a0 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf1e78 bytes 32970194
+ 00bf22a0 bytes 28970194
- 00bf1f00 ["INT_ADD", "register:40f0:8", ["const:bf1f00:8", "const:4:8"]]
- 00bf1f00 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf2328 ["INT_ADD", "register:40f0:8", ["const:bf2328:8", "const:4:8"]]
+ 00bf2328 ["CALL", null, ["callee:00c57e90:8"]]
- 00bf1f00 bytes e4960194
+ 00bf2328 bytes da960194
- 00bf1f18 ["INT_ADD", "register:40f0:8", ["const:bf1f18:8", "const:4:8"]]
- 00bf1f18 ["CALL", null, ["callee:00c58000:8"]]
+ 00bf2340 ["INT_ADD", "register:40f0:8", ["const:bf2340:8", "const:4:8"]]
+ 00bf2340 ["CALL", null, ["callee:00c58000:8"]]
- 00bf1f18 bytes 3a970194
+ 00bf2340 bytes 30970194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-437ab561cd36b37fe129ed9a1fdd184b"></a>

### [`00bf1f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1f58.md) → [`00bf2380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2380.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) · 呼出先 3件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c5aca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aca0.md)
- 新版 呼出元 1件 [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) · 呼出先 3件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c5b0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1f58.md#insn-00bf1f7c) · [`00bf1fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1f58.md#insn-00bf1fd8) · [`00bf1ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1f58.md#insn-00bf1ffc)
- 新版 [`00bf23a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2380.md#insn-00bf23a4) · [`00bf2400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2380.md#insn-00bf2400) · [`00bf2424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2380.md#insn-00bf2424)

~~~diff
- 00bf1f7c ["INT_ADD", "register:40f0:8", ["const:bf1f7c:8", "const:4:8"]]
- 00bf1f7c ["CALL", null, ["callee:00c57fe0:8"]]
+ 00bf23a4 ["INT_ADD", "register:40f0:8", ["const:bf23a4:8", "const:4:8"]]
+ 00bf23a4 ["CALL", null, ["callee:00c57fe0:8"]]
- 00bf1f7c bytes 19970194
+ 00bf23a4 bytes 0f970194
- 00bf1fd8 ["INT_ADD", "register:40f0:8", ["const:bf1fd8:8", "const:4:8"]]
- 00bf1fd8 ["CALL", null, ["callee:00c5b0a0:8"]]
+ 00bf2400 ["INT_ADD", "register:40f0:8", ["const:bf2400:8", "const:4:8"]]
+ 00bf2400 ["CALL", null, ["callee:00c5b0a0:8"]]
- 00bf1fd8 bytes 32a30194
+ 00bf2400 bytes 28a30194
- 00bf1ffc ["INT_ADD", "register:40f0:8", ["const:bf1ffc:8", "const:4:8"]]
- 00bf1ffc ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf2424 ["INT_ADD", "register:40f0:8", ["const:bf2424:8", "const:4:8"]]
+ 00bf2424 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf1ffc bytes d1960194
+ 00bf2424 bytes c7960194
~~~


<a id="compare-85e9fd61bd95306d3ed4c45f930c22e6"></a>

### [`00bf203c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf203c.md) → [`00bf2464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2464.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmRKS5_mm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c58070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58070.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf203c.md#insn-00bf2088)
- 新版 [`00bf24b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2464.md#insn-00bf24b0)

~~~diff
- 00bf2088 ["INT_ADD", "register:40f0:8", ["const:bf2088:8", "const:4:8"]]
- 00bf2088 ["CALL", null, ["callee:0044291c:8"]]
+ 00bf24b0 ["INT_ADD", "register:40f0:8", ["const:bf24b0:8", "const:4:8"]]
+ 00bf24b0 ["CALL", null, ["callee:0044291c:8"]]
- 00bf2088 bytes 1542e197
+ 00bf24b0 bytes 1b41e197
~~~


<a id="compare-68d9e64a47b5957f4a74bc9c50e29a2f"></a>

### [`00bf208c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf208c.md) → [`00bf24b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf24b4.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertENS_11__wrap_iterIPKcEEc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf208c.md#insn-00bf2150) · [`00bf217c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf208c.md#insn-00bf217c) · [`00bf219c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf208c.md#insn-00bf219c)
- 新版 [`00bf2578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf24b4.md#insn-00bf2578) · [`00bf25a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf24b4.md#insn-00bf25a4) · [`00bf25c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf24b4.md#insn-00bf25c4)

~~~diff
- 00bf2150 ["INT_ADD", "register:40f0:8", ["const:bf2150:8", "const:4:8"]]
- 00bf2150 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf2578 ["INT_ADD", "register:40f0:8", ["const:bf2578:8", "const:4:8"]]
+ 00bf2578 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf2150 bytes 7c960194
+ 00bf2578 bytes 72960194
- 00bf217c ["INT_ADD", "register:40f0:8", ["const:bf217c:8", "const:4:8"]]
- 00bf217c ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf25a4 ["INT_ADD", "register:40f0:8", ["const:bf25a4:8", "const:4:8"]]
+ 00bf25a4 ["CALL", null, ["callee:00c57e90:8"]]
- 00bf217c bytes 45960194
+ 00bf25a4 bytes 3b960194
- 00bf219c ["INT_ADD", "register:40f0:8", ["const:bf219c:8", "const:4:8"]]
- 00bf219c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bf25c4 ["INT_ADD", "register:40f0:8", ["const:bf25c4:8", "const:4:8"]]
+ 00bf25c4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00bf219c bytes 45960194
+ 00bf25c4 bytes 3b960194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ca958b34d314bc87528e5466a9747fc"></a>

### [`00bf2288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2288.md) → [`00bf26b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf26b0.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmRKS5_mm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c58bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c58fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf22d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2288.md#insn-00bf22d4)
- 新版 [`00bf26fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf26b0.md#insn-00bf26fc)

~~~diff
- 00bf22d4 ["INT_ADD", "register:40f0:8", ["const:bf22d4:8", "const:4:8"]]
- 00bf22d4 ["CALL", null, ["callee:0044291c:8"]]
+ 00bf26fc ["INT_ADD", "register:40f0:8", ["const:bf26fc:8", "const:4:8"]]
+ 00bf26fc ["CALL", null, ["callee:0044291c:8"]]
- 00bf22d4 bytes 8241e197
+ 00bf26fc bytes 8840e197
~~~


<a id="compare-99efd5237687c5ce84140d8e6efd4748"></a>

### [`00bf22d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf22d8.md) → [`00bf2700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2700.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7replaceEmmPKwm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5dbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbe0.md) · 呼出先 3件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5dbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbf0.md)
- 新版 呼出元 1件 [`00c5dfe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfe0.md) · 呼出先 3件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5dff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dff0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf22d8.md#insn-00bf2378) · [`00bf23c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf22d8.md#insn-00bf23c8) · [`00bf23d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf22d8.md#insn-00bf23d8)
- 新版 [`00bf27a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2700.md#insn-00bf27a0) · [`00bf27f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2700.md#insn-00bf27f0) · [`00bf2800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2700.md#insn-00bf2800)

~~~diff
- 00bf2378 ["INT_ADD", "register:40f0:8", ["const:bf2378:8", "const:4:8"]]
- 00bf2378 ["CALL", null, ["callee:00c5dff0:8"]]
+ 00bf27a0 ["INT_ADD", "register:40f0:8", ["const:bf27a0:8", "const:4:8"]]
+ 00bf27a0 ["CALL", null, ["callee:00c5dff0:8"]]
- 00bf2378 bytes 1eae0194
+ 00bf27a0 bytes 14ae0194
- 00bf23c8 ["INT_ADD", "register:40f0:8", ["const:bf23c8:8", "const:4:8"]]
- 00bf23c8 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf27f0 ["INT_ADD", "register:40f0:8", ["const:bf27f0:8", "const:4:8"]]
+ 00bf27f0 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf23c8 bytes de950194
+ 00bf27f0 bytes d4950194
- 00bf23d8 ["INT_ADD", "register:40f0:8", ["const:bf23d8:8", "const:4:8"]]
- 00bf23d8 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf2800 ["INT_ADD", "register:40f0:8", ["const:bf2800:8", "const:4:8"]]
+ 00bf2800 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf23d8 bytes da950194
+ 00bf2800 bytes d0950194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77edeabc65c509eaa817724b06803c53"></a>

### [`00bf24c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24c8.md) → [`00bf28f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28f0.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE21__grow_by_and_replaceEmmmmmmPKw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5dbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbf0.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00c5dff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dff0.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24c8.md#insn-00bf2594) · [`00bf25b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24c8.md#insn-00bf25b0) · [`00bf25c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24c8.md#insn-00bf25c4)
- 新版 [`00bf29bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28f0.md#insn-00bf29bc) · [`00bf29d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28f0.md#insn-00bf29d8) · [`00bf29ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28f0.md#insn-00bf29ec)

~~~diff
- 00bf2594 ["INT_ADD", "register:40f0:8", ["const:bf2594:8", "const:4:8"]]
- 00bf2594 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf29bc ["INT_ADD", "register:40f0:8", ["const:bf29bc:8", "const:4:8"]]
+ 00bf29bc ["CALL", null, ["callee:00c57e90:8"]]
- 00bf2594 bytes 3f950194
+ 00bf29bc bytes 35950194
- 00bf25b0 ["INT_ADD", "register:40f0:8", ["const:bf25b0:8", "const:4:8"]]
- 00bf25b0 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf29d8 ["INT_ADD", "register:40f0:8", ["const:bf29d8:8", "const:4:8"]]
+ 00bf29d8 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf25b0 bytes 64950194
+ 00bf29d8 bytes 5a950194
- 00bf25c4 ["INT_ADD", "register:40f0:8", ["const:bf25c4:8", "const:4:8"]]
- 00bf25c4 ["CALL", null, ["callee:00c58000:8"]]
+ 00bf29ec ["INT_ADD", "register:40f0:8", ["const:bf29ec:8", "const:4:8"]]
+ 00bf29ec ["CALL", null, ["callee:00c58000:8"]]
- 00bf25c4 bytes 8f950194
+ 00bf29ec bytes 85950194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e3600bcb9f25b726f344c86e7f57824"></a>

### [`00bf270c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf270c.md) → [`00bf2b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2b34.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6__initEPKwmm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf270c.md#insn-00bf2750) · [`00bf2798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf270c.md#insn-00bf2798) · [`00bf27bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf270c.md#insn-00bf27bc)
- 新版 [`00bf2b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2b34.md#insn-00bf2b78) · [`00bf2bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2b34.md#insn-00bf2bc0) · [`00bf2be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2b34.md#insn-00bf2be4)

~~~diff
- 00bf2750 ["INT_ADD", "register:40f0:8", ["const:bf2750:8", "const:4:8"]]
- 00bf2750 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf2b78 ["INT_ADD", "register:40f0:8", ["const:bf2b78:8", "const:4:8"]]
+ 00bf2b78 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf2750 bytes fc940194
+ 00bf2b78 bytes f2940194
- 00bf2798 ["INT_ADD", "register:40f0:8", ["const:bf2798:8", "const:4:8"]]
- 00bf2798 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf2bc0 ["INT_ADD", "register:40f0:8", ["const:bf2bc0:8", "const:4:8"]]
+ 00bf2bc0 ["CALL", null, ["callee:00c57e90:8"]]
- 00bf2798 bytes be940194
+ 00bf2bc0 bytes b4940194
- 00bf27bc ["INT_ADD", "register:40f0:8", ["const:bf27bc:8", "const:4:8"]]
- 00bf27bc ["CALL", null, ["callee:006d76a0:8"]]
+ 00bf2be4 ["INT_ADD", "register:40f0:8", ["const:bf2be4:8", "const:4:8"]]
+ 00bf2be4 ["CALL", null, ["callee:006d76a0:8"]]
- 00bf27bc bytes a993eb97
+ 00bf2be4 bytes af92eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ce70922c47fc520890adce685ca5b14"></a>

### [`00bf27f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf27f0.md) → [`00bf2c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2c18.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7replaceEmmPKw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5dbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbe0.md) [`00c5dc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5dfe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfe0.md) [`00c5e000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf27f0.md#insn-00bf2818)
- 新版 [`00bf2c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2c18.md#insn-00bf2c40)

~~~diff
- 00bf2818 ["INT_ADD", "register:40f0:8", ["const:bf2818:8", "const:4:8"]]
- 00bf2818 ["CALL", null, ["callee:00c5e000:8"]]
+ 00bf2c40 ["INT_ADD", "register:40f0:8", ["const:bf2c40:8", "const:4:8"]]
+ 00bf2c40 ["CALL", null, ["callee:00c5e000:8"]]
- 00bf2818 bytes faac0194
+ 00bf2c40 bytes f0ac0194
~~~


<a id="compare-9530eaf1e5c1bb94c257be8290631fd7"></a>

### [`00bf2870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2870.md) → [`00bf2c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2c98.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE16find_last_not_ofEPKwmm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf28d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2870.md#insn-00bf28d4)
- 新版 [`00bf2cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2c98.md#insn-00bf2cfc)

~~~diff
- 00bf28d4 ["INT_ADD", "register:40f0:8", ["const:bf28d4:8", "const:4:8"]]
- 00bf28d4 ["CALL", null, ["callee:00c58450:8"]]
+ 00bf2cfc ["INT_ADD", "register:40f0:8", ["const:bf2cfc:8", "const:4:8"]]
+ 00bf2cfc ["CALL", null, ["callee:00c58450:8"]]
- 00bf28d4 bytes df950194
+ 00bf2cfc bytes d5950194
~~~


<a id="compare-9ae99abff000637fc0504f3666240a19"></a>

### [`00bf2918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2918.md) → [`00bf2d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2d40.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE17find_first_not_ofEPKwmm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2918.md#insn-00bf2978)
- 新版 [`00bf2da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2d40.md#insn-00bf2da0)

~~~diff
- 00bf2978 ["INT_ADD", "register:40f0:8", ["const:bf2978:8", "const:4:8"]]
- 00bf2978 ["CALL", null, ["callee:00c58450:8"]]
+ 00bf2da0 ["INT_ADD", "register:40f0:8", ["const:bf2da0:8", "const:4:8"]]
+ 00bf2da0 ["CALL", null, ["callee:00c58450:8"]]
- 00bf2978 bytes b6950194
+ 00bf2da0 bytes ac950194
~~~


<a id="compare-ab89c3ba027524b5dd468519cab6bf84"></a>

### [`00bf29b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf29b4.md) → [`00bf2ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2ddc.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmmw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5dc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc10.md) · 呼出先 3件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5a4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4a0.md)
- 新版 呼出元 1件 [`00c5e010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e010.md) · 呼出先 3件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf29b4.md#insn-00bf2a38) · [`00bf2a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf29b4.md#insn-00bf2a78) · [`00bf2b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf29b4.md#insn-00bf2b08)
- 新版 [`00bf2e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2ddc.md#insn-00bf2e60) · [`00bf2ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2ddc.md#insn-00bf2ea0) · [`00bf2f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2ddc.md#insn-00bf2f30)

~~~diff
- 00bf2a38 ["INT_ADD", "register:40f0:8", ["const:bf2a38:8", "const:4:8"]]
- 00bf2a38 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00bf2e60 ["INT_ADD", "register:40f0:8", ["const:bf2e60:8", "const:4:8"]]
+ 00bf2e60 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00bf2a38 bytes 9a9e0194
+ 00bf2e60 bytes 909e0194
- 00bf2a78 ["INT_ADD", "register:40f0:8", ["const:bf2a78:8", "const:4:8"]]
- 00bf2a78 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf2ea0 ["INT_ADD", "register:40f0:8", ["const:bf2ea0:8", "const:4:8"]]
+ 00bf2ea0 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf2a78 bytes 32940194
+ 00bf2ea0 bytes 28940194
- 00bf2b08 ["INT_ADD", "register:40f0:8", ["const:bf2b08:8", "const:4:8"]]
- 00bf2b08 ["CALL", null, ["callee:00bf28d8:8"]]
+ 00bf2f30 ["INT_ADD", "register:40f0:8", ["const:bf2f30:8", "const:4:8"]]
+ 00bf2f30 ["CALL", null, ["callee:00bf28d8:8"]]
- 00bf2b08 bytes 6afeff97
+ 00bf2f30 bytes 6afeff97
~~~


<a id="compare-659bdcab7898e3e042cf7b7d7bf860cf"></a>

### [`00bf2b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2b40.md) → [`00bf2f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2f68.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6__initEPKwm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2b40.md#insn-00bf2bac) · [`00bf2bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2b40.md#insn-00bf2bcc) · [`00bf2bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2b40.md#insn-00bf2bec)
- 新版 [`00bf2fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2f68.md#insn-00bf2fd4) · [`00bf2ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2f68.md#insn-00bf2ff4) · [`00bf3014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2f68.md#insn-00bf3014)

~~~diff
- 00bf2bac ["INT_ADD", "register:40f0:8", ["const:bf2bac:8", "const:4:8"]]
- 00bf2bac ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf2fd4 ["INT_ADD", "register:40f0:8", ["const:bf2fd4:8", "const:4:8"]]
+ 00bf2fd4 ["CALL", null, ["callee:00c57e90:8"]]
- 00bf2bac bytes b9930194
+ 00bf2fd4 bytes af930194
- 00bf2bcc ["INT_ADD", "register:40f0:8", ["const:bf2bcc:8", "const:4:8"]]
- 00bf2bcc ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf2ff4 ["INT_ADD", "register:40f0:8", ["const:bf2ff4:8", "const:4:8"]]
+ 00bf2ff4 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf2bcc bytes dd930194
+ 00bf2ff4 bytes d3930194
- 00bf2bec ["INT_ADD", "register:40f0:8", ["const:bf2bec:8", "const:4:8"]]
- 00bf2bec ["CALL", null, ["callee:006d76a0:8"]]
+ 00bf3014 ["INT_ADD", "register:40f0:8", ["const:bf3014:8", "const:4:8"]]
+ 00bf3014 ["CALL", null, ["callee:006d76a0:8"]]
- 00bf2bec bytes 9d92eb97
+ 00bf3014 bytes a391eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73cefb862b4732676bdea72b7217cc25"></a>

### [`00bf2bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2bf4.md) → [`00bf301c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf301c.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE2atEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2bf4.md#insn-00bf2c38)
- 新版 [`00bf3060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf301c.md#insn-00bf3060)

~~~diff
- 00bf2c38 ["INT_ADD", "register:40f0:8", ["const:bf2c38:8", "const:4:8"]]
- 00bf2c38 ["CALL", null, ["callee:00bf28d8:8"]]
+ 00bf3060 ["INT_ADD", "register:40f0:8", ["const:bf3060:8", "const:4:8"]]
+ 00bf3060 ["CALL", null, ["callee:00bf28d8:8"]]
- 00bf2c38 bytes 1efeff97
+ 00bf3060 bytes 1efeff97
~~~


<a id="compare-e806e0193b80f7a6ab72f4f3b00c238b"></a>

### [`00bf2c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2c3c.md) → [`00bf3064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3064.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmPKwm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5dc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc20.md) · 呼出先 3件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5dbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbf0.md)
- 新版 呼出元 1件 [`00c5e020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e020.md) · 呼出先 3件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5dff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dff0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2c3c.md#insn-00bf2cc0) · [`00bf2d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2c3c.md#insn-00bf2d08) · [`00bf2d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2c3c.md#insn-00bf2d18)
- 新版 [`00bf30e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3064.md#insn-00bf30e8) · [`00bf3130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3064.md#insn-00bf3130) · [`00bf3140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3064.md#insn-00bf3140)

~~~diff
- 00bf2cc0 ["INT_ADD", "register:40f0:8", ["const:bf2cc0:8", "const:4:8"]]
- 00bf2cc0 ["CALL", null, ["callee:00c5dff0:8"]]
+ 00bf30e8 ["INT_ADD", "register:40f0:8", ["const:bf30e8:8", "const:4:8"]]
+ 00bf30e8 ["CALL", null, ["callee:00c5dff0:8"]]
- 00bf2cc0 bytes ccab0194
+ 00bf30e8 bytes c2ab0194
- 00bf2d08 ["INT_ADD", "register:40f0:8", ["const:bf2d08:8", "const:4:8"]]
- 00bf2d08 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf3130 ["INT_ADD", "register:40f0:8", ["const:bf3130:8", "const:4:8"]]
+ 00bf3130 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf2d08 bytes 8e930194
+ 00bf3130 bytes 84930194
- 00bf2d18 ["INT_ADD", "register:40f0:8", ["const:bf2d18:8", "const:4:8"]]
- 00bf2d18 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf3140 ["INT_ADD", "register:40f0:8", ["const:bf3140:8", "const:4:8"]]
+ 00bf3140 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf2d18 bytes 8a930194
+ 00bf3140 bytes 80930194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-859241efff03cb10949511004f13e96b"></a>

### [`00bf2de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2de8.md) → [`00bf3210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3210.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7replaceEmmmw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5a4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4a0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2de8.md#insn-00bf2e7c) · [`00bf2ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2de8.md#insn-00bf2ed0) · [`00bf2f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2de8.md#insn-00bf2f6c)
- 新版 [`00bf32a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3210.md#insn-00bf32a4) · [`00bf32f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3210.md#insn-00bf32f8) · [`00bf3394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3210.md#insn-00bf3394)

~~~diff
- 00bf2e7c ["INT_ADD", "register:40f0:8", ["const:bf2e7c:8", "const:4:8"]]
- 00bf2e7c ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00bf32a4 ["INT_ADD", "register:40f0:8", ["const:bf32a4:8", "const:4:8"]]
+ 00bf32a4 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00bf2e7c bytes 899d0194
+ 00bf32a4 bytes 7f9d0194
- 00bf2ed0 ["INT_ADD", "register:40f0:8", ["const:bf2ed0:8", "const:4:8"]]
- 00bf2ed0 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf32f8 ["INT_ADD", "register:40f0:8", ["const:bf32f8:8", "const:4:8"]]
+ 00bf32f8 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf2ed0 bytes 1c930194
+ 00bf32f8 bytes 12930194
- 00bf2f6c ["INT_ADD", "register:40f0:8", ["const:bf2f6c:8", "const:4:8"]]
- 00bf2f6c ["CALL", null, ["callee:00bf28d8:8"]]
+ 00bf3394 ["INT_ADD", "register:40f0:8", ["const:bf3394:8", "const:4:8"]]
+ 00bf3394 ["CALL", null, ["callee:00bf28d8:8"]]
- 00bf2f6c bytes 51fdff97
+ 00bf3394 bytes 51fdff97
~~~


<a id="compare-dd9fbf31a1d6d52b4eb1c5b5425c1b78"></a>

### [`00bf2f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2f78.md) → [`00bf33a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf33a0.md) FUN_00bf33a0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00bf2f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2f70.md) [`00bf32f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf32f8.md) [`00bf3fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3fcc.md) [`00c2cb6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2cb6c.md) [`00c2d600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2d600.md) · 呼出先 2件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5dbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbf0.md)
- 新版 呼出元 5件 [`00bf3398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3398.md) [`00bf3720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3720.md) [`00bf43f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf43f4.md) [`00c2cf94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cf94.md) [`00c2da28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2da28.md) · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5dff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dff0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2f78.md#insn-00bf2fe0) · [`00bf3008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2f78.md#insn-00bf3008)
- 新版 [`00bf3408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf33a0.md#insn-00bf3408) · [`00bf3430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf33a0.md#insn-00bf3430)

~~~diff
- 00bf2fe0 ["INT_ADD", "register:40f0:8", ["const:bf2fe0:8", "const:4:8"]]
- 00bf2fe0 ["CALL", null, ["callee:00c5dff0:8"]]
+ 00bf3408 ["INT_ADD", "register:40f0:8", ["const:bf3408:8", "const:4:8"]]
+ 00bf3408 ["CALL", null, ["callee:00c5dff0:8"]]
- 00bf2fe0 bytes 04ab0194
+ 00bf3408 bytes faaa0194
- 00bf3008 ["INT_ADD", "register:40f0:8", ["const:bf3008:8", "const:4:8"]]
- 00bf3008 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf3430 ["INT_ADD", "register:40f0:8", ["const:bf3430:8", "const:4:8"]]
+ 00bf3430 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf3008 bytes ce920194
+ 00bf3430 bytes c4920194
~~~


<a id="compare-328ffc4e2379a09f073847fa77249849"></a>

### [`00bf3040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3040.md) → [`00bf3468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3468.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7reserveEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00bf30dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf30dc.md)
- 新版 呼出元 0件  · 呼出先 2件 [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00bf3504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3504.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf30d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3040.md#insn-00bf30d8)
- 新版 [`00bf3500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3468.md#insn-00bf3500)

~~~diff
- 00bf30d8 ["INT_ADD", "register:40f0:8", ["const:bf30d8:8", "const:4:8"]]
- 00bf30d8 ["CALL", null, ["callee:006d76a0:8"]]
+ 00bf3500 ["INT_ADD", "register:40f0:8", ["const:bf3500:8", "const:4:8"]]
+ 00bf3500 ["CALL", null, ["callee:006d76a0:8"]]
- 00bf30d8 bytes 6291eb97
+ 00bf3500 bytes 6890eb97
~~~


<a id="compare-df4f8af4e954a9d16e56634383e5f859"></a>

### [`00bf30dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf30dc.md) → [`00bf3504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3504.md) FUN_00bf3504

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bf3040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3040.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00bf3468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3468.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf314c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf30dc.md#insn-00bf314c) · [`00bf3178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf30dc.md#insn-00bf3178) · [`00bf319c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf30dc.md#insn-00bf319c)
- 新版 [`00bf3574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3504.md#insn-00bf3574) · [`00bf35a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3504.md#insn-00bf35a0) · [`00bf35c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3504.md#insn-00bf35c4)

~~~diff
- 00bf314c ["INT_ADD", "register:40f0:8", ["const:bf314c:8", "const:4:8"]]
- 00bf314c ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf3574 ["INT_ADD", "register:40f0:8", ["const:bf3574:8", "const:4:8"]]
+ 00bf3574 ["CALL", null, ["callee:00c57e90:8"]]
- 00bf314c bytes 51920194
+ 00bf3574 bytes 47920194
- 00bf3178 ["INT_ADD", "register:40f0:8", ["const:bf3178:8", "const:4:8"]]
- 00bf3178 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf35a0 ["INT_ADD", "register:40f0:8", ["const:bf35a0:8", "const:4:8"]]
+ 00bf35a0 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf3178 bytes 72920194
+ 00bf35a0 bytes 68920194
- 00bf319c ["INT_ADD", "register:40f0:8", ["const:bf319c:8", "const:4:8"]]
- 00bf319c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bf35c4 ["INT_ADD", "register:40f0:8", ["const:bf35c4:8", "const:4:8"]]
+ 00bf35c4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00bf319c bytes 45920194
+ 00bf35c4 bytes 3b920194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3dcdc0acf2cbfdab8d6ded5451c46a50"></a>

### [`00bf3220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3220.md) → [`00bf3648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3648.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendEPKwm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4b0.md) · 呼出先 2件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5dbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbf0.md)
- 新版 呼出元 1件 [`00c5a8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8b0.md) · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5dff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dff0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3220.md#insn-00bf3294) · [`00bf32bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3220.md#insn-00bf32bc)
- 新版 [`00bf36bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3648.md#insn-00bf36bc) · [`00bf36e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3648.md#insn-00bf36e4)

~~~diff
- 00bf3294 ["INT_ADD", "register:40f0:8", ["const:bf3294:8", "const:4:8"]]
- 00bf3294 ["CALL", null, ["callee:00c5dff0:8"]]
+ 00bf36bc ["INT_ADD", "register:40f0:8", ["const:bf36bc:8", "const:4:8"]]
+ 00bf36bc ["CALL", null, ["callee:00c5dff0:8"]]
- 00bf3294 bytes 57aa0194
+ 00bf36bc bytes 4daa0194
- 00bf32bc ["INT_ADD", "register:40f0:8", ["const:bf32bc:8", "const:4:8"]]
- 00bf32bc ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf36e4 ["INT_ADD", "register:40f0:8", ["const:bf36e4:8", "const:4:8"]]
+ 00bf36e4 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf32bc bytes 21920194
+ 00bf36e4 bytes 17920194
~~~


<a id="compare-3aa96f97cb7fa73c62302c11e6e48338"></a>

### [`00bf32f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf32f8.md) → [`00bf3720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3720.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6assignERKS5_mm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00bf2f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2f78.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00bf33a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf33a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf32f8.md#insn-00bf3348)
- 新版 [`00bf3770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3720.md#insn-00bf3770)

~~~diff
- 00bf3348 ["INT_ADD", "register:40f0:8", ["const:bf3348:8", "const:4:8"]]
- 00bf3348 ["CALL", null, ["callee:00bf28d8:8"]]
+ 00bf3770 ["INT_ADD", "register:40f0:8", ["const:bf3770:8", "const:4:8"]]
+ 00bf3770 ["CALL", null, ["callee:00bf28d8:8"]]
- 00bf3348 bytes 5afcff97
+ 00bf3770 bytes 5afcff97
~~~


<a id="compare-cafbd465a69aec2c4805464c1b9aa8b4"></a>

### [`00bf334c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf334c.md) → [`00bf3774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3774.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE4copyEPwmm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf33a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf334c.md#insn-00bf33a4) · [`00bf33bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf334c.md#insn-00bf33bc)
- 新版 [`00bf37cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3774.md#insn-00bf37cc) · [`00bf37e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3774.md#insn-00bf37e4)

~~~diff
- 00bf33a4 ["INT_ADD", "register:40f0:8", ["const:bf33a4:8", "const:4:8"]]
- 00bf33a4 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf37cc ["INT_ADD", "register:40f0:8", ["const:bf37cc:8", "const:4:8"]]
+ 00bf37cc ["CALL", null, ["callee:00c57f40:8"]]
- 00bf33a4 bytes e7910194
+ 00bf37cc bytes dd910194
- 00bf33bc ["INT_ADD", "register:40f0:8", ["const:bf33bc:8", "const:4:8"]]
- 00bf33bc ["CALL", null, ["callee:00bf28d8:8"]]
+ 00bf37e4 ["INT_ADD", "register:40f0:8", ["const:bf37e4:8", "const:4:8"]]
+ 00bf37e4 ["CALL", null, ["callee:00bf28d8:8"]]
- 00bf33bc bytes 3dfcff97
+ 00bf37e4 bytes 3dfcff97
~~~


<a id="compare-142ddf5a461c676aaab2c4322d7cf3f3"></a>

### [`00bf33c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf33c0.md) → [`00bf37e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf37e8.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEC2ERKS5_mmRKS4_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a510.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00c5a910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a910.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf33c0.md#insn-00bf3460) · [`00bf3480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf33c0.md#insn-00bf3480) · [`00bf34a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf33c0.md#insn-00bf34a4)
- 新版 [`00bf3888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf37e8.md#insn-00bf3888) · [`00bf38a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf37e8.md#insn-00bf38a8) · [`00bf38cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf37e8.md#insn-00bf38cc)

~~~diff
- 00bf3460 ["INT_ADD", "register:40f0:8", ["const:bf3460:8", "const:4:8"]]
- 00bf3460 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf3888 ["INT_ADD", "register:40f0:8", ["const:bf3888:8", "const:4:8"]]
+ 00bf3888 ["CALL", null, ["callee:00c57e90:8"]]
- 00bf3460 bytes 8c910194
+ 00bf3888 bytes 82910194
- 00bf3480 ["INT_ADD", "register:40f0:8", ["const:bf3480:8", "const:4:8"]]
- 00bf3480 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf38a8 ["INT_ADD", "register:40f0:8", ["const:bf38a8:8", "const:4:8"]]
+ 00bf38a8 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf3480 bytes b0910194
+ 00bf38a8 bytes a6910194
- 00bf34a4 ["INT_ADD", "register:40f0:8", ["const:bf34a4:8", "const:4:8"]]
- 00bf34a4 ["CALL", null, ["callee:00bf28d8:8"]]
+ 00bf38cc ["INT_ADD", "register:40f0:8", ["const:bf38cc:8", "const:4:8"]]
+ 00bf38cc ["CALL", null, ["callee:00bf28d8:8"]]
- 00bf34a4 bytes 03fcff97
+ 00bf38cc bytes 03fcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be89d6b2be7cebd3eefa57da39bf184c"></a>

### [`00bf34b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf34b4.md) → [`00bf38dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf38dc.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE4findEwm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf34fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf34b4.md#insn-00bf34fc)
- 新版 [`00bf3924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf38dc.md#insn-00bf3924)

~~~diff
- 00bf34fc ["INT_ADD", "register:40f0:8", ["const:bf34fc:8", "const:4:8"]]
- 00bf34fc ["CALL", null, ["callee:00c58450:8"]]
+ 00bf3924 ["INT_ADD", "register:40f0:8", ["const:bf3924:8", "const:4:8"]]
+ 00bf3924 ["CALL", null, ["callee:00c58450:8"]]
- 00bf34fc bytes d5920194
+ 00bf3924 bytes cb920194
~~~


<a id="compare-444ea899abe17f0c57f59caa4d699bec"></a>

### [`00bf3528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3528.md) → [`00bf3950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3950.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6__initEmw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3528.md#insn-00bf3594) · [`00bf3610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3528.md#insn-00bf3610) · [`00bf3614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3528.md#insn-00bf3614)
- 新版 [`00bf39bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3950.md#insn-00bf39bc) · [`00bf3a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3950.md#insn-00bf3a38) · [`00bf3a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3950.md#insn-00bf3a3c)

~~~diff
- 00bf3594 ["INT_ADD", "register:40f0:8", ["const:bf3594:8", "const:4:8"]]
- 00bf3594 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf39bc ["INT_ADD", "register:40f0:8", ["const:bf39bc:8", "const:4:8"]]
+ 00bf39bc ["CALL", null, ["callee:00c57e90:8"]]
- 00bf3594 bytes 3f910194
+ 00bf39bc bytes 35910194
- 00bf3610 ["INT_ADD", "register:40f0:8", ["const:bf3610:8", "const:4:8"]]
- 00bf3610 ["CALL", null, ["callee:006d76a0:8"]]
+ 00bf3a38 ["INT_ADD", "register:40f0:8", ["const:bf3a38:8", "const:4:8"]]
+ 00bf3a38 ["CALL", null, ["callee:006d76a0:8"]]
- 00bf3610 bytes 1490eb97
+ 00bf3a38 bytes 1a8feb97
- 00bf3614 ["INT_ADD", "register:40f0:8", ["const:bf3614:8", "const:4:8"]]
- 00bf3614 ["CALL", null, ["callee:00440ec0:8"]]
+ 00bf3a3c ["INT_ADD", "register:40f0:8", ["const:bf3a3c:8", "const:4:8"]]
+ 00bf3a3c ["CALL", null, ["callee:00440ec0:8"]]
- 00bf3614 bytes 1b36e197
+ 00bf3a3c bytes 2135e197
~~~


<a id="compare-5b9cb9aa57876c915a22d2868aba9d80"></a>

### [`00bf3618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3618.md) → [`00bf3a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3a40.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmPKw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5dc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc00.md) [`00c5dc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e000.md) [`00c5e020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf363c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3618.md#insn-00bf363c)
- 新版 [`00bf3a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3a40.md#insn-00bf3a64)

~~~diff
- 00bf363c ["INT_ADD", "register:40f0:8", ["const:bf363c:8", "const:4:8"]]
- 00bf363c ["CALL", null, ["callee:00c5e000:8"]]
+ 00bf3a64 ["INT_ADD", "register:40f0:8", ["const:bf3a64:8", "const:4:8"]]
+ 00bf3a64 ["CALL", null, ["callee:00c5e000:8"]]
- 00bf363c bytes 71a90194
+ 00bf3a64 bytes 67a90194
~~~


<a id="compare-116bdc4ecbb8087dbe07f534f76b5628"></a>

### [`00bf3664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3664.md) → [`00bf3a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3a8c.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE12find_last_ofEPKwmm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf36cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3664.md#insn-00bf36cc)
- 新版 [`00bf3af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3a8c.md#insn-00bf3af4)

~~~diff
- 00bf36cc ["INT_ADD", "register:40f0:8", ["const:bf36cc:8", "const:4:8"]]
- 00bf36cc ["CALL", null, ["callee:00c58450:8"]]
+ 00bf3af4 ["INT_ADD", "register:40f0:8", ["const:bf3af4:8", "const:4:8"]]
+ 00bf3af4 ["CALL", null, ["callee:00c58450:8"]]
- 00bf36cc bytes 61920194
+ 00bf3af4 bytes 57920194
~~~


<a id="compare-6f690489f7c3a123ebf407ad47dc77d8"></a>

### [`00bf3700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3700.md) → [`00bf3b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3b28.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE9__grow_byEmmmmmm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4a0.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00c5a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8a0.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf37b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3700.md#insn-00bf37b4) · [`00bf37d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3700.md#insn-00bf37d0) · [`00bf37f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3700.md#insn-00bf37f4)
- 新版 [`00bf3bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3b28.md#insn-00bf3bdc) · [`00bf3bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3b28.md#insn-00bf3bf8) · [`00bf3c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3b28.md#insn-00bf3c1c)

~~~diff
- 00bf37b4 ["INT_ADD", "register:40f0:8", ["const:bf37b4:8", "const:4:8"]]
- 00bf37b4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf3bdc ["INT_ADD", "register:40f0:8", ["const:bf3bdc:8", "const:4:8"]]
+ 00bf3bdc ["CALL", null, ["callee:00c57e90:8"]]
- 00bf37b4 bytes b7900194
+ 00bf3bdc bytes ad900194
- 00bf37d0 ["INT_ADD", "register:40f0:8", ["const:bf37d0:8", "const:4:8"]]
- 00bf37d0 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf3bf8 ["INT_ADD", "register:40f0:8", ["const:bf3bf8:8", "const:4:8"]]
+ 00bf3bf8 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf37d0 bytes dc900194
+ 00bf3bf8 bytes d2900194
- 00bf37f4 ["INT_ADD", "register:40f0:8", ["const:bf37f4:8", "const:4:8"]]
- 00bf37f4 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf3c1c ["INT_ADD", "register:40f0:8", ["const:bf3c1c:8", "const:4:8"]]
+ 00bf3c1c ["CALL", null, ["callee:00c57f40:8"]]
- 00bf37f4 bytes d3900194
+ 00bf3c1c bytes c9900194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7469877945501704e3a21192ba5de7c"></a>

### [`00bf3840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3840.md) → [`00bf3c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3c68.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE9push_backEw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5dc30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc30.md) · 呼出先 1件 [`00c5a4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4a0.md)
- 新版 呼出元 1件 [`00c5e030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e030.md) · 呼出先 1件 [`00c5a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf38a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3840.md#insn-00bf38a4)
- 新版 [`00bf3ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3c68.md#insn-00bf3ccc)

~~~diff
- 00bf38a4 ["INT_ADD", "register:40f0:8", ["const:bf38a4:8", "const:4:8"]]
- 00bf38a4 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00bf3ccc ["INT_ADD", "register:40f0:8", ["const:bf3ccc:8", "const:4:8"]]
+ 00bf3ccc ["CALL", null, ["callee:00c5a8a0:8"]]
- 00bf38a4 bytes ff9a0194
+ 00bf3ccc bytes f59a0194
~~~


<a id="compare-4b947bce562dcd90eb73b05fa8757b0a"></a>

### [`00bf38e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf38e8.md) → [`00bf3d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3d10.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendEmw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf38e8.md#insn-00bf3960)
- 新版 [`00bf3d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3d10.md#insn-00bf3d88)

~~~diff
- 00bf3960 ["INT_ADD", "register:40f0:8", ["const:bf3960:8", "const:4:8"]]
- 00bf3960 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00bf3d88 ["INT_ADD", "register:40f0:8", ["const:bf3d88:8", "const:4:8"]]
+ 00bf3d88 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00bf3960 bytes d09a0194
+ 00bf3d88 bytes c69a0194
~~~


<a id="compare-8d0d62884292386849a1385cf389ac3f"></a>

### [`00bf3a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3a68.md) → [`00bf3e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3e90.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6assignEmw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3a68.md#insn-00bf3acc)
- 新版 [`00bf3ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3e90.md#insn-00bf3ef4)

~~~diff
- 00bf3acc ["INT_ADD", "register:40f0:8", ["const:bf3acc:8", "const:4:8"]]
- 00bf3acc ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00bf3ef4 ["INT_ADD", "register:40f0:8", ["const:bf3ef4:8", "const:4:8"]]
+ 00bf3ef4 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00bf3acc bytes 759a0194
+ 00bf3ef4 bytes 6b9a0194
~~~


<a id="compare-670a1c309350ad33c9e98eefa10802b2"></a>

### [`00bf3b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3b80.md) → [`00bf3fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3fa8.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE5eraseEmm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00bf3bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3bf8.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00bf4020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3b80.md#insn-00bf3bb8) · [`00bf3bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3b80.md#insn-00bf3bf4)
- 新版 [`00bf3fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3fa8.md#insn-00bf3fe0) · [`00bf401c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3fa8.md#insn-00bf401c)

~~~diff
- 00bf3bb8 ["INT_ADD", "register:40f0:8", ["const:bf3bb8:8", "const:4:8"]]
- 00bf3bb8 ["CALL", null, ["callee:00bf4020:8"]]
+ 00bf3fe0 ["INT_ADD", "register:40f0:8", ["const:bf3fe0:8", "const:4:8"]]
+ 00bf3fe0 ["CALL", null, ["callee:00bf4020:8"]]
- 00bf3bb8 bytes 10000094
+ 00bf3fe0 bytes 10000094
- 00bf3bf4 ["INT_ADD", "register:40f0:8", ["const:bf3bf4:8", "const:4:8"]]
- 00bf3bf4 ["CALL", null, ["callee:00bf28d8:8"]]
+ 00bf401c ["INT_ADD", "register:40f0:8", ["const:bf401c:8", "const:4:8"]]
+ 00bf401c ["CALL", null, ["callee:00bf28d8:8"]]
- 00bf3bf4 bytes 2ffaff97
+ 00bf401c bytes 2ffaff97
~~~


<a id="compare-2c1442bd5d5632f4d35f72b3abb7abce"></a>

### [`00bf3bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3bf8.md) → [`00bf4020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4020.md) FUN_00bf4020

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bf3b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3b80.md) [`00c35ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35ce8.md) · 呼出先 1件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 2件 [`00bf3fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3fa8.md) [`00c36110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36110.md) · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3bf8.md#insn-00bf3c58)
- 新版 [`00bf4080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4020.md#insn-00bf4080)

~~~diff
- 00bf3c58 ["INT_ADD", "register:40f0:8", ["const:bf3c58:8", "const:4:8"]]
- 00bf3c58 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf4080 ["INT_ADD", "register:40f0:8", ["const:bf4080:8", "const:4:8"]]
+ 00bf4080 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf3c58 bytes ba8f0194
+ 00bf4080 bytes b08f0194
~~~


<a id="compare-2d75c2f3a4cd7dbcad83637acb2ea404"></a>

### [`00bf3c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3c94.md) → [`00bf40bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf40bc.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendERKS5_mm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5dbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbf0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5dff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dff0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3c94.md#insn-00bf3d30) · [`00bf3d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3c94.md#insn-00bf3d5c) · [`00bf3d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3c94.md#insn-00bf3d9c)
- 新版 [`00bf4158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf40bc.md#insn-00bf4158) · [`00bf4184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf40bc.md#insn-00bf4184) · [`00bf41c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf40bc.md#insn-00bf41c4)

~~~diff
- 00bf3d30 ["INT_ADD", "register:40f0:8", ["const:bf3d30:8", "const:4:8"]]
- 00bf3d30 ["CALL", null, ["callee:00c5dff0:8"]]
+ 00bf4158 ["INT_ADD", "register:40f0:8", ["const:bf4158:8", "const:4:8"]]
+ 00bf4158 ["CALL", null, ["callee:00c5dff0:8"]]
- 00bf3d30 bytes b0a70194
+ 00bf4158 bytes a6a70194
- 00bf3d5c ["INT_ADD", "register:40f0:8", ["const:bf3d5c:8", "const:4:8"]]
- 00bf3d5c ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf4184 ["INT_ADD", "register:40f0:8", ["const:bf4184:8", "const:4:8"]]
+ 00bf4184 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf3d5c bytes 798f0194
+ 00bf4184 bytes 6f8f0194
- 00bf3d9c ["INT_ADD", "register:40f0:8", ["const:bf3d9c:8", "const:4:8"]]
- 00bf3d9c ["CALL", null, ["callee:00bf28d8:8"]]
+ 00bf41c4 ["INT_ADD", "register:40f0:8", ["const:bf41c4:8", "const:4:8"]]
+ 00bf41c4 ["CALL", null, ["callee:00bf28d8:8"]]
- 00bf3d9c bytes c5f9ff97
+ 00bf41c4 bytes c5f9ff97
~~~


<a id="compare-1ff074bbec1fe3f2645ae66f73be3952"></a>

### [`00bf3da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3da0.md) → [`00bf41c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf41c8.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7compareEPKw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00c5dc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc00.md) [`00c5dc40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c5e000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e000.md) [`00c5e040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3da0.md#insn-00bf3dc0) · [`00bf3e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3da0.md#insn-00bf3e04) · [`00bf3e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3da0.md#insn-00bf3e30)
- 新版 [`00bf41e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf41c8.md#insn-00bf41e8) · [`00bf422c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf41c8.md#insn-00bf422c) · [`00bf4258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf41c8.md#insn-00bf4258)

~~~diff
- 00bf3dc0 ["INT_ADD", "register:40f0:8", ["const:bf3dc0:8", "const:4:8"]]
- 00bf3dc0 ["CALL", null, ["callee:00c5e000:8"]]
+ 00bf41e8 ["INT_ADD", "register:40f0:8", ["const:bf41e8:8", "const:4:8"]]
+ 00bf41e8 ["CALL", null, ["callee:00c5e000:8"]]
- 00bf3dc0 bytes 90a70194
+ 00bf41e8 bytes 86a70194
- 00bf3e04 ["INT_ADD", "register:40f0:8", ["const:bf3e04:8", "const:4:8"]]
- 00bf3e04 ["CALL", null, ["callee:00c5e040:8"]]
+ 00bf422c ["INT_ADD", "register:40f0:8", ["const:bf422c:8", "const:4:8"]]
+ 00bf422c ["CALL", null, ["callee:00c5e040:8"]]
- 00bf3e04 bytes 8fa70194
+ 00bf422c bytes 85a70194
- 00bf3e30 ["INT_ADD", "register:40f0:8", ["const:bf3e30:8", "const:4:8"]]
- 00bf3e30 ["CALL", null, ["callee:00bf28d8:8"]]
+ 00bf4258 ["INT_ADD", "register:40f0:8", ["const:bf4258:8", "const:4:8"]]
+ 00bf4258 ["CALL", null, ["callee:00bf28d8:8"]]
- 00bf3e30 bytes a0f9ff97
+ 00bf4258 bytes a0f9ff97
~~~


<a id="compare-b5ae7c7281ecb7ef150e92287858ac02"></a>

### [`00bf3e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3e38.md) → [`00bf4260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4260.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7compareEmmPKwm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00c5dc40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c5e040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3e38.md#insn-00bf3e9c) · [`00bf3ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3e38.md#insn-00bf3ec0)
- 新版 [`00bf42c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4260.md#insn-00bf42c4) · [`00bf42e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4260.md#insn-00bf42e8)

~~~diff
- 00bf3e9c ["INT_ADD", "register:40f0:8", ["const:bf3e9c:8", "const:4:8"]]
- 00bf3e9c ["CALL", null, ["callee:00c5e040:8"]]
+ 00bf42c4 ["INT_ADD", "register:40f0:8", ["const:bf42c4:8", "const:4:8"]]
+ 00bf42c4 ["CALL", null, ["callee:00c5e040:8"]]
- 00bf3e9c bytes 69a70194
+ 00bf42c4 bytes 5fa70194
- 00bf3ec0 ["INT_ADD", "register:40f0:8", ["const:bf3ec0:8", "const:4:8"]]
- 00bf3ec0 ["CALL", null, ["callee:00bf28d8:8"]]
+ 00bf42e8 ["INT_ADD", "register:40f0:8", ["const:bf42e8:8", "const:4:8"]]
+ 00bf42e8 ["CALL", null, ["callee:00bf28d8:8"]]
- 00bf3ec0 bytes 7cf9ff97
+ 00bf42e8 bytes 7cf9ff97
~~~


<a id="compare-6264c5eabf9fa8af124987c23cae5a53"></a>

### [`00bf3ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3ec4.md) → [`00bf42ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf42ec.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7compareEmmPKw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00c5dc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc00.md) [`00c5dc40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c5e000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e000.md) [`00c5e040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3ec4.md#insn-00bf3ef0) · [`00bf3f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3ec4.md#insn-00bf3f48) · [`00bf3f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3ec4.md#insn-00bf3f78)
- 新版 [`00bf4318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf42ec.md#insn-00bf4318) · [`00bf4370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf42ec.md#insn-00bf4370) · [`00bf43a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf42ec.md#insn-00bf43a0)

~~~diff
- 00bf3ef0 ["INT_ADD", "register:40f0:8", ["const:bf3ef0:8", "const:4:8"]]
- 00bf3ef0 ["CALL", null, ["callee:00c5e000:8"]]
+ 00bf4318 ["INT_ADD", "register:40f0:8", ["const:bf4318:8", "const:4:8"]]
+ 00bf4318 ["CALL", null, ["callee:00c5e000:8"]]
- 00bf3ef0 bytes 44a70194
+ 00bf4318 bytes 3aa70194
- 00bf3f48 ["INT_ADD", "register:40f0:8", ["const:bf3f48:8", "const:4:8"]]
- 00bf3f48 ["CALL", null, ["callee:00c5e040:8"]]
+ 00bf4370 ["INT_ADD", "register:40f0:8", ["const:bf4370:8", "const:4:8"]]
+ 00bf4370 ["CALL", null, ["callee:00c5e040:8"]]
- 00bf3f48 bytes 3ea70194
+ 00bf4370 bytes 34a70194
- 00bf3f78 ["INT_ADD", "register:40f0:8", ["const:bf3f78:8", "const:4:8"]]
- 00bf3f78 ["CALL", null, ["callee:00bf28d8:8"]]
+ 00bf43a0 ["INT_ADD", "register:40f0:8", ["const:bf43a0:8", "const:4:8"]]
+ 00bf43a0 ["CALL", null, ["callee:00bf28d8:8"]]
- 00bf3f78 bytes 4ef9ff97
+ 00bf43a0 bytes 4ef9ff97
~~~


<a id="compare-a88d3f797c2c6632a635d7f7e62bbe69"></a>

### [`00bf3f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3f7c.md) → [`00bf43a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf43a4.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE2atEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3f7c.md#insn-00bf3fc0)
- 新版 [`00bf43e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf43a4.md#insn-00bf43e8)

~~~diff
- 00bf3fc0 ["INT_ADD", "register:40f0:8", ["const:bf3fc0:8", "const:4:8"]]
- 00bf3fc0 ["CALL", null, ["callee:00bf28d8:8"]]
+ 00bf43e8 ["INT_ADD", "register:40f0:8", ["const:bf43e8:8", "const:4:8"]]
+ 00bf43e8 ["CALL", null, ["callee:00bf28d8:8"]]
- 00bf3fc0 bytes 3cf9ff97
+ 00bf43e8 bytes 3cf9ff97
~~~


<a id="compare-93ea53ff2b23c979d8b998972cbfcf3d"></a>

### [`00bf3fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3fcc.md) → [`00bf43f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf43f4.md) FUN_00bf43f4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bf3fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3fc4.md) · 呼出先 2件 [`00bf2f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2f78.md) [`00c5dc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc00.md)
- 新版 呼出元 1件 [`00bf43ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf43ec.md) · 呼出先 2件 [`00bf33a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf33a0.md) [`00c5e000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3fcc.md#insn-00bf3fe8)
- 新版 [`00bf4410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf43f4.md#insn-00bf4410)

~~~diff
- 00bf3fe8 ["INT_ADD", "register:40f0:8", ["const:bf3fe8:8", "const:4:8"]]
- 00bf3fe8 ["CALL", null, ["callee:00c5e000:8"]]
+ 00bf4410 ["INT_ADD", "register:40f0:8", ["const:bf4410:8", "const:4:8"]]
+ 00bf4410 ["CALL", null, ["callee:00c5e000:8"]]
- 00bf3fe8 bytes 06a70194
+ 00bf4410 bytes fca60194
~~~


<a id="compare-e54e0b6e4c44606ab8327641a70728a9"></a>

### [`00bf4008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4008.md) → [`00bf4430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4430.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE4findEPKwmm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md) [`00c5dc40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md) [`00c5e040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf40b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4008.md#insn-00bf40b4) · [`00bf40c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4008.md#insn-00bf40c8)
- 新版 [`00bf44dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4430.md#insn-00bf44dc) · [`00bf44f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4430.md#insn-00bf44f0)

~~~diff
- 00bf40b4 ["INT_ADD", "register:40f0:8", ["const:bf40b4:8", "const:4:8"]]
- 00bf40b4 ["CALL", null, ["callee:00c58450:8"]]
+ 00bf44dc ["INT_ADD", "register:40f0:8", ["const:bf44dc:8", "const:4:8"]]
+ 00bf44dc ["CALL", null, ["callee:00c58450:8"]]
- 00bf40b4 bytes e78f0194
+ 00bf44dc bytes dd8f0194
- 00bf40c8 ["INT_ADD", "register:40f0:8", ["const:bf40c8:8", "const:4:8"]]
- 00bf40c8 ["CALL", null, ["callee:00c5e040:8"]]
+ 00bf44f0 ["INT_ADD", "register:40f0:8", ["const:bf44f0:8", "const:4:8"]]
+ 00bf44f0 ["CALL", null, ["callee:00c5e040:8"]]
- 00bf40c8 bytes dea60194
+ 00bf44f0 bytes d4a60194
~~~


<a id="compare-69ca5761c722bd19cafeba95054506b8"></a>

### [`00bf41f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf41f8.md) → [`00bf4620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4620.md) FUN_00bf4620

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bf41a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf41a0.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00bf45c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf45c8.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf4238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf41f8.md#insn-00bf4238) · [`00bf4280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf41f8.md#insn-00bf4280) · [`00bf4290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf41f8.md#insn-00bf4290)
- 新版 [`00bf4660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4620.md#insn-00bf4660) · [`00bf46a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4620.md#insn-00bf46a8) · [`00bf46b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4620.md#insn-00bf46b8)

~~~diff
- 00bf4238 ["INT_ADD", "register:40f0:8", ["const:bf4238:8", "const:4:8"]]
- 00bf4238 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf4660 ["INT_ADD", "register:40f0:8", ["const:bf4660:8", "const:4:8"]]
+ 00bf4660 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf4238 bytes 428e0194
+ 00bf4660 bytes 388e0194
- 00bf4280 ["INT_ADD", "register:40f0:8", ["const:bf4280:8", "const:4:8"]]
- 00bf4280 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf46a8 ["INT_ADD", "register:40f0:8", ["const:bf46a8:8", "const:4:8"]]
+ 00bf46a8 ["CALL", null, ["callee:00c57e90:8"]]
- 00bf4280 bytes 048e0194
+ 00bf46a8 bytes fa8d0194
- 00bf4290 ["INT_ADD", "register:40f0:8", ["const:bf4290:8", "const:4:8"]]
- 00bf4290 ["CALL", null, ["callee:00c58000:8"]]
+ 00bf46b8 ["INT_ADD", "register:40f0:8", ["const:bf46b8:8", "const:4:8"]]
+ 00bf46b8 ["CALL", null, ["callee:00c58000:8"]]
- 00bf4290 bytes 5c8e0194
+ 00bf46b8 bytes 528e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1109792964b43466057b61227b48bb9"></a>

### [`00bf42cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf42cc.md) → [`00bf46f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf46f4.md) FUN_00bf46f4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bf41a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf41a0.md) · 呼出先 2件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5dbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbf0.md)
- 新版 呼出元 1件 [`00bf45c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf45c8.md) · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5dff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dff0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf4314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf42cc.md#insn-00bf4314) · [`00bf4340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf42cc.md#insn-00bf4340)
- 新版 [`00bf473c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf46f4.md#insn-00bf473c) · [`00bf4768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf46f4.md#insn-00bf4768)

~~~diff
- 00bf4314 ["INT_ADD", "register:40f0:8", ["const:bf4314:8", "const:4:8"]]
- 00bf4314 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf473c ["INT_ADD", "register:40f0:8", ["const:bf473c:8", "const:4:8"]]
+ 00bf473c ["CALL", null, ["callee:00c57f40:8"]]
- 00bf4314 bytes 0b8e0194
+ 00bf473c bytes 018e0194
- 00bf4340 ["INT_ADD", "register:40f0:8", ["const:bf4340:8", "const:4:8"]]
- 00bf4340 ["CALL", null, ["callee:00c5dff0:8"]]
+ 00bf4768 ["INT_ADD", "register:40f0:8", ["const:bf4768:8", "const:4:8"]]
+ 00bf4768 ["CALL", null, ["callee:00c5dff0:8"]]
- 00bf4340 bytes 2ca60194
+ 00bf4768 bytes 22a60194
~~~


<a id="compare-28cd030d66a1694c79e8d4da584647c9"></a>

### [`00bf435c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf435c.md) → [`00bf4784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4784.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendEPKw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5dbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbf0.md) [`00c5dc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5dff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dff0.md) [`00c5e000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf4380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf435c.md#insn-00bf4380) · [`00bf43dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf435c.md#insn-00bf43dc) · [`00bf4404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf435c.md#insn-00bf4404)
- 新版 [`00bf47a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4784.md#insn-00bf47a8) · [`00bf4804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4784.md#insn-00bf4804) · [`00bf482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4784.md#insn-00bf482c)

~~~diff
- 00bf4380 ["INT_ADD", "register:40f0:8", ["const:bf4380:8", "const:4:8"]]
- 00bf4380 ["CALL", null, ["callee:00c5e000:8"]]
+ 00bf47a8 ["INT_ADD", "register:40f0:8", ["const:bf47a8:8", "const:4:8"]]
+ 00bf47a8 ["CALL", null, ["callee:00c5e000:8"]]
- 00bf4380 bytes 20a60194
+ 00bf47a8 bytes 16a60194
- 00bf43dc ["INT_ADD", "register:40f0:8", ["const:bf43dc:8", "const:4:8"]]
- 00bf43dc ["CALL", null, ["callee:00c5dff0:8"]]
+ 00bf4804 ["INT_ADD", "register:40f0:8", ["const:bf4804:8", "const:4:8"]]
+ 00bf4804 ["CALL", null, ["callee:00c5dff0:8"]]
- 00bf43dc bytes 05a60194
+ 00bf4804 bytes fba50194
- 00bf4404 ["INT_ADD", "register:40f0:8", ["const:bf4404:8", "const:4:8"]]
- 00bf4404 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf482c ["INT_ADD", "register:40f0:8", ["const:bf482c:8", "const:4:8"]]
+ 00bf482c ["CALL", null, ["callee:00c57f40:8"]]
- 00bf4404 bytes cf8d0194
+ 00bf482c bytes c58d0194
~~~


<a id="compare-a23ece3803cbac10f128a4f85098838c"></a>

### [`00bf4444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4444.md) → [`00bf486c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf486c.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7replaceEmmRKS5_mm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00c5dbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c5dfe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf4490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4444.md#insn-00bf4490)
- 新版 [`00bf48b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf486c.md#insn-00bf48b8)

~~~diff
- 00bf4490 ["INT_ADD", "register:40f0:8", ["const:bf4490:8", "const:4:8"]]
- 00bf4490 ["CALL", null, ["callee:00bf28d8:8"]]
+ 00bf48b8 ["INT_ADD", "register:40f0:8", ["const:bf48b8:8", "const:4:8"]]
+ 00bf48b8 ["CALL", null, ["callee:00bf28d8:8"]]
- 00bf4490 bytes 08f8ff97
+ 00bf48b8 bytes 08f8ff97
~~~


<a id="compare-7dca1473ce8ff8a0ebc9cacd91c04292"></a>

### [`00bf4494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4494.md) → [`00bf48bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf48bc.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertENS_11__wrap_iterIPKwEEw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5a4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf4514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4494.md#insn-00bf4514) · [`00bf4544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4494.md#insn-00bf4544)
- 新版 [`00bf493c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf48bc.md#insn-00bf493c) · [`00bf496c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf48bc.md#insn-00bf496c)

~~~diff
- 00bf4514 ["INT_ADD", "register:40f0:8", ["const:bf4514:8", "const:4:8"]]
- 00bf4514 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00bf493c ["INT_ADD", "register:40f0:8", ["const:bf493c:8", "const:4:8"]]
+ 00bf493c ["CALL", null, ["callee:00c5a8a0:8"]]
- 00bf4514 bytes e3970194
+ 00bf493c bytes d9970194
- 00bf4544 ["INT_ADD", "register:40f0:8", ["const:bf4544:8", "const:4:8"]]
- 00bf4544 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf496c ["INT_ADD", "register:40f0:8", ["const:bf496c:8", "const:4:8"]]
+ 00bf496c ["CALL", null, ["callee:00c57f40:8"]]
- 00bf4544 bytes 7f8d0194
+ 00bf496c bytes 758d0194
~~~


<a id="compare-f9f206ef846aeb994beb8300bd6d38fd"></a>

### [`00bf4598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4598.md) → [`00bf49c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf49c0.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6resizeEmw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a490.md) · 呼出先 1件 [`00c5a4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4a0.md)
- 新版 呼出元 1件 [`00c5a890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a890.md) · 呼出先 1件 [`00c5a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf461c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4598.md#insn-00bf461c)
- 新版 [`00bf4a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf49c0.md#insn-00bf4a44)

~~~diff
- 00bf461c ["INT_ADD", "register:40f0:8", ["const:bf461c:8", "const:4:8"]]
- 00bf461c ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00bf4a44 ["INT_ADD", "register:40f0:8", ["const:bf4a44:8", "const:4:8"]]
+ 00bf4a44 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00bf461c bytes a1970194
+ 00bf4a44 bytes 97970194
~~~


<a id="compare-6a09a64619d1cddc303f7ed590e7213a"></a>

### [`00bf46f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf46f8.md) → [`00bf4b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4b20.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmRKS5_mm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00c5dc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c5e020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf4744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf46f8.md#insn-00bf4744)
- 新版 [`00bf4b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4b20.md#insn-00bf4b6c)

~~~diff
- 00bf4744 ["INT_ADD", "register:40f0:8", ["const:bf4744:8", "const:4:8"]]
- 00bf4744 ["CALL", null, ["callee:00bf28d8:8"]]
+ 00bf4b6c ["INT_ADD", "register:40f0:8", ["const:bf4b6c:8", "const:4:8"]]
+ 00bf4b6c ["CALL", null, ["callee:00bf28d8:8"]]
- 00bf4744 bytes 5bf7ff97
+ 00bf4b6c bytes 5bf7ff97
~~~


<a id="compare-2b007f72ced28c4d90436f6ab2d79034"></a>

### [`00bf62a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf6/00bf62a0.md) → [`00bf66c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf6/00bf66c8.md) _ZNSt6__ndk19to_stringEj

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58390.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00bf7e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7e30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c58790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58790.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00bf8258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8258.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf62c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf6/00bf62a0.md#insn-00bf62c8) · [`00bf630c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf6/00bf62a0.md#insn-00bf630c) · [`00bf6338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf6/00bf62a0.md#insn-00bf6338)
- 新版 [`00bf66f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf6/00bf66c8.md#insn-00bf66f0) · [`00bf6734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf6/00bf66c8.md#insn-00bf6734) · [`00bf6760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf6/00bf66c8.md#insn-00bf6760)

~~~diff
- 00bf62c8 ["INT_ADD", "register:40f0:8", ["const:bf62c8:8", "const:4:8"]]
- 00bf62c8 ["CALL", null, ["callee:00bf8258:8"]]
+ 00bf66f0 ["INT_ADD", "register:40f0:8", ["const:bf66f0:8", "const:4:8"]]
+ 00bf66f0 ["CALL", null, ["callee:00bf8258:8"]]
- 00bf62c8 bytes da060094
+ 00bf66f0 bytes da060094
- 00bf630c ["INT_ADD", "register:40f0:8", ["const:bf630c:8", "const:4:8"]]
- 00bf630c ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf6734 ["INT_ADD", "register:40f0:8", ["const:bf6734:8", "const:4:8"]]
+ 00bf6734 ["CALL", null, ["callee:00c57e90:8"]]
- 00bf630c bytes e1850194
+ 00bf6734 bytes d7850194
- 00bf6338 ["INT_ADD", "register:40f0:8", ["const:bf6338:8", "const:4:8"]]
- 00bf6338 ["CALL", null, ["callee:00c58000:8"]]
+ 00bf6760 ["INT_ADD", "register:40f0:8", ["const:bf6760:8", "const:4:8"]]
+ 00bf6760 ["CALL", null, ["callee:00c58000:8"]]
- 00bf6338 bytes 32860194
+ 00bf6760 bytes 28860194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5aee9337d4f7422dd50ac5743eeb798"></a>

### [`00bf8c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8c14.md) → [`00bf903c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf903c.md) _ZNSt6__ndk112system_errorD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dd80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dd80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf8c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8c14.md#insn-00bf8c28)
- 新版 [`00bf9050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf903c.md#insn-00bf9050)

~~~diff
- 00bf8c28 ["INT_ADD", "register:40f0:8", ["const:bf8c28:8", "const:4:8"]]
- 00bf8c28 ["CALL", null, ["callee:00c5e180:8"]]
+ 00bf9050 ["INT_ADD", "register:40f0:8", ["const:bf9050:8", "const:4:8"]]
+ 00bf9050 ["CALL", null, ["callee:00c5e180:8"]]
- 00bf8c28 bytes 56940194
+ 00bf9050 bytes 4c940194
~~~


<a id="compare-d8e1d5bf6c246271afa7bea9cf6fd072"></a>

### [`00bf8cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8cc8.md) → [`00bf90f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf90f0.md) FUN_00bf90f0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5daf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5daf0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5def0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5def0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf8cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8cc8.md#insn-00bf8cdc)
- 新版 [`00bf9104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf90f0.md#insn-00bf9104)

~~~diff
- 00bf8cdc ["INT_ADD", "register:40f0:8", ["const:bf8cdc:8", "const:4:8"]]
- 00bf8cdc ["CALL", null, ["callee:00c5def0:8"]]
+ 00bf9104 ["INT_ADD", "register:40f0:8", ["const:bf9104:8", "const:4:8"]]
+ 00bf9104 ["CALL", null, ["callee:00c5def0:8"]]
- 00bf8cdc bytes 85930194
+ 00bf9104 bytes 7b930194
~~~


<a id="compare-58d7aa1970fc439ab7c102ab9ae269ab"></a>

### [`00bf8cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8cf4.md) → [`00bf911c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf911c.md) FUN_00bf911c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5daf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5daf0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5def0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5def0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf8d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8cf4.md#insn-00bf8d08)
- 新版 [`00bf9130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf911c.md#insn-00bf9130)

~~~diff
- 00bf8d08 ["INT_ADD", "register:40f0:8", ["const:bf8d08:8", "const:4:8"]]
- 00bf8d08 ["CALL", null, ["callee:00c5def0:8"]]
+ 00bf9130 ["INT_ADD", "register:40f0:8", ["const:bf9130:8", "const:4:8"]]
+ 00bf9130 ["CALL", null, ["callee:00c5def0:8"]]
- 00bf8d08 bytes 7a930194
+ 00bf9130 bytes 70930194
~~~


<a id="compare-95b57ef6a9d078f11740db6837f9a103"></a>

### [`00bf8d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8d5c.md) → [`00bf9184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9184.md) _ZNKSt6__ndk114error_category10equivalentEiRKNS_15error_conditionE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf8d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8d5c.md#insn-00bf8d78)
- 新版 [`00bf91a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9184.md#insn-00bf91a0)

~~~diff
- 00bf8d78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bf8d78 ["INT_ADD", "register:40f0:8", ["const:bf8d78:8", "const:4:8"]]
- 00bf8d78 ["CALLIND", null, ["register:0:8"]]
+ 00bf91a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bf91a0 ["INT_ADD", "register:40f0:8", ["const:bf91a0:8", "const:4:8"]]
+ 00bf91a0 ["CALLIND", null, ["register:0:8"]]
- 00bf8d78 bytes 00013fd6
+ 00bf91a0 bytes 00013fd6
~~~


<a id="compare-fdef81356ba40e0640ecd95bbf9e0a13"></a>

### [`00bf8dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8dbc.md) → [`00bf91e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf91e4.md) _ZNSt6__ndk118condition_variableD2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c57cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cd0.md) · 呼出先 1件 [`00c5d220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d220.md)
- 新版 呼出元 1件 [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md) · 呼出先 1件 [`00c5d620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d620.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf8dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8dbc.md#insn-00bf8dc8)
- 新版 [`00bf91f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf91e4.md#insn-00bf91f0)

~~~diff
- 00bf8dc8 ["INT_ADD", "register:40f0:8", ["const:bf8dc8:8", "const:4:8"]]
- 00bf8dc8 ["CALL", null, ["callee:00c5d620:8"]]
+ 00bf91f0 ["INT_ADD", "register:40f0:8", ["const:bf91f0:8", "const:4:8"]]
+ 00bf91f0 ["CALL", null, ["callee:00c5d620:8"]]
- 00bf8dc8 bytes 16910194
+ 00bf91f0 bytes 0c910194
~~~


<a id="compare-ed42c7a6ef7784f9e8edf909c3bc187a"></a>

### [`00bf8ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8ddc.md) → [`00bf9204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9204.md) _ZNSt6__ndk118condition_variable10notify_oneEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d10.md) · 呼出先 1件 [`00c5d230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d230.md)
- 新版 呼出元 1件 [`00c59110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59110.md) · 呼出先 1件 [`00c5d630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d630.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf8de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8ddc.md#insn-00bf8de8)
- 新版 [`00bf9210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9204.md#insn-00bf9210)

~~~diff
- 00bf8de8 ["INT_ADD", "register:40f0:8", ["const:bf8de8:8", "const:4:8"]]
- 00bf8de8 ["CALL", null, ["callee:00c5d630:8"]]
+ 00bf9210 ["INT_ADD", "register:40f0:8", ["const:bf9210:8", "const:4:8"]]
+ 00bf9210 ["CALL", null, ["callee:00c5d630:8"]]
- 00bf8de8 bytes 12910194
+ 00bf9210 bytes 08910194
~~~


<a id="compare-9444328ad8ecbff0743eb9c88e5b8968"></a>

### [`00bf8dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8dfc.md) → [`00bf9224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9224.md) _ZNSt6__ndk118condition_variable10notify_allEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c57f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f80.md) · 呼出先 1件 [`00c5ddc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5ddc0.md)
- 新版 呼出元 1件 [`00c58380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58380.md) · 呼出先 1件 [`00c5e1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e1c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf8e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8dfc.md#insn-00bf8e08)
- 新版 [`00bf9230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9224.md#insn-00bf9230)

~~~diff
- 00bf8e08 ["INT_ADD", "register:40f0:8", ["const:bf8e08:8", "const:4:8"]]
- 00bf8e08 ["CALL", null, ["callee:00c5e1c0:8"]]
+ 00bf9230 ["INT_ADD", "register:40f0:8", ["const:bf9230:8", "const:4:8"]]
+ 00bf9230 ["CALL", null, ["callee:00c5e1c0:8"]]
- 00bf8e08 bytes ee930194
+ 00bf9230 bytes e4930194
~~~


<a id="compare-8cf74231f451a9ab0fd0773b0a7b5700"></a>

### [`00bf8f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8f08.md) → [`00bf9330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9330.md) _ZNSt6__ndk125notify_all_at_thread_exitERNS_18condition_variableENS_11unique_lockINS_5mutexEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d00.md) [`00c57d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d30.md) [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c5ddf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5ddf0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58100.md) [`00c58130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58130.md) [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c5e1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e1f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf8f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8f08.md#insn-00bf8f24) · [`00bf8f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8f08.md#insn-00bf8f30) · [`00bf8f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8f08.md#insn-00bf8f3c)
- 新版 [`00bf934c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9330.md#insn-00bf934c) · [`00bf9358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9330.md#insn-00bf9358) · [`00bf9364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9330.md#insn-00bf9364)

~~~diff
- 00bf8f24 ["INT_ADD", "register:40f0:8", ["const:bf8f24:8", "const:4:8"]]
- 00bf8f24 ["CALL", null, ["callee:00c58130:8"]]
+ 00bf934c ["INT_ADD", "register:40f0:8", ["const:bf934c:8", "const:4:8"]]
+ 00bf934c ["CALL", null, ["callee:00c58130:8"]]
- 00bf8f24 bytes 837b0194
+ 00bf934c bytes 797b0194
- 00bf8f30 ["INT_ADD", "register:40f0:8", ["const:bf8f30:8", "const:4:8"]]
- 00bf8f30 ["CALL", null, ["callee:00c5e1f0:8"]]
+ 00bf9358 ["INT_ADD", "register:40f0:8", ["const:bf9358:8", "const:4:8"]]
+ 00bf9358 ["CALL", null, ["callee:00c5e1f0:8"]]
- 00bf8f30 bytes b0930194
+ 00bf9358 bytes a6930194
- 00bf8f3c ["INT_ADD", "register:40f0:8", ["const:bf8f3c:8", "const:4:8"]]
- 00bf8f3c ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf9364 ["INT_ADD", "register:40f0:8", ["const:bf9364:8", "const:4:8"]]
+ 00bf9364 ["CALL", null, ["callee:00c57e90:8"]]
- 00bf8f3c bytes d57a0194
+ 00bf9364 bytes cb7a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30e37522d6aa991f4710a1cb8ac6a979"></a>

### [`00bf9218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9218.md) → [`00bf9640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9640.md) _ZNSt6__ndk112future_errorD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58370.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf922c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9218.md#insn-00bf922c)
- 新版 [`00bf9654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9640.md#insn-00bf9654)

~~~diff
- 00bf922c ["INT_ADD", "register:40f0:8", ["const:bf922c:8", "const:4:8"]]
- 00bf922c ["CALL", null, ["callee:00c58370:8"]]
+ 00bf9654 ["INT_ADD", "register:40f0:8", ["const:bf9654:8", "const:4:8"]]
+ 00bf9654 ["CALL", null, ["callee:00c58370:8"]]
- 00bf922c bytes 517b0194
+ 00bf9654 bytes 477b0194
~~~


<a id="compare-cc77e039a982d6e212498f982d1ca030"></a>

### [`00bf9254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9254.md) → [`00bf967c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf967c.md) _ZNSt6__ndk117__assoc_sub_state9set_valueEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58150.md) · 呼出先 5件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md) [`00c57f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00c58550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58550.md) · 呼出先 5件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md) [`00c58380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9254.md#insn-00bf9270) · [`00bf9288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9254.md#insn-00bf9288) · [`00bf92a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9254.md#insn-00bf92a4)
- 新版 [`00bf9698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf967c.md#insn-00bf9698) · [`00bf96b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf967c.md#insn-00bf96b0) · [`00bf96cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf967c.md#insn-00bf96cc)

~~~diff
- 00bf9270 ["INT_ADD", "register:40f0:8", ["const:bf9270:8", "const:4:8"]]
- 00bf9270 ["CALL", null, ["callee:00c580e0:8"]]
+ 00bf9698 ["INT_ADD", "register:40f0:8", ["const:bf9698:8", "const:4:8"]]
+ 00bf9698 ["CALL", null, ["callee:00c580e0:8"]]
- 00bf9270 bytes 9c7a0194
+ 00bf9698 bytes 927a0194
- 00bf9288 ["INT_ADD", "register:40f0:8", ["const:bf9288:8", "const:4:8"]]
- 00bf9288 ["CALL", null, ["callee:00c582f0:8"]]
+ 00bf96b0 ["INT_ADD", "register:40f0:8", ["const:bf96b0:8", "const:4:8"]]
+ 00bf96b0 ["CALL", null, ["callee:00c582f0:8"]]
- 00bf9288 bytes 1a7b0194
+ 00bf96b0 bytes 107b0194
- 00bf92a4 ["INT_ADD", "register:40f0:8", ["const:bf92a4:8", "const:4:8"]]
- 00bf92a4 ["CALL", null, ["callee:00c58380:8"]]
+ 00bf96cc ["INT_ADD", "register:40f0:8", ["const:bf96cc:8", "const:4:8"]]
+ 00bf96cc ["CALL", null, ["callee:00c58380:8"]]
- 00bf92a4 bytes 377b0194
+ 00bf96cc bytes 2d7b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5c09a2cc3f111877d7039c74035ec31"></a>

### [`00bf92e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf92e0.md) → [`00bf9708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9708.md) _ZNSt6__ndk117__assoc_sub_state24set_value_at_thread_exitEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5de20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de20.md) · 呼出先 7件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d30.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c5e220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e220.md) · 呼出先 7件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c58130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58130.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf92fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf92e0.md#insn-00bf92fc) · [`00bf9314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf92e0.md#insn-00bf9314) · [`00bf9328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf92e0.md#insn-00bf9328)
- 新版 [`00bf9724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9708.md#insn-00bf9724) · [`00bf973c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9708.md#insn-00bf973c) · [`00bf9750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9708.md#insn-00bf9750)

~~~diff
- 00bf92fc ["INT_ADD", "register:40f0:8", ["const:bf92fc:8", "const:4:8"]]
- 00bf92fc ["CALL", null, ["callee:00c580e0:8"]]
+ 00bf9724 ["INT_ADD", "register:40f0:8", ["const:bf9724:8", "const:4:8"]]
+ 00bf9724 ["CALL", null, ["callee:00c580e0:8"]]
- 00bf92fc bytes 797a0194
+ 00bf9724 bytes 6f7a0194
- 00bf9314 ["INT_ADD", "register:40f0:8", ["const:bf9314:8", "const:4:8"]]
- 00bf9314 ["CALL", null, ["callee:00c582f0:8"]]
+ 00bf973c ["INT_ADD", "register:40f0:8", ["const:bf973c:8", "const:4:8"]]
+ 00bf973c ["CALL", null, ["callee:00c582f0:8"]]
- 00bf9314 bytes f77a0194
+ 00bf973c bytes ed7a0194
- 00bf9328 ["INT_ADD", "register:40f0:8", ["const:bf9328:8", "const:4:8"]]
- 00bf9328 ["CALL", null, ["callee:00c58130:8"]]
+ 00bf9750 ["INT_ADD", "register:40f0:8", ["const:bf9750:8", "const:4:8"]]
+ 00bf9750 ["CALL", null, ["callee:00c58130:8"]]
- 00bf9328 bytes 827a0194
+ 00bf9750 bytes 787a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2db8d4a4e7eb8d5121d1928b0432a57"></a>

### [`00bf9374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9374.md) → [`00bf979c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf979c.md) _ZNSt6__ndk117__assoc_sub_state13set_exceptionESt13exception_ptr

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c57f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f60.md) · 呼出先 6件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md) [`00c57f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00c58360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58360.md) · 呼出先 6件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md) [`00c58380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9374.md#insn-00bf9398) · [`00bf93b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9374.md#insn-00bf93b4) · [`00bf93c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9374.md#insn-00bf93c4)
- 新版 [`00bf97c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf979c.md#insn-00bf97c0) · [`00bf97dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf979c.md#insn-00bf97dc) · [`00bf97ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf979c.md#insn-00bf97ec)

~~~diff
- 00bf9398 ["INT_ADD", "register:40f0:8", ["const:bf9398:8", "const:4:8"]]
- 00bf9398 ["CALL", null, ["callee:00c580e0:8"]]
+ 00bf97c0 ["INT_ADD", "register:40f0:8", ["const:bf97c0:8", "const:4:8"]]
+ 00bf97c0 ["CALL", null, ["callee:00c580e0:8"]]
- 00bf9398 bytes 527a0194
+ 00bf97c0 bytes 487a0194
- 00bf93b4 ["INT_ADD", "register:40f0:8", ["const:bf93b4:8", "const:4:8"]]
- 00bf93b4 ["CALL", null, ["callee:00c582f0:8"]]
+ 00bf97dc ["INT_ADD", "register:40f0:8", ["const:bf97dc:8", "const:4:8"]]
+ 00bf97dc ["CALL", null, ["callee:00c582f0:8"]]
- 00bf93b4 bytes cf7a0194
+ 00bf97dc bytes c57a0194
- 00bf93c4 ["INT_ADD", "register:40f0:8", ["const:bf93c4:8", "const:4:8"]]
- 00bf93c4 ["CALL", null, ["callee:00c5df30:8"]]
+ 00bf97ec ["INT_ADD", "register:40f0:8", ["const:bf97ec:8", "const:4:8"]]
+ 00bf97ec ["CALL", null, ["callee:00c5df30:8"]]
- 00bf93c4 bytes db910194
+ 00bf97ec bytes d1910194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c532684bf2cf0ec2dfc03dd316a1d679"></a>

### [`00bf9418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9418.md) → [`00bf9840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9840.md) _ZNSt6__ndk117__assoc_sub_state28set_exception_at_thread_exitESt13exception_ptr

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5de40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de40.md) · 呼出先 8件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d30.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c5e240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e240.md) · 呼出先 8件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c58130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58130.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf943c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9418.md#insn-00bf943c) · [`00bf9458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9418.md#insn-00bf9458) · [`00bf9468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9418.md#insn-00bf9468)
- 新版 [`00bf9864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9840.md#insn-00bf9864) · [`00bf9880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9840.md#insn-00bf9880) · [`00bf9890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9840.md#insn-00bf9890)

~~~diff
- 00bf943c ["INT_ADD", "register:40f0:8", ["const:bf943c:8", "const:4:8"]]
- 00bf943c ["CALL", null, ["callee:00c580e0:8"]]
+ 00bf9864 ["INT_ADD", "register:40f0:8", ["const:bf9864:8", "const:4:8"]]
+ 00bf9864 ["CALL", null, ["callee:00c580e0:8"]]
- 00bf943c bytes 297a0194
+ 00bf9864 bytes 1f7a0194
- 00bf9458 ["INT_ADD", "register:40f0:8", ["const:bf9458:8", "const:4:8"]]
- 00bf9458 ["CALL", null, ["callee:00c582f0:8"]]
+ 00bf9880 ["INT_ADD", "register:40f0:8", ["const:bf9880:8", "const:4:8"]]
+ 00bf9880 ["CALL", null, ["callee:00c582f0:8"]]
- 00bf9458 bytes a67a0194
+ 00bf9880 bytes 9c7a0194
- 00bf9468 ["INT_ADD", "register:40f0:8", ["const:bf9468:8", "const:4:8"]]
- 00bf9468 ["CALL", null, ["callee:00c5df30:8"]]
+ 00bf9890 ["INT_ADD", "register:40f0:8", ["const:bf9890:8", "const:4:8"]]
+ 00bf9890 ["CALL", null, ["callee:00c5df30:8"]]
- 00bf9468 bytes b2910194
+ 00bf9890 bytes a8910194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55fc63321a2f7a31111feea578e6b374"></a>

### [`00bf94bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf94bc.md) → [`00bf98e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf98e4.md) _ZNSt6__ndk117__assoc_sub_state12__make_readyEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5de50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de50.md) · 呼出先 3件 [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00c5e250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e250.md) · 呼出先 3件 [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c58380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf94d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf94bc.md#insn-00bf94d4) · [`00bf94e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf94bc.md#insn-00bf94e8)
- 新版 [`00bf98fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf98e4.md#insn-00bf98fc) · [`00bf9910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf98e4.md#insn-00bf9910)

~~~diff
- 00bf94d4 ["INT_ADD", "register:40f0:8", ["const:bf94d4:8", "const:4:8"]]
- 00bf94d4 ["CALL", null, ["callee:00c580e0:8"]]
+ 00bf98fc ["INT_ADD", "register:40f0:8", ["const:bf98fc:8", "const:4:8"]]
+ 00bf98fc ["CALL", null, ["callee:00c580e0:8"]]
- 00bf94d4 bytes 037a0194
+ 00bf98fc bytes f9790194
- 00bf94e8 ["INT_ADD", "register:40f0:8", ["const:bf94e8:8", "const:4:8"]]
- 00bf94e8 ["CALL", null, ["callee:00c58380:8"]]
+ 00bf9910 ["INT_ADD", "register:40f0:8", ["const:bf9910:8", "const:4:8"]]
+ 00bf9910 ["CALL", null, ["callee:00c58380:8"]]
- 00bf94e8 bytes a67a0194
+ 00bf9910 bytes 9c7a0194
~~~


<a id="compare-4374534313b7fa30c366b68f0eafca8c"></a>

### [`00bf9500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9500.md) → [`00bf9928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9928.md) _ZNSt6__ndk117__assoc_sub_state4copyEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5de60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de60.md) · 呼出先 7件 [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md) [`00c58080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58080.md)
- 新版 呼出元 1件 [`00c5e260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e260.md) · 呼出先 7件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md) [`00c58480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf952c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9500.md#insn-00bf952c) · [`00bf9544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9500.md#insn-00bf9544) · [`00bf9560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9500.md#insn-00bf9560)
- 新版 [`00bf9954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9928.md#insn-00bf9954) · [`00bf996c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9928.md#insn-00bf996c) · [`00bf9988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9928.md#insn-00bf9988)

~~~diff
- 00bf952c ["INT_ADD", "register:40f0:8", ["const:bf952c:8", "const:4:8"]]
- 00bf952c ["CALL", null, ["callee:00c580e0:8"]]
+ 00bf9954 ["INT_ADD", "register:40f0:8", ["const:bf9954:8", "const:4:8"]]
+ 00bf9954 ["CALL", null, ["callee:00c580e0:8"]]
- 00bf952c bytes ed790194
+ 00bf9954 bytes e3790194
- 00bf9544 ["INT_ADD", "register:40f0:8", ["const:bf9544:8", "const:4:8"]]
- 00bf9544 ["CALL", null, ["callee:00c58480:8"]]
+ 00bf996c ["INT_ADD", "register:40f0:8", ["const:bf996c:8", "const:4:8"]]
+ 00bf996c ["CALL", null, ["callee:00c58480:8"]]
- 00bf9544 bytes cf7a0194
+ 00bf996c bytes c57a0194
- 00bf9560 ["INT_ADD", "register:40f0:8", ["const:bf9560:8", "const:4:8"]]
- 00bf9560 ["CALL", null, ["callee:00c580f0:8"]]
+ 00bf9988 ["INT_ADD", "register:40f0:8", ["const:bf9988:8", "const:4:8"]]
+ 00bf9988 ["CALL", null, ["callee:00c580f0:8"]]
- 00bf9560 bytes e4790194
+ 00bf9988 bytes da790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb80a01d4fbea49f27dabe143f58a5b5"></a>

### [`00bf9678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9678.md) → [`00bf9aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9aa0.md) _ZNSt6__ndk117__assoc_sub_state4waitEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58130.md) · 呼出先 3件 [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c58080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58080.md)
- 新版 呼出元 1件 [`00c58530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58530.md) · 呼出先 3件 [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c58480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf96a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9678.md#insn-00bf96a4) · [`00bf96bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9678.md#insn-00bf96bc) · [`00bf96d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9678.md#insn-00bf96d4)
- 新版 [`00bf9acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9aa0.md#insn-00bf9acc) · [`00bf9ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9aa0.md#insn-00bf9ae4) · [`00bf9afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9aa0.md#insn-00bf9afc)

~~~diff
- 00bf96a4 ["INT_ADD", "register:40f0:8", ["const:bf96a4:8", "const:4:8"]]
- 00bf96a4 ["CALL", null, ["callee:00c580e0:8"]]
+ 00bf9acc ["INT_ADD", "register:40f0:8", ["const:bf9acc:8", "const:4:8"]]
+ 00bf9acc ["CALL", null, ["callee:00c580e0:8"]]
- 00bf96a4 bytes 8f790194
+ 00bf9acc bytes 85790194
- 00bf96bc ["INT_ADD", "register:40f0:8", ["const:bf96bc:8", "const:4:8"]]
- 00bf96bc ["CALL", null, ["callee:00c58480:8"]]
+ 00bf9ae4 ["INT_ADD", "register:40f0:8", ["const:bf9ae4:8", "const:4:8"]]
+ 00bf9ae4 ["CALL", null, ["callee:00c58480:8"]]
- 00bf96bc bytes 717a0194
+ 00bf9ae4 bytes 677a0194
- 00bf96d4 ["INT_ADD", "register:40f0:8", ["const:bf96d4:8", "const:4:8"]]
- 00bf96d4 ["CALL", null, ["callee:00c580f0:8"]]
+ 00bf9afc ["INT_ADD", "register:40f0:8", ["const:bf9afc:8", "const:4:8"]]
+ 00bf9afc ["CALL", null, ["callee:00c580f0:8"]]
- 00bf96d4 bytes 87790194
+ 00bf9afc bytes 7d790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d64cf3d2266457b17583d58dd72ff437"></a>

### [`00bf971c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf971c.md) → [`00bf9b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9b44.md) _ZNSt6__ndk117__assoc_sub_state9__executeEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf972c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf971c.md#insn-00bf972c)
- 新版 [`00bf9b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9b44.md#insn-00bf9b54)

~~~diff
- 00bf972c ["INT_ADD", "register:40f0:8", ["const:bf972c:8", "const:4:8"]]
- 00bf972c ["CALL", null, ["callee:0045a6d4:8"]]
+ 00bf9b54 ["INT_ADD", "register:40f0:8", ["const:bf9b54:8", "const:4:8"]]
+ 00bf9b54 ["CALL", null, ["callee:0045a6d4:8"]]
- 00bf972c bytes da83e197
+ 00bf9b54 bytes e082e197
~~~


<a id="compare-9250d47ac4322b634ec8f90393ff4c48"></a>

### [`00bf9730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9730.md) → [`00bf9b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9b58.md) _ZNSt6__ndk16futureIvEC1EPNS_17__assoc_sub_stateE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58120.md) · 呼出先 4件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)
- 新版 呼出元 1件 [`00c58520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58520.md) · 呼出先 4件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf974c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9730.md#insn-00bf974c) · [`00bf9760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9730.md#insn-00bf9760) · [`00bf9784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9730.md#insn-00bf9784)
- 新版 [`00bf9b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9b58.md#insn-00bf9b74) · [`00bf9b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9b58.md#insn-00bf9b88) · [`00bf9bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9b58.md#insn-00bf9bac)

~~~diff
- 00bf974c ["INT_ADD", "register:40f0:8", ["const:bf974c:8", "const:4:8"]]
- 00bf974c ["CALL", null, ["callee:00c580e0:8"]]
+ 00bf9b74 ["INT_ADD", "register:40f0:8", ["const:bf9b74:8", "const:4:8"]]
+ 00bf9b74 ["CALL", null, ["callee:00c580e0:8"]]
- 00bf974c bytes 65790194
+ 00bf9b74 bytes 5b790194
- 00bf9760 ["INT_ADD", "register:40f0:8", ["const:bf9760:8", "const:4:8"]]
- 00bf9760 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00bf9b88 ["INT_ADD", "register:40f0:8", ["const:bf9b88:8", "const:4:8"]]
+ 00bf9b88 ["CALL", null, ["callee:00c53cd0:8"]]
- 00bf9760 bytes 54680194
+ 00bf9b88 bytes 52680194
- 00bf9784 ["INT_ADD", "register:40f0:8", ["const:bf9784:8", "const:4:8"]]
- 00bf9784 ["CALL", null, ["callee:0045a6d4:8"]]
+ 00bf9bac ["INT_ADD", "register:40f0:8", ["const:bf9bac:8", "const:4:8"]]
+ 00bf9bac ["CALL", null, ["callee:0045a6d4:8"]]
- 00bf9784 bytes c483e197
+ 00bf9bac bytes ca82e197
~~~


<a id="compare-6c1f521bfcc1013780c9ca6137a6babe"></a>

### [`00bf979c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf979c.md) → [`00bf9bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9bc4.md) _ZNSt6__ndk16futureIvED1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c580e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580e0.md) · 呼出先 1件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c584e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584e0.md) · 呼出先 1件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf97bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf979c.md#insn-00bf97bc)
- 新版 [`00bf9be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9bc4.md#insn-00bf9be4)

~~~diff
- 00bf97bc ["INT_ADD", "register:40f0:8", ["const:bf97bc:8", "const:4:8"]]
- 00bf97bc ["CALL", null, ["callee:00c53d00:8"]]
+ 00bf9be4 ["INT_ADD", "register:40f0:8", ["const:bf9be4:8", "const:4:8"]]
+ 00bf9be4 ["CALL", null, ["callee:00c53d00:8"]]
- 00bf97bc bytes 49680194
+ 00bf9be4 bytes 47680194
~~~


<a id="compare-b9ea2fd2676ec0c99d9666bad8de4e1c"></a>

### [`00bf97f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf97f0.md) → [`00bf9c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9c18.md) _ZNSt6__ndk16futureIvE3getEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5de60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5e260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e260.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf980c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf97f0.md#insn-00bf980c) · [`00bf9818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf97f0.md#insn-00bf9818)
- 新版 [`00bf9c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9c18.md#insn-00bf9c34) · [`00bf9c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9c18.md#insn-00bf9c40)

~~~diff
- 00bf980c ["INT_ADD", "register:40f0:8", ["const:bf980c:8", "const:4:8"]]
- 00bf980c ["CALL", null, ["callee:00c5e260:8"]]
+ 00bf9c34 ["INT_ADD", "register:40f0:8", ["const:bf9c34:8", "const:4:8"]]
+ 00bf9c34 ["CALL", null, ["callee:00c5e260:8"]]
- 00bf980c bytes 95910194
+ 00bf9c34 bytes 8b910194
- 00bf9818 ["INT_ADD", "register:40f0:8", ["const:bf9818:8", "const:4:8"]]
- 00bf9818 ["CALL", null, ["callee:00c53d00:8"]]
+ 00bf9c40 ["INT_ADD", "register:40f0:8", ["const:bf9c40:8", "const:4:8"]]
+ 00bf9c40 ["CALL", null, ["callee:00c53d00:8"]]
- 00bf9818 bytes 32680194
+ 00bf9c40 bytes 30680194
~~~


<a id="compare-23281fe25f17d5cf6d0191ac2861e65b"></a>

### [`00bf9a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9a64.md) → [`00bf9e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9e8c.md) _ZNSt6__ndk17promiseIvE10get_futureEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00c58120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58120.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c58520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58520.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9a64.md#insn-00bf9a88)
- 新版 [`00bf9eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9e8c.md#insn-00bf9eb0)

~~~diff
- 00bf9a88 ["INT_ADD", "register:40f0:8", ["const:bf9a88:8", "const:4:8"]]
- 00bf9a88 ["CALL", null, ["callee:0045a6d4:8"]]
+ 00bf9eb0 ["INT_ADD", "register:40f0:8", ["const:bf9eb0:8", "const:4:8"]]
+ 00bf9eb0 ["CALL", null, ["callee:0045a6d4:8"]]
- 00bf9a88 bytes 0383e197
+ 00bf9eb0 bytes 0982e197
~~~


<a id="compare-71a9f5debbd30eec46161fdcc188b4b3"></a>

### [`00bf9a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9a8c.md) → [`00bf9eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9eb4.md) _ZNSt6__ndk17promiseIvE9set_valueEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00c58150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58150.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c58550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9a8c.md#insn-00bf9aac)
- 新版 [`00bf9ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9eb4.md#insn-00bf9ed4)

~~~diff
- 00bf9aac ["INT_ADD", "register:40f0:8", ["const:bf9aac:8", "const:4:8"]]
- 00bf9aac ["CALL", null, ["callee:0045a6d4:8"]]
+ 00bf9ed4 ["INT_ADD", "register:40f0:8", ["const:bf9ed4:8", "const:4:8"]]
+ 00bf9ed4 ["CALL", null, ["callee:0045a6d4:8"]]
- 00bf9aac bytes fa82e197
+ 00bf9ed4 bytes 0082e197
~~~


<a id="compare-03f7e8312d6b22055830792b5366e339"></a>

### [`00bf9ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9ab0.md) → [`00bf9ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9ed8.md) _ZNSt6__ndk17promiseIvE13set_exceptionESt13exception_ptr

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md) [`00c57f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f60.md) [`00c580b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md) [`00c58360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58360.md) [`00c584b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9ab0.md#insn-00bf9acc) · [`00bf9ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9ab0.md#insn-00bf9ad8) · [`00bf9ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9ab0.md#insn-00bf9ae0)
- 新版 [`00bf9ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9ed8.md#insn-00bf9ef4) · [`00bf9f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9ed8.md#insn-00bf9f00) · [`00bf9f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9ed8.md#insn-00bf9f08)

~~~diff
- 00bf9acc ["INT_ADD", "register:40f0:8", ["const:bf9acc:8", "const:4:8"]]
- 00bf9acc ["CALL", null, ["callee:00c584b0:8"]]
+ 00bf9ef4 ["INT_ADD", "register:40f0:8", ["const:bf9ef4:8", "const:4:8"]]
+ 00bf9ef4 ["CALL", null, ["callee:00c584b0:8"]]
- 00bf9acc bytes 79790194
+ 00bf9ef4 bytes 6f790194
- 00bf9ad8 ["INT_ADD", "register:40f0:8", ["const:bf9ad8:8", "const:4:8"]]
- 00bf9ad8 ["CALL", null, ["callee:00c58360:8"]]
+ 00bf9f00 ["INT_ADD", "register:40f0:8", ["const:bf9f00:8", "const:4:8"]]
+ 00bf9f00 ["CALL", null, ["callee:00c58360:8"]]
- 00bf9ad8 bytes 22790194
+ 00bf9f00 bytes 18790194
- 00bf9ae0 ["INT_ADD", "register:40f0:8", ["const:bf9ae0:8", "const:4:8"]]
- 00bf9ae0 ["CALL", null, ["callee:00c582f0:8"]]
+ 00bf9f08 ["INT_ADD", "register:40f0:8", ["const:bf9f08:8", "const:4:8"]]
+ 00bf9f08 ["CALL", null, ["callee:00c582f0:8"]]
- 00bf9ae0 bytes 04790194
+ 00bf9f08 bytes fa780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f414ae5b71df2563c2697ab46e810f4"></a>

### [`00bf9b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9b10.md) → [`00bf9f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9f38.md) _ZNSt6__ndk17promiseIvE24set_value_at_thread_exitEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00c5de20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c5e220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9b10.md#insn-00bf9b30)
- 新版 [`00bf9f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9f38.md#insn-00bf9f58)

~~~diff
- 00bf9b30 ["INT_ADD", "register:40f0:8", ["const:bf9b30:8", "const:4:8"]]
- 00bf9b30 ["CALL", null, ["callee:0045a6d4:8"]]
+ 00bf9f58 ["INT_ADD", "register:40f0:8", ["const:bf9f58:8", "const:4:8"]]
+ 00bf9f58 ["CALL", null, ["callee:0045a6d4:8"]]
- 00bf9b30 bytes d982e197
+ 00bf9f58 bytes df81e197
~~~


<a id="compare-6d714e92719cf8b1259e77df30a8b52e"></a>

### [`00bf9b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9b34.md) → [`00bf9f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9f5c.md) _ZNSt6__ndk17promiseIvE28set_exception_at_thread_exitESt13exception_ptr

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md) [`00c580b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580b0.md) [`00c5de40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md) [`00c584b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584b0.md) [`00c5e240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9b34.md#insn-00bf9b50) · [`00bf9b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9b34.md#insn-00bf9b5c) · [`00bf9b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9b34.md#insn-00bf9b64)
- 新版 [`00bf9f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9f5c.md#insn-00bf9f78) · [`00bf9f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9f5c.md#insn-00bf9f84) · [`00bf9f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9f5c.md#insn-00bf9f8c)

~~~diff
- 00bf9b50 ["INT_ADD", "register:40f0:8", ["const:bf9b50:8", "const:4:8"]]
- 00bf9b50 ["CALL", null, ["callee:00c584b0:8"]]
+ 00bf9f78 ["INT_ADD", "register:40f0:8", ["const:bf9f78:8", "const:4:8"]]
+ 00bf9f78 ["CALL", null, ["callee:00c584b0:8"]]
- 00bf9b50 bytes 58790194
+ 00bf9f78 bytes 4e790194
- 00bf9b5c ["INT_ADD", "register:40f0:8", ["const:bf9b5c:8", "const:4:8"]]
- 00bf9b5c ["CALL", null, ["callee:00c5e240:8"]]
+ 00bf9f84 ["INT_ADD", "register:40f0:8", ["const:bf9f84:8", "const:4:8"]]
+ 00bf9f84 ["CALL", null, ["callee:00c5e240:8"]]
- 00bf9b5c bytes b9900194
+ 00bf9f84 bytes af900194
- 00bf9b64 ["INT_ADD", "register:40f0:8", ["const:bf9b64:8", "const:4:8"]]
- 00bf9b64 ["CALL", null, ["callee:00c582f0:8"]]
+ 00bf9f8c ["INT_ADD", "register:40f0:8", ["const:bf9f8c:8", "const:4:8"]]
+ 00bf9f8c ["CALL", null, ["callee:00c582f0:8"]]
- 00bf9b64 bytes e3780194
+ 00bf9f8c bytes d9780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c597bd207b13c31695014b925c9a73a"></a>

### [`00bf9b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9b94.md) → [`00bf9fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9fbc.md) _ZNSt6__ndk113shared_futureIvED1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9b94.md#insn-00bf9bb4)
- 新版 [`00bf9fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9fbc.md#insn-00bf9fdc)

~~~diff
- 00bf9bb4 ["INT_ADD", "register:40f0:8", ["const:bf9bb4:8", "const:4:8"]]
- 00bf9bb4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00bf9fdc ["INT_ADD", "register:40f0:8", ["const:bf9fdc:8", "const:4:8"]]
+ 00bf9fdc ["CALL", null, ["callee:00c53d00:8"]]
- 00bf9bb4 bytes 4b670194
+ 00bf9fdc bytes 49670194
~~~


<a id="compare-2ebe3f8d5928300452fdf00a63741662"></a>

### [`00bf9be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9be8.md) → [`00bfa010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa010.md) _ZNSt6__ndk113shared_futureIvEaSERKS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9be8.md#insn-00bf9c14) · [`00bf9c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9be8.md#insn-00bf9c28) · [`00bf9c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9be8.md#insn-00bf9c3c)
- 新版 [`00bfa03c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa010.md#insn-00bfa03c) · [`00bfa050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa010.md#insn-00bfa050) · [`00bfa064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa010.md#insn-00bfa064)

~~~diff
- 00bf9c14 ["INT_ADD", "register:40f0:8", ["const:bf9c14:8", "const:4:8"]]
- 00bf9c14 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00bfa03c ["INT_ADD", "register:40f0:8", ["const:bfa03c:8", "const:4:8"]]
+ 00bfa03c ["CALL", null, ["callee:00c53cd0:8"]]
- 00bf9c14 bytes 27670194
+ 00bfa03c bytes 25670194
- 00bf9c28 ["INT_ADD", "register:40f0:8", ["const:bf9c28:8", "const:4:8"]]
- 00bf9c28 ["CALL", null, ["callee:00c53d00:8"]]
+ 00bfa050 ["INT_ADD", "register:40f0:8", ["const:bfa050:8", "const:4:8"]]
+ 00bfa050 ["CALL", null, ["callee:00c53d00:8"]]
- 00bf9c28 bytes 2e670194
+ 00bfa050 bytes 2c670194
- 00bf9c3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bf9c3c ["INT_ADD", "register:40f0:8", ["const:bf9c3c:8", "const:4:8"]]
- 00bf9c3c ["CALLIND", null, ["register:0:8"]]
+ 00bfa064 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfa064 ["INT_ADD", "register:40f0:8", ["const:bfa064:8", "const:4:8"]]
+ 00bfa064 ["CALLIND", null, ["register:0:8"]]
- 00bf9c3c bytes 00013fd6
+ 00bfa064 bytes 00013fd6
~~~


<a id="compare-9f9dc9eeb6409c68dee4363b1c2ff879"></a>

### [`00bf9cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9cbc.md) → [`00bfa0e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa0e4.md) FUN_00bfa0e4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5daf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5daf0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5def0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5def0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9cbc.md#insn-00bf9cd0)
- 新版 [`00bfa0f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa0e4.md#insn-00bfa0f8)

~~~diff
- 00bf9cd0 ["INT_ADD", "register:40f0:8", ["const:bf9cd0:8", "const:4:8"]]
- 00bf9cd0 ["CALL", null, ["callee:00c5def0:8"]]
+ 00bfa0f8 ["INT_ADD", "register:40f0:8", ["const:bfa0f8:8", "const:4:8"]]
+ 00bfa0f8 ["CALL", null, ["callee:00c5def0:8"]]
- 00bf9cd0 bytes 888f0194
+ 00bfa0f8 bytes 7e8f0194
~~~


<a id="compare-ca99cc5508003e1f3f883f349d2bc2cf"></a>

### [`00bf9ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9ce8.md) → [`00bfa110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa110.md) _ZNSt6__ndk15mutexD1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`0043ae38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae38.md) [`004524a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/004524a8.md) [`00452c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md) [`0048bab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048bab0.md) [`0058f670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f670.md) · 呼出先 1件 [`00c5b290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b290.md)
- 新版 呼出元 6件 [`0043ae78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae78.md) [`004524e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/004524e8.md) [`00452c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md) [`0048baf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048baf0.md) [`0058f6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f6b0.md) · 呼出先 1件 [`00c5b690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b690.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9ce8.md#insn-00bf9cf4)
- 新版 [`00bfa11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa110.md#insn-00bfa11c)

~~~diff
- 00bf9cf4 ["INT_ADD", "register:40f0:8", ["const:bf9cf4:8", "const:4:8"]]
- 00bf9cf4 ["CALL", null, ["callee:00c5b690:8"]]
+ 00bfa11c ["INT_ADD", "register:40f0:8", ["const:bfa11c:8", "const:4:8"]]
+ 00bfa11c ["CALL", null, ["callee:00c5b690:8"]]
- 00bf9cf4 bytes 67850194
+ 00bfa11c bytes 5d850194
~~~


<a id="compare-c12d51a8b1c186b4f7e5e89b79922779"></a>

### [`00bf9d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9d34.md) → [`00bfa15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa15c.md) _ZNSt6__ndk15mutex8try_lockEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5de70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9d34.md#insn-00bf9d40)
- 新版 [`00bfa168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa15c.md#insn-00bfa168)

~~~diff
- 00bf9d40 ["INT_ADD", "register:40f0:8", ["const:bf9d40:8", "const:4:8"]]
- 00bf9d40 ["CALL", null, ["callee:00c5e270:8"]]
+ 00bfa168 ["INT_ADD", "register:40f0:8", ["const:bfa168:8", "const:4:8"]]
+ 00bfa168 ["CALL", null, ["callee:00c5e270:8"]]
- 00bf9d40 bytes 4c900194
+ 00bfa168 bytes 42900194
~~~


<a id="compare-b498323dee2da967a2f56709ebdeae4b"></a>

### [`00bf9d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9d5c.md) → [`00bfa184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa184.md) _ZNSt6__ndk15mutex6unlockEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) · 呼出先 1件 [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)
- 新版 呼出元 1件 [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) · 呼出先 1件 [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9d5c.md#insn-00bf9d68)
- 新版 [`00bfa190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa184.md#insn-00bfa190)

~~~diff
- 00bf9d68 ["INT_ADD", "register:40f0:8", ["const:bf9d68:8", "const:4:8"]]
- 00bf9d68 ["CALL", null, ["callee:00c5b6b0:8"]]
+ 00bfa190 ["INT_ADD", "register:40f0:8", ["const:bfa190:8", "const:4:8"]]
+ 00bfa190 ["CALL", null, ["callee:00c5b6b0:8"]]
- 00bf9d68 bytes 52850194
+ 00bfa190 bytes 48850194
~~~


<a id="compare-e11b67b56116d76113b9330009cd224d"></a>

### [`00bf9e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9e20.md) → [`00bfa248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa248.md) _ZNSt6__ndk115recursive_mutexD1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59cd0.md) · 呼出先 1件 [`00c5b290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b290.md)
- 新版 呼出元 1件 [`00c5a0d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0d0.md) · 呼出先 1件 [`00c5b690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b690.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9e20.md#insn-00bf9e2c)
- 新版 [`00bfa254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa248.md#insn-00bfa254)

~~~diff
- 00bf9e2c ["INT_ADD", "register:40f0:8", ["const:bf9e2c:8", "const:4:8"]]
- 00bf9e2c ["CALL", null, ["callee:00c5b690:8"]]
+ 00bfa254 ["INT_ADD", "register:40f0:8", ["const:bfa254:8", "const:4:8"]]
+ 00bfa254 ["CALL", null, ["callee:00c5b690:8"]]
- 00bf9e2c bytes 19850194
+ 00bfa254 bytes 0f850194
~~~


<a id="compare-d0b58365a79116eb1b24fa06e9079e01"></a>

### [`00bf9e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9e6c.md) → [`00bfa294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa294.md) _ZNSt6__ndk115recursive_mutex6unlockEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59cf0.md) · 呼出先 1件 [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)
- 新版 呼出元 1件 [`00c5a0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0f0.md) · 呼出先 1件 [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9e6c.md#insn-00bf9e78)
- 新版 [`00bfa2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa294.md#insn-00bfa2a0)

~~~diff
- 00bf9e78 ["INT_ADD", "register:40f0:8", ["const:bf9e78:8", "const:4:8"]]
- 00bf9e78 ["CALL", null, ["callee:00c5b6b0:8"]]
+ 00bfa2a0 ["INT_ADD", "register:40f0:8", ["const:bfa2a0:8", "const:4:8"]]
+ 00bfa2a0 ["CALL", null, ["callee:00c5b6b0:8"]]
- 00bf9e78 bytes 0e850194
+ 00bfa2a0 bytes 04850194
~~~


<a id="compare-2ef4664dec9ea3e6422b03f33960bb5b"></a>

### [`00bf9e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9e8c.md) → [`00bfa2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa2b4.md) _ZNSt6__ndk115recursive_mutex8try_lockEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5de70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9e8c.md#insn-00bf9e98)
- 新版 [`00bfa2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa2b4.md#insn-00bfa2c0)

~~~diff
- 00bf9e98 ["INT_ADD", "register:40f0:8", ["const:bf9e98:8", "const:4:8"]]
- 00bf9e98 ["CALL", null, ["callee:00c5e270:8"]]
+ 00bfa2c0 ["INT_ADD", "register:40f0:8", ["const:bfa2c0:8", "const:4:8"]]
+ 00bfa2c0 ["CALL", null, ["callee:00c5e270:8"]]
- 00bf9e98 bytes f68f0194
+ 00bfa2c0 bytes ec8f0194
~~~


<a id="compare-44953720bce21203ce0fe5763186c76b"></a>

### [`00bf9fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9fb4.md) → [`00bfa3dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa3dc.md) _ZNSt6__ndk111timed_mutex8try_lockEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md) [`00c5de70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md) [`00c5e270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf9fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9fb4.md#insn-00bf9fc8) · [`00bf9ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9fb4.md#insn-00bf9ff4)
- 新版 [`00bfa3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa3dc.md#insn-00bfa3f0) · [`00bfa41c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa3dc.md#insn-00bfa41c)

~~~diff
- 00bf9fc8 ["INT_ADD", "register:40f0:8", ["const:bf9fc8:8", "const:4:8"]]
- 00bf9fc8 ["CALL", null, ["callee:00c5e270:8"]]
+ 00bfa3f0 ["INT_ADD", "register:40f0:8", ["const:bfa3f0:8", "const:4:8"]]
+ 00bfa3f0 ["CALL", null, ["callee:00c5e270:8"]]
- 00bf9fc8 bytes aa8f0194
+ 00bfa3f0 bytes a08f0194
- 00bf9ff4 ["INT_ADD", "register:40f0:8", ["const:bf9ff4:8", "const:4:8"]]
- 00bf9ff4 ["CALL", null, ["callee:00c5b6b0:8"]]
+ 00bfa41c ["INT_ADD", "register:40f0:8", ["const:bfa41c:8", "const:4:8"]]
+ 00bfa41c ["CALL", null, ["callee:00c5b6b0:8"]]
- 00bf9ff4 bytes af840194
+ 00bfa41c bytes a5840194
~~~


<a id="compare-c241616e23fdfae2e2e9f3b0557513cd"></a>

### [`00bfa1b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa1b8.md) → [`00bfa5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa5e0.md) _ZNSt6__ndk121recursive_timed_mutex8try_lockEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58220.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md) [`00c5de70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de70.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58620.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md) [`00c5e270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfa1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa1b8.md#insn-00bfa1d0) · [`00bfa1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa1b8.md#insn-00bfa1dc) · [`00bfa21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa1b8.md#insn-00bfa21c)
- 新版 [`00bfa5f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa5e0.md#insn-00bfa5f8) · [`00bfa604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa5e0.md#insn-00bfa604) · [`00bfa644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa5e0.md#insn-00bfa644)

~~~diff
- 00bfa1d0 ["INT_ADD", "register:40f0:8", ["const:bfa1d0:8", "const:4:8"]]
- 00bfa1d0 ["CALL", null, ["callee:00c58620:8"]]
+ 00bfa5f8 ["INT_ADD", "register:40f0:8", ["const:bfa5f8:8", "const:4:8"]]
+ 00bfa5f8 ["CALL", null, ["callee:00c58620:8"]]
- 00bfa1d0 bytes 14780194
+ 00bfa5f8 bytes 0a780194
- 00bfa1dc ["INT_ADD", "register:40f0:8", ["const:bfa1dc:8", "const:4:8"]]
- 00bfa1dc ["CALL", null, ["callee:00c5e270:8"]]
+ 00bfa604 ["INT_ADD", "register:40f0:8", ["const:bfa604:8", "const:4:8"]]
+ 00bfa604 ["CALL", null, ["callee:00c5e270:8"]]
- 00bfa1dc bytes 258f0194
+ 00bfa604 bytes 1b8f0194
- 00bfa21c ["INT_ADD", "register:40f0:8", ["const:bfa21c:8", "const:4:8"]]
- 00bfa21c ["CALL", null, ["callee:00c5b6b0:8"]]
+ 00bfa644 ["INT_ADD", "register:40f0:8", ["const:bfa644:8", "const:4:8"]]
+ 00bfa644 ["CALL", null, ["callee:00c5b6b0:8"]]
- 00bfa21c bytes 25840194
+ 00bfa644 bytes 1b840194
~~~


