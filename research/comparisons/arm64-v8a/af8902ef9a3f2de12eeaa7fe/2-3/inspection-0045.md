# v16.0.0 → v16.0.1 · 要調査の変更候補 (45)

[一覧の目次](README.md)

<a id="compare-8200b7e1b9bd6dde7a32eace00ce0909"></a>

### [`00c485c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c485c8.md) → [`00c489f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c489f0.md) FUN_00c489f0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c485f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c485c8.md#insn-00c485f4) · [`00c48618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c485c8.md#insn-00c48618)
- 新版 `00c48a1c`（命令位置の公開資料なし） · `00c48a40`（命令位置の公開資料なし）

~~~diff
- 00c485f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c485f4 ["INT_ADD", "register:40f0:8", ["const:c485f4:8", "const:4:8"]]
- 00c485f4 ["CALLIND", null, ["register:0:8"]]
+ 00c48a1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c48a1c ["INT_ADD", "register:40f0:8", ["const:c48a1c:8", "const:4:8"]]
+ 00c48a1c ["CALLIND", null, ["register:0:8"]]
- 00c485f4 bytes 00013fd6
+ 00c48a1c bytes 00013fd6
- 00c48618 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c48618 ["INT_ADD", "register:40f0:8", ["const:c48618:8", "const:4:8"]]
- 00c48618 ["CALLIND", null, ["register:0:8"]]
+ 00c48a40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c48a40 ["INT_ADD", "register:40f0:8", ["const:c48a40:8", "const:4:8"]]
+ 00c48a40 ["CALLIND", null, ["register:0:8"]]
- 00c48618 bytes 00013fd6
+ 00c48a40 bytes 00013fd6
~~~


<a id="compare-d71c4450a6a37bf8187b5916728415e5"></a>

### [`00c4888c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4888c.md) → [`00c48cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48cb4.md) FUN_00c48cb4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c488ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4888c.md#insn-00c488ac) · [`00c488d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4888c.md#insn-00c488d8) · [`00c48918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4888c.md#insn-00c48918)
- 新版 `00c48cd4`（命令位置の公開資料なし） · `00c48d00`（命令位置の公開資料なし） · `00c48d40`（命令位置の公開資料なし）

~~~diff
- 00c488ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00c488ac ["INT_ADD", "register:40f0:8", ["const:c488ac:8", "const:4:8"]]
- 00c488ac ["CALLIND", null, ["register:0:8"]]
+ 00c48cd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c48cd4 ["INT_ADD", "register:40f0:8", ["const:c48cd4:8", "const:4:8"]]
+ 00c48cd4 ["CALLIND", null, ["register:0:8"]]
- 00c488ac bytes 00013fd6
+ 00c48cd4 bytes 00013fd6
- 00c488d8 ["INT_ADD", "register:40f0:8", ["const:c488d8:8", "const:4:8"]]
- 00c488d8 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c48d00 ["INT_ADD", "register:40f0:8", ["const:c48d00:8", "const:4:8"]]
+ 00c48d00 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c488d8 bytes f2440094
+ 00c48d00 bytes e8440094
- 00c48918 ["INT_ADD", "register:40f0:8", ["const:c48918:8", "const:4:8"]]
- 00c48918 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c48d40 ["INT_ADD", "register:40f0:8", ["const:c48d40:8", "const:4:8"]]
+ 00c48d40 ["CALL", null, ["callee:00c5b140:8"]]
- 00c48918 bytes 0a490094
+ 00c48d40 bytes 00490094
~~~


<a id="compare-e25426305ae156fa09ccfe5341cbee1d"></a>

### [`00c48938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48938.md) → [`00c48d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48d60.md) FUN_00c48d60

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c48a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48a98.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c48ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48ec0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c48980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48938.md#insn-00c48980) · [`00c489f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48938.md#insn-00c489f0) · [`00c48a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48938.md#insn-00c48a0c)
- 新版 `00c48da8`（命令位置の公開資料なし） · `00c48e18`（命令位置の公開資料なし） · `00c48e34`（命令位置の公開資料なし）

~~~diff
- 00c48980 ["INT_ADD", "register:40f0:8", ["const:c48980:8", "const:4:8"]]
- 00c48980 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c48da8 ["INT_ADD", "register:40f0:8", ["const:c48da8:8", "const:4:8"]]
+ 00c48da8 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c48980 bytes c8440094
+ 00c48da8 bytes be440094
- 00c489f0 ["INT_ADD", "register:40f0:8", ["const:c489f0:8", "const:4:8"]]
- 00c489f0 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c48e18 ["INT_ADD", "register:40f0:8", ["const:c48e18:8", "const:4:8"]]
+ 00c48e18 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c489f0 bytes ac440094
+ 00c48e18 bytes a2440094
- 00c48a0c ["INT_ADD", "register:40f0:8", ["const:c48a0c:8", "const:4:8"]]
- 00c48a0c ["CALL", null, ["callee:00c58000:8"]]
+ 00c48e34 ["INT_ADD", "register:40f0:8", ["const:c48e34:8", "const:4:8"]]
+ 00c48e34 ["CALL", null, ["callee:00c58000:8"]]
- 00c48a0c bytes 7d3c0094
+ 00c48e34 bytes 733c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-034acb5b0af81d2051e20c6a84849fdf"></a>

### [`00c48df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48df8.md) → [`00c49220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c49220.md) FUN_00c49220

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c48a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48a98.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c48ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48ec0.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c48e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48df8.md#insn-00c48e3c) · [`00c48e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48df8.md#insn-00c48e78) · [`00c48ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48df8.md#insn-00c48ea8)
- 新版 `00c49264`（命令位置の公開資料なし） · `00c492a0`（命令位置の公開資料なし） · `00c492d0`（命令位置の公開資料なし）

~~~diff
- 00c48e3c ["INT_ADD", "register:40f0:8", ["const:c48e3c:8", "const:4:8"]]
- 00c48e3c ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c49264 ["INT_ADD", "register:40f0:8", ["const:c49264:8", "const:4:8"]]
+ 00c49264 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c48e3c bytes 99430094
+ 00c49264 bytes 8f430094
- 00c48e78 ["INT_ADD", "register:40f0:8", ["const:c48e78:8", "const:4:8"]]
- 00c48e78 ["CALL", null, ["callee:00c48ec0:8"]]
+ 00c492a0 ["INT_ADD", "register:40f0:8", ["const:c492a0:8", "const:4:8"]]
+ 00c492a0 ["CALL", null, ["callee:00c48ec0:8"]]
- 00c48e78 bytes 08ffff97
+ 00c492a0 bytes 08ffff97
- 00c48ea8 ["INT_ADD", "register:40f0:8", ["const:c48ea8:8", "const:4:8"]]
- 00c48ea8 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c492d0 ["INT_ADD", "register:40f0:8", ["const:c492d0:8", "const:4:8"]]
+ 00c492d0 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c48ea8 bytes 7e430094
+ 00c492d0 bytes 74430094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cd82d916a6e6dc9912935140ed63a15"></a>

### [`00c48efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48efc.md) → [`00c49324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c49324.md) FUN_00c49324

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c48f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48efc.md#insn-00c48f4c) · [`00c48f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48efc.md#insn-00c48f80) · [`00c48fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48efc.md#insn-00c48fa4)
- 新版 `00c49374`（命令位置の公開資料なし） · `00c493a8`（命令位置の公開資料なし） · `00c493cc`（命令位置の公開資料なし）

~~~diff
- 00c48f4c ["INT_ADD", "register:40f0:8", ["const:c48f4c:8", "const:4:8"]]
- 00c48f4c ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c49374 ["INT_ADD", "register:40f0:8", ["const:c49374:8", "const:4:8"]]
+ 00c49374 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c48f4c bytes 55430094
+ 00c49374 bytes 4b430094
- 00c48f80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c48f80 ["INT_ADD", "register:40f0:8", ["const:c48f80:8", "const:4:8"]]
- 00c48f80 ["CALLIND", null, ["register:0:8"]]
+ 00c493a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c493a8 ["INT_ADD", "register:40f0:8", ["const:c493a8:8", "const:4:8"]]
+ 00c493a8 ["CALLIND", null, ["register:0:8"]]
- 00c48f80 bytes 00013fd6
+ 00c493a8 bytes 00013fd6
- 00c48fa4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c48fa4 ["INT_ADD", "register:40f0:8", ["const:c48fa4:8", "const:4:8"]]
- 00c48fa4 ["CALLIND", null, ["register:0:8"]]
+ 00c493cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c493cc ["INT_ADD", "register:40f0:8", ["const:c493cc:8", "const:4:8"]]
+ 00c493cc ["CALLIND", null, ["register:0:8"]]
- 00c48fa4 bytes 00013fd6
+ 00c493cc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0724793475265c22a0f7d923faa86615"></a>

### [`00c491d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c491d4.md) → [`00c495fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c495fc.md) FUN_00c495fc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4921c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c491d4.md#insn-00c4921c) · [`00c49278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c491d4.md#insn-00c49278) · [`00c49294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c491d4.md#insn-00c49294)
- 新版 `00c49644`（命令位置の公開資料なし） · `00c496a0`（命令位置の公開資料なし） · `00c496bc`（命令位置の公開資料なし）

~~~diff
- 00c4921c ["INT_ADD", "register:40f0:8", ["const:c4921c:8", "const:4:8"]]
- 00c4921c ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c49644 ["INT_ADD", "register:40f0:8", ["const:c49644:8", "const:4:8"]]
+ 00c49644 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4921c bytes a1420094
+ 00c49644 bytes 97420094
- 00c49278 ["INT_ADD", "register:40f0:8", ["const:c49278:8", "const:4:8"]]
- 00c49278 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c496a0 ["INT_ADD", "register:40f0:8", ["const:c496a0:8", "const:4:8"]]
+ 00c496a0 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c49278 bytes 8a420094
+ 00c496a0 bytes 80420094
- 00c49294 ["INT_ADD", "register:40f0:8", ["const:c49294:8", "const:4:8"]]
- 00c49294 ["CALL", null, ["callee:00c58000:8"]]
+ 00c496bc ["INT_ADD", "register:40f0:8", ["const:c496bc:8", "const:4:8"]]
+ 00c496bc ["CALL", null, ["callee:00c58000:8"]]
- 00c49294 bytes 5b3a0094
+ 00c496bc bytes 513a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fce4917fea7948440fb9c14d165bf2c"></a>

### [`00c49a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49a4c.md) → [`00c49e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c49e74.md) FUN_00c49e74

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c492c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c492c8.md) [`00c4af8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4af8c.md) · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 2件 [`00c496f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c496f0.md) [`00c4b3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b3b4.md) · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c49a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49a4c.md#insn-00c49a90) · [`00c49ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49a4c.md#insn-00c49ab4) · [`00c49b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49a4c.md#insn-00c49b10)
- 新版 `00c49eb8`（命令位置の公開資料なし） · `00c49edc`（命令位置の公開資料なし） · `00c49f38`（命令位置の公開資料なし）

~~~diff
- 00c49a90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c49a90 ["INT_ADD", "register:40f0:8", ["const:c49a90:8", "const:4:8"]]
- 00c49a90 ["CALLIND", null, ["register:0:8"]]
+ 00c49eb8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c49eb8 ["INT_ADD", "register:40f0:8", ["const:c49eb8:8", "const:4:8"]]
+ 00c49eb8 ["CALLIND", null, ["register:0:8"]]
- 00c49a90 bytes 00013fd6
+ 00c49eb8 bytes 00013fd6
- 00c49ab4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c49ab4 ["INT_ADD", "register:40f0:8", ["const:c49ab4:8", "const:4:8"]]
- 00c49ab4 ["CALLIND", null, ["register:0:8"]]
+ 00c49edc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c49edc ["INT_ADD", "register:40f0:8", ["const:c49edc:8", "const:4:8"]]
+ 00c49edc ["CALLIND", null, ["register:0:8"]]
- 00c49ab4 bytes 00013fd6
+ 00c49edc bytes 00013fd6
- 00c49b10 ["INT_ADD", "register:40f0:8", ["const:c49b10:8", "const:4:8"]]
- 00c49b10 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c49f38 ["INT_ADD", "register:40f0:8", ["const:c49f38:8", "const:4:8"]]
+ 00c49f38 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c49b10 bytes 64400094
+ 00c49f38 bytes 5a400094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34dbcfa122798ed102f8cb221b888e81"></a>

### [`00c49c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49c0c.md) → [`00c4a034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a034.md) FUN_00c4a034

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c49c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49c0c.md#insn-00c49c58) · [`00c49c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49c0c.md#insn-00c49c8c) · [`00c49cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49c0c.md#insn-00c49cb0)
- 新版 `00c4a080`（命令位置の公開資料なし） · `00c4a0b4`（命令位置の公開資料なし） · `00c4a0d8`（命令位置の公開資料なし）

~~~diff
- 00c49c58 ["INT_ADD", "register:40f0:8", ["const:c49c58:8", "const:4:8"]]
- 00c49c58 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4a080 ["INT_ADD", "register:40f0:8", ["const:c4a080:8", "const:4:8"]]
+ 00c4a080 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c49c58 bytes 12400094
+ 00c4a080 bytes 08400094
- 00c49c8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c49c8c ["INT_ADD", "register:40f0:8", ["const:c49c8c:8", "const:4:8"]]
- 00c49c8c ["CALLIND", null, ["register:0:8"]]
+ 00c4a0b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4a0b4 ["INT_ADD", "register:40f0:8", ["const:c4a0b4:8", "const:4:8"]]
+ 00c4a0b4 ["CALLIND", null, ["register:0:8"]]
- 00c49c8c bytes 00013fd6
+ 00c4a0b4 bytes 00013fd6
- 00c49cb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c49cb0 ["INT_ADD", "register:40f0:8", ["const:c49cb0:8", "const:4:8"]]
- 00c49cb0 ["CALLIND", null, ["register:0:8"]]
+ 00c4a0d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4a0d8 ["INT_ADD", "register:40f0:8", ["const:c4a0d8:8", "const:4:8"]]
+ 00c4a0d8 ["CALLIND", null, ["register:0:8"]]
- 00c49cb0 bytes 00013fd6
+ 00c4a0d8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ac69602b0a1c56688bd03a6ad60a946"></a>

### [`00c49e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49e58.md) → [`00c4a280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a280.md) FUN_00c4a280

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c49ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49e58.md#insn-00c49ea0) · [`00c49ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49e58.md#insn-00c49ed8) · [`00c49efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49e58.md#insn-00c49efc)
- 新版 `00c4a2c8`（命令位置の公開資料なし） · `00c4a300`（命令位置の公開資料なし） · `00c4a324`（命令位置の公開資料なし）

~~~diff
- 00c49ea0 ["INT_ADD", "register:40f0:8", ["const:c49ea0:8", "const:4:8"]]
- 00c49ea0 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4a2c8 ["INT_ADD", "register:40f0:8", ["const:c4a2c8:8", "const:4:8"]]
+ 00c4a2c8 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c49ea0 bytes 803f0094
+ 00c4a2c8 bytes 763f0094
- 00c49ed8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c49ed8 ["INT_ADD", "register:40f0:8", ["const:c49ed8:8", "const:4:8"]]
- 00c49ed8 ["CALLIND", null, ["register:0:8"]]
+ 00c4a300 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4a300 ["INT_ADD", "register:40f0:8", ["const:c4a300:8", "const:4:8"]]
+ 00c4a300 ["CALLIND", null, ["register:0:8"]]
- 00c49ed8 bytes 00013fd6
+ 00c4a300 bytes 00013fd6
- 00c49efc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c49efc ["INT_ADD", "register:40f0:8", ["const:c49efc:8", "const:4:8"]]
- 00c49efc ["CALLIND", null, ["register:0:8"]]
+ 00c4a324 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4a324 ["INT_ADD", "register:40f0:8", ["const:c4a324:8", "const:4:8"]]
+ 00c4a324 ["CALLIND", null, ["register:0:8"]]
- 00c49efc bytes 00013fd6
+ 00c4a324 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2f7d1bd6583e0b5b4295398b3ffe495"></a>

### [`00c4a0c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a0c4.md) → [`00c4a4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a4ec.md) FUN_00c4a4ec

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4a0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a0c4.md#insn-00c4a0f8) · [`00c4a11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a0c4.md#insn-00c4a11c) · [`00c4a148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a0c4.md#insn-00c4a148)
- 新版 `00c4a520`（命令位置の公開資料なし） · `00c4a544`（命令位置の公開資料なし） · `00c4a570`（命令位置の公開資料なし）

~~~diff
- 00c4a0f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a0f8 ["INT_ADD", "register:40f0:8", ["const:c4a0f8:8", "const:4:8"]]
- 00c4a0f8 ["CALLIND", null, ["register:0:8"]]
+ 00c4a520 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4a520 ["INT_ADD", "register:40f0:8", ["const:c4a520:8", "const:4:8"]]
+ 00c4a520 ["CALLIND", null, ["register:0:8"]]
- 00c4a0f8 bytes 00013fd6
+ 00c4a520 bytes 00013fd6
- 00c4a11c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a11c ["INT_ADD", "register:40f0:8", ["const:c4a11c:8", "const:4:8"]]
- 00c4a11c ["CALLIND", null, ["register:0:8"]]
+ 00c4a544 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4a544 ["INT_ADD", "register:40f0:8", ["const:c4a544:8", "const:4:8"]]
+ 00c4a544 ["CALLIND", null, ["register:0:8"]]
- 00c4a11c bytes 00013fd6
+ 00c4a544 bytes 00013fd6
- 00c4a148 ["INT_ADD", "register:40f0:8", ["const:c4a148:8", "const:4:8"]]
- 00c4a148 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4a570 ["INT_ADD", "register:40f0:8", ["const:c4a570:8", "const:4:8"]]
+ 00c4a570 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4a148 bytes d63e0094
+ 00c4a570 bytes cc3e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-619b8aa41a3710bf44368941fa817d71"></a>

### [`00c4a1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a1e0.md) → [`00c4a608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a608.md) FUN_00c4a608

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4a230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a1e0.md#insn-00c4a230) · [`00c4a264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a1e0.md#insn-00c4a264) · [`00c4a288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a1e0.md#insn-00c4a288)
- 新版 `00c4a658`（命令位置の公開資料なし） · `00c4a68c`（命令位置の公開資料なし） · `00c4a6b0`（命令位置の公開資料なし）

~~~diff
- 00c4a230 ["INT_ADD", "register:40f0:8", ["const:c4a230:8", "const:4:8"]]
- 00c4a230 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4a658 ["INT_ADD", "register:40f0:8", ["const:c4a658:8", "const:4:8"]]
+ 00c4a658 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4a230 bytes 9c3e0094
+ 00c4a658 bytes 923e0094
- 00c4a264 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a264 ["INT_ADD", "register:40f0:8", ["const:c4a264:8", "const:4:8"]]
- 00c4a264 ["CALLIND", null, ["register:0:8"]]
+ 00c4a68c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4a68c ["INT_ADD", "register:40f0:8", ["const:c4a68c:8", "const:4:8"]]
+ 00c4a68c ["CALLIND", null, ["register:0:8"]]
- 00c4a264 bytes 00013fd6
+ 00c4a68c bytes 00013fd6
- 00c4a288 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a288 ["INT_ADD", "register:40f0:8", ["const:c4a288:8", "const:4:8"]]
- 00c4a288 ["CALLIND", null, ["register:0:8"]]
+ 00c4a6b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4a6b0 ["INT_ADD", "register:40f0:8", ["const:c4a6b0:8", "const:4:8"]]
+ 00c4a6b0 ["CALLIND", null, ["register:0:8"]]
- 00c4a288 bytes 00013fd6
+ 00c4a6b0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-548b03519e8f6cb6f8b33186556d44ce"></a>

### [`00c4a924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a924.md) → [`00c4ad4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4ad4c.md) FUN_00c4ad4c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4a96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a924.md#insn-00c4a96c) · [`00c4a9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a924.md#insn-00c4a9d0) · [`00c4aa24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a924.md#insn-00c4aa24)
- 新版 `00c4ad94`（命令位置の公開資料なし） · `00c4adf8`（命令位置の公開資料なし） · `00c4ae4c`（命令位置の公開資料なし）

~~~diff
- 00c4a96c ["INT_ADD", "register:40f0:8", ["const:c4a96c:8", "const:4:8"]]
- 00c4a96c ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4ad94 ["INT_ADD", "register:40f0:8", ["const:c4ad94:8", "const:4:8"]]
+ 00c4ad94 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4a96c bytes cd3c0094
+ 00c4ad94 bytes c33c0094
- 00c4a9d0 ["INT_ADD", "register:40f0:8", ["const:c4a9d0:8", "const:4:8"]]
- 00c4a9d0 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4adf8 ["INT_ADD", "register:40f0:8", ["const:c4adf8:8", "const:4:8"]]
+ 00c4adf8 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4a9d0 bytes b43c0094
+ 00c4adf8 bytes aa3c0094
- 00c4aa24 ["INT_ADD", "register:40f0:8", ["const:c4aa24:8", "const:4:8"]]
- 00c4aa24 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4ae4c ["INT_ADD", "register:40f0:8", ["const:c4ae4c:8", "const:4:8"]]
+ 00c4ae4c ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4aa24 bytes 9f3c0094
+ 00c4ae4c bytes 953c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7ef0e378100604c8b6a5953e94f9779"></a>

### [`00c4b120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b120.md) → [`00c4b548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b548.md) FUN_00c4b548

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4b164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b120.md#insn-00c4b164) · [`00c4b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b120.md#insn-00c4b1b0) · [`00c4b1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b120.md#insn-00c4b1f4)
- 新版 `00c4b58c`（命令位置の公開資料なし） · `00c4b5d8`（命令位置の公開資料なし） · `00c4b61c`（命令位置の公開資料なし）

~~~diff
- 00c4b164 ["INT_ADD", "register:40f0:8", ["const:c4b164:8", "const:4:8"]]
- 00c4b164 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4b58c ["INT_ADD", "register:40f0:8", ["const:c4b58c:8", "const:4:8"]]
+ 00c4b58c ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4b164 bytes cf3a0094
+ 00c4b58c bytes c53a0094
- 00c4b1b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4b1b0 ["INT_ADD", "register:40f0:8", ["const:c4b1b0:8", "const:4:8"]]
- 00c4b1b0 ["CALLIND", null, ["register:0:8"]]
+ 00c4b5d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4b5d8 ["INT_ADD", "register:40f0:8", ["const:c4b5d8:8", "const:4:8"]]
+ 00c4b5d8 ["CALLIND", null, ["register:0:8"]]
- 00c4b1b0 bytes 00013fd6
+ 00c4b5d8 bytes 00013fd6
- 00c4b1f4 ["INT_ADD", "register:40f0:8", ["const:c4b1f4:8", "const:4:8"]]
- 00c4b1f4 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4b61c ["INT_ADD", "register:40f0:8", ["const:c4b61c:8", "const:4:8"]]
+ 00c4b61c ["CALL", null, ["callee:00c5b140:8"]]
- 00c4b1f4 bytes d33e0094
+ 00c4b61c bytes c93e0094
~~~


<a id="compare-dbfb50df9ac9fca3603929d14722903d"></a>

### [`00c4b200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b200.md) → [`00c4b628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b628.md) FUN_00c4b628

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c43244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43244.md) [`00c4b384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b384.md) · 呼出先 8件 [`00c3e714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e714.md) [`00c3ead8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3ead8.md) [`00c3ec0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3ec0c.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 2件 [`00c4366c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c4366c.md) [`00c4b7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b7ac.md) · 呼出先 8件 [`00c3eb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3eb3c.md) [`00c3ef00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ef00.md) [`00c3f034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f034.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4b23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b200.md#insn-00c4b23c) · [`00c4b270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b200.md#insn-00c4b270) · [`00c4b280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b200.md#insn-00c4b280)
- 新版 `00c4b664`（命令位置の公開資料なし） · `00c4b698`（命令位置の公開資料なし） · `00c4b6a8`（命令位置の公開資料なし）

~~~diff
- 00c4b23c ["INT_ADD", "register:40f0:8", ["const:c4b23c:8", "const:4:8"]]
- 00c4b23c ["CALL", null, ["callee:00c3eb3c:8"]]
+ 00c4b664 ["INT_ADD", "register:40f0:8", ["const:c4b664:8", "const:4:8"]]
+ 00c4b664 ["CALL", null, ["callee:00c3eb3c:8"]]
- 00c4b23c bytes 36cdff97
+ 00c4b664 bytes 36cdff97
- 00c4b270 ["INT_ADD", "register:40f0:8", ["const:c4b270:8", "const:4:8"]]
- 00c4b270 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4b698 ["INT_ADD", "register:40f0:8", ["const:c4b698:8", "const:4:8"]]
+ 00c4b698 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4b270 bytes 8c3a0094
+ 00c4b698 bytes 823a0094
- 00c4b280 ["INT_ADD", "register:40f0:8", ["const:c4b280:8", "const:4:8"]]
- 00c4b280 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4b6a8 ["INT_ADD", "register:40f0:8", ["const:c4b6a8:8", "const:4:8"]]
+ 00c4b6a8 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4b280 bytes b03e0094
+ 00c4b6a8 bytes a63e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37e9fb1c24bf78a29039d0b9246c41cf"></a>

### [`00c4b614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b614.md) → [`00c4ba3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4ba3c.md) FUN_00c4ba3c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4b640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b614.md#insn-00c4b640) · [`00c4b664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b614.md#insn-00c4b664) · [`00c4b690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b614.md#insn-00c4b690)
- 新版 `00c4ba68`（命令位置の公開資料なし） · `00c4ba8c`（命令位置の公開資料なし） · `00c4bab8`（命令位置の公開資料なし）

~~~diff
- 00c4b640 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4b640 ["INT_ADD", "register:40f0:8", ["const:c4b640:8", "const:4:8"]]
- 00c4b640 ["CALLIND", null, ["register:0:8"]]
+ 00c4ba68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4ba68 ["INT_ADD", "register:40f0:8", ["const:c4ba68:8", "const:4:8"]]
+ 00c4ba68 ["CALLIND", null, ["register:0:8"]]
- 00c4b640 bytes 00013fd6
+ 00c4ba68 bytes 00013fd6
- 00c4b664 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4b664 ["INT_ADD", "register:40f0:8", ["const:c4b664:8", "const:4:8"]]
- 00c4b664 ["CALLIND", null, ["register:0:8"]]
+ 00c4ba8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4ba8c ["INT_ADD", "register:40f0:8", ["const:c4ba8c:8", "const:4:8"]]
+ 00c4ba8c ["CALLIND", null, ["register:0:8"]]
- 00c4b664 bytes 00013fd6
+ 00c4ba8c bytes 00013fd6
- 00c4b690 ["INT_ADD", "register:40f0:8", ["const:c4b690:8", "const:4:8"]]
- 00c4b690 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4bab8 ["INT_ADD", "register:40f0:8", ["const:c4bab8:8", "const:4:8"]]
+ 00c4bab8 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4b690 bytes 84390094
+ 00c4bab8 bytes 7a390094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b72b1a082e8e0465ae787025fdf7f16"></a>

### [`00c4bab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bab4.md) → [`00c4bedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bedc.md) FUN_00c4bedc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4bafc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bab4.md#insn-00c4bafc) · [`00c4bb44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bab4.md#insn-00c4bb44)
- 新版 `00c4bf24`（命令位置の公開資料なし） · `00c4bf6c`（命令位置の公開資料なし）

~~~diff
- 00c4bafc ["INT_ADD", "register:40f0:8", ["const:c4bafc:8", "const:4:8"]]
- 00c4bafc ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4bf24 ["INT_ADD", "register:40f0:8", ["const:c4bf24:8", "const:4:8"]]
+ 00c4bf24 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4bafc bytes 69380094
+ 00c4bf24 bytes 5f380094
- 00c4bb44 ["INT_ADD", "register:40f0:8", ["const:c4bb44:8", "const:4:8"]]
- 00c4bb44 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4bf6c ["INT_ADD", "register:40f0:8", ["const:c4bf6c:8", "const:4:8"]]
+ 00c4bf6c ["CALL", null, ["callee:00c5b140:8"]]
- 00c4bb44 bytes 7f3c0094
+ 00c4bf6c bytes 753c0094
~~~


<a id="compare-fa8ea450eee85d2b286de5d058635b13"></a>

### [`00c4bd1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bd1c.md) → [`00c4c144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c144.md) FUN_00c4c144

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4bd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bd1c.md#insn-00c4bd60) · [`00c4bd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bd1c.md#insn-00c4bd9c) · [`00c4bde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bd1c.md#insn-00c4bde0)
- 新版 `00c4c188`（命令位置の公開資料なし） · `00c4c1c4`（命令位置の公開資料なし） · `00c4c208`（命令位置の公開資料なし）

~~~diff
- 00c4bd60 ["INT_ADD", "register:40f0:8", ["const:c4bd60:8", "const:4:8"]]
- 00c4bd60 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4c188 ["INT_ADD", "register:40f0:8", ["const:c4c188:8", "const:4:8"]]
+ 00c4c188 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4bd60 bytes d0370094
+ 00c4c188 bytes c6370094
- 00c4bd9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4bd9c ["INT_ADD", "register:40f0:8", ["const:c4bd9c:8", "const:4:8"]]
- 00c4bd9c ["CALLIND", null, ["register:0:8"]]
+ 00c4c1c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4c1c4 ["INT_ADD", "register:40f0:8", ["const:c4c1c4:8", "const:4:8"]]
+ 00c4c1c4 ["CALLIND", null, ["register:0:8"]]
- 00c4bd9c bytes 00013fd6
+ 00c4c1c4 bytes 00013fd6
- 00c4bde0 ["INT_ADD", "register:40f0:8", ["const:c4bde0:8", "const:4:8"]]
- 00c4bde0 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4c208 ["INT_ADD", "register:40f0:8", ["const:c4c208:8", "const:4:8"]]
+ 00c4c208 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4bde0 bytes d83b0094
+ 00c4c208 bytes ce3b0094
~~~


<a id="compare-7b5d6e5e00efc96de12b1145bd0be23e"></a>

### [`00c4c418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c418.md) → [`00c4c840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c840.md) FUN_00c4c840

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c4be00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4be00.md) · 呼出先 1件 [`00c3dd34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3dd34.md)
- 新版 呼出元 1件 [`00c4c228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c228.md) · 呼出先 1件 [`00c3e15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e15c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4c434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c418.md#insn-00c4c434)
- 新版 `00c4c85c`（命令位置の公開資料なし）

~~~diff
- 00c4c434 ["INT_ADD", "register:40f0:8", ["const:c4c434:8", "const:4:8"]]
- 00c4c434 ["CALL", null, ["callee:00c3e15c:8"]]
+ 00c4c85c ["INT_ADD", "register:40f0:8", ["const:c4c85c:8", "const:4:8"]]
+ 00c4c85c ["CALL", null, ["callee:00c3e15c:8"]]
- 00c4c434 bytes 40c6ff97
+ 00c4c85c bytes 40c6ff97
~~~


<a id="compare-31d0df7e1ef72ded24dbb1c944816bcb"></a>

### [`00c4c480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c480.md) → [`00c4c8a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c8a8.md) FUN_00c4c8a8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4c4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c480.md#insn-00c4c4a8) · [`00c4c4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c480.md#insn-00c4c4d4) · [`00c4c53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c480.md#insn-00c4c53c)
- 新版 `00c4c8d0`（命令位置の公開資料なし） · `00c4c8fc`（命令位置の公開資料なし） · `00c4c964`（命令位置の公開資料なし）

~~~diff
- 00c4c4a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4c4a8 ["INT_ADD", "register:40f0:8", ["const:c4c4a8:8", "const:4:8"]]
- 00c4c4a8 ["CALLIND", null, ["register:0:8"]]
+ 00c4c8d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4c8d0 ["INT_ADD", "register:40f0:8", ["const:c4c8d0:8", "const:4:8"]]
+ 00c4c8d0 ["CALLIND", null, ["register:0:8"]]
- 00c4c4a8 bytes 00013fd6
+ 00c4c8d0 bytes 00013fd6
- 00c4c4d4 ["INT_ADD", "register:40f0:8", ["const:c4c4d4:8", "const:4:8"]]
- 00c4c4d4 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4c8fc ["INT_ADD", "register:40f0:8", ["const:c4c8fc:8", "const:4:8"]]
+ 00c4c8fc ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4c4d4 bytes f3350094
+ 00c4c8fc bytes e9350094
- 00c4c53c ["INT_ADD", "register:40f0:8", ["const:c4c53c:8", "const:4:8"]]
- 00c4c53c ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4c964 ["INT_ADD", "register:40f0:8", ["const:c4c964:8", "const:4:8"]]
+ 00c4c964 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4c53c bytes d9350094
+ 00c4c964 bytes cf350094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c5d36f3b3a3680c22125ce732c0ef9b"></a>

### [`00c4c5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c5f0.md) → [`00c4ca18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4ca18.md) FUN_00c4ca18

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4c63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c5f0.md#insn-00c4c63c) · [`00c4c664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c5f0.md#insn-00c4c664) · [`00c4c69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c5f0.md#insn-00c4c69c)
- 新版 `00c4ca64`（命令位置の公開資料なし） · `00c4ca8c`（命令位置の公開資料なし） · `00c4cac4`（命令位置の公開資料なし）

~~~diff
- 00c4c63c ["INT_ADD", "register:40f0:8", ["const:c4c63c:8", "const:4:8"]]
- 00c4c63c ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4ca64 ["INT_ADD", "register:40f0:8", ["const:c4ca64:8", "const:4:8"]]
+ 00c4ca64 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4c63c bytes 99350094
+ 00c4ca64 bytes 8f350094
- 00c4c664 ["INT_ADD", "register:40f0:8", ["const:c4c664:8", "const:4:8"]]
- 00c4c664 ["CALL", null, ["callee:00c45144:8"]]
+ 00c4ca8c ["INT_ADD", "register:40f0:8", ["const:c4ca8c:8", "const:4:8"]]
+ 00c4ca8c ["CALL", null, ["callee:00c45144:8"]]
- 00c4c664 bytes aee1ff97
+ 00c4ca8c bytes aee1ff97
- 00c4c69c ["INT_ADD", "register:40f0:8", ["const:c4c69c:8", "const:4:8"]]
- 00c4c69c ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4cac4 ["INT_ADD", "register:40f0:8", ["const:c4cac4:8", "const:4:8"]]
+ 00c4cac4 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4c69c bytes 81350094
+ 00c4cac4 bytes 77350094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-694a88057fbe7bbedd00199124e33d65"></a>

### [`00c4c79c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c79c.md) → [`00c4cbc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cbc4.md) FUN_00c4cbc4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4c7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c79c.md#insn-00c4c7ec) · [`00c4c820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c79c.md#insn-00c4c820) · [`00c4c858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c79c.md#insn-00c4c858)
- 新版 `00c4cc14`（命令位置の公開資料なし） · `00c4cc48`（命令位置の公開資料なし） · `00c4cc80`（命令位置の公開資料なし）

~~~diff
- 00c4c7ec ["INT_ADD", "register:40f0:8", ["const:c4c7ec:8", "const:4:8"]]
- 00c4c7ec ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4cc14 ["INT_ADD", "register:40f0:8", ["const:c4cc14:8", "const:4:8"]]
+ 00c4cc14 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4c7ec bytes 2d350094
+ 00c4cc14 bytes 23350094
- 00c4c820 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4c820 ["INT_ADD", "register:40f0:8", ["const:c4c820:8", "const:4:8"]]
- 00c4c820 ["CALLIND", null, ["register:0:8"]]
+ 00c4cc48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4cc48 ["INT_ADD", "register:40f0:8", ["const:c4cc48:8", "const:4:8"]]
+ 00c4cc48 ["CALLIND", null, ["register:0:8"]]
- 00c4c820 bytes 00013fd6
+ 00c4cc48 bytes 00013fd6
- 00c4c858 ["INT_ADD", "register:40f0:8", ["const:c4c858:8", "const:4:8"]]
- 00c4c858 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4cc80 ["INT_ADD", "register:40f0:8", ["const:c4cc80:8", "const:4:8"]]
+ 00c4cc80 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4c858 bytes 12350094
+ 00c4cc80 bytes 08350094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07fcc543d68718c4366282daac15b4e2"></a>

### [`00c4c8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c8a8.md) → [`00c4ccd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4ccd0.md) FUN_00c4ccd0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4c8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c8a8.md#insn-00c4c8d4) · [`00c4c8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c8a8.md#insn-00c4c8f8) · [`00c4c924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c8a8.md#insn-00c4c924)
- 新版 `00c4ccfc`（命令位置の公開資料なし） · `00c4cd20`（命令位置の公開資料なし） · `00c4cd4c`（命令位置の公開資料なし）

~~~diff
- 00c4c8d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4c8d4 ["INT_ADD", "register:40f0:8", ["const:c4c8d4:8", "const:4:8"]]
- 00c4c8d4 ["CALLIND", null, ["register:0:8"]]
+ 00c4ccfc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4ccfc ["INT_ADD", "register:40f0:8", ["const:c4ccfc:8", "const:4:8"]]
+ 00c4ccfc ["CALLIND", null, ["register:0:8"]]
- 00c4c8d4 bytes 00013fd6
+ 00c4ccfc bytes 00013fd6
- 00c4c8f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4c8f8 ["INT_ADD", "register:40f0:8", ["const:c4c8f8:8", "const:4:8"]]
- 00c4c8f8 ["CALLIND", null, ["register:0:8"]]
+ 00c4cd20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4cd20 ["INT_ADD", "register:40f0:8", ["const:c4cd20:8", "const:4:8"]]
+ 00c4cd20 ["CALLIND", null, ["register:0:8"]]
- 00c4c8f8 bytes 00013fd6
+ 00c4cd20 bytes 00013fd6
- 00c4c924 ["INT_ADD", "register:40f0:8", ["const:c4c924:8", "const:4:8"]]
- 00c4c924 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4cd4c ["INT_ADD", "register:40f0:8", ["const:c4cd4c:8", "const:4:8"]]
+ 00c4cd4c ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4c924 bytes df340094
+ 00c4cd4c bytes d5340094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ddec448c2528782c31f010fd2ffc605"></a>

### [`00c4caf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4caf8.md) → [`00c4cf20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cf20.md) FUN_00c4cf20

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4cb24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4caf8.md#insn-00c4cb24) · [`00c4cb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4caf8.md#insn-00c4cb48) · [`00c4cb74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4caf8.md#insn-00c4cb74)
- 新版 `00c4cf4c`（命令位置の公開資料なし） · `00c4cf70`（命令位置の公開資料なし） · `00c4cf9c`（命令位置の公開資料なし）

~~~diff
- 00c4cb24 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4cb24 ["INT_ADD", "register:40f0:8", ["const:c4cb24:8", "const:4:8"]]
- 00c4cb24 ["CALLIND", null, ["register:0:8"]]
+ 00c4cf4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4cf4c ["INT_ADD", "register:40f0:8", ["const:c4cf4c:8", "const:4:8"]]
+ 00c4cf4c ["CALLIND", null, ["register:0:8"]]
- 00c4cb24 bytes 00013fd6
+ 00c4cf4c bytes 00013fd6
- 00c4cb48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4cb48 ["INT_ADD", "register:40f0:8", ["const:c4cb48:8", "const:4:8"]]
- 00c4cb48 ["CALLIND", null, ["register:0:8"]]
+ 00c4cf70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4cf70 ["INT_ADD", "register:40f0:8", ["const:c4cf70:8", "const:4:8"]]
+ 00c4cf70 ["CALLIND", null, ["register:0:8"]]
- 00c4cb48 bytes 00013fd6
+ 00c4cf70 bytes 00013fd6
- 00c4cb74 ["INT_ADD", "register:40f0:8", ["const:c4cb74:8", "const:4:8"]]
- 00c4cb74 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4cf9c ["INT_ADD", "register:40f0:8", ["const:c4cf9c:8", "const:4:8"]]
+ 00c4cf9c ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4cb74 bytes 4b340094
+ 00c4cf9c bytes 41340094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d64cd25a8232405bbb107cb1a2f3602e"></a>

### [`00c4ce1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4ce1c.md) → [`00c4d244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d244.md) FUN_00c4d244

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4ce48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4ce1c.md#insn-00c4ce48) · [`00c4ce6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4ce1c.md#insn-00c4ce6c) · [`00c4ce98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4ce1c.md#insn-00c4ce98)
- 新版 `00c4d270`（命令位置の公開資料なし） · `00c4d294`（命令位置の公開資料なし） · `00c4d2c0`（命令位置の公開資料なし）

~~~diff
- 00c4ce48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4ce48 ["INT_ADD", "register:40f0:8", ["const:c4ce48:8", "const:4:8"]]
- 00c4ce48 ["CALLIND", null, ["register:0:8"]]
+ 00c4d270 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d270 ["INT_ADD", "register:40f0:8", ["const:c4d270:8", "const:4:8"]]
+ 00c4d270 ["CALLIND", null, ["register:0:8"]]
- 00c4ce48 bytes 00013fd6
+ 00c4d270 bytes 00013fd6
- 00c4ce6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4ce6c ["INT_ADD", "register:40f0:8", ["const:c4ce6c:8", "const:4:8"]]
- 00c4ce6c ["CALLIND", null, ["register:0:8"]]
+ 00c4d294 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d294 ["INT_ADD", "register:40f0:8", ["const:c4d294:8", "const:4:8"]]
+ 00c4d294 ["CALLIND", null, ["register:0:8"]]
- 00c4ce6c bytes 00013fd6
+ 00c4d294 bytes 00013fd6
- 00c4ce98 ["INT_ADD", "register:40f0:8", ["const:c4ce98:8", "const:4:8"]]
- 00c4ce98 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4d2c0 ["INT_ADD", "register:40f0:8", ["const:c4d2c0:8", "const:4:8"]]
+ 00c4d2c0 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4ce98 bytes 82330094
+ 00c4d2c0 bytes 78330094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bf2d75267fd3df57367ebd5f59c080f"></a>

### [`00c4d158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d158.md) → [`00c4d580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d580.md) FUN_00c4d580

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4d1a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d158.md#insn-00c4d1a4) · [`00c4d1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d158.md#insn-00c4d1d0) · [`00c4d1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d158.md#insn-00c4d1fc)
- 新版 `00c4d5cc`（命令位置の公開資料なし） · `00c4d5f8`（命令位置の公開資料なし） · `00c4d624`（命令位置の公開資料なし）

~~~diff
- 00c4d1a4 ["INT_ADD", "register:40f0:8", ["const:c4d1a4:8", "const:4:8"]]
- 00c4d1a4 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4d5cc ["INT_ADD", "register:40f0:8", ["const:c4d5cc:8", "const:4:8"]]
+ 00c4d5cc ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4d1a4 bytes bf320094
+ 00c4d5cc bytes b5320094
- 00c4d1d0 ["INT_ADD", "register:40f0:8", ["const:c4d1d0:8", "const:4:8"]]
- 00c4d1d0 ["CALL", null, ["callee:00c45144:8"]]
+ 00c4d5f8 ["INT_ADD", "register:40f0:8", ["const:c4d5f8:8", "const:4:8"]]
+ 00c4d5f8 ["CALL", null, ["callee:00c45144:8"]]
- 00c4d1d0 bytes d3deff97
+ 00c4d5f8 bytes d3deff97
- 00c4d1fc ["INT_ADD", "register:40f0:8", ["const:c4d1fc:8", "const:4:8"]]
- 00c4d1fc ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4d624 ["INT_ADD", "register:40f0:8", ["const:c4d624:8", "const:4:8"]]
+ 00c4d624 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4d1fc bytes a9320094
+ 00c4d624 bytes 9f320094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10808bccd45292047c1a5c55a4193c49"></a>

### [`00c4d250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d250.md) → [`00c4d678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d678.md) FUN_00c4d678

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4d27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d250.md#insn-00c4d27c) · [`00c4d2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d250.md#insn-00c4d2a0) · [`00c4d2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d250.md#insn-00c4d2b8)
- 新版 `00c4d6a4`（命令位置の公開資料なし） · `00c4d6c8`（命令位置の公開資料なし） · `00c4d6e0`（命令位置の公開資料なし）

~~~diff
- 00c4d27c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4d27c ["INT_ADD", "register:40f0:8", ["const:c4d27c:8", "const:4:8"]]
- 00c4d27c ["CALLIND", null, ["register:0:8"]]
+ 00c4d6a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d6a4 ["INT_ADD", "register:40f0:8", ["const:c4d6a4:8", "const:4:8"]]
+ 00c4d6a4 ["CALLIND", null, ["register:0:8"]]
- 00c4d27c bytes 00013fd6
+ 00c4d6a4 bytes 00013fd6
- 00c4d2a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4d2a0 ["INT_ADD", "register:40f0:8", ["const:c4d2a0:8", "const:4:8"]]
- 00c4d2a0 ["CALLIND", null, ["register:0:8"]]
+ 00c4d6c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d6c8 ["INT_ADD", "register:40f0:8", ["const:c4d6c8:8", "const:4:8"]]
+ 00c4d6c8 ["CALLIND", null, ["register:0:8"]]
- 00c4d2a0 bytes 00013fd6
+ 00c4d6c8 bytes 00013fd6
- 00c4d2b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4d2b8 ["INT_ADD", "register:40f0:8", ["const:c4d2b8:8", "const:4:8"]]
- 00c4d2b8 ["CALLIND", null, ["register:0:8"]]
+ 00c4d6e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d6e0 ["INT_ADD", "register:40f0:8", ["const:c4d6e0:8", "const:4:8"]]
+ 00c4d6e0 ["CALLIND", null, ["register:0:8"]]
- 00c4d2b8 bytes 00013fd6
+ 00c4d6e0 bytes 00013fd6
~~~


<a id="compare-bdab2c79c19f3f0e1b223d611616f1d5"></a>

### [`00c4d49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d49c.md) → [`00c4d8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d8c4.md) FUN_00c4d8c4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4d4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d49c.md#insn-00c4d4e0) · [`00c4d52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d49c.md#insn-00c4d52c) · [`00c4d570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d49c.md#insn-00c4d570)
- 新版 `00c4d908`（命令位置の公開資料なし） · `00c4d954`（命令位置の公開資料なし） · `00c4d998`（命令位置の公開資料なし）

~~~diff
- 00c4d4e0 ["INT_ADD", "register:40f0:8", ["const:c4d4e0:8", "const:4:8"]]
- 00c4d4e0 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4d908 ["INT_ADD", "register:40f0:8", ["const:c4d908:8", "const:4:8"]]
+ 00c4d908 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4d4e0 bytes f0310094
+ 00c4d908 bytes e6310094
- 00c4d52c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4d52c ["INT_ADD", "register:40f0:8", ["const:c4d52c:8", "const:4:8"]]
- 00c4d52c ["CALLIND", null, ["register:0:8"]]
+ 00c4d954 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d954 ["INT_ADD", "register:40f0:8", ["const:c4d954:8", "const:4:8"]]
+ 00c4d954 ["CALLIND", null, ["register:0:8"]]
- 00c4d52c bytes 00013fd6
+ 00c4d954 bytes 00013fd6
- 00c4d570 ["INT_ADD", "register:40f0:8", ["const:c4d570:8", "const:4:8"]]
- 00c4d570 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4d998 ["INT_ADD", "register:40f0:8", ["const:c4d998:8", "const:4:8"]]
+ 00c4d998 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4d570 bytes f4350094
+ 00c4d998 bytes ea350094
~~~


<a id="compare-e5be66fad803ee67fff4a9d4a7eb8867"></a>

### [`00c4d594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d594.md) → [`00c4d9bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d9bc.md) FUN_00c4d9bc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4d5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d594.md#insn-00c4d5c0) · [`00c4d5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d594.md#insn-00c4d5e4) · [`00c4d620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d594.md#insn-00c4d620)
- 新版 `00c4d9e8`（命令位置の公開資料なし） · `00c4da0c`（命令位置の公開資料なし） · `00c4da48`（命令位置の公開資料なし）

~~~diff
- 00c4d5c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4d5c0 ["INT_ADD", "register:40f0:8", ["const:c4d5c0:8", "const:4:8"]]
- 00c4d5c0 ["CALLIND", null, ["register:0:8"]]
+ 00c4d9e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d9e8 ["INT_ADD", "register:40f0:8", ["const:c4d9e8:8", "const:4:8"]]
+ 00c4d9e8 ["CALLIND", null, ["register:0:8"]]
- 00c4d5c0 bytes 00013fd6
+ 00c4d9e8 bytes 00013fd6
- 00c4d5e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4d5e4 ["INT_ADD", "register:40f0:8", ["const:c4d5e4:8", "const:4:8"]]
- 00c4d5e4 ["CALLIND", null, ["register:0:8"]]
+ 00c4da0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4da0c ["INT_ADD", "register:40f0:8", ["const:c4da0c:8", "const:4:8"]]
+ 00c4da0c ["CALLIND", null, ["register:0:8"]]
- 00c4d5e4 bytes 00013fd6
+ 00c4da0c bytes 00013fd6
- 00c4d620 ["INT_ADD", "register:40f0:8", ["const:c4d620:8", "const:4:8"]]
- 00c4d620 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4da48 ["INT_ADD", "register:40f0:8", ["const:c4da48:8", "const:4:8"]]
+ 00c4da48 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4d620 bytes a0310094
+ 00c4da48 bytes 96310094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57b8ebae5c9b2111dd43639bbdcda4eb"></a>

### [`00c4daa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4daa4.md) → [`00c4decc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4decc.md) FUN_00c4decc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4dad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4daa4.md#insn-00c4dad0) · [`00c4daf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4daa4.md#insn-00c4daf4) · [`00c4db20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4daa4.md#insn-00c4db20)
- 新版 `00c4def8`（命令位置の公開資料なし） · `00c4df1c`（命令位置の公開資料なし） · `00c4df48`（命令位置の公開資料なし）

~~~diff
- 00c4dad0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4dad0 ["INT_ADD", "register:40f0:8", ["const:c4dad0:8", "const:4:8"]]
- 00c4dad0 ["CALLIND", null, ["register:0:8"]]
+ 00c4def8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4def8 ["INT_ADD", "register:40f0:8", ["const:c4def8:8", "const:4:8"]]
+ 00c4def8 ["CALLIND", null, ["register:0:8"]]
- 00c4dad0 bytes 00013fd6
+ 00c4def8 bytes 00013fd6
- 00c4daf4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4daf4 ["INT_ADD", "register:40f0:8", ["const:c4daf4:8", "const:4:8"]]
- 00c4daf4 ["CALLIND", null, ["register:0:8"]]
+ 00c4df1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4df1c ["INT_ADD", "register:40f0:8", ["const:c4df1c:8", "const:4:8"]]
+ 00c4df1c ["CALLIND", null, ["register:0:8"]]
- 00c4daf4 bytes 00013fd6
+ 00c4df1c bytes 00013fd6
- 00c4db20 ["INT_ADD", "register:40f0:8", ["const:c4db20:8", "const:4:8"]]
- 00c4db20 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4df48 ["INT_ADD", "register:40f0:8", ["const:c4df48:8", "const:4:8"]]
+ 00c4df48 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4db20 bytes 60300094
+ 00c4df48 bytes 56300094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b99ddc3ba57fe9d5828a008f43931390"></a>

### [`00c4f114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f114.md) → [`00c4f53c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f53c.md) FUN_00c4f53c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4f158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f114.md#insn-00c4f158) · [`00c4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f114.md#insn-00c4f1bc) · [`00c4f200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f114.md#insn-00c4f200)
- 新版 `00c4f580`（命令位置の公開資料なし） · `00c4f5e4`（命令位置の公開資料なし） · `00c4f628`（命令位置の公開資料なし）

~~~diff
- 00c4f158 ["INT_ADD", "register:40f0:8", ["const:c4f158:8", "const:4:8"]]
- 00c4f158 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4f580 ["INT_ADD", "register:40f0:8", ["const:c4f580:8", "const:4:8"]]
+ 00c4f580 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4f158 bytes d22a0094
+ 00c4f580 bytes c82a0094
- 00c4f1bc ["INT_ADD", "register:40f0:8", ["const:c4f1bc:8", "const:4:8"]]
- 00c4f1bc ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4f5e4 ["INT_ADD", "register:40f0:8", ["const:c4f5e4:8", "const:4:8"]]
+ 00c4f5e4 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4f1bc bytes b92a0094
+ 00c4f5e4 bytes af2a0094
- 00c4f200 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4f200 ["INT_ADD", "register:40f0:8", ["const:c4f200:8", "const:4:8"]]
- 00c4f200 ["CALLIND", null, ["register:0:8"]]
+ 00c4f628 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4f628 ["INT_ADD", "register:40f0:8", ["const:c4f628:8", "const:4:8"]]
+ 00c4f628 ["CALLIND", null, ["register:0:8"]]
- 00c4f200 bytes 00013fd6
+ 00c4f628 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-189cee95a9ded14fc4d61d735a7863be"></a>

### [`00c4f38c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f38c.md) → [`00c4f7b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f7b4.md) FUN_00c4f7b4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4f3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f38c.md#insn-00c4f3d0) · [`00c4f438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f38c.md#insn-00c4f438) · [`00c4f460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f38c.md#insn-00c4f460)
- 新版 `00c4f7f8`（命令位置の公開資料なし） · `00c4f860`（命令位置の公開資料なし） · `00c4f888`（命令位置の公開資料なし）

~~~diff
- 00c4f3d0 ["INT_ADD", "register:40f0:8", ["const:c4f3d0:8", "const:4:8"]]
- 00c4f3d0 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4f7f8 ["INT_ADD", "register:40f0:8", ["const:c4f7f8:8", "const:4:8"]]
+ 00c4f7f8 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4f3d0 bytes 342a0094
+ 00c4f7f8 bytes 2a2a0094
- 00c4f438 ["INT_ADD", "register:40f0:8", ["const:c4f438:8", "const:4:8"]]
- 00c4f438 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4f860 ["INT_ADD", "register:40f0:8", ["const:c4f860:8", "const:4:8"]]
+ 00c4f860 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4f438 bytes 1a2a0094
+ 00c4f860 bytes 102a0094
- 00c4f460 ["INT_ADD", "register:40f0:8", ["const:c4f460:8", "const:4:8"]]
- 00c4f460 ["CALL", null, ["callee:00c45144:8"]]
+ 00c4f888 ["INT_ADD", "register:40f0:8", ["const:c4f888:8", "const:4:8"]]
+ 00c4f888 ["CALL", null, ["callee:00c45144:8"]]
- 00c4f460 bytes 2fd6ff97
+ 00c4f888 bytes 2fd6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d9b14f7f6d855b4e7a793aa6846cfef"></a>

### [`00c4f4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f4f4.md) → [`00c4f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f91c.md) FUN_00c4f91c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4f514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f4f4.md#insn-00c4f514) · [`00c4f540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f4f4.md#insn-00c4f540) · [`00c4f574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f4f4.md#insn-00c4f574)
- 新版 `00c4f93c`（命令位置の公開資料なし） · `00c4f968`（命令位置の公開資料なし） · `00c4f99c`（命令位置の公開資料なし）

~~~diff
- 00c4f514 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4f514 ["INT_ADD", "register:40f0:8", ["const:c4f514:8", "const:4:8"]]
- 00c4f514 ["CALLIND", null, ["register:0:8"]]
+ 00c4f93c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4f93c ["INT_ADD", "register:40f0:8", ["const:c4f93c:8", "const:4:8"]]
+ 00c4f93c ["CALLIND", null, ["register:0:8"]]
- 00c4f514 bytes 00013fd6
+ 00c4f93c bytes 00013fd6
- 00c4f540 ["INT_ADD", "register:40f0:8", ["const:c4f540:8", "const:4:8"]]
- 00c4f540 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4f968 ["INT_ADD", "register:40f0:8", ["const:c4f968:8", "const:4:8"]]
+ 00c4f968 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4f540 bytes d8290094
+ 00c4f968 bytes ce290094
- 00c4f574 ["INT_ADD", "register:40f0:8", ["const:c4f574:8", "const:4:8"]]
- 00c4f574 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4f99c ["INT_ADD", "register:40f0:8", ["const:c4f99c:8", "const:4:8"]]
+ 00c4f99c ["CALL", null, ["callee:00c5b140:8"]]
- 00c4f574 bytes f32d0094
+ 00c4f99c bytes e92d0094
~~~


<a id="compare-ff4550e98384faebe4f93571aa348073"></a>

### [`00c4f914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f914.md) → [`00c4fd3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4fd3c.md) FUN_00c4fd3c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4f940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f914.md#insn-00c4f940) · [`00c4f964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f914.md#insn-00c4f964) · [`00c4f990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f914.md#insn-00c4f990)
- 新版 `00c4fd68`（命令位置の公開資料なし） · `00c4fd8c`（命令位置の公開資料なし） · `00c4fdb8`（命令位置の公開資料なし）

~~~diff
- 00c4f940 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4f940 ["INT_ADD", "register:40f0:8", ["const:c4f940:8", "const:4:8"]]
- 00c4f940 ["CALLIND", null, ["register:0:8"]]
+ 00c4fd68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4fd68 ["INT_ADD", "register:40f0:8", ["const:c4fd68:8", "const:4:8"]]
+ 00c4fd68 ["CALLIND", null, ["register:0:8"]]
- 00c4f940 bytes 00013fd6
+ 00c4fd68 bytes 00013fd6
- 00c4f964 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4f964 ["INT_ADD", "register:40f0:8", ["const:c4f964:8", "const:4:8"]]
- 00c4f964 ["CALLIND", null, ["register:0:8"]]
+ 00c4fd8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4fd8c ["INT_ADD", "register:40f0:8", ["const:c4fd8c:8", "const:4:8"]]
+ 00c4fd8c ["CALLIND", null, ["register:0:8"]]
- 00c4f964 bytes 00013fd6
+ 00c4fd8c bytes 00013fd6
- 00c4f990 ["INT_ADD", "register:40f0:8", ["const:c4f990:8", "const:4:8"]]
- 00c4f990 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4fdb8 ["INT_ADD", "register:40f0:8", ["const:c4fdb8:8", "const:4:8"]]
+ 00c4fdb8 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4f990 bytes c4280094
+ 00c4fdb8 bytes ba280094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef7e4c77ff202d6c02c5faf1ae2f9dc8"></a>

### [`00c4fa88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4fa88.md) → [`00c4feb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4feb0.md) FUN_00c4feb0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4fab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4fa88.md#insn-00c4fab4) · [`00c4fad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4fa88.md#insn-00c4fad8) · [`00c4fb04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4fa88.md#insn-00c4fb04)
- 新版 `00c4fedc`（命令位置の公開資料なし） · `00c4ff00`（命令位置の公開資料なし） · `00c4ff2c`（命令位置の公開資料なし）

~~~diff
- 00c4fab4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4fab4 ["INT_ADD", "register:40f0:8", ["const:c4fab4:8", "const:4:8"]]
- 00c4fab4 ["CALLIND", null, ["register:0:8"]]
+ 00c4fedc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4fedc ["INT_ADD", "register:40f0:8", ["const:c4fedc:8", "const:4:8"]]
+ 00c4fedc ["CALLIND", null, ["register:0:8"]]
- 00c4fab4 bytes 00013fd6
+ 00c4fedc bytes 00013fd6
- 00c4fad8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4fad8 ["INT_ADD", "register:40f0:8", ["const:c4fad8:8", "const:4:8"]]
- 00c4fad8 ["CALLIND", null, ["register:0:8"]]
+ 00c4ff00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4ff00 ["INT_ADD", "register:40f0:8", ["const:c4ff00:8", "const:4:8"]]
+ 00c4ff00 ["CALLIND", null, ["register:0:8"]]
- 00c4fad8 bytes 00013fd6
+ 00c4ff00 bytes 00013fd6
- 00c4fb04 ["INT_ADD", "register:40f0:8", ["const:c4fb04:8", "const:4:8"]]
- 00c4fb04 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4ff2c ["INT_ADD", "register:40f0:8", ["const:c4ff2c:8", "const:4:8"]]
+ 00c4ff2c ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4fb04 bytes 67280094
+ 00c4ff2c bytes 5d280094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7280c390c23160ab0dc8ed2c5d57961a"></a>

### [`00c4fe20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4fe20.md) → [`00c50248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50248.md) FUN_00c50248

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4fe74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4fe20.md#insn-00c4fe74) · [`00c4fe90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4fe20.md#insn-00c4fe90) · [`00c4fec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4fe20.md#insn-00c4fec8)
- 新版 `00c5029c`（命令位置の公開資料なし） · `00c502b8`（命令位置の公開資料なし） · `00c502f0`（命令位置の公開資料なし）

~~~diff
- 00c4fe74 ["INT_ADD", "register:40f0:8", ["const:c4fe74:8", "const:4:8"]]
- 00c4fe74 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c5029c ["INT_ADD", "register:40f0:8", ["const:c5029c:8", "const:4:8"]]
+ 00c5029c ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4fe74 bytes 8b270094
+ 00c5029c bytes 81270094
- 00c4fe90 ["INT_ADD", "register:40f0:8", ["const:c4fe90:8", "const:4:8"]]
- 00c4fe90 ["CALL", null, ["callee:00c58000:8"]]
+ 00c502b8 ["INT_ADD", "register:40f0:8", ["const:c502b8:8", "const:4:8"]]
+ 00c502b8 ["CALL", null, ["callee:00c58000:8"]]
- 00c4fe90 bytes 5c1f0094
+ 00c502b8 bytes 521f0094
- 00c4fec8 ["INT_ADD", "register:40f0:8", ["const:c4fec8:8", "const:4:8"]]
- 00c4fec8 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c502f0 ["INT_ADD", "register:40f0:8", ["const:c502f0:8", "const:4:8"]]
+ 00c502f0 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4fec8 bytes 76270094
+ 00c502f0 bytes 6c270094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9621f279df4fa75f8a06428dd3cd1f69"></a>

### [`00c4ff94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4ff94.md) → [`00c503bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c503bc.md) FUN_00c503bc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4ffd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4ff94.md#insn-00c4ffd8) · [`00c50024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4ff94.md#insn-00c50024) · [`00c50068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4ff94.md#insn-00c50068)
- 新版 `00c50400`（命令位置の公開資料なし） · `00c5044c`（命令位置の公開資料なし） · `00c50490`（命令位置の公開資料なし）

~~~diff
- 00c4ffd8 ["INT_ADD", "register:40f0:8", ["const:c4ffd8:8", "const:4:8"]]
- 00c4ffd8 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c50400 ["INT_ADD", "register:40f0:8", ["const:c50400:8", "const:4:8"]]
+ 00c50400 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4ffd8 bytes 32270094
+ 00c50400 bytes 28270094
- 00c50024 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c50024 ["INT_ADD", "register:40f0:8", ["const:c50024:8", "const:4:8"]]
- 00c50024 ["CALLIND", null, ["register:0:8"]]
+ 00c5044c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c5044c ["INT_ADD", "register:40f0:8", ["const:c5044c:8", "const:4:8"]]
+ 00c5044c ["CALLIND", null, ["register:0:8"]]
- 00c50024 bytes 00013fd6
+ 00c5044c bytes 00013fd6
- 00c50068 ["INT_ADD", "register:40f0:8", ["const:c50068:8", "const:4:8"]]
- 00c50068 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c50490 ["INT_ADD", "register:40f0:8", ["const:c50490:8", "const:4:8"]]
+ 00c50490 ["CALL", null, ["callee:00c5b140:8"]]
- 00c50068 bytes 362b0094
+ 00c50490 bytes 2c2b0094
~~~


<a id="compare-ccd67af5c88c903033903bd0927eba6b"></a>

### [`00c5035c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c5035c.md) → [`00c50784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50784.md) FUN_00c50784

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c50384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c5035c.md#insn-00c50384) · [`00c503bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c5035c.md#insn-00c503bc) · [`00c503d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c5035c.md#insn-00c503d8)
- 新版 `00c507ac`（命令位置の公開資料なし） · `00c507e4`（命令位置の公開資料なし） · `00c50800`（命令位置の公開資料なし）

~~~diff
- 00c50384 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c50384 ["INT_ADD", "register:40f0:8", ["const:c50384:8", "const:4:8"]]
- 00c50384 ["CALLIND", null, ["register:0:8"]]
+ 00c507ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c507ac ["INT_ADD", "register:40f0:8", ["const:c507ac:8", "const:4:8"]]
+ 00c507ac ["CALLIND", null, ["register:0:8"]]
- 00c50384 bytes 00013fd6
+ 00c507ac bytes 00013fd6
- 00c503bc ["INT_ADD", "register:40f0:8", ["const:c503bc:8", "const:4:8"]]
- 00c503bc ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c507e4 ["INT_ADD", "register:40f0:8", ["const:c507e4:8", "const:4:8"]]
+ 00c507e4 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c503bc bytes 39260094
+ 00c507e4 bytes 2f260094
- 00c503d8 ["INT_ADD", "register:40f0:8", ["const:c503d8:8", "const:4:8"]]
- 00c503d8 ["CALL", null, ["callee:00c58000:8"]]
+ 00c50800 ["INT_ADD", "register:40f0:8", ["const:c50800:8", "const:4:8"]]
+ 00c50800 ["CALL", null, ["callee:00c58000:8"]]
- 00c503d8 bytes 0a1e0094
+ 00c50800 bytes 001e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c0c8c6ea7b59176a48043f8e2315c18"></a>

### [`00c50678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50678.md) → [`00c50aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50aa0.md) FUN_00c50aa0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c506a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50678.md#insn-00c506a4) · [`00c506c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50678.md#insn-00c506c8) · [`00c506f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50678.md#insn-00c506f4)
- 新版 `00c50acc`（命令位置の公開資料なし） · `00c50af0`（命令位置の公開資料なし） · `00c50b1c`（命令位置の公開資料なし）

~~~diff
- 00c506a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c506a4 ["INT_ADD", "register:40f0:8", ["const:c506a4:8", "const:4:8"]]
- 00c506a4 ["CALLIND", null, ["register:0:8"]]
+ 00c50acc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c50acc ["INT_ADD", "register:40f0:8", ["const:c50acc:8", "const:4:8"]]
+ 00c50acc ["CALLIND", null, ["register:0:8"]]
- 00c506a4 bytes 00013fd6
+ 00c50acc bytes 00013fd6
- 00c506c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c506c8 ["INT_ADD", "register:40f0:8", ["const:c506c8:8", "const:4:8"]]
- 00c506c8 ["CALLIND", null, ["register:0:8"]]
+ 00c50af0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c50af0 ["INT_ADD", "register:40f0:8", ["const:c50af0:8", "const:4:8"]]
+ 00c50af0 ["CALLIND", null, ["register:0:8"]]
- 00c506c8 bytes 00013fd6
+ 00c50af0 bytes 00013fd6
- 00c506f4 ["INT_ADD", "register:40f0:8", ["const:c506f4:8", "const:4:8"]]
- 00c506f4 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c50b1c ["INT_ADD", "register:40f0:8", ["const:c50b1c:8", "const:4:8"]]
+ 00c50b1c ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c506f4 bytes 6b250094
+ 00c50b1c bytes 61250094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d653df9a5d28d3e2659df1d6ab9e525"></a>

### [`00c50b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50b34.md) → [`00c50f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50f5c.md) FUN_00c50f5c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c50b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50b34.md#insn-00c50b58) · [`00c50b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50b34.md#insn-00c50b80) · [`00c50bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50b34.md#insn-00c50bb0)
- 新版 `00c50f80`（命令位置の公開資料なし） · `00c50fa8`（命令位置の公開資料なし） · `00c50fd8`（命令位置の公開資料なし）

~~~diff
- 00c50b58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c50b58 ["INT_ADD", "register:40f0:8", ["const:c50b58:8", "const:4:8"]]
- 00c50b58 ["CALLIND", null, ["register:0:8"]]
+ 00c50f80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c50f80 ["INT_ADD", "register:40f0:8", ["const:c50f80:8", "const:4:8"]]
+ 00c50f80 ["CALLIND", null, ["register:0:8"]]
- 00c50b58 bytes 00013fd6
+ 00c50f80 bytes 00013fd6
- 00c50b80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c50b80 ["INT_ADD", "register:40f0:8", ["const:c50b80:8", "const:4:8"]]
- 00c50b80 ["CALLIND", null, ["register:0:8"]]
+ 00c50fa8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c50fa8 ["INT_ADD", "register:40f0:8", ["const:c50fa8:8", "const:4:8"]]
+ 00c50fa8 ["CALLIND", null, ["register:0:8"]]
- 00c50b80 bytes 00013fd6
+ 00c50fa8 bytes 00013fd6
- 00c50bb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c50bb0 ["INT_ADD", "register:40f0:8", ["const:c50bb0:8", "const:4:8"]]
- 00c50bb0 ["CALLIND", null, ["register:0:8"]]
+ 00c50fd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c50fd8 ["INT_ADD", "register:40f0:8", ["const:c50fd8:8", "const:4:8"]]
+ 00c50fd8 ["CALLIND", null, ["register:0:8"]]
- 00c50bb0 bytes 00013fd6
+ 00c50fd8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-844dac4617bc3516e2c68ebbf2bd77a6"></a>

### [`00c50cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50cf4.md) → [`00c5111c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c5111c.md) FUN_00c5111c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c50d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50cf4.md#insn-00c50d30) · [`00c50d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50cf4.md#insn-00c50d60) · [`00c50d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50cf4.md#insn-00c50d90)
- 新版 `00c51158`（命令位置の公開資料なし） · `00c51188`（命令位置の公開資料なし） · `00c511b8`（命令位置の公開資料なし）

~~~diff
- 00c50d30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c50d30 ["INT_ADD", "register:40f0:8", ["const:c50d30:8", "const:4:8"]]
- 00c50d30 ["CALLIND", null, ["register:0:8"]]
+ 00c51158 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c51158 ["INT_ADD", "register:40f0:8", ["const:c51158:8", "const:4:8"]]
+ 00c51158 ["CALLIND", null, ["register:0:8"]]
- 00c50d30 bytes 00013fd6
+ 00c51158 bytes 00013fd6
- 00c50d60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c50d60 ["INT_ADD", "register:40f0:8", ["const:c50d60:8", "const:4:8"]]
- 00c50d60 ["CALLIND", null, ["register:0:8"]]
+ 00c51188 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c51188 ["INT_ADD", "register:40f0:8", ["const:c51188:8", "const:4:8"]]
+ 00c51188 ["CALLIND", null, ["register:0:8"]]
- 00c50d60 bytes 00013fd6
+ 00c51188 bytes 00013fd6
- 00c50d90 ["INT_ADD", "register:40f0:8", ["const:c50d90:8", "const:4:8"]]
- 00c50d90 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c511b8 ["INT_ADD", "register:40f0:8", ["const:c511b8:8", "const:4:8"]]
+ 00c511b8 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c50d90 bytes c4230094
+ 00c511b8 bytes ba230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ddab2acdac9f0a5f7a36793144d43fb"></a>

### [`00c50de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50de0.md) → [`00c51208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51208.md) FUN_00c51208

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c50e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50de0.md#insn-00c50e34) · [`00c50e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50de0.md#insn-00c50e50) · [`00c50e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50de0.md#insn-00c50e88)
- 新版 `00c5125c`（命令位置の公開資料なし） · `00c51278`（命令位置の公開資料なし） · `00c512b0`（命令位置の公開資料なし）

~~~diff
- 00c50e34 ["INT_ADD", "register:40f0:8", ["const:c50e34:8", "const:4:8"]]
- 00c50e34 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c5125c ["INT_ADD", "register:40f0:8", ["const:c5125c:8", "const:4:8"]]
+ 00c5125c ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c50e34 bytes 9b230094
+ 00c5125c bytes 91230094
- 00c50e50 ["INT_ADD", "register:40f0:8", ["const:c50e50:8", "const:4:8"]]
- 00c50e50 ["CALL", null, ["callee:00c58000:8"]]
+ 00c51278 ["INT_ADD", "register:40f0:8", ["const:c51278:8", "const:4:8"]]
+ 00c51278 ["CALL", null, ["callee:00c58000:8"]]
- 00c50e50 bytes 6c1b0094
+ 00c51278 bytes 621b0094
- 00c50e88 ["INT_ADD", "register:40f0:8", ["const:c50e88:8", "const:4:8"]]
- 00c50e88 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c512b0 ["INT_ADD", "register:40f0:8", ["const:c512b0:8", "const:4:8"]]
+ 00c512b0 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c50e88 bytes 86230094
+ 00c512b0 bytes 7c230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2feeaf234d2ea83d0983f205c3c8c2a2"></a>

### [`00c50f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50f48.md) → [`00c51370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51370.md) FUN_00c51370

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c50fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50f48.md#insn-00c50fd4) · [`00c50ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50f48.md#insn-00c50ffc) · [`00c5102c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50f48.md#insn-00c5102c)
- 新版 `00c513fc`（命令位置の公開資料なし） · `00c51424`（命令位置の公開資料なし） · `00c51454`（命令位置の公開資料なし）

~~~diff
- 00c50fd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c50fd4 ["INT_ADD", "register:40f0:8", ["const:c50fd4:8", "const:4:8"]]
- 00c50fd4 ["CALLIND", null, ["register:0:8"]]
+ 00c513fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c513fc ["INT_ADD", "register:40f0:8", ["const:c513fc:8", "const:4:8"]]
+ 00c513fc ["CALLIND", null, ["register:0:8"]]
- 00c50fd4 bytes 00013fd6
+ 00c513fc bytes 00013fd6
- 00c50ffc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c50ffc ["INT_ADD", "register:40f0:8", ["const:c50ffc:8", "const:4:8"]]
- 00c50ffc ["CALLIND", null, ["register:0:8"]]
+ 00c51424 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c51424 ["INT_ADD", "register:40f0:8", ["const:c51424:8", "const:4:8"]]
+ 00c51424 ["CALLIND", null, ["register:0:8"]]
- 00c50ffc bytes 00013fd6
+ 00c51424 bytes 00013fd6
- 00c5102c ["INT_ADD", "register:40f0:8", ["const:c5102c:8", "const:4:8"]]
- 00c5102c ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c51454 ["INT_ADD", "register:40f0:8", ["const:c51454:8", "const:4:8"]]
+ 00c51454 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c5102c bytes 1d230094
+ 00c51454 bytes 13230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8b622ed1029fe1b61c632750079ef4e"></a>

### [`00c51288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51288.md) → [`00c516b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c516b0.md) FUN_00c516b0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51288.md#insn-00c51324) · [`00c51354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51288.md#insn-00c51354) · [`00c51384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51288.md#insn-00c51384)
- 新版 `00c5174c`（命令位置の公開資料なし） · `00c5177c`（命令位置の公開資料なし） · `00c517ac`（命令位置の公開資料なし）

~~~diff
- 00c51324 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c51324 ["INT_ADD", "register:40f0:8", ["const:c51324:8", "const:4:8"]]
- 00c51324 ["CALLIND", null, ["register:0:8"]]
+ 00c5174c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c5174c ["INT_ADD", "register:40f0:8", ["const:c5174c:8", "const:4:8"]]
+ 00c5174c ["CALLIND", null, ["register:0:8"]]
- 00c51324 bytes 00013fd6
+ 00c5174c bytes 00013fd6
- 00c51354 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c51354 ["INT_ADD", "register:40f0:8", ["const:c51354:8", "const:4:8"]]
- 00c51354 ["CALLIND", null, ["register:0:8"]]
+ 00c5177c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c5177c ["INT_ADD", "register:40f0:8", ["const:c5177c:8", "const:4:8"]]
+ 00c5177c ["CALLIND", null, ["register:0:8"]]
- 00c51354 bytes 00013fd6
+ 00c5177c bytes 00013fd6
- 00c51384 ["INT_ADD", "register:40f0:8", ["const:c51384:8", "const:4:8"]]
- 00c51384 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c517ac ["INT_ADD", "register:40f0:8", ["const:c517ac:8", "const:4:8"]]
+ 00c517ac ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c51384 bytes 47220094
+ 00c517ac bytes 3d220094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-723f409d1a3240ac912c3d61d163fde2"></a>

### [`00c51624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51624.md) → [`00c51a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51a4c.md) FUN_00c51a4c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5174c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c5174c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c51b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51b74.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51624.md#insn-00c51650) · [`00c51680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51624.md#insn-00c51680) · [`00c516b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51624.md#insn-00c516b0)
- 新版 `00c51a78`（命令位置の公開資料なし） · `00c51aa8`（命令位置の公開資料なし） · `00c51ad8`（命令位置の公開資料なし）

~~~diff
- 00c51650 ["INT_ADD", "register:40f0:8", ["const:c51650:8", "const:4:8"]]
- 00c51650 ["CALL", null, ["callee:00c51b74:8"]]
+ 00c51a78 ["INT_ADD", "register:40f0:8", ["const:c51a78:8", "const:4:8"]]
+ 00c51a78 ["CALL", null, ["callee:00c51b74:8"]]
- 00c51650 bytes 3f000094
+ 00c51a78 bytes 3f000094
- 00c51680 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c51680 ["INT_ADD", "register:40f0:8", ["const:c51680:8", "const:4:8"]]
- 00c51680 ["CALLIND", null, ["register:0:8"]]
+ 00c51aa8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c51aa8 ["INT_ADD", "register:40f0:8", ["const:c51aa8:8", "const:4:8"]]
+ 00c51aa8 ["CALLIND", null, ["register:0:8"]]
- 00c51680 bytes 00013fd6
+ 00c51aa8 bytes 00013fd6
- 00c516b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c516b0 ["INT_ADD", "register:40f0:8", ["const:c516b0:8", "const:4:8"]]
- 00c516b0 ["CALLIND", null, ["register:0:8"]]
+ 00c51ad8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c51ad8 ["INT_ADD", "register:40f0:8", ["const:c51ad8:8", "const:4:8"]]
+ 00c51ad8 ["CALLIND", null, ["register:0:8"]]
- 00c516b0 bytes 00013fd6
+ 00c51ad8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bfab16c734f53766ddff6f10f72a7cb"></a>

### [`00c518f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c518f8.md) → [`00c51d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51d20.md) _ZnwmRKSt9nothrow_t

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a450.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00c5a850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a850.md) · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c518f8.md#insn-00c51904)
- 新版 `00c51d2c`（命令位置の公開資料なし）

~~~diff
- 00c51904 ["INT_ADD", "register:40f0:8", ["const:c51904:8", "const:4:8"]]
- 00c51904 ["CALL", null, ["callee:00c57e90:8"]]
+ 00c51d2c ["INT_ADD", "register:40f0:8", ["const:c51d2c:8", "const:4:8"]]
+ 00c51d2c ["CALL", null, ["callee:00c57e90:8"]]
- 00c51904 bytes 63180094
+ 00c51d2c bytes 59180094
~~~


<a id="compare-1471bc41fb543ea997adabc2621cbfc8"></a>

### [`00c51928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51928.md) → [`00c51d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51d50.md) _ZnamRKSt9nothrow_t

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ba50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5be50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51928.md#insn-00c51934)
- 新版 `00c51d5c`（命令位置の公開資料なし）

~~~diff
- 00c51934 ["INT_ADD", "register:40f0:8", ["const:c51934:8", "const:4:8"]]
- 00c51934 ["CALL", null, ["callee:00c5be50:8"]]
+ 00c51d5c ["INT_ADD", "register:40f0:8", ["const:c51d5c:8", "const:4:8"]]
+ 00c51d5c ["CALL", null, ["callee:00c5be50:8"]]
- 00c51934 bytes 47280094
+ 00c51d5c bytes 3d280094
~~~


<a id="compare-891abc39d485dfb328ab380aa29d3165"></a>

### [`00c51988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51988.md) → [`00c51db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51db0.md) _ZnwmSt11align_val_tRKSt9nothrow_t

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5eac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5eec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eec0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51988.md#insn-00c51994)
- 新版 `00c51dbc`（命令位置の公開資料なし）

~~~diff
- 00c51994 ["INT_ADD", "register:40f0:8", ["const:c51994:8", "const:4:8"]]
- 00c51994 ["CALL", null, ["callee:00c5eec0:8"]]
+ 00c51dbc ["INT_ADD", "register:40f0:8", ["const:c51dbc:8", "const:4:8"]]
+ 00c51dbc ["CALL", null, ["callee:00c5eec0:8"]]
- 00c51994 bytes 4b340094
+ 00c51dbc bytes 41340094
~~~


<a id="compare-ff8ccac55890803e2ecbfec647541057"></a>

### [`00c519b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c519b8.md) → [`00c51de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51de0.md) _ZnamSt11align_val_tRKSt9nothrow_t

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5eae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5eee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c519c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c519b8.md#insn-00c519c4)
- 新版 `00c51dec`（命令位置の公開資料なし）

~~~diff
- 00c519c4 ["INT_ADD", "register:40f0:8", ["const:c519c4:8", "const:4:8"]]
- 00c519c4 ["CALL", null, ["callee:00c5eee0:8"]]
+ 00c51dec ["INT_ADD", "register:40f0:8", ["const:c51dec:8", "const:4:8"]]
+ 00c51dec ["CALL", null, ["callee:00c5eee0:8"]]
- 00c519c4 bytes 47340094
+ 00c51dec bytes 3d340094
~~~


<a id="compare-f93db462e824a83da98b9da52416aa72"></a>

### [`00c51a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51a50.md) → [`00c51e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51e78.md) __cxa_allocate_exception

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) · 呼出先 3件 [`00c5221c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c5221c.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 1件 [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) · 呼出先 3件 [`00c52644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52644.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51a50.md#insn-00c51a68) · [`00c51a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51a50.md#insn-00c51a80) · [`00c51a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51a50.md#insn-00c51a98)
- 新版 `00c51e90`（命令位置の公開資料なし） · `00c51ea8`（命令位置の公開資料なし） · `00c51ec0`（命令位置の公開資料なし）

~~~diff
- 00c51a68 ["INT_ADD", "register:40f0:8", ["const:c51a68:8", "const:4:8"]]
- 00c51a68 ["CALL", null, ["callee:00c52644:8"]]
+ 00c51e90 ["INT_ADD", "register:40f0:8", ["const:c51e90:8", "const:4:8"]]
+ 00c51e90 ["CALL", null, ["callee:00c52644:8"]]
- 00c51a68 bytes ed010094
+ 00c51e90 bytes ed010094
- 00c51a80 ["INT_ADD", "register:40f0:8", ["const:c51a80:8", "const:4:8"]]
- 00c51a80 ["CALL", null, ["callee:00c58090:8"]]
+ 00c51ea8 ["INT_ADD", "register:40f0:8", ["const:c51ea8:8", "const:4:8"]]
+ 00c51ea8 ["CALL", null, ["callee:00c58090:8"]]
- 00c51a80 bytes 84180094
+ 00c51ea8 bytes 7a180094
- 00c51a98 ["INT_ADD", "register:40f0:8", ["const:c51a98:8", "const:4:8"]]
- 00c51a98 ["CALL", null, ["callee:00c58020:8"]]
+ 00c51ec0 ["INT_ADD", "register:40f0:8", ["const:c51ec0:8", "const:4:8"]]
+ 00c51ec0 ["CALL", null, ["callee:00c58020:8"]]
- 00c51a98 bytes 62180094
+ 00c51ec0 bytes 58180094
~~~


<a id="compare-3c8b48954579c2e7ff48f0e49d55b4e2"></a>

### [`00c51aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51aa0.md) → [`00c51ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51ec8.md) __cxa_begin_catch

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c57c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c10.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c5e990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e990.md)
- 新版 呼出元 1件 [`00c58010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58010.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5ed90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51aa0.md#insn-00c51ab4) · [`00c51b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51aa0.md#insn-00c51b34)
- 新版 `00c51edc`（命令位置の公開資料なし） · `00c51f5c`（命令位置の公開資料なし）

~~~diff
- 00c51ab4 ["INT_ADD", "register:40f0:8", ["const:c51ab4:8", "const:4:8"]]
- 00c51ab4 ["CALL", null, ["callee:00c5ed90:8"]]
+ 00c51edc ["INT_ADD", "register:40f0:8", ["const:c51edc:8", "const:4:8"]]
+ 00c51edc ["CALL", null, ["callee:00c5ed90:8"]]
- 00c51ab4 bytes b7330094
+ 00c51edc bytes ad330094
- 00c51b34 ["INT_ADD", "register:40f0:8", ["const:c51b34:8", "const:4:8"]]
- 00c51b34 ["CALL", null, ["callee:00c58020:8"]]
+ 00c51f5c ["INT_ADD", "register:40f0:8", ["const:c51f5c:8", "const:4:8"]]
+ 00c51f5c ["CALL", null, ["callee:00c58020:8"]]
- 00c51b34 bytes 3b180094
+ 00c51f5c bytes 31180094
~~~


<a id="compare-901eb52e6135ee223a617700c0e267a9"></a>

### [`00c51c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51c38.md) → [`00c52060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52060.md) __cxa_allocate_dependent_exception

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5221c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c5221c.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c52644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52644.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51c38.md#insn-00c51c48) · [`00c51c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51c38.md#insn-00c51c70)
- 新版 `00c52070`（命令位置の公開資料なし） · `00c52098`（命令位置の公開資料なし）

~~~diff
- 00c51c48 ["INT_ADD", "register:40f0:8", ["const:c51c48:8", "const:4:8"]]
- 00c51c48 ["CALL", null, ["callee:00c52644:8"]]
+ 00c52070 ["INT_ADD", "register:40f0:8", ["const:c52070:8", "const:4:8"]]
+ 00c52070 ["CALL", null, ["callee:00c52644:8"]]
- 00c51c48 bytes 75010094
+ 00c52070 bytes 75010094
- 00c51c70 ["INT_ADD", "register:40f0:8", ["const:c51c70:8", "const:4:8"]]
- 00c51c70 ["CALL", null, ["callee:00c58020:8"]]
+ 00c52098 ["INT_ADD", "register:40f0:8", ["const:c52098:8", "const:4:8"]]
+ 00c52098 ["CALL", null, ["callee:00c58020:8"]]
- 00c51c70 bytes ec170094
+ 00c52098 bytes e2170094
~~~


<a id="compare-14cf69ecb911c0c7b543b59ba5deeb07"></a>

### [`00c51c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51c7c.md) → [`00c520a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c520a4.md) __cxa_throw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) · 呼出先 4件 [`00c51cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51cd8.md) [`00c53910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53910.md) [`00c57f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f30.md) [`00c5e990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e990.md)
- 新版 呼出元 1件 [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) · 呼出先 4件 [`00c52100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52100.md) [`00c53d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d30.md) [`00c58330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58330.md) [`00c5ed90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51c7c.md#insn-00c51c9c) · [`00c51cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51c7c.md#insn-00c51cb8) · [`00c51ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51c7c.md#insn-00c51ccc)
- 新版 `00c520c4`（命令位置の公開資料なし） · `00c520e0`（命令位置の公開資料なし） · `00c520f4`（命令位置の公開資料なし）

~~~diff
- 00c51c9c ["INT_ADD", "register:40f0:8", ["const:c51c9c:8", "const:4:8"]]
- 00c51c9c ["CALL", null, ["callee:00c5ed90:8"]]
+ 00c520c4 ["INT_ADD", "register:40f0:8", ["const:c520c4:8", "const:4:8"]]
+ 00c520c4 ["CALL", null, ["callee:00c5ed90:8"]]
- 00c51c9c bytes 3d330094
+ 00c520c4 bytes 33330094
- 00c51cb8 ["INT_ADD", "register:40f0:8", ["const:c51cb8:8", "const:4:8"]]
- 00c51cb8 ["CALL", null, ["callee:00c58330:8"]]
+ 00c520e0 ["INT_ADD", "register:40f0:8", ["const:c520e0:8", "const:4:8"]]
+ 00c520e0 ["CALL", null, ["callee:00c58330:8"]]
- 00c51cb8 bytes 9e180094
+ 00c520e0 bytes 94180094
- 00c51ccc ["INT_ADD", "register:40f0:8", ["const:c51ccc:8", "const:4:8"]]
- 00c51ccc ["CALL", null, ["callee:00c53d30:8"]]
+ 00c520f4 ["INT_ADD", "register:40f0:8", ["const:c520f4:8", "const:4:8"]]
+ 00c520f4 ["CALL", null, ["callee:00c53d30:8"]]
- 00c51ccc bytes 11070094
+ 00c520f4 bytes 0f070094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-026c5f3f3bc8d2fac33d5b48385b8110"></a>

### [`00c51cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51cd8.md) → [`00c52100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52100.md) FUN_00c52100

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c51c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51c7c.md) · 呼出先 2件 [`00c374b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374b8.md) [`00c57c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c10.md)
- 新版 呼出元 1件 [`00c520a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c520a4.md) · 呼出先 2件 [`00c378e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378e0.md) [`00c58010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51cd8.md#insn-00c51cf0) · [`00c51cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51cd8.md#insn-00c51cf8)
- 新版 `00c52118`（命令位置の公開資料なし） · `00c52120`（命令位置の公開資料なし）

~~~diff
- 00c51cf0 ["INT_ADD", "register:40f0:8", ["const:c51cf0:8", "const:4:8"]]
- 00c51cf0 ["CALL", null, ["callee:00c58010:8"]]
+ 00c52118 ["INT_ADD", "register:40f0:8", ["const:c52118:8", "const:4:8"]]
+ 00c52118 ["CALL", null, ["callee:00c58010:8"]]
- 00c51cf0 bytes c8170094
+ 00c52118 bytes be170094
- 00c51cf8 ["INT_ADD", "register:40f0:8", ["const:c51cf8:8", "const:4:8"]]
- 00c51cf8 ["CALL", null, ["callee:00c378e0:8"]]
+ 00c52120 ["INT_ADD", "register:40f0:8", ["const:c52120:8", "const:4:8"]]
+ 00c52120 ["CALL", null, ["callee:00c378e0:8"]]
- 00c51cf8 bytes f095ff97
+ 00c52120 bytes f095ff97
~~~


<a id="compare-6cf6711f670e53d9466fd99d5dd6f454"></a>

### [`00c51e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51e50.md) → [`00c52278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52278.md) __cxa_current_exception_type

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e9a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5eda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eda0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51e50.md#insn-00c51e5c)
- 新版 `00c52284`（命令位置の公開資料なし）

~~~diff
- 00c51e5c ["INT_ADD", "register:40f0:8", ["const:c51e5c:8", "const:4:8"]]
- 00c51e5c ["CALL", null, ["callee:00c5eda0:8"]]
+ 00c52284 ["INT_ADD", "register:40f0:8", ["const:c52284:8", "const:4:8"]]
+ 00c52284 ["CALL", null, ["callee:00c5eda0:8"]]
- 00c51e5c bytes d1320094
+ 00c52284 bytes c7320094
~~~


<a id="compare-54aa260f56a37987b07bb728e35ca4af"></a>

### [`00c51ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51ea0.md) → [`00c522c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c522c8.md) __cxa_rethrow

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58100.md) · 呼出先 5件 [`00440bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00c374b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374b8.md) [`00c53910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53910.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c5e990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e990.md)
- 新版 呼出元 1件 [`00c58500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58500.md) · 呼出先 5件 [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00c378e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378e0.md) [`00c53d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d30.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5ed90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51ea0.md#insn-00c51eb4) · [`00c51ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51ea0.md#insn-00c51ec0) · [`00c51f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51ea0.md#insn-00c51f0c)
- 新版 `00c522dc`（命令位置の公開資料なし） · `00c522e8`（命令位置の公開資料なし） · `00c52334`（命令位置の公開資料なし）

~~~diff
- 00c51eb4 ["INT_ADD", "register:40f0:8", ["const:c51eb4:8", "const:4:8"]]
- 00c51eb4 ["CALL", null, ["callee:00c5ed90:8"]]
+ 00c522dc ["INT_ADD", "register:40f0:8", ["const:c522dc:8", "const:4:8"]]
+ 00c522dc ["CALL", null, ["callee:00c5ed90:8"]]
- 00c51eb4 bytes b7320094
+ 00c522dc bytes ad320094
- 00c51ec0 ["INT_ADD", "register:40f0:8", ["const:c51ec0:8", "const:4:8"]]
- 00c51ec0 ["CALL", null, ["callee:00c58020:8"]]
+ 00c522e8 ["INT_ADD", "register:40f0:8", ["const:c522e8:8", "const:4:8"]]
+ 00c522e8 ["CALL", null, ["callee:00c58020:8"]]
- 00c51ec0 bytes 58170094
+ 00c522e8 bytes 4e170094
- 00c51f0c ["INT_ADD", "register:40f0:8", ["const:c51f0c:8", "const:4:8"]]
- 00c51f0c ["CALL", null, ["callee:00c53d30:8"]]
+ 00c52334 ["INT_ADD", "register:40f0:8", ["const:c52334:8", "const:4:8"]]
+ 00c52334 ["CALL", null, ["callee:00c53d30:8"]]
- 00c51f0c bytes 81060094
+ 00c52334 bytes 7f060094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6847cefbb3b74c22e888d2fcdb20f8e6"></a>

### [`00c51f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51f84.md) → [`00c523ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c523ac.md) __cxa_increment_exception_refcount

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5db20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db20.md) · 呼出先 1件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c5df20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df20.md) · 呼出先 1件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51f84.md#insn-00c51fa0)
- 新版 `00c523c8`（命令位置の公開資料なし）

~~~diff
- 00c51fa0 ["INT_ADD", "register:40f0:8", ["const:c51fa0:8", "const:4:8"]]
- 00c51fa0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00c523c8 ["INT_ADD", "register:40f0:8", ["const:c523c8:8", "const:4:8"]]
+ 00c523c8 ["CALL", null, ["callee:00c53d00:8"]]
- 00c51fa0 bytes 50060094
+ 00c523c8 bytes 4e060094
~~~


<a id="compare-0b889e0687d93180bf8ccf9ff0a5953f"></a>

### [`00c51fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51fb0.md) → [`00c523d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c523d8.md) __cxa_current_primary_exception

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5db40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db40.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5e9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e9a0.md)
- 新版 呼出元 1件 [`00c5df40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df40.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5eda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eda0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51fb0.md#insn-00c51fc0) · [`00c5200c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51fb0.md#insn-00c5200c)
- 新版 `00c523e8`（命令位置の公開資料なし） · `00c52434`（命令位置の公開資料なし）

~~~diff
- 00c51fc0 ["INT_ADD", "register:40f0:8", ["const:c51fc0:8", "const:4:8"]]
- 00c51fc0 ["CALL", null, ["callee:00c5eda0:8"]]
+ 00c523e8 ["INT_ADD", "register:40f0:8", ["const:c523e8:8", "const:4:8"]]
+ 00c523e8 ["CALL", null, ["callee:00c5eda0:8"]]
- 00c51fc0 bytes 78320094
+ 00c523e8 bytes 6e320094
- 00c5200c ["INT_ADD", "register:40f0:8", ["const:c5200c:8", "const:4:8"]]
- 00c5200c ["CALL", null, ["callee:00c53d00:8"]]
+ 00c52434 ["INT_ADD", "register:40f0:8", ["const:c52434:8", "const:4:8"]]
+ 00c52434 ["CALL", null, ["callee:00c53d00:8"]]
- 00c5200c bytes 35060094
+ 00c52434 bytes 33060094
~~~


<a id="compare-12f690f49b148e3c5a0c2e21a085a0d5"></a>

### [`00c521c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c521c4.md) → [`00c525ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c525ec.md) __cxa_uncaught_exception

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e9a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5eda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eda0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c521d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c521c4.md#insn-00c521d0)
- 新版 `00c525f8`（命令位置の公開資料なし）

~~~diff
- 00c521d0 ["INT_ADD", "register:40f0:8", ["const:c521d0:8", "const:4:8"]]
- 00c521d0 ["CALL", null, ["callee:00c5eda0:8"]]
+ 00c525f8 ["INT_ADD", "register:40f0:8", ["const:c525f8:8", "const:4:8"]]
+ 00c525f8 ["CALL", null, ["callee:00c5eda0:8"]]
- 00c521d0 bytes f4310094
+ 00c525f8 bytes ea310094
~~~


<a id="compare-4f7aa15426a01afcfb6c5f6150364745"></a>

### [`00c521f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c521f4.md) → [`00c5261c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c5261c.md) __cxa_uncaught_exceptions

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5db00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db00.md) · 呼出先 1件 [`00c5e9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e9a0.md)
- 新版 呼出元 1件 [`00c5df00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df00.md) · 呼出先 1件 [`00c5eda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eda0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c52200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c521f4.md#insn-00c52200)
- 新版 `00c52628`（命令位置の公開資料なし）

~~~diff
- 00c52200 ["INT_ADD", "register:40f0:8", ["const:c52200:8", "const:4:8"]]
- 00c52200 ["CALL", null, ["callee:00c5eda0:8"]]
+ 00c52628 ["INT_ADD", "register:40f0:8", ["const:c52628:8", "const:4:8"]]
+ 00c52628 ["CALL", null, ["callee:00c5eda0:8"]]
- 00c52200 bytes e8310094
+ 00c52628 bytes de310094
~~~


<a id="compare-ef51bd158bc2efb0a485ba43ff12860e"></a>

### [`00c5221c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c5221c.md) → [`00c52644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52644.md) FUN_00c52644

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00c51a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51a50.md) [`00c51c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51c38.md) [`00c52030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52030.md) · 呼出先 2件 [`00c52268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52268.md) [`00c5ead0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ead0.md)
- 新版 呼出元 3件 [`00c51e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51e78.md) [`00c52060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52060.md) [`00c52458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52458.md) · 呼出先 2件 [`00c52690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52690.md) [`00c5eed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eed0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c52244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c5221c.md#insn-00c52244) · [`00c52254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c5221c.md#insn-00c52254)
- 新版 `00c5266c`（命令位置の公開資料なし） · `00c5267c`（命令位置の公開資料なし）

~~~diff
- 00c52244 ["INT_ADD", "register:40f0:8", ["const:c52244:8", "const:4:8"]]
- 00c52244 ["CALL", null, ["callee:00c5eed0:8"]]
+ 00c5266c ["INT_ADD", "register:40f0:8", ["const:c5266c:8", "const:4:8"]]
+ 00c5266c ["CALL", null, ["callee:00c5eed0:8"]]
- 00c52244 bytes 23320094
+ 00c5266c bytes 19320094
- 00c52254 ["INT_ADD", "register:40f0:8", ["const:c52254:8", "const:4:8"]]
- 00c52254 ["CALL", null, ["callee:00c52690:8"]]
+ 00c5267c ["INT_ADD", "register:40f0:8", ["const:c5267c:8", "const:4:8"]]
+ 00c5267c ["CALL", null, ["callee:00c52690:8"]]
- 00c52254 bytes 05000094
+ 00c5267c bytes 05000094
~~~


<a id="compare-5bad0ba6a76199dd87cd658dc1145243"></a>

### [`00c52cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52cd8.md) → [`00c53100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53100.md) FUN_00c53100

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00c52520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52520.md) [`00c52abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52abc.md) [`00c52e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52e80.md) · 呼出先 1件 [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 3件 [`00c52948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52948.md) [`00c52ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52ee4.md) [`00c532a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c532a8.md) · 呼出先 1件 [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c52e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52cd8.md#insn-00c52e78) · [`00c52e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52cd8.md#insn-00c52e7c)
- 新版 `00c532a0`（命令位置の公開資料なし） · `00c532a4`（命令位置の公開資料なし）

~~~diff
- 00c52e78 ["INT_ADD", "register:40f0:8", ["const:c52e78:8", "const:4:8"]]
- 00c52e78 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c532a0 ["INT_ADD", "register:40f0:8", ["const:c532a0:8", "const:4:8"]]
+ 00c532a0 ["CALL", null, ["callee:00c5b140:8"]]
- 00c52e78 bytes b21f0094
+ 00c532a0 bytes a81f0094
- 00c52e7c ["INT_ADD", "register:40f0:8", ["const:c52e7c:8", "const:4:8"]]
- 00c52e7c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c532a4 ["INT_ADD", "register:40f0:8", ["const:c532a4:8", "const:4:8"]]
+ 00c532a4 ["CALL", null, ["callee:00c5b140:8"]]
- 00c52e7c bytes b11f0094
+ 00c532a4 bytes a71f0094
~~~


<a id="compare-8a8337b1de84171ed6a88935f1fd0850"></a>

### [`00c53910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53910.md) → [`00c53d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d30.md) FUN_00c53d30

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00c51c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51c7c.md) [`00c51ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51ea0.md) [`00c52030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52030.md) · 呼出先 6件 [`00c53a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53a08.md) [`00c53d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d80.md) [`00c53e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53e28.md) [`00c53f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53f90.md) [`00c53fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53fb8.md)
- 新版 呼出元 3件 [`00c520a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c520a4.md) [`00c522c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c522c8.md) [`00c52458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52458.md) · 呼出先 6件 [`00c53e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53e28.md) [`00c541a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c541a0.md) [`00c54248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54248.md) [`00c543b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c543b0.md) [`00c543d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c543d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c5392c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53910.md#insn-00c5392c) · [`00c5393c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53910.md#insn-00c5393c) · [`00c53944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53910.md#insn-00c53944)
- 新版 `00c53d4c`（命令位置の公開資料なし） · `00c53d5c`（命令位置の公開資料なし） · `00c53d64`（命令位置の公開資料なし）

~~~diff
- 00c5392c ["INT_ADD", "register:40f0:8", ["const:c5392c:8", "const:4:8"]]
- 00c5392c ["CALL", null, ["callee:00c57c48:8"]]
+ 00c53d4c ["INT_ADD", "register:40f0:8", ["const:c53d4c:8", "const:4:8"]]
+ 00c53d4c ["CALL", null, ["callee:00c57c48:8"]]
- 00c5392c bytes bf0f0094
+ 00c53d4c bytes bf0f0094
- 00c5393c ["INT_ADD", "register:40f0:8", ["const:c5393c:8", "const:4:8"]]
- 00c5393c ["CALL", null, ["callee:00c541a0:8"]]
+ 00c53d5c ["INT_ADD", "register:40f0:8", ["const:c53d5c:8", "const:4:8"]]
+ 00c53d5c ["CALL", null, ["callee:00c541a0:8"]]
- 00c5393c bytes 11010094
+ 00c53d5c bytes 11010094
- 00c53944 ["INT_ADD", "register:40f0:8", ["const:c53944:8", "const:4:8"]]
- 00c53944 ["CALL", null, ["callee:00c543b0:8"]]
+ 00c53d64 ["INT_ADD", "register:40f0:8", ["const:c53d64:8", "const:4:8"]]
+ 00c53d64 ["CALL", null, ["callee:00c543b0:8"]]
- 00c53944 bytes 93010094
+ 00c53d64 bytes 93010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7164ad5c869deee6d30aa45e83cfc4d7"></a>

### [`00c53bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53bc0.md) → [`00c53fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53fe0.md) FUN_00c53fe0

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) · 呼出先 4件 [`00c53d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d80.md) [`00c53fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53fa4.md) [`00c53fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53fb8.md) [`00c53ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53ff8.md)
- 新版 呼出元 1件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) · 呼出先 4件 [`00c541a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c541a0.md) [`00c543c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c543c4.md) [`00c543d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c543d8.md) [`00c54418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54418.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c53bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53bc0.md#insn-00c53bf0) · [`00c53bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53bc0.md#insn-00c53bf8) · [`00c53c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53bc0.md#insn-00c53c1c)
- 新版 `00c54010`（命令位置の公開資料なし） · `00c54018`（命令位置の公開資料なし） · `00c5403c`（命令位置の公開資料なし）

~~~diff
- 00c53bf0 ["INT_ADD", "register:40f0:8", ["const:c53bf0:8", "const:4:8"]]
- 00c53bf0 ["CALL", null, ["callee:00c541a0:8"]]
+ 00c54010 ["INT_ADD", "register:40f0:8", ["const:c54010:8", "const:4:8"]]
+ 00c54010 ["CALL", null, ["callee:00c541a0:8"]]
- 00c53bf0 bytes 64000094
+ 00c54010 bytes 64000094
- 00c53bf8 ["INT_ADD", "register:40f0:8", ["const:c53bf8:8", "const:4:8"]]
- 00c53bf8 ["CALL", null, ["callee:00c543c4:8"]]
+ 00c54018 ["INT_ADD", "register:40f0:8", ["const:c54018:8", "const:4:8"]]
+ 00c54018 ["CALL", null, ["callee:00c543c4:8"]]
- 00c53bf8 bytes eb000094
+ 00c54018 bytes eb000094
- 00c53c1c ["COPY", "register:0:8", ["register:4098:8"]]
- 00c53c1c ["INT_ADD", "register:40f0:8", ["const:c53c1c:8", "const:4:8"]]
- 00c53c1c ["CALLIND", null, ["register:0:8"]]
+ 00c5403c ["COPY", "register:0:8", ["register:4098:8"]]
+ 00c5403c ["INT_ADD", "register:40f0:8", ["const:c5403c:8", "const:4:8"]]
+ 00c5403c ["CALLIND", null, ["register:0:8"]]
- 00c53c1c bytes 60023fd6
+ 00c5403c bytes 60023fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-469a6b1fb42702d88113d4e7c70100c4"></a>

### [`00c53cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53cb4.md) → [`00c540d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c540d4.md) FUN_00c540d4

採用 · 移動量 `+0x420` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c52520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52520.md) · 呼出先 1件 [`00c53fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53fb8.md)
- 新版 呼出元 1件 [`00c52948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52948.md) · 呼出先 1件 [`00c543d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c543d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c53cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53cb4.md#insn-00c53cc8)
- 新版 `00c540e8`（命令位置の公開資料なし）

~~~diff
- 00c53cc8 ["INT_ADD", "register:40f0:8", ["const:c53cc8:8", "const:4:8"]]
- 00c53cc8 ["CALL", null, ["callee:00c543d8:8"]]
+ 00c540e8 ["INT_ADD", "register:40f0:8", ["const:c540e8:8", "const:4:8"]]
+ 00c540e8 ["CALL", null, ["callee:00c543d8:8"]]
- 00c53cc8 bytes bc000094
+ 00c540e8 bytes bc000094
~~~


<a id="compare-079b48f061a745bbb21691aa8b89eeb4"></a>

### [`00c53ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53ce8.md) → [`00c54108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54108.md) FUN_00c54108

採用 · 移動量 `+0x420` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c52520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52520.md) · 呼出先 1件 [`00c53fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53fb8.md)
- 新版 呼出元 1件 [`00c52948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52948.md) · 呼出先 1件 [`00c543d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c543d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c53cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53ce8.md#insn-00c53cfc)
- 新版 `00c5411c`（命令位置の公開資料なし）

~~~diff
- 00c53cfc ["INT_ADD", "register:40f0:8", ["const:c53cfc:8", "const:4:8"]]
- 00c53cfc ["CALL", null, ["callee:00c543d8:8"]]
+ 00c5411c ["INT_ADD", "register:40f0:8", ["const:c5411c:8", "const:4:8"]]
+ 00c5411c ["CALL", null, ["callee:00c543d8:8"]]
- 00c53cfc bytes af000094
+ 00c5411c bytes af000094
~~~


<a id="compare-16d4f4c643bfab819bc1e7c59d659964"></a>

### [`00c53d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d40.md) → [`00c54160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54160.md) FUN_00c54160

採用 · 移動量 `+0x420` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c52520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52520.md) · 呼出先 1件 [`00c53e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53e28.md)
- 新版 呼出元 1件 [`00c52948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52948.md) · 呼出先 1件 [`00c54248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54248.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c53d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d40.md#insn-00c53d58)
- 新版 `00c54178`（命令位置の公開資料なし）

~~~diff
- 00c53d58 ["INT_ADD", "register:40f0:8", ["const:c53d58:8", "const:4:8"]]
- 00c53d58 ["CALL", null, ["callee:00c54248:8"]]
+ 00c54178 ["INT_ADD", "register:40f0:8", ["const:c54178:8", "const:4:8"]]
+ 00c54178 ["CALL", null, ["callee:00c54248:8"]]
- 00c53d58 bytes 34000094
+ 00c54178 bytes 34000094
~~~


<a id="compare-0b4668122ce7d4b059735fc9b73c922d"></a>

### [`00c53e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53e28.md) → [`00c54248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54248.md) FUN_00c54248

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00c53910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53910.md) [`00c53a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53a08.md) [`00c53d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d40.md) · 呼出先 0件 
- 新版 呼出元 3件 [`00c53d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d30.md) [`00c53e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53e28.md) [`00c54160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54160.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c53e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53e28.md#insn-00c53e50) · [`00c53e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53e28.md#insn-00c53e68)
- 新版 `00c54270`（命令位置の公開資料なし） · `00c54288`（命令位置の公開資料なし）

~~~diff
- 00c53e50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c53e50 ["INT_ADD", "register:40f0:8", ["const:c53e50:8", "const:4:8"]]
- 00c53e50 ["CALLIND", null, ["register:0:8"]]
+ 00c54270 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c54270 ["INT_ADD", "register:40f0:8", ["const:c54270:8", "const:4:8"]]
+ 00c54270 ["CALLIND", null, ["register:0:8"]]
- 00c53e50 bytes 00013fd6
+ 00c54270 bytes 00013fd6
- 00c53e68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c53e68 ["INT_ADD", "register:40f0:8", ["const:c53e68:8", "const:4:8"]]
- 00c53e68 ["CALLIND", null, ["register:0:8"]]
+ 00c54288 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c54288 ["INT_ADD", "register:40f0:8", ["const:c54288:8", "const:4:8"]]
+ 00c54288 ["CALLIND", null, ["register:0:8"]]
- 00c53e68 bytes 00013fd6
+ 00c54288 bytes 00013fd6
~~~


<a id="compare-41e2e7d0b376f883077a78c6ad68eef2"></a>

### [`00c53ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53ea4.md) → [`00c542c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c542c4.md) FUN_00c542c4

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c53d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d38.md) [`00c53d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d70.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00c54158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54158.md) [`00c54190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54190.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c53ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53ea4.md#insn-00c53ed0) · [`00c53eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53ea4.md#insn-00c53eec) · [`00c53f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53ea4.md#insn-00c53f08)
- 新版 `00c542f0`（命令位置の公開資料なし） · `00c5430c`（命令位置の公開資料なし） · `00c54328`（命令位置の公開資料なし）

~~~diff
- 00c53ed0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c53ed0 ["INT_ADD", "register:40f0:8", ["const:c53ed0:8", "const:4:8"]]
- 00c53ed0 ["CALLIND", null, ["register:0:8"]]
+ 00c542f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c542f0 ["INT_ADD", "register:40f0:8", ["const:c542f0:8", "const:4:8"]]
+ 00c542f0 ["CALLIND", null, ["register:0:8"]]
- 00c53ed0 bytes 00013fd6
+ 00c542f0 bytes 00013fd6
- 00c53eec ["COPY", "register:0:8", ["register:4040:8"]]
- 00c53eec ["INT_ADD", "register:40f0:8", ["const:c53eec:8", "const:4:8"]]
- 00c53eec ["CALLIND", null, ["register:0:8"]]
+ 00c5430c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c5430c ["INT_ADD", "register:40f0:8", ["const:c5430c:8", "const:4:8"]]
+ 00c5430c ["CALLIND", null, ["register:0:8"]]
- 00c53eec bytes 00013fd6
+ 00c5430c bytes 00013fd6
- 00c53f08 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c53f08 ["INT_ADD", "register:40f0:8", ["const:c53f08:8", "const:4:8"]]
- 00c53f08 ["CALLIND", null, ["register:0:8"]]
+ 00c54328 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c54328 ["INT_ADD", "register:40f0:8", ["const:c54328:8", "const:4:8"]]
+ 00c54328 ["CALLIND", null, ["register:0:8"]]
- 00c53f08 bytes 00013fd6
+ 00c54328 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdc8c908ff4894ffeb72c8bd3e014688"></a>

### [`00c53fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53fb8.md) → [`00c543d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c543d8.md) FUN_00c543d8

採用 · 移動量 `+0x420` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00c53910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53910.md) [`00c53a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53a08.md) [`00c53bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53bc0.md) [`00c53cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53cb4.md) [`00c53ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53ce8.md) · 呼出先 0件 
- 新版 呼出元 5件 [`00c53d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d30.md) [`00c53e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53e28.md) [`00c53fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53fe0.md) [`00c540d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c540d4.md) [`00c54108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54108.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c53fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53fb8.md#insn-00c53fd4)
- 新版 `00c543f4`（命令位置の公開資料なし）

~~~diff
- 00c53fd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c53fd4 ["INT_ADD", "register:40f0:8", ["const:c53fd4:8", "const:4:8"]]
- 00c53fd4 ["CALLIND", null, ["register:0:8"]]
+ 00c543f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c543f4 ["INT_ADD", "register:40f0:8", ["const:c543f4:8", "const:4:8"]]
+ 00c543f4 ["CALLIND", null, ["register:0:8"]]
- 00c53fd4 bytes 00013fd6
+ 00c543f4 bytes 00013fd6
~~~


<a id="compare-9f582e4097b1ae0603c267793b65791a"></a>

### [`00c53ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53ff8.md) → [`00c54418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54418.md) FUN_00c54418

採用 · 移動量 `+0x420` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c53a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53a08.md) [`00c53bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53bc0.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00c53e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53e28.md) [`00c53fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53fe0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c5400c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53ff8.md#insn-00c5400c)
- 新版 `00c5442c`（命令位置の公開資料なし）

~~~diff
- 00c5400c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c5400c ["INT_ADD", "register:40f0:8", ["const:c5400c:8", "const:4:8"]]
- 00c5400c ["CALLIND", null, ["register:0:8"]]
+ 00c5442c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c5442c ["INT_ADD", "register:40f0:8", ["const:c5442c:8", "const:4:8"]]
+ 00c5442c ["CALLIND", null, ["register:0:8"]]
- 00c5400c bytes 00013fd6
+ 00c5442c bytes 00013fd6
~~~


<a id="compare-8e3340c77002c8bca6628b3bfdaebde4"></a>

### [`00c546d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c546d0.md) → [`00c54af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54af0.md) FUN_00c54af0

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c54a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54a90.md) [`00c54bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54bb0.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54eb0.md) [`00c54fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54fd0.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c54714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c546d0.md#insn-00c54714) · [`00c54720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c546d0.md#insn-00c54720) · [`00c54758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c546d0.md#insn-00c54758)
- 新版 `00c54b34`（命令位置の公開資料なし） · `00c54b40`（命令位置の公開資料なし） · `00c54b78`（命令位置の公開資料なし）

~~~diff
- 00c54714 ["INT_ADD", "register:40f0:8", ["const:c54714:8", "const:4:8"]]
- 00c54714 ["CALL", null, ["callee:00c58090:8"]]
+ 00c54b34 ["INT_ADD", "register:40f0:8", ["const:c54b34:8", "const:4:8"]]
+ 00c54b34 ["CALL", null, ["callee:00c58090:8"]]
- 00c54714 bytes 5f0d0094
+ 00c54b34 bytes 570d0094
- 00c54720 ["INT_ADD", "register:40f0:8", ["const:c54720:8", "const:4:8"]]
- 00c54720 ["CALL", null, ["callee:00c54eb0:8"]]
+ 00c54b40 ["INT_ADD", "register:40f0:8", ["const:c54b40:8", "const:4:8"]]
+ 00c54b40 ["CALL", null, ["callee:00c54eb0:8"]]
- 00c54720 bytes dc000094
+ 00c54b40 bytes dc000094
- 00c54758 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c54758 ["INT_ADD", "register:40f0:8", ["const:c54758:8", "const:4:8"]]
- 00c54758 ["CALLIND", null, ["register:0:8"]]
+ 00c54b78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c54b78 ["INT_ADD", "register:40f0:8", ["const:c54b78:8", "const:4:8"]]
+ 00c54b78 ["CALLIND", null, ["register:0:8"]]
- 00c54758 bytes 00013fd6
+ 00c54b78 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecac6365d87ccf30d40a4c77f5fcddb1"></a>

### [`00c570ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c570ec.md) → [`00c5750c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c5750c.md) FUN_00c5750c

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c54848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54848.md) · 呼出先 1件 [`00c5721c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5721c.md)
- 新版 呼出元 1件 [`00c54c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54c68.md) · 呼出先 1件 [`00c5763c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c5763c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c571fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c570ec.md#insn-00c571fc)
- 新版 `00c5761c`（命令位置の公開資料なし）

~~~diff
- 00c571fc ["INT_ADD", "register:40f0:8", ["const:c571fc:8", "const:4:8"]]
- 00c571fc ["CALL", null, ["callee:00c5763c:8"]]
+ 00c5761c ["INT_ADD", "register:40f0:8", ["const:c5761c:8", "const:4:8"]]
+ 00c5761c ["CALL", null, ["callee:00c5763c:8"]]
- 00c571fc bytes 08000094
+ 00c5761c bytes 08000094
~~~


<a id="compare-67b46a304e3ca5bb432af70195a922fc"></a>

### [`00c5733c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5733c.md) → [`00c5775c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c5775c.md) FUN_00c5775c

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c56e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56e18.md) · 呼出先 3件 [`00c541b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c541b0.md) [`00c55f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55f00.md) [`00c5628c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c5628c.md)
- 新版 呼出元 1件 [`00c57238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57238.md) · 呼出先 3件 [`00c545d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c545d0.md) [`00c56320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56320.md) [`00c566ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c566ac.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c573f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5733c.md#insn-00c573f4) · [`00c5741c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5733c.md#insn-00c5741c) · [`00c5743c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5733c.md#insn-00c5743c)
- 新版 `00c57814`（命令位置の公開資料なし） · `00c5783c`（命令位置の公開資料なし） · `00c5785c`（命令位置の公開資料なし）

~~~diff
- 00c573f4 ["INT_ADD", "register:40f0:8", ["const:c573f4:8", "const:4:8"]]
- 00c573f4 ["CALL", null, ["callee:00c545d0:8"]]
+ 00c57814 ["INT_ADD", "register:40f0:8", ["const:c57814:8", "const:4:8"]]
+ 00c57814 ["CALL", null, ["callee:00c545d0:8"]]
- 00c573f4 bytes 6ff3ff97
+ 00c57814 bytes 6ff3ff97
- 00c5741c ["INT_ADD", "register:40f0:8", ["const:c5741c:8", "const:4:8"]]
- 00c5741c ["CALL", null, ["callee:00c56320:8"]]
+ 00c5783c ["INT_ADD", "register:40f0:8", ["const:c5783c:8", "const:4:8"]]
+ 00c5783c ["CALL", null, ["callee:00c56320:8"]]
- 00c5741c bytes b9faff97
+ 00c5783c bytes b9faff97
- 00c5743c ["INT_ADD", "register:40f0:8", ["const:c5743c:8", "const:4:8"]]
- 00c5743c ["CALL", null, ["callee:00c56320:8"]]
+ 00c5785c ["INT_ADD", "register:40f0:8", ["const:c5785c:8", "const:4:8"]]
+ 00c5785c ["CALL", null, ["callee:00c56320:8"]]
- 00c5743c bytes b1faff97
+ 00c5785c bytes b1faff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fa1e005407c94e6e3758986b5ce2159"></a>

### [`00c57504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57504.md) → [`00c57924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57924.md) FUN_00c57924

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c56e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56e18.md) · 呼出先 4件 [`00c54020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54020.md) [`00c55f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55f00.md) [`00c5721c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5721c.md) [`00c5766c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5766c.md)
- 新版 呼出元 1件 [`00c57238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57238.md) · 呼出先 4件 [`00c54440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54440.md) [`00c56320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56320.md) [`00c5763c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c5763c.md) [`00c57a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57a8c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c5754c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57504.md#insn-00c5754c) · [`00c57564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57504.md#insn-00c57564) · [`00c575a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57504.md#insn-00c575a8)
- 新版 `00c5796c`（命令位置の公開資料なし） · `00c57984`（命令位置の公開資料なし） · `00c579c8`（命令位置の公開資料なし）

~~~diff
- 00c5754c ["INT_ADD", "register:40f0:8", ["const:c5754c:8", "const:4:8"]]
- 00c5754c ["CALL", null, ["callee:00c5763c:8"]]
+ 00c5796c ["INT_ADD", "register:40f0:8", ["const:c5796c:8", "const:4:8"]]
+ 00c5796c ["CALL", null, ["callee:00c5763c:8"]]
- 00c5754c bytes 34ffff97
+ 00c5796c bytes 34ffff97
- 00c57564 ["INT_ADD", "register:40f0:8", ["const:c57564:8", "const:4:8"]]
- 00c57564 ["CALL", null, ["callee:00c57a8c:8"]]
+ 00c57984 ["INT_ADD", "register:40f0:8", ["const:c57984:8", "const:4:8"]]
+ 00c57984 ["CALL", null, ["callee:00c57a8c:8"]]
- 00c57564 bytes 42000094
+ 00c57984 bytes 42000094
- 00c575a8 ["INT_ADD", "register:40f0:8", ["const:c575a8:8", "const:4:8"]]
- 00c575a8 ["CALL", null, ["callee:00c56320:8"]]
+ 00c579c8 ["INT_ADD", "register:40f0:8", ["const:c579c8:8", "const:4:8"]]
+ 00c579c8 ["CALL", null, ["callee:00c56320:8"]]
- 00c575a8 bytes 56faff97
+ 00c579c8 bytes 56faff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

