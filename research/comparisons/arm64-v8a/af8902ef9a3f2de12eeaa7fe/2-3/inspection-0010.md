# v16.0.0 → v16.0.1 · 要調査の変更候補 (10)

[一覧の目次](README.md)

<a id="compare-6ed542e0e89b3df111cef14caa7cba9b"></a>

### [`005331dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005331dc.md) → [`0053321c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/0053321c.md) FUN_0053321c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005331f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005331dc.md#insn-005331f8) · [`00533210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005331dc.md#insn-00533210)
- 新版 `00533238`（命令位置の公開資料なし） · `00533250`（命令位置の公開資料なし）

~~~diff
- 005331f8 ["INT_ADD", "register:40f0:8", ["const:5331f8:8", "const:4:8"]]
- 005331f8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00533238 ["INT_ADD", "register:40f0:8", ["const:533238:8", "const:4:8"]]
+ 00533238 ["CALL", null, ["callee:00c57eb0:8"]]
- 005331f8 bytes 2e921c94
+ 00533238 bytes 1e931c94
- 00533210 ["COPY", "register:0:8", ["register:4040:8"]]
- 00533210 ["INT_ADD", "register:40f0:8", ["const:533210:8", "const:4:8"]]
- 00533210 ["CALLIND", null, ["register:0:8"]]
+ 00533250 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00533250 ["INT_ADD", "register:40f0:8", ["const:533250:8", "const:4:8"]]
+ 00533250 ["CALLIND", null, ["register:0:8"]]
- 00533210 bytes 00013fd6
+ 00533250 bytes 00013fd6
~~~


<a id="compare-208d465883ca2fbb9e433f37201eeecf"></a>

### [`00533224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533224.md) → [`00533264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533264.md) FUN_00533264

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c59110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59110.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c59510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59510.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00533238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533224.md#insn-00533238) · [`00533250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533224.md#insn-00533250) · [`0053325c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533224.md#insn-0053325c)
- 新版 `00533278`（命令位置の公開資料なし） · `00533290`（命令位置の公開資料なし） · `0053329c`（命令位置の公開資料なし）

~~~diff
- 00533238 ["INT_ADD", "register:40f0:8", ["const:533238:8", "const:4:8"]]
- 00533238 ["CALL", null, ["callee:00c57e90:8"]]
+ 00533278 ["INT_ADD", "register:40f0:8", ["const:533278:8", "const:4:8"]]
+ 00533278 ["CALL", null, ["callee:00c57e90:8"]]
- 00533238 bytes 16921c94
+ 00533278 bytes 06931c94
- 00533250 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533250 ["INT_ADD", "register:40f0:8", ["const:533250:8", "const:4:8"]]
- 00533250 ["CALLIND", null, ["register:0:8"]]
+ 00533290 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533290 ["INT_ADD", "register:40f0:8", ["const:533290:8", "const:4:8"]]
+ 00533290 ["CALLIND", null, ["register:0:8"]]
- 00533250 bytes 20013fd6
+ 00533290 bytes 20013fd6
- 0053325c ["INT_ADD", "register:40f0:8", ["const:53325c:8", "const:4:8"]]
- 0053325c ["CALL", null, ["callee:00c59510:8"]]
+ 0053329c ["INT_ADD", "register:40f0:8", ["const:53329c:8", "const:4:8"]]
+ 0053329c ["CALL", null, ["callee:00c59510:8"]]
- 0053325c bytes ad971c94
+ 0053329c bytes 9d981c94
~~~


<a id="compare-98651cdd9517e8078350a73eddcc12de"></a>

### [`00533378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533378.md) → [`005333b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/005333b8.md) FUN_005333b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59100.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59500.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053339c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533378.md#insn-0053339c) · [`005333ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533378.md#insn-005333ac) · [`005333bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533378.md#insn-005333bc)
- 新版 `005333dc`（命令位置の公開資料なし） · `005333ec`（命令位置の公開資料なし） · `005333fc`（命令位置の公開資料なし）

~~~diff
- 0053339c ["INT_ADD", "register:40f0:8", ["const:53339c:8", "const:4:8"]]
- 0053339c ["CALL", null, ["callee:00c57e90:8"]]
+ 005333dc ["INT_ADD", "register:40f0:8", ["const:5333dc:8", "const:4:8"]]
+ 005333dc ["CALL", null, ["callee:00c57e90:8"]]
- 0053339c bytes bd911c94
+ 005333dc bytes ad921c94
- 005333ac ["INT_ADD", "register:40f0:8", ["const:5333ac:8", "const:4:8"]]
- 005333ac ["CALL", null, ["callee:00c59500:8"]]
+ 005333ec ["INT_ADD", "register:40f0:8", ["const:5333ec:8", "const:4:8"]]
+ 005333ec ["CALL", null, ["callee:00c59500:8"]]
- 005333ac bytes 55971c94
+ 005333ec bytes 45981c94
- 005333bc ["INT_ADD", "register:40f0:8", ["const:5333bc:8", "const:4:8"]]
- 005333bc ["CALL", null, ["callee:00c57eb0:8"]]
+ 005333fc ["INT_ADD", "register:40f0:8", ["const:5333fc:8", "const:4:8"]]
+ 005333fc ["CALL", null, ["callee:00c57eb0:8"]]
- 005333bc bytes bd911c94
+ 005333fc bytes ad921c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f7c3e941719cfdb8b865bde8b1a4d5a"></a>

### [`0053353c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/0053353c.md) → [`0053357c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/0053357c.md) FUN_0053357c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00533564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/0053353c.md#insn-00533564)
- 新版 `005335a4`（命令位置の公開資料なし）

~~~diff
- 00533564 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533564 ["INT_ADD", "register:40f0:8", ["const:533564:8", "const:4:8"]]
- 00533564 ["CALLIND", null, ["register:0:8"]]
+ 005335a4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005335a4 ["INT_ADD", "register:40f0:8", ["const:5335a4:8", "const:4:8"]]
+ 005335a4 ["CALLIND", null, ["register:0:8"]]
- 00533564 bytes 20013fd6
+ 005335a4 bytes 20013fd6
~~~


<a id="compare-38a27eeebdddfb93d990f7fb30503e87"></a>

### [`00533578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533578.md) → [`005335b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/005335b8.md) FUN_005335b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c59120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59120.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c59520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59520.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053358c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533578.md#insn-0053358c) · [`005335a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533578.md#insn-005335a4) · [`005335b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533578.md#insn-005335b4)
- 新版 `005335cc`（命令位置の公開資料なし） · `005335e4`（命令位置の公開資料なし） · `005335f4`（命令位置の公開資料なし）

~~~diff
- 0053358c ["INT_ADD", "register:40f0:8", ["const:53358c:8", "const:4:8"]]
- 0053358c ["CALL", null, ["callee:00c57e90:8"]]
+ 005335cc ["INT_ADD", "register:40f0:8", ["const:5335cc:8", "const:4:8"]]
+ 005335cc ["CALL", null, ["callee:00c57e90:8"]]
- 0053358c bytes 41911c94
+ 005335cc bytes 31921c94
- 005335a4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005335a4 ["INT_ADD", "register:40f0:8", ["const:5335a4:8", "const:4:8"]]
- 005335a4 ["CALLIND", null, ["register:0:8"]]
+ 005335e4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005335e4 ["INT_ADD", "register:40f0:8", ["const:5335e4:8", "const:4:8"]]
+ 005335e4 ["CALLIND", null, ["register:0:8"]]
- 005335a4 bytes 20013fd6
+ 005335e4 bytes 20013fd6
- 005335b4 ["INT_ADD", "register:40f0:8", ["const:5335b4:8", "const:4:8"]]
- 005335b4 ["CALL", null, ["callee:00c59520:8"]]
+ 005335f4 ["INT_ADD", "register:40f0:8", ["const:5335f4:8", "const:4:8"]]
+ 005335f4 ["CALL", null, ["callee:00c59520:8"]]
- 005335b4 bytes db961c94
+ 005335f4 bytes cb971c94
~~~


<a id="compare-d6a2a1e9375ce47d5e84e354a98d5f20"></a>

### [`005336b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005336b8.md) → [`005336f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/005336f8.md) FUN_005336f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c59130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59130.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c59530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59530.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005336cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005336b8.md#insn-005336cc) · [`005336e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005336b8.md#insn-005336e4) · [`005336f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005336b8.md#insn-005336f4)
- 新版 `0053370c`（命令位置の公開資料なし） · `00533724`（命令位置の公開資料なし） · `00533734`（命令位置の公開資料なし）

~~~diff
- 005336cc ["INT_ADD", "register:40f0:8", ["const:5336cc:8", "const:4:8"]]
- 005336cc ["CALL", null, ["callee:00c57e90:8"]]
+ 0053370c ["INT_ADD", "register:40f0:8", ["const:53370c:8", "const:4:8"]]
+ 0053370c ["CALL", null, ["callee:00c57e90:8"]]
- 005336cc bytes f1901c94
+ 0053370c bytes e1911c94
- 005336e4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005336e4 ["INT_ADD", "register:40f0:8", ["const:5336e4:8", "const:4:8"]]
- 005336e4 ["CALLIND", null, ["register:0:8"]]
+ 00533724 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533724 ["INT_ADD", "register:40f0:8", ["const:533724:8", "const:4:8"]]
+ 00533724 ["CALLIND", null, ["register:0:8"]]
- 005336e4 bytes 20013fd6
+ 00533724 bytes 20013fd6
- 005336f4 ["INT_ADD", "register:40f0:8", ["const:5336f4:8", "const:4:8"]]
- 005336f4 ["CALL", null, ["callee:00c59530:8"]]
+ 00533734 ["INT_ADD", "register:40f0:8", ["const:533734:8", "const:4:8"]]
+ 00533734 ["CALL", null, ["callee:00c59530:8"]]
- 005336f4 bytes 8f961c94
+ 00533734 bytes 7f971c94
~~~


<a id="compare-092135402ba4f2cfb31d4aabc266f4bd"></a>

### [`005337f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005337f8.md) → [`00533838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533838.md) FUN_00533838

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053372c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/0053372c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053376c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/0053376c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00533808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005337f8.md#insn-00533808)
- 新版 `00533848`（命令位置の公開資料なし）

~~~diff
- 00533808 ["INT_ADD", "register:40f0:8", ["const:533808:8", "const:4:8"]]
- 00533808 ["CALL", null, ["callee:0053376c:8"]]
+ 00533848 ["INT_ADD", "register:40f0:8", ["const:533848:8", "const:4:8"]]
+ 00533848 ["CALL", null, ["callee:0053376c:8"]]
- 00533808 bytes c9ffff97
+ 00533848 bytes c9ffff97
~~~


<a id="compare-4599640623e1954bf130c6b04d3e2cc8"></a>

### [`00533a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533a80.md) → [`00533ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533ac0.md) FUN_00533ac0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00533964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533964.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005339a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/005339a4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00533a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533a80.md#insn-00533a90)
- 新版 `00533ad0`（命令位置の公開資料なし）

~~~diff
- 00533a90 ["INT_ADD", "register:40f0:8", ["const:533a90:8", "const:4:8"]]
- 00533a90 ["CALL", null, ["callee:005339a4:8"]]
+ 00533ad0 ["INT_ADD", "register:40f0:8", ["const:533ad0:8", "const:4:8"]]
+ 00533ad0 ["CALL", null, ["callee:005339a4:8"]]
- 00533a90 bytes b5ffff97
+ 00533ad0 bytes b5ffff97
~~~


<a id="compare-c78e3b578c61baefb76c9052d0b50bc1"></a>

### [`00533aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533aac.md) → [`00533aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533aec.md) FUN_00533aec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00533964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533964.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005339a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/005339a4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00533ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533aac.md#insn-00533ac0)
- 新版 `00533b00`（命令位置の公開資料なし）

~~~diff
- 00533ac0 ["INT_ADD", "register:40f0:8", ["const:533ac0:8", "const:4:8"]]
- 00533ac0 ["CALL", null, ["callee:005339a4:8"]]
+ 00533b00 ["INT_ADD", "register:40f0:8", ["const:533b00:8", "const:4:8"]]
+ 00533b00 ["CALL", null, ["callee:005339a4:8"]]
- 00533ac0 bytes a9ffff97
+ 00533b00 bytes a9ffff97
~~~


<a id="compare-00f334c62cca438348fd6d5f8b73b341"></a>

### [`00534634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534634.md) → [`00534674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534674.md) FUN_00534674

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00534680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534634.md#insn-00534680) · [`00534694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534634.md#insn-00534694) · [`0053469c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534634.md#insn-0053469c)
- 新版 `005346c0`（命令位置の公開資料なし） · `005346d4`（命令位置の公開資料なし） · `005346dc`（命令位置の公開資料なし）

~~~diff
- 00534680 ["INT_ADD", "register:40f0:8", ["const:534680:8", "const:4:8"]]
- 00534680 ["CALL", null, ["callee:00c53d00:8"]]
+ 005346c0 ["INT_ADD", "register:40f0:8", ["const:5346c0:8", "const:4:8"]]
+ 005346c0 ["CALL", null, ["callee:00c53d00:8"]]
- 00534680 bytes 987c1c94
+ 005346c0 bytes 907d1c94
- 00534694 ["COPY", "register:0:8", ["register:4040:8"]]
- 00534694 ["INT_ADD", "register:40f0:8", ["const:534694:8", "const:4:8"]]
- 00534694 ["CALLIND", null, ["register:0:8"]]
+ 005346d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005346d4 ["INT_ADD", "register:40f0:8", ["const:5346d4:8", "const:4:8"]]
+ 005346d4 ["CALLIND", null, ["register:0:8"]]
- 00534694 bytes 00013fd6
+ 005346d4 bytes 00013fd6
- 0053469c ["INT_ADD", "register:40f0:8", ["const:53469c:8", "const:4:8"]]
- 0053469c ["CALL", null, ["callee:00c57e80:8"]]
+ 005346dc ["INT_ADD", "register:40f0:8", ["const:5346dc:8", "const:4:8"]]
+ 005346dc ["CALL", null, ["callee:00c57e80:8"]]
- 0053469c bytes f98c1c94
+ 005346dc bytes e98d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b995890a49e7e95af3261c3aa307af04"></a>

### [`0053472c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053472c.md) → [`0053476c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/0053476c.md) FUN_0053476c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00534748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053472c.md#insn-00534748) · [`00534768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053472c.md#insn-00534768)
- 新版 `00534788`（命令位置の公開資料なし） · `005347a8`（命令位置の公開資料なし）

~~~diff
- 00534748 ["INT_ADD", "register:40f0:8", ["const:534748:8", "const:4:8"]]
- 00534748 ["CALL", null, ["callee:00c53d00:8"]]
+ 00534788 ["INT_ADD", "register:40f0:8", ["const:534788:8", "const:4:8"]]
+ 00534788 ["CALL", null, ["callee:00c53d00:8"]]
- 00534748 bytes 667c1c94
+ 00534788 bytes 5e7d1c94
- 00534768 ["COPY", "register:0:8", ["register:4040:8"]]
- 00534768 ["INT_ADD", "register:40f0:8", ["const:534768:8", "const:4:8"]]
- 00534768 ["CALLIND", null, ["register:0:8"]]
+ 005347a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005347a8 ["INT_ADD", "register:40f0:8", ["const:5347a8:8", "const:4:8"]]
+ 005347a8 ["CALLIND", null, ["register:0:8"]]
- 00534768 bytes 00013fd6
+ 005347a8 bytes 00013fd6
~~~


<a id="compare-d5ff7fe152cb4162f5f82a70b280cad6"></a>

### [`0053477c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053477c.md) → [`005347bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/005347bc.md) FUN_005347bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053479c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053477c.md#insn-0053479c) · [`005347b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053477c.md#insn-005347b0) · [`005347b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053477c.md#insn-005347b8)
- 新版 `005347dc`（命令位置の公開資料なし） · `005347f0`（命令位置の公開資料なし） · `005347f8`（命令位置の公開資料なし）

~~~diff
- 0053479c ["INT_ADD", "register:40f0:8", ["const:53479c:8", "const:4:8"]]
- 0053479c ["CALL", null, ["callee:00c53d00:8"]]
+ 005347dc ["INT_ADD", "register:40f0:8", ["const:5347dc:8", "const:4:8"]]
+ 005347dc ["CALL", null, ["callee:00c53d00:8"]]
- 0053479c bytes 517c1c94
+ 005347dc bytes 497d1c94
- 005347b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005347b0 ["INT_ADD", "register:40f0:8", ["const:5347b0:8", "const:4:8"]]
- 005347b0 ["CALLIND", null, ["register:0:8"]]
+ 005347f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005347f0 ["INT_ADD", "register:40f0:8", ["const:5347f0:8", "const:4:8"]]
+ 005347f0 ["CALLIND", null, ["register:0:8"]]
- 005347b0 bytes 00013fd6
+ 005347f0 bytes 00013fd6
- 005347b8 ["INT_ADD", "register:40f0:8", ["const:5347b8:8", "const:4:8"]]
- 005347b8 ["CALL", null, ["callee:00c57e80:8"]]
+ 005347f8 ["INT_ADD", "register:40f0:8", ["const:5347f8:8", "const:4:8"]]
+ 005347f8 ["CALL", null, ["callee:00c57e80:8"]]
- 005347b8 bytes b28c1c94
+ 005347f8 bytes a28d1c94
~~~


<a id="compare-04f5eb6f69a237361c47b15cac16945c"></a>

### [`00535068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535068.md) → [`005350a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005350a8.md) FUN_005350a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053508c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535068.md#insn-0053508c)
- 新版 `005350cc`（命令位置の公開資料なし）

~~~diff
- 0053508c ["COPY", "register:0:8", ["register:4040:8"]]
- 0053508c ["INT_ADD", "register:40f0:8", ["const:53508c:8", "const:4:8"]]
- 0053508c ["CALLIND", null, ["register:0:8"]]
+ 005350cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005350cc ["INT_ADD", "register:40f0:8", ["const:5350cc:8", "const:4:8"]]
+ 005350cc ["CALLIND", null, ["register:0:8"]]
- 0053508c bytes 00013fd6
+ 005350cc bytes 00013fd6
~~~


<a id="compare-5f25b1790b730fe271612f14450369de"></a>

### [`005350a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005350a0.md) → [`005350e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005350e0.md) FUN_005350e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005350c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005350a0.md#insn-005350c4) · [`005350cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005350a0.md#insn-005350cc)
- 新版 `00535104`（命令位置の公開資料なし） · `0053510c`（命令位置の公開資料なし）

~~~diff
- 005350c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005350c4 ["INT_ADD", "register:40f0:8", ["const:5350c4:8", "const:4:8"]]
- 005350c4 ["CALLIND", null, ["register:0:8"]]
+ 00535104 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00535104 ["INT_ADD", "register:40f0:8", ["const:535104:8", "const:4:8"]]
+ 00535104 ["CALLIND", null, ["register:0:8"]]
- 005350c4 bytes 00013fd6
+ 00535104 bytes 00013fd6
- 005350cc ["INT_ADD", "register:40f0:8", ["const:5350cc:8", "const:4:8"]]
- 005350cc ["CALL", null, ["callee:00c57e60:8"]]
+ 0053510c ["INT_ADD", "register:40f0:8", ["const:53510c:8", "const:4:8"]]
+ 0053510c ["CALL", null, ["callee:00c57e60:8"]]
- 005350cc bytes 658a1c94
+ 0053510c bytes 558b1c94
~~~


<a id="compare-676a8da5f5a90e80b4c337b657e1c1f3"></a>

### [`005350e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005350e0.md) → [`00535120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535120.md) FUN_00535120

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00535100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005350e0.md#insn-00535100) · [`00535118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005350e0.md#insn-00535118)
- 新版 `00535140`（命令位置の公開資料なし） · `00535158`（命令位置の公開資料なし）

~~~diff
- 00535100 ["INT_ADD", "register:40f0:8", ["const:535100:8", "const:4:8"]]
- 00535100 ["CALL", null, ["callee:00c580e0:8"]]
+ 00535140 ["INT_ADD", "register:40f0:8", ["const:535140:8", "const:4:8"]]
+ 00535140 ["CALL", null, ["callee:00c580e0:8"]]
- 00535100 bytes f88a1c94
+ 00535140 bytes e88b1c94
- 00535118 ["COPY", "register:0:8", ["register:4040:8"]]
- 00535118 ["INT_ADD", "register:40f0:8", ["const:535118:8", "const:4:8"]]
- 00535118 ["CALLIND", null, ["register:0:8"]]
+ 00535158 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00535158 ["INT_ADD", "register:40f0:8", ["const:535158:8", "const:4:8"]]
+ 00535158 ["CALLIND", null, ["register:0:8"]]
- 00535118 bytes 00013fd6
+ 00535158 bytes 00013fd6
~~~


<a id="compare-376067647cc8b75565ff68c899a95641"></a>

### [`00535144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535144.md) → [`00535184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535184.md) FUN_00535184

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00535164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535144.md#insn-00535164) · [`0053517c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535144.md#insn-0053517c)
- 新版 `005351a4`（命令位置の公開資料なし） · `005351bc`（命令位置の公開資料なし）

~~~diff
- 00535164 ["INT_ADD", "register:40f0:8", ["const:535164:8", "const:4:8"]]
- 00535164 ["CALL", null, ["callee:00c580e0:8"]]
+ 005351a4 ["INT_ADD", "register:40f0:8", ["const:5351a4:8", "const:4:8"]]
+ 005351a4 ["CALL", null, ["callee:00c580e0:8"]]
- 00535164 bytes df8a1c94
+ 005351a4 bytes cf8b1c94
- 0053517c ["COPY", "register:0:8", ["register:4040:8"]]
- 0053517c ["INT_ADD", "register:40f0:8", ["const:53517c:8", "const:4:8"]]
- 0053517c ["CALLIND", null, ["register:0:8"]]
+ 005351bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005351bc ["INT_ADD", "register:40f0:8", ["const:5351bc:8", "const:4:8"]]
+ 005351bc ["CALLIND", null, ["register:0:8"]]
- 0053517c bytes 00013fd6
+ 005351bc bytes 00013fd6
~~~


<a id="compare-565b5043bf999f2adaf286d7014ef927"></a>

### [`005351a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005351a8.md) → [`005351e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005351e8.md) FUN_005351e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005351c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005351a8.md#insn-005351c0) · [`005351d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005351a8.md#insn-005351d4)
- 新版 `00535200`（命令位置の公開資料なし） · `00535214`（命令位置の公開資料なし）

~~~diff
- 005351c0 ["INT_ADD", "register:40f0:8", ["const:5351c0:8", "const:4:8"]]
- 005351c0 ["CALL", null, ["callee:00c580e0:8"]]
+ 00535200 ["INT_ADD", "register:40f0:8", ["const:535200:8", "const:4:8"]]
+ 00535200 ["CALL", null, ["callee:00c580e0:8"]]
- 005351c0 bytes c88a1c94
+ 00535200 bytes b88b1c94
- 005351d4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005351d4 ["INT_ADD", "register:40f0:8", ["const:5351d4:8", "const:4:8"]]
- 005351d4 ["CALLIND", null, ["register:0:8"]]
+ 00535214 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00535214 ["INT_ADD", "register:40f0:8", ["const:535214:8", "const:4:8"]]
+ 00535214 ["CALLIND", null, ["register:0:8"]]
- 005351d4 bytes 20013fd6
+ 00535214 bytes 20013fd6
~~~


<a id="compare-4efc497e6fefac84e67c036e5f6a4396"></a>

### [`005351fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005351fc.md) → [`0053523c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/0053523c.md) FUN_0053523c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00535210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005351fc.md#insn-00535210) · [`00535220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005351fc.md#insn-00535220)
- 新版 `00535250`（命令位置の公開資料なし） · `00535260`（命令位置の公開資料なし）

~~~diff
- 00535210 ["INT_ADD", "register:40f0:8", ["const:535210:8", "const:4:8"]]
- 00535210 ["CALL", null, ["callee:00c580e0:8"]]
+ 00535250 ["INT_ADD", "register:40f0:8", ["const:535250:8", "const:4:8"]]
+ 00535250 ["CALL", null, ["callee:00c580e0:8"]]
- 00535210 bytes b48a1c94
+ 00535250 bytes a48b1c94
- 00535220 ["COPY", "register:0:8", ["register:4040:8"]]
- 00535220 ["INT_ADD", "register:40f0:8", ["const:535220:8", "const:4:8"]]
- 00535220 ["CALLIND", null, ["register:0:8"]]
+ 00535260 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00535260 ["INT_ADD", "register:40f0:8", ["const:535260:8", "const:4:8"]]
+ 00535260 ["CALLIND", null, ["register:0:8"]]
- 00535220 bytes 00013fd6
+ 00535260 bytes 00013fd6
~~~


<a id="compare-152109695627bc5c39c6fc9d568402dc"></a>

### [`00535248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535248.md) → [`00535288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535288.md) FUN_00535288

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053525c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535248.md#insn-0053525c) · [`0053526c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535248.md#insn-0053526c) · [`00535278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535248.md#insn-00535278)
- 新版 `0053529c`（命令位置の公開資料なし） · `005352ac`（命令位置の公開資料なし） · `005352b8`（命令位置の公開資料なし）

~~~diff
- 0053525c ["INT_ADD", "register:40f0:8", ["const:53525c:8", "const:4:8"]]
- 0053525c ["CALL", null, ["callee:00c580e0:8"]]
+ 0053529c ["INT_ADD", "register:40f0:8", ["const:53529c:8", "const:4:8"]]
+ 0053529c ["CALL", null, ["callee:00c580e0:8"]]
- 0053525c bytes a18a1c94
+ 0053529c bytes 918b1c94
- 0053526c ["COPY", "register:0:8", ["register:4040:8"]]
- 0053526c ["INT_ADD", "register:40f0:8", ["const:53526c:8", "const:4:8"]]
- 0053526c ["CALLIND", null, ["register:0:8"]]
+ 005352ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 005352ac ["INT_ADD", "register:40f0:8", ["const:5352ac:8", "const:4:8"]]
+ 005352ac ["CALLIND", null, ["register:0:8"]]
- 0053526c bytes 00013fd6
+ 005352ac bytes 00013fd6
- 00535278 ["INT_ADD", "register:40f0:8", ["const:535278:8", "const:4:8"]]
- 00535278 ["CALL", null, ["callee:00c580f0:8"]]
+ 005352b8 ["INT_ADD", "register:40f0:8", ["const:5352b8:8", "const:4:8"]]
+ 005352b8 ["CALL", null, ["callee:00c580f0:8"]]
- 00535278 bytes 9e8a1c94
+ 005352b8 bytes 8e8b1c94
~~~


<a id="compare-b86b382a35499772c6226c2efebbffeb"></a>

### [`005352a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005352a0.md) → [`005352e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005352e0.md) FUN_005352e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005352c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005352a0.md#insn-005352c4) · [`005352e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005352a0.md#insn-005352e0) · [`005352ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005352a0.md#insn-005352ec)
- 新版 `00535304`（命令位置の公開資料なし） · `00535320`（命令位置の公開資料なし） · `0053532c`（命令位置の公開資料なし）

~~~diff
- 005352c4 ["INT_ADD", "register:40f0:8", ["const:5352c4:8", "const:4:8"]]
- 005352c4 ["CALL", null, ["callee:00c580e0:8"]]
+ 00535304 ["INT_ADD", "register:40f0:8", ["const:535304:8", "const:4:8"]]
+ 00535304 ["CALL", null, ["callee:00c580e0:8"]]
- 005352c4 bytes 878a1c94
+ 00535304 bytes 778b1c94
- 005352e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005352e0 ["INT_ADD", "register:40f0:8", ["const:5352e0:8", "const:4:8"]]
- 005352e0 ["CALLIND", null, ["register:0:8"]]
+ 00535320 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00535320 ["INT_ADD", "register:40f0:8", ["const:535320:8", "const:4:8"]]
+ 00535320 ["CALLIND", null, ["register:0:8"]]
- 005352e0 bytes 00013fd6
+ 00535320 bytes 00013fd6
- 005352ec ["INT_ADD", "register:40f0:8", ["const:5352ec:8", "const:4:8"]]
- 005352ec ["CALL", null, ["callee:00c580f0:8"]]
+ 0053532c ["INT_ADD", "register:40f0:8", ["const:53532c:8", "const:4:8"]]
+ 0053532c ["CALL", null, ["callee:00c580f0:8"]]
- 005352ec bytes 818a1c94
+ 0053532c bytes 718b1c94
~~~


<a id="compare-243dc67286d0ee3ed9b0ac2fc8a616ac"></a>

### [`00536364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536364.md) → [`005363a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/005363a4.md) FUN_005363a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053638c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536364.md#insn-0053638c)
- 新版 `005363cc`（命令位置の公開資料なし）

~~~diff
- 0053638c ["COPY", "register:0:8", ["register:4048:8"]]
- 0053638c ["INT_ADD", "register:40f0:8", ["const:53638c:8", "const:4:8"]]
- 0053638c ["CALLIND", null, ["register:0:8"]]
+ 005363cc ["COPY", "register:0:8", ["register:4048:8"]]
+ 005363cc ["INT_ADD", "register:40f0:8", ["const:5363cc:8", "const:4:8"]]
+ 005363cc ["CALLIND", null, ["register:0:8"]]
- 0053638c bytes 20013fd6
+ 005363cc bytes 20013fd6
~~~


<a id="compare-b82afd98a1c8c8b0c1307390c7075738"></a>

### [`0053689c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053689c.md) → [`005368dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/005368dc.md) FUN_005368dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004ebc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004ebc2c.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 1件 [`004ebc6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004ebc6c.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005368c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053689c.md#insn-005368c0) · [`00536908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053689c.md#insn-00536908) · [`00536928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053689c.md#insn-00536928)
- 新版 `00536900`（命令位置の公開資料なし） · `00536948`（命令位置の公開資料なし） · `00536968`（命令位置の公開資料なし）

~~~diff
- 005368c0 ["INT_ADD", "register:40f0:8", ["const:5368c0:8", "const:4:8"]]
- 005368c0 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00536900 ["INT_ADD", "register:40f0:8", ["const:536900:8", "const:4:8"]]
+ 00536900 ["CALL", null, ["callee:00c57fe0:8"]]
- 005368c0 bytes c8841c94
+ 00536900 bytes b8851c94
- 00536908 ["INT_ADD", "register:40f0:8", ["const:536908:8", "const:4:8"]]
- 00536908 ["CALL", null, ["callee:00c57e90:8"]]
+ 00536948 ["INT_ADD", "register:40f0:8", ["const:536948:8", "const:4:8"]]
+ 00536948 ["CALL", null, ["callee:00c57e90:8"]]
- 00536908 bytes 62841c94
+ 00536948 bytes 52851c94
- 00536928 ["INT_ADD", "register:40f0:8", ["const:536928:8", "const:4:8"]]
- 00536928 ["CALL", null, ["callee:00c57f40:8"]]
+ 00536968 ["INT_ADD", "register:40f0:8", ["const:536968:8", "const:4:8"]]
+ 00536968 ["CALL", null, ["callee:00c57f40:8"]]
- 00536928 bytes 86841c94
+ 00536968 bytes 76851c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5c7e7c5ccd8e9d9c850b0b4d3d4d6c5"></a>

### [`00537980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00537/00537980.md) → [`005379c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00537/005379c0.md) FUN_005379c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ef0.md) [`00c58f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c592f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c592f0.md) [`00c59300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00537998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00537/00537980.md#insn-00537998)
- 新版 `005379d8`（命令位置の公開資料なし）

~~~diff
- 00537998 ["INT_ADD", "register:40f0:8", ["const:537998:8", "const:4:8"]]
- 00537998 ["CALL", null, ["callee:00c592f0:8"]]
+ 005379d8 ["INT_ADD", "register:40f0:8", ["const:5379d8:8", "const:4:8"]]
+ 005379d8 ["CALL", null, ["callee:00c592f0:8"]]
- 00537998 bytes 56851c94
+ 005379d8 bytes 46861c94
~~~


<a id="compare-b95b0620754d0d62923174436bad3ba8"></a>

### [`00538bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00538/00538bc0.md) → [`00538c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00538/00538c00.md) FUN_00538c00

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00538a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00538/00538a4c.md) [`00538f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00538/00538f5c.md) · 呼出先 6件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md)
- 新版 呼出元 2件 [`00538a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00538/00538a8c.md) [`00538f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00538/00538f9c.md) · 呼出先 6件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00538bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00538/00538bc0.md#insn-00538bec) · [`00538c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00538/00538bc0.md#insn-00538c04) · [`00538c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00538/00538bc0.md#insn-00538c68)
- 新版 `00538c2c`（命令位置の公開資料なし） · `00538c44`（命令位置の公開資料なし） · `00538ca8`（命令位置の公開資料なし）

~~~diff
- 00538bec ["INT_ADD", "register:40f0:8", ["const:538bec:8", "const:4:8"]]
- 00538bec ["CALL", null, ["callee:00c580e0:8"]]
+ 00538c2c ["INT_ADD", "register:40f0:8", ["const:538c2c:8", "const:4:8"]]
+ 00538c2c ["CALL", null, ["callee:00c580e0:8"]]
- 00538bec bytes 3d7c1c94
+ 00538c2c bytes 2d7d1c94
- 00538c04 ["INT_ADD", "register:40f0:8", ["const:538c04:8", "const:4:8"]]
- 00538c04 ["CALL", null, ["callee:00c582f0:8"]]
+ 00538c44 ["INT_ADD", "register:40f0:8", ["const:538c44:8", "const:4:8"]]
+ 00538c44 ["CALL", null, ["callee:00c582f0:8"]]
- 00538c04 bytes bb7c1c94
+ 00538c44 bytes ab7d1c94
- 00538c68 ["INT_ADD", "register:40f0:8", ["const:538c68:8", "const:4:8"]]
- 00538c68 ["CALL", null, ["callee:00c58380:8"]]
+ 00538ca8 ["INT_ADD", "register:40f0:8", ["const:538ca8:8", "const:4:8"]]
+ 00538ca8 ["CALL", null, ["callee:00c58380:8"]]
- 00538c68 bytes c67c1c94
+ 00538ca8 bytes b67d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d12ceaa682a97b5ef27eaefc640a96f"></a>

### [`00538cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00538/00538cd8.md) → [`00538d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00538/00538d18.md) FUN_00538d18

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0053876c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00538/0053876c.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d30.md) [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c57d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d50.md)
- 新版 呼出元 1件 [`005387ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00538/005387ac.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58130.md) [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00538d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00538/00538cd8.md#insn-00538d00) · [`00538d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00538/00538cd8.md#insn-00538d10) · [`00538d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00538/00538cd8.md#insn-00538d2c)
- 新版 `00538d40`（命令位置の公開資料なし） · `00538d50`（命令位置の公開資料なし） · `00538d6c`（命令位置の公開資料なし）

~~~diff
- 00538d00 ["INT_ADD", "register:40f0:8", ["const:538d00:8", "const:4:8"]]
- 00538d00 ["CALL", null, ["callee:00c58130:8"]]
+ 00538d40 ["INT_ADD", "register:40f0:8", ["const:538d40:8", "const:4:8"]]
+ 00538d40 ["CALL", null, ["callee:00c58130:8"]]
- 00538d00 bytes 0c7c1c94
+ 00538d40 bytes fc7c1c94
- 00538d10 ["INT_ADD", "register:40f0:8", ["const:538d10:8", "const:4:8"]]
- 00538d10 ["CALL", null, ["callee:00c58140:8"]]
+ 00538d50 ["INT_ADD", "register:40f0:8", ["const:538d50:8", "const:4:8"]]
+ 00538d50 ["CALL", null, ["callee:00c58140:8"]]
- 00538d10 bytes 0c7c1c94
+ 00538d50 bytes fc7c1c94
- 00538d2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00538d2c ["INT_ADD", "register:40f0:8", ["const:538d2c:8", "const:4:8"]]
- 00538d2c ["CALLIND", null, ["register:0:8"]]
+ 00538d6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00538d6c ["INT_ADD", "register:40f0:8", ["const:538d6c:8", "const:4:8"]]
+ 00538d6c ["CALLIND", null, ["register:0:8"]]
- 00538d2c bytes 00013fd6
+ 00538d6c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb4b6d493843ccc0116c2dce6203c519"></a>

### [`00538da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00538/00538da4.md) → [`00538de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00538/00538de4.md) FUN_00538de4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00538dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00538/00538da4.md#insn-00538dcc) · [`00538dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00538/00538da4.md#insn-00538dd4)
- 新版 `00538e0c`（命令位置の公開資料なし） · `00538e14`（命令位置の公開資料なし）

~~~diff
- 00538dcc ["INT_ADD", "register:40f0:8", ["const:538dcc:8", "const:4:8"]]
- 00538dcc ["CALL", null, ["callee:00c58150:8"]]
+ 00538e0c ["INT_ADD", "register:40f0:8", ["const:538e0c:8", "const:4:8"]]
+ 00538e0c ["CALL", null, ["callee:00c58150:8"]]
- 00538dcc bytes e17b1c94
+ 00538e0c bytes d17c1c94
- 00538dd4 ["INT_ADD", "register:40f0:8", ["const:538dd4:8", "const:4:8"]]
- 00538dd4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00538e14 ["INT_ADD", "register:40f0:8", ["const:538e14:8", "const:4:8"]]
+ 00538e14 ["CALL", null, ["callee:00c57eb0:8"]]
- 00538dd4 bytes 377b1c94
+ 00538e14 bytes 277c1c94
~~~


<a id="compare-39eee031e122ba7fd401ebed4a98b78a"></a>

### [`0053906c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/0053906c.md) → [`005390ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00539/005390ac.md) FUN_005390ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00537b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00537/00537b58.md) · 呼出先 8件 [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00537b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00537/00537b98.md) · 呼出先 8件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005390a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/0053906c.md#insn-005390a8) · [`005390b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/0053906c.md#insn-005390b4) · [`005390c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/0053906c.md#insn-005390c8)
- 新版 `005390e8`（命令位置の公開資料なし） · `005390f4`（命令位置の公開資料なし） · `00539108`（命令位置の公開資料なし）

~~~diff
- 005390a8 ["INT_ADD", "register:40f0:8", ["const:5390a8:8", "const:4:8"]]
- 005390a8 ["CALL", null, ["callee:00c580e0:8"]]
+ 005390e8 ["INT_ADD", "register:40f0:8", ["const:5390e8:8", "const:4:8"]]
+ 005390e8 ["CALL", null, ["callee:00c580e0:8"]]
- 005390a8 bytes 0e7b1c94
+ 005390e8 bytes fe7b1c94
- 005390b4 ["INT_ADD", "register:40f0:8", ["const:5390b4:8", "const:4:8"]]
- 005390b4 ["CALL", null, ["callee:00c584a0:8"]]
+ 005390f4 ["INT_ADD", "register:40f0:8", ["const:5390f4:8", "const:4:8"]]
+ 005390f4 ["CALL", null, ["callee:00c584a0:8"]]
- 005390b4 bytes fb7b1c94
+ 005390f4 bytes eb7c1c94
- 005390c8 ["INT_ADD", "register:40f0:8", ["const:5390c8:8", "const:4:8"]]
- 005390c8 ["CALL", null, ["callee:00c582f0:8"]]
+ 00539108 ["INT_ADD", "register:40f0:8", ["const:539108:8", "const:4:8"]]
+ 00539108 ["CALL", null, ["callee:00c582f0:8"]]
- 005390c8 bytes 8a7b1c94
+ 00539108 bytes 7a7c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fd69dcbb47445c62da0c8a8ca203ef9"></a>

### [`005399d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/005399d4.md) → [`00539a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00539/00539a14.md) FUN_00539a14

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c593d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c593d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c597d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c597d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005399e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/005399d4.md#insn-005399e8)
- 新版 `00539a28`（命令位置の公開資料なし）

~~~diff
- 005399e8 ["INT_ADD", "register:40f0:8", ["const:5399e8:8", "const:4:8"]]
- 005399e8 ["CALL", null, ["callee:00c597d0:8"]]
+ 00539a28 ["INT_ADD", "register:40f0:8", ["const:539a28:8", "const:4:8"]]
+ 00539a28 ["CALL", null, ["callee:00c597d0:8"]]
- 005399e8 bytes 7a7e1c94
+ 00539a28 bytes 6a7f1c94
~~~


<a id="compare-444d2d55051cbd46219875356a4f2a7e"></a>

### [`00539e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/00539e28.md) → [`00539e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00539/00539e68.md) FUN_00539e68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00539e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/00539e28.md#insn-00539e6c) · [`00539e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/00539e28.md#insn-00539e9c) · [`00539ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/00539e28.md#insn-00539ed0)
- 新版 `00539eac`（命令位置の公開資料なし） · `00539edc`（命令位置の公開資料なし） · `00539f10`（命令位置の公開資料なし）

~~~diff
- 00539e6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00539e6c ["INT_ADD", "register:40f0:8", ["const:539e6c:8", "const:4:8"]]
- 00539e6c ["CALLIND", null, ["register:0:8"]]
+ 00539eac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00539eac ["INT_ADD", "register:40f0:8", ["const:539eac:8", "const:4:8"]]
+ 00539eac ["CALLIND", null, ["register:0:8"]]
- 00539e6c bytes 00013fd6
+ 00539eac bytes 00013fd6
- 00539e9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00539e9c ["INT_ADD", "register:40f0:8", ["const:539e9c:8", "const:4:8"]]
- 00539e9c ["CALLIND", null, ["register:0:8"]]
+ 00539edc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00539edc ["INT_ADD", "register:40f0:8", ["const:539edc:8", "const:4:8"]]
+ 00539edc ["CALLIND", null, ["register:0:8"]]
- 00539e9c bytes 00013fd6
+ 00539edc bytes 00013fd6
- 00539ed0 ["INT_ADD", "register:40f0:8", ["const:539ed0:8", "const:4:8"]]
- 00539ed0 ["CALL", null, ["callee:00459d74:8"]]
+ 00539f10 ["INT_ADD", "register:40f0:8", ["const:539f10:8", "const:4:8"]]
+ 00539f10 ["CALL", null, ["callee:00459d74:8"]]
- 00539ed0 bytes 997ffc97
+ 00539f10 bytes 997ffc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03903816f3163f45ceea5de47a348a72"></a>

### [`00539edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/00539edc.md) → [`00539f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00539/00539f1c.md) FUN_00539f1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004fbebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbebc.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`004fbefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbefc.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00539f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/00539edc.md#insn-00539f78) · [`00539fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/00539edc.md#insn-00539fc4) · [`0053a010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/00539edc.md#insn-0053a010)
- 新版 `00539fb8`（命令位置の公開資料なし） · `0053a004`（命令位置の公開資料なし） · `0053a050`（命令位置の公開資料なし）

~~~diff
- 00539f78 ["INT_ADD", "register:40f0:8", ["const:539f78:8", "const:4:8"]]
- 00539f78 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00539fb8 ["INT_ADD", "register:40f0:8", ["const:539fb8:8", "const:4:8"]]
+ 00539fb8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00539f78 bytes ce761c94
+ 00539fb8 bytes be771c94
- 00539fc4 ["INT_ADD", "register:40f0:8", ["const:539fc4:8", "const:4:8"]]
- 00539fc4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053a004 ["INT_ADD", "register:40f0:8", ["const:53a004:8", "const:4:8"]]
+ 0053a004 ["CALL", null, ["callee:00c57eb0:8"]]
- 00539fc4 bytes bb761c94
+ 0053a004 bytes ab771c94
- 0053a010 ["INT_ADD", "register:40f0:8", ["const:53a010:8", "const:4:8"]]
- 0053a010 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053a050 ["INT_ADD", "register:40f0:8", ["const:53a050:8", "const:4:8"]]
+ 0053a050 ["CALL", null, ["callee:00c57eb0:8"]]
- 0053a010 bytes a8761c94
+ 0053a050 bytes 98771c94
~~~


<a id="compare-b2eafc03177da1a641d88250ae4677e3"></a>

### [`0053a074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a074.md) → [`0053a0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053a0b4.md) FUN_0053a0b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004fbebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbebc.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0053a534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a534.md) [`0053a6bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a6bc.md) [`0053a848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a848.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`004fbefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbefc.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0053a574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053a574.md) [`0053a6fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053a6fc.md) [`0053a888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053a888.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053a10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a074.md#insn-0053a10c) · [`0053a150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a074.md#insn-0053a150) · [`0053a160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a074.md#insn-0053a160)
- 新版 `0053a14c`（命令位置の公開資料なし） · `0053a190`（命令位置の公開資料なし） · `0053a1a0`（命令位置の公開資料なし）

~~~diff
- 0053a10c ["INT_ADD", "register:40f0:8", ["const:53a10c:8", "const:4:8"]]
- 0053a10c ["CALL", null, ["callee:00c57f40:8"]]
+ 0053a14c ["INT_ADD", "register:40f0:8", ["const:53a14c:8", "const:4:8"]]
+ 0053a14c ["CALL", null, ["callee:00c57f40:8"]]
- 0053a10c bytes 8d761c94
+ 0053a14c bytes 7d771c94
- 0053a150 ["INT_ADD", "register:40f0:8", ["const:53a150:8", "const:4:8"]]
- 0053a150 ["CALL", null, ["callee:00c57e90:8"]]
+ 0053a190 ["INT_ADD", "register:40f0:8", ["const:53a190:8", "const:4:8"]]
+ 0053a190 ["CALL", null, ["callee:00c57e90:8"]]
- 0053a150 bytes 50761c94
+ 0053a190 bytes 40771c94
- 0053a160 ["INT_ADD", "register:40f0:8", ["const:53a160:8", "const:4:8"]]
- 0053a160 ["CALL", null, ["callee:0053a574:8"]]
+ 0053a1a0 ["INT_ADD", "register:40f0:8", ["const:53a1a0:8", "const:4:8"]]
+ 0053a1a0 ["CALL", null, ["callee:0053a574:8"]]
- 0053a160 bytes f5000094
+ 0053a1a0 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf728c5184ac60b85d66ef090b595211"></a>

### [`0053a534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a534.md) → [`0053a574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053a574.md) FUN_0053a574

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0053a074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a074.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`0053a0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053a0b4.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053a59c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a534.md#insn-0053a59c) · [`0053a5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a534.md#insn-0053a5d4) · [`0053a684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a534.md#insn-0053a684)
- 新版 `0053a5dc`（命令位置の公開資料なし） · `0053a614`（命令位置の公開資料なし） · `0053a6c4`（命令位置の公開資料なし）

~~~diff
- 0053a59c ["INT_ADD", "register:40f0:8", ["const:53a59c:8", "const:4:8"]]
- 0053a59c ["CALL", null, ["callee:00c57f40:8"]]
+ 0053a5dc ["INT_ADD", "register:40f0:8", ["const:53a5dc:8", "const:4:8"]]
+ 0053a5dc ["CALL", null, ["callee:00c57f40:8"]]
- 0053a59c bytes 69751c94
+ 0053a5dc bytes 59761c94
- 0053a5d4 ["INT_ADD", "register:40f0:8", ["const:53a5d4:8", "const:4:8"]]
- 0053a5d4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0053a614 ["INT_ADD", "register:40f0:8", ["const:53a614:8", "const:4:8"]]
+ 0053a614 ["CALL", null, ["callee:00c57e90:8"]]
- 0053a5d4 bytes 2f751c94
+ 0053a614 bytes 1f761c94
- 0053a684 ["INT_ADD", "register:40f0:8", ["const:53a684:8", "const:4:8"]]
- 0053a684 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053a6c4 ["INT_ADD", "register:40f0:8", ["const:53a6c4:8", "const:4:8"]]
+ 0053a6c4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0053a684 bytes 0b751c94
+ 0053a6c4 bytes fb751c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-715ed2a0c45716512fe83e4eac4ea971"></a>

### [`0053a6bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a6bc.md) → [`0053a6fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053a6fc.md) FUN_0053a6fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0053a074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a074.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`0053a0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053a0b4.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053a72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a6bc.md#insn-0053a72c) · [`0053a764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a6bc.md#insn-0053a764) · [`0053a814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a6bc.md#insn-0053a814)
- 新版 `0053a76c`（命令位置の公開資料なし） · `0053a7a4`（命令位置の公開資料なし） · `0053a854`（命令位置の公開資料なし）

~~~diff
- 0053a72c ["INT_ADD", "register:40f0:8", ["const:53a72c:8", "const:4:8"]]
- 0053a72c ["CALL", null, ["callee:00c57f40:8"]]
+ 0053a76c ["INT_ADD", "register:40f0:8", ["const:53a76c:8", "const:4:8"]]
+ 0053a76c ["CALL", null, ["callee:00c57f40:8"]]
- 0053a72c bytes 05751c94
+ 0053a76c bytes f5751c94
- 0053a764 ["INT_ADD", "register:40f0:8", ["const:53a764:8", "const:4:8"]]
- 0053a764 ["CALL", null, ["callee:00c57e90:8"]]
+ 0053a7a4 ["INT_ADD", "register:40f0:8", ["const:53a7a4:8", "const:4:8"]]
+ 0053a7a4 ["CALL", null, ["callee:00c57e90:8"]]
- 0053a764 bytes cb741c94
+ 0053a7a4 bytes bb751c94
- 0053a814 ["INT_ADD", "register:40f0:8", ["const:53a814:8", "const:4:8"]]
- 0053a814 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053a854 ["INT_ADD", "register:40f0:8", ["const:53a854:8", "const:4:8"]]
+ 0053a854 ["CALL", null, ["callee:00c57eb0:8"]]
- 0053a814 bytes a7741c94
+ 0053a854 bytes 97751c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da127d93d3cbf05b7f044bb14122fc92"></a>

### [`0053a848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a848.md) → [`0053a888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053a888.md) FUN_0053a888

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0053a074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a074.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`0053a0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053a0b4.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053a8b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a848.md#insn-0053a8b8) · [`0053a8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a848.md#insn-0053a8f0) · [`0053a9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a848.md#insn-0053a9a0)
- 新版 `0053a8f8`（命令位置の公開資料なし） · `0053a930`（命令位置の公開資料なし） · `0053a9e0`（命令位置の公開資料なし）

~~~diff
- 0053a8b8 ["INT_ADD", "register:40f0:8", ["const:53a8b8:8", "const:4:8"]]
- 0053a8b8 ["CALL", null, ["callee:00c57f40:8"]]
+ 0053a8f8 ["INT_ADD", "register:40f0:8", ["const:53a8f8:8", "const:4:8"]]
+ 0053a8f8 ["CALL", null, ["callee:00c57f40:8"]]
- 0053a8b8 bytes a2741c94
+ 0053a8f8 bytes 92751c94
- 0053a8f0 ["INT_ADD", "register:40f0:8", ["const:53a8f0:8", "const:4:8"]]
- 0053a8f0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0053a930 ["INT_ADD", "register:40f0:8", ["const:53a930:8", "const:4:8"]]
+ 0053a930 ["CALL", null, ["callee:00c57e90:8"]]
- 0053a8f0 bytes 68741c94
+ 0053a930 bytes 58751c94
- 0053a9a0 ["INT_ADD", "register:40f0:8", ["const:53a9a0:8", "const:4:8"]]
- 0053a9a0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053a9e0 ["INT_ADD", "register:40f0:8", ["const:53a9e0:8", "const:4:8"]]
+ 0053a9e0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0053a9a0 bytes 44741c94
+ 0053a9e0 bytes 34751c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9bf100441ce6495dac530be90cf8183"></a>

### [`0053aa64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053aa64.md) → [`0053aaa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053aaa4.md) FUN_0053aaa4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`005027b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005027b8.md) [`00515684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md) [`0051e358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051e358.md) [`0052d4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d4d0.md) [`0052e2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e2f4.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0053ab64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053ab64.md) [`0053ade4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053ade4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 6件 [`005027f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005027f8.md) [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) [`0051e398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051e398.md) [`0052d510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d510.md) [`0052e334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052e334.md) · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0053aba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053aba4.md) [`0053ae24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053ae24.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053aa9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053aa64.md#insn-0053aa9c) · [`0053aab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053aa64.md#insn-0053aab4) · [`0053aad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053aa64.md#insn-0053aad0)
- 新版 `0053aadc`（命令位置の公開資料なし） · `0053aaf4`（命令位置の公開資料なし） · `0053ab10`（命令位置の公開資料なし）

~~~diff
- 0053aa9c ["INT_ADD", "register:40f0:8", ["const:53aa9c:8", "const:4:8"]]
- 0053aa9c ["CALL", null, ["callee:00c57e90:8"]]
+ 0053aadc ["INT_ADD", "register:40f0:8", ["const:53aadc:8", "const:4:8"]]
+ 0053aadc ["CALL", null, ["callee:00c57e90:8"]]
- 0053aa9c bytes fd731c94
+ 0053aadc bytes ed741c94
- 0053aab4 ["INT_ADD", "register:40f0:8", ["const:53aab4:8", "const:4:8"]]
- 0053aab4 ["CALL", null, ["callee:0053ae24:8"]]
+ 0053aaf4 ["INT_ADD", "register:40f0:8", ["const:53aaf4:8", "const:4:8"]]
+ 0053aaf4 ["CALL", null, ["callee:0053ae24:8"]]
- 0053aab4 bytes cc000094
+ 0053aaf4 bytes cc000094
- 0053aad0 ["INT_ADD", "register:40f0:8", ["const:53aad0:8", "const:4:8"]]
- 0053aad0 ["CALL", null, ["callee:0053aba4:8"]]
+ 0053ab10 ["INT_ADD", "register:40f0:8", ["const:53ab10:8", "const:4:8"]]
+ 0053ab10 ["CALL", null, ["callee:0053aba4:8"]]
- 0053aad0 bytes 25000094
+ 0053ab10 bytes 25000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5348fcbc9297b70e7365e7ae21451474"></a>

### [`0053ad78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053ad78.md) → [`0053adb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053adb8.md) FUN_0053adb8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053ada4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053ad78.md#insn-0053ada4) · [`0053adb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053ad78.md#insn-0053adb4) · [`0053adc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053ad78.md#insn-0053adc4)
- 新版 `0053ade4`（命令位置の公開資料なし） · `0053adf4`（命令位置の公開資料なし） · `0053ae04`（命令位置の公開資料なし）

~~~diff
- 0053ada4 ["INT_ADD", "register:40f0:8", ["const:53ada4:8", "const:4:8"]]
- 0053ada4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053ade4 ["INT_ADD", "register:40f0:8", ["const:53ade4:8", "const:4:8"]]
+ 0053ade4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0053ada4 bytes 43731c94
+ 0053ade4 bytes 33741c94
- 0053adb4 ["INT_ADD", "register:40f0:8", ["const:53adb4:8", "const:4:8"]]
- 0053adb4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053adf4 ["INT_ADD", "register:40f0:8", ["const:53adf4:8", "const:4:8"]]
+ 0053adf4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0053adb4 bytes 3f731c94
+ 0053adf4 bytes 2f741c94
- 0053adc4 ["INT_ADD", "register:40f0:8", ["const:53adc4:8", "const:4:8"]]
- 0053adc4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053ae04 ["INT_ADD", "register:40f0:8", ["const:53ae04:8", "const:4:8"]]
+ 0053ae04 ["CALL", null, ["callee:00c57eb0:8"]]
- 0053adc4 bytes 3b731c94
+ 0053ae04 bytes 2b741c94
~~~


<a id="compare-cd956fe9bea9cbb193e1742b67f642f9"></a>

### [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) → [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) FUN_0053af90

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 43件 [`004ffa6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffa6c.md) [`004ffde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffde0.md) [`00500ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00500/00500ecc.md) [`005017b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/005017b8.md) [`005025bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005025bc.md) · 呼出先 2件 [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 43件 [`004ffaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ffaac.md) [`004ffe20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ffe20.md) [`00500f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00500/00500f0c.md) [`005017f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/005017f8.md) [`005025fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005025fc.md) · 呼出先 2件 [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053af6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md#insn-0053af6c) · [`0053af78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md#insn-0053af78) · [`0053af88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md#insn-0053af88)
- 新版 `0053afac`（命令位置の公開資料なし） · `0053afb8`（命令位置の公開資料なし） · `0053afc8`（命令位置の公開資料なし）

~~~diff
- 0053af6c ["INT_ADD", "register:40f0:8", ["const:53af6c:8", "const:4:8"]]
- 0053af6c ["CALL", null, ["local:b0:8"]]
+ 0053afac ["INT_ADD", "register:40f0:8", ["const:53afac:8", "const:4:8"]]
+ 0053afac ["CALL", null, ["local:b0:8"]]
- 0053af6c bytes f9ffff97
+ 0053afac bytes f9ffff97
- 0053af78 ["INT_ADD", "register:40f0:8", ["const:53af78:8", "const:4:8"]]
- 0053af78 ["CALL", null, ["local:b0:8"]]
+ 0053afb8 ["INT_ADD", "register:40f0:8", ["const:53afb8:8", "const:4:8"]]
+ 0053afb8 ["CALL", null, ["local:b0:8"]]
- 0053af78 bytes f6ffff97
+ 0053afb8 bytes f6ffff97
- 0053af88 ["INT_ADD", "register:40f0:8", ["const:53af88:8", "const:4:8"]]
- 0053af88 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053afc8 ["INT_ADD", "register:40f0:8", ["const:53afc8:8", "const:4:8"]]
+ 0053afc8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0053af88 bytes ca721c94
+ 0053afc8 bytes ba731c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-247c66857ea08251c6911d10a1a41bef"></a>

### [`0053b378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b378.md) → [`0053b3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b3b8.md) FUN_0053b3b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053b3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b378.md#insn-0053b3a0)
- 新版 `0053b3e0`（命令位置の公開資料なし）

~~~diff
- 0053b3a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0053b3a0 ["INT_ADD", "register:40f0:8", ["const:53b3a0:8", "const:4:8"]]
- 0053b3a0 ["CALLIND", null, ["register:0:8"]]
+ 0053b3e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0053b3e0 ["INT_ADD", "register:40f0:8", ["const:53b3e0:8", "const:4:8"]]
+ 0053b3e0 ["CALLIND", null, ["register:0:8"]]
- 0053b3a0 bytes 00013fd6
+ 0053b3e0 bytes 00013fd6
~~~


<a id="compare-6fd0a44ba5311d0f5613fc4f756fa5ce"></a>

### [`0053b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) → [`0053b424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b424.md) FUN_0053b424

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 17件 [`00509bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509bd4.md) [`0050b31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b31c.md) [`0050ce74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050ce74.md) [`00510d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510d18.md) [`0051209c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/0051209c.md) · 呼出先 4件 [`0053b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 17件 [`00509c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509c14.md) [`0050b35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b35c.md) [`0050ceb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050ceb4.md) [`00510d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510d58.md) [`005120dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/005120dc.md) · 呼出先 4件 [`0053b424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b424.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053b400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md#insn-0053b400) · [`0053b40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md#insn-0053b40c) · [`0053b41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md#insn-0053b41c)
- 新版 `0053b440`（命令位置の公開資料なし） · `0053b44c`（命令位置の公開資料なし） · `0053b45c`（命令位置の公開資料なし）

~~~diff
- 0053b400 ["INT_ADD", "register:40f0:8", ["const:53b400:8", "const:4:8"]]
- 0053b400 ["CALL", null, ["local:b0:8"]]
+ 0053b440 ["INT_ADD", "register:40f0:8", ["const:53b440:8", "const:4:8"]]
+ 0053b440 ["CALL", null, ["local:b0:8"]]
- 0053b400 bytes f9ffff97
+ 0053b440 bytes f9ffff97
- 0053b40c ["INT_ADD", "register:40f0:8", ["const:53b40c:8", "const:4:8"]]
- 0053b40c ["CALL", null, ["local:b0:8"]]
+ 0053b44c ["INT_ADD", "register:40f0:8", ["const:53b44c:8", "const:4:8"]]
+ 0053b44c ["CALL", null, ["local:b0:8"]]
- 0053b40c bytes f6ffff97
+ 0053b44c bytes f6ffff97
- 0053b41c ["INT_ADD", "register:40f0:8", ["const:53b41c:8", "const:4:8"]]
- 0053b41c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053b45c ["INT_ADD", "register:40f0:8", ["const:53b45c:8", "const:4:8"]]
+ 0053b45c ["CALL", null, ["callee:00c57eb0:8"]]
- 0053b41c bytes a5711c94
+ 0053b45c bytes 95721c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eab48757c08ebbd375f57990db94335d"></a>

### [`0053b73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b73c.md) → [`0053b77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b77c.md) FUN_0053b77c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`0050e004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050e004.md) [`0051ea80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051ea80.md) [`00520e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520e70.md) [`0075d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md) [`00bb7828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7828.md) · 呼出先 5件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053b9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b9d0.md) [`0053bb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bb30.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58030.md)
- 新版 呼出元 7件 [`0050e044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050e044.md) [`0051eac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051eac0.md) [`00520eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520eb0.md) [`0075d75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075d/0075d75c.md) [`00bb7c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7c50.md) · 呼出先 5件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053ba10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053ba10.md) [`0053bb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bb70.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053b824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b73c.md#insn-0053b824) · [`0053b830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b73c.md#insn-0053b830) · [`0053b83c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b73c.md#insn-0053b83c)
- 新版 `0053b864`（命令位置の公開資料なし） · `0053b870`（命令位置の公開資料なし） · `0053b87c`（命令位置の公開資料なし）

~~~diff
- 0053b824 ["INT_ADD", "register:40f0:8", ["const:53b824:8", "const:4:8"]]
- 0053b824 ["CALL", null, ["callee:00c58430:8"]]
+ 0053b864 ["INT_ADD", "register:40f0:8", ["const:53b864:8", "const:4:8"]]
+ 0053b864 ["CALL", null, ["callee:00c58430:8"]]
- 0053b824 bytes 03721c94
+ 0053b864 bytes f3721c94
- 0053b830 ["INT_ADD", "register:40f0:8", ["const:53b830:8", "const:4:8"]]
- 0053b830 ["CALL", null, ["callee:00c58430:8"]]
+ 0053b870 ["INT_ADD", "register:40f0:8", ["const:53b870:8", "const:4:8"]]
+ 0053b870 ["CALL", null, ["callee:00c58430:8"]]
- 0053b830 bytes 00721c94
+ 0053b870 bytes f0721c94
- 0053b83c ["INT_ADD", "register:40f0:8", ["const:53b83c:8", "const:4:8"]]
- 0053b83c ["CALL", null, ["callee:0053ba10:8"]]
+ 0053b87c ["INT_ADD", "register:40f0:8", ["const:53b87c:8", "const:4:8"]]
+ 0053b87c ["CALL", null, ["callee:0053ba10:8"]]
- 0053b83c bytes 65000094
+ 0053b87c bytes 65000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a64dfe2f1a75efa399ca2c52d529c494"></a>

### [`0053b9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b9d0.md) → [`0053ba10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053ba10.md) FUN_0053ba10

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0053b73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b73c.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`0053b77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b77c.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053ba4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b9d0.md#insn-0053ba4c) · [`0053bab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b9d0.md#insn-0053bab0)
- 新版 `0053ba8c`（命令位置の公開資料なし） · `0053baf0`（命令位置の公開資料なし）

~~~diff
- 0053ba4c ["INT_ADD", "register:40f0:8", ["const:53ba4c:8", "const:4:8"]]
- 0053ba4c ["CALL", null, ["callee:00c58050:8"]]
+ 0053ba8c ["INT_ADD", "register:40f0:8", ["const:53ba8c:8", "const:4:8"]]
+ 0053ba8c ["CALL", null, ["callee:00c58050:8"]]
- 0053ba4c bytes 81701c94
+ 0053ba8c bytes 71711c94
- 0053bab0 ["INT_ADD", "register:40f0:8", ["const:53bab0:8", "const:4:8"]]
- 0053bab0 ["CALL", null, ["callee:0043bba4:8"]]
+ 0053baf0 ["INT_ADD", "register:40f0:8", ["const:53baf0:8", "const:4:8"]]
+ 0053baf0 ["CALL", null, ["callee:0043bba4:8"]]
- 0053bab0 bytes 2d00fc97
+ 0053baf0 bytes 2d00fc97
~~~


<a id="compare-33611a590079a6023d79b0460f9ea71c"></a>

### [`0053bad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bad8.md) → [`0053bb18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bb18.md) FUN_0053bb18

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053baf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bad8.md#insn-0053baf0)
- 新版 `0053bb30`（命令位置の公開資料なし）

~~~diff
- 0053baf0 ["INT_ADD", "register:40f0:8", ["const:53baf0:8", "const:4:8"]]
- 0053baf0 ["CALL", null, ["callee:0046d490:8"]]
+ 0053bb30 ["INT_ADD", "register:40f0:8", ["const:53bb30:8", "const:4:8"]]
+ 0053bb30 ["CALL", null, ["callee:0046d490:8"]]
- 0053baf0 bytes 58c6fc97
+ 0053bb30 bytes 58c6fc97
~~~


<a id="compare-f2b7def0a7f1cdf590a1086dbd758ebe"></a>

### [`0053bb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bb30.md) → [`0053bb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bb70.md) FUN_0053bb70

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00504d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504d50.md) [`005199bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/005199bc.md) [`00519aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/00519aa4.md) [`00520e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520e70.md) [`0053b73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b73c.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0053bc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bc70.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 5件 [`00504d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504d90.md) [`005199fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/005199fc.md) [`00519ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/00519ae4.md) [`00520eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520eb0.md) [`0053b77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b77c.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0053bcb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bcb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053bb60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bb30.md#insn-0053bb60) · [`0053bbc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bb30.md#insn-0053bbc8) · [`0053bc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bb30.md#insn-0053bc2c)
- 新版 `0053bba0`（命令位置の公開資料なし） · `0053bc08`（命令位置の公開資料なし） · `0053bc6c`（命令位置の公開資料なし）

~~~diff
- 0053bb60 ["INT_ADD", "register:40f0:8", ["const:53bb60:8", "const:4:8"]]
- 0053bb60 ["CALL", null, ["callee:0053bcb0:8"]]
+ 0053bba0 ["INT_ADD", "register:40f0:8", ["const:53bba0:8", "const:4:8"]]
+ 0053bba0 ["CALL", null, ["callee:0053bcb0:8"]]
- 0053bb60 bytes 44000094
+ 0053bba0 bytes 44000094
- 0053bbc8 ["INT_ADD", "register:40f0:8", ["const:53bbc8:8", "const:4:8"]]
- 0053bbc8 ["CALL", null, ["callee:00c58050:8"]]
+ 0053bc08 ["INT_ADD", "register:40f0:8", ["const:53bc08:8", "const:4:8"]]
+ 0053bc08 ["CALL", null, ["callee:00c58050:8"]]
- 0053bbc8 bytes 22701c94
+ 0053bc08 bytes 12711c94
- 0053bc2c ["INT_ADD", "register:40f0:8", ["const:53bc2c:8", "const:4:8"]]
- 0053bc2c ["CALL", null, ["callee:0043bba4:8"]]
+ 0053bc6c ["INT_ADD", "register:40f0:8", ["const:53bc6c:8", "const:4:8"]]
+ 0053bc6c ["CALL", null, ["callee:0043bba4:8"]]
- 0053bc2c bytes cefffb97
+ 0053bc6c bytes cefffb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f67641a42f9fed61aa16f8523d0de369"></a>

### [`0053bc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bc70.md) → [`0053bcb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bcb0.md) FUN_0053bcb0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0052dcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052dcc0.md) [`0053bb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bb30.md) [`0053ca48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053ca48.md) [`00726234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726234.md) [`00944e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/00944e18.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 5件 [`0052dd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dd00.md) [`0053bb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bb70.md) [`0053ca88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053ca88.md) [`00726274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726274.md) [`00944fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/00944fb4.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053bc90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bc70.md#insn-0053bc90) · [`0053bcc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bc70.md#insn-0053bcc4) · [`0053bcf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bc70.md#insn-0053bcf0)
- 新版 `0053bcd0`（命令位置の公開資料なし） · `0053bd04`（命令位置の公開資料なし） · `0053bd30`（命令位置の公開資料なし）

~~~diff
- 0053bc90 ["INT_ADD", "register:40f0:8", ["const:53bc90:8", "const:4:8"]]
- 0053bc90 ["CALL", null, ["callee:00c57e90:8"]]
+ 0053bcd0 ["INT_ADD", "register:40f0:8", ["const:53bcd0:8", "const:4:8"]]
+ 0053bcd0 ["CALL", null, ["callee:00c57e90:8"]]
- 0053bc90 bytes 806f1c94
+ 0053bcd0 bytes 70701c94
- 0053bcc4 ["INT_ADD", "register:40f0:8", ["const:53bcc4:8", "const:4:8"]]
- 0053bcc4 ["CALL", null, ["callee:0043bb20:8"]]
+ 0053bd04 ["INT_ADD", "register:40f0:8", ["const:53bd04:8", "const:4:8"]]
+ 0053bd04 ["CALL", null, ["callee:0043bb20:8"]]
- 0053bcc4 bytes 87fffb97
+ 0053bd04 bytes 87fffb97
- 0053bcf0 ["INT_ADD", "register:40f0:8", ["const:53bcf0:8", "const:4:8"]]
- 0053bcf0 ["CALL", null, ["callee:0043bb20:8"]]
+ 0053bd30 ["INT_ADD", "register:40f0:8", ["const:53bd30:8", "const:4:8"]]
+ 0053bd30 ["CALL", null, ["callee:0043bb20:8"]]
- 0053bcf0 bytes 7cfffb97
+ 0053bd30 bytes 7cfffb97
~~~


<a id="compare-7e48601f6343dd98212bbd496712dd43"></a>

### [`0053bd38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bd38.md) → [`0053bd78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bd78.md) FUN_0053bd78

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0050aaa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050aaa4.md) [`0050e004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050e004.md) [`00512cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512cc8.md) [`0051ea80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051ea80.md) [`00520e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520e70.md) · 呼出先 7件 [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`0053bff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bff4.md) [`0053c138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c138.md) [`0053c268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c268.md) [`00548e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548e28.md)
- 新版 呼出元 5件 [`0050aae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050a/0050aae4.md) [`0050e044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050e044.md) [`00512d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512d08.md) [`0051eac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051eac0.md) [`00520eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520eb0.md) · 呼出先 7件 [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`0053c034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c034.md) [`0053c178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c178.md) [`0053c2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c2a8.md) [`00548e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548e68.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053be30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bd38.md#insn-0053be30) · [`0053be40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bd38.md#insn-0053be40) · [`0053be4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bd38.md#insn-0053be4c)
- 新版 `0053be70`（命令位置の公開資料なし） · `0053be80`（命令位置の公開資料なし） · `0053be8c`（命令位置の公開資料なし）

~~~diff
- 0053be30 ["INT_ADD", "register:40f0:8", ["const:53be30:8", "const:4:8"]]
- 0053be30 ["CALL", null, ["callee:0053c178:8"]]
+ 0053be70 ["INT_ADD", "register:40f0:8", ["const:53be70:8", "const:4:8"]]
+ 0053be70 ["CALL", null, ["callee:0053c178:8"]]
- 0053be30 bytes c2000094
+ 0053be70 bytes c2000094
- 0053be40 ["INT_ADD", "register:40f0:8", ["const:53be40:8", "const:4:8"]]
- 0053be40 ["CALL", null, ["callee:00548e68:8"]]
+ 0053be80 ["INT_ADD", "register:40f0:8", ["const:53be80:8", "const:4:8"]]
+ 0053be80 ["CALL", null, ["callee:00548e68:8"]]
- 0053be40 bytes fa330094
+ 0053be80 bytes fa330094
- 0053be4c ["INT_ADD", "register:40f0:8", ["const:53be4c:8", "const:4:8"]]
- 0053be4c ["CALL", null, ["callee:00c58430:8"]]
+ 0053be8c ["INT_ADD", "register:40f0:8", ["const:53be8c:8", "const:4:8"]]
+ 0053be8c ["CALL", null, ["callee:00c58430:8"]]
- 0053be4c bytes 79701c94
+ 0053be8c bytes 69711c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29fbc8b25ea82939043173f58b03514e"></a>

### [`0053bff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bff4.md) → [`0053c034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c034.md) FUN_0053c034

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0053bd38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bd38.md) · 呼出先 1件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md)
- 新版 呼出元 1件 [`0053bd78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bd78.md) · 呼出先 1件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053c0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bff4.md#insn-0053c0c0)
- 新版 `0053c100`（命令位置の公開資料なし）

~~~diff
- 0053c0c0 ["INT_ADD", "register:40f0:8", ["const:53c0c0:8", "const:4:8"]]
- 0053c0c0 ["CALL", null, ["callee:0043bba4:8"]]
+ 0053c100 ["INT_ADD", "register:40f0:8", ["const:53c100:8", "const:4:8"]]
+ 0053c100 ["CALL", null, ["callee:0043bba4:8"]]
- 0053c0c0 bytes a9fefb97
+ 0053c100 bytes a9fefb97
~~~


<a id="compare-f750074a5cec3069c91f010dacb77c68"></a>

### [`0053c0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c0e0.md) → [`0053c120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c120.md) FUN_0053c120

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053c0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c0e0.md#insn-0053c0f8)
- 新版 `0053c138`（命令位置の公開資料なし）

~~~diff
- 0053c0f8 ["INT_ADD", "register:40f0:8", ["const:53c0f8:8", "const:4:8"]]
- 0053c0f8 ["CALL", null, ["callee:0053af90:8"]]
+ 0053c138 ["INT_ADD", "register:40f0:8", ["const:53c138:8", "const:4:8"]]
+ 0053c138 ["CALL", null, ["callee:0053af90:8"]]
- 0053c0f8 bytes 96fbff97
+ 0053c138 bytes 96fbff97
~~~


<a id="compare-8b8b14a291362def91cb49ca82811dfa"></a>

### [`0053c138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c138.md) → [`0053c178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c178.md) FUN_0053c178

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`004e443c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e443c.md) [`0053bd38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bd38.md) [`0053ec30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053ec30.md) [`0054a1b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a1b8.md) [`0055ce28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055ce28.md) · 呼出先 5件 [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 5件 [`004e447c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e447c.md) [`0053bd78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bd78.md) [`0053ec70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053e/0053ec70.md) [`0054a1f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a1f8.md) [`0055ce68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055ce68.md) · 呼出先 5件 [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053c17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c138.md#insn-0053c17c) · [`0053c1c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c138.md#insn-0053c1c4) · [`0053c1ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c138.md#insn-0053c1ec)
- 新版 `0053c1bc`（命令位置の公開資料なし） · `0053c204`（命令位置の公開資料なし） · `0053c22c`（命令位置の公開資料なし）

~~~diff
- 0053c17c ["INT_ADD", "register:40f0:8", ["const:53c17c:8", "const:4:8"]]
- 0053c17c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053c1bc ["INT_ADD", "register:40f0:8", ["const:53c1bc:8", "const:4:8"]]
+ 0053c1bc ["CALL", null, ["callee:00c57eb0:8"]]
- 0053c17c bytes 4d6e1c94
+ 0053c1bc bytes 3d6f1c94
- 0053c1c4 ["INT_ADD", "register:40f0:8", ["const:53c1c4:8", "const:4:8"]]
- 0053c1c4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0053c204 ["INT_ADD", "register:40f0:8", ["const:53c204:8", "const:4:8"]]
+ 0053c204 ["CALL", null, ["callee:00c57e90:8"]]
- 0053c1c4 bytes 336e1c94
+ 0053c204 bytes 236f1c94
- 0053c1ec ["INT_ADD", "register:40f0:8", ["const:53c1ec:8", "const:4:8"]]
- 0053c1ec ["CALL", null, ["callee:00c58000:8"]]
+ 0053c22c ["INT_ADD", "register:40f0:8", ["const:53c22c:8", "const:4:8"]]
+ 0053c22c ["CALL", null, ["callee:00c58000:8"]]
- 0053c1ec bytes 856e1c94
+ 0053c22c bytes 756f1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8d5fee5495dcec7e0399fc4f4966915"></a>

### [`0053c268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c268.md) → [`0053c2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c2a8.md) FUN_0053c2a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0053bd38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bd38.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0053ade4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053ade4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0053bd78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bd78.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0053ae24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053ae24.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053c29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c268.md#insn-0053c29c) · [`0053c2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c268.md#insn-0053c2b4) · [`0053c368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c268.md#insn-0053c368)
- 新版 `0053c2dc`（命令位置の公開資料なし） · `0053c2f4`（命令位置の公開資料なし） · `0053c3a8`（命令位置の公開資料なし）

~~~diff
- 0053c29c ["INT_ADD", "register:40f0:8", ["const:53c29c:8", "const:4:8"]]
- 0053c29c ["CALL", null, ["callee:00c57e90:8"]]
+ 0053c2dc ["INT_ADD", "register:40f0:8", ["const:53c2dc:8", "const:4:8"]]
+ 0053c2dc ["CALL", null, ["callee:00c57e90:8"]]
- 0053c29c bytes fd6d1c94
+ 0053c2dc bytes ed6e1c94
- 0053c2b4 ["INT_ADD", "register:40f0:8", ["const:53c2b4:8", "const:4:8"]]
- 0053c2b4 ["CALL", null, ["callee:0053ae24:8"]]
+ 0053c2f4 ["INT_ADD", "register:40f0:8", ["const:53c2f4:8", "const:4:8"]]
+ 0053c2f4 ["CALL", null, ["callee:0053ae24:8"]]
- 0053c2b4 bytes ccfaff97
+ 0053c2f4 bytes ccfaff97
- 0053c368 ["INT_ADD", "register:40f0:8", ["const:53c368:8", "const:4:8"]]
- 0053c368 ["CALL", null, ["callee:0043bba4:8"]]
+ 0053c3a8 ["INT_ADD", "register:40f0:8", ["const:53c3a8:8", "const:4:8"]]
+ 0053c3a8 ["CALL", null, ["callee:0043bba4:8"]]
- 0053c368 bytes fffdfb97
+ 0053c3a8 bytes fffdfb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7e4207ade3edf43af28c49172e6ef0e"></a>

### [`0053c3cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c3cc.md) → [`0053c40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c40c.md) FUN_0053c40c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005111e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/005111e4.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00517448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517448.md) [`0053c4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c4d8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00511224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511224.md) · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00517488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517488.md) [`0053c518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c518.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053c404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c3cc.md#insn-0053c404) · [`0053c424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c3cc.md#insn-0053c424) · [`0053c43c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c3cc.md#insn-0053c43c)
- 新版 `0053c444`（命令位置の公開資料なし） · `0053c464`（命令位置の公開資料なし） · `0053c47c`（命令位置の公開資料なし）

~~~diff
- 0053c404 ["INT_ADD", "register:40f0:8", ["const:53c404:8", "const:4:8"]]
- 0053c404 ["CALL", null, ["callee:0053c518:8"]]
+ 0053c444 ["INT_ADD", "register:40f0:8", ["const:53c444:8", "const:4:8"]]
+ 0053c444 ["CALL", null, ["callee:0053c518:8"]]
- 0053c404 bytes 35000094
+ 0053c444 bytes 35000094
- 0053c424 ["INT_ADD", "register:40f0:8", ["const:53c424:8", "const:4:8"]]
- 0053c424 ["CALL", null, ["callee:00c57e90:8"]]
+ 0053c464 ["INT_ADD", "register:40f0:8", ["const:53c464:8", "const:4:8"]]
+ 0053c464 ["CALL", null, ["callee:00c57e90:8"]]
- 0053c424 bytes 9b6d1c94
+ 0053c464 bytes 8b6e1c94
- 0053c43c ["INT_ADD", "register:40f0:8", ["const:53c43c:8", "const:4:8"]]
- 0053c43c ["CALL", null, ["callee:00517488:8"]]
+ 0053c47c ["INT_ADD", "register:40f0:8", ["const:53c47c:8", "const:4:8"]]
+ 0053c47c ["CALL", null, ["callee:00517488:8"]]
- 0053c43c bytes 036cff97
+ 0053c47c bytes 036cff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bf8579407233c4cfc83aeb76b1b969d"></a>

### [`0053c874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c874.md) → [`0053c8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c8b4.md) FUN_0053c8b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053c8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c874.md#insn-0053c8a0) · [`0053c8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c874.md#insn-0053c8b4) · [`0053c8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c874.md#insn-0053c8c8)
- 新版 `0053c8e0`（命令位置の公開資料なし） · `0053c8f4`（命令位置の公開資料なし） · `0053c908`（命令位置の公開資料なし）

~~~diff
- 0053c8a0 ["INT_ADD", "register:40f0:8", ["const:53c8a0:8", "const:4:8"]]
- 0053c8a0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053c8e0 ["INT_ADD", "register:40f0:8", ["const:53c8e0:8", "const:4:8"]]
+ 0053c8e0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0053c8a0 bytes 846c1c94
+ 0053c8e0 bytes 746d1c94
- 0053c8b4 ["INT_ADD", "register:40f0:8", ["const:53c8b4:8", "const:4:8"]]
- 0053c8b4 ["CALL", null, ["callee:00c53d00:8"]]
+ 0053c8f4 ["INT_ADD", "register:40f0:8", ["const:53c8f4:8", "const:4:8"]]
+ 0053c8f4 ["CALL", null, ["callee:00c53d00:8"]]
- 0053c8b4 bytes 0b5c1c94
+ 0053c8f4 bytes 035d1c94
- 0053c8c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0053c8c8 ["INT_ADD", "register:40f0:8", ["const:53c8c8:8", "const:4:8"]]
- 0053c8c8 ["CALLIND", null, ["register:0:8"]]
+ 0053c908 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0053c908 ["INT_ADD", "register:40f0:8", ["const:53c908:8", "const:4:8"]]
+ 0053c908 ["CALLIND", null, ["register:0:8"]]
- 0053c8c8 bytes 00013fd6
+ 0053c908 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6533ce11434861bedf306a9b9bde189d"></a>

### [`0053ca48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053ca48.md) → [`0053ca88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053ca88.md) FUN_0053ca88

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00515684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md) [`0051e358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051e358.md) [`0052d4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d4d0.md) [`0052e2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e2f4.md) [`0053c900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c900.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0053bc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bc70.md) [`0053cb1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053cb1c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 5件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) [`0051e398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051e398.md) [`0052d510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d510.md) [`0052e334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052e334.md) [`0053c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c940.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0053bcb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bcb0.md) [`0053cb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053cb5c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053ca78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053ca48.md#insn-0053ca78) · [`0053ca90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053ca48.md#insn-0053ca90) · [`0053cabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053ca48.md#insn-0053cabc)
- 新版 `0053cab8`（命令位置の公開資料なし） · `0053cad0`（命令位置の公開資料なし） · `0053cafc`（命令位置の公開資料なし）

~~~diff
- 0053ca78 ["INT_ADD", "register:40f0:8", ["const:53ca78:8", "const:4:8"]]
- 0053ca78 ["CALL", null, ["callee:0053bcb0:8"]]
+ 0053cab8 ["INT_ADD", "register:40f0:8", ["const:53cab8:8", "const:4:8"]]
+ 0053cab8 ["CALL", null, ["callee:0053bcb0:8"]]
- 0053ca78 bytes 7efcff97
+ 0053cab8 bytes 7efcff97
- 0053ca90 ["INT_ADD", "register:40f0:8", ["const:53ca90:8", "const:4:8"]]
- 0053ca90 ["CALL", null, ["callee:0053cb5c:8"]]
+ 0053cad0 ["INT_ADD", "register:40f0:8", ["const:53cad0:8", "const:4:8"]]
+ 0053cad0 ["CALL", null, ["callee:0053cb5c:8"]]
- 0053ca90 bytes 23000094
+ 0053cad0 bytes 23000094
- 0053cabc ["INT_ADD", "register:40f0:8", ["const:53cabc:8", "const:4:8"]]
- 0053cabc ["CALL", null, ["callee:0043bba4:8"]]
+ 0053cafc ["INT_ADD", "register:40f0:8", ["const:53cafc:8", "const:4:8"]]
+ 0053cafc ["CALL", null, ["callee:0043bba4:8"]]
- 0053cabc bytes 2afcfb97
+ 0053cafc bytes 2afcfb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2015919b48a4fb3fa4ed6ac2a162ae60"></a>

### [`0053cb1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053cb1c.md) → [`0053cb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053cb5c.md) FUN_0053cb5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0053ca48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053ca48.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`0053ca88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053ca88.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053cb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053cb1c.md#insn-0053cb90) · [`0053cbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053cb1c.md#insn-0053cbe4) · [`0053cc98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053cb1c.md#insn-0053cc98)
- 新版 `0053cbd0`（命令位置の公開資料なし） · `0053cc24`（命令位置の公開資料なし） · `0053ccd8`（命令位置の公開資料なし）

~~~diff
- 0053cb90 ["INT_ADD", "register:40f0:8", ["const:53cb90:8", "const:4:8"]]
- 0053cb90 ["CALL", null, ["callee:00c58050:8"]]
+ 0053cbd0 ["INT_ADD", "register:40f0:8", ["const:53cbd0:8", "const:4:8"]]
+ 0053cbd0 ["CALL", null, ["callee:00c58050:8"]]
- 0053cb90 bytes 306c1c94
+ 0053cbd0 bytes 206d1c94
- 0053cbe4 ["INT_ADD", "register:40f0:8", ["const:53cbe4:8", "const:4:8"]]
- 0053cbe4 ["CALL", null, ["callee:00c58050:8"]]
+ 0053cc24 ["INT_ADD", "register:40f0:8", ["const:53cc24:8", "const:4:8"]]
+ 0053cc24 ["CALL", null, ["callee:00c58050:8"]]
- 0053cbe4 bytes 1b6c1c94
+ 0053cc24 bytes 0b6d1c94
- 0053cc98 ["INT_ADD", "register:40f0:8", ["const:53cc98:8", "const:4:8"]]
- 0053cc98 ["CALL", null, ["callee:00c58050:8"]]
+ 0053ccd8 ["INT_ADD", "register:40f0:8", ["const:53ccd8:8", "const:4:8"]]
+ 0053ccd8 ["CALL", null, ["callee:00c58050:8"]]
- 0053cc98 bytes ee6b1c94
+ 0053ccd8 bytes de6c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24f4b2511103f740177ffd277b4c6724"></a>

### [`0053d674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d674.md) → [`0053d6b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d6b4.md) FUN_0053d6b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053d690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d674.md#insn-0053d690) · [`0053d6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d674.md#insn-0053d6b0)
- 新版 `0053d6d0`（命令位置の公開資料なし） · `0053d6f0`（命令位置の公開資料なし）

~~~diff
- 0053d690 ["INT_ADD", "register:40f0:8", ["const:53d690:8", "const:4:8"]]
- 0053d690 ["CALL", null, ["callee:00c53d00:8"]]
+ 0053d6d0 ["INT_ADD", "register:40f0:8", ["const:53d6d0:8", "const:4:8"]]
+ 0053d6d0 ["CALL", null, ["callee:00c53d00:8"]]
- 0053d690 bytes 94581c94
+ 0053d6d0 bytes 8c591c94
- 0053d6b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0053d6b0 ["INT_ADD", "register:40f0:8", ["const:53d6b0:8", "const:4:8"]]
- 0053d6b0 ["CALLIND", null, ["register:0:8"]]
+ 0053d6f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0053d6f0 ["INT_ADD", "register:40f0:8", ["const:53d6f0:8", "const:4:8"]]
+ 0053d6f0 ["CALLIND", null, ["register:0:8"]]
- 0053d6b0 bytes 00013fd6
+ 0053d6f0 bytes 00013fd6
~~~


<a id="compare-e59c5fbf44450e2b024f959bad428635"></a>

### [`0053d6c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d6c4.md) → [`0053d704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d704.md) FUN_0053d704

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053d6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d6c4.md#insn-0053d6d4)
- 新版 `0053d714`（命令位置の公開資料なし）

~~~diff
- 0053d6d4 ["INT_ADD", "register:40f0:8", ["const:53d6d4:8", "const:4:8"]]
- 0053d6d4 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0053d714 ["INT_ADD", "register:40f0:8", ["const:53d714:8", "const:4:8"]]
+ 0053d714 ["CALL", null, ["callee:00c57ea0:8"]]
- 0053d6d4 bytes f3681c94
+ 0053d714 bytes e3691c94
~~~


<a id="compare-992758d2bd999a7116d667ee51892687"></a>

### [`0053d720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d720.md) → [`0053d760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d760.md) FUN_0053d760

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0051a994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a994.md) [`0053f8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f8d0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0051a9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a9d4.md) [`0053f910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f910.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053d784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d720.md#insn-0053d784) · [`0053d794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d720.md#insn-0053d794)
- 新版 `0053d7c4`（命令位置の公開資料なし） · `0053d7d4`（命令位置の公開資料なし）

~~~diff
- 0053d784 ["INT_ADD", "register:40f0:8", ["const:53d784:8", "const:4:8"]]
- 0053d784 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053d7c4 ["INT_ADD", "register:40f0:8", ["const:53d7c4:8", "const:4:8"]]
+ 0053d7c4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0053d784 bytes cb681c94
+ 0053d7c4 bytes bb691c94
- 0053d794 ["INT_ADD", "register:40f0:8", ["const:53d794:8", "const:4:8"]]
- 0053d794 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053d7d4 ["INT_ADD", "register:40f0:8", ["const:53d7d4:8", "const:4:8"]]
+ 0053d7d4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0053d794 bytes c7681c94
+ 0053d7d4 bytes b7691c94
~~~


<a id="compare-8d0e670cc702fcc8ab9158edbf581d76"></a>

### [`0053d920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d920.md) → [`0053d960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d960.md) FUN_0053d960

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053d960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d920.md#insn-0053d960) · [`0053d970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d920.md#insn-0053d970)
- 新版 `0053d9a0`（命令位置の公開資料なし） · `0053d9b0`（命令位置の公開資料なし）

~~~diff
- 0053d960 ["INT_ADD", "register:40f0:8", ["const:53d960:8", "const:4:8"]]
- 0053d960 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053d9a0 ["INT_ADD", "register:40f0:8", ["const:53d9a0:8", "const:4:8"]]
+ 0053d9a0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0053d960 bytes 54681c94
+ 0053d9a0 bytes 44691c94
- 0053d970 ["INT_ADD", "register:40f0:8", ["const:53d970:8", "const:4:8"]]
- 0053d970 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053d9b0 ["INT_ADD", "register:40f0:8", ["const:53d9b0:8", "const:4:8"]]
+ 0053d9b0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0053d970 bytes 50681c94
+ 0053d9b0 bytes 40691c94
~~~


<a id="compare-8a539306324bc8bcad5fdc1c2c05d0dc"></a>

### [`0053d984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d984.md) → [`0053d9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d9c4.md) FUN_0053d9c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c582b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582b0.md) [`00c582d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c586b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586b0.md) [`00c586d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053d9a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d984.md#insn-0053d9a4) · [`0053d9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d984.md#insn-0053d9b8)
- 新版 `0053d9e4`（命令位置の公開資料なし） · `0053d9f8`（命令位置の公開資料なし）

~~~diff
- 0053d9a4 ["INT_ADD", "register:40f0:8", ["const:53d9a4:8", "const:4:8"]]
- 0053d9a4 ["CALL", null, ["callee:00c586b0:8"]]
+ 0053d9e4 ["INT_ADD", "register:40f0:8", ["const:53d9e4:8", "const:4:8"]]
+ 0053d9e4 ["CALL", null, ["callee:00c586b0:8"]]
- 0053d9a4 bytes 436a1c94
+ 0053d9e4 bytes 336b1c94
- 0053d9b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0053d9b8 ["INT_ADD", "register:40f0:8", ["const:53d9b8:8", "const:4:8"]]
- 0053d9b8 ["CALLIND", null, ["register:0:8"]]
+ 0053d9f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0053d9f8 ["INT_ADD", "register:40f0:8", ["const:53d9f8:8", "const:4:8"]]
+ 0053d9f8 ["CALLIND", null, ["register:0:8"]]
- 0053d9b8 bytes 00013fd6
+ 0053d9f8 bytes 00013fd6
~~~


<a id="compare-4089bcb4148edb337a57034e66c291f2"></a>

### [`0053dad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053dad0.md) → [`0053db10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053db10.md) FUN_0053db10

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053daf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053dad0.md#insn-0053daf0)
- 新版 `0053db30`（命令位置の公開資料なし）

~~~diff
- 0053daf0 ["INT_ADD", "register:40f0:8", ["const:53daf0:8", "const:4:8"]]
- 0053daf0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053db30 ["INT_ADD", "register:40f0:8", ["const:53db30:8", "const:4:8"]]
+ 0053db30 ["CALL", null, ["callee:00c57eb0:8"]]
- 0053daf0 bytes f0671c94
+ 0053db30 bytes e0681c94
~~~


<a id="compare-77a725c64397da4bf49604abcc78fd78"></a>

### [`0053e9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053e9cc.md) → [`0053ea0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053e/0053ea0c.md) FUN_0053ea0c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00520e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520e70.md) · 呼出先 6件 [`0053d7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d7b8.md) [`0053d7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d7cc.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00520eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520eb0.md) · 呼出先 6件 [`0053d7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d7f8.md) [`0053d80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d80c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053e9cc.md#insn-0053ea50) · [`0053ea60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053e9cc.md#insn-0053ea60) · [`0053ea9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053e9cc.md#insn-0053ea9c)
- 新版 `0053ea90`（命令位置の公開資料なし） · `0053eaa0`（命令位置の公開資料なし） · `0053eadc`（命令位置の公開資料なし）

~~~diff
- 0053ea50 ["INT_ADD", "register:40f0:8", ["const:53ea50:8", "const:4:8"]]
- 0053ea50 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053ea90 ["INT_ADD", "register:40f0:8", ["const:53ea90:8", "const:4:8"]]
+ 0053ea90 ["CALL", null, ["callee:00c57eb0:8"]]
- 0053ea50 bytes 18641c94
+ 0053ea90 bytes 08651c94
- 0053ea60 ["INT_ADD", "register:40f0:8", ["const:53ea60:8", "const:4:8"]]
- 0053ea60 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053eaa0 ["INT_ADD", "register:40f0:8", ["const:53eaa0:8", "const:4:8"]]
+ 0053eaa0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0053ea60 bytes 14641c94
+ 0053eaa0 bytes 04651c94
- 0053ea9c ["INT_ADD", "register:40f0:8", ["const:53ea9c:8", "const:4:8"]]
- 0053ea9c ["CALL", null, ["callee:00c58430:8"]]
+ 0053eadc ["INT_ADD", "register:40f0:8", ["const:53eadc:8", "const:4:8"]]
+ 0053eadc ["CALL", null, ["callee:00c58430:8"]]
- 0053ea9c bytes 65651c94
+ 0053eadc bytes 55661c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-184be02a2e40442e89348566e50981e4"></a>

### [`0053ec30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053ec30.md) → [`0053ec70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053e/0053ec70.md) FUN_0053ec70

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0050b144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b144.md) [`00520e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520e70.md) · 呼出先 6件 [`0053c138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c138.md) [`0053ee30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053ee30.md) [`0053efc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053efc4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`0050b184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b184.md) [`00520eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520eb0.md) · 呼出先 6件 [`0053c178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c178.md) [`0053ee70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053e/0053ee70.md) [`0053f004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f004.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053eca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053ec30.md#insn-0053eca0) · [`0053ecf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053ec30.md#insn-0053ecf4) · [`0053ed30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053ec30.md#insn-0053ed30)
- 新版 `0053ece0`（命令位置の公開資料なし） · `0053ed34`（命令位置の公開資料なし） · `0053ed70`（命令位置の公開資料なし）

~~~diff
- 0053eca0 ["INT_ADD", "register:40f0:8", ["const:53eca0:8", "const:4:8"]]
- 0053eca0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053ece0 ["INT_ADD", "register:40f0:8", ["const:53ece0:8", "const:4:8"]]
+ 0053ece0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0053eca0 bytes 84631c94
+ 0053ece0 bytes 74641c94
- 0053ecf4 ["INT_ADD", "register:40f0:8", ["const:53ecf4:8", "const:4:8"]]
- 0053ecf4 ["CALL", null, ["callee:0053c178:8"]]
+ 0053ed34 ["INT_ADD", "register:40f0:8", ["const:53ed34:8", "const:4:8"]]
+ 0053ed34 ["CALL", null, ["callee:0053c178:8"]]
- 0053ecf4 bytes 11f5ff97
+ 0053ed34 bytes 11f5ff97
- 0053ed30 ["INT_ADD", "register:40f0:8", ["const:53ed30:8", "const:4:8"]]
- 0053ed30 ["CALL", null, ["callee:0053c178:8"]]
+ 0053ed70 ["INT_ADD", "register:40f0:8", ["const:53ed70:8", "const:4:8"]]
+ 0053ed70 ["CALL", null, ["callee:0053c178:8"]]
- 0053ed30 bytes 02f5ff97
+ 0053ed70 bytes 02f5ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0365c1a4eb6b73ae9096c935af198dba"></a>

### [`0053ef70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053ef70.md) → [`0053efb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053e/0053efb0.md) FUN_0053efb0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0053ee30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053ee30.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0053ee70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053e/0053ee70.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053efb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053ef70.md#insn-0053efb0)
- 新版 `0053eff0`（命令位置の公開資料なし）

~~~diff
- 0053efb0 ["INT_ADD", "register:40f0:8", ["const:53efb0:8", "const:4:8"]]
- 0053efb0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053eff0 ["INT_ADD", "register:40f0:8", ["const:53eff0:8", "const:4:8"]]
+ 0053eff0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0053efb0 bytes c0621c94
+ 0053eff0 bytes b0631c94
~~~


<a id="compare-7f7da78fadfe6851dd86225d3997b251"></a>

### [`0053efd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053efd8.md) → [`0053f018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f018.md) FUN_0053f018

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00520e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520e70.md) [`005b6428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6428.md) [`008a5094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5094.md) [`008a65d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a6/008a65d8.md) · 呼出先 8件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00479670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479670.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 4件 [`00520eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520eb0.md) [`005b6468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6468.md) [`008a50d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a5/008a50d8.md) [`008a661c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a6/008a661c.md) · 呼出先 8件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`004796b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004796b0.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053f06c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053efd8.md#insn-0053f06c) · [`0053f0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053efd8.md#insn-0053f0a0) · [`0053f114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053efd8.md#insn-0053f114)
- 新版 `0053f0ac`（命令位置の公開資料なし） · `0053f0e0`（命令位置の公開資料なし） · `0053f154`（命令位置の公開資料なし）

~~~diff
- 0053f06c ["INT_ADD", "register:40f0:8", ["const:53f06c:8", "const:4:8"]]
- 0053f06c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053f0ac ["INT_ADD", "register:40f0:8", ["const:53f0ac:8", "const:4:8"]]
+ 0053f0ac ["CALL", null, ["callee:00c57eb0:8"]]
- 0053f06c bytes 91621c94
+ 0053f0ac bytes 81631c94
- 0053f0a0 ["INT_ADD", "register:40f0:8", ["const:53f0a0:8", "const:4:8"]]
- 0053f0a0 ["CALL", null, ["callee:00c58430:8"]]
+ 0053f0e0 ["INT_ADD", "register:40f0:8", ["const:53f0e0:8", "const:4:8"]]
+ 0053f0e0 ["CALL", null, ["callee:00c58430:8"]]
- 0053f0a0 bytes e4631c94
+ 0053f0e0 bytes d4641c94
- 0053f114 ["INT_ADD", "register:40f0:8", ["const:53f114:8", "const:4:8"]]
- 0053f114 ["CALL", null, ["callee:0043bb20:8"]]
+ 0053f154 ["INT_ADD", "register:40f0:8", ["const:53f154:8", "const:4:8"]]
+ 0053f154 ["CALL", null, ["callee:0043bb20:8"]]
- 0053f114 bytes 73f2fb97
+ 0053f154 bytes 73f2fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cba3452f2766328b0de4db68720b49a0"></a>

### [`0053f2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f2f0.md) → [`0053f330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f330.md) FUN_0053f330

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0052cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052cdb0.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0053f504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f504.md) [`0053f7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f7d0.md) [`0053f86c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f86c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`0052cdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052cdf0.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0053f544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f544.md) [`0053f810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f810.md) [`0053f8ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f8ac.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053f390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f2f0.md#insn-0053f390) · [`0053f3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f2f0.md#insn-0053f3d0) · [`0053f44c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f2f0.md#insn-0053f44c)
- 新版 `0053f3d0`（命令位置の公開資料なし） · `0053f410`（命令位置の公開資料なし） · `0053f48c`（命令位置の公開資料なし）

~~~diff
- 0053f390 ["INT_ADD", "register:40f0:8", ["const:53f390:8", "const:4:8"]]
- 0053f390 ["CALL", null, ["callee:00c57e90:8"]]
+ 0053f3d0 ["INT_ADD", "register:40f0:8", ["const:53f3d0:8", "const:4:8"]]
+ 0053f3d0 ["CALL", null, ["callee:00c57e90:8"]]
- 0053f390 bytes c0611c94
+ 0053f3d0 bytes b0621c94
- 0053f3d0 ["INT_ADD", "register:40f0:8", ["const:53f3d0:8", "const:4:8"]]
- 0053f3d0 ["CALL", null, ["callee:0053f544:8"]]
+ 0053f410 ["INT_ADD", "register:40f0:8", ["const:53f410:8", "const:4:8"]]
+ 0053f410 ["CALL", null, ["callee:0053f544:8"]]
- 0053f3d0 bytes 4d000094
+ 0053f410 bytes 4d000094
- 0053f44c ["INT_ADD", "register:40f0:8", ["const:53f44c:8", "const:4:8"]]
- 0053f44c ["CALL", null, ["callee:0053f810:8"]]
+ 0053f48c ["INT_ADD", "register:40f0:8", ["const:53f48c:8", "const:4:8"]]
+ 0053f48c ["CALL", null, ["callee:0053f810:8"]]
- 0053f44c bytes e1000094
+ 0053f48c bytes e1000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73be156d00b483621670a33fef4e4082"></a>

### [`0053f504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f504.md) → [`0053f544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f544.md) FUN_0053f544

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0052cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052cdb0.md) [`0053f2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f2f0.md) [`0054eb4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eb4c.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0053f628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f628.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 3件 [`0052cdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052cdf0.md) [`0053f330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f330.md) [`0054eb8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054eb8c.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0053f668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f668.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053f560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f504.md#insn-0053f560) · [`0053f580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f504.md#insn-0053f580) · [`0053f5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f504.md#insn-0053f5bc)
- 新版 `0053f5a0`（命令位置の公開資料なし） · `0053f5c0`（命令位置の公開資料なし） · `0053f5fc`（命令位置の公開資料なし）

~~~diff
- 0053f560 ["INT_ADD", "register:40f0:8", ["const:53f560:8", "const:4:8"]]
- 0053f560 ["CALL", null, ["callee:0053f668:8"]]
+ 0053f5a0 ["INT_ADD", "register:40f0:8", ["const:53f5a0:8", "const:4:8"]]
+ 0053f5a0 ["CALL", null, ["callee:0053f668:8"]]
- 0053f560 bytes 32000094
+ 0053f5a0 bytes 32000094
- 0053f580 ["INT_ADD", "register:40f0:8", ["const:53f580:8", "const:4:8"]]
- 0053f580 ["CALL", null, ["callee:00c57e90:8"]]
+ 0053f5c0 ["INT_ADD", "register:40f0:8", ["const:53f5c0:8", "const:4:8"]]
+ 0053f5c0 ["CALL", null, ["callee:00c57e90:8"]]
- 0053f580 bytes 44611c94
+ 0053f5c0 bytes 34621c94
- 0053f5bc ["INT_ADD", "register:40f0:8", ["const:53f5bc:8", "const:4:8"]]
- 0053f5bc ["CALL", null, ["callee:0043bba4:8"]]
+ 0053f5fc ["INT_ADD", "register:40f0:8", ["const:53f5fc:8", "const:4:8"]]
+ 0053f5fc ["CALL", null, ["callee:0043bba4:8"]]
- 0053f5bc bytes 6af1fb97
+ 0053f5fc bytes 6af1fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c582973675de40ae566ab19f0094ce6"></a>

### [`0053f7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f7d0.md) → [`0053f810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f810.md) FUN_0053f810

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 12件 [`00527d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527d7c.md) [`00527de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527de8.md) [`00528364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00528/00528364.md) [`0052b6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b6f8.md) [`0052c204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c204.md) · 呼出先 2件 [`0053f7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f7d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 12件 [`00527dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527dbc.md) [`00527e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527e28.md) [`005283a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00528/005283a4.md) [`0052b738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b738.md) [`0052c244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c244.md) · 呼出先 2件 [`0053f810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f810.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053f7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f7d0.md#insn-0053f7f0) · [`0053f7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f7d0.md#insn-0053f7fc)
- 新版 `0053f830`（命令位置の公開資料なし） · `0053f83c`（命令位置の公開資料なし）

~~~diff
- 0053f7f0 ["INT_ADD", "register:40f0:8", ["const:53f7f0:8", "const:4:8"]]
- 0053f7f0 ["CALL", null, ["local:b0:8"]]
+ 0053f830 ["INT_ADD", "register:40f0:8", ["const:53f830:8", "const:4:8"]]
+ 0053f830 ["CALL", null, ["local:b0:8"]]
- 0053f7f0 bytes f8ffff97
+ 0053f830 bytes f8ffff97
- 0053f7fc ["INT_ADD", "register:40f0:8", ["const:53f7fc:8", "const:4:8"]]
- 0053f7fc ["CALL", null, ["local:b0:8"]]
+ 0053f83c ["INT_ADD", "register:40f0:8", ["const:53f83c:8", "const:4:8"]]
+ 0053f83c ["CALL", null, ["local:b0:8"]]
- 0053f7fc bytes f5ffff97
+ 0053f83c bytes f5ffff97
~~~


<a id="compare-6a83b76a5bb51e023bbeba9adefa8443"></a>

### [`0053f814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f814.md) → [`0053f854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f854.md) FUN_0053f854

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053f7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f7d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053f810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f810.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053f83c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f814.md#insn-0053f83c)
- 新版 `0053f87c`（命令位置の公開資料なし）

~~~diff
- 0053f83c ["INT_ADD", "register:40f0:8", ["const:53f83c:8", "const:4:8"]]
- 0053f83c ["CALL", null, ["callee:0053f810:8"]]
+ 0053f87c ["INT_ADD", "register:40f0:8", ["const:53f87c:8", "const:4:8"]]
+ 0053f87c ["CALL", null, ["callee:0053f810:8"]]
- 0053f83c bytes e5ffff97
+ 0053f87c bytes e5ffff97
~~~


<a id="compare-bafb4a548311ddae59dd5003f91153b8"></a>

### [`0053f880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f880.md) → [`0053f8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f8c0.md) FUN_0053f8c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0053f7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f7d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0053f810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f810.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053f8b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f880.md#insn-0053f8b8)
- 新版 `0053f8f8`（命令位置の公開資料なし）

~~~diff
- 0053f8b8 ["INT_ADD", "register:40f0:8", ["const:53f8b8:8", "const:4:8"]]
- 0053f8b8 ["CALL", null, ["callee:0053f810:8"]]
+ 0053f8f8 ["INT_ADD", "register:40f0:8", ["const:53f8f8:8", "const:4:8"]]
+ 0053f8f8 ["CALL", null, ["callee:0053f810:8"]]
- 0053f8b8 bytes c6ffff97
+ 0053f8f8 bytes c6ffff97
~~~


<a id="compare-d2b5e3790b097e922bf5e7b01e09409c"></a>

### [`0053f8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f8d0.md) → [`0053f910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f910.md) FUN_0053f910

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00531c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531c94.md) · 呼出先 7件 [`0051ad64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ad64.md) [`0053d720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d720.md) [`0053d7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d7b8.md) [`0053d7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d7cc.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 1件 [`00531cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531cd4.md) · 呼出先 7件 [`0051ada4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051ada4.md) [`0053d760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d760.md) [`0053d7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d7f8.md) [`0053d80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d80c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053f948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f8d0.md#insn-0053f948) · [`0053f96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f8d0.md#insn-0053f96c) · [`0053f9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f8d0.md#insn-0053f9b8)
- 新版 `0053f988`（命令位置の公開資料なし） · `0053f9ac`（命令位置の公開資料なし） · `0053f9f8`（命令位置の公開資料なし）

~~~diff
- 0053f948 ["INT_ADD", "register:40f0:8", ["const:53f948:8", "const:4:8"]]
- 0053f948 ["CALL", null, ["callee:00c57e90:8"]]
+ 0053f988 ["INT_ADD", "register:40f0:8", ["const:53f988:8", "const:4:8"]]
+ 0053f988 ["CALL", null, ["callee:00c57e90:8"]]
- 0053f948 bytes 52601c94
+ 0053f988 bytes 42611c94
- 0053f96c ["INT_ADD", "register:40f0:8", ["const:53f96c:8", "const:4:8"]]
- 0053f96c ["CALL", null, ["callee:0053d80c:8"]]
+ 0053f9ac ["INT_ADD", "register:40f0:8", ["const:53f9ac:8", "const:4:8"]]
+ 0053f9ac ["CALL", null, ["callee:0053d80c:8"]]
- 0053f96c bytes 98f7ff97
+ 0053f9ac bytes 98f7ff97
- 0053f9b8 ["INT_ADD", "register:40f0:8", ["const:53f9b8:8", "const:4:8"]]
- 0053f9b8 ["CALL", null, ["callee:00c57e90:8"]]
+ 0053f9f8 ["INT_ADD", "register:40f0:8", ["const:53f9f8:8", "const:4:8"]]
+ 0053f9f8 ["CALL", null, ["callee:00c57e90:8"]]
- 0053f9b8 bytes 36601c94
+ 0053f9f8 bytes 26611c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-841c922dbede2b818235d09809e0a957"></a>

### [`0053fbcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fbcc.md) → [`0053fc0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053fc0c.md) FUN_0053fc0c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0053fa98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fa98.md) · 呼出先 3件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0053fad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053fad8.md) · 呼出先 3件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053fc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fbcc.md#insn-0053fc20) · [`0053fc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fbcc.md#insn-0053fc2c)
- 新版 `0053fc60`（命令位置の公開資料なし） · `0053fc6c`（命令位置の公開資料なし）

~~~diff
- 0053fc20 ["INT_ADD", "register:40f0:8", ["const:53fc20:8", "const:4:8"]]
- 0053fc20 ["CALL", null, ["callee:0053af90:8"]]
+ 0053fc60 ["INT_ADD", "register:40f0:8", ["const:53fc60:8", "const:4:8"]]
+ 0053fc60 ["CALL", null, ["callee:0053af90:8"]]
- 0053fc20 bytes ccecff97
+ 0053fc60 bytes ccecff97
- 0053fc2c ["INT_ADD", "register:40f0:8", ["const:53fc2c:8", "const:4:8"]]
- 0053fc2c ["CALL", null, ["callee:0046d490:8"]]
+ 0053fc6c ["INT_ADD", "register:40f0:8", ["const:53fc6c:8", "const:4:8"]]
+ 0053fc6c ["CALL", null, ["callee:0046d490:8"]]
- 0053fc2c bytes 09b6fc97
+ 0053fc6c bytes 09b6fc97
~~~


<a id="compare-3ffd25020d8e370f8d26f3514f9d1f99"></a>

### [`0053fc74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fc74.md) → [`0053fcb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053fcb4.md) FUN_0053fcb4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053fcac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fc74.md#insn-0053fcac) · [`0053fcb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fc74.md#insn-0053fcb8)
- 新版 `0053fcec`（命令位置の公開資料なし） · `0053fcf8`（命令位置の公開資料なし）

~~~diff
- 0053fcac ["INT_ADD", "register:40f0:8", ["const:53fcac:8", "const:4:8"]]
- 0053fcac ["CALL", null, ["callee:0053af90:8"]]
+ 0053fcec ["INT_ADD", "register:40f0:8", ["const:53fcec:8", "const:4:8"]]
+ 0053fcec ["CALL", null, ["callee:0053af90:8"]]
- 0053fcac bytes a9ecff97
+ 0053fcec bytes a9ecff97
- 0053fcb8 ["INT_ADD", "register:40f0:8", ["const:53fcb8:8", "const:4:8"]]
- 0053fcb8 ["CALL", null, ["callee:0046d490:8"]]
+ 0053fcf8 ["INT_ADD", "register:40f0:8", ["const:53fcf8:8", "const:4:8"]]
+ 0053fcf8 ["CALL", null, ["callee:0046d490:8"]]
- 0053fcb8 bytes e6b5fc97
+ 0053fcf8 bytes e6b5fc97
~~~


<a id="compare-09541b097ef3af07c26f30cc09d92079"></a>

### [`0053fcd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fcd8.md) → [`0053fd18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053fd18.md) FUN_0053fd18

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00532d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532d40.md) [`0053ff60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053ff60.md) · 呼出先 6件 [`0053fe08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fe08.md) [`0053fec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fec4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`00532d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532d80.md) [`0053ffa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053ffa0.md) · 呼出先 6件 [`0053fe48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053fe48.md) [`0053ff04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053ff04.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053fd24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fcd8.md#insn-0053fd24) · [`0053fd64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fcd8.md#insn-0053fd64) · [`0053fdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fcd8.md#insn-0053fdc8)
- 新版 `0053fd64`（命令位置の公開資料なし） · `0053fda4`（命令位置の公開資料なし） · `0053fe08`（命令位置の公開資料なし）

~~~diff
- 0053fd24 ["INT_ADD", "register:40f0:8", ["const:53fd24:8", "const:4:8"]]
- 0053fd24 ["CALL", null, ["callee:00c57e90:8"]]
+ 0053fd64 ["INT_ADD", "register:40f0:8", ["const:53fd64:8", "const:4:8"]]
+ 0053fd64 ["CALL", null, ["callee:00c57e90:8"]]
- 0053fd24 bytes 5b5f1c94
+ 0053fd64 bytes 4b601c94
- 0053fd64 ["INT_ADD", "register:40f0:8", ["const:53fd64:8", "const:4:8"]]
- 0053fd64 ["CALL", null, ["callee:00c58b40:8"]]
+ 0053fda4 ["INT_ADD", "register:40f0:8", ["const:53fda4:8", "const:4:8"]]
+ 0053fda4 ["CALL", null, ["callee:00c58b40:8"]]
- 0053fd64 bytes 77621c94
+ 0053fda4 bytes 67631c94
- 0053fdc8 ["INT_ADD", "register:40f0:8", ["const:53fdc8:8", "const:4:8"]]
- 0053fdc8 ["CALL", null, ["callee:0053ff04:8"]]
+ 0053fe08 ["INT_ADD", "register:40f0:8", ["const:53fe08:8", "const:4:8"]]
+ 0053fe08 ["CALL", null, ["callee:0053ff04:8"]]
- 0053fdc8 bytes 3f000094
+ 0053fe08 bytes 3f000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8a578776583f62aad5a3a1426241775"></a>

### [`00540694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540694.md) → [`005406d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005406d4.md) FUN_005406d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0050f3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f3ac.md) [`00510d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510d18.md) [`005111e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/005111e4.md) [`005319ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005319ac.md) [`00531e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531e1c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 5件 [`0050f3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f3ec.md) [`00510d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510d58.md) [`00511224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511224.md) [`005319ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005319ec.md) [`00531e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531e5c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005406f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540694.md#insn-005406f8)
- 新版 `00540738`（命令位置の公開資料なし）

~~~diff
- 005406f8 ["INT_ADD", "register:40f0:8", ["const:5406f8:8", "const:4:8"]]
- 005406f8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00540738 ["INT_ADD", "register:40f0:8", ["const:540738:8", "const:4:8"]]
+ 00540738 ["CALL", null, ["callee:00c57eb0:8"]]
- 005406f8 bytes ee5c1c94
+ 00540738 bytes de5d1c94
~~~


<a id="compare-082f8ef5bc691dcdafdfcda3113927da"></a>

### [`0054071c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md) → [`0054075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054075c.md) FUN_0054075c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 29件 [`004e7604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7604.md) [`00520e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520e70.md) [`00522fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522fb8.md) [`005249a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005249a0.md) [`0053212c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/0053212c.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`004795e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004795e4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 29件 [`004e7644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e7644.md) [`00520eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520eb0.md) [`00522ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522ff8.md) [`005249e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/005249e0.md) [`0053216c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/0053216c.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00479624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479624.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00540778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md#insn-00540778) · [`005407ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md#insn-005407ec) · [`0054083c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md#insn-0054083c)
- 新版 `005407b8`（命令位置の公開資料なし） · `0054082c`（命令位置の公開資料なし） · `0054087c`（命令位置の公開資料なし）

~~~diff
- 00540778 ["INT_ADD", "register:40f0:8", ["const:540778:8", "const:4:8"]]
- 00540778 ["CALL", null, ["callee:00c57e90:8"]]
+ 005407b8 ["INT_ADD", "register:40f0:8", ["const:5407b8:8", "const:4:8"]]
+ 005407b8 ["CALL", null, ["callee:00c57e90:8"]]
- 00540778 bytes c65c1c94
+ 005407b8 bytes b65d1c94
- 005407ec ["INT_ADD", "register:40f0:8", ["const:5407ec:8", "const:4:8"]]
- 005407ec ["CALL", null, ["callee:0043bb20:8"]]
+ 0054082c ["INT_ADD", "register:40f0:8", ["const:54082c:8", "const:4:8"]]
+ 0054082c ["CALL", null, ["callee:0043bb20:8"]]
- 005407ec bytes bdecfb97
+ 0054082c bytes bdecfb97
- 0054083c ["INT_ADD", "register:40f0:8", ["const:54083c:8", "const:4:8"]]
- 0054083c ["CALL", null, ["callee:00440f5c:8"]]
+ 0054087c ["INT_ADD", "register:40f0:8", ["const:54087c:8", "const:4:8"]]
+ 0054087c ["CALL", null, ["callee:00440f5c:8"]]
- 0054083c bytes b801fc97
+ 0054087c bytes b801fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2bfda94e383d7d6289ce445ad46bbec"></a>

### [`00540890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540890.md) → [`005408d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005408d0.md) FUN_005408d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`0050e004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050e004.md) [`005292f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/005292f4.md) [`00529d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529d78.md) [`00540890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540890.md) [`00b6a414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6a414.md) · 呼出先 2件 [`00540890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540890.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 7件 [`0050e044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050e044.md) [`00529334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529334.md) [`00529db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529db8.md) [`005408d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005408d0.md) [`00b6a83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6a/00b6a83c.md) · 呼出先 2件 [`005408d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005408d0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005408ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540890.md#insn-005408ac) · [`005408b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540890.md#insn-005408b8) · [`005408c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540890.md#insn-005408c8)
- 新版 `005408ec`（命令位置の公開資料なし） · `005408f8`（命令位置の公開資料なし） · `00540908`（命令位置の公開資料なし）

~~~diff
- 005408ac ["INT_ADD", "register:40f0:8", ["const:5408ac:8", "const:4:8"]]
- 005408ac ["CALL", null, ["local:b0:8"]]
+ 005408ec ["INT_ADD", "register:40f0:8", ["const:5408ec:8", "const:4:8"]]
+ 005408ec ["CALL", null, ["local:b0:8"]]
- 005408ac bytes f9ffff97
+ 005408ec bytes f9ffff97
- 005408b8 ["INT_ADD", "register:40f0:8", ["const:5408b8:8", "const:4:8"]]
- 005408b8 ["CALL", null, ["local:b0:8"]]
+ 005408f8 ["INT_ADD", "register:40f0:8", ["const:5408f8:8", "const:4:8"]]
+ 005408f8 ["CALL", null, ["local:b0:8"]]
- 005408b8 bytes f6ffff97
+ 005408f8 bytes f6ffff97
- 005408c8 ["INT_ADD", "register:40f0:8", ["const:5408c8:8", "const:4:8"]]
- 005408c8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00540908 ["INT_ADD", "register:40f0:8", ["const:540908:8", "const:4:8"]]
+ 00540908 ["CALL", null, ["callee:00c57eb0:8"]]
- 005408c8 bytes 7a5c1c94
+ 00540908 bytes 6a5d1c94
~~~


<a id="compare-9a2e9051ade040030a01f5aa68c0e005"></a>

### [`00540c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540c24.md) → [`00540c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540c64.md) FUN_00540c64

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004ad734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad734.md) · 呼出先 4件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`004ad774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad774.md) · 呼出先 4件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00540c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540c24.md#insn-00540c68) · [`00540ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540c24.md#insn-00540ca0) · [`00540ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540c24.md#insn-00540ce8)
- 新版 `00540ca8`（命令位置の公開資料なし） · `00540ce0`（命令位置の公開資料なし） · `00540d28`（命令位置の公開資料なし）

~~~diff
- 00540c68 ["INT_ADD", "register:40f0:8", ["const:540c68:8", "const:4:8"]]
- 00540c68 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00540ca8 ["INT_ADD", "register:40f0:8", ["const:540ca8:8", "const:4:8"]]
+ 00540ca8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00540c68 bytes 925b1c94
+ 00540ca8 bytes 825c1c94
- 00540ca0 ["INT_ADD", "register:40f0:8", ["const:540ca0:8", "const:4:8"]]
- 00540ca0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00540ce0 ["INT_ADD", "register:40f0:8", ["const:540ce0:8", "const:4:8"]]
+ 00540ce0 ["CALL", null, ["callee:00c57e90:8"]]
- 00540ca0 bytes 7c5b1c94
+ 00540ce0 bytes 6c5c1c94
- 00540ce8 ["INT_ADD", "register:40f0:8", ["const:540ce8:8", "const:4:8"]]
- 00540ce8 ["CALL", null, ["callee:00c57f40:8"]]
+ 00540d28 ["INT_ADD", "register:40f0:8", ["const:540d28:8", "const:4:8"]]
+ 00540d28 ["CALL", null, ["callee:00c57f40:8"]]
- 00540ce8 bytes 965b1c94
+ 00540d28 bytes 865c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdaf5bb769a73359b437880371fb29c4"></a>

### [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) → [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) FUN_00540d7c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 34件 [`004add24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004add24.md) [`004bc238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc238.md) [`004cc00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc00c.md) [`004cd868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd868.md) [`004ce6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce6a8.md) · 呼出先 7件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 34件 [`004add64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004add64.md) [`004bc278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc278.md) [`004cc04c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc04c.md) [`004cd8a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd8a8.md) [`004ce6e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce6e8.md) · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00540de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md#insn-00540de0) · [`00540e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md#insn-00540e28) · [`00540e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md#insn-00540e50)
- 新版 `00540e20`（命令位置の公開資料なし） · `00540e68`（命令位置の公開資料なし） · `00540e90`（命令位置の公開資料なし）

~~~diff
- 00540de0 ["INT_ADD", "register:40f0:8", ["const:540de0:8", "const:4:8"]]
- 00540de0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00540e20 ["INT_ADD", "register:40f0:8", ["const:540e20:8", "const:4:8"]]
+ 00540e20 ["CALL", null, ["callee:00c57e90:8"]]
- 00540de0 bytes 2c5b1c94
+ 00540e20 bytes 1c5c1c94
- 00540e28 ["INT_ADD", "register:40f0:8", ["const:540e28:8", "const:4:8"]]
- 00540e28 ["CALL", null, ["callee:0043bb20:8"]]
+ 00540e68 ["INT_ADD", "register:40f0:8", ["const:540e68:8", "const:4:8"]]
+ 00540e68 ["CALL", null, ["callee:0043bb20:8"]]
- 00540e28 bytes 2eebfb97
+ 00540e68 bytes 2eebfb97
- 00540e50 ["INT_ADD", "register:40f0:8", ["const:540e50:8", "const:4:8"]]
- 00540e50 ["CALL", null, ["callee:00c58000:8"]]
+ 00540e90 ["INT_ADD", "register:40f0:8", ["const:540e90:8", "const:4:8"]]
+ 00540e90 ["CALL", null, ["callee:00c58000:8"]]
- 00540e50 bytes 6c5b1c94
+ 00540e90 bytes 5c5c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1859706a4d10ec3a521bdb4a8228883"></a>

### [`0054104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/0054104c.md) → [`0054108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/0054108c.md) FUN_0054108c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004b1b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1b14.md) · 呼出先 4件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`004b1b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1b54.md) · 呼出先 4件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00541090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/0054104c.md#insn-00541090) · [`005410c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/0054104c.md#insn-005410c8) · [`00541110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/0054104c.md#insn-00541110)
- 新版 `005410d0`（命令位置の公開資料なし） · `00541108`（命令位置の公開資料なし） · `00541150`（命令位置の公開資料なし）

~~~diff
- 00541090 ["INT_ADD", "register:40f0:8", ["const:541090:8", "const:4:8"]]
- 00541090 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005410d0 ["INT_ADD", "register:40f0:8", ["const:5410d0:8", "const:4:8"]]
+ 005410d0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00541090 bytes 885a1c94
+ 005410d0 bytes 785b1c94
- 005410c8 ["INT_ADD", "register:40f0:8", ["const:5410c8:8", "const:4:8"]]
- 005410c8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00541108 ["INT_ADD", "register:40f0:8", ["const:541108:8", "const:4:8"]]
+ 00541108 ["CALL", null, ["callee:00c57e90:8"]]
- 005410c8 bytes 725a1c94
+ 00541108 bytes 625b1c94
- 00541110 ["INT_ADD", "register:40f0:8", ["const:541110:8", "const:4:8"]]
- 00541110 ["CALL", null, ["callee:00c57f40:8"]]
+ 00541150 ["INT_ADD", "register:40f0:8", ["const:541150:8", "const:4:8"]]
+ 00541150 ["CALL", null, ["callee:00c57f40:8"]]
- 00541110 bytes 8c5a1c94
+ 00541150 bytes 7c5b1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1950c9755d0bdeec8028c92577ee85a1"></a>

### [`00541270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541270.md) → [`005412b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005412b0.md) FUN_005412b0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004b1eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1eac.md) [`00541270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541270.md) · 呼出先 9件 [`00541270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541270.md) [`00541884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541884.md) [`00541ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541ae8.md) [`00541e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541e1c.md) [`0054214c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/0054214c.md)
- 新版 呼出元 2件 [`004b1eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1eec.md) [`005412b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005412b0.md) · 呼出先 9件 [`005412b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005412b0.md) [`005418c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005418c4.md) [`00541b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/00541b28.md) [`00541e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/00541e5c.md) [`0054218c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00542/0054218c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00541330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541270.md#insn-00541330) · [`00541358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541270.md#insn-00541358) · [`0054136c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541270.md#insn-0054136c)
- 新版 `00541370`（命令位置の公開資料なし） · `00541398`（命令位置の公開資料なし） · `005413ac`（命令位置の公開資料なし）

~~~diff
- 00541330 ["INT_ADD", "register:40f0:8", ["const:541330:8", "const:4:8"]]
- 00541330 ["CALL", null, ["callee:005418c4:8"]]
+ 00541370 ["INT_ADD", "register:40f0:8", ["const:541370:8", "const:4:8"]]
+ 00541370 ["CALL", null, ["callee:005418c4:8"]]
- 00541330 bytes 55010094
+ 00541370 bytes 55010094
- 00541358 ["INT_ADD", "register:40f0:8", ["const:541358:8", "const:4:8"]]
- 00541358 ["CALL", null, ["callee:005418c4:8"]]
+ 00541398 ["INT_ADD", "register:40f0:8", ["const:541398:8", "const:4:8"]]
+ 00541398 ["CALL", null, ["callee:005418c4:8"]]
- 00541358 bytes 4b010094
+ 00541398 bytes 4b010094
- 0054136c ["INT_ADD", "register:40f0:8", ["const:54136c:8", "const:4:8"]]
- 0054136c ["CALL", null, ["callee:005418c4:8"]]
+ 005413ac ["INT_ADD", "register:40f0:8", ["const:5413ac:8", "const:4:8"]]
+ 005413ac ["CALL", null, ["callee:005418c4:8"]]
- 0054136c bytes 46010094
+ 005413ac bytes 46010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2226a11aa894d4d1329255a52a418b0f"></a>

### [`0054214c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/0054214c.md) → [`0054218c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00542/0054218c.md) FUN_0054218c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00541270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541270.md) · 呼出先 3件 [`00541884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541884.md) [`005423d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/005423d4.md) [`00542568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/00542568.md)
- 新版 呼出元 1件 [`005412b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005412b0.md) · 呼出先 3件 [`005418c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005418c4.md) [`00542414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00542/00542414.md) [`005425a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00542/005425a8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005421b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/0054214c.md#insn-005421b0) · [`00542220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/0054214c.md#insn-00542220) · [`00542244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/0054214c.md#insn-00542244)
- 新版 `005421f0`（命令位置の公開資料なし） · `00542260`（命令位置の公開資料なし） · `00542284`（命令位置の公開資料なし）

~~~diff
- 005421b0 ["INT_ADD", "register:40f0:8", ["const:5421b0:8", "const:4:8"]]
- 005421b0 ["CALL", null, ["callee:005425a8:8"]]
+ 005421f0 ["INT_ADD", "register:40f0:8", ["const:5421f0:8", "const:4:8"]]
+ 005421f0 ["CALL", null, ["callee:005425a8:8"]]
- 005421b0 bytes ee000094
+ 005421f0 bytes ee000094
- 00542220 ["INT_ADD", "register:40f0:8", ["const:542220:8", "const:4:8"]]
- 00542220 ["CALL", null, ["callee:005418c4:8"]]
+ 00542260 ["INT_ADD", "register:40f0:8", ["const:542260:8", "const:4:8"]]
+ 00542260 ["CALL", null, ["callee:005418c4:8"]]
- 00542220 bytes 99fdff97
+ 00542260 bytes 99fdff97
- 00542244 ["INT_ADD", "register:40f0:8", ["const:542244:8", "const:4:8"]]
- 00542244 ["CALL", null, ["callee:005418c4:8"]]
+ 00542284 ["INT_ADD", "register:40f0:8", ["const:542284:8", "const:4:8"]]
+ 00542284 ["CALL", null, ["callee:005418c4:8"]]
- 00542244 bytes 90fdff97
+ 00542284 bytes 90fdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb67340f48a4219b2800552692f9c584"></a>

### [`005423d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/005423d4.md) → [`00542414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00542/00542414.md) FUN_00542414

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00541270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541270.md) [`0054214c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/0054214c.md) [`00542568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/00542568.md) · 呼出先 1件 [`00541884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541884.md)
- 新版 呼出元 3件 [`005412b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005412b0.md) [`0054218c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00542/0054218c.md) [`005425a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00542/005425a8.md) · 呼出先 1件 [`005418c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005418c4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005423f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/005423d4.md#insn-005423f8)
- 新版 `00542438`（命令位置の公開資料なし）

~~~diff
- 005423f8 ["INT_ADD", "register:40f0:8", ["const:5423f8:8", "const:4:8"]]
- 005423f8 ["CALL", null, ["callee:005418c4:8"]]
+ 00542438 ["INT_ADD", "register:40f0:8", ["const:542438:8", "const:4:8"]]
+ 00542438 ["CALL", null, ["callee:005418c4:8"]]
- 005423f8 bytes 23fdff97
+ 00542438 bytes 23fdff97
~~~


<a id="compare-2e20b15ff5b5076321d910ef8989778c"></a>

### [`00542568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/00542568.md) → [`005425a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00542/005425a8.md) FUN_005425a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00541270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541270.md) [`0054214c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/0054214c.md) · 呼出先 1件 [`005423d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/005423d4.md)
- 新版 呼出元 2件 [`005412b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005412b0.md) [`0054218c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00542/0054218c.md) · 呼出先 1件 [`00542414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00542/00542414.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00542594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/00542568.md#insn-00542594)
- 新版 `005425d4`（命令位置の公開資料なし）

~~~diff
- 00542594 ["INT_ADD", "register:40f0:8", ["const:542594:8", "const:4:8"]]
- 00542594 ["CALL", null, ["callee:00542414:8"]]
+ 005425d4 ["INT_ADD", "register:40f0:8", ["const:5425d4:8", "const:4:8"]]
+ 005425d4 ["CALL", null, ["callee:00542414:8"]]
- 00542594 bytes 90ffff97
+ 005425d4 bytes 90ffff97
~~~


<a id="compare-7f923b39b5598eca276e82d5e3a95f8a"></a>

### [`00542f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/00542f48.md) → [`00542f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00542/00542f88.md) FUN_00542f88

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004a5398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5398.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`005430fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/005430fc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`004a53d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a53d8.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`0054313c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/0054313c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00542fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/00542f48.md#insn-00542fe8) · [`005430b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/00542f48.md#insn-005430b0) · [`005430d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/00542f48.md#insn-005430d4)
- 新版 `00543028`（命令位置の公開資料なし） · `005430f0`（命令位置の公開資料なし） · `00543114`（命令位置の公開資料なし）

~~~diff
- 00542fe8 ["INT_ADD", "register:40f0:8", ["const:542fe8:8", "const:4:8"]]
- 00542fe8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00543028 ["INT_ADD", "register:40f0:8", ["const:543028:8", "const:4:8"]]
+ 00543028 ["CALL", null, ["callee:00c57e90:8"]]
- 00542fe8 bytes aa521c94
+ 00543028 bytes 9a531c94
- 005430b0 ["INT_ADD", "register:40f0:8", ["const:5430b0:8", "const:4:8"]]
- 005430b0 ["CALL", null, ["callee:00535b80:8"]]
+ 005430f0 ["INT_ADD", "register:40f0:8", ["const:5430f0:8", "const:4:8"]]
+ 005430f0 ["CALL", null, ["callee:00535b80:8"]]
- 005430b0 bytes a4caff97
+ 005430f0 bytes a4caff97
- 005430d4 ["INT_ADD", "register:40f0:8", ["const:5430d4:8", "const:4:8"]]
- 005430d4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00543114 ["INT_ADD", "register:40f0:8", ["const:543114:8", "const:4:8"]]
+ 00543114 ["CALL", null, ["callee:00c57eb0:8"]]
- 005430d4 bytes 77521c94
+ 00543114 bytes 67531c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fea7f923f70ec8de31a39fc294ae127"></a>

### [`00543110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543110.md) → [`00543150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543150.md) FUN_00543150

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004b3ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b3ea4.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0054336c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054336c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`004b3ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3ee4.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005433ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/005433ac.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00543194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543110.md#insn-00543194) · [`005431e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543110.md#insn-005431e4) · [`0054325c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543110.md#insn-0054325c)
- 新版 `005431d4`（命令位置の公開資料なし） · `00543224`（命令位置の公開資料なし） · `0054329c`（命令位置の公開資料なし）

~~~diff
- 00543194 ["INT_ADD", "register:40f0:8", ["const:543194:8", "const:4:8"]]
- 00543194 ["CALL", null, ["callee:00c57e90:8"]]
+ 005431d4 ["INT_ADD", "register:40f0:8", ["const:5431d4:8", "const:4:8"]]
+ 005431d4 ["CALL", null, ["callee:00c57e90:8"]]
- 00543194 bytes 3f521c94
+ 005431d4 bytes 2f531c94
- 005431e4 ["INT_ADD", "register:40f0:8", ["const:5431e4:8", "const:4:8"]]
- 005431e4 ["CALL", null, ["callee:0043bb20:8"]]
+ 00543224 ["INT_ADD", "register:40f0:8", ["const:543224:8", "const:4:8"]]
+ 00543224 ["CALL", null, ["callee:0043bb20:8"]]
- 005431e4 bytes 3fe2fb97
+ 00543224 bytes 3fe2fb97
- 0054325c ["INT_ADD", "register:40f0:8", ["const:54325c:8", "const:4:8"]]
- 0054325c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054329c ["INT_ADD", "register:40f0:8", ["const:54329c:8", "const:4:8"]]
+ 0054329c ["CALL", null, ["callee:00c57eb0:8"]]
- 0054325c bytes 15521c94
+ 0054329c bytes 05531c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5acb41e5216e291de4f1caf1671d5ee2"></a>

### [`00543304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543304.md) → [`00543344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543344.md) FUN_00543344

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00543354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543304.md#insn-00543354)
- 新版 `00543394`（命令位置の公開資料なし）

~~~diff
- 00543354 ["INT_ADD", "register:40f0:8", ["const:543354:8", "const:4:8"]]
- 00543354 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00543394 ["INT_ADD", "register:40f0:8", ["const:543394:8", "const:4:8"]]
+ 00543394 ["CALL", null, ["callee:00c57eb0:8"]]
- 00543354 bytes d7511c94
+ 00543394 bytes c7521c94
~~~


<a id="compare-b84e6abb46ab13aea12bef8f2897e84e"></a>

### [`005434e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/005434e8.md) → [`00543528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543528.md) FUN_00543528

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004b8500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8500.md) [`004fe3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fe3e8.md) · 呼出先 4件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c58200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58200.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 2件 [`004b8540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8540.md) [`004fe428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004fe428.md) · 呼出先 4件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c58600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58600.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00543524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/005434e8.md#insn-00543524) · [`00543584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/005434e8.md#insn-00543584) · [`005435a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/005434e8.md#insn-005435a4)
- 新版 `00543564`（命令位置の公開資料なし） · `005435c4`（命令位置の公開資料なし） · `005435e4`（命令位置の公開資料なし）

~~~diff
- 00543524 ["INT_ADD", "register:40f0:8", ["const:543524:8", "const:4:8"]]
- 00543524 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00543564 ["INT_ADD", "register:40f0:8", ["const:543564:8", "const:4:8"]]
+ 00543564 ["CALL", null, ["callee:00c59dd0:8"]]
- 00543524 bytes 2b591c94
+ 00543564 bytes 1b5a1c94
- 00543584 ["COPY", "register:0:8", ["register:4040:8"]]
- 00543584 ["INT_ADD", "register:40f0:8", ["const:543584:8", "const:4:8"]]
- 00543584 ["CALLIND", null, ["register:0:8"]]
+ 005435c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005435c4 ["INT_ADD", "register:40f0:8", ["const:5435c4:8", "const:4:8"]]
+ 005435c4 ["CALLIND", null, ["register:0:8"]]
- 00543584 bytes 00013fd6
+ 005435c4 bytes 00013fd6
- 005435a4 ["INT_ADD", "register:40f0:8", ["const:5435a4:8", "const:4:8"]]
- 005435a4 ["CALL", null, ["callee:00c58600:8"]]
+ 005435e4 ["INT_ADD", "register:40f0:8", ["const:5435e4:8", "const:4:8"]]
+ 005435e4 ["CALL", null, ["callee:00c58600:8"]]
- 005435a4 bytes 17531c94
+ 005435e4 bytes 07541c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc8b152bf6d615d5743f26b06eff1f75"></a>

### [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) → [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) FUN_00543c5c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 20件 [`004c3ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3ed8.md) [`004c4028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4028.md) [`004c41c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c41c0.md) [`004c4468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4468.md) [`004c46b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c46b4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00543d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543d48.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 20件 [`004c3f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c3f18.md) [`004c4068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4068.md) [`004c4200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4200.md) [`004c44a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c44a8.md) [`004c46f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c46f4.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00543d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543d88.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00543c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md#insn-00543c94) · [`00543cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md#insn-00543cb8) · [`00543ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md#insn-00543ce4)
- 新版 `00543cd4`（命令位置の公開資料なし） · `00543cf8`（命令位置の公開資料なし） · `00543d24`（命令位置の公開資料なし）

~~~diff
- 00543c94 ["INT_ADD", "register:40f0:8", ["const:543c94:8", "const:4:8"]]
- 00543c94 ["CALL", null, ["callee:00c57e90:8"]]
+ 00543cd4 ["INT_ADD", "register:40f0:8", ["const:543cd4:8", "const:4:8"]]
+ 00543cd4 ["CALL", null, ["callee:00c57e90:8"]]
- 00543c94 bytes 7f4f1c94
+ 00543cd4 bytes 6f501c94
- 00543cb8 ["INT_ADD", "register:40f0:8", ["const:543cb8:8", "const:4:8"]]
- 00543cb8 ["CALL", null, ["callee:00c58090:8"]]
+ 00543cf8 ["INT_ADD", "register:40f0:8", ["const:543cf8:8", "const:4:8"]]
+ 00543cf8 ["CALL", null, ["callee:00c58090:8"]]
- 00543cb8 bytes f64f1c94
+ 00543cf8 bytes e6501c94
- 00543ce4 ["INT_ADD", "register:40f0:8", ["const:543ce4:8", "const:4:8"]]
- 00543ce4 ["CALL", null, ["callee:00c58090:8"]]
+ 00543d24 ["INT_ADD", "register:40f0:8", ["const:543d24:8", "const:4:8"]]
+ 00543d24 ["CALL", null, ["callee:00c58090:8"]]
- 00543ce4 bytes eb4f1c94
+ 00543d24 bytes db501c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a884579cbe5870c327df25db781fe53"></a>

### [`00543d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543d5c.md) → [`00543d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543d9c.md) FUN_00543d9c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`004c5348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5348.md) [`004c54a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c54a0.md) [`004c6acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6acc.md) [`004ca930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca930.md) · 呼出先 5件 [`00543d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543d48.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 4件 [`004c5388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5388.md) [`004c54e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c54e0.md) [`004c6b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c6b0c.md) [`004ca970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004ca970.md) · 呼出先 5件 [`00543d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543d88.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00543da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543d5c.md#insn-00543da0) · [`00543de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543d5c.md#insn-00543de8) · [`00543e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543d5c.md#insn-00543e10)
- 新版 `00543de0`（命令位置の公開資料なし） · `00543e28`（命令位置の公開資料なし） · `00543e50`（命令位置の公開資料なし）

~~~diff
- 00543da0 ["INT_ADD", "register:40f0:8", ["const:543da0:8", "const:4:8"]]
- 00543da0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00543de0 ["INT_ADD", "register:40f0:8", ["const:543de0:8", "const:4:8"]]
+ 00543de0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00543da0 bytes 444f1c94
+ 00543de0 bytes 34501c94
- 00543de8 ["INT_ADD", "register:40f0:8", ["const:543de8:8", "const:4:8"]]
- 00543de8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00543e28 ["INT_ADD", "register:40f0:8", ["const:543e28:8", "const:4:8"]]
+ 00543e28 ["CALL", null, ["callee:00c57e90:8"]]
- 00543de8 bytes 2a4f1c94
+ 00543e28 bytes 1a501c94
- 00543e10 ["INT_ADD", "register:40f0:8", ["const:543e10:8", "const:4:8"]]
- 00543e10 ["CALL", null, ["callee:00c58000:8"]]
+ 00543e50 ["INT_ADD", "register:40f0:8", ["const:543e50:8", "const:4:8"]]
+ 00543e50 ["CALL", null, ["callee:00c58000:8"]]
- 00543e10 bytes 7c4f1c94
+ 00543e50 bytes 6c501c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e497d08a7afb889a1a71863807a7eb24"></a>

### [`00543e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543e8c.md) → [`00543ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543ecc.md) FUN_00543ecc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004c7a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7a88.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0054434c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/0054434c.md) [`005444d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/005444d4.md) [`00544660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544660.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`004c7ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7ac8.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0054438c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/0054438c.md) [`00544514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/00544514.md) [`005446a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/005446a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00543f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543e8c.md#insn-00543f24) · [`00543f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543e8c.md#insn-00543f68) · [`00543f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543e8c.md#insn-00543f78)
- 新版 `00543f64`（命令位置の公開資料なし） · `00543fa8`（命令位置の公開資料なし） · `00543fb8`（命令位置の公開資料なし）

~~~diff
- 00543f24 ["INT_ADD", "register:40f0:8", ["const:543f24:8", "const:4:8"]]
- 00543f24 ["CALL", null, ["callee:00c57f40:8"]]
+ 00543f64 ["INT_ADD", "register:40f0:8", ["const:543f64:8", "const:4:8"]]
+ 00543f64 ["CALL", null, ["callee:00c57f40:8"]]
- 00543f24 bytes 074f1c94
+ 00543f64 bytes f74f1c94
- 00543f68 ["INT_ADD", "register:40f0:8", ["const:543f68:8", "const:4:8"]]
- 00543f68 ["CALL", null, ["callee:00c57e90:8"]]
+ 00543fa8 ["INT_ADD", "register:40f0:8", ["const:543fa8:8", "const:4:8"]]
+ 00543fa8 ["CALL", null, ["callee:00c57e90:8"]]
- 00543f68 bytes ca4e1c94
+ 00543fa8 bytes ba4f1c94
- 00543f78 ["INT_ADD", "register:40f0:8", ["const:543f78:8", "const:4:8"]]
- 00543f78 ["CALL", null, ["callee:0054438c:8"]]
+ 00543fb8 ["INT_ADD", "register:40f0:8", ["const:543fb8:8", "const:4:8"]]
+ 00543fb8 ["CALL", null, ["callee:0054438c:8"]]
- 00543f78 bytes f5000094
+ 00543fb8 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26fa8d2572dd29f7d4a0e0d20a45dd04"></a>

### [`0054434c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/0054434c.md) → [`0054438c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/0054438c.md) FUN_0054438c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00543e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543e8c.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00543ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543ecc.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005443b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/0054434c.md#insn-005443b4) · [`005443ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/0054434c.md#insn-005443ec) · [`0054449c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/0054434c.md#insn-0054449c)
- 新版 `005443f4`（命令位置の公開資料なし） · `0054442c`（命令位置の公開資料なし） · `005444dc`（命令位置の公開資料なし）

~~~diff
- 005443b4 ["INT_ADD", "register:40f0:8", ["const:5443b4:8", "const:4:8"]]
- 005443b4 ["CALL", null, ["callee:00c57f40:8"]]
+ 005443f4 ["INT_ADD", "register:40f0:8", ["const:5443f4:8", "const:4:8"]]
+ 005443f4 ["CALL", null, ["callee:00c57f40:8"]]
- 005443b4 bytes e34d1c94
+ 005443f4 bytes d34e1c94
- 005443ec ["INT_ADD", "register:40f0:8", ["const:5443ec:8", "const:4:8"]]
- 005443ec ["CALL", null, ["callee:00c57e90:8"]]
+ 0054442c ["INT_ADD", "register:40f0:8", ["const:54442c:8", "const:4:8"]]
+ 0054442c ["CALL", null, ["callee:00c57e90:8"]]
- 005443ec bytes a94d1c94
+ 0054442c bytes 994e1c94
- 0054449c ["INT_ADD", "register:40f0:8", ["const:54449c:8", "const:4:8"]]
- 0054449c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005444dc ["INT_ADD", "register:40f0:8", ["const:5444dc:8", "const:4:8"]]
+ 005444dc ["CALL", null, ["callee:00c57eb0:8"]]
- 0054449c bytes 854d1c94
+ 005444dc bytes 754e1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dce5d3e398f0d06956d1bb34ae9ea456"></a>

### [`005444d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/005444d4.md) → [`00544514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/00544514.md) FUN_00544514

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00543e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543e8c.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00543ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543ecc.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00544544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/005444d4.md#insn-00544544) · [`0054457c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/005444d4.md#insn-0054457c) · [`0054462c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/005444d4.md#insn-0054462c)
- 新版 `00544584`（命令位置の公開資料なし） · `005445bc`（命令位置の公開資料なし） · `0054466c`（命令位置の公開資料なし）

~~~diff
- 00544544 ["INT_ADD", "register:40f0:8", ["const:544544:8", "const:4:8"]]
- 00544544 ["CALL", null, ["callee:00c57f40:8"]]
+ 00544584 ["INT_ADD", "register:40f0:8", ["const:544584:8", "const:4:8"]]
+ 00544584 ["CALL", null, ["callee:00c57f40:8"]]
- 00544544 bytes 7f4d1c94
+ 00544584 bytes 6f4e1c94
- 0054457c ["INT_ADD", "register:40f0:8", ["const:54457c:8", "const:4:8"]]
- 0054457c ["CALL", null, ["callee:00c57e90:8"]]
+ 005445bc ["INT_ADD", "register:40f0:8", ["const:5445bc:8", "const:4:8"]]
+ 005445bc ["CALL", null, ["callee:00c57e90:8"]]
- 0054457c bytes 454d1c94
+ 005445bc bytes 354e1c94
- 0054462c ["INT_ADD", "register:40f0:8", ["const:54462c:8", "const:4:8"]]
- 0054462c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0054466c ["INT_ADD", "register:40f0:8", ["const:54466c:8", "const:4:8"]]
+ 0054466c ["CALL", null, ["callee:00c57eb0:8"]]
- 0054462c bytes 214d1c94
+ 0054466c bytes 114e1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3be8cd02a40c5ffc4d12b41b3392f5aa"></a>

### [`00544660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544660.md) → [`005446a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/005446a0.md) FUN_005446a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00543e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543e8c.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00543ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543ecc.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005446d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544660.md#insn-005446d0) · [`00544708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544660.md#insn-00544708) · [`005447b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544660.md#insn-005447b8)
- 新版 `00544710`（命令位置の公開資料なし） · `00544748`（命令位置の公開資料なし） · `005447f8`（命令位置の公開資料なし）

~~~diff
- 005446d0 ["INT_ADD", "register:40f0:8", ["const:5446d0:8", "const:4:8"]]
- 005446d0 ["CALL", null, ["callee:00c57f40:8"]]
+ 00544710 ["INT_ADD", "register:40f0:8", ["const:544710:8", "const:4:8"]]
+ 00544710 ["CALL", null, ["callee:00c57f40:8"]]
- 005446d0 bytes 1c4d1c94
+ 00544710 bytes 0c4e1c94
- 00544708 ["INT_ADD", "register:40f0:8", ["const:544708:8", "const:4:8"]]
- 00544708 ["CALL", null, ["callee:00c57e90:8"]]
+ 00544748 ["INT_ADD", "register:40f0:8", ["const:544748:8", "const:4:8"]]
+ 00544748 ["CALL", null, ["callee:00c57e90:8"]]
- 00544708 bytes e24c1c94
+ 00544748 bytes d24d1c94
- 005447b8 ["INT_ADD", "register:40f0:8", ["const:5447b8:8", "const:4:8"]]
- 005447b8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005447f8 ["INT_ADD", "register:40f0:8", ["const:5447f8:8", "const:4:8"]]
+ 005447f8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005447b8 bytes be4c1c94
+ 005447f8 bytes ae4d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82234cfd9ec0aa869436c31a532e6aac"></a>

### [`005447ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/005447ec.md) → [`0054482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/0054482c.md) FUN_0054482c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004c80d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c80d0.md) [`004c810c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c810c.md) · 呼出先 2件 [`0053078c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053078c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`004c8110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8110.md) [`004c814c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c814c.md) · 呼出先 2件 [`005307cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005307cc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00544870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/005447ec.md#insn-00544870) · [`00544878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/005447ec.md#insn-00544878) · [`005448c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/005447ec.md#insn-005448c0)
- 新版 `005448b0`（命令位置の公開資料なし） · `005448b8`（命令位置の公開資料なし） · `00544900`（命令位置の公開資料なし）

~~~diff
- 00544870 ["INT_ADD", "register:40f0:8", ["const:544870:8", "const:4:8"]]
- 00544870 ["CALL", null, ["callee:005307cc:8"]]
+ 005448b0 ["INT_ADD", "register:40f0:8", ["const:5448b0:8", "const:4:8"]]
+ 005448b0 ["CALL", null, ["callee:005307cc:8"]]
- 00544870 bytes c7afff97
+ 005448b0 bytes c7afff97
- 00544878 ["INT_ADD", "register:40f0:8", ["const:544878:8", "const:4:8"]]
- 00544878 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005448b8 ["INT_ADD", "register:40f0:8", ["const:5448b8:8", "const:4:8"]]
+ 005448b8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00544878 bytes 8e4c1c94
+ 005448b8 bytes 7e4d1c94
- 005448c0 ["INT_ADD", "register:40f0:8", ["const:5448c0:8", "const:4:8"]]
- 005448c0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00544900 ["INT_ADD", "register:40f0:8", ["const:544900:8", "const:4:8"]]
+ 00544900 ["CALL", null, ["callee:00c57eb0:8"]]
- 005448c0 bytes 7c4c1c94
+ 00544900 bytes 6c4d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18012cef2585b4a960a648c7295cd263"></a>

### [`00544984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544984.md) → [`005449c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/005449c4.md) FUN_005449c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004cb1c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb1c4.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d30.md) [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c57d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d50.md)
- 新版 呼出元 1件 [`004cb204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb204.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58130.md) [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005449ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544984.md#insn-005449ac) · [`005449bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544984.md#insn-005449bc) · [`005449dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544984.md#insn-005449dc)
- 新版 `005449ec`（命令位置の公開資料なし） · `005449fc`（命令位置の公開資料なし） · `00544a1c`（命令位置の公開資料なし）

~~~diff
- 005449ac ["INT_ADD", "register:40f0:8", ["const:5449ac:8", "const:4:8"]]
- 005449ac ["CALL", null, ["callee:00c58130:8"]]
+ 005449ec ["INT_ADD", "register:40f0:8", ["const:5449ec:8", "const:4:8"]]
+ 005449ec ["CALL", null, ["callee:00c58130:8"]]
- 005449ac bytes e14c1c94
+ 005449ec bytes d14d1c94
- 005449bc ["INT_ADD", "register:40f0:8", ["const:5449bc:8", "const:4:8"]]
- 005449bc ["CALL", null, ["callee:00c58140:8"]]
+ 005449fc ["INT_ADD", "register:40f0:8", ["const:5449fc:8", "const:4:8"]]
+ 005449fc ["CALL", null, ["callee:00c58140:8"]]
- 005449bc bytes e14c1c94
+ 005449fc bytes d14d1c94
- 005449dc ["COPY", "register:0:8", ["register:4040:8"]]
- 005449dc ["INT_ADD", "register:40f0:8", ["const:5449dc:8", "const:4:8"]]
- 005449dc ["CALLIND", null, ["register:0:8"]]
+ 00544a1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00544a1c ["INT_ADD", "register:40f0:8", ["const:544a1c:8", "const:4:8"]]
+ 00544a1c ["CALLIND", null, ["register:0:8"]]
- 005449dc bytes 00013fd6
+ 00544a1c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e66c89da31626c6f6ecb8755ff5cf64"></a>

### [`00544a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544a54.md) → [`00544a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/00544a94.md) FUN_00544a94

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00544a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544a54.md#insn-00544a7c) · [`00544a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544a54.md#insn-00544a84)
- 新版 `00544abc`（命令位置の公開資料なし） · `00544ac4`（命令位置の公開資料なし）

~~~diff
- 00544a7c ["INT_ADD", "register:40f0:8", ["const:544a7c:8", "const:4:8"]]
- 00544a7c ["CALL", null, ["callee:00c58150:8"]]
+ 00544abc ["INT_ADD", "register:40f0:8", ["const:544abc:8", "const:4:8"]]
+ 00544abc ["CALL", null, ["callee:00c58150:8"]]
- 00544a7c bytes b54c1c94
+ 00544abc bytes a54d1c94
- 00544a84 ["INT_ADD", "register:40f0:8", ["const:544a84:8", "const:4:8"]]
- 00544a84 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00544ac4 ["INT_ADD", "register:40f0:8", ["const:544ac4:8", "const:4:8"]]
+ 00544ac4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00544a84 bytes 0b4c1c94
+ 00544ac4 bytes fb4c1c94
~~~


<a id="compare-ddea27263aca1ac64540c9d6f20c842a"></a>

### [`00544aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544aa4.md) → [`00544ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/00544ae4.md) FUN_00544ae4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00544ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544aa4.md#insn-00544ac0)
- 新版 `00544b00`（命令位置の公開資料なし）

~~~diff
- 00544ac0 ["INT_ADD", "register:40f0:8", ["const:544ac0:8", "const:4:8"]]
- 00544ac0 ["CALL", null, ["callee:00c58180:8"]]
+ 00544b00 ["INT_ADD", "register:40f0:8", ["const:544b00:8", "const:4:8"]]
+ 00544b00 ["CALL", null, ["callee:00c58180:8"]]
- 00544ac0 bytes b04c1c94
+ 00544b00 bytes a04d1c94
~~~


<a id="compare-059d3713e75a16b502770e9abc596229"></a>

### [`00544ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544ae0.md) → [`00544b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/00544b20.md) FUN_00544b20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00544af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544ae0.md#insn-00544af0)
- 新版 `00544b30`（命令位置の公開資料なし）

~~~diff
- 00544af0 ["INT_ADD", "register:40f0:8", ["const:544af0:8", "const:4:8"]]
- 00544af0 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00544b30 ["INT_ADD", "register:40f0:8", ["const:544b30:8", "const:4:8"]]
+ 00544b30 ["CALL", null, ["callee:00c57ea0:8"]]
- 00544af0 bytes ec4b1c94
+ 00544b30 bytes dc4c1c94
~~~


<a id="compare-099159d52e410fe81c43caf561371149"></a>

### [`00544b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544b04.md) → [`00544b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/00544b44.md) FUN_00544b44

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004ca930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca930.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d80.md)
- 新版 呼出元 1件 [`004ca970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004ca970.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00544b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544b04.md#insn-00544b1c)
- 新版 `00544b5c`（命令位置の公開資料なし）

~~~diff
- 00544b1c ["INT_ADD", "register:40f0:8", ["const:544b1c:8", "const:4:8"]]
- 00544b1c ["CALL", null, ["callee:00c58180:8"]]
+ 00544b5c ["INT_ADD", "register:40f0:8", ["const:544b5c:8", "const:4:8"]]
+ 00544b5c ["CALL", null, ["callee:00c58180:8"]]
- 00544b1c bytes 994c1c94
+ 00544b5c bytes 894d1c94
~~~


<a id="compare-e25fc19c57aab197d6d11a22db4a20c8"></a>

### [`00544b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544b5c.md) → [`00544b9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/00544b9c.md) FUN_00544b9c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004ca930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca930.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00544970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544970.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`004ca970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004ca970.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005449b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/005449b0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00544bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544b5c.md#insn-00544bc8) · [`00544c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544b5c.md#insn-00544c38) · [`00544c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544b5c.md#insn-00544c4c)
- 新版 `00544c08`（命令位置の公開資料なし） · `00544c78`（命令位置の公開資料なし） · `00544c8c`（命令位置の公開資料なし）

~~~diff
- 00544bc8 ["INT_ADD", "register:40f0:8", ["const:544bc8:8", "const:4:8"]]
- 00544bc8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00544c08 ["INT_ADD", "register:40f0:8", ["const:544c08:8", "const:4:8"]]
+ 00544c08 ["CALL", null, ["callee:00c57e90:8"]]
- 00544bc8 bytes b24b1c94
+ 00544c08 bytes a24c1c94
- 00544c38 ["INT_ADD", "register:40f0:8", ["const:544c38:8", "const:4:8"]]
- 00544c38 ["CALL", null, ["callee:00c53d00:8"]]
+ 00544c78 ["INT_ADD", "register:40f0:8", ["const:544c78:8", "const:4:8"]]
+ 00544c78 ["CALL", null, ["callee:00c53d00:8"]]
- 00544c38 bytes 2a3b1c94
+ 00544c78 bytes 223c1c94
- 00544c4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00544c4c ["INT_ADD", "register:40f0:8", ["const:544c4c:8", "const:4:8"]]
- 00544c4c ["CALLIND", null, ["register:0:8"]]
+ 00544c8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00544c8c ["INT_ADD", "register:40f0:8", ["const:544c8c:8", "const:4:8"]]
+ 00544c8c ["CALLIND", null, ["register:0:8"]]
- 00544c4c bytes 00013fd6
+ 00544c8c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e9ef8cc538b6c6067cbd2ea185868fb"></a>

### [`00544e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544e1c.md) → [`00544e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/00544e5c.md) FUN_00544e5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004def08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004def08.md) [`004df69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df69c.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0053fec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fec4.md) [`0054507c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/0054507c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`004def48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004de/004def48.md) [`004df6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004df/004df6dc.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0053ff04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053ff04.md) [`005450bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/005450bc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00544eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544e1c.md#insn-00544eb0) · [`00544f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544e1c.md#insn-00544f40) · [`00544f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544e1c.md#insn-00544f58)
- 新版 `00544ef0`（命令位置の公開資料なし） · `00544f80`（命令位置の公開資料なし） · `00544f98`（命令位置の公開資料なし）

~~~diff
- 00544eb0 ["INT_ADD", "register:40f0:8", ["const:544eb0:8", "const:4:8"]]
- 00544eb0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00544ef0 ["INT_ADD", "register:40f0:8", ["const:544ef0:8", "const:4:8"]]
+ 00544ef0 ["CALL", null, ["callee:00c57e90:8"]]
- 00544eb0 bytes f84a1c94
+ 00544ef0 bytes e84b1c94
- 00544f40 ["INT_ADD", "register:40f0:8", ["const:544f40:8", "const:4:8"]]
- 00544f40 ["CALL", null, ["callee:005450bc:8"]]
+ 00544f80 ["INT_ADD", "register:40f0:8", ["const:544f80:8", "const:4:8"]]
+ 00544f80 ["CALL", null, ["callee:005450bc:8"]]
- 00544f40 bytes 4f000094
+ 00544f80 bytes 4f000094
- 00544f58 ["INT_ADD", "register:40f0:8", ["const:544f58:8", "const:4:8"]]
- 00544f58 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00544f98 ["INT_ADD", "register:40f0:8", ["const:544f98:8", "const:4:8"]]
+ 00544f98 ["CALL", null, ["callee:00c57eb0:8"]]
- 00544f58 bytes d64a1c94
+ 00544f98 bytes c64b1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

