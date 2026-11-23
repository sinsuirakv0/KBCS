# v16.0.0 → v16.0.1 · 要調査の変更候補 (14)

[一覧の目次](README.md)

<a id="compare-d54b2fa0690f3a40b8657708da9c9588"></a>

### [`005851d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/005851d4.md) → [`00585214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585214.md) FUN_00585214

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00585020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585020.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00585060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585060.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00585214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/005851d4.md#insn-00585214) · [`00585260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/005851d4.md#insn-00585260) · [`00585274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/005851d4.md#insn-00585274)
- 新版 `00585254`（命令位置の公開資料なし） · `005852a0`（命令位置の公開資料なし） · `005852b4`（命令位置の公開資料なし）

~~~diff
- 00585214 ["INT_ADD", "register:40f0:8", ["const:585214:8", "const:4:8"]]
- 00585214 ["CALL", null, ["callee:00c57e90:8"]]
+ 00585254 ["INT_ADD", "register:40f0:8", ["const:585254:8", "const:4:8"]]
+ 00585254 ["CALL", null, ["callee:00c57e90:8"]]
- 00585214 bytes 1f4a1b94
+ 00585254 bytes 0f4b1b94
- 00585260 ["INT_ADD", "register:40f0:8", ["const:585260:8", "const:4:8"]]
- 00585260 ["CALL", null, ["callee:00c53d00:8"]]
+ 005852a0 ["INT_ADD", "register:40f0:8", ["const:5852a0:8", "const:4:8"]]
+ 005852a0 ["CALL", null, ["callee:00c53d00:8"]]
- 00585260 bytes a0391b94
+ 005852a0 bytes 983a1b94
- 00585274 ["COPY", "register:0:8", ["register:4040:8"]]
- 00585274 ["INT_ADD", "register:40f0:8", ["const:585274:8", "const:4:8"]]
- 00585274 ["CALLIND", null, ["register:0:8"]]
+ 005852b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005852b4 ["INT_ADD", "register:40f0:8", ["const:5852b4:8", "const:4:8"]]
+ 005852b4 ["CALLIND", null, ["register:0:8"]]
- 00585274 bytes 00013fd6
+ 005852b4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca41221b4f951af35c4a064ccf8cea51"></a>

### [`005852e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/005852e4.md) → [`00585324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585324.md) FUN_00585324

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00561cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md) · 呼出先 3件 [`00587d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587d68.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00561d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md) · 呼出先 3件 [`00587da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587da8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058531c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/005852e4.md#insn-0058531c) · [`00585330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/005852e4.md#insn-00585330) · [`00585388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/005852e4.md#insn-00585388)
- 新版 `0058535c`（命令位置の公開資料なし） · `00585370`（命令位置の公開資料なし） · `005853c8`（命令位置の公開資料なし）

~~~diff
- 0058531c ["INT_ADD", "register:40f0:8", ["const:58531c:8", "const:4:8"]]
- 0058531c ["CALL", null, ["callee:00c57e90:8"]]
+ 0058535c ["INT_ADD", "register:40f0:8", ["const:58535c:8", "const:4:8"]]
+ 0058535c ["CALL", null, ["callee:00c57e90:8"]]
- 0058531c bytes dd491b94
+ 0058535c bytes cd4a1b94
- 00585330 ["INT_ADD", "register:40f0:8", ["const:585330:8", "const:4:8"]]
- 00585330 ["CALL", null, ["callee:00587da8:8"]]
+ 00585370 ["INT_ADD", "register:40f0:8", ["const:585370:8", "const:4:8"]]
+ 00585370 ["CALL", null, ["callee:00587da8:8"]]
- 00585330 bytes 8e0a0094
+ 00585370 bytes 8e0a0094
- 00585388 ["INT_ADD", "register:40f0:8", ["const:585388:8", "const:4:8"]]
- 00585388 ["CALL", null, ["callee:00c57ee0:8"]]
+ 005853c8 ["INT_ADD", "register:40f0:8", ["const:5853c8:8", "const:4:8"]]
+ 005853c8 ["CALL", null, ["callee:00c57ee0:8"]]
- 00585388 bytes d6491b94
+ 005853c8 bytes c64a1b94
~~~


<a id="compare-3e2c8ecd60949c12bd531ae7e7ef40a0"></a>

### [`00585d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585d10.md) → [`00585d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585d50.md) FUN_00585d50

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0058568c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058568c.md) [`00585ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585ed0.md) · 呼出先 3件 [`005881cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005881cc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 2件 [`005856cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005856cc.md) [`00585f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585f10.md) · 呼出先 3件 [`0058820c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/0058820c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00585d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585d10.md#insn-00585d8c) · [`00585de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585d10.md#insn-00585de8) · [`00585e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585d10.md#insn-00585e18)
- 新版 `00585dcc`（命令位置の公開資料なし） · `00585e28`（命令位置の公開資料なし） · `00585e58`（命令位置の公開資料なし）

~~~diff
- 00585d8c ["INT_ADD", "register:40f0:8", ["const:585d8c:8", "const:4:8"]]
- 00585d8c ["CALL", null, ["callee:00c58050:8"]]
+ 00585dcc ["INT_ADD", "register:40f0:8", ["const:585dcc:8", "const:4:8"]]
+ 00585dcc ["CALL", null, ["callee:00c58050:8"]]
- 00585d8c bytes b1471b94
+ 00585dcc bytes a1481b94
- 00585de8 ["INT_ADD", "register:40f0:8", ["const:585de8:8", "const:4:8"]]
- 00585de8 ["CALL", null, ["callee:00c58050:8"]]
+ 00585e28 ["INT_ADD", "register:40f0:8", ["const:585e28:8", "const:4:8"]]
+ 00585e28 ["CALL", null, ["callee:00c58050:8"]]
- 00585de8 bytes 9a471b94
+ 00585e28 bytes 8a481b94
- 00585e18 ["INT_ADD", "register:40f0:8", ["const:585e18:8", "const:4:8"]]
- 00585e18 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00585e58 ["INT_ADD", "register:40f0:8", ["const:585e58:8", "const:4:8"]]
+ 00585e58 ["CALL", null, ["callee:00c57eb0:8"]]
- 00585e18 bytes 26471b94
+ 00585e58 bytes 16481b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-664601e35a49d074c7ca6a3d24f3ced8"></a>

### [`00585e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585e80.md) → [`00585ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585ec0.md) FUN_00585ec0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00585e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585e80.md#insn-00585e9c) · [`00585ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585e80.md#insn-00585ebc)
- 新版 `00585edc`（命令位置の公開資料なし） · `00585efc`（命令位置の公開資料なし）

~~~diff
- 00585e9c ["INT_ADD", "register:40f0:8", ["const:585e9c:8", "const:4:8"]]
- 00585e9c ["CALL", null, ["callee:00c53d00:8"]]
+ 00585edc ["INT_ADD", "register:40f0:8", ["const:585edc:8", "const:4:8"]]
+ 00585edc ["CALL", null, ["callee:00c53d00:8"]]
- 00585e9c bytes 91361b94
+ 00585edc bytes 89371b94
- 00585ebc ["COPY", "register:0:8", ["register:4040:8"]]
- 00585ebc ["INT_ADD", "register:40f0:8", ["const:585ebc:8", "const:4:8"]]
- 00585ebc ["CALLIND", null, ["register:0:8"]]
+ 00585efc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00585efc ["INT_ADD", "register:40f0:8", ["const:585efc:8", "const:4:8"]]
+ 00585efc ["CALLIND", null, ["register:0:8"]]
- 00585ebc bytes 00013fd6
+ 00585efc bytes 00013fd6
~~~


<a id="compare-b47466953da38ffd17e4ff1832a2355e"></a>

### [`0058669c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/0058669c.md) → [`005866dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/005866dc.md) FUN_005866dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0058659c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/0058659c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005865dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/005865dc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005866ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/0058669c.md#insn-005866ac)
- 新版 `005866ec`（命令位置の公開資料なし）

~~~diff
- 005866ac ["INT_ADD", "register:40f0:8", ["const:5866ac:8", "const:4:8"]]
- 005866ac ["CALL", null, ["callee:005865dc:8"]]
+ 005866ec ["INT_ADD", "register:40f0:8", ["const:5866ec:8", "const:4:8"]]
+ 005866ec ["CALL", null, ["callee:005865dc:8"]]
- 005866ac bytes bcffff97
+ 005866ec bytes bcffff97
~~~


<a id="compare-1c1396d23f3a9d92403a452a600540de"></a>

### [`005867d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/005867d0.md) → [`00586810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586810.md) FUN_00586810

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058416c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/0058416c.md) · 呼出先 0件 
- 新版 呼出元 1件 [`005841ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005841ac.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00586808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/005867d0.md#insn-00586808) · [`00586830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/005867d0.md#insn-00586830) · [`00586850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/005867d0.md#insn-00586850)
- 新版 `00586848`（命令位置の公開資料なし） · `00586870`（命令位置の公開資料なし） · `00586890`（命令位置の公開資料なし）

~~~diff
- 00586808 ["COPY", "register:0:8", ["register:4048:8"]]
- 00586808 ["INT_ADD", "register:40f0:8", ["const:586808:8", "const:4:8"]]
- 00586808 ["CALLIND", null, ["register:0:8"]]
+ 00586848 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00586848 ["INT_ADD", "register:40f0:8", ["const:586848:8", "const:4:8"]]
+ 00586848 ["CALLIND", null, ["register:0:8"]]
- 00586808 bytes 20013fd6
+ 00586848 bytes 20013fd6
- 00586830 ["COPY", "register:0:8", ["register:4040:8"]]
- 00586830 ["INT_ADD", "register:40f0:8", ["const:586830:8", "const:4:8"]]
- 00586830 ["CALLIND", null, ["register:0:8"]]
+ 00586870 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00586870 ["INT_ADD", "register:40f0:8", ["const:586870:8", "const:4:8"]]
+ 00586870 ["CALLIND", null, ["register:0:8"]]
- 00586830 bytes 00013fd6
+ 00586870 bytes 00013fd6
- 00586850 ["COPY", "register:0:8", ["register:4040:8"]]
- 00586850 ["INT_ADD", "register:40f0:8", ["const:586850:8", "const:4:8"]]
- 00586850 ["CALLIND", null, ["register:0:8"]]
+ 00586890 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00586890 ["INT_ADD", "register:40f0:8", ["const:586890:8", "const:4:8"]]
+ 00586890 ["CALLIND", null, ["register:0:8"]]
- 00586850 bytes 00013fd6
+ 00586890 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7a975d0a9c7557ad8b5fb1207abcfa1"></a>

### [`00586934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586934.md) → [`00586974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586974.md) FUN_00586974

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058416c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/0058416c.md) · 呼出先 0件 
- 新版 呼出元 1件 [`005841ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005841ac.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00586968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586934.md#insn-00586968) · [`00586990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586934.md#insn-00586990) · [`005869b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586934.md#insn-005869b4)
- 新版 `005869a8`（命令位置の公開資料なし） · `005869d0`（命令位置の公開資料なし） · `005869f4`（命令位置の公開資料なし）

~~~diff
- 00586968 ["COPY", "register:0:8", ["register:4048:8"]]
- 00586968 ["INT_ADD", "register:40f0:8", ["const:586968:8", "const:4:8"]]
- 00586968 ["CALLIND", null, ["register:0:8"]]
+ 005869a8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005869a8 ["INT_ADD", "register:40f0:8", ["const:5869a8:8", "const:4:8"]]
+ 005869a8 ["CALLIND", null, ["register:0:8"]]
- 00586968 bytes 20013fd6
+ 005869a8 bytes 20013fd6
- 00586990 ["COPY", "register:0:8", ["register:4040:8"]]
- 00586990 ["INT_ADD", "register:40f0:8", ["const:586990:8", "const:4:8"]]
- 00586990 ["CALLIND", null, ["register:0:8"]]
+ 005869d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005869d0 ["INT_ADD", "register:40f0:8", ["const:5869d0:8", "const:4:8"]]
+ 005869d0 ["CALLIND", null, ["register:0:8"]]
- 00586990 bytes 00013fd6
+ 005869d0 bytes 00013fd6
- 005869b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005869b4 ["INT_ADD", "register:40f0:8", ["const:5869b4:8", "const:4:8"]]
- 005869b4 ["CALLIND", null, ["register:0:8"]]
+ 005869f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005869f4 ["INT_ADD", "register:40f0:8", ["const:5869f4:8", "const:4:8"]]
+ 005869f4 ["CALLIND", null, ["register:0:8"]]
- 005869b4 bytes 00013fd6
+ 005869f4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0441016caad23aeb68430d780f65fe5f"></a>

### [`00586a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586a9c.md) → [`00586adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586adc.md) FUN_00586adc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0058333c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058333c.md) [`00586a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586a9c.md) · 呼出先 2件 [`00586a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586a9c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0058337c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058337c.md) [`00586adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586adc.md) · 呼出先 2件 [`00586adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586adc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00586ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586a9c.md#insn-00586ab8) · [`00586ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586a9c.md#insn-00586ac4) · [`00586af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586a9c.md#insn-00586af8)
- 新版 `00586af8`（命令位置の公開資料なし） · `00586b04`（命令位置の公開資料なし） · `00586b38`（命令位置の公開資料なし）

~~~diff
- 00586ab8 ["INT_ADD", "register:40f0:8", ["const:586ab8:8", "const:4:8"]]
- 00586ab8 ["CALL", null, ["local:b0:8"]]
+ 00586af8 ["INT_ADD", "register:40f0:8", ["const:586af8:8", "const:4:8"]]
+ 00586af8 ["CALL", null, ["local:b0:8"]]
- 00586ab8 bytes f9ffff97
+ 00586af8 bytes f9ffff97
- 00586ac4 ["INT_ADD", "register:40f0:8", ["const:586ac4:8", "const:4:8"]]
- 00586ac4 ["CALL", null, ["local:b0:8"]]
+ 00586b04 ["INT_ADD", "register:40f0:8", ["const:586b04:8", "const:4:8"]]
+ 00586b04 ["CALL", null, ["local:b0:8"]]
- 00586ac4 bytes f6ffff97
+ 00586b04 bytes f6ffff97
- 00586af8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00586af8 ["INT_ADD", "register:40f0:8", ["const:586af8:8", "const:4:8"]]
- 00586af8 ["CALLIND", null, ["register:0:8"]]
+ 00586b38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00586b38 ["INT_ADD", "register:40f0:8", ["const:586b38:8", "const:4:8"]]
+ 00586b38 ["CALLIND", null, ["register:0:8"]]
- 00586af8 bytes 00013fd6
+ 00586b38 bytes 00013fd6
~~~


<a id="compare-05206c7ae7e23011896cd0da60be9b04"></a>

### [`00586b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586b0c.md) → [`00586b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586b4c.md) FUN_00586b4c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00583344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583344.md) [`00586b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586b0c.md) · 呼出先 2件 [`00586b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586b0c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00583384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583384.md) [`00586b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586b4c.md) · 呼出先 2件 [`00586b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586b4c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00586b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586b0c.md#insn-00586b28) · [`00586b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586b0c.md#insn-00586b34) · [`00586b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586b0c.md#insn-00586b68)
- 新版 `00586b68`（命令位置の公開資料なし） · `00586b74`（命令位置の公開資料なし） · `00586ba8`（命令位置の公開資料なし）

~~~diff
- 00586b28 ["INT_ADD", "register:40f0:8", ["const:586b28:8", "const:4:8"]]
- 00586b28 ["CALL", null, ["local:b0:8"]]
+ 00586b68 ["INT_ADD", "register:40f0:8", ["const:586b68:8", "const:4:8"]]
+ 00586b68 ["CALL", null, ["local:b0:8"]]
- 00586b28 bytes f9ffff97
+ 00586b68 bytes f9ffff97
- 00586b34 ["INT_ADD", "register:40f0:8", ["const:586b34:8", "const:4:8"]]
- 00586b34 ["CALL", null, ["local:b0:8"]]
+ 00586b74 ["INT_ADD", "register:40f0:8", ["const:586b74:8", "const:4:8"]]
+ 00586b74 ["CALL", null, ["local:b0:8"]]
- 00586b34 bytes f6ffff97
+ 00586b74 bytes f6ffff97
- 00586b68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00586b68 ["INT_ADD", "register:40f0:8", ["const:586b68:8", "const:4:8"]]
- 00586b68 ["CALLIND", null, ["register:0:8"]]
+ 00586ba8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00586ba8 ["INT_ADD", "register:40f0:8", ["const:586ba8:8", "const:4:8"]]
+ 00586ba8 ["CALLIND", null, ["register:0:8"]]
- 00586b68 bytes 00013fd6
+ 00586ba8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49cdef7a29822c7d2c33522865a9e966"></a>

### [`00586bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586bdc.md) → [`00586c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586c1c.md) FUN_00586c1c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00588314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588314.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00586cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586cf8.md) [`00586f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586f70.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00588354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588354.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00586d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586d38.md) [`00586fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586fb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00586c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586bdc.md#insn-00586c38) · [`00586c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586bdc.md#insn-00586c60) · [`00586c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586bdc.md#insn-00586c8c)
- 新版 `00586c78`（命令位置の公開資料なし） · `00586ca0`（命令位置の公開資料なし） · `00586ccc`（命令位置の公開資料なし）

~~~diff
- 00586c38 ["INT_ADD", "register:40f0:8", ["const:586c38:8", "const:4:8"]]
- 00586c38 ["CALL", null, ["callee:00586d38:8"]]
+ 00586c78 ["INT_ADD", "register:40f0:8", ["const:586c78:8", "const:4:8"]]
+ 00586c78 ["CALL", null, ["callee:00586d38:8"]]
- 00586c38 bytes 30000094
+ 00586c78 bytes 30000094
- 00586c60 ["INT_ADD", "register:40f0:8", ["const:586c60:8", "const:4:8"]]
- 00586c60 ["CALL", null, ["callee:00586fb0:8"]]
+ 00586ca0 ["INT_ADD", "register:40f0:8", ["const:586ca0:8", "const:4:8"]]
+ 00586ca0 ["CALL", null, ["callee:00586fb0:8"]]
- 00586c60 bytes c4000094
+ 00586ca0 bytes c4000094
- 00586c8c ["INT_ADD", "register:40f0:8", ["const:586c8c:8", "const:4:8"]]
- 00586c8c ["CALL", null, ["callee:0043bba4:8"]]
+ 00586ccc ["INT_ADD", "register:40f0:8", ["const:586ccc:8", "const:4:8"]]
+ 00586ccc ["CALL", null, ["callee:0043bba4:8"]]
- 00586c8c bytes b6d3fa97
+ 00586ccc bytes b6d3fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e82fd9784ba06ae44d4b2e6724f648e"></a>

### [`00586cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586cf8.md) → [`00586d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586d38.md) FUN_00586d38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00586bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586bdc.md) · 呼出先 1件 [`00c59ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ee0.md)
- 新版 呼出元 1件 [`00586c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586c1c.md) · 呼出先 1件 [`00c5a2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a2e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00586d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586cf8.md#insn-00586d5c) · [`00586d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586cf8.md#insn-00586d94) · [`00586e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586cf8.md#insn-00586e04)
- 新版 `00586d9c`（命令位置の公開資料なし） · `00586dd4`（命令位置の公開資料なし） · `00586e44`（命令位置の公開資料なし）

~~~diff
- 00586d5c ["INT_ADD", "register:40f0:8", ["const:586d5c:8", "const:4:8"]]
- 00586d5c ["CALL", null, ["callee:00c5a2e0:8"]]
+ 00586d9c ["INT_ADD", "register:40f0:8", ["const:586d9c:8", "const:4:8"]]
+ 00586d9c ["CALL", null, ["callee:00c5a2e0:8"]]
- 00586d5c bytes 614c1b94
+ 00586d9c bytes 514d1b94
- 00586d94 ["INT_ADD", "register:40f0:8", ["const:586d94:8", "const:4:8"]]
- 00586d94 ["CALL", null, ["callee:00c5a2e0:8"]]
+ 00586dd4 ["INT_ADD", "register:40f0:8", ["const:586dd4:8", "const:4:8"]]
+ 00586dd4 ["CALL", null, ["callee:00c5a2e0:8"]]
- 00586d94 bytes 534c1b94
+ 00586dd4 bytes 434d1b94
- 00586e04 ["INT_ADD", "register:40f0:8", ["const:586e04:8", "const:4:8"]]
- 00586e04 ["CALL", null, ["callee:00c5a2e0:8"]]
+ 00586e44 ["INT_ADD", "register:40f0:8", ["const:586e44:8", "const:4:8"]]
+ 00586e44 ["CALL", null, ["callee:00c5a2e0:8"]]
- 00586e04 bytes 374c1b94
+ 00586e44 bytes 274d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b816d21a62ceca5e7019bccd6c02595a"></a>

### [`00586f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586f70.md) → [`00586fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586fb0.md) FUN_00586fb0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00586bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586bdc.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00586c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586c1c.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00586f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586f70.md#insn-00586f90) · [`00586fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586f70.md#insn-00586fc4) · [`00586ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586f70.md#insn-00586ff0)
- 新版 `00586fd0`（命令位置の公開資料なし） · `00587004`（命令位置の公開資料なし） · `00587030`（命令位置の公開資料なし）

~~~diff
- 00586f90 ["INT_ADD", "register:40f0:8", ["const:586f90:8", "const:4:8"]]
- 00586f90 ["CALL", null, ["callee:00c57e90:8"]]
+ 00586fd0 ["INT_ADD", "register:40f0:8", ["const:586fd0:8", "const:4:8"]]
+ 00586fd0 ["CALL", null, ["callee:00c57e90:8"]]
- 00586f90 bytes c0421b94
+ 00586fd0 bytes b0431b94
- 00586fc4 ["INT_ADD", "register:40f0:8", ["const:586fc4:8", "const:4:8"]]
- 00586fc4 ["CALL", null, ["callee:0043bb20:8"]]
+ 00587004 ["INT_ADD", "register:40f0:8", ["const:587004:8", "const:4:8"]]
+ 00587004 ["CALL", null, ["callee:0043bb20:8"]]
- 00586fc4 bytes c7d2fa97
+ 00587004 bytes c7d2fa97
- 00586ff0 ["INT_ADD", "register:40f0:8", ["const:586ff0:8", "const:4:8"]]
- 00586ff0 ["CALL", null, ["callee:0043bb20:8"]]
+ 00587030 ["INT_ADD", "register:40f0:8", ["const:587030:8", "const:4:8"]]
+ 00587030 ["CALL", null, ["callee:0043bb20:8"]]
- 00586ff0 bytes bcd2fa97
+ 00587030 bytes bcd2fa97
~~~


<a id="compare-1fb9aeaae5835591029d9ed3f4c9c482"></a>

### [`00587038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587038.md) → [`00587078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587078.md) FUN_00587078

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00587038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587038.md) [`00587ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587ed4.md) · 呼出先 2件 [`00587038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587038.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00587078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587078.md) [`00587f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587f14.md) · 呼出先 2件 [`00587078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587078.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00587054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587038.md#insn-00587054) · [`00587060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587038.md#insn-00587060) · [`00587070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587038.md#insn-00587070)
- 新版 `00587094`（命令位置の公開資料なし） · `005870a0`（命令位置の公開資料なし） · `005870b0`（命令位置の公開資料なし）

~~~diff
- 00587054 ["INT_ADD", "register:40f0:8", ["const:587054:8", "const:4:8"]]
- 00587054 ["CALL", null, ["local:b0:8"]]
+ 00587094 ["INT_ADD", "register:40f0:8", ["const:587094:8", "const:4:8"]]
+ 00587094 ["CALL", null, ["local:b0:8"]]
- 00587054 bytes f9ffff97
+ 00587094 bytes f9ffff97
- 00587060 ["INT_ADD", "register:40f0:8", ["const:587060:8", "const:4:8"]]
- 00587060 ["CALL", null, ["local:b0:8"]]
+ 005870a0 ["INT_ADD", "register:40f0:8", ["const:5870a0:8", "const:4:8"]]
+ 005870a0 ["CALL", null, ["local:b0:8"]]
- 00587060 bytes f6ffff97
+ 005870a0 bytes f6ffff97
- 00587070 ["INT_ADD", "register:40f0:8", ["const:587070:8", "const:4:8"]]
- 00587070 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005870b0 ["INT_ADD", "register:40f0:8", ["const:5870b0:8", "const:4:8"]]
+ 005870b0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00587070 bytes 90421b94
+ 005870b0 bytes 80431b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea26cfeb34d152773d7ea0af90bc1171"></a>

### [`005870e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005870e8.md) → [`00587128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587128.md) FUN_00587128

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058386c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058386c.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`005838ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005838ac.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00587154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005870e8.md#insn-00587154) · [`005871b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005870e8.md#insn-005871b0) · [`005871dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005870e8.md#insn-005871dc)
- 新版 `00587194`（命令位置の公開資料なし） · `005871f0`（命令位置の公開資料なし） · `0058721c`（命令位置の公開資料なし）

~~~diff
- 00587154 ["INT_ADD", "register:40f0:8", ["const:587154:8", "const:4:8"]]
- 00587154 ["CALL", null, ["callee:00c57e90:8"]]
+ 00587194 ["INT_ADD", "register:40f0:8", ["const:587194:8", "const:4:8"]]
+ 00587194 ["CALL", null, ["callee:00c57e90:8"]]
- 00587154 bytes 4f421b94
+ 00587194 bytes 3f431b94
- 005871b0 ["COPY", "register:0:8", ["register:4048:8"]]
- 005871b0 ["INT_ADD", "register:40f0:8", ["const:5871b0:8", "const:4:8"]]
- 005871b0 ["CALLIND", null, ["register:0:8"]]
+ 005871f0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005871f0 ["INT_ADD", "register:40f0:8", ["const:5871f0:8", "const:4:8"]]
+ 005871f0 ["CALLIND", null, ["register:0:8"]]
- 005871b0 bytes 20013fd6
+ 005871f0 bytes 20013fd6
- 005871dc ["INT_ADD", "register:40f0:8", ["const:5871dc:8", "const:4:8"]]
- 005871dc ["CALL", null, ["callee:0043bba4:8"]]
+ 0058721c ["INT_ADD", "register:40f0:8", ["const:58721c:8", "const:4:8"]]
+ 0058721c ["CALL", null, ["callee:0043bba4:8"]]
- 005871dc bytes 62d2fa97
+ 0058721c bytes 62d2fa97
~~~


<a id="compare-df3bd3f633c5b5382308e82dfbe10e65"></a>

### [`0058720c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058720c.md) → [`0058724c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058724c.md) FUN_0058724c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0058416c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/0058416c.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`005872f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005872f4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`005841ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005841ac.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00587334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587334.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058727c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058720c.md#insn-0058727c) · [`00587294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058720c.md#insn-00587294) · [`005872c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058720c.md#insn-005872c0)
- 新版 `005872bc`（命令位置の公開資料なし） · `005872d4`（命令位置の公開資料なし） · `00587300`（命令位置の公開資料なし）

~~~diff
- 0058727c ["INT_ADD", "register:40f0:8", ["const:58727c:8", "const:4:8"]]
- 0058727c ["CALL", null, ["callee:00c57e90:8"]]
+ 005872bc ["INT_ADD", "register:40f0:8", ["const:5872bc:8", "const:4:8"]]
+ 005872bc ["CALL", null, ["callee:00c57e90:8"]]
- 0058727c bytes 05421b94
+ 005872bc bytes f5421b94
- 00587294 ["INT_ADD", "register:40f0:8", ["const:587294:8", "const:4:8"]]
- 00587294 ["CALL", null, ["callee:00587334:8"]]
+ 005872d4 ["INT_ADD", "register:40f0:8", ["const:5872d4:8", "const:4:8"]]
+ 005872d4 ["CALL", null, ["callee:00587334:8"]]
- 00587294 bytes 18000094
+ 005872d4 bytes 18000094
- 005872c0 ["INT_ADD", "register:40f0:8", ["const:5872c0:8", "const:4:8"]]
- 005872c0 ["CALL", null, ["callee:0043bba4:8"]]
+ 00587300 ["INT_ADD", "register:40f0:8", ["const:587300:8", "const:4:8"]]
+ 00587300 ["CALL", null, ["callee:0043bba4:8"]]
- 005872c0 bytes 29d2fa97
+ 00587300 bytes 29d2fa97
~~~


<a id="compare-d0e611fc78f8c83e9621bd6e0380da08"></a>

### [`005872f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005872f4.md) → [`00587334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587334.md) FUN_00587334

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058720c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058720c.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0058724c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058724c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00587344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005872f4.md#insn-00587344) · [`00587388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005872f4.md#insn-00587388) · [`005873cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005872f4.md#insn-005873cc)
- 新版 `00587384`（命令位置の公開資料なし） · `005873c8`（命令位置の公開資料なし） · `0058740c`（命令位置の公開資料なし）

~~~diff
- 00587344 ["COPY", "register:0:8", ["register:4040:8"]]
- 00587344 ["INT_ADD", "register:40f0:8", ["const:587344:8", "const:4:8"]]
- 00587344 ["CALLIND", null, ["register:0:8"]]
+ 00587384 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00587384 ["INT_ADD", "register:40f0:8", ["const:587384:8", "const:4:8"]]
+ 00587384 ["CALLIND", null, ["register:0:8"]]
- 00587344 bytes 00013fd6
+ 00587384 bytes 00013fd6
- 00587388 ["COPY", "register:0:8", ["register:4040:8"]]
- 00587388 ["INT_ADD", "register:40f0:8", ["const:587388:8", "const:4:8"]]
- 00587388 ["CALLIND", null, ["register:0:8"]]
+ 005873c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005873c8 ["INT_ADD", "register:40f0:8", ["const:5873c8:8", "const:4:8"]]
+ 005873c8 ["CALLIND", null, ["register:0:8"]]
- 00587388 bytes 00013fd6
+ 005873c8 bytes 00013fd6
- 005873cc ["COPY", "register:0:8", ["register:4040:8"]]
- 005873cc ["INT_ADD", "register:40f0:8", ["const:5873cc:8", "const:4:8"]]
- 005873cc ["CALLIND", null, ["register:0:8"]]
+ 0058740c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058740c ["INT_ADD", "register:40f0:8", ["const:58740c:8", "const:4:8"]]
+ 0058740c ["CALLIND", null, ["register:0:8"]]
- 005873cc bytes 00013fd6
+ 0058740c bytes 00013fd6
~~~


<a id="compare-44e2ebb2a56324bf70f3ef46dc724e40"></a>

### [`00587488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587488.md) → [`005874c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005874c8.md) FUN_005874c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005848f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/005848f8.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00584938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584938.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005874b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587488.md#insn-005874b0) · [`005874c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587488.md#insn-005874c4) · [`005874cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587488.md#insn-005874cc)
- 新版 `005874f0`（命令位置の公開資料なし） · `00587504`（命令位置の公開資料なし） · `0058750c`（命令位置の公開資料なし）

~~~diff
- 005874b0 ["INT_ADD", "register:40f0:8", ["const:5874b0:8", "const:4:8"]]
- 005874b0 ["CALL", null, ["callee:00c53d00:8"]]
+ 005874f0 ["INT_ADD", "register:40f0:8", ["const:5874f0:8", "const:4:8"]]
+ 005874f0 ["CALL", null, ["callee:00c53d00:8"]]
- 005874b0 bytes 0c311b94
+ 005874f0 bytes 04321b94
- 005874c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005874c4 ["INT_ADD", "register:40f0:8", ["const:5874c4:8", "const:4:8"]]
- 005874c4 ["CALLIND", null, ["register:0:8"]]
+ 00587504 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00587504 ["INT_ADD", "register:40f0:8", ["const:587504:8", "const:4:8"]]
+ 00587504 ["CALLIND", null, ["register:0:8"]]
- 005874c4 bytes 00013fd6
+ 00587504 bytes 00013fd6
- 005874cc ["INT_ADD", "register:40f0:8", ["const:5874cc:8", "const:4:8"]]
- 005874cc ["CALL", null, ["callee:00c57e80:8"]]
+ 0058750c ["INT_ADD", "register:40f0:8", ["const:58750c:8", "const:4:8"]]
+ 0058750c ["CALL", null, ["callee:00c57e80:8"]]
- 005874cc bytes 6d411b94
+ 0058750c bytes 5d421b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e82e865afb016b8ddc17e024788e4e2f"></a>

### [`00587518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587518.md) → [`00587558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587558.md) FUN_00587558

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00587538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587518.md#insn-00587538) · [`00587550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587518.md#insn-00587550) · [`00587570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587518.md#insn-00587570)
- 新版 `00587578`（命令位置の公開資料なし） · `00587590`（命令位置の公開資料なし） · `005875b0`（命令位置の公開資料なし）

~~~diff
- 00587538 ["INT_ADD", "register:40f0:8", ["const:587538:8", "const:4:8"]]
- 00587538 ["CALL", null, ["callee:00c53d00:8"]]
+ 00587578 ["INT_ADD", "register:40f0:8", ["const:587578:8", "const:4:8"]]
+ 00587578 ["CALL", null, ["callee:00c53d00:8"]]
- 00587538 bytes ea301b94
+ 00587578 bytes e2311b94
- 00587550 ["INT_ADD", "register:40f0:8", ["const:587550:8", "const:4:8"]]
- 00587550 ["CALL", null, ["callee:00c53d00:8"]]
+ 00587590 ["INT_ADD", "register:40f0:8", ["const:587590:8", "const:4:8"]]
+ 00587590 ["CALL", null, ["callee:00c53d00:8"]]
- 00587550 bytes e4301b94
+ 00587590 bytes dc311b94
- 00587570 ["COPY", "register:0:8", ["register:4040:8"]]
- 00587570 ["INT_ADD", "register:40f0:8", ["const:587570:8", "const:4:8"]]
- 00587570 ["CALLIND", null, ["register:0:8"]]
+ 005875b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005875b0 ["INT_ADD", "register:40f0:8", ["const:5875b0:8", "const:4:8"]]
+ 005875b0 ["CALLIND", null, ["register:0:8"]]
- 00587570 bytes 00013fd6
+ 005875b0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1e26c1213c90abfd3b27dd1dc0e150b"></a>

### [`0058780c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058780c.md) → [`0058784c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058784c.md) FUN_0058784c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005848f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/005848f8.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00584938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584938.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00587828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058780c.md#insn-00587828) · [`00587848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058780c.md#insn-00587848)
- 新版 `00587868`（命令位置の公開資料なし） · `00587888`（命令位置の公開資料なし）

~~~diff
- 00587828 ["INT_ADD", "register:40f0:8", ["const:587828:8", "const:4:8"]]
- 00587828 ["CALL", null, ["callee:00c53d00:8"]]
+ 00587868 ["INT_ADD", "register:40f0:8", ["const:587868:8", "const:4:8"]]
+ 00587868 ["CALL", null, ["callee:00c53d00:8"]]
- 00587828 bytes 2e301b94
+ 00587868 bytes 26311b94
- 00587848 ["COPY", "register:0:8", ["register:4040:8"]]
- 00587848 ["INT_ADD", "register:40f0:8", ["const:587848:8", "const:4:8"]]
- 00587848 ["CALLIND", null, ["register:0:8"]]
+ 00587888 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00587888 ["INT_ADD", "register:40f0:8", ["const:587888:8", "const:4:8"]]
+ 00587888 ["CALLIND", null, ["register:0:8"]]
- 00587848 bytes 00013fd6
+ 00587888 bytes 00013fd6
~~~


<a id="compare-1c63540fb026f975167735bb7253771f"></a>

### [`0058785c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058785c.md) → [`0058789c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058789c.md) FUN_0058789c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005848f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/005848f8.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00584938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584938.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058787c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058785c.md#insn-0058787c) · [`00587890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058785c.md#insn-00587890) · [`00587898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058785c.md#insn-00587898)
- 新版 `005878bc`（命令位置の公開資料なし） · `005878d0`（命令位置の公開資料なし） · `005878d8`（命令位置の公開資料なし）

~~~diff
- 0058787c ["INT_ADD", "register:40f0:8", ["const:58787c:8", "const:4:8"]]
- 0058787c ["CALL", null, ["callee:00c53d00:8"]]
+ 005878bc ["INT_ADD", "register:40f0:8", ["const:5878bc:8", "const:4:8"]]
+ 005878bc ["CALL", null, ["callee:00c53d00:8"]]
- 0058787c bytes 19301b94
+ 005878bc bytes 11311b94
- 00587890 ["COPY", "register:0:8", ["register:4040:8"]]
- 00587890 ["INT_ADD", "register:40f0:8", ["const:587890:8", "const:4:8"]]
- 00587890 ["CALLIND", null, ["register:0:8"]]
+ 005878d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005878d0 ["INT_ADD", "register:40f0:8", ["const:5878d0:8", "const:4:8"]]
+ 005878d0 ["CALLIND", null, ["register:0:8"]]
- 00587890 bytes 00013fd6
+ 005878d0 bytes 00013fd6
- 00587898 ["INT_ADD", "register:40f0:8", ["const:587898:8", "const:4:8"]]
- 00587898 ["CALL", null, ["callee:00c57e80:8"]]
+ 005878d8 ["INT_ADD", "register:40f0:8", ["const:5878d8:8", "const:4:8"]]
+ 005878d8 ["CALL", null, ["callee:00c57e80:8"]]
- 00587898 bytes 7a401b94
+ 005878d8 bytes 6a411b94
~~~


<a id="compare-e08b41bb6b74e7913c26bd4c6d3cb9e1"></a>

### [`005878ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005878ac.md) → [`005878ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005878ec.md) FUN_005878ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00587a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587a08.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00587a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587a48.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005878ac.md#insn-005878ec) · [`00587904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005878ac.md#insn-00587904) · [`00587918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005878ac.md#insn-00587918)
- 新版 `0058792c`（命令位置の公開資料なし） · `00587944`（命令位置の公開資料なし） · `00587958`（命令位置の公開資料なし）

~~~diff
- 005878ec ["INT_ADD", "register:40f0:8", ["const:5878ec:8", "const:4:8"]]
- 005878ec ["CALL", null, ["callee:00c53cd0:8"]]
+ 0058792c ["INT_ADD", "register:40f0:8", ["const:58792c:8", "const:4:8"]]
+ 0058792c ["CALL", null, ["callee:00c53cd0:8"]]
- 005878ec bytes f12f1b94
+ 0058792c bytes e9301b94
- 00587904 ["INT_ADD", "register:40f0:8", ["const:587904:8", "const:4:8"]]
- 00587904 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00587944 ["INT_ADD", "register:40f0:8", ["const:587944:8", "const:4:8"]]
+ 00587944 ["CALL", null, ["callee:00c53cd0:8"]]
- 00587904 bytes eb2f1b94
+ 00587944 bytes e3301b94
- 00587918 ["INT_ADD", "register:40f0:8", ["const:587918:8", "const:4:8"]]
- 00587918 ["CALL", null, ["callee:00587a48:8"]]
+ 00587958 ["INT_ADD", "register:40f0:8", ["const:587958:8", "const:4:8"]]
+ 00587958 ["CALL", null, ["callee:00587a48:8"]]
- 00587918 bytes 3c000094
+ 00587958 bytes 3c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ad26066640d60f360feba248a6363ee"></a>

### [`00587a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587a08.md) → [`00587a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587a48.md) FUN_00587a48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005878ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005878ac.md) · 呼出先 6件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`005878ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005878ec.md) · 呼出先 6件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00587a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587a08.md#insn-00587a34) · [`00587a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587a08.md#insn-00587a4c) · [`00587a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587a08.md#insn-00587a88)
- 新版 `00587a74`（命令位置の公開資料なし） · `00587a8c`（命令位置の公開資料なし） · `00587ac8`（命令位置の公開資料なし）

~~~diff
- 00587a34 ["INT_ADD", "register:40f0:8", ["const:587a34:8", "const:4:8"]]
- 00587a34 ["CALL", null, ["callee:00c580e0:8"]]
+ 00587a74 ["INT_ADD", "register:40f0:8", ["const:587a74:8", "const:4:8"]]
+ 00587a74 ["CALL", null, ["callee:00c580e0:8"]]
- 00587a34 bytes ab401b94
+ 00587a74 bytes 9b411b94
- 00587a4c ["INT_ADD", "register:40f0:8", ["const:587a4c:8", "const:4:8"]]
- 00587a4c ["CALL", null, ["callee:00c582f0:8"]]
+ 00587a8c ["INT_ADD", "register:40f0:8", ["const:587a8c:8", "const:4:8"]]
+ 00587a8c ["CALL", null, ["callee:00c582f0:8"]]
- 00587a4c bytes 29411b94
+ 00587a8c bytes 19421b94
- 00587a88 ["INT_ADD", "register:40f0:8", ["const:587a88:8", "const:4:8"]]
- 00587a88 ["CALL", null, ["callee:00c58380:8"]]
+ 00587ac8 ["INT_ADD", "register:40f0:8", ["const:587ac8:8", "const:4:8"]]
+ 00587ac8 ["CALL", null, ["callee:00c58380:8"]]
- 00587a88 bytes 3e411b94
+ 00587ac8 bytes 2e421b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-210db13067c1d7aa0ebec7a6f0d5d7c9"></a>

### [`00587af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587af8.md) → [`00587b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587b38.md) FUN_00587b38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005848f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/005848f8.md) · 呼出先 8件 [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00584938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584938.md) · 呼出先 8件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00587b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587af8.md#insn-00587b34) · [`00587b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587af8.md#insn-00587b40) · [`00587b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587af8.md#insn-00587b54)
- 新版 `00587b74`（命令位置の公開資料なし） · `00587b80`（命令位置の公開資料なし） · `00587b94`（命令位置の公開資料なし）

~~~diff
- 00587b34 ["INT_ADD", "register:40f0:8", ["const:587b34:8", "const:4:8"]]
- 00587b34 ["CALL", null, ["callee:00c580e0:8"]]
+ 00587b74 ["INT_ADD", "register:40f0:8", ["const:587b74:8", "const:4:8"]]
+ 00587b74 ["CALL", null, ["callee:00c580e0:8"]]
- 00587b34 bytes 6b401b94
+ 00587b74 bytes 5b411b94
- 00587b40 ["INT_ADD", "register:40f0:8", ["const:587b40:8", "const:4:8"]]
- 00587b40 ["CALL", null, ["callee:00c584a0:8"]]
+ 00587b80 ["INT_ADD", "register:40f0:8", ["const:587b80:8", "const:4:8"]]
+ 00587b80 ["CALL", null, ["callee:00c584a0:8"]]
- 00587b40 bytes 58411b94
+ 00587b80 bytes 48421b94
- 00587b54 ["INT_ADD", "register:40f0:8", ["const:587b54:8", "const:4:8"]]
- 00587b54 ["CALL", null, ["callee:00c582f0:8"]]
+ 00587b94 ["INT_ADD", "register:40f0:8", ["const:587b94:8", "const:4:8"]]
+ 00587b94 ["CALL", null, ["callee:00c582f0:8"]]
- 00587b54 bytes e7401b94
+ 00587b94 bytes d7411b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43bc3762e4661e22486aa05fa96730b1"></a>

### [`00587c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587c14.md) → [`00587c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587c54.md) FUN_00587c54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00585020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585020.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00587d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587d54.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00585060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585060.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00587d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587d94.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00587c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587c14.md#insn-00587c80) · [`00587cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587c14.md#insn-00587cf0) · [`00587d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587c14.md#insn-00587d04)
- 新版 `00587cc0`（命令位置の公開資料なし） · `00587d30`（命令位置の公開資料なし） · `00587d44`（命令位置の公開資料なし）

~~~diff
- 00587c80 ["INT_ADD", "register:40f0:8", ["const:587c80:8", "const:4:8"]]
- 00587c80 ["CALL", null, ["callee:00c57e90:8"]]
+ 00587cc0 ["INT_ADD", "register:40f0:8", ["const:587cc0:8", "const:4:8"]]
+ 00587cc0 ["CALL", null, ["callee:00c57e90:8"]]
- 00587c80 bytes 843f1b94
+ 00587cc0 bytes 74401b94
- 00587cf0 ["INT_ADD", "register:40f0:8", ["const:587cf0:8", "const:4:8"]]
- 00587cf0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00587d30 ["INT_ADD", "register:40f0:8", ["const:587d30:8", "const:4:8"]]
+ 00587d30 ["CALL", null, ["callee:00c53d00:8"]]
- 00587cf0 bytes fc2e1b94
+ 00587d30 bytes f42f1b94
- 00587d04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00587d04 ["INT_ADD", "register:40f0:8", ["const:587d04:8", "const:4:8"]]
- 00587d04 ["CALLIND", null, ["register:0:8"]]
+ 00587d44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00587d44 ["INT_ADD", "register:40f0:8", ["const:587d44:8", "const:4:8"]]
+ 00587d44 ["CALLIND", null, ["register:0:8"]]
- 00587d04 bytes 00013fd6
+ 00587d44 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47447ddda4dbcc39f927027b369151aa"></a>

### [`005880b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005880b4.md) → [`005880f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005880f4.md) FUN_005880f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058538c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058538c.md) · 呼出先 2件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005853cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005853cc.md) · 呼出先 2件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058811c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005880b4.md#insn-0058811c) · [`0058814c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005880b4.md#insn-0058814c) · [`00588180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005880b4.md#insn-00588180)
- 新版 `0058815c`（命令位置の公開資料なし） · `0058818c`（命令位置の公開資料なし） · `005881c0`（命令位置の公開資料なし）

~~~diff
- 0058811c ["INT_ADD", "register:40f0:8", ["const:58811c:8", "const:4:8"]]
- 0058811c ["CALL", null, ["callee:00494610:8"]]
+ 0058815c ["INT_ADD", "register:40f0:8", ["const:58815c:8", "const:4:8"]]
+ 0058815c ["CALL", null, ["callee:00494610:8"]]
- 0058811c bytes 2d31fc97
+ 0058815c bytes 2d31fc97
- 0058814c ["COPY", "register:0:8", ["register:4040:8"]]
- 0058814c ["INT_ADD", "register:40f0:8", ["const:58814c:8", "const:4:8"]]
- 0058814c ["CALLIND", null, ["register:0:8"]]
+ 0058818c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058818c ["INT_ADD", "register:40f0:8", ["const:58818c:8", "const:4:8"]]
+ 0058818c ["CALLIND", null, ["register:0:8"]]
- 0058814c bytes 00013fd6
+ 0058818c bytes 00013fd6
- 00588180 ["COPY", "register:0:8", ["register:4040:8"]]
- 00588180 ["INT_ADD", "register:40f0:8", ["const:588180:8", "const:4:8"]]
- 00588180 ["CALLIND", null, ["register:0:8"]]
+ 005881c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005881c0 ["INT_ADD", "register:40f0:8", ["const:5881c0:8", "const:4:8"]]
+ 005881c0 ["CALLIND", null, ["register:0:8"]]
- 00588180 bytes 00013fd6
+ 005881c0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff970b27ac916a2ec4be3ecabb706106"></a>

### [`005881cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005881cc.md) → [`0058820c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/0058820c.md) FUN_0058820c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00585d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585d10.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0054f154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f154.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00585d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585d50.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0054f194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054f/0054f194.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058820c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005881cc.md#insn-0058820c) · [`0058822c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005881cc.md#insn-0058822c) · [`00588260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005881cc.md#insn-00588260)
- 新版 `0058824c`（命令位置の公開資料なし） · `0058826c`（命令位置の公開資料なし） · `005882a0`（命令位置の公開資料なし）

~~~diff
- 0058820c ["INT_ADD", "register:40f0:8", ["const:58820c:8", "const:4:8"]]
- 0058820c ["CALL", null, ["callee:0054f194:8"]]
+ 0058824c ["INT_ADD", "register:40f0:8", ["const:58824c:8", "const:4:8"]]
+ 0058824c ["CALL", null, ["callee:0054f194:8"]]
- 0058820c bytes d21bff97
+ 0058824c bytes d21bff97
- 0058822c ["INT_ADD", "register:40f0:8", ["const:58822c:8", "const:4:8"]]
- 0058822c ["CALL", null, ["callee:00c57e90:8"]]
+ 0058826c ["INT_ADD", "register:40f0:8", ["const:58826c:8", "const:4:8"]]
+ 0058826c ["CALL", null, ["callee:00c57e90:8"]]
- 0058822c bytes 193e1b94
+ 0058826c bytes 093f1b94
- 00588260 ["INT_ADD", "register:40f0:8", ["const:588260:8", "const:4:8"]]
- 00588260 ["CALL", null, ["callee:0043bb20:8"]]
+ 005882a0 ["INT_ADD", "register:40f0:8", ["const:5882a0:8", "const:4:8"]]
+ 005882a0 ["CALL", null, ["callee:0043bb20:8"]]
- 00588260 bytes 20cefa97
+ 005882a0 bytes 20cefa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87233572c8dd491974197b8266d8e736"></a>

### [`00588568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588568.md) → [`005885a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005885a8.md) FUN_005885a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00588584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588568.md#insn-00588584) · [`005885a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588568.md#insn-005885a4)
- 新版 `005885c4`（命令位置の公開資料なし） · `005885e4`（命令位置の公開資料なし）

~~~diff
- 00588584 ["INT_ADD", "register:40f0:8", ["const:588584:8", "const:4:8"]]
- 00588584 ["CALL", null, ["callee:00c53d00:8"]]
+ 005885c4 ["INT_ADD", "register:40f0:8", ["const:5885c4:8", "const:4:8"]]
+ 005885c4 ["CALL", null, ["callee:00c53d00:8"]]
- 00588584 bytes d72c1b94
+ 005885c4 bytes cf2d1b94
- 005885a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005885a4 ["INT_ADD", "register:40f0:8", ["const:5885a4:8", "const:4:8"]]
- 005885a4 ["CALLIND", null, ["register:0:8"]]
+ 005885e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005885e4 ["INT_ADD", "register:40f0:8", ["const:5885e4:8", "const:4:8"]]
+ 005885e4 ["CALLIND", null, ["register:0:8"]]
- 005885a4 bytes 00013fd6
+ 005885e4 bytes 00013fd6
~~~


<a id="compare-626656d68f8e1b56ee3c5e291127b68b"></a>

### [`005888b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005888b4.md) → [`005888f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005888f4.md) FUN_005888f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005888cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005888b4.md#insn-005888cc)
- 新版 `0058890c`（命令位置の公開資料なし）

~~~diff
- 005888cc ["COPY", "register:0:8", ["register:4040:8"]]
- 005888cc ["INT_ADD", "register:40f0:8", ["const:5888cc:8", "const:4:8"]]
- 005888cc ["CALLIND", null, ["register:0:8"]]
+ 0058890c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058890c ["INT_ADD", "register:40f0:8", ["const:58890c:8", "const:4:8"]]
+ 0058890c ["CALLIND", null, ["register:0:8"]]
- 005888cc bytes 00013fd6
+ 0058890c bytes 00013fd6
~~~


<a id="compare-b39d60ac772a8c488d4d57f27dd1d7b5"></a>

### [`00588908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588908.md) → [`00588948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588948.md) FUN_00588948

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00588934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588908.md#insn-00588934) · [`00588964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588908.md#insn-00588964)
- 新版 `00588974`（命令位置の公開資料なし） · `005889a4`（命令位置の公開資料なし）

~~~diff
- 00588934 ["COPY", "register:0:8", ["register:4040:8"]]
- 00588934 ["INT_ADD", "register:40f0:8", ["const:588934:8", "const:4:8"]]
- 00588934 ["CALLIND", null, ["register:0:8"]]
+ 00588974 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588974 ["INT_ADD", "register:40f0:8", ["const:588974:8", "const:4:8"]]
+ 00588974 ["CALLIND", null, ["register:0:8"]]
- 00588934 bytes 00013fd6
+ 00588974 bytes 00013fd6
- 00588964 ["COPY", "register:0:8", ["register:4040:8"]]
- 00588964 ["INT_ADD", "register:40f0:8", ["const:588964:8", "const:4:8"]]
- 00588964 ["CALLIND", null, ["register:0:8"]]
+ 005889a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005889a4 ["INT_ADD", "register:40f0:8", ["const:5889a4:8", "const:4:8"]]
+ 005889a4 ["CALLIND", null, ["register:0:8"]]
- 00588964 bytes 00013fd6
+ 005889a4 bytes 00013fd6
~~~


<a id="compare-5502d132f68c5897d55ef62a38e9783a"></a>

### [`005889b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005889b8.md) → [`005889f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005889f8.md) FUN_005889f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005889d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005889b8.md#insn-005889d0)
- 新版 `00588a10`（命令位置の公開資料なし）

~~~diff
- 005889d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005889d0 ["INT_ADD", "register:40f0:8", ["const:5889d0:8", "const:4:8"]]
- 005889d0 ["CALLIND", null, ["register:0:8"]]
+ 00588a10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588a10 ["INT_ADD", "register:40f0:8", ["const:588a10:8", "const:4:8"]]
+ 00588a10 ["CALLIND", null, ["register:0:8"]]
- 005889d0 bytes 00013fd6
+ 00588a10 bytes 00013fd6
~~~


<a id="compare-4883d4d3d5cbf68662df22f11ea4e00e"></a>

### [`00588a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588a08.md) → [`00588a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588a48.md) FUN_00588a48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00588a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588a08.md#insn-00588a34) · [`00588a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588a08.md#insn-00588a64)
- 新版 `00588a74`（命令位置の公開資料なし） · `00588aa4`（命令位置の公開資料なし）

~~~diff
- 00588a34 ["COPY", "register:0:8", ["register:4040:8"]]
- 00588a34 ["INT_ADD", "register:40f0:8", ["const:588a34:8", "const:4:8"]]
- 00588a34 ["CALLIND", null, ["register:0:8"]]
+ 00588a74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588a74 ["INT_ADD", "register:40f0:8", ["const:588a74:8", "const:4:8"]]
+ 00588a74 ["CALLIND", null, ["register:0:8"]]
- 00588a34 bytes 00013fd6
+ 00588a74 bytes 00013fd6
- 00588a64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00588a64 ["INT_ADD", "register:40f0:8", ["const:588a64:8", "const:4:8"]]
- 00588a64 ["CALLIND", null, ["register:0:8"]]
+ 00588aa4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588aa4 ["INT_ADD", "register:40f0:8", ["const:588aa4:8", "const:4:8"]]
+ 00588aa4 ["CALLIND", null, ["register:0:8"]]
- 00588a64 bytes 00013fd6
+ 00588aa4 bytes 00013fd6
~~~


<a id="compare-ba3ea0f2d3dc3b3ed52f1c9ca56b34ec"></a>

### [`00588ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588ab8.md) → [`00588af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588af8.md) FUN_00588af8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005975c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975c0.md) · 呼出先 5件 [`00550b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550b64.md) [`00588b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588b80.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00597600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597600.md) · 呼出先 5件 [`00550ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550ba4.md) [`00588bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588bc0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00588ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588ab8.md#insn-00588ae0) · [`00588af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588ab8.md#insn-00588af4) · [`00588b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588ab8.md#insn-00588b18)
- 新版 `00588b20`（命令位置の公開資料なし） · `00588b34`（命令位置の公開資料なし） · `00588b58`（命令位置の公開資料なし）

~~~diff
- 00588ae0 ["INT_ADD", "register:40f0:8", ["const:588ae0:8", "const:4:8"]]
- 00588ae0 ["CALL", null, ["callee:00550ba4:8"]]
+ 00588b20 ["INT_ADD", "register:40f0:8", ["const:588b20:8", "const:4:8"]]
+ 00588b20 ["CALL", null, ["callee:00550ba4:8"]]
- 00588ae0 bytes 2120ff97
+ 00588b20 bytes 2120ff97
- 00588af4 ["INT_ADD", "register:40f0:8", ["const:588af4:8", "const:4:8"]]
- 00588af4 ["CALL", null, ["callee:00588bc0:8"]]
+ 00588b34 ["INT_ADD", "register:40f0:8", ["const:588b34:8", "const:4:8"]]
+ 00588b34 ["CALL", null, ["callee:00588bc0:8"]]
- 00588af4 bytes 23000094
+ 00588b34 bytes 23000094
- 00588b18 ["INT_ADD", "register:40f0:8", ["const:588b18:8", "const:4:8"]]
- 00588b18 ["CALL", null, ["callee:00c53d00:8"]]
+ 00588b58 ["INT_ADD", "register:40f0:8", ["const:588b58:8", "const:4:8"]]
+ 00588b58 ["CALL", null, ["callee:00c53d00:8"]]
- 00588b18 bytes 722b1b94
+ 00588b58 bytes 6a2c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ab351c48fc832b46492edd256cdaf09"></a>

### [`00588cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588cac.md) → [`00588cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588cec.md) FUN_00588cec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`005885b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005885b8.md) [`0058b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b0f0.md) [`0058b170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b170.md) [`00594fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594fe8.md) · 呼出先 4件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 4件 [`005885f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005885f8.md) [`0058b130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b130.md) [`0058b1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b1b0.md) [`00595028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595028.md) · 呼出先 4件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00588d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588cac.md#insn-00588d40) · [`00588d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588cac.md#insn-00588d6c) · [`00588d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588cac.md#insn-00588d80)
- 新版 `00588d80`（命令位置の公開資料なし） · `00588dac`（命令位置の公開資料なし） · `00588dc0`（命令位置の公開資料なし）

~~~diff
- 00588d40 ["INT_ADD", "register:40f0:8", ["const:588d40:8", "const:4:8"]]
- 00588d40 ["CALL", null, ["callee:00c57e90:8"]]
+ 00588d80 ["INT_ADD", "register:40f0:8", ["const:588d80:8", "const:4:8"]]
+ 00588d80 ["CALL", null, ["callee:00c57e90:8"]]
- 00588d40 bytes 543b1b94
+ 00588d80 bytes 443c1b94
- 00588d6c ["INT_ADD", "register:40f0:8", ["const:588d6c:8", "const:4:8"]]
- 00588d6c ["CALL", null, ["callee:00c58000:8"]]
+ 00588dac ["INT_ADD", "register:40f0:8", ["const:588dac:8", "const:4:8"]]
+ 00588dac ["CALL", null, ["callee:00c58000:8"]]
- 00588d6c bytes a53b1b94
+ 00588dac bytes 953c1b94
- 00588d80 ["INT_ADD", "register:40f0:8", ["const:588d80:8", "const:4:8"]]
- 00588d80 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00588dc0 ["INT_ADD", "register:40f0:8", ["const:588dc0:8", "const:4:8"]]
+ 00588dc0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00588d80 bytes 4c3b1b94
+ 00588dc0 bytes 3c3c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea2328571b0242e00436403f2fea8ad8"></a>

### [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) → [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) FUN_005896f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 33件 [`00589150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589150.md) [`00b40f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40f0c.md) [`00b41538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b41538.md) [`00b4163c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b4163c.md) [`00b41b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b41b28.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 33件 [`00589190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589190.md) [`00b41334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41334.md) [`00b41960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41960.md) [`00b41a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41a64.md) [`00b41f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41f50.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00589728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md#insn-00589728) · [`0058974c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md#insn-0058974c)
- 新版 `00589768`（命令位置の公開資料なし） · `0058978c`（命令位置の公開資料なし）

~~~diff
- 00589728 ["COPY", "register:0:8", ["register:4040:8"]]
- 00589728 ["INT_ADD", "register:40f0:8", ["const:589728:8", "const:4:8"]]
- 00589728 ["CALLIND", null, ["register:0:8"]]
+ 00589768 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589768 ["INT_ADD", "register:40f0:8", ["const:589768:8", "const:4:8"]]
+ 00589768 ["CALLIND", null, ["register:0:8"]]
- 00589728 bytes 00013fd6
+ 00589768 bytes 00013fd6
- 0058974c ["INT_ADD", "register:40f0:8", ["const:58974c:8", "const:4:8"]]
- 0058974c ["CALL", null, ["callee:00c57ee0:8"]]
+ 0058978c ["INT_ADD", "register:40f0:8", ["const:58978c:8", "const:4:8"]]
+ 0058978c ["CALL", null, ["callee:00c57ee0:8"]]
- 0058974c bytes e5381b94
+ 0058978c bytes d5391b94
~~~


<a id="compare-f9991c31d57bcd521d05d6aa4eef3fa9"></a>

### [`00589820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589820.md) → [`00589860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589860.md) FUN_00589860

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0058d130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d130.md) · 呼出先 1件 [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md)
- 新版 呼出元 1件 [`0058d170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d170.md) · 呼出先 1件 [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00589838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589820.md#insn-00589838)
- 新版 `00589878`（命令位置の公開資料なし）

~~~diff
- 00589838 ["INT_ADD", "register:40f0:8", ["const:589838:8", "const:4:8"]]
- 00589838 ["CALL", null, ["callee:00588ecc:8"]]
+ 00589878 ["INT_ADD", "register:40f0:8", ["const:589878:8", "const:4:8"]]
+ 00589878 ["CALL", null, ["callee:00588ecc:8"]]
- 00589838 bytes 95fdff97
+ 00589878 bytes 95fdff97
~~~


<a id="compare-a894eb0d72c5041c84dd7d3709d5ec92"></a>

### [`0058984c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058984c.md) → [`0058988c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058988c.md) FUN_0058988c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00589868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058984c.md#insn-00589868)
- 新版 `005898a8`（命令位置の公開資料なし）

~~~diff
- 00589868 ["INT_ADD", "register:40f0:8", ["const:589868:8", "const:4:8"]]
- 00589868 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005898a8 ["INT_ADD", "register:40f0:8", ["const:5898a8:8", "const:4:8"]]
+ 005898a8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00589868 bytes 92381b94
+ 005898a8 bytes 82391b94
~~~


<a id="compare-f00f18d9c62f45edbba3374104bdf2f4"></a>

### [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md) → [`00589954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589954.md) FUN_00589954

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 33件 [`0043b3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b3e8.md) [`0043b57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b57c.md) [`0043b694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b694.md) [`00497664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497664.md) [`00573b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00573/00573b20.md) · 呼出先 6件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 33件 [`0043b428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b428.md) [`0043b5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b5bc.md) [`0043b6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b6d4.md) [`004976a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004976a4.md) [`00573b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00573/00573b60.md) · 呼出先 6件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00589958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md#insn-00589958) · [`00589974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md#insn-00589974) · [`0058997c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md#insn-0058997c)
- 新版 `00589998`（命令位置の公開資料なし） · `005899b4`（命令位置の公開資料なし） · `005899bc`（命令位置の公開資料なし）

~~~diff
- 00589958 ["COPY", "register:0:8", ["register:4040:8"]]
- 00589958 ["INT_ADD", "register:40f0:8", ["const:589958:8", "const:4:8"]]
- 00589958 ["CALLIND", null, ["register:0:8"]]
+ 00589998 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589998 ["INT_ADD", "register:40f0:8", ["const:589998:8", "const:4:8"]]
+ 00589998 ["CALLIND", null, ["register:0:8"]]
- 00589958 bytes 00013fd6
+ 00589998 bytes 00013fd6
- 00589974 ["COPY", "register:0:8", ["register:4040:8"]]
- 00589974 ["INT_ADD", "register:40f0:8", ["const:589974:8", "const:4:8"]]
- 00589974 ["CALLIND", null, ["register:0:8"]]
+ 005899b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005899b4 ["INT_ADD", "register:40f0:8", ["const:5899b4:8", "const:4:8"]]
+ 005899b4 ["CALLIND", null, ["register:0:8"]]
- 00589974 bytes 00013fd6
+ 005899b4 bytes 00013fd6
- 0058997c ["INT_ADD", "register:40f0:8", ["const:58997c:8", "const:4:8"]]
- 0058997c ["CALL", null, ["callee:00c57fe0:8"]]
+ 005899bc ["INT_ADD", "register:40f0:8", ["const:5899bc:8", "const:4:8"]]
+ 005899bc ["CALL", null, ["callee:00c57fe0:8"]]
- 0058997c bytes 99381b94
+ 005899bc bytes 89391b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ce06a3bf0ecba733831a44d4c6a24a0"></a>

### [`0058a008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a008.md) → [`0058a048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a048.md) FUN_0058a048

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00589ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589ec8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00589f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589f08.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058a018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a008.md#insn-0058a018)
- 新版 `0058a058`（命令位置の公開資料なし）

~~~diff
- 0058a018 ["INT_ADD", "register:40f0:8", ["const:58a018:8", "const:4:8"]]
- 0058a018 ["CALL", null, ["callee:00589f08:8"]]
+ 0058a058 ["INT_ADD", "register:40f0:8", ["const:58a058:8", "const:4:8"]]
+ 0058a058 ["CALL", null, ["callee:00589f08:8"]]
- 0058a018 bytes acffff97
+ 0058a058 bytes acffff97
~~~


<a id="compare-c493fa150b7b8cc987c7213dadb933d0"></a>

### [`0058a664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a664.md) → [`0058a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a6a4.md) FUN_0058a6a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00572420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572420.md) [`00578e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578e7c.md) [`0057b124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b124.md) [`0058386c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058386c.md) [`0058416c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/0058416c.md) · 呼出先 0件 
- 新版 呼出元 5件 [`00572460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572460.md) [`00578ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578ebc.md) [`0057b164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b164.md) [`005838ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005838ac.md) [`005841ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005841ac.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058a69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a664.md#insn-0058a69c) · [`0058a6bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a664.md#insn-0058a6bc)
- 新版 `0058a6dc`（命令位置の公開資料なし） · `0058a6fc`（命令位置の公開資料なし）

~~~diff
- 0058a69c ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a69c ["INT_ADD", "register:40f0:8", ["const:58a69c:8", "const:4:8"]]
- 0058a69c ["CALLIND", null, ["register:0:8"]]
+ 0058a6dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a6dc ["INT_ADD", "register:40f0:8", ["const:58a6dc:8", "const:4:8"]]
+ 0058a6dc ["CALLIND", null, ["register:0:8"]]
- 0058a69c bytes 00013fd6
+ 0058a6dc bytes 00013fd6
- 0058a6bc ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a6bc ["INT_ADD", "register:40f0:8", ["const:58a6bc:8", "const:4:8"]]
- 0058a6bc ["CALLIND", null, ["register:0:8"]]
+ 0058a6fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a6fc ["INT_ADD", "register:40f0:8", ["const:58a6fc:8", "const:4:8"]]
+ 0058a6fc ["CALLIND", null, ["register:0:8"]]
- 0058a6bc bytes 00013fd6
+ 0058a6fc bytes 00013fd6
~~~


<a id="compare-39115c3316899141fe30a33095a2994b"></a>

### [`0058a6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a6e0.md) → [`0058a720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a720.md) FUN_0058a720

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00572c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572c28.md) [`00573e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00573/00573e40.md) [`005740a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005740a0.md) · 呼出先 1件 [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md)
- 新版 呼出元 3件 [`00572c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572c68.md) [`00573e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00573/00573e80.md) [`005740e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005740e0.md) · 呼出先 1件 [`00589954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589954.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058a708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a6e0.md#insn-0058a708) · [`0058a71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a6e0.md#insn-0058a71c) · [`0058a734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a6e0.md#insn-0058a734)
- 新版 `0058a748`（命令位置の公開資料なし） · `0058a75c`（命令位置の公開資料なし） · `0058a774`（命令位置の公開資料なし）

~~~diff
- 0058a708 ["COPY", "register:0:8", ["register:4048:8"]]
- 0058a708 ["INT_ADD", "register:40f0:8", ["const:58a708:8", "const:4:8"]]
- 0058a708 ["CALLIND", null, ["register:0:8"]]
+ 0058a748 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0058a748 ["INT_ADD", "register:40f0:8", ["const:58a748:8", "const:4:8"]]
+ 0058a748 ["CALLIND", null, ["register:0:8"]]
- 0058a708 bytes 20013fd6
+ 0058a748 bytes 20013fd6
- 0058a71c ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a71c ["INT_ADD", "register:40f0:8", ["const:58a71c:8", "const:4:8"]]
- 0058a71c ["CALLIND", null, ["register:0:8"]]
+ 0058a75c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a75c ["INT_ADD", "register:40f0:8", ["const:58a75c:8", "const:4:8"]]
+ 0058a75c ["CALLIND", null, ["register:0:8"]]
- 0058a71c bytes 00013fd6
+ 0058a75c bytes 00013fd6
- 0058a734 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a734 ["INT_ADD", "register:40f0:8", ["const:58a734:8", "const:4:8"]]
- 0058a734 ["CALLIND", null, ["register:0:8"]]
+ 0058a774 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a774 ["INT_ADD", "register:40f0:8", ["const:58a774:8", "const:4:8"]]
+ 0058a774 ["CALLIND", null, ["register:0:8"]]
- 0058a734 bytes 00013fd6
+ 0058a774 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8c686e133fd70f7f1b005b3b6c0f342"></a>

### [`0058a90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a90c.md) → [`0058a94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a94c.md) FUN_0058a94c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md) [`005897b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005897b4.md) [`0058a274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a274.md) [`0058a7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a7e4.md) [`0058a830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a830.md) · 呼出先 2件 [`0058a90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a90c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 8件 [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md) [`005897f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005897f4.md) [`0058a2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a2b4.md) [`0058a824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a824.md) [`0058a870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a870.md) · 呼出先 2件 [`0058a94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a94c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058a928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a90c.md#insn-0058a928) · [`0058a934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a90c.md#insn-0058a934) · [`0058a944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a90c.md#insn-0058a944)
- 新版 `0058a968`（命令位置の公開資料なし） · `0058a974`（命令位置の公開資料なし） · `0058a984`（命令位置の公開資料なし）

~~~diff
- 0058a928 ["INT_ADD", "register:40f0:8", ["const:58a928:8", "const:4:8"]]
- 0058a928 ["CALL", null, ["local:b0:8"]]
+ 0058a968 ["INT_ADD", "register:40f0:8", ["const:58a968:8", "const:4:8"]]
+ 0058a968 ["CALL", null, ["local:b0:8"]]
- 0058a928 bytes f9ffff97
+ 0058a968 bytes f9ffff97
- 0058a934 ["INT_ADD", "register:40f0:8", ["const:58a934:8", "const:4:8"]]
- 0058a934 ["CALL", null, ["local:b0:8"]]
+ 0058a974 ["INT_ADD", "register:40f0:8", ["const:58a974:8", "const:4:8"]]
+ 0058a974 ["CALL", null, ["local:b0:8"]]
- 0058a934 bytes f6ffff97
+ 0058a974 bytes f6ffff97
- 0058a944 ["INT_ADD", "register:40f0:8", ["const:58a944:8", "const:4:8"]]
- 0058a944 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0058a984 ["INT_ADD", "register:40f0:8", ["const:58a984:8", "const:4:8"]]
+ 0058a984 ["CALL", null, ["callee:00c57eb0:8"]]
- 0058a944 bytes 5b341b94
+ 0058a984 bytes 4b351b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e457f9b2d2f0b4a0de3e2f2defc970a"></a>

### [`0058a96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a96c.md) → [`0058a9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a9ac.md) FUN_0058a9ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`0058aa94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058aa94.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 2件 [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`0058aad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058aad4.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058a9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a96c.md#insn-0058a9d0) · [`0058aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a96c.md#insn-0058aa00) · [`0058aa64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a96c.md#insn-0058aa64)
- 新版 `0058aa10`（命令位置の公開資料なし） · `0058aa40`（命令位置の公開資料なし） · `0058aaa4`（命令位置の公開資料なし）

~~~diff
- 0058a9d0 ["INT_ADD", "register:40f0:8", ["const:58a9d0:8", "const:4:8"]]
- 0058a9d0 ["CALL", null, ["callee:00c58050:8"]]
+ 0058aa10 ["INT_ADD", "register:40f0:8", ["const:58aa10:8", "const:4:8"]]
+ 0058aa10 ["CALL", null, ["callee:00c58050:8"]]
- 0058a9d0 bytes a0341b94
+ 0058aa10 bytes 90351b94
- 0058aa00 ["INT_ADD", "register:40f0:8", ["const:58aa00:8", "const:4:8"]]
- 0058aa00 ["CALL", null, ["callee:00c58050:8"]]
+ 0058aa40 ["INT_ADD", "register:40f0:8", ["const:58aa40:8", "const:4:8"]]
+ 0058aa40 ["CALL", null, ["callee:00c58050:8"]]
- 0058aa00 bytes 94341b94
+ 0058aa40 bytes 84351b94
- 0058aa64 ["INT_ADD", "register:40f0:8", ["const:58aa64:8", "const:4:8"]]
- 0058aa64 ["CALL", null, ["callee:00c58050:8"]]
+ 0058aaa4 ["INT_ADD", "register:40f0:8", ["const:58aaa4:8", "const:4:8"]]
+ 0058aaa4 ["CALL", null, ["callee:00c58050:8"]]
- 0058aa64 bytes 7b341b94
+ 0058aaa4 bytes 6b351b94
~~~


<a id="compare-b8608c198d7f98f25a53cbd80c7c64a7"></a>

### [`0058aa94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058aa94.md) → [`0058aad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058aad4.md) FUN_0058aad4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0058a96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a96c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0058a9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a9ac.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058aadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058aa94.md#insn-0058aadc) · [`0058aaec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058aa94.md#insn-0058aaec) · [`0058ab0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058aa94.md#insn-0058ab0c)
- 新版 `0058ab1c`（命令位置の公開資料なし） · `0058ab2c`（命令位置の公開資料なし） · `0058ab4c`（命令位置の公開資料なし）

~~~diff
- 0058aadc ["INT_ADD", "register:40f0:8", ["const:58aadc:8", "const:4:8"]]
- 0058aadc ["CALL", null, ["callee:0058a9ac:8"]]
+ 0058ab1c ["INT_ADD", "register:40f0:8", ["const:58ab1c:8", "const:4:8"]]
+ 0058ab1c ["CALL", null, ["callee:0058a9ac:8"]]
- 0058aadc bytes a4ffff97
+ 0058ab1c bytes a4ffff97
- 0058aaec ["INT_ADD", "register:40f0:8", ["const:58aaec:8", "const:4:8"]]
- 0058aaec ["CALL", null, ["callee:0058a9ac:8"]]
+ 0058ab2c ["INT_ADD", "register:40f0:8", ["const:58ab2c:8", "const:4:8"]]
+ 0058ab2c ["CALL", null, ["callee:0058a9ac:8"]]
- 0058aaec bytes a0ffff97
+ 0058ab2c bytes a0ffff97
- 0058ab0c ["INT_ADD", "register:40f0:8", ["const:58ab0c:8", "const:4:8"]]
- 0058ab0c ["CALL", null, ["callee:00c57e90:8"]]
+ 0058ab4c ["INT_ADD", "register:40f0:8", ["const:58ab4c:8", "const:4:8"]]
+ 0058ab4c ["CALL", null, ["callee:00c57e90:8"]]
- 0058ab0c bytes e1331b94
+ 0058ab4c bytes d1341b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04fec5101f4da697a3cfd6153417a910"></a>

### [`0058ac90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058ac90.md) → [`0058acd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058acd0.md) FUN_0058acd0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058acec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058ac90.md#insn-0058acec) · [`0058ad0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058ac90.md#insn-0058ad0c) · [`0058ad28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058ac90.md#insn-0058ad28)
- 新版 `0058ad2c`（命令位置の公開資料なし） · `0058ad4c`（命令位置の公開資料なし） · `0058ad68`（命令位置の公開資料なし）

~~~diff
- 0058acec ["INT_ADD", "register:40f0:8", ["const:58acec:8", "const:4:8"]]
- 0058acec ["CALL", null, ["callee:00c57e90:8"]]
+ 0058ad2c ["INT_ADD", "register:40f0:8", ["const:58ad2c:8", "const:4:8"]]
+ 0058ad2c ["CALL", null, ["callee:00c57e90:8"]]
- 0058acec bytes 69331b94
+ 0058ad2c bytes 59341b94
- 0058ad0c ["INT_ADD", "register:40f0:8", ["const:58ad0c:8", "const:4:8"]]
- 0058ad0c ["CALL", null, ["callee:00c57f40:8"]]
+ 0058ad4c ["INT_ADD", "register:40f0:8", ["const:58ad4c:8", "const:4:8"]]
+ 0058ad4c ["CALL", null, ["callee:00c57f40:8"]]
- 0058ad0c bytes 8d331b94
+ 0058ad4c bytes 7d341b94
- 0058ad28 ["INT_ADD", "register:40f0:8", ["const:58ad28:8", "const:4:8"]]
- 0058ad28 ["CALL", null, ["callee:0043b764:8"]]
+ 0058ad68 ["INT_ADD", "register:40f0:8", ["const:58ad68:8", "const:4:8"]]
+ 0058ad68 ["CALL", null, ["callee:0043b764:8"]]
- 0058ad28 bytes 7fc2fa97
+ 0058ad68 bytes 7fc2fa97
~~~


<a id="compare-4ffd8eaad46b1f0d36b44ff29da44694"></a>

### [`0058ad2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058ad2c.md) → [`0058ad6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058ad6c.md) FUN_0058ad6c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00584d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584d5c.md) · 呼出先 2件 [`0058b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b5d4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00584d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584d9c.md) · 呼出先 2件 [`0058b614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b614.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058ad58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058ad2c.md#insn-0058ad58) · [`0058ad84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058ad2c.md#insn-0058ad84)
- 新版 `0058ad98`（命令位置の公開資料なし） · `0058adc4`（命令位置の公開資料なし）

~~~diff
- 0058ad58 ["INT_ADD", "register:40f0:8", ["const:58ad58:8", "const:4:8"]]
- 0058ad58 ["CALL", null, ["callee:0058b614:8"]]
+ 0058ad98 ["INT_ADD", "register:40f0:8", ["const:58ad98:8", "const:4:8"]]
+ 0058ad98 ["CALL", null, ["callee:0058b614:8"]]
- 0058ad58 bytes 1f020094
+ 0058ad98 bytes 1f020094
- 0058ad84 ["INT_ADD", "register:40f0:8", ["const:58ad84:8", "const:4:8"]]
- 0058ad84 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0058adc4 ["INT_ADD", "register:40f0:8", ["const:58adc4:8", "const:4:8"]]
+ 0058adc4 ["CALL", null, ["callee:00c57ee0:8"]]
- 0058ad84 bytes 57331b94
+ 0058adc4 bytes 47341b94
~~~


<a id="compare-75f8ad42e41ead4e92c837c6f8fd4fe5"></a>

### [`0058ad88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058ad88.md) → [`0058adc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058adc8.md) FUN_0058adc8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005975c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975c8.md) [`0087d340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d340.md) · 呼出先 5件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0058b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b5d4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`00597608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597608.md) [`0087d380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d380.md) · 呼出先 5件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0058b614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b614.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058add8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058ad88.md#insn-0058add8) · [`0058ae6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058ad88.md#insn-0058ae6c) · [`0058ae84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058ad88.md#insn-0058ae84)
- 新版 `0058ae18`（命令位置の公開資料なし） · `0058aeac`（命令位置の公開資料なし） · `0058aec4`（命令位置の公開資料なし）

~~~diff
- 0058add8 ["INT_ADD", "register:40f0:8", ["const:58add8:8", "const:4:8"]]
- 0058add8 ["CALL", null, ["callee:00c57e90:8"]]
+ 0058ae18 ["INT_ADD", "register:40f0:8", ["const:58ae18:8", "const:4:8"]]
+ 0058ae18 ["CALL", null, ["callee:00c57e90:8"]]
- 0058add8 bytes 2e331b94
+ 0058ae18 bytes 1e341b94
- 0058ae6c ["INT_ADD", "register:40f0:8", ["const:58ae6c:8", "const:4:8"]]
- 0058ae6c ["CALL", null, ["callee:0058b614:8"]]
+ 0058aeac ["INT_ADD", "register:40f0:8", ["const:58aeac:8", "const:4:8"]]
+ 0058aeac ["CALL", null, ["callee:0058b614:8"]]
- 0058ae6c bytes da010094
+ 0058aeac bytes da010094
- 0058ae84 ["INT_ADD", "register:40f0:8", ["const:58ae84:8", "const:4:8"]]
- 0058ae84 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0058aec4 ["INT_ADD", "register:40f0:8", ["const:58aec4:8", "const:4:8"]]
+ 0058aec4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0058ae84 bytes 0b331b94
+ 0058aec4 bytes fb331b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bbfecf90bb4fe76096c0ddce78fb943"></a>

### [`0058aefc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058aefc.md) → [`0058af3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058af3c.md) FUN_0058af3c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005975cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975cc.md) · 呼出先 6件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0058b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b5d4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0059760c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059760c.md) · 呼出先 6件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0058b614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b614.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058af40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058aefc.md#insn-0058af40) · [`0058af58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058aefc.md#insn-0058af58) · [`0058af6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058aefc.md#insn-0058af6c)
- 新版 `0058af80`（命令位置の公開資料なし） · `0058af98`（命令位置の公開資料なし） · `0058afac`（命令位置の公開資料なし）

~~~diff
- 0058af40 ["INT_ADD", "register:40f0:8", ["const:58af40:8", "const:4:8"]]
- 0058af40 ["CALL", null, ["callee:00c57e90:8"]]
+ 0058af80 ["INT_ADD", "register:40f0:8", ["const:58af80:8", "const:4:8"]]
+ 0058af80 ["CALL", null, ["callee:00c57e90:8"]]
- 0058af40 bytes d4321b94
+ 0058af80 bytes c4331b94
- 0058af58 ["INT_ADD", "register:40f0:8", ["const:58af58:8", "const:4:8"]]
- 0058af58 ["CALL", null, ["callee:00c58000:8"]]
+ 0058af98 ["INT_ADD", "register:40f0:8", ["const:58af98:8", "const:4:8"]]
+ 0058af98 ["CALL", null, ["callee:00c58000:8"]]
- 0058af58 bytes 2a331b94
+ 0058af98 bytes 1a341b94
- 0058af6c ["INT_ADD", "register:40f0:8", ["const:58af6c:8", "const:4:8"]]
- 0058af6c ["CALL", null, ["callee:0058b614:8"]]
+ 0058afac ["INT_ADD", "register:40f0:8", ["const:58afac:8", "const:4:8"]]
+ 0058afac ["CALL", null, ["callee:0058b614:8"]]
- 0058af6c bytes 9a010094
+ 0058afac bytes 9a010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-893c870000006636dd485922d4b422c9"></a>

### [`0058b014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b014.md) → [`0058b054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b054.md) FUN_0058b054

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058b070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b014.md#insn-0058b070) · [`0058b090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b014.md#insn-0058b090) · [`0058b0ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b014.md#insn-0058b0ac)
- 新版 `0058b0b0`（命令位置の公開資料なし） · `0058b0d0`（命令位置の公開資料なし） · `0058b0ec`（命令位置の公開資料なし）

~~~diff
- 0058b070 ["INT_ADD", "register:40f0:8", ["const:58b070:8", "const:4:8"]]
- 0058b070 ["CALL", null, ["callee:00c57e90:8"]]
+ 0058b0b0 ["INT_ADD", "register:40f0:8", ["const:58b0b0:8", "const:4:8"]]
+ 0058b0b0 ["CALL", null, ["callee:00c57e90:8"]]
- 0058b070 bytes 88321b94
+ 0058b0b0 bytes 78331b94
- 0058b090 ["INT_ADD", "register:40f0:8", ["const:58b090:8", "const:4:8"]]
- 0058b090 ["CALL", null, ["callee:00c57f40:8"]]
+ 0058b0d0 ["INT_ADD", "register:40f0:8", ["const:58b0d0:8", "const:4:8"]]
+ 0058b0d0 ["CALL", null, ["callee:00c57f40:8"]]
- 0058b090 bytes ac321b94
+ 0058b0d0 bytes 9c331b94
- 0058b0ac ["INT_ADD", "register:40f0:8", ["const:58b0ac:8", "const:4:8"]]
- 0058b0ac ["CALL", null, ["callee:0043b764:8"]]
+ 0058b0ec ["INT_ADD", "register:40f0:8", ["const:58b0ec:8", "const:4:8"]]
+ 0058b0ec ["CALL", null, ["callee:0043b764:8"]]
- 0058b0ac bytes 9ec1fa97
+ 0058b0ec bytes 9ec1fa97
~~~


<a id="compare-1984b01be4b94e5295cb28102d18d12e"></a>

### [`0058b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b0f0.md) → [`0058b130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b130.md) FUN_0058b130

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00588cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588cac.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00588cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588cec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058b11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b0f0.md#insn-0058b11c) · [`0058b134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b0f0.md#insn-0058b134) · [`0058b14c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b0f0.md#insn-0058b14c)
- 新版 `0058b15c`（命令位置の公開資料なし） · `0058b174`（命令位置の公開資料なし） · `0058b18c`（命令位置の公開資料なし）

~~~diff
- 0058b11c ["COPY", "register:0:8", ["register:4048:8"]]
- 0058b11c ["INT_ADD", "register:40f0:8", ["const:58b11c:8", "const:4:8"]]
- 0058b11c ["CALLIND", null, ["register:0:8"]]
+ 0058b15c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0058b15c ["INT_ADD", "register:40f0:8", ["const:58b15c:8", "const:4:8"]]
+ 0058b15c ["CALLIND", null, ["register:0:8"]]
- 0058b11c bytes 20013fd6
+ 0058b15c bytes 20013fd6
- 0058b134 ["COPY", "register:0:8", ["register:4048:8"]]
- 0058b134 ["INT_ADD", "register:40f0:8", ["const:58b134:8", "const:4:8"]]
- 0058b134 ["CALLIND", null, ["register:0:8"]]
+ 0058b174 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0058b174 ["INT_ADD", "register:40f0:8", ["const:58b174:8", "const:4:8"]]
+ 0058b174 ["CALLIND", null, ["register:0:8"]]
- 0058b134 bytes 20013fd6
+ 0058b174 bytes 20013fd6
- 0058b14c ["COPY", "register:0:8", ["register:4048:8"]]
- 0058b14c ["INT_ADD", "register:40f0:8", ["const:58b14c:8", "const:4:8"]]
- 0058b14c ["CALLIND", null, ["register:0:8"]]
+ 0058b18c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0058b18c ["INT_ADD", "register:40f0:8", ["const:58b18c:8", "const:4:8"]]
+ 0058b18c ["CALLIND", null, ["register:0:8"]]
- 0058b14c bytes 20013fd6
+ 0058b18c bytes 20013fd6
~~~


<a id="compare-52acd0b4c6fdbdb4cd1abd4e933147a1"></a>

### [`0058b190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b190.md) → [`0058b1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b1d0.md) FUN_0058b1d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005975d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975d0.md) · 呼出先 3件 [`0058b7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b7b4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00597610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597610.md) · 呼出先 3件 [`0058b7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b7f4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058b1c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b190.md#insn-0058b1c4) · [`0058b1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b190.md#insn-0058b1dc) · [`0058b230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b190.md#insn-0058b230)
- 新版 `0058b204`（命令位置の公開資料なし） · `0058b21c`（命令位置の公開資料なし） · `0058b270`（命令位置の公開資料なし）

~~~diff
- 0058b1c4 ["INT_ADD", "register:40f0:8", ["const:58b1c4:8", "const:4:8"]]
- 0058b1c4 ["CALL", null, ["callee:0058b7f4:8"]]
+ 0058b204 ["INT_ADD", "register:40f0:8", ["const:58b204:8", "const:4:8"]]
+ 0058b204 ["CALL", null, ["callee:0058b7f4:8"]]
- 0058b1c4 bytes 7c010094
+ 0058b204 bytes 7c010094
- 0058b1dc ["INT_ADD", "register:40f0:8", ["const:58b1dc:8", "const:4:8"]]
- 0058b1dc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0058b21c ["INT_ADD", "register:40f0:8", ["const:58b21c:8", "const:4:8"]]
+ 0058b21c ["CALL", null, ["callee:00c57eb0:8"]]
- 0058b1dc bytes 35321b94
+ 0058b21c bytes 25331b94
- 0058b230 ["INT_ADD", "register:40f0:8", ["const:58b230:8", "const:4:8"]]
- 0058b230 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0058b270 ["INT_ADD", "register:40f0:8", ["const:58b270:8", "const:4:8"]]
+ 0058b270 ["CALL", null, ["callee:00c57ee0:8"]]
- 0058b230 bytes 2c321b94
+ 0058b270 bytes 1c331b94
~~~


<a id="compare-62fa56f52a41f172321294d3f879fd40"></a>

### [`0058b234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b234.md) → [`0058b274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b274.md) FUN_0058b274

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005975d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975d4.md) · 呼出先 5件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0058b7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b7b4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00597614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597614.md) · 呼出先 5件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0058b7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b7f4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058b284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b234.md#insn-0058b284) · [`0058b318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b234.md#insn-0058b318) · [`0058b330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b234.md#insn-0058b330)
- 新版 `0058b2c4`（命令位置の公開資料なし） · `0058b358`（命令位置の公開資料なし） · `0058b370`（命令位置の公開資料なし）

~~~diff
- 0058b284 ["INT_ADD", "register:40f0:8", ["const:58b284:8", "const:4:8"]]
- 0058b284 ["CALL", null, ["callee:00c57e90:8"]]
+ 0058b2c4 ["INT_ADD", "register:40f0:8", ["const:58b2c4:8", "const:4:8"]]
+ 0058b2c4 ["CALL", null, ["callee:00c57e90:8"]]
- 0058b284 bytes 03321b94
+ 0058b2c4 bytes f3321b94
- 0058b318 ["INT_ADD", "register:40f0:8", ["const:58b318:8", "const:4:8"]]
- 0058b318 ["CALL", null, ["callee:0058b7f4:8"]]
+ 0058b358 ["INT_ADD", "register:40f0:8", ["const:58b358:8", "const:4:8"]]
+ 0058b358 ["CALL", null, ["callee:0058b7f4:8"]]
- 0058b318 bytes 27010094
+ 0058b358 bytes 27010094
- 0058b330 ["INT_ADD", "register:40f0:8", ["const:58b330:8", "const:4:8"]]
- 0058b330 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0058b370 ["INT_ADD", "register:40f0:8", ["const:58b370:8", "const:4:8"]]
+ 0058b370 ["CALL", null, ["callee:00c57eb0:8"]]
- 0058b330 bytes e0311b94
+ 0058b370 bytes d0321b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b38fc68313cbf0fd67eb12d76fe2d2b"></a>

### [`0058b3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b3a8.md) → [`0058b3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b3e8.md) FUN_0058b3e8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005975d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975d8.md) · 呼出先 6件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0058b7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b7b4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00597618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597618.md) · 呼出先 6件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0058b7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b7f4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b3a8.md#insn-0058b3e4) · [`0058b3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b3a8.md#insn-0058b3fc) · [`0058b414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b3a8.md#insn-0058b414)
- 新版 `0058b424`（命令位置の公開資料なし） · `0058b43c`（命令位置の公開資料なし） · `0058b454`（命令位置の公開資料なし）

~~~diff
- 0058b3e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058b3e4 ["INT_ADD", "register:40f0:8", ["const:58b3e4:8", "const:4:8"]]
- 0058b3e4 ["CALLIND", null, ["register:0:8"]]
+ 0058b424 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058b424 ["INT_ADD", "register:40f0:8", ["const:58b424:8", "const:4:8"]]
+ 0058b424 ["CALLIND", null, ["register:0:8"]]
- 0058b3e4 bytes 00013fd6
+ 0058b424 bytes 00013fd6
- 0058b3fc ["COPY", "register:0:8", ["register:4048:8"]]
- 0058b3fc ["INT_ADD", "register:40f0:8", ["const:58b3fc:8", "const:4:8"]]
- 0058b3fc ["CALLIND", null, ["register:0:8"]]
+ 0058b43c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0058b43c ["INT_ADD", "register:40f0:8", ["const:58b43c:8", "const:4:8"]]
+ 0058b43c ["CALLIND", null, ["register:0:8"]]
- 0058b3fc bytes 20013fd6
+ 0058b43c bytes 20013fd6
- 0058b414 ["COPY", "register:0:8", ["register:4048:8"]]
- 0058b414 ["INT_ADD", "register:40f0:8", ["const:58b414:8", "const:4:8"]]
- 0058b414 ["CALLIND", null, ["register:0:8"]]
+ 0058b454 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0058b454 ["INT_ADD", "register:40f0:8", ["const:58b454:8", "const:4:8"]]
+ 0058b454 ["CALLIND", null, ["register:0:8"]]
- 0058b414 bytes 20013fd6
+ 0058b454 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb56ba5b0093593039599a3d1c6e3562"></a>

### [`0058b6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b6ac.md) → [`0058b6ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b6ec.md) FUN_0058b6ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0058b0b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b0b8.md) · 呼出先 4件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`0058b0f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b0f8.md) · 呼出先 4件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058b740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b6ac.md#insn-0058b740) · [`0058b768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b6ac.md#insn-0058b768) · [`0058b77c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b6ac.md#insn-0058b77c)
- 新版 `0058b780`（命令位置の公開資料なし） · `0058b7a8`（命令位置の公開資料なし） · `0058b7bc`（命令位置の公開資料なし）

~~~diff
- 0058b740 ["INT_ADD", "register:40f0:8", ["const:58b740:8", "const:4:8"]]
- 0058b740 ["CALL", null, ["callee:00c57e90:8"]]
+ 0058b780 ["INT_ADD", "register:40f0:8", ["const:58b780:8", "const:4:8"]]
+ 0058b780 ["CALL", null, ["callee:00c57e90:8"]]
- 0058b740 bytes d4301b94
+ 0058b780 bytes c4311b94
- 0058b768 ["INT_ADD", "register:40f0:8", ["const:58b768:8", "const:4:8"]]
- 0058b768 ["CALL", null, ["callee:00c58000:8"]]
+ 0058b7a8 ["INT_ADD", "register:40f0:8", ["const:58b7a8:8", "const:4:8"]]
+ 0058b7a8 ["CALL", null, ["callee:00c58000:8"]]
- 0058b768 bytes 26311b94
+ 0058b7a8 bytes 16321b94
- 0058b77c ["INT_ADD", "register:40f0:8", ["const:58b77c:8", "const:4:8"]]
- 0058b77c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0058b7bc ["INT_ADD", "register:40f0:8", ["const:58b7bc:8", "const:4:8"]]
+ 0058b7bc ["CALL", null, ["callee:00c57eb0:8"]]
- 0058b77c bytes cd301b94
+ 0058b7bc bytes bd311b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d07448fd7356fdb58d521c9e1b4733b"></a>

### [`0058eb04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058eb04.md) → [`0058eb44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058eb44.md) FUN_0058eb44

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058eb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058eb04.md#insn-0058eb2c) · [`0058eb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058eb04.md#insn-0058eb34) · [`0058eb80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058eb04.md#insn-0058eb80)
- 新版 `0058eb6c`（命令位置の公開資料なし） · `0058eb74`（命令位置の公開資料なし） · `0058ebc0`（命令位置の公開資料なし）

~~~diff
- 0058eb2c ["INT_ADD", "register:40f0:8", ["const:58eb2c:8", "const:4:8"]]
- 0058eb2c ["CALL", null, ["callee:00589840:8"]]
+ 0058eb6c ["INT_ADD", "register:40f0:8", ["const:58eb6c:8", "const:4:8"]]
+ 0058eb6c ["CALL", null, ["callee:00589840:8"]]
- 0058eb2c bytes 35ebff97
+ 0058eb6c bytes 35ebff97
- 0058eb34 ["INT_ADD", "register:40f0:8", ["const:58eb34:8", "const:4:8"]]
- 0058eb34 ["CALL", null, ["callee:00588e6c:8"]]
+ 0058eb74 ["INT_ADD", "register:40f0:8", ["const:58eb74:8", "const:4:8"]]
+ 0058eb74 ["CALL", null, ["callee:00588e6c:8"]]
- 0058eb34 bytes bee8ff97
+ 0058eb74 bytes bee8ff97
- 0058eb80 ["INT_ADD", "register:40f0:8", ["const:58eb80:8", "const:4:8"]]
- 0058eb80 ["CALL", null, ["callee:00589320:8"]]
+ 0058ebc0 ["INT_ADD", "register:40f0:8", ["const:58ebc0:8", "const:4:8"]]
+ 0058ebc0 ["CALL", null, ["callee:00589320:8"]]
- 0058eb80 bytes d8e9ff97
+ 0058ebc0 bytes d8e9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bfdfeca0c1ce5b07664b98810b58fe3"></a>

### [`0058ecf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058ecf4.md) → [`0058ed34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058ed34.md) FUN_0058ed34

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00597e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e80.md) · 呼出先 8件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`00597ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ec0.md) · 呼出先 8件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058ed14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058ecf4.md#insn-0058ed14) · [`0058ed1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058ecf4.md#insn-0058ed1c) · [`0058ed60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058ecf4.md#insn-0058ed60)
- 新版 `0058ed54`（命令位置の公開資料なし） · `0058ed5c`（命令位置の公開資料なし） · `0058eda0`（命令位置の公開資料なし）

~~~diff
- 0058ed14 ["INT_ADD", "register:40f0:8", ["const:58ed14:8", "const:4:8"]]
- 0058ed14 ["CALL", null, ["callee:00588e6c:8"]]
+ 0058ed54 ["INT_ADD", "register:40f0:8", ["const:58ed54:8", "const:4:8"]]
+ 0058ed54 ["CALL", null, ["callee:00588e6c:8"]]
- 0058ed14 bytes 46e8ff97
+ 0058ed54 bytes 46e8ff97
- 0058ed1c ["INT_ADD", "register:40f0:8", ["const:58ed1c:8", "const:4:8"]]
- 0058ed1c ["CALL", null, ["callee:0058915c:8"]]
+ 0058ed5c ["INT_ADD", "register:40f0:8", ["const:58ed5c:8", "const:4:8"]]
+ 0058ed5c ["CALL", null, ["callee:0058915c:8"]]
- 0058ed1c bytes 00e9ff97
+ 0058ed5c bytes 00e9ff97
- 0058ed60 ["INT_ADD", "register:40f0:8", ["const:58ed60:8", "const:4:8"]]
- 0058ed60 ["CALL", null, ["callee:00589320:8"]]
+ 0058eda0 ["INT_ADD", "register:40f0:8", ["const:58eda0:8", "const:4:8"]]
+ 0058eda0 ["CALL", null, ["callee:00589320:8"]]
- 0058ed60 bytes 60e9ff97
+ 0058eda0 bytes 60e9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02e62cd95e1e7789d213855e25cd1eff"></a>

### [`0058f2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f2d0.md) → [`0058f310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f310.md) FUN_0058f310

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058c524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c524.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`0058c564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c564.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058f33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f2d0.md#insn-0058f33c) · [`0058f398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f2d0.md#insn-0058f398) · [`0058f3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f2d0.md#insn-0058f3c4)
- 新版 `0058f37c`（命令位置の公開資料なし） · `0058f3d8`（命令位置の公開資料なし） · `0058f404`（命令位置の公開資料なし）

~~~diff
- 0058f33c ["INT_ADD", "register:40f0:8", ["const:58f33c:8", "const:4:8"]]
- 0058f33c ["CALL", null, ["callee:00c57e90:8"]]
+ 0058f37c ["INT_ADD", "register:40f0:8", ["const:58f37c:8", "const:4:8"]]
+ 0058f37c ["CALL", null, ["callee:00c57e90:8"]]
- 0058f33c bytes d5211b94
+ 0058f37c bytes c5221b94
- 0058f398 ["COPY", "register:0:8", ["register:4048:8"]]
- 0058f398 ["INT_ADD", "register:40f0:8", ["const:58f398:8", "const:4:8"]]
- 0058f398 ["CALLIND", null, ["register:0:8"]]
+ 0058f3d8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0058f3d8 ["INT_ADD", "register:40f0:8", ["const:58f3d8:8", "const:4:8"]]
+ 0058f3d8 ["CALLIND", null, ["register:0:8"]]
- 0058f398 bytes 20013fd6
+ 0058f3d8 bytes 20013fd6
- 0058f3c4 ["INT_ADD", "register:40f0:8", ["const:58f3c4:8", "const:4:8"]]
- 0058f3c4 ["CALL", null, ["callee:0043bba4:8"]]
+ 0058f404 ["INT_ADD", "register:40f0:8", ["const:58f404:8", "const:4:8"]]
+ 0058f404 ["CALL", null, ["callee:0043bba4:8"]]
- 0058f3c4 bytes e8b1fa97
+ 0058f404 bytes e8b1fa97
~~~


<a id="compare-675b3d6cf24c708734aa38435915f0ce"></a>

### [`0058f3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f3f4.md) → [`0058f434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f434.md) FUN_0058f434

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`0058cc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058cc70.md) [`0058cf18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058cf18.md) [`005ad378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad378.md) [`008883e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/008883e8.md) [`008905cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/008905cc.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 7件 [`0058ccb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058ccb0.md) [`0058cf58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058cf58.md) [`005ad3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad3b8.md) [`00888428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888428.md) [`00890610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890610.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058f460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f3f4.md#insn-0058f460) · [`0058f470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f3f4.md#insn-0058f470) · [`0058f490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f3f4.md#insn-0058f490)
- 新版 `0058f4a0`（命令位置の公開資料なし） · `0058f4b0`（命令位置の公開資料なし） · `0058f4d0`（命令位置の公開資料なし）

~~~diff
- 0058f460 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058f460 ["INT_ADD", "register:40f0:8", ["const:58f460:8", "const:4:8"]]
- 0058f460 ["CALLIND", null, ["register:0:8"]]
+ 0058f4a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f4a0 ["INT_ADD", "register:40f0:8", ["const:58f4a0:8", "const:4:8"]]
+ 0058f4a0 ["CALLIND", null, ["register:0:8"]]
- 0058f460 bytes 00013fd6
+ 0058f4a0 bytes 00013fd6
- 0058f470 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058f470 ["INT_ADD", "register:40f0:8", ["const:58f470:8", "const:4:8"]]
- 0058f470 ["CALLIND", null, ["register:0:8"]]
+ 0058f4b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f4b0 ["INT_ADD", "register:40f0:8", ["const:58f4b0:8", "const:4:8"]]
+ 0058f4b0 ["CALLIND", null, ["register:0:8"]]
- 0058f470 bytes 00013fd6
+ 0058f4b0 bytes 00013fd6
- 0058f490 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058f490 ["INT_ADD", "register:40f0:8", ["const:58f490:8", "const:4:8"]]
- 0058f490 ["CALLIND", null, ["register:0:8"]]
+ 0058f4d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f4d0 ["INT_ADD", "register:40f0:8", ["const:58f4d0:8", "const:4:8"]]
+ 0058f4d0 ["CALLIND", null, ["register:0:8"]]
- 0058f490 bytes 00013fd6
+ 0058f4d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09190facd611fbc5cf897f3051830e5c"></a>

### [`0058f55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f55c.md) → [`0058f59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f59c.md) FUN_0058f59c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 9件 [`0058db4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058db4c.md) [`00b5258c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b5258c.md) [`00b53ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53ec0.md) [`00bc4c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4c34.md) [`00bc4f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4f30.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 9件 [`0058db8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058db8c.md) [`00b529b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b529b4.md) [`00b542e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b542e8.md) [`00bc505c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc505c.md) [`00bc5358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5358.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058f5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f55c.md#insn-0058f5d0) · [`0058f5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f55c.md#insn-0058f5f4)
- 新版 `0058f610`（命令位置の公開資料なし） · `0058f634`（命令位置の公開資料なし）

~~~diff
- 0058f5d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058f5d0 ["INT_ADD", "register:40f0:8", ["const:58f5d0:8", "const:4:8"]]
- 0058f5d0 ["CALLIND", null, ["register:0:8"]]
+ 0058f610 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f610 ["INT_ADD", "register:40f0:8", ["const:58f610:8", "const:4:8"]]
+ 0058f610 ["CALLIND", null, ["register:0:8"]]
- 0058f5d0 bytes 00013fd6
+ 0058f610 bytes 00013fd6
- 0058f5f4 ["INT_ADD", "register:40f0:8", ["const:58f5f4:8", "const:4:8"]]
- 0058f5f4 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0058f634 ["INT_ADD", "register:40f0:8", ["const:58f634:8", "const:4:8"]]
+ 0058f634 ["CALL", null, ["callee:00c57ee0:8"]]
- 0058f5f4 bytes 3b211b94
+ 0058f634 bytes 2b221b94
~~~


<a id="compare-209926dcdb7dad1a4de49f0d8803e376"></a>

### [`0058f6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f6e8.md) → [`0058f728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f728.md) FUN_0058f728

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00590cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590cd8.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00590d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590d18.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058f704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f6e8.md#insn-0058f704) · [`0058f724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f6e8.md#insn-0058f724)
- 新版 `0058f744`（命令位置の公開資料なし） · `0058f764`（命令位置の公開資料なし）

~~~diff
- 0058f704 ["INT_ADD", "register:40f0:8", ["const:58f704:8", "const:4:8"]]
- 0058f704 ["CALL", null, ["callee:00c53d00:8"]]
+ 0058f744 ["INT_ADD", "register:40f0:8", ["const:58f744:8", "const:4:8"]]
+ 0058f744 ["CALL", null, ["callee:00c53d00:8"]]
- 0058f704 bytes 77101b94
+ 0058f744 bytes 6f111b94
- 0058f724 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058f724 ["INT_ADD", "register:40f0:8", ["const:58f724:8", "const:4:8"]]
- 0058f724 ["CALLIND", null, ["register:0:8"]]
+ 0058f764 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f764 ["INT_ADD", "register:40f0:8", ["const:58f764:8", "const:4:8"]]
+ 0058f764 ["CALLIND", null, ["register:0:8"]]
- 0058f724 bytes 00013fd6
+ 0058f764 bytes 00013fd6
~~~


<a id="compare-e395e1028c04fddfd1ebb1731c935e68"></a>

### [`005902a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/005902a8.md) → [`005902e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005902e8.md) FUN_005902e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0058f738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f738.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0058f778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f778.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005902d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/005902a8.md#insn-005902d8) · [`00590324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/005902a8.md#insn-00590324)
- 新版 `00590318`（命令位置の公開資料なし） · `00590364`（命令位置の公開資料なし）

~~~diff
- 005902d8 ["INT_ADD", "register:40f0:8", ["const:5902d8:8", "const:4:8"]]
- 005902d8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00590318 ["INT_ADD", "register:40f0:8", ["const:590318:8", "const:4:8"]]
+ 00590318 ["CALL", null, ["callee:00c57eb0:8"]]
- 005902d8 bytes f61d1b94
+ 00590318 bytes e61e1b94
- 00590324 ["INT_ADD", "register:40f0:8", ["const:590324:8", "const:4:8"]]
- 00590324 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00590364 ["INT_ADD", "register:40f0:8", ["const:590364:8", "const:4:8"]]
+ 00590364 ["CALL", null, ["callee:00c57eb0:8"]]
- 00590324 bytes e31d1b94
+ 00590364 bytes d31e1b94
~~~


<a id="compare-76747863d9b44e588b411862e17e7a14"></a>

### [`00590378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590378.md) → [`005903b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005903b8.md) FUN_005903b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0058fd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fd5c.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00590838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590838.md) [`005909c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/005909c0.md) [`00590b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590b4c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`0058fd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fd9c.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00590878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590878.md) [`00590a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590a00.md) [`00590b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590b8c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00590410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590378.md#insn-00590410) · [`00590454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590378.md#insn-00590454) · [`00590464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590378.md#insn-00590464)
- 新版 `00590450`（命令位置の公開資料なし） · `00590494`（命令位置の公開資料なし） · `005904a4`（命令位置の公開資料なし）

~~~diff
- 00590410 ["INT_ADD", "register:40f0:8", ["const:590410:8", "const:4:8"]]
- 00590410 ["CALL", null, ["callee:00c57f40:8"]]
+ 00590450 ["INT_ADD", "register:40f0:8", ["const:590450:8", "const:4:8"]]
+ 00590450 ["CALL", null, ["callee:00c57f40:8"]]
- 00590410 bytes cc1d1b94
+ 00590450 bytes bc1e1b94
- 00590454 ["INT_ADD", "register:40f0:8", ["const:590454:8", "const:4:8"]]
- 00590454 ["CALL", null, ["callee:00c57e90:8"]]
+ 00590494 ["INT_ADD", "register:40f0:8", ["const:590494:8", "const:4:8"]]
+ 00590494 ["CALL", null, ["callee:00c57e90:8"]]
- 00590454 bytes 8f1d1b94
+ 00590494 bytes 7f1e1b94
- 00590464 ["INT_ADD", "register:40f0:8", ["const:590464:8", "const:4:8"]]
- 00590464 ["CALL", null, ["callee:00590878:8"]]
+ 005904a4 ["INT_ADD", "register:40f0:8", ["const:5904a4:8", "const:4:8"]]
+ 005904a4 ["CALL", null, ["callee:00590878:8"]]
- 00590464 bytes f5000094
+ 005904a4 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4656a6273ce2a7b2e97363908e32b0d4"></a>

### [`00590838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590838.md) → [`00590878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590878.md) FUN_00590878

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00590378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590378.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`005903b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005903b8.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005908a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590838.md#insn-005908a0) · [`005908d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590838.md#insn-005908d8) · [`00590988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590838.md#insn-00590988)
- 新版 `005908e0`（命令位置の公開資料なし） · `00590918`（命令位置の公開資料なし） · `005909c8`（命令位置の公開資料なし）

~~~diff
- 005908a0 ["INT_ADD", "register:40f0:8", ["const:5908a0:8", "const:4:8"]]
- 005908a0 ["CALL", null, ["callee:00c57f40:8"]]
+ 005908e0 ["INT_ADD", "register:40f0:8", ["const:5908e0:8", "const:4:8"]]
+ 005908e0 ["CALL", null, ["callee:00c57f40:8"]]
- 005908a0 bytes a81c1b94
+ 005908e0 bytes 981d1b94
- 005908d8 ["INT_ADD", "register:40f0:8", ["const:5908d8:8", "const:4:8"]]
- 005908d8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00590918 ["INT_ADD", "register:40f0:8", ["const:590918:8", "const:4:8"]]
+ 00590918 ["CALL", null, ["callee:00c57e90:8"]]
- 005908d8 bytes 6e1c1b94
+ 00590918 bytes 5e1d1b94
- 00590988 ["INT_ADD", "register:40f0:8", ["const:590988:8", "const:4:8"]]
- 00590988 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005909c8 ["INT_ADD", "register:40f0:8", ["const:5909c8:8", "const:4:8"]]
+ 005909c8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00590988 bytes 4a1c1b94
+ 005909c8 bytes 3a1d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6432752d5937c5802cc036141bf599c"></a>

### [`005909c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/005909c0.md) → [`00590a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590a00.md) FUN_00590a00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00590378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590378.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`005903b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005903b8.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00590a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/005909c0.md#insn-00590a30) · [`00590a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/005909c0.md#insn-00590a68) · [`00590b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/005909c0.md#insn-00590b18)
- 新版 `00590a70`（命令位置の公開資料なし） · `00590aa8`（命令位置の公開資料なし） · `00590b58`（命令位置の公開資料なし）

~~~diff
- 00590a30 ["INT_ADD", "register:40f0:8", ["const:590a30:8", "const:4:8"]]
- 00590a30 ["CALL", null, ["callee:00c57f40:8"]]
+ 00590a70 ["INT_ADD", "register:40f0:8", ["const:590a70:8", "const:4:8"]]
+ 00590a70 ["CALL", null, ["callee:00c57f40:8"]]
- 00590a30 bytes 441c1b94
+ 00590a70 bytes 341d1b94
- 00590a68 ["INT_ADD", "register:40f0:8", ["const:590a68:8", "const:4:8"]]
- 00590a68 ["CALL", null, ["callee:00c57e90:8"]]
+ 00590aa8 ["INT_ADD", "register:40f0:8", ["const:590aa8:8", "const:4:8"]]
+ 00590aa8 ["CALL", null, ["callee:00c57e90:8"]]
- 00590a68 bytes 0a1c1b94
+ 00590aa8 bytes fa1c1b94
- 00590b18 ["INT_ADD", "register:40f0:8", ["const:590b18:8", "const:4:8"]]
- 00590b18 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00590b58 ["INT_ADD", "register:40f0:8", ["const:590b58:8", "const:4:8"]]
+ 00590b58 ["CALL", null, ["callee:00c57eb0:8"]]
- 00590b18 bytes e61b1b94
+ 00590b58 bytes d61c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-395c444e830cc57a4634ca7818feeee5"></a>

### [`00590b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590b4c.md) → [`00590b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590b8c.md) FUN_00590b8c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00590378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590378.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`005903b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005903b8.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00590bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590b4c.md#insn-00590bbc) · [`00590bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590b4c.md#insn-00590bf4) · [`00590ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590b4c.md#insn-00590ca4)
- 新版 `00590bfc`（命令位置の公開資料なし） · `00590c34`（命令位置の公開資料なし） · `00590ce4`（命令位置の公開資料なし）

~~~diff
- 00590bbc ["INT_ADD", "register:40f0:8", ["const:590bbc:8", "const:4:8"]]
- 00590bbc ["CALL", null, ["callee:00c57f40:8"]]
+ 00590bfc ["INT_ADD", "register:40f0:8", ["const:590bfc:8", "const:4:8"]]
+ 00590bfc ["CALL", null, ["callee:00c57f40:8"]]
- 00590bbc bytes e11b1b94
+ 00590bfc bytes d11c1b94
- 00590bf4 ["INT_ADD", "register:40f0:8", ["const:590bf4:8", "const:4:8"]]
- 00590bf4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00590c34 ["INT_ADD", "register:40f0:8", ["const:590c34:8", "const:4:8"]]
+ 00590c34 ["CALL", null, ["callee:00c57e90:8"]]
- 00590bf4 bytes a71b1b94
+ 00590c34 bytes 971c1b94
- 00590ca4 ["INT_ADD", "register:40f0:8", ["const:590ca4:8", "const:4:8"]]
- 00590ca4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00590ce4 ["INT_ADD", "register:40f0:8", ["const:590ce4:8", "const:4:8"]]
+ 00590ce4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00590ca4 bytes 831b1b94
+ 00590ce4 bytes 731c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-233f48deabf0b8daf5156d373775884e"></a>

### [`005911cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/005911cc.md) → [`0059120c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/0059120c.md) FUN_0059120c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005911e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/005911cc.md#insn-005911e8) · [`00591208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/005911cc.md#insn-00591208)
- 新版 `00591228`（命令位置の公開資料なし） · `00591248`（命令位置の公開資料なし）

~~~diff
- 005911e8 ["INT_ADD", "register:40f0:8", ["const:5911e8:8", "const:4:8"]]
- 005911e8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00591228 ["INT_ADD", "register:40f0:8", ["const:591228:8", "const:4:8"]]
+ 00591228 ["CALL", null, ["callee:00c53d00:8"]]
- 005911e8 bytes be091b94
+ 00591228 bytes b60a1b94
- 00591208 ["COPY", "register:0:8", ["register:4040:8"]]
- 00591208 ["INT_ADD", "register:40f0:8", ["const:591208:8", "const:4:8"]]
- 00591208 ["CALLIND", null, ["register:0:8"]]
+ 00591248 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00591248 ["INT_ADD", "register:40f0:8", ["const:591248:8", "const:4:8"]]
+ 00591248 ["CALLIND", null, ["register:0:8"]]
- 00591208 bytes 00013fd6
+ 00591248 bytes 00013fd6
~~~


<a id="compare-eea011b7bc61940ba7ed632d7edbece1"></a>

### [`0059121c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/0059121c.md) → [`0059125c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/0059125c.md) FUN_0059125c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00590d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590d78.md) · 呼出先 2件 [`00593c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593c64.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00590db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590db8.md) · 呼出先 2件 [`00593ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593ca4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00591248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/0059121c.md#insn-00591248) · [`00591274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/0059121c.md#insn-00591274)
- 新版 `00591288`（命令位置の公開資料なし） · `005912b4`（命令位置の公開資料なし）

~~~diff
- 00591248 ["INT_ADD", "register:40f0:8", ["const:591248:8", "const:4:8"]]
- 00591248 ["CALL", null, ["callee:00593ca4:8"]]
+ 00591288 ["INT_ADD", "register:40f0:8", ["const:591288:8", "const:4:8"]]
+ 00591288 ["CALL", null, ["callee:00593ca4:8"]]
- 00591248 bytes 870a0094
+ 00591288 bytes 870a0094
- 00591274 ["INT_ADD", "register:40f0:8", ["const:591274:8", "const:4:8"]]
- 00591274 ["CALL", null, ["callee:00c57ee0:8"]]
+ 005912b4 ["INT_ADD", "register:40f0:8", ["const:5912b4:8", "const:4:8"]]
+ 005912b4 ["CALL", null, ["callee:00c57ee0:8"]]
- 00591274 bytes 1b1a1b94
+ 005912b4 bytes 0b1b1b94
~~~


<a id="compare-00dd73bf16330bef8e0a087e5a33d60b"></a>

### [`0059168c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/0059168c.md) → [`005916cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005916cc.md) FUN_005916cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00592b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592b2c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00592b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592b6c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005916b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/0059168c.md#insn-005916b4) · [`005916e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/0059168c.md#insn-005916e0)
- 新版 `005916f4`（命令位置の公開資料なし） · `00591720`（命令位置の公開資料なし）

~~~diff
- 005916b4 ["INT_ADD", "register:40f0:8", ["const:5916b4:8", "const:4:8"]]
- 005916b4 ["CALL", null, ["callee:00592b6c:8"]]
+ 005916f4 ["INT_ADD", "register:40f0:8", ["const:5916f4:8", "const:4:8"]]
+ 005916f4 ["CALL", null, ["callee:00592b6c:8"]]
- 005916b4 bytes 1e050094
+ 005916f4 bytes 1e050094
- 005916e0 ["INT_ADD", "register:40f0:8", ["const:5916e0:8", "const:4:8"]]
- 005916e0 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00591720 ["INT_ADD", "register:40f0:8", ["const:591720:8", "const:4:8"]]
+ 00591720 ["CALL", null, ["callee:00c57ee0:8"]]
- 005916e0 bytes 00191b94
+ 00591720 bytes f0191b94
~~~


<a id="compare-2f222310df614cc47c589d35072cdf32"></a>

### [`00591790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591790.md) → [`005917d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005917d0.md) FUN_005917d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59fb0.md) [`00c5a010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a3b0.md) [`00c5a410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a410.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005917a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591790.md#insn-005917a4)
- 新版 `005917e4`（命令位置の公開資料なし）

~~~diff
- 005917a4 ["INT_ADD", "register:40f0:8", ["const:5917a4:8", "const:4:8"]]
- 005917a4 ["CALL", null, ["callee:00c5a3b0:8"]]
+ 005917e4 ["INT_ADD", "register:40f0:8", ["const:5917e4:8", "const:4:8"]]
+ 005917e4 ["CALL", null, ["callee:00c5a3b0:8"]]
- 005917a4 bytes 03221b94
+ 005917e4 bytes f3221b94
~~~


<a id="compare-09729417a6f309dbd8affd84c88c0063"></a>

### [`005917cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/005917cc.md) → [`0059180c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/0059180c.md) FUN_0059180c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c59fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59fb0.md) [`00c5a020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a020.md) [`00c5a050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a050.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5a3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a3b0.md) [`00c5a420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a420.md) [`00c5a450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005917e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/005917cc.md#insn-005917e4)
- 新版 `00591824`（命令位置の公開資料なし）

~~~diff
- 005917e4 ["INT_ADD", "register:40f0:8", ["const:5917e4:8", "const:4:8"]]
- 005917e4 ["CALL", null, ["callee:00c5a3b0:8"]]
+ 00591824 ["INT_ADD", "register:40f0:8", ["const:591824:8", "const:4:8"]]
+ 00591824 ["CALL", null, ["callee:00c5a3b0:8"]]
- 005917e4 bytes f3211b94
+ 00591824 bytes e3221b94
~~~


<a id="compare-730c434f713227aa2c69bcc97bf12664"></a>

### [`005918e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/005918e0.md) → [`00591920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591920.md) FUN_00591920

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ad0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59fb0.md) [`00c5a060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a060.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ed0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a3b0.md) [`00c5a460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a460.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00591918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/005918e0.md#insn-00591918) · [`00591924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/005918e0.md#insn-00591924) · [`00591940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/005918e0.md#insn-00591940)
- 新版 `00591958`（命令位置の公開資料なし） · `00591964`（命令位置の公開資料なし） · `00591980`（命令位置の公開資料なし）

~~~diff
- 00591918 ["INT_ADD", "register:40f0:8", ["const:591918:8", "const:4:8"]]
- 00591918 ["CALL", null, ["callee:00c5a3b0:8"]]
+ 00591958 ["INT_ADD", "register:40f0:8", ["const:591958:8", "const:4:8"]]
+ 00591958 ["CALL", null, ["callee:00c5a3b0:8"]]
- 00591918 bytes a6211b94
+ 00591958 bytes 96221b94
- 00591924 ["INT_ADD", "register:40f0:8", ["const:591924:8", "const:4:8"]]
- 00591924 ["CALL", null, ["callee:00c57ed0:8"]]
+ 00591964 ["INT_ADD", "register:40f0:8", ["const:591964:8", "const:4:8"]]
+ 00591964 ["CALL", null, ["callee:00c57ed0:8"]]
- 00591924 bytes 6b181b94
+ 00591964 bytes 5b191b94
- 00591940 ["INT_ADD", "register:40f0:8", ["const:591940:8", "const:4:8"]]
- 00591940 ["CALL", null, ["callee:00c5a460:8"]]
+ 00591980 ["INT_ADD", "register:40f0:8", ["const:591980:8", "const:4:8"]]
+ 00591980 ["CALL", null, ["callee:00c5a460:8"]]
- 00591940 bytes c8211b94
+ 00591980 bytes b8221b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3af7aa6562139d5e50df3bbd4d889f77"></a>

### [`00591a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591a7c.md) → [`00591abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591abc.md) FUN_00591abc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c59fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59fb0.md) [`00c5a080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a080.md) [`00c5a090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a090.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5a3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a3b0.md) [`00c5a480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a480.md) [`00c5a490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a490.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00591a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591a7c.md#insn-00591a94) · [`00591aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591a7c.md#insn-00591aa4)
- 新版 `00591ad4`（命令位置の公開資料なし） · `00591ae4`（命令位置の公開資料なし）

~~~diff
- 00591a94 ["INT_ADD", "register:40f0:8", ["const:591a94:8", "const:4:8"]]
- 00591a94 ["CALL", null, ["callee:00c5a3b0:8"]]
+ 00591ad4 ["INT_ADD", "register:40f0:8", ["const:591ad4:8", "const:4:8"]]
+ 00591ad4 ["CALL", null, ["callee:00c5a3b0:8"]]
- 00591a94 bytes 47211b94
+ 00591ad4 bytes 37221b94
- 00591aa4 ["INT_ADD", "register:40f0:8", ["const:591aa4:8", "const:4:8"]]
- 00591aa4 ["CALL", null, ["callee:00c5a480:8"]]
+ 00591ae4 ["INT_ADD", "register:40f0:8", ["const:591ae4:8", "const:4:8"]]
+ 00591ae4 ["CALL", null, ["callee:00c5a480:8"]]
- 00591aa4 bytes 77211b94
+ 00591ae4 bytes 67221b94
~~~


<a id="compare-eee7c80f4ec7caa38e45f7068e8e5f1c"></a>

### [`00591adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591adc.md) → [`00591b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591b1c.md) FUN_00591b1c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a0b0.md) [`00c5a0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a0c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a4b0.md) [`00c5a4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a4c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00591ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591adc.md#insn-00591ae4)
- 新版 `00591b24`（命令位置の公開資料なし）

~~~diff
- 00591ae4 ["INT_ADD", "register:40f0:8", ["const:591ae4:8", "const:4:8"]]
- 00591ae4 ["CALL", null, ["callee:00c5a4b0:8"]]
+ 00591b24 ["INT_ADD", "register:40f0:8", ["const:591b24:8", "const:4:8"]]
+ 00591b24 ["CALL", null, ["callee:00c5a4b0:8"]]
- 00591ae4 bytes 73211b94
+ 00591b24 bytes 63221b94
~~~


<a id="compare-b92dbc2c7770ac7a1cf62417bae553aa"></a>

### [`00591af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591af4.md) → [`00591b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591b34.md) FUN_00591b34

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`0058fb84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fb84.md) [`00c59f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f70.md) [`00c5a0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a0d0.md) [`00c5a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a0e0.md) [`00c5a0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0058fbc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fbc4.md) [`00c5a370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a370.md) [`00c5a4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a4d0.md) [`00c5a4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a4e0.md) [`00c5a4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a4f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00591b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591af4.md#insn-00591b1c) · [`00591b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591af4.md#insn-00591b20) · [`00591b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591af4.md#insn-00591b3c)
- 新版 `00591b5c`（命令位置の公開資料なし） · `00591b60`（命令位置の公開資料なし） · `00591b7c`（命令位置の公開資料なし）

~~~diff
- 00591b1c ["INT_ADD", "register:40f0:8", ["const:591b1c:8", "const:4:8"]]
- 00591b1c ["CALL", null, ["callee:00c5a370:8"]]
+ 00591b5c ["INT_ADD", "register:40f0:8", ["const:591b5c:8", "const:4:8"]]
+ 00591b5c ["CALL", null, ["callee:00c5a370:8"]]
- 00591b1c bytes 15211b94
+ 00591b5c bytes 05221b94
- 00591b20 ["INT_ADD", "register:40f0:8", ["const:591b20:8", "const:4:8"]]
- 00591b20 ["CALL", null, ["callee:0058fbc4:8"]]
+ 00591b60 ["INT_ADD", "register:40f0:8", ["const:591b60:8", "const:4:8"]]
+ 00591b60 ["CALL", null, ["callee:0058fbc4:8"]]
- 00591b20 bytes 19f8ff97
+ 00591b60 bytes 19f8ff97
- 00591b3c ["INT_ADD", "register:40f0:8", ["const:591b3c:8", "const:4:8"]]
- 00591b3c ["CALL", null, ["callee:00c5a4d0:8"]]
+ 00591b7c ["INT_ADD", "register:40f0:8", ["const:591b7c:8", "const:4:8"]]
+ 00591b7c ["CALL", null, ["callee:00c5a4d0:8"]]
- 00591b3c bytes 65211b94
+ 00591b7c bytes 55221b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-996a7db0461b2a8b4d8f7a0bdecfbd7d"></a>

### [`00592108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592108.md) → [`00592148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592148.md) FUN_00592148

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00592080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592080.md) · 呼出先 9件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ad0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005920c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005920c0.md) · 呼出先 9件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ed0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00592150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592108.md#insn-00592150) · [`0059215c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592108.md#insn-0059215c) · [`0059216c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592108.md#insn-0059216c)
- 新版 `00592190`（命令位置の公開資料なし） · `0059219c`（命令位置の公開資料なし） · `005921ac`（命令位置の公開資料なし）

~~~diff
- 00592150 ["INT_ADD", "register:40f0:8", ["const:592150:8", "const:4:8"]]
- 00592150 ["CALL", null, ["callee:00c57ed0:8"]]
+ 00592190 ["INT_ADD", "register:40f0:8", ["const:592190:8", "const:4:8"]]
+ 00592190 ["CALL", null, ["callee:00c57ed0:8"]]
- 00592150 bytes 60161b94
+ 00592190 bytes 50171b94
- 0059215c ["INT_ADD", "register:40f0:8", ["const:59215c:8", "const:4:8"]]
- 0059215c ["CALL", null, ["callee:00c5a520:8"]]
+ 0059219c ["INT_ADD", "register:40f0:8", ["const:59219c:8", "const:4:8"]]
+ 0059219c ["CALL", null, ["callee:00c5a520:8"]]
- 0059215c bytes f11f1b94
+ 0059219c bytes e1201b94
- 0059216c ["COPY", "register:0:8", ["register:4040:8"]]
- 0059216c ["INT_ADD", "register:40f0:8", ["const:59216c:8", "const:4:8"]]
- 0059216c ["CALLIND", null, ["register:0:8"]]
+ 005921ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 005921ac ["INT_ADD", "register:40f0:8", ["const:5921ac:8", "const:4:8"]]
+ 005921ac ["CALLIND", null, ["register:0:8"]]
- 0059216c bytes 00013fd6
+ 005921ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a47642f36176cf667e4addf616f4829a"></a>

### [`00592538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592538.md) → [`00592578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592578.md) FUN_00592578

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`00590d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590d78.md) [`00591748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591748.md) [`00591800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591800.md) [`00591848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591848.md) [`00591898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591898.md) · 呼出先 1件 [`00592538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592538.md)
- 新版 呼出元 7件 [`00590db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590db8.md) [`00591788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591788.md) [`00591840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591840.md) [`00591888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591888.md) [`005918d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005918d8.md) · 呼出先 1件 [`00592578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592578.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00592564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592538.md#insn-00592564)
- 新版 `005925a4`（命令位置の公開資料なし）

~~~diff
- 00592564 ["INT_ADD", "register:40f0:8", ["const:592564:8", "const:4:8"]]
- 00592564 ["CALL", null, ["local:b0:8"]]
+ 005925a4 ["INT_ADD", "register:40f0:8", ["const:5925a4:8", "const:4:8"]]
+ 005925a4 ["CALL", null, ["local:b0:8"]]
- 00592564 bytes f5ffff97
+ 005925a4 bytes f5ffff97
~~~


<a id="compare-9ba06f14be8643f9b3e6ca8174738cdc"></a>

### [`00592668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592668.md) → [`005926a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005926a8.md) FUN_005926a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00592678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592668.md#insn-00592678)
- 新版 `005926b8`（命令位置の公開資料なし）

~~~diff
- 00592678 ["INT_ADD", "register:40f0:8", ["const:592678:8", "const:4:8"]]
- 00592678 ["CALL", null, ["callee:00555288:8"]]
+ 005926b8 ["INT_ADD", "register:40f0:8", ["const:5926b8:8", "const:4:8"]]
+ 005926b8 ["CALL", null, ["callee:00555288:8"]]
- 00592678 bytes f40aff97
+ 005926b8 bytes f40aff97
~~~


<a id="compare-523a1d8b22e0d9bd9c8fc3fddbc0532e"></a>

### [`00592690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592690.md) → [`005926d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005926d0.md) FUN_005926d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ad0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f70.md) [`00c59f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ed0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a370.md) [`00c5a390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005926d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592690.md#insn-005926d4) · [`005926e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592690.md#insn-005926e0) · [`00592708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592690.md#insn-00592708)
- 新版 `00592714`（命令位置の公開資料なし） · `00592720`（命令位置の公開資料なし） · `00592748`（命令位置の公開資料なし）

~~~diff
- 005926d4 ["INT_ADD", "register:40f0:8", ["const:5926d4:8", "const:4:8"]]
- 005926d4 ["CALL", null, ["callee:00c57ed0:8"]]
+ 00592714 ["INT_ADD", "register:40f0:8", ["const:592714:8", "const:4:8"]]
+ 00592714 ["CALL", null, ["callee:00c57ed0:8"]]
- 005926d4 bytes ff141b94
+ 00592714 bytes ef151b94
- 005926e0 ["INT_ADD", "register:40f0:8", ["const:5926e0:8", "const:4:8"]]
- 005926e0 ["CALL", null, ["callee:00c5a370:8"]]
+ 00592720 ["INT_ADD", "register:40f0:8", ["const:592720:8", "const:4:8"]]
+ 00592720 ["CALL", null, ["callee:00c5a370:8"]]
- 005926e0 bytes 241e1b94
+ 00592720 bytes 141f1b94
- 00592708 ["INT_ADD", "register:40f0:8", ["const:592708:8", "const:4:8"]]
- 00592708 ["CALL", null, ["callee:00c5a390:8"]]
+ 00592748 ["INT_ADD", "register:40f0:8", ["const:592748:8", "const:4:8"]]
+ 00592748 ["CALL", null, ["callee:00c5a390:8"]]
- 00592708 bytes 221e1b94
+ 00592748 bytes 121f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a071c19c550b7ae262b30e56a881d6ac"></a>

### [`00592744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592744.md) → [`00592784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592784.md) FUN_00592784

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ad0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f70.md) [`00c59f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ed0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a370.md) [`00c5a380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00592774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592744.md#insn-00592774) · [`00592780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592744.md#insn-00592780) · [`00592790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592744.md#insn-00592790)
- 新版 `005927b4`（命令位置の公開資料なし） · `005927c0`（命令位置の公開資料なし） · `005927d0`（命令位置の公開資料なし）

~~~diff
- 00592774 ["INT_ADD", "register:40f0:8", ["const:592774:8", "const:4:8"]]
- 00592774 ["CALL", null, ["callee:00c57ed0:8"]]
+ 005927b4 ["INT_ADD", "register:40f0:8", ["const:5927b4:8", "const:4:8"]]
+ 005927b4 ["CALL", null, ["callee:00c57ed0:8"]]
- 00592774 bytes d7141b94
+ 005927b4 bytes c7151b94
- 00592780 ["INT_ADD", "register:40f0:8", ["const:592780:8", "const:4:8"]]
- 00592780 ["CALL", null, ["callee:00c5a370:8"]]
+ 005927c0 ["INT_ADD", "register:40f0:8", ["const:5927c0:8", "const:4:8"]]
+ 005927c0 ["CALL", null, ["callee:00c5a370:8"]]
- 00592780 bytes fc1d1b94
+ 005927c0 bytes ec1e1b94
- 00592790 ["INT_ADD", "register:40f0:8", ["const:592790:8", "const:4:8"]]
- 00592790 ["CALL", null, ["callee:00c5a380:8"]]
+ 005927d0 ["INT_ADD", "register:40f0:8", ["const:5927d0:8", "const:4:8"]]
+ 005927d0 ["CALL", null, ["callee:00c5a380:8"]]
- 00592790 bytes fc1d1b94
+ 005927d0 bytes ec1e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dcd3ca0a46e75d892443ccda940d546"></a>

### [`005928f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/005928f0.md) → [`00592930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592930.md) FUN_00592930

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00592900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/005928f0.md#insn-00592900)
- 新版 `00592940`（命令位置の公開資料なし）

~~~diff
- 00592900 ["INT_ADD", "register:40f0:8", ["const:592900:8", "const:4:8"]]
- 00592900 ["CALL", null, ["callee:00555288:8"]]
+ 00592940 ["INT_ADD", "register:40f0:8", ["const:592940:8", "const:4:8"]]
+ 00592940 ["CALL", null, ["callee:00555288:8"]]
- 00592900 bytes 520aff97
+ 00592940 bytes 520aff97
~~~


<a id="compare-6830ad5ed10e74dba7f0821e5ac0f4bf"></a>

### [`00592a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592a1c.md) → [`00592a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592a5c.md) FUN_00592a5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5a100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a100.md) [`00c5a180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a180.md) [`00c5a190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a190.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5a500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a500.md) [`00c5a580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a580.md) [`00c5a590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a590.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00592a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592a1c.md#insn-00592a48) · [`00592a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592a1c.md#insn-00592a60) · [`00592a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592a1c.md#insn-00592a74)
- 新版 `00592a88`（命令位置の公開資料なし） · `00592aa0`（命令位置の公開資料なし） · `00592ab4`（命令位置の公開資料なし）

~~~diff
- 00592a48 ["INT_ADD", "register:40f0:8", ["const:592a48:8", "const:4:8"]]
- 00592a48 ["CALL", null, ["callee:00c5a500:8"]]
+ 00592a88 ["INT_ADD", "register:40f0:8", ["const:592a88:8", "const:4:8"]]
+ 00592a88 ["CALL", null, ["callee:00c5a500:8"]]
- 00592a48 bytes ae1d1b94
+ 00592a88 bytes 9e1e1b94
- 00592a60 ["INT_ADD", "register:40f0:8", ["const:592a60:8", "const:4:8"]]
- 00592a60 ["CALL", null, ["callee:00c5a580:8"]]
+ 00592aa0 ["INT_ADD", "register:40f0:8", ["const:592aa0:8", "const:4:8"]]
+ 00592aa0 ["CALL", null, ["callee:00c5a580:8"]]
- 00592a60 bytes c81d1b94
+ 00592aa0 bytes b81e1b94
- 00592a74 ["INT_ADD", "register:40f0:8", ["const:592a74:8", "const:4:8"]]
- 00592a74 ["CALL", null, ["callee:00c5a590:8"]]
+ 00592ab4 ["INT_ADD", "register:40f0:8", ["const:592ab4:8", "const:4:8"]]
+ 00592ab4 ["CALL", null, ["callee:00c5a590:8"]]
- 00592a74 bytes c71d1b94
+ 00592ab4 bytes b71e1b94
~~~


<a id="compare-25ac0121197fd9df0d63659180327f0c"></a>

### [`00592a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592a90.md) → [`00592ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592ad0.md) FUN_00592ad0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a100.md) [`00c5a1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a1a0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a500.md) [`00c5a5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a5a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00592ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592a90.md#insn-00592ab8) · [`00592ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592a90.md#insn-00592ac8) · [`00592ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592a90.md#insn-00592ad4)
- 新版 `00592af8`（命令位置の公開資料なし） · `00592b08`（命令位置の公開資料なし） · `00592b14`（命令位置の公開資料なし）

~~~diff
- 00592ab8 ["INT_ADD", "register:40f0:8", ["const:592ab8:8", "const:4:8"]]
- 00592ab8 ["CALL", null, ["callee:00c5a500:8"]]
+ 00592af8 ["INT_ADD", "register:40f0:8", ["const:592af8:8", "const:4:8"]]
+ 00592af8 ["CALL", null, ["callee:00c5a500:8"]]
- 00592ab8 bytes 921d1b94
+ 00592af8 bytes 821e1b94
- 00592ac8 ["INT_ADD", "register:40f0:8", ["const:592ac8:8", "const:4:8"]]
- 00592ac8 ["CALL", null, ["callee:00c5a5a0:8"]]
+ 00592b08 ["INT_ADD", "register:40f0:8", ["const:592b08:8", "const:4:8"]]
+ 00592b08 ["CALL", null, ["callee:00c5a5a0:8"]]
- 00592ac8 bytes b61d1b94
+ 00592b08 bytes a61e1b94
- 00592ad4 ["INT_ADD", "register:40f0:8", ["const:592ad4:8", "const:4:8"]]
- 00592ad4 ["CALL", null, ["callee:00c5a500:8"]]
+ 00592b14 ["INT_ADD", "register:40f0:8", ["const:592b14:8", "const:4:8"]]
+ 00592b14 ["CALL", null, ["callee:00c5a500:8"]]
- 00592ad4 bytes 8b1d1b94
+ 00592b14 bytes 7b1e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33d20dcec3f08fafdd3f1f6de4e83185"></a>

### [`00592b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592b00.md) → [`00592b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592b40.md) FUN_00592b40

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00592b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592b00.md#insn-00592b10)
- 新版 `00592b50`（命令位置の公開資料なし）

~~~diff
- 00592b10 ["INT_ADD", "register:40f0:8", ["const:592b10:8", "const:4:8"]]
- 00592b10 ["CALL", null, ["callee:00555288:8"]]
+ 00592b50 ["INT_ADD", "register:40f0:8", ["const:592b50:8", "const:4:8"]]
+ 00592b50 ["CALL", null, ["callee:00555288:8"]]
- 00592b10 bytes ce09ff97
+ 00592b50 bytes ce09ff97
~~~


<a id="compare-05388134e252e405f6d1b95dc2d2108e"></a>

### [`00592c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592c24.md) → [`00592c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592c64.md) FUN_00592c64

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00592c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592c24.md#insn-00592c40) · [`00592c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592c24.md#insn-00592c60)
- 新版 `00592c80`（命令位置の公開資料なし） · `00592ca0`（命令位置の公開資料なし）

~~~diff
- 00592c40 ["INT_ADD", "register:40f0:8", ["const:592c40:8", "const:4:8"]]
- 00592c40 ["CALL", null, ["callee:00c53d00:8"]]
+ 00592c80 ["INT_ADD", "register:40f0:8", ["const:592c80:8", "const:4:8"]]
+ 00592c80 ["CALL", null, ["callee:00c53d00:8"]]
- 00592c40 bytes 28031b94
+ 00592c80 bytes 20041b94
- 00592c60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00592c60 ["INT_ADD", "register:40f0:8", ["const:592c60:8", "const:4:8"]]
- 00592c60 ["CALLIND", null, ["register:0:8"]]
+ 00592ca0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00592ca0 ["INT_ADD", "register:40f0:8", ["const:592ca0:8", "const:4:8"]]
+ 00592ca0 ["CALLIND", null, ["register:0:8"]]
- 00592c60 bytes 00013fd6
+ 00592ca0 bytes 00013fd6
~~~


<a id="compare-e4dc4204fc2a1140a513bd5454477f13"></a>

### [`00593a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593a68.md) → [`00593aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593aa8.md) FUN_00593aa8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a070.md) [`00c5a250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a250.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a470.md) [`00c5a650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00593acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593a68.md#insn-00593acc)
- 新版 `00593b0c`（命令位置の公開資料なし）

~~~diff
- 00593acc ["INT_ADD", "register:40f0:8", ["const:593acc:8", "const:4:8"]]
- 00593acc ["CALL", null, ["callee:00c5a470:8"]]
+ 00593b0c ["INT_ADD", "register:40f0:8", ["const:593b0c:8", "const:4:8"]]
+ 00593b0c ["CALL", null, ["callee:00c5a470:8"]]
- 00593acc bytes 69191b94
+ 00593b0c bytes 591a1b94
~~~


<a id="compare-567d73ac3d9ce5062a08ed2490558e15"></a>

### [`00593ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593ae8.md) → [`00593b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593b28.md) FUN_00593b28

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a070.md) [`00c5a260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a260.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a470.md) [`00c5a660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a660.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00593b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593ae8.md#insn-00593b50)
- 新版 `00593b90`（命令位置の公開資料なし）

~~~diff
- 00593b50 ["INT_ADD", "register:40f0:8", ["const:593b50:8", "const:4:8"]]
- 00593b50 ["CALL", null, ["callee:00c5a470:8"]]
+ 00593b90 ["INT_ADD", "register:40f0:8", ["const:593b90:8", "const:4:8"]]
+ 00593b90 ["CALL", null, ["callee:00c5a470:8"]]
- 00593b50 bytes 48191b94
+ 00593b90 bytes 381a1b94
~~~


<a id="compare-3b2f4d29c71d86d57cb5e6866d0bf84b"></a>

### [`00593b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593b70.md) → [`00593bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593bb0.md) FUN_00593bb0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a070.md) [`00c5a270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a270.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a470.md) [`00c5a670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a670.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00593bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593b70.md#insn-00593bcc)
- 新版 `00593c0c`（命令位置の公開資料なし）

~~~diff
- 00593bcc ["INT_ADD", "register:40f0:8", ["const:593bcc:8", "const:4:8"]]
- 00593bcc ["CALL", null, ["callee:00c5a470:8"]]
+ 00593c0c ["INT_ADD", "register:40f0:8", ["const:593c0c:8", "const:4:8"]]
+ 00593c0c ["CALL", null, ["callee:00c5a470:8"]]
- 00593bcc bytes 29191b94
+ 00593c0c bytes 191a1b94
~~~


<a id="compare-fa8f63128be4bbd33d57dd26f2ba5478"></a>

### [`00593be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593be8.md) → [`00593c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593c28.md) FUN_00593c28

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a070.md) [`00c5a280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a280.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a470.md) [`00c5a680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00593c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593be8.md#insn-00593c44)
- 新版 `00593c84`（命令位置の公開資料なし）

~~~diff
- 00593c44 ["INT_ADD", "register:40f0:8", ["const:593c44:8", "const:4:8"]]
- 00593c44 ["CALL", null, ["callee:00c5a470:8"]]
+ 00593c84 ["INT_ADD", "register:40f0:8", ["const:593c84:8", "const:4:8"]]
+ 00593c84 ["CALL", null, ["callee:00c5a470:8"]]
- 00593c44 bytes 0b191b94
+ 00593c84 bytes fb191b94
~~~


<a id="compare-676f3d7c260f3f7f759ecc41bdffb57f"></a>

### [`00594300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594300.md) → [`00594340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594340.md) FUN_00594340

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00594300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594300.md) [`005948a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/005948a0.md) · 呼出先 2件 [`00594300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594300.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00594340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594340.md) [`005948e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005948e0.md) · 呼出先 2件 [`00594340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594340.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00594320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594300.md#insn-00594320) · [`0059432c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594300.md#insn-0059432c)
- 新版 `00594360`（命令位置の公開資料なし） · `0059436c`（命令位置の公開資料なし）

~~~diff
- 00594320 ["INT_ADD", "register:40f0:8", ["const:594320:8", "const:4:8"]]
- 00594320 ["CALL", null, ["local:b0:8"]]
+ 00594360 ["INT_ADD", "register:40f0:8", ["const:594360:8", "const:4:8"]]
+ 00594360 ["CALL", null, ["local:b0:8"]]
- 00594320 bytes f8ffff97
+ 00594360 bytes f8ffff97
- 0059432c ["INT_ADD", "register:40f0:8", ["const:59432c:8", "const:4:8"]]
- 0059432c ["CALL", null, ["local:b0:8"]]
+ 0059436c ["INT_ADD", "register:40f0:8", ["const:59436c:8", "const:4:8"]]
+ 0059436c ["CALL", null, ["local:b0:8"]]
- 0059432c bytes f5ffff97
+ 0059436c bytes f5ffff97
~~~


<a id="compare-279c7ec1170cf26c43fa21b0bf0d93cd"></a>

### [`00594344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594344.md) → [`00594384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594384.md) FUN_00594384

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00593340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593340.md) [`00b075a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b07/00b075a0.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00594470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594470.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`00593380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593380.md) [`00b079c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b079c8.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005944b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005944b0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059437c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594344.md#insn-0059437c) · [`0059439c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594344.md#insn-0059439c) · [`005943d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594344.md#insn-005943d0)
- 新版 `005943bc`（命令位置の公開資料なし） · `005943dc`（命令位置の公開資料なし） · `00594410`（命令位置の公開資料なし）

~~~diff
- 0059437c ["INT_ADD", "register:40f0:8", ["const:59437c:8", "const:4:8"]]
- 0059437c ["CALL", null, ["callee:005944b0:8"]]
+ 005943bc ["INT_ADD", "register:40f0:8", ["const:5943bc:8", "const:4:8"]]
+ 005943bc ["CALL", null, ["callee:005944b0:8"]]
- 0059437c bytes 3d000094
+ 005943bc bytes 3d000094
- 0059439c ["INT_ADD", "register:40f0:8", ["const:59439c:8", "const:4:8"]]
- 0059439c ["CALL", null, ["callee:00c57e90:8"]]
+ 005943dc ["INT_ADD", "register:40f0:8", ["const:5943dc:8", "const:4:8"]]
+ 005943dc ["CALL", null, ["callee:00c57e90:8"]]
- 0059439c bytes bd0d1b94
+ 005943dc bytes ad0e1b94
- 005943d0 ["INT_ADD", "register:40f0:8", ["const:5943d0:8", "const:4:8"]]
- 005943d0 ["CALL", null, ["callee:0043bb20:8"]]
+ 00594410 ["INT_ADD", "register:40f0:8", ["const:594410:8", "const:4:8"]]
+ 00594410 ["CALL", null, ["callee:0043bb20:8"]]
- 005943d0 bytes c49dfa97
+ 00594410 bytes c49dfa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d36856ef035569ca0c8a3d7e8258c900"></a>

### [`00594470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594470.md) → [`005944b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005944b0.md) FUN_005944b0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00594344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594344.md) · 呼出先 2件 [`0044ac8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044ac8c.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00594384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594384.md) · 呼出先 2件 [`0044accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044a/0044accc.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005944f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594470.md#insn-005944f8) · [`0059454c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594470.md#insn-0059454c) · [`005945e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594470.md#insn-005945e8)
- 新版 `00594538`（命令位置の公開資料なし） · `0059458c`（命令位置の公開資料なし） · `00594628`（命令位置の公開資料なし）

~~~diff
- 005944f8 ["INT_ADD", "register:40f0:8", ["const:5944f8:8", "const:4:8"]]
- 005944f8 ["CALL", null, ["callee:00c58050:8"]]
+ 00594538 ["INT_ADD", "register:40f0:8", ["const:594538:8", "const:4:8"]]
+ 00594538 ["CALL", null, ["callee:00c58050:8"]]
- 005944f8 bytes d60d1b94
+ 00594538 bytes c60e1b94
- 0059454c ["INT_ADD", "register:40f0:8", ["const:59454c:8", "const:4:8"]]
- 0059454c ["CALL", null, ["callee:00c58050:8"]]
+ 0059458c ["INT_ADD", "register:40f0:8", ["const:59458c:8", "const:4:8"]]
+ 0059458c ["CALL", null, ["callee:00c58050:8"]]
- 0059454c bytes c10d1b94
+ 0059458c bytes b10e1b94
- 005945e8 ["INT_ADD", "register:40f0:8", ["const:5945e8:8", "const:4:8"]]
- 005945e8 ["CALL", null, ["callee:00c58050:8"]]
+ 00594628 ["INT_ADD", "register:40f0:8", ["const:594628:8", "const:4:8"]]
+ 00594628 ["CALL", null, ["callee:00c58050:8"]]
- 005945e8 bytes 9a0d1b94
+ 00594628 bytes 8a0e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60f3500602e7b49aace90908f33fe87d"></a>

### [`0059470c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/0059470c.md) → [`0059474c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/0059474c.md) FUN_0059474c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00594744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/0059470c.md#insn-00594744)
- 新版 `00594784`（命令位置の公開資料なし）

~~~diff
- 00594744 ["INT_ADD", "register:40f0:8", ["const:594744:8", "const:4:8"]]
- 00594744 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00594784 ["INT_ADD", "register:40f0:8", ["const:594784:8", "const:4:8"]]
+ 00594784 ["CALL", null, ["callee:00c57eb0:8"]]
- 00594744 bytes db0c1b94
+ 00594784 bytes cb0d1b94
~~~


<a id="compare-813985abad5bf91aadf9e854ad347151"></a>

### [`0059475c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/0059475c.md) → [`0059479c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/0059479c.md) FUN_0059479c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00593340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593340.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00593380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593380.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005947c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/0059475c.md#insn-005947c8) · [`00594824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/0059475c.md#insn-00594824)
- 新版 `00594808`（命令位置の公開資料なし） · `00594864`（命令位置の公開資料なし）

~~~diff
- 005947c8 ["INT_ADD", "register:40f0:8", ["const:5947c8:8", "const:4:8"]]
- 005947c8 ["CALL", null, ["callee:00c58050:8"]]
+ 00594808 ["INT_ADD", "register:40f0:8", ["const:594808:8", "const:4:8"]]
+ 00594808 ["CALL", null, ["callee:00c58050:8"]]
- 005947c8 bytes 220d1b94
+ 00594808 bytes 120e1b94
- 00594824 ["INT_ADD", "register:40f0:8", ["const:594824:8", "const:4:8"]]
- 00594824 ["CALL", null, ["callee:00c58050:8"]]
+ 00594864 ["INT_ADD", "register:40f0:8", ["const:594864:8", "const:4:8"]]
+ 00594864 ["CALL", null, ["callee:00c58050:8"]]
- 00594824 bytes 0b0d1b94
+ 00594864 bytes fb0d1b94
~~~


<a id="compare-3f6f5666bbd1316ba02bec9755e3656c"></a>

### [`00594fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594fe8.md) → [`00595028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595028.md) FUN_00595028

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00588cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588cac.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00588cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588cec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059501c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594fe8.md#insn-0059501c) · [`00595050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594fe8.md#insn-00595050)
- 新版 `0059505c`（命令位置の公開資料なし） · `00595090`（命令位置の公開資料なし）

~~~diff
- 0059501c ["COPY", "register:0:8", ["register:4048:8"]]
- 0059501c ["INT_ADD", "register:40f0:8", ["const:59501c:8", "const:4:8"]]
- 0059501c ["CALLIND", null, ["register:0:8"]]
+ 0059505c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0059505c ["INT_ADD", "register:40f0:8", ["const:59505c:8", "const:4:8"]]
+ 0059505c ["CALLIND", null, ["register:0:8"]]
- 0059501c bytes 20013fd6
+ 0059505c bytes 20013fd6
- 00595050 ["INT_ADD", "register:40f0:8", ["const:595050:8", "const:4:8"]]
- 00595050 ["CALL", null, ["callee:00588cec:8"]]
+ 00595090 ["INT_ADD", "register:40f0:8", ["const:595090:8", "const:4:8"]]
+ 00595090 ["CALL", null, ["callee:00588cec:8"]]
- 00595050 bytes 17cfff97
+ 00595090 bytes 17cfff97
~~~


<a id="compare-8f7ae62a8470f812b3695e47c6476008"></a>

### [`00595150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595150.md) → [`00595190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595190.md) FUN_00595190

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00594b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594b2c.md) · 呼出先 2件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f500.md)
- 新版 呼出元 1件 [`00594b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594b6c.md) · 呼出先 2件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f540.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00595168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595150.md#insn-00595168)
- 新版 `005951a8`（命令位置の公開資料なし）

~~~diff
- 00595168 ["INT_ADD", "register:40f0:8", ["const:595168:8", "const:4:8"]]
- 00595168 ["CALL", null, ["callee:0055f4c4:8"]]
+ 005951a8 ["INT_ADD", "register:40f0:8", ["const:5951a8:8", "const:4:8"]]
+ 005951a8 ["CALL", null, ["callee:0055f4c4:8"]]
- 00595168 bytes c728ff97
+ 005951a8 bytes c728ff97
~~~


<a id="compare-f2de571fc5ff414453a81ee797b713c6"></a>

### [`00595190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595190.md) → [`005951d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005951d0.md) FUN_005951d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00594b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594b2c.md) · 呼出先 2件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f528.md)
- 新版 呼出元 1件 [`00594b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594b6c.md) · 呼出先 2件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f568.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005951a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595190.md#insn-005951a8)
- 新版 `005951e8`（命令位置の公開資料なし）

~~~diff
- 005951a8 ["INT_ADD", "register:40f0:8", ["const:5951a8:8", "const:4:8"]]
- 005951a8 ["CALL", null, ["callee:0055f4c4:8"]]
+ 005951e8 ["INT_ADD", "register:40f0:8", ["const:5951e8:8", "const:4:8"]]
+ 005951e8 ["CALL", null, ["callee:0055f4c4:8"]]
- 005951a8 bytes b728ff97
+ 005951e8 bytes b728ff97
~~~


<a id="compare-cc72a0b7d498a758d579a502f7fdd50a"></a>

### [`00596194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596194.md) → [`005961d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005961d4.md) FUN_005961d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00595cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md) · 呼出先 2件 [`005971f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005971f0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00595d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md) · 呼出先 2件 [`00597230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597230.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00596210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596194.md#insn-00596210) · [`0059626c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596194.md#insn-0059626c) · [`005962a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596194.md#insn-005962a8)
- 新版 `00596250`（命令位置の公開資料なし） · `005962ac`（命令位置の公開資料なし） · `005962e8`（命令位置の公開資料なし）

~~~diff
- 00596210 ["INT_ADD", "register:40f0:8", ["const:596210:8", "const:4:8"]]
- 00596210 ["CALL", null, ["callee:00c58050:8"]]
+ 00596250 ["INT_ADD", "register:40f0:8", ["const:596250:8", "const:4:8"]]
+ 00596250 ["CALL", null, ["callee:00c58050:8"]]
- 00596210 bytes 90061b94
+ 00596250 bytes 80071b94
- 0059626c ["INT_ADD", "register:40f0:8", ["const:59626c:8", "const:4:8"]]
- 0059626c ["CALL", null, ["callee:00c58050:8"]]
+ 005962ac ["INT_ADD", "register:40f0:8", ["const:5962ac:8", "const:4:8"]]
+ 005962ac ["CALL", null, ["callee:00c58050:8"]]
- 0059626c bytes 79061b94
+ 005962ac bytes 69071b94
- 005962a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005962a8 ["INT_ADD", "register:40f0:8", ["const:5962a8:8", "const:4:8"]]
- 005962a8 ["CALLIND", null, ["register:0:8"]]
+ 005962e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005962e8 ["INT_ADD", "register:40f0:8", ["const:5962e8:8", "const:4:8"]]
+ 005962e8 ["CALLIND", null, ["register:0:8"]]
- 005962a8 bytes 00013fd6
+ 005962e8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68d8a7861a792730e5adc959a234715f"></a>

### [`005962fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005962fc.md) → [`0059633c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/0059633c.md) FUN_0059633c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00595cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md) · 呼出先 2件 [`0059732c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059732c.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00595d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md) · 呼出先 2件 [`0059736c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059736c.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00596378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005962fc.md#insn-00596378) · [`005963d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005962fc.md#insn-005963d4) · [`00596410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005962fc.md#insn-00596410)
- 新版 `005963b8`（命令位置の公開資料なし） · `00596414`（命令位置の公開資料なし） · `00596450`（命令位置の公開資料なし）

~~~diff
- 00596378 ["INT_ADD", "register:40f0:8", ["const:596378:8", "const:4:8"]]
- 00596378 ["CALL", null, ["callee:00c58050:8"]]
+ 005963b8 ["INT_ADD", "register:40f0:8", ["const:5963b8:8", "const:4:8"]]
+ 005963b8 ["CALL", null, ["callee:00c58050:8"]]
- 00596378 bytes 36061b94
+ 005963b8 bytes 26071b94
- 005963d4 ["INT_ADD", "register:40f0:8", ["const:5963d4:8", "const:4:8"]]
- 005963d4 ["CALL", null, ["callee:00c58050:8"]]
+ 00596414 ["INT_ADD", "register:40f0:8", ["const:596414:8", "const:4:8"]]
+ 00596414 ["CALL", null, ["callee:00c58050:8"]]
- 005963d4 bytes 1f061b94
+ 00596414 bytes 0f071b94
- 00596410 ["COPY", "register:0:8", ["register:4040:8"]]
- 00596410 ["INT_ADD", "register:40f0:8", ["const:596410:8", "const:4:8"]]
- 00596410 ["CALLIND", null, ["register:0:8"]]
+ 00596450 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00596450 ["INT_ADD", "register:40f0:8", ["const:596450:8", "const:4:8"]]
+ 00596450 ["CALLIND", null, ["register:0:8"]]
- 00596410 bytes 00013fd6
+ 00596450 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51820b836ad52967b9960d2105b7963d"></a>

### [`00596ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596ddc.md) → [`00596e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596e1c.md) FUN_00596e1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00596fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596fdc.md) · 呼出先 5件 [`00550b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550b64.md) [`00596cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596cd0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0059701c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059701c.md) · 呼出先 5件 [`00550ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550ba4.md) [`00596d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00596e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596ddc.md#insn-00596e04) · [`00596e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596ddc.md#insn-00596e1c) · [`00596e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596ddc.md#insn-00596e28)
- 新版 `00596e44`（命令位置の公開資料なし） · `00596e5c`（命令位置の公開資料なし） · `00596e68`（命令位置の公開資料なし）

~~~diff
- 00596e04 ["INT_ADD", "register:40f0:8", ["const:596e04:8", "const:4:8"]]
- 00596e04 ["CALL", null, ["callee:00550ba4:8"]]
+ 00596e44 ["INT_ADD", "register:40f0:8", ["const:596e44:8", "const:4:8"]]
+ 00596e44 ["CALL", null, ["callee:00550ba4:8"]]
- 00596e04 bytes 58e7fe97
+ 00596e44 bytes 58e7fe97
- 00596e1c ["COPY", "register:0:8", ["register:4048:8"]]
- 00596e1c ["INT_ADD", "register:40f0:8", ["const:596e1c:8", "const:4:8"]]
- 00596e1c ["CALLIND", null, ["register:0:8"]]
+ 00596e5c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00596e5c ["INT_ADD", "register:40f0:8", ["const:596e5c:8", "const:4:8"]]
+ 00596e5c ["CALLIND", null, ["register:0:8"]]
- 00596e1c bytes 20013fd6
+ 00596e5c bytes 20013fd6
- 00596e28 ["INT_ADD", "register:40f0:8", ["const:596e28:8", "const:4:8"]]
- 00596e28 ["CALL", null, ["callee:00596d10:8"]]
+ 00596e68 ["INT_ADD", "register:40f0:8", ["const:596e68:8", "const:4:8"]]
+ 00596e68 ["CALL", null, ["callee:00596d10:8"]]
- 00596e28 bytes aaffff97
+ 00596e68 bytes aaffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-977ae4541ceddfc618416a198925b61c"></a>

### [`005971f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005971f0.md) → [`00597230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597230.md) FUN_00597230

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00596194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596194.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00458f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/00458f8c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005961d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005961d4.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00458fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458fcc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00597230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005971f0.md#insn-00597230) · [`00597250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005971f0.md#insn-00597250) · [`00597284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005971f0.md#insn-00597284)
- 新版 `00597270`（命令位置の公開資料なし） · `00597290`（命令位置の公開資料なし） · `005972c4`（命令位置の公開資料なし）

~~~diff
- 00597230 ["INT_ADD", "register:40f0:8", ["const:597230:8", "const:4:8"]]
- 00597230 ["CALL", null, ["callee:00458fcc:8"]]
+ 00597270 ["INT_ADD", "register:40f0:8", ["const:597270:8", "const:4:8"]]
+ 00597270 ["CALL", null, ["callee:00458fcc:8"]]
- 00597230 bytes 5707fb97
+ 00597270 bytes 5707fb97
- 00597250 ["INT_ADD", "register:40f0:8", ["const:597250:8", "const:4:8"]]
- 00597250 ["CALL", null, ["callee:00c57e90:8"]]
+ 00597290 ["INT_ADD", "register:40f0:8", ["const:597290:8", "const:4:8"]]
+ 00597290 ["CALL", null, ["callee:00c57e90:8"]]
- 00597250 bytes 10021b94
+ 00597290 bytes 00031b94
- 00597284 ["INT_ADD", "register:40f0:8", ["const:597284:8", "const:4:8"]]
- 00597284 ["CALL", null, ["callee:0043bb20:8"]]
+ 005972c4 ["INT_ADD", "register:40f0:8", ["const:5972c4:8", "const:4:8"]]
+ 005972c4 ["CALL", null, ["callee:0043bb20:8"]]
- 00597284 bytes 1792fa97
+ 005972c4 bytes 1792fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fc6f312a72ac45b996eb7d385ff9fb4"></a>

### [`0059732c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059732c.md) → [`0059736c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059736c.md) FUN_0059736c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005962fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005962fc.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00458f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/00458f8c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0059633c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/0059633c.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00458fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458fcc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059736c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059732c.md#insn-0059736c) · [`0059738c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059732c.md#insn-0059738c) · [`005973c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059732c.md#insn-005973c0)
- 新版 `005973ac`（命令位置の公開資料なし） · `005973cc`（命令位置の公開資料なし） · `00597400`（命令位置の公開資料なし）

~~~diff
- 0059736c ["INT_ADD", "register:40f0:8", ["const:59736c:8", "const:4:8"]]
- 0059736c ["CALL", null, ["callee:00458fcc:8"]]
+ 005973ac ["INT_ADD", "register:40f0:8", ["const:5973ac:8", "const:4:8"]]
+ 005973ac ["CALL", null, ["callee:00458fcc:8"]]
- 0059736c bytes 0807fb97
+ 005973ac bytes 0807fb97
- 0059738c ["INT_ADD", "register:40f0:8", ["const:59738c:8", "const:4:8"]]
- 0059738c ["CALL", null, ["callee:00c57e90:8"]]
+ 005973cc ["INT_ADD", "register:40f0:8", ["const:5973cc:8", "const:4:8"]]
+ 005973cc ["CALL", null, ["callee:00c57e90:8"]]
- 0059738c bytes c1011b94
+ 005973cc bytes b1021b94
- 005973c0 ["INT_ADD", "register:40f0:8", ["const:5973c0:8", "const:4:8"]]
- 005973c0 ["CALL", null, ["callee:0043bb20:8"]]
+ 00597400 ["INT_ADD", "register:40f0:8", ["const:597400:8", "const:4:8"]]
+ 00597400 ["CALL", null, ["callee:0043bb20:8"]]
- 005973c0 bytes c891fa97
+ 00597400 bytes c891fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

