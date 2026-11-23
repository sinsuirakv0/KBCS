# v16.0.0 → v16.0.1 · 要調査の変更候補 (2)

[一覧の目次](README.md)

<a id="compare-1ce7e59cddcb0cd7e8fc62d1b55866d0"></a>

### [`0046134c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/0046134c.md) → [`0046138c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/0046138c.md) FUN_0046138c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00461394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/0046134c.md#insn-00461394) · [`004613a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/0046134c.md#insn-004613a4) · [`004613d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/0046134c.md#insn-004613d4)
- 新版 `004613d4`（命令位置の公開資料なし） · `004613e4`（命令位置の公開資料なし） · `00461414`（命令位置の公開資料なし）

~~~diff
- 00461394 ["INT_ADD", "register:40f0:8", ["const:461394:8", "const:4:8"]]
- 00461394 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004613d4 ["INT_ADD", "register:40f0:8", ["const:4613d4:8", "const:4:8"]]
+ 004613d4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00461394 bytes c7d91f94
+ 004613d4 bytes b7da1f94
- 004613a4 ["INT_ADD", "register:40f0:8", ["const:4613a4:8", "const:4:8"]]
- 004613a4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004613e4 ["INT_ADD", "register:40f0:8", ["const:4613e4:8", "const:4:8"]]
+ 004613e4 ["CALL", null, ["callee:00c57eb0:8"]]
- 004613a4 bytes c3d91f94
+ 004613e4 bytes b3da1f94
- 004613d4 ["INT_ADD", "register:40f0:8", ["const:4613d4:8", "const:4:8"]]
- 004613d4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00461414 ["INT_ADD", "register:40f0:8", ["const:461414:8", "const:4:8"]]
+ 00461414 ["CALL", null, ["callee:00c57eb0:8"]]
- 004613d4 bytes b7d91f94
+ 00461414 bytes a7da1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-866cd49ad798bd7a5e87776b972649d3"></a>

### [`00461404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461404.md) → [`00461444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461444.md) FUN_00461444

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00461a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461a40.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00461a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046143c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461404.md#insn-0046143c)
- 新版 `0046147c`（命令位置の公開資料なし）

~~~diff
- 0046143c ["INT_ADD", "register:40f0:8", ["const:46143c:8", "const:4:8"]]
- 0046143c ["CALL", null, ["callee:00461a80:8"]]
+ 0046147c ["INT_ADD", "register:40f0:8", ["const:46147c:8", "const:4:8"]]
+ 0046147c ["CALL", null, ["callee:00461a80:8"]]
- 0046143c bytes 81010094
+ 0046147c bytes 81010094
~~~


<a id="compare-1406c79651dfff4fcd699d7e3075e919"></a>

### [`00461470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461470.md) → [`004614b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004614b0.md) FUN_004614b0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00460750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460750.md) · 呼出先 6件 [`004615a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004615a0.md) [`00461620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461620.md) [`00461690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461690.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00460790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460790.md) · 呼出先 6件 [`004615e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004615e0.md) [`00461660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461660.md) [`004616d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004616d0.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004614bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461470.md#insn-004614bc) · [`004614fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461470.md#insn-004614fc) · [`00461560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461470.md#insn-00461560)
- 新版 `004614fc`（命令位置の公開資料なし） · `0046153c`（命令位置の公開資料なし） · `004615a0`（命令位置の公開資料なし）

~~~diff
- 004614bc ["INT_ADD", "register:40f0:8", ["const:4614bc:8", "const:4:8"]]
- 004614bc ["CALL", null, ["callee:00c57e90:8"]]
+ 004614fc ["INT_ADD", "register:40f0:8", ["const:4614fc:8", "const:4:8"]]
+ 004614fc ["CALL", null, ["callee:00c57e90:8"]]
- 004614bc bytes 75d91f94
+ 004614fc bytes 65da1f94
- 004614fc ["INT_ADD", "register:40f0:8", ["const:4614fc:8", "const:4:8"]]
- 004614fc ["CALL", null, ["callee:004616d0:8"]]
+ 0046153c ["INT_ADD", "register:40f0:8", ["const:46153c:8", "const:4:8"]]
+ 0046153c ["CALL", null, ["callee:004616d0:8"]]
- 004614fc bytes 65000094
+ 0046153c bytes 65000094
- 00461560 ["INT_ADD", "register:40f0:8", ["const:461560:8", "const:4:8"]]
- 00461560 ["CALL", null, ["callee:00461660:8"]]
+ 004615a0 ["INT_ADD", "register:40f0:8", ["const:4615a0:8", "const:4:8"]]
+ 004615a0 ["CALL", null, ["callee:00461660:8"]]
- 00461560 bytes 30000094
+ 004615a0 bytes 30000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a3598570148c5ed0fca925cf9ab5b03"></a>

### [`004615a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004615a0.md) → [`004615e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004615e0.md) FUN_004615e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00461470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461470.md) · 呼出先 2件 [`00461a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461a40.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`004614b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004614b0.md) · 呼出先 2件 [`00461a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004615f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004615a0.md#insn-004615f4)
- 新版 `00461634`（命令位置の公開資料なし）

~~~diff
- 004615f4 ["INT_ADD", "register:40f0:8", ["const:4615f4:8", "const:4:8"]]
- 004615f4 ["CALL", null, ["callee:00461a80:8"]]
+ 00461634 ["INT_ADD", "register:40f0:8", ["const:461634:8", "const:4:8"]]
+ 00461634 ["CALL", null, ["callee:00461a80:8"]]
- 004615f4 bytes 13010094
+ 00461634 bytes 13010094
~~~


<a id="compare-ec99978dda3f7fd02b013f58edba76e3"></a>

### [`00461634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461634.md) → [`00461674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461674.md) FUN_00461674

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00461a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461a40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00461a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00461674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461634.md#insn-00461674)
- 新版 `004616b4`（命令位置の公開資料なし）

~~~diff
- 00461674 ["INT_ADD", "register:40f0:8", ["const:461674:8", "const:4:8"]]
- 00461674 ["CALL", null, ["callee:00461a80:8"]]
+ 004616b4 ["INT_ADD", "register:40f0:8", ["const:4616b4:8", "const:4:8"]]
+ 004616b4 ["CALL", null, ["callee:00461a80:8"]]
- 00461674 bytes f3000094
+ 004616b4 bytes f3000094
~~~


<a id="compare-baea301ee4d89ef2e201d51827c8ef1a"></a>

### [`00461690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461690.md) → [`004616d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004616d0.md) FUN_004616d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00460750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460750.md) [`00461470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461470.md) [`00461d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461d88.md) [`009c0d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c0d64.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004617d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004617d8.md)
- 新版 呼出元 4件 [`00460790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460790.md) [`004614b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004614b0.md) [`00461dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461dc8.md) [`009c0f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c0/009c0f00.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00461818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461818.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004616c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461690.md#insn-004616c8) · [`004616f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461690.md#insn-004616f4) · [`00461720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461690.md#insn-00461720)
- 新版 `00461708`（命令位置の公開資料なし） · `00461734`（命令位置の公開資料なし） · `00461760`（命令位置の公開資料なし）

~~~diff
- 004616c8 ["INT_ADD", "register:40f0:8", ["const:4616c8:8", "const:4:8"]]
- 004616c8 ["CALL", null, ["callee:0043bb20:8"]]
+ 00461708 ["INT_ADD", "register:40f0:8", ["const:461708:8", "const:4:8"]]
+ 00461708 ["CALL", null, ["callee:0043bb20:8"]]
- 004616c8 bytes 0669ff97
+ 00461708 bytes 0669ff97
- 004616f4 ["INT_ADD", "register:40f0:8", ["const:4616f4:8", "const:4:8"]]
- 004616f4 ["CALL", null, ["callee:0043bb20:8"]]
+ 00461734 ["INT_ADD", "register:40f0:8", ["const:461734:8", "const:4:8"]]
+ 00461734 ["CALL", null, ["callee:0043bb20:8"]]
- 004616f4 bytes fb68ff97
+ 00461734 bytes fb68ff97
- 00461720 ["INT_ADD", "register:40f0:8", ["const:461720:8", "const:4:8"]]
- 00461720 ["CALL", null, ["callee:0043bb20:8"]]
+ 00461760 ["INT_ADD", "register:40f0:8", ["const:461760:8", "const:4:8"]]
+ 00461760 ["CALL", null, ["callee:0043bb20:8"]]
- 00461720 bytes f068ff97
+ 00461760 bytes f068ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc70769d57181190d06d5e15a5cf8aa9"></a>

### [`004617d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004617d8.md) → [`00461818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461818.md) FUN_00461818

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00461690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461690.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00461950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461950.md) [`004619d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004619d8.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`004616d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004616d0.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00461990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461990.md) [`00461a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a18.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00461834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004617d8.md#insn-00461834) · [`004618c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004617d8.md#insn-004618c0) · [`00461910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004617d8.md#insn-00461910)
- 新版 `00461874`（命令位置の公開資料なし） · `00461900`（命令位置の公開資料なし） · `00461950`（命令位置の公開資料なし）

~~~diff
- 00461834 ["INT_ADD", "register:40f0:8", ["const:461834:8", "const:4:8"]]
- 00461834 ["CALL", null, ["callee:00c57e90:8"]]
+ 00461874 ["INT_ADD", "register:40f0:8", ["const:461874:8", "const:4:8"]]
+ 00461874 ["CALL", null, ["callee:00c57e90:8"]]
- 00461834 bytes 97d81f94
+ 00461874 bytes 87d91f94
- 004618c0 ["INT_ADD", "register:40f0:8", ["const:4618c0:8", "const:4:8"]]
- 004618c0 ["CALL", null, ["callee:0043bb20:8"]]
+ 00461900 ["INT_ADD", "register:40f0:8", ["const:461900:8", "const:4:8"]]
+ 00461900 ["CALL", null, ["callee:0043bb20:8"]]
- 004618c0 bytes 8868ff97
+ 00461900 bytes 8868ff97
- 00461910 ["INT_ADD", "register:40f0:8", ["const:461910:8", "const:4:8"]]
- 00461910 ["CALL", null, ["callee:00461a18:8"]]
+ 00461950 ["INT_ADD", "register:40f0:8", ["const:461950:8", "const:4:8"]]
+ 00461950 ["CALL", null, ["callee:00461a18:8"]]
- 00461910 bytes 32000094
+ 00461950 bytes 32000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36a80211e27d8386e147d56cbab4dfdc"></a>

### [`00461950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461950.md) → [`00461990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461990.md) FUN_00461990

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004617d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004617d8.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00461818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461818.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004619b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461950.md#insn-004619b4)
- 新版 `004619f4`（命令位置の公開資料なし）

~~~diff
- 004619b4 ["INT_ADD", "register:40f0:8", ["const:4619b4:8", "const:4:8"]]
- 004619b4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004619f4 ["INT_ADD", "register:40f0:8", ["const:4619f4:8", "const:4:8"]]
+ 004619f4 ["CALL", null, ["callee:00c57eb0:8"]]
- 004619b4 bytes 3fd81f94
+ 004619f4 bytes 2fd91f94
~~~


<a id="compare-063428d0c34499ba702bf1eb3bd2ddca"></a>

### [`004619ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004619ec.md) → [`00461a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a2c.md) FUN_00461a2c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009bf078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf078.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`009bf214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bf/009bf214.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00461a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004619ec.md#insn-00461a2c)
- 新版 `00461a6c`（命令位置の公開資料なし）

~~~diff
- 00461a2c ["INT_ADD", "register:40f0:8", ["const:461a2c:8", "const:4:8"]]
- 00461a2c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00461a6c ["INT_ADD", "register:40f0:8", ["const:461a6c:8", "const:4:8"]]
+ 00461a6c ["CALL", null, ["callee:00c57eb0:8"]]
- 00461a2c bytes 21d81f94
+ 00461a6c bytes 11d91f94
~~~


<a id="compare-c39ed616bab42ea589ffba53534e0112"></a>

### [`00461a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461a40.md) → [`00461a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a80.md) FUN_00461a80

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 11件 [`00460750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460750.md) [`004612d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004612d8.md) [`00461404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461404.md) [`004615a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004615a0.md) [`00461634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461634.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 11件 [`00460790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460790.md) [`00461318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461318.md) [`00461444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461444.md) [`004615e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004615e0.md) [`00461674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461674.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00461a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461a40.md#insn-00461a88) · [`00461a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461a40.md#insn-00461a98) · [`00461ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461a40.md#insn-00461ac8)
- 新版 `00461ac8`（命令位置の公開資料なし） · `00461ad8`（命令位置の公開資料なし） · `00461b08`（命令位置の公開資料なし）

~~~diff
- 00461a88 ["INT_ADD", "register:40f0:8", ["const:461a88:8", "const:4:8"]]
- 00461a88 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00461ac8 ["INT_ADD", "register:40f0:8", ["const:461ac8:8", "const:4:8"]]
+ 00461ac8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00461a88 bytes 0ad81f94
+ 00461ac8 bytes fad81f94
- 00461a98 ["INT_ADD", "register:40f0:8", ["const:461a98:8", "const:4:8"]]
- 00461a98 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00461ad8 ["INT_ADD", "register:40f0:8", ["const:461ad8:8", "const:4:8"]]
+ 00461ad8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00461a98 bytes 06d81f94
+ 00461ad8 bytes f6d81f94
- 00461ac8 ["INT_ADD", "register:40f0:8", ["const:461ac8:8", "const:4:8"]]
- 00461ac8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00461b08 ["INT_ADD", "register:40f0:8", ["const:461b08:8", "const:4:8"]]
+ 00461b08 ["CALL", null, ["callee:00c57eb0:8"]]
- 00461ac8 bytes fad71f94
+ 00461b08 bytes ead81f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f91ca4327a82904f65a18f92571560b0"></a>

### [`00461af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461af8.md) → [`00461b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461b38.md) FUN_00461b38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00460750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460750.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004619d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004619d8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00460790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460790.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00461a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a18.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00461b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461af8.md#insn-00461b9c) · [`00461bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461af8.md#insn-00461bfc) · [`00461c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461af8.md#insn-00461c78)
- 新版 `00461bdc`（命令位置の公開資料なし） · `00461c3c`（命令位置の公開資料なし） · `00461cb8`（命令位置の公開資料なし）

~~~diff
- 00461b9c ["INT_ADD", "register:40f0:8", ["const:461b9c:8", "const:4:8"]]
- 00461b9c ["CALL", null, ["callee:00c57e90:8"]]
+ 00461bdc ["INT_ADD", "register:40f0:8", ["const:461bdc:8", "const:4:8"]]
+ 00461bdc ["CALL", null, ["callee:00c57e90:8"]]
- 00461b9c bytes bdd71f94
+ 00461bdc bytes add81f94
- 00461bfc ["INT_ADD", "register:40f0:8", ["const:461bfc:8", "const:4:8"]]
- 00461bfc ["CALL", null, ["callee:0043bb20:8"]]
+ 00461c3c ["INT_ADD", "register:40f0:8", ["const:461c3c:8", "const:4:8"]]
+ 00461c3c ["CALL", null, ["callee:0043bb20:8"]]
- 00461bfc bytes b967ff97
+ 00461c3c bytes b967ff97
- 00461c78 ["INT_ADD", "register:40f0:8", ["const:461c78:8", "const:4:8"]]
- 00461c78 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00461cb8 ["INT_ADD", "register:40f0:8", ["const:461cb8:8", "const:4:8"]]
+ 00461cb8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00461c78 bytes 8ed71f94
+ 00461cb8 bytes 7ed81f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-673b1a59dac84e64dc33365191d00abf"></a>

### [`00461d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461d20.md) → [`00461d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461d60.md) FUN_00461d60

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00461d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461d20.md#insn-00461d70)
- 新版 `00461db0`（命令位置の公開資料なし）

~~~diff
- 00461d70 ["INT_ADD", "register:40f0:8", ["const:461d70:8", "const:4:8"]]
- 00461d70 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00461db0 ["INT_ADD", "register:40f0:8", ["const:461db0:8", "const:4:8"]]
+ 00461db0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00461d70 bytes 50d71f94
+ 00461db0 bytes 40d81f94
~~~


<a id="compare-d3155be23b0ea978bf7b12c907738416"></a>

### [`00461d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461d88.md) → [`00461dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461dc8.md) FUN_00461dc8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00460750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460750.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00461620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461620.md) [`00461690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461690.md) [`00461a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461a40.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00460790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460790.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00461660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461660.md) [`004616d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004616d0.md) [`00461a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00461e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461d88.md#insn-00461e0c) · [`00461e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461d88.md#insn-00461e30) · [`00461ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461d88.md#insn-00461ee8)
- 新版 `00461e4c`（命令位置の公開資料なし） · `00461e70`（命令位置の公開資料なし） · `00461f28`（命令位置の公開資料なし）

~~~diff
- 00461e0c ["INT_ADD", "register:40f0:8", ["const:461e0c:8", "const:4:8"]]
- 00461e0c ["CALL", null, ["callee:00c57e90:8"]]
+ 00461e4c ["INT_ADD", "register:40f0:8", ["const:461e4c:8", "const:4:8"]]
+ 00461e4c ["CALL", null, ["callee:00c57e90:8"]]
- 00461e0c bytes 21d71f94
+ 00461e4c bytes 11d81f94
- 00461e30 ["INT_ADD", "register:40f0:8", ["const:461e30:8", "const:4:8"]]
- 00461e30 ["CALL", null, ["callee:004616d0:8"]]
+ 00461e70 ["INT_ADD", "register:40f0:8", ["const:461e70:8", "const:4:8"]]
+ 00461e70 ["CALL", null, ["callee:004616d0:8"]]
- 00461e30 bytes 18feff97
+ 00461e70 bytes 18feff97
- 00461ee8 ["INT_ADD", "register:40f0:8", ["const:461ee8:8", "const:4:8"]]
- 00461ee8 ["CALL", null, ["callee:00461a80:8"]]
+ 00461f28 ["INT_ADD", "register:40f0:8", ["const:461f28:8", "const:4:8"]]
+ 00461f28 ["CALL", null, ["callee:00461a80:8"]]
- 00461ee8 bytes d6feff97
+ 00461f28 bytes d6feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b74163d1ac52ee7defab3479f058d630"></a>

### [`00461f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461f98.md) → [`00461fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461fd8.md) FUN_00461fd8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00461a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461a40.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00461a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00461fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461f98.md#insn-00461fc0)
- 新版 `00462000`（命令位置の公開資料なし）

~~~diff
- 00461fc0 ["INT_ADD", "register:40f0:8", ["const:461fc0:8", "const:4:8"]]
- 00461fc0 ["CALL", null, ["callee:00461a80:8"]]
+ 00462000 ["INT_ADD", "register:40f0:8", ["const:462000:8", "const:4:8"]]
+ 00462000 ["CALL", null, ["callee:00461a80:8"]]
- 00461fc0 bytes a0feff97
+ 00462000 bytes a0feff97
~~~


<a id="compare-b022728391318d10dd3bea74b99c947c"></a>

### [`004621c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004621c4.md) → [`00462204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462204.md) FUN_00462204

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00454804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454804.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00454844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454844.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00462200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004621c4.md#insn-00462200)
- 新版 `00462240`（命令位置の公開資料なし）

~~~diff
- 00462200 ["COPY", "register:0:8", ["register:4040:8"]]
- 00462200 ["INT_ADD", "register:40f0:8", ["const:462200:8", "const:4:8"]]
- 00462200 ["CALLIND", null, ["register:0:8"]]
+ 00462240 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00462240 ["INT_ADD", "register:40f0:8", ["const:462240:8", "const:4:8"]]
+ 00462240 ["CALLIND", null, ["register:0:8"]]
- 00462200 bytes 00013fd6
+ 00462240 bytes 00013fd6
~~~


<a id="compare-c915598e5d6580d813c5288d6f39b99c"></a>

### [`00462214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462214.md) → [`00462254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462254.md) FUN_00462254

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00461a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461a40.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00461a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00462264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462214.md#insn-00462264) · [`00462298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462214.md#insn-00462298) · [`004622ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462214.md#insn-004622ac)
- 新版 `004622a4`（命令位置の公開資料なし） · `004622d8`（命令位置の公開資料なし） · `004622ec`（命令位置の公開資料なし）

~~~diff
- 00462264 ["COPY", "register:0:8", ["register:4040:8"]]
- 00462264 ["INT_ADD", "register:40f0:8", ["const:462264:8", "const:4:8"]]
- 00462264 ["CALLIND", null, ["register:0:8"]]
+ 004622a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004622a4 ["INT_ADD", "register:40f0:8", ["const:4622a4:8", "const:4:8"]]
+ 004622a4 ["CALLIND", null, ["register:0:8"]]
- 00462264 bytes 00013fd6
+ 004622a4 bytes 00013fd6
- 00462298 ["INT_ADD", "register:40f0:8", ["const:462298:8", "const:4:8"]]
- 00462298 ["CALL", null, ["callee:00461a80:8"]]
+ 004622d8 ["INT_ADD", "register:40f0:8", ["const:4622d8:8", "const:4:8"]]
+ 004622d8 ["CALL", null, ["callee:00461a80:8"]]
- 00462298 bytes eafdff97
+ 004622d8 bytes eafdff97
- 004622ac ["INT_ADD", "register:40f0:8", ["const:4622ac:8", "const:4:8"]]
- 004622ac ["CALL", null, ["callee:00c57eb0:8"]]
+ 004622ec ["INT_ADD", "register:40f0:8", ["const:4622ec:8", "const:4:8"]]
+ 004622ec ["CALL", null, ["callee:00c57eb0:8"]]
- 004622ac bytes 01d61f94
+ 004622ec bytes f1d61f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1302a9d05f443a69a0445335c72493d"></a>

### [`00462554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462554.md) → [`00462594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462594.md) FUN_00462594

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00454ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454ce8.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00454d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454d28.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00462590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462554.md#insn-00462590)
- 新版 `004625d0`（命令位置の公開資料なし）

~~~diff
- 00462590 ["COPY", "register:0:8", ["register:4040:8"]]
- 00462590 ["INT_ADD", "register:40f0:8", ["const:462590:8", "const:4:8"]]
- 00462590 ["CALLIND", null, ["register:0:8"]]
+ 004625d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004625d0 ["INT_ADD", "register:40f0:8", ["const:4625d0:8", "const:4:8"]]
+ 004625d0 ["CALLIND", null, ["register:0:8"]]
- 00462590 bytes 00013fd6
+ 004625d0 bytes 00013fd6
~~~


<a id="compare-fc4fd1c1149d44cf83fa409363feb96f"></a>

### [`004625a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004625a4.md) → [`004625e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004625e4.md) FUN_004625e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004625dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004625a4.md#insn-004625dc) · [`00462610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004625a4.md#insn-00462610) · [`00462614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004625a4.md#insn-00462614)
- 新版 `0046261c`（命令位置の公開資料なし） · `00462650`（命令位置の公開資料なし） · `00462654`（命令位置の公開資料なし）

~~~diff
- 004625dc ["COPY", "register:0:8", ["register:4040:8"]]
- 004625dc ["INT_ADD", "register:40f0:8", ["const:4625dc:8", "const:4:8"]]
- 004625dc ["CALLIND", null, ["register:0:8"]]
+ 0046261c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046261c ["INT_ADD", "register:40f0:8", ["const:46261c:8", "const:4:8"]]
+ 0046261c ["CALLIND", null, ["register:0:8"]]
- 004625dc bytes 00013fd6
+ 0046261c bytes 00013fd6
- 00462610 ["INT_ADD", "register:40f0:8", ["const:462610:8", "const:4:8"]]
- 00462610 ["CALL", null, ["callee:00459d74:8"]]
+ 00462650 ["INT_ADD", "register:40f0:8", ["const:462650:8", "const:4:8"]]
+ 00462650 ["CALL", null, ["callee:00459d74:8"]]
- 00462610 bytes c9ddff97
+ 00462650 bytes c9ddff97
- 00462614 ["INT_ADD", "register:40f0:8", ["const:462614:8", "const:4:8"]]
- 00462614 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00462654 ["INT_ADD", "register:40f0:8", ["const:462654:8", "const:4:8"]]
+ 00462654 ["CALL", null, ["callee:00c57ee0:8"]]
- 00462614 bytes 33d51f94
+ 00462654 bytes 23d61f94
~~~


<a id="compare-5cb69bf912aa8c03f11e290ae49a4816"></a>

### [`00462814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462814.md) → [`00462854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462854.md) FUN_00462854

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00454ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454ce8.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00454d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454d28.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00462850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462814.md#insn-00462850)
- 新版 `00462890`（命令位置の公開資料なし）

~~~diff
- 00462850 ["COPY", "register:0:8", ["register:4040:8"]]
- 00462850 ["INT_ADD", "register:40f0:8", ["const:462850:8", "const:4:8"]]
- 00462850 ["CALLIND", null, ["register:0:8"]]
+ 00462890 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00462890 ["INT_ADD", "register:40f0:8", ["const:462890:8", "const:4:8"]]
+ 00462890 ["CALLIND", null, ["register:0:8"]]
- 00462850 bytes 00013fd6
+ 00462890 bytes 00013fd6
~~~


<a id="compare-b566e75070041d9b2c34e7f1a7438504"></a>

### [`00462864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462864.md) → [`004628a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004628a4.md) FUN_004628a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046289c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462864.md#insn-0046289c) · [`004628d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462864.md#insn-004628d0) · [`004628d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462864.md#insn-004628d4)
- 新版 `004628dc`（命令位置の公開資料なし） · `00462910`（命令位置の公開資料なし） · `00462914`（命令位置の公開資料なし）

~~~diff
- 0046289c ["COPY", "register:0:8", ["register:4040:8"]]
- 0046289c ["INT_ADD", "register:40f0:8", ["const:46289c:8", "const:4:8"]]
- 0046289c ["CALLIND", null, ["register:0:8"]]
+ 004628dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004628dc ["INT_ADD", "register:40f0:8", ["const:4628dc:8", "const:4:8"]]
+ 004628dc ["CALLIND", null, ["register:0:8"]]
- 0046289c bytes 00013fd6
+ 004628dc bytes 00013fd6
- 004628d0 ["INT_ADD", "register:40f0:8", ["const:4628d0:8", "const:4:8"]]
- 004628d0 ["CALL", null, ["callee:00459d74:8"]]
+ 00462910 ["INT_ADD", "register:40f0:8", ["const:462910:8", "const:4:8"]]
+ 00462910 ["CALL", null, ["callee:00459d74:8"]]
- 004628d0 bytes 19ddff97
+ 00462910 bytes 19ddff97
- 004628d4 ["INT_ADD", "register:40f0:8", ["const:4628d4:8", "const:4:8"]]
- 004628d4 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00462914 ["INT_ADD", "register:40f0:8", ["const:462914:8", "const:4:8"]]
+ 00462914 ["CALL", null, ["callee:00c57ee0:8"]]
- 004628d4 bytes 83d41f94
+ 00462914 bytes 73d51f94
~~~


<a id="compare-ffdab2a595dbcb84dd5ffc4d5e05168a"></a>

### [`00462ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462ad4.md) → [`00462b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462b14.md) FUN_00462b14

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004552b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/004552b8.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`004552f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004552f8.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00462b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462ad4.md#insn-00462b10)
- 新版 `00462b50`（命令位置の公開資料なし）

~~~diff
- 00462b10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00462b10 ["INT_ADD", "register:40f0:8", ["const:462b10:8", "const:4:8"]]
- 00462b10 ["CALLIND", null, ["register:0:8"]]
+ 00462b50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00462b50 ["INT_ADD", "register:40f0:8", ["const:462b50:8", "const:4:8"]]
+ 00462b50 ["CALLIND", null, ["register:0:8"]]
- 00462b10 bytes 00013fd6
+ 00462b50 bytes 00013fd6
~~~


<a id="compare-f36e8062023777686ced5377545bd64b"></a>

### [`00462b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462b24.md) → [`00462b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462b64.md) FUN_00462b64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00461a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461a40.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00461a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00462b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462b24.md#insn-00462b80) · [`00462bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462b24.md#insn-00462bac) · [`00462bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462b24.md#insn-00462bd8)
- 新版 `00462bc0`（命令位置の公開資料なし） · `00462bec`（命令位置の公開資料なし） · `00462c18`（命令位置の公開資料なし）

~~~diff
- 00462b80 ["INT_ADD", "register:40f0:8", ["const:462b80:8", "const:4:8"]]
- 00462b80 ["CALL", null, ["callee:0044108c:8"]]
+ 00462bc0 ["INT_ADD", "register:40f0:8", ["const:462bc0:8", "const:4:8"]]
+ 00462bc0 ["CALL", null, ["callee:0044108c:8"]]
- 00462b80 bytes 3379ff97
+ 00462bc0 bytes 3379ff97
- 00462bac ["INT_ADD", "register:40f0:8", ["const:462bac:8", "const:4:8"]]
- 00462bac ["CALL", null, ["callee:00c57eb0:8"]]
+ 00462bec ["INT_ADD", "register:40f0:8", ["const:462bec:8", "const:4:8"]]
+ 00462bec ["CALL", null, ["callee:00c57eb0:8"]]
- 00462bac bytes c1d31f94
+ 00462bec bytes b1d41f94
- 00462bd8 ["INT_ADD", "register:40f0:8", ["const:462bd8:8", "const:4:8"]]
- 00462bd8 ["CALL", null, ["callee:0044108c:8"]]
+ 00462c18 ["INT_ADD", "register:40f0:8", ["const:462c18:8", "const:4:8"]]
+ 00462c18 ["CALL", null, ["callee:0044108c:8"]]
- 00462bd8 bytes 1d79ff97
+ 00462c18 bytes 1d79ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a32ae70421146859d8e0a490df59a385"></a>

### [`00462f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462f50.md) → [`00462f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462f90.md) FUN_00462f90

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004552b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/004552b8.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`004552f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004552f8.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00462f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462f50.md#insn-00462f8c)
- 新版 `00462fcc`（命令位置の公開資料なし）

~~~diff
- 00462f8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00462f8c ["INT_ADD", "register:40f0:8", ["const:462f8c:8", "const:4:8"]]
- 00462f8c ["CALLIND", null, ["register:0:8"]]
+ 00462fcc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00462fcc ["INT_ADD", "register:40f0:8", ["const:462fcc:8", "const:4:8"]]
+ 00462fcc ["CALLIND", null, ["register:0:8"]]
- 00462f8c bytes 00013fd6
+ 00462fcc bytes 00013fd6
~~~


<a id="compare-31a68efa7bd855e781f3829deb61e3d6"></a>

### [`00462fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462fa0.md) → [`00462fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462fe0.md) FUN_00462fe0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00462fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462fa0.md#insn-00462fe0) · [`00463014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462fa0.md#insn-00463014) · [`00463018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462fa0.md#insn-00463018)
- 新版 `00463020`（命令位置の公開資料なし） · `00463054`（命令位置の公開資料なし） · `00463058`（命令位置の公開資料なし）

~~~diff
- 00462fe0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00462fe0 ["INT_ADD", "register:40f0:8", ["const:462fe0:8", "const:4:8"]]
- 00462fe0 ["CALLIND", null, ["register:0:8"]]
+ 00463020 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463020 ["INT_ADD", "register:40f0:8", ["const:463020:8", "const:4:8"]]
+ 00463020 ["CALLIND", null, ["register:0:8"]]
- 00462fe0 bytes 00013fd6
+ 00463020 bytes 00013fd6
- 00463014 ["INT_ADD", "register:40f0:8", ["const:463014:8", "const:4:8"]]
- 00463014 ["CALL", null, ["callee:00459d74:8"]]
+ 00463054 ["INT_ADD", "register:40f0:8", ["const:463054:8", "const:4:8"]]
+ 00463054 ["CALL", null, ["callee:00459d74:8"]]
- 00463014 bytes 48dbff97
+ 00463054 bytes 48dbff97
- 00463018 ["INT_ADD", "register:40f0:8", ["const:463018:8", "const:4:8"]]
- 00463018 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00463058 ["INT_ADD", "register:40f0:8", ["const:463058:8", "const:4:8"]]
+ 00463058 ["CALL", null, ["callee:00c57ee0:8"]]
- 00463018 bytes b2d21f94
+ 00463058 bytes a2d31f94
~~~


<a id="compare-91d91882dc719ec5963a6a79b4297062"></a>

### [`00463218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463218.md) → [`00463258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463258.md) FUN_00463258

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0045579c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/0045579c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`004557dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004557dc.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00463254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463218.md#insn-00463254)
- 新版 `00463294`（命令位置の公開資料なし）

~~~diff
- 00463254 ["COPY", "register:0:8", ["register:4040:8"]]
- 00463254 ["INT_ADD", "register:40f0:8", ["const:463254:8", "const:4:8"]]
- 00463254 ["CALLIND", null, ["register:0:8"]]
+ 00463294 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463294 ["INT_ADD", "register:40f0:8", ["const:463294:8", "const:4:8"]]
+ 00463294 ["CALLIND", null, ["register:0:8"]]
- 00463254 bytes 00013fd6
+ 00463294 bytes 00013fd6
~~~


<a id="compare-0fded3ced46db07c57105dce3ec372cb"></a>

### [`00463700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463700.md) → [`00463740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463740.md) FUN_00463740

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0045579c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/0045579c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`004557dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004557dc.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463700.md#insn-0046373c)
- 新版 `0046377c`（命令位置の公開資料なし）

~~~diff
- 0046373c ["COPY", "register:0:8", ["register:4040:8"]]
- 0046373c ["INT_ADD", "register:40f0:8", ["const:46373c:8", "const:4:8"]]
- 0046373c ["CALLIND", null, ["register:0:8"]]
+ 0046377c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046377c ["INT_ADD", "register:40f0:8", ["const:46377c:8", "const:4:8"]]
+ 0046377c ["CALLIND", null, ["register:0:8"]]
- 0046373c bytes 00013fd6
+ 0046377c bytes 00013fd6
~~~


<a id="compare-192678632114fb4edb8d1a47a0805149"></a>

### [`00463750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463750.md) → [`00463790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463790.md) FUN_00463790

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00463794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463750.md#insn-00463794) · [`004637ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463750.md#insn-004637ac) · [`004637e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463750.md#insn-004637e0)
- 新版 `004637d4`（命令位置の公開資料なし） · `004637ec`（命令位置の公開資料なし） · `00463820`（命令位置の公開資料なし）

~~~diff
- 00463794 ["COPY", "register:0:8", ["register:4040:8"]]
- 00463794 ["INT_ADD", "register:40f0:8", ["const:463794:8", "const:4:8"]]
- 00463794 ["CALLIND", null, ["register:0:8"]]
+ 004637d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004637d4 ["INT_ADD", "register:40f0:8", ["const:4637d4:8", "const:4:8"]]
+ 004637d4 ["CALLIND", null, ["register:0:8"]]
- 00463794 bytes 00013fd6
+ 004637d4 bytes 00013fd6
- 004637ac ["INT_ADD", "register:40f0:8", ["const:4637ac:8", "const:4:8"]]
- 004637ac ["CALL", null, ["callee:00c57eb0:8"]]
+ 004637ec ["INT_ADD", "register:40f0:8", ["const:4637ec:8", "const:4:8"]]
+ 004637ec ["CALL", null, ["callee:00c57eb0:8"]]
- 004637ac bytes c1d01f94
+ 004637ec bytes b1d11f94
- 004637e0 ["INT_ADD", "register:40f0:8", ["const:4637e0:8", "const:4:8"]]
- 004637e0 ["CALL", null, ["callee:00459d74:8"]]
+ 00463820 ["INT_ADD", "register:40f0:8", ["const:463820:8", "const:4:8"]]
+ 00463820 ["CALL", null, ["callee:00459d74:8"]]
- 004637e0 bytes 55d9ff97
+ 00463820 bytes 55d9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87542f2bc1d600aabf7da08b6ee12673"></a>

### [`00463a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463a18.md) → [`00463a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463a58.md) FUN_00463a58

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00455d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/00455d18.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00455d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/00455d58.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00463a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463a18.md#insn-00463a54)
- 新版 `00463a94`（命令位置の公開資料なし）

~~~diff
- 00463a54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00463a54 ["INT_ADD", "register:40f0:8", ["const:463a54:8", "const:4:8"]]
- 00463a54 ["CALLIND", null, ["register:0:8"]]
+ 00463a94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463a94 ["INT_ADD", "register:40f0:8", ["const:463a94:8", "const:4:8"]]
+ 00463a94 ["CALLIND", null, ["register:0:8"]]
- 00463a54 bytes 00013fd6
+ 00463a94 bytes 00013fd6
~~~


<a id="compare-dd38b0b4d9388b70830ba04df4ccf494"></a>

### [`00463a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463a68.md) → [`00463aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463aa8.md) FUN_00463aa8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00463aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463a68.md#insn-00463aa0) · [`00463ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463a68.md#insn-00463ad4) · [`00463ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463a68.md#insn-00463ad8)
- 新版 `00463ae0`（命令位置の公開資料なし） · `00463b14`（命令位置の公開資料なし） · `00463b18`（命令位置の公開資料なし）

~~~diff
- 00463aa0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00463aa0 ["INT_ADD", "register:40f0:8", ["const:463aa0:8", "const:4:8"]]
- 00463aa0 ["CALLIND", null, ["register:0:8"]]
+ 00463ae0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463ae0 ["INT_ADD", "register:40f0:8", ["const:463ae0:8", "const:4:8"]]
+ 00463ae0 ["CALLIND", null, ["register:0:8"]]
- 00463aa0 bytes 00013fd6
+ 00463ae0 bytes 00013fd6
- 00463ad4 ["INT_ADD", "register:40f0:8", ["const:463ad4:8", "const:4:8"]]
- 00463ad4 ["CALL", null, ["callee:00459d74:8"]]
+ 00463b14 ["INT_ADD", "register:40f0:8", ["const:463b14:8", "const:4:8"]]
+ 00463b14 ["CALL", null, ["callee:00459d74:8"]]
- 00463ad4 bytes 98d8ff97
+ 00463b14 bytes 98d8ff97
- 00463ad8 ["INT_ADD", "register:40f0:8", ["const:463ad8:8", "const:4:8"]]
- 00463ad8 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00463b18 ["INT_ADD", "register:40f0:8", ["const:463b18:8", "const:4:8"]]
+ 00463b18 ["CALL", null, ["callee:00c57ee0:8"]]
- 00463ad8 bytes 02d01f94
+ 00463b18 bytes f2d01f94
~~~


<a id="compare-e4f3254ae8ae15c18adc6a4cd4a5642c"></a>

### [`00463cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463cd8.md) → [`00463d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463d18.md) FUN_00463d18

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00455d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/00455d18.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00455d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/00455d58.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00463d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463cd8.md#insn-00463d14)
- 新版 `00463d54`（命令位置の公開資料なし）

~~~diff
- 00463d14 ["COPY", "register:0:8", ["register:4040:8"]]
- 00463d14 ["INT_ADD", "register:40f0:8", ["const:463d14:8", "const:4:8"]]
- 00463d14 ["CALLIND", null, ["register:0:8"]]
+ 00463d54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463d54 ["INT_ADD", "register:40f0:8", ["const:463d54:8", "const:4:8"]]
+ 00463d54 ["CALLIND", null, ["register:0:8"]]
- 00463d14 bytes 00013fd6
+ 00463d54 bytes 00013fd6
~~~


<a id="compare-b682b1cc1dc2873340d5efd240303563"></a>

### [`00463d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463d28.md) → [`00463d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463d68.md) FUN_00463d68

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00463d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463d28.md#insn-00463d60) · [`00463d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463d28.md#insn-00463d94) · [`00463d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463d28.md#insn-00463d98)
- 新版 `00463da0`（命令位置の公開資料なし） · `00463dd4`（命令位置の公開資料なし） · `00463dd8`（命令位置の公開資料なし）

~~~diff
- 00463d60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00463d60 ["INT_ADD", "register:40f0:8", ["const:463d60:8", "const:4:8"]]
- 00463d60 ["CALLIND", null, ["register:0:8"]]
+ 00463da0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463da0 ["INT_ADD", "register:40f0:8", ["const:463da0:8", "const:4:8"]]
+ 00463da0 ["CALLIND", null, ["register:0:8"]]
- 00463d60 bytes 00013fd6
+ 00463da0 bytes 00013fd6
- 00463d94 ["INT_ADD", "register:40f0:8", ["const:463d94:8", "const:4:8"]]
- 00463d94 ["CALL", null, ["callee:00459d74:8"]]
+ 00463dd4 ["INT_ADD", "register:40f0:8", ["const:463dd4:8", "const:4:8"]]
+ 00463dd4 ["CALL", null, ["callee:00459d74:8"]]
- 00463d94 bytes e8d7ff97
+ 00463dd4 bytes e8d7ff97
- 00463d98 ["INT_ADD", "register:40f0:8", ["const:463d98:8", "const:4:8"]]
- 00463d98 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00463dd8 ["INT_ADD", "register:40f0:8", ["const:463dd8:8", "const:4:8"]]
+ 00463dd8 ["CALL", null, ["callee:00c57ee0:8"]]
- 00463d98 bytes 52cf1f94
+ 00463dd8 bytes 42d01f94
~~~


<a id="compare-551358b905f43d7cf5caf37381610ebc"></a>

### [`00463f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463f98.md) → [`00463fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463fd8.md) FUN_00463fd8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004562e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004562e4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00456324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456324.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00463fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463f98.md#insn-00463fd4)
- 新版 `00464014`（命令位置の公開資料なし）

~~~diff
- 00463fd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00463fd4 ["INT_ADD", "register:40f0:8", ["const:463fd4:8", "const:4:8"]]
- 00463fd4 ["CALLIND", null, ["register:0:8"]]
+ 00464014 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00464014 ["INT_ADD", "register:40f0:8", ["const:464014:8", "const:4:8"]]
+ 00464014 ["CALLIND", null, ["register:0:8"]]
- 00463fd4 bytes 00013fd6
+ 00464014 bytes 00013fd6
~~~


<a id="compare-f1f6ceb2520838e06b4460545b0b11b3"></a>

### [`0046475c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/0046475c.md) → [`0046479c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/0046479c.md) FUN_0046479c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`00463fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463fe8.md) [`00464cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464cec.md) [`0086d6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d6dc.md) [`0086dc24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086dc24.md) [`0086dc44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086dc44.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 8件 [`00464028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464028.md) [`00464d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464d2c.md) [`0086d71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d71c.md) [`0086dc64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086dc64.md) [`0086dc84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086dc84.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004647bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/0046475c.md#insn-004647bc) · [`004647cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/0046475c.md#insn-004647cc) · [`004647dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/0046475c.md#insn-004647dc)
- 新版 `004647fc`（命令位置の公開資料なし） · `0046480c`（命令位置の公開資料なし） · `0046481c`（命令位置の公開資料なし）

~~~diff
- 004647bc ["INT_ADD", "register:40f0:8", ["const:4647bc:8", "const:4:8"]]
- 004647bc ["CALL", null, ["callee:00c57eb0:8"]]
+ 004647fc ["INT_ADD", "register:40f0:8", ["const:4647fc:8", "const:4:8"]]
+ 004647fc ["CALL", null, ["callee:00c57eb0:8"]]
- 004647bc bytes bdcc1f94
+ 004647fc bytes adcd1f94
- 004647cc ["INT_ADD", "register:40f0:8", ["const:4647cc:8", "const:4:8"]]
- 004647cc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0046480c ["INT_ADD", "register:40f0:8", ["const:46480c:8", "const:4:8"]]
+ 0046480c ["CALL", null, ["callee:00c57eb0:8"]]
- 004647cc bytes b9cc1f94
+ 0046480c bytes a9cd1f94
- 004647dc ["INT_ADD", "register:40f0:8", ["const:4647dc:8", "const:4:8"]]
- 004647dc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0046481c ["INT_ADD", "register:40f0:8", ["const:46481c:8", "const:4:8"]]
+ 0046481c ["CALL", null, ["callee:00c57eb0:8"]]
- 004647dc bytes b5cc1f94
+ 0046481c bytes a5cd1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b328f8dc743eca4142ac3950ebfe4db"></a>

### [`00464838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464838.md) → [`00464878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464878.md) FUN_00464878

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00463fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463fe8.md) [`0086d6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d6dc.md) [`0086dc80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086dc80.md) [`0086dd10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086dd10.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 4件 [`00464028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464028.md) [`0086d71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d71c.md) [`0086dcc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086dcc0.md) [`0086dd50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086dd50.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00464870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464838.md#insn-00464870) · [`0046489c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464838.md#insn-0046489c) · [`004648c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464838.md#insn-004648c8)
- 新版 `004648b0`（命令位置の公開資料なし） · `004648dc`（命令位置の公開資料なし） · `00464908`（命令位置の公開資料なし）

~~~diff
- 00464870 ["INT_ADD", "register:40f0:8", ["const:464870:8", "const:4:8"]]
- 00464870 ["CALL", null, ["callee:0043bb20:8"]]
+ 004648b0 ["INT_ADD", "register:40f0:8", ["const:4648b0:8", "const:4:8"]]
+ 004648b0 ["CALL", null, ["callee:0043bb20:8"]]
- 00464870 bytes 9c5cff97
+ 004648b0 bytes 9c5cff97
- 0046489c ["INT_ADD", "register:40f0:8", ["const:46489c:8", "const:4:8"]]
- 0046489c ["CALL", null, ["callee:0043bb20:8"]]
+ 004648dc ["INT_ADD", "register:40f0:8", ["const:4648dc:8", "const:4:8"]]
+ 004648dc ["CALL", null, ["callee:0043bb20:8"]]
- 0046489c bytes 915cff97
+ 004648dc bytes 915cff97
- 004648c8 ["INT_ADD", "register:40f0:8", ["const:4648c8:8", "const:4:8"]]
- 004648c8 ["CALL", null, ["callee:0043bb20:8"]]
+ 00464908 ["INT_ADD", "register:40f0:8", ["const:464908:8", "const:4:8"]]
+ 00464908 ["CALL", null, ["callee:0043bb20:8"]]
- 004648c8 bytes 865cff97
+ 00464908 bytes 865cff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7830e22eca56120f630c677569fab41b"></a>

### [`00464c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464c9c.md) → [`00464cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464cdc.md) FUN_00464cdc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004562e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004562e4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00456324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456324.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00464cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464c9c.md#insn-00464cd8)
- 新版 `00464d18`（命令位置の公開資料なし）

~~~diff
- 00464cd8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00464cd8 ["INT_ADD", "register:40f0:8", ["const:464cd8:8", "const:4:8"]]
- 00464cd8 ["CALLIND", null, ["register:0:8"]]
+ 00464d18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00464d18 ["INT_ADD", "register:40f0:8", ["const:464d18:8", "const:4:8"]]
+ 00464d18 ["CALLIND", null, ["register:0:8"]]
- 00464cd8 bytes 00013fd6
+ 00464d18 bytes 00013fd6
~~~


<a id="compare-e290fe69bb3e1799283548c946f6f313"></a>

### [`00464cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464cec.md) → [`00464d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464d2c.md) FUN_00464d2c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0046475c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/0046475c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0046479c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/0046479c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00464d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464cec.md#insn-00464d30) · [`00464d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464cec.md#insn-00464d40) · [`00464d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464cec.md#insn-00464d74)
- 新版 `00464d70`（命令位置の公開資料なし） · `00464d80`（命令位置の公開資料なし） · `00464db4`（命令位置の公開資料なし）

~~~diff
- 00464d30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00464d30 ["INT_ADD", "register:40f0:8", ["const:464d30:8", "const:4:8"]]
- 00464d30 ["CALLIND", null, ["register:0:8"]]
+ 00464d70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00464d70 ["INT_ADD", "register:40f0:8", ["const:464d70:8", "const:4:8"]]
+ 00464d70 ["CALLIND", null, ["register:0:8"]]
- 00464d30 bytes 00013fd6
+ 00464d70 bytes 00013fd6
- 00464d40 ["INT_ADD", "register:40f0:8", ["const:464d40:8", "const:4:8"]]
- 00464d40 ["CALL", null, ["callee:0046479c:8"]]
+ 00464d80 ["INT_ADD", "register:40f0:8", ["const:464d80:8", "const:4:8"]]
+ 00464d80 ["CALL", null, ["callee:0046479c:8"]]
- 00464d40 bytes 87feff97
+ 00464d80 bytes 87feff97
- 00464d74 ["INT_ADD", "register:40f0:8", ["const:464d74:8", "const:4:8"]]
- 00464d74 ["CALL", null, ["callee:00459d74:8"]]
+ 00464db4 ["INT_ADD", "register:40f0:8", ["const:464db4:8", "const:4:8"]]
+ 00464db4 ["CALL", null, ["callee:00459d74:8"]]
- 00464d74 bytes f0d3ff97
+ 00464db4 bytes f0d3ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5fd6753feed6c0b6ccdaba84744da76"></a>

### [`00464fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464fa4.md) → [`00464fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464fe4.md) FUN_00464fe4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004567c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004567c8.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00456808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456808.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00464fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464fa4.md#insn-00464fe0)
- 新版 `00465020`（命令位置の公開資料なし）

~~~diff
- 00464fe0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00464fe0 ["INT_ADD", "register:40f0:8", ["const:464fe0:8", "const:4:8"]]
- 00464fe0 ["CALLIND", null, ["register:0:8"]]
+ 00465020 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00465020 ["INT_ADD", "register:40f0:8", ["const:465020:8", "const:4:8"]]
+ 00465020 ["CALLIND", null, ["register:0:8"]]
- 00464fe0 bytes 00013fd6
+ 00465020 bytes 00013fd6
~~~


<a id="compare-c2a8b9ff8c3de58adcb0d8715703c6d4"></a>

### [`00464ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464ff4.md) → [`00465034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465034.md) FUN_00465034

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00465028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464ff4.md#insn-00465028) · [`00465058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464ff4.md#insn-00465058) · [`0046507c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464ff4.md#insn-0046507c)
- 新版 `00465068`（命令位置の公開資料なし） · `00465098`（命令位置の公開資料なし） · `004650bc`（命令位置の公開資料なし）

~~~diff
- 00465028 ["COPY", "register:0:8", ["register:4040:8"]]
- 00465028 ["INT_ADD", "register:40f0:8", ["const:465028:8", "const:4:8"]]
- 00465028 ["CALLIND", null, ["register:0:8"]]
+ 00465068 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00465068 ["INT_ADD", "register:40f0:8", ["const:465068:8", "const:4:8"]]
+ 00465068 ["CALLIND", null, ["register:0:8"]]
- 00465028 bytes 00013fd6
+ 00465068 bytes 00013fd6
- 00465058 ["INT_ADD", "register:40f0:8", ["const:465058:8", "const:4:8"]]
- 00465058 ["CALL", null, ["callee:00459d74:8"]]
+ 00465098 ["INT_ADD", "register:40f0:8", ["const:465098:8", "const:4:8"]]
+ 00465098 ["CALL", null, ["callee:00459d74:8"]]
- 00465058 bytes 37d3ff97
+ 00465098 bytes 37d3ff97
- 0046507c ["COPY", "register:0:8", ["register:4040:8"]]
- 0046507c ["INT_ADD", "register:40f0:8", ["const:46507c:8", "const:4:8"]]
- 0046507c ["CALLIND", null, ["register:0:8"]]
+ 004650bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004650bc ["INT_ADD", "register:40f0:8", ["const:4650bc:8", "const:4:8"]]
+ 004650bc ["CALLIND", null, ["register:0:8"]]
- 0046507c bytes 00013fd6
+ 004650bc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d82448d7c24fb33170a6a57ab90ddb19"></a>

### [`00465834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465834.md) → [`00465874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465874.md) FUN_00465874

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046586c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465834.md#insn-0046586c) · [`0046587c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465834.md#insn-0046587c)
- 新版 `004658ac`（命令位置の公開資料なし） · `004658bc`（命令位置の公開資料なし）

~~~diff
- 0046586c ["INT_ADD", "register:40f0:8", ["const:46586c:8", "const:4:8"]]
- 0046586c ["CALL", null, ["callee:00c57eb0:8"]]
+ 004658ac ["INT_ADD", "register:40f0:8", ["const:4658ac:8", "const:4:8"]]
+ 004658ac ["CALL", null, ["callee:00c57eb0:8"]]
- 0046586c bytes 91c81f94
+ 004658ac bytes 81c91f94
- 0046587c ["INT_ADD", "register:40f0:8", ["const:46587c:8", "const:4:8"]]
- 0046587c ["CALL", null, ["callee:00c57eb0:8"]]
+ 004658bc ["INT_ADD", "register:40f0:8", ["const:4658bc:8", "const:4:8"]]
+ 004658bc ["CALL", null, ["callee:00c57eb0:8"]]
- 0046587c bytes 8dc81f94
+ 004658bc bytes 7dc91f94
~~~


<a id="compare-42a32ba48e9f9ab8e24941ef99d0cb2b"></a>

### [`00465898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465898.md) → [`004658d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/004658d8.md) FUN_004658d8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00457838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/00457838.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00457878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457878.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004658c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465898.md#insn-004658c4) · [`004658dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465898.md#insn-004658dc) · [`004658ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465898.md#insn-004658ec)
- 新版 `00465904`（命令位置の公開資料なし） · `0046591c`（命令位置の公開資料なし） · `0046592c`（命令位置の公開資料なし）

~~~diff
- 004658c4 ["INT_ADD", "register:40f0:8", ["const:4658c4:8", "const:4:8"]]
- 004658c4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00465904 ["INT_ADD", "register:40f0:8", ["const:465904:8", "const:4:8"]]
+ 00465904 ["CALL", null, ["callee:00c57eb0:8"]]
- 004658c4 bytes 7bc81f94
+ 00465904 bytes 6bc91f94
- 004658dc ["INT_ADD", "register:40f0:8", ["const:4658dc:8", "const:4:8"]]
- 004658dc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0046591c ["INT_ADD", "register:40f0:8", ["const:46591c:8", "const:4:8"]]
+ 0046591c ["CALL", null, ["callee:00c57eb0:8"]]
- 004658dc bytes 75c81f94
+ 0046591c bytes 65c91f94
- 004658ec ["INT_ADD", "register:40f0:8", ["const:4658ec:8", "const:4:8"]]
- 004658ec ["CALL", null, ["callee:00c57eb0:8"]]
+ 0046592c ["INT_ADD", "register:40f0:8", ["const:46592c:8", "const:4:8"]]
+ 0046592c ["CALL", null, ["callee:00c57eb0:8"]]
- 004658ec bytes 71c81f94
+ 0046592c bytes 61c91f94
~~~


<a id="compare-08301b454151e265f2e68c8e4271987e"></a>

### [`0046688c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/0046688c.md) → [`004668cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/004668cc.md) FUN_004668cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004657c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004657c4.md) [`00465818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465818.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 2件 [`00465804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465804.md) [`00465858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465858.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004668c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/0046688c.md#insn-004668c4) · [`004668f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/0046688c.md#insn-004668f0) · [`0046691c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/0046688c.md#insn-0046691c)
- 新版 `00466904`（命令位置の公開資料なし） · `00466930`（命令位置の公開資料なし） · `0046695c`（命令位置の公開資料なし）

~~~diff
- 004668c4 ["INT_ADD", "register:40f0:8", ["const:4668c4:8", "const:4:8"]]
- 004668c4 ["CALL", null, ["callee:0043bb20:8"]]
+ 00466904 ["INT_ADD", "register:40f0:8", ["const:466904:8", "const:4:8"]]
+ 00466904 ["CALL", null, ["callee:0043bb20:8"]]
- 004668c4 bytes 8754ff97
+ 00466904 bytes 8754ff97
- 004668f0 ["INT_ADD", "register:40f0:8", ["const:4668f0:8", "const:4:8"]]
- 004668f0 ["CALL", null, ["callee:0043bb20:8"]]
+ 00466930 ["INT_ADD", "register:40f0:8", ["const:466930:8", "const:4:8"]]
+ 00466930 ["CALL", null, ["callee:0043bb20:8"]]
- 004668f0 bytes 7c54ff97
+ 00466930 bytes 7c54ff97
- 0046691c ["INT_ADD", "register:40f0:8", ["const:46691c:8", "const:4:8"]]
- 0046691c ["CALL", null, ["callee:0043bb20:8"]]
+ 0046695c ["INT_ADD", "register:40f0:8", ["const:46695c:8", "const:4:8"]]
+ 0046695c ["CALL", null, ["callee:0043bb20:8"]]
- 0046691c bytes 7154ff97
+ 0046695c bytes 7154ff97
~~~


<a id="compare-e1ed18f275b5e15a90880903a0d601b6"></a>

### [`00466ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466ccc.md) → [`00466d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466d0c.md) FUN_00466d0c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0045868c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/0045868c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`004586cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/004586cc.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00466d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466ccc.md#insn-00466d08)
- 新版 `00466d48`（命令位置の公開資料なし）

~~~diff
- 00466d08 ["COPY", "register:0:8", ["register:4040:8"]]
- 00466d08 ["INT_ADD", "register:40f0:8", ["const:466d08:8", "const:4:8"]]
- 00466d08 ["CALLIND", null, ["register:0:8"]]
+ 00466d48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00466d48 ["INT_ADD", "register:40f0:8", ["const:466d48:8", "const:4:8"]]
+ 00466d48 ["CALLIND", null, ["register:0:8"]]
- 00466d08 bytes 00013fd6
+ 00466d48 bytes 00013fd6
~~~


<a id="compare-3d61ff5c2d9d773702d242e96e6406f0"></a>

### [`00466d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466d1c.md) → [`00466d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466d5c.md) FUN_00466d5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00466d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466d1c.md#insn-00466d5c) · [`00466d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466d1c.md#insn-00466d7c) · [`00466da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466d1c.md#insn-00466da4)
- 新版 `00466d9c`（命令位置の公開資料なし） · `00466dbc`（命令位置の公開資料なし） · `00466de4`（命令位置の公開資料なし）

~~~diff
- 00466d5c ["COPY", "register:0:8", ["register:4048:8"]]
- 00466d5c ["INT_ADD", "register:40f0:8", ["const:466d5c:8", "const:4:8"]]
- 00466d5c ["CALLIND", null, ["register:0:8"]]
+ 00466d9c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00466d9c ["INT_ADD", "register:40f0:8", ["const:466d9c:8", "const:4:8"]]
+ 00466d9c ["CALLIND", null, ["register:0:8"]]
- 00466d5c bytes 20013fd6
+ 00466d9c bytes 20013fd6
- 00466d7c ["INT_ADD", "register:40f0:8", ["const:466d7c:8", "const:4:8"]]
- 00466d7c ["CALL", null, ["callee:00c53cd0:8"]]
+ 00466dbc ["INT_ADD", "register:40f0:8", ["const:466dbc:8", "const:4:8"]]
+ 00466dbc ["CALL", null, ["callee:00c53cd0:8"]]
- 00466d7c bytes cdb21f94
+ 00466dbc bytes c5b31f94
- 00466da4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00466da4 ["INT_ADD", "register:40f0:8", ["const:466da4:8", "const:4:8"]]
- 00466da4 ["CALLIND", null, ["register:0:8"]]
+ 00466de4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00466de4 ["INT_ADD", "register:40f0:8", ["const:466de4:8", "const:4:8"]]
+ 00466de4 ["CALLIND", null, ["register:0:8"]]
- 00466da4 bytes 00013fd6
+ 00466de4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54ef33816dcbadf2a33d6216b378f604"></a>

### [`004675c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004675c4.md) → [`00467604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467604.md) FUN_00467604

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005fc360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fc/005fc360.md) · 呼出先 2件 [`0046d934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d934.md) [`0046d96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d96c.md)
- 新版 呼出元 1件 [`005fc3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fc/005fc3a0.md) · 呼出先 2件 [`0046d974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d974.md) [`0046d9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d9ac.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004675dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004675c4.md#insn-004675dc) · [`004675e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004675c4.md#insn-004675e8)
- 新版 `0046761c`（命令位置の公開資料なし） · `00467628`（命令位置の公開資料なし）

~~~diff
- 004675dc ["INT_ADD", "register:40f0:8", ["const:4675dc:8", "const:4:8"]]
- 004675dc ["CALL", null, ["callee:0046d9ac:8"]]
+ 0046761c ["INT_ADD", "register:40f0:8", ["const:46761c:8", "const:4:8"]]
+ 0046761c ["CALL", null, ["callee:0046d9ac:8"]]
- 004675dc bytes e4180094
+ 0046761c bytes e4180094
- 004675e8 ["INT_ADD", "register:40f0:8", ["const:4675e8:8", "const:4:8"]]
- 004675e8 ["CALL", null, ["callee:0046d974:8"]]
+ 00467628 ["INT_ADD", "register:40f0:8", ["const:467628:8", "const:4:8"]]
+ 00467628 ["CALL", null, ["callee:0046d974:8"]]
- 004675e8 bytes d3180094
+ 00467628 bytes d3180094
~~~


<a id="compare-dd32c3d1c43ca5cfee4c180c1d2ef750"></a>

### [`004676d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004676d8.md) → [`00467718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467718.md) FUN_00467718

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0046dde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dde4.md) [`00a46f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46f0c.md) [`00a4743c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a4743c.md) · 呼出先 2件 [`0046d934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d934.md) [`0046d96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d96c.md)
- 新版 呼出元 3件 [`0046de24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046de24.md) [`00a47104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47104.md) [`00a47634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47634.md) · 呼出先 2件 [`0046d974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d974.md) [`0046d9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d9ac.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004676f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004676d8.md#insn-004676f0) · [`004676fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004676d8.md#insn-004676fc)
- 新版 `00467730`（命令位置の公開資料なし） · `0046773c`（命令位置の公開資料なし）

~~~diff
- 004676f0 ["INT_ADD", "register:40f0:8", ["const:4676f0:8", "const:4:8"]]
- 004676f0 ["CALL", null, ["callee:0046d9ac:8"]]
+ 00467730 ["INT_ADD", "register:40f0:8", ["const:467730:8", "const:4:8"]]
+ 00467730 ["CALL", null, ["callee:0046d9ac:8"]]
- 004676f0 bytes 9f180094
+ 00467730 bytes 9f180094
- 004676fc ["INT_ADD", "register:40f0:8", ["const:4676fc:8", "const:4:8"]]
- 004676fc ["CALL", null, ["callee:0046d974:8"]]
+ 0046773c ["INT_ADD", "register:40f0:8", ["const:46773c:8", "const:4:8"]]
+ 0046773c ["CALL", null, ["callee:0046d974:8"]]
- 004676fc bytes 8e180094
+ 0046773c bytes 8e180094
~~~


<a id="compare-18fbc1d84b407338b11bdc0e85b88f1e"></a>

### [`004678dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004678dc.md) → [`0046791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046791c.md) FUN_0046791c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004678f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004678dc.md#insn-004678f8) · [`00467918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004678dc.md#insn-00467918)
- 新版 `00467938`（命令位置の公開資料なし） · `00467958`（命令位置の公開資料なし）

~~~diff
- 004678f8 ["INT_ADD", "register:40f0:8", ["const:4678f8:8", "const:4:8"]]
- 004678f8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00467938 ["INT_ADD", "register:40f0:8", ["const:467938:8", "const:4:8"]]
+ 00467938 ["CALL", null, ["callee:00c53d00:8"]]
- 004678f8 bytes faaf1f94
+ 00467938 bytes f2b01f94
- 00467918 ["COPY", "register:0:8", ["register:4040:8"]]
- 00467918 ["INT_ADD", "register:40f0:8", ["const:467918:8", "const:4:8"]]
- 00467918 ["CALLIND", null, ["register:0:8"]]
+ 00467958 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00467958 ["INT_ADD", "register:40f0:8", ["const:467958:8", "const:4:8"]]
+ 00467958 ["CALLIND", null, ["register:0:8"]]
- 00467918 bytes 00013fd6
+ 00467958 bytes 00013fd6
~~~


<a id="compare-f825ac66ac5e160296f24e25a4e9a4b9"></a>

### [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) → [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) FUN_00467b60

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 70件 [`005c4918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c4918.md) [`005f176c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f1/005f176c.md) [`005f51f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f5/005f51f0.md) [`005f5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f5/005f5750.md) [`0062a1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a1fc.md) · 呼出先 2件 [`0055cf0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cf0c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 69件 [`005c4958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c4/005c4958.md) [`005f17ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f1/005f17ac.md) [`005f5230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5230.md) [`005f5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5790.md) [`0062a23c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062a/0062a23c.md) · 呼出先 2件 [`0055cf4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cf4c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00467b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md#insn-00467b80) · [`00467ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md#insn-00467ba4)
- 新版 `00467bc0`（命令位置の公開資料なし） · `00467be4`（命令位置の公開資料なし）

~~~diff
- 00467b80 ["INT_ADD", "register:40f0:8", ["const:467b80:8", "const:4:8"]]
- 00467b80 ["CALL", null, ["callee:0055cf4c:8"]]
+ 00467bc0 ["INT_ADD", "register:40f0:8", ["const:467bc0:8", "const:4:8"]]
+ 00467bc0 ["CALL", null, ["callee:0055cf4c:8"]]
- 00467b80 bytes e3d40394
+ 00467bc0 bytes e3d40394
- 00467ba4 ["INT_ADD", "register:40f0:8", ["const:467ba4:8", "const:4:8"]]
- 00467ba4 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00467be4 ["INT_ADD", "register:40f0:8", ["const:467be4:8", "const:4:8"]]
+ 00467be4 ["CALL", null, ["callee:00c57ee0:8"]]
- 00467ba4 bytes cfbf1f94
+ 00467be4 bytes bfc01f94
~~~


<a id="compare-11445da3d34a2922274fc03a6501c0ab"></a>

### [`00467d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d04.md) → [`00467d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467d44.md) FUN_00467d44

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 1件 [`0058fa08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fa08.md)
- 新版 呼出元 1件 [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 1件 [`0058fa48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fa48.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00467d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d04.md#insn-00467d34)
- 新版 `00467d74`（命令位置の公開資料なし）

~~~diff
- 00467d34 ["INT_ADD", "register:40f0:8", ["const:467d34:8", "const:4:8"]]
- 00467d34 ["CALL", null, ["callee:0058fa48:8"]]
+ 00467d74 ["INT_ADD", "register:40f0:8", ["const:467d74:8", "const:4:8"]]
+ 00467d74 ["CALL", null, ["callee:0058fa48:8"]]
- 00467d34 bytes 359f0494
+ 00467d74 bytes 359f0494
~~~


<a id="compare-49705ce8f5e2dd129070b5a94593e85e"></a>

### [`00467d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d4c.md) → [`00467d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467d8c.md) FUN_00467d8c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006728c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/006728c4.md) [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 2件 [`00467d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md) [`0055ce0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055ce0c.md)
- 新版 呼出元 2件 [`00672904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672904.md) [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 2件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`0055ce4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055ce4c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00467d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d4c.md#insn-00467d60)
- 新版 `00467da0`（命令位置の公開資料なし）

~~~diff
- 00467d60 ["INT_ADD", "register:40f0:8", ["const:467d60:8", "const:4:8"]]
- 00467d60 ["CALL", null, ["callee:00467dbc:8"]]
+ 00467da0 ["INT_ADD", "register:40f0:8", ["const:467da0:8", "const:4:8"]]
+ 00467da0 ["CALL", null, ["callee:00467dbc:8"]]
- 00467d60 bytes 07000094
+ 00467da0 bytes 07000094
~~~


<a id="compare-9489f2279375aca865f4b8a0dfd348e5"></a>

### [`00467d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md) → [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) FUN_00467dbc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 13件 [`0046792c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/0046792c.md) [`00467abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467abc.md) [`00467d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d4c.md) [`00467d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d74.md) [`00467e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467e6c.md) · 呼出先 7件 [`00555418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555418.md) [`0055a5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5bc.md) [`0055cef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cef8.md) [`0055cf4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cf4c.md) [`0055cf78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cf78.md)
- 新版 呼出元 13件 [`0046796c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046796c.md) [`00467afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467afc.md) [`00467d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467d8c.md) [`00467db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467db4.md) [`00467eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467eac.md) · 呼出先 7件 [`00555458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555458.md) [`0055a5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5fc.md) [`0055cf38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cf38.md) [`0055cf8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cf8c.md) [`0055cfb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cfb8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00467da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md#insn-00467da0) · [`00467dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md#insn-00467dc8) · [`00467dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md#insn-00467dd4)
- 新版 `00467de0`（命令位置の公開資料なし） · `00467e08`（命令位置の公開資料なし） · `00467e14`（命令位置の公開資料なし）

~~~diff
- 00467da0 ["INT_ADD", "register:40f0:8", ["const:467da0:8", "const:4:8"]]
- 00467da0 ["CALL", null, ["callee:0055cf38:8"]]
+ 00467de0 ["INT_ADD", "register:40f0:8", ["const:467de0:8", "const:4:8"]]
+ 00467de0 ["CALL", null, ["callee:0055cf38:8"]]
- 00467da0 bytes 56d40394
+ 00467de0 bytes 56d40394
- 00467dc8 ["INT_ADD", "register:40f0:8", ["const:467dc8:8", "const:4:8"]]
- 00467dc8 ["CALL", null, ["callee:0055cf8c:8"]]
+ 00467e08 ["INT_ADD", "register:40f0:8", ["const:467e08:8", "const:4:8"]]
+ 00467e08 ["CALL", null, ["callee:0055cf8c:8"]]
- 00467dc8 bytes 61d40394
+ 00467e08 bytes 61d40394
- 00467dd4 ["INT_ADD", "register:40f0:8", ["const:467dd4:8", "const:4:8"]]
- 00467dd4 ["CALL", null, ["callee:0055cfb8:8"]]
+ 00467e14 ["INT_ADD", "register:40f0:8", ["const:467e14:8", "const:4:8"]]
+ 00467e14 ["CALL", null, ["callee:0055cfb8:8"]]
- 00467dd4 bytes 69d40394
+ 00467e14 bytes 69d40394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29751fbfeccaa47b5a43344cb7d07ca8"></a>

### [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) → [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) FUN_00467f54

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 77件 [`004954d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/004954d8.md) [`005c7cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c7cc0.md) [`005ed234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005ed234.md) [`005eda3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005eda3c.md) [`005ef56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ef/005ef56c.md) · 呼出先 2件 [`00467d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md) [`0055a4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a4fc.md)
- 新版 呼出元 77件 [`00495518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495518.md) [`005c7d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c7/005c7d00.md) [`005ed274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005ed274.md) [`005eda7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005eda7c.md) [`005ef5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ef/005ef5ac.md) · 呼出先 2件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`0055a53c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a53c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00467f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md#insn-00467f44)
- 新版 `00467f84`（命令位置の公開資料なし）

~~~diff
- 00467f44 ["INT_ADD", "register:40f0:8", ["const:467f44:8", "const:4:8"]]
- 00467f44 ["CALL", null, ["callee:00467dbc:8"]]
+ 00467f84 ["INT_ADD", "register:40f0:8", ["const:467f84:8", "const:4:8"]]
+ 00467f84 ["CALL", null, ["callee:00467dbc:8"]]
- 00467f44 bytes 8effff97
+ 00467f84 bytes 8effff97
~~~


<a id="compare-99680dbef5e18b64421bc0e33902ef1b"></a>

### [`00467f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f6c.md) → [`00467fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467fac.md) FUN_00467fac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005f466c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f4/005f466c.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 2件 [`00467d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md) [`0055a4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a4fc.md)
- 新版 呼出元 2件 [`005f46ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f4/005f46ac.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 2件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`0055a53c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a53c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00467f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f6c.md#insn-00467f94)
- 新版 `00467fd4`（命令位置の公開資料なし）

~~~diff
- 00467f94 ["INT_ADD", "register:40f0:8", ["const:467f94:8", "const:4:8"]]
- 00467f94 ["CALL", null, ["callee:00467dbc:8"]]
+ 00467fd4 ["INT_ADD", "register:40f0:8", ["const:467fd4:8", "const:4:8"]]
+ 00467fd4 ["CALL", null, ["callee:00467dbc:8"]]
- 00467f94 bytes 7affff97
+ 00467fd4 bytes 7affff97
~~~


<a id="compare-54ee61a86b40f053e4c5ce178df84393"></a>

### [`00467fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467fbc.md) → [`00467ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467ffc.md) FUN_00467ffc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`005ee590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ee/005ee590.md) [`005f466c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f4/005f466c.md) [`006797c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00679/006797c0.md) [`006ad3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ad/006ad3d4.md) [`006b66a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b6/006b66a8.md) · 呼出先 8件 [`00467d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md) [`0046c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c420.md) [`0055a3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a3f8.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 7件 [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) [`005f46ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f4/005f46ac.md) [`00679800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00679/00679800.md) [`006ad414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ad/006ad414.md) [`006b66e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b6/006b66e8.md) · 呼出先 8件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`0046c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c460.md) [`0055a438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a438.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00468014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467fbc.md#insn-00468014) · [`00468030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467fbc.md#insn-00468030) · [`004680e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467fbc.md#insn-004680e0)
- 新版 `00468054`（命令位置の公開資料なし） · `00468070`（命令位置の公開資料なし） · `00468120`（命令位置の公開資料なし）

~~~diff
- 00468014 ["INT_ADD", "register:40f0:8", ["const:468014:8", "const:4:8"]]
- 00468014 ["CALL", null, ["callee:00c57e90:8"]]
+ 00468054 ["INT_ADD", "register:40f0:8", ["const:468054:8", "const:4:8"]]
+ 00468054 ["CALL", null, ["callee:00c57e90:8"]]
- 00468014 bytes 9fbe1f94
+ 00468054 bytes 8fbf1f94
- 00468030 ["INT_ADD", "register:40f0:8", ["const:468030:8", "const:4:8"]]
- 00468030 ["CALL", null, ["callee:00c58090:8"]]
+ 00468070 ["INT_ADD", "register:40f0:8", ["const:468070:8", "const:4:8"]]
+ 00468070 ["CALL", null, ["callee:00c58090:8"]]
- 00468030 bytes 18bf1f94
+ 00468070 bytes 08c01f94
- 004680e0 ["INT_ADD", "register:40f0:8", ["const:4680e0:8", "const:4:8"]]
- 004680e0 ["CALL", null, ["callee:00467dbc:8"]]
+ 00468120 ["INT_ADD", "register:40f0:8", ["const:468120:8", "const:4:8"]]
+ 00468120 ["CALL", null, ["callee:00467dbc:8"]]
- 004680e0 bytes 27ffff97
+ 00468120 bytes 27ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22ed4aef55c450d60381eac2a6f6e5bc"></a>

### [`004684c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004684c0.md) → [`00468500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468500.md) FUN_00468500

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00468180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468180.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046c40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c40c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`004681c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004681c0.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046c44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c44c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004685a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004684c0.md#insn-004685a8) · [`004685d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004684c0.md#insn-004685d8) · [`004685ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004684c0.md#insn-004685ec)
- 新版 `004685e8`（命令位置の公開資料なし） · `00468618`（命令位置の公開資料なし） · `0046862c`（命令位置の公開資料なし）

~~~diff
- 004685a8 ["INT_ADD", "register:40f0:8", ["const:4685a8:8", "const:4:8"]]
- 004685a8 ["CALL", null, ["callee:00c57e90:8"]]
+ 004685e8 ["INT_ADD", "register:40f0:8", ["const:4685e8:8", "const:4:8"]]
+ 004685e8 ["CALL", null, ["callee:00c57e90:8"]]
- 004685a8 bytes 3abd1f94
+ 004685e8 bytes 2abe1f94
- 004685d8 ["INT_ADD", "register:40f0:8", ["const:4685d8:8", "const:4:8"]]
- 004685d8 ["CALL", null, ["callee:00c58000:8"]]
+ 00468618 ["INT_ADD", "register:40f0:8", ["const:468618:8", "const:4:8"]]
+ 00468618 ["CALL", null, ["callee:00c58000:8"]]
- 004685d8 bytes 8abd1f94
+ 00468618 bytes 7abe1f94
- 004685ec ["INT_ADD", "register:40f0:8", ["const:4685ec:8", "const:4:8"]]
- 004685ec ["CALL", null, ["callee:00c57eb0:8"]]
+ 0046862c ["INT_ADD", "register:40f0:8", ["const:46862c:8", "const:4:8"]]
+ 0046862c ["CALL", null, ["callee:00c57eb0:8"]]
- 004685ec bytes 31bd1f94
+ 0046862c bytes 21be1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58c1264a006628e97250d961bd4e0b94"></a>

### [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) → [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) FUN_00468804

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 48件 [`004954d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/004954d8.md) [`005f466c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f4/005f466c.md) [`005fb0b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fb/005fb0b8.md) [`006122a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00612/006122a4.md) [`006350c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006350c4.md) · 呼出先 4件 [`00467d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md) [`0048aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aaf0.md) [`0048aaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aaf8.md) [`0048ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ab10.md)
- 新版 呼出元 48件 [`00495518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495518.md) [`005f46ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f4/005f46ac.md) [`005fb0f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fb/005fb0f8.md) [`006122e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00612/006122e4.md) [`00635104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/00635104.md) · 呼出先 4件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`0048ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab30.md) [`0048ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab38.md) [`0048ab50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004687fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md#insn-004687fc) · [`00468814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md#insn-00468814) · [`00468824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md#insn-00468824)
- 新版 `0046883c`（命令位置の公開資料なし） · `00468854`（命令位置の公開資料なし） · `00468864`（命令位置の公開資料なし）

~~~diff
- 004687fc ["INT_ADD", "register:40f0:8", ["const:4687fc:8", "const:4:8"]]
- 004687fc ["CALL", null, ["callee:0048ab30:8"]]
+ 0046883c ["INT_ADD", "register:40f0:8", ["const:46883c:8", "const:4:8"]]
+ 0046883c ["CALL", null, ["callee:0048ab30:8"]]
- 004687fc bytes bd880094
+ 0046883c bytes bd880094
- 00468814 ["INT_ADD", "register:40f0:8", ["const:468814:8", "const:4:8"]]
- 00468814 ["CALL", null, ["callee:0048ab38:8"]]
+ 00468854 ["INT_ADD", "register:40f0:8", ["const:468854:8", "const:4:8"]]
+ 00468854 ["CALL", null, ["callee:0048ab38:8"]]
- 00468814 bytes b9880094
+ 00468854 bytes b9880094
- 00468824 ["INT_ADD", "register:40f0:8", ["const:468824:8", "const:4:8"]]
- 00468824 ["CALL", null, ["callee:0048ab30:8"]]
+ 00468864 ["INT_ADD", "register:40f0:8", ["const:468864:8", "const:4:8"]]
+ 00468864 ["CALL", null, ["callee:0048ab30:8"]]
- 00468824 bytes b3880094
+ 00468864 bytes b3880094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b53f3479de1aec83634d6358bc207f93"></a>

### [`00468878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468878.md) → [`004688b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004688b8.md) FUN_004688b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006acaac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ac/006acaac.md) [`00963e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00963/00963e3c.md) · 呼出先 5件 [`00467d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md) [`0048aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aaf0.md) [`0048ab00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ab00.md) [`0048ab08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ab08.md) [`0048ab40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ab40.md)
- 新版 呼出元 2件 [`006acaec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ac/006acaec.md) [`00963fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00963/00963fd8.md) · 呼出先 5件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`0048ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab30.md) [`0048ab40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab40.md) [`0048ab48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab48.md) [`0048ab80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004688b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468878.md#insn-004688b0) · [`004688bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468878.md#insn-004688bc) · [`004688d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468878.md#insn-004688d8)
- 新版 `004688f0`（命令位置の公開資料なし） · `004688fc`（命令位置の公開資料なし） · `00468918`（命令位置の公開資料なし）

~~~diff
- 004688b0 ["INT_ADD", "register:40f0:8", ["const:4688b0:8", "const:4:8"]]
- 004688b0 ["CALL", null, ["callee:0048ab40:8"]]
+ 004688f0 ["INT_ADD", "register:40f0:8", ["const:4688f0:8", "const:4:8"]]
+ 004688f0 ["CALL", null, ["callee:0048ab40:8"]]
- 004688b0 bytes 94880094
+ 004688f0 bytes 94880094
- 004688bc ["INT_ADD", "register:40f0:8", ["const:4688bc:8", "const:4:8"]]
- 004688bc ["CALL", null, ["callee:0048ab48:8"]]
+ 004688fc ["INT_ADD", "register:40f0:8", ["const:4688fc:8", "const:4:8"]]
+ 004688fc ["CALL", null, ["callee:0048ab48:8"]]
- 004688bc bytes 93880094
+ 004688fc bytes 93880094
- 004688d8 ["INT_ADD", "register:40f0:8", ["const:4688d8:8", "const:4:8"]]
- 004688d8 ["CALL", null, ["callee:0048ab30:8"]]
+ 00468918 ["INT_ADD", "register:40f0:8", ["const:468918:8", "const:4:8"]]
+ 00468918 ["CALL", null, ["callee:0048ab30:8"]]
- 004688d8 bytes 86880094
+ 00468918 bytes 86880094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-290abc006cfc4a024b3caeede1ba4367"></a>

### [`00468980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468980.md) → [`004689c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004689c0.md) FUN_004689c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004954d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/004954d8.md) · 呼出先 4件 [`00467d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md) [`0048aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aaf0.md) [`0048aaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aaf8.md) [`0048ab40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ab40.md)
- 新版 呼出元 1件 [`00495518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495518.md) · 呼出先 4件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`0048ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab30.md) [`0048ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab38.md) [`0048ab80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004689cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468980.md#insn-004689cc) · [`004689e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468980.md#insn-004689e4) · [`004689f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468980.md#insn-004689f4)
- 新版 `00468a0c`（命令位置の公開資料なし） · `00468a24`（命令位置の公開資料なし） · `00468a34`（命令位置の公開資料なし）

~~~diff
- 004689cc ["INT_ADD", "register:40f0:8", ["const:4689cc:8", "const:4:8"]]
- 004689cc ["CALL", null, ["callee:0048ab30:8"]]
+ 00468a0c ["INT_ADD", "register:40f0:8", ["const:468a0c:8", "const:4:8"]]
+ 00468a0c ["CALL", null, ["callee:0048ab30:8"]]
- 004689cc bytes 49880094
+ 00468a0c bytes 49880094
- 004689e4 ["INT_ADD", "register:40f0:8", ["const:4689e4:8", "const:4:8"]]
- 004689e4 ["CALL", null, ["callee:0048ab38:8"]]
+ 00468a24 ["INT_ADD", "register:40f0:8", ["const:468a24:8", "const:4:8"]]
+ 00468a24 ["CALL", null, ["callee:0048ab38:8"]]
- 004689e4 bytes 45880094
+ 00468a24 bytes 45880094
- 004689f4 ["INT_ADD", "register:40f0:8", ["const:4689f4:8", "const:4:8"]]
- 004689f4 ["CALL", null, ["callee:0048ab30:8"]]
+ 00468a34 ["INT_ADD", "register:40f0:8", ["const:468a34:8", "const:4:8"]]
+ 00468a34 ["CALL", null, ["callee:0048ab30:8"]]
- 004689f4 bytes 3f880094
+ 00468a34 bytes 3f880094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abcbc00d98e0788efa49c43de1076652"></a>

### [`00468a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468a94.md) → [`00468ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468ad4.md) FUN_00468ad4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00789da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md) · 呼出先 4件 [`00467d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md) [`0048aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aaf0.md) [`0048aaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aaf8.md) [`0048ab40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ab40.md)
- 新版 呼出元 1件 [`00789de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789de0.md) · 呼出先 4件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`0048ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab30.md) [`0048ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab38.md) [`0048ab80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00468adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468a94.md#insn-00468adc) · [`00468aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468a94.md#insn-00468aec) · [`00468b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468a94.md#insn-00468b14)
- 新版 `00468b1c`（命令位置の公開資料なし） · `00468b2c`（命令位置の公開資料なし） · `00468b54`（命令位置の公開資料なし）

~~~diff
- 00468adc ["INT_ADD", "register:40f0:8", ["const:468adc:8", "const:4:8"]]
- 00468adc ["CALL", null, ["callee:0048ab30:8"]]
+ 00468b1c ["INT_ADD", "register:40f0:8", ["const:468b1c:8", "const:4:8"]]
+ 00468b1c ["CALL", null, ["callee:0048ab30:8"]]
- 00468adc bytes 05880094
+ 00468b1c bytes 05880094
- 00468aec ["INT_ADD", "register:40f0:8", ["const:468aec:8", "const:4:8"]]
- 00468aec ["CALL", null, ["callee:0048ab30:8"]]
+ 00468b2c ["INT_ADD", "register:40f0:8", ["const:468b2c:8", "const:4:8"]]
+ 00468b2c ["CALL", null, ["callee:0048ab30:8"]]
- 00468aec bytes 01880094
+ 00468b2c bytes 01880094
- 00468b14 ["INT_ADD", "register:40f0:8", ["const:468b14:8", "const:4:8"]]
- 00468b14 ["CALL", null, ["callee:0048ab38:8"]]
+ 00468b54 ["INT_ADD", "register:40f0:8", ["const:468b54:8", "const:4:8"]]
+ 00468b54 ["CALL", null, ["callee:0048ab38:8"]]
- 00468b14 bytes f9870094
+ 00468b54 bytes f9870094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c427200c41908a00de267c9c0a643ca2"></a>

### [`00468b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468b9c.md) → [`00468bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md) FUN_00468bdc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 37件 [`0046e548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e548.md) [`005c7cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c7cc0.md) [`005eda3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005eda3c.md) [`005ee590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ee/005ee590.md) [`005f5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f5/005f5750.md) · 呼出先 2件 [`0055cf0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cf0c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 37件 [`0046e588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e588.md) [`005c7d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c7/005c7d00.md) [`005eda7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005eda7c.md) [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) [`005f5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5790.md) · 呼出先 2件 [`0055cf4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cf4c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00468bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468b9c.md#insn-00468bf8) · [`00468c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468b9c.md#insn-00468c1c)
- 新版 `00468c38`（命令位置の公開資料なし） · `00468c5c`（命令位置の公開資料なし）

~~~diff
- 00468bf8 ["INT_ADD", "register:40f0:8", ["const:468bf8:8", "const:4:8"]]
- 00468bf8 ["CALL", null, ["callee:0055cf4c:8"]]
+ 00468c38 ["INT_ADD", "register:40f0:8", ["const:468c38:8", "const:4:8"]]
+ 00468c38 ["CALL", null, ["callee:0055cf4c:8"]]
- 00468bf8 bytes c5d00394
+ 00468c38 bytes c5d00394
- 00468c1c ["INT_ADD", "register:40f0:8", ["const:468c1c:8", "const:4:8"]]
- 00468c1c ["CALL", null, ["callee:00c57ee0:8"]]
+ 00468c5c ["INT_ADD", "register:40f0:8", ["const:468c5c:8", "const:4:8"]]
+ 00468c5c ["CALL", null, ["callee:00c57ee0:8"]]
- 00468c1c bytes b1bb1f94
+ 00468c5c bytes a1bc1f94
~~~


<a id="compare-72e3b3c1309386fd6ac5cbf40f7de6b1"></a>

### [`00468c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468c28.md) → [`00468c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468c68.md) FUN_00468c68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`0060eb10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060eb10.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) [`007fb1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fb/007fb1f0.md) [`008c9c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c9/008c9c0c.md) [`00963e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00963/00963e3c.md) · 呼出先 3件 [`00468cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468cc8.md) [`0048aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aaf0.md) [`0048aaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aaf8.md)
- 新版 呼出元 7件 [`0060eb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060e/0060eb50.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) [`007fb230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fb230.md) [`008c9da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c9/008c9da8.md) [`00963fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00963/00963fd8.md) · 呼出先 3件 [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md) [`0048ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab30.md) [`0048ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab38.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00468c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468c28.md#insn-00468c58) · [`00468c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468c28.md#insn-00468c64) · [`00468c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468c28.md#insn-00468c70)
- 新版 `00468c98`（命令位置の公開資料なし） · `00468ca4`（命令位置の公開資料なし） · `00468cb0`（命令位置の公開資料なし）

~~~diff
- 00468c58 ["INT_ADD", "register:40f0:8", ["const:468c58:8", "const:4:8"]]
- 00468c58 ["CALL", null, ["callee:0048ab30:8"]]
+ 00468c98 ["INT_ADD", "register:40f0:8", ["const:468c98:8", "const:4:8"]]
+ 00468c98 ["CALL", null, ["callee:0048ab30:8"]]
- 00468c58 bytes a6870094
+ 00468c98 bytes a6870094
- 00468c64 ["INT_ADD", "register:40f0:8", ["const:468c64:8", "const:4:8"]]
- 00468c64 ["CALL", null, ["callee:0048ab38:8"]]
+ 00468ca4 ["INT_ADD", "register:40f0:8", ["const:468ca4:8", "const:4:8"]]
+ 00468ca4 ["CALL", null, ["callee:0048ab38:8"]]
- 00468c64 bytes a5870094
+ 00468ca4 bytes a5870094
- 00468c70 ["INT_ADD", "register:40f0:8", ["const:468c70:8", "const:4:8"]]
- 00468c70 ["CALL", null, ["callee:0048ab30:8"]]
+ 00468cb0 ["INT_ADD", "register:40f0:8", ["const:468cb0:8", "const:4:8"]]
+ 00468cb0 ["CALL", null, ["callee:0048ab30:8"]]
- 00468c70 bytes a0870094
+ 00468cb0 bytes a0870094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3a2f09dfaf26bf14eb2788fc26864ff"></a>

### [`00468cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468cc8.md) → [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md) FUN_00468d08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 13件 [`00468c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468c28.md) [`00468f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f0c.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00469104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469104.md) [`0046961c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/0046961c.md) · 呼出先 5件 [`0048ac50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ac50.md) [`0055a568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a568.md) [`0055a5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5bc.md) [`0055cf0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cf0c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 13件 [`00468c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468c68.md) [`00468f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f4c.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00469144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469144.md) [`0046965c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md) · 呼出先 5件 [`0048ac90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ac90.md) [`0055a5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5a8.md) [`0055a5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5fc.md) [`0055cf4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cf4c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00468d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468cc8.md#insn-00468d1c) · [`00468d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468cc8.md#insn-00468d64) · [`00468d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468cc8.md#insn-00468d94)
- 新版 `00468d5c`（命令位置の公開資料なし） · `00468da4`（命令位置の公開資料なし） · `00468dd4`（命令位置の公開資料なし）

~~~diff
- 00468d1c ["INT_ADD", "register:40f0:8", ["const:468d1c:8", "const:4:8"]]
- 00468d1c ["CALL", null, ["callee:0055a5a8:8"]]
+ 00468d5c ["INT_ADD", "register:40f0:8", ["const:468d5c:8", "const:4:8"]]
+ 00468d5c ["CALL", null, ["callee:0055a5a8:8"]]
- 00468d1c bytes 13c60394
+ 00468d5c bytes 13c60394
- 00468d64 ["INT_ADD", "register:40f0:8", ["const:468d64:8", "const:4:8"]]
- 00468d64 ["CALL", null, ["callee:0055cf4c:8"]]
+ 00468da4 ["INT_ADD", "register:40f0:8", ["const:468da4:8", "const:4:8"]]
+ 00468da4 ["CALL", null, ["callee:0055cf4c:8"]]
- 00468d64 bytes 6ad00394
+ 00468da4 bytes 6ad00394
- 00468d94 ["INT_ADD", "register:40f0:8", ["const:468d94:8", "const:4:8"]]
- 00468d94 ["CALL", null, ["callee:0048ac90:8"]]
+ 00468dd4 ["INT_ADD", "register:40f0:8", ["const:468dd4:8", "const:4:8"]]
+ 00468dd4 ["CALL", null, ["callee:0048ac90:8"]]
- 00468d94 bytes af870094
+ 00468dd4 bytes af870094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdbda62c7a6e3b032b34ba68063ab5eb"></a>

### [`00468de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468de0.md) → [`00468e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468e20.md) FUN_00468e20

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`00469028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469028.md) [`00469c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469c8c.md) [`0046a210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a210.md) [`0046a938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a938.md) [`0046aee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aee0.md) · 呼出先 5件 [`0048ae98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ae98.md) [`0055a568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a568.md) [`0055a5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5bc.md) [`0055cf0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cf0c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 7件 [`00469068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469068.md) [`00469ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469ccc.md) [`0046a250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a250.md) [`0046a978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a978.md) [`0046af20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af20.md) · 呼出先 5件 [`0048aed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aed8.md) [`0055a5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5a8.md) [`0055a5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5fc.md) [`0055cf4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cf4c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00468e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468de0.md#insn-00468e44) · [`00468e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468de0.md#insn-00468e8c) · [`00468ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468de0.md#insn-00468ebc)
- 新版 `00468e84`（命令位置の公開資料なし） · `00468ecc`（命令位置の公開資料なし） · `00468efc`（命令位置の公開資料なし）

~~~diff
- 00468e44 ["INT_ADD", "register:40f0:8", ["const:468e44:8", "const:4:8"]]
- 00468e44 ["CALL", null, ["callee:0055a5a8:8"]]
+ 00468e84 ["INT_ADD", "register:40f0:8", ["const:468e84:8", "const:4:8"]]
+ 00468e84 ["CALL", null, ["callee:0055a5a8:8"]]
- 00468e44 bytes c9c50394
+ 00468e84 bytes c9c50394
- 00468e8c ["INT_ADD", "register:40f0:8", ["const:468e8c:8", "const:4:8"]]
- 00468e8c ["CALL", null, ["callee:0055cf4c:8"]]
+ 00468ecc ["INT_ADD", "register:40f0:8", ["const:468ecc:8", "const:4:8"]]
+ 00468ecc ["CALL", null, ["callee:0055cf4c:8"]]
- 00468e8c bytes 20d00394
+ 00468ecc bytes 20d00394
- 00468ebc ["INT_ADD", "register:40f0:8", ["const:468ebc:8", "const:4:8"]]
- 00468ebc ["CALL", null, ["callee:0048aed8:8"]]
+ 00468efc ["INT_ADD", "register:40f0:8", ["const:468efc:8", "const:4:8"]]
+ 00468efc ["CALL", null, ["callee:0048aed8:8"]]
- 00468ebc bytes f7870094
+ 00468efc bytes f7870094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1df9f76b0c1c0b1140f7d1aabf936d16"></a>

### [`00468f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f0c.md) → [`00468f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f4c.md) FUN_00468f4c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`006dde48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dd/006dde48.md) [`006f89c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f8/006f89c8.md) [`007475b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/007475b0.md) [`0077acec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077a/0077acec.md) [`008e7234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e7/008e7234.md) · 呼出先 1件 [`00468cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468cc8.md)
- 新版 呼出元 6件 [`006dde88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006dd/006dde88.md) [`006f8a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f8/006f8a08.md) [`007475f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/007475f0.md) [`0077ad2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077a/0077ad2c.md) [`008e73d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e7/008e73d0.md) · 呼出先 1件 [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00468f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f0c.md#insn-00468f38)
- 新版 `00468f78`（命令位置の公開資料なし）

~~~diff
- 00468f38 ["INT_ADD", "register:40f0:8", ["const:468f38:8", "const:4:8"]]
- 00468f38 ["CALL", null, ["callee:00468d08:8"]]
+ 00468f78 ["INT_ADD", "register:40f0:8", ["const:468f78:8", "const:4:8"]]
+ 00468f78 ["CALL", null, ["callee:00468d08:8"]]
- 00468f38 bytes 64ffff97
+ 00468f78 bytes 64ffff97
~~~


<a id="compare-467b926434b207829dadc95dba1a9f69"></a>

### [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) → [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) FUN_00468f88

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 111件 [`004954d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/004954d8.md) [`005c7cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c7cc0.md) [`005eda3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005eda3c.md) [`005f5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f5/005f5750.md) [`005f6c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f6/005f6c14.md) · 呼出先 2件 [`00468cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468cc8.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md)
- 新版 呼出元 111件 [`00495518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495518.md) [`005c7d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c7/005c7d00.md) [`005eda7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005eda7c.md) [`005f5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5790.md) [`005f6c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f6/005f6c54.md) · 呼出先 2件 [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00468f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md#insn-00468f84) · [`00468f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md#insn-00468f94) · [`00468fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md#insn-00468fa4)
- 新版 `00468fc4`（命令位置の公開資料なし） · `00468fd4`（命令位置の公開資料なし） · `00468fe4`（命令位置の公開資料なし）

~~~diff
- 00468f84 ["INT_ADD", "register:40f0:8", ["const:468f84:8", "const:4:8"]]
- 00468f84 ["CALL", null, ["callee:00489f4c:8"]]
+ 00468fc4 ["INT_ADD", "register:40f0:8", ["const:468fc4:8", "const:4:8"]]
+ 00468fc4 ["CALL", null, ["callee:00489f4c:8"]]
- 00468f84 bytes e2830094
+ 00468fc4 bytes e2830094
- 00468f94 ["INT_ADD", "register:40f0:8", ["const:468f94:8", "const:4:8"]]
- 00468f94 ["CALL", null, ["callee:00489f4c:8"]]
+ 00468fd4 ["INT_ADD", "register:40f0:8", ["const:468fd4:8", "const:4:8"]]
+ 00468fd4 ["CALL", null, ["callee:00489f4c:8"]]
- 00468f94 bytes de830094
+ 00468fd4 bytes de830094
- 00468fa4 ["INT_ADD", "register:40f0:8", ["const:468fa4:8", "const:4:8"]]
- 00468fa4 ["CALL", null, ["callee:00489f4c:8"]]
+ 00468fe4 ["INT_ADD", "register:40f0:8", ["const:468fe4:8", "const:4:8"]]
+ 00468fe4 ["CALL", null, ["callee:00489f4c:8"]]
- 00468fa4 bytes da830094
+ 00468fe4 bytes da830094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12d7f694424a9408d082d6504af2686b"></a>

### [`00469028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469028.md) → [`00469068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469068.md) FUN_00469068

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00646570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00646/00646570.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) [`0082d768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d768.md) [`009f6a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f6/009f6a78.md) · 呼出先 2件 [`00468de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468de0.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md)
- 新版 呼出元 4件 [`006465b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00646/006465b0.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`0082d7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d7a8.md) [`009f6c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f6c14.md) · 呼出先 2件 [`00468e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468e20.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00469060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469028.md#insn-00469060) · [`00469074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469028.md#insn-00469074) · [`00469088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469028.md#insn-00469088)
- 新版 `004690a0`（命令位置の公開資料なし） · `004690b4`（命令位置の公開資料なし） · `004690c8`（命令位置の公開資料なし）

~~~diff
- 00469060 ["INT_ADD", "register:40f0:8", ["const:469060:8", "const:4:8"]]
- 00469060 ["CALL", null, ["callee:00489f4c:8"]]
+ 004690a0 ["INT_ADD", "register:40f0:8", ["const:4690a0:8", "const:4:8"]]
+ 004690a0 ["CALL", null, ["callee:00489f4c:8"]]
- 00469060 bytes ab830094
+ 004690a0 bytes ab830094
- 00469074 ["INT_ADD", "register:40f0:8", ["const:469074:8", "const:4:8"]]
- 00469074 ["CALL", null, ["callee:00489f4c:8"]]
+ 004690b4 ["INT_ADD", "register:40f0:8", ["const:4690b4:8", "const:4:8"]]
+ 004690b4 ["CALL", null, ["callee:00489f4c:8"]]
- 00469074 bytes a6830094
+ 004690b4 bytes a6830094
- 00469088 ["INT_ADD", "register:40f0:8", ["const:469088:8", "const:4:8"]]
- 00469088 ["CALL", null, ["callee:00489f4c:8"]]
+ 004690c8 ["INT_ADD", "register:40f0:8", ["const:4690c8:8", "const:4:8"]]
+ 004690c8 ["CALL", null, ["callee:00489f4c:8"]]
- 00469088 bytes a1830094
+ 004690c8 bytes a1830094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d793215e0ebbc912639551da5fcb8d2"></a>

### [`00469104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469104.md) → [`00469144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469144.md) FUN_00469144

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`0062b498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062b498.md) [`006c43a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c4/006c43a4.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 2件 [`00468cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468cc8.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md)
- 新版 呼出元 9件 [`0062b4d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062b/0062b4d8.md) [`006c43e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c4/006c43e4.md) [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 2件 [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00469180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469104.md#insn-00469180) · [`00469190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469104.md#insn-00469190) · [`004691c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469104.md#insn-004691c0)
- 新版 `004691c0`（命令位置の公開資料なし） · `004691d0`（命令位置の公開資料なし） · `00469200`（命令位置の公開資料なし）

~~~diff
- 00469180 ["INT_ADD", "register:40f0:8", ["const:469180:8", "const:4:8"]]
- 00469180 ["CALL", null, ["callee:00489f4c:8"]]
+ 004691c0 ["INT_ADD", "register:40f0:8", ["const:4691c0:8", "const:4:8"]]
+ 004691c0 ["CALL", null, ["callee:00489f4c:8"]]
- 00469180 bytes 63830094
+ 004691c0 bytes 63830094
- 00469190 ["INT_ADD", "register:40f0:8", ["const:469190:8", "const:4:8"]]
- 00469190 ["CALL", null, ["callee:00489f4c:8"]]
+ 004691d0 ["INT_ADD", "register:40f0:8", ["const:4691d0:8", "const:4:8"]]
+ 004691d0 ["CALL", null, ["callee:00489f4c:8"]]
- 00469190 bytes 5f830094
+ 004691d0 bytes 5f830094
- 004691c0 ["INT_ADD", "register:40f0:8", ["const:4691c0:8", "const:4:8"]]
- 004691c0 ["CALL", null, ["callee:00468d08:8"]]
+ 00469200 ["INT_ADD", "register:40f0:8", ["const:469200:8", "const:4:8"]]
+ 00469200 ["CALL", null, ["callee:00468d08:8"]]
- 004691c0 bytes c2feff97
+ 00469200 bytes c2feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1714090fb560acb5ec365cefac25464b"></a>

### [`0046961c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/0046961c.md) → [`0046965c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md) FUN_0046965c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 37件 [`004954d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/004954d8.md) [`005f5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f5/005f5750.md) [`0060eb10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060eb10.md) [`00613c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/00613c24.md) [`0065cc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065c/0065cc8c.md) · 呼出先 2件 [`00468cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468cc8.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md)
- 新版 呼出元 37件 [`00495518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495518.md) [`005f5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5790.md) [`0060eb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060e/0060eb50.md) [`00613c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00613/00613c64.md) [`0065cccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065c/0065cccc.md) · 呼出先 2件 [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046967c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/0046961c.md#insn-0046967c) · [`0046968c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/0046961c.md#insn-0046968c) · [`004696a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/0046961c.md#insn-004696a0)
- 新版 `004696bc`（命令位置の公開資料なし） · `004696cc`（命令位置の公開資料なし） · `004696e0`（命令位置の公開資料なし）

~~~diff
- 0046967c ["INT_ADD", "register:40f0:8", ["const:46967c:8", "const:4:8"]]
- 0046967c ["CALL", null, ["callee:00489f4c:8"]]
+ 004696bc ["INT_ADD", "register:40f0:8", ["const:4696bc:8", "const:4:8"]]
+ 004696bc ["CALL", null, ["callee:00489f4c:8"]]
- 0046967c bytes 24820094
+ 004696bc bytes 24820094
- 0046968c ["INT_ADD", "register:40f0:8", ["const:46968c:8", "const:4:8"]]
- 0046968c ["CALL", null, ["callee:00489f4c:8"]]
+ 004696cc ["INT_ADD", "register:40f0:8", ["const:4696cc:8", "const:4:8"]]
+ 004696cc ["CALL", null, ["callee:00489f4c:8"]]
- 0046968c bytes 20820094
+ 004696cc bytes 20820094
- 004696a0 ["INT_ADD", "register:40f0:8", ["const:4696a0:8", "const:4:8"]]
- 004696a0 ["CALL", null, ["callee:00489f4c:8"]]
+ 004696e0 ["INT_ADD", "register:40f0:8", ["const:4696e0:8", "const:4:8"]]
+ 004696e0 ["CALL", null, ["callee:00489f4c:8"]]
- 004696a0 bytes 1b820094
+ 004696e0 bytes 1b820094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ac7b65670c50931ca37b3b50a7a5a0c"></a>

### [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) → [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) FUN_00469c04

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 120件 [`005ed234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005ed234.md) [`005eda3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005eda3c.md) [`005ee590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ee/005ee590.md) [`005f176c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f1/005f176c.md) [`005f3c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f3/005f3c9c.md) · 呼出先 2件 [`00468cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468cc8.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md)
- 新版 呼出元 120件 [`005ed274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005ed274.md) [`005eda7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005eda7c.md) [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) [`005f17ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f1/005f17ac.md) [`005f3cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f3/005f3cdc.md) · 呼出先 2件 [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00469c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md#insn-00469c08) · [`00469c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md#insn-00469c18) · [`00469c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md#insn-00469c28)
- 新版 `00469c48`（命令位置の公開資料なし） · `00469c58`（命令位置の公開資料なし） · `00469c68`（命令位置の公開資料なし）

~~~diff
- 00469c08 ["INT_ADD", "register:40f0:8", ["const:469c08:8", "const:4:8"]]
- 00469c08 ["CALL", null, ["callee:00489f4c:8"]]
+ 00469c48 ["INT_ADD", "register:40f0:8", ["const:469c48:8", "const:4:8"]]
+ 00469c48 ["CALL", null, ["callee:00489f4c:8"]]
- 00469c08 bytes c1800094
+ 00469c48 bytes c1800094
- 00469c18 ["INT_ADD", "register:40f0:8", ["const:469c18:8", "const:4:8"]]
- 00469c18 ["CALL", null, ["callee:00489f4c:8"]]
+ 00469c58 ["INT_ADD", "register:40f0:8", ["const:469c58:8", "const:4:8"]]
+ 00469c58 ["CALL", null, ["callee:00489f4c:8"]]
- 00469c18 bytes bd800094
+ 00469c58 bytes bd800094
- 00469c28 ["INT_ADD", "register:40f0:8", ["const:469c28:8", "const:4:8"]]
- 00469c28 ["CALL", null, ["callee:00489f4c:8"]]
+ 00469c68 ["INT_ADD", "register:40f0:8", ["const:469c68:8", "const:4:8"]]
+ 00469c68 ["CALL", null, ["callee:00489f4c:8"]]
- 00469c28 bytes b9800094
+ 00469c68 bytes b9800094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65e9d04af92a8d74627117767b6b8a8a"></a>

### [`00469c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469c8c.md) → [`00469ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469ccc.md) FUN_00469ccc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`005c4918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c4918.md) [`005c7cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c7cc0.md) [`00789da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md) [`00a79a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a79/00a79a0c.md) [`00ae0e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0e64.md) · 呼出先 2件 [`00468de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468de0.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md)
- 新版 呼出元 5件 [`005c4958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c4/005c4958.md) [`005c7d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c7/005c7d00.md) [`00789de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789de0.md) [`00a79c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a79/00a79c04.md) [`00ae128c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae1/00ae128c.md) · 呼出先 2件 [`00468e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468e20.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00469cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469c8c.md#insn-00469cf0) · [`00469d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469c8c.md#insn-00469d00) · [`00469d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469c8c.md#insn-00469d18)
- 新版 `00469d30`（命令位置の公開資料なし） · `00469d40`（命令位置の公開資料なし） · `00469d58`（命令位置の公開資料なし）

~~~diff
- 00469cf0 ["INT_ADD", "register:40f0:8", ["const:469cf0:8", "const:4:8"]]
- 00469cf0 ["CALL", null, ["callee:00489f4c:8"]]
+ 00469d30 ["INT_ADD", "register:40f0:8", ["const:469d30:8", "const:4:8"]]
+ 00469d30 ["CALL", null, ["callee:00489f4c:8"]]
- 00469cf0 bytes 87800094
+ 00469d30 bytes 87800094
- 00469d00 ["INT_ADD", "register:40f0:8", ["const:469d00:8", "const:4:8"]]
- 00469d00 ["CALL", null, ["callee:00489f4c:8"]]
+ 00469d40 ["INT_ADD", "register:40f0:8", ["const:469d40:8", "const:4:8"]]
+ 00469d40 ["CALL", null, ["callee:00489f4c:8"]]
- 00469d00 bytes 83800094
+ 00469d40 bytes 83800094
- 00469d18 ["INT_ADD", "register:40f0:8", ["const:469d18:8", "const:4:8"]]
- 00469d18 ["CALL", null, ["callee:00489f4c:8"]]
+ 00469d58 ["INT_ADD", "register:40f0:8", ["const:469d58:8", "const:4:8"]]
+ 00469d58 ["CALL", null, ["callee:00489f4c:8"]]
- 00469d18 bytes 7d800094
+ 00469d58 bytes 7d800094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96fb5b04a652384b711f3c8cd5f737d6"></a>

### [`0046a210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a210.md) → [`0046a250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a250.md) FUN_0046a250

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 26件 [`005c4918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c4918.md) [`005f3c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f3/005f3c9c.md) [`006122a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00612/006122a4.md) [`00646570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00646/00646570.md) [`006d4d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d4/006d4d54.md) · 呼出先 2件 [`00468de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468de0.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md)
- 新版 呼出元 24件 [`005c4958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c4/005c4958.md) [`005f3cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f3/005f3cdc.md) [`006122e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00612/006122e4.md) [`006465b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00646/006465b0.md) [`006d4d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d4/006d4d94.md) · 呼出先 2件 [`00468e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468e20.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046a250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a210.md#insn-0046a250) · [`0046a260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a210.md#insn-0046a260) · [`0046a270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a210.md#insn-0046a270)
- 新版 `0046a290`（命令位置の公開資料なし） · `0046a2a0`（命令位置の公開資料なし） · `0046a2b0`（命令位置の公開資料なし）

~~~diff
- 0046a250 ["INT_ADD", "register:40f0:8", ["const:46a250:8", "const:4:8"]]
- 0046a250 ["CALL", null, ["callee:00489f4c:8"]]
+ 0046a290 ["INT_ADD", "register:40f0:8", ["const:46a290:8", "const:4:8"]]
+ 0046a290 ["CALL", null, ["callee:00489f4c:8"]]
- 0046a250 bytes 2f7f0094
+ 0046a290 bytes 2f7f0094
- 0046a260 ["INT_ADD", "register:40f0:8", ["const:46a260:8", "const:4:8"]]
- 0046a260 ["CALL", null, ["callee:00489f4c:8"]]
+ 0046a2a0 ["INT_ADD", "register:40f0:8", ["const:46a2a0:8", "const:4:8"]]
+ 0046a2a0 ["CALL", null, ["callee:00489f4c:8"]]
- 0046a260 bytes 2b7f0094
+ 0046a2a0 bytes 2b7f0094
- 0046a270 ["INT_ADD", "register:40f0:8", ["const:46a270:8", "const:4:8"]]
- 0046a270 ["CALL", null, ["callee:00489f4c:8"]]
+ 0046a2b0 ["INT_ADD", "register:40f0:8", ["const:46a2b0:8", "const:4:8"]]
+ 0046a2b0 ["CALL", null, ["callee:00489f4c:8"]]
- 0046a270 bytes 277f0094
+ 0046a2b0 bytes 277f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bac7c5cb8699fd227db89c25254da1d"></a>

### [`0046a2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a2cc.md) → [`0046a30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a30c.md) FUN_0046a30c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0065cc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065c/0065cc8c.md) [`0065d5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065d/0065d5f0.md) [`0072c29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c29c.md) · 呼出先 2件 [`00468cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468cc8.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md)
- 新版 呼出元 3件 [`0065cccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065c/0065cccc.md) [`0065d630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065d/0065d630.md) [`0072c2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c2dc.md) · 呼出先 2件 [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046a318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a2cc.md#insn-0046a318) · [`0046a328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a2cc.md#insn-0046a328) · [`0046a33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a2cc.md#insn-0046a33c)
- 新版 `0046a358`（命令位置の公開資料なし） · `0046a368`（命令位置の公開資料なし） · `0046a37c`（命令位置の公開資料なし）

~~~diff
- 0046a318 ["INT_ADD", "register:40f0:8", ["const:46a318:8", "const:4:8"]]
- 0046a318 ["CALL", null, ["callee:00489f4c:8"]]
+ 0046a358 ["INT_ADD", "register:40f0:8", ["const:46a358:8", "const:4:8"]]
+ 0046a358 ["CALL", null, ["callee:00489f4c:8"]]
- 0046a318 bytes fd7e0094
+ 0046a358 bytes fd7e0094
- 0046a328 ["INT_ADD", "register:40f0:8", ["const:46a328:8", "const:4:8"]]
- 0046a328 ["CALL", null, ["callee:00489f4c:8"]]
+ 0046a368 ["INT_ADD", "register:40f0:8", ["const:46a368:8", "const:4:8"]]
+ 0046a368 ["CALL", null, ["callee:00489f4c:8"]]
- 0046a328 bytes f97e0094
+ 0046a368 bytes f97e0094
- 0046a33c ["INT_ADD", "register:40f0:8", ["const:46a33c:8", "const:4:8"]]
- 0046a33c ["CALL", null, ["callee:00489f4c:8"]]
+ 0046a37c ["INT_ADD", "register:40f0:8", ["const:46a37c:8", "const:4:8"]]
+ 0046a37c ["CALL", null, ["callee:00489f4c:8"]]
- 0046a33c bytes f47e0094
+ 0046a37c bytes f47e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-789b24f3c9c71d69bc28f317a1ae513b"></a>

### [`0046a8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a8a8.md) → [`0046a8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a8e8.md) FUN_0046a8e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 24件 [`005e4034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e4034.md) [`005ee590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ee/005ee590.md) [`0065cc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065c/0065cc8c.md) [`0065d5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065d/0065d5f0.md) [`006954cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/006954cc.md) · 呼出先 3件 [`00468cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468cc8.md) [`0048aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aaf0.md) [`0048aaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aaf8.md)
- 新版 呼出元 24件 [`005e4074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4074.md) [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) [`0065cccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065c/0065cccc.md) [`0065d630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065d/0065d630.md) [`0069550c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/0069550c.md) · 呼出先 3件 [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md) [`0048ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab30.md) [`0048ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab38.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046a8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a8a8.md#insn-0046a8e0) · [`0046a8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a8a8.md#insn-0046a8ec) · [`0046a918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a8a8.md#insn-0046a918)
- 新版 `0046a920`（命令位置の公開資料なし） · `0046a92c`（命令位置の公開資料なし） · `0046a958`（命令位置の公開資料なし）

~~~diff
- 0046a8e0 ["INT_ADD", "register:40f0:8", ["const:46a8e0:8", "const:4:8"]]
- 0046a8e0 ["CALL", null, ["callee:0048ab30:8"]]
+ 0046a920 ["INT_ADD", "register:40f0:8", ["const:46a920:8", "const:4:8"]]
+ 0046a920 ["CALL", null, ["callee:0048ab30:8"]]
- 0046a8e0 bytes 84800094
+ 0046a920 bytes 84800094
- 0046a8ec ["INT_ADD", "register:40f0:8", ["const:46a8ec:8", "const:4:8"]]
- 0046a8ec ["CALL", null, ["callee:0048ab38:8"]]
+ 0046a92c ["INT_ADD", "register:40f0:8", ["const:46a92c:8", "const:4:8"]]
+ 0046a92c ["CALL", null, ["callee:0048ab38:8"]]
- 0046a8ec bytes 83800094
+ 0046a92c bytes 83800094
- 0046a918 ["INT_ADD", "register:40f0:8", ["const:46a918:8", "const:4:8"]]
- 0046a918 ["CALL", null, ["callee:00468d08:8"]]
+ 0046a958 ["INT_ADD", "register:40f0:8", ["const:46a958:8", "const:4:8"]]
+ 0046a958 ["CALL", null, ["callee:00468d08:8"]]
- 0046a918 bytes ecf8ff97
+ 0046a958 bytes ecf8ff97
~~~


<a id="compare-dc168c7a9b83cca23334c34c0840d217"></a>

### [`0046a938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a938.md) → [`0046a978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a978.md) FUN_0046a978

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00646570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00646/00646570.md) [`0073edf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073e/0073edf4.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) [`0099b8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0099b/0099b8d4.md) · 呼出先 3件 [`00468de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468de0.md) [`0048aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aaf0.md) [`0048aaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aaf8.md)
- 新版 呼出元 6件 [`006465b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00646/006465b0.md) [`0073ee34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073e/0073ee34.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) [`0099ba70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0099b/0099ba70.md) · 呼出先 3件 [`00468e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468e20.md) [`0048ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab30.md) [`0048ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab38.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046a96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a938.md#insn-0046a96c) · [`0046a978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a938.md#insn-0046a978)
- 新版 `0046a9ac`（命令位置の公開資料なし） · `0046a9b8`（命令位置の公開資料なし）

~~~diff
- 0046a96c ["INT_ADD", "register:40f0:8", ["const:46a96c:8", "const:4:8"]]
- 0046a96c ["CALL", null, ["callee:0048ab30:8"]]
+ 0046a9ac ["INT_ADD", "register:40f0:8", ["const:46a9ac:8", "const:4:8"]]
+ 0046a9ac ["CALL", null, ["callee:0048ab30:8"]]
- 0046a96c bytes 61800094
+ 0046a9ac bytes 61800094
- 0046a978 ["INT_ADD", "register:40f0:8", ["const:46a978:8", "const:4:8"]]
- 0046a978 ["CALL", null, ["callee:0048ab38:8"]]
+ 0046a9b8 ["INT_ADD", "register:40f0:8", ["const:46a9b8:8", "const:4:8"]]
+ 0046a9b8 ["CALL", null, ["callee:0048ab38:8"]]
- 0046a978 bytes 60800094
+ 0046a9b8 bytes 60800094
~~~


<a id="compare-50537f230955a1a3946e05be2c9d6121"></a>

### [`0046a9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a9bc.md) → [`0046a9fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a9fc.md) FUN_0046a9fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0046adf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046adf4.md) [`0046b4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046b4c8.md) [`005fc360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fc/005fc360.md) [`00a471fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a471fc.md) · 呼出先 5件 [`0048b09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b09c.md) [`0055a568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a568.md) [`0055a5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5bc.md) [`0055cf0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cf0c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 4件 [`0046ae34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046ae34.md) [`0046b508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b508.md) [`005fc3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fc/005fc3a0.md) [`00a473f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a473f4.md) · 呼出先 5件 [`0048b0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b0dc.md) [`0055a5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5a8.md) [`0055a5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5fc.md) [`0055cf4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cf4c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046aa24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a9bc.md#insn-0046aa24) · [`0046aa6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a9bc.md#insn-0046aa6c) · [`0046aabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a9bc.md#insn-0046aabc)
- 新版 `0046aa64`（命令位置の公開資料なし） · `0046aaac`（命令位置の公開資料なし） · `0046aafc`（命令位置の公開資料なし）

~~~diff
- 0046aa24 ["INT_ADD", "register:40f0:8", ["const:46aa24:8", "const:4:8"]]
- 0046aa24 ["CALL", null, ["callee:0055a5a8:8"]]
+ 0046aa64 ["INT_ADD", "register:40f0:8", ["const:46aa64:8", "const:4:8"]]
+ 0046aa64 ["CALL", null, ["callee:0055a5a8:8"]]
- 0046aa24 bytes d1be0394
+ 0046aa64 bytes d1be0394
- 0046aa6c ["INT_ADD", "register:40f0:8", ["const:46aa6c:8", "const:4:8"]]
- 0046aa6c ["CALL", null, ["callee:0055cf4c:8"]]
+ 0046aaac ["INT_ADD", "register:40f0:8", ["const:46aaac:8", "const:4:8"]]
+ 0046aaac ["CALL", null, ["callee:0055cf4c:8"]]
- 0046aa6c bytes 28c90394
+ 0046aaac bytes 28c90394
- 0046aabc ["INT_ADD", "register:40f0:8", ["const:46aabc:8", "const:4:8"]]
- 0046aabc ["CALL", null, ["callee:0048b0dc:8"]]
+ 0046aafc ["INT_ADD", "register:40f0:8", ["const:46aafc:8", "const:4:8"]]
+ 0046aafc ["CALL", null, ["callee:0048b0dc:8"]]
- 0046aabc bytes 78810094
+ 0046aafc bytes 78810094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-234d8f1103fc9706af5d00000c49bd20"></a>

### [`0046ab08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046ab08.md) → [`0046ab48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046ab48.md) FUN_0046ab48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0046b6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046b6b4.md) · 呼出先 5件 [`0048b210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b210.md) [`0055a568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a568.md) [`0055a5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5bc.md) [`0055cf0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cf0c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0046b6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b6f4.md) · 呼出先 5件 [`0048b250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b250.md) [`0055a5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5a8.md) [`0055a5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5fc.md) [`0055cf4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cf4c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046ab84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046ab08.md#insn-0046ab84) · [`0046abcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046ab08.md#insn-0046abcc) · [`0046ac08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046ab08.md#insn-0046ac08)
- 新版 `0046abc4`（命令位置の公開資料なし） · `0046ac0c`（命令位置の公開資料なし） · `0046ac48`（命令位置の公開資料なし）

~~~diff
- 0046ab84 ["INT_ADD", "register:40f0:8", ["const:46ab84:8", "const:4:8"]]
- 0046ab84 ["CALL", null, ["callee:0055a5a8:8"]]
+ 0046abc4 ["INT_ADD", "register:40f0:8", ["const:46abc4:8", "const:4:8"]]
+ 0046abc4 ["CALL", null, ["callee:0055a5a8:8"]]
- 0046ab84 bytes 79be0394
+ 0046abc4 bytes 79be0394
- 0046abcc ["INT_ADD", "register:40f0:8", ["const:46abcc:8", "const:4:8"]]
- 0046abcc ["CALL", null, ["callee:0055cf4c:8"]]
+ 0046ac0c ["INT_ADD", "register:40f0:8", ["const:46ac0c:8", "const:4:8"]]
+ 0046ac0c ["CALL", null, ["callee:0055cf4c:8"]]
- 0046abcc bytes d0c80394
+ 0046ac0c bytes d0c80394
- 0046ac08 ["INT_ADD", "register:40f0:8", ["const:46ac08:8", "const:4:8"]]
- 0046ac08 ["CALL", null, ["callee:0048b250:8"]]
+ 0046ac48 ["INT_ADD", "register:40f0:8", ["const:46ac48:8", "const:4:8"]]
+ 0046ac48 ["CALL", null, ["callee:0048b250:8"]]
- 0046ac08 bytes 82810094
+ 0046ac48 bytes 82810094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01f0ac123a0553c0bd5a68baf3497e61"></a>

### [`0046ac60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046ac60.md) → [`0046aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046aca0.md) FUN_0046aca0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0046be38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046be38.md) [`0046e548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e548.md) · 呼出先 5件 [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`00489f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f18.md) [`0048aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aaf0.md) [`0048aaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aaf8.md) [`0048b09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b09c.md)
- 新版 呼出元 2件 [`0046be78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046be78.md) [`0046e588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e588.md) · 呼出先 5件 [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`00489f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f58.md) [`0048ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab30.md) [`0048ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab38.md) [`0048b0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b0dc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046acb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046ac60.md#insn-0046acb8) · [`0046acc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046ac60.md#insn-0046acc4) · [`0046ad08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046ac60.md#insn-0046ad08)
- 新版 `0046acf8`（命令位置の公開資料なし） · `0046ad04`（命令位置の公開資料なし） · `0046ad48`（命令位置の公開資料なし）

~~~diff
- 0046acb8 ["INT_ADD", "register:40f0:8", ["const:46acb8:8", "const:4:8"]]
- 0046acb8 ["CALL", null, ["callee:0048ab30:8"]]
+ 0046acf8 ["INT_ADD", "register:40f0:8", ["const:46acf8:8", "const:4:8"]]
+ 0046acf8 ["CALL", null, ["callee:0048ab30:8"]]
- 0046acb8 bytes 8e7f0094
+ 0046acf8 bytes 8e7f0094
- 0046acc4 ["INT_ADD", "register:40f0:8", ["const:46acc4:8", "const:4:8"]]
- 0046acc4 ["CALL", null, ["callee:0048ab38:8"]]
+ 0046ad04 ["INT_ADD", "register:40f0:8", ["const:46ad04:8", "const:4:8"]]
+ 0046ad04 ["CALL", null, ["callee:0048ab38:8"]]
- 0046acc4 bytes 8d7f0094
+ 0046ad04 bytes 8d7f0094
- 0046ad08 ["INT_ADD", "register:40f0:8", ["const:46ad08:8", "const:4:8"]]
- 0046ad08 ["CALL", null, ["callee:0048b0dc:8"]]
+ 0046ad48 ["INT_ADD", "register:40f0:8", ["const:46ad48:8", "const:4:8"]]
+ 0046ad48 ["CALL", null, ["callee:0048b0dc:8"]]
- 0046ad08 bytes e5800094
+ 0046ad48 bytes e5800094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d577756d697b3b2ada81452527f5642e"></a>

### [`0046adf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046adf4.md) → [`0046ae34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046ae34.md) FUN_0046ae34

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005fc360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fc/005fc360.md) · 呼出先 2件 [`0046a9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a9bc.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md)
- 新版 呼出元 1件 [`005fc3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fc/005fc3a0.md) · 呼出先 2件 [`0046a9fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a9fc.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046ae40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046adf4.md#insn-0046ae40) · [`0046ae50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046adf4.md#insn-0046ae50) · [`0046ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046adf4.md#insn-0046ae60)
- 新版 `0046ae80`（命令位置の公開資料なし） · `0046ae90`（命令位置の公開資料なし） · `0046aea0`（命令位置の公開資料なし）

~~~diff
- 0046ae40 ["INT_ADD", "register:40f0:8", ["const:46ae40:8", "const:4:8"]]
- 0046ae40 ["CALL", null, ["callee:00489f4c:8"]]
+ 0046ae80 ["INT_ADD", "register:40f0:8", ["const:46ae80:8", "const:4:8"]]
+ 0046ae80 ["CALL", null, ["callee:00489f4c:8"]]
- 0046ae40 bytes 337c0094
+ 0046ae80 bytes 337c0094
- 0046ae50 ["INT_ADD", "register:40f0:8", ["const:46ae50:8", "const:4:8"]]
- 0046ae50 ["CALL", null, ["callee:00489f4c:8"]]
+ 0046ae90 ["INT_ADD", "register:40f0:8", ["const:46ae90:8", "const:4:8"]]
+ 0046ae90 ["CALL", null, ["callee:00489f4c:8"]]
- 0046ae50 bytes 2f7c0094
+ 0046ae90 bytes 2f7c0094
- 0046ae60 ["INT_ADD", "register:40f0:8", ["const:46ae60:8", "const:4:8"]]
- 0046ae60 ["CALL", null, ["callee:00489f4c:8"]]
+ 0046aea0 ["INT_ADD", "register:40f0:8", ["const:46aea0:8", "const:4:8"]]
+ 0046aea0 ["CALL", null, ["callee:00489f4c:8"]]
- 0046ae60 bytes 2b7c0094
+ 0046aea0 bytes 2b7c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6001d5c91de00d3848a4c6f8255b7d12"></a>

### [`0046aee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aee0.md) → [`0046af20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af20.md) FUN_0046af20

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0046aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aecc.md) [`0046aed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aed8.md) [`008d3700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d3700.md) [`0099b8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0099b/0099b8d4.md) [`00ae0e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0e64.md) · 呼出先 4件 [`00468de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468de0.md) [`0046da04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da04.md) [`0046da1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da1c.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md)
- 新版 呼出元 5件 [`0046af0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af0c.md) [`0046af18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af18.md) [`008d389c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d389c.md) [`0099ba70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0099b/0099ba70.md) [`00ae128c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae1/00ae128c.md) · 呼出先 4件 [`00468e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468e20.md) [`0046da44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046da44.md) [`0046da5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046da5c.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046af4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aee0.md#insn-0046af4c) · [`0046af8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aee0.md#insn-0046af8c) · [`0046afb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aee0.md#insn-0046afb4)
- 新版 `0046af8c`（命令位置の公開資料なし） · `0046afcc`（命令位置の公開資料なし） · `0046aff4`（命令位置の公開資料なし）

~~~diff
- 0046af4c ["INT_ADD", "register:40f0:8", ["const:46af4c:8", "const:4:8"]]
- 0046af4c ["CALL", null, ["callee:0046da5c:8"]]
+ 0046af8c ["INT_ADD", "register:40f0:8", ["const:46af8c:8", "const:4:8"]]
+ 0046af8c ["CALL", null, ["callee:0046da5c:8"]]
- 0046af4c bytes b40a0094
+ 0046af8c bytes b40a0094
- 0046af8c ["INT_ADD", "register:40f0:8", ["const:46af8c:8", "const:4:8"]]
- 0046af8c ["CALL", null, ["callee:0046da44:8"]]
+ 0046afcc ["INT_ADD", "register:40f0:8", ["const:46afcc:8", "const:4:8"]]
+ 0046afcc ["CALL", null, ["callee:0046da44:8"]]
- 0046af8c bytes 9e0a0094
+ 0046afcc bytes 9e0a0094
- 0046afb4 ["INT_ADD", "register:40f0:8", ["const:46afb4:8", "const:4:8"]]
- 0046afb4 ["CALL", null, ["callee:00489f4c:8"]]
+ 0046aff4 ["INT_ADD", "register:40f0:8", ["const:46aff4:8", "const:4:8"]]
+ 0046aff4 ["CALL", null, ["callee:00489f4c:8"]]
- 0046afb4 bytes d67b0094
+ 0046aff4 bytes d67b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d02c33e7552b8db19a5079df20826a2"></a>

### [`0046b19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046b19c.md) → [`0046b1dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b1dc.md) FUN_0046b1dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e3bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e3/008e3bb4.md) · 呼出先 3件 [`00468de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468de0.md) [`0046da50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da50.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md)
- 新版 呼出元 1件 [`008e3d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e3/008e3d50.md) · 呼出先 3件 [`00468e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468e20.md) [`0046da90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046da90.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046b20c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046b19c.md#insn-0046b20c) · [`0046b2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046b19c.md#insn-0046b2dc) · [`0046b33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046b19c.md#insn-0046b33c)
- 新版 `0046b24c`（命令位置の公開資料なし） · `0046b31c`（命令位置の公開資料なし） · `0046b37c`（命令位置の公開資料なし）

~~~diff
- 0046b20c ["INT_ADD", "register:40f0:8", ["const:46b20c:8", "const:4:8"]]
- 0046b20c ["CALL", null, ["callee:0046da90:8"]]
+ 0046b24c ["INT_ADD", "register:40f0:8", ["const:46b24c:8", "const:4:8"]]
+ 0046b24c ["CALL", null, ["callee:0046da90:8"]]
- 0046b20c bytes 110a0094
+ 0046b24c bytes 110a0094
- 0046b2dc ["INT_ADD", "register:40f0:8", ["const:46b2dc:8", "const:4:8"]]
- 0046b2dc ["CALL", null, ["callee:00489f4c:8"]]
+ 0046b31c ["INT_ADD", "register:40f0:8", ["const:46b31c:8", "const:4:8"]]
+ 0046b31c ["CALL", null, ["callee:00489f4c:8"]]
- 0046b2dc bytes 0c7b0094
+ 0046b31c bytes 0c7b0094
- 0046b33c ["INT_ADD", "register:40f0:8", ["const:46b33c:8", "const:4:8"]]
- 0046b33c ["CALL", null, ["callee:00489f4c:8"]]
+ 0046b37c ["INT_ADD", "register:40f0:8", ["const:46b37c:8", "const:4:8"]]
+ 0046b37c ["CALL", null, ["callee:00489f4c:8"]]
- 0046b33c bytes f47a0094
+ 0046b37c bytes f47a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f234b35466fed3f27f15747de9e68fc"></a>

### [`0046b840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046b840.md) → [`0046b880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b880.md) FUN_0046b880

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`005ee590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ee/005ee590.md) [`007f7164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7164.md) [`007f8010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8010.md) [`007f848c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f848c.md) [`007f8674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8674.md) · 呼出先 2件 [`0046b4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046b4c8.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md)
- 新版 呼出元 7件 [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) [`007f71a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f71a4.md) [`007f8050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8050.md) [`007f84cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f84cc.md) [`007f86b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f86b4.md) · 呼出先 2件 [`0046b508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b508.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046b88c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046b840.md#insn-0046b88c) · [`0046b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046b840.md#insn-0046b89c) · [`0046b8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046b840.md#insn-0046b8ac)
- 新版 `0046b8cc`（命令位置の公開資料なし） · `0046b8dc`（命令位置の公開資料なし） · `0046b8ec`（命令位置の公開資料なし）

~~~diff
- 0046b88c ["INT_ADD", "register:40f0:8", ["const:46b88c:8", "const:4:8"]]
- 0046b88c ["CALL", null, ["callee:00489f4c:8"]]
+ 0046b8cc ["INT_ADD", "register:40f0:8", ["const:46b8cc:8", "const:4:8"]]
+ 0046b8cc ["CALL", null, ["callee:00489f4c:8"]]
- 0046b88c bytes a0790094
+ 0046b8cc bytes a0790094
- 0046b89c ["INT_ADD", "register:40f0:8", ["const:46b89c:8", "const:4:8"]]
- 0046b89c ["CALL", null, ["callee:00489f4c:8"]]
+ 0046b8dc ["INT_ADD", "register:40f0:8", ["const:46b8dc:8", "const:4:8"]]
+ 0046b8dc ["CALL", null, ["callee:00489f4c:8"]]
- 0046b89c bytes 9c790094
+ 0046b8dc bytes 9c790094
- 0046b8ac ["INT_ADD", "register:40f0:8", ["const:46b8ac:8", "const:4:8"]]
- 0046b8ac ["CALL", null, ["callee:00489f4c:8"]]
+ 0046b8ec ["INT_ADD", "register:40f0:8", ["const:46b8ec:8", "const:4:8"]]
+ 0046b8ec ["CALL", null, ["callee:00489f4c:8"]]
- 0046b8ac bytes 98790094
+ 0046b8ec bytes 98790094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be6bfb1b85a1a4e56630cd642e65f875"></a>

### [`0046b944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046b944.md) → [`0046b984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b984.md) FUN_0046b984

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007fb1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fb/007fb1f0.md) · 呼出先 2件 [`0046b6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046b6b4.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md)
- 新版 呼出元 1件 [`007fb230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fb230.md) · 呼出先 2件 [`0046b6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b6f4.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046b99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046b944.md#insn-0046b99c) · [`0046b9b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046b944.md#insn-0046b9b0) · [`0046b9c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046b944.md#insn-0046b9c4)
- 新版 `0046b9dc`（命令位置の公開資料なし） · `0046b9f0`（命令位置の公開資料なし） · `0046ba04`（命令位置の公開資料なし）

~~~diff
- 0046b99c ["INT_ADD", "register:40f0:8", ["const:46b99c:8", "const:4:8"]]
- 0046b99c ["CALL", null, ["callee:00489f4c:8"]]
+ 0046b9dc ["INT_ADD", "register:40f0:8", ["const:46b9dc:8", "const:4:8"]]
+ 0046b9dc ["CALL", null, ["callee:00489f4c:8"]]
- 0046b99c bytes 5c790094
+ 0046b9dc bytes 5c790094
- 0046b9b0 ["INT_ADD", "register:40f0:8", ["const:46b9b0:8", "const:4:8"]]
- 0046b9b0 ["CALL", null, ["callee:00489f4c:8"]]
+ 0046b9f0 ["INT_ADD", "register:40f0:8", ["const:46b9f0:8", "const:4:8"]]
+ 0046b9f0 ["CALL", null, ["callee:00489f4c:8"]]
- 0046b9b0 bytes 57790094
+ 0046b9f0 bytes 57790094
- 0046b9c4 ["INT_ADD", "register:40f0:8", ["const:46b9c4:8", "const:4:8"]]
- 0046b9c4 ["CALL", null, ["callee:00489f4c:8"]]
+ 0046ba04 ["INT_ADD", "register:40f0:8", ["const:46ba04:8", "const:4:8"]]
+ 0046ba04 ["CALL", null, ["callee:00489f4c:8"]]
- 0046b9c4 bytes 52790094
+ 0046ba04 bytes 52790094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2541ecf2f8e575a30fcf0a0218322ef3"></a>

### [`0046ba60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046ba60.md) → [`0046baa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046baa0.md) FUN_0046baa0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005ee590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ee/005ee590.md) [`00a79a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a79/00a79a0c.md) · 呼出先 3件 [`0046b4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046b4c8.md) [`0048aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aaf0.md) [`0048aaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aaf8.md)
- 新版 呼出元 2件 [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) [`00a79c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a79/00a79c04.md) · 呼出先 3件 [`0046b508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b508.md) [`0048ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab30.md) [`0048ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab38.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046bab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046ba60.md#insn-0046bab4) · [`0046bac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046ba60.md#insn-0046bac0) · [`0046bb00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046ba60.md#insn-0046bb00)
- 新版 `0046baf4`（命令位置の公開資料なし） · `0046bb00`（命令位置の公開資料なし） · `0046bb40`（命令位置の公開資料なし）

~~~diff
- 0046bab4 ["INT_ADD", "register:40f0:8", ["const:46bab4:8", "const:4:8"]]
- 0046bab4 ["CALL", null, ["callee:0048ab30:8"]]
+ 0046baf4 ["INT_ADD", "register:40f0:8", ["const:46baf4:8", "const:4:8"]]
+ 0046baf4 ["CALL", null, ["callee:0048ab30:8"]]
- 0046bab4 bytes 0f7c0094
+ 0046baf4 bytes 0f7c0094
- 0046bac0 ["INT_ADD", "register:40f0:8", ["const:46bac0:8", "const:4:8"]]
- 0046bac0 ["CALL", null, ["callee:0048ab38:8"]]
+ 0046bb00 ["INT_ADD", "register:40f0:8", ["const:46bb00:8", "const:4:8"]]
+ 0046bb00 ["CALL", null, ["callee:0048ab38:8"]]
- 0046bac0 bytes 0e7c0094
+ 0046bb00 bytes 0e7c0094
- 0046bb00 ["INT_ADD", "register:40f0:8", ["const:46bb00:8", "const:4:8"]]
- 0046bb00 ["CALL", null, ["callee:0046b508:8"]]
+ 0046bb40 ["INT_ADD", "register:40f0:8", ["const:46bb40:8", "const:4:8"]]
+ 0046bb40 ["CALL", null, ["callee:0046b508:8"]]
- 0046bb00 bytes 72feff97
+ 0046bb40 bytes 72feff97
~~~


<a id="compare-0eecea90a8fd203b1da5e023174a0935"></a>

### [`0046bb28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bb28.md) → [`0046bb68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bb68.md) FUN_0046bb68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`005eda3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005eda3c.md) [`005ee590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ee/005ee590.md) [`005f3c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f3/005f3c9c.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 2件 [`0046b4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046b4c8.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md)
- 新版 呼出元 8件 [`005eda7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005eda7c.md) [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) [`005f3cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f3/005f3cdc.md) [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 2件 [`0046b508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b508.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046bb80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bb28.md#insn-0046bb80) · [`0046bb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bb28.md#insn-0046bb90) · [`0046bba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bb28.md#insn-0046bba0)
- 新版 `0046bbc0`（命令位置の公開資料なし） · `0046bbd0`（命令位置の公開資料なし） · `0046bbe0`（命令位置の公開資料なし）

~~~diff
- 0046bb80 ["INT_ADD", "register:40f0:8", ["const:46bb80:8", "const:4:8"]]
- 0046bb80 ["CALL", null, ["callee:00489f4c:8"]]
+ 0046bbc0 ["INT_ADD", "register:40f0:8", ["const:46bbc0:8", "const:4:8"]]
+ 0046bbc0 ["CALL", null, ["callee:00489f4c:8"]]
- 0046bb80 bytes e3780094
+ 0046bbc0 bytes e3780094
- 0046bb90 ["INT_ADD", "register:40f0:8", ["const:46bb90:8", "const:4:8"]]
- 0046bb90 ["CALL", null, ["callee:00489f4c:8"]]
+ 0046bbd0 ["INT_ADD", "register:40f0:8", ["const:46bbd0:8", "const:4:8"]]
+ 0046bbd0 ["CALL", null, ["callee:00489f4c:8"]]
- 0046bb90 bytes df780094
+ 0046bbd0 bytes df780094
- 0046bba0 ["INT_ADD", "register:40f0:8", ["const:46bba0:8", "const:4:8"]]
- 0046bba0 ["CALL", null, ["callee:00489f4c:8"]]
+ 0046bbe0 ["INT_ADD", "register:40f0:8", ["const:46bbe0:8", "const:4:8"]]
+ 0046bbe0 ["CALL", null, ["callee:00489f4c:8"]]
- 0046bba0 bytes db780094
+ 0046bbe0 bytes db780094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-603c1016117073090829f78647f239fb"></a>

### [`0046bc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bc18.md) → [`0046bc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bc58.md) FUN_0046bc58

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005f3c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f3/005f3c9c.md) · 呼出先 2件 [`0046b6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046b6b4.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md)
- 新版 呼出元 1件 [`005f3cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f3/005f3cdc.md) · 呼出先 2件 [`0046b6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b6f4.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046bc78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bc18.md#insn-0046bc78) · [`0046bc88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bc18.md#insn-0046bc88) · [`0046bc98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bc18.md#insn-0046bc98)
- 新版 `0046bcb8`（命令位置の公開資料なし） · `0046bcc8`（命令位置の公開資料なし） · `0046bcd8`（命令位置の公開資料なし）

~~~diff
- 0046bc78 ["INT_ADD", "register:40f0:8", ["const:46bc78:8", "const:4:8"]]
- 0046bc78 ["CALL", null, ["callee:00489f4c:8"]]
+ 0046bcb8 ["INT_ADD", "register:40f0:8", ["const:46bcb8:8", "const:4:8"]]
+ 0046bcb8 ["CALL", null, ["callee:00489f4c:8"]]
- 0046bc78 bytes a5780094
+ 0046bcb8 bytes a5780094
- 0046bc88 ["INT_ADD", "register:40f0:8", ["const:46bc88:8", "const:4:8"]]
- 0046bc88 ["CALL", null, ["callee:00489f4c:8"]]
+ 0046bcc8 ["INT_ADD", "register:40f0:8", ["const:46bcc8:8", "const:4:8"]]
+ 0046bcc8 ["CALL", null, ["callee:00489f4c:8"]]
- 0046bc88 bytes a1780094
+ 0046bcc8 bytes a1780094
- 0046bc98 ["INT_ADD", "register:40f0:8", ["const:46bc98:8", "const:4:8"]]
- 0046bc98 ["CALL", null, ["callee:00489f4c:8"]]
+ 0046bcd8 ["INT_ADD", "register:40f0:8", ["const:46bcd8:8", "const:4:8"]]
+ 0046bcd8 ["CALL", null, ["callee:00489f4c:8"]]
- 0046bc98 bytes 9d780094
+ 0046bcd8 bytes 9d780094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-226b2e645450d761308318d028aa08fc"></a>

### [`0046bd34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd34.md) → [`0046bd74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bd74.md) FUN_0046bd74

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0046bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd14.md) · 呼出先 3件 [`0046e548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e548.md) [`0055cf0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cf0c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0046bd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bd54.md) · 呼出先 3件 [`0046e588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e588.md) [`0055cf4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cf4c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046bdbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd34.md#insn-0046bdbc) · [`0046be00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd34.md#insn-0046be00) · [`0046be34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd34.md#insn-0046be34)
- 新版 `0046bdfc`（命令位置の公開資料なし） · `0046be40`（命令位置の公開資料なし） · `0046be74`（命令位置の公開資料なし）

~~~diff
- 0046bdbc ["INT_ADD", "register:40f0:8", ["const:46bdbc:8", "const:4:8"]]
- 0046bdbc ["CALL", null, ["callee:0046e588:8"]]
+ 0046bdfc ["INT_ADD", "register:40f0:8", ["const:46bdfc:8", "const:4:8"]]
+ 0046bdfc ["CALL", null, ["callee:0046e588:8"]]
- 0046bdbc bytes e3090094
+ 0046bdfc bytes e3090094
- 0046be00 ["INT_ADD", "register:40f0:8", ["const:46be00:8", "const:4:8"]]
- 0046be00 ["CALL", null, ["callee:0055cf4c:8"]]
+ 0046be40 ["INT_ADD", "register:40f0:8", ["const:46be40:8", "const:4:8"]]
+ 0046be40 ["CALL", null, ["callee:0055cf4c:8"]]
- 0046be00 bytes 43c40394
+ 0046be40 bytes 43c40394
- 0046be34 ["INT_ADD", "register:40f0:8", ["const:46be34:8", "const:4:8"]]
- 0046be34 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0046be74 ["INT_ADD", "register:40f0:8", ["const:46be74:8", "const:4:8"]]
+ 0046be74 ["CALL", null, ["callee:00c57ee0:8"]]
- 0046be34 bytes 2baf1f94
+ 0046be74 bytes 1bb01f94
~~~


<a id="compare-ff5179fc4db40366e727d9c1803ecf40"></a>

### [`0046be38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046be38.md) → [`0046be78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046be78.md) FUN_0046be78

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 3件 [`0046ac60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046ac60.md) [`0055cf0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cf0c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) · 呼出先 3件 [`0046aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046aca0.md) [`0055cf4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cf4c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046bfd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046be38.md#insn-0046bfd8) · [`0046c0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046be38.md#insn-0046c0a0) · [`0046c0e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046be38.md#insn-0046c0e4)
- 新版 `0046c018`（命令位置の公開資料なし） · `0046c0e0`（命令位置の公開資料なし） · `0046c124`（命令位置の公開資料なし）

~~~diff
- 0046bfd8 ["INT_ADD", "register:40f0:8", ["const:46bfd8:8", "const:4:8"]]
- 0046bfd8 ["CALL", null, ["callee:0046aca0:8"]]
+ 0046c018 ["INT_ADD", "register:40f0:8", ["const:46c018:8", "const:4:8"]]
+ 0046c018 ["CALL", null, ["callee:0046aca0:8"]]
- 0046bfd8 bytes 22fbff97
+ 0046c018 bytes 22fbff97
- 0046c0a0 ["INT_ADD", "register:40f0:8", ["const:46c0a0:8", "const:4:8"]]
- 0046c0a0 ["CALL", null, ["callee:0055cf4c:8"]]
+ 0046c0e0 ["INT_ADD", "register:40f0:8", ["const:46c0e0:8", "const:4:8"]]
+ 0046c0e0 ["CALL", null, ["callee:0055cf4c:8"]]
- 0046c0a0 bytes 9bc30394
+ 0046c0e0 bytes 9bc30394
- 0046c0e4 ["INT_ADD", "register:40f0:8", ["const:46c0e4:8", "const:4:8"]]
- 0046c0e4 ["CALL", null, ["callee:0055cf4c:8"]]
+ 0046c124 ["INT_ADD", "register:40f0:8", ["const:46c124:8", "const:4:8"]]
+ 0046c124 ["CALL", null, ["callee:0055cf4c:8"]]
- 0046c0e4 bytes 8ac30394
+ 0046c124 bytes 8ac30394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd9983a221e9a31fcc2fabebb46d7039"></a>

### [`0046c128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c128.md) → [`0046c168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c168.md) FUN_0046c168

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046c144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c128.md#insn-0046c144) · [`0046c164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c128.md#insn-0046c164)
- 新版 `0046c184`（命令位置の公開資料なし） · `0046c1a4`（命令位置の公開資料なし）

~~~diff
- 0046c144 ["INT_ADD", "register:40f0:8", ["const:46c144:8", "const:4:8"]]
- 0046c144 ["CALL", null, ["callee:00c53d00:8"]]
+ 0046c184 ["INT_ADD", "register:40f0:8", ["const:46c184:8", "const:4:8"]]
+ 0046c184 ["CALL", null, ["callee:00c53d00:8"]]
- 0046c144 bytes e79d1f94
+ 0046c184 bytes df9e1f94
- 0046c164 ["COPY", "register:0:8", ["register:4040:8"]]
- 0046c164 ["INT_ADD", "register:40f0:8", ["const:46c164:8", "const:4:8"]]
- 0046c164 ["CALLIND", null, ["register:0:8"]]
+ 0046c1a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046c1a4 ["INT_ADD", "register:40f0:8", ["const:46c1a4:8", "const:4:8"]]
+ 0046c1a4 ["CALLIND", null, ["register:0:8"]]
- 0046c164 bytes 00013fd6
+ 0046c1a4 bytes 00013fd6
~~~


<a id="compare-54756b3bb4029838813e35311a32daae"></a>

### [`0046c178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c178.md) → [`0046c1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c1b8.md) FUN_0046c1b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0048ac50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ac50.md) [`0048ae98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ae98.md) [`0048b09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b09c.md) [`0048b210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b210.md) · 呼出先 3件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 4件 [`0048ac90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ac90.md) [`0048aed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aed8.md) [`0048b0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b0dc.md) [`0048b250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b250.md) · 呼出先 3件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046c19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c178.md#insn-0046c19c) · [`0046c1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c178.md#insn-0046c1b4) · [`0046c1d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c178.md#insn-0046c1d8)
- 新版 `0046c1dc`（命令位置の公開資料なし） · `0046c1f4`（命令位置の公開資料なし） · `0046c218`（命令位置の公開資料なし）

~~~diff
- 0046c19c ["INT_ADD", "register:40f0:8", ["const:46c19c:8", "const:4:8"]]
- 0046c19c ["CALL", null, ["callee:00c53cd0:8"]]
+ 0046c1dc ["INT_ADD", "register:40f0:8", ["const:46c1dc:8", "const:4:8"]]
+ 0046c1dc ["CALL", null, ["callee:00c53cd0:8"]]
- 0046c19c bytes c59d1f94
+ 0046c1dc bytes bd9e1f94
- 0046c1b4 ["INT_ADD", "register:40f0:8", ["const:46c1b4:8", "const:4:8"]]
- 0046c1b4 ["CALL", null, ["callee:00c53d00:8"]]
+ 0046c1f4 ["INT_ADD", "register:40f0:8", ["const:46c1f4:8", "const:4:8"]]
+ 0046c1f4 ["CALL", null, ["callee:00c53d00:8"]]
- 0046c1b4 bytes cb9d1f94
+ 0046c1f4 bytes c39e1f94
- 0046c1d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0046c1d8 ["INT_ADD", "register:40f0:8", ["const:46c1d8:8", "const:4:8"]]
- 0046c1d8 ["CALLIND", null, ["register:0:8"]]
+ 0046c218 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046c218 ["INT_ADD", "register:40f0:8", ["const:46c218:8", "const:4:8"]]
+ 0046c218 ["CALLIND", null, ["register:0:8"]]
- 0046c1d8 bytes 00013fd6
+ 0046c218 bytes 00013fd6
~~~


<a id="compare-c0b771c3877cbb573bf0840e80129cb7"></a>

### [`0046c1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c1f0.md) → [`0046c230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c230.md) FUN_0046c230

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0048ac50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ac50.md) [`0048ae98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ae98.md) [`0048b09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b09c.md) [`0048b210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b210.md) · 呼出先 5件 [`0046c434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c434.md) [`0055cd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cd40.md) [`0055cef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055cef8.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 4件 [`0048ac90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ac90.md) [`0048aed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aed8.md) [`0048b0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b0dc.md) [`0048b250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b250.md) · 呼出先 5件 [`0046c474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c474.md) [`0055cd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cd80.md) [`0055cf38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cf38.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046c2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c1f0.md#insn-0046c2dc) · [`0046c2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c1f0.md#insn-0046c2f4) · [`0046c338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c1f0.md#insn-0046c338)
- 新版 `0046c31c`（命令位置の公開資料なし） · `0046c334`（命令位置の公開資料なし） · `0046c378`（命令位置の公開資料なし）

~~~diff
- 0046c2dc ["INT_ADD", "register:40f0:8", ["const:46c2dc:8", "const:4:8"]]
- 0046c2dc ["CALL", null, ["callee:0055cf38:8"]]
+ 0046c31c ["INT_ADD", "register:40f0:8", ["const:46c31c:8", "const:4:8"]]
+ 0046c31c ["CALL", null, ["callee:0055cf38:8"]]
- 0046c2dc bytes 07c30394
+ 0046c31c bytes 07c30394
- 0046c2f4 ["INT_ADD", "register:40f0:8", ["const:46c2f4:8", "const:4:8"]]
- 0046c2f4 ["CALL", null, ["callee:0055cf38:8"]]
+ 0046c334 ["INT_ADD", "register:40f0:8", ["const:46c334:8", "const:4:8"]]
+ 0046c334 ["CALL", null, ["callee:0055cf38:8"]]
- 0046c2f4 bytes 01c30394
+ 0046c334 bytes 01c30394
- 0046c338 ["INT_ADD", "register:40f0:8", ["const:46c338:8", "const:4:8"]]
- 0046c338 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0046c378 ["INT_ADD", "register:40f0:8", ["const:46c378:8", "const:4:8"]]
+ 0046c378 ["CALL", null, ["callee:00c53cd0:8"]]
- 0046c338 bytes 5e9d1f94
+ 0046c378 bytes 569e1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfe4355f24a06d7f944da81c32ede439"></a>

### [`0046c434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c434.md) → [`0046c474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c474.md) FUN_0046c474

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0046c1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c1f0.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046c5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c5d4.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0046c230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c230.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046c614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c614.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046c4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c434.md#insn-0046c4b0) · [`0046c4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c434.md#insn-0046c4f0) · [`0046c56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c434.md#insn-0046c56c)
- 新版 `0046c4f0`（命令位置の公開資料なし） · `0046c530`（命令位置の公開資料なし） · `0046c5ac`（命令位置の公開資料なし）

~~~diff
- 0046c4b0 ["INT_ADD", "register:40f0:8", ["const:46c4b0:8", "const:4:8"]]
- 0046c4b0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0046c4f0 ["INT_ADD", "register:40f0:8", ["const:46c4f0:8", "const:4:8"]]
+ 0046c4f0 ["CALL", null, ["callee:00c57e90:8"]]
- 0046c4b0 bytes 78ad1f94
+ 0046c4f0 bytes 68ae1f94
- 0046c4f0 ["INT_ADD", "register:40f0:8", ["const:46c4f0:8", "const:4:8"]]
- 0046c4f0 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0046c530 ["INT_ADD", "register:40f0:8", ["const:46c530:8", "const:4:8"]]
+ 0046c530 ["CALL", null, ["callee:00c53cd0:8"]]
- 0046c4f0 bytes f09c1f94
+ 0046c530 bytes e89d1f94
- 0046c56c ["INT_ADD", "register:40f0:8", ["const:46c56c:8", "const:4:8"]]
- 0046c56c ["CALL", null, ["callee:00c53d00:8"]]
+ 0046c5ac ["INT_ADD", "register:40f0:8", ["const:46c5ac:8", "const:4:8"]]
+ 0046c5ac ["CALL", null, ["callee:00c53d00:8"]]
- 0046c56c bytes dd9c1f94
+ 0046c5ac bytes d59d1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c15902bf0eb1c103938be08fa98559f4"></a>

### [`0046d3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d3bc.md) → [`0046d3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d3fc.md) FUN_0046d3fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0046d66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d66c.md)
- 新版 呼出元 1件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0046d6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d6ac.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046d3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d3bc.md#insn-0046d3d8)
- 新版 `0046d418`（命令位置の公開資料なし）

~~~diff
- 0046d3d8 ["INT_ADD", "register:40f0:8", ["const:46d3d8:8", "const:4:8"]]
- 0046d3d8 ["CALL", null, ["callee:0046d6ac:8"]]
+ 0046d418 ["INT_ADD", "register:40f0:8", ["const:46d418:8", "const:4:8"]]
+ 0046d418 ["CALL", null, ["callee:0046d6ac:8"]]
- 0046d3d8 bytes a5000094
+ 0046d418 bytes a5000094
~~~


<a id="compare-0fb2cfce24515294296b4b8c3a657228"></a>

### [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) → [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) FUN_0046d490

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 130件 [`0046d0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d0d8.md) [`0046d0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d0e0.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0048dd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dd00.md) [`00493c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493c38.md) · 呼出先 2件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 129件 [`0046d118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d118.md) [`0046d120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d120.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0048dd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dd40.md) [`00493c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493c78.md) · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046d46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md#insn-0046d46c) · [`0046d478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md#insn-0046d478) · [`0046d488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md#insn-0046d488)
- 新版 `0046d4ac`（命令位置の公開資料なし） · `0046d4b8`（命令位置の公開資料なし） · `0046d4c8`（命令位置の公開資料なし）

~~~diff
- 0046d46c ["INT_ADD", "register:40f0:8", ["const:46d46c:8", "const:4:8"]]
- 0046d46c ["CALL", null, ["local:b0:8"]]
+ 0046d4ac ["INT_ADD", "register:40f0:8", ["const:46d4ac:8", "const:4:8"]]
+ 0046d4ac ["CALL", null, ["local:b0:8"]]
- 0046d46c bytes f9ffff97
+ 0046d4ac bytes f9ffff97
- 0046d478 ["INT_ADD", "register:40f0:8", ["const:46d478:8", "const:4:8"]]
- 0046d478 ["CALL", null, ["local:b0:8"]]
+ 0046d4b8 ["INT_ADD", "register:40f0:8", ["const:46d4b8:8", "const:4:8"]]
+ 0046d4b8 ["CALL", null, ["local:b0:8"]]
- 0046d478 bytes f6ffff97
+ 0046d4b8 bytes f6ffff97
- 0046d488 ["INT_ADD", "register:40f0:8", ["const:46d488:8", "const:4:8"]]
- 0046d488 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0046d4c8 ["INT_ADD", "register:40f0:8", ["const:46d4c8:8", "const:4:8"]]
+ 0046d4c8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0046d488 bytes 8aa91f94
+ 0046d4c8 bytes 7aaa1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e50d24f19f636682899c6bd89bb3b08"></a>

### [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) → [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) FUN_0046d5a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 21件 [`0046d0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d0e0.md) [`00494c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494c3c.md) [`00510020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510020.md) [`0054a7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a7a4.md) [`0054f154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f154.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 21件 [`0046d120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d120.md) [`00494c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494c7c.md) [`00510060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510060.md) [`0054a7e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a7e4.md) [`0054f194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054f/0054f194.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046d5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md#insn-0046d5ec) · [`0046d618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md#insn-0046d618)
- 新版 `0046d62c`（命令位置の公開資料なし） · `0046d658`（命令位置の公開資料なし）

~~~diff
- 0046d5ec ["INT_ADD", "register:40f0:8", ["const:46d5ec:8", "const:4:8"]]
- 0046d5ec ["CALL", null, ["callee:00c58050:8"]]
+ 0046d62c ["INT_ADD", "register:40f0:8", ["const:46d62c:8", "const:4:8"]]
+ 0046d62c ["CALL", null, ["callee:00c58050:8"]]
- 0046d5ec bytes 99a91f94
+ 0046d62c bytes 89aa1f94
- 0046d618 ["INT_ADD", "register:40f0:8", ["const:46d618:8", "const:4:8"]]
- 0046d618 ["CALL", null, ["callee:00c58050:8"]]
+ 0046d658 ["INT_ADD", "register:40f0:8", ["const:46d658:8", "const:4:8"]]
+ 0046d658 ["CALL", null, ["callee:00c58050:8"]]
- 0046d618 bytes 8ea91f94
+ 0046d658 bytes 7eaa1f94
~~~


<a id="compare-2fe8c66dfa27cd5c21a7ad262790e20c"></a>

### [`0046d66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d66c.md) → [`0046d6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d6ac.md) FUN_0046d6ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0046d3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d3bc.md) [`008648d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00864/008648d0.md) [`0088f2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f2b4.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 3件 [`0046d3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d3fc.md) [`00864910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00864/00864910.md) [`0088f2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f2f4.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046d6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d66c.md#insn-0046d6d8) · [`0046d734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d66c.md#insn-0046d734)
- 新版 `0046d718`（命令位置の公開資料なし） · `0046d774`（命令位置の公開資料なし）

~~~diff
- 0046d6d8 ["INT_ADD", "register:40f0:8", ["const:46d6d8:8", "const:4:8"]]
- 0046d6d8 ["CALL", null, ["callee:00c58050:8"]]
+ 0046d718 ["INT_ADD", "register:40f0:8", ["const:46d718:8", "const:4:8"]]
+ 0046d718 ["CALL", null, ["callee:00c58050:8"]]
- 0046d6d8 bytes 5ea91f94
+ 0046d718 bytes 4eaa1f94
- 0046d734 ["INT_ADD", "register:40f0:8", ["const:46d734:8", "const:4:8"]]
- 0046d734 ["CALL", null, ["callee:00c58050:8"]]
+ 0046d774 ["INT_ADD", "register:40f0:8", ["const:46d774:8", "const:4:8"]]
+ 0046d774 ["CALL", null, ["callee:00c58050:8"]]
- 0046d734 bytes 47a91f94
+ 0046d774 bytes 37aa1f94
~~~


<a id="compare-5b9d0c159211a7bb602fac4fda57e586"></a>

### [`0046dde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dde4.md) → [`0046de24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046de24.md) FUN_0046de24

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0046f71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f71c.md) · 呼出先 12件 [`00467610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467610.md) [`00467660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467660.md) [`004676d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004676d8.md) [`004677a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004677a0.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md)
- 新版 呼出元 1件 [`0046f75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f75c.md) · 呼出先 12件 [`00467650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467650.md) [`004676a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/004676a0.md) [`00467718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467718.md) [`004677e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/004677e0.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046df74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dde4.md#insn-0046df74) · [`0046df80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dde4.md#insn-0046df80) · [`0046dfa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dde4.md#insn-0046dfa4)
- 新版 `0046dfb4`（命令位置の公開資料なし） · `0046dfc0`（命令位置の公開資料なし） · `0046dfe4`（命令位置の公開資料なし）

~~~diff
- 0046df74 ["INT_ADD", "register:40f0:8", ["const:46df74:8", "const:4:8"]]
- 0046df74 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0046dfb4 ["INT_ADD", "register:40f0:8", ["const:46dfb4:8", "const:4:8"]]
+ 0046dfb4 ["CALL", null, ["callee:00c53cd0:8"]]
- 0046df74 bytes 4f961f94
+ 0046dfb4 bytes 47971f94
- 0046df80 ["INT_ADD", "register:40f0:8", ["const:46df80:8", "const:4:8"]]
- 0046df80 ["CALL", null, ["callee:00c53d00:8"]]
+ 0046dfc0 ["INT_ADD", "register:40f0:8", ["const:46dfc0:8", "const:4:8"]]
+ 0046dfc0 ["CALL", null, ["callee:00c53d00:8"]]
- 0046df80 bytes 58961f94
+ 0046dfc0 bytes 50971f94
- 0046dfa4 ["INT_ADD", "register:40f0:8", ["const:46dfa4:8", "const:4:8"]]
- 0046dfa4 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0046dfe4 ["INT_ADD", "register:40f0:8", ["const:46dfe4:8", "const:4:8"]]
+ 0046dfe4 ["CALL", null, ["callee:00c53cd0:8"]]
- 0046dfa4 bytes 43961f94
+ 0046dfe4 bytes 3b971f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82b7eabfea69f0bc8e71e32458ca4c48"></a>

### [`0046e4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e4f8.md) → [`0046e538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e538.md) FUN_0046e538

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 30件 [`005e30d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e3/005e30d4.md) [`005eda3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005eda3c.md) [`005ee590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ee/005ee590.md) [`005ef56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ef/005ef56c.md) [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 30件 [`005e3114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e3/005e3114.md) [`005eda7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005eda7c.md) [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) [`005ef5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ef/005ef5ac.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046e514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e4f8.md#insn-0046e514) · [`0046e534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e4f8.md#insn-0046e534)
- 新版 `0046e554`（命令位置の公開資料なし） · `0046e574`（命令位置の公開資料なし）

~~~diff
- 0046e514 ["INT_ADD", "register:40f0:8", ["const:46e514:8", "const:4:8"]]
- 0046e514 ["CALL", null, ["callee:00c53d00:8"]]
+ 0046e554 ["INT_ADD", "register:40f0:8", ["const:46e554:8", "const:4:8"]]
+ 0046e554 ["CALL", null, ["callee:00c53d00:8"]]
- 0046e514 bytes f3941f94
+ 0046e554 bytes eb951f94
- 0046e534 ["COPY", "register:0:8", ["register:4040:8"]]
- 0046e534 ["INT_ADD", "register:40f0:8", ["const:46e534:8", "const:4:8"]]
- 0046e534 ["CALLIND", null, ["register:0:8"]]
+ 0046e574 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046e574 ["INT_ADD", "register:40f0:8", ["const:46e574:8", "const:4:8"]]
+ 0046e574 ["CALLIND", null, ["register:0:8"]]
- 0046e534 bytes 00013fd6
+ 0046e574 bytes 00013fd6
~~~


<a id="compare-f22c515dad8b8af58b35ed49dafefc70"></a>

### [`0046e548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e548.md) → [`0046e588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e588.md) FUN_0046e588

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0046bd34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd34.md) · 呼出先 7件 [`00467ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467ab0.md) [`00468b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468b9c.md) [`0046ac60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046ac60.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`0046bd74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bd74.md) · 呼出先 7件 [`00467af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467af0.md) [`00468bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md) [`0046aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046aca0.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046e5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e548.md#insn-0046e5a4) · [`0046e5c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e548.md#insn-0046e5c4) · [`0046e5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e548.md#insn-0046e5e4)
- 新版 `0046e5e4`（命令位置の公開資料なし） · `0046e604`（命令位置の公開資料なし） · `0046e624`（命令位置の公開資料なし）

~~~diff
- 0046e5a4 ["INT_ADD", "register:40f0:8", ["const:46e5a4:8", "const:4:8"]]
- 0046e5a4 ["CALL", null, ["callee:00467af0:8"]]
+ 0046e5e4 ["INT_ADD", "register:40f0:8", ["const:46e5e4:8", "const:4:8"]]
+ 0046e5e4 ["CALL", null, ["callee:00467af0:8"]]
- 0046e5a4 bytes 43e5ff97
+ 0046e5e4 bytes 43e5ff97
- 0046e5c4 ["INT_ADD", "register:40f0:8", ["const:46e5c4:8", "const:4:8"]]
- 0046e5c4 ["CALL", null, ["callee:00468bdc:8"]]
+ 0046e604 ["INT_ADD", "register:40f0:8", ["const:46e604:8", "const:4:8"]]
+ 0046e604 ["CALL", null, ["callee:00468bdc:8"]]
- 0046e5c4 bytes 76e9ff97
+ 0046e604 bytes 76e9ff97
- 0046e5e4 ["INT_ADD", "register:40f0:8", ["const:46e5e4:8", "const:4:8"]]
- 0046e5e4 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0046e624 ["INT_ADD", "register:40f0:8", ["const:46e624:8", "const:4:8"]]
+ 0046e624 ["CALL", null, ["callee:00c53cd0:8"]]
- 0046e5e4 bytes b3941f94
+ 0046e624 bytes ab951f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad6df9d381af6d10ba485abcbb801ba4"></a>

### [`0046e7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e7ec.md) → [`0046e82c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e82c.md) FUN_0046e82c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007f1a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1a78.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`007f1ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ab8.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046e834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e7ec.md#insn-0046e834)
- 新版 `0046e874`（命令位置の公開資料なし）

~~~diff
- 0046e834 ["INT_ADD", "register:40f0:8", ["const:46e834:8", "const:4:8"]]
- 0046e834 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0046e874 ["INT_ADD", "register:40f0:8", ["const:46e874:8", "const:4:8"]]
+ 0046e874 ["CALL", null, ["callee:00c57eb0:8"]]
- 0046e834 bytes 9fa41f94
+ 0046e874 bytes 8fa51f94
~~~


<a id="compare-41fd4b984fce9463e946c480e0afccff"></a>

### [`0046f62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f62c.md) → [`0046f66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f66c.md) FUN_0046f66c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 13件 [`005eda3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005eda3c.md) [`005ee590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ee/005ee590.md) [`005ef56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ef/005ef56c.md) [`006dc900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc900.md) [`0078c1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078c/0078c1dc.md) · 呼出先 3件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 13件 [`005eda7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005eda7c.md) [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) [`005ef5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ef/005ef5ac.md) [`006dc940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006dc/006dc940.md) [`0078c21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078c/0078c21c.md) · 呼出先 3件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046f650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f62c.md#insn-0046f650) · [`0046f668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f62c.md#insn-0046f668) · [`0046f68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f62c.md#insn-0046f68c)
- 新版 `0046f690`（命令位置の公開資料なし） · `0046f6a8`（命令位置の公開資料なし） · `0046f6cc`（命令位置の公開資料なし）

~~~diff
- 0046f650 ["INT_ADD", "register:40f0:8", ["const:46f650:8", "const:4:8"]]
- 0046f650 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0046f690 ["INT_ADD", "register:40f0:8", ["const:46f690:8", "const:4:8"]]
+ 0046f690 ["CALL", null, ["callee:00c53cd0:8"]]
- 0046f650 bytes 98901f94
+ 0046f690 bytes 90911f94
- 0046f668 ["INT_ADD", "register:40f0:8", ["const:46f668:8", "const:4:8"]]
- 0046f668 ["CALL", null, ["callee:00c53d00:8"]]
+ 0046f6a8 ["INT_ADD", "register:40f0:8", ["const:46f6a8:8", "const:4:8"]]
+ 0046f6a8 ["CALL", null, ["callee:00c53d00:8"]]
- 0046f668 bytes 9e901f94
+ 0046f6a8 bytes 96911f94
- 0046f68c ["COPY", "register:0:8", ["register:4040:8"]]
- 0046f68c ["INT_ADD", "register:40f0:8", ["const:46f68c:8", "const:4:8"]]
- 0046f68c ["CALLIND", null, ["register:0:8"]]
+ 0046f6cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046f6cc ["INT_ADD", "register:40f0:8", ["const:46f6cc:8", "const:4:8"]]
+ 0046f6cc ["CALLIND", null, ["register:0:8"]]
- 0046f68c bytes 00013fd6
+ 0046f6cc bytes 00013fd6
~~~


<a id="compare-69b9724a21db08da0299fc1ee0439d59"></a>

### [`0046f6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f6a4.md) → [`0046f6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f6e4.md) FUN_0046f6e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 31件 [`005e1b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1b78.md) [`005e30d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e3/005e30d4.md) [`005eda3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005eda3c.md) [`005ee590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ee/005ee590.md) [`005ef56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ef/005ef56c.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 31件 [`005e1bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1bb8.md) [`005e3114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e3/005e3114.md) [`005eda7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005eda7c.md) [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) [`005ef5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ef/005ef5ac.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046f6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f6a4.md#insn-0046f6d0) · [`0046f6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f6a4.md#insn-0046f6e4) · [`0046f6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f6a4.md#insn-0046f6ec)
- 新版 `0046f710`（命令位置の公開資料なし） · `0046f724`（命令位置の公開資料なし） · `0046f72c`（命令位置の公開資料なし）

~~~diff
- 0046f6d0 ["INT_ADD", "register:40f0:8", ["const:46f6d0:8", "const:4:8"]]
- 0046f6d0 ["CALL", null, ["callee:00c53d00:8"]]
+ 0046f710 ["INT_ADD", "register:40f0:8", ["const:46f710:8", "const:4:8"]]
+ 0046f710 ["CALL", null, ["callee:00c53d00:8"]]
- 0046f6d0 bytes 84901f94
+ 0046f710 bytes 7c911f94
- 0046f6e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0046f6e4 ["INT_ADD", "register:40f0:8", ["const:46f6e4:8", "const:4:8"]]
- 0046f6e4 ["CALLIND", null, ["register:0:8"]]
+ 0046f724 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046f724 ["INT_ADD", "register:40f0:8", ["const:46f724:8", "const:4:8"]]
+ 0046f724 ["CALLIND", null, ["register:0:8"]]
- 0046f6e4 bytes 00013fd6
+ 0046f724 bytes 00013fd6
- 0046f6ec ["INT_ADD", "register:40f0:8", ["const:46f6ec:8", "const:4:8"]]
- 0046f6ec ["CALL", null, ["callee:00c57e80:8"]]
+ 0046f72c ["INT_ADD", "register:40f0:8", ["const:46f72c:8", "const:4:8"]]
+ 0046f72c ["CALL", null, ["callee:00c57e80:8"]]
- 0046f6ec bytes e5a01f94
+ 0046f72c bytes d5a11f94
~~~


