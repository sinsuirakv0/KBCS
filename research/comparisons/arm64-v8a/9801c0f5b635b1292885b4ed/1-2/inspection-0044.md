# v16.0.0 → v16.0.1 · 要調査の変更候補 (44)

[一覧の目次](README.md)

<a id="compare-d993aee27e04c5e0da714eac8d1bec59"></a>

### [`00c34d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d0c.md) → [`00c35134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35134.md) FUN_00c35134

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c36a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36a54.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c36e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36e7c.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d0c.md#insn-00c34d24)
- 新版 [`00c3514c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35134.md#insn-00c3514c)

~~~diff
- 00c34d24 ["INT_ADD", "register:40f0:8", ["const:c34d24:8", "const:4:8"]]
- 00c34d24 ["CALL", null, ["callee:00c36e7c:8"]]
+ 00c3514c ["INT_ADD", "register:40f0:8", ["const:c3514c:8", "const:4:8"]]
+ 00c3514c ["CALL", null, ["callee:00c36e7c:8"]]
- 00c34d24 bytes 4c070094
+ 00c3514c bytes 4c070094
~~~


<a id="compare-b9141aa974a62f7fc7cc36ea0c3b5d36"></a>

### [`00c34d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d3c.md) → [`00c35164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35164.md) FUN_00c35164

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c36a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36a54.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c36e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36e7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d3c.md#insn-00c34d54) · [`00c34d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d3c.md#insn-00c34d5c)
- 新版 [`00c3517c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35164.md#insn-00c3517c) · [`00c35184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35164.md#insn-00c35184)

~~~diff
- 00c34d54 ["INT_ADD", "register:40f0:8", ["const:c34d54:8", "const:4:8"]]
- 00c34d54 ["CALL", null, ["callee:00c36e7c:8"]]
+ 00c3517c ["INT_ADD", "register:40f0:8", ["const:c3517c:8", "const:4:8"]]
+ 00c3517c ["CALL", null, ["callee:00c36e7c:8"]]
- 00c34d54 bytes 40070094
+ 00c3517c bytes 40070094
- 00c34d5c ["INT_ADD", "register:40f0:8", ["const:c34d5c:8", "const:4:8"]]
- 00c34d5c ["CALL", null, ["callee:00c58300:8"]]
+ 00c35184 ["INT_ADD", "register:40f0:8", ["const:c35184:8", "const:4:8"]]
+ 00c35184 ["CALL", null, ["callee:00c58300:8"]]
- 00c34d5c bytes 698c0094
+ 00c35184 bytes 5f8c0094
~~~


<a id="compare-76e4a8dad3a87b9e3c6632874e13f14b"></a>

### [`00c34e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e28.md) → [`00c35250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35250.md) FUN_00c35250

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md) [`00c5e950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e950.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5ed50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e28.md#insn-00c34e40) · [`00c34e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e28.md#insn-00c34e48)
- 新版 [`00c35268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35250.md#insn-00c35268) · [`00c35270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35250.md#insn-00c35270)

~~~diff
- 00c34e40 ["INT_ADD", "register:40f0:8", ["const:c34e40:8", "const:4:8"]]
- 00c34e40 ["CALL", null, ["callee:00c5ed50:8"]]
+ 00c35268 ["INT_ADD", "register:40f0:8", ["const:c35268:8", "const:4:8"]]
+ 00c35268 ["CALL", null, ["callee:00c5ed50:8"]]
- 00c34e40 bytes c4a60094
+ 00c35268 bytes baa60094
- 00c34e48 ["INT_ADD", "register:40f0:8", ["const:c34e48:8", "const:4:8"]]
- 00c34e48 ["CALL", null, ["callee:00c58300:8"]]
+ 00c35270 ["INT_ADD", "register:40f0:8", ["const:c35270:8", "const:4:8"]]
+ 00c35270 ["CALL", null, ["callee:00c58300:8"]]
- 00c34e48 bytes 2e8c0094
+ 00c35270 bytes 248c0094
~~~


<a id="compare-8f5c3b2e0e38c2c2091db7a231cea8f4"></a>

### [`00c34e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e60.md) → [`00c35288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35288.md) FUN_00c35288

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md) [`00c5e950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e950.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5ed50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e60.md#insn-00c34e78) · [`00c34e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e60.md#insn-00c34e80)
- 新版 [`00c352a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35288.md#insn-00c352a0) · [`00c352a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35288.md#insn-00c352a8)

~~~diff
- 00c34e78 ["INT_ADD", "register:40f0:8", ["const:c34e78:8", "const:4:8"]]
- 00c34e78 ["CALL", null, ["callee:00c5ed50:8"]]
+ 00c352a0 ["INT_ADD", "register:40f0:8", ["const:c352a0:8", "const:4:8"]]
+ 00c352a0 ["CALL", null, ["callee:00c5ed50:8"]]
- 00c34e78 bytes b6a60094
+ 00c352a0 bytes aca60094
- 00c34e80 ["INT_ADD", "register:40f0:8", ["const:c34e80:8", "const:4:8"]]
- 00c34e80 ["CALL", null, ["callee:00c58300:8"]]
+ 00c352a8 ["INT_ADD", "register:40f0:8", ["const:c352a8:8", "const:4:8"]]
+ 00c352a8 ["CALL", null, ["callee:00c58300:8"]]
- 00c34e80 bytes 208c0094
+ 00c352a8 bytes 168c0094
~~~


<a id="compare-3a374c2213ea4d833fd7e2447850f874"></a>

### [`00c34e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e98.md) → [`00c352c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c352c0.md) FUN_00c352c0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md) [`00c5e950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e950.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5ed50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e98.md#insn-00c34eb0)
- 新版 [`00c352d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c352c0.md#insn-00c352d8)

~~~diff
- 00c34eb0 ["INT_ADD", "register:40f0:8", ["const:c34eb0:8", "const:4:8"]]
- 00c34eb0 ["CALL", null, ["callee:00c5ed50:8"]]
+ 00c352d8 ["INT_ADD", "register:40f0:8", ["const:c352d8:8", "const:4:8"]]
+ 00c352d8 ["CALL", null, ["callee:00c5ed50:8"]]
- 00c34eb0 bytes a8a60094
+ 00c352d8 bytes 9ea60094
~~~


<a id="compare-2693adfff8f21cae0f5b476863cdf685"></a>

### [`00c34ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34ec8.md) → [`00c352f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c352f0.md) FUN_00c352f0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md) [`00c5e950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e950.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5ed50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34ec8.md#insn-00c34ee0) · [`00c34ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34ec8.md#insn-00c34ee8)
- 新版 [`00c35308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c352f0.md#insn-00c35308) · [`00c35310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c352f0.md#insn-00c35310)

~~~diff
- 00c34ee0 ["INT_ADD", "register:40f0:8", ["const:c34ee0:8", "const:4:8"]]
- 00c34ee0 ["CALL", null, ["callee:00c5ed50:8"]]
+ 00c35308 ["INT_ADD", "register:40f0:8", ["const:c35308:8", "const:4:8"]]
+ 00c35308 ["CALL", null, ["callee:00c5ed50:8"]]
- 00c34ee0 bytes 9ca60094
+ 00c35308 bytes 92a60094
- 00c34ee8 ["INT_ADD", "register:40f0:8", ["const:c34ee8:8", "const:4:8"]]
- 00c34ee8 ["CALL", null, ["callee:00c58300:8"]]
+ 00c35310 ["INT_ADD", "register:40f0:8", ["const:c35310:8", "const:4:8"]]
+ 00c35310 ["CALL", null, ["callee:00c58300:8"]]
- 00c34ee8 bytes 068c0094
+ 00c35310 bytes fc8b0094
~~~


<a id="compare-7371b685fff6e1268ce80dbf295ee204"></a>

### [`00c34f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34f00.md) → [`00c35328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35328.md) FUN_00c35328

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md) [`00c5e950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e950.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5ed50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34f00.md#insn-00c34f18)
- 新版 [`00c35340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35328.md#insn-00c35340)

~~~diff
- 00c34f18 ["INT_ADD", "register:40f0:8", ["const:c34f18:8", "const:4:8"]]
- 00c34f18 ["CALL", null, ["callee:00c5ed50:8"]]
+ 00c35340 ["INT_ADD", "register:40f0:8", ["const:c35340:8", "const:4:8"]]
+ 00c35340 ["CALL", null, ["callee:00c5ed50:8"]]
- 00c34f18 bytes 8ea60094
+ 00c35340 bytes 84a60094
~~~


<a id="compare-90b31989c3a8952625fb5dbf21e92a30"></a>

### [`00c34f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34f30.md) → [`00c35358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35358.md) FUN_00c35358

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md) [`00c5e950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e950.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5ed50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34f30.md#insn-00c34f48) · [`00c34f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34f30.md#insn-00c34f50)
- 新版 [`00c35370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35358.md#insn-00c35370) · [`00c35378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35358.md#insn-00c35378)

~~~diff
- 00c34f48 ["INT_ADD", "register:40f0:8", ["const:c34f48:8", "const:4:8"]]
- 00c34f48 ["CALL", null, ["callee:00c5ed50:8"]]
+ 00c35370 ["INT_ADD", "register:40f0:8", ["const:c35370:8", "const:4:8"]]
+ 00c35370 ["CALL", null, ["callee:00c5ed50:8"]]
- 00c34f48 bytes 82a60094
+ 00c35370 bytes 78a60094
- 00c34f50 ["INT_ADD", "register:40f0:8", ["const:c34f50:8", "const:4:8"]]
- 00c34f50 ["CALL", null, ["callee:00c58300:8"]]
+ 00c35378 ["INT_ADD", "register:40f0:8", ["const:c35378:8", "const:4:8"]]
+ 00c35378 ["CALL", null, ["callee:00c58300:8"]]
- 00c34f50 bytes ec8b0094
+ 00c35378 bytes e28b0094
~~~


<a id="compare-1ad1800c028ea8dfb049bb2a67be6921"></a>

### [`00c34f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34f68.md) → [`00c35390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35390.md) FUN_00c35390

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34f68.md#insn-00c34f7c)
- 新版 [`00c353a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35390.md#insn-00c353a4)

~~~diff
- 00c34f7c ["INT_ADD", "register:40f0:8", ["const:c34f7c:8", "const:4:8"]]
- 00c34f7c ["CALL", null, ["callee:00c58300:8"]]
+ 00c353a4 ["INT_ADD", "register:40f0:8", ["const:c353a4:8", "const:4:8"]]
+ 00c353a4 ["CALL", null, ["callee:00c58300:8"]]
- 00c34f7c bytes e18b0094
+ 00c353a4 bytes d78b0094
~~~


<a id="compare-660002a9a1cd5f9f66881c22b25840c6"></a>

### [`00c34f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34f94.md) → [`00c353bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c353bc.md) FUN_00c353bc

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34f94.md#insn-00c34fa8)
- 新版 [`00c353d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c353bc.md#insn-00c353d0)

~~~diff
- 00c34fa8 ["INT_ADD", "register:40f0:8", ["const:c34fa8:8", "const:4:8"]]
- 00c34fa8 ["CALL", null, ["callee:00c58300:8"]]
+ 00c353d0 ["INT_ADD", "register:40f0:8", ["const:c353d0:8", "const:4:8"]]
+ 00c353d0 ["CALL", null, ["callee:00c58300:8"]]
- 00c34fa8 bytes d68b0094
+ 00c353d0 bytes cc8b0094
~~~


<a id="compare-c0ec20eee4cad12954765a26965eb561"></a>

### [`00c34fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34fc0.md) → [`00c353e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c353e8.md) FUN_00c353e8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34fc0.md#insn-00c34fd4)
- 新版 [`00c353fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c353e8.md#insn-00c353fc)

~~~diff
- 00c34fd4 ["INT_ADD", "register:40f0:8", ["const:c34fd4:8", "const:4:8"]]
- 00c34fd4 ["CALL", null, ["callee:00c58300:8"]]
+ 00c353fc ["INT_ADD", "register:40f0:8", ["const:c353fc:8", "const:4:8"]]
+ 00c353fc ["CALL", null, ["callee:00c58300:8"]]
- 00c34fd4 bytes cb8b0094
+ 00c353fc bytes c18b0094
~~~


<a id="compare-2a726d33402d86cede6a01b2cd8ff615"></a>

### [`00c34fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34fec.md) → [`00c35414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35414.md) FUN_00c35414

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34fec.md#insn-00c35000)
- 新版 [`00c35428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35414.md#insn-00c35428)

~~~diff
- 00c35000 ["INT_ADD", "register:40f0:8", ["const:c35000:8", "const:4:8"]]
- 00c35000 ["CALL", null, ["callee:00c58300:8"]]
+ 00c35428 ["INT_ADD", "register:40f0:8", ["const:c35428:8", "const:4:8"]]
+ 00c35428 ["CALL", null, ["callee:00c58300:8"]]
- 00c35000 bytes c08b0094
+ 00c35428 bytes b68b0094
~~~


<a id="compare-6494a24bcbb8969a904aac91c7d97727"></a>

### [`00c350ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c350ac.md) → [`00c354d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c354d4.md) FUN_00c354d4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c35018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35018.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c35440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35440.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c350c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c350ac.md#insn-00c350c0)
- 新版 [`00c354e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c354d4.md#insn-00c354e8)

~~~diff
- 00c350c0 ["INT_ADD", "register:40f0:8", ["const:c350c0:8", "const:4:8"]]
- 00c350c0 ["CALL", null, ["callee:00c35440:8"]]
+ 00c354e8 ["INT_ADD", "register:40f0:8", ["const:c354e8:8", "const:4:8"]]
+ 00c354e8 ["CALL", null, ["callee:00c35440:8"]]
- 00c350c0 bytes d6ffff97
+ 00c354e8 bytes d6ffff97
~~~


<a id="compare-391ad7c6c1b23cb78394527fd5eaf409"></a>

### [`00c3516c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3516c.md) → [`00c35594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35594.md) FUN_00c35594

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c350d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c350d8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c35500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35500.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3516c.md#insn-00c35180)
- 新版 [`00c355a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35594.md#insn-00c355a8)

~~~diff
- 00c35180 ["INT_ADD", "register:40f0:8", ["const:c35180:8", "const:4:8"]]
- 00c35180 ["CALL", null, ["callee:00c35500:8"]]
+ 00c355a8 ["INT_ADD", "register:40f0:8", ["const:c355a8:8", "const:4:8"]]
+ 00c355a8 ["CALL", null, ["callee:00c35500:8"]]
- 00c35180 bytes d6ffff97
+ 00c355a8 bytes d6ffff97
~~~


<a id="compare-46fea38d341a8fd40753438f1b6b1925"></a>

### [`00c3522c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3522c.md) → [`00c35654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35654.md) FUN_00c35654

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c35198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35198.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c355c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c355c0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3522c.md#insn-00c35240)
- 新版 [`00c35668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35654.md#insn-00c35668)

~~~diff
- 00c35240 ["INT_ADD", "register:40f0:8", ["const:c35240:8", "const:4:8"]]
- 00c35240 ["CALL", null, ["callee:00c355c0:8"]]
+ 00c35668 ["INT_ADD", "register:40f0:8", ["const:c35668:8", "const:4:8"]]
+ 00c35668 ["CALL", null, ["callee:00c355c0:8"]]
- 00c35240 bytes d6ffff97
+ 00c35668 bytes d6ffff97
~~~


<a id="compare-83baa2a5f6a892393fec269b7d4ac3fc"></a>

### [`00c352ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c352ec.md) → [`00c35714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35714.md) FUN_00c35714

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c35258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35258.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c35680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35680.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c352ec.md#insn-00c35300)
- 新版 [`00c35728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35714.md#insn-00c35728)

~~~diff
- 00c35300 ["INT_ADD", "register:40f0:8", ["const:c35300:8", "const:4:8"]]
- 00c35300 ["CALL", null, ["callee:00c35680:8"]]
+ 00c35728 ["INT_ADD", "register:40f0:8", ["const:c35728:8", "const:4:8"]]
+ 00c35728 ["CALL", null, ["callee:00c35680:8"]]
- 00c35300 bytes d6ffff97
+ 00c35728 bytes d6ffff97
~~~


<a id="compare-35e5ad7a82eae278258666de14038a22"></a>

### [`00c35318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35318.md) → [`00c35740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35740.md) FUN_00c35740

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3532c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35318.md#insn-00c3532c)
- 新版 [`00c35754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35740.md#insn-00c35754)

~~~diff
- 00c3532c ["INT_ADD", "register:40f0:8", ["const:c3532c:8", "const:4:8"]]
- 00c3532c ["CALL", null, ["callee:00c58300:8"]]
+ 00c35754 ["INT_ADD", "register:40f0:8", ["const:c35754:8", "const:4:8"]]
+ 00c35754 ["CALL", null, ["callee:00c58300:8"]]
- 00c3532c bytes f58a0094
+ 00c35754 bytes eb8a0094
~~~


<a id="compare-35761c5c23d6889693db31b59d6f18ea"></a>

### [`00c35344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35344.md) → [`00c3576c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c3576c.md) FUN_00c3576c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35344.md#insn-00c35358)
- 新版 [`00c35780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c3576c.md#insn-00c35780)

~~~diff
- 00c35358 ["INT_ADD", "register:40f0:8", ["const:c35358:8", "const:4:8"]]
- 00c35358 ["CALL", null, ["callee:00c58300:8"]]
+ 00c35780 ["INT_ADD", "register:40f0:8", ["const:c35780:8", "const:4:8"]]
+ 00c35780 ["CALL", null, ["callee:00c58300:8"]]
- 00c35358 bytes ea8a0094
+ 00c35780 bytes e08a0094
~~~


<a id="compare-2c8491b1ffc3fc2bf9a4194cb28b209a"></a>

### [`00c35370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35370.md) → [`00c35798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35798.md) FUN_00c35798

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35370.md#insn-00c35384)
- 新版 [`00c357ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35798.md#insn-00c357ac)

~~~diff
- 00c35384 ["INT_ADD", "register:40f0:8", ["const:c35384:8", "const:4:8"]]
- 00c35384 ["CALL", null, ["callee:00c58300:8"]]
+ 00c357ac ["INT_ADD", "register:40f0:8", ["const:c357ac:8", "const:4:8"]]
+ 00c357ac ["CALL", null, ["callee:00c58300:8"]]
- 00c35384 bytes df8a0094
+ 00c357ac bytes d58a0094
~~~


<a id="compare-0614320e8051abe9f5ce68dff26f2a1b"></a>

### [`00c3539c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3539c.md) → [`00c357c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c357c4.md) FUN_00c357c4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c353b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3539c.md#insn-00c353b0)
- 新版 [`00c357d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c357c4.md#insn-00c357d8)

~~~diff
- 00c353b0 ["INT_ADD", "register:40f0:8", ["const:c353b0:8", "const:4:8"]]
- 00c353b0 ["CALL", null, ["callee:00c58300:8"]]
+ 00c357d8 ["INT_ADD", "register:40f0:8", ["const:c357d8:8", "const:4:8"]]
+ 00c357d8 ["CALL", null, ["callee:00c58300:8"]]
- 00c353b0 bytes d48a0094
+ 00c357d8 bytes ca8a0094
~~~


<a id="compare-a86c027933e03a6eb3375a5b805cb5ab"></a>

### [`00c353c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c353c8.md) → [`00c357f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c357f0.md) FUN_00c357f0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c353dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c353c8.md#insn-00c353dc)
- 新版 [`00c35804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c357f0.md#insn-00c35804)

~~~diff
- 00c353dc ["INT_ADD", "register:40f0:8", ["const:c353dc:8", "const:4:8"]]
- 00c353dc ["CALL", null, ["callee:00c58300:8"]]
+ 00c35804 ["INT_ADD", "register:40f0:8", ["const:c35804:8", "const:4:8"]]
+ 00c35804 ["CALL", null, ["callee:00c58300:8"]]
- 00c353dc bytes c98a0094
+ 00c35804 bytes bf8a0094
~~~


<a id="compare-61f3a276ad03798f2e2e9091bcdd0123"></a>

### [`00c353f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c353f4.md) → [`00c3581c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c3581c.md) FUN_00c3581c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c353f4.md#insn-00c35408)
- 新版 [`00c35830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c3581c.md#insn-00c35830)

~~~diff
- 00c35408 ["INT_ADD", "register:40f0:8", ["const:c35408:8", "const:4:8"]]
- 00c35408 ["CALL", null, ["callee:00c58300:8"]]
+ 00c35830 ["INT_ADD", "register:40f0:8", ["const:c35830:8", "const:4:8"]]
+ 00c35830 ["CALL", null, ["callee:00c58300:8"]]
- 00c35408 bytes be8a0094
+ 00c35830 bytes b48a0094
~~~


<a id="compare-b05613fd7b38f86c7b65566982f369da"></a>

### [`00c35420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35420.md) → [`00c35848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35848.md) FUN_00c35848

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35420.md#insn-00c35434)
- 新版 [`00c3585c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35848.md#insn-00c3585c)

~~~diff
- 00c35434 ["INT_ADD", "register:40f0:8", ["const:c35434:8", "const:4:8"]]
- 00c35434 ["CALL", null, ["callee:00c58300:8"]]
+ 00c3585c ["INT_ADD", "register:40f0:8", ["const:c3585c:8", "const:4:8"]]
+ 00c3585c ["CALL", null, ["callee:00c58300:8"]]
- 00c35434 bytes b38a0094
+ 00c3585c bytes a98a0094
~~~


<a id="compare-8053f8f030ec81c95467cfbd9863bb3e"></a>

### [`00c35454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35454.md) → [`00c3587c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c3587c.md) FUN_00c3587c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35454.md#insn-00c35468)
- 新版 [`00c35890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c3587c.md#insn-00c35890)

~~~diff
- 00c35468 ["INT_ADD", "register:40f0:8", ["const:c35468:8", "const:4:8"]]
- 00c35468 ["CALL", null, ["callee:00c58300:8"]]
+ 00c35890 ["INT_ADD", "register:40f0:8", ["const:c35890:8", "const:4:8"]]
+ 00c35890 ["CALL", null, ["callee:00c58300:8"]]
- 00c35468 bytes a68a0094
+ 00c35890 bytes 9c8a0094
~~~


<a id="compare-44f7bd83641e24b7c7ebc057a992fe46"></a>

### [`00c35480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35480.md) → [`00c358a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358a8.md) FUN_00c358a8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e170.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35480.md#insn-00c35494)
- 新版 [`00c358bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358a8.md#insn-00c358bc)

~~~diff
- 00c35494 ["INT_ADD", "register:40f0:8", ["const:c35494:8", "const:4:8"]]
- 00c35494 ["CALL", null, ["callee:00c5e570:8"]]
+ 00c358bc ["INT_ADD", "register:40f0:8", ["const:c358bc:8", "const:4:8"]]
+ 00c358bc ["CALL", null, ["callee:00c5e570:8"]]
- 00c35494 bytes 37a30094
+ 00c358bc bytes 2da30094
~~~


<a id="compare-a0bfd4926bf38958387629cd20c5d753"></a>

### [`00c354c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c354c0.md) → [`00c358e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358e8.md) FUN_00c358e8

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) [`00c244ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c244ac.md) · 呼出先 4件 [`00c354a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c354a8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 4件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) [`00c248d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c248d4.md) · 呼出先 4件 [`00c358d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358d0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c354c0.md#insn-00c35510) · [`00c35540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c354c0.md#insn-00c35540) · [`00c355cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c354c0.md#insn-00c355cc)
- 新版 [`00c35938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358e8.md#insn-00c35938) · [`00c35968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358e8.md#insn-00c35968) · [`00c359f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358e8.md#insn-00c359f4)

~~~diff
- 00c35510 ["INT_ADD", "register:40f0:8", ["const:c35510:8", "const:4:8"]]
- 00c35510 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00c35938 ["INT_ADD", "register:40f0:8", ["const:c35938:8", "const:4:8"]]
+ 00c35938 ["CALL", null, ["callee:00c57eb0:8"]]
- 00c35510 bytes 68890094
+ 00c35938 bytes 5e890094
- 00c35540 ["INT_ADD", "register:40f0:8", ["const:c35540:8", "const:4:8"]]
- 00c35540 ["CALL", null, ["callee:00c57f40:8"]]
+ 00c35968 ["INT_ADD", "register:40f0:8", ["const:c35968:8", "const:4:8"]]
+ 00c35968 ["CALL", null, ["callee:00c57f40:8"]]
- 00c35540 bytes 80890094
+ 00c35968 bytes 76890094
- 00c355cc ["INT_ADD", "register:40f0:8", ["const:c355cc:8", "const:4:8"]]
- 00c355cc ["CALL", null, ["callee:00c57e90:8"]]
+ 00c359f4 ["INT_ADD", "register:40f0:8", ["const:c359f4:8", "const:4:8"]]
+ 00c359f4 ["CALL", null, ["callee:00c57e90:8"]]
- 00c355cc bytes 31890094
+ 00c359f4 bytes 27890094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df565d84043affb49f55af16d1be11a9"></a>

### [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) → [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) FUN_00c35a44

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 54件 [`00c1d274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d274.md) [`00c1f7a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f7a8.md) [`00c1f8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f8d4.md) [`00c1fa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fa00.md) [`00c1fb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fb2c.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c354a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c354a8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 54件 [`00c1d69c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d69c.md) [`00c1fbd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fbd0.md) [`00c1fcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fcfc.md) [`00c1fe28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fe28.md) [`00c1ff54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1ff54.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c358d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358d0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c356bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md#insn-00c356bc) · [`00c356e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md#insn-00c356e4) · [`00c35704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md#insn-00c35704)
- 新版 [`00c35ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md#insn-00c35ae4) · [`00c35b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md#insn-00c35b0c) · [`00c35b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md#insn-00c35b2c)

~~~diff
- 00c356bc ["INT_ADD", "register:40f0:8", ["const:c356bc:8", "const:4:8"]]
- 00c356bc ["CALL", null, ["callee:00c58090:8"]]
+ 00c35ae4 ["INT_ADD", "register:40f0:8", ["const:c35ae4:8", "const:4:8"]]
+ 00c35ae4 ["CALL", null, ["callee:00c58090:8"]]
- 00c356bc bytes 75890094
+ 00c35ae4 bytes 6b890094
- 00c356e4 ["INT_ADD", "register:40f0:8", ["const:c356e4:8", "const:4:8"]]
- 00c356e4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00c35b0c ["INT_ADD", "register:40f0:8", ["const:c35b0c:8", "const:4:8"]]
+ 00c35b0c ["CALL", null, ["callee:00c57e90:8"]]
- 00c356e4 bytes eb880094
+ 00c35b0c bytes e1880094
- 00c35704 ["INT_ADD", "register:40f0:8", ["const:c35704:8", "const:4:8"]]
- 00c35704 ["CALL", null, ["callee:00c58090:8"]]
+ 00c35b2c ["INT_ADD", "register:40f0:8", ["const:c35b2c:8", "const:4:8"]]
+ 00c35b2c ["CALL", null, ["callee:00c58090:8"]]
- 00c35704 bytes 63890094
+ 00c35b2c bytes 59890094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-121af9514b212fdf22d00b32360b1bff"></a>

### [`00c35c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35c90.md) → [`00c360b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c360b8.md) FUN_00c360b8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c32a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c32/00c32a44.md) · 呼出先 2件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00bf17e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf17e4.md)
- 新版 呼出元 1件 [`00c32e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c32e6c.md) · 呼出先 2件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00bf1c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1c0c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35c90.md#insn-00c35ccc) · [`00c35ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35c90.md#insn-00c35ce4)
- 新版 [`00c360f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c360b8.md#insn-00c360f4) · [`00c3610c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c360b8.md#insn-00c3610c)

~~~diff
- 00c35ccc ["INT_ADD", "register:40f0:8", ["const:c35ccc:8", "const:4:8"]]
- 00c35ccc ["CALL", null, ["callee:00bf1c0c:8"]]
+ 00c360f4 ["INT_ADD", "register:40f0:8", ["const:c360f4:8", "const:4:8"]]
+ 00c360f4 ["CALL", null, ["callee:00bf1c0c:8"]]
- 00c35ccc bytes c6eefe97
+ 00c360f4 bytes c6eefe97
- 00c35ce4 ["INT_ADD", "register:40f0:8", ["const:c35ce4:8", "const:4:8"]]
- 00c35ce4 ["CALL", null, ["callee:0044291c:8"]]
+ 00c3610c ["INT_ADD", "register:40f0:8", ["const:c3610c:8", "const:4:8"]]
+ 00c3610c ["CALL", null, ["callee:0044291c:8"]]
- 00c35ce4 bytes fe32e097
+ 00c3610c bytes 0432e097
~~~


<a id="compare-6d1f89326f8276fa55d6f50844d811ef"></a>

### [`00c35ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35ce8.md) → [`00c36110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36110.md) FUN_00c36110

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c33b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c33/00c33b0c.md) · 呼出先 2件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00bf3bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3bf8.md)
- 新版 呼出元 1件 [`00c33f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c33/00c33f34.md) · 呼出先 2件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00bf4020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35ce8.md#insn-00c35d28) · [`00c35d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35ce8.md#insn-00c35d40)
- 新版 [`00c36150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36110.md#insn-00c36150) · [`00c36168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36110.md#insn-00c36168)

~~~diff
- 00c35d28 ["INT_ADD", "register:40f0:8", ["const:c35d28:8", "const:4:8"]]
- 00c35d28 ["CALL", null, ["callee:00bf4020:8"]]
+ 00c36150 ["INT_ADD", "register:40f0:8", ["const:c36150:8", "const:4:8"]]
+ 00c36150 ["CALL", null, ["callee:00bf4020:8"]]
- 00c35d28 bytes b4f7fe97
+ 00c36150 bytes b4f7fe97
- 00c35d40 ["INT_ADD", "register:40f0:8", ["const:c35d40:8", "const:4:8"]]
- 00c35d40 ["CALL", null, ["callee:00bf28d8:8"]]
+ 00c36168 ["INT_ADD", "register:40f0:8", ["const:c36168:8", "const:4:8"]]
+ 00c36168 ["CALL", null, ["callee:00bf28d8:8"]]
- 00c35d40 bytes dcf1fe97
+ 00c36168 bytes dcf1fe97
~~~


<a id="compare-81d3344a31af19a48d831ac51dabc416"></a>

### [`00c36824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36824.md) → [`00c36c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36c4c.md) FUN_00c36c4c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c34bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34bf0.md) [`00c34c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c20.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdd0.md)
- 新版 呼出元 2件 [`00c35018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35018.md) [`00c35048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35048.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3686c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36824.md#insn-00c3686c) · [`00c36890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36824.md#insn-00c36890) · [`00c3690c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36824.md#insn-00c3690c)
- 新版 [`00c36c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36c4c.md#insn-00c36c94) · [`00c36cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36c4c.md#insn-00c36cb8) · [`00c36d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36c4c.md#insn-00c36d34)

~~~diff
- 00c3686c ["INT_ADD", "register:40f0:8", ["const:c3686c:8", "const:4:8"]]
- 00c3686c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00c36c94 ["INT_ADD", "register:40f0:8", ["const:c36c94:8", "const:4:8"]]
+ 00c36c94 ["CALL", null, ["callee:00c57eb0:8"]]
- 00c3686c bytes 91840094
+ 00c36c94 bytes 87840094
- 00c36890 ["INT_ADD", "register:40f0:8", ["const:c36890:8", "const:4:8"]]
- 00c36890 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00c36cb8 ["INT_ADD", "register:40f0:8", ["const:c36cb8:8", "const:4:8"]]
+ 00c36cb8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00c36890 bytes 88840094
+ 00c36cb8 bytes 7e840094
- 00c3690c ["INT_ADD", "register:40f0:8", ["const:c3690c:8", "const:4:8"]]
- 00c3690c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00c36d34 ["INT_ADD", "register:40f0:8", ["const:c36d34:8", "const:4:8"]]
+ 00c36d34 ["CALL", null, ["callee:00c57eb0:8"]]
- 00c3690c bytes 69840094
+ 00c36d34 bytes 5f840094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da5db0c81a9174bb2d5c455fbaccd1d3"></a>

### [`00c36a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36a54.md) → [`00c36e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36e7c.md) FUN_00c36e7c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c34d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d0c.md) [`00c34d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d3c.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdd0.md)
- 新版 呼出元 2件 [`00c35134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35134.md) [`00c35164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35164.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c36a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36a54.md#insn-00c36a9c) · [`00c36ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36a54.md#insn-00c36ac0) · [`00c36b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36a54.md#insn-00c36b3c)
- 新版 [`00c36ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36e7c.md#insn-00c36ec4) · [`00c36ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36e7c.md#insn-00c36ee8) · [`00c36f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36e7c.md#insn-00c36f64)

~~~diff
- 00c36a9c ["INT_ADD", "register:40f0:8", ["const:c36a9c:8", "const:4:8"]]
- 00c36a9c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00c36ec4 ["INT_ADD", "register:40f0:8", ["const:c36ec4:8", "const:4:8"]]
+ 00c36ec4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00c36a9c bytes 05840094
+ 00c36ec4 bytes fb830094
- 00c36ac0 ["INT_ADD", "register:40f0:8", ["const:c36ac0:8", "const:4:8"]]
- 00c36ac0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00c36ee8 ["INT_ADD", "register:40f0:8", ["const:c36ee8:8", "const:4:8"]]
+ 00c36ee8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00c36ac0 bytes fc830094
+ 00c36ee8 bytes f2830094
- 00c36b3c ["INT_ADD", "register:40f0:8", ["const:c36b3c:8", "const:4:8"]]
- 00c36b3c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00c36f64 ["INT_ADD", "register:40f0:8", ["const:c36f64:8", "const:4:8"]]
+ 00c36f64 ["CALL", null, ["callee:00c57eb0:8"]]
- 00c36b3c bytes dd830094
+ 00c36f64 bytes d3830094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9f1e52f4750cebb2a43c7044edcf9af"></a>

### [`00c36e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36e68.md) → [`00c37290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37290.md) _ZNSt6__ndk111regex_errorD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c36e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36e68.md#insn-00c36e7c)
- 新版 [`00c372a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37290.md#insn-00c372a4)

~~~diff
- 00c36e7c ["INT_ADD", "register:40f0:8", ["const:c36e7c:8", "const:4:8"]]
- 00c36e7c ["CALL", null, ["callee:00c5a7c0:8"]]
+ 00c372a4 ["INT_ADD", "register:40f0:8", ["const:c372a4:8", "const:4:8"]]
+ 00c372a4 ["CALL", null, ["callee:00c5a7c0:8"]]
- 00c36e7c bytes 518d0094
+ 00c372a4 bytes 478d0094
~~~


<a id="compare-8ab3ea4ae89bc1738b15dbb95171f3e8"></a>

### [`00c37784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37784.md) → [`00c37bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37bac.md) _ZNSt9exceptionD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37784.md#insn-00c37798)
- 新版 [`00c37bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37bac.md#insn-00c37bc0)

~~~diff
- 00c37798 ["INT_ADD", "register:40f0:8", ["const:c37798:8", "const:4:8"]]
- 00c37798 ["CALL", null, ["callee:00c5ee00:8"]]
+ 00c37bc0 ["INT_ADD", "register:40f0:8", ["const:c37bc0:8", "const:4:8"]]
+ 00c37bc0 ["CALL", null, ["callee:00c5ee00:8"]]
- 00c37798 bytes 9a9c0094
+ 00c37bc0 bytes 909c0094
~~~


<a id="compare-1fd6b1a8665500b32d086b64c63c6416"></a>

### [`00c377c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c377c0.md) → [`00c37be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37be8.md) _ZNSt13bad_exceptionD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c377d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c377c0.md#insn-00c377d4)
- 新版 [`00c37bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37be8.md#insn-00c37bfc)

~~~diff
- 00c377d4 ["INT_ADD", "register:40f0:8", ["const:c377d4:8", "const:4:8"]]
- 00c377d4 ["CALL", null, ["callee:00c5ee10:8"]]
+ 00c37bfc ["INT_ADD", "register:40f0:8", ["const:c37bfc:8", "const:4:8"]]
+ 00c37bfc ["CALL", null, ["callee:00c5ee10:8"]]
- 00c377d4 bytes 8f9c0094
+ 00c37bfc bytes 859c0094
~~~


<a id="compare-3308e146d01b813b846149dfcd3ea7d2"></a>

### [`00c37814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37814.md) → [`00c37c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37c3c.md) _ZNSt9bad_allocD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58650.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37814.md#insn-00c37828)
- 新版 [`00c37c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37c3c.md#insn-00c37c50)

~~~diff
- 00c37828 ["INT_ADD", "register:40f0:8", ["const:c37828:8", "const:4:8"]]
- 00c37828 ["CALL", null, ["callee:00c58a50:8"]]
+ 00c37c50 ["INT_ADD", "register:40f0:8", ["const:c37c50:8", "const:4:8"]]
+ 00c37c50 ["CALL", null, ["callee:00c58a50:8"]]
- 00c37828 bytes 8a830094
+ 00c37c50 bytes 80830094
~~~


<a id="compare-a72e0f27babd188a57f55672a702d70d"></a>

### [`00c37868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37868.md) → [`00c37c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37c90.md) _ZNSt20bad_array_new_lengthD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3787c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37868.md#insn-00c3787c)
- 新版 [`00c37ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37c90.md#insn-00c37ca4)

~~~diff
- 00c3787c ["INT_ADD", "register:40f0:8", ["const:c3787c:8", "const:4:8"]]
- 00c3787c ["CALL", null, ["callee:00c58040:8"]]
+ 00c37ca4 ["INT_ADD", "register:40f0:8", ["const:c37ca4:8", "const:4:8"]]
+ 00c37ca4 ["CALL", null, ["callee:00c58040:8"]]
- 00c3787c bytes f1800094
+ 00c37ca4 bytes e7800094
~~~


<a id="compare-8ddb657ed0cd1a9c6895bc0cb8a8907e"></a>

### [`00c378fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c378fc.md) → [`00c37d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37d24.md) _ZNSt11logic_errorD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c378fc.md#insn-00c37910)
- 新版 [`00c37d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37d24.md#insn-00c37d38)

~~~diff
- 00c37910 ["INT_ADD", "register:40f0:8", ["const:c37910:8", "const:4:8"]]
- 00c37910 ["CALL", null, ["callee:00c5ee20:8"]]
+ 00c37d38 ["INT_ADD", "register:40f0:8", ["const:c37d38:8", "const:4:8"]]
+ 00c37d38 ["CALL", null, ["callee:00c5ee20:8"]]
- 00c37910 bytes 449c0094
+ 00c37d38 bytes 3a9c0094
~~~


<a id="compare-9268c9ea726a4fc988e9af6cae05f1b0"></a>

### [`00c3798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3798c.md) → [`00c37db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37db4.md) _ZNSt13runtime_errorD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5dfd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c379a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3798c.md#insn-00c379a0)
- 新版 [`00c37dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37db4.md#insn-00c37dc8)

~~~diff
- 00c379a0 ["INT_ADD", "register:40f0:8", ["const:c379a0:8", "const:4:8"]]
- 00c379a0 ["CALL", null, ["callee:00c5dfd0:8"]]
+ 00c37dc8 ["INT_ADD", "register:40f0:8", ["const:c37dc8:8", "const:4:8"]]
+ 00c37dc8 ["CALL", null, ["callee:00c5dfd0:8"]]
- 00c379a0 bytes 8c980094
+ 00c37dc8 bytes 82980094
~~~


<a id="compare-a327828e3c73e1dc0e113a6905b0aa3d"></a>

### [`00c379c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c379c4.md) → [`00c37dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37dec.md) _ZNSt12domain_errorD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c379d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c379c4.md#insn-00c379d8)
- 新版 [`00c37e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37dec.md#insn-00c37e00)

~~~diff
- 00c379d8 ["INT_ADD", "register:40f0:8", ["const:c379d8:8", "const:4:8"]]
- 00c379d8 ["CALL", null, ["callee:00c5ee30:8"]]
+ 00c37e00 ["INT_ADD", "register:40f0:8", ["const:c37e00:8", "const:4:8"]]
+ 00c37e00 ["CALL", null, ["callee:00c5ee30:8"]]
- 00c379d8 bytes 169c0094
+ 00c37e00 bytes 0c9c0094
~~~


<a id="compare-c06d4a3bab648fe60e96b8b807fc370c"></a>

### [`00c379f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c379f0.md) → [`00c37e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37e18.md) _ZNSt16invalid_argumentD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dd30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c379f0.md#insn-00c37a04)
- 新版 [`00c37e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37e18.md#insn-00c37e2c)

~~~diff
- 00c37a04 ["INT_ADD", "register:40f0:8", ["const:c37a04:8", "const:4:8"]]
- 00c37a04 ["CALL", null, ["callee:00c5e130:8"]]
+ 00c37e2c ["INT_ADD", "register:40f0:8", ["const:c37e2c:8", "const:4:8"]]
+ 00c37e2c ["CALL", null, ["callee:00c5e130:8"]]
- 00c37a04 bytes cb980094
+ 00c37e2c bytes c1980094
~~~


<a id="compare-b3b91497eaf9fbfabbf1447ceee1d384"></a>

### [`00c37a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37a1c.md) → [`00c37e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37e44.md) _ZNSt12length_errorD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37a1c.md#insn-00c37a30)
- 新版 [`00c37e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37e44.md#insn-00c37e58)

~~~diff
- 00c37a30 ["INT_ADD", "register:40f0:8", ["const:c37a30:8", "const:4:8"]]
- 00c37a30 ["CALL", null, ["callee:00c57f00:8"]]
+ 00c37e58 ["INT_ADD", "register:40f0:8", ["const:c37e58:8", "const:4:8"]]
+ 00c37e58 ["CALL", null, ["callee:00c57f00:8"]]
- 00c37a30 bytes 34800094
+ 00c37e58 bytes 2a800094
~~~


<a id="compare-edb867d7c5f4a305a9ba71409a297b72"></a>

### [`00c37a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37a48.md) → [`00c37e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37e70.md) _ZNSt12out_of_rangeD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ca0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37a5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37a48.md#insn-00c37a5c)
- 新版 [`00c37e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37e70.md#insn-00c37e84)

~~~diff
- 00c37a5c ["INT_ADD", "register:40f0:8", ["const:c37a5c:8", "const:4:8"]]
- 00c37a5c ["CALL", null, ["callee:00c580a0:8"]]
+ 00c37e84 ["INT_ADD", "register:40f0:8", ["const:c37e84:8", "const:4:8"]]
+ 00c37e84 ["CALL", null, ["callee:00c580a0:8"]]
- 00c37a5c bytes 91800094
+ 00c37e84 bytes 87800094
~~~


<a id="compare-c4988939a7f91dea131903018cdd8082"></a>

### [`00c37a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37a74.md) → [`00c37e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37e9c.md) _ZNSt11range_errorD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37a74.md#insn-00c37a88)
- 新版 [`00c37eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37e9c.md#insn-00c37eb0)

~~~diff
- 00c37a88 ["INT_ADD", "register:40f0:8", ["const:c37a88:8", "const:4:8"]]
- 00c37a88 ["CALL", null, ["callee:00c5a8c0:8"]]
+ 00c37eb0 ["INT_ADD", "register:40f0:8", ["const:c37eb0:8", "const:4:8"]]
+ 00c37eb0 ["CALL", null, ["callee:00c5a8c0:8"]]
- 00c37a88 bytes 8e8a0094
+ 00c37eb0 bytes 848a0094
~~~


<a id="compare-8e95f9506a148029bc84d7d5cbf678d1"></a>

### [`00c37aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37aa0.md) → [`00c37ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ec8.md) _ZNSt14overflow_errorD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5db70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5df70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37aa0.md#insn-00c37ab4)
- 新版 [`00c37edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ec8.md#insn-00c37edc)

~~~diff
- 00c37ab4 ["INT_ADD", "register:40f0:8", ["const:c37ab4:8", "const:4:8"]]
- 00c37ab4 ["CALL", null, ["callee:00c5df70:8"]]
+ 00c37edc ["INT_ADD", "register:40f0:8", ["const:c37edc:8", "const:4:8"]]
+ 00c37edc ["CALL", null, ["callee:00c5df70:8"]]
- 00c37ab4 bytes 2f980094
+ 00c37edc bytes 25980094
~~~


<a id="compare-291baadc671405b59e9375ada02c4f86"></a>

### [`00c37acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37acc.md) → [`00c37ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ef4.md) _ZNSt15underflow_errorD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37acc.md#insn-00c37ae0)
- 新版 [`00c37f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ef4.md#insn-00c37f08)

~~~diff
- 00c37ae0 ["INT_ADD", "register:40f0:8", ["const:c37ae0:8", "const:4:8"]]
- 00c37ae0 ["CALL", null, ["callee:00c5ee40:8"]]
+ 00c37f08 ["INT_ADD", "register:40f0:8", ["const:c37f08:8", "const:4:8"]]
+ 00c37f08 ["CALL", null, ["callee:00c5ee40:8"]]
- 00c37ae0 bytes d89b0094
+ 00c37f08 bytes ce9b0094
~~~


<a id="compare-ee1076f94c1d823e1f15c9c06cc1df92"></a>

### [`00c37b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37b00.md) → [`00c37f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37f28.md) _ZNSt9type_infoD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37b00.md#insn-00c37b14)
- 新版 [`00c37f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37f28.md#insn-00c37f3c)

~~~diff
- 00c37b14 ["INT_ADD", "register:40f0:8", ["const:c37b14:8", "const:4:8"]]
- 00c37b14 ["CALL", null, ["callee:00c5ee60:8"]]
+ 00c37f3c ["INT_ADD", "register:40f0:8", ["const:c37f3c:8", "const:4:8"]]
+ 00c37f3c ["CALL", null, ["callee:00c5ee60:8"]]
- 00c37b14 bytes d39b0094
+ 00c37f3c bytes c99b0094
~~~


<a id="compare-d7cdb834eae8669cb12fe09488af78b6"></a>

### [`00c37b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37b4c.md) → [`00c37f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37f74.md) _ZNSt8bad_castD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e490.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37b4c.md#insn-00c37b60)
- 新版 [`00c37f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37f74.md#insn-00c37f88)

~~~diff
- 00c37b60 ["INT_ADD", "register:40f0:8", ["const:c37b60:8", "const:4:8"]]
- 00c37b60 ["CALL", null, ["callee:00c5e490:8"]]
+ 00c37f88 ["INT_ADD", "register:40f0:8", ["const:c37f88:8", "const:4:8"]]
+ 00c37f88 ["CALL", null, ["callee:00c5e490:8"]]
- 00c37b60 bytes 4c990094
+ 00c37f88 bytes 42990094
~~~


<a id="compare-6b099070272684c1e9c1f67c6a8314ad"></a>

### [`00c37ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ba8.md) → [`00c37fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37fd0.md) _ZNSt10bad_typeidD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e980.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ed80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ba8.md#insn-00c37bbc)
- 新版 [`00c37fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37fd0.md#insn-00c37fe4)

~~~diff
- 00c37bbc ["INT_ADD", "register:40f0:8", ["const:c37bbc:8", "const:4:8"]]
- 00c37bbc ["CALL", null, ["callee:00c5ed80:8"]]
+ 00c37fe4 ["INT_ADD", "register:40f0:8", ["const:c37fe4:8", "const:4:8"]]
+ 00c37fe4 ["CALL", null, ["callee:00c5ed80:8"]]
- 00c37bbc bytes 719b0094
+ 00c37fe4 bytes 679b0094
~~~


<a id="compare-ca81dfa365764ba5c6eabd7f997c8d3d"></a>

### [`00c37d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37d08.md) → [`00c38130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38130.md) FUN_00c38130

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37d08.md#insn-00c37d1c)
- 新版 [`00c38144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38130.md#insn-00c38144)

~~~diff
- 00c37d1c ["INT_ADD", "register:40f0:8", ["const:c37d1c:8", "const:4:8"]]
- 00c37d1c ["CALL", null, ["callee:00c5ee50:8"]]
+ 00c38144 ["INT_ADD", "register:40f0:8", ["const:c38144:8", "const:4:8"]]
+ 00c38144 ["CALL", null, ["callee:00c5ee50:8"]]
- 00c37d1c bytes 4d9b0094
+ 00c38144 bytes 439b0094
~~~


<a id="compare-5d67ac0be3d3ae7ee0a0444ec3367b78"></a>

### [`00c37d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37d34.md) → [`00c3815c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3815c.md) FUN_00c3815c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37d34.md#insn-00c37d48)
- 新版 [`00c38170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3815c.md#insn-00c38170)

~~~diff
- 00c37d48 ["INT_ADD", "register:40f0:8", ["const:c37d48:8", "const:4:8"]]
- 00c37d48 ["CALL", null, ["callee:00c5ee50:8"]]
+ 00c38170 ["INT_ADD", "register:40f0:8", ["const:c38170:8", "const:4:8"]]
+ 00c38170 ["CALL", null, ["callee:00c5ee50:8"]]
- 00c37d48 bytes 429b0094
+ 00c38170 bytes 389b0094
~~~


<a id="compare-b41499ecfb2a48dada787e7ce9dfa23b"></a>

### [`00c37d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37d60.md) → [`00c38188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38188.md) FUN_00c38188

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37d60.md#insn-00c37d74)
- 新版 [`00c3819c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38188.md#insn-00c3819c)

~~~diff
- 00c37d74 ["INT_ADD", "register:40f0:8", ["const:c37d74:8", "const:4:8"]]
- 00c37d74 ["CALL", null, ["callee:00c5ee50:8"]]
+ 00c3819c ["INT_ADD", "register:40f0:8", ["const:c3819c:8", "const:4:8"]]
+ 00c3819c ["CALL", null, ["callee:00c5ee50:8"]]
- 00c37d74 bytes 379b0094
+ 00c3819c bytes 2d9b0094
~~~


<a id="compare-0404ca531c5aed1bd25c7f7ea8a3f788"></a>

### [`00c37d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37d8c.md) → [`00c381b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c381b4.md) FUN_00c381b4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37d8c.md#insn-00c37da0)
- 新版 [`00c381c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c381b4.md#insn-00c381c8)

~~~diff
- 00c37da0 ["INT_ADD", "register:40f0:8", ["const:c37da0:8", "const:4:8"]]
- 00c37da0 ["CALL", null, ["callee:00c5ee50:8"]]
+ 00c381c8 ["INT_ADD", "register:40f0:8", ["const:c381c8:8", "const:4:8"]]
+ 00c381c8 ["CALL", null, ["callee:00c5ee50:8"]]
- 00c37da0 bytes 2c9b0094
+ 00c381c8 bytes 229b0094
~~~


<a id="compare-e1798fdc9f0d0ce3444aa985e04d43fe"></a>

### [`00c37db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37db8.md) → [`00c381e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c381e0.md) FUN_00c381e0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37db8.md#insn-00c37dcc)
- 新版 [`00c381f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c381e0.md#insn-00c381f4)

~~~diff
- 00c37dcc ["INT_ADD", "register:40f0:8", ["const:c37dcc:8", "const:4:8"]]
- 00c37dcc ["CALL", null, ["callee:00c5ee50:8"]]
+ 00c381f4 ["INT_ADD", "register:40f0:8", ["const:c381f4:8", "const:4:8"]]
+ 00c381f4 ["CALL", null, ["callee:00c5ee50:8"]]
- 00c37dcc bytes 219b0094
+ 00c381f4 bytes 179b0094
~~~


<a id="compare-d435376addea9b094b9930a70c21510c"></a>

### [`00c37de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37de4.md) → [`00c3820c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3820c.md) FUN_00c3820c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37de4.md#insn-00c37df8)
- 新版 [`00c38220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3820c.md#insn-00c38220)

~~~diff
- 00c37df8 ["INT_ADD", "register:40f0:8", ["const:c37df8:8", "const:4:8"]]
- 00c37df8 ["CALL", null, ["callee:00c5ee50:8"]]
+ 00c38220 ["INT_ADD", "register:40f0:8", ["const:c38220:8", "const:4:8"]]
+ 00c38220 ["CALL", null, ["callee:00c5ee50:8"]]
- 00c37df8 bytes 169b0094
+ 00c38220 bytes 0c9b0094
~~~


<a id="compare-8e5d89fb78e0adee9de6a0219843c6d7"></a>

### [`00c37e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37e10.md) → [`00c38238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38238.md) FUN_00c38238

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37e10.md#insn-00c37e24)
- 新版 [`00c3824c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38238.md#insn-00c3824c)

~~~diff
- 00c37e24 ["INT_ADD", "register:40f0:8", ["const:c37e24:8", "const:4:8"]]
- 00c37e24 ["CALL", null, ["callee:00c5ee50:8"]]
+ 00c3824c ["INT_ADD", "register:40f0:8", ["const:c3824c:8", "const:4:8"]]
+ 00c3824c ["CALL", null, ["callee:00c5ee50:8"]]
- 00c37e24 bytes 0b9b0094
+ 00c3824c bytes 019b0094
~~~


<a id="compare-391192ccb61aba15c843ca5363e3fd4c"></a>

### [`00c37e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37e3c.md) → [`00c38264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38264.md) FUN_00c38264

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37e3c.md#insn-00c37e50)
- 新版 [`00c38278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38264.md#insn-00c38278)

~~~diff
- 00c37e50 ["INT_ADD", "register:40f0:8", ["const:c37e50:8", "const:4:8"]]
- 00c37e50 ["CALL", null, ["callee:00c5ee50:8"]]
+ 00c38278 ["INT_ADD", "register:40f0:8", ["const:c38278:8", "const:4:8"]]
+ 00c38278 ["CALL", null, ["callee:00c5ee50:8"]]
- 00c37e50 bytes 009b0094
+ 00c38278 bytes f69a0094
~~~


<a id="compare-67b47aa69942bda46a28571c78d2cb60"></a>

### [`00c37e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37e68.md) → [`00c38290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38290.md) FUN_00c38290

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37e68.md#insn-00c37e7c)
- 新版 [`00c382a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38290.md#insn-00c382a4)

~~~diff
- 00c37e7c ["INT_ADD", "register:40f0:8", ["const:c37e7c:8", "const:4:8"]]
- 00c37e7c ["CALL", null, ["callee:00c5ee50:8"]]
+ 00c382a4 ["INT_ADD", "register:40f0:8", ["const:c382a4:8", "const:4:8"]]
+ 00c382a4 ["CALL", null, ["callee:00c5ee50:8"]]
- 00c37e7c bytes f59a0094
+ 00c382a4 bytes eb9a0094
~~~


<a id="compare-9f334b6c1f5e0f8e225402dd4ee43bbe"></a>

### [`00c37e94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37e94.md) → [`00c382bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c382bc.md) FUN_00c382bc

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37e94.md#insn-00c37ea8)
- 新版 [`00c382d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c382bc.md#insn-00c382d0)

~~~diff
- 00c37ea8 ["INT_ADD", "register:40f0:8", ["const:c37ea8:8", "const:4:8"]]
- 00c37ea8 ["CALL", null, ["callee:00c5ee50:8"]]
+ 00c382d0 ["INT_ADD", "register:40f0:8", ["const:c382d0:8", "const:4:8"]]
+ 00c382d0 ["CALL", null, ["callee:00c5ee50:8"]]
- 00c37ea8 bytes ea9a0094
+ 00c382d0 bytes e09a0094
~~~


<a id="compare-7e70a624ef30ddb77e395ed7dee268f2"></a>

### [`00c37ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ff4.md) → [`00c3841c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3841c.md) __dynamic_cast

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c38098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ff4.md#insn-00c38098) · [`00c380f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ff4.md#insn-00c380f8) · [`00c381d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ff4.md#insn-00c381d0)
- 新版 [`00c384c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3841c.md#insn-00c384c0) · [`00c38520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3841c.md#insn-00c38520) · [`00c385f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3841c.md#insn-00c385f8)

~~~diff
- 00c38098 ["COPY", "register:0:8", ["register:4048:8"]]
- 00c38098 ["INT_ADD", "register:40f0:8", ["const:c38098:8", "const:4:8"]]
- 00c38098 ["CALLIND", null, ["register:0:8"]]
+ 00c384c0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c384c0 ["INT_ADD", "register:40f0:8", ["const:c384c0:8", "const:4:8"]]
+ 00c384c0 ["CALLIND", null, ["register:0:8"]]
- 00c38098 bytes 20013fd6
+ 00c384c0 bytes 20013fd6
- 00c380f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c380f8 ["INT_ADD", "register:40f0:8", ["const:c380f8:8", "const:4:8"]]
- 00c380f8 ["CALLIND", null, ["register:0:8"]]
+ 00c38520 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c38520 ["INT_ADD", "register:40f0:8", ["const:c38520:8", "const:4:8"]]
+ 00c38520 ["CALLIND", null, ["register:0:8"]]
- 00c380f8 bytes 00013fd6
+ 00c38520 bytes 00013fd6
- 00c381d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c381d0 ["INT_ADD", "register:40f0:8", ["const:c381d0:8", "const:4:8"]]
- 00c381d0 ["CALLIND", null, ["register:0:8"]]
+ 00c385f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c385f8 ["INT_ADD", "register:40f0:8", ["const:c385f8:8", "const:4:8"]]
+ 00c385f8 ["CALLIND", null, ["register:0:8"]]
- 00c381d0 bytes 00013fd6
+ 00c385f8 bytes 00013fd6
~~~


<a id="compare-a9468354283572b9e67a317c85e2ecff"></a>

### [`00c3831c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c3831c.md) → [`00c38744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38744.md) FUN_00c38744

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c38424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c3831c.md#insn-00c38424) · [`00c384a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c3831c.md#insn-00c384a8)
- 新版 [`00c3884c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38744.md#insn-00c3884c) · [`00c388d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38744.md#insn-00c388d0)

~~~diff
- 00c38424 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c38424 ["INT_ADD", "register:40f0:8", ["const:c38424:8", "const:4:8"]]
- 00c38424 ["CALLIND", null, ["register:0:8"]]
+ 00c3884c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3884c ["INT_ADD", "register:40f0:8", ["const:c3884c:8", "const:4:8"]]
+ 00c3884c ["CALLIND", null, ["register:0:8"]]
- 00c38424 bytes 00013fd6
+ 00c3884c bytes 00013fd6
- 00c384a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c384a8 ["INT_ADD", "register:40f0:8", ["const:c384a8:8", "const:4:8"]]
- 00c384a8 ["CALLIND", null, ["register:0:8"]]
+ 00c388d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c388d0 ["INT_ADD", "register:40f0:8", ["const:c388d0:8", "const:4:8"]]
+ 00c388d0 ["CALLIND", null, ["register:0:8"]]
- 00c384a8 bytes 00013fd6
+ 00c388d0 bytes 00013fd6
~~~


<a id="compare-af8fa8a806b51786ce9f98f92887b65e"></a>

### [`00c38b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38b54.md) → [`00c38f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38f7c.md) FUN_00c38f7c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c38ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38b54.md#insn-00c38ba4) · [`00c38bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38b54.md#insn-00c38bc0) · [`00c38c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38b54.md#insn-00c38c70)
- 新版 [`00c38fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38f7c.md#insn-00c38fcc) · [`00c38fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38f7c.md#insn-00c38fe8) · [`00c39098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38f7c.md#insn-00c39098)

~~~diff
- 00c38ba4 ["INT_ADD", "register:40f0:8", ["const:c38ba4:8", "const:4:8"]]
- 00c38ba4 ["CALL", null, ["callee:00c5b850:8"]]
+ 00c38fcc ["INT_ADD", "register:40f0:8", ["const:c38fcc:8", "const:4:8"]]
+ 00c38fcc ["CALL", null, ["callee:00c5b850:8"]]
- 00c38ba4 bytes 2b8a0094
+ 00c38fcc bytes 218a0094
- 00c38bc0 ["INT_ADD", "register:40f0:8", ["const:c38bc0:8", "const:4:8"]]
- 00c38bc0 ["CALL", null, ["callee:00c5b850:8"]]
+ 00c38fe8 ["INT_ADD", "register:40f0:8", ["const:c38fe8:8", "const:4:8"]]
+ 00c38fe8 ["CALL", null, ["callee:00c5b850:8"]]
- 00c38bc0 bytes 248a0094
+ 00c38fe8 bytes 1a8a0094
- 00c38c70 ["COPY", "register:0:8", ["register:4050:8"]]
- 00c38c70 ["INT_ADD", "register:40f0:8", ["const:c38c70:8", "const:4:8"]]
- 00c38c70 ["CALLIND", null, ["register:0:8"]]
+ 00c39098 ["COPY", "register:0:8", ["register:4050:8"]]
+ 00c39098 ["INT_ADD", "register:40f0:8", ["const:c39098:8", "const:4:8"]]
+ 00c39098 ["CALLIND", null, ["register:0:8"]]
- 00c38c70 bytes 40013fd6
+ 00c39098 bytes 40013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04edf93db17016468688b687a8a66e47"></a>

### [`00c38f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38f04.md) → [`00c3932c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c3932c.md) FUN_00c3932c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c38f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38f04.md#insn-00c38f4c) · [`00c38f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38f04.md#insn-00c38f6c) · [`00c38fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38f04.md#insn-00c38fc4)
- 新版 [`00c39374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c3932c.md#insn-00c39374) · [`00c39394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c3932c.md#insn-00c39394) · [`00c393ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c3932c.md#insn-00c393ec)

~~~diff
- 00c38f4c ["INT_ADD", "register:40f0:8", ["const:c38f4c:8", "const:4:8"]]
- 00c38f4c ["CALL", null, ["callee:00c5b850:8"]]
+ 00c39374 ["INT_ADD", "register:40f0:8", ["const:c39374:8", "const:4:8"]]
+ 00c39374 ["CALL", null, ["callee:00c5b850:8"]]
- 00c38f4c bytes 41890094
+ 00c39374 bytes 37890094
- 00c38f6c ["INT_ADD", "register:40f0:8", ["const:c38f6c:8", "const:4:8"]]
- 00c38f6c ["CALL", null, ["callee:00c5b850:8"]]
+ 00c39394 ["INT_ADD", "register:40f0:8", ["const:c39394:8", "const:4:8"]]
+ 00c39394 ["CALL", null, ["callee:00c5b850:8"]]
- 00c38f6c bytes 39890094
+ 00c39394 bytes 2f890094
- 00c38fc4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c38fc4 ["INT_ADD", "register:40f0:8", ["const:c38fc4:8", "const:4:8"]]
- 00c38fc4 ["CALLIND", null, ["register:0:8"]]
+ 00c393ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c393ec ["INT_ADD", "register:40f0:8", ["const:c393ec:8", "const:4:8"]]
+ 00c393ec ["CALLIND", null, ["register:0:8"]]
- 00c38fc4 bytes 00013fd6
+ 00c393ec bytes 00013fd6
~~~


<a id="compare-16158241b7e0e4827b9303891c3986dd"></a>

### [`00c390b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c390b4.md) → [`00c394dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c394dc.md) FUN_00c394dc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c390f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c390b4.md#insn-00c390f8) · [`00c39114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c390b4.md#insn-00c39114)
- 新版 [`00c39520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c394dc.md#insn-00c39520) · [`00c3953c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c394dc.md#insn-00c3953c)

~~~diff
- 00c390f8 ["INT_ADD", "register:40f0:8", ["const:c390f8:8", "const:4:8"]]
- 00c390f8 ["CALL", null, ["callee:00c5b850:8"]]
+ 00c39520 ["INT_ADD", "register:40f0:8", ["const:c39520:8", "const:4:8"]]
+ 00c39520 ["CALL", null, ["callee:00c5b850:8"]]
- 00c390f8 bytes d6880094
+ 00c39520 bytes cc880094
- 00c39114 ["INT_ADD", "register:40f0:8", ["const:c39114:8", "const:4:8"]]
- 00c39114 ["CALL", null, ["callee:00c5b850:8"]]
+ 00c3953c ["INT_ADD", "register:40f0:8", ["const:c3953c:8", "const:4:8"]]
+ 00c3953c ["CALL", null, ["callee:00c5b850:8"]]
- 00c39114 bytes cf880094
+ 00c3953c bytes c5880094
~~~


<a id="compare-6709c74f7e70bfdb1d8981a530bdead1"></a>

### [`00c39410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39410.md) → [`00c39838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c39838.md) FUN_00c39838

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c39460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39410.md#insn-00c39460)
- 新版 [`00c39888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c39838.md#insn-00c39888)

~~~diff
- 00c39460 ["INT_ADD", "register:40f0:8", ["const:c39460:8", "const:4:8"]]
- 00c39460 ["CALL", null, ["callee:00c5b850:8"]]
+ 00c39888 ["INT_ADD", "register:40f0:8", ["const:c39888:8", "const:4:8"]]
+ 00c39888 ["CALL", null, ["callee:00c5b850:8"]]
- 00c39460 bytes fc870094
+ 00c39888 bytes f2870094
~~~


<a id="compare-15c2875a02c3ebfda3ec5231eb1135c9"></a>

### [`00c39554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39554.md) → [`00c3997c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c3997c.md) FUN_00c3997c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c39598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39554.md#insn-00c39598)
- 新版 [`00c399c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c3997c.md#insn-00c399c0)

~~~diff
- 00c39598 ["INT_ADD", "register:40f0:8", ["const:c39598:8", "const:4:8"]]
- 00c39598 ["CALL", null, ["callee:00c5b850:8"]]
+ 00c399c0 ["INT_ADD", "register:40f0:8", ["const:c399c0:8", "const:4:8"]]
+ 00c399c0 ["CALL", null, ["callee:00c5b850:8"]]
- 00c39598 bytes ae870094
+ 00c399c0 bytes a4870094
~~~


<a id="compare-c43adeccf25e6ef83e0002d1992a56ad"></a>

### [`00c39c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39c20.md) → [`00c3a048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a048.md) FUN_00c3a048

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c39c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39c20.md#insn-00c39c44) · [`00c39c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39c20.md#insn-00c39c80) · [`00c39c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39c20.md#insn-00c39c94)
- 新版 [`00c3a06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a048.md#insn-00c3a06c) · [`00c3a0a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a048.md#insn-00c3a0a8) · [`00c3a0bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a048.md#insn-00c3a0bc)

~~~diff
- 00c39c44 ["INT_ADD", "register:40f0:8", ["const:c39c44:8", "const:4:8"]]
- 00c39c44 ["CALL", null, ["callee:00c58660:8"]]
+ 00c3a06c ["INT_ADD", "register:40f0:8", ["const:c3a06c:8", "const:4:8"]]
+ 00c3a06c ["CALL", null, ["callee:00c58660:8"]]
- 00c39c44 bytes 87790094
+ 00c3a06c bytes 7d790094
- 00c39c80 ["INT_ADD", "register:40f0:8", ["const:c39c80:8", "const:4:8"]]
- 00c39c80 ["CALL", null, ["callee:00c58660:8"]]
+ 00c3a0a8 ["INT_ADD", "register:40f0:8", ["const:c3a0a8:8", "const:4:8"]]
+ 00c3a0a8 ["CALL", null, ["callee:00c58660:8"]]
- 00c39c80 bytes 78790094
+ 00c3a0a8 bytes 6e790094
- 00c39c94 ["INT_ADD", "register:40f0:8", ["const:c39c94:8", "const:4:8"]]
- 00c39c94 ["CALL", null, ["callee:00c58660:8"]]
+ 00c3a0bc ["INT_ADD", "register:40f0:8", ["const:c3a0bc:8", "const:4:8"]]
+ 00c3a0bc ["CALL", null, ["callee:00c58660:8"]]
- 00c39c94 bytes 73790094
+ 00c3a0bc bytes 69790094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f04cfe760c333f6bf8b1ca88a046750f"></a>

### [`00c39cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39cf0.md) → [`00c3a118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a118.md) FUN_00c3a118

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c41328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41328.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 2件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c41750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c39d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39cf0.md#insn-00c39d20)
- 新版 [`00c3a148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a118.md#insn-00c3a148)

~~~diff
- 00c39d20 ["INT_ADD", "register:40f0:8", ["const:c39d20:8", "const:4:8"]]
- 00c39d20 ["CALL", null, ["callee:00c58050:8"]]
+ 00c3a148 ["INT_ADD", "register:40f0:8", ["const:c3a148:8", "const:4:8"]]
+ 00c3a148 ["CALL", null, ["callee:00c58050:8"]]
- 00c39d20 bytes cc770094
+ 00c3a148 bytes c2770094
~~~


<a id="compare-2e449f688e17d5485037dbe705863714"></a>

### [`00c3bc3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bc3c.md) → [`00c3c064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c064.md) FUN_00c3c064

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) · 呼出先 2件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)
- 新版 呼出元 2件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3bcd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bc3c.md#insn-00c3bcd8) · [`00c3bd54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bc3c.md#insn-00c3bd54) · [`00c3bd74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bc3c.md#insn-00c3bd74)
- 新版 [`00c3c100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c064.md#insn-00c3c100) · [`00c3c17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c064.md#insn-00c3c17c) · [`00c3c19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c064.md#insn-00c3c19c)

~~~diff
- 00c3bcd8 ["INT_ADD", "register:40f0:8", ["const:c3bcd8:8", "const:4:8"]]
- 00c3bcd8 ["CALL", null, ["callee:00c57f40:8"]]
+ 00c3c100 ["INT_ADD", "register:40f0:8", ["const:c3c100:8", "const:4:8"]]
+ 00c3c100 ["CALL", null, ["callee:00c57f40:8"]]
- 00c3bcd8 bytes 9a6f0094
+ 00c3c100 bytes 906f0094
- 00c3bd54 ["INT_ADD", "register:40f0:8", ["const:c3bd54:8", "const:4:8"]]
- 00c3bd54 ["CALL", null, ["callee:00c58660:8"]]
+ 00c3c17c ["INT_ADD", "register:40f0:8", ["const:c3c17c:8", "const:4:8"]]
+ 00c3c17c ["CALL", null, ["callee:00c58660:8"]]
- 00c3bd54 bytes 43710094
+ 00c3c17c bytes 39710094
- 00c3bd74 ["INT_ADD", "register:40f0:8", ["const:c3bd74:8", "const:4:8"]]
- 00c3bd74 ["CALL", null, ["callee:00c57f40:8"]]
+ 00c3c19c ["INT_ADD", "register:40f0:8", ["const:c3c19c:8", "const:4:8"]]
+ 00c3c19c ["CALL", null, ["callee:00c57f40:8"]]
- 00c3bd74 bytes 736f0094
+ 00c3c19c bytes 696f0094
~~~


<a id="compare-5640bdbda066a07ed507e35fc5300e3a"></a>

### [`00c3c840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c840.md) → [`00c3cc68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cc68.md) FUN_00c3cc68

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 4件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 2件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 4件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3c888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c840.md#insn-00c3c888) · [`00c3c89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c840.md#insn-00c3c89c) · [`00c3c8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c840.md#insn-00c3c8a4)
- 新版 [`00c3ccb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cc68.md#insn-00c3ccb0) · [`00c3ccc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cc68.md#insn-00c3ccc4) · [`00c3cccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cc68.md#insn-00c3cccc)

~~~diff
- 00c3c888 ["INT_ADD", "register:40f0:8", ["const:c3c888:8", "const:4:8"]]
- 00c3c888 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c3ccb0 ["INT_ADD", "register:40f0:8", ["const:c3ccb0:8", "const:4:8"]]
+ 00c3ccb0 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c3c888 bytes 06750094
+ 00c3ccb0 bytes fc740094
- 00c3c89c ["INT_ADD", "register:40f0:8", ["const:c3c89c:8", "const:4:8"]]
- 00c3c89c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c3ccc4 ["INT_ADD", "register:40f0:8", ["const:c3ccc4:8", "const:4:8"]]
+ 00c3ccc4 ["CALL", null, ["callee:00c5b140:8"]]
- 00c3c89c bytes 29790094
+ 00c3ccc4 bytes 1f790094
- 00c3c8a4 ["INT_ADD", "register:40f0:8", ["const:c3c8a4:8", "const:4:8"]]
- 00c3c8a4 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3cccc ["INT_ADD", "register:40f0:8", ["const:c3cccc:8", "const:4:8"]]
+ 00c3cccc ["CALL", null, ["callee:00c5a020:8"]]
- 00c3c8a4 bytes df740094
+ 00c3cccc bytes d5740094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-016af622fb8b6ca84fc2c719862b4404"></a>

### [`00c3cc08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cc08.md) → [`00c3d030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d030.md) FUN_00c3d030

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) · 呼出先 2件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)
- 新版 呼出元 2件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3cc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cc08.md#insn-00c3cc7c) · [`00c3cca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cc08.md#insn-00c3cca4) · [`00c3cd38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cc08.md#insn-00c3cd38)
- 新版 [`00c3d0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d030.md#insn-00c3d0a4) · [`00c3d0cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d030.md#insn-00c3d0cc) · [`00c3d160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d030.md#insn-00c3d160)

~~~diff
- 00c3cc7c ["INT_ADD", "register:40f0:8", ["const:c3cc7c:8", "const:4:8"]]
- 00c3cc7c ["CALL", null, ["callee:00c58660:8"]]
+ 00c3d0a4 ["INT_ADD", "register:40f0:8", ["const:c3d0a4:8", "const:4:8"]]
+ 00c3d0a4 ["CALL", null, ["callee:00c58660:8"]]
- 00c3cc7c bytes 796d0094
+ 00c3d0a4 bytes 6f6d0094
- 00c3cca4 ["INT_ADD", "register:40f0:8", ["const:c3cca4:8", "const:4:8"]]
- 00c3cca4 ["CALL", null, ["callee:00c57f40:8"]]
+ 00c3d0cc ["INT_ADD", "register:40f0:8", ["const:c3d0cc:8", "const:4:8"]]
+ 00c3d0cc ["CALL", null, ["callee:00c57f40:8"]]
- 00c3cca4 bytes a76b0094
+ 00c3d0cc bytes 9d6b0094
- 00c3cd38 ["INT_ADD", "register:40f0:8", ["const:c3cd38:8", "const:4:8"]]
- 00c3cd38 ["CALL", null, ["callee:00c58660:8"]]
+ 00c3d160 ["INT_ADD", "register:40f0:8", ["const:c3d160:8", "const:4:8"]]
+ 00c3d160 ["CALL", null, ["callee:00c58660:8"]]
- 00c3cd38 bytes 4a6d0094
+ 00c3d160 bytes 406d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29b93f1268fd872a69c7037a8b4b86f0"></a>

### [`00c3d908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d908.md) → [`00c3dd30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dd30.md) FUN_00c3dd30

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3d958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d908.md#insn-00c3d958) · [`00c3d974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d908.md#insn-00c3d974) · [`00c3d998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d908.md#insn-00c3d998)
- 新版 [`00c3dd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dd30.md#insn-00c3dd80) · [`00c3dd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dd30.md#insn-00c3dd9c) · [`00c3ddc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dd30.md#insn-00c3ddc0)

~~~diff
- 00c3d958 ["INT_ADD", "register:40f0:8", ["const:c3d958:8", "const:4:8"]]
- 00c3d958 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c3dd80 ["INT_ADD", "register:40f0:8", ["const:c3dd80:8", "const:4:8"]]
+ 00c3dd80 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c3d958 bytes d2700094
+ 00c3dd80 bytes c8700094
- 00c3d974 ["INT_ADD", "register:40f0:8", ["const:c3d974:8", "const:4:8"]]
- 00c3d974 ["CALL", null, ["callee:00c58000:8"]]
+ 00c3dd9c ["INT_ADD", "register:40f0:8", ["const:c3dd9c:8", "const:4:8"]]
+ 00c3dd9c ["CALL", null, ["callee:00c58000:8"]]
- 00c3d974 bytes a3680094
+ 00c3dd9c bytes 99680094
- 00c3d998 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c3d998 ["INT_ADD", "register:40f0:8", ["const:c3d998:8", "const:4:8"]]
- 00c3d998 ["CALLIND", null, ["register:0:8"]]
+ 00c3ddc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3ddc0 ["INT_ADD", "register:40f0:8", ["const:c3ddc0:8", "const:4:8"]]
+ 00c3ddc0 ["CALLIND", null, ["register:0:8"]]
- 00c3d998 bytes 00013fd6
+ 00c3ddc0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07443e50782c108c3b0d8ff24ca48493"></a>

### [`00c3de54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3de54.md) → [`00c3e27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e27c.md) FUN_00c3e27c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3dea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3de54.md#insn-00c3dea4) · [`00c3dec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3de54.md#insn-00c3dec0) · [`00c3dee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3de54.md#insn-00c3dee4)
- 新版 [`00c3e2cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e27c.md#insn-00c3e2cc) · [`00c3e2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e27c.md#insn-00c3e2e8) · [`00c3e30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e27c.md#insn-00c3e30c)

~~~diff
- 00c3dea4 ["INT_ADD", "register:40f0:8", ["const:c3dea4:8", "const:4:8"]]
- 00c3dea4 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c3e2cc ["INT_ADD", "register:40f0:8", ["const:c3e2cc:8", "const:4:8"]]
+ 00c3e2cc ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c3dea4 bytes 7f6f0094
+ 00c3e2cc bytes 756f0094
- 00c3dec0 ["INT_ADD", "register:40f0:8", ["const:c3dec0:8", "const:4:8"]]
- 00c3dec0 ["CALL", null, ["callee:00c58000:8"]]
+ 00c3e2e8 ["INT_ADD", "register:40f0:8", ["const:c3e2e8:8", "const:4:8"]]
+ 00c3e2e8 ["CALL", null, ["callee:00c58000:8"]]
- 00c3dec0 bytes 50670094
+ 00c3e2e8 bytes 46670094
- 00c3dee4 ["INT_ADD", "register:40f0:8", ["const:c3dee4:8", "const:4:8"]]
- 00c3dee4 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c3e30c ["INT_ADD", "register:40f0:8", ["const:c3e30c:8", "const:4:8"]]
+ 00c3e30c ["CALL", null, ["callee:00c5b140:8"]]
- 00c3dee4 bytes 97730094
+ 00c3e30c bytes 8d730094
~~~


<a id="compare-561dcbf1b8e749944c00020cd490c8be"></a>

### [`00c3df00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3df00.md) → [`00c3e328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e328.md) FUN_00c3e328

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3df34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3df00.md#insn-00c3df34) · [`00c3df58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3df00.md#insn-00c3df58) · [`00c3dfa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3df00.md#insn-00c3dfa4)
- 新版 [`00c3e35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e328.md#insn-00c3e35c) · [`00c3e380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e328.md#insn-00c3e380) · [`00c3e3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e328.md#insn-00c3e3cc)

~~~diff
- 00c3df34 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c3df34 ["INT_ADD", "register:40f0:8", ["const:c3df34:8", "const:4:8"]]
- 00c3df34 ["CALLIND", null, ["register:0:8"]]
+ 00c3e35c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3e35c ["INT_ADD", "register:40f0:8", ["const:c3e35c:8", "const:4:8"]]
+ 00c3e35c ["CALLIND", null, ["register:0:8"]]
- 00c3df34 bytes 00013fd6
+ 00c3e35c bytes 00013fd6
- 00c3df58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c3df58 ["INT_ADD", "register:40f0:8", ["const:c3df58:8", "const:4:8"]]
- 00c3df58 ["CALLIND", null, ["register:0:8"]]
+ 00c3e380 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3e380 ["INT_ADD", "register:40f0:8", ["const:c3e380:8", "const:4:8"]]
+ 00c3e380 ["CALLIND", null, ["register:0:8"]]
- 00c3df58 bytes 00013fd6
+ 00c3e380 bytes 00013fd6
- 00c3dfa4 ["INT_ADD", "register:40f0:8", ["const:c3dfa4:8", "const:4:8"]]
- 00c3dfa4 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c3e3cc ["INT_ADD", "register:40f0:8", ["const:c3e3cc:8", "const:4:8"]]
+ 00c3e3cc ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c3dfa4 bytes 3f6f0094
+ 00c3e3cc bytes 356f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbdb2a0d7fc8e046e596ed18c2c20663"></a>

### [`00c3f548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f548.md) → [`00c3f970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f970.md) FUN_00c3f970

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c3e714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e714.md) · 呼出先 4件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c3eb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3eb3c.md) · 呼出先 4件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3f590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f548.md#insn-00c3f590) · [`00c3f5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f548.md#insn-00c3f5a4) · [`00c3f5ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f548.md#insn-00c3f5ac)
- 新版 [`00c3f9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f970.md#insn-00c3f9b8) · [`00c3f9cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f970.md#insn-00c3f9cc) · [`00c3f9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f970.md#insn-00c3f9d4)

~~~diff
- 00c3f590 ["INT_ADD", "register:40f0:8", ["const:c3f590:8", "const:4:8"]]
- 00c3f590 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c3f9b8 ["INT_ADD", "register:40f0:8", ["const:c3f9b8:8", "const:4:8"]]
+ 00c3f9b8 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c3f590 bytes c4690094
+ 00c3f9b8 bytes ba690094
- 00c3f5a4 ["INT_ADD", "register:40f0:8", ["const:c3f5a4:8", "const:4:8"]]
- 00c3f5a4 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c3f9cc ["INT_ADD", "register:40f0:8", ["const:c3f9cc:8", "const:4:8"]]
+ 00c3f9cc ["CALL", null, ["callee:00c5b140:8"]]
- 00c3f5a4 bytes e76d0094
+ 00c3f9cc bytes dd6d0094
- 00c3f5ac ["INT_ADD", "register:40f0:8", ["const:c3f5ac:8", "const:4:8"]]
- 00c3f5ac ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3f9d4 ["INT_ADD", "register:40f0:8", ["const:c3f9d4:8", "const:4:8"]]
+ 00c3f9d4 ["CALL", null, ["callee:00c5a020:8"]]
- 00c3f5ac bytes 9d690094
+ 00c3f9d4 bytes 93690094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fa9ed3715338c61cb2b3bd10a480119"></a>

### [`00c3f6cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f6cc.md) → [`00c3faf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3faf4.md) FUN_00c3faf4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3f718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f6cc.md#insn-00c3f718)
- 新版 [`00c3fb40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3faf4.md#insn-00c3fb40)

~~~diff
- 00c3f718 ["COPY", "register:0:8", ["register:4048:8"]]
- 00c3f718 ["INT_ADD", "register:40f0:8", ["const:c3f718:8", "const:4:8"]]
- 00c3f718 ["CALLIND", null, ["register:0:8"]]
+ 00c3fb40 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c3fb40 ["INT_ADD", "register:40f0:8", ["const:c3fb40:8", "const:4:8"]]
+ 00c3fb40 ["CALLIND", null, ["register:0:8"]]
- 00c3f718 bytes 20013fd6
+ 00c3fb40 bytes 20013fd6
~~~


<a id="compare-92267f4caac8a9dd3b3cbe764c67bdc4"></a>

### [`00c3f750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f750.md) → [`00c3fb78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fb78.md) FUN_00c3fb78

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3f79c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f750.md#insn-00c3f79c)
- 新版 [`00c3fbc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fb78.md#insn-00c3fbc4)

~~~diff
- 00c3f79c ["COPY", "register:0:8", ["register:4048:8"]]
- 00c3f79c ["INT_ADD", "register:40f0:8", ["const:c3f79c:8", "const:4:8"]]
- 00c3f79c ["CALLIND", null, ["register:0:8"]]
+ 00c3fbc4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c3fbc4 ["INT_ADD", "register:40f0:8", ["const:c3fbc4:8", "const:4:8"]]
+ 00c3fbc4 ["CALLIND", null, ["register:0:8"]]
- 00c3f79c bytes 20013fd6
+ 00c3fbc4 bytes 20013fd6
~~~


<a id="compare-8d3ff68ca0fb55842c9a86ff27067f1f"></a>

### [`00c3f7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f7d4.md) → [`00c3fbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fbfc.md) FUN_00c3fbfc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3f820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f7d4.md#insn-00c3f820)
- 新版 [`00c3fc48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fbfc.md#insn-00c3fc48)

~~~diff
- 00c3f820 ["COPY", "register:0:8", ["register:4048:8"]]
- 00c3f820 ["INT_ADD", "register:40f0:8", ["const:c3f820:8", "const:4:8"]]
- 00c3f820 ["CALLIND", null, ["register:0:8"]]
+ 00c3fc48 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c3fc48 ["INT_ADD", "register:40f0:8", ["const:c3fc48:8", "const:4:8"]]
+ 00c3fc48 ["CALLIND", null, ["register:0:8"]]
- 00c3f820 bytes 20013fd6
+ 00c3fc48 bytes 20013fd6
~~~


<a id="compare-bea7295f98b2b422225b8adfeb93fcfa"></a>

### [`00c3f858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f858.md) → [`00c3fc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fc80.md) FUN_00c3fc80

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3f88c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f858.md#insn-00c3f88c)
- 新版 [`00c3fcb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fc80.md#insn-00c3fcb4)

~~~diff
- 00c3f88c ["COPY", "register:0:8", ["register:4048:8"]]
- 00c3f88c ["INT_ADD", "register:40f0:8", ["const:c3f88c:8", "const:4:8"]]
- 00c3f88c ["CALLIND", null, ["register:0:8"]]
+ 00c3fcb4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c3fcb4 ["INT_ADD", "register:40f0:8", ["const:c3fcb4:8", "const:4:8"]]
+ 00c3fcb4 ["CALLIND", null, ["register:0:8"]]
- 00c3f88c bytes 20013fd6
+ 00c3fcb4 bytes 20013fd6
~~~


<a id="compare-f761aad1e9f00e1ad655d7545a9d4cf0"></a>

### [`00c3f8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f8ac.md) → [`00c3fcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fcd4.md) FUN_00c3fcd4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f8ac.md#insn-00c3f8dc)
- 新版 [`00c3fd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fcd4.md#insn-00c3fd04)

~~~diff
- 00c3f8dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c3f8dc ["INT_ADD", "register:40f0:8", ["const:c3f8dc:8", "const:4:8"]]
- 00c3f8dc ["CALLIND", null, ["register:0:8"]]
+ 00c3fd04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3fd04 ["INT_ADD", "register:40f0:8", ["const:c3fd04:8", "const:4:8"]]
+ 00c3fd04 ["CALLIND", null, ["register:0:8"]]
- 00c3f8dc bytes 00013fd6
+ 00c3fd04 bytes 00013fd6
~~~


<a id="compare-3c4b01fae060c177f7f1af3bd4a3e164"></a>

### [`00c3f8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f8fc.md) → [`00c3fd24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd24.md) FUN_00c3fd24

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3f92c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f8fc.md#insn-00c3f92c)
- 新版 [`00c3fd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd24.md#insn-00c3fd54)

~~~diff
- 00c3f92c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c3f92c ["INT_ADD", "register:40f0:8", ["const:c3f92c:8", "const:4:8"]]
- 00c3f92c ["CALLIND", null, ["register:0:8"]]
+ 00c3fd54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3fd54 ["INT_ADD", "register:40f0:8", ["const:c3fd54:8", "const:4:8"]]
+ 00c3fd54 ["CALLIND", null, ["register:0:8"]]
- 00c3f92c bytes 00013fd6
+ 00c3fd54 bytes 00013fd6
~~~


<a id="compare-8b6ee2ab833ab91fdfa3da57b0343952"></a>

### [`00c43984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43984.md) → [`00c43dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43dac.md) FUN_00c43dac

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c439f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43984.md#insn-00c439f8) · [`00c43a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43984.md#insn-00c43a1c) · [`00c43a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43984.md#insn-00c43a58)
- 新版 [`00c43e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43dac.md#insn-00c43e20) · [`00c43e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43dac.md#insn-00c43e44) · [`00c43e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43dac.md#insn-00c43e80)

~~~diff
- 00c439f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c439f8 ["INT_ADD", "register:40f0:8", ["const:c439f8:8", "const:4:8"]]
- 00c439f8 ["CALLIND", null, ["register:0:8"]]
+ 00c43e20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c43e20 ["INT_ADD", "register:40f0:8", ["const:c43e20:8", "const:4:8"]]
+ 00c43e20 ["CALLIND", null, ["register:0:8"]]
- 00c439f8 bytes 00013fd6
+ 00c43e20 bytes 00013fd6
- 00c43a1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c43a1c ["INT_ADD", "register:40f0:8", ["const:c43a1c:8", "const:4:8"]]
- 00c43a1c ["CALLIND", null, ["register:0:8"]]
+ 00c43e44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c43e44 ["INT_ADD", "register:40f0:8", ["const:c43e44:8", "const:4:8"]]
+ 00c43e44 ["CALLIND", null, ["register:0:8"]]
- 00c43a1c bytes 00013fd6
+ 00c43e44 bytes 00013fd6
- 00c43a58 ["INT_ADD", "register:40f0:8", ["const:c43a58:8", "const:4:8"]]
- 00c43a58 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c43e80 ["INT_ADD", "register:40f0:8", ["const:c43e80:8", "const:4:8"]]
+ 00c43e80 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c43a58 bytes 92580094
+ 00c43e80 bytes 88580094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da97d704a535bfd137f7d268e327b9ef"></a>

### [`00c43f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43f58.md) → [`00c44380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44380.md) FUN_00c44380

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c43fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43f58.md#insn-00c43fa8) · [`00c43fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43f58.md#insn-00c43fc4) · [`00c44000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43f58.md#insn-00c44000)
- 新版 [`00c443d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44380.md#insn-00c443d0) · [`00c443ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44380.md#insn-00c443ec) · [`00c44428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44380.md#insn-00c44428)

~~~diff
- 00c43fa8 ["INT_ADD", "register:40f0:8", ["const:c43fa8:8", "const:4:8"]]
- 00c43fa8 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c443d0 ["INT_ADD", "register:40f0:8", ["const:c443d0:8", "const:4:8"]]
+ 00c443d0 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c43fa8 bytes 3e570094
+ 00c443d0 bytes 34570094
- 00c43fc4 ["INT_ADD", "register:40f0:8", ["const:c43fc4:8", "const:4:8"]]
- 00c43fc4 ["CALL", null, ["callee:00c58000:8"]]
+ 00c443ec ["INT_ADD", "register:40f0:8", ["const:c443ec:8", "const:4:8"]]
+ 00c443ec ["CALL", null, ["callee:00c58000:8"]]
- 00c43fc4 bytes 0f4f0094
+ 00c443ec bytes 054f0094
- 00c44000 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c44000 ["INT_ADD", "register:40f0:8", ["const:c44000:8", "const:4:8"]]
- 00c44000 ["CALLIND", null, ["register:0:8"]]
+ 00c44428 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c44428 ["INT_ADD", "register:40f0:8", ["const:c44428:8", "const:4:8"]]
+ 00c44428 ["CALLIND", null, ["register:0:8"]]
- 00c44000 bytes 00013fd6
+ 00c44428 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fbd8177ce6ce8cb0c8728d0deb0853a"></a>

### [`00c44140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44140.md) → [`00c44568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44568.md) FUN_00c44568

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4418c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44140.md#insn-00c4418c) · [`00c441b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44140.md#insn-00c441b0) · [`00c441f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44140.md#insn-00c441f4)
- 新版 [`00c445b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44568.md#insn-00c445b4) · [`00c445d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44568.md#insn-00c445d8) · [`00c4461c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44568.md#insn-00c4461c)

~~~diff
- 00c4418c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4418c ["INT_ADD", "register:40f0:8", ["const:c4418c:8", "const:4:8"]]
- 00c4418c ["CALLIND", null, ["register:0:8"]]
+ 00c445b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c445b4 ["INT_ADD", "register:40f0:8", ["const:c445b4:8", "const:4:8"]]
+ 00c445b4 ["CALLIND", null, ["register:0:8"]]
- 00c4418c bytes 00013fd6
+ 00c445b4 bytes 00013fd6
- 00c441b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c441b0 ["INT_ADD", "register:40f0:8", ["const:c441b0:8", "const:4:8"]]
- 00c441b0 ["CALLIND", null, ["register:0:8"]]
+ 00c445d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c445d8 ["INT_ADD", "register:40f0:8", ["const:c445d8:8", "const:4:8"]]
+ 00c445d8 ["CALLIND", null, ["register:0:8"]]
- 00c441b0 bytes 00013fd6
+ 00c445d8 bytes 00013fd6
- 00c441f4 ["INT_ADD", "register:40f0:8", ["const:c441f4:8", "const:4:8"]]
- 00c441f4 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4461c ["INT_ADD", "register:40f0:8", ["const:c4461c:8", "const:4:8"]]
+ 00c4461c ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c441f4 bytes ab560094
+ 00c4461c bytes a1560094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b46113d4b9f74caab920bc639c5530ae"></a>

### [`00c44328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44328.md) → [`00c44750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44750.md) FUN_00c44750

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c44370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44328.md#insn-00c44370) · [`00c44394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44328.md#insn-00c44394) · [`00c443d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44328.md#insn-00c443d0)
- 新版 [`00c44798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44750.md#insn-00c44798) · [`00c447bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44750.md#insn-00c447bc) · [`00c447f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44750.md#insn-00c447f8)

~~~diff
- 00c44370 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c44370 ["INT_ADD", "register:40f0:8", ["const:c44370:8", "const:4:8"]]
- 00c44370 ["CALLIND", null, ["register:0:8"]]
+ 00c44798 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c44798 ["INT_ADD", "register:40f0:8", ["const:c44798:8", "const:4:8"]]
+ 00c44798 ["CALLIND", null, ["register:0:8"]]
- 00c44370 bytes 00013fd6
+ 00c44798 bytes 00013fd6
- 00c44394 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c44394 ["INT_ADD", "register:40f0:8", ["const:c44394:8", "const:4:8"]]
- 00c44394 ["CALLIND", null, ["register:0:8"]]
+ 00c447bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c447bc ["INT_ADD", "register:40f0:8", ["const:c447bc:8", "const:4:8"]]
+ 00c447bc ["CALLIND", null, ["register:0:8"]]
- 00c44394 bytes 00013fd6
+ 00c447bc bytes 00013fd6
- 00c443d0 ["INT_ADD", "register:40f0:8", ["const:c443d0:8", "const:4:8"]]
- 00c443d0 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c447f8 ["INT_ADD", "register:40f0:8", ["const:c447f8:8", "const:4:8"]]
+ 00c447f8 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c443d0 bytes 34560094
+ 00c447f8 bytes 2a560094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a539dc9494c30a3aff5ac0f0b73765f9"></a>

### [`00c44688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44688.md) → [`00c44ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44ab0.md) FUN_00c44ab0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c446d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44688.md#insn-00c446d4) · [`00c446f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44688.md#insn-00c446f8) · [`00c4473c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44688.md#insn-00c4473c)
- 新版 [`00c44afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44ab0.md#insn-00c44afc) · [`00c44b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44ab0.md#insn-00c44b20) · [`00c44b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44ab0.md#insn-00c44b64)

~~~diff
- 00c446d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c446d4 ["INT_ADD", "register:40f0:8", ["const:c446d4:8", "const:4:8"]]
- 00c446d4 ["CALLIND", null, ["register:0:8"]]
+ 00c44afc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c44afc ["INT_ADD", "register:40f0:8", ["const:c44afc:8", "const:4:8"]]
+ 00c44afc ["CALLIND", null, ["register:0:8"]]
- 00c446d4 bytes 00013fd6
+ 00c44afc bytes 00013fd6
- 00c446f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c446f8 ["INT_ADD", "register:40f0:8", ["const:c446f8:8", "const:4:8"]]
- 00c446f8 ["CALLIND", null, ["register:0:8"]]
+ 00c44b20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c44b20 ["INT_ADD", "register:40f0:8", ["const:c44b20:8", "const:4:8"]]
+ 00c44b20 ["CALLIND", null, ["register:0:8"]]
- 00c446f8 bytes 00013fd6
+ 00c44b20 bytes 00013fd6
- 00c4473c ["INT_ADD", "register:40f0:8", ["const:c4473c:8", "const:4:8"]]
- 00c4473c ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c44b64 ["INT_ADD", "register:40f0:8", ["const:c44b64:8", "const:4:8"]]
+ 00c44b64 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4473c bytes 59550094
+ 00c44b64 bytes 4f550094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e39f817b9e102519f8b45969f5f41166"></a>

### [`00c449bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c449bc.md) → [`00c44de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44de4.md) FUN_00c44de4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c44a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c449bc.md#insn-00c44a0c) · [`00c44a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c449bc.md#insn-00c44a58) · [`00c44ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c449bc.md#insn-00c44ab8)
- 新版 [`00c44e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44de4.md#insn-00c44e34) · [`00c44e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44de4.md#insn-00c44e80) · [`00c44ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44de4.md#insn-00c44ee0)

~~~diff
- 00c44a0c ["INT_ADD", "register:40f0:8", ["const:c44a0c:8", "const:4:8"]]
- 00c44a0c ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c44e34 ["INT_ADD", "register:40f0:8", ["const:c44e34:8", "const:4:8"]]
+ 00c44e34 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c44a0c bytes a5540094
+ 00c44e34 bytes 9b540094
- 00c44a58 ["INT_ADD", "register:40f0:8", ["const:c44a58:8", "const:4:8"]]
- 00c44a58 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c44e80 ["INT_ADD", "register:40f0:8", ["const:c44e80:8", "const:4:8"]]
+ 00c44e80 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c44a58 bytes 92540094
+ 00c44e80 bytes 88540094
- 00c44ab8 ["INT_ADD", "register:40f0:8", ["const:c44ab8:8", "const:4:8"]]
- 00c44ab8 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c44ee0 ["INT_ADD", "register:40f0:8", ["const:c44ee0:8", "const:4:8"]]
+ 00c44ee0 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c44ab8 bytes 7a540094
+ 00c44ee0 bytes 70540094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43387912737640b74f4a7547d17c4bd5"></a>

### [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) → [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) FUN_00c45144

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 15件 [`00c449bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c449bc.md) [`00c45124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45124.md) [`00c45250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45250.md) [`00c48648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48648.md) [`00c48a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48a98.md) · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 15件 [`00c44de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c44de4.md) [`00c4554c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c4554c.md) [`00c45678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45678.md) [`00c48a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48a70.md) [`00c48ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48ec0.md) · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c44dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md#insn-00c44dac) · [`00c44dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md#insn-00c44dfc) · [`00c44e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md#insn-00c44e20)
- 新版 [`00c451d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md#insn-00c451d4) · [`00c45224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md#insn-00c45224) · [`00c45248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md#insn-00c45248)

~~~diff
- 00c44dac ["INT_ADD", "register:40f0:8", ["const:c44dac:8", "const:4:8"]]
- 00c44dac ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c451d4 ["INT_ADD", "register:40f0:8", ["const:c451d4:8", "const:4:8"]]
+ 00c451d4 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c44dac bytes bd530094
+ 00c451d4 bytes b3530094
- 00c44dfc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c44dfc ["INT_ADD", "register:40f0:8", ["const:c44dfc:8", "const:4:8"]]
- 00c44dfc ["CALLIND", null, ["register:0:8"]]
+ 00c45224 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c45224 ["INT_ADD", "register:40f0:8", ["const:c45224:8", "const:4:8"]]
+ 00c45224 ["CALLIND", null, ["register:0:8"]]
- 00c44dfc bytes 00013fd6
+ 00c45224 bytes 00013fd6
- 00c44e20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c44e20 ["INT_ADD", "register:40f0:8", ["const:c44e20:8", "const:4:8"]]
- 00c44e20 ["CALLIND", null, ["register:0:8"]]
+ 00c45248 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c45248 ["INT_ADD", "register:40f0:8", ["const:c45248:8", "const:4:8"]]
+ 00c45248 ["CALLIND", null, ["register:0:8"]]
- 00c44e20 bytes 00013fd6
+ 00c45248 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-722b638c23fb48cba726f3d04984b1b3"></a>

### [`00c44f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44f4c.md) → [`00c45374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45374.md) FUN_00c45374

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c44f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44f4c.md#insn-00c44f98) · [`00c44fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44f4c.md#insn-00c44fe4) · [`00c45048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44f4c.md#insn-00c45048)
- 新版 [`00c453c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45374.md#insn-00c453c0) · [`00c4540c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45374.md#insn-00c4540c) · [`00c45470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45374.md#insn-00c45470)

~~~diff
- 00c44f98 ["INT_ADD", "register:40f0:8", ["const:c44f98:8", "const:4:8"]]
- 00c44f98 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c453c0 ["INT_ADD", "register:40f0:8", ["const:c453c0:8", "const:4:8"]]
+ 00c453c0 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c44f98 bytes 42530094
+ 00c453c0 bytes 38530094
- 00c44fe4 ["INT_ADD", "register:40f0:8", ["const:c44fe4:8", "const:4:8"]]
- 00c44fe4 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4540c ["INT_ADD", "register:40f0:8", ["const:c4540c:8", "const:4:8"]]
+ 00c4540c ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c44fe4 bytes 2f530094
+ 00c4540c bytes 25530094
- 00c45048 ["INT_ADD", "register:40f0:8", ["const:c45048:8", "const:4:8"]]
- 00c45048 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c45470 ["INT_ADD", "register:40f0:8", ["const:c45470:8", "const:4:8"]]
+ 00c45470 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c45048 bytes 16530094
+ 00c45470 bytes 0c530094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f44cb559103de9faee964af738882687"></a>

### [`00c45124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45124.md) → [`00c4554c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c4554c.md) FUN_00c4554c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c45150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45124.md#insn-00c45150) · [`00c45174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45124.md#insn-00c45174) · [`00c451ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45124.md#insn-00c451ac)
- 新版 [`00c45578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c4554c.md#insn-00c45578) · [`00c4559c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c4554c.md#insn-00c4559c) · [`00c455d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c4554c.md#insn-00c455d4)

~~~diff
- 00c45150 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c45150 ["INT_ADD", "register:40f0:8", ["const:c45150:8", "const:4:8"]]
- 00c45150 ["CALLIND", null, ["register:0:8"]]
+ 00c45578 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c45578 ["INT_ADD", "register:40f0:8", ["const:c45578:8", "const:4:8"]]
+ 00c45578 ["CALLIND", null, ["register:0:8"]]
- 00c45150 bytes 00013fd6
+ 00c45578 bytes 00013fd6
- 00c45174 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c45174 ["INT_ADD", "register:40f0:8", ["const:c45174:8", "const:4:8"]]
- 00c45174 ["CALLIND", null, ["register:0:8"]]
+ 00c4559c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4559c ["INT_ADD", "register:40f0:8", ["const:c4559c:8", "const:4:8"]]
+ 00c4559c ["CALLIND", null, ["register:0:8"]]
- 00c45174 bytes 00013fd6
+ 00c4559c bytes 00013fd6
- 00c451ac ["INT_ADD", "register:40f0:8", ["const:c451ac:8", "const:4:8"]]
- 00c451ac ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c455d4 ["INT_ADD", "register:40f0:8", ["const:c455d4:8", "const:4:8"]]
+ 00c455d4 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c451ac bytes bd520094
+ 00c455d4 bytes b3520094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50b25bd56e06de394ea08b4b0b9a3f9f"></a>

### [`00c45250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45250.md) → [`00c45678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45678.md) FUN_00c45678

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c452a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45250.md#insn-00c452a0) · [`00c452d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45250.md#insn-00c452d4) · [`00c452f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45250.md#insn-00c452f8)
- 新版 [`00c456c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45678.md#insn-00c456c8) · [`00c456fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45678.md#insn-00c456fc) · [`00c45720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45678.md#insn-00c45720)

~~~diff
- 00c452a0 ["INT_ADD", "register:40f0:8", ["const:c452a0:8", "const:4:8"]]
- 00c452a0 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c456c8 ["INT_ADD", "register:40f0:8", ["const:c456c8:8", "const:4:8"]]
+ 00c456c8 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c452a0 bytes 80520094
+ 00c456c8 bytes 76520094
- 00c452d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c452d4 ["INT_ADD", "register:40f0:8", ["const:c452d4:8", "const:4:8"]]
- 00c452d4 ["CALLIND", null, ["register:0:8"]]
+ 00c456fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c456fc ["INT_ADD", "register:40f0:8", ["const:c456fc:8", "const:4:8"]]
+ 00c456fc ["CALLIND", null, ["register:0:8"]]
- 00c452d4 bytes 00013fd6
+ 00c456fc bytes 00013fd6
- 00c452f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c452f8 ["INT_ADD", "register:40f0:8", ["const:c452f8:8", "const:4:8"]]
- 00c452f8 ["CALLIND", null, ["register:0:8"]]
+ 00c45720 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c45720 ["INT_ADD", "register:40f0:8", ["const:c45720:8", "const:4:8"]]
+ 00c45720 ["CALLIND", null, ["register:0:8"]]
- 00c452f8 bytes 00013fd6
+ 00c45720 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f4eb83acfe550bd4b315b81a6fc95fd"></a>

### [`00c45430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45430.md) → [`00c45858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45858.md) FUN_00c45858

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c45478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45430.md#insn-00c45478) · [`00c4549c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45430.md#insn-00c4549c) · [`00c454d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45430.md#insn-00c454d8)
- 新版 [`00c458a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45858.md#insn-00c458a0) · [`00c458c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45858.md#insn-00c458c4) · [`00c45900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45858.md#insn-00c45900)

~~~diff
- 00c45478 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c45478 ["INT_ADD", "register:40f0:8", ["const:c45478:8", "const:4:8"]]
- 00c45478 ["CALLIND", null, ["register:0:8"]]
+ 00c458a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c458a0 ["INT_ADD", "register:40f0:8", ["const:c458a0:8", "const:4:8"]]
+ 00c458a0 ["CALLIND", null, ["register:0:8"]]
- 00c45478 bytes 00013fd6
+ 00c458a0 bytes 00013fd6
- 00c4549c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4549c ["INT_ADD", "register:40f0:8", ["const:c4549c:8", "const:4:8"]]
- 00c4549c ["CALLIND", null, ["register:0:8"]]
+ 00c458c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c458c4 ["INT_ADD", "register:40f0:8", ["const:c458c4:8", "const:4:8"]]
+ 00c458c4 ["CALLIND", null, ["register:0:8"]]
- 00c4549c bytes 00013fd6
+ 00c458c4 bytes 00013fd6
- 00c454d8 ["INT_ADD", "register:40f0:8", ["const:c454d8:8", "const:4:8"]]
- 00c454d8 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c45900 ["INT_ADD", "register:40f0:8", ["const:c45900:8", "const:4:8"]]
+ 00c45900 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c454d8 bytes f2510094
+ 00c45900 bytes e8510094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-924455dfe34bb86530bacc459d39a3e6"></a>

### [`00c458dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c458dc.md) → [`00c45d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45d04.md) FUN_00c45d04

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c45930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c458dc.md#insn-00c45930) · [`00c4594c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c458dc.md#insn-00c4594c) · [`00c4598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c458dc.md#insn-00c4598c)
- 新版 [`00c45d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45d04.md#insn-00c45d58) · [`00c45d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45d04.md#insn-00c45d74) · [`00c45db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45d04.md#insn-00c45db4)

~~~diff
- 00c45930 ["INT_ADD", "register:40f0:8", ["const:c45930:8", "const:4:8"]]
- 00c45930 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c45d58 ["INT_ADD", "register:40f0:8", ["const:c45d58:8", "const:4:8"]]
+ 00c45d58 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c45930 bytes dc500094
+ 00c45d58 bytes d2500094
- 00c4594c ["INT_ADD", "register:40f0:8", ["const:c4594c:8", "const:4:8"]]
- 00c4594c ["CALL", null, ["callee:00c58000:8"]]
+ 00c45d74 ["INT_ADD", "register:40f0:8", ["const:c45d74:8", "const:4:8"]]
+ 00c45d74 ["CALL", null, ["callee:00c58000:8"]]
- 00c4594c bytes ad480094
+ 00c45d74 bytes a3480094
- 00c4598c ["INT_ADD", "register:40f0:8", ["const:c4598c:8", "const:4:8"]]
- 00c4598c ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c45db4 ["INT_ADD", "register:40f0:8", ["const:c45db4:8", "const:4:8"]]
+ 00c45db4 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4598c bytes c5500094
+ 00c45db4 bytes bb500094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e980ca16e521641f49067c857a509d7c"></a>

### [`00c45c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45c20.md) → [`00c46048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46048.md) FUN_00c46048

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c45c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45c20.md#insn-00c45c74) · [`00c45c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45c20.md#insn-00c45c90) · [`00c45cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45c20.md#insn-00c45cd4)
- 新版 [`00c4609c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46048.md#insn-00c4609c) · [`00c460b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46048.md#insn-00c460b8) · [`00c460fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46048.md#insn-00c460fc)

~~~diff
- 00c45c74 ["INT_ADD", "register:40f0:8", ["const:c45c74:8", "const:4:8"]]
- 00c45c74 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4609c ["INT_ADD", "register:40f0:8", ["const:c4609c:8", "const:4:8"]]
+ 00c4609c ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c45c74 bytes 0b500094
+ 00c4609c bytes 01500094
- 00c45c90 ["INT_ADD", "register:40f0:8", ["const:c45c90:8", "const:4:8"]]
- 00c45c90 ["CALL", null, ["callee:00c58000:8"]]
+ 00c460b8 ["INT_ADD", "register:40f0:8", ["const:c460b8:8", "const:4:8"]]
+ 00c460b8 ["CALL", null, ["callee:00c58000:8"]]
- 00c45c90 bytes dc470094
+ 00c460b8 bytes d2470094
- 00c45cd4 ["INT_ADD", "register:40f0:8", ["const:c45cd4:8", "const:4:8"]]
- 00c45cd4 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c460fc ["INT_ADD", "register:40f0:8", ["const:c460fc:8", "const:4:8"]]
+ 00c460fc ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c45cd4 bytes f34f0094
+ 00c460fc bytes e94f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e64bf8f425b102a091de729dfc793d2"></a>

### [`00c469c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c469c4.md) → [`00c46dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46dec.md) FUN_00c46dec

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c46a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c469c4.md#insn-00c46a24) · [`00c46a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c469c4.md#insn-00c46a7c) · [`00c46a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c469c4.md#insn-00c46a98)
- 新版 [`00c46e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46dec.md#insn-00c46e4c) · [`00c46ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46dec.md#insn-00c46ea4) · [`00c46ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46dec.md#insn-00c46ec0)

~~~diff
- 00c46a24 ["INT_ADD", "register:40f0:8", ["const:c46a24:8", "const:4:8"]]
- 00c46a24 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c46e4c ["INT_ADD", "register:40f0:8", ["const:c46e4c:8", "const:4:8"]]
+ 00c46e4c ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c46a24 bytes 9f4c0094
+ 00c46e4c bytes 954c0094
- 00c46a7c ["INT_ADD", "register:40f0:8", ["const:c46a7c:8", "const:4:8"]]
- 00c46a7c ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c46ea4 ["INT_ADD", "register:40f0:8", ["const:c46ea4:8", "const:4:8"]]
+ 00c46ea4 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c46a7c bytes 894c0094
+ 00c46ea4 bytes 7f4c0094
- 00c46a98 ["INT_ADD", "register:40f0:8", ["const:c46a98:8", "const:4:8"]]
- 00c46a98 ["CALL", null, ["callee:00c58000:8"]]
+ 00c46ec0 ["INT_ADD", "register:40f0:8", ["const:c46ec0:8", "const:4:8"]]
+ 00c46ec0 ["CALL", null, ["callee:00c58000:8"]]
- 00c46a98 bytes 5a440094
+ 00c46ec0 bytes 50440094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78f3c9f4359c2691d9c0f16a7186f995"></a>

### [`00c472f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c472f8.md) → [`00c47720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47720.md) FUN_00c47720

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4733c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c472f8.md#insn-00c4733c) · [`00c47378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c472f8.md#insn-00c47378) · [`00c4739c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c472f8.md#insn-00c4739c)
- 新版 [`00c47764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47720.md#insn-00c47764) · [`00c477a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47720.md#insn-00c477a0) · [`00c477c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47720.md#insn-00c477c4)

~~~diff
- 00c4733c ["INT_ADD", "register:40f0:8", ["const:c4733c:8", "const:4:8"]]
- 00c4733c ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c47764 ["INT_ADD", "register:40f0:8", ["const:c47764:8", "const:4:8"]]
+ 00c47764 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4733c bytes 594a0094
+ 00c47764 bytes 4f4a0094
- 00c47378 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c47378 ["INT_ADD", "register:40f0:8", ["const:c47378:8", "const:4:8"]]
- 00c47378 ["CALLIND", null, ["register:0:8"]]
+ 00c477a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c477a0 ["INT_ADD", "register:40f0:8", ["const:c477a0:8", "const:4:8"]]
+ 00c477a0 ["CALLIND", null, ["register:0:8"]]
- 00c47378 bytes 00013fd6
+ 00c477a0 bytes 00013fd6
- 00c4739c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4739c ["INT_ADD", "register:40f0:8", ["const:c4739c:8", "const:4:8"]]
- 00c4739c ["CALLIND", null, ["register:0:8"]]
+ 00c477c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c477c4 ["INT_ADD", "register:40f0:8", ["const:c477c4:8", "const:4:8"]]
+ 00c477c4 ["CALLIND", null, ["register:0:8"]]
- 00c4739c bytes 00013fd6
+ 00c477c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66e5e079c4327c61424ee3ca87995209"></a>

### [`00c47ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c47ed4.md) → [`00c482fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c482fc.md) FUN_00c482fc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c47f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c47ed4.md#insn-00c47f1c) · [`00c47f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c47ed4.md#insn-00c47f84) · [`00c47fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c47ed4.md#insn-00c47fa0)
- 新版 [`00c48344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c482fc.md#insn-00c48344) · [`00c483ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c482fc.md#insn-00c483ac) · [`00c483c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c482fc.md#insn-00c483c8)

~~~diff
- 00c47f1c ["INT_ADD", "register:40f0:8", ["const:c47f1c:8", "const:4:8"]]
- 00c47f1c ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c48344 ["INT_ADD", "register:40f0:8", ["const:c48344:8", "const:4:8"]]
+ 00c48344 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c47f1c bytes 61470094
+ 00c48344 bytes 57470094
- 00c47f84 ["INT_ADD", "register:40f0:8", ["const:c47f84:8", "const:4:8"]]
- 00c47f84 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c483ac ["INT_ADD", "register:40f0:8", ["const:c483ac:8", "const:4:8"]]
+ 00c483ac ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c47f84 bytes 47470094
+ 00c483ac bytes 3d470094
- 00c47fa0 ["INT_ADD", "register:40f0:8", ["const:c47fa0:8", "const:4:8"]]
- 00c47fa0 ["CALL", null, ["callee:00c58000:8"]]
+ 00c483c8 ["INT_ADD", "register:40f0:8", ["const:c483c8:8", "const:4:8"]]
+ 00c483c8 ["CALL", null, ["callee:00c58000:8"]]
- 00c47fa0 bytes 183f0094
+ 00c483c8 bytes 0e3f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72bbea3833bf9ff345952f4e6bf50837"></a>

### [`00c480c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c480c4.md) → [`00c484ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c484ec.md) FUN_00c484ec

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c48130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c480c4.md#insn-00c48130) · [`00c48188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c480c4.md#insn-00c48188) · [`00c481e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c480c4.md#insn-00c481e8)
- 新版 [`00c48558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c484ec.md#insn-00c48558) · [`00c485b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c484ec.md#insn-00c485b0) · [`00c48610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c484ec.md#insn-00c48610)

~~~diff
- 00c48130 ["INT_ADD", "register:40f0:8", ["const:c48130:8", "const:4:8"]]
- 00c48130 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c48558 ["INT_ADD", "register:40f0:8", ["const:c48558:8", "const:4:8"]]
+ 00c48558 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c48130 bytes dc460094
+ 00c48558 bytes d2460094
- 00c48188 ["INT_ADD", "register:40f0:8", ["const:c48188:8", "const:4:8"]]
- 00c48188 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c485b0 ["INT_ADD", "register:40f0:8", ["const:c485b0:8", "const:4:8"]]
+ 00c485b0 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c48188 bytes c6460094
+ 00c485b0 bytes bc460094
- 00c481e8 ["INT_ADD", "register:40f0:8", ["const:c481e8:8", "const:4:8"]]
- 00c481e8 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c48610 ["INT_ADD", "register:40f0:8", ["const:c48610:8", "const:4:8"]]
+ 00c48610 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c481e8 bytes ae460094
+ 00c48610 bytes a4460094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c076b94ea1328726d7caf9d6d73396fa"></a>

### [`00c48380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48380.md) → [`00c487a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c487a8.md) FUN_00c487a8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c483a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48380.md#insn-00c483a4)
- 新版 [`00c487cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c487a8.md#insn-00c487cc)

~~~diff
- 00c483a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c483a4 ["INT_ADD", "register:40f0:8", ["const:c483a4:8", "const:4:8"]]
- 00c483a4 ["CALLIND", null, ["register:0:8"]]
+ 00c487cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c487cc ["INT_ADD", "register:40f0:8", ["const:c487cc:8", "const:4:8"]]
+ 00c487cc ["CALLIND", null, ["register:0:8"]]
- 00c483a4 bytes 00013fd6
+ 00c487cc bytes 00013fd6
~~~


<a id="compare-430e9b5bcbfc3d0419a4a652067c1fa1"></a>

### [`00c483f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c483f0.md) → [`00c48818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48818.md) FUN_00c48818

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c48414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c483f0.md#insn-00c48414) · [`00c48438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c483f0.md#insn-00c48438) · [`00c48464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c483f0.md#insn-00c48464)
- 新版 [`00c4883c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48818.md#insn-00c4883c) · [`00c48860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48818.md#insn-00c48860) · [`00c4888c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48818.md#insn-00c4888c)

~~~diff
- 00c48414 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c48414 ["INT_ADD", "register:40f0:8", ["const:c48414:8", "const:4:8"]]
- 00c48414 ["CALLIND", null, ["register:0:8"]]
+ 00c4883c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4883c ["INT_ADD", "register:40f0:8", ["const:c4883c:8", "const:4:8"]]
+ 00c4883c ["CALLIND", null, ["register:0:8"]]
- 00c48414 bytes 00013fd6
+ 00c4883c bytes 00013fd6
- 00c48438 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c48438 ["INT_ADD", "register:40f0:8", ["const:c48438:8", "const:4:8"]]
- 00c48438 ["CALLIND", null, ["register:0:8"]]
+ 00c48860 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c48860 ["INT_ADD", "register:40f0:8", ["const:c48860:8", "const:4:8"]]
+ 00c48860 ["CALLIND", null, ["register:0:8"]]
- 00c48438 bytes 00013fd6
+ 00c48860 bytes 00013fd6
- 00c48464 ["INT_ADD", "register:40f0:8", ["const:c48464:8", "const:4:8"]]
- 00c48464 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4888c ["INT_ADD", "register:40f0:8", ["const:c4888c:8", "const:4:8"]]
+ 00c4888c ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c48464 bytes 0f460094
+ 00c4888c bytes 05460094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f548e6eccd24336aa115326dbb5a2e4"></a>

### [`00c4850c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4850c.md) → [`00c48934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48934.md) FUN_00c48934

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c48530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4850c.md#insn-00c48530) · [`00c48554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4850c.md#insn-00c48554) · [`00c48590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4850c.md#insn-00c48590)
- 新版 [`00c48958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48934.md#insn-00c48958) · [`00c4897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48934.md#insn-00c4897c) · [`00c489b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48934.md#insn-00c489b8)

~~~diff
- 00c48530 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c48530 ["INT_ADD", "register:40f0:8", ["const:c48530:8", "const:4:8"]]
- 00c48530 ["CALLIND", null, ["register:0:8"]]
+ 00c48958 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c48958 ["INT_ADD", "register:40f0:8", ["const:c48958:8", "const:4:8"]]
+ 00c48958 ["CALLIND", null, ["register:0:8"]]
- 00c48530 bytes 00013fd6
+ 00c48958 bytes 00013fd6
- 00c48554 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c48554 ["INT_ADD", "register:40f0:8", ["const:c48554:8", "const:4:8"]]
- 00c48554 ["CALLIND", null, ["register:0:8"]]
+ 00c4897c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4897c ["INT_ADD", "register:40f0:8", ["const:c4897c:8", "const:4:8"]]
+ 00c4897c ["CALLIND", null, ["register:0:8"]]
- 00c48554 bytes 00013fd6
+ 00c4897c bytes 00013fd6
- 00c48590 ["INT_ADD", "register:40f0:8", ["const:c48590:8", "const:4:8"]]
- 00c48590 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c489b8 ["INT_ADD", "register:40f0:8", ["const:c489b8:8", "const:4:8"]]
+ 00c489b8 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c48590 bytes c4450094
+ 00c489b8 bytes ba450094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

