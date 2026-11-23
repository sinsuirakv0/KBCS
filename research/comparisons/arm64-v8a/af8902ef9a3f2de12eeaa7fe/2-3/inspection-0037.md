# v16.0.0 → v16.0.1 · 要調査の変更候補 (37)

[一覧の目次](README.md)

<a id="compare-aa828f2983e39e80b10a5134720644de"></a>

### [`00afd834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afd834.md) → [`00afdc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afd/00afdc5c.md) FUN_00afdc5c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afd850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afd834.md#insn-00afd850)
- 新版 `00afdc78`（命令位置の公開資料なし）

~~~diff
- 00afd850 ["INT_ADD", "register:40f0:8", ["const:afd850:8", "const:4:8"]]
- 00afd850 ["CALL", null, ["callee:008514f8:8"]]
+ 00afdc78 ["INT_ADD", "register:40f0:8", ["const:afdc78:8", "const:4:8"]]
+ 00afdc78 ["CALL", null, ["callee:008514f8:8"]]
- 00afd850 bytes 1a4ff597
+ 00afdc78 bytes 204ef597
~~~


<a id="compare-b6dbfab43649674bbc030ec44317081d"></a>

### [`00afd880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afd880.md) → [`00afdca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afd/00afdca8.md) FUN_00afdca8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afd894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afd880.md#insn-00afd894)
- 新版 `00afdcbc`（命令位置の公開資料なし）

~~~diff
- 00afd894 ["INT_ADD", "register:40f0:8", ["const:afd894:8", "const:4:8"]]
- 00afd894 ["CALL", null, ["callee:008514f8:8"]]
+ 00afdcbc ["INT_ADD", "register:40f0:8", ["const:afdcbc:8", "const:4:8"]]
+ 00afdcbc ["CALL", null, ["callee:008514f8:8"]]
- 00afd894 bytes 094ff597
+ 00afdcbc bytes 0f4ef597
~~~


<a id="compare-0b017c3a7fadb5b9fcc9321691360f2b"></a>

### [`00afd8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afd8c0.md) → [`00afdce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afd/00afdce8.md) FUN_00afdce8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afd8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afd8c0.md#insn-00afd8dc)
- 新版 `00afdd04`（命令位置の公開資料なし）

~~~diff
- 00afd8dc ["INT_ADD", "register:40f0:8", ["const:afd8dc:8", "const:4:8"]]
- 00afd8dc ["CALL", null, ["callee:008514f8:8"]]
+ 00afdd04 ["INT_ADD", "register:40f0:8", ["const:afdd04:8", "const:4:8"]]
+ 00afdd04 ["CALL", null, ["callee:008514f8:8"]]
- 00afd8dc bytes f74ef597
+ 00afdd04 bytes fd4df597
~~~


<a id="compare-cf9a27bf3763a4defb6a60d09288df12"></a>

### [`00afd90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afd90c.md) → [`00afdd34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afd/00afdd34.md) FUN_00afdd34

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afd920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afd90c.md#insn-00afd920)
- 新版 `00afdd48`（命令位置の公開資料なし）

~~~diff
- 00afd920 ["INT_ADD", "register:40f0:8", ["const:afd920:8", "const:4:8"]]
- 00afd920 ["CALL", null, ["callee:008514f8:8"]]
+ 00afdd48 ["INT_ADD", "register:40f0:8", ["const:afdd48:8", "const:4:8"]]
+ 00afdd48 ["CALL", null, ["callee:008514f8:8"]]
- 00afd920 bytes e64ef597
+ 00afdd48 bytes ec4df597
~~~


<a id="compare-458f022e3796a16f846474f416614c0a"></a>

### [`00afd94c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afd94c.md) → [`00afdd74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afd/00afdd74.md) FUN_00afdd74

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afd968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afd94c.md#insn-00afd968)
- 新版 `00afdd90`（命令位置の公開資料なし）

~~~diff
- 00afd968 ["INT_ADD", "register:40f0:8", ["const:afd968:8", "const:4:8"]]
- 00afd968 ["CALL", null, ["callee:008514f8:8"]]
+ 00afdd90 ["INT_ADD", "register:40f0:8", ["const:afdd90:8", "const:4:8"]]
+ 00afdd90 ["CALL", null, ["callee:008514f8:8"]]
- 00afd968 bytes d44ef597
+ 00afdd90 bytes da4df597
~~~


<a id="compare-ba3ae10fd55af017b2d83ff0afcb7543"></a>

### [`00afd998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afd998.md) → [`00afddc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afd/00afddc0.md) FUN_00afddc0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afd9ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afd998.md#insn-00afd9ac)
- 新版 `00afddd4`（命令位置の公開資料なし）

~~~diff
- 00afd9ac ["INT_ADD", "register:40f0:8", ["const:afd9ac:8", "const:4:8"]]
- 00afd9ac ["CALL", null, ["callee:008514f8:8"]]
+ 00afddd4 ["INT_ADD", "register:40f0:8", ["const:afddd4:8", "const:4:8"]]
+ 00afddd4 ["CALL", null, ["callee:008514f8:8"]]
- 00afd9ac bytes c34ef597
+ 00afddd4 bytes c94df597
~~~


<a id="compare-e59cbdb656dd51a59e606f3e2667c340"></a>

### [`00afd9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afd9d8.md) → [`00afde00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afd/00afde00.md) FUN_00afde00

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afd9f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afd9d8.md#insn-00afd9f4)
- 新版 `00afde1c`（命令位置の公開資料なし）

~~~diff
- 00afd9f4 ["INT_ADD", "register:40f0:8", ["const:afd9f4:8", "const:4:8"]]
- 00afd9f4 ["CALL", null, ["callee:008514f8:8"]]
+ 00afde1c ["INT_ADD", "register:40f0:8", ["const:afde1c:8", "const:4:8"]]
+ 00afde1c ["CALL", null, ["callee:008514f8:8"]]
- 00afd9f4 bytes b14ef597
+ 00afde1c bytes b74df597
~~~


<a id="compare-7500c1538c57a01ac20996b006c2f740"></a>

### [`00afda24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afda24.md) → [`00afde4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afd/00afde4c.md) FUN_00afde4c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afda38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afda24.md#insn-00afda38)
- 新版 `00afde60`（命令位置の公開資料なし）

~~~diff
- 00afda38 ["INT_ADD", "register:40f0:8", ["const:afda38:8", "const:4:8"]]
- 00afda38 ["CALL", null, ["callee:008514f8:8"]]
+ 00afde60 ["INT_ADD", "register:40f0:8", ["const:afde60:8", "const:4:8"]]
+ 00afde60 ["CALL", null, ["callee:008514f8:8"]]
- 00afda38 bytes a04ef597
+ 00afde60 bytes a64df597
~~~


<a id="compare-45c2a4166918d70ebfe6c738bbd2cbf7"></a>

### [`00afda64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afda64.md) → [`00afde8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afd/00afde8c.md) FUN_00afde8c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afda80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afda64.md#insn-00afda80)
- 新版 `00afdea8`（命令位置の公開資料なし）

~~~diff
- 00afda80 ["INT_ADD", "register:40f0:8", ["const:afda80:8", "const:4:8"]]
- 00afda80 ["CALL", null, ["callee:008514f8:8"]]
+ 00afdea8 ["INT_ADD", "register:40f0:8", ["const:afdea8:8", "const:4:8"]]
+ 00afdea8 ["CALL", null, ["callee:008514f8:8"]]
- 00afda80 bytes 8e4ef597
+ 00afdea8 bytes 944df597
~~~


<a id="compare-8b7f7f649761c8bc036806519f22c5ec"></a>

### [`00afdab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afdab0.md) → [`00afded8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afd/00afded8.md) FUN_00afded8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007154c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007154c0.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00715500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00715/00715500.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afdac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afdab0.md#insn-00afdac4)
- 新版 `00afdeec`（命令位置の公開資料なし）

~~~diff
- 00afdac4 ["INT_ADD", "register:40f0:8", ["const:afdac4:8", "const:4:8"]]
- 00afdac4 ["CALL", null, ["callee:008514f8:8"]]
+ 00afdeec ["INT_ADD", "register:40f0:8", ["const:afdeec:8", "const:4:8"]]
+ 00afdeec ["CALL", null, ["callee:008514f8:8"]]
- 00afdac4 bytes 7d4ef597
+ 00afdeec bytes 834df597
~~~


<a id="compare-d475304337588657d069e6660c1e8ec1"></a>

### [`00afdaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afdaf0.md) → [`00afdf18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afd/00afdf18.md) FUN_00afdf18

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afdb0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afdaf0.md#insn-00afdb0c)
- 新版 `00afdf34`（命令位置の公開資料なし）

~~~diff
- 00afdb0c ["INT_ADD", "register:40f0:8", ["const:afdb0c:8", "const:4:8"]]
- 00afdb0c ["CALL", null, ["callee:008514f8:8"]]
+ 00afdf34 ["INT_ADD", "register:40f0:8", ["const:afdf34:8", "const:4:8"]]
+ 00afdf34 ["CALL", null, ["callee:008514f8:8"]]
- 00afdb0c bytes 6b4ef597
+ 00afdf34 bytes 714df597
~~~


<a id="compare-5180e9e2ec88fe351034f94b42002cca"></a>

### [`00afdb3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afdb3c.md) → [`00afdf64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afd/00afdf64.md) FUN_00afdf64

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007154c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007154c0.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00715500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00715/00715500.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afdb50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afdb3c.md#insn-00afdb50)
- 新版 `00afdf78`（命令位置の公開資料なし）

~~~diff
- 00afdb50 ["INT_ADD", "register:40f0:8", ["const:afdb50:8", "const:4:8"]]
- 00afdb50 ["CALL", null, ["callee:008514f8:8"]]
+ 00afdf78 ["INT_ADD", "register:40f0:8", ["const:afdf78:8", "const:4:8"]]
+ 00afdf78 ["CALL", null, ["callee:008514f8:8"]]
- 00afdb50 bytes 5a4ef597
+ 00afdf78 bytes 604df597
~~~


<a id="compare-53292c5dfbfe1515a144723ba0a5e7de"></a>

### [`00afdb7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afdb7c.md) → [`00afdfa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afd/00afdfa4.md) FUN_00afdfa4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00a51dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a51/00a51dcc.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00a51fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a51/00a51fc4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afdb98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afdb7c.md#insn-00afdb98)
- 新版 `00afdfc0`（命令位置の公開資料なし）

~~~diff
- 00afdb98 ["INT_ADD", "register:40f0:8", ["const:afdb98:8", "const:4:8"]]
- 00afdb98 ["CALL", null, ["callee:008514f8:8"]]
+ 00afdfc0 ["INT_ADD", "register:40f0:8", ["const:afdfc0:8", "const:4:8"]]
+ 00afdfc0 ["CALL", null, ["callee:008514f8:8"]]
- 00afdb98 bytes 484ef597
+ 00afdfc0 bytes 4e4df597
~~~


<a id="compare-13106f2c45222ce4189ddeb39285f72a"></a>

### [`00afdbc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afdbc8.md) → [`00afdff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afd/00afdff0.md) FUN_00afdff0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afdbdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afdbc8.md#insn-00afdbdc)
- 新版 `00afe004`（命令位置の公開資料なし）

~~~diff
- 00afdbdc ["INT_ADD", "register:40f0:8", ["const:afdbdc:8", "const:4:8"]]
- 00afdbdc ["CALL", null, ["callee:008514f8:8"]]
+ 00afe004 ["INT_ADD", "register:40f0:8", ["const:afe004:8", "const:4:8"]]
+ 00afe004 ["CALL", null, ["callee:008514f8:8"]]
- 00afdbdc bytes 374ef597
+ 00afe004 bytes 3d4df597
~~~


<a id="compare-e6db4b1e38f041dd4e6fd31e42aa949a"></a>

### [`00afdc08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afdc08.md) → [`00afe030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afe030.md) FUN_00afe030

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afdc24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afdc08.md#insn-00afdc24)
- 新版 `00afe04c`（命令位置の公開資料なし）

~~~diff
- 00afdc24 ["INT_ADD", "register:40f0:8", ["const:afdc24:8", "const:4:8"]]
- 00afdc24 ["CALL", null, ["callee:008514f8:8"]]
+ 00afe04c ["INT_ADD", "register:40f0:8", ["const:afe04c:8", "const:4:8"]]
+ 00afe04c ["CALL", null, ["callee:008514f8:8"]]
- 00afdc24 bytes 254ef597
+ 00afe04c bytes 2b4df597
~~~


<a id="compare-f07d55ad8ca634182442e8f00da45135"></a>

### [`00afff54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aff/00afff54.md) → [`00b0037c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b0037c.md) FUN_00b0037c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005b068c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b068c.md) · 呼出先 4件 [`0046da7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da7c.md) [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 1件 [`005b06cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b06cc.md) · 呼出先 4件 [`0046dabc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046dabc.md) [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afff70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aff/00afff54.md#insn-00afff70) · [`00afff84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aff/00afff54.md#insn-00afff84) · [`00afff94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aff/00afff54.md#insn-00afff94)
- 新版 `00b00398`（命令位置の公開資料なし） · `00b003ac`（命令位置の公開資料なし） · `00b003bc`（命令位置の公開資料なし）

~~~diff
- 00afff70 ["INT_ADD", "register:40f0:8", ["const:afff70:8", "const:4:8"]]
- 00afff70 ["CALL", null, ["callee:008514f8:8"]]
+ 00b00398 ["INT_ADD", "register:40f0:8", ["const:b00398:8", "const:4:8"]]
+ 00b00398 ["CALL", null, ["callee:008514f8:8"]]
- 00afff70 bytes 5245f597
+ 00b00398 bytes 5844f597
- 00afff84 ["INT_ADD", "register:40f0:8", ["const:afff84:8", "const:4:8"]]
- 00afff84 ["CALL", null, ["callee:005e7420:8"]]
+ 00b003ac ["INT_ADD", "register:40f0:8", ["const:b003ac:8", "const:4:8"]]
+ 00b003ac ["CALL", null, ["callee:005e7420:8"]]
- 00afff84 bytes 179deb97
+ 00b003ac bytes 1d9ceb97
- 00afff94 ["INT_ADD", "register:40f0:8", ["const:afff94:8", "const:4:8"]]
- 00afff94 ["CALL", null, ["callee:008514f8:8"]]
+ 00b003bc ["INT_ADD", "register:40f0:8", ["const:b003bc:8", "const:4:8"]]
+ 00b003bc ["CALL", null, ["callee:008514f8:8"]]
- 00afff94 bytes 4945f597
+ 00b003bc bytes 4f44f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adb49a480a2117e57e3d50227f97ff71"></a>

### [`00b0110c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0110c.md) → [`00b01534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b01/00b01534.md) FUN_00b01534

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00685548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685548.md) [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md)
- 新版 呼出元 4件 [`00685588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685588.md) [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b01128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0110c.md#insn-00b01128) · [`00b0113c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0110c.md#insn-00b0113c) · [`00b0114c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0110c.md#insn-00b0114c)
- 新版 `00b01550`（命令位置の公開資料なし） · `00b01564`（命令位置の公開資料なし） · `00b01574`（命令位置の公開資料なし）

~~~diff
- 00b01128 ["INT_ADD", "register:40f0:8", ["const:b01128:8", "const:4:8"]]
- 00b01128 ["CALL", null, ["callee:008514f8:8"]]
+ 00b01550 ["INT_ADD", "register:40f0:8", ["const:b01550:8", "const:4:8"]]
+ 00b01550 ["CALL", null, ["callee:008514f8:8"]]
- 00b01128 bytes e440f597
+ 00b01550 bytes ea3ff597
- 00b0113c ["INT_ADD", "register:40f0:8", ["const:b0113c:8", "const:4:8"]]
- 00b0113c ["CALL", null, ["callee:005e7420:8"]]
+ 00b01564 ["INT_ADD", "register:40f0:8", ["const:b01564:8", "const:4:8"]]
+ 00b01564 ["CALL", null, ["callee:005e7420:8"]]
- 00b0113c bytes a998eb97
+ 00b01564 bytes af97eb97
- 00b0114c ["INT_ADD", "register:40f0:8", ["const:b0114c:8", "const:4:8"]]
- 00b0114c ["CALL", null, ["callee:008514f8:8"]]
+ 00b01574 ["INT_ADD", "register:40f0:8", ["const:b01574:8", "const:4:8"]]
+ 00b01574 ["CALL", null, ["callee:008514f8:8"]]
- 00b0114c bytes db40f597
+ 00b01574 bytes e13ff597
~~~


<a id="compare-2b593705344ea77dd831abf601d4c0d8"></a>

### [`00b011a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b011a4.md) → [`00b015cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b01/00b015cc.md) FUN_00b015cc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00685548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685548.md) [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md)
- 新版 呼出元 4件 [`00685588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685588.md) [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b011c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b011a4.md#insn-00b011c0) · [`00b011d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b011a4.md#insn-00b011d4) · [`00b011e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b011a4.md#insn-00b011e4)
- 新版 `00b015e8`（命令位置の公開資料なし） · `00b015fc`（命令位置の公開資料なし） · `00b0160c`（命令位置の公開資料なし）

~~~diff
- 00b011c0 ["INT_ADD", "register:40f0:8", ["const:b011c0:8", "const:4:8"]]
- 00b011c0 ["CALL", null, ["callee:008514f8:8"]]
+ 00b015e8 ["INT_ADD", "register:40f0:8", ["const:b015e8:8", "const:4:8"]]
+ 00b015e8 ["CALL", null, ["callee:008514f8:8"]]
- 00b011c0 bytes be40f597
+ 00b015e8 bytes c43ff597
- 00b011d4 ["INT_ADD", "register:40f0:8", ["const:b011d4:8", "const:4:8"]]
- 00b011d4 ["CALL", null, ["callee:005e7420:8"]]
+ 00b015fc ["INT_ADD", "register:40f0:8", ["const:b015fc:8", "const:4:8"]]
+ 00b015fc ["CALL", null, ["callee:005e7420:8"]]
- 00b011d4 bytes 8398eb97
+ 00b015fc bytes 8997eb97
- 00b011e4 ["INT_ADD", "register:40f0:8", ["const:b011e4:8", "const:4:8"]]
- 00b011e4 ["CALL", null, ["callee:008514f8:8"]]
+ 00b0160c ["INT_ADD", "register:40f0:8", ["const:b0160c:8", "const:4:8"]]
+ 00b0160c ["CALL", null, ["callee:008514f8:8"]]
- 00b011e4 bytes b540f597
+ 00b0160c bytes bb3ff597
~~~


<a id="compare-d78e83434c7ec55386b9e193c47c7104"></a>

### [`00b0123c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0123c.md) → [`00b01664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b01/00b01664.md) FUN_00b01664

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b01258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0123c.md#insn-00b01258) · [`00b0126c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0123c.md#insn-00b0126c) · [`00b0127c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0123c.md#insn-00b0127c)
- 新版 `00b01680`（命令位置の公開資料なし） · `00b01694`（命令位置の公開資料なし） · `00b016a4`（命令位置の公開資料なし）

~~~diff
- 00b01258 ["INT_ADD", "register:40f0:8", ["const:b01258:8", "const:4:8"]]
- 00b01258 ["CALL", null, ["callee:008514f8:8"]]
+ 00b01680 ["INT_ADD", "register:40f0:8", ["const:b01680:8", "const:4:8"]]
+ 00b01680 ["CALL", null, ["callee:008514f8:8"]]
- 00b01258 bytes 9840f597
+ 00b01680 bytes 9e3ff597
- 00b0126c ["INT_ADD", "register:40f0:8", ["const:b0126c:8", "const:4:8"]]
- 00b0126c ["CALL", null, ["callee:005e7420:8"]]
+ 00b01694 ["INT_ADD", "register:40f0:8", ["const:b01694:8", "const:4:8"]]
+ 00b01694 ["CALL", null, ["callee:005e7420:8"]]
- 00b0126c bytes 5d98eb97
+ 00b01694 bytes 6397eb97
- 00b0127c ["INT_ADD", "register:40f0:8", ["const:b0127c:8", "const:4:8"]]
- 00b0127c ["CALL", null, ["callee:008514f8:8"]]
+ 00b016a4 ["INT_ADD", "register:40f0:8", ["const:b016a4:8", "const:4:8"]]
+ 00b016a4 ["CALL", null, ["callee:008514f8:8"]]
- 00b0127c bytes 8f40f597
+ 00b016a4 bytes 953ff597
~~~


<a id="compare-ca90d434b1149ee6aace6a3150d6c5f0"></a>

### [`00b02128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02128.md) → [`00b02550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02550.md) FUN_00b02550

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b02144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02128.md#insn-00b02144) · [`00b02158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02128.md#insn-00b02158) · [`00b02168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02128.md#insn-00b02168)
- 新版 `00b0256c`（命令位置の公開資料なし） · `00b02580`（命令位置の公開資料なし） · `00b02590`（命令位置の公開資料なし）

~~~diff
- 00b02144 ["INT_ADD", "register:40f0:8", ["const:b02144:8", "const:4:8"]]
- 00b02144 ["CALL", null, ["callee:008514f8:8"]]
+ 00b0256c ["INT_ADD", "register:40f0:8", ["const:b0256c:8", "const:4:8"]]
+ 00b0256c ["CALL", null, ["callee:008514f8:8"]]
- 00b02144 bytes dd3cf597
+ 00b0256c bytes e33bf597
- 00b02158 ["INT_ADD", "register:40f0:8", ["const:b02158:8", "const:4:8"]]
- 00b02158 ["CALL", null, ["callee:005e7420:8"]]
+ 00b02580 ["INT_ADD", "register:40f0:8", ["const:b02580:8", "const:4:8"]]
+ 00b02580 ["CALL", null, ["callee:005e7420:8"]]
- 00b02158 bytes a294eb97
+ 00b02580 bytes a893eb97
- 00b02168 ["INT_ADD", "register:40f0:8", ["const:b02168:8", "const:4:8"]]
- 00b02168 ["CALL", null, ["callee:008514f8:8"]]
+ 00b02590 ["INT_ADD", "register:40f0:8", ["const:b02590:8", "const:4:8"]]
+ 00b02590 ["CALL", null, ["callee:008514f8:8"]]
- 00b02168 bytes d43cf597
+ 00b02590 bytes da3bf597
~~~


<a id="compare-d870d03fe4f19a02b0c3333391ebc197"></a>

### [`00b034e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b034e8.md) → [`00b03910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03910.md) FUN_00b03910

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`006cb190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cb/006cb190.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md)
- 新版 呼出元 4件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`006cb1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006cb/006cb1d0.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b03504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b034e8.md#insn-00b03504) · [`00b03518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b034e8.md#insn-00b03518) · [`00b03528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b034e8.md#insn-00b03528)
- 新版 `00b0392c`（命令位置の公開資料なし） · `00b03940`（命令位置の公開資料なし） · `00b03950`（命令位置の公開資料なし）

~~~diff
- 00b03504 ["INT_ADD", "register:40f0:8", ["const:b03504:8", "const:4:8"]]
- 00b03504 ["CALL", null, ["callee:008514f8:8"]]
+ 00b0392c ["INT_ADD", "register:40f0:8", ["const:b0392c:8", "const:4:8"]]
+ 00b0392c ["CALL", null, ["callee:008514f8:8"]]
- 00b03504 bytes ed37f597
+ 00b0392c bytes f336f597
- 00b03518 ["INT_ADD", "register:40f0:8", ["const:b03518:8", "const:4:8"]]
- 00b03518 ["CALL", null, ["callee:005e7420:8"]]
+ 00b03940 ["INT_ADD", "register:40f0:8", ["const:b03940:8", "const:4:8"]]
+ 00b03940 ["CALL", null, ["callee:005e7420:8"]]
- 00b03518 bytes b28feb97
+ 00b03940 bytes b88eeb97
- 00b03528 ["INT_ADD", "register:40f0:8", ["const:b03528:8", "const:4:8"]]
- 00b03528 ["CALL", null, ["callee:008514f8:8"]]
+ 00b03950 ["INT_ADD", "register:40f0:8", ["const:b03950:8", "const:4:8"]]
+ 00b03950 ["CALL", null, ["callee:008514f8:8"]]
- 00b03528 bytes e437f597
+ 00b03950 bytes ea36f597
~~~


<a id="compare-269ac6dd722a520da5309818d48ab1cf"></a>

### [`00b037f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b037f0.md) → [`00b03c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03c18.md) FUN_00b03c18

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0380c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b037f0.md#insn-00b0380c) · [`00b03820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b037f0.md#insn-00b03820) · [`00b03830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b037f0.md#insn-00b03830)
- 新版 `00b03c34`（命令位置の公開資料なし） · `00b03c48`（命令位置の公開資料なし） · `00b03c58`（命令位置の公開資料なし）

~~~diff
- 00b0380c ["INT_ADD", "register:40f0:8", ["const:b0380c:8", "const:4:8"]]
- 00b0380c ["CALL", null, ["callee:008514f8:8"]]
+ 00b03c34 ["INT_ADD", "register:40f0:8", ["const:b03c34:8", "const:4:8"]]
+ 00b03c34 ["CALL", null, ["callee:008514f8:8"]]
- 00b0380c bytes 2b37f597
+ 00b03c34 bytes 3136f597
- 00b03820 ["INT_ADD", "register:40f0:8", ["const:b03820:8", "const:4:8"]]
- 00b03820 ["CALL", null, ["callee:005e7420:8"]]
+ 00b03c48 ["INT_ADD", "register:40f0:8", ["const:b03c48:8", "const:4:8"]]
+ 00b03c48 ["CALL", null, ["callee:005e7420:8"]]
- 00b03820 bytes f08eeb97
+ 00b03c48 bytes f68deb97
- 00b03830 ["INT_ADD", "register:40f0:8", ["const:b03830:8", "const:4:8"]]
- 00b03830 ["CALL", null, ["callee:008514f8:8"]]
+ 00b03c58 ["INT_ADD", "register:40f0:8", ["const:b03c58:8", "const:4:8"]]
+ 00b03c58 ["CALL", null, ["callee:008514f8:8"]]
- 00b03830 bytes 2237f597
+ 00b03c58 bytes 2836f597
~~~


<a id="compare-6d9eeb85cfcd6eb6127eb25805bae797"></a>

### [`00b03888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03888.md) → [`00b03cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03cb0.md) FUN_00b03cb0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b038a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03888.md#insn-00b038a4) · [`00b038b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03888.md#insn-00b038b8) · [`00b038c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03888.md#insn-00b038c8)
- 新版 `00b03ccc`（命令位置の公開資料なし） · `00b03ce0`（命令位置の公開資料なし） · `00b03cf0`（命令位置の公開資料なし）

~~~diff
- 00b038a4 ["INT_ADD", "register:40f0:8", ["const:b038a4:8", "const:4:8"]]
- 00b038a4 ["CALL", null, ["callee:008514f8:8"]]
+ 00b03ccc ["INT_ADD", "register:40f0:8", ["const:b03ccc:8", "const:4:8"]]
+ 00b03ccc ["CALL", null, ["callee:008514f8:8"]]
- 00b038a4 bytes 0537f597
+ 00b03ccc bytes 0b36f597
- 00b038b8 ["INT_ADD", "register:40f0:8", ["const:b038b8:8", "const:4:8"]]
- 00b038b8 ["CALL", null, ["callee:005e7420:8"]]
+ 00b03ce0 ["INT_ADD", "register:40f0:8", ["const:b03ce0:8", "const:4:8"]]
+ 00b03ce0 ["CALL", null, ["callee:005e7420:8"]]
- 00b038b8 bytes ca8eeb97
+ 00b03ce0 bytes d08deb97
- 00b038c8 ["INT_ADD", "register:40f0:8", ["const:b038c8:8", "const:4:8"]]
- 00b038c8 ["CALL", null, ["callee:008514f8:8"]]
+ 00b03cf0 ["INT_ADD", "register:40f0:8", ["const:b03cf0:8", "const:4:8"]]
+ 00b03cf0 ["CALL", null, ["callee:008514f8:8"]]
- 00b038c8 bytes fc36f597
+ 00b03cf0 bytes 0236f597
~~~


<a id="compare-84cced398e637b42d3cf8fe6256bd9ad"></a>

### [`00b060dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b060dc.md) → [`00b06504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b06504.md) FUN_00b06504

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b060f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b060dc.md#insn-00b060f8) · [`00b0610c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b060dc.md#insn-00b0610c) · [`00b0611c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b060dc.md#insn-00b0611c)
- 新版 `00b06520`（命令位置の公開資料なし） · `00b06534`（命令位置の公開資料なし） · `00b06544`（命令位置の公開資料なし）

~~~diff
- 00b060f8 ["INT_ADD", "register:40f0:8", ["const:b060f8:8", "const:4:8"]]
- 00b060f8 ["CALL", null, ["callee:008514f8:8"]]
+ 00b06520 ["INT_ADD", "register:40f0:8", ["const:b06520:8", "const:4:8"]]
+ 00b06520 ["CALL", null, ["callee:008514f8:8"]]
- 00b060f8 bytes f02cf597
+ 00b06520 bytes f62bf597
- 00b0610c ["INT_ADD", "register:40f0:8", ["const:b0610c:8", "const:4:8"]]
- 00b0610c ["CALL", null, ["callee:005e7420:8"]]
+ 00b06534 ["INT_ADD", "register:40f0:8", ["const:b06534:8", "const:4:8"]]
+ 00b06534 ["CALL", null, ["callee:005e7420:8"]]
- 00b0610c bytes b584eb97
+ 00b06534 bytes bb83eb97
- 00b0611c ["INT_ADD", "register:40f0:8", ["const:b0611c:8", "const:4:8"]]
- 00b0611c ["CALL", null, ["callee:008514f8:8"]]
+ 00b06544 ["INT_ADD", "register:40f0:8", ["const:b06544:8", "const:4:8"]]
+ 00b06544 ["CALL", null, ["callee:008514f8:8"]]
- 00b0611c bytes e72cf597
+ 00b06544 bytes ed2bf597
~~~


<a id="compare-e0aa4f34be7685b17bf35e38a4e92d38"></a>

### [`00b06154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06154.md) → [`00b0657c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b0657c.md) FUN_00b0657c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b06170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06154.md#insn-00b06170) · [`00b06184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06154.md#insn-00b06184) · [`00b06194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06154.md#insn-00b06194)
- 新版 `00b06598`（命令位置の公開資料なし） · `00b065ac`（命令位置の公開資料なし） · `00b065bc`（命令位置の公開資料なし）

~~~diff
- 00b06170 ["INT_ADD", "register:40f0:8", ["const:b06170:8", "const:4:8"]]
- 00b06170 ["CALL", null, ["callee:008514f8:8"]]
+ 00b06598 ["INT_ADD", "register:40f0:8", ["const:b06598:8", "const:4:8"]]
+ 00b06598 ["CALL", null, ["callee:008514f8:8"]]
- 00b06170 bytes d22cf597
+ 00b06598 bytes d82bf597
- 00b06184 ["INT_ADD", "register:40f0:8", ["const:b06184:8", "const:4:8"]]
- 00b06184 ["CALL", null, ["callee:005e7420:8"]]
+ 00b065ac ["INT_ADD", "register:40f0:8", ["const:b065ac:8", "const:4:8"]]
+ 00b065ac ["CALL", null, ["callee:005e7420:8"]]
- 00b06184 bytes 9784eb97
+ 00b065ac bytes 9d83eb97
- 00b06194 ["INT_ADD", "register:40f0:8", ["const:b06194:8", "const:4:8"]]
- 00b06194 ["CALL", null, ["callee:008514f8:8"]]
+ 00b065bc ["INT_ADD", "register:40f0:8", ["const:b065bc:8", "const:4:8"]]
+ 00b065bc ["CALL", null, ["callee:008514f8:8"]]
- 00b06194 bytes c92cf597
+ 00b065bc bytes cf2bf597
~~~


<a id="compare-74a9d0de640fbc882a7fef0749e78c5f"></a>

### [`00b06460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06460.md) → [`00b06888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b06888.md) FUN_00b06888

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b04854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04854.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 1件 [`00b04c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04c7c.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b064c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06460.md#insn-00b064c8) · [`00b064e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06460.md#insn-00b064e0) · [`00b0650c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06460.md#insn-00b0650c)
- 新版 `00b068f0`（命令位置の公開資料なし） · `00b06908`（命令位置の公開資料なし） · `00b06934`（命令位置の公開資料なし）

~~~diff
- 00b064c8 ["INT_ADD", "register:40f0:8", ["const:b064c8:8", "const:4:8"]]
- 00b064c8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b068f0 ["INT_ADD", "register:40f0:8", ["const:b068f0:8", "const:4:8"]]
+ 00b068f0 ["CALL", null, ["callee:00c57e90:8"]]
- 00b064c8 bytes 72450594
+ 00b068f0 bytes 68450594
- 00b064e0 ["INT_ADD", "register:40f0:8", ["const:b064e0:8", "const:4:8"]]
- 00b064e0 ["CALL", null, ["callee:00c58090:8"]]
+ 00b06908 ["INT_ADD", "register:40f0:8", ["const:b06908:8", "const:4:8"]]
+ 00b06908 ["CALL", null, ["callee:00c58090:8"]]
- 00b064e0 bytes ec450594
+ 00b06908 bytes e2450594
- 00b0650c ["INT_ADD", "register:40f0:8", ["const:b0650c:8", "const:4:8"]]
- 00b0650c ["CALL", null, ["callee:0043bba4:8"]]
+ 00b06934 ["INT_ADD", "register:40f0:8", ["const:b06934:8", "const:4:8"]]
+ 00b06934 ["CALL", null, ["callee:0043bba4:8"]]
- 00b0650c bytes 96d5e497
+ 00b06934 bytes 9cd4e497
~~~


<a id="compare-24abf370a4e907bbcfcdfc3898bb1b6a"></a>

### [`00b06ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06ca8.md) → [`00b070d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b070d0.md) FUN_00b070d0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b04854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04854.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00b06fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06fc4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00b04c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04c7c.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00b073ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b073ec.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b06cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06ca8.md#insn-00b06cf4) · [`00b06d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06ca8.md#insn-00b06d24) · [`00b06d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06ca8.md#insn-00b06d38)
- 新版 `00b0711c`（命令位置の公開資料なし） · `00b0714c`（命令位置の公開資料なし） · `00b07160`（命令位置の公開資料なし）

~~~diff
- 00b06cf4 ["INT_ADD", "register:40f0:8", ["const:b06cf4:8", "const:4:8"]]
- 00b06cf4 ["CALL", null, ["callee:0043bba4:8"]]
+ 00b0711c ["INT_ADD", "register:40f0:8", ["const:b0711c:8", "const:4:8"]]
+ 00b0711c ["CALL", null, ["callee:0043bba4:8"]]
- 00b06cf4 bytes 9cd3e497
+ 00b0711c bytes a2d2e497
- 00b06d24 ["INT_ADD", "register:40f0:8", ["const:b06d24:8", "const:4:8"]]
- 00b06d24 ["CALL", null, ["callee:00b073ec:8"]]
+ 00b0714c ["INT_ADD", "register:40f0:8", ["const:b0714c:8", "const:4:8"]]
+ 00b0714c ["CALL", null, ["callee:00b073ec:8"]]
- 00b06d24 bytes a8000094
+ 00b0714c bytes a8000094
- 00b06d38 ["INT_ADD", "register:40f0:8", ["const:b06d38:8", "const:4:8"]]
- 00b06d38 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b07160 ["INT_ADD", "register:40f0:8", ["const:b07160:8", "const:4:8"]]
+ 00b07160 ["CALL", null, ["callee:00c57e90:8"]]
- 00b06d38 bytes 56430594
+ 00b07160 bytes 4c430594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c92d5f0bf84ace6046b46b097b535bc"></a>

### [`00b0716c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b07/00b0716c.md) → [`00b07594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b07594.md) FUN_00b07594

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b04854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04854.md) [`00b0716c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b07/00b0716c.md) · 呼出先 2件 [`00b0716c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b07/00b0716c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00b04c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04c7c.md) [`00b07594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b07594.md) · 呼出先 2件 [`00b07594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b07594.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0718c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b07/00b0716c.md#insn-00b0718c) · [`00b07198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b07/00b0716c.md#insn-00b07198)
- 新版 `00b075b4`（命令位置の公開資料なし） · `00b075c0`（命令位置の公開資料なし）

~~~diff
- 00b0718c ["INT_ADD", "register:40f0:8", ["const:b0718c:8", "const:4:8"]]
- 00b0718c ["CALL", null, ["local:b0:8"]]
+ 00b075b4 ["INT_ADD", "register:40f0:8", ["const:b075b4:8", "const:4:8"]]
+ 00b075b4 ["CALL", null, ["local:b0:8"]]
- 00b0718c bytes f8ffff97
+ 00b075b4 bytes f8ffff97
- 00b07198 ["INT_ADD", "register:40f0:8", ["const:b07198:8", "const:4:8"]]
- 00b07198 ["CALL", null, ["local:b0:8"]]
+ 00b075c0 ["INT_ADD", "register:40f0:8", ["const:b075c0:8", "const:4:8"]]
+ 00b075c0 ["CALL", null, ["local:b0:8"]]
- 00b07198 bytes f5ffff97
+ 00b075c0 bytes f5ffff97
~~~


<a id="compare-6181a4dbc19284350a8955c2536fad5b"></a>

### [`00b07540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b07/00b07540.md) → [`00b07968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b07968.md) FUN_00b07968

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b07558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b07/00b07540.md#insn-00b07558) · [`00b07564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b07/00b07540.md#insn-00b07564) · [`00b07570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b07/00b07540.md#insn-00b07570)
- 新版 `00b07980`（命令位置の公開資料なし） · `00b0798c`（命令位置の公開資料なし） · `00b07998`（命令位置の公開資料なし）

~~~diff
- 00b07558 ["INT_ADD", "register:40f0:8", ["const:b07558:8", "const:4:8"]]
- 00b07558 ["CALL", null, ["callee:005c179c:8"]]
+ 00b07980 ["INT_ADD", "register:40f0:8", ["const:b07980:8", "const:4:8"]]
+ 00b07980 ["CALL", null, ["callee:005c179c:8"]]
- 00b07558 bytes 81e8ea97
+ 00b07980 bytes 87e7ea97
- 00b07564 ["INT_ADD", "register:40f0:8", ["const:b07564:8", "const:4:8"]]
- 00b07564 ["CALL", null, ["callee:008514f8:8"]]
+ 00b0798c ["INT_ADD", "register:40f0:8", ["const:b0798c:8", "const:4:8"]]
+ 00b0798c ["CALL", null, ["callee:008514f8:8"]]
- 00b07564 bytes d527f597
+ 00b0798c bytes db26f597
- 00b07570 ["INT_ADD", "register:40f0:8", ["const:b07570:8", "const:4:8"]]
- 00b07570 ["CALL", null, ["callee:008514f8:8"]]
+ 00b07998 ["INT_ADD", "register:40f0:8", ["const:b07998:8", "const:4:8"]]
+ 00b07998 ["CALL", null, ["callee:008514f8:8"]]
- 00b07570 bytes d227f597
+ 00b07998 bytes d826f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee3ddd0d8564debeb22e2159bfcc8fff"></a>

### [`00b088f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b08/00b088f4.md) → [`00b08d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b08/00b08d1c.md) FUN_00b08d1c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b08918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b08/00b088f4.md#insn-00b08918) · [`00b08928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b08/00b088f4.md#insn-00b08928)
- 新版 `00b08d40`（命令位置の公開資料なし） · `00b08d50`（命令位置の公開資料なし）

~~~diff
- 00b08918 ["INT_ADD", "register:40f0:8", ["const:b08918:8", "const:4:8"]]
- 00b08918 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b08d40 ["INT_ADD", "register:40f0:8", ["const:b08d40:8", "const:4:8"]]
+ 00b08d40 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b08918 bytes 663c0594
+ 00b08d40 bytes 5c3c0594
- 00b08928 ["INT_ADD", "register:40f0:8", ["const:b08928:8", "const:4:8"]]
- 00b08928 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b08d50 ["INT_ADD", "register:40f0:8", ["const:b08d50:8", "const:4:8"]]
+ 00b08d50 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b08928 bytes 623c0594
+ 00b08d50 bytes 583c0594
~~~


<a id="compare-9a80a60330e90d587d590d837b7b2d51"></a>

### [`00b08948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b08/00b08948.md) → [`00b08d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b08/00b08d70.md) FUN_00b08d70

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) [`00b3d1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3d/00b3d1f0.md) · 呼出先 7件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b08cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b08/00b08cf4.md)
- 新版 呼出元 2件 [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) [`00b3d618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3d/00b3d618.md) · 呼出先 7件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0911c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b0911c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b08974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b08/00b08948.md#insn-00b08974) · [`00b08984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b08/00b08948.md#insn-00b08984) · [`00b08990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b08/00b08948.md#insn-00b08990)
- 新版 `00b08d9c`（命令位置の公開資料なし） · `00b08dac`（命令位置の公開資料なし） · `00b08db8`（命令位置の公開資料なし）

~~~diff
- 00b08974 ["INT_ADD", "register:40f0:8", ["const:b08974:8", "const:4:8"]]
- 00b08974 ["CALL", null, ["callee:005c179c:8"]]
+ 00b08d9c ["INT_ADD", "register:40f0:8", ["const:b08d9c:8", "const:4:8"]]
+ 00b08d9c ["CALL", null, ["callee:005c179c:8"]]
- 00b08974 bytes 7ae3ea97
+ 00b08d9c bytes 80e2ea97
- 00b08984 ["INT_ADD", "register:40f0:8", ["const:b08984:8", "const:4:8"]]
- 00b08984 ["CALL", null, ["callee:008514f8:8"]]
+ 00b08dac ["INT_ADD", "register:40f0:8", ["const:b08dac:8", "const:4:8"]]
+ 00b08dac ["CALL", null, ["callee:008514f8:8"]]
- 00b08984 bytes cd22f597
+ 00b08dac bytes d321f597
- 00b08990 ["INT_ADD", "register:40f0:8", ["const:b08990:8", "const:4:8"]]
- 00b08990 ["CALL", null, ["callee:008514f8:8"]]
+ 00b08db8 ["INT_ADD", "register:40f0:8", ["const:b08db8:8", "const:4:8"]]
+ 00b08db8 ["CALL", null, ["callee:008514f8:8"]]
- 00b08990 bytes ca22f597
+ 00b08db8 bytes d021f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a924928f161c2a97daf8290298d03017"></a>

### [`00b08cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b08/00b08cf4.md) → [`00b0911c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b0911c.md) FUN_00b0911c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b08948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b08/00b08948.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00b08d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b08/00b08d70.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b08d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b08/00b08cf4.md#insn-00b08d1c) · [`00b08d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b08/00b08cf4.md#insn-00b08d34) · [`00b08d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b08/00b08cf4.md#insn-00b08d4c)
- 新版 `00b09144`（命令位置の公開資料なし） · `00b0915c`（命令位置の公開資料なし） · `00b09174`（命令位置の公開資料なし）

~~~diff
- 00b08d1c ["INT_ADD", "register:40f0:8", ["const:b08d1c:8", "const:4:8"]]
- 00b08d1c ["CALL", null, ["callee:008514f8:8"]]
+ 00b09144 ["INT_ADD", "register:40f0:8", ["const:b09144:8", "const:4:8"]]
+ 00b09144 ["CALL", null, ["callee:008514f8:8"]]
- 00b08d1c bytes e721f597
+ 00b09144 bytes ed20f597
- 00b08d34 ["INT_ADD", "register:40f0:8", ["const:b08d34:8", "const:4:8"]]
- 00b08d34 ["CALL", null, ["callee:008514f8:8"]]
+ 00b0915c ["INT_ADD", "register:40f0:8", ["const:b0915c:8", "const:4:8"]]
+ 00b0915c ["CALL", null, ["callee:008514f8:8"]]
- 00b08d34 bytes e121f597
+ 00b0915c bytes e720f597
- 00b08d4c ["INT_ADD", "register:40f0:8", ["const:b08d4c:8", "const:4:8"]]
- 00b08d4c ["CALL", null, ["callee:008514f8:8"]]
+ 00b09174 ["INT_ADD", "register:40f0:8", ["const:b09174:8", "const:4:8"]]
+ 00b09174 ["CALL", null, ["callee:008514f8:8"]]
- 00b08d4c bytes db21f597
+ 00b09174 bytes e120f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-497c44bedc614ba78625f54a1b08d565"></a>

### [`00b091dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b091dc.md) → [`00b09604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09604.md) FUN_00b09604

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · 呼出先 2件 [`0086a764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a764.md) [`0086a7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a7f8.md)
- 新版 呼出元 1件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) · 呼出先 2件 [`0086a7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a7a4.md) [`0086a838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a838.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b091f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b091dc.md#insn-00b091f8) · [`00b09214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b091dc.md#insn-00b09214)
- 新版 `00b09620`（命令位置の公開資料なし） · `00b0963c`（命令位置の公開資料なし）

~~~diff
- 00b091f8 ["INT_ADD", "register:40f0:8", ["const:b091f8:8", "const:4:8"]]
- 00b091f8 ["CALL", null, ["callee:0086a838:8"]]
+ 00b09620 ["INT_ADD", "register:40f0:8", ["const:b09620:8", "const:4:8"]]
+ 00b09620 ["CALL", null, ["callee:0086a838:8"]]
- 00b091f8 bytes 8085f597
+ 00b09620 bytes 8684f597
- 00b09214 ["INT_ADD", "register:40f0:8", ["const:b09214:8", "const:4:8"]]
- 00b09214 ["CALL", null, ["callee:0086a7a4:8"]]
+ 00b0963c ["INT_ADD", "register:40f0:8", ["const:b0963c:8", "const:4:8"]]
+ 00b0963c ["CALL", null, ["callee:0086a7a4:8"]]
- 00b09214 bytes 5485f597
+ 00b0963c bytes 5a84f597
~~~


<a id="compare-625b13d9b84e32bcc4211e8b23051781"></a>

### [`00b092e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b092e0.md) → [`00b09708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09708.md) FUN_00b09708

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 14件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004800d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004800d8.md) [`00480138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480138.md) [`00480198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480198.md)
- 新版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 14件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00480118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480118.md) [`00480178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md) [`004801d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004801d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b09314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b092e0.md#insn-00b09314) · [`00b09330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b092e0.md#insn-00b09330) · [`00b0934c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b092e0.md#insn-00b0934c)
- 新版 `00b0973c`（命令位置の公開資料なし） · `00b09758`（命令位置の公開資料なし） · `00b09774`（命令位置の公開資料なし）

~~~diff
- 00b09314 ["INT_ADD", "register:40f0:8", ["const:b09314:8", "const:4:8"]]
- 00b09314 ["CALL", null, ["callee:0086a838:8"]]
+ 00b0973c ["INT_ADD", "register:40f0:8", ["const:b0973c:8", "const:4:8"]]
+ 00b0973c ["CALL", null, ["callee:0086a838:8"]]
- 00b09314 bytes 3985f597
+ 00b0973c bytes 3f84f597
- 00b09330 ["INT_ADD", "register:40f0:8", ["const:b09330:8", "const:4:8"]]
- 00b09330 ["CALL", null, ["callee:0086a7a4:8"]]
+ 00b09758 ["INT_ADD", "register:40f0:8", ["const:b09758:8", "const:4:8"]]
+ 00b09758 ["CALL", null, ["callee:0086a7a4:8"]]
- 00b09330 bytes 0d85f597
+ 00b09758 bytes 1384f597
- 00b0934c ["INT_ADD", "register:40f0:8", ["const:b0934c:8", "const:4:8"]]
- 00b0934c ["CALL", null, ["callee:00480178:8"]]
+ 00b09774 ["INT_ADD", "register:40f0:8", ["const:b09774:8", "const:4:8"]]
+ 00b09774 ["CALL", null, ["callee:00480178:8"]]
- 00b0934c bytes 7bdbe597
+ 00b09774 bytes 81dae597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0660af40e77ccd21395ee912db38b294"></a>

### [`00b09a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b09a84.md) → [`00b09eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09eac.md) FUN_00b09eac

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 3件 [`00480af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480af8.md) [`00480b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480b50.md) [`00480ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ba8.md)
- 新版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 3件 [`00480b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md) [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md) [`00480be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b09ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b09a84.md#insn-00b09ab0) · [`00b09acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b09a84.md#insn-00b09acc) · [`00b09b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b09a84.md#insn-00b09b00)
- 新版 `00b09ed8`（命令位置の公開資料なし） · `00b09ef4`（命令位置の公開資料なし） · `00b09f28`（命令位置の公開資料なし）

~~~diff
- 00b09ab0 ["INT_ADD", "register:40f0:8", ["const:b09ab0:8", "const:4:8"]]
- 00b09ab0 ["CALL", null, ["callee:00480b90:8"]]
+ 00b09ed8 ["INT_ADD", "register:40f0:8", ["const:b09ed8:8", "const:4:8"]]
+ 00b09ed8 ["CALL", null, ["callee:00480b90:8"]]
- 00b09ab0 bytes 28dce597
+ 00b09ed8 bytes 2edbe597
- 00b09acc ["INT_ADD", "register:40f0:8", ["const:b09acc:8", "const:4:8"]]
- 00b09acc ["CALL", null, ["callee:00480b90:8"]]
+ 00b09ef4 ["INT_ADD", "register:40f0:8", ["const:b09ef4:8", "const:4:8"]]
+ 00b09ef4 ["CALL", null, ["callee:00480b90:8"]]
- 00b09acc bytes 21dce597
+ 00b09ef4 bytes 27dbe597
- 00b09b00 ["INT_ADD", "register:40f0:8", ["const:b09b00:8", "const:4:8"]]
- 00b09b00 ["CALL", null, ["callee:00480be8:8"]]
+ 00b09f28 ["INT_ADD", "register:40f0:8", ["const:b09f28:8", "const:4:8"]]
+ 00b09f28 ["CALL", null, ["callee:00480be8:8"]]
- 00b09b00 bytes 2adce597
+ 00b09f28 bytes 30dbe597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa39c6f172bf034ac1194c32d37f9ebf"></a>

### [`00b0a190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0a190.md) → [`00b0a5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0a5b8.md) FUN_00b0a5b8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00b09c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b09c60.md) [`00b0a930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0a930.md) [`00b0be2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0be2c.md) · 呼出先 9件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00802b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b18.md) [`00802c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802c68.md)
- 新版 呼出元 3件 [`00b0a088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0a088.md) [`00b0ad58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0ad58.md) [`00b0c254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0c254.md) · 呼出先 9件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0a1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0a190.md#insn-00b0a1c0) · [`00b0a1c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0a190.md#insn-00b0a1c8) · [`00b0a1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0a190.md#insn-00b0a1d0)
- 新版 `00b0a5e8`（命令位置の公開資料なし） · `00b0a5f0`（命令位置の公開資料なし） · `00b0a5f8`（命令位置の公開資料なし）

~~~diff
- 00b0a1c0 ["INT_ADD", "register:40f0:8", ["const:b0a1c0:8", "const:4:8"]]
- 00b0a1c0 ["CALL", null, ["callee:00802b58:8"]]
+ 00b0a5e8 ["INT_ADD", "register:40f0:8", ["const:b0a5e8:8", "const:4:8"]]
+ 00b0a5e8 ["CALL", null, ["callee:00802b58:8"]]
- 00b0a1c0 bytes 56e2f397
+ 00b0a5e8 bytes 5ce1f397
- 00b0a1c8 ["INT_ADD", "register:40f0:8", ["const:b0a1c8:8", "const:4:8"]]
- 00b0a1c8 ["CALL", null, ["callee:00802ca8:8"]]
+ 00b0a5f0 ["INT_ADD", "register:40f0:8", ["const:b0a5f0:8", "const:4:8"]]
+ 00b0a5f0 ["CALL", null, ["callee:00802ca8:8"]]
- 00b0a1c8 bytes a8e2f397
+ 00b0a5f0 bytes aee1f397
- 00b0a1d0 ["INT_ADD", "register:40f0:8", ["const:b0a1d0:8", "const:4:8"]]
- 00b0a1d0 ["CALL", null, ["callee:00802ee0:8"]]
+ 00b0a5f8 ["INT_ADD", "register:40f0:8", ["const:b0a5f8:8", "const:4:8"]]
+ 00b0a5f8 ["CALL", null, ["callee:00802ee0:8"]]
- 00b0a1d0 bytes 34e3f397
+ 00b0a5f8 bytes 3ae2f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f3ded0b6b1f618b23f731e225d464ac"></a>

### [`00b0a3cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0a3cc.md) → [`00b0a7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0a7f4.md) FUN_00b0a7f4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00ae0740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0740.md) [`00aed350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed350.md) · 呼出先 13件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006623ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/006623ac.md) [`00662450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/00662450.md) [`006624f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/006624f4.md)
- 新版 呼出元 2件 [`00ae0b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae0/00ae0b68.md) [`00aed778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aed/00aed778.md) · 呼出先 13件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`006623ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/006623ec.md) [`00662490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/00662490.md) [`00662534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/00662534.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0a3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0a3cc.md#insn-00b0a3fc) · [`00b0a404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0a3cc.md#insn-00b0a404) · [`00b0a408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0a3cc.md#insn-00b0a408)
- 新版 `00b0a824`（命令位置の公開資料なし） · `00b0a82c`（命令位置の公開資料なし） · `00b0a830`（命令位置の公開資料なし）

~~~diff
- 00b0a3fc ["INT_ADD", "register:40f0:8", ["const:b0a3fc:8", "const:4:8"]]
- 00b0a3fc ["CALL", null, ["callee:00802b58:8"]]
+ 00b0a824 ["INT_ADD", "register:40f0:8", ["const:b0a824:8", "const:4:8"]]
+ 00b0a824 ["CALL", null, ["callee:00802b58:8"]]
- 00b0a3fc bytes c7e1f397
+ 00b0a824 bytes cde0f397
- 00b0a404 ["INT_ADD", "register:40f0:8", ["const:b0a404:8", "const:4:8"]]
- 00b0a404 ["CALL", null, ["callee:00802ca8:8"]]
+ 00b0a82c ["INT_ADD", "register:40f0:8", ["const:b0a82c:8", "const:4:8"]]
+ 00b0a82c ["CALL", null, ["callee:00802ca8:8"]]
- 00b0a404 bytes 19e2f397
+ 00b0a82c bytes 1fe1f397
- 00b0a408 ["INT_ADD", "register:40f0:8", ["const:b0a408:8", "const:4:8"]]
- 00b0a408 ["CALL", null, ["callee:00802ee0:8"]]
+ 00b0a830 ["INT_ADD", "register:40f0:8", ["const:b0a830:8", "const:4:8"]]
+ 00b0a830 ["CALL", null, ["callee:00802ee0:8"]]
- 00b0a408 bytes a6e2f397
+ 00b0a830 bytes ace1f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22db221f9d37805f9531f7c161a60a4f"></a>

### [`00b0a8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0a8ec.md) → [`00b0ad14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0ad14.md) FUN_00b0ad14

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`00ad075c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad075c.md) [`00ad688c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad688c.md) [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) [`00adee94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ade/00adee94.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)
- 新版 呼出元 8件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`00ad0958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad0/00ad0958.md) [`00ad6a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6a88.md) [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) [`00adf090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00adf/00adf090.md) · 呼出先 1件 [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0a90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0a8ec.md#insn-00b0a90c)
- 新版 `00b0ad34`（命令位置の公開資料なし）

~~~diff
- 00b0a90c ["INT_ADD", "register:40f0:8", ["const:b0a90c:8", "const:4:8"]]
- 00b0a90c ["CALL", null, ["callee:00c58450:8"]]
+ 00b0ad34 ["INT_ADD", "register:40f0:8", ["const:b0ad34:8", "const:4:8"]]
+ 00b0ad34 ["CALL", null, ["callee:00c58450:8"]]
- 00b0a90c bytes d1350594
+ 00b0ad34 bytes c7350594
~~~


<a id="compare-e405fd23495d8ab19785d9af1f0e9cdf"></a>

### [`00b0a930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0a930.md) → [`00b0ad58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0ad58.md) FUN_00b0ad58

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`00ad075c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad075c.md) · 呼出先 6件 [`00802b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b18.md) [`00802c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802c68.md) [`00802ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802ea0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b0a190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0a190.md)
- 新版 呼出元 2件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00ad0958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad0/00ad0958.md) · 呼出先 6件 [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) [`00802ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ee0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0a5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0a5b8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0a930.md#insn-00b0a950) · [`00b0a958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0a930.md#insn-00b0a958) · [`00b0a960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0a930.md#insn-00b0a960)
- 新版 `00b0ad78`（命令位置の公開資料なし） · `00b0ad80`（命令位置の公開資料なし） · `00b0ad88`（命令位置の公開資料なし）

~~~diff
- 00b0a950 ["INT_ADD", "register:40f0:8", ["const:b0a950:8", "const:4:8"]]
- 00b0a950 ["CALL", null, ["callee:00802b58:8"]]
+ 00b0ad78 ["INT_ADD", "register:40f0:8", ["const:b0ad78:8", "const:4:8"]]
+ 00b0ad78 ["CALL", null, ["callee:00802b58:8"]]
- 00b0a950 bytes 72e0f397
+ 00b0ad78 bytes 78dff397
- 00b0a958 ["INT_ADD", "register:40f0:8", ["const:b0a958:8", "const:4:8"]]
- 00b0a958 ["CALL", null, ["callee:00802ca8:8"]]
+ 00b0ad80 ["INT_ADD", "register:40f0:8", ["const:b0ad80:8", "const:4:8"]]
+ 00b0ad80 ["CALL", null, ["callee:00802ca8:8"]]
- 00b0a958 bytes c4e0f397
+ 00b0ad80 bytes cadff397
- 00b0a960 ["INT_ADD", "register:40f0:8", ["const:b0a960:8", "const:4:8"]]
- 00b0a960 ["CALL", null, ["callee:00802ee0:8"]]
+ 00b0ad88 ["INT_ADD", "register:40f0:8", ["const:b0ad88:8", "const:4:8"]]
+ 00b0ad88 ["CALL", null, ["callee:00802ee0:8"]]
- 00b0a960 bytes 50e1f397
+ 00b0ad88 bytes 56e0f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26cf3443d007d532f9ce79b1738ce455"></a>

### [`00b0aa78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0aa78.md) → [`00b0aea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0aea0.md) FUN_00b0aea0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) · 呼出先 12件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00802b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b18.md) [`00802c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802c68.md) [`00802ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802ea0.md)
- 新版 呼出元 1件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) · 呼出先 12件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) [`00802ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0aac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0aa78.md#insn-00b0aac0) · [`00b0aac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0aa78.md#insn-00b0aac8) · [`00b0aad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0aa78.md#insn-00b0aad0)
- 新版 `00b0aee8`（命令位置の公開資料なし） · `00b0aef0`（命令位置の公開資料なし） · `00b0aef8`（命令位置の公開資料なし）

~~~diff
- 00b0aac0 ["INT_ADD", "register:40f0:8", ["const:b0aac0:8", "const:4:8"]]
- 00b0aac0 ["CALL", null, ["callee:00802b58:8"]]
+ 00b0aee8 ["INT_ADD", "register:40f0:8", ["const:b0aee8:8", "const:4:8"]]
+ 00b0aee8 ["CALL", null, ["callee:00802b58:8"]]
- 00b0aac0 bytes 16e0f397
+ 00b0aee8 bytes 1cdff397
- 00b0aac8 ["INT_ADD", "register:40f0:8", ["const:b0aac8:8", "const:4:8"]]
- 00b0aac8 ["CALL", null, ["callee:00802ca8:8"]]
+ 00b0aef0 ["INT_ADD", "register:40f0:8", ["const:b0aef0:8", "const:4:8"]]
+ 00b0aef0 ["CALL", null, ["callee:00802ca8:8"]]
- 00b0aac8 bytes 68e0f397
+ 00b0aef0 bytes 6edff397
- 00b0aad0 ["INT_ADD", "register:40f0:8", ["const:b0aad0:8", "const:4:8"]]
- 00b0aad0 ["CALL", null, ["callee:00802ee0:8"]]
+ 00b0aef8 ["INT_ADD", "register:40f0:8", ["const:b0aef8:8", "const:4:8"]]
+ 00b0aef8 ["CALL", null, ["callee:00802ee0:8"]]
- 00b0aad0 bytes f4e0f397
+ 00b0aef8 bytes fadff397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e46b6d94c56b82f5a0fb5e59297adc12"></a>

### [`00b0af5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0af5c.md) → [`00b0b384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b384.md) FUN_00b0b384

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) [`00ad075c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad075c.md) [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00802b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b18.md) [`00802c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802c68.md) [`00802ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802ea0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 8件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`00ad0958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad0/00ad0958.md) [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) [`00802ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ee0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0af94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0af5c.md#insn-00b0af94) · [`00b0af9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0af5c.md#insn-00b0af9c) · [`00b0afa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0af5c.md#insn-00b0afa4)
- 新版 `00b0b3bc`（命令位置の公開資料なし） · `00b0b3c4`（命令位置の公開資料なし） · `00b0b3cc`（命令位置の公開資料なし）

~~~diff
- 00b0af94 ["INT_ADD", "register:40f0:8", ["const:b0af94:8", "const:4:8"]]
- 00b0af94 ["CALL", null, ["callee:00802b58:8"]]
+ 00b0b3bc ["INT_ADD", "register:40f0:8", ["const:b0b3bc:8", "const:4:8"]]
+ 00b0b3bc ["CALL", null, ["callee:00802b58:8"]]
- 00b0af94 bytes e1def397
+ 00b0b3bc bytes e7ddf397
- 00b0af9c ["INT_ADD", "register:40f0:8", ["const:b0af9c:8", "const:4:8"]]
- 00b0af9c ["CALL", null, ["callee:00802ca8:8"]]
+ 00b0b3c4 ["INT_ADD", "register:40f0:8", ["const:b0b3c4:8", "const:4:8"]]
+ 00b0b3c4 ["CALL", null, ["callee:00802ca8:8"]]
- 00b0af9c bytes 33dff397
+ 00b0b3c4 bytes 39def397
- 00b0afa4 ["INT_ADD", "register:40f0:8", ["const:b0afa4:8", "const:4:8"]]
- 00b0afa4 ["CALL", null, ["callee:00802ee0:8"]]
+ 00b0b3cc ["INT_ADD", "register:40f0:8", ["const:b0b3cc:8", "const:4:8"]]
+ 00b0b3cc ["CALL", null, ["callee:00802ee0:8"]]
- 00b0afa4 bytes bfdff397
+ 00b0b3cc bytes c5def397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b0c8665a3fc5dd17ae645340b22ea6c"></a>

### [`00b0b0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0b0b4.md) → [`00b0b4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b4dc.md) FUN_00b0b4dc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b0b218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0b218.md) [`00b0b8d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0b8d8.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00802b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b18.md) [`00802c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802c68.md) [`00802ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802ea0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`00b0b640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b640.md) [`00b0bd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0bd00.md) · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) [`00802ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ee0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0b0b4.md#insn-00b0b0f0) · [`00b0b0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0b0b4.md#insn-00b0b0f8) · [`00b0b100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0b0b4.md#insn-00b0b100)
- 新版 `00b0b518`（命令位置の公開資料なし） · `00b0b520`（命令位置の公開資料なし） · `00b0b528`（命令位置の公開資料なし）

~~~diff
- 00b0b0f0 ["INT_ADD", "register:40f0:8", ["const:b0b0f0:8", "const:4:8"]]
- 00b0b0f0 ["CALL", null, ["callee:00802b58:8"]]
+ 00b0b518 ["INT_ADD", "register:40f0:8", ["const:b0b518:8", "const:4:8"]]
+ 00b0b518 ["CALL", null, ["callee:00802b58:8"]]
- 00b0b0f0 bytes 8adef397
+ 00b0b518 bytes 90ddf397
- 00b0b0f8 ["INT_ADD", "register:40f0:8", ["const:b0b0f8:8", "const:4:8"]]
- 00b0b0f8 ["CALL", null, ["callee:00802ca8:8"]]
+ 00b0b520 ["INT_ADD", "register:40f0:8", ["const:b0b520:8", "const:4:8"]]
+ 00b0b520 ["CALL", null, ["callee:00802ca8:8"]]
- 00b0b0f8 bytes dcdef397
+ 00b0b520 bytes e2ddf397
- 00b0b100 ["INT_ADD", "register:40f0:8", ["const:b0b100:8", "const:4:8"]]
- 00b0b100 ["CALL", null, ["callee:00802ee0:8"]]
+ 00b0b528 ["INT_ADD", "register:40f0:8", ["const:b0b528:8", "const:4:8"]]
+ 00b0b528 ["CALL", null, ["callee:00802ee0:8"]]
- 00b0b100 bytes 68dff397
+ 00b0b528 bytes 6edef397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8c6733166d3d7ed277d8306efbfec86"></a>

### [`00b0c3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c3f4.md) → [`00b0c81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0c81c.md) FUN_00b0c81c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b092e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b092e0.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00b0c600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c600.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 1件 [`00b09708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09708.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b0ca28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0ca28.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0c4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c3f4.md#insn-00b0c4a0) · [`00b0c4e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c3f4.md#insn-00b0c4e4) · [`00b0c528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c3f4.md#insn-00b0c528)
- 新版 `00b0c8c8`（命令位置の公開資料なし） · `00b0c90c`（命令位置の公開資料なし） · `00b0c950`（命令位置の公開資料なし）

~~~diff
- 00b0c4a0 ["INT_ADD", "register:40f0:8", ["const:b0c4a0:8", "const:4:8"]]
- 00b0c4a0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b0c8c8 ["INT_ADD", "register:40f0:8", ["const:b0c8c8:8", "const:4:8"]]
+ 00b0c8c8 ["CALL", null, ["callee:00c57e90:8"]]
- 00b0c4a0 bytes 7c2d0594
+ 00b0c8c8 bytes 722d0594
- 00b0c4e4 ["INT_ADD", "register:40f0:8", ["const:b0c4e4:8", "const:4:8"]]
- 00b0c4e4 ["CALL", null, ["callee:00c58090:8"]]
+ 00b0c90c ["INT_ADD", "register:40f0:8", ["const:b0c90c:8", "const:4:8"]]
+ 00b0c90c ["CALL", null, ["callee:00c58090:8"]]
- 00b0c4e4 bytes eb2d0594
+ 00b0c90c bytes e12d0594
- 00b0c528 ["INT_ADD", "register:40f0:8", ["const:b0c528:8", "const:4:8"]]
- 00b0c528 ["CALL", null, ["callee:00c58090:8"]]
+ 00b0c950 ["INT_ADD", "register:40f0:8", ["const:b0c950:8", "const:4:8"]]
+ 00b0c950 ["CALL", null, ["callee:00c58090:8"]]
- 00b0c528 bytes da2d0594
+ 00b0c950 bytes d02d0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2f33eba47bbf2fcb8139254c57bbebe"></a>

### [`00b0c628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c628.md) → [`00b0ca50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0ca50.md) FUN_00b0ca50

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b0aa78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0aa78.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00b0c600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c600.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00b0aea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0aea0.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b0ca28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0ca28.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0c6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c628.md#insn-00b0c6b4) · [`00b0c76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c628.md#insn-00b0c76c) · [`00b0c788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c628.md#insn-00b0c788)
- 新版 `00b0cadc`（命令位置の公開資料なし） · `00b0cb94`（命令位置の公開資料なし） · `00b0cbb0`（命令位置の公開資料なし）

~~~diff
- 00b0c6b4 ["INT_ADD", "register:40f0:8", ["const:b0c6b4:8", "const:4:8"]]
- 00b0c6b4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b0cadc ["INT_ADD", "register:40f0:8", ["const:b0cadc:8", "const:4:8"]]
+ 00b0cadc ["CALL", null, ["callee:00c57e90:8"]]
- 00b0c6b4 bytes f72c0594
+ 00b0cadc bytes ed2c0594
- 00b0c76c ["INT_ADD", "register:40f0:8", ["const:b0c76c:8", "const:4:8"]]
- 00b0c76c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b0cb94 ["INT_ADD", "register:40f0:8", ["const:b0cb94:8", "const:4:8"]]
+ 00b0cb94 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b0c76c bytes d12c0594
+ 00b0cb94 bytes c72c0594
- 00b0c788 ["INT_ADD", "register:40f0:8", ["const:b0c788:8", "const:4:8"]]
- 00b0c788 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b0cbb0 ["INT_ADD", "register:40f0:8", ["const:b0cbb0:8", "const:4:8"]]
+ 00b0cbb0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b0c788 bytes ca2c0594
+ 00b0cbb0 bytes c02c0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1965b6f0978b9f66c899b3b66e1938ae"></a>

### [`00b0cecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cecc.md) → [`00b0d2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d2f4.md) FUN_00b0d2f4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6a18.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md)
- 新版 呼出元 0件  · 呼出先 3件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6a5c.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0ced8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cecc.md#insn-00b0ced8) · [`00b0cee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cecc.md#insn-00b0cee8) · [`00b0cef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cecc.md#insn-00b0cef0)
- 新版 `00b0d300`（命令位置の公開資料なし） · `00b0d310`（命令位置の公開資料なし） · `00b0d318`（命令位置の公開資料なし）

~~~diff
- 00b0ced8 ["INT_ADD", "register:40f0:8", ["const:b0ced8:8", "const:4:8"]]
- 00b0ced8 ["CALL", null, ["callee:008514f8:8"]]
+ 00b0d300 ["INT_ADD", "register:40f0:8", ["const:b0d300:8", "const:4:8"]]
+ 00b0d300 ["CALL", null, ["callee:008514f8:8"]]
- 00b0ced8 bytes 7811f597
+ 00b0d300 bytes 7e10f597
- 00b0cee8 ["INT_ADD", "register:40f0:8", ["const:b0cee8:8", "const:4:8"]]
- 00b0cee8 ["CALL", null, ["callee:008b79c8:8"]]
+ 00b0d310 ["INT_ADD", "register:40f0:8", ["const:b0d310:8", "const:4:8"]]
+ 00b0d310 ["CALL", null, ["callee:008b79c8:8"]]
- 00b0cee8 bytes a7aaf697
+ 00b0d310 bytes aea9f697
- 00b0cef0 ["INT_ADD", "register:40f0:8", ["const:b0cef0:8", "const:4:8"]]
- 00b0cef0 ["CALL", null, ["callee:008b6a5c:8"]]
+ 00b0d318 ["INT_ADD", "register:40f0:8", ["const:b0d318:8", "const:4:8"]]
+ 00b0d318 ["CALL", null, ["callee:008b6a5c:8"]]
- 00b0cef0 bytes caa6f697
+ 00b0d318 bytes d1a5f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61b6621897e30e6b3a46dafacef63766"></a>

### [`00b0cfa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cfa8.md) → [`00b0d3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d3d0.md) FUN_00b0d3d0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 13件 [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0cfd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cfa8.md#insn-00b0cfd4) · [`00b0cff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cfa8.md#insn-00b0cff4) · [`00b0d000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cfa8.md#insn-00b0d000)
- 新版 `00b0d3fc`（命令位置の公開資料なし） · `00b0d41c`（命令位置の公開資料なし） · `00b0d428`（命令位置の公開資料なし）

~~~diff
- 00b0cfd4 ["INT_ADD", "register:40f0:8", ["const:b0cfd4:8", "const:4:8"]]
- 00b0cfd4 ["CALL", null, ["callee:008b9290:8"]]
+ 00b0d3fc ["INT_ADD", "register:40f0:8", ["const:b0d3fc:8", "const:4:8"]]
+ 00b0d3fc ["CALL", null, ["callee:008b9290:8"]]
- 00b0cfd4 bytes 9eb0f697
+ 00b0d3fc bytes a5aff697
- 00b0cff4 ["INT_ADD", "register:40f0:8", ["const:b0cff4:8", "const:4:8"]]
- 00b0cff4 ["CALL", null, ["callee:008b9298:8"]]
+ 00b0d41c ["INT_ADD", "register:40f0:8", ["const:b0d41c:8", "const:4:8"]]
+ 00b0d41c ["CALL", null, ["callee:008b9298:8"]]
- 00b0cff4 bytes 98b0f697
+ 00b0d41c bytes 9faff697
- 00b0d000 ["INT_ADD", "register:40f0:8", ["const:b0d000:8", "const:4:8"]]
- 00b0d000 ["CALL", null, ["callee:008b9298:8"]]
+ 00b0d428 ["INT_ADD", "register:40f0:8", ["const:b0d428:8", "const:4:8"]]
+ 00b0d428 ["CALL", null, ["callee:008b9298:8"]]
- 00b0d000 bytes 95b0f697
+ 00b0d428 bytes 9caff697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24288cd9545439c03c486378ed9b4bd6"></a>

### [`00b0d678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d678.md) → [`00b0daa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0daa0.md) FUN_00b0daa0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b0be2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0be2c.md) · 呼出先 2件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00b0c254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0c254.md) · 呼出先 2件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d678.md#insn-00b0d6e0) · [`00b0d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d678.md#insn-00b0d71c) · [`00b0d72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d678.md#insn-00b0d72c)
- 新版 `00b0db08`（命令位置の公開資料なし） · `00b0db44`（命令位置の公開資料なし） · `00b0db54`（命令位置の公開資料なし）

~~~diff
- 00b0d6e0 ["INT_ADD", "register:40f0:8", ["const:b0d6e0:8", "const:4:8"]]
- 00b0d6e0 ["CALL", null, ["callee:00494610:8"]]
+ 00b0db08 ["INT_ADD", "register:40f0:8", ["const:b0db08:8", "const:4:8"]]
+ 00b0db08 ["CALL", null, ["callee:00494610:8"]]
- 00b0d6e0 bytes bc1be697
+ 00b0db08 bytes c21ae697
- 00b0d71c ["INT_ADD", "register:40f0:8", ["const:b0d71c:8", "const:4:8"]]
- 00b0d71c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b0db44 ["INT_ADD", "register:40f0:8", ["const:b0db44:8", "const:4:8"]]
+ 00b0db44 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b0d71c bytes e5280594
+ 00b0db44 bytes db280594
- 00b0d72c ["INT_ADD", "register:40f0:8", ["const:b0d72c:8", "const:4:8"]]
- 00b0d72c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b0db54 ["INT_ADD", "register:40f0:8", ["const:b0db54:8", "const:4:8"]]
+ 00b0db54 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b0d72c bytes e1280594
+ 00b0db54 bytes d7280594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dff6e0d364b07790fc605fa3efd56e2d"></a>

### [`00b0e994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e994.md) → [`00b0edbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0edbc.md) FUN_00b0edbc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) · 呼出先 2件 [`004802b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md) [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md)
- 新版 呼出元 1件 [`00a1a750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a750.md) · 呼出先 2件 [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md) [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0e9b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e994.md#insn-00b0e9b4) · [`00b0e9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e994.md#insn-00b0e9c0) · [`00b0e9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e994.md#insn-00b0e9cc)
- 新版 `00b0eddc`（命令位置の公開資料なし） · `00b0ede8`（命令位置の公開資料なし） · `00b0edf4`（命令位置の公開資料なし）

~~~diff
- 00b0e9b4 ["INT_ADD", "register:40f0:8", ["const:b0e9b4:8", "const:4:8"]]
- 00b0e9b4 ["CALL", null, ["callee:004803f0:8"]]
+ 00b0eddc ["INT_ADD", "register:40f0:8", ["const:b0eddc:8", "const:4:8"]]
+ 00b0eddc ["CALL", null, ["callee:004803f0:8"]]
- 00b0e9b4 bytes 7fc6e597
+ 00b0eddc bytes 85c5e597
- 00b0e9c0 ["INT_ADD", "register:40f0:8", ["const:b0e9c0:8", "const:4:8"]]
- 00b0e9c0 ["CALL", null, ["callee:004803f0:8"]]
+ 00b0ede8 ["INT_ADD", "register:40f0:8", ["const:b0ede8:8", "const:4:8"]]
+ 00b0ede8 ["CALL", null, ["callee:004803f0:8"]]
- 00b0e9c0 bytes 7cc6e597
+ 00b0ede8 bytes 82c5e597
- 00b0e9cc ["INT_ADD", "register:40f0:8", ["const:b0e9cc:8", "const:4:8"]]
- 00b0e9cc ["CALL", null, ["callee:004803f0:8"]]
+ 00b0edf4 ["INT_ADD", "register:40f0:8", ["const:b0edf4:8", "const:4:8"]]
+ 00b0edf4 ["CALL", null, ["callee:004803f0:8"]]
- 00b0e9cc bytes 79c6e597
+ 00b0edf4 bytes 7fc5e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-126e707470984468c84ae6c463d29c66"></a>

### [`00b0eab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0eab4.md) → [`00b0eedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0eedc.md) FUN_00b0eedc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a22234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a22/00a22234.md) · 呼出先 2件 [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md) [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md)
- 新版 呼出元 1件 [`00a223d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a22/00a223d0.md) · 呼出先 2件 [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0ead4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0eab4.md#insn-00b0ead4) · [`00b0eae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0eab4.md#insn-00b0eae0) · [`00b0eaec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0eab4.md#insn-00b0eaec)
- 新版 `00b0eefc`（命令位置の公開資料なし） · `00b0ef08`（命令位置の公開資料なし） · `00b0ef14`（命令位置の公開資料なし）

~~~diff
- 00b0ead4 ["INT_ADD", "register:40f0:8", ["const:b0ead4:8", "const:4:8"]]
- 00b0ead4 ["CALL", null, ["callee:00480e28:8"]]
+ 00b0eefc ["INT_ADD", "register:40f0:8", ["const:b0eefc:8", "const:4:8"]]
+ 00b0eefc ["CALL", null, ["callee:00480e28:8"]]
- 00b0ead4 bytes c5c8e597
+ 00b0eefc bytes cbc7e597
- 00b0eae0 ["INT_ADD", "register:40f0:8", ["const:b0eae0:8", "const:4:8"]]
- 00b0eae0 ["CALL", null, ["callee:00480e28:8"]]
+ 00b0ef08 ["INT_ADD", "register:40f0:8", ["const:b0ef08:8", "const:4:8"]]
+ 00b0ef08 ["CALL", null, ["callee:00480e28:8"]]
- 00b0eae0 bytes c2c8e597
+ 00b0ef08 bytes c8c7e597
- 00b0eaec ["INT_ADD", "register:40f0:8", ["const:b0eaec:8", "const:4:8"]]
- 00b0eaec ["CALL", null, ["callee:00480e28:8"]]
+ 00b0ef14 ["INT_ADD", "register:40f0:8", ["const:b0ef14:8", "const:4:8"]]
+ 00b0ef14 ["CALL", null, ["callee:00480e28:8"]]
- 00b0eaec bytes bfc8e597
+ 00b0ef14 bytes c5c7e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-988fa9a07bcbcc1aadbcbd871f920304"></a>

### [`00b0eb78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0eb78.md) → [`00b0efa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0efa0.md) FUN_00b0efa0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) · 呼出先 1件 [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md)
- 新版 呼出元 1件 [`00a1a750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a750.md) · 呼出先 1件 [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0eb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0eb78.md#insn-00b0eb90) · [`00b0eb9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0eb78.md#insn-00b0eb9c)
- 新版 `00b0efb8`（命令位置の公開資料なし） · `00b0efc4`（命令位置の公開資料なし）

~~~diff
- 00b0eb90 ["INT_ADD", "register:40f0:8", ["const:b0eb90:8", "const:4:8"]]
- 00b0eb90 ["CALL", null, ["callee:004803f0:8"]]
+ 00b0efb8 ["INT_ADD", "register:40f0:8", ["const:b0efb8:8", "const:4:8"]]
+ 00b0efb8 ["CALL", null, ["callee:004803f0:8"]]
- 00b0eb90 bytes 08c6e597
+ 00b0efb8 bytes 0ec5e597
- 00b0eb9c ["INT_ADD", "register:40f0:8", ["const:b0eb9c:8", "const:4:8"]]
- 00b0eb9c ["CALL", null, ["callee:004803f0:8"]]
+ 00b0efc4 ["INT_ADD", "register:40f0:8", ["const:b0efc4:8", "const:4:8"]]
+ 00b0efc4 ["CALL", null, ["callee:004803f0:8"]]
- 00b0eb9c bytes 05c6e597
+ 00b0efc4 bytes 0bc5e597
~~~


<a id="compare-ce8ce29c12302a7f29a3acb27aa57c28"></a>

### [`00b0ebb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0ebb0.md) → [`00b0efd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0efd8.md) FUN_00b0efd8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a22234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a22/00a22234.md) · 呼出先 1件 [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md)
- 新版 呼出元 1件 [`00a223d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a22/00a223d0.md) · 呼出先 1件 [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0ebd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0ebb0.md#insn-00b0ebd0)
- 新版 `00b0eff8`（命令位置の公開資料なし）

~~~diff
- 00b0ebd0 ["INT_ADD", "register:40f0:8", ["const:b0ebd0:8", "const:4:8"]]
- 00b0ebd0 ["CALL", null, ["callee:00480e28:8"]]
+ 00b0eff8 ["INT_ADD", "register:40f0:8", ["const:b0eff8:8", "const:4:8"]]
+ 00b0eff8 ["CALL", null, ["callee:00480e28:8"]]
- 00b0ebd0 bytes 86c8e597
+ 00b0eff8 bytes 8cc7e597
~~~


<a id="compare-f8a0a7105d172fd257baf1f8c3e462da"></a>

### [`00b0efe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0efe4.md) → [`00b0f40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f40c.md) FUN_00b0f40c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b0f1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0f/00b0f1cc.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00b1090c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b1090c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00b0f5f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f5f4.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00b10d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b10/00b10d34.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0f024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0efe4.md#insn-00b0f024) · [`00b0f034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0efe4.md#insn-00b0f034) · [`00b0f05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0efe4.md#insn-00b0f05c)
- 新版 `00b0f44c`（命令位置の公開資料なし） · `00b0f45c`（命令位置の公開資料なし） · `00b0f484`（命令位置の公開資料なし）

~~~diff
- 00b0f024 ["INT_ADD", "register:40f0:8", ["const:b0f024:8", "const:4:8"]]
- 00b0f024 ["CALL", null, ["callee:0048793c:8"]]
+ 00b0f44c ["INT_ADD", "register:40f0:8", ["const:b0f44c:8", "const:4:8"]]
+ 00b0f44c ["CALL", null, ["callee:0048793c:8"]]
- 00b0f024 bytes 36e2e597
+ 00b0f44c bytes 3ce1e597
- 00b0f034 ["INT_ADD", "register:40f0:8", ["const:b0f034:8", "const:4:8"]]
- 00b0f034 ["CALL", null, ["callee:0048793c:8"]]
+ 00b0f45c ["INT_ADD", "register:40f0:8", ["const:b0f45c:8", "const:4:8"]]
+ 00b0f45c ["CALL", null, ["callee:0048793c:8"]]
- 00b0f034 bytes 32e2e597
+ 00b0f45c bytes 38e1e597
- 00b0f05c ["INT_ADD", "register:40f0:8", ["const:b0f05c:8", "const:4:8"]]
- 00b0f05c ["CALL", null, ["callee:0048791c:8"]]
+ 00b0f484 ["INT_ADD", "register:40f0:8", ["const:b0f484:8", "const:4:8"]]
+ 00b0f484 ["CALL", null, ["callee:0048791c:8"]]
- 00b0f05c bytes 20e2e597
+ 00b0f484 bytes 26e1e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6395586acca6a6cb16ac157803c842aa"></a>

### [`00b289e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b289e4.md) → [`00b28e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28e0c.md) FUN_00b28e0c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b28a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b289e4.md#insn-00b28a40) · [`00b28a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b289e4.md#insn-00b28a68)
- 新版 `00b28e68`（命令位置の公開資料なし） · `00b28e90`（命令位置の公開資料なし）

~~~diff
- 00b28a40 ["INT_ADD", "register:40f0:8", ["const:b28a40:8", "const:4:8"]]
- 00b28a40 ["CALL", null, ["callee:0043bb20:8"]]
+ 00b28e68 ["INT_ADD", "register:40f0:8", ["const:b28e68:8", "const:4:8"]]
+ 00b28e68 ["CALL", null, ["callee:0043bb20:8"]]
- 00b28a40 bytes 284ce497
+ 00b28e68 bytes 2e4be497
- 00b28a68 ["INT_ADD", "register:40f0:8", ["const:b28a68:8", "const:4:8"]]
- 00b28a68 ["CALL", null, ["callee:0043bb20:8"]]
+ 00b28e90 ["INT_ADD", "register:40f0:8", ["const:b28e90:8", "const:4:8"]]
+ 00b28e90 ["CALL", null, ["callee:0043bb20:8"]]
- 00b28a68 bytes 1e4ce497
+ 00b28e90 bytes 244be497
~~~


<a id="compare-4e0df513e5889f54a47f4b7951ce6a26"></a>

### [`00b28ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28ac8.md) → [`00b28ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28ef0.md) FUN_00b28ef0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b28b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28ac8.md#insn-00b28b04) · [`00b28b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28ac8.md#insn-00b28b14)
- 新版 `00b28f2c`（命令位置の公開資料なし） · `00b28f3c`（命令位置の公開資料なし）

~~~diff
- 00b28b04 ["INT_ADD", "register:40f0:8", ["const:b28b04:8", "const:4:8"]]
- 00b28b04 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b28f2c ["INT_ADD", "register:40f0:8", ["const:b28f2c:8", "const:4:8"]]
+ 00b28f2c ["CALL", null, ["callee:00c57eb0:8"]]
- 00b28b04 bytes ebbb0494
+ 00b28f2c bytes e1bb0494
- 00b28b14 ["INT_ADD", "register:40f0:8", ["const:b28b14:8", "const:4:8"]]
- 00b28b14 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b28f3c ["INT_ADD", "register:40f0:8", ["const:b28f3c:8", "const:4:8"]]
+ 00b28f3c ["CALL", null, ["callee:00c57eb0:8"]]
- 00b28b14 bytes e7bb0494
+ 00b28f3c bytes ddbb0494
~~~


<a id="compare-3e417ba2af4970d7dfb9dc1c4a739ab8"></a>

### [`00b295c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b295c0.md) → [`00b299e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b299e8.md) FUN_00b299e8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`007532d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/007532d0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00753310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00753/00753310.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b29638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b295c0.md#insn-00b29638) · [`00b2965c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b295c0.md#insn-00b2965c) · [`00b29688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b295c0.md#insn-00b29688)
- 新版 `00b29a60`（命令位置の公開資料なし） · `00b29a84`（命令位置の公開資料なし） · `00b29ab0`（命令位置の公開資料なし）

~~~diff
- 00b29638 ["INT_ADD", "register:40f0:8", ["const:b29638:8", "const:4:8"]]
- 00b29638 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b29a60 ["INT_ADD", "register:40f0:8", ["const:b29a60:8", "const:4:8"]]
+ 00b29a60 ["CALL", null, ["callee:00c57e90:8"]]
- 00b29638 bytes 16b90494
+ 00b29a60 bytes 0cb90494
- 00b2965c ["INT_ADD", "register:40f0:8", ["const:b2965c:8", "const:4:8"]]
- 00b2965c ["CALL", null, ["callee:00c58090:8"]]
+ 00b29a84 ["INT_ADD", "register:40f0:8", ["const:b29a84:8", "const:4:8"]]
+ 00b29a84 ["CALL", null, ["callee:00c58090:8"]]
- 00b2965c bytes 8db90494
+ 00b29a84 bytes 83b90494
- 00b29688 ["INT_ADD", "register:40f0:8", ["const:b29688:8", "const:4:8"]]
- 00b29688 ["CALL", null, ["callee:00c58090:8"]]
+ 00b29ab0 ["INT_ADD", "register:40f0:8", ["const:b29ab0:8", "const:4:8"]]
+ 00b29ab0 ["CALL", null, ["callee:00c58090:8"]]
- 00b29688 bytes 82b90494
+ 00b29ab0 bytes 78b90494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ae12ad9d557622dfba9abaa9c52d64d"></a>

### [`00b29bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29bfc.md) → [`00b2a024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a024.md) FUN_00b2a024

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00b29d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29d28.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b2a150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a150.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b29c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29bfc.md#insn-00b29c74) · [`00b29c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29bfc.md#insn-00b29c98) · [`00b29cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29bfc.md#insn-00b29cc4)
- 新版 `00b2a09c`（命令位置の公開資料なし） · `00b2a0c0`（命令位置の公開資料なし） · `00b2a0ec`（命令位置の公開資料なし）

~~~diff
- 00b29c74 ["INT_ADD", "register:40f0:8", ["const:b29c74:8", "const:4:8"]]
- 00b29c74 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b2a09c ["INT_ADD", "register:40f0:8", ["const:b2a09c:8", "const:4:8"]]
+ 00b2a09c ["CALL", null, ["callee:00c57e90:8"]]
- 00b29c74 bytes 87b70494
+ 00b2a09c bytes 7db70494
- 00b29c98 ["INT_ADD", "register:40f0:8", ["const:b29c98:8", "const:4:8"]]
- 00b29c98 ["CALL", null, ["callee:00c58090:8"]]
+ 00b2a0c0 ["INT_ADD", "register:40f0:8", ["const:b2a0c0:8", "const:4:8"]]
+ 00b2a0c0 ["CALL", null, ["callee:00c58090:8"]]
- 00b29c98 bytes feb70494
+ 00b2a0c0 bytes f4b70494
- 00b29cc4 ["INT_ADD", "register:40f0:8", ["const:b29cc4:8", "const:4:8"]]
- 00b29cc4 ["CALL", null, ["callee:00c58090:8"]]
+ 00b2a0ec ["INT_ADD", "register:40f0:8", ["const:b2a0ec:8", "const:4:8"]]
+ 00b2a0ec ["CALL", null, ["callee:00c58090:8"]]
- 00b29cc4 bytes f3b70494
+ 00b2a0ec bytes e9b70494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7869c6ff63ef992191120bd7d180e91c"></a>

### [`00b29d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29d3c.md) → [`00b2a164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a164.md) FUN_00b2a164

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00b29ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29ed0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b2a2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a2f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b29de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29d3c.md#insn-00b29de4) · [`00b29e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29d3c.md#insn-00b29e24) · [`00b29e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29d3c.md#insn-00b29e68)
- 新版 `00b2a20c`（命令位置の公開資料なし） · `00b2a24c`（命令位置の公開資料なし） · `00b2a290`（命令位置の公開資料なし）

~~~diff
- 00b29de4 ["INT_ADD", "register:40f0:8", ["const:b29de4:8", "const:4:8"]]
- 00b29de4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b2a20c ["INT_ADD", "register:40f0:8", ["const:b2a20c:8", "const:4:8"]]
+ 00b2a20c ["CALL", null, ["callee:00c57e90:8"]]
- 00b29de4 bytes 2bb70494
+ 00b2a20c bytes 21b70494
- 00b29e24 ["INT_ADD", "register:40f0:8", ["const:b29e24:8", "const:4:8"]]
- 00b29e24 ["CALL", null, ["callee:00c58090:8"]]
+ 00b2a24c ["INT_ADD", "register:40f0:8", ["const:b2a24c:8", "const:4:8"]]
+ 00b2a24c ["CALL", null, ["callee:00c58090:8"]]
- 00b29e24 bytes 9bb70494
+ 00b2a24c bytes 91b70494
- 00b29e68 ["INT_ADD", "register:40f0:8", ["const:b29e68:8", "const:4:8"]]
- 00b29e68 ["CALL", null, ["callee:00c58090:8"]]
+ 00b2a290 ["INT_ADD", "register:40f0:8", ["const:b2a290:8", "const:4:8"]]
+ 00b2a290 ["CALL", null, ["callee:00c58090:8"]]
- 00b29e68 bytes 8ab70494
+ 00b2a290 bytes 80b70494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00895d7f37bc6fd795d04511e9b81393"></a>

### [`00b29ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29ee4.md) → [`00b2a30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a30c.md) FUN_00b2a30c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00b2a074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a074.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b2a49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a49c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b29f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29ee4.md#insn-00b29f88) · [`00b29fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29ee4.md#insn-00b29fc8) · [`00b2a014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29ee4.md#insn-00b2a014)
- 新版 `00b2a3b0`（命令位置の公開資料なし） · `00b2a3f0`（命令位置の公開資料なし） · `00b2a43c`（命令位置の公開資料なし）

~~~diff
- 00b29f88 ["INT_ADD", "register:40f0:8", ["const:b29f88:8", "const:4:8"]]
- 00b29f88 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b2a3b0 ["INT_ADD", "register:40f0:8", ["const:b2a3b0:8", "const:4:8"]]
+ 00b2a3b0 ["CALL", null, ["callee:00c57e90:8"]]
- 00b29f88 bytes c2b60494
+ 00b2a3b0 bytes b8b60494
- 00b29fc8 ["INT_ADD", "register:40f0:8", ["const:b29fc8:8", "const:4:8"]]
- 00b29fc8 ["CALL", null, ["callee:00c58090:8"]]
+ 00b2a3f0 ["INT_ADD", "register:40f0:8", ["const:b2a3f0:8", "const:4:8"]]
+ 00b2a3f0 ["CALL", null, ["callee:00c58090:8"]]
- 00b29fc8 bytes 32b70494
+ 00b2a3f0 bytes 28b70494
- 00b2a014 ["INT_ADD", "register:40f0:8", ["const:b2a014:8", "const:4:8"]]
- 00b2a014 ["CALL", null, ["callee:00c58090:8"]]
+ 00b2a43c ["INT_ADD", "register:40f0:8", ["const:b2a43c:8", "const:4:8"]]
+ 00b2a43c ["CALL", null, ["callee:00c58090:8"]]
- 00b2a014 bytes 1fb70494
+ 00b2a43c bytes 15b70494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-997ea0f88e550dc9e6844d4b2f990ac5"></a>

### [`00b2a09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a09c.md) → [`00b2a4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a4c4.md) FUN_00b2a4c4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00b2a1c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a1c8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b2a5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a5f0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2a114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a09c.md#insn-00b2a114) · [`00b2a138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a09c.md#insn-00b2a138) · [`00b2a164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a09c.md#insn-00b2a164)
- 新版 `00b2a53c`（命令位置の公開資料なし） · `00b2a560`（命令位置の公開資料なし） · `00b2a58c`（命令位置の公開資料なし）

~~~diff
- 00b2a114 ["INT_ADD", "register:40f0:8", ["const:b2a114:8", "const:4:8"]]
- 00b2a114 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b2a53c ["INT_ADD", "register:40f0:8", ["const:b2a53c:8", "const:4:8"]]
+ 00b2a53c ["CALL", null, ["callee:00c57e90:8"]]
- 00b2a114 bytes 5fb60494
+ 00b2a53c bytes 55b60494
- 00b2a138 ["INT_ADD", "register:40f0:8", ["const:b2a138:8", "const:4:8"]]
- 00b2a138 ["CALL", null, ["callee:00c58090:8"]]
+ 00b2a560 ["INT_ADD", "register:40f0:8", ["const:b2a560:8", "const:4:8"]]
+ 00b2a560 ["CALL", null, ["callee:00c58090:8"]]
- 00b2a138 bytes d6b60494
+ 00b2a560 bytes ccb60494
- 00b2a164 ["INT_ADD", "register:40f0:8", ["const:b2a164:8", "const:4:8"]]
- 00b2a164 ["CALL", null, ["callee:00c58090:8"]]
+ 00b2a58c ["INT_ADD", "register:40f0:8", ["const:b2a58c:8", "const:4:8"]]
+ 00b2a58c ["CALL", null, ["callee:00c58090:8"]]
- 00b2a164 bytes cbb60494
+ 00b2a58c bytes c1b60494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99e3abe80710f33679adcdc20be90c0f"></a>

### [`00b2a69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a69c.md) → [`00b2aac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2aac4.md) FUN_00b2aac4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b2a414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a414.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00b2a83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a83c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2a75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a69c.md#insn-00b2a75c) · [`00b2a76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a69c.md#insn-00b2a76c) · [`00b2a77c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a69c.md#insn-00b2a77c)
- 新版 `00b2ab84`（命令位置の公開資料なし） · `00b2ab94`（命令位置の公開資料なし） · `00b2aba4`（命令位置の公開資料なし）

~~~diff
- 00b2a75c ["INT_ADD", "register:40f0:8", ["const:b2a75c:8", "const:4:8"]]
- 00b2a75c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b2ab84 ["INT_ADD", "register:40f0:8", ["const:b2ab84:8", "const:4:8"]]
+ 00b2ab84 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b2a75c bytes d5b40494
+ 00b2ab84 bytes cbb40494
- 00b2a76c ["INT_ADD", "register:40f0:8", ["const:b2a76c:8", "const:4:8"]]
- 00b2a76c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b2ab94 ["INT_ADD", "register:40f0:8", ["const:b2ab94:8", "const:4:8"]]
+ 00b2ab94 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b2a76c bytes d1b40494
+ 00b2ab94 bytes c7b40494
- 00b2a77c ["INT_ADD", "register:40f0:8", ["const:b2a77c:8", "const:4:8"]]
- 00b2a77c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b2aba4 ["INT_ADD", "register:40f0:8", ["const:b2aba4:8", "const:4:8"]]
+ 00b2aba4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b2a77c bytes cdb40494
+ 00b2aba4 bytes c3b40494
~~~


<a id="compare-ac7e0152b2e934ce249467542e4c4d43"></a>

### [`00b2a7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a7a4.md) → [`00b2abcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2abcc.md) FUN_00b2abcc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0054071c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md) [`00794b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794b2c.md) [`0080da1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080da1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0054075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054075c.md) [`00794b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794b6c.md) [`0080da5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080da5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2a848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a7a4.md#insn-00b2a848) · [`00b2a890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a7a4.md#insn-00b2a890) · [`00b2a8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a7a4.md#insn-00b2a8a8)
- 新版 `00b2ac70`（命令位置の公開資料なし） · `00b2acb8`（命令位置の公開資料なし） · `00b2acd0`（命令位置の公開資料なし）

~~~diff
- 00b2a848 ["INT_ADD", "register:40f0:8", ["const:b2a848:8", "const:4:8"]]
- 00b2a848 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b2ac70 ["INT_ADD", "register:40f0:8", ["const:b2ac70:8", "const:4:8"]]
+ 00b2ac70 ["CALL", null, ["callee:00c57e90:8"]]
- 00b2a848 bytes 92b40494
+ 00b2ac70 bytes 88b40494
- 00b2a890 ["INT_ADD", "register:40f0:8", ["const:b2a890:8", "const:4:8"]]
- 00b2a890 ["CALL", null, ["callee:0054075c:8"]]
+ 00b2acb8 ["INT_ADD", "register:40f0:8", ["const:b2acb8:8", "const:4:8"]]
+ 00b2acb8 ["CALL", null, ["callee:0054075c:8"]]
- 00b2a890 bytes a357e897
+ 00b2acb8 bytes a956e897
- 00b2a8a8 ["INT_ADD", "register:40f0:8", ["const:b2a8a8:8", "const:4:8"]]
- 00b2a8a8 ["CALL", null, ["callee:0080da5c:8"]]
+ 00b2acd0 ["INT_ADD", "register:40f0:8", ["const:b2acd0:8", "const:4:8"]]
+ 00b2acd0 ["CALL", null, ["callee:0080da5c:8"]]
- 00b2a8a8 bytes 5d8cf397
+ 00b2acd0 bytes 638bf397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-261f3a078a291aa438aaeaf58ddce345"></a>

### [`00b2a9b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a9b4.md) → [`00b2addc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2addc.md) FUN_00b2addc

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`005e8158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e8/005e8158.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005e8198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e8/005e8198.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2aa34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a9b4.md#insn-00b2aa34) · [`00b2aa68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a9b4.md#insn-00b2aa68) · [`00b2aa74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a9b4.md#insn-00b2aa74)
- 新版 `00b2ae5c`（命令位置の公開資料なし） · `00b2ae90`（命令位置の公開資料なし） · `00b2ae9c`（命令位置の公開資料なし）

~~~diff
- 00b2aa34 ["INT_ADD", "register:40f0:8", ["const:b2aa34:8", "const:4:8"]]
- 00b2aa34 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b2ae5c ["INT_ADD", "register:40f0:8", ["const:b2ae5c:8", "const:4:8"]]
+ 00b2ae5c ["CALL", null, ["callee:00c57e90:8"]]
- 00b2aa34 bytes 17b40494
+ 00b2ae5c bytes 0db40494
- 00b2aa68 ["INT_ADD", "register:40f0:8", ["const:b2aa68:8", "const:4:8"]]
- 00b2aa68 ["CALL", null, ["callee:005e8198:8"]]
+ 00b2ae90 ["INT_ADD", "register:40f0:8", ["const:b2ae90:8", "const:4:8"]]
+ 00b2ae90 ["CALL", null, ["callee:005e8198:8"]]
- 00b2aa68 bytes bcf5ea97
+ 00b2ae90 bytes c2f4ea97
- 00b2aa74 ["INT_ADD", "register:40f0:8", ["const:b2aa74:8", "const:4:8"]]
- 00b2aa74 ["CALL", null, ["callee:005e8198:8"]]
+ 00b2ae9c ["INT_ADD", "register:40f0:8", ["const:b2ae9c:8", "const:4:8"]]
+ 00b2ae9c ["CALL", null, ["callee:005e8198:8"]]
- 00b2aa74 bytes b9f5ea97
+ 00b2ae9c bytes bff4ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8509797accdf65a133081180170f6de"></a>

### [`00b2ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2ab20.md) → [`00b2af48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2af48.md) FUN_00b2af48

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 6件 [`00615e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/00615e8c.md) [`00652480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/00652480.md) [`0065250c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/0065250c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 6件 [`00615ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615ecc.md) [`006524c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00652/006524c0.md) [`0065254c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00652/0065254c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2ab98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2ab20.md#insn-00b2ab98) · [`00b2abbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2ab20.md#insn-00b2abbc) · [`00b2ac0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2ab20.md#insn-00b2ac0c)
- 新版 `00b2afc0`（命令位置の公開資料なし） · `00b2afe4`（命令位置の公開資料なし） · `00b2b034`（命令位置の公開資料なし）

~~~diff
- 00b2ab98 ["INT_ADD", "register:40f0:8", ["const:b2ab98:8", "const:4:8"]]
- 00b2ab98 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b2afc0 ["INT_ADD", "register:40f0:8", ["const:b2afc0:8", "const:4:8"]]
+ 00b2afc0 ["CALL", null, ["callee:00c57e90:8"]]
- 00b2ab98 bytes beb30494
+ 00b2afc0 bytes b4b30494
- 00b2abbc ["INT_ADD", "register:40f0:8", ["const:b2abbc:8", "const:4:8"]]
- 00b2abbc ["CALL", null, ["callee:0065254c:8"]]
+ 00b2afe4 ["INT_ADD", "register:40f0:8", ["const:b2afe4:8", "const:4:8"]]
+ 00b2afe4 ["CALL", null, ["callee:0065254c:8"]]
- 00b2abbc bytes 549eec97
+ 00b2afe4 bytes 5a9dec97
- 00b2ac0c ["INT_ADD", "register:40f0:8", ["const:b2ac0c:8", "const:4:8"]]
- 00b2ac0c ["CALL", null, ["callee:00615ecc:8"]]
+ 00b2b034 ["INT_ADD", "register:40f0:8", ["const:b2b034:8", "const:4:8"]]
+ 00b2b034 ["CALL", null, ["callee:00615ecc:8"]]
- 00b2ac0c bytes a0aceb97
+ 00b2b034 bytes a6abeb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a79c4f1e7e41460d5e455834b81d8054"></a>

### [`00b2ac48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2ac48.md) → [`00b2b070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b070.md) FUN_00b2b070

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 11件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00615e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/00615e8c.md) [`00652480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/00652480.md) [`0065250c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/0065250c.md) [`00b2aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2aecc.md)
- 新版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 11件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00615ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615ecc.md) [`006524c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00652/006524c0.md) [`0065254c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00652/0065254c.md) [`00b2b2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b2f4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2acec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2ac48.md#insn-00b2acec) · [`00b2ad4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2ac48.md#insn-00b2ad4c) · [`00b2ad70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2ac48.md#insn-00b2ad70)
- 新版 `00b2b114`（命令位置の公開資料なし） · `00b2b174`（命令位置の公開資料なし） · `00b2b198`（命令位置の公開資料なし）

~~~diff
- 00b2acec ["INT_ADD", "register:40f0:8", ["const:b2acec:8", "const:4:8"]]
- 00b2acec ["CALL", null, ["callee:00c57e90:8"]]
+ 00b2b114 ["INT_ADD", "register:40f0:8", ["const:b2b114:8", "const:4:8"]]
+ 00b2b114 ["CALL", null, ["callee:00c57e90:8"]]
- 00b2acec bytes 69b30494
+ 00b2b114 bytes 5fb30494
- 00b2ad4c ["INT_ADD", "register:40f0:8", ["const:b2ad4c:8", "const:4:8"]]
- 00b2ad4c ["CALL", null, ["callee:00c57e90:8"]]
+ 00b2b174 ["INT_ADD", "register:40f0:8", ["const:b2b174:8", "const:4:8"]]
+ 00b2b174 ["CALL", null, ["callee:00c57e90:8"]]
- 00b2ad4c bytes 51b30494
+ 00b2b174 bytes 47b30494
- 00b2ad70 ["INT_ADD", "register:40f0:8", ["const:b2ad70:8", "const:4:8"]]
- 00b2ad70 ["CALL", null, ["callee:0065254c:8"]]
+ 00b2b198 ["INT_ADD", "register:40f0:8", ["const:b2b198:8", "const:4:8"]]
+ 00b2b198 ["CALL", null, ["callee:0065254c:8"]]
- 00b2ad70 bytes e79dec97
+ 00b2b198 bytes ed9cec97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a86f33226ecfeeba2e0bd6f85fb2c5c5"></a>

### [`00b2aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2aecc.md) → [`00b2b2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b2f4.md) FUN_00b2b2f4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b2ac48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2ac48.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00b2b070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b070.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2af48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2aecc.md#insn-00b2af48) · [`00b2af90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2aecc.md#insn-00b2af90)
- 新版 `00b2b370`（命令位置の公開資料なし） · `00b2b3b8`（命令位置の公開資料なし）

~~~diff
- 00b2af48 ["INT_ADD", "register:40f0:8", ["const:b2af48:8", "const:4:8"]]
- 00b2af48 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b2b370 ["INT_ADD", "register:40f0:8", ["const:b2b370:8", "const:4:8"]]
+ 00b2b370 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b2af48 bytes dab20494
+ 00b2b370 bytes d0b20494
- 00b2af90 ["INT_ADD", "register:40f0:8", ["const:b2af90:8", "const:4:8"]]
- 00b2af90 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b2b3b8 ["INT_ADD", "register:40f0:8", ["const:b2b3b8:8", "const:4:8"]]
+ 00b2b3b8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b2af90 bytes c8b20494
+ 00b2b3b8 bytes beb20494
~~~


<a id="compare-638f3d5c4cd714b68dea794e0b81ab65"></a>

### [`00b2afe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2afe8.md) → [`00b2b410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b410.md) FUN_00b2b410

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b2ac48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2ac48.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00b2b070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b070.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2b01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2afe8.md#insn-00b2b01c) · [`00b2b06c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2afe8.md#insn-00b2b06c)
- 新版 `00b2b444`（命令位置の公開資料なし） · `00b2b494`（命令位置の公開資料なし）

~~~diff
- 00b2b01c ["INT_ADD", "register:40f0:8", ["const:b2b01c:8", "const:4:8"]]
- 00b2b01c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b2b444 ["INT_ADD", "register:40f0:8", ["const:b2b444:8", "const:4:8"]]
+ 00b2b444 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b2b01c bytes a5b20494
+ 00b2b444 bytes 9bb20494
- 00b2b06c ["INT_ADD", "register:40f0:8", ["const:b2b06c:8", "const:4:8"]]
- 00b2b06c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b2b494 ["INT_ADD", "register:40f0:8", ["const:b2b494:8", "const:4:8"]]
+ 00b2b494 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b2b06c bytes 91b20494
+ 00b2b494 bytes 87b20494
~~~


<a id="compare-387d9c5267477bc66d5039aca8d08a23"></a>

### [`00b2b7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b7a4.md) → [`00b2bbcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bbcc.md) FUN_00b2bbcc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0043b568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b568.md) [`0043b618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b618.md) · 呼出先 4件 [`0046ca64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca64.md) [`0046ca7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca7c.md) [`0046ca88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca88.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`0043b5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b5a8.md) [`0043b658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b658.md) · 呼出先 4件 [`0046caa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046caa4.md) [`0046cabc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cabc.md) [`0046cac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cac8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2b7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b7a4.md#insn-00b2b7b4) · [`00b2b7bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b7a4.md#insn-00b2b7bc) · [`00b2b7c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b7a4.md#insn-00b2b7c4)
- 新版 `00b2bbdc`（命令位置の公開資料なし） · `00b2bbe4`（命令位置の公開資料なし） · `00b2bbec`（命令位置の公開資料なし）

~~~diff
- 00b2b7b4 ["INT_ADD", "register:40f0:8", ["const:b2b7b4:8", "const:4:8"]]
- 00b2b7b4 ["CALL", null, ["callee:008514f8:8"]]
+ 00b2bbdc ["INT_ADD", "register:40f0:8", ["const:b2bbdc:8", "const:4:8"]]
+ 00b2bbdc ["CALL", null, ["callee:008514f8:8"]]
- 00b2b7b4 bytes 4197f497
+ 00b2bbdc bytes 4796f497
- 00b2b7bc ["INT_ADD", "register:40f0:8", ["const:b2b7bc:8", "const:4:8"]]
- 00b2b7bc ["CALL", null, ["callee:0046cabc:8"]]
+ 00b2bbe4 ["INT_ADD", "register:40f0:8", ["const:b2bbe4:8", "const:4:8"]]
+ 00b2bbe4 ["CALL", null, ["callee:0046cabc:8"]]
- 00b2b7bc bytes b004e597
+ 00b2bbe4 bytes b603e597
- 00b2b7c4 ["INT_ADD", "register:40f0:8", ["const:b2b7c4:8", "const:4:8"]]
- 00b2b7c4 ["CALL", null, ["callee:008514f8:8"]]
+ 00b2bbec ["INT_ADD", "register:40f0:8", ["const:b2bbec:8", "const:4:8"]]
+ 00b2bbec ["CALL", null, ["callee:008514f8:8"]]
- 00b2b7c4 bytes 3d97f497
+ 00b2bbec bytes 4396f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b170c07e7d52bf4be80abb5e42f4162"></a>

### [`00b2b80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b80c.md) → [`00b2bc34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bc34.md) FUN_00b2bc34

採用 · 移動量 `+0x428` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0043b3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b3e8.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`0043b428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b428.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2b81c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b80c.md#insn-00b2b81c)
- 新版 `00b2bc44`（命令位置の公開資料なし）

~~~diff
- 00b2b81c ["INT_ADD", "register:40f0:8", ["const:b2b81c:8", "const:4:8"]]
- 00b2b81c ["CALL", null, ["callee:008514f8:8"]]
+ 00b2bc44 ["INT_ADD", "register:40f0:8", ["const:b2bc44:8", "const:4:8"]]
+ 00b2bc44 ["CALL", null, ["callee:008514f8:8"]]
- 00b2b81c bytes 2797f497
+ 00b2bc44 bytes 2d96f497
~~~


<a id="compare-49ccadf55e08025b8e3374a00dbbeaf1"></a>

### [`00b2ce34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ce34.md) → [`00b2d25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d25c.md) FUN_00b2d25c

採用 · 移動量 `+0x428` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0043b328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b328.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`0043b368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b368.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2ce50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ce34.md#insn-00b2ce50)
- 新版 `00b2d278`（命令位置の公開資料なし）

~~~diff
- 00b2ce50 ["INT_ADD", "register:40f0:8", ["const:b2ce50:8", "const:4:8"]]
- 00b2ce50 ["CALL", null, ["callee:008514f8:8"]]
+ 00b2d278 ["INT_ADD", "register:40f0:8", ["const:b2d278:8", "const:4:8"]]
+ 00b2d278 ["CALL", null, ["callee:008514f8:8"]]
- 00b2ce50 bytes 9a91f497
+ 00b2d278 bytes a090f497
~~~


<a id="compare-a036c75071bdfaddf75d92f2b130c309"></a>

### [`00b2ce7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ce7c.md) → [`00b2d2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d2a4.md) FUN_00b2d2a4

採用 · 移動量 `+0x428` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0043b328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b328.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`0043b368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b368.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2ce98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ce7c.md#insn-00b2ce98)
- 新版 `00b2d2c0`（命令位置の公開資料なし）

~~~diff
- 00b2ce98 ["INT_ADD", "register:40f0:8", ["const:b2ce98:8", "const:4:8"]]
- 00b2ce98 ["CALL", null, ["callee:008514f8:8"]]
+ 00b2d2c0 ["INT_ADD", "register:40f0:8", ["const:b2d2c0:8", "const:4:8"]]
+ 00b2d2c0 ["CALL", null, ["callee:008514f8:8"]]
- 00b2ce98 bytes 8891f497
+ 00b2d2c0 bytes 8e90f497
~~~


<a id="compare-ce6c91b0620c52cefbad4af3bcb881e8"></a>

### [`00b2cec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cec4.md) → [`00b2d2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d2ec.md) FUN_00b2d2ec

採用 · 移動量 `+0x428` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0043b328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b328.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`0043b368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b368.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2cee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cec4.md#insn-00b2cee0)
- 新版 `00b2d308`（命令位置の公開資料なし）

~~~diff
- 00b2cee0 ["INT_ADD", "register:40f0:8", ["const:b2cee0:8", "const:4:8"]]
- 00b2cee0 ["CALL", null, ["callee:008514f8:8"]]
+ 00b2d308 ["INT_ADD", "register:40f0:8", ["const:b2d308:8", "const:4:8"]]
+ 00b2d308 ["CALL", null, ["callee:008514f8:8"]]
- 00b2cee0 bytes 7691f497
+ 00b2d308 bytes 7c90f497
~~~


<a id="compare-796c29c4fe1cb15c46a054d0bbf3c58a"></a>

### [`00b2cfec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cfec.md) → [`00b2d414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d414.md) FUN_00b2d414

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2cff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cfec.md#insn-00b2cff4)
- 新版 `00b2d41c`（命令位置の公開資料なし）

~~~diff
- 00b2cff4 ["INT_ADD", "register:40f0:8", ["const:b2cff4:8", "const:4:8"]]
- 00b2cff4 ["CALL", null, ["callee:008514f8:8"]]
+ 00b2d41c ["INT_ADD", "register:40f0:8", ["const:b2d41c:8", "const:4:8"]]
+ 00b2d41c ["CALL", null, ["callee:008514f8:8"]]
- 00b2cff4 bytes 3191f497
+ 00b2d41c bytes 3790f497
~~~


<a id="compare-1701495d38ab06e733d3980a855600a2"></a>

### [`00b2d070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d070.md) → [`00b2d498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d498.md) FUN_00b2d498

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2d078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d070.md#insn-00b2d078)
- 新版 `00b2d4a0`（命令位置の公開資料なし）

~~~diff
- 00b2d078 ["INT_ADD", "register:40f0:8", ["const:b2d078:8", "const:4:8"]]
- 00b2d078 ["CALL", null, ["callee:008514f8:8"]]
+ 00b2d4a0 ["INT_ADD", "register:40f0:8", ["const:b2d4a0:8", "const:4:8"]]
+ 00b2d4a0 ["CALL", null, ["callee:008514f8:8"]]
- 00b2d078 bytes 1091f497
+ 00b2d4a0 bytes 1690f497
~~~


<a id="compare-31fd22ca6feee6c5e0589a3b4b72fb57"></a>

### [`00b2d3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d3fc.md) → [`00b2d824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d824.md) FUN_00b2d824

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b2c028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2c028.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00b2c450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c450.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2d41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d3fc.md#insn-00b2d41c)
- 新版 `00b2d844`（命令位置の公開資料なし）

~~~diff
- 00b2d41c ["INT_ADD", "register:40f0:8", ["const:b2d41c:8", "const:4:8"]]
- 00b2d41c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b2d844 ["INT_ADD", "register:40f0:8", ["const:b2d844:8", "const:4:8"]]
+ 00b2d844 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b2d41c bytes a5a90494
+ 00b2d844 bytes 9ba90494
~~~


<a id="compare-9a78733e482d5586ed721a08c425cd3c"></a>

### [`00b2f458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f458.md) → [`00b2f880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f880.md) FUN_00b2f880

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 19件 [`0060a860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060a/0060a860.md) [`00664a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664a4c.md) [`00664b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664b8c.md) [`00664be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664be8.md) [`006650d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/006650d0.md) · 呼出先 1件 [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md)
- 新版 呼出元 19件 [`0060a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060a/0060a8a0.md) [`00664a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664a8c.md) [`00664bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664bcc.md) [`00664c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664c28.md) [`00665110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00665/00665110.md) · 呼出先 1件 [`00b3be94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be94.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2f460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f458.md#insn-00b2f460)
- 新版 `00b2f888`（命令位置の公開資料なし）

~~~diff
- 00b2f460 ["INT_ADD", "register:40f0:8", ["const:b2f460:8", "const:4:8"]]
- 00b2f460 ["CALL", null, ["callee:00b3be94:8"]]
+ 00b2f888 ["INT_ADD", "register:40f0:8", ["const:b2f888:8", "const:4:8"]]
+ 00b2f888 ["CALL", null, ["callee:00b3be94:8"]]
- 00b2f460 bytes 83310094
+ 00b2f888 bytes 83310094
~~~


<a id="compare-bc22c60226e528ab6267f912ba0e1b1b"></a>

### [`00b2f590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f590.md) → [`00b2f9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f9b8.md) FUN_00b2f9b8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 32件 [`005afc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afc38.md) [`005fdc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fd/005fdc18.md) [`0063d8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063d8d4.md) [`0064a4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064a/0064a4f0.md) [`00653560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/00653560.md) · 呼出先 1件 [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md)
- 新版 呼出元 32件 [`005afc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afc78.md) [`005fdc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fd/005fdc58.md) [`0063d914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063d/0063d914.md) [`0064a530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064a/0064a530.md) [`006535a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00653/006535a0.md) · 呼出先 1件 [`00b3be94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be94.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2f5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f590.md#insn-00b2f5a4) · [`00b2f5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f590.md#insn-00b2f5c0)
- 新版 `00b2f9cc`（命令位置の公開資料なし） · `00b2f9e8`（命令位置の公開資料なし）

~~~diff
- 00b2f5a4 ["INT_ADD", "register:40f0:8", ["const:b2f5a4:8", "const:4:8"]]
- 00b2f5a4 ["CALL", null, ["callee:00b3be94:8"]]
+ 00b2f9cc ["INT_ADD", "register:40f0:8", ["const:b2f9cc:8", "const:4:8"]]
+ 00b2f9cc ["CALL", null, ["callee:00b3be94:8"]]
- 00b2f5a4 bytes 32310094
+ 00b2f9cc bytes 32310094
- 00b2f5c0 ["INT_ADD", "register:40f0:8", ["const:b2f5c0:8", "const:4:8"]]
- 00b2f5c0 ["CALL", null, ["callee:00b3be94:8"]]
+ 00b2f9e8 ["INT_ADD", "register:40f0:8", ["const:b2f9e8:8", "const:4:8"]]
+ 00b2f9e8 ["CALL", null, ["callee:00b3be94:8"]]
- 00b2f5c0 bytes 2b310094
+ 00b2f9e8 bytes 2b310094
~~~


<a id="compare-2f640c760f8fef1a1e737836884ca4eb"></a>

### [`00b342d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b342d8.md) → [`00b34700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34700.md) FUN_00b34700

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b342f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b342d8.md#insn-00b342f4) · [`00b34330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b342d8.md#insn-00b34330) · [`00b34340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b342d8.md#insn-00b34340)
- 新版 `00b3471c`（命令位置の公開資料なし） · `00b34758`（命令位置の公開資料なし） · `00b34768`（命令位置の公開資料なし）

~~~diff
- 00b342f4 ["INT_ADD", "register:40f0:8", ["const:b342f4:8", "const:4:8"]]
- 00b342f4 ["CALL", null, ["callee:0046d490:8"]]
+ 00b3471c ["INT_ADD", "register:40f0:8", ["const:b3471c:8", "const:4:8"]]
+ 00b3471c ["CALL", null, ["callee:0046d490:8"]]
- 00b342f4 bytes 57e4e497
+ 00b3471c bytes 5de3e497
- 00b34330 ["INT_ADD", "register:40f0:8", ["const:b34330:8", "const:4:8"]]
- 00b34330 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b34758 ["INT_ADD", "register:40f0:8", ["const:b34758:8", "const:4:8"]]
+ 00b34758 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b34330 bytes e08d0494
+ 00b34758 bytes d68d0494
- 00b34340 ["INT_ADD", "register:40f0:8", ["const:b34340:8", "const:4:8"]]
- 00b34340 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b34768 ["INT_ADD", "register:40f0:8", ["const:b34768:8", "const:4:8"]]
+ 00b34768 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b34340 bytes dc8d0494
+ 00b34768 bytes d28d0494
~~~


<a id="compare-5c84e3f2efd560652ecd7af3aae2ec21"></a>

### [`00b34370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34370.md) → [`00b34798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34798.md) FUN_00b34798

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b33e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33e58.md) [`00b365cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b365cc.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`00b34280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34280.md) [`00b369f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b369f4.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b343dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34370.md#insn-00b343dc) · [`00b343ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34370.md#insn-00b343ec) · [`00b3440c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34370.md#insn-00b3440c)
- 新版 `00b34804`（命令位置の公開資料なし） · `00b34814`（命令位置の公開資料なし） · `00b34834`（命令位置の公開資料なし）

~~~diff
- 00b343dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b343dc ["INT_ADD", "register:40f0:8", ["const:b343dc:8", "const:4:8"]]
- 00b343dc ["CALLIND", null, ["register:0:8"]]
+ 00b34804 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b34804 ["INT_ADD", "register:40f0:8", ["const:b34804:8", "const:4:8"]]
+ 00b34804 ["CALLIND", null, ["register:0:8"]]
- 00b343dc bytes 00013fd6
+ 00b34804 bytes 00013fd6
- 00b343ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00b343ec ["INT_ADD", "register:40f0:8", ["const:b343ec:8", "const:4:8"]]
- 00b343ec ["CALLIND", null, ["register:0:8"]]
+ 00b34814 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b34814 ["INT_ADD", "register:40f0:8", ["const:b34814:8", "const:4:8"]]
+ 00b34814 ["CALLIND", null, ["register:0:8"]]
- 00b343ec bytes 00013fd6
+ 00b34814 bytes 00013fd6
- 00b3440c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b3440c ["INT_ADD", "register:40f0:8", ["const:b3440c:8", "const:4:8"]]
- 00b3440c ["CALLIND", null, ["register:0:8"]]
+ 00b34834 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b34834 ["INT_ADD", "register:40f0:8", ["const:b34834:8", "const:4:8"]]
+ 00b34834 ["CALLIND", null, ["register:0:8"]]
- 00b3440c bytes 00013fd6
+ 00b34834 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fbb00cf3954c32b379b8e8dc3067f01"></a>

### [`00b344d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b344d8.md) → [`00b34900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34900.md) FUN_00b34900

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b33f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33f20.md) [`00b36694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36694.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`00b34348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34348.md) [`00b36abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b36abc.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b34544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b344d8.md#insn-00b34544) · [`00b34554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b344d8.md#insn-00b34554) · [`00b34574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b344d8.md#insn-00b34574)
- 新版 `00b3496c`（命令位置の公開資料なし） · `00b3497c`（命令位置の公開資料なし） · `00b3499c`（命令位置の公開資料なし）

~~~diff
- 00b34544 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b34544 ["INT_ADD", "register:40f0:8", ["const:b34544:8", "const:4:8"]]
- 00b34544 ["CALLIND", null, ["register:0:8"]]
+ 00b3496c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b3496c ["INT_ADD", "register:40f0:8", ["const:b3496c:8", "const:4:8"]]
+ 00b3496c ["CALLIND", null, ["register:0:8"]]
- 00b34544 bytes 00013fd6
+ 00b3496c bytes 00013fd6
- 00b34554 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b34554 ["INT_ADD", "register:40f0:8", ["const:b34554:8", "const:4:8"]]
- 00b34554 ["CALLIND", null, ["register:0:8"]]
+ 00b3497c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b3497c ["INT_ADD", "register:40f0:8", ["const:b3497c:8", "const:4:8"]]
+ 00b3497c ["CALLIND", null, ["register:0:8"]]
- 00b34554 bytes 00013fd6
+ 00b3497c bytes 00013fd6
- 00b34574 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b34574 ["INT_ADD", "register:40f0:8", ["const:b34574:8", "const:4:8"]]
- 00b34574 ["CALLIND", null, ["register:0:8"]]
+ 00b3499c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b3499c ["INT_ADD", "register:40f0:8", ["const:b3499c:8", "const:4:8"]]
+ 00b3499c ["CALLIND", null, ["register:0:8"]]
- 00b34574 bytes 00013fd6
+ 00b3499c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-260742b5c49a50f0b0887dc85da731e5"></a>

### [`00b34640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34640.md) → [`00b34a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34a68.md) FUN_00b34a68

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b33fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33fe8.md) · 呼出先 9件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00b34410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34410.md) · 呼出先 9件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b346e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34640.md#insn-00b346e0) · [`00b34704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34640.md#insn-00b34704) · [`00b34748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34640.md#insn-00b34748)
- 新版 `00b34b08`（命令位置の公開資料なし） · `00b34b2c`（命令位置の公開資料なし） · `00b34b70`（命令位置の公開資料なし）

~~~diff
- 00b346e0 ["INT_ADD", "register:40f0:8", ["const:b346e0:8", "const:4:8"]]
- 00b346e0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b34b08 ["INT_ADD", "register:40f0:8", ["const:b34b08:8", "const:4:8"]]
+ 00b34b08 ["CALL", null, ["callee:00c57e90:8"]]
- 00b346e0 bytes ec8c0494
+ 00b34b08 bytes e28c0494
- 00b34704 ["INT_ADD", "register:40f0:8", ["const:b34704:8", "const:4:8"]]
- 00b34704 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00b34b2c ["INT_ADD", "register:40f0:8", ["const:b34b2c:8", "const:4:8"]]
+ 00b34b2c ["CALL", null, ["callee:00c57fe0:8"]]
- 00b34704 bytes 378d0494
+ 00b34b2c bytes 2d8d0494
- 00b34748 ["INT_ADD", "register:40f0:8", ["const:b34748:8", "const:4:8"]]
- 00b34748 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b34b70 ["INT_ADD", "register:40f0:8", ["const:b34b70:8", "const:4:8"]]
+ 00b34b70 ["CALL", null, ["callee:00c57e90:8"]]
- 00b34748 bytes d28c0494
+ 00b34b70 bytes c88c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0448856f047f9cd1399a1ad5bc2be5f2"></a>

### [`00b3483c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b3483c.md) → [`00b34c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34c64.md) FUN_00b34c64

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b33fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33fe8.md) · 呼出先 9件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00b34410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34410.md) · 呼出先 9件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b348dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b3483c.md#insn-00b348dc) · [`00b34900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b3483c.md#insn-00b34900) · [`00b34944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b3483c.md#insn-00b34944)
- 新版 `00b34d04`（命令位置の公開資料なし） · `00b34d28`（命令位置の公開資料なし） · `00b34d6c`（命令位置の公開資料なし）

~~~diff
- 00b348dc ["INT_ADD", "register:40f0:8", ["const:b348dc:8", "const:4:8"]]
- 00b348dc ["CALL", null, ["callee:00c57e90:8"]]
+ 00b34d04 ["INT_ADD", "register:40f0:8", ["const:b34d04:8", "const:4:8"]]
+ 00b34d04 ["CALL", null, ["callee:00c57e90:8"]]
- 00b348dc bytes 6d8c0494
+ 00b34d04 bytes 638c0494
- 00b34900 ["INT_ADD", "register:40f0:8", ["const:b34900:8", "const:4:8"]]
- 00b34900 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00b34d28 ["INT_ADD", "register:40f0:8", ["const:b34d28:8", "const:4:8"]]
+ 00b34d28 ["CALL", null, ["callee:00c57fe0:8"]]
- 00b34900 bytes b88c0494
+ 00b34d28 bytes ae8c0494
- 00b34944 ["INT_ADD", "register:40f0:8", ["const:b34944:8", "const:4:8"]]
- 00b34944 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b34d6c ["INT_ADD", "register:40f0:8", ["const:b34d6c:8", "const:4:8"]]
+ 00b34d6c ["CALL", null, ["callee:00c57e90:8"]]
- 00b34944 bytes 538c0494
+ 00b34d6c bytes 498c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-518c289681eb1bea4cc6e9e648ca7748"></a>

### [`00b35a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35a50.md) → [`00b35e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35e78.md) FUN_00b35e78

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b358dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b358dc.md) [`00b35a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35a50.md) · 呼出先 2件 [`00b35a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35a50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00b35d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35d04.md) [`00b35e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35e78.md) · 呼出先 2件 [`00b35e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b35e78.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b35a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35a50.md#insn-00b35a6c) · [`00b35a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35a50.md#insn-00b35a78) · [`00b35aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35a50.md#insn-00b35aac)
- 新版 `00b35e94`（命令位置の公開資料なし） · `00b35ea0`（命令位置の公開資料なし） · `00b35ed4`（命令位置の公開資料なし）

~~~diff
- 00b35a6c ["INT_ADD", "register:40f0:8", ["const:b35a6c:8", "const:4:8"]]
- 00b35a6c ["CALL", null, ["local:b0:8"]]
+ 00b35e94 ["INT_ADD", "register:40f0:8", ["const:b35e94:8", "const:4:8"]]
+ 00b35e94 ["CALL", null, ["local:b0:8"]]
- 00b35a6c bytes f9ffff97
+ 00b35e94 bytes f9ffff97
- 00b35a78 ["INT_ADD", "register:40f0:8", ["const:b35a78:8", "const:4:8"]]
- 00b35a78 ["CALL", null, ["local:b0:8"]]
+ 00b35ea0 ["INT_ADD", "register:40f0:8", ["const:b35ea0:8", "const:4:8"]]
+ 00b35ea0 ["CALL", null, ["local:b0:8"]]
- 00b35a78 bytes f6ffff97
+ 00b35ea0 bytes f6ffff97
- 00b35aac ["COPY", "register:0:8", ["register:4040:8"]]
- 00b35aac ["INT_ADD", "register:40f0:8", ["const:b35aac:8", "const:4:8"]]
- 00b35aac ["CALLIND", null, ["register:0:8"]]
+ 00b35ed4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b35ed4 ["INT_ADD", "register:40f0:8", ["const:b35ed4:8", "const:4:8"]]
+ 00b35ed4 ["CALLIND", null, ["register:0:8"]]
- 00b35aac bytes 00013fd6
+ 00b35ed4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f30dabdda387feac3c5a621a7d90b50a"></a>

### [`00b36ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36ed0.md) → [`00b372f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b372f8.md) FUN_00b372f8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b38a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b38a60.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00b38e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b38/00b38e88.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b36f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36ed0.md#insn-00b36f0c) · [`00b36f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36ed0.md#insn-00b36f3c) · [`00b36f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36ed0.md#insn-00b36f6c)
- 新版 `00b37334`（命令位置の公開資料なし） · `00b37364`（命令位置の公開資料なし） · `00b37394`（命令位置の公開資料なし）

~~~diff
- 00b36f0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b36f0c ["INT_ADD", "register:40f0:8", ["const:b36f0c:8", "const:4:8"]]
- 00b36f0c ["CALLIND", null, ["register:0:8"]]
+ 00b37334 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b37334 ["INT_ADD", "register:40f0:8", ["const:b37334:8", "const:4:8"]]
+ 00b37334 ["CALLIND", null, ["register:0:8"]]
- 00b36f0c bytes 00013fd6
+ 00b37334 bytes 00013fd6
- 00b36f3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b36f3c ["INT_ADD", "register:40f0:8", ["const:b36f3c:8", "const:4:8"]]
- 00b36f3c ["CALLIND", null, ["register:0:8"]]
+ 00b37364 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b37364 ["INT_ADD", "register:40f0:8", ["const:b37364:8", "const:4:8"]]
+ 00b37364 ["CALLIND", null, ["register:0:8"]]
- 00b36f3c bytes 00013fd6
+ 00b37364 bytes 00013fd6
- 00b36f6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b36f6c ["INT_ADD", "register:40f0:8", ["const:b36f6c:8", "const:4:8"]]
- 00b36f6c ["CALLIND", null, ["register:0:8"]]
+ 00b37394 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b37394 ["INT_ADD", "register:40f0:8", ["const:b37394:8", "const:4:8"]]
+ 00b37394 ["CALLIND", null, ["register:0:8"]]
- 00b36f6c bytes 00013fd6
+ 00b37394 bytes 00013fd6
~~~


<a id="compare-f579d2f97230652020ae9f02db5b8dc6"></a>

### [`00b3fa7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fa7c.md) → [`00b3fea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3fea4.md) FUN_00b3fea4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b3ff84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ff84.md) · 呼出先 2件 [`00c5a540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a540.md) [`00c5a860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a860.md)
- 新版 呼出元 1件 [`00b403ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b403ac.md) · 呼出先 2件 [`00c5a940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a940.md) [`00c5ac60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3fa8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fa7c.md#insn-00b3fa8c)
- 新版 `00b3feb4`（命令位置の公開資料なし）

~~~diff
- 00b3fa8c ["INT_ADD", "register:40f0:8", ["const:b3fa8c:8", "const:4:8"]]
- 00b3fa8c ["CALL", null, ["callee:00c5ac60:8"]]
+ 00b3feb4 ["INT_ADD", "register:40f0:8", ["const:b3feb4:8", "const:4:8"]]
+ 00b3feb4 ["CALL", null, ["callee:00c5ac60:8"]]
- 00b3fa8c bytes 756b0494
+ 00b3feb4 bytes 6b6b0494
~~~


<a id="compare-d2259e4650796011a32c679199b82ed7"></a>

### [`00b40c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40c80.md) → [`00b410a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b410a8.md) _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b40cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40c80.md#insn-00b40cf4) · [`00b40d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40c80.md#insn-00b40d18)
- 新版 `00b4111c`（命令位置の公開資料なし） · `00b41140`（命令位置の公開資料なし）

~~~diff
- 00b40cf4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b40cf4 ["INT_ADD", "register:40f0:8", ["const:b40cf4:8", "const:4:8"]]
- 00b40cf4 ["CALLIND", null, ["register:0:8"]]
+ 00b4111c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4111c ["INT_ADD", "register:40f0:8", ["const:b4111c:8", "const:4:8"]]
+ 00b4111c ["CALLIND", null, ["register:0:8"]]
- 00b40cf4 bytes 00013fd6
+ 00b4111c bytes 00013fd6
- 00b40d18 ["INT_ADD", "register:40f0:8", ["const:b40d18:8", "const:4:8"]]
- 00b40d18 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00b41140 ["INT_ADD", "register:40f0:8", ["const:b41140:8", "const:4:8"]]
+ 00b41140 ["CALL", null, ["callee:00c57ee0:8"]]
- 00b40d18 bytes 725b0494
+ 00b41140 bytes 685b0494
~~~


<a id="compare-075c7712fe6bede60586443b509e69f0"></a>

### [`00b4221c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b4221c.md) → [`00b42644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42644.md) _ZN8firebase6FutureIvEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5a9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9d0.md) · 呼出先 3件 [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9f0.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)
- 新版 呼出元 1件 [`00c5add0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5add0.md) · 呼出先 3件 [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5adf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5adf0.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4223c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b4221c.md#insn-00b4223c) · [`00b42250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b4221c.md#insn-00b42250) · [`00b42264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b4221c.md#insn-00b42264)
- 新版 `00b42664`（命令位置の公開資料なし） · `00b42678`（命令位置の公開資料なし） · `00b4268c`（命令位置の公開資料なし）

~~~diff
- 00b4223c ["INT_ADD", "register:40f0:8", ["const:b4223c:8", "const:4:8"]]
- 00b4223c ["CALL", null, ["callee:00c5ac70:8"]]
+ 00b42664 ["INT_ADD", "register:40f0:8", ["const:b42664:8", "const:4:8"]]
+ 00b42664 ["CALL", null, ["callee:00c5ac70:8"]]
- 00b4223c bytes 8d610494
+ 00b42664 bytes 83610494
- 00b42250 ["INT_ADD", "register:40f0:8", ["const:b42250:8", "const:4:8"]]
- 00b42250 ["CALL", null, ["callee:00c5ae00:8"]]
+ 00b42678 ["INT_ADD", "register:40f0:8", ["const:b42678:8", "const:4:8"]]
+ 00b42678 ["CALL", null, ["callee:00c5ae00:8"]]
- 00b42250 bytes ec610494
+ 00b42678 bytes e2610494
- 00b42264 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b42264 ["INT_ADD", "register:40f0:8", ["const:b42264:8", "const:4:8"]]
- 00b42264 ["CALLIND", null, ["register:0:8"]]
+ 00b4268c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4268c ["INT_ADD", "register:40f0:8", ["const:b4268c:8", "const:4:8"]]
+ 00b4268c ["CALLIND", null, ["register:0:8"]]
- 00b42264 bytes 00013fd6
+ 00b4268c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04f713b6d30bdaa550aae747b7063597"></a>

### [`00b43cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43cf8.md) → [`00b44120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44120.md) FUN_00b44120

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00b43d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43d28.md) [`00b44224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44224.md) [`00b44250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44250.md) · 呼出先 2件 [`00b44298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44298.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 3件 [`00b44150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44150.md) [`00b4464c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b4464c.md) [`00b44678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44678.md) · 呼出先 2件 [`00b446c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b446c0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b43d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43cf8.md#insn-00b43d0c) · [`00b43d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43cf8.md#insn-00b43d24)
- 新版 `00b44134`（命令位置の公開資料なし） · `00b4414c`（命令位置の公開資料なし）

~~~diff
- 00b43d0c ["INT_ADD", "register:40f0:8", ["const:b43d0c:8", "const:4:8"]]
- 00b43d0c ["CALL", null, ["callee:00b446c0:8"]]
+ 00b44134 ["INT_ADD", "register:40f0:8", ["const:b44134:8", "const:4:8"]]
+ 00b44134 ["CALL", null, ["callee:00b446c0:8"]]
- 00b43d0c bytes 63010094
+ 00b44134 bytes 63010094
- 00b43d24 ["INT_ADD", "register:40f0:8", ["const:b43d24:8", "const:4:8"]]
- 00b43d24 ["CALL", null, ["callee:00c5b140:8"]]
+ 00b4414c ["INT_ADD", "register:40f0:8", ["const:b4414c:8", "const:4:8"]]
+ 00b4414c ["CALL", null, ["callee:00c5b140:8"]]
- 00b43d24 bytes 075c0494
+ 00b4414c bytes fd5b0494
~~~


<a id="compare-9f07c9f1febe4646549d48dc7e1981e9"></a>

### [`00b44378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44378.md) → [`00b447a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b447a0.md) _ZN8firebase18AndroidLogMessageVEiPKcS1_St9__va_list

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5adf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5adf0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b1f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b443a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44378.md#insn-00b443a0) · [`00b443c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44378.md#insn-00b443c4)
- 新版 `00b447c8`（命令位置の公開資料なし） · `00b447ec`（命令位置の公開資料なし）

~~~diff
- 00b443a0 ["INT_ADD", "register:40f0:8", ["const:b443a0:8", "const:4:8"]]
- 00b443a0 ["CALL", null, ["callee:00c5b1f0:8"]]
+ 00b447c8 ["INT_ADD", "register:40f0:8", ["const:b447c8:8", "const:4:8"]]
+ 00b447c8 ["CALL", null, ["callee:00c5b1f0:8"]]
- 00b443a0 bytes 945a0494
+ 00b447c8 bytes 8a5a0494
- 00b443c4 ["INT_ADD", "register:40f0:8", ["const:b443c4:8", "const:4:8"]]
- 00b443c4 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00b447ec ["INT_ADD", "register:40f0:8", ["const:b447ec:8", "const:4:8"]]
+ 00b447ec ["CALL", null, ["callee:00c57ee0:8"]]
- 00b443c4 bytes c74d0494
+ 00b447ec bytes bd4d0494
~~~


<a id="compare-c9637b146c7b6fe67322cc516673d792"></a>

### [`00b51378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51378.md) → [`00b517a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b517a0.md) FUN_00b517a0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b4491c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b4491c.md) [`00b44c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44c34.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ad50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad50.md)
- 新版 呼出元 2件 [`00b44d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44d44.md) [`00b4505c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b4505c.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b513e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51378.md#insn-00b513e8) · [`00b5140c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51378.md#insn-00b5140c)
- 新版 `00b51810`（命令位置の公開資料なし） · `00b51834`（命令位置の公開資料なし）

~~~diff
- 00b513e8 ["INT_ADD", "register:40f0:8", ["const:b513e8:8", "const:4:8"]]
- 00b513e8 ["CALL", null, ["callee:00c5b150:8"]]
+ 00b51810 ["INT_ADD", "register:40f0:8", ["const:b51810:8", "const:4:8"]]
+ 00b51810 ["CALL", null, ["callee:00c5b150:8"]]
- 00b513e8 bytes 5a260494
+ 00b51810 bytes 50260494
- 00b5140c ["INT_ADD", "register:40f0:8", ["const:b5140c:8", "const:4:8"]]
- 00b5140c ["CALL", null, ["callee:00c57ee0:8"]]
+ 00b51834 ["INT_ADD", "register:40f0:8", ["const:b51834:8", "const:4:8"]]
+ 00b51834 ["CALL", null, ["callee:00c57ee0:8"]]
- 00b5140c bytes b5190494
+ 00b51834 bytes ab190494
~~~


<a id="compare-7aa483063de25d77fda85c53bd61bb94"></a>

### [`00b5aa54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5aa54.md) → [`00b5ae7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5ae7c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b410.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5b810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b810.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5aaec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5aa54.md#insn-00b5aaec) · [`00b5ab34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5aa54.md#insn-00b5ab34)
- 新版 `00b5af14`（命令位置の公開資料なし） · `00b5af5c`（命令位置の公開資料なし）

~~~diff
- 00b5aaec ["INT_ADD", "register:40f0:8", ["const:b5aaec:8", "const:4:8"]]
- 00b5aaec ["CALL", null, ["callee:00c58050:8"]]
+ 00b5af14 ["INT_ADD", "register:40f0:8", ["const:b5af14:8", "const:4:8"]]
+ 00b5af14 ["CALL", null, ["callee:00c58050:8"]]
- 00b5aaec bytes 59f40394
+ 00b5af14 bytes 4ff40394
- 00b5ab34 ["INT_ADD", "register:40f0:8", ["const:b5ab34:8", "const:4:8"]]
- 00b5ab34 ["CALL", null, ["callee:00c58050:8"]]
+ 00b5af5c ["INT_ADD", "register:40f0:8", ["const:b5af5c:8", "const:4:8"]]
+ 00b5af5c ["CALL", null, ["callee:00c58050:8"]]
- 00b5ab34 bytes 47f40394
+ 00b5af5c bytes 3df40394
~~~


<a id="compare-a669eee3072a179df0de643dedb8e2ed"></a>

### [`00b5ab68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ab68.md) → [`00b5af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5af90.md) _ZNSt6__ndk16vectorIPN8firebase3AppENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b440.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5b840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b840.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5abcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ab68.md#insn-00b5abcc) · [`00b5abd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ab68.md#insn-00b5abd8) · [`00b5ac04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ab68.md#insn-00b5ac04)
- 新版 `00b5aff4`（命令位置の公開資料なし） · `00b5b000`（命令位置の公開資料なし） · `00b5b02c`（命令位置の公開資料なし）

~~~diff
- 00b5abcc ["INT_ADD", "register:40f0:8", ["const:b5abcc:8", "const:4:8"]]
- 00b5abcc ["CALL", null, ["callee:00c5b140:8"]]
+ 00b5aff4 ["INT_ADD", "register:40f0:8", ["const:b5aff4:8", "const:4:8"]]
+ 00b5aff4 ["CALL", null, ["callee:00c5b140:8"]]
- 00b5abcc bytes 5d000494
+ 00b5aff4 bytes 53000494
- 00b5abd8 ["INT_ADD", "register:40f0:8", ["const:b5abd8:8", "const:4:8"]]
- 00b5abd8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b5b000 ["INT_ADD", "register:40f0:8", ["const:b5b000:8", "const:4:8"]]
+ 00b5b000 ["CALL", null, ["callee:00c57e90:8"]]
- 00b5abd8 bytes aef30394
+ 00b5b000 bytes a4f30394
- 00b5ac04 ["INT_ADD", "register:40f0:8", ["const:b5ac04:8", "const:4:8"]]
- 00b5ac04 ["CALL", null, ["callee:00c58000:8"]]
+ 00b5b02c ["INT_ADD", "register:40f0:8", ["const:b5b02c:8", "const:4:8"]]
+ 00b5b02c ["CALL", null, ["callee:00c58000:8"]]
- 00b5ac04 bytes fff30394
+ 00b5b02c bytes f5f30394
~~~


<a id="compare-42f5e39de15a44d4de9aa41026db1003"></a>

### [`00b5ac50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ac50.md) → [`00b5b078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b078.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b420.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a830.md) [`00c5ad60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad60.md) [`00c5b1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1d0.md)
- 新版 呼出元 1件 [`00c5b820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b820.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ac30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac30.md) [`00c5b160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b160.md) [`00c5b5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5accc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ac50.md#insn-00b5accc) · [`00b5ace0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ac50.md#insn-00b5ace0) · [`00b5ace8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ac50.md#insn-00b5ace8)
- 新版 `00b5b0f4`（命令位置の公開資料なし） · `00b5b108`（命令位置の公開資料なし） · `00b5b110`（命令位置の公開資料なし）

~~~diff
- 00b5accc ["INT_ADD", "register:40f0:8", ["const:b5accc:8", "const:4:8"]]
- 00b5accc ["CALL", null, ["callee:00c5b5d0:8"]]
+ 00b5b0f4 ["INT_ADD", "register:40f0:8", ["const:b5b0f4:8", "const:4:8"]]
+ 00b5b0f4 ["CALL", null, ["callee:00c5b5d0:8"]]
- 00b5accc bytes 41010494
+ 00b5b0f4 bytes 37010494
- 00b5ace0 ["INT_ADD", "register:40f0:8", ["const:b5ace0:8", "const:4:8"]]
- 00b5ace0 ["CALL", null, ["callee:00c5b160:8"]]
+ 00b5b108 ["INT_ADD", "register:40f0:8", ["const:b5b108:8", "const:4:8"]]
+ 00b5b108 ["CALL", null, ["callee:00c5b160:8"]]
- 00b5ace0 bytes 20000494
+ 00b5b108 bytes 16000494
- 00b5ace8 ["INT_ADD", "register:40f0:8", ["const:b5ace8:8", "const:4:8"]]
- 00b5ace8 ["CALL", null, ["callee:00c5ac30:8"]]
+ 00b5b110 ["INT_ADD", "register:40f0:8", ["const:b5b110:8", "const:4:8"]]
+ 00b5b110 ["CALL", null, ["callee:00c5ac30:8"]]
- 00b5ace8 bytes d2fe0394
+ 00b5b110 bytes c8fe0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd2d93de0b381dd5a4fd15ecb2b0be3f"></a>

### [`00b5ad20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ad20.md) → [`00b5b148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b148.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b430.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a830.md) [`00c5ad60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad60.md) [`00c5b430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b430.md)
- 新版 呼出元 1件 [`00c5b830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b830.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ac30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac30.md) [`00c5b160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b160.md) [`00c5b830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b830.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5ad3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ad20.md#insn-00b5ad3c) · [`00b5ad48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ad20.md#insn-00b5ad48) · [`00b5ad5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ad20.md#insn-00b5ad5c)
- 新版 `00b5b164`（命令位置の公開資料なし） · `00b5b170`（命令位置の公開資料なし） · `00b5b184`（命令位置の公開資料なし）

~~~diff
- 00b5ad3c ["INT_ADD", "register:40f0:8", ["const:b5ad3c:8", "const:4:8"]]
- 00b5ad3c ["CALL", null, ["callee:00c5b830:8"]]
+ 00b5b164 ["INT_ADD", "register:40f0:8", ["const:b5b164:8", "const:4:8"]]
+ 00b5b164 ["CALL", null, ["callee:00c5b830:8"]]
- 00b5ad3c bytes bd010494
+ 00b5b164 bytes b3010494
- 00b5ad48 ["INT_ADD", "register:40f0:8", ["const:b5ad48:8", "const:4:8"]]
- 00b5ad48 ["CALL", null, ["callee:00c5b830:8"]]
+ 00b5b170 ["INT_ADD", "register:40f0:8", ["const:b5b170:8", "const:4:8"]]
+ 00b5b170 ["CALL", null, ["callee:00c5b830:8"]]
- 00b5ad48 bytes ba010494
+ 00b5b170 bytes b0010494
- 00b5ad5c ["INT_ADD", "register:40f0:8", ["const:b5ad5c:8", "const:4:8"]]
- 00b5ad5c ["CALL", null, ["callee:00c5b160:8"]]
+ 00b5b184 ["INT_ADD", "register:40f0:8", ["const:b5b184:8", "const:4:8"]]
+ 00b5b184 ["CALL", null, ["callee:00c5b160:8"]]
- 00b5ad5c bytes 01000494
+ 00b5b184 bytes f7ff0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea87d37b10d269fff622c4b53141036a"></a>

### [`00b5adec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5adec.md) → [`00b5b214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b214.md) _ZNK8firebase10LoggerBase8LogDebugEPKcz

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5ae64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5adec.md#insn-00b5ae64) · [`00b5ae90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5adec.md#insn-00b5ae90) · [`00b5aeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5adec.md#insn-00b5aeb8)
- 新版 `00b5b28c`（命令位置の公開資料なし） · `00b5b2b8`（命令位置の公開資料なし） · `00b5b2e0`（命令位置の公開資料なし）

~~~diff
- 00b5ae64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5ae64 ["INT_ADD", "register:40f0:8", ["const:b5ae64:8", "const:4:8"]]
- 00b5ae64 ["CALLIND", null, ["register:0:8"]]
+ 00b5b28c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5b28c ["INT_ADD", "register:40f0:8", ["const:b5b28c:8", "const:4:8"]]
+ 00b5b28c ["CALLIND", null, ["register:0:8"]]
- 00b5ae64 bytes 00013fd6
+ 00b5b28c bytes 00013fd6
- 00b5ae90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5ae90 ["INT_ADD", "register:40f0:8", ["const:b5ae90:8", "const:4:8"]]
- 00b5ae90 ["CALLIND", null, ["register:0:8"]]
+ 00b5b2b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5b2b8 ["INT_ADD", "register:40f0:8", ["const:b5b2b8:8", "const:4:8"]]
+ 00b5b2b8 ["CALLIND", null, ["register:0:8"]]
- 00b5ae90 bytes 00013fd6
+ 00b5b2b8 bytes 00013fd6
- 00b5aeb8 ["INT_ADD", "register:40f0:8", ["const:b5aeb8:8", "const:4:8"]]
- 00b5aeb8 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00b5b2e0 ["INT_ADD", "register:40f0:8", ["const:b5b2e0:8", "const:4:8"]]
+ 00b5b2e0 ["CALL", null, ["callee:00c57ee0:8"]]
- 00b5aeb8 bytes 0af30394
+ 00b5b2e0 bytes 00f30394
~~~


<a id="compare-d467ad82abc753598c596c96c4c3134c"></a>

### [`00b5b370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b370.md) → [`00b5b798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b798.md) _ZNK8firebase10LoggerBase11LogMessageVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b370.md#insn-00b5b3ac) · [`00b5b3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b370.md#insn-00b5b3d8) · [`00b5b400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b370.md#insn-00b5b400)
- 新版 `00b5b7d4`（命令位置の公開資料なし） · `00b5b800`（命令位置の公開資料なし） · `00b5b828`（命令位置の公開資料なし）

~~~diff
- 00b5b3ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b3ac ["INT_ADD", "register:40f0:8", ["const:b5b3ac:8", "const:4:8"]]
- 00b5b3ac ["CALLIND", null, ["register:0:8"]]
+ 00b5b7d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5b7d4 ["INT_ADD", "register:40f0:8", ["const:b5b7d4:8", "const:4:8"]]
+ 00b5b7d4 ["CALLIND", null, ["register:0:8"]]
- 00b5b3ac bytes 00013fd6
+ 00b5b7d4 bytes 00013fd6
- 00b5b3d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b3d8 ["INT_ADD", "register:40f0:8", ["const:b5b3d8:8", "const:4:8"]]
- 00b5b3d8 ["CALLIND", null, ["register:0:8"]]
+ 00b5b800 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5b800 ["INT_ADD", "register:40f0:8", ["const:b5b800:8", "const:4:8"]]
+ 00b5b800 ["CALLIND", null, ["register:0:8"]]
- 00b5b3d8 bytes 00013fd6
+ 00b5b800 bytes 00013fd6
- 00b5b400 ["INT_ADD", "register:40f0:8", ["const:b5b400:8", "const:4:8"]]
- 00b5b400 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00b5b828 ["INT_ADD", "register:40f0:8", ["const:b5b828:8", "const:4:8"]]
+ 00b5b828 ["CALL", null, ["callee:00c57ee0:8"]]
- 00b5b400 bytes b8f10394
+ 00b5b828 bytes aef10394
~~~


<a id="compare-5225ba2863e53517e5c907a8e6f49bd3"></a>

### [`00b5b414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b414.md) → [`00b5b83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b83c.md) _ZNK8firebase12SystemLogger15LogMessageImplVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ad20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b414.md#insn-00b5b448) · [`00b5b46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b414.md#insn-00b5b46c)
- 新版 `00b5b870`（命令位置の公開資料なし） · `00b5b894`（命令位置の公開資料なし）

~~~diff
- 00b5b448 ["INT_ADD", "register:40f0:8", ["const:b5b448:8", "const:4:8"]]
- 00b5b448 ["CALL", null, ["callee:00c5b120:8"]]
+ 00b5b870 ["INT_ADD", "register:40f0:8", ["const:b5b870:8", "const:4:8"]]
+ 00b5b870 ["CALL", null, ["callee:00c5b120:8"]]
- 00b5b448 bytes 36fe0394
+ 00b5b870 bytes 2cfe0394
- 00b5b46c ["INT_ADD", "register:40f0:8", ["const:b5b46c:8", "const:4:8"]]
- 00b5b46c ["CALL", null, ["callee:00c57ee0:8"]]
+ 00b5b894 ["INT_ADD", "register:40f0:8", ["const:b5b894:8", "const:4:8"]]
+ 00b5b894 ["CALL", null, ["callee:00c57ee0:8"]]
- 00b5b46c bytes 9df10394
+ 00b5b894 bytes 93f10394
~~~


<a id="compare-c95f5153ce490fcdc3c8ab4297db3e72"></a>

### [`00b5b484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b484.md) → [`00b5b8ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b8ac.md) _ZNK8firebase6Logger15LogMessageImplVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b484.md#insn-00b5b4c4) · [`00b5b4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b484.md#insn-00b5b4f0) · [`00b5b518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b484.md#insn-00b5b518)
- 新版 `00b5b8ec`（命令位置の公開資料なし） · `00b5b918`（命令位置の公開資料なし） · `00b5b940`（命令位置の公開資料なし）

~~~diff
- 00b5b4c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b4c4 ["INT_ADD", "register:40f0:8", ["const:b5b4c4:8", "const:4:8"]]
- 00b5b4c4 ["CALLIND", null, ["register:0:8"]]
+ 00b5b8ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5b8ec ["INT_ADD", "register:40f0:8", ["const:b5b8ec:8", "const:4:8"]]
+ 00b5b8ec ["CALLIND", null, ["register:0:8"]]
- 00b5b4c4 bytes 00013fd6
+ 00b5b8ec bytes 00013fd6
- 00b5b4f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b4f0 ["INT_ADD", "register:40f0:8", ["const:b5b4f0:8", "const:4:8"]]
- 00b5b4f0 ["CALLIND", null, ["register:0:8"]]
+ 00b5b918 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5b918 ["INT_ADD", "register:40f0:8", ["const:b5b918:8", "const:4:8"]]
+ 00b5b918 ["CALLIND", null, ["register:0:8"]]
- 00b5b4f0 bytes 00013fd6
+ 00b5b918 bytes 00013fd6
- 00b5b518 ["INT_ADD", "register:40f0:8", ["const:b5b518:8", "const:4:8"]]
- 00b5b518 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00b5b940 ["INT_ADD", "register:40f0:8", ["const:b5b940:8", "const:4:8"]]
+ 00b5b940 ["CALL", null, ["callee:00c57ee0:8"]]
- 00b5b518 bytes 72f10394
+ 00b5b940 bytes 68f10394
~~~


<a id="compare-a7b31a7d459b28ff69ff9490fd2f669e"></a>

### [`00b5b604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b604.md) → [`00b5ba2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5ba2c.md) _ZN8firebase8callback18CallbackDispatcher14FlushCallbacksEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b720.md) · 呼出先 4件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 1件 [`00c5bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bb20.md) · 呼出先 4件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b604.md#insn-00b5b624) · [`00b5b63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b604.md#insn-00b5b63c) · [`00b5b680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b604.md#insn-00b5b680)
- 新版 `00b5ba4c`（命令位置の公開資料なし） · `00b5ba64`（命令位置の公開資料なし） · `00b5baa8`（命令位置の公開資料なし）

~~~diff
- 00b5b624 ["INT_ADD", "register:40f0:8", ["const:b5b624:8", "const:4:8"]]
- 00b5b624 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b5ba4c ["INT_ADD", "register:40f0:8", ["const:b5ba4c:8", "const:4:8"]]
+ 00b5ba4c ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5b624 bytes f7fb0394
+ 00b5ba4c bytes edfb0394
- 00b5b63c ["INT_ADD", "register:40f0:8", ["const:b5b63c:8", "const:4:8"]]
- 00b5b63c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b5ba64 ["INT_ADD", "register:40f0:8", ["const:b5ba64:8", "const:4:8"]]
+ 00b5ba64 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b5b63c bytes 1df10394
+ 00b5ba64 bytes 13f10394
- 00b5b680 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b680 ["INT_ADD", "register:40f0:8", ["const:b5b680:8", "const:4:8"]]
- 00b5b680 ["CALLIND", null, ["register:0:8"]]
+ 00b5baa8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5baa8 ["INT_ADD", "register:40f0:8", ["const:b5baa8:8", "const:4:8"]]
+ 00b5baa8 ["CALLIND", null, ["register:0:8"]]
- 00b5b680 bytes 00013fd6
+ 00b5baa8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b757612c7854e67f8a80844582b52bb"></a>

### [`00b5bcfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bcfc.md) → [`00b5c124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c124.md) _ZN8firebase8callback18CallbackDispatcher17DispatchCallbacksEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b730.md) · 呼出先 5件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5b700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b700.md)
- 新版 呼出元 1件 [`00c5bb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bb30.md) · 呼出先 5件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5bb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bb00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5bd20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bcfc.md#insn-00b5bd20) · [`00b5bda4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bcfc.md#insn-00b5bda4) · [`00b5bdac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bcfc.md#insn-00b5bdac)
- 新版 `00b5c148`（命令位置の公開資料なし） · `00b5c1cc`（命令位置の公開資料なし） · `00b5c1d4`（命令位置の公開資料なし）

~~~diff
- 00b5bd20 ["INT_ADD", "register:40f0:8", ["const:b5bd20:8", "const:4:8"]]
- 00b5bd20 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b5c148 ["INT_ADD", "register:40f0:8", ["const:b5c148:8", "const:4:8"]]
+ 00b5c148 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5bd20 bytes 38fa0394
+ 00b5c148 bytes 2efa0394
- 00b5bda4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5bda4 ["INT_ADD", "register:40f0:8", ["const:b5bda4:8", "const:4:8"]]
- 00b5bda4 ["CALLIND", null, ["register:0:8"]]
+ 00b5c1cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5c1cc ["INT_ADD", "register:40f0:8", ["const:b5c1cc:8", "const:4:8"]]
+ 00b5c1cc ["CALLIND", null, ["register:0:8"]]
- 00b5bda4 bytes 00013fd6
+ 00b5c1cc bytes 00013fd6
- 00b5bdac ["INT_ADD", "register:40f0:8", ["const:b5bdac:8", "const:4:8"]]
- 00b5bdac ["CALL", null, ["callee:00c57e80:8"]]
+ 00b5c1d4 ["INT_ADD", "register:40f0:8", ["const:b5c1d4:8", "const:4:8"]]
+ 00b5c1d4 ["CALL", null, ["callee:00c57e80:8"]]
- 00b5bdac bytes 35ef0394
+ 00b5c1d4 bytes 2bef0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c85b1e86f33d973589b272c48d06d3f"></a>

### [`00b5dac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5dac4.md) → [`00b5deec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5deec.md) _ZN8firebase4Path11GetRelativeERKS0_S2_PS0_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md) [`00c5b7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b7e0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md) [`00c5bbe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bbe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5daf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5dac4.md#insn-00b5daf0) · [`00b5db28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5dac4.md#insn-00b5db28) · [`00b5db40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5dac4.md#insn-00b5db40)
- 新版 `00b5df18`（命令位置の公開資料なし） · `00b5df50`（命令位置の公開資料なし） · `00b5df68`（命令位置の公開資料なし）

~~~diff
- 00b5daf0 ["INT_ADD", "register:40f0:8", ["const:b5daf0:8", "const:4:8"]]
- 00b5daf0 ["CALL", null, ["callee:00c5bbe0:8"]]
+ 00b5df18 ["INT_ADD", "register:40f0:8", ["const:b5df18:8", "const:4:8"]]
+ 00b5df18 ["CALL", null, ["callee:00c5bbe0:8"]]
- 00b5daf0 bytes 3cf70394
+ 00b5df18 bytes 32f70394
- 00b5db28 ["INT_ADD", "register:40f0:8", ["const:b5db28:8", "const:4:8"]]
- 00b5db28 ["CALL", null, ["callee:00c5b0b0:8"]]
+ 00b5df50 ["INT_ADD", "register:40f0:8", ["const:b5df50:8", "const:4:8"]]
+ 00b5df50 ["CALL", null, ["callee:00c5b0b0:8"]]
- 00b5db28 bytes 62f40394
+ 00b5df50 bytes 58f40394
- 00b5db40 ["INT_ADD", "register:40f0:8", ["const:b5db40:8", "const:4:8"]]
- 00b5db40 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b5df68 ["INT_ADD", "register:40f0:8", ["const:b5df68:8", "const:4:8"]]
+ 00b5df68 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b5db40 bytes dce70394
+ 00b5df68 bytes d2e70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

