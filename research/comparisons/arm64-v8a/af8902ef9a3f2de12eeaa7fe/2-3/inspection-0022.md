# v16.0.0 → v16.0.1 · 要調査の変更候補 (22)

[一覧の目次](README.md)

<a id="compare-2dfd5e8e107f00b3a4b126a0be32e3d4"></a>

### [`006faa28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fa/006faa28.md) → [`006faa68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fa/006faa68.md) FUN_006faa68

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006fa294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fa/006fa294.md) [`006faa28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fa/006faa28.md) · 呼出先 3件 [`006fa598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fa/006fa598.md) [`006faa28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fa/006faa28.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 2件 [`006fa2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fa/006fa2d4.md) [`006faa68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fa/006faa68.md) · 呼出先 3件 [`006fa5d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fa/006fa5d8.md) [`006faa68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fa/006faa68.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006faa88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fa/006faa28.md#insn-006faa88) · [`006faaf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fa/006faa28.md#insn-006faaf4) · [`006fabe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fa/006faa28.md#insn-006fabe0)
- 新版 `006faac8`（命令位置の公開資料なし） · `006fab34`（命令位置の公開資料なし） · `006fac20`（命令位置の公開資料なし）

~~~diff
- 006faa88 ["INT_ADD", "register:40f0:8", ["const:6faa88:8", "const:4:8"]]
- 006faa88 ["CALL", null, ["callee:006fa5d8:8"]]
+ 006faac8 ["INT_ADD", "register:40f0:8", ["const:6faac8:8", "const:4:8"]]
+ 006faac8 ["CALL", null, ["callee:006fa5d8:8"]]
- 006faa88 bytes c4feff97
+ 006faac8 bytes c4feff97
- 006faaf4 ["INT_ADD", "register:40f0:8", ["const:6faaf4:8", "const:4:8"]]
- 006faaf4 ["CALL", null, ["callee:006fa5d8:8"]]
+ 006fab34 ["INT_ADD", "register:40f0:8", ["const:6fab34:8", "const:4:8"]]
+ 006fab34 ["CALL", null, ["callee:006fa5d8:8"]]
- 006faaf4 bytes a9feff97
+ 006fab34 bytes a9feff97
- 006fabe0 ["INT_ADD", "register:40f0:8", ["const:6fabe0:8", "const:4:8"]]
- 006fabe0 ["CALL", null, ["callee:006fa5d8:8"]]
+ 006fac20 ["INT_ADD", "register:40f0:8", ["const:6fac20:8", "const:4:8"]]
+ 006fac20 ["CALL", null, ["callee:006fa5d8:8"]]
- 006fabe0 bytes 6efeff97
+ 006fac20 bytes 6efeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-310e4748a9a66b17f33da8a391bd3ddd"></a>

### [`006fb034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb034.md) → [`006fb074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb074.md) FUN_006fb074

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 10件 [`006e44a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e44a0.md) [`006e5d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5d30.md) [`006fb034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb034.md) [`006fb8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb8d0.md) [`006fbc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbc6c.md) · 呼出先 4件 [`006fb034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb034.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 10件 [`006e44e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e44e0.md) [`006e5d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e5/006e5d70.md) [`006fb074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb074.md) [`006fb910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb910.md) [`006fbcac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fbcac.md) · 呼出先 4件 [`006fb074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb074.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006fb050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb034.md#insn-006fb050) · [`006fb05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb034.md#insn-006fb05c) · [`006fb070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb034.md#insn-006fb070)
- 新版 `006fb090`（命令位置の公開資料なし） · `006fb09c`（命令位置の公開資料なし） · `006fb0b0`（命令位置の公開資料なし）

~~~diff
- 006fb050 ["INT_ADD", "register:40f0:8", ["const:6fb050:8", "const:4:8"]]
- 006fb050 ["CALL", null, ["local:b0:8"]]
+ 006fb090 ["INT_ADD", "register:40f0:8", ["const:6fb090:8", "const:4:8"]]
+ 006fb090 ["CALL", null, ["local:b0:8"]]
- 006fb050 bytes f9ffff97
+ 006fb090 bytes f9ffff97
- 006fb05c ["INT_ADD", "register:40f0:8", ["const:6fb05c:8", "const:4:8"]]
- 006fb05c ["CALL", null, ["local:b0:8"]]
+ 006fb09c ["INT_ADD", "register:40f0:8", ["const:6fb09c:8", "const:4:8"]]
+ 006fb09c ["CALL", null, ["local:b0:8"]]
- 006fb05c bytes f6ffff97
+ 006fb09c bytes f6ffff97
- 006fb070 ["INT_ADD", "register:40f0:8", ["const:6fb070:8", "const:4:8"]]
- 006fb070 ["CALL", null, ["callee:00c53d00:8"]]
+ 006fb0b0 ["INT_ADD", "register:40f0:8", ["const:6fb0b0:8", "const:4:8"]]
+ 006fb0b0 ["CALL", null, ["callee:00c53d00:8"]]
- 006fb070 bytes 1c621594
+ 006fb0b0 bytes 14631594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be6464d58eaaa0ada1149bc6038d5283"></a>

### [`007000e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/007000e4.md) → [`00700124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700124.md) FUN_00700124

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00700104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/007000e4.md#insn-00700104)
- 新版 `00700144`（命令位置の公開資料なし）

~~~diff
- 00700104 ["INT_ADD", "register:40f0:8", ["const:700104:8", "const:4:8"]]
- 00700104 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00700144 ["INT_ADD", "register:40f0:8", ["const:700144:8", "const:4:8"]]
+ 00700144 ["CALL", null, ["callee:00c57eb0:8"]]
- 00700104 bytes 6b5e1594
+ 00700144 bytes 5b5f1594
~~~


<a id="compare-897c5ec17a620c5041149b6b141199f4"></a>

### [`007004d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/007004d0.md) → [`00700510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700510.md) FUN_00700510

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007004f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/007004d0.md#insn-007004f0)
- 新版 `00700530`（命令位置の公開資料なし）

~~~diff
- 007004f0 ["INT_ADD", "register:40f0:8", ["const:7004f0:8", "const:4:8"]]
- 007004f0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00700530 ["INT_ADD", "register:40f0:8", ["const:700530:8", "const:4:8"]]
+ 00700530 ["CALL", null, ["callee:00c57eb0:8"]]
- 007004f0 bytes 705d1594
+ 00700530 bytes 605e1594
~~~


<a id="compare-2f7333359929e2b7fceeaaf631f804cb"></a>

### [`007078ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/007078ec.md) → [`0070792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/0070792c.md) FUN_0070792c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`007154c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007154c0.md) [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 9件 [`005e0898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0898.md) [`005e08e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e08e0.md) [`00af34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af34c8.md) [`00af37f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af37f4.md) [`00af3a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3a44.md)
- 新版 呼出元 3件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`00715500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00715/00715500.md) [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 9件 [`005e08d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e08d8.md) [`005e0920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0920.md) [`00af38f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af38f0.md) [`00af3c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3c1c.md) [`00af3e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3e6c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0070792c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/007078ec.md#insn-0070792c) · [`0070793c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/007078ec.md#insn-0070793c) · [`00707954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/007078ec.md#insn-00707954)
- 新版 `0070796c`（命令位置の公開資料なし） · `0070797c`（命令位置の公開資料なし） · `00707994`（命令位置の公開資料なし）

~~~diff
- 0070792c ["INT_ADD", "register:40f0:8", ["const:70792c:8", "const:4:8"]]
- 0070792c ["CALL", null, ["callee:005e08d8:8"]]
+ 0070796c ["INT_ADD", "register:40f0:8", ["const:70796c:8", "const:4:8"]]
+ 0070796c ["CALL", null, ["callee:005e08d8:8"]]
- 0070792c bytes db63fb97
+ 0070796c bytes db63fb97
- 0070793c ["INT_ADD", "register:40f0:8", ["const:70793c:8", "const:4:8"]]
- 0070793c ["CALL", null, ["callee:00af5298:8"]]
+ 0070797c ["INT_ADD", "register:40f0:8", ["const:70797c:8", "const:4:8"]]
+ 0070797c ["CALL", null, ["callee:00af5298:8"]]
- 0070793c bytes 4db50f94
+ 0070797c bytes 47b60f94
- 00707954 ["INT_ADD", "register:40f0:8", ["const:707954:8", "const:4:8"]]
- 00707954 ["CALL", null, ["callee:005e0920:8"]]
+ 00707994 ["INT_ADD", "register:40f0:8", ["const:707994:8", "const:4:8"]]
+ 00707994 ["CALL", null, ["callee:005e0920:8"]]
- 00707954 bytes e363fb97
+ 00707994 bytes e363fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6de4b37e83e8dbf07da95b0c393cf0a"></a>

### [`00707d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707d30.md) → [`00707d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707d70.md) FUN_00707d70

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005f2d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f2/005f2d28.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`00710298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710298.md) · 呼出先 2件 [`00afc0e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc0e4.md) [`00afc140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc140.md)
- 新版 呼出元 3件 [`005f2d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f2/005f2d68.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`007102d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) · 呼出先 2件 [`00afc50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afc50c.md) [`00afc568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afc568.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00707d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707d30.md#insn-00707d58) · [`00707d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707d30.md#insn-00707d70) · [`00707d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707d30.md#insn-00707d88)
- 新版 `00707d98`（命令位置の公開資料なし） · `00707db0`（命令位置の公開資料なし） · `00707dc8`（命令位置の公開資料なし）

~~~diff
- 00707d58 ["INT_ADD", "register:40f0:8", ["const:707d58:8", "const:4:8"]]
- 00707d58 ["CALL", null, ["callee:00afc50c:8"]]
+ 00707d98 ["INT_ADD", "register:40f0:8", ["const:707d98:8", "const:4:8"]]
+ 00707d98 ["CALL", null, ["callee:00afc50c:8"]]
- 00707d58 bytes e3d00f94
+ 00707d98 bytes ddd10f94
- 00707d70 ["INT_ADD", "register:40f0:8", ["const:707d70:8", "const:4:8"]]
- 00707d70 ["CALL", null, ["callee:00afc50c:8"]]
+ 00707db0 ["INT_ADD", "register:40f0:8", ["const:707db0:8", "const:4:8"]]
+ 00707db0 ["CALL", null, ["callee:00afc50c:8"]]
- 00707d70 bytes ddd00f94
+ 00707db0 bytes d7d10f94
- 00707d88 ["INT_ADD", "register:40f0:8", ["const:707d88:8", "const:4:8"]]
- 00707d88 ["CALL", null, ["callee:00afc50c:8"]]
+ 00707dc8 ["INT_ADD", "register:40f0:8", ["const:707dc8:8", "const:4:8"]]
+ 00707dc8 ["CALL", null, ["callee:00afc50c:8"]]
- 00707d88 bytes d7d00f94
+ 00707dc8 bytes d1d10f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9559c64d0b43ada91c8332f1b7e6d329"></a>

### [`00707e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707e70.md) → [`00707eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707eb0.md) FUN_00707eb0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00707e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707e70.md#insn-00707e88)
- 新版 `00707ec8`（命令位置の公開資料なし）

~~~diff
- 00707e88 ["INT_ADD", "register:40f0:8", ["const:707e88:8", "const:4:8"]]
- 00707e88 ["CALL", null, ["callee:00676a60:8"]]
+ 00707ec8 ["INT_ADD", "register:40f0:8", ["const:707ec8:8", "const:4:8"]]
+ 00707ec8 ["CALL", null, ["callee:00676a60:8"]]
- 00707e88 bytes e6bafd97
+ 00707ec8 bytes e6bafd97
~~~


<a id="compare-cfeecb36dbcb10af95e8c14fd9a67b59"></a>

### [`0070deb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070d/0070deb0.md) → [`0070def0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070d/0070def0.md) FUN_0070def0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005f2d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f2/005f2d28.md) · 呼出先 2件 [`00afc0e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc0e4.md) [`00afc140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc140.md)
- 新版 呼出元 1件 [`005f2d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f2/005f2d68.md) · 呼出先 2件 [`00afc50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afc50c.md) [`00afc568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afc568.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0070ded8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070d/0070deb0.md#insn-0070ded8) · [`0070def4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070d/0070deb0.md#insn-0070def4) · [`0070df04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070d/0070deb0.md#insn-0070df04)
- 新版 `0070df18`（命令位置の公開資料なし） · `0070df34`（命令位置の公開資料なし） · `0070df44`（命令位置の公開資料なし）

~~~diff
- 0070ded8 ["INT_ADD", "register:40f0:8", ["const:70ded8:8", "const:4:8"]]
- 0070ded8 ["CALL", null, ["callee:00afc50c:8"]]
+ 0070df18 ["INT_ADD", "register:40f0:8", ["const:70df18:8", "const:4:8"]]
+ 0070df18 ["CALL", null, ["callee:00afc50c:8"]]
- 0070ded8 bytes 83b80f94
+ 0070df18 bytes 7db90f94
- 0070def4 ["INT_ADD", "register:40f0:8", ["const:70def4:8", "const:4:8"]]
- 0070def4 ["CALL", null, ["callee:00afc568:8"]]
+ 0070df34 ["INT_ADD", "register:40f0:8", ["const:70df34:8", "const:4:8"]]
+ 0070df34 ["CALL", null, ["callee:00afc568:8"]]
- 0070def4 bytes 93b80f94
+ 0070df34 bytes 8db90f94
- 0070df04 ["INT_ADD", "register:40f0:8", ["const:70df04:8", "const:4:8"]]
- 0070df04 ["CALL", null, ["callee:00afc50c:8"]]
+ 0070df44 ["INT_ADD", "register:40f0:8", ["const:70df44:8", "const:4:8"]]
+ 0070df44 ["CALL", null, ["callee:00afc50c:8"]]
- 0070df04 bytes 78b80f94
+ 0070df44 bytes 72b90f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0c3a2b5c16c894ac51f8f86d4fa8f14"></a>

### [`0070dfc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070d/0070dfc4.md) → [`0070e004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e004.md) FUN_0070e004

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`00a52c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a52/00a52c38.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046eeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`00a52e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a52/00a52e30.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0070e044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070d/0070dfc4.md#insn-0070e044) · [`0070e064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070d/0070dfc4.md#insn-0070e064) · [`0070e090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070d/0070dfc4.md#insn-0070e090)
- 新版 `0070e084`（命令位置の公開資料なし） · `0070e0a4`（命令位置の公開資料なし） · `0070e0d0`（命令位置の公開資料なし）

~~~diff
- 0070e044 ["INT_ADD", "register:40f0:8", ["const:70e044:8", "const:4:8"]]
- 0070e044 ["CALL", null, ["callee:00c57e90:8"]]
+ 0070e084 ["INT_ADD", "register:40f0:8", ["const:70e084:8", "const:4:8"]]
+ 0070e084 ["CALL", null, ["callee:00c57e90:8"]]
- 0070e044 bytes 93261594
+ 0070e084 bytes 83271594
- 0070e064 ["INT_ADD", "register:40f0:8", ["const:70e064:8", "const:4:8"]]
- 0070e064 ["CALL", null, ["callee:0046eef8:8"]]
+ 0070e0a4 ["INT_ADD", "register:40f0:8", ["const:70e0a4:8", "const:4:8"]]
+ 0070e0a4 ["CALL", null, ["callee:0046eef8:8"]]
- 0070e064 bytes 9583f597
+ 0070e0a4 bytes 9583f597
- 0070e090 ["INT_ADD", "register:40f0:8", ["const:70e090:8", "const:4:8"]]
- 0070e090 ["CALL", null, ["callee:0043bba4:8"]]
+ 0070e0d0 ["INT_ADD", "register:40f0:8", ["const:70e0d0:8", "const:4:8"]]
+ 0070e0d0 ["CALL", null, ["callee:0043bba4:8"]]
- 0070e090 bytes b5b6f497
+ 0070e0d0 bytes b5b6f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61fd47267d2847911eb196850d2ae0df"></a>

### [`0070e108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e108.md) → [`0070e148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e148.md) FUN_0070e148

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0070e12c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e108.md#insn-0070e12c)
- 新版 `0070e16c`（命令位置の公開資料なし）

~~~diff
- 0070e12c ["INT_ADD", "register:40f0:8", ["const:70e12c:8", "const:4:8"]]
- 0070e12c ["CALL", null, ["callee:0046efdc:8"]]
+ 0070e16c ["INT_ADD", "register:40f0:8", ["const:70e16c:8", "const:4:8"]]
+ 0070e16c ["CALL", null, ["callee:0046efdc:8"]]
- 0070e12c bytes 9c83f597
+ 0070e16c bytes 9c83f597
~~~


<a id="compare-b4bba8e209bd49c368095dfd54e69c9f"></a>

### [`00710090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710090.md) → [`007100d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007100d0.md) FUN_007100d0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 15件 [`00ab9080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab9080.md) [`00af5f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5f88.md) [`00af5ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5ff8.md) [`00af6068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6068.md) [`00af60d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af60d8.md)
- 新版 呼出元 2件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 15件 [`00ab927c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab9/00ab927c.md) [`00af63b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af63b0.md) [`00af6420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6420.md) [`00af6490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6490.md) [`00af6500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6500.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007100b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710090.md#insn-007100b4) · [`007100c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710090.md#insn-007100c4) · [`007100e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710090.md#insn-007100e0)
- 新版 `007100f4`（命令位置の公開資料なし） · `00710104`（命令位置の公開資料なし） · `00710120`（命令位置の公開資料なし）

~~~diff
- 007100b4 ["INT_ADD", "register:40f0:8", ["const:7100b4:8", "const:4:8"]]
- 007100b4 ["CALL", null, ["callee:00af63b0:8"]]
+ 007100f4 ["INT_ADD", "register:40f0:8", ["const:7100f4:8", "const:4:8"]]
+ 007100f4 ["CALL", null, ["callee:00af63b0:8"]]
- 007100b4 bytes b5970f94
+ 007100f4 bytes af980f94
- 007100c4 ["INT_ADD", "register:40f0:8", ["const:7100c4:8", "const:4:8"]]
- 007100c4 ["CALL", null, ["callee:00af6420:8"]]
+ 00710104 ["INT_ADD", "register:40f0:8", ["const:710104:8", "const:4:8"]]
+ 00710104 ["CALL", null, ["callee:00af6420:8"]]
- 007100c4 bytes cd970f94
+ 00710104 bytes c7980f94
- 007100e0 ["INT_ADD", "register:40f0:8", ["const:7100e0:8", "const:4:8"]]
- 007100e0 ["CALL", null, ["callee:00ab927c:8"]]
+ 00710120 ["INT_ADD", "register:40f0:8", ["const:710120:8", "const:4:8"]]
+ 00710120 ["CALL", null, ["callee:00ab927c:8"]]
- 007100e0 bytes e8a30e94
+ 00710120 bytes 57a40e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27a07d11a141762c7c217a43e62e4f85"></a>

### [`007140e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/007140e4.md) → [`00714124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714124.md) FUN_00714124

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005fe21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe21c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005fe25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe25c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00714164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/007140e4.md#insn-00714164) · [`007141a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/007140e4.md#insn-007141a0) · [`007141b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/007140e4.md#insn-007141b4)
- 新版 `007141a4`（命令位置の公開資料なし） · `007141e0`（命令位置の公開資料なし） · `007141f4`（命令位置の公開資料なし）

~~~diff
- 00714164 ["INT_ADD", "register:40f0:8", ["const:714164:8", "const:4:8"]]
- 00714164 ["CALL", null, ["callee:00c57e90:8"]]
+ 007141a4 ["INT_ADD", "register:40f0:8", ["const:7141a4:8", "const:4:8"]]
+ 007141a4 ["CALL", null, ["callee:00c57e90:8"]]
- 00714164 bytes 4b0e1594
+ 007141a4 bytes 3b0f1594
- 007141a0 ["INT_ADD", "register:40f0:8", ["const:7141a0:8", "const:4:8"]]
- 007141a0 ["CALL", null, ["callee:00c58000:8"]]
+ 007141e0 ["INT_ADD", "register:40f0:8", ["const:7141e0:8", "const:4:8"]]
+ 007141e0 ["CALL", null, ["callee:00c58000:8"]]
- 007141a0 bytes 980e1594
+ 007141e0 bytes 880f1594
- 007141b4 ["INT_ADD", "register:40f0:8", ["const:7141b4:8", "const:4:8"]]
- 007141b4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007141f4 ["INT_ADD", "register:40f0:8", ["const:7141f4:8", "const:4:8"]]
+ 007141f4 ["CALL", null, ["callee:00c57eb0:8"]]
- 007141b4 bytes 3f0e1594
+ 007141f4 bytes 2f0f1594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7435f7eaab618e8dbcbbbcdf6e28b134"></a>

### [`007141dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/007141dc.md) → [`0071421c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/0071421c.md) FUN_0071421c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005fe258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe258.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005fe298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe298.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007141fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/007141dc.md#insn-007141fc)
- 新版 `0071423c`（命令位置の公開資料なし）

~~~diff
- 007141fc ["INT_ADD", "register:40f0:8", ["const:7141fc:8", "const:4:8"]]
- 007141fc ["CALL", null, ["callee:005fe298:8"]]
+ 0071423c ["INT_ADD", "register:40f0:8", ["const:71423c:8", "const:4:8"]]
+ 0071423c ["CALL", null, ["callee:005fe298:8"]]
- 007141fc bytes 17a8fb97
+ 0071423c bytes 17a8fb97
~~~


<a id="compare-5aa3d69bd0a7f1c8e03a405a444bc797"></a>

### [`00716a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716a50.md) → [`00716a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716a90.md) FUN_00716a90

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`007154c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007154c0.md) [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 6件 [`00af37f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af37f4.md) [`00af3834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3834.md) [`00af399c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af399c.md) [`00af3d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3d4c.md) [`00af4fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af4/00af4fdc.md)
- 新版 呼出元 3件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`00715500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00715/00715500.md) [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 6件 [`00af3c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3c1c.md) [`00af3c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3c5c.md) [`00af3dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3dc4.md) [`00af4174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af4/00af4174.md) [`00af5404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5404.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00716a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716a50.md#insn-00716a6c) · [`00716a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716a50.md#insn-00716a7c) · [`00716a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716a50.md#insn-00716a90)
- 新版 `00716aac`（命令位置の公開資料なし） · `00716abc`（命令位置の公開資料なし） · `00716ad0`（命令位置の公開資料なし）

~~~diff
- 00716a6c ["INT_ADD", "register:40f0:8", ["const:716a6c:8", "const:4:8"]]
- 00716a6c ["CALL", null, ["callee:00af5864:8"]]
+ 00716aac ["INT_ADD", "register:40f0:8", ["const:716aac:8", "const:4:8"]]
+ 00716aac ["CALL", null, ["callee:00af5864:8"]]
- 00716a6c bytes 747a0f94
+ 00716aac bytes 6e7b0f94
- 00716a7c ["INT_ADD", "register:40f0:8", ["const:716a7c:8", "const:4:8"]]
- 00716a7c ["CALL", null, ["callee:00af5864:8"]]
+ 00716abc ["INT_ADD", "register:40f0:8", ["const:716abc:8", "const:4:8"]]
+ 00716abc ["CALL", null, ["callee:00af5864:8"]]
- 00716a7c bytes 707a0f94
+ 00716abc bytes 6a7b0f94
- 00716a90 ["INT_ADD", "register:40f0:8", ["const:716a90:8", "const:4:8"]]
- 00716a90 ["CALL", null, ["callee:00af3c1c:8"]]
+ 00716ad0 ["INT_ADD", "register:40f0:8", ["const:716ad0:8", "const:4:8"]]
+ 00716ad0 ["CALL", null, ["callee:00af3c1c:8"]]
- 00716a90 bytes 59730f94
+ 00716ad0 bytes 53740f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-093b559b712ff15302189a2357c06b28"></a>

### [`00718578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00718/00718578.md) → [`007185b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00718/007185b8.md) FUN_007185b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007185e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00718/00718578.md#insn-007185e0) · [`0071861c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00718/00718578.md#insn-0071861c)
- 新版 `00718620`（命令位置の公開資料なし） · `0071865c`（命令位置の公開資料なし）

~~~diff
- 007185e0 ["INT_ADD", "register:40f0:8", ["const:7185e0:8", "const:4:8"]]
- 007185e0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00718620 ["INT_ADD", "register:40f0:8", ["const:718620:8", "const:4:8"]]
+ 00718620 ["CALL", null, ["callee:00c57e90:8"]]
- 007185e0 bytes 2cfd1494
+ 00718620 bytes 1cfe1494
- 0071861c ["INT_ADD", "register:40f0:8", ["const:71861c:8", "const:4:8"]]
- 0071861c ["CALL", null, ["callee:0043bba4:8"]]
+ 0071865c ["INT_ADD", "register:40f0:8", ["const:71865c:8", "const:4:8"]]
+ 0071865c ["CALL", null, ["callee:0043bba4:8"]]
- 0071861c bytes 528df497
+ 0071865c bytes 528df497
~~~


<a id="compare-400036fa20fbb8661bd11031dcd8208d"></a>

### [`00718644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00718/00718644.md) → [`00718684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00718/00718684.md) FUN_00718684

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 2件 [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007186c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00718/00718644.md#insn-007186c4) · [`007186f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00718/00718644.md#insn-007186f4) · [`00718708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00718/00718644.md#insn-00718708)
- 新版 `00718704`（命令位置の公開資料なし） · `00718734`（命令位置の公開資料なし） · `00718748`（命令位置の公開資料なし）

~~~diff
- 007186c4 ["INT_ADD", "register:40f0:8", ["const:7186c4:8", "const:4:8"]]
- 007186c4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00718704 ["INT_ADD", "register:40f0:8", ["const:718704:8", "const:4:8"]]
+ 00718704 ["CALL", null, ["callee:00c57e90:8"]]
- 007186c4 bytes f3fc1494
+ 00718704 bytes e3fd1494
- 007186f4 ["INT_ADD", "register:40f0:8", ["const:7186f4:8", "const:4:8"]]
- 007186f4 ["CALL", null, ["callee:00c58000:8"]]
+ 00718734 ["INT_ADD", "register:40f0:8", ["const:718734:8", "const:4:8"]]
+ 00718734 ["CALL", null, ["callee:00c58000:8"]]
- 007186f4 bytes 43fd1494
+ 00718734 bytes 33fe1494
- 00718708 ["INT_ADD", "register:40f0:8", ["const:718708:8", "const:4:8"]]
- 00718708 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00718748 ["INT_ADD", "register:40f0:8", ["const:718748:8", "const:4:8"]]
+ 00718748 ["CALL", null, ["callee:00c57eb0:8"]]
- 00718708 bytes eafc1494
+ 00718748 bytes dafd1494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68714a04a84f63b49e4adf7cd96e04ea"></a>

### [`007196f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00719/007196f8.md) → [`00719738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00719/00719738.md) FUN_00719738

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) [`009385d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/009385d8.md) [`0093b2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b2c4.md) [`00a321a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a321a8.md) [`00a32280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a32280.md) · 呼出先 2件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 6件 [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) [`00938774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00938/00938774.md) [`0093b460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b460.md) [`00a323a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a323a0.md) [`00a32478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32478.md) · 呼出先 2件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007197a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00719/007196f8.md#insn-007197a8) · [`007197b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00719/007196f8.md#insn-007197b8) · [`007197c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00719/007196f8.md#insn-007197c0)
- 新版 `007197e8`（命令位置の公開資料なし） · `007197f8`（命令位置の公開資料なし） · `00719800`（命令位置の公開資料なし）

~~~diff
- 007197a8 ["INT_ADD", "register:40f0:8", ["const:7197a8:8", "const:4:8"]]
- 007197a8 ["CALL", null, ["callee:00494610:8"]]
+ 007197e8 ["INT_ADD", "register:40f0:8", ["const:7197e8:8", "const:4:8"]]
+ 007197e8 ["CALL", null, ["callee:00494610:8"]]
- 007197a8 bytes 8aebf597
+ 007197e8 bytes 8aebf597
- 007197b8 ["INT_ADD", "register:40f0:8", ["const:7197b8:8", "const:4:8"]]
- 007197b8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007197f8 ["INT_ADD", "register:40f0:8", ["const:7197f8:8", "const:4:8"]]
+ 007197f8 ["CALL", null, ["callee:00c57eb0:8"]]
- 007197b8 bytes bef81494
+ 007197f8 bytes aef91494
- 007197c0 ["INT_ADD", "register:40f0:8", ["const:7197c0:8", "const:4:8"]]
- 007197c0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00719800 ["INT_ADD", "register:40f0:8", ["const:719800:8", "const:4:8"]]
+ 00719800 ["CALL", null, ["callee:00c57eb0:8"]]
- 007197c0 bytes bcf81494
+ 00719800 bytes acf91494
~~~


<a id="compare-12e3f0fc52afaf831ab546c33320d078"></a>

### [`00719b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00719/00719b64.md) → [`00719ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00719/00719ba4.md) FUN_00719ba4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0090db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090db60.md) · 呼出先 1件 [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md)
- 新版 呼出元 1件 [`0090dcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090d/0090dcfc.md) · 呼出先 1件 [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00719bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00719/00719b64.md#insn-00719bb8)
- 新版 `00719bf8`（命令位置の公開資料なし）

~~~diff
- 00719bb8 ["INT_ADD", "register:40f0:8", ["const:719bb8:8", "const:4:8"]]
- 00719bb8 ["CALL", null, ["callee:0046d7b0:8"]]
+ 00719bf8 ["INT_ADD", "register:40f0:8", ["const:719bf8:8", "const:4:8"]]
+ 00719bf8 ["CALL", null, ["callee:0046d7b0:8"]]
- 00719bb8 bytes ee4ef597
+ 00719bf8 bytes ee4ef597
~~~


<a id="compare-8c135ffa786bc6a2d5c7944af5945f73"></a>

### [`0071a198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071a198.md) → [`0071a1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071a/0071a1d8.md) FUN_0071a1d8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071a1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071a198.md#insn-0071a1e4) · [`0071a204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071a198.md#insn-0071a204)
- 新版 `0071a224`（命令位置の公開資料なし） · `0071a244`（命令位置の公開資料なし）

~~~diff
- 0071a1e4 ["INT_ADD", "register:40f0:8", ["const:71a1e4:8", "const:4:8"]]
- 0071a1e4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0071a224 ["INT_ADD", "register:40f0:8", ["const:71a224:8", "const:4:8"]]
+ 0071a224 ["CALL", null, ["callee:00c57eb0:8"]]
- 0071a1e4 bytes 33f61494
+ 0071a224 bytes 23f71494
- 0071a204 ["INT_ADD", "register:40f0:8", ["const:71a204:8", "const:4:8"]]
- 0071a204 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0071a244 ["INT_ADD", "register:40f0:8", ["const:71a244:8", "const:4:8"]]
+ 0071a244 ["CALL", null, ["callee:00c57eb0:8"]]
- 0071a204 bytes 2bf61494
+ 0071a244 bytes 1bf71494
~~~


<a id="compare-d4ddd39fffbc83f58dc413f443eff561"></a>

### [`0071a290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071a290.md) → [`0071a2d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071a/0071a2d0.md) FUN_0071a2d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00719c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00719/00719c28.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00719c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00719/00719c68.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071a2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071a290.md#insn-0071a2b8) · [`0071a2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071a290.md#insn-0071a2c0) · [`0071a314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071a290.md#insn-0071a314)
- 新版 `0071a2f8`（命令位置の公開資料なし） · `0071a300`（命令位置の公開資料なし） · `0071a354`（命令位置の公開資料なし）

~~~diff
- 0071a2b8 ["INT_ADD", "register:40f0:8", ["const:71a2b8:8", "const:4:8"]]
- 0071a2b8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0071a2f8 ["INT_ADD", "register:40f0:8", ["const:71a2f8:8", "const:4:8"]]
+ 0071a2f8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0071a2b8 bytes fef51494
+ 0071a2f8 bytes eef61494
- 0071a2c0 ["INT_ADD", "register:40f0:8", ["const:71a2c0:8", "const:4:8"]]
- 0071a2c0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0071a300 ["INT_ADD", "register:40f0:8", ["const:71a300:8", "const:4:8"]]
+ 0071a300 ["CALL", null, ["callee:00c57eb0:8"]]
- 0071a2c0 bytes fcf51494
+ 0071a300 bytes ecf61494
- 0071a314 ["INT_ADD", "register:40f0:8", ["const:71a314:8", "const:4:8"]]
- 0071a314 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0071a354 ["INT_ADD", "register:40f0:8", ["const:71a354:8", "const:4:8"]]
+ 0071a354 ["CALL", null, ["callee:00c57eb0:8"]]
- 0071a314 bytes e7f51494
+ 0071a354 bytes d7f61494
~~~


<a id="compare-6a3438aa2b7823869b0d21ddc4738045"></a>

### [`0071a704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071a704.md) → [`0071a744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071a/0071a744.md) FUN_0071a744

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0071ad24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071ad24.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0071ad64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071a/0071ad64.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071a73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071a704.md#insn-0071a73c) · [`0071a76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071a704.md#insn-0071a76c) · [`0071a780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071a704.md#insn-0071a780)
- 新版 `0071a77c`（命令位置の公開資料なし） · `0071a7ac`（命令位置の公開資料なし） · `0071a7c0`（命令位置の公開資料なし）

~~~diff
- 0071a73c ["COPY", "register:0:8", ["register:4040:8"]]
- 0071a73c ["INT_ADD", "register:40f0:8", ["const:71a73c:8", "const:4:8"]]
- 0071a73c ["CALLIND", null, ["register:0:8"]]
+ 0071a77c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0071a77c ["INT_ADD", "register:40f0:8", ["const:71a77c:8", "const:4:8"]]
+ 0071a77c ["CALLIND", null, ["register:0:8"]]
- 0071a73c bytes 00013fd6
+ 0071a77c bytes 00013fd6
- 0071a76c ["COPY", "register:0:8", ["register:4040:8"]]
- 0071a76c ["INT_ADD", "register:40f0:8", ["const:71a76c:8", "const:4:8"]]
- 0071a76c ["CALLIND", null, ["register:0:8"]]
+ 0071a7ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 0071a7ac ["INT_ADD", "register:40f0:8", ["const:71a7ac:8", "const:4:8"]]
+ 0071a7ac ["CALLIND", null, ["register:0:8"]]
- 0071a76c bytes 00013fd6
+ 0071a7ac bytes 00013fd6
- 0071a780 ["INT_ADD", "register:40f0:8", ["const:71a780:8", "const:4:8"]]
- 0071a780 ["CALL", null, ["callee:0048793c:8"]]
+ 0071a7c0 ["INT_ADD", "register:40f0:8", ["const:71a7c0:8", "const:4:8"]]
+ 0071a7c0 ["CALL", null, ["callee:0048793c:8"]]
- 0071a780 bytes 5fb4f597
+ 0071a7c0 bytes 5fb4f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff3053640357f20b3390f12e21872f6f"></a>

### [`0071a85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071a85c.md) → [`0071a89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071a/0071a89c.md) FUN_0071a89c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0071ad24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071ad24.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0071ad64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071a/0071ad64.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071a898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071a85c.md#insn-0071a898) · [`0071a8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071a85c.md#insn-0071a8c4) · [`0071a8d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071a85c.md#insn-0071a8d8)
- 新版 `0071a8d8`（命令位置の公開資料なし） · `0071a904`（命令位置の公開資料なし） · `0071a918`（命令位置の公開資料なし）

~~~diff
- 0071a898 ["COPY", "register:0:8", ["register:4040:8"]]
- 0071a898 ["INT_ADD", "register:40f0:8", ["const:71a898:8", "const:4:8"]]
- 0071a898 ["CALLIND", null, ["register:0:8"]]
+ 0071a8d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0071a8d8 ["INT_ADD", "register:40f0:8", ["const:71a8d8:8", "const:4:8"]]
+ 0071a8d8 ["CALLIND", null, ["register:0:8"]]
- 0071a898 bytes 00013fd6
+ 0071a8d8 bytes 00013fd6
- 0071a8c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0071a8c4 ["INT_ADD", "register:40f0:8", ["const:71a8c4:8", "const:4:8"]]
- 0071a8c4 ["CALLIND", null, ["register:0:8"]]
+ 0071a904 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0071a904 ["INT_ADD", "register:40f0:8", ["const:71a904:8", "const:4:8"]]
+ 0071a904 ["CALLIND", null, ["register:0:8"]]
- 0071a8c4 bytes 00013fd6
+ 0071a904 bytes 00013fd6
- 0071a8d8 ["INT_ADD", "register:40f0:8", ["const:71a8d8:8", "const:4:8"]]
- 0071a8d8 ["CALL", null, ["callee:0048793c:8"]]
+ 0071a918 ["INT_ADD", "register:40f0:8", ["const:71a918:8", "const:4:8"]]
+ 0071a918 ["CALL", null, ["callee:0048793c:8"]]
- 0071a8d8 bytes 09b4f597
+ 0071a918 bytes 09b4f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56ac42e7122c8c4ba8abb3befe2a1ce7"></a>

### [`0071a9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071a9b8.md) → [`0071a9f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071a/0071a9f8.md) FUN_0071a9f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0071ad24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071ad24.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0071ad64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071a/0071ad64.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071a9f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071a9b8.md#insn-0071a9f4) · [`0071aa20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071a9b8.md#insn-0071aa20) · [`0071aa34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071a9b8.md#insn-0071aa34)
- 新版 `0071aa34`（命令位置の公開資料なし） · `0071aa60`（命令位置の公開資料なし） · `0071aa74`（命令位置の公開資料なし）

~~~diff
- 0071a9f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0071a9f4 ["INT_ADD", "register:40f0:8", ["const:71a9f4:8", "const:4:8"]]
- 0071a9f4 ["CALLIND", null, ["register:0:8"]]
+ 0071aa34 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0071aa34 ["INT_ADD", "register:40f0:8", ["const:71aa34:8", "const:4:8"]]
+ 0071aa34 ["CALLIND", null, ["register:0:8"]]
- 0071a9f4 bytes 00013fd6
+ 0071aa34 bytes 00013fd6
- 0071aa20 ["COPY", "register:0:8", ["register:4040:8"]]
- 0071aa20 ["INT_ADD", "register:40f0:8", ["const:71aa20:8", "const:4:8"]]
- 0071aa20 ["CALLIND", null, ["register:0:8"]]
+ 0071aa60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0071aa60 ["INT_ADD", "register:40f0:8", ["const:71aa60:8", "const:4:8"]]
+ 0071aa60 ["CALLIND", null, ["register:0:8"]]
- 0071aa20 bytes 00013fd6
+ 0071aa60 bytes 00013fd6
- 0071aa34 ["INT_ADD", "register:40f0:8", ["const:71aa34:8", "const:4:8"]]
- 0071aa34 ["CALL", null, ["callee:0048793c:8"]]
+ 0071aa74 ["INT_ADD", "register:40f0:8", ["const:71aa74:8", "const:4:8"]]
+ 0071aa74 ["CALL", null, ["callee:0048793c:8"]]
- 0071aa34 bytes b2b3f597
+ 0071aa74 bytes b2b3f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35cddeac7a4070ca20e57edcec4f8aaa"></a>

### [`0071ab14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071ab14.md) → [`0071ab54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071a/0071ab54.md) FUN_0071ab54

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0071ad24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071ad24.md) · 呼出先 1件 [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md)
- 新版 呼出元 1件 [`0071ad64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071a/0071ad64.md) · 呼出先 1件 [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071ab14.md#insn-0071ab30) · [`0071ab48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071ab14.md#insn-0071ab48) · [`0071ab58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071ab14.md#insn-0071ab58)
- 新版 `0071ab70`（命令位置の公開資料なし） · `0071ab88`（命令位置の公開資料なし） · `0071ab98`（命令位置の公開資料なし）

~~~diff
- 0071ab30 ["INT_ADD", "register:40f0:8", ["const:71ab30:8", "const:4:8"]]
- 0071ab30 ["CALL", null, ["callee:0048793c:8"]]
+ 0071ab70 ["INT_ADD", "register:40f0:8", ["const:71ab70:8", "const:4:8"]]
+ 0071ab70 ["CALL", null, ["callee:0048793c:8"]]
- 0071ab30 bytes 73b3f597
+ 0071ab70 bytes 73b3f597
- 0071ab48 ["INT_ADD", "register:40f0:8", ["const:71ab48:8", "const:4:8"]]
- 0071ab48 ["CALL", null, ["callee:0048793c:8"]]
+ 0071ab88 ["INT_ADD", "register:40f0:8", ["const:71ab88:8", "const:4:8"]]
+ 0071ab88 ["CALL", null, ["callee:0048793c:8"]]
- 0071ab48 bytes 6db3f597
+ 0071ab88 bytes 6db3f597
- 0071ab58 ["INT_ADD", "register:40f0:8", ["const:71ab58:8", "const:4:8"]]
- 0071ab58 ["CALL", null, ["callee:0048793c:8"]]
+ 0071ab98 ["INT_ADD", "register:40f0:8", ["const:71ab98:8", "const:4:8"]]
+ 0071ab98 ["CALL", null, ["callee:0048793c:8"]]
- 0071ab58 bytes 69b3f597
+ 0071ab98 bytes 69b3f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ddc8b1ba1788ed707886a19660cbe34"></a>

### [`0071e2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e2b4.md) → [`0071e2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071e2f4.md) FUN_0071e2f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0071d1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d1bc.md) · 呼出先 3件 [`00b3ba38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba38.md) [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md) [`00b3bab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3bab0.md)
- 新版 呼出元 1件 [`0071d1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071d/0071d1fc.md) · 呼出先 3件 [`00b3be60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be60.md) [`00b3be94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be94.md) [`00b3bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3bed8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071e2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e2b4.md#insn-0071e2f4) · [`0071e2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e2b4.md#insn-0071e2fc) · [`0071e330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e2b4.md#insn-0071e330)
- 新版 `0071e334`（命令位置の公開資料なし） · `0071e33c`（命令位置の公開資料なし） · `0071e370`（命令位置の公開資料なし）

~~~diff
- 0071e2f4 ["INT_ADD", "register:40f0:8", ["const:71e2f4:8", "const:4:8"]]
- 0071e2f4 ["CALL", null, ["callee:00b3bed8:8"]]
+ 0071e334 ["INT_ADD", "register:40f0:8", ["const:71e334:8", "const:4:8"]]
+ 0071e334 ["CALL", null, ["callee:00b3bed8:8"]]
- 0071e2f4 bytes ef751094
+ 0071e334 bytes e9761094
- 0071e2fc ["INT_ADD", "register:40f0:8", ["const:71e2fc:8", "const:4:8"]]
- 0071e2fc ["CALL", null, ["callee:00b3be94:8"]]
+ 0071e33c ["INT_ADD", "register:40f0:8", ["const:71e33c:8", "const:4:8"]]
+ 0071e33c ["CALL", null, ["callee:00b3be94:8"]]
- 0071e2fc bytes dc751094
+ 0071e33c bytes d6761094
- 0071e330 ["INT_ADD", "register:40f0:8", ["const:71e330:8", "const:4:8"]]
- 0071e330 ["CALL", null, ["callee:00b3bed8:8"]]
+ 0071e370 ["INT_ADD", "register:40f0:8", ["const:71e370:8", "const:4:8"]]
+ 0071e370 ["CALL", null, ["callee:00b3bed8:8"]]
- 0071e330 bytes e0751094
+ 0071e370 bytes da761094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89a7e3b854f2689daede21a5d4b18d43"></a>

### [`0071e78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e78c.md) → [`0071e7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071e7cc.md) FUN_0071e7cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0071d1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d1bc.md) · 呼出先 3件 [`00b3ba38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba38.md) [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md) [`00b3bab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3bab0.md)
- 新版 呼出元 1件 [`0071d1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071d/0071d1fc.md) · 呼出先 3件 [`00b3be60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be60.md) [`00b3be94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be94.md) [`00b3bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3bed8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071e7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e78c.md#insn-0071e7b4) · [`0071e7bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e78c.md#insn-0071e7bc)
- 新版 `0071e7f4`（命令位置の公開資料なし） · `0071e7fc`（命令位置の公開資料なし）

~~~diff
- 0071e7b4 ["INT_ADD", "register:40f0:8", ["const:71e7b4:8", "const:4:8"]]
- 0071e7b4 ["CALL", null, ["callee:00b3bed8:8"]]
+ 0071e7f4 ["INT_ADD", "register:40f0:8", ["const:71e7f4:8", "const:4:8"]]
+ 0071e7f4 ["CALL", null, ["callee:00b3bed8:8"]]
- 0071e7b4 bytes bf741094
+ 0071e7f4 bytes b9751094
- 0071e7bc ["INT_ADD", "register:40f0:8", ["const:71e7bc:8", "const:4:8"]]
- 0071e7bc ["CALL", null, ["callee:00b3be94:8"]]
+ 0071e7fc ["INT_ADD", "register:40f0:8", ["const:71e7fc:8", "const:4:8"]]
+ 0071e7fc ["CALL", null, ["callee:00b3be94:8"]]
- 0071e7bc bytes ac741094
+ 0071e7fc bytes a6751094
~~~


<a id="compare-931e3883bcec35d076bd1d92269ae147"></a>

### [`0071e7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e7f4.md) → [`0071e834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071e834.md) FUN_0071e834

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0071d1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d1bc.md) · 呼出先 6件 [`00697250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697250.md) [`00b3ba38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba38.md) [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md) [`00b3bab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3bab0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0071d1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071d/0071d1fc.md) · 呼出先 6件 [`00697290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697290.md) [`00b3be60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be60.md) [`00b3be94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be94.md) [`00b3bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3bed8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071e834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e7f4.md#insn-0071e834) · [`0071e83c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e7f4.md#insn-0071e83c) · [`0071e854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e7f4.md#insn-0071e854)
- 新版 `0071e874`（命令位置の公開資料なし） · `0071e87c`（命令位置の公開資料なし） · `0071e894`（命令位置の公開資料なし）

~~~diff
- 0071e834 ["INT_ADD", "register:40f0:8", ["const:71e834:8", "const:4:8"]]
- 0071e834 ["CALL", null, ["callee:00b3bed8:8"]]
+ 0071e874 ["INT_ADD", "register:40f0:8", ["const:71e874:8", "const:4:8"]]
+ 0071e874 ["CALL", null, ["callee:00b3bed8:8"]]
- 0071e834 bytes 9f741094
+ 0071e874 bytes 99751094
- 0071e83c ["INT_ADD", "register:40f0:8", ["const:71e83c:8", "const:4:8"]]
- 0071e83c ["CALL", null, ["callee:00b3be94:8"]]
+ 0071e87c ["INT_ADD", "register:40f0:8", ["const:71e87c:8", "const:4:8"]]
+ 0071e87c ["CALL", null, ["callee:00b3be94:8"]]
- 0071e83c bytes 8c741094
+ 0071e87c bytes 86751094
- 0071e854 ["INT_ADD", "register:40f0:8", ["const:71e854:8", "const:4:8"]]
- 0071e854 ["CALL", null, ["callee:00b3be60:8"]]
+ 0071e894 ["INT_ADD", "register:40f0:8", ["const:71e894:8", "const:4:8"]]
+ 0071e894 ["CALL", null, ["callee:00b3be60:8"]]
- 0071e854 bytes 79741094
+ 0071e894 bytes 73751094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5df01e32d04d8942712a35509f11ce25"></a>

### [`0071ed38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071ed38.md) → [`0071ed78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071ed78.md) FUN_0071ed78

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`005f466c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f4/005f466c.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) [`00963e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00963/00963e3c.md) · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 7件 [`005f46ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f4/005f46ac.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`00963fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00963/00963fd8.md) · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071ed78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071ed38.md#insn-0071ed78) · [`0071ed84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071ed38.md#insn-0071ed84) · [`0071ed88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071ed38.md#insn-0071ed88)
- 新版 `0071edb8`（命令位置の公開資料なし） · `0071edc4`（命令位置の公開資料なし） · `0071edc8`（命令位置の公開資料なし）

~~~diff
- 0071ed78 ["INT_ADD", "register:40f0:8", ["const:71ed78:8", "const:4:8"]]
- 0071ed78 ["CALL", null, ["callee:008514f8:8"]]
+ 0071edb8 ["INT_ADD", "register:40f0:8", ["const:71edb8:8", "const:4:8"]]
+ 0071edb8 ["CALL", null, ["callee:008514f8:8"]]
- 0071ed78 bytes d0c90494
+ 0071edb8 bytes d0c90494
- 0071ed84 ["INT_ADD", "register:40f0:8", ["const:71ed84:8", "const:4:8"]]
- 0071ed84 ["CALL", null, ["callee:008514f8:8"]]
+ 0071edc4 ["INT_ADD", "register:40f0:8", ["const:71edc4:8", "const:4:8"]]
+ 0071edc4 ["CALL", null, ["callee:008514f8:8"]]
- 0071ed84 bytes cdc90494
+ 0071edc4 bytes cdc90494
- 0071ed88 ["INT_ADD", "register:40f0:8", ["const:71ed88:8", "const:4:8"]]
- 0071ed88 ["CALL", null, ["callee:008514f8:8"]]
+ 0071edc8 ["INT_ADD", "register:40f0:8", ["const:71edc8:8", "const:4:8"]]
+ 0071edc8 ["CALL", null, ["callee:008514f8:8"]]
- 0071ed88 bytes ccc90494
+ 0071edc8 bytes ccc90494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec4e4762267588002e09c370a96bbeed"></a>

### [`0071f420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071f/0071f420.md) → [`0071f460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071f/0071f460.md) FUN_0071f460

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009d8e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d8/009d8e7c.md) · 呼出先 4件 [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`005e8158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e8/005e8158.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`009d9018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d9/009d9018.md) · 呼出先 4件 [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`005e8198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e8/005e8198.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071f44c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071f/0071f420.md#insn-0071f44c) · [`0071f458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071f/0071f420.md#insn-0071f458) · [`0071f464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071f/0071f420.md#insn-0071f464)
- 新版 `0071f48c`（命令位置の公開資料なし） · `0071f498`（命令位置の公開資料なし） · `0071f4a4`（命令位置の公開資料なし）

~~~diff
- 0071f44c ["INT_ADD", "register:40f0:8", ["const:71f44c:8", "const:4:8"]]
- 0071f44c ["CALL", null, ["callee:0048791c:8"]]
+ 0071f48c ["INT_ADD", "register:40f0:8", ["const:71f48c:8", "const:4:8"]]
+ 0071f48c ["CALL", null, ["callee:0048791c:8"]]
- 0071f44c bytes 24a1f597
+ 0071f48c bytes 24a1f597
- 0071f458 ["INT_ADD", "register:40f0:8", ["const:71f458:8", "const:4:8"]]
- 0071f458 ["CALL", null, ["callee:0048793c:8"]]
+ 0071f498 ["INT_ADD", "register:40f0:8", ["const:71f498:8", "const:4:8"]]
+ 0071f498 ["CALL", null, ["callee:0048793c:8"]]
- 0071f458 bytes 29a1f597
+ 0071f498 bytes 29a1f597
- 0071f464 ["INT_ADD", "register:40f0:8", ["const:71f464:8", "const:4:8"]]
- 0071f464 ["CALL", null, ["callee:005e8198:8"]]
+ 0071f4a4 ["INT_ADD", "register:40f0:8", ["const:71f4a4:8", "const:4:8"]]
+ 0071f4a4 ["CALL", null, ["callee:005e8198:8"]]
- 0071f464 bytes 3d23fb97
+ 0071f4a4 bytes 3d23fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b797314c381646798c4c65be9d5f9ab5"></a>

### [`00725230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725230.md) → [`00725270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00725/00725270.md) FUN_00725270

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0075d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`0075d75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075d/0075d75c.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00725308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725230.md#insn-00725308) · [`00725340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725230.md#insn-00725340) · [`007253cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725230.md#insn-007253cc)
- 新版 `00725348`（命令位置の公開資料なし） · `00725380`（命令位置の公開資料なし） · `0072540c`（命令位置の公開資料なし）

~~~diff
- 00725308 ["INT_ADD", "register:40f0:8", ["const:725308:8", "const:4:8"]]
- 00725308 ["CALL", null, ["callee:00c57e90:8"]]
+ 00725348 ["INT_ADD", "register:40f0:8", ["const:725348:8", "const:4:8"]]
+ 00725348 ["CALL", null, ["callee:00c57e90:8"]]
- 00725308 bytes e2c91494
+ 00725348 bytes d2ca1494
- 00725340 ["INT_ADD", "register:40f0:8", ["const:725340:8", "const:4:8"]]
- 00725340 ["CALL", null, ["callee:0043bba4:8"]]
+ 00725380 ["INT_ADD", "register:40f0:8", ["const:725380:8", "const:4:8"]]
+ 00725380 ["CALL", null, ["callee:0043bba4:8"]]
- 00725340 bytes 095af497
+ 00725380 bytes 095af497
- 007253cc ["INT_ADD", "register:40f0:8", ["const:7253cc:8", "const:4:8"]]
- 007253cc ["CALL", null, ["callee:00c57e90:8"]]
+ 0072540c ["INT_ADD", "register:40f0:8", ["const:72540c:8", "const:4:8"]]
+ 0072540c ["CALL", null, ["callee:00c57e90:8"]]
- 007253cc bytes b1c91494
+ 0072540c bytes a1ca1494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4618b23f63919f8df1783d05af350eac"></a>

### [`00725d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725d4c.md) → [`00725d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00725/00725d8c.md) FUN_00725d8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00725d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725d4c.md#insn-00725d68) · [`00725d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725d4c.md#insn-00725d74) · [`00725dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725d4c.md#insn-00725dac)
- 新版 `00725da8`（命令位置の公開資料なし） · `00725db4`（命令位置の公開資料なし） · `00725dec`（命令位置の公開資料なし）

~~~diff
- 00725d68 ["INT_ADD", "register:40f0:8", ["const:725d68:8", "const:4:8"]]
- 00725d68 ["CALL", null, ["callee:0046d490:8"]]
+ 00725da8 ["INT_ADD", "register:40f0:8", ["const:725da8:8", "const:4:8"]]
+ 00725da8 ["CALL", null, ["callee:0046d490:8"]]
- 00725d68 bytes ba1df597
+ 00725da8 bytes ba1df597
- 00725d74 ["INT_ADD", "register:40f0:8", ["const:725d74:8", "const:4:8"]]
- 00725d74 ["CALL", null, ["callee:0046d490:8"]]
+ 00725db4 ["INT_ADD", "register:40f0:8", ["const:725db4:8", "const:4:8"]]
+ 00725db4 ["CALL", null, ["callee:0046d490:8"]]
- 00725d74 bytes b71df597
+ 00725db4 bytes b71df597
- 00725dac ["INT_ADD", "register:40f0:8", ["const:725dac:8", "const:4:8"]]
- 00725dac ["CALL", null, ["callee:00c57eb0:8"]]
+ 00725dec ["INT_ADD", "register:40f0:8", ["const:725dec:8", "const:4:8"]]
+ 00725dec ["CALL", null, ["callee:00c57eb0:8"]]
- 00725dac bytes 41c71494
+ 00725dec bytes 31c81494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd5e9b9b6586af1bd3e33d360362c88c"></a>

### [`00725dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725dec.md) → [`00725e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00725/00725e2c.md) FUN_00725e2c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00725e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725dec.md#insn-00725e34) · [`00725e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725dec.md#insn-00725e44)
- 新版 `00725e74`（命令位置の公開資料なし） · `00725e84`（命令位置の公開資料なし）

~~~diff
- 00725e34 ["INT_ADD", "register:40f0:8", ["const:725e34:8", "const:4:8"]]
- 00725e34 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00725e74 ["INT_ADD", "register:40f0:8", ["const:725e74:8", "const:4:8"]]
+ 00725e74 ["CALL", null, ["callee:00c57eb0:8"]]
- 00725e34 bytes 1fc71494
+ 00725e74 bytes 0fc81494
- 00725e44 ["INT_ADD", "register:40f0:8", ["const:725e44:8", "const:4:8"]]
- 00725e44 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00725e84 ["INT_ADD", "register:40f0:8", ["const:725e84:8", "const:4:8"]]
+ 00725e84 ["CALL", null, ["callee:00c57eb0:8"]]
- 00725e44 bytes 1bc71494
+ 00725e84 bytes 0bc81494
~~~


<a id="compare-9635a45dd46164a36a881482b8e57ff7"></a>

### [`00725e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725e74.md) → [`00725eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00725/00725eb4.md) FUN_00725eb4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00725424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725424.md) [`00a3446c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a34/00a3446c.md) · 呼出先 6件 [`00725fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725fb4.md) [`0072604c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/0072604c.md) [`007260c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/007260c4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`00725464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00725/00725464.md) [`00a34664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a34/00a34664.md) · 呼出先 6件 [`00725ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00725/00725ff4.md) [`0072608c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/0072608c.md) [`00726104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726104.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00725ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725e74.md#insn-00725ecc) · [`00725f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725e74.md#insn-00725f10) · [`00725f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725e74.md#insn-00725f74)
- 新版 `00725f0c`（命令位置の公開資料なし） · `00725f50`（命令位置の公開資料なし） · `00725fb4`（命令位置の公開資料なし）

~~~diff
- 00725ecc ["INT_ADD", "register:40f0:8", ["const:725ecc:8", "const:4:8"]]
- 00725ecc ["CALL", null, ["callee:00c57e90:8"]]
+ 00725f0c ["INT_ADD", "register:40f0:8", ["const:725f0c:8", "const:4:8"]]
+ 00725f0c ["CALL", null, ["callee:00c57e90:8"]]
- 00725ecc bytes f1c61494
+ 00725f0c bytes e1c71494
- 00725f10 ["INT_ADD", "register:40f0:8", ["const:725f10:8", "const:4:8"]]
- 00725f10 ["CALL", null, ["callee:00726104:8"]]
+ 00725f50 ["INT_ADD", "register:40f0:8", ["const:725f50:8", "const:4:8"]]
+ 00725f50 ["CALL", null, ["callee:00726104:8"]]
- 00725f10 bytes 6d000094
+ 00725f50 bytes 6d000094
- 00725f74 ["INT_ADD", "register:40f0:8", ["const:725f74:8", "const:4:8"]]
- 00725f74 ["CALL", null, ["callee:0072608c:8"]]
+ 00725fb4 ["INT_ADD", "register:40f0:8", ["const:725fb4:8", "const:4:8"]]
+ 00725fb4 ["CALL", null, ["callee:0072608c:8"]]
- 00725f74 bytes 36000094
+ 00725fb4 bytes 36000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e4b26b2fccb5061f5d5f80a74a1223a"></a>

### [`00725fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725fb4.md) → [`00725ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00725/00725ff4.md) FUN_00725ff4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00725e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725e74.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00725eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00725/00725eb4.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00726018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725fb4.md#insn-00726018) · [`00726028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725fb4.md#insn-00726028)
- 新版 `00726058`（命令位置の公開資料なし） · `00726068`（命令位置の公開資料なし）

~~~diff
- 00726018 ["INT_ADD", "register:40f0:8", ["const:726018:8", "const:4:8"]]
- 00726018 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00726058 ["INT_ADD", "register:40f0:8", ["const:726058:8", "const:4:8"]]
+ 00726058 ["CALL", null, ["callee:00c57eb0:8"]]
- 00726018 bytes a6c61494
+ 00726058 bytes 96c71494
- 00726028 ["INT_ADD", "register:40f0:8", ["const:726028:8", "const:4:8"]]
- 00726028 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00726068 ["INT_ADD", "register:40f0:8", ["const:726068:8", "const:4:8"]]
+ 00726068 ["CALL", null, ["callee:00c57eb0:8"]]
- 00726028 bytes a2c61494
+ 00726068 bytes 92c71494
~~~


<a id="compare-34db090acdb3d2cdb57a6a83ec773294"></a>

### [`00726060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726060.md) → [`007260a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/007260a0.md) FUN_007260a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0077c150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c150.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0077c190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c190.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007260a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726060.md#insn-007260a0) · [`007260b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726060.md#insn-007260b0)
- 新版 `007260e0`（命令位置の公開資料なし） · `007260f0`（命令位置の公開資料なし）

~~~diff
- 007260a0 ["INT_ADD", "register:40f0:8", ["const:7260a0:8", "const:4:8"]]
- 007260a0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007260e0 ["INT_ADD", "register:40f0:8", ["const:7260e0:8", "const:4:8"]]
+ 007260e0 ["CALL", null, ["callee:00c57eb0:8"]]
- 007260a0 bytes 84c61494
+ 007260e0 bytes 74c71494
- 007260b0 ["INT_ADD", "register:40f0:8", ["const:7260b0:8", "const:4:8"]]
- 007260b0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007260f0 ["INT_ADD", "register:40f0:8", ["const:7260f0:8", "const:4:8"]]
+ 007260f0 ["CALL", null, ["callee:00c57eb0:8"]]
- 007260b0 bytes 80c61494
+ 007260f0 bytes 70c71494
~~~


<a id="compare-a77d4962efbc5e1e6699ddbcbf2806fc"></a>

### [`007260c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/007260c4.md) → [`00726104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726104.md) FUN_00726104

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00725e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725e74.md) [`0077c150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c150.md) · 呼出先 5件 [`00726220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726220.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 2件 [`00725eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00725/00725eb4.md) [`0077c190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c190.md) · 呼出先 5件 [`00726260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726260.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00726140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/007260c4.md#insn-00726140) · [`00726158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/007260c4.md#insn-00726158) · [`00726194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/007260c4.md#insn-00726194)
- 新版 `00726180`（命令位置の公開資料なし） · `00726198`（命令位置の公開資料なし） · `007261d4`（命令位置の公開資料なし）

~~~diff
- 00726140 ["INT_ADD", "register:40f0:8", ["const:726140:8", "const:4:8"]]
- 00726140 ["CALL", null, ["callee:00c57e90:8"]]
+ 00726180 ["INT_ADD", "register:40f0:8", ["const:726180:8", "const:4:8"]]
+ 00726180 ["CALL", null, ["callee:00c57e90:8"]]
- 00726140 bytes 54c61494
+ 00726180 bytes 44c71494
- 00726158 ["INT_ADD", "register:40f0:8", ["const:726158:8", "const:4:8"]]
- 00726158 ["CALL", null, ["callee:00c58000:8"]]
+ 00726198 ["INT_ADD", "register:40f0:8", ["const:726198:8", "const:4:8"]]
+ 00726198 ["CALL", null, ["callee:00c58000:8"]]
- 00726158 bytes aac61494
+ 00726198 bytes 9ac71494
- 00726194 ["INT_ADD", "register:40f0:8", ["const:726194:8", "const:4:8"]]
- 00726194 ["CALL", null, ["callee:00c57e90:8"]]
+ 007261d4 ["INT_ADD", "register:40f0:8", ["const:7261d4:8", "const:4:8"]]
+ 007261d4 ["CALL", null, ["callee:00c57e90:8"]]
- 00726194 bytes 3fc61494
+ 007261d4 bytes 2fc71494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4657957370591c0a122ea2ca5950df11"></a>

### [`00726234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726234.md) → [`00726274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726274.md) FUN_00726274

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00725424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725424.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0053bc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bc70.md) [`0054f154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f154.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00725464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00725/00725464.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0053bcb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bcb0.md) [`0054f194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054f/0054f194.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00726290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726234.md#insn-00726290) · [`007262b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726234.md#insn-007262b8) · [`007262e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726234.md#insn-007262e4)
- 新版 `007262d0`（命令位置の公開資料なし） · `007262f8`（命令位置の公開資料なし） · `00726324`（命令位置の公開資料なし）

~~~diff
- 00726290 ["INT_ADD", "register:40f0:8", ["const:726290:8", "const:4:8"]]
- 00726290 ["CALL", null, ["callee:0054f194:8"]]
+ 007262d0 ["INT_ADD", "register:40f0:8", ["const:7262d0:8", "const:4:8"]]
+ 007262d0 ["CALL", null, ["callee:0054f194:8"]]
- 00726290 bytes b1a3f897
+ 007262d0 bytes b1a3f897
- 007262b8 ["INT_ADD", "register:40f0:8", ["const:7262b8:8", "const:4:8"]]
- 007262b8 ["CALL", null, ["callee:0053bcb0:8"]]
+ 007262f8 ["INT_ADD", "register:40f0:8", ["const:7262f8:8", "const:4:8"]]
+ 007262f8 ["CALL", null, ["callee:0053bcb0:8"]]
- 007262b8 bytes 6e56f897
+ 007262f8 bytes 6e56f897
- 007262e4 ["INT_ADD", "register:40f0:8", ["const:7262e4:8", "const:4:8"]]
- 007262e4 ["CALL", null, ["callee:0043bba4:8"]]
+ 00726324 ["INT_ADD", "register:40f0:8", ["const:726324:8", "const:4:8"]]
+ 00726324 ["CALL", null, ["callee:0043bba4:8"]]
- 007262e4 bytes 2056f497
+ 00726324 bytes 2056f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d8ecd1f6e13cb0a77c3ee119d3c3d18"></a>

### [`00726350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726350.md) → [`00726390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726390.md) FUN_00726390

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`007247b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00724/007247b0.md) [`00726350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726350.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849b94.md) · 呼出先 3件 [`00726350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726350.md) [`007263a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/007263a0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`007247f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00724/007247f0.md) [`00726390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726390.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849bd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849bd4.md) · 呼出先 3件 [`00726390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726390.md) [`007263e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/007263e0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00726370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726350.md#insn-00726370) · [`0072637c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726350.md#insn-0072637c) · [`00726388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726350.md#insn-00726388)
- 新版 `007263b0`（命令位置の公開資料なし） · `007263bc`（命令位置の公開資料なし） · `007263c8`（命令位置の公開資料なし）

~~~diff
- 00726370 ["INT_ADD", "register:40f0:8", ["const:726370:8", "const:4:8"]]
- 00726370 ["CALL", null, ["local:b0:8"]]
+ 007263b0 ["INT_ADD", "register:40f0:8", ["const:7263b0:8", "const:4:8"]]
+ 007263b0 ["CALL", null, ["local:b0:8"]]
- 00726370 bytes f8ffff97
+ 007263b0 bytes f8ffff97
- 0072637c ["INT_ADD", "register:40f0:8", ["const:72637c:8", "const:4:8"]]
- 0072637c ["CALL", null, ["local:b0:8"]]
+ 007263bc ["INT_ADD", "register:40f0:8", ["const:7263bc:8", "const:4:8"]]
+ 007263bc ["CALL", null, ["local:b0:8"]]
- 0072637c bytes f5ffff97
+ 007263bc bytes f5ffff97
- 00726388 ["INT_ADD", "register:40f0:8", ["const:726388:8", "const:4:8"]]
- 00726388 ["CALL", null, ["callee:007263e0:8"]]
+ 007263c8 ["INT_ADD", "register:40f0:8", ["const:7263c8:8", "const:4:8"]]
+ 007263c8 ["CALL", null, ["callee:007263e0:8"]]
- 00726388 bytes 06000094
+ 007263c8 bytes 06000094
~~~


<a id="compare-375e55e19359893c0a5e1d0078f2fa70"></a>

### [`007263a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/007263a0.md) → [`007263e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/007263e0.md) FUN_007263e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00726350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726350.md) [`007263a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/007263a0.md) · 呼出先 2件 [`007263a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/007263a0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00726390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726390.md) [`007263e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/007263e0.md) · 呼出先 2件 [`007263e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/007263e0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007263bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/007263a0.md#insn-007263bc) · [`007263c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/007263a0.md#insn-007263c8) · [`007263d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/007263a0.md#insn-007263d8)
- 新版 `007263fc`（命令位置の公開資料なし） · `00726408`（命令位置の公開資料なし） · `00726418`（命令位置の公開資料なし）

~~~diff
- 007263bc ["INT_ADD", "register:40f0:8", ["const:7263bc:8", "const:4:8"]]
- 007263bc ["CALL", null, ["local:b0:8"]]
+ 007263fc ["INT_ADD", "register:40f0:8", ["const:7263fc:8", "const:4:8"]]
+ 007263fc ["CALL", null, ["local:b0:8"]]
- 007263bc bytes f9ffff97
+ 007263fc bytes f9ffff97
- 007263c8 ["INT_ADD", "register:40f0:8", ["const:7263c8:8", "const:4:8"]]
- 007263c8 ["CALL", null, ["local:b0:8"]]
+ 00726408 ["INT_ADD", "register:40f0:8", ["const:726408:8", "const:4:8"]]
+ 00726408 ["CALL", null, ["local:b0:8"]]
- 007263c8 bytes f6ffff97
+ 00726408 bytes f6ffff97
- 007263d8 ["INT_ADD", "register:40f0:8", ["const:7263d8:8", "const:4:8"]]
- 007263d8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00726418 ["INT_ADD", "register:40f0:8", ["const:726418:8", "const:4:8"]]
+ 00726418 ["CALL", null, ["callee:00c57eb0:8"]]
- 007263d8 bytes b6c51494
+ 00726418 bytes a6c61494
~~~


<a id="compare-2fbc3e3dcc0919fcecf741f15ca949eb"></a>

### [`00726f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726f08.md) → [`00726f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726f48.md) FUN_00726f48

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) [`00930278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00930/00930278.md) [`00934bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934bbc.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 1件 [`00550984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550984.md)
- 新版 呼出元 4件 [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`00930414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00930/00930414.md) [`00934d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934d58.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 1件 [`005509c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509c4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00726f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726f08.md#insn-00726f18)
- 新版 `00726f58`（命令位置の公開資料なし）

~~~diff
- 00726f18 ["INT_ADD", "register:40f0:8", ["const:726f18:8", "const:4:8"]]
- 00726f18 ["CALL", null, ["callee:005509c4:8"]]
+ 00726f58 ["INT_ADD", "register:40f0:8", ["const:726f58:8", "const:4:8"]]
+ 00726f58 ["CALL", null, ["callee:005509c4:8"]]
- 00726f18 bytes 9ba6f897
+ 00726f58 bytes 9ba6f897
~~~


<a id="compare-492b300018b00b681cebee6f3ffad31d"></a>

### [`00726f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726f30.md) → [`00726f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726f70.md) FUN_00726f70

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`009302e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00930/009302e0.md) · 呼出先 1件 [`00550988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550988.md)
- 新版 呼出元 4件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`0093047c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00930/0093047c.md) · 呼出先 1件 [`005509c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00726f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726f30.md#insn-00726f40)
- 新版 `00726f80`（命令位置の公開資料なし）

~~~diff
- 00726f40 ["INT_ADD", "register:40f0:8", ["const:726f40:8", "const:4:8"]]
- 00726f40 ["CALL", null, ["callee:005509c8:8"]]
+ 00726f80 ["INT_ADD", "register:40f0:8", ["const:726f80:8", "const:4:8"]]
+ 00726f80 ["CALL", null, ["callee:005509c8:8"]]
- 00726f40 bytes 92a6f897
+ 00726f80 bytes 92a6f897
~~~


<a id="compare-0cca66e138043e5963474881690617fe"></a>

### [`00727120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727120.md) → [`00727160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727160.md) FUN_00727160

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`0055098c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/0055098c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`005509cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509cc.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00727148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727120.md#insn-00727148) · [`00727154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727120.md#insn-00727154) · [`007271b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727120.md#insn-007271b0)
- 新版 `00727188`（命令位置の公開資料なし） · `00727194`（命令位置の公開資料なし） · `007271f0`（命令位置の公開資料なし）

~~~diff
- 00727148 ["INT_ADD", "register:40f0:8", ["const:727148:8", "const:4:8"]]
- 00727148 ["CALL", null, ["callee:008514f8:8"]]
+ 00727188 ["INT_ADD", "register:40f0:8", ["const:727188:8", "const:4:8"]]
+ 00727188 ["CALL", null, ["callee:008514f8:8"]]
- 00727148 bytes dca80494
+ 00727188 bytes dca80494
- 00727154 ["INT_ADD", "register:40f0:8", ["const:727154:8", "const:4:8"]]
- 00727154 ["CALL", null, ["callee:0048ce84:8"]]
+ 00727194 ["INT_ADD", "register:40f0:8", ["const:727194:8", "const:4:8"]]
+ 00727194 ["CALL", null, ["callee:0048ce84:8"]]
- 00727154 bytes 3c97f597
+ 00727194 bytes 3c97f597
- 007271b0 ["INT_ADD", "register:40f0:8", ["const:7271b0:8", "const:4:8"]]
- 007271b0 ["CALL", null, ["callee:00c57e90:8"]]
+ 007271f0 ["INT_ADD", "register:40f0:8", ["const:7271f0:8", "const:4:8"]]
+ 007271f0 ["CALL", null, ["callee:00c57e90:8"]]
- 007271b0 bytes 38c21494
+ 007271f0 bytes 28c31494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-316292bbbca80604347a6eeb4dcd532a"></a>

### [`0072756c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/0072756c.md) → [`007275ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007275ac.md) FUN_007275ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00726780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726780.md) [`0072756c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/0072756c.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 3件 [`0072756c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/0072756c.md) [`007275bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/007275bc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`007267c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/007267c0.md) [`007275ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007275ac.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 3件 [`007275ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007275ac.md) [`007275fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007275fc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072758c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/0072756c.md#insn-0072758c) · [`00727598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/0072756c.md#insn-00727598) · [`007275a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/0072756c.md#insn-007275a4)
- 新版 `007275cc`（命令位置の公開資料なし） · `007275d8`（命令位置の公開資料なし） · `007275e4`（命令位置の公開資料なし）

~~~diff
- 0072758c ["INT_ADD", "register:40f0:8", ["const:72758c:8", "const:4:8"]]
- 0072758c ["CALL", null, ["local:b0:8"]]
+ 007275cc ["INT_ADD", "register:40f0:8", ["const:7275cc:8", "const:4:8"]]
+ 007275cc ["CALL", null, ["local:b0:8"]]
- 0072758c bytes f8ffff97
+ 007275cc bytes f8ffff97
- 00727598 ["INT_ADD", "register:40f0:8", ["const:727598:8", "const:4:8"]]
- 00727598 ["CALL", null, ["local:b0:8"]]
+ 007275d8 ["INT_ADD", "register:40f0:8", ["const:7275d8:8", "const:4:8"]]
+ 007275d8 ["CALL", null, ["local:b0:8"]]
- 00727598 bytes f5ffff97
+ 007275d8 bytes f5ffff97
- 007275a4 ["INT_ADD", "register:40f0:8", ["const:7275a4:8", "const:4:8"]]
- 007275a4 ["CALL", null, ["callee:007275fc:8"]]
+ 007275e4 ["INT_ADD", "register:40f0:8", ["const:7275e4:8", "const:4:8"]]
+ 007275e4 ["CALL", null, ["callee:007275fc:8"]]
- 007275a4 bytes 06000094
+ 007275e4 bytes 06000094
~~~


<a id="compare-98bc60ecfb70f6b29fb6d05c97b3ddbe"></a>

### [`007275bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/007275bc.md) → [`007275fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007275fc.md) FUN_007275fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0072756c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/0072756c.md) [`007275bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/007275bc.md) · 呼出先 2件 [`007275bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/007275bc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`007275ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007275ac.md) [`007275fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007275fc.md) · 呼出先 2件 [`007275fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007275fc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007275dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/007275bc.md#insn-007275dc) · [`007275e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/007275bc.md#insn-007275e8)
- 新版 `0072761c`（命令位置の公開資料なし） · `00727628`（命令位置の公開資料なし）

~~~diff
- 007275dc ["INT_ADD", "register:40f0:8", ["const:7275dc:8", "const:4:8"]]
- 007275dc ["CALL", null, ["local:b0:8"]]
+ 0072761c ["INT_ADD", "register:40f0:8", ["const:72761c:8", "const:4:8"]]
+ 0072761c ["CALL", null, ["local:b0:8"]]
- 007275dc bytes f8ffff97
+ 0072761c bytes f8ffff97
- 007275e8 ["INT_ADD", "register:40f0:8", ["const:7275e8:8", "const:4:8"]]
- 007275e8 ["CALL", null, ["local:b0:8"]]
+ 00727628 ["INT_ADD", "register:40f0:8", ["const:727628:8", "const:4:8"]]
+ 00727628 ["CALL", null, ["local:b0:8"]]
- 007275e8 bytes f5ffff97
+ 00727628 bytes f5ffff97
~~~


<a id="compare-a9c9cedb79eb9b8ef1f910058300078f"></a>

### [`00727990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727990.md) → [`007279d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007279d0.md) FUN_007279d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 37件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`0063d8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063d8d4.md) [`0069a4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a4c4.md) [`006b8a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8a24.md) [`006e4d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e4d2c.md) · 呼出先 3件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b2f3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f3c8.md) [`00b2f458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f458.md)
- 新版 呼出元 37件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`0063d914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063d/0063d914.md) [`0069a504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069a/0069a504.md) [`006b8a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8a64.md) [`006e4d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e4d6c.md) · 呼出先 3件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b2f7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f7f0.md) [`00b2f880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f880.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007279ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727990.md#insn-007279ec) · [`00727a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727990.md#insn-00727a40) · [`00727a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727990.md#insn-00727a48)
- 新版 `00727a2c`（命令位置の公開資料なし） · `00727a80`（命令位置の公開資料なし） · `00727a88`（命令位置の公開資料なし）

~~~diff
- 007279ec ["INT_ADD", "register:40f0:8", ["const:7279ec:8", "const:4:8"]]
- 007279ec ["CALL", null, ["callee:008514f8:8"]]
+ 00727a2c ["INT_ADD", "register:40f0:8", ["const:727a2c:8", "const:4:8"]]
+ 00727a2c ["CALL", null, ["callee:008514f8:8"]]
- 007279ec bytes b3a60494
+ 00727a2c bytes b3a60494
- 00727a40 ["INT_ADD", "register:40f0:8", ["const:727a40:8", "const:4:8"]]
- 00727a40 ["CALL", null, ["callee:008514f8:8"]]
+ 00727a80 ["INT_ADD", "register:40f0:8", ["const:727a80:8", "const:4:8"]]
+ 00727a80 ["CALL", null, ["callee:008514f8:8"]]
- 00727a40 bytes 9ea60494
+ 00727a80 bytes 9ea60494
- 00727a48 ["INT_ADD", "register:40f0:8", ["const:727a48:8", "const:4:8"]]
- 00727a48 ["CALL", null, ["callee:00b2f880:8"]]
+ 00727a88 ["INT_ADD", "register:40f0:8", ["const:727a88:8", "const:4:8"]]
+ 00727a88 ["CALL", null, ["callee:00b2f880:8"]]
- 00727a48 bytes 841e1094
+ 00727a88 bytes 7e1f1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e1dc9d72c88dcb33cd27088e52224ac"></a>

### [`00727c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727c60.md) → [`00727ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727ca0.md) FUN_00727ca0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006650d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/006650d0.md) [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) [`00996ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996ea0.md) · 呼出先 1件 [`00727990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727990.md)
- 新版 呼出元 3件 [`00665110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00665/00665110.md) [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) [`0099703c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00997/0099703c.md) · 呼出先 1件 [`007279d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007279d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00727c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727c60.md#insn-00727c68)
- 新版 `00727ca8`（命令位置の公開資料なし）

~~~diff
- 00727c68 ["INT_ADD", "register:40f0:8", ["const:727c68:8", "const:4:8"]]
- 00727c68 ["CALL", null, ["callee:007279d0:8"]]
+ 00727ca8 ["INT_ADD", "register:40f0:8", ["const:727ca8:8", "const:4:8"]]
+ 00727ca8 ["CALL", null, ["callee:007279d0:8"]]
- 00727c68 bytes 4affff97
+ 00727ca8 bytes 4affff97
~~~


<a id="compare-8014b4d15dd1ec9f0c423d9e269a94fb"></a>

### [`00727c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727c7c.md) → [`00727cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727cbc.md) FUN_00727cbc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0073c8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073c/0073c8f8.md) [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`0073c938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073c/0073c938.md) [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00727c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727c7c.md#insn-00727c84)
- 新版 `00727cc4`（命令位置の公開資料なし）

~~~diff
- 00727c84 ["INT_ADD", "register:40f0:8", ["const:727c84:8", "const:4:8"]]
- 00727c84 ["CALL", null, ["callee:008514f8:8"]]
+ 00727cc4 ["INT_ADD", "register:40f0:8", ["const:727cc4:8", "const:4:8"]]
+ 00727cc4 ["CALL", null, ["callee:008514f8:8"]]
- 00727c84 bytes 0da60494
+ 00727cc4 bytes 0da60494
~~~


<a id="compare-5c243a0fb882a7ef746929e25fb5ea6f"></a>

### [`00727cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727cdc.md) → [`00727d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727d1c.md) FUN_00727d1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 28件 [`0069a4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a4c4.md) [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) [`00739464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/00739464.md) [`00739e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/00739e04.md) [`0075b984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b984.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 28件 [`0069a504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069a/0069a504.md) [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`007394a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00739/007394a4.md) [`00739e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00739/00739e44.md) [`0075b9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075b/0075b9c4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00727d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727cdc.md#insn-00727d08) · [`00727d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727cdc.md#insn-00727d64) · [`00727db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727cdc.md#insn-00727db4)
- 新版 `00727d48`（命令位置の公開資料なし） · `00727da4`（命令位置の公開資料なし） · `00727df4`（命令位置の公開資料なし）

~~~diff
- 00727d08 ["INT_ADD", "register:40f0:8", ["const:727d08:8", "const:4:8"]]
- 00727d08 ["CALL", null, ["callee:008514f8:8"]]
+ 00727d48 ["INT_ADD", "register:40f0:8", ["const:727d48:8", "const:4:8"]]
+ 00727d48 ["CALL", null, ["callee:008514f8:8"]]
- 00727d08 bytes eca50494
+ 00727d48 bytes eca50494
- 00727d64 ["INT_ADD", "register:40f0:8", ["const:727d64:8", "const:4:8"]]
- 00727d64 ["CALL", null, ["callee:008514f8:8"]]
+ 00727da4 ["INT_ADD", "register:40f0:8", ["const:727da4:8", "const:4:8"]]
+ 00727da4 ["CALL", null, ["callee:008514f8:8"]]
- 00727d64 bytes d5a50494
+ 00727da4 bytes d5a50494
- 00727db4 ["INT_ADD", "register:40f0:8", ["const:727db4:8", "const:4:8"]]
- 00727db4 ["CALL", null, ["callee:008514f8:8"]]
+ 00727df4 ["INT_ADD", "register:40f0:8", ["const:727df4:8", "const:4:8"]]
+ 00727df4 ["CALL", null, ["callee:008514f8:8"]]
- 00727db4 bytes c1a50494
+ 00727df4 bytes c1a50494
~~~


<a id="compare-942b1f232d15125831016ad0df37dea5"></a>

### [`00727e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727e28.md) → [`00727e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727e68.md) FUN_00727e68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`0075b984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b984.md) [`0075e548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075e548.md) [`00788c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788c6c.md) [`0089a514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089a/0089a514.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 8件 [`0075b9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075b/0075b9c4.md) [`0075e588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075e588.md) [`00788cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/00788cac.md) [`0089a558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089a/0089a558.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00727e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727e28.md#insn-00727e54) · [`00727eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727e28.md#insn-00727eb0) · [`00727f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727e28.md#insn-00727f00)
- 新版 `00727e94`（命令位置の公開資料なし） · `00727ef0`（命令位置の公開資料なし） · `00727f40`（命令位置の公開資料なし）

~~~diff
- 00727e54 ["INT_ADD", "register:40f0:8", ["const:727e54:8", "const:4:8"]]
- 00727e54 ["CALL", null, ["callee:008514f8:8"]]
+ 00727e94 ["INT_ADD", "register:40f0:8", ["const:727e94:8", "const:4:8"]]
+ 00727e94 ["CALL", null, ["callee:008514f8:8"]]
- 00727e54 bytes 99a50494
+ 00727e94 bytes 99a50494
- 00727eb0 ["INT_ADD", "register:40f0:8", ["const:727eb0:8", "const:4:8"]]
- 00727eb0 ["CALL", null, ["callee:008514f8:8"]]
+ 00727ef0 ["INT_ADD", "register:40f0:8", ["const:727ef0:8", "const:4:8"]]
+ 00727ef0 ["CALL", null, ["callee:008514f8:8"]]
- 00727eb0 bytes 82a50494
+ 00727ef0 bytes 82a50494
- 00727f00 ["INT_ADD", "register:40f0:8", ["const:727f00:8", "const:4:8"]]
- 00727f00 ["CALL", null, ["callee:008514f8:8"]]
+ 00727f40 ["INT_ADD", "register:40f0:8", ["const:727f40:8", "const:4:8"]]
+ 00727f40 ["CALL", null, ["callee:008514f8:8"]]
- 00727f00 bytes 6ea50494
+ 00727f40 bytes 6ea50494
~~~


<a id="compare-af904aab2fb70e1b117eac27325da8ac"></a>

### [`00727f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727f74.md) → [`00727fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727fb4.md) FUN_00727fb4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`0075b984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b984.md) [`0075e548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075e548.md) [`00788c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788c6c.md) [`0089a514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089a/0089a514.md) [`00a35500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a35500.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 8件 [`0075b9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075b/0075b9c4.md) [`0075e588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075e588.md) [`00788cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/00788cac.md) [`0089a558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089a/0089a558.md) [`00a356f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a356f8.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00727fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727f74.md#insn-00727fa0) · [`00727ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727f74.md#insn-00727ffc) · [`0072804c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727f74.md#insn-0072804c)
- 新版 `00727fe0`（命令位置の公開資料なし） · `0072803c`（命令位置の公開資料なし） · `0072808c`（命令位置の公開資料なし）

~~~diff
- 00727fa0 ["INT_ADD", "register:40f0:8", ["const:727fa0:8", "const:4:8"]]
- 00727fa0 ["CALL", null, ["callee:008514f8:8"]]
+ 00727fe0 ["INT_ADD", "register:40f0:8", ["const:727fe0:8", "const:4:8"]]
+ 00727fe0 ["CALL", null, ["callee:008514f8:8"]]
- 00727fa0 bytes 46a50494
+ 00727fe0 bytes 46a50494
- 00727ffc ["INT_ADD", "register:40f0:8", ["const:727ffc:8", "const:4:8"]]
- 00727ffc ["CALL", null, ["callee:008514f8:8"]]
+ 0072803c ["INT_ADD", "register:40f0:8", ["const:72803c:8", "const:4:8"]]
+ 0072803c ["CALL", null, ["callee:008514f8:8"]]
- 00727ffc bytes 2fa50494
+ 0072803c bytes 2fa50494
- 0072804c ["INT_ADD", "register:40f0:8", ["const:72804c:8", "const:4:8"]]
- 0072804c ["CALL", null, ["callee:008514f8:8"]]
+ 0072808c ["INT_ADD", "register:40f0:8", ["const:72808c:8", "const:4:8"]]
+ 0072808c ["CALL", null, ["callee:008514f8:8"]]
- 0072804c bytes 1ba50494
+ 0072808c bytes 1ba50494
~~~


<a id="compare-e464f9640b3e308b09c5a377a61fdee3"></a>

### [`00728e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728e90.md) → [`00728ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00728/00728ed0.md) FUN_00728ed0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00728e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728e08.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`00728e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00728/00728e48.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00728ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728e90.md#insn-00728ec0) · [`00728edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728e90.md#insn-00728edc) · [`00728ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728e90.md#insn-00728ef8)
- 新版 `00728f00`（命令位置の公開資料なし） · `00728f1c`（命令位置の公開資料なし） · `00728f38`（命令位置の公開資料なし）

~~~diff
- 00728ec0 ["INT_ADD", "register:40f0:8", ["const:728ec0:8", "const:4:8"]]
- 00728ec0 ["CALL", null, ["callee:008514f8:8"]]
+ 00728f00 ["INT_ADD", "register:40f0:8", ["const:728f00:8", "const:4:8"]]
+ 00728f00 ["CALL", null, ["callee:008514f8:8"]]
- 00728ec0 bytes 7ea10494
+ 00728f00 bytes 7ea10494
- 00728edc ["INT_ADD", "register:40f0:8", ["const:728edc:8", "const:4:8"]]
- 00728edc ["CALL", null, ["callee:008514f8:8"]]
+ 00728f1c ["INT_ADD", "register:40f0:8", ["const:728f1c:8", "const:4:8"]]
+ 00728f1c ["CALL", null, ["callee:008514f8:8"]]
- 00728edc bytes 77a10494
+ 00728f1c bytes 77a10494
- 00728ef8 ["INT_ADD", "register:40f0:8", ["const:728ef8:8", "const:4:8"]]
- 00728ef8 ["CALL", null, ["callee:008514f8:8"]]
+ 00728f38 ["INT_ADD", "register:40f0:8", ["const:728f38:8", "const:4:8"]]
+ 00728f38 ["CALL", null, ["callee:008514f8:8"]]
- 00728ef8 bytes 70a10494
+ 00728f38 bytes 70a10494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f39447e8f8390999f980de7f1cdbaf3b"></a>

### [`00729934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/00729934.md) → [`00729974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00729/00729974.md) FUN_00729974

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`007290c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/007290c8.md) [`00752f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00752/00752f64.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) [`009afd0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009af/009afd0c.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0072c340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c340.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 4件 [`00729108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00729/00729108.md) [`00752fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00752/00752fa4.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) [`009afea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009af/009afea8.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0072c380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c380.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00729990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/00729934.md#insn-00729990) · [`007299a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/00729934.md#insn-007299a0) · [`007299d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/00729934.md#insn-007299d0)
- 新版 `007299d0`（命令位置の公開資料なし） · `007299e0`（命令位置の公開資料なし） · `00729a10`（命令位置の公開資料なし）

~~~diff
- 00729990 ["INT_ADD", "register:40f0:8", ["const:729990:8", "const:4:8"]]
- 00729990 ["CALL", null, ["callee:0043bb20:8"]]
+ 007299d0 ["INT_ADD", "register:40f0:8", ["const:7299d0:8", "const:4:8"]]
+ 007299d0 ["CALL", null, ["callee:0043bb20:8"]]
- 00729990 bytes 5448f497
+ 007299d0 bytes 5448f497
- 007299a0 ["INT_ADD", "register:40f0:8", ["const:7299a0:8", "const:4:8"]]
- 007299a0 ["CALL", null, ["callee:0043bb20:8"]]
+ 007299e0 ["INT_ADD", "register:40f0:8", ["const:7299e0:8", "const:4:8"]]
+ 007299e0 ["CALL", null, ["callee:0043bb20:8"]]
- 007299a0 bytes 5048f497
+ 007299e0 bytes 5048f497
- 007299d0 ["INT_ADD", "register:40f0:8", ["const:7299d0:8", "const:4:8"]]
- 007299d0 ["CALL", null, ["callee:0072c380:8"]]
+ 00729a10 ["INT_ADD", "register:40f0:8", ["const:729a10:8", "const:4:8"]]
+ 00729a10 ["CALL", null, ["callee:0072c380:8"]]
- 007299d0 bytes 5c0a0094
+ 00729a10 bytes 5c0a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b77ea5704a2b93a094cd7105cf1ad1e2"></a>

### [`0072bc78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072bc78.md) → [`0072bcb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072b/0072bcb8.md) FUN_0072bcb8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0061037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00610/0061037c.md) [`00624768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00624/00624768.md) · 呼出先 4件 [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0072b264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072b264.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) [`006247a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/006247a8.md) · 呼出先 4件 [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0072b2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072b/0072b2a4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072bc98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072bc78.md#insn-0072bc98) · [`0072bcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072bc78.md#insn-0072bcb4) · [`0072bcd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072bc78.md#insn-0072bcd8)
- 新版 `0072bcd8`（命令位置の公開資料なし） · `0072bcf4`（命令位置の公開資料なし） · `0072bd18`（命令位置の公開資料なし）

~~~diff
- 0072bc98 ["INT_ADD", "register:40f0:8", ["const:72bc98:8", "const:4:8"]]
- 0072bc98 ["CALL", null, ["callee:0072b2a4:8"]]
+ 0072bcd8 ["INT_ADD", "register:40f0:8", ["const:72bcd8:8", "const:4:8"]]
+ 0072bcd8 ["CALL", null, ["callee:0072b2a4:8"]]
- 0072bc98 bytes 73fdff97
+ 0072bcd8 bytes 73fdff97
- 0072bcb4 ["INT_ADD", "register:40f0:8", ["const:72bcb4:8", "const:4:8"]]
- 0072bcb4 ["CALL", null, ["callee:0046d7b0:8"]]
+ 0072bcf4 ["INT_ADD", "register:40f0:8", ["const:72bcf4:8", "const:4:8"]]
+ 0072bcf4 ["CALL", null, ["callee:0046d7b0:8"]]
- 0072bcb4 bytes af06f597
+ 0072bcf4 bytes af06f597
- 0072bcd8 ["INT_ADD", "register:40f0:8", ["const:72bcd8:8", "const:4:8"]]
- 0072bcd8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0072bd18 ["INT_ADD", "register:40f0:8", ["const:72bd18:8", "const:4:8"]]
+ 0072bd18 ["CALL", null, ["callee:00c57eb0:8"]]
- 0072bcd8 bytes 76af1494
+ 0072bd18 bytes 66b01494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad5e54e4062d035d4e2da70a35c36ff8"></a>

### [`0072c29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c29c.md) → [`0072c2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c2dc.md) FUN_0072c2dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0074fba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074f/0074fba0.md) [`00750d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00750/00750d08.md) [`0077b2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077b2cc.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) [`009a1464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a1/009a1464.md) · 呼出先 4件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046a2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a2cc.md)
- 新版 呼出元 5件 [`0074fbe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074f/0074fbe0.md) [`00750d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00750/00750d48.md) [`0077b30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077b/0077b30c.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`009a1600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a1/009a1600.md) · 呼出先 4件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046a30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a30c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072c2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c29c.md#insn-0072c2b0) · [`0072c2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c29c.md#insn-0072c2d4) · [`0072c318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c29c.md#insn-0072c318)
- 新版 `0072c2f0`（命令位置の公開資料なし） · `0072c314`（命令位置の公開資料なし） · `0072c358`（命令位置の公開資料なし）

~~~diff
- 0072c2b0 ["INT_ADD", "register:40f0:8", ["const:72c2b0:8", "const:4:8"]]
- 0072c2b0 ["CALL", null, ["callee:00467860:8"]]
+ 0072c2f0 ["INT_ADD", "register:40f0:8", ["const:72c2f0:8", "const:4:8"]]
+ 0072c2f0 ["CALL", null, ["callee:00467860:8"]]
- 0072c2b0 bytes 5cedf497
+ 0072c2f0 bytes 5cedf497
- 0072c2d4 ["INT_ADD", "register:40f0:8", ["const:72c2d4:8", "const:4:8"]]
- 0072c2d4 ["CALL", null, ["callee:0046a30c:8"]]
+ 0072c314 ["INT_ADD", "register:40f0:8", ["const:72c314:8", "const:4:8"]]
+ 0072c314 ["CALL", null, ["callee:0046a30c:8"]]
- 0072c2d4 bytes fef7f497
+ 0072c314 bytes fef7f497
- 0072c318 ["INT_ADD", "register:40f0:8", ["const:72c318:8", "const:4:8"]]
- 0072c318 ["CALL", null, ["callee:00469c04:8"]]
+ 0072c358 ["INT_ADD", "register:40f0:8", ["const:72c358:8", "const:4:8"]]
+ 0072c358 ["CALL", null, ["callee:00469c04:8"]]
- 0072c318 bytes 2bf6f497
+ 0072c358 bytes 2bf6f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-799661980f8ea4c3e79bcd82e470badc"></a>

### [`0072c340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c340.md) → [`0072c380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c380.md) FUN_0072c380

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00729934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/00729934.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0061aeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061aeb8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00729974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00729/00729974.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0061aef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061aef8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072c39c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c340.md#insn-0072c39c) · [`0072c3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c340.md#insn-0072c3ac) · [`0072c3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c340.md#insn-0072c3e0)
- 新版 `0072c3dc`（命令位置の公開資料なし） · `0072c3ec`（命令位置の公開資料なし） · `0072c420`（命令位置の公開資料なし）

~~~diff
- 0072c39c ["INT_ADD", "register:40f0:8", ["const:72c39c:8", "const:4:8"]]
- 0072c39c ["CALL", null, ["callee:0043bb20:8"]]
+ 0072c3dc ["INT_ADD", "register:40f0:8", ["const:72c3dc:8", "const:4:8"]]
+ 0072c3dc ["CALL", null, ["callee:0043bb20:8"]]
- 0072c39c bytes d13df497
+ 0072c3dc bytes d13df497
- 0072c3ac ["INT_ADD", "register:40f0:8", ["const:72c3ac:8", "const:4:8"]]
- 0072c3ac ["CALL", null, ["callee:0043bb20:8"]]
+ 0072c3ec ["INT_ADD", "register:40f0:8", ["const:72c3ec:8", "const:4:8"]]
+ 0072c3ec ["CALL", null, ["callee:0043bb20:8"]]
- 0072c3ac bytes cd3df497
+ 0072c3ec bytes cd3df497
- 0072c3e0 ["INT_ADD", "register:40f0:8", ["const:72c3e0:8", "const:4:8"]]
- 0072c3e0 ["CALL", null, ["callee:0061aef8:8"]]
+ 0072c420 ["INT_ADD", "register:40f0:8", ["const:72c420:8", "const:4:8"]]
+ 0072c420 ["CALL", null, ["callee:0061aef8:8"]]
- 0072c3e0 bytes b6bafb97
+ 0072c420 bytes b6bafb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f8bfbd1d8165a80b8fe0c8383965f65"></a>

### [`0072c80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c80c.md) → [`0072c84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c84c.md) FUN_0072c84c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 4件 [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`008005ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008005ec.md) [`00805bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00805/00805bb4.md) [`00805cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00805/00805cf4.md)
- 新版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 4件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`0080062c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/0080062c.md) [`00805bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/00805bf4.md) [`00805d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/00805d34.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072c82c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c80c.md#insn-0072c82c) · [`0072c838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c80c.md#insn-0072c838) · [`0072c848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c80c.md#insn-0072c848)
- 新版 `0072c86c`（命令位置の公開資料なし） · `0072c878`（命令位置の公開資料なし） · `0072c888`（命令位置の公開資料なし）

~~~diff
- 0072c82c ["INT_ADD", "register:40f0:8", ["const:72c82c:8", "const:4:8"]]
- 0072c82c ["CALL", null, ["callee:0048ce84:8"]]
+ 0072c86c ["INT_ADD", "register:40f0:8", ["const:72c86c:8", "const:4:8"]]
+ 0072c86c ["CALL", null, ["callee:0048ce84:8"]]
- 0072c82c bytes 8681f597
+ 0072c86c bytes 8681f597
- 0072c838 ["INT_ADD", "register:40f0:8", ["const:72c838:8", "const:4:8"]]
- 0072c838 ["CALL", null, ["callee:0080062c:8"]]
+ 0072c878 ["INT_ADD", "register:40f0:8", ["const:72c878:8", "const:4:8"]]
+ 0072c878 ["CALL", null, ["callee:0080062c:8"]]
- 0072c838 bytes 6d4f0394
+ 0072c878 bytes 6d4f0394
- 0072c848 ["INT_ADD", "register:40f0:8", ["const:72c848:8", "const:4:8"]]
- 0072c848 ["CALL", null, ["callee:00805d34:8"]]
+ 0072c888 ["INT_ADD", "register:40f0:8", ["const:72c888:8", "const:4:8"]]
+ 0072c888 ["CALL", null, ["callee:00805d34:8"]]
- 0072c848 bytes 2b650394
+ 0072c888 bytes 2b650394
~~~


<a id="compare-dfdcd66cda70e818ef5b9757edebe641"></a>

### [`0072c86c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c86c.md) → [`0072c8ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c8ac.md) FUN_0072c8ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 2件 [`00731ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731ab8.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 2件 [`00731af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731af8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072c884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c86c.md#insn-0072c884) · [`0072c8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c86c.md#insn-0072c8d0)
- 新版 `0072c8c4`（命令位置の公開資料なし） · `0072c910`（命令位置の公開資料なし）

~~~diff
- 0072c884 ["INT_ADD", "register:40f0:8", ["const:72c884:8", "const:4:8"]]
- 0072c884 ["CALL", null, ["callee:008514f8:8"]]
+ 0072c8c4 ["INT_ADD", "register:40f0:8", ["const:72c8c4:8", "const:4:8"]]
+ 0072c8c4 ["CALL", null, ["callee:008514f8:8"]]
- 0072c884 bytes 0d930494
+ 0072c8c4 bytes 0d930494
- 0072c8d0 ["INT_ADD", "register:40f0:8", ["const:72c8d0:8", "const:4:8"]]
- 0072c8d0 ["CALL", null, ["callee:00731af8:8"]]
+ 0072c910 ["INT_ADD", "register:40f0:8", ["const:72c910:8", "const:4:8"]]
+ 0072c910 ["CALL", null, ["callee:00731af8:8"]]
- 0072c8d0 bytes 7a140094
+ 0072c910 bytes 7a140094
~~~


<a id="compare-c04faa70ada04f555fb1f2475053058a"></a>

### [`0072c8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c8d4.md) → [`0072c914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c914.md) FUN_0072c914

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 1件 [`00731ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731ab8.md)
- 新版 呼出元 2件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) · 呼出先 1件 [`00731af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731af8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072c8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c8d4.md#insn-0072c8f8)
- 新版 `0072c938`（命令位置の公開資料なし）

~~~diff
- 0072c8f8 ["INT_ADD", "register:40f0:8", ["const:72c8f8:8", "const:4:8"]]
- 0072c8f8 ["CALL", null, ["callee:00731af8:8"]]
+ 0072c938 ["INT_ADD", "register:40f0:8", ["const:72c938:8", "const:4:8"]]
+ 0072c938 ["CALL", null, ["callee:00731af8:8"]]
- 0072c8f8 bytes 70140094
+ 0072c938 bytes 70140094
~~~


<a id="compare-2a3d90096ca8037819e536c45c90b5c6"></a>

### [`0072c8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c8fc.md) → [`0072c93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c93c.md) FUN_0072c93c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00805cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00805/00805cf4.md) · 呼出先 3件 [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`008001ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008001ac.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00805d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/00805d34.md) · 呼出先 3件 [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`008001ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001ec.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072c914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c8fc.md#insn-0072c914) · [`0072c928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c8fc.md#insn-0072c928) · [`0072c970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c8fc.md#insn-0072c970)
- 新版 `0072c954`（命令位置の公開資料なし） · `0072c968`（命令位置の公開資料なし） · `0072c9b0`（命令位置の公開資料なし）

~~~diff
- 0072c914 ["INT_ADD", "register:40f0:8", ["const:72c914:8", "const:4:8"]]
- 0072c914 ["CALL", null, ["callee:008514f8:8"]]
+ 0072c954 ["INT_ADD", "register:40f0:8", ["const:72c954:8", "const:4:8"]]
+ 0072c954 ["CALL", null, ["callee:008514f8:8"]]
- 0072c914 bytes e9920494
+ 0072c954 bytes e9920494
- 0072c928 ["INT_ADD", "register:40f0:8", ["const:72c928:8", "const:4:8"]]
- 0072c928 ["CALL", null, ["callee:008001ec:8"]]
+ 0072c968 ["INT_ADD", "register:40f0:8", ["const:72c968:8", "const:4:8"]]
+ 0072c968 ["CALL", null, ["callee:008001ec:8"]]
- 0072c928 bytes 214e0394
+ 0072c968 bytes 214e0394
- 0072c970 ["INT_ADD", "register:40f0:8", ["const:72c970:8", "const:4:8"]]
- 0072c970 ["CALL", null, ["callee:0049f3f0:8"]]
+ 0072c9b0 ["INT_ADD", "register:40f0:8", ["const:72c9b0:8", "const:4:8"]]
+ 0072c9b0 ["CALL", null, ["callee:0049f3f0:8"]]
- 0072c970 bytes 90caf597
+ 0072c9b0 bytes 90caf597
~~~


<a id="compare-5a3ec64bfc3c482b97486bc16a85bcec"></a>

### [`0072eb98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072eb98.md) → [`0072ebd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072e/0072ebd8.md) FUN_0072ebd8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072ebbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072eb98.md#insn-0072ebbc) · [`0072ebcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072eb98.md#insn-0072ebcc)
- 新版 `0072ebfc`（命令位置の公開資料なし） · `0072ec0c`（命令位置の公開資料なし）

~~~diff
- 0072ebbc ["INT_ADD", "register:40f0:8", ["const:72ebbc:8", "const:4:8"]]
- 0072ebbc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0072ebfc ["INT_ADD", "register:40f0:8", ["const:72ebfc:8", "const:4:8"]]
+ 0072ebfc ["CALL", null, ["callee:00c57eb0:8"]]
- 0072ebbc bytes bda31494
+ 0072ebfc bytes ada41494
- 0072ebcc ["INT_ADD", "register:40f0:8", ["const:72ebcc:8", "const:4:8"]]
- 0072ebcc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0072ec0c ["INT_ADD", "register:40f0:8", ["const:72ec0c:8", "const:4:8"]]
+ 0072ec0c ["CALL", null, ["callee:00c57eb0:8"]]
- 0072ebcc bytes b9a31494
+ 0072ec0c bytes a9a41494
~~~


<a id="compare-2bff16133eb88abe397af7d62c9d3f39"></a>

### [`0072ebec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ebec.md) → [`0072ec2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072e/0072ec2c.md) FUN_0072ec2c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072ec10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ebec.md#insn-0072ec10) · [`0072ec20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ebec.md#insn-0072ec20)
- 新版 `0072ec50`（命令位置の公開資料なし） · `0072ec60`（命令位置の公開資料なし）

~~~diff
- 0072ec10 ["INT_ADD", "register:40f0:8", ["const:72ec10:8", "const:4:8"]]
- 0072ec10 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0072ec50 ["INT_ADD", "register:40f0:8", ["const:72ec50:8", "const:4:8"]]
+ 0072ec50 ["CALL", null, ["callee:00c57eb0:8"]]
- 0072ec10 bytes a8a31494
+ 0072ec50 bytes 98a41494
- 0072ec20 ["INT_ADD", "register:40f0:8", ["const:72ec20:8", "const:4:8"]]
- 0072ec20 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0072ec60 ["INT_ADD", "register:40f0:8", ["const:72ec60:8", "const:4:8"]]
+ 0072ec60 ["CALL", null, ["callee:00c57eb0:8"]]
- 0072ec20 bytes a4a31494
+ 0072ec60 bytes 94a41494
~~~


<a id="compare-e8d6d9e5e491327f27f44c824d3f1c3a"></a>

### [`0072ec40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ec40.md) → [`0072ec80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072e/0072ec80.md) FUN_0072ec80

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072ec64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ec40.md#insn-0072ec64) · [`0072ec74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ec40.md#insn-0072ec74)
- 新版 `0072eca4`（命令位置の公開資料なし） · `0072ecb4`（命令位置の公開資料なし）

~~~diff
- 0072ec64 ["INT_ADD", "register:40f0:8", ["const:72ec64:8", "const:4:8"]]
- 0072ec64 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0072eca4 ["INT_ADD", "register:40f0:8", ["const:72eca4:8", "const:4:8"]]
+ 0072eca4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0072ec64 bytes 93a31494
+ 0072eca4 bytes 83a41494
- 0072ec74 ["INT_ADD", "register:40f0:8", ["const:72ec74:8", "const:4:8"]]
- 0072ec74 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0072ecb4 ["INT_ADD", "register:40f0:8", ["const:72ecb4:8", "const:4:8"]]
+ 0072ecb4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0072ec74 bytes 8fa31494
+ 0072ecb4 bytes 7fa41494
~~~


<a id="compare-155939780dafdf85626fe5713382e740"></a>

### [`0072ec94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ec94.md) → [`0072ecd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072e/0072ecd4.md) FUN_0072ecd4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072ecb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ec94.md#insn-0072ecb8) · [`0072ecc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ec94.md#insn-0072ecc8)
- 新版 `0072ecf8`（命令位置の公開資料なし） · `0072ed08`（命令位置の公開資料なし）

~~~diff
- 0072ecb8 ["INT_ADD", "register:40f0:8", ["const:72ecb8:8", "const:4:8"]]
- 0072ecb8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0072ecf8 ["INT_ADD", "register:40f0:8", ["const:72ecf8:8", "const:4:8"]]
+ 0072ecf8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0072ecb8 bytes 7ea31494
+ 0072ecf8 bytes 6ea41494
- 0072ecc8 ["INT_ADD", "register:40f0:8", ["const:72ecc8:8", "const:4:8"]]
- 0072ecc8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0072ed08 ["INT_ADD", "register:40f0:8", ["const:72ed08:8", "const:4:8"]]
+ 0072ed08 ["CALL", null, ["callee:00c57eb0:8"]]
- 0072ecc8 bytes 7aa31494
+ 0072ed08 bytes 6aa41494
~~~


<a id="compare-6f08aca1b0303c841735fb8391b69525"></a>

### [`0072ece8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ece8.md) → [`0072ed28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072e/0072ed28.md) FUN_0072ed28

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 9件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004800d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004800d8.md) [`004802b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md) [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md) [`00480704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md)
- 新版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 9件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00480118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480118.md) [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md) [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md) [`00480744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072ed18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ece8.md#insn-0072ed18) · [`0072ed24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ece8.md#insn-0072ed24) · [`0072ed30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ece8.md#insn-0072ed30)
- 新版 `0072ed58`（命令位置の公開資料なし） · `0072ed64`（命令位置の公開資料なし） · `0072ed70`（命令位置の公開資料なし）

~~~diff
- 0072ed18 ["INT_ADD", "register:40f0:8", ["const:72ed18:8", "const:4:8"]]
- 0072ed18 ["CALL", null, ["callee:004803f0:8"]]
+ 0072ed58 ["INT_ADD", "register:40f0:8", ["const:72ed58:8", "const:4:8"]]
+ 0072ed58 ["CALL", null, ["callee:004803f0:8"]]
- 0072ed18 bytes a645f597
+ 0072ed58 bytes a645f597
- 0072ed24 ["INT_ADD", "register:40f0:8", ["const:72ed24:8", "const:4:8"]]
- 0072ed24 ["CALL", null, ["callee:004803f0:8"]]
+ 0072ed64 ["INT_ADD", "register:40f0:8", ["const:72ed64:8", "const:4:8"]]
+ 0072ed64 ["CALL", null, ["callee:004803f0:8"]]
- 0072ed24 bytes a345f597
+ 0072ed64 bytes a345f597
- 0072ed30 ["INT_ADD", "register:40f0:8", ["const:72ed30:8", "const:4:8"]]
- 0072ed30 ["CALL", null, ["callee:00480118:8"]]
+ 0072ed70 ["INT_ADD", "register:40f0:8", ["const:72ed70:8", "const:4:8"]]
+ 0072ed70 ["CALL", null, ["callee:00480118:8"]]
- 0072ed30 bytes ea44f597
+ 0072ed70 bytes ea44f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c97b53b784288b6a3f70dbd9edaa3b1a"></a>

### [`0072ef2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ef2c.md) → [`0072ef6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072e/0072ef6c.md) FUN_0072ef6c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 4件 [`00480cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480cb0.md) [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md) [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md) [`00481058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481058.md)
- 新版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 4件 [`00480cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480cf0.md) [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md) [`00481098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481098.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072ef50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ef2c.md#insn-0072ef50) · [`0072ef5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ef2c.md#insn-0072ef5c) · [`0072ef68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ef2c.md#insn-0072ef68)
- 新版 `0072ef90`（命令位置の公開資料なし） · `0072ef9c`（命令位置の公開資料なし） · `0072efa8`（命令位置の公開資料なし）

~~~diff
- 0072ef50 ["INT_ADD", "register:40f0:8", ["const:72ef50:8", "const:4:8"]]
- 0072ef50 ["CALL", null, ["callee:00480e28:8"]]
+ 0072ef90 ["INT_ADD", "register:40f0:8", ["const:72ef90:8", "const:4:8"]]
+ 0072ef90 ["CALL", null, ["callee:00480e28:8"]]
- 0072ef50 bytes a647f597
+ 0072ef90 bytes a647f597
- 0072ef5c ["INT_ADD", "register:40f0:8", ["const:72ef5c:8", "const:4:8"]]
- 0072ef5c ["CALL", null, ["callee:00480e28:8"]]
+ 0072ef9c ["INT_ADD", "register:40f0:8", ["const:72ef9c:8", "const:4:8"]]
+ 0072ef9c ["CALL", null, ["callee:00480e28:8"]]
- 0072ef5c bytes a347f597
+ 0072ef9c bytes a347f597
- 0072ef68 ["INT_ADD", "register:40f0:8", ["const:72ef68:8", "const:4:8"]]
- 0072ef68 ["CALL", null, ["callee:00480cf0:8"]]
+ 0072efa8 ["INT_ADD", "register:40f0:8", ["const:72efa8:8", "const:4:8"]]
+ 0072efa8 ["CALL", null, ["callee:00480cf0:8"]]
- 0072ef68 bytes 5247f597
+ 0072efa8 bytes 5247f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e53e592f8511e0488b5f0c228cf4b17"></a>

### [`0072f050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072f/0072f050.md) → [`0072f090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072f/0072f090.md) FUN_0072f090

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) · 呼出先 3件 [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00abd09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd09c.md)
- 新版 呼出元 1件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) · 呼出先 3件 [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00abd298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abd/00abd298.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072f088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072f/0072f050.md#insn-0072f088) · [`0072f0a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072f/0072f050.md#insn-0072f0a4) · [`0072f0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072f/0072f050.md#insn-0072f0fc)
- 新版 `0072f0c8`（命令位置の公開資料なし） · `0072f0e4`（命令位置の公開資料なし） · `0072f13c`（命令位置の公開資料なし）

~~~diff
- 0072f088 ["INT_ADD", "register:40f0:8", ["const:72f088:8", "const:4:8"]]
- 0072f088 ["CALL", null, ["callee:008514f8:8"]]
+ 0072f0c8 ["INT_ADD", "register:40f0:8", ["const:72f0c8:8", "const:4:8"]]
+ 0072f0c8 ["CALL", null, ["callee:008514f8:8"]]
- 0072f088 bytes 0c890494
+ 0072f0c8 bytes 0c890494
- 0072f0a4 ["INT_ADD", "register:40f0:8", ["const:72f0a4:8", "const:4:8"]]
- 0072f0a4 ["CALL", null, ["callee:00abd298:8"]]
+ 0072f0e4 ["INT_ADD", "register:40f0:8", ["const:72f0e4:8", "const:4:8"]]
+ 0072f0e4 ["CALL", null, ["callee:00abd298:8"]]
- 0072f0a4 bytes fe370e94
+ 0072f0e4 bytes 6d380e94
- 0072f0fc ["INT_ADD", "register:40f0:8", ["const:72f0fc:8", "const:4:8"]]
- 0072f0fc ["CALL", null, ["callee:0049f3f0:8"]]
+ 0072f13c ["INT_ADD", "register:40f0:8", ["const:72f13c:8", "const:4:8"]]
+ 0072f13c ["CALL", null, ["callee:0049f3f0:8"]]
- 0072f0fc bytes adc0f597
+ 0072f13c bytes adc0f597
~~~


<a id="compare-f86d8b9b3733824814d5ae2a75010699"></a>

### [`0072f100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072f/0072f100.md) → [`0072f140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072f/0072f140.md) FUN_0072f140

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`0089a514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089a/0089a514.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) [`00b3e3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3e/00b3e3ac.md) · 呼出先 3件 [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00abd09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd09c.md)
- 新版 呼出元 4件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`0089a558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089a/0089a558.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) [`00b3e7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3e/00b3e7d4.md) · 呼出先 3件 [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00abd298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abd/00abd298.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0072f134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072f/0072f100.md#insn-0072f134) · [`0072f150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072f/0072f100.md#insn-0072f150) · [`0072f194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072f/0072f100.md#insn-0072f194)
- 新版 `0072f174`（命令位置の公開資料なし） · `0072f190`（命令位置の公開資料なし） · `0072f1d4`（命令位置の公開資料なし）

~~~diff
- 0072f134 ["INT_ADD", "register:40f0:8", ["const:72f134:8", "const:4:8"]]
- 0072f134 ["CALL", null, ["callee:008514f8:8"]]
+ 0072f174 ["INT_ADD", "register:40f0:8", ["const:72f174:8", "const:4:8"]]
+ 0072f174 ["CALL", null, ["callee:008514f8:8"]]
- 0072f134 bytes e1880494
+ 0072f174 bytes e1880494
- 0072f150 ["INT_ADD", "register:40f0:8", ["const:72f150:8", "const:4:8"]]
- 0072f150 ["CALL", null, ["callee:00abd298:8"]]
+ 0072f190 ["INT_ADD", "register:40f0:8", ["const:72f190:8", "const:4:8"]]
+ 0072f190 ["CALL", null, ["callee:00abd298:8"]]
- 0072f150 bytes d3370e94
+ 0072f190 bytes 42380e94
- 0072f194 ["INT_ADD", "register:40f0:8", ["const:72f194:8", "const:4:8"]]
- 0072f194 ["CALL", null, ["callee:0049f3f0:8"]]
+ 0072f1d4 ["INT_ADD", "register:40f0:8", ["const:72f1d4:8", "const:4:8"]]
+ 0072f1d4 ["CALL", null, ["callee:0049f3f0:8"]]
- 0072f194 bytes 87c0f597
+ 0072f1d4 bytes 87c0f597
~~~


<a id="compare-4399a4c877cccdab66a563b46de912f5"></a>

### [`00730334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00730/00730334.md) → [`00730374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00730/00730374.md) FUN_00730374

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0072f198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072f/0072f198.md) · 呼出先 11件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`00731ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731ab8.md)
- 新版 呼出元 1件 [`0072f1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072f/0072f1d8.md) · 呼出先 11件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`00731af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731af8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00730388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00730/00730334.md#insn-00730388) · [`007303a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00730/00730334.md#insn-007303a4) · [`0073047c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00730/00730334.md#insn-0073047c)
- 新版 `007303c8`（命令位置の公開資料なし） · `007303e4`（命令位置の公開資料なし） · `007304bc`（命令位置の公開資料なし）

~~~diff
- 00730388 ["INT_ADD", "register:40f0:8", ["const:730388:8", "const:4:8"]]
- 00730388 ["CALL", null, ["callee:008514f8:8"]]
+ 007303c8 ["INT_ADD", "register:40f0:8", ["const:7303c8:8", "const:4:8"]]
+ 007303c8 ["CALL", null, ["callee:008514f8:8"]]
- 00730388 bytes 4c840494
+ 007303c8 bytes 4c840494
- 007303a4 ["INT_ADD", "register:40f0:8", ["const:7303a4:8", "const:4:8"]]
- 007303a4 ["CALL", null, ["callee:00abd298:8"]]
+ 007303e4 ["INT_ADD", "register:40f0:8", ["const:7303e4:8", "const:4:8"]]
+ 007303e4 ["CALL", null, ["callee:00abd298:8"]]
- 007303a4 bytes 3e330e94
+ 007303e4 bytes ad330e94
- 0073047c ["INT_ADD", "register:40f0:8", ["const:73047c:8", "const:4:8"]]
- 0073047c ["CALL", null, ["callee:0043bba4:8"]]
+ 007304bc ["INT_ADD", "register:40f0:8", ["const:7304bc:8", "const:4:8"]]
+ 007304bc ["CALL", null, ["callee:0043bba4:8"]]
- 0073047c bytes ba2df497
+ 007304bc bytes ba2df497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1b8f8f7e3b78f9423270441da3bc608"></a>

### [`00730cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00730/00730cbc.md) → [`00730cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00730/00730cfc.md) FUN_00730cfc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`0085d4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085d/0085d4b4.md) [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 1件 [`00731aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731aa4.md)
- 新版 呼出元 3件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`0085d4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085d/0085d4f4.md) [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 1件 [`00731ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731ae4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00730ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00730/00730cbc.md#insn-00730ce0)
- 新版 `00730d20`（命令位置の公開資料なし）

~~~diff
- 00730ce0 ["INT_ADD", "register:40f0:8", ["const:730ce0:8", "const:4:8"]]
- 00730ce0 ["CALL", null, ["callee:00731ae4:8"]]
+ 00730d20 ["INT_ADD", "register:40f0:8", ["const:730d20:8", "const:4:8"]]
+ 00730d20 ["CALL", null, ["callee:00731ae4:8"]]
- 00730ce0 bytes 71030094
+ 00730d20 bytes 71030094
~~~


<a id="compare-c690f9f083fab51a12e032ef28aa2766"></a>

### [`007312e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007312e8.md) → [`00731328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731328.md) FUN_00731328

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 4件 [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00731aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731aa4.md) [`00731ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731ab8.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 4件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00731ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731ae4.md) [`00731af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731af8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00731304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007312e8.md#insn-00731304) · [`0073134c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007312e8.md#insn-0073134c) · [`007313c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007312e8.md#insn-007313c0)
- 新版 `00731344`（命令位置の公開資料なし） · `0073138c`（命令位置の公開資料なし） · `00731400`（命令位置の公開資料なし）

~~~diff
- 00731304 ["INT_ADD", "register:40f0:8", ["const:731304:8", "const:4:8"]]
- 00731304 ["CALL", null, ["callee:0048ce84:8"]]
+ 00731344 ["INT_ADD", "register:40f0:8", ["const:731344:8", "const:4:8"]]
+ 00731344 ["CALL", null, ["callee:0048ce84:8"]]
- 00731304 bytes d06ef597
+ 00731344 bytes d06ef597
- 0073134c ["INT_ADD", "register:40f0:8", ["const:73134c:8", "const:4:8"]]
- 0073134c ["CALL", null, ["callee:008514f8:8"]]
+ 0073138c ["INT_ADD", "register:40f0:8", ["const:73138c:8", "const:4:8"]]
+ 0073138c ["CALL", null, ["callee:008514f8:8"]]
- 0073134c bytes 5b800494
+ 0073138c bytes 5b800494
- 007313c0 ["INT_ADD", "register:40f0:8", ["const:7313c0:8", "const:4:8"]]
- 007313c0 ["CALL", null, ["callee:00731af8:8"]]
+ 00731400 ["INT_ADD", "register:40f0:8", ["const:731400:8", "const:4:8"]]
+ 00731400 ["CALL", null, ["callee:00731af8:8"]]
- 007313c0 bytes be010094
+ 00731400 bytes be010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65c7ee353602fe498b642acf370c81ff"></a>

### [`007313cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007313cc.md) → [`0073140c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/0073140c.md) FUN_0073140c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b3dd10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3d/00b3dd10.md) · 呼出先 3件 [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00abd09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd09c.md)
- 新版 呼出元 1件 [`00b3e138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3e/00b3e138.md) · 呼出先 3件 [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00abd298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abd/00abd298.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00731410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007313cc.md#insn-00731410) · [`0073142c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007313cc.md#insn-0073142c) · [`0073147c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007313cc.md#insn-0073147c)
- 新版 `00731450`（命令位置の公開資料なし） · `0073146c`（命令位置の公開資料なし） · `007314bc`（命令位置の公開資料なし）

~~~diff
- 00731410 ["INT_ADD", "register:40f0:8", ["const:731410:8", "const:4:8"]]
- 00731410 ["CALL", null, ["callee:008514f8:8"]]
+ 00731450 ["INT_ADD", "register:40f0:8", ["const:731450:8", "const:4:8"]]
+ 00731450 ["CALL", null, ["callee:008514f8:8"]]
- 00731410 bytes 2a800494
+ 00731450 bytes 2a800494
- 0073142c ["INT_ADD", "register:40f0:8", ["const:73142c:8", "const:4:8"]]
- 0073142c ["CALL", null, ["callee:00abd298:8"]]
+ 0073146c ["INT_ADD", "register:40f0:8", ["const:73146c:8", "const:4:8"]]
+ 0073146c ["CALL", null, ["callee:00abd298:8"]]
- 0073142c bytes 1c2f0e94
+ 0073146c bytes 8b2f0e94
- 0073147c ["INT_ADD", "register:40f0:8", ["const:73147c:8", "const:4:8"]]
- 0073147c ["CALL", null, ["callee:008514f8:8"]]
+ 007314bc ["INT_ADD", "register:40f0:8", ["const:7314bc:8", "const:4:8"]]
+ 007314bc ["CALL", null, ["callee:008514f8:8"]]
- 0073147c bytes 0f800494
+ 007314bc bytes 0f800494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6aa94c85645cdc46be33ea1adfd915b"></a>

### [`007314e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007314e8.md) → [`00731528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731528.md) FUN_00731528

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b3d1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3d/00b3d1f0.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00abd09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd09c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00b3d618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3d/00b3d618.md) · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00abd298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abd/00abd298.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00731524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007314e8.md#insn-00731524) · [`00731540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007314e8.md#insn-00731540) · [`0073156c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007314e8.md#insn-0073156c)
- 新版 `00731564`（命令位置の公開資料なし） · `00731580`（命令位置の公開資料なし） · `007315ac`（命令位置の公開資料なし）

~~~diff
- 00731524 ["INT_ADD", "register:40f0:8", ["const:731524:8", "const:4:8"]]
- 00731524 ["CALL", null, ["callee:008514f8:8"]]
+ 00731564 ["INT_ADD", "register:40f0:8", ["const:731564:8", "const:4:8"]]
+ 00731564 ["CALL", null, ["callee:008514f8:8"]]
- 00731524 bytes e57f0494
+ 00731564 bytes e57f0494
- 00731540 ["INT_ADD", "register:40f0:8", ["const:731540:8", "const:4:8"]]
- 00731540 ["CALL", null, ["callee:00abd298:8"]]
+ 00731580 ["INT_ADD", "register:40f0:8", ["const:731580:8", "const:4:8"]]
+ 00731580 ["CALL", null, ["callee:00abd298:8"]]
- 00731540 bytes d72e0e94
+ 00731580 bytes 462f0e94
- 0073156c ["INT_ADD", "register:40f0:8", ["const:73156c:8", "const:4:8"]]
- 0073156c ["CALL", null, ["callee:008514f8:8"]]
+ 007315ac ["INT_ADD", "register:40f0:8", ["const:7315ac:8", "const:4:8"]]
+ 007315ac ["CALL", null, ["callee:008514f8:8"]]
- 0073156c bytes d37f0494
+ 007315ac bytes d37f0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-739ac894570e70a18022158def2365e8"></a>

### [`00731630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731630.md) → [`00731670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731670.md) FUN_00731670

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 3件 [`008001ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008001ac.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`008005ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008005ec.md)
- 新版 呼出元 2件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) · 呼出先 3件 [`008001ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001ec.md) [`00800378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md) [`0080062c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/0080062c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073164c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731630.md#insn-0073164c) · [`00731658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731630.md#insn-00731658) · [`0073166c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731630.md#insn-0073166c)
- 新版 `0073168c`（命令位置の公開資料なし） · `00731698`（命令位置の公開資料なし） · `007316ac`（命令位置の公開資料なし）

~~~diff
- 0073164c ["INT_ADD", "register:40f0:8", ["const:73164c:8", "const:4:8"]]
- 0073164c ["CALL", null, ["callee:00800378:8"]]
+ 0073168c ["INT_ADD", "register:40f0:8", ["const:73168c:8", "const:4:8"]]
+ 0073168c ["CALL", null, ["callee:00800378:8"]]
- 0073164c bytes 3b3b0394
+ 0073168c bytes 3b3b0394
- 00731658 ["INT_ADD", "register:40f0:8", ["const:731658:8", "const:4:8"]]
- 00731658 ["CALL", null, ["callee:0080062c:8"]]
+ 00731698 ["INT_ADD", "register:40f0:8", ["const:731698:8", "const:4:8"]]
+ 00731698 ["CALL", null, ["callee:0080062c:8"]]
- 00731658 bytes e53b0394
+ 00731698 bytes e53b0394
- 0073166c ["INT_ADD", "register:40f0:8", ["const:73166c:8", "const:4:8"]]
- 0073166c ["CALL", null, ["callee:008001ec:8"]]
+ 007316ac ["INT_ADD", "register:40f0:8", ["const:7316ac:8", "const:4:8"]]
+ 007316ac ["CALL", null, ["callee:008001ec:8"]]
- 0073166c bytes d03a0394
+ 007316ac bytes d03a0394
~~~


<a id="compare-9b392cb208f55c3607afde2a1e907d09"></a>

### [`007316f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007316f4.md) → [`00731734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731734.md) FUN_00731734

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00731758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007316f4.md#insn-00731758) · [`00731798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007316f4.md#insn-00731798)
- 新版 `00731798`（命令位置の公開資料なし） · `007317d8`（命令位置の公開資料なし）

~~~diff
- 00731758 ["INT_ADD", "register:40f0:8", ["const:731758:8", "const:4:8"]]
- 00731758 ["CALL", null, ["callee:00c57e90:8"]]
+ 00731798 ["INT_ADD", "register:40f0:8", ["const:731798:8", "const:4:8"]]
+ 00731798 ["CALL", null, ["callee:00c57e90:8"]]
- 00731758 bytes ce981494
+ 00731798 bytes be991494
- 00731798 ["INT_ADD", "register:40f0:8", ["const:731798:8", "const:4:8"]]
- 00731798 ["CALL", null, ["callee:0043bba4:8"]]
+ 007317d8 ["INT_ADD", "register:40f0:8", ["const:7317d8:8", "const:4:8"]]
+ 007317d8 ["CALL", null, ["callee:0043bba4:8"]]
- 00731798 bytes f328f497
+ 007317d8 bytes f328f497
~~~


<a id="compare-aef5d4d79b626c1c6305b6bff34542c1"></a>

### [`00731968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731968.md) → [`007319a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/007319a8.md) FUN_007319a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0072c9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c9d0.md) [`00731968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731968.md) [`00848d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848d04.md) · 呼出先 3件 [`00731968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731968.md) [`007319b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007319b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0072ca10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072ca10.md) [`007319a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/007319a8.md) [`00848d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848d44.md) · 呼出先 3件 [`007319a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/007319a8.md) [`007319f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/007319f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00731988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731968.md#insn-00731988) · [`00731994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731968.md#insn-00731994) · [`007319a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731968.md#insn-007319a0)
- 新版 `007319c8`（命令位置の公開資料なし） · `007319d4`（命令位置の公開資料なし） · `007319e0`（命令位置の公開資料なし）

~~~diff
- 00731988 ["INT_ADD", "register:40f0:8", ["const:731988:8", "const:4:8"]]
- 00731988 ["CALL", null, ["local:b0:8"]]
+ 007319c8 ["INT_ADD", "register:40f0:8", ["const:7319c8:8", "const:4:8"]]
+ 007319c8 ["CALL", null, ["local:b0:8"]]
- 00731988 bytes f8ffff97
+ 007319c8 bytes f8ffff97
- 00731994 ["INT_ADD", "register:40f0:8", ["const:731994:8", "const:4:8"]]
- 00731994 ["CALL", null, ["local:b0:8"]]
+ 007319d4 ["INT_ADD", "register:40f0:8", ["const:7319d4:8", "const:4:8"]]
+ 007319d4 ["CALL", null, ["local:b0:8"]]
- 00731994 bytes f5ffff97
+ 007319d4 bytes f5ffff97
- 007319a0 ["INT_ADD", "register:40f0:8", ["const:7319a0:8", "const:4:8"]]
- 007319a0 ["CALL", null, ["callee:007319f8:8"]]
+ 007319e0 ["INT_ADD", "register:40f0:8", ["const:7319e0:8", "const:4:8"]]
+ 007319e0 ["CALL", null, ["callee:007319f8:8"]]
- 007319a0 bytes 06000094
+ 007319e0 bytes 06000094
~~~


<a id="compare-b1d7fe555b290554b640be4869746c5b"></a>

### [`007319b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007319b8.md) → [`007319f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/007319f8.md) FUN_007319f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00731968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731968.md) [`007319b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007319b8.md) · 呼出先 2件 [`007319b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007319b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`007319a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/007319a8.md) [`007319f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/007319f8.md) · 呼出先 2件 [`007319f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/007319f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007319d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007319b8.md#insn-007319d4) · [`007319e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007319b8.md#insn-007319e0) · [`007319fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007319b8.md#insn-007319fc)
- 新版 `00731a14`（命令位置の公開資料なし） · `00731a20`（命令位置の公開資料なし） · `00731a3c`（命令位置の公開資料なし）

~~~diff
- 007319d4 ["INT_ADD", "register:40f0:8", ["const:7319d4:8", "const:4:8"]]
- 007319d4 ["CALL", null, ["local:b0:8"]]
+ 00731a14 ["INT_ADD", "register:40f0:8", ["const:731a14:8", "const:4:8"]]
+ 00731a14 ["CALL", null, ["local:b0:8"]]
- 007319d4 bytes f9ffff97
+ 00731a14 bytes f9ffff97
- 007319e0 ["INT_ADD", "register:40f0:8", ["const:7319e0:8", "const:4:8"]]
- 007319e0 ["CALL", null, ["local:b0:8"]]
+ 00731a20 ["INT_ADD", "register:40f0:8", ["const:731a20:8", "const:4:8"]]
+ 00731a20 ["CALL", null, ["local:b0:8"]]
- 007319e0 bytes f6ffff97
+ 00731a20 bytes f6ffff97
- 007319fc ["INT_ADD", "register:40f0:8", ["const:7319fc:8", "const:4:8"]]
- 007319fc ["CALL", null, ["callee:00c57eb0:8"]]
+ 00731a3c ["INT_ADD", "register:40f0:8", ["const:731a3c:8", "const:4:8"]]
+ 00731a3c ["CALL", null, ["callee:00c57eb0:8"]]
- 007319fc bytes 2d981494
+ 00731a3c bytes 1d991494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ea479105d68a699a15a6b7eaceda214"></a>

### [`00731a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731a40.md) → [`00731a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731a80.md) FUN_00731a80

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0072c9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c9d0.md) [`00731a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731a40.md) [`00848d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848d04.md) · 呼出先 2件 [`00731a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731a40.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0072ca10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072ca10.md) [`00731a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731a80.md) [`00848d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848d44.md) · 呼出先 2件 [`00731a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731a80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00731a5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731a40.md#insn-00731a5c) · [`00731a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731a40.md#insn-00731a68) · [`00731a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731a40.md#insn-00731a78)
- 新版 `00731a9c`（命令位置の公開資料なし） · `00731aa8`（命令位置の公開資料なし） · `00731ab8`（命令位置の公開資料なし）

~~~diff
- 00731a5c ["INT_ADD", "register:40f0:8", ["const:731a5c:8", "const:4:8"]]
- 00731a5c ["CALL", null, ["local:b0:8"]]
+ 00731a9c ["INT_ADD", "register:40f0:8", ["const:731a9c:8", "const:4:8"]]
+ 00731a9c ["CALL", null, ["local:b0:8"]]
- 00731a5c bytes f9ffff97
+ 00731a9c bytes f9ffff97
- 00731a68 ["INT_ADD", "register:40f0:8", ["const:731a68:8", "const:4:8"]]
- 00731a68 ["CALL", null, ["local:b0:8"]]
+ 00731aa8 ["INT_ADD", "register:40f0:8", ["const:731aa8:8", "const:4:8"]]
+ 00731aa8 ["CALL", null, ["local:b0:8"]]
- 00731a68 bytes f6ffff97
+ 00731aa8 bytes f6ffff97
- 00731a78 ["INT_ADD", "register:40f0:8", ["const:731a78:8", "const:4:8"]]
- 00731a78 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00731ab8 ["INT_ADD", "register:40f0:8", ["const:731ab8:8", "const:4:8"]]
+ 00731ab8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00731a78 bytes 0e981494
+ 00731ab8 bytes fe981494
~~~


<a id="compare-5b501a91317a2690fa08a36b1017b17b"></a>

### [`00731fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731fec.md) → [`0073202c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/0073202c.md) FUN_0073202c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00acbca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbca4.md) [`00acbce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbce0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00acbea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acbea0.md) [`00acbedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acbedc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00732018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731fec.md#insn-00732018) · [`00732024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731fec.md#insn-00732024) · [`00732030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731fec.md#insn-00732030)
- 新版 `00732058`（命令位置の公開資料なし） · `00732064`（命令位置の公開資料なし） · `00732070`（命令位置の公開資料なし）

~~~diff
- 00732018 ["INT_ADD", "register:40f0:8", ["const:732018:8", "const:4:8"]]
- 00732018 ["CALL", null, ["callee:00467b60:8"]]
+ 00732058 ["INT_ADD", "register:40f0:8", ["const:732058:8", "const:4:8"]]
+ 00732058 ["CALL", null, ["callee:00467b60:8"]]
- 00732018 bytes c2d6f497
+ 00732058 bytes c2d6f497
- 00732024 ["INT_ADD", "register:40f0:8", ["const:732024:8", "const:4:8"]]
- 00732024 ["CALL", null, ["callee:00acbea0:8"]]
+ 00732064 ["INT_ADD", "register:40f0:8", ["const:732064:8", "const:4:8"]]
+ 00732064 ["CALL", null, ["callee:00acbea0:8"]]
- 00732024 bytes 20670e94
+ 00732064 bytes 8f670e94
- 00732030 ["INT_ADD", "register:40f0:8", ["const:732030:8", "const:4:8"]]
- 00732030 ["CALL", null, ["callee:00acbedc:8"]]
+ 00732070 ["INT_ADD", "register:40f0:8", ["const:732070:8", "const:4:8"]]
+ 00732070 ["CALL", null, ["callee:00acbedc:8"]]
- 00732030 bytes 2c670e94
+ 00732070 bytes 9b670e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-feb3e275617ff75060f685eb2897a7f7"></a>

### [`007327f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/007327f4.md) → [`00732834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732834.md) FUN_00732834

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`007efc68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efc68.md) [`0089b248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089b/0089b248.md) · 呼出先 2件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00a86fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86fb8.md)
- 新版 呼出元 3件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) [`0089b28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089b28c.md) · 呼出先 2件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00a871b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a87/00a871b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007328bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/007327f4.md#insn-007328bc) · [`007328c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/007327f4.md#insn-007328c4)
- 新版 `007328fc`（命令位置の公開資料なし） · `00732904`（命令位置の公開資料なし）

~~~diff
- 007328bc ["INT_ADD", "register:40f0:8", ["const:7328bc:8", "const:4:8"]]
- 007328bc ["CALL", null, ["callee:008514f8:8"]]
+ 007328fc ["INT_ADD", "register:40f0:8", ["const:7328fc:8", "const:4:8"]]
+ 007328fc ["CALL", null, ["callee:008514f8:8"]]
- 007328bc bytes ff7a0494
+ 007328fc bytes ff7a0494
- 007328c4 ["INT_ADD", "register:40f0:8", ["const:7328c4:8", "const:4:8"]]
- 007328c4 ["CALL", null, ["callee:00a871b0:8"]]
+ 00732904 ["INT_ADD", "register:40f0:8", ["const:732904:8", "const:4:8"]]
+ 00732904 ["CALL", null, ["callee:00a871b0:8"]]
- 007328c4 bytes bd510d94
+ 00732904 bytes 2b520d94
~~~


<a id="compare-d1b0632ab888ac67d4826c7af58a2220"></a>

### [`00732904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732904.md) → [`00732944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732944.md) FUN_00732944

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 3件 [`004800d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004800d8.md) [`004802b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md) [`00480704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md)
- 新版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 3件 [`00480118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480118.md) [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md) [`00480744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073291c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732904.md#insn-0073291c) · [`0073292c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732904.md#insn-0073292c) · [`0073293c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732904.md#insn-0073293c)
- 新版 `0073295c`（命令位置の公開資料なし） · `0073296c`（命令位置の公開資料なし） · `0073297c`（命令位置の公開資料なし）

~~~diff
- 0073291c ["INT_ADD", "register:40f0:8", ["const:73291c:8", "const:4:8"]]
- 0073291c ["CALL", null, ["callee:004802f8:8"]]
+ 0073295c ["INT_ADD", "register:40f0:8", ["const:73295c:8", "const:4:8"]]
+ 0073295c ["CALL", null, ["callee:004802f8:8"]]
- 0073291c bytes 6736f597
+ 0073295c bytes 6736f597
- 0073292c ["INT_ADD", "register:40f0:8", ["const:73292c:8", "const:4:8"]]
- 0073292c ["CALL", null, ["callee:004802f8:8"]]
+ 0073296c ["INT_ADD", "register:40f0:8", ["const:73296c:8", "const:4:8"]]
+ 0073296c ["CALL", null, ["callee:004802f8:8"]]
- 0073292c bytes 6336f597
+ 0073296c bytes 6336f597
- 0073293c ["INT_ADD", "register:40f0:8", ["const:73293c:8", "const:4:8"]]
- 0073293c ["CALL", null, ["callee:00480118:8"]]
+ 0073297c ["INT_ADD", "register:40f0:8", ["const:73297c:8", "const:4:8"]]
+ 0073297c ["CALL", null, ["callee:00480118:8"]]
- 0073293c bytes e735f597
+ 0073297c bytes e735f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a3b0ddb6c95e5cb0519ba9bc968423a"></a>

### [`00732abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732abc.md) → [`00732afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732afc.md) FUN_00732afc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 3件 [`00480cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480cb0.md) [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md) [`00481058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481058.md)
- 新版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 3件 [`00480cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480cf0.md) [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) [`00481098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481098.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00732adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732abc.md#insn-00732adc) · [`00732ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732abc.md#insn-00732ae8) · [`00732af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732abc.md#insn-00732af4)
- 新版 `00732b1c`（命令位置の公開資料なし） · `00732b28`（命令位置の公開資料なし） · `00732b34`（命令位置の公開資料なし）

~~~diff
- 00732adc ["INT_ADD", "register:40f0:8", ["const:732adc:8", "const:4:8"]]
- 00732adc ["CALL", null, ["callee:00480d48:8"]]
+ 00732b1c ["INT_ADD", "register:40f0:8", ["const:732b1c:8", "const:4:8"]]
+ 00732b1c ["CALL", null, ["callee:00480d48:8"]]
- 00732adc bytes 8b38f597
+ 00732b1c bytes 8b38f597
- 00732ae8 ["INT_ADD", "register:40f0:8", ["const:732ae8:8", "const:4:8"]]
- 00732ae8 ["CALL", null, ["callee:00480d48:8"]]
+ 00732b28 ["INT_ADD", "register:40f0:8", ["const:732b28:8", "const:4:8"]]
+ 00732b28 ["CALL", null, ["callee:00480d48:8"]]
- 00732ae8 bytes 8838f597
+ 00732b28 bytes 8838f597
- 00732af4 ["INT_ADD", "register:40f0:8", ["const:732af4:8", "const:4:8"]]
- 00732af4 ["CALL", null, ["callee:00480cf0:8"]]
+ 00732b34 ["INT_ADD", "register:40f0:8", ["const:732b34:8", "const:4:8"]]
+ 00732b34 ["CALL", null, ["callee:00480cf0:8"]]
- 00732af4 bytes 6f38f597
+ 00732b34 bytes 6f38f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94268eae0e03a15ac02eee74b72dc7af"></a>

### [`007330f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/007330f4.md) → [`00733134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733134.md) FUN_00733134

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00732e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732e8c.md) [`00735b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735b4c.md) [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00734030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734030.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 4件 [`00732ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732ecc.md) [`00735b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/00735b8c.md) [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00734070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/00734070.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00733134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/007330f4.md#insn-00733134) · [`00733180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/007330f4.md#insn-00733180) · [`0073320c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/007330f4.md#insn-0073320c)
- 新版 `00733174`（命令位置の公開資料なし） · `007331c0`（命令位置の公開資料なし） · `0073324c`（命令位置の公開資料なし）

~~~diff
- 00733134 ["INT_ADD", "register:40f0:8", ["const:733134:8", "const:4:8"]]
- 00733134 ["CALL", null, ["callee:008514f8:8"]]
+ 00733174 ["INT_ADD", "register:40f0:8", ["const:733174:8", "const:4:8"]]
+ 00733174 ["CALL", null, ["callee:008514f8:8"]]
- 00733134 bytes e1780494
+ 00733174 bytes e1780494
- 00733180 ["INT_ADD", "register:40f0:8", ["const:733180:8", "const:4:8"]]
- 00733180 ["CALL", null, ["callee:00734070:8"]]
+ 007331c0 ["INT_ADD", "register:40f0:8", ["const:7331c0:8", "const:4:8"]]
+ 007331c0 ["CALL", null, ["callee:00734070:8"]]
- 00733180 bytes ac030094
+ 007331c0 bytes ac030094
- 0073320c ["INT_ADD", "register:40f0:8", ["const:73320c:8", "const:4:8"]]
- 0073320c ["CALL", null, ["callee:00c57e90:8"]]
+ 0073324c ["INT_ADD", "register:40f0:8", ["const:73324c:8", "const:4:8"]]
+ 0073324c ["CALL", null, ["callee:00c57e90:8"]]
- 0073320c bytes 21921494
+ 0073324c bytes 11931494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-074ffb36f1d9b011b299f2985f7437f5"></a>

### [`0073369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/0073369c.md) → [`007336dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/007336dc.md) FUN_007336dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00764730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764730.md) [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`0089b248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089b/0089b248.md) · 呼出先 2件 [`007336c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/007336c8.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 6件 [`00764770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764770.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`0089b28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089b28c.md) · 呼出先 2件 [`00733708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733708.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007336ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/0073369c.md#insn-007336ac)
- 新版 `007336ec`（命令位置の公開資料なし）

~~~diff
- 007336ac ["INT_ADD", "register:40f0:8", ["const:7336ac:8", "const:4:8"]]
- 007336ac ["CALL", null, ["callee:008514f8:8"]]
+ 007336ec ["INT_ADD", "register:40f0:8", ["const:7336ec:8", "const:4:8"]]
+ 007336ec ["CALL", null, ["callee:008514f8:8"]]
- 007336ac bytes 83770494
+ 007336ec bytes 83770494
~~~


<a id="compare-38f7eb153683d3fb2388af4438f50d0d"></a>

### [`007336c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/007336c8.md) → [`00733708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733708.md) FUN_00733708

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 17件 [`00732cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732cb8.md) [`0073369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/0073369c.md) [`00734388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734388.md) [`00735924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735924.md) [`00735c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735c9c.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 17件 [`00732cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732cf8.md) [`007336dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/007336dc.md) [`007343c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/007343c8.md) [`00735964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/00735964.md) [`00735cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/00735cdc.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00733794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/007336c8.md#insn-00733794) · [`007337cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/007336c8.md#insn-007337cc)
- 新版 `007337d4`（命令位置の公開資料なし） · `0073380c`（命令位置の公開資料なし）

~~~diff
- 00733794 ["INT_ADD", "register:40f0:8", ["const:733794:8", "const:4:8"]]
- 00733794 ["CALL", null, ["callee:00c57e90:8"]]
+ 007337d4 ["INT_ADD", "register:40f0:8", ["const:7337d4:8", "const:4:8"]]
+ 007337d4 ["CALL", null, ["callee:00c57e90:8"]]
- 00733794 bytes bf901494
+ 007337d4 bytes af911494
- 007337cc ["INT_ADD", "register:40f0:8", ["const:7337cc:8", "const:4:8"]]
- 007337cc ["CALL", null, ["callee:0043bba4:8"]]
+ 0073380c ["INT_ADD", "register:40f0:8", ["const:73380c:8", "const:4:8"]]
+ 0073380c ["CALL", null, ["callee:0043bba4:8"]]
- 007337cc bytes e620f497
+ 0073380c bytes e620f497
~~~


<a id="compare-71118fb6fd21ef7bdfe01305e82d10d9"></a>

### [`00733e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/00733e24.md) → [`00733e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733e64.md) FUN_00733e64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00733ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/00733ab8.md) [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00737b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/00737b24.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`00733af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733af8.md) [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00737b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00737/00737b64.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00733e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/00733e24.md#insn-00733e38) · [`00733e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/00733e24.md#insn-00733e48) · [`00733ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/00733e24.md#insn-00733ea0)
- 新版 `00733e78`（命令位置の公開資料なし） · `00733e88`（命令位置の公開資料なし） · `00733ee0`（命令位置の公開資料なし）

~~~diff
- 00733e38 ["INT_ADD", "register:40f0:8", ["const:733e38:8", "const:4:8"]]
- 00733e38 ["CALL", null, ["callee:00737b64:8"]]
+ 00733e78 ["INT_ADD", "register:40f0:8", ["const:733e78:8", "const:4:8"]]
+ 00733e78 ["CALL", null, ["callee:00737b64:8"]]
- 00733e38 bytes 3b0f0094
+ 00733e78 bytes 3b0f0094
- 00733e48 ["INT_ADD", "register:40f0:8", ["const:733e48:8", "const:4:8"]]
- 00733e48 ["CALL", null, ["callee:008514f8:8"]]
+ 00733e88 ["INT_ADD", "register:40f0:8", ["const:733e88:8", "const:4:8"]]
+ 00733e88 ["CALL", null, ["callee:008514f8:8"]]
- 00733e48 bytes 9c750494
+ 00733e88 bytes 9c750494
- 00733ea0 ["INT_ADD", "register:40f0:8", ["const:733ea0:8", "const:4:8"]]
- 00733ea0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00733ee0 ["INT_ADD", "register:40f0:8", ["const:733ee0:8", "const:4:8"]]
+ 00733ee0 ["CALL", null, ["callee:00c57e90:8"]]
- 00733ea0 bytes fc8e1494
+ 00733ee0 bytes ec8f1494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5abc77dcc6eda3888b2e06433bc94ae9"></a>

### [`0073413c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/0073413c.md) → [`0073417c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/0073417c.md) FUN_0073417c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00734030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734030.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0073a314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a314.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00734070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/00734070.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0073a354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073a354.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00734190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/0073413c.md#insn-00734190) · [`007341a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/0073413c.md#insn-007341a0) · [`007341d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/0073413c.md#insn-007341d0)
- 新版 `007341d0`（命令位置の公開資料なし） · `007341e0`（命令位置の公開資料なし） · `00734210`（命令位置の公開資料なし）

~~~diff
- 00734190 ["INT_ADD", "register:40f0:8", ["const:734190:8", "const:4:8"]]
- 00734190 ["CALL", null, ["callee:0043bb20:8"]]
+ 007341d0 ["INT_ADD", "register:40f0:8", ["const:7341d0:8", "const:4:8"]]
+ 007341d0 ["CALL", null, ["callee:0043bb20:8"]]
- 00734190 bytes 541ef497
+ 007341d0 bytes 541ef497
- 007341a0 ["INT_ADD", "register:40f0:8", ["const:7341a0:8", "const:4:8"]]
- 007341a0 ["CALL", null, ["callee:0043bb20:8"]]
+ 007341e0 ["INT_ADD", "register:40f0:8", ["const:7341e0:8", "const:4:8"]]
+ 007341e0 ["CALL", null, ["callee:0043bb20:8"]]
- 007341a0 bytes 501ef497
+ 007341e0 bytes 501ef497
- 007341d0 ["INT_ADD", "register:40f0:8", ["const:7341d0:8", "const:4:8"]]
- 007341d0 ["CALL", null, ["callee:0073a354:8"]]
+ 00734210 ["INT_ADD", "register:40f0:8", ["const:734210:8", "const:4:8"]]
+ 00734210 ["CALL", null, ["callee:0073a354:8"]]
- 007341d0 bytes 51180094
+ 00734210 bytes 51180094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3407815774239ef696544c841e40d49"></a>

### [`00734260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734260.md) → [`007342a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/007342a0.md) FUN_007342a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · 呼出先 6件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005c1bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1bb0.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`00734388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734388.md) [`0073ae08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae08.md)
- 新版 呼出元 1件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) · 呼出先 6件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005c1bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1bf0.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`007343c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/007343c8.md) [`0073ae48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073ae48.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00734280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734260.md#insn-00734280) · [`0073429c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734260.md#insn-0073429c) · [`007342b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734260.md#insn-007342b0)
- 新版 `007342c0`（命令位置の公開資料なし） · `007342dc`（命令位置の公開資料なし） · `007342f0`（命令位置の公開資料なし）

~~~diff
- 00734280 ["INT_ADD", "register:40f0:8", ["const:734280:8", "const:4:8"]]
- 00734280 ["CALL", null, ["callee:0073ae48:8"]]
+ 007342c0 ["INT_ADD", "register:40f0:8", ["const:7342c0:8", "const:4:8"]]
+ 007342c0 ["CALL", null, ["callee:0073ae48:8"]]
- 00734280 bytes e21a0094
+ 007342c0 bytes e21a0094
- 0073429c ["INT_ADD", "register:40f0:8", ["const:73429c:8", "const:4:8"]]
- 0073429c ["CALL", null, ["callee:00676a60:8"]]
+ 007342dc ["INT_ADD", "register:40f0:8", ["const:7342dc:8", "const:4:8"]]
+ 007342dc ["CALL", null, ["callee:00676a60:8"]]
- 0073429c bytes e109fd97
+ 007342dc bytes e109fd97
- 007342b0 ["INT_ADD", "register:40f0:8", ["const:7342b0:8", "const:4:8"]]
- 007342b0 ["CALL", null, ["callee:007343c8:8"]]
+ 007342f0 ["INT_ADD", "register:40f0:8", ["const:7342f0:8", "const:4:8"]]
+ 007342f0 ["CALL", null, ["callee:007343c8:8"]]
- 007342b0 bytes 36000094
+ 007342f0 bytes 36000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c575f18a1c48802109934d627782709d"></a>

### [`00735670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735670.md) → [`007356b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/007356b0.md) FUN_007356b0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00734388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734388.md) [`007366c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00736/007366c4.md) [`00736bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00736/00736bdc.md) · 呼出先 5件 [`00a359a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a359a0.md) [`00a36e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a36/00a36e6c.md) [`00a37684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37684.md) [`00a389c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a38/00a389c4.md) [`00a389e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a38/00a389e0.md)
- 新版 呼出元 3件 [`007343c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/007343c8.md) [`00736704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00736/00736704.md) [`00736c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00736/00736c1c.md) · 呼出先 5件 [`00a35b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a35b98.md) [`00a37064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37064.md) [`00a3787c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a3787c.md) [`00a38bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38bbc.md) [`00a38bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38bd8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073568c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735670.md#insn-0073568c) · [`00735690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735670.md#insn-00735690) · [`007356a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735670.md#insn-007356a8)
- 新版 `007356cc`（命令位置の公開資料なし） · `007356d0`（命令位置の公開資料なし） · `007356e8`（命令位置の公開資料なし）

~~~diff
- 0073568c ["INT_ADD", "register:40f0:8", ["const:73568c:8", "const:4:8"]]
- 0073568c ["CALL", null, ["callee:00a35b98:8"]]
+ 007356cc ["INT_ADD", "register:40f0:8", ["const:7356cc:8", "const:4:8"]]
+ 007356cc ["CALL", null, ["callee:00a35b98:8"]]
- 0073568c bytes c5000c94
+ 007356cc bytes 33010c94
- 00735690 ["INT_ADD", "register:40f0:8", ["const:735690:8", "const:4:8"]]
- 00735690 ["CALL", null, ["callee:00a38bbc:8"]]
+ 007356d0 ["INT_ADD", "register:40f0:8", ["const:7356d0:8", "const:4:8"]]
+ 007356d0 ["CALL", null, ["callee:00a38bbc:8"]]
- 00735690 bytes cd0c0c94
+ 007356d0 bytes 3b0d0c94
- 007356a8 ["INT_ADD", "register:40f0:8", ["const:7356a8:8", "const:4:8"]]
- 007356a8 ["CALL", null, ["callee:00a35b98:8"]]
+ 007356e8 ["INT_ADD", "register:40f0:8", ["const:7356e8:8", "const:4:8"]]
+ 007356e8 ["CALL", null, ["callee:00a35b98:8"]]
- 007356a8 bytes be000c94
+ 007356e8 bytes 2c010c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11edbb4ce005e935f1e9d2dc52fd9b00"></a>

### [`00735704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735704.md) → [`00735744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/00735744.md) FUN_00735744

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00734388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734388.md) [`00735c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735c9c.md) [`00739464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/00739464.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0073af08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073af08.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 3件 [`007343c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/007343c8.md) [`00735cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/00735cdc.md) [`007394a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00739/007394a4.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0073af48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073af48.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007357a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735704.md#insn-007357a8) · [`00735820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735704.md#insn-00735820) · [`00735868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735704.md#insn-00735868)
- 新版 `007357e8`（命令位置の公開資料なし） · `00735860`（命令位置の公開資料なし） · `007358a8`（命令位置の公開資料なし）

~~~diff
- 007357a8 ["INT_ADD", "register:40f0:8", ["const:7357a8:8", "const:4:8"]]
- 007357a8 ["CALL", null, ["callee:00c57e90:8"]]
+ 007357e8 ["INT_ADD", "register:40f0:8", ["const:7357e8:8", "const:4:8"]]
+ 007357e8 ["CALL", null, ["callee:00c57e90:8"]]
- 007357a8 bytes ba881494
+ 007357e8 bytes aa891494
- 00735820 ["INT_ADD", "register:40f0:8", ["const:735820:8", "const:4:8"]]
- 00735820 ["CALL", null, ["callee:00c57f40:8"]]
+ 00735860 ["INT_ADD", "register:40f0:8", ["const:735860:8", "const:4:8"]]
+ 00735860 ["CALL", null, ["callee:00c57f40:8"]]
- 00735820 bytes c8881494
+ 00735860 bytes b8891494
- 00735868 ["INT_ADD", "register:40f0:8", ["const:735868:8", "const:4:8"]]
- 00735868 ["CALL", null, ["callee:00c57e90:8"]]
+ 007358a8 ["INT_ADD", "register:40f0:8", ["const:7358a8:8", "const:4:8"]]
+ 007358a8 ["CALL", null, ["callee:00c57e90:8"]]
- 00735868 bytes 8a881494
+ 007358a8 bytes 7a891494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-730834f46970eb18832e2919d72765f3"></a>

### [`00735924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735924.md) → [`00735964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/00735964.md) FUN_00735964

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00734388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734388.md) [`00735c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735c9c.md) [`00735fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735fdc.md) · 呼出先 6件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00732e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732e8c.md) [`007336c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/007336c8.md) [`0073aef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073aef4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`007343c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/007343c8.md) [`00735cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/00735cdc.md) [`0073601c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00736/0073601c.md) · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00732ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732ecc.md) [`00733708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733708.md) [`0073af34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073af34.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00735974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735924.md#insn-00735974) · [`007359a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735924.md#insn-007359a4) · [`007359c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735924.md#insn-007359c0)
- 新版 `007359b4`（命令位置の公開資料なし） · `007359e4`（命令位置の公開資料なし） · `00735a00`（命令位置の公開資料なし）

~~~diff
- 00735974 ["INT_ADD", "register:40f0:8", ["const:735974:8", "const:4:8"]]
- 00735974 ["CALL", null, ["callee:0043bba4:8"]]
+ 007359b4 ["INT_ADD", "register:40f0:8", ["const:7359b4:8", "const:4:8"]]
+ 007359b4 ["CALL", null, ["callee:0043bba4:8"]]
- 00735974 bytes 7c18f497
+ 007359b4 bytes 7c18f497
- 007359a4 ["INT_ADD", "register:40f0:8", ["const:7359a4:8", "const:4:8"]]
- 007359a4 ["CALL", null, ["callee:00732ecc:8"]]
+ 007359e4 ["INT_ADD", "register:40f0:8", ["const:7359e4:8", "const:4:8"]]
+ 007359e4 ["CALL", null, ["callee:00732ecc:8"]]
- 007359a4 bytes 3af5ff97
+ 007359e4 bytes 3af5ff97
- 007359c0 ["INT_ADD", "register:40f0:8", ["const:7359c0:8", "const:4:8"]]
- 007359c0 ["CALL", null, ["callee:008514f8:8"]]
+ 00735a00 ["INT_ADD", "register:40f0:8", ["const:735a00:8", "const:4:8"]]
+ 00735a00 ["CALL", null, ["callee:008514f8:8"]]
- 007359c0 bytes be6e0494
+ 00735a00 bytes be6e0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-045c5b1fa8c345ed5586e5353fd62ed1"></a>

### [`00735b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735b4c.md) → [`00735b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/00735b8c.md) FUN_00735b8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00735fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735fdc.md) [`0075d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md) [`00922c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00922/00922c2c.md) [`00a8a220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8a/00a8a220.md) [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 11件 [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`007330f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/007330f4.md) [`00735c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735c9c.md) [`00a359a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a359a0.md) [`00a36e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a36/00a36e6c.md)
- 新版 呼出元 5件 [`0073601c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00736/0073601c.md) [`0075d75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075d/0075d75c.md) [`00922dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00922/00922dc8.md) [`00a8a418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8a/00a8a418.md) [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 11件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00733134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733134.md) [`00735cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/00735cdc.md) [`00a35b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a35b98.md) [`00a37064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37064.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00735b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735b4c.md#insn-00735b7c) · [`00735b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735b4c.md#insn-00735b84) · [`00735b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735b4c.md#insn-00735b88)
- 新版 `00735bbc`（命令位置の公開資料なし） · `00735bc4`（命令位置の公開資料なし） · `00735bc8`（命令位置の公開資料なし）

~~~diff
- 00735b7c ["INT_ADD", "register:40f0:8", ["const:735b7c:8", "const:4:8"]]
- 00735b7c ["CALL", null, ["callee:0048ce84:8"]]
+ 00735bbc ["INT_ADD", "register:40f0:8", ["const:735bbc:8", "const:4:8"]]
+ 00735bbc ["CALL", null, ["callee:0048ce84:8"]]
- 00735b7c bytes b25cf597
+ 00735bbc bytes b25cf597
- 00735b84 ["INT_ADD", "register:40f0:8", ["const:735b84:8", "const:4:8"]]
- 00735b84 ["CALL", null, ["callee:00a35b98:8"]]
+ 00735bc4 ["INT_ADD", "register:40f0:8", ["const:735bc4:8", "const:4:8"]]
+ 00735bc4 ["CALL", null, ["callee:00a35b98:8"]]
- 00735b84 bytes 87ff0b94
+ 00735bc4 bytes f5ff0b94
- 00735b88 ["INT_ADD", "register:40f0:8", ["const:735b88:8", "const:4:8"]]
- 00735b88 ["CALL", null, ["callee:00a38bbc:8"]]
+ 00735bc8 ["INT_ADD", "register:40f0:8", ["const:735bc8:8", "const:4:8"]]
+ 00735bc8 ["CALL", null, ["callee:00a38bbc:8"]]
- 00735b88 bytes 8f0b0c94
+ 00735bc8 bytes fd0b0c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd6349977814b5cf288363d398bb8d51"></a>

### [`00735c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735c9c.md) → [`00735cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/00735cdc.md) FUN_00735cdc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00735b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735b4c.md) · 呼出先 13件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00732cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732cb8.md) [`00732e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732e8c.md) [`007336c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/007336c8.md)
- 新版 呼出元 1件 [`00735b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/00735b8c.md) · 呼出先 13件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00732cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732cf8.md) [`00732ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732ecc.md) [`00733708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733708.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00735cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735c9c.md#insn-00735cd0) · [`00735ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735c9c.md#insn-00735ce0) · [`00735d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735c9c.md#insn-00735d24)
- 新版 `00735d10`（命令位置の公開資料なし） · `00735d20`（命令位置の公開資料なし） · `00735d64`（命令位置の公開資料なし）

~~~diff
- 00735cd0 ["INT_ADD", "register:40f0:8", ["const:735cd0:8", "const:4:8"]]
- 00735cd0 ["CALL", null, ["callee:00732cf8:8"]]
+ 00735d10 ["INT_ADD", "register:40f0:8", ["const:735d10:8", "const:4:8"]]
+ 00735d10 ["CALL", null, ["callee:00732cf8:8"]]
- 00735cd0 bytes faf3ff97
+ 00735d10 bytes faf3ff97
- 00735ce0 ["INT_ADD", "register:40f0:8", ["const:735ce0:8", "const:4:8"]]
- 00735ce0 ["CALL", null, ["callee:0048ce84:8"]]
+ 00735d20 ["INT_ADD", "register:40f0:8", ["const:735d20:8", "const:4:8"]]
+ 00735d20 ["CALL", null, ["callee:0048ce84:8"]]
- 00735ce0 bytes 595cf597
+ 00735d20 bytes 595cf597
- 00735d24 ["INT_ADD", "register:40f0:8", ["const:735d24:8", "const:4:8"]]
- 00735d24 ["CALL", null, ["callee:008514f8:8"]]
+ 00735d64 ["INT_ADD", "register:40f0:8", ["const:735d64:8", "const:4:8"]]
+ 00735d64 ["CALL", null, ["callee:008514f8:8"]]
- 00735d24 bytes e56d0494
+ 00735d64 bytes e56d0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8da31166b94f3f927876ac35249a0e99"></a>

### [`00735fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735fdc.md) → [`0073601c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00736/0073601c.md) FUN_0073601c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) [`0089b248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089b/0089b248.md) [`008d9a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9a68.md) · 呼出先 10件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00732e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732e8c.md) [`007336c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/007336c8.md) [`00734388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734388.md) [`00735924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735924.md)
- 新版 呼出元 3件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) [`0089b28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089b28c.md) [`008d9c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9c04.md) · 呼出先 10件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00732ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732ecc.md) [`00733708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733708.md) [`007343c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/007343c8.md) [`00735964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/00735964.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00736018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735fdc.md#insn-00736018) · [`00736024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735fdc.md#insn-00736024) · [`0073602c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735fdc.md#insn-0073602c)
- 新版 `00736058`（命令位置の公開資料なし） · `00736064`（命令位置の公開資料なし） · `0073606c`（命令位置の公開資料なし）

~~~diff
- 00736018 ["INT_ADD", "register:40f0:8", ["const:736018:8", "const:4:8"]]
- 00736018 ["CALL", null, ["callee:00732ecc:8"]]
+ 00736058 ["INT_ADD", "register:40f0:8", ["const:736058:8", "const:4:8"]]
+ 00736058 ["CALL", null, ["callee:00732ecc:8"]]
- 00736018 bytes 9df3ff97
+ 00736058 bytes 9df3ff97
- 00736024 ["INT_ADD", "register:40f0:8", ["const:736024:8", "const:4:8"]]
- 00736024 ["CALL", null, ["callee:007343c8:8"]]
+ 00736064 ["INT_ADD", "register:40f0:8", ["const:736064:8", "const:4:8"]]
+ 00736064 ["CALL", null, ["callee:007343c8:8"]]
- 00736024 bytes d9f8ff97
+ 00736064 bytes d9f8ff97
- 0073602c ["INT_ADD", "register:40f0:8", ["const:73602c:8", "const:4:8"]]
- 0073602c ["CALL", null, ["callee:00735b8c:8"]]
+ 0073606c ["INT_ADD", "register:40f0:8", ["const:73606c:8", "const:4:8"]]
+ 0073606c ["CALL", null, ["callee:00735b8c:8"]]
- 0073602c bytes c8feff97
+ 0073606c bytes c8feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc883c13c6b4f9a13b325978058a0a17"></a>

### [`007362ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00736/007362ac.md) → [`007362ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00736/007362ec.md) FUN_007362ec

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`00a955d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a95/00a955d0.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00727990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727990.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`00a957c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a95/00a957c8.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`007279d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007279d0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007362d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00736/007362ac.md#insn-007362d0) · [`007362d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00736/007362ac.md#insn-007362d8) · [`0073641c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00736/007362ac.md#insn-0073641c)
- 新版 `00736310`（命令位置の公開資料なし） · `00736318`（命令位置の公開資料なし） · `0073645c`（命令位置の公開資料なし）

~~~diff
- 007362d0 ["INT_ADD", "register:40f0:8", ["const:7362d0:8", "const:4:8"]]
- 007362d0 ["CALL", null, ["callee:007279d0:8"]]
+ 00736310 ["INT_ADD", "register:40f0:8", ["const:736310:8", "const:4:8"]]
+ 00736310 ["CALL", null, ["callee:007279d0:8"]]
- 007362d0 bytes b0c5ff97
+ 00736310 bytes b0c5ff97
- 007362d8 ["INT_ADD", "register:40f0:8", ["const:7362d8:8", "const:4:8"]]
- 007362d8 ["CALL", null, ["callee:0048ce84:8"]]
+ 00736318 ["INT_ADD", "register:40f0:8", ["const:736318:8", "const:4:8"]]
+ 00736318 ["CALL", null, ["callee:0048ce84:8"]]
- 007362d8 bytes db5af597
+ 00736318 bytes db5af597
- 0073641c ["INT_ADD", "register:40f0:8", ["const:73641c:8", "const:4:8"]]
- 0073641c ["CALL", null, ["callee:00c57e90:8"]]
+ 0073645c ["INT_ADD", "register:40f0:8", ["const:73645c:8", "const:4:8"]]
+ 0073645c ["CALL", null, ["callee:00c57e90:8"]]
- 0073641c bytes 9d851494
+ 0073645c bytes 8d861494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbc3a5d980b31639608b9e1c311304f2"></a>

### [`0073730c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/0073730c.md) → [`0073734c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00737/0073734c.md) FUN_0073734c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00764730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764730.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 4件 [`00732e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732e8c.md) [`007336c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/007336c8.md) [`0073aef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073aef4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`00764770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764770.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) · 呼出先 4件 [`00732ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732ecc.md) [`00733708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733708.md) [`0073af34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073af34.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073736c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/0073730c.md#insn-0073736c) · [`00737384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/0073730c.md#insn-00737384) · [`00737390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/0073730c.md#insn-00737390)
- 新版 `007373ac`（命令位置の公開資料なし） · `007373c4`（命令位置の公開資料なし） · `007373d0`（命令位置の公開資料なし）

~~~diff
- 0073736c ["INT_ADD", "register:40f0:8", ["const:73736c:8", "const:4:8"]]
- 0073736c ["CALL", null, ["callee:00732ecc:8"]]
+ 007373ac ["INT_ADD", "register:40f0:8", ["const:7373ac:8", "const:4:8"]]
+ 007373ac ["CALL", null, ["callee:00732ecc:8"]]
- 0073736c bytes c8eeff97
+ 007373ac bytes c8eeff97
- 00737384 ["INT_ADD", "register:40f0:8", ["const:737384:8", "const:4:8"]]
- 00737384 ["CALL", null, ["callee:008514f8:8"]]
+ 007373c4 ["INT_ADD", "register:40f0:8", ["const:7373c4:8", "const:4:8"]]
+ 007373c4 ["CALL", null, ["callee:008514f8:8"]]
- 00737384 bytes 4d680494
+ 007373c4 bytes 4d680494
- 00737390 ["INT_ADD", "register:40f0:8", ["const:737390:8", "const:4:8"]]
- 00737390 ["CALL", null, ["callee:00733708:8"]]
+ 007373d0 ["INT_ADD", "register:40f0:8", ["const:7373d0:8", "const:4:8"]]
+ 007373d0 ["CALL", null, ["callee:00733708:8"]]
- 00737390 bytes cef0ff97
+ 007373d0 bytes cef0ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d947fdad1110745c40f8c8912a90da0"></a>

### [`007373f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/007373f4.md) → [`00737434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00737/00737434.md) FUN_00737434

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00764730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764730.md) [`0077a3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077a/0077a3d8.md) · 呼出先 4件 [`00732e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732e8c.md) [`007336c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/007336c8.md) [`0073aef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073aef4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00764770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764770.md) [`0077a418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077a/0077a418.md) · 呼出先 4件 [`00732ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732ecc.md) [`00733708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733708.md) [`0073af34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073af34.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00737454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/007373f4.md#insn-00737454) · [`0073746c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/007373f4.md#insn-0073746c) · [`00737478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/007373f4.md#insn-00737478)
- 新版 `00737494`（命令位置の公開資料なし） · `007374ac`（命令位置の公開資料なし） · `007374b8`（命令位置の公開資料なし）

~~~diff
- 00737454 ["INT_ADD", "register:40f0:8", ["const:737454:8", "const:4:8"]]
- 00737454 ["CALL", null, ["callee:00732ecc:8"]]
+ 00737494 ["INT_ADD", "register:40f0:8", ["const:737494:8", "const:4:8"]]
+ 00737494 ["CALL", null, ["callee:00732ecc:8"]]
- 00737454 bytes 8eeeff97
+ 00737494 bytes 8eeeff97
- 0073746c ["INT_ADD", "register:40f0:8", ["const:73746c:8", "const:4:8"]]
- 0073746c ["CALL", null, ["callee:008514f8:8"]]
+ 007374ac ["INT_ADD", "register:40f0:8", ["const:7374ac:8", "const:4:8"]]
+ 007374ac ["CALL", null, ["callee:008514f8:8"]]
- 0073746c bytes 13680494
+ 007374ac bytes 13680494
- 00737478 ["INT_ADD", "register:40f0:8", ["const:737478:8", "const:4:8"]]
- 00737478 ["CALL", null, ["callee:00733708:8"]]
+ 007374b8 ["INT_ADD", "register:40f0:8", ["const:7374b8:8", "const:4:8"]]
+ 007374b8 ["CALL", null, ["callee:00733708:8"]]
- 00737478 bytes 94f0ff97
+ 007374b8 bytes 94f0ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-038b4198cb78b2a704eb25da0ac6370f"></a>

### [`007374f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/007374f0.md) → [`00737530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00737/00737530.md) FUN_00737530

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 4件 [`00732e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732e8c.md) [`007336c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/007336c8.md) [`0073aef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073aef4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) · 呼出先 4件 [`00732ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732ecc.md) [`00733708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733708.md) [`0073af34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073af34.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073754c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/007374f0.md#insn-0073754c) · [`00737564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/007374f0.md#insn-00737564) · [`00737570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/007374f0.md#insn-00737570)
- 新版 `0073758c`（命令位置の公開資料なし） · `007375a4`（命令位置の公開資料なし） · `007375b0`（命令位置の公開資料なし）

~~~diff
- 0073754c ["INT_ADD", "register:40f0:8", ["const:73754c:8", "const:4:8"]]
- 0073754c ["CALL", null, ["callee:00732ecc:8"]]
+ 0073758c ["INT_ADD", "register:40f0:8", ["const:73758c:8", "const:4:8"]]
+ 0073758c ["CALL", null, ["callee:00732ecc:8"]]
- 0073754c bytes 50eeff97
+ 0073758c bytes 50eeff97
- 00737564 ["INT_ADD", "register:40f0:8", ["const:737564:8", "const:4:8"]]
- 00737564 ["CALL", null, ["callee:008514f8:8"]]
+ 007375a4 ["INT_ADD", "register:40f0:8", ["const:7375a4:8", "const:4:8"]]
+ 007375a4 ["CALL", null, ["callee:008514f8:8"]]
- 00737564 bytes d5670494
+ 007375a4 bytes d5670494
- 00737570 ["INT_ADD", "register:40f0:8", ["const:737570:8", "const:4:8"]]
- 00737570 ["CALL", null, ["callee:00733708:8"]]
+ 007375b0 ["INT_ADD", "register:40f0:8", ["const:7375b0:8", "const:4:8"]]
+ 007375b0 ["CALL", null, ["callee:00733708:8"]]
- 00737570 bytes 56f0ff97
+ 007375b0 bytes 56f0ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-399f11410b90ffe9a5ea07cd99717add"></a>

### [`007375e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/007375e4.md) → [`00737624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00737/00737624.md) FUN_00737624

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 4件 [`00732e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732e8c.md) [`007336c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/007336c8.md) [`0073aef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073aef4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 4件 [`00732ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732ecc.md) [`00733708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733708.md) [`0073af34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073af34.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00737644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/007375e4.md#insn-00737644) · [`0073765c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/007375e4.md#insn-0073765c) · [`00737668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/007375e4.md#insn-00737668)
- 新版 `00737684`（命令位置の公開資料なし） · `0073769c`（命令位置の公開資料なし） · `007376a8`（命令位置の公開資料なし）

~~~diff
- 00737644 ["INT_ADD", "register:40f0:8", ["const:737644:8", "const:4:8"]]
- 00737644 ["CALL", null, ["callee:00732ecc:8"]]
+ 00737684 ["INT_ADD", "register:40f0:8", ["const:737684:8", "const:4:8"]]
+ 00737684 ["CALL", null, ["callee:00732ecc:8"]]
- 00737644 bytes 12eeff97
+ 00737684 bytes 12eeff97
- 0073765c ["INT_ADD", "register:40f0:8", ["const:73765c:8", "const:4:8"]]
- 0073765c ["CALL", null, ["callee:008514f8:8"]]
+ 0073769c ["INT_ADD", "register:40f0:8", ["const:73769c:8", "const:4:8"]]
+ 0073769c ["CALL", null, ["callee:008514f8:8"]]
- 0073765c bytes 97670494
+ 0073769c bytes 97670494
- 00737668 ["INT_ADD", "register:40f0:8", ["const:737668:8", "const:4:8"]]
- 00737668 ["CALL", null, ["callee:00733708:8"]]
+ 007376a8 ["INT_ADD", "register:40f0:8", ["const:7376a8:8", "const:4:8"]]
+ 007376a8 ["CALL", null, ["callee:00733708:8"]]
- 00737668 bytes 18f0ff97
+ 007376a8 bytes 18f0ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41d50bc45e6ca235538b1a430b336dc4"></a>

### [`007376d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/007376d4.md) → [`00737714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00737/00737714.md) FUN_00737714

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00737750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/007376d4.md#insn-00737750) · [`00737788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/007376d4.md#insn-00737788)
- 新版 `00737790`（命令位置の公開資料なし） · `007377c8`（命令位置の公開資料なし）

~~~diff
- 00737750 ["INT_ADD", "register:40f0:8", ["const:737750:8", "const:4:8"]]
- 00737750 ["CALL", null, ["callee:00c57e90:8"]]
+ 00737790 ["INT_ADD", "register:40f0:8", ["const:737790:8", "const:4:8"]]
+ 00737790 ["CALL", null, ["callee:00c57e90:8"]]
- 00737750 bytes d0801494
+ 00737790 bytes c0811494
- 00737788 ["INT_ADD", "register:40f0:8", ["const:737788:8", "const:4:8"]]
- 00737788 ["CALL", null, ["callee:0043bba4:8"]]
+ 007377c8 ["INT_ADD", "register:40f0:8", ["const:7377c8:8", "const:4:8"]]
+ 007377c8 ["CALL", null, ["callee:0043bba4:8"]]
- 00737788 bytes f710f497
+ 007377c8 bytes f710f497
~~~


<a id="compare-0633eb58e5ab717f3b08cf5651e1e77b"></a>

### [`007377b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/007377b8.md) → [`007377f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00737/007377f8.md) FUN_007377f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00737838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/007377b8.md#insn-00737838) · [`00737870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/007377b8.md#insn-00737870)
- 新版 `00737878`（命令位置の公開資料なし） · `007378b0`（命令位置の公開資料なし）

~~~diff
- 00737838 ["INT_ADD", "register:40f0:8", ["const:737838:8", "const:4:8"]]
- 00737838 ["CALL", null, ["callee:00c57e90:8"]]
+ 00737878 ["INT_ADD", "register:40f0:8", ["const:737878:8", "const:4:8"]]
+ 00737878 ["CALL", null, ["callee:00c57e90:8"]]
- 00737838 bytes 96801494
+ 00737878 bytes 86811494
- 00737870 ["INT_ADD", "register:40f0:8", ["const:737870:8", "const:4:8"]]
- 00737870 ["CALL", null, ["callee:0043bba4:8"]]
+ 007378b0 ["INT_ADD", "register:40f0:8", ["const:7378b0:8", "const:4:8"]]
+ 007378b0 ["CALL", null, ["callee:0043bba4:8"]]
- 00737870 bytes bd10f497
+ 007378b0 bytes bd10f497
~~~


